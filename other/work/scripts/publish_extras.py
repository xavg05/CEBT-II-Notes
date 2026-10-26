"""Publish supervision extras from the native Obsidian copy to GitHub-compatible notes/extras/.

Source: other/obsidian/CEBT-II Notes/Extras/<subject>/*.md (dollar maths).
Output: notes/extras/<subject>/*.md (GitHub maths), same maths conversion as build_notes.py.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT/'other/obsidian/CEBT-II Notes/Extras'
OUT = ROOT/'notes/extras'
MATH = re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')

def compatible(s):
    return re.sub(r'\\operatorname\{(Cov|Var|Re)\}', r'\\mathrm{\1}', s).replace('i<j', r'i\lt j')

def github(s):
    def render(m):
        if m[1] is not None:
            return '\n```math\n' + compatible(m[1].strip()) + '\n```\n'
        return '$`' + compatible(m[2]) + '`$'
    return MATH.sub(render, s)

count = 0
for src in sorted(SRC.rglob('*.md')):
    dst = OUT/src.relative_to(SRC)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(github(src.read_text(encoding='utf-8')), encoding='utf-8', newline='\n')
    count += 1
print(f'Published {count} extras file(s) to {OUT.relative_to(ROOT)}.')
