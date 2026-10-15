from pathlib import Path
import pymupdf
from PIL import Image, ImageDraw
root=Path(__file__).resolve().parents[4]
out=Path(__file__).parent/'re-pages'; out.mkdir(exist_ok=True)
for section in (3,4,5,6):
    doc=pymupdf.open(root/f'other/sources/Reaction Engineering II/CEBT II reaction engineering {section}.pdf')
    for start in range(0,len(doc),6):
        sheet=Image.new('RGB',(1500,1460),'#dddddd'); draw=ImageDraw.Draw(sheet)
        for j in range(start,min(start+6,len(doc))):
            p=doc[j]; pix=p.get_pixmap(matrix=pymupdf.Matrix(1.5,1.5))
            im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
            im.save(out/f's{section}-p{j+1:02}.png')
            im.thumbnail((490,700)); x=(j-start)%3*500; y=(j-start)//3*730
            sheet.paste(im,(x,y+25));draw.text((x+5,y+5),f'Section {section}, PDF page {j+1}',fill='black')
        sheet.save(out/f's{section}-montage-{start+1:02}.png')
print(out)
