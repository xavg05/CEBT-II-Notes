from pathlib import Path
import pymupdf as fitz,json
root=Path('out/work/scratch/final-ab-31-47'); dest=root/'figures';dest.mkdir(exist_ok=True)
specs={
'AB-31-bioprocess-steps':(9,9,[0]),'AB-32-cost-vs-price':(9,23,[0]),'AB-32-process-logic':(9,21,[0]),'AB-32-purity-table':(9,20,[0]),
'AB-33-dead-end-filter':(9,27,[0]),'AB-33-filter-aids':(9,28,[0,1]),'AB-33-plate-frame':(9,30,[0,1]),'AB-33-rotary-drum':(9,33,[0]),
'AB-35-comparison-table':(10,16,[0]),'AB-35-disc-stack':(10,13,[0]),'AB-35-tubular-bowl':(10,12,[0]),'AB-36-tubular-geometry':(10,24,[0]),'AB-37-disc-stack-geometry':(10,34,[0]),
'AB-38-cell-walls':(10,44,[0]),'AB-38-inclusion-bodies':(10,41,[0]),'AB-38-yeast-wall':(10,45,[0]),'AB-39-bead-mill':(10,48,[0]),'AB-39-french-press':(10,54,[0]),'AB-39-homogeniser-valve':(10,51,[0]),'AB-39-ultrasonication':(10,50,[0]),'AB-40-fit-plot':(10,59,[0]),
'AB-41-decompression':(11,10,[0]),'AB-41-detergent':(11,13,[0]),'AB-41-osmotic-shock':(11,11,[0]),'AB-42-ATPE-phases':(11,25,[0,1]),'AB-42-countercurrent':(11,24,[0]),'AB-42-solvent-extraction':(11,22,[0]),'AB-43-precipitation':(11,31,[0]),'AB-43-salting-out-curve':(11,34,[0]),'AB-44-polymer-depletion':(11,48,[0]),'AB-44-sugar-beet':(11,46,[0]),
'AB-45-adsorption-column':(12,8,[0]),'AB-45-breakthrough':(12,10,[0]),'AB-45-freundlich-plot':(12,15,[0]),'AB-45-langmuir-plot':(12,14,[0]),'AB-46-C18-beads':(12,27,[0,1]),'AB-46-NiNTA':(12,33,[0]),'AB-46-gel-principle':(12,28,[0]),'AB-46-ion-exchange':(12,30,[0]),'AB-46-proteinA':(12,34,[0,1]),'AB-47-HPLC-FPLC':(12,40,[0,1]),'AB-47-differential-migration':(12,35,[0])}
map={}
for name,(l,p,inds) in specs.items():
 d=fitz.open(f'sources/Advanced Biotechnology/Lecture{l}.pdf'); infos=d[p-1].get_image_info(xrefs=True)
 imgs=[]
 for i in inds:
  xref=infos[i]['xref']; pix=fitz.Pixmap(d,xref)
  smask=int(d.xref_get_key(xref,'SMask')[1].split()[0]) if d.xref_get_key(xref,'SMask')[0]=='xref' else 0
  if smask: pix=fitz.Pixmap(fitz.Pixmap(pix,0) if pix.alpha else pix,fitz.Pixmap(d,smask))
  imgs.append(pix)
 path=dest/(name+'.png')
 if len(imgs)==1: imgs[0].save(path)
 else:
  width=max(i.width for i in imgs); heights=[i.height*width/i.width for i in imgs]; gap=30
  canvas=fitz.open(); pg=canvas.new_page(width=width,height=sum(heights)+gap*(len(imgs)-1));y=0
  for img,h in zip(imgs,heights):pg.insert_image(fitz.Rect(0,y,width,y+h),stream=img.tobytes('png'));y+=h+gap
  pg.get_pixmap().save(path)
 map['figs/'+name+'.png']=str(path)
for name,l,p,rect in [('AB-36-stokes-forces',10,19,(20,190,220,400)),('AB-44-isoelectric-curve',11,45,(585,40,930,400))]:
 d=fitz.open(f'sources/Advanced Biotechnology/Lecture{l}.pdf'); path=dest/(name+'.png');d[p-1].get_pixmap(matrix=fitz.Matrix(4,4),clip=fitz.Rect(*rect)).save(path);map['figs/'+name+'.png']=str(path)
