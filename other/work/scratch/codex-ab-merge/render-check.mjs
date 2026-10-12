import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
const require=createRequire(import.meta.url);
const katex=require('./render/node_modules/katex');
const {marked}=await import('./render/node_modules/marked/lib/marked.esm.js');
const root=path.resolve('out');
const files=[...fs.readdirSync(root+'/AB').filter(x=>/^AB-5[0-7]-.*\.md$|^AB-4[89]-.*\.md$/.test(x)).map(x=>root+'/AB/'+x),...fs.readdirSync(root+'/merged').filter(x=>/^Advanced Biotechnology .*\.md$/.test(x)).map(x=>root+'/merged/'+x)];
const failures=[];let count=0;
for(const file of files){let text=fs.readFileSync(file,'utf8');
 text=text.replace(/(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$/g,(match,display,inline)=>{count++;try{return katex.renderToString(display??inline,{displayMode:display!==undefined,throwOnError:true,strict:'ignore'});}catch(e){failures.push({file,math:display??inline,error:e.message});return match;}});
 const html=marked.parse(text);
 if(!html.includes('<h1>'))failures.push({file,error:'No rendered H1'});
 fs.writeFileSync(new URL('./'+path.basename(file)+'.html',import.meta.url),'<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="render/node_modules/katex/dist/katex.min.css"><style>body{max-width:850px;margin:auto;font-family:Arial;line-height:1.5}img{max-width:100%}</style>'+html.replaceAll('src="figs/','src="../../../merged/figs/'));
}
fs.writeFileSync(new URL('./render-validation.json',import.meta.url),JSON.stringify({files:files.length,mathExpressions:count,failures},null,2));
console.log(JSON.stringify({files:files.length,mathExpressions:count,failures},null,2));
process.exitCode=failures.length?1:0;
