from pathlib import Path
import pymupdf
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[4]
out=Path(__file__).parent/'et-pages';out.mkdir(exist_ok=True)
for lecture in range(1,17):
    doc=pymupdf.open(root/f'other/sources/Equilibrium Thermodynamics/20TLect{lecture}.pdf')
    for start in range(0,len(doc),6):
        sheet=Image.new('RGB',(1800,1060),'#dddddd');draw=ImageDraw.Draw(sheet)
        for j in range(start,min(start+6,len(doc))):
            pix=doc[j].get_pixmap(matrix=pymupdf.Matrix(1.3,1.3))
            im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
            im.thumbnail((595,505));x=(j-start)%3*600;y=(j-start)//3*530
            sheet.paste(im,(x,y+25));draw.text((x+5,y+5),f'ET lecture {lecture}, PDF page {j+1}',fill='black')
        sheet.save(out/f'L{lecture:02}-{start+1:02}.png')
print('ET visual coverage sheets prepared')
