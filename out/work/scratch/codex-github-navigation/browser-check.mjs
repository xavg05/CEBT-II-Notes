import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {chromium} from './tools/node_modules/playwright/index.mjs';
const manifest=JSON.parse(fs.readFileSync(new URL('./manifest.json',import.meta.url)));
const pages=manifest.subjects.flatMap(s=>s.pages);
const mode=process.argv[2]??'local';
const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,timeout:20000});
const context=await browser.newContext({viewport:{width:1440,height:1050}});
const results=[];
try{
  if(mode==='local'){
    const selections=[pages[0],...manifest.subjects.map(s=>[...s.pages].sort((a,b)=>b.cost-a.cost)[0]),pages.find(p=>p.path.includes('gene-regulation')&&p.part===3)];
    for(const item of [...new Map(selections.map(p=>[p.path,p])).values()]){
      const page=await context.newPage();
      const html=new URL('./'+item.path.replaceAll('/','__')+'.html',import.meta.url);
      await page.goto(html.href,{waitUntil:'load'});await page.evaluate(()=>document.fonts.ready);
      const rendered=await page.locator('.katex').count();
      const missingImages=await page.locator('img').evaluateAll(nodes=>nodes.filter(n=>!n.complete||!n.naturalWidth).map(n=>n.src));
      const failures=[];if(rendered!==item.expressions)failures.push('Expression count');if(missingImages.length)failures.push('Missing images');
      await page.screenshot({path:new URL('./local-'+path.basename(item.path)+'.png',import.meta.url).pathname,fullPage:false});
      results.push({file:item.path,rendered,missingImages,failures});await page.close();
    }
  }else{
    let cursor=0;
    async function worker(){
      const page=await context.newPage();
      while(cursor<pages.length){
        const item=pages[cursor++];let result;
        for(let attempt=0;attempt<3;attempt++){
          const url='https://github.com/xavg05/CEBT-II-Notes/blob/main/'+item.path.split('/').map(encodeURIComponent).join('/');
          try{
            const response=await page.goto(url,{waitUntil:'domcontentloaded',timeout:45000});
            if(response.status()!==200)throw new Error('HTTP '+response.status());
            await page.waitForFunction(()=>document.querySelector('article')!==null,{timeout:15000});
            await page.waitForFunction(expected=>document.querySelectorAll('article math-renderer math').length>=expected,item.expressions,{timeout:12000}).catch(()=>{});
            result=await page.locator('article').evaluate((article,expected)=>{
              const nodes=[...article.querySelectorAll('math-renderer')];
              const errors=nodes.filter(n=>!n.querySelector('math')||n.querySelector('merror')||n.getAttribute('data-error')).map(n=>n.outerHTML.slice(0,350));
              const invisible=nodes.filter(n=>{const m=n.querySelector('math');if(!m)return false;const r=m.getBoundingClientRect();return !r.width||!r.height;}).length;
              const failures=[];
              if(nodes.length!==expected.expressions)failures.push(`Expected ${expected.expressions} math nodes, got ${nodes.length}`);
              if(errors.length)failures.push('MathML errors or missing MathML');
              if(invisible)failures.push(`${invisible} invisible math nodes`);
              const renderedTags=nodes.map(n=>n.textContent.replace(/\s/g,'')).filter(x=>/\(\d+\)$/.test(x)).map(x=>Number(x.match(/\((\d+)\)$/)[1]));
              // Native MathML puts the equation label before the expression on some pages.
              const tagsPresent=expected.tags.every(tag=>nodes.some(n=>n.textContent.replace(/\s/g,'').includes(`(${tag})`)));
              if(!tagsPresent)failures.push('Missing equation labels');
              return {rendered:nodes.length,errors,invisible,tagsPresent,failures};
            },item);
            result={file:item.path,status:response.status(),...result};break;
          }catch(e){result={file:item.path,failures:[e.message]};if(attempt<2)await page.waitForTimeout(4000*(attempt+1));}
        }
        if(!result.failures.length && (item.path===pages[0].path||item.path.includes('gene-regulation')&&item.part===3)){
          await page.locator('article').screenshot({path:new URL('./github-'+path.basename(item.path)+'.png',import.meta.url).pathname}).catch(()=>{});
        }
        results.push(result);
        if(results.length%10===0)console.log(`Checked ${results.length}/${pages.length} GitHub pages; failures ${results.filter(r=>r.failures.length).length}`);
      }
      await page.close();
    }
    await Promise.all([worker(),worker(),worker()]);
  }
}finally{await browser.close();}
results.sort((a,b)=>a.file.localeCompare(b.file));
const summary={mode,pages:results.length,expressions:results.reduce((sum,r)=>sum+(r.rendered??0),0),failures:results.filter(r=>r.failures.length),results};
fs.writeFileSync(new URL('./browser-'+mode+'.json',import.meta.url),JSON.stringify(summary,null,2)+'\n');
console.log(JSON.stringify({mode,pages:summary.pages,expressions:summary.expressions,failures:summary.failures},null,2));
process.exitCode=summary.failures.length?1:0;
