import fs from 'node:fs';
import path from 'node:path';
import katex from '../tools/math/node_modules/katex/dist/katex.mjs';
import {marked} from '../tools/math/node_modules/marked/lib/marked.esm.js';

const base='notes';
const out='other/work/scratch/finalisation-20261022/render';fs.mkdirSync(out,{recursive:true});
const files=[];
function walk(dir){for(const ent of fs.readdirSync(dir,{withFileTypes:true})){const p=path.join(dir,ent.name);if(ent.isDirectory())walk(p);else if(p.endsWith('.md'))files.push(p);}}
walk(base);
const gm=/^```math\r?\n([\s\S]*?)\r?\n```|(?<!\\)\$`([^`]*?)`\$/gm;
const nm=/(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$/g;
const key=s=>s.replace(/\\tag\{\d+\}/g,'').trim().replace(/\r\n/g,'\n').replace(/\\operatorname\{(Cov|Var|Re)\}/g,'\\mathrm{$1}').replaceAll('i<j','i\\lt j');
const results=[],failures=[];let expressions=0,links=0,figures=new Set();
for(const file of files){
 const text=fs.readFileSync(file,'utf8');
 const native=path.join('other/obsidian/CEBT-II Notes',path.relative(base,file));
 const nt=fs.existsSync(native)?fs.readFileSync(native,'utf8'):'';
 if(!nt)failures.push({file,error:'Missing native mirror'});
 const g=[...text.matchAll(gm)].map(m=>m[1]??m[2]);
 const n=[...nt.matchAll(nm)].map(m=>m[1]??m[2]);
 if(JSON.stringify(g.map(key))!==JSON.stringify(n.map(key)))failures.push({file,error:'Formula mismatch with native mirror'});
 const tokens=new Map();let serial=0;
 const protectedText=text.replace(gm,(_,display,inline)=>{
  const token=`MATHRENDERTOKEN${++serial}END`;
  try{tokens.set(token,katex.renderToString(display??inline,{displayMode:display!==undefined,throwOnError:true,strict:'ignore'}));}
  catch(e){failures.push({file,error:e.message});tokens.set(token,'');}return token;
 });
 let html=marked.parse(protectedText);for(const [token,value] of tokens)html=html.replace(token,value);
 if((html.match(/class="katex"/g)??[]).length!==g.length)failures.push({file,error:'HTML lost formulas'});
 if((html.match(/<h1[ >]/g)??[]).length!==1)failures.push({file,error:'Expected one H1'});
 const cost=g.reduce((sum,x)=>sum+(x.match(/\{/g)??[]).length+1,0);
 if(cost>=2000)failures.push({file,error:'Math budget >=2000'});
 for(const [source,value] of [[file,text.replace(gm,'')],[native,nt.replace(nm,'')]])for(const m of value.matchAll(/(!?)\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)/g)){
  const target=m[2]??m[3];if(/^[a-z][a-z\d+.-]*:/i.test(target)||target.startsWith('#'))continue;
  const dest=path.resolve(path.dirname(source),decodeURIComponent(target.split('#')[0]));links++;
  if(!fs.existsSync(dest))failures.push({file:source,error:`Missing link: ${target}`});
  if(m[1])figures.add(dest);
 }
 expressions+=g.length;results.push({file,expressions:g.length,math_cost:cost});
 fs.writeFileSync(path.join(out,path.relative(base,file).replace(/[\\/]/g,'__')+'.html'),`<!doctype html><meta charset="utf-8">${html}`);
}
const result={reading_pages:files.length,expressions_per_edition:expressions,links_in_both_editions:links,distinct_figure_paths:figures.size,failures,results};
fs.writeFileSync('other/work/progress/all-reading-validation.json',JSON.stringify(result,null,2));
console.log(JSON.stringify({...result,results:undefined},null,2));if(failures.length)process.exitCode=1;
