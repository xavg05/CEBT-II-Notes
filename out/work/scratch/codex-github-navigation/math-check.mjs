import fs from 'node:fs';
import katex from './tools/node_modules/katex/dist/katex.mjs';
import {marked} from './tools/node_modules/marked/lib/marked.esm.js';
const manifest=JSON.parse(fs.readFileSync(new URL('./manifest.json',import.meta.url)));
const pattern=/^```math\n([\s\S]*?)\n```|(?<!\\)\$`([^`]*?)`\$/gm;
const results=[];const failures=[];
for(const subject of manifest.subjects){
  for(const page of subject.pages){
    const text=fs.readFileSync(page.path,'utf8');let count=0;
    const html=marked.parse(text.replace(pattern,(_,display,inline)=>{
      count++;
      try{return katex.renderToString(display??inline,{displayMode:display!==undefined,throwOnError:true,strict:'ignore'});}
      catch(e){failures.push({file:page.path,math:display??inline,error:e.message});return '';}
    }));
    const protectedText=text.replace(pattern,'MATHPLACEHOLDER');
    function visit(v){
      if(!v||typeof v!=='object')return;
      if(v.type==='em' && v.raw?.includes('MATHPLACEHOLDER'))failures.push({file:page.path,error:'Math remains inside emphasis'});
      for(const x of Object.values(v)){if(Array.isArray(x))x.forEach(visit);else if(x&&typeof x==='object')visit(x);}
    }
    visit(marked.lexer(protectedText));
    if(count!==page.expressions)failures.push({file:page.path,error:'Expression count mismatch'});
    fs.writeFileSync(new URL('./'+page.path.replaceAll('/','__')+'.html',import.meta.url),'<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="tools/node_modules/katex/dist/katex.min.css"><style>body{max-width:950px;margin:30px auto;font:16px/1.6 Arial}img{max-width:100%}.katex-display{overflow-x:auto}</style>'+html.replaceAll('src="figs/','src="../../../../'+page.path.split('/').slice(0,-1).join('/')+'/figs/'));
    results.push({file:page.path,expressions:count});
  }
}
const result={pages:results.length,expressions:results.reduce((n,r)=>n+r.expressions,0),failures};
fs.writeFileSync(new URL('./math-validation.json',import.meta.url),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result,null,2));process.exitCode=failures.length?1:0;
