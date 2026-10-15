from pathlib import Path
import pymupdf
root=Path(__file__).resolve().parents[5]
out=Path(__file__).parent
for num in range(1,13):
    pdf=pymupdf.open(root/'other'/'sources'/'Advanced Biotechnology'/f'Lecture{num}.pdf')
    texts=[]
    heads=[]
    for i,p in enumerate(pdf):
        t=p.get_text()
        texts.append(f'\n--- Lecture {num}, PDF page {i+1} ---\n'+t)
        lines=[x.strip() for x in t.splitlines() if x.strip()]
        heads.append(f'p{i+1}: '+ ' | '.join(lines[:3]))
    (out/f'ab-L{num}.txt').write_text(''.join(texts),encoding='utf-8')
    print(f'LECTURE {num}: {len(pdf)}pp\n'+'\n'.join(heads))
