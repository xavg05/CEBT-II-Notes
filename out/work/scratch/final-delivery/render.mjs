import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import katex from '../codex-github-navigation/tools/node_modules/katex/dist/katex.mjs';
import {marked} from '../codex-github-navigation/tools/node_modules/marked/lib/marked.esm.js';
import {chromium} from '../codex-github-navigation/tools/node_modules/playwright/index.mjs';

const root=process.cwd();
const output=new URL('./',import.meta.url).pathname;
const manifest=JSON.parse(fs.readFileSync(output+'package-manifest.json','utf8'));
const formulas=/(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$/g;
const css=pathToFileURL(path.resolve(root,'out/work/scratch/codex-github-navigation/tools/node_modules/katex/dist/katex.min.css')).href;
const results=[],errors=[];
for (const [index,item] of manifest.entries()) {
  const file=path.resolve(root,item.path);
  const original=fs.readFileSync(file,'utf8');let count=0;const rendered=new Map();
  const transformed=original.replace(formulas,(_,display,inline)=>{
    count++;
    try{
      const token=`MATHTOKEN${count}END`;
      rendered.set(token,katex.renderToString(display??inline,{displayMode:display!==undefined,throwOnError:true,strict:'ignore'}));
      return token;
    }
    catch(e){errors.push({file:item.path,expression:display??inline,error:e.message});return '';}
  });
  let html=marked.parse(transformed);
  for(const [token,value] of rendered)html=html.replace(token,value);
  if((html.match(/class="katex"/g)??[]).length!==count)errors.push({file:item.path,error:'Rendered HTML lost mathematical expressions'});
  const filename=output+`unit-${String(index+1).padStart(2,'0')}.html`;
  fs.writeFileSync(filename,`<!doctype html><meta charset="utf-8"><base href="${pathToFileURL(path.dirname(file)+'/').href}"><link rel="stylesheet" href="${css}"><style>body{max-width:980px;margin:32px auto;font:16px/1.65 Arial}img{display:block;max-width:100%;height:auto;margin:1em auto}.katex-display{overflow-x:auto;padding:.4em 0}table{border-collapse:collapse}td,th{padding:5px;border:1px solid #ddd}</style>`+html);
  results.push({file:item.path,html:filename,expressions:count});
}
// Parse the complete alternatives as well, rather than assuming unit checks suffice.
let completeCount=0;
for (const subject of ['equilibrium-thermodynamics','advanced-biotechnology']) {
 const file=`notes/${subject}/complete-obsidian.md`;
 const s=fs.readFileSync(file,'utf8');
 for(const m of s.matchAll(formulas)){
  completeCount++;
  try{katex.renderToString(m[1]??m[2],{displayMode:m[1]!==undefined,throwOnError:true,strict:'ignore'});}
  catch(e){errors.push({file,error:e.message});}
 }
}
let browser;
const browserRequested=process.argv.includes('--browser');
try{
 if(browserRequested){
 browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,timeout:20000,args:['--disable-crashpad-for-testing','--disable-crash-reporter','--noerrdialogs']});
 const page=await browser.newPage({viewport:{width:1440,height:1050}});
 for(const [i,item] of results.entries()){
  await page.goto(pathToFileURL(item.html).href,{waitUntil:'load',timeout:20000});
  await page.evaluate(()=>document.fonts.ready);
  const check=await page.evaluate(()=>({math:document.querySelectorAll('.katex').length,missingImages:[...document.images].filter(x=>!x.complete||!x.naturalWidth).map(x=>x.src),errors:[...document.querySelectorAll('.katex-error')].map(x=>x.textContent)}));
  if(check.math!==item.expressions||check.missingImages.length||check.errors.length)errors.push({file:item.file,...check});
  item.browser=check;
  if([0,1,6,11,12,16,18,19,22,23,26,28].includes(i))await page.screenshot({path:output+`preview-${String(i+1).padStart(2,'0')}.png`});
 }
 await page.close();
 }
}catch(e){errors.push({browser:e.message});}
finally{if(browser)await browser.close();}
const result={unitFiles:results.length,unitExpressions:results.reduce((n,r)=>n+r.expressions,0),completeExpressions:completeCount,browserRequested,errors,results};
fs.writeFileSync(output+'render-validation.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({unitFiles:result.unitFiles,unitExpressions:result.unitExpressions,completeExpressions:completeCount,errors},null,2));
process.exitCode=errors.length?1:0;
