from pathlib import Path
import math,json,re
import pymupdf
root=Path(__file__).parent
R=1.98720425864083
nn={'AA':(-7.9,-22.2),'AT':(-7.2,-20.4),'TA':(-7.2,-21.3),'CA':(-8.5,-22.7),'GT':(-8.4,-22.4),'CT':(-7.8,-21.0),'GA':(-8.2,-22.2),'CG':(-10.6,-27.2),'GC':(-9.8,-24.4),'GG':(-8,-19.9)}
rc=lambda s:s.translate(str.maketrans('ACGT','TGCA'))[::-1]
def thermo(seq):
 h=s=0
 for a,b in zip(seq,seq[1:]):
  key=a+b
  hi,si=nn[key if key in nn else rc(key)];h+=hi;s+=si
 for b in (seq[0],seq[-1]):
  hi,si=(.1,-2.8) if b in 'GC' else (2.3,4.1);h+=hi;s+=si
 if seq==rc(seq):s-=1.4
 return h,s
def tm(h,s,c,selfcomp=False,salt=1,n=0):return 1000*h/(s+.368*n*math.log(salt)+R*math.log(c if selfcomp else c/2))-273.15
def tail(n,p):return sum(math.comb(n,k)*p**k*(1-p)**(n-k) for k in range(n//2+1,n+1))
data={}
data['01']={'contour':1000*.34,'turns':1000/10.5,'charge':-2*19}
data['02']={n:[n*.34,math.sqrt(2*50*n*.34-2*50**2*(1-math.exp(-n*.34/50)))] for n in (20,150,1000,48502)}
data['03']={'tm':[tm(-80,-220,c) for c in (1e-6,1e-4)],'K37':math.exp(-(-80000+310.15*220)/(R*310.15)), 'width':[(-80000/(-220+R*math.log(f/(1-f)**2/1e-6)))-273.15 for f in (.9,.1)]}
data['04']={'GTATTTGGCTGT':thermo('GTATTTGGCTGT'),'ATCGAT':thermo('ATCGAT')}
seq='GTATTTGGCTGTACGATCAG'
data['05']={}
for n in (5,8,12,20):
 h,s=thermo(seq[:n]);dg=h-310.15*s/1000
 data['05'][n]=[h,s,dg,*[1e5*math.exp((h*1000-T*s)/(R*T)) for T in (310.15,298.15)]]
data['07']={'yield':{p:[p**(n-1) for n in (20,60,120,200)] for p in (.994,.991)},'half':{p:1+math.log(.5)/math.log(p) for p in (.994,.991)},'P50':[.5**(1/(n-1)) for n in (200,1000)]}
p=.994;n=60
data['07']['impurities']={'full':p**59,'conditional_trunc_mean':sum(k*p**(k-1)*(1-p) for k in range(1,n))/(1-p**59),'59mer':p**58*(1-p),'one_deletion':59*(1-p)*p**58,'two_deletion':math.comb(59,2)*(1-p)**2*p**57}
h,s=thermo(seq)
data['08']={'pieces':math.ceil((1000-20)/40),'tm':[tm(h,s,.25e-6,salt=a,n=19) for a in (1,.05)],'clones':{e:[(1-e)**1000,math.ceil(math.log(.05)/math.log(1-(1-e)**1000))] for e in (1/300,1/600,1/1500)}}
data['10']={'years':8*3.1e9/700/96*2/(365.25*24),'coverage':{c:[math.exp(-c),3.1e9*math.exp(-c)] for c in (1,5,10,30)}}
data['11']={'reads':30*3.1e9/150,'genomes':2e10/(30*3.1e9/150)}
data['12']={'one_read_error':1-.999**150,'tail30':tail(30,.001)}
data['13']={'model_strict_majority_bound':{n:tail(n,.05) for n in (5,10,30)},'model_wrong_base_majority':{n:3*tail(n,.05/3) for n in (5,10,30)},'timing':[1000/450,1e5/450,10/450]}
data['14']={'one_molecule_conc':1/(6.02214076e23*2e-20),'strict_majority_bound':{n:tail(n,.12) for n in (1,3,5,10)},'wrong_base_majority':{n:3*tail(n,.12/3) for n in (1,3,5,10)}}
p=46.7/3100;dp=.05*p
data['15']={'p':p,'pprime':p+dp,'N5':p*(1-p)*(5/dp)**2,'sigma_z':{n:[math.sqrt(p*(1-p)/n),dp/math.sqrt(p*(1-p)/n)] for n in (1e5,1e6,5e6)}}
data['16']={'Ct':{n:math.log2(1e10/n) for n in (1e6,1e3,10,1)},'E':{m:10**(-1/m)-1 for m in (-3.1,-3.32,-3.6,-3.92)}}
data['17']={'fold':2**3.3,'fold90':1.9**3.3,'overestimate':2**3.3/1.9**3.3-1,'uncertainty':[2**3,2**3.6]}
data['18']={'fold_Ct20_35':2**15}
data['19']={'moles':1e15/6.02214076e23,'space':{n:[4**n,1e15/4**n] for n in (20,30,40,80)},'enrichment':{r:1e-10*10**r/(1-1e-10+1e-10*10**r) for r in (0,3,6,9,12,15)}}
data['20']={'DG20':-87.2+293.15*.2403,'ratio':math.exp(13.9/.58),'space':4**12}
data['21']={'staples':7249/32,'mass':7249*2*330,'square_bp':40*100/.34,'square_side':math.sqrt(7249*.34*2.5)}
data['22']={'rates':{n:[3e6*math.exp(-1.5*n/.592),3e6/(1+3e6*math.exp(-1.5*n/.592))] for n in (0,2,4,6,8)},'cross':.592*math.log(3e6)/1.5,'times':[math.log(2)/(1*1e-7),math.log(2)/(1.7e6*1e-7)]}
data['23']={'configs':3**198,'years':3**198*1e-13/(365.25*24*3600),'stability_kBT':[v/(8.314462618*310) for v in (2e4,4e4)]}
data['24']={'Bragg_angles':[math.degrees(math.asin(1.54/(2*d))) for d in (2,.8)]}
data['27']={'affinity_DG':R*310.15*math.log(1e4)/1000}
data['28']={'k':math.log(5)/45,'half':math.log(2)/(math.log(5)/45)}
data['30']={'space':20**200,'fraction':1e9/20**200}
(root/'numerical-evidence.json').write_text(json.dumps(data,indent=2))
text=Path('notes/advanced-biotechnology/complete-obsidian.md').read_text().split('## 10.')[0]
figs=list(dict.fromkeys(re.findall(r'!\[[^\]]*\]\(([^)]+)\)',text)))
manifest=[]
for start in range(0,len(figs),8):
 doc=pymupdf.open();page=doc.new_page(width=1600,height=1600)
 for i,f in enumerate(figs[start:start+8]):
  path=Path('notes/advanced-biotechnology')/f
  x=(i%2)*800;y=(i//2)*400
  page.insert_text((x+10,y+18),path.name,fontsize=11)
  pix=pymupdf.Pixmap(str(path));manifest.append({'path':str(path),'width':pix.width,'height':pix.height})
  page.insert_image(pymupdf.Rect(x+10,y+26,x+790,y+390),filename=str(path),keep_proportion=True)
 page.get_pixmap().save(root/f'figures-{start//8+1:02d}.png')
(root/'figures.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps(data,indent=2));print('FIGURES',len(figs))
