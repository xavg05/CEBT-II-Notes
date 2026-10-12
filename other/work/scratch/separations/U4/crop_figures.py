from pathlib import Path
from PIL import Image
import json
root=Path(__file__).resolve().parents[5]
src=root/'other/work/scratch/separations/U4'
dest=root/'notes/Separations II/figs';dest.mkdir(parents=True,exist_ok=True)
# Fractional boxes refer to the unmodified original-resolution scan dimensions.
items=[('u4-transport.png',9,(.025,.315,.96,.55)),('u4-fronts.png',12,(.25,.25,.75,.545)),('u4-breakthrough.png',14,(.07,.30,.72,.53)),('u4-pressure-swing.png',17,(0,.225,.96,.55)),('u4-chromatography.png',18,(.32,.32,.64,.595)),('u4-van-deemter.png',22,(.055,.31,.96,.59)),('u4-resolution.png',23,(.26,.095,.715,.38))]
records=[]
for name,page,box in items:
    im=Image.open(src/f'p{page:03d}.png').convert('RGB')
    pixels=tuple(round(v*(im.width if i%2==0 else im.height)) for i,v in enumerate(box))
    im.crop(pixels).save(dest/name)
    records.append({'figure':name,'page':page,'scan':f'p{page:03d}.png','pixel_box':pixels,'scan_size':im.size})
(src/'crops.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print('Cropped',len(records),'figures')
