// Parse both editions and compare complete text after normalising maths layout.
import fs from 'node:fs';
import path from 'node:path';
import katex from '../tools/math/node_modules/katex/dist/katex.mjs';
import {marked} from '../tools/math/node_modules/marked/lib/marked.esm.js';
const root='other/obsidian/CEBT-II Notes';
const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(d,e.name)):e.name.endsWith('.md')?[path.join(d,e.name)]:[]);
const gm=/^```math\r?\n([\s\S]*?)\r?\n```|(?<!\\)\$`([^`]*?)`\$/gm;
const nm=/(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$/g;
const compat=s=>s.replace(/\\operatorname\{(Cov|Var|Re)\}/g,'\\mathrm{$1}').replaceAll('i<j','i\\lt j');
const formula=s=>compat(s.replace(/\\tag\{\d+\}/g,'').trim()).replace(/\s+/g,'');
const textkey=s=>s.replace(/\s+/g,' ').trim();
const errors=[],pages=[];let expressions=0,rendered=0;
for(const subject of ['Equilibrium Thermodynamics','Advanced Biotechnology','Reaction Engineering II','Separations II','Process Dynamics and Control']){
 for(const f of walk(path.join(root,subject))){
  if(path.basename(f)==='README.md')continue;
  const g=path.join('notes',path.relative(root,f));
  const native=fs.readFileSync(f,'utf8'),reading=fs.readFileSync(g,'utf8');
  const n=[...native.matchAll(nm)],r=[...reading.matchAll(gm)];
  if(JSON.stringify(n.map(m=>formula(m[1]??m[2])))!==JSON.stringify(r.map(m=>formula(m[1]??m[2]))))errors.push({file:g,error:'formula parity'});
  const nt=native.replace(nm,(_,a,b)=>' MATH '+formula(a??b)+' ');
  const rt=reading.replace(/^\*\*Equation \(\d+\)\*\*\s*$/gm,'').replace(gm,(_,a,b)=>' MATH '+formula(a??b)+' ');
  if(textkey(nt)!==textkey(rt))errors.push({file:g,error:'full text parity'});
  let serial=0;const tokens=new Map();
  const protectedText=reading.replace(gm,(_,a,b)=>{
   const token=`RECOVERYMATHTOKEN${++serial}END`;
   try{tokens.set(token,katex.renderToString(a??b,{displayMode:a!==undefined,throwOnError:true,strict:'ignore'}));expressions++;}
   catch(e){errors.push({file:g,error:e.message});tokens.set(token,'');}
   return token;
  });
  let html=marked.parse(protectedText);
  for(const [token,value] of tokens)html=html.replace(token,value);
  if((html.match(/class="katex"/g)??[]).length!==r.length)errors.push({file:g,error:'HTML lost formula'});
  if((html.match(/<h1[ >]/g)??[]).length!==1)errors.push({file:g,error:'H1 structure'});
  for(const m of n)try{katex.renderToString(m[1]??m[2],{displayMode:m[1]!==undefined,throwOnError:true,strict:'ignore'});expressions++;}catch(e){errors.push({file:f,error:e.message});}
  const tags=[...native.matchAll(/\\tag\{(\d+)\}/g)].map(m=>m[1]);
  const labels=[...reading.matchAll(/^\*\*Equation \((\d+)\)\*\*/gm)].map(m=>m[1]);
  if(JSON.stringify(tags)!==JSON.stringify(labels))errors.push({file:g,error:'label parity'});
  if(/^#{2,6}\s+Worked examples?\s*$/mi.test(reading))errors.push({file:g,error:'worked-example section survived'});
  if(/\bworked example (?:above|below)|\bthe worked example (?:shows|makes|contrasts)/i.test(reading))errors.push({file:g,error:'dangling worked example'});
  pages.push({file:g,formulas:r.length});rendered++;
 }
}
const result={pages_per_edition:rendered,parsed_expressions:expressions,errors,pages};
fs.writeFileSync('other/work/progress/teaching-recovery-math-20261022.json',JSON.stringify(result,null,2));
console.log(JSON.stringify({pages_per_edition:rendered,parsed_expressions:expressions,errors},null,2));
process.exitCode=errors.length?1:0;
