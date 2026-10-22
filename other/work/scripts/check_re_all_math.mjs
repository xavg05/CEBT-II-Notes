// Parse every Reaction Engineering II expression with KaTeX in both editions and check parity.
// Usage: node other/work/scripts/check_re_all_math.mjs [root]   (run from the repository root)
import fs from 'node:fs';
import path from 'node:path';
import katex from '../tools/math/node_modules/katex/dist/katex.mjs';

const root = process.argv[2] ?? '.';
const subject = 'Reaction Engineering II';
const readDir = path.join(root, 'notes', subject);
const nativeDir = path.join(root, 'other/obsidian/CEBT-II Notes', subject);
const github = /^```math\n([\s\S]*?)\n```|(?<!\\)\$`([^`]*?)`\$/gm;
const native = /(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$/g;
const strip = s => s.replace(/\\tag\{\d+\}/g, '').trim();

const walk = d => fs.readdirSync(d, {withFileTypes: true}).flatMap(e =>
  e.isDirectory() ? walk(path.join(d, e.name)) : e.name.endsWith('.md') ? [path.join(d, e.name)] : []);

let expressions = 0;
const failures = [];
for (const file of walk(nativeDir)) {
  const rel = path.relative(nativeDir, file);
  const n = fs.readFileSync(file, 'utf8').replaceAll('\r\n', '\n');
  const g = fs.readFileSync(path.join(readDir, rel), 'utf8').replaceAll('\r\n', '\n');
  const nx = [...n.matchAll(native)].map(m => ({tex: m[1] ?? m[2], display: m[1] !== undefined}));
  const gx = [...g.matchAll(github)].map(m => m[1] ?? m[2]);
  if (nx.length !== gx.length || nx.some((x, i) => strip(x.tex) !== strip(gx[i])))
    failures.push(`${rel}: editions differ`);
  for (const x of nx) {
    expressions++;
    try {
      katex.renderToString(x.tex, {displayMode: x.display, throwOnError: true, strict: 'ignore'});
    } catch (e) {
      failures.push(`${rel}: ${e.message.split('\n')[0]} :: ${x.tex.slice(0, 80)}`);
    }
  }
}
console.log(JSON.stringify({expressions, failures}, null, 2));
process.exit(failures.length ? 1 : 0);
