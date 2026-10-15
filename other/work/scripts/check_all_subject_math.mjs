// KaTeX parse of every native and reading note in the four revised subjects, plus native/reading formula parity.
import fs from 'node:fs';
import path from 'node:path';
import katex from '../tools/math/node_modules/katex/dist/katex.mjs';
const gm=/^```math\r?\n([\s\S]*?)\r?\n```|(?<!\\)\$`([^`]*?)`\$/gm;
const nm=/(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$/g;
const key=s=>s.replace(/\\tag\{\d+\}/g,'').trim().replace(/\r\n/g,'\n');
const compat=s=>s.replace(/\\operatorname\{(Cov|Var|Re)\}/g,'\\mathrm{$1}').replaceAll('i<j','i\\lt j');
const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(d,e.name)):e.name.endsWith('.md')?[path.join(d,e.name)]:[]);
const res={files:0,formulas:0,errors:[]};
for(const s of ['Equilibrium Thermodynamics','Advanced Biotechnology','Reaction Engineering II','Separations II'])
 for(const f of walk(path.join('other/obsidian/CEBT-II Notes',s))){
  const g=path.join('notes',path.relative('other/obsidian/CEBT-II Notes',f));
  const n=[...fs.readFileSync(f,'utf8').matchAll(nm)],r=[...fs.readFileSync(g,'utf8').matchAll(gm)].map(m=>m[1]??m[2]);
  if(JSON.stringify(n.map(m=>key(compat(m[1]??m[2]))))!==JSON.stringify(r.map(key)))res.errors.push({file:g,error:'math mirror mismatch'});
  for(const m of n)try{katex.renderToString(m[1]??m[2],{displayMode:m[1]!==undefined,throwOnError:true,strict:'ignore'});res.formulas++}catch(e){res.errors.push({file:f,error:e.message})}
  for(const x of r)try{katex.renderToString(x,{throwOnError:true,strict:'ignore'})}catch(e){res.errors.push({file:g,error:e.message})}
  res.files++;
 }
fs.writeFileSync('other/work/scratch/all-subject-explanations/math-validation.json',JSON.stringify(res,null,2));
console.log(JSON.stringify({files:res.files,formulas:res.formulas,errors:res.errors.length,first:res.errors.slice(0,5)},null,2));