(root/'figure-overrides.json').write_text(json.dumps(map,indent=2)+'\n')
# Clean annotation-only margins and retain complete panels where source bitmap itself is clipped.
def clean(name, masks=(), crop=None):
 path=dest/(name+'.png'); pix=fitz.Pixmap(path); d=fitz.open(); pg=d.new_page(width=pix.width,height=pix.height)
 pg.insert_image(pg.rect,filename=str(path))
 for rect in masks:pg.draw_rect(fitz.Rect(*rect),color=(1,1,1),fill=(1,1,1),overlay=True)
 pg.get_pixmap(clip=fitz.Rect(*crop) if crop else None).save(path)
clean('AB-32-process-logic',[(0,0,290,80),(0,440,275,555)])
clean('AB-33-rotary-drum',[(810,405,1060,450)])
clean('AB-36-stokes-forces',crop=(0,0,800,760))
clean('AB-44-isoelectric-curve',[(0,0,180,100),(0,100,155,120)])
clean('AB-39-ultrasonication',crop=(0,0,410,750))
path=dest/'AB-39-ultrasonication.png';pix=fitz.Pixmap(path);d=fitz.open();pg=d.new_page(width=pix.width,height=pix.height);pg.insert_image(pg.rect,filename=str(path))
pg.draw_rect(fitz.Rect(145,345,287,395),color=(0,254/255,254/255),fill=(0,254/255,254/255))
pg.draw_rect(fitz.Rect(289,345,410,395),color=(1,1,1),fill=(1,1,1));pg.get_pixmap().save(path)
# Complete left-hand tubes from the intrinsically truncated two ATPE diagrams.
d=fitz.open('sources/Advanced Biotechnology/Lecture11.pdf'); infos=d[24].get_image_info(xrefs=True)
canvas=fitz.open(); pg=canvas.new_page(width=625,height=455)
for x,i,rect in [(0,0,(0,0,295,445)),(320,1,(0,0,295,445))]:
 pix=fitz.Pixmap(d,infos[i]['xref']); tmp=fitz.open(); tp=tmp.new_page(width=pix.width,height=pix.height);tp.insert_image(tp.rect,stream=pix.tobytes('png'))
 pg.show_pdf_page(fitz.Rect(x,0,x+295,445),tmp,0,clip=fitz.Rect(*rect))
for rect in [(275,0,295,445),(600,0,625,445)]:pg.draw_rect(fitz.Rect(*rect),color=(1,1,1),fill=(1,1,1),overlay=True)
pg.get_pixmap(matrix=fitz.Matrix(2,2)).save(dest/'AB-42-ATPE-phases.png')
# Restore complete label intrinsically cut off in the native column bitmap.
path=dest/'AB-45-adsorption-column.png'; pix=fitz.Pixmap(path); d=fitz.open();pg=d.new_page(width=pix.width+80,height=pix.height)
pg.insert_image(fitz.Rect(0,0,pix.width,pix.height),filename=str(path));pg.draw_rect(fitz.Rect(580,390,869,460),color=(1,1,1),fill=(1,1,1));pg.draw_rect(fitz.Rect(0,890,90,972),color=(1,1,1),fill=(1,1,1));pg.insert_text((588,430),'Adsorption',fontname='tiro',fontsize=38);pg.get_pixmap().save(path)
# Contact sheets with enough resolution to read most diagrams, and filename labels.
paths=sorted(dest.glob('*.png'))
for start in range(0,len(paths),6):
 doc=fitz.open(); pg=doc.new_page(width=1600,height=2100)
 for j,path in enumerate(paths[start:start+6]):
  x=(j%2)*800;y=(j//2)*700
  pg.insert_text((x+10,y+20),path.stem,fontsize=15)
  pg.insert_image(fitz.Rect(x+15,y+30,x+785,y+680),filename=str(path))
 pg.get_pixmap().save(root/f'repaired-{start//6+1}.png')
print('Created',len(map),'replacements')
