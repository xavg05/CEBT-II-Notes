from pathlib import Path
import pymupdf,json
root=Path(__file__).resolve().parents[4]
specs=[
 (3,18,(140,275,470,490),'RE-S3-03-staged-beds.png'),
 (3,29,(55,50,550,710),'RE-S3-05-transport-pathway.png'),
 (4,8,(88,235,455,455),'RE-S4-03-bet-isotherms.png'),
 (4,12,(130,515,515,655),'RE-S4-04-pore-hysteresis.png'),
 (5,3,(88,312,455,535),'RE-S5-01-rate-maximum.png'),
 (5,5,(65,353,535,540),'RE-S5-02-temperature-effects.png'),
 (6,6,(115,480,500,690),'RE-S6-02-pellet-profiles.png'),
]
out=root/'notes/Reaction Engineering II/figs';out.mkdir(exist_ok=True)
for section,page,rect,name in specs:
    doc=pymupdf.open(root/f'other/sources/Reaction Engineering II/CEBT II reaction engineering {section}.pdf')
    doc[page-1].get_pixmap(matrix=pymupdf.Matrix(3,3),clip=pymupdf.Rect(rect)).save(out/name)
(Path(__file__).parent/'re-crops.json').write_text(json.dumps(specs,indent=2))
