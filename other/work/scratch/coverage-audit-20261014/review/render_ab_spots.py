from pathlib import Path
import pymupdf
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[5]
out=Path(__file__).parent/'ab-visual-spots'
out.mkdir(exist_ok=True)
chosen={1:[22,30,33,37],2:[20,24,25,26],3:[20,21,35],4:[14,15,16,18],5:[15,19,24],6:[37,38],7:[10,32,33,38,39,41,43,47,48,50,51,55,56,58,59,61,62],8:[14,15,21,25,42],9:[7,8,20,21,40],10:[16,27,34,35,55],11:[36,38,42,46],12:[30,36,39,40]}
cards=[]
for n, nums in chosen.items():
    pdf=pymupdf.open(root/'other/sources/Advanced Biotechnology'/f'Lecture{n}.pdf')
    for p in nums:
        pix=pdf[p-1].get_pixmap(matrix=pymupdf.Matrix(1.4,1.4))
        f=out/f'L{n}-p{p:02}.png';pix.save(str(f))
        im=Image.open(f).convert('RGB');im.thumbnail((620,650))
        tile=Image.new('RGB',(640,680),'white');ImageDraw.Draw(tile).text((5,5),f'Original Lecture {n}, PDF p{p}',fill='black');tile.paste(im,(10,25));cards.append(tile)
for start in range(0,len(cards),6):
    sheet=Image.new('RGB',(1280,2040),'#dddddd')
    for i,card in enumerate(cards[start:start+6]):sheet.paste(card,((i%2)*640,(i//2)*680))
    f=out/f'spots-{start//6+1:02}.png';sheet.save(f);print(f.name)
