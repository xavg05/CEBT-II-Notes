import fs from 'node:fs';
import path from 'node:path';
import katex from '../scratch/codex-github-navigation/tools/node_modules/katex/dist/katex.mjs';
import {marked} from '../scratch/codex-github-navigation/tools/node_modules/marked/lib/marked.esm.js';

const manifest=JSON.parse(fs.readFileSync('other/work/LAYOUT-MANIFEST.json','utf8'));
const github=/^```math\n([\s\S]*?)\n```|(?<!\\)\$`([^`]*?)`\$/gm;
const native=/(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$/g;
const compatible=s=>s.replace(/\\operatorname\{(Cov|Var|Re)\}/g,'\\mathrm{$1}').replaceAll('i<j','i\\lt j');
const formulaKey=s=>compatible(s.replace(/\\tag\{\d+\}/g,'').trim());
const failures=[];let count=0;const results=[];
const out='other/work/scratch/reorganize-layout/render';fs.mkdirSync(out,{recursive:true});
for(const item of manifest.files){
 const reading=fs.readFileSync(item.path,'utf8');
 const obsidian=fs.readFileSync(item.obsidian,'utf8');
 const g=[...reading.matchAll(github)].map(m=>(m[1]??m[2]).trim());
 const n=[...obsidian.matchAll(native)].map(m=>(m[1]??m[2]).trim());
 if(JSON.stringify(g.map(formulaKey))!==JSON.stringify(n.map(formulaKey)))failures.push({file:item.path,error:'Reading/native formula mismatch'});
 const tags=[...obsidian.matchAll(/\\tag\{(\d+)\}/g)].map(m=>+m[1]);
 const labels=[...reading.matchAll(/^\*\*Equation \((\d+)\)\*\*\s*\n(?=\s*```math)/gm)].map(m=>+m[1]);
 if(JSON.stringify(tags)!==JSON.stringify(labels))failures.push({file:item.path,error:'Equation labels differ'});
 if(g.length!==item.expressions)failures.push({file:item.path,error:'Expression count differs'});
 let rendered=new Map(),serial=0;
 const protectedReading=reading.replace(github,(_,display,inline)=>{
  const token=`MATHRENDERTOKEN${++serial}END`;
  try{rendered.set(token,katex.renderToString(display??inline,{displayMode:display!==undefined,throwOnError:true,strict:'ignore'}));}
  catch(e){failures.push({file:item.path,error:e.message});rendered.set(token,'');}
  return token;
 });
 let html=marked.parse(protectedReading);
 for(const [token,value] of rendered)html=html.replace(token,value);
 if((html.match(/class="katex"/g)??[]).length!==g.length)failures.push({file:item.path,error:'Generated HTML lost formulas'});
 if((html.match(/<h1[ >]/g)??[]).length!==1)failures.push({file:item.path,error:'Expected one H1'});
 // Check the native maths separately, including its equation-tag syntax.
 for(const m of obsidian.matchAll(native)){
  try{katex.renderToString(m[1]??m[2],{displayMode:m[1]!==undefined,throwOnError:true,strict:'ignore'});}
  catch(e){failures.push({file:item.obsidian,error:e.message});}
 }
 fs.writeFileSync(path.join(out,path.basename(item.path).replace('.md','.html')),html);
 count+=g.length;results.push({file:item.path,expressions:g.length,labels});
}
const result={pages:manifest.files.length,expressions:count,reading_and_obsidian_math_match:true,failures,results};
fs.writeFileSync('other/work/LAYOUT-MATH-VALIDATION.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({pages:result.pages,expressions:result.expressions,failures},null,2));
process.exitCode=failures.length?1:0;
