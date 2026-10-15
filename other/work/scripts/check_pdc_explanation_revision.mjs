import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import katex from '../tools/math/node_modules/katex/dist/katex.mjs';
import {marked} from '../tools/math/node_modules/marked/lib/marked.esm.js';

const root=process.cwd(), out=path.join(root,'other/work/scratch/pdc-explanation-revision');
const manifest=JSON.parse(fs.readFileSync('other/work/scratch/pdc/publish-validation.json','utf8')).manifest;
const gm=/^```math\r?\n([\s\S]*?)\r?\n```|(?<!\\)\$`([^`]*?)`\$/gm;
const nm=/(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$/g;
const key=s=>s.replace(/\\tag\{\d+\}/g,'').trim().replace(/\r\n/g,'\n');
const result={files:[],errors:[]};let sections=[],tags=[];
for(const item of manifest){
 const native=fs.readFileSync(item.obsidian,'utf8').replace(/\r\n/g,'\n'),github=fs.readFileSync(item.path,'utf8').replace(/\r\n/g,'\n');
 const n=[...native.matchAll(nm)].map(m=>m[1]??m[2]),g=[...github.matchAll(gm)].map(m=>m[1]??m[2]);
 if(JSON.stringify(n.map(key))!==JSON.stringify(g.map(key)))result.errors.push({file:item.path,error:'Math mirror mismatch'});
 for(const formula of g)try{katex.renderToString(formula,{throwOnError:true,strict:'ignore'});}catch(e){result.errors.push({file:item.path,error:e.message});}
 let tokens=new Map(),i=0;
 const source=native.replace(nm,(_,display,inline)=>{
  const token=`PDCMATHTOKEN${++i}END`;
  try{tokens.set(token,katex.renderToString(display??inline,{displayMode:display!==undefined,throwOnError:true,strict:'ignore'}));}
  catch(e){result.errors.push({file:item.obsidian,error:e.message});tokens.set(token,'');}return token;
 });
 let html=marked.parse(source);for(const [token,value] of tokens)html=html.replaceAll(token,value);
 html=html.replace(/src="([^\"]+)"/g,(_,src)=>`src="${pathToFileURL(path.resolve(path.dirname(item.obsidian),decodeURIComponent(src))).href}"`);
 if((html.match(/class="katex"/g)??[]).length!==n.length)result.errors.push({file:item.path,error:'Lost rendered formula'});
 if(path.basename(item.path).startsWith('PDC-')){
  const canonical=path.join(root,'other/work/drafts/Process Dynamics and Control',path.basename(item.path));
  const draft=fs.readFileSync(canonical,'utf8').replace(/\r\n/g,'\n').trim();
  const content=native.split('<!-- note-content:start -->\n')[1].split('\n<!-- note-content:end -->')[0].trim();
  if(content!==draft)result.errors.push({file:item.path,error:'Draft mismatch'});
  tags.push(...[...draft.matchAll(/\\tag\{(\d+)\}/g)].map(m=>Number(m[1])));
  sections.push(`<article>${html}</article>`);
 }
 result.files.push({file:item.path,expressions:n.length});
}
if(JSON.stringify(tags)!==JSON.stringify(Array.from({length:71},(_,i)=>i+1)))result.errors.push({error:'Equation label sequence changed'});
const css=pathToFileURL(path.join(root,'other/work/tools/math/node_modules/katex/dist/katex.min.css')).href;
fs.writeFileSync(path.join(out,'all-notes.html'),`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="${css}"><style>@page{size:A4;margin:16mm}body{font:15px/1.55 Arial;color:#20242a;max-width:900px;margin:auto}article{break-before:page}h1,h2{break-after:avoid;line-height:1.25}img{display:block;max-width:100%;max-height:500px;margin:20px auto}table{border-collapse:collapse}td,th{border:1px solid #ccd1d7;padding:6px}.katex-display{overflow-x:auto;padding:5px 0}a{color:#17519c}</style></head><body>${sections.join('\n')}</body></html>`);
result.numberedEquations=tags.length;
result.expressionsPerEdition=result.files.reduce((a,x)=>a+x.expressions,0);
fs.writeFileSync(path.join(out,'render-validation.json'),JSON.stringify(result,null,2));
console.log(JSON.stringify({files:result.files.length,expressions:result.expressionsPerEdition,numberedEquations:tags.length,errors:result.errors},null,2));
process.exitCode=result.errors.length?1:0;
