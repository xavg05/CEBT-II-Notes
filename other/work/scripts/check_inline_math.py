"""Reject detached mathematical scripts that can swallow prose on GitHub."""
from pathlib import Path
import re

MATH = re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')

def check_files(paths):
    count = 0
    for path in paths:
        text = path.read_text(encoding='utf-8')
        # Accept native and GitHub inline delimiters.
        text = re.sub(r'\$`([^`]*?)`\$', lambda m: '$' + m[1] + '$', text)
        for match in MATH.finditer(text):
            if match[2] is not None and match[2].lstrip().startswith(('^', '_')):
                line = text.count('\n', 0, match.start()) + 1
                raise ValueError(f'{path}:{line}: detached maths script; include its base inside the maths delimiters')
        count += 1
    return count

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[3]
    roots = [root/'notes', root/'other/obsidian', root/'other/work/drafts', root/'other/work/archive/reviewed-units']
    print(f'Inline maths check passed: {check_files(p for base in roots for p in base.rglob("*.md"))} Markdown files.')
