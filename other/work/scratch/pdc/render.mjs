import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import katex from '../codex-github-navigation/tools/node_modules/katex/dist/katex.mjs';
import {marked} from '../codex-github-navigation/tools/node_modules/marked/lib/marked.esm.js';
import {chromium} from '../codex-github-navigation/tools/node_modules/playwright/index.mjs';
const root=process.cwd(),out=path.join(root,'other/work/scratch/pdc');
const manifest=JSON.parse(fs.readFileSync(out+'/publish-validation.json','utf8')).manifest;
const math=/(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$/g;
const css=pathToFileURL(path.join(root,'other/work/scratch/codex-github-navigation/tools/node_modules/katex/dist/katex.min.css')).href;
const result={files:[],errors:[],browser:false};
for(const item of manifest){
 const file=path.join(root,item.obsidian),source=fs.readFileSync(file,'utf8');let count=0;const rendered=new Map();
 const transformed=source.replace(math,(_,display,inline)=>{
  const token=`PDCMATHTOKEN${++count}END`;
  try{rendered.set(token,katex.renderToString(display??inline,{displayMode:display!==undefined,throwOnError:true,strict:'ignore'}));}
  catch(e){result.errors.push({file:item.obsidian,expression:display??inline,error:e.message});rendered.set(token,'');}
  return token;
 });
 let html=marked.parse(transformed);for(const [token,value] of rendered)html=html.replaceAll(token,value);
 const github=fs.readFileSync(path.join(root,item.path),'utf8');
 const gitmath=[...github.matchAll(/```math\n([\s\S]*?)\n```|\$`([^`]*?)`\$/g)];
 if(gitmath.length!==count)result.errors.push({file:item.path,error:'Math expression count mismatch',github:gitmath.length,native:count});
 for(const m of gitmath)try{katex.renderToString(m[1]??m[2],{displayMode:m[1]!==undefined,throwOnError:true,strict:'ignore'});}catch(e){result.errors.push({file:item.path,error:e.message});}
 const filename=path.join(out,path.basename(item.path)+'.html');
 fs.writeFileSync(filename,`<!doctype html><meta charset="utf-8"><base href="${pathToFileURL(path.dirname(file)+'/').href}"><link rel="stylesheet" href="${css}"><style>body{max-width:920px;margin:36px auto;padding:0 20px;font:16px/1.65 Arial;color:#20242a}img{display:block;max-width:100%;max-height:640px;height:auto;margin:24px auto}h1,h2{line-height:1.3}.katex-display{overflow-x:auto;padding:6px 0}table{border-collapse:collapse}td,th{padding:8px;border:1px solid #ccd1d7}a{color:#17519c}</style>`+html);
 result.files.push({file:item.path,html:filename,expressions:count});
}
let browser;
if(process.argv.includes('--browser'))try{
 browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,args:['--disable-crashpad-for-testing','--disable-crash-reporter','--noerrdialogs']});
 const page=await browser.newPage({viewport:{width:1200,height:1000}});
 for(const item of result.files){
  await page.goto(pathToFileURL(item.html).href,{waitUntil:'load'});await page.evaluate(()=>document.fonts.ready);
  const check=await page.evaluate(()=>({math:document.querySelectorAll('.katex').length,images:[...document.images].map(x=>({src:x.src,loaded:x.complete&&x.naturalWidth>0})),errors:[...document.querySelectorAll('.katex-error')].map(x=>x.textContent),overflow:[...document.querySelectorAll('table')].filter(x=>x.scrollWidth>document.body.clientWidth).length}));
  if(check.math!==item.expressions||check.images.some(x=>!x.loaded)||check.errors.length||check.overflow)result.errors.push({file:item.file,...check});
  item.browser=check;
  if(path.basename(item.file).startsWith('PDC-'))await page.screenshot({path:path.join(out,path.basename(item.file)+'.png'),fullPage:true});
 }
 result.browser=true;await page.close();
}catch(e){result.errors.push({browser:e.message});}finally{if(browser)await browser.close();}
result.browserRequested=process.argv.includes('--browser');
fs.writeFileSync(out+'/render-validation.json',JSON.stringify(result,null,2));
console.log(JSON.stringify({files:result.files.length,expressions:result.files.reduce((a,x)=>a+x.expressions,0),browser:result.browser,errors:result.errors},null,2));
process.exitCode=result.errors.length?1:0;
