import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import katex from '../tools/math/node_modules/katex/dist/katex.mjs';
import {marked} from '../tools/math/node_modules/marked/lib/marked.esm.js';
const scratch='other/work/scratch/separations';
const manifest=JSON.parse(fs.readFileSync(scratch+'/publish-validation.json','utf8'));
const github=/^```math\n([\s\S]*?)\n```|(?<!\\)\$`([^`]*?)`\$/gm;
const native=/(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$/g;
const key=s=>s.replace(/\\tag\{\d+\}/g,'').trim();
const out=scratch+'/render';fs.mkdirSync(out,{recursive:true});
const results=[],failures=[],combined=[];let expressions=0;
const css=pathToFileURL(path.resolve('other/work/tools/math/node_modules/katex/dist/katex.min.css')).href;
for(const item of manifest.files){
 const gtext=fs.readFileSync(item.path,'utf8').replaceAll('\r\n','\n');
 const ntext=fs.readFileSync(item.obsidian,'utf8').replaceAll('\r\n','\n');
 const g=[...gtext.matchAll(github)].map(m=>m[1]??m[2]);
 const n=[...ntext.matchAll(native)].map(m=>m[1]??m[2]);
 if(JSON.stringify(g.map(key))!==JSON.stringify(n.map(key)))failures.push(`${item.path}: formula mismatch`);
 const tags=[...ntext.matchAll(/\\tag\{(\d+)\}/g)].map(m=>m[1]);
 const labels=[...gtext.matchAll(/\*\*Equation \((\d+)\)\*\*/g)].map(m=>m[1]);
 if(JSON.stringify(tags)!==JSON.stringify(labels))failures.push(`${item.path}: numbering mismatch`);
 let serial=0;const rendered=new Map();
 const protectedText=gtext.replace(github,(_,display,inline)=>{
  const token=`SEPMATHTOKEN${++serial}END`;
  try{rendered.set(token,katex.renderToString(display??inline,{displayMode:display!==undefined,throwOnError:true,strict:'ignore'}));}
  catch(e){failures.push(`${item.path}: ${e.message}`);rendered.set(token,'');}
  return token;
 });
 for(const m of ntext.matchAll(native))try{katex.renderToString(m[1]??m[2],{displayMode:m[1]!==undefined,throwOnError:true,strict:'ignore'});}catch(e){failures.push(`${item.obsidian}: ${e.message}`);}
 let html=marked.parse(protectedText);
 for(const [token,value] of rendered)html=html.replaceAll(token,value);
 if((html.match(/class="katex"/g)??[]).length!==g.length)failures.push(`${item.path}: lost formula`);
 if((html.match(/<h1[ >]/g)??[]).length!==1)failures.push(`${item.path}: heading count`);
 html=html.replace(/src="([^"]+)"/g,(_,src)=>`src="${pathToFileURL(path.resolve(path.dirname(item.path),src)).href}"`);
 const body=html;
 const preview=path.join(out,item.path.split('/').slice(-2).join('_')+'.html');
 fs.writeFileSync(preview,`<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="${css}"><style>body{max-width:850px;margin:40px auto;font:17px/1.55 Georgia}img{max-width:100%;max-height:650px}h1{font-size:30px}h2{font-size:23px}.katex-display{overflow-x:auto}</style>${body}`);
 if(path.basename(item.path).startsWith('SEP-'))combined.push(`<article>${body}</article>`);
 expressions+=g.length;results.push({file:item.path,preview,expressions:g.length,labels});
}
fs.writeFileSync(out+'/all-notes.html',`<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="${css}"><style>@page{size:A4;margin:16mm}body{font:12px/1.45 Georgia}h1{font-size:23px}h2{font-size:17px}img{max-width:100%;max-height:250px}.katex{font-size:1.02em}article{break-before:page}article:first-of-type{break-before:auto}h2{break-after:avoid}</style>${combined.join('\n')}`);
fs.writeFileSync(scratch+'/math-validation.json',JSON.stringify({pages:results.length,expressions,failures,results},null,2));
console.log(JSON.stringify({pages:results.length,expressions,failures}));
process.exitCode=failures.length?1:0;
