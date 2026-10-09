import fs from 'node:fs';
import {marked} from './tools/node_modules/marked/lib/marked.esm.js';
const input=JSON.parse(fs.readFileSync(0,'utf8'));
const pattern=/(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$/g;
const result=input.map(text=>{
  const maths=[];
  let protectedText=text.replace(pattern,raw=>{const key=`MATHPLACEHOLDER${maths.length}END`;maths.push(raw);return key;});
  const edits=new Set();
  function visit(value){
    if(!value || typeof value!=='object')return;
    if(value.type==='em' && /MATHPLACEHOLDER\d+END/.test(value.raw))edits.add(value.raw);
    for(const child of Object.values(value)){
      if(Array.isArray(child))child.forEach(visit);
      else if(child && typeof child==='object')visit(child);
    }
  }
  visit(marked.lexer(protectedText));
  for(const raw of [...edits].sort((a,b)=>b.length-a.length))protectedText=protectedText.replaceAll(raw,raw.slice(1,-1));
  return protectedText.replace(/MATHPLACEHOLDER(\d+)END/g,(_,i)=>maths[Number(i)]);
});
process.stdout.write(JSON.stringify(result));
