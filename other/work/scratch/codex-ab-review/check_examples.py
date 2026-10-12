from pathlib import Path
import math,json,re,hashlib
base=Path("out/work/scratch/codex-ab-review");base.mkdir(parents=True,exist_ok=True)
out={}
G=270*2*(3e-4)**2*35000**0.5/(3e-5)**2
out["AB34"]={"group":G,"areas_m2":{str(p):math.sqrt(G*.5**2/(2*3600))*p**(-.25) for p in [70000,35000]},"halving_pressure_ratios":[2**((1-s)/2) for s in [0,.5,.8,1]]}
r1,r2,h=.0165,.0222,.115; w=2*math.pi*10000/60;g=9.81
b=(.7e-6)**2*330/(18*.001);vc=math.pi*(r2*r2-r1*r1)*h
tc=math.log(2*r2/(r1+r2))/(b*w*w);ug=b*g
q=vc/tc;sg=q/(2*ug);sg7=math.pi*w*w*h*(3*r2*r2+r1*r1)/(2*g)
fulltc=math.log(r2/r1)/(b*w*w)
out["AB36_37"]={"omega_rad_s":w,"acceleration":r2*w*w,"G":r2*w*w/g,"t_mid_s":tc,"volume_m3":vc,"Q_mid_m3_s":q,"Q_mid_L_min":q*60000,"u_gravity_m_s":ug,"Sigma_m2":sg,"gravity_area_m2":2*sg,"alternative_Sigma_m2":sg7,"ratio_alternative":sg7/sg,"doubled_speed_rpm":10000/math.sqrt(8),"t_full_s":fulltc,"Q_full_L_min":vc/fulltc*60000,"capture_fraction_uniform_cross_section_at_mid_Q":(r2*r2-((r1+r2)/2)**2)/(r2*r2-r1*r1),"gravity_1um_days":.1/((1e-6)**2*300*g/(18*.001))/86400}
data=[[5,13.5,23.3,36,42],[9.5,23.5,40,58.5,66],[14,33.5,52.5,75,83.7],[18,43,66.6,82.5,88.5],[22,47.5,73,88.5,94.5],[26,55,79.5,91.3,None]]
ps=[200,300,400,500,550]
sl=[]
for j in range(5):
    pairs=[(i+1,-math.log1p(-row[j]/100)) for i,row in enumerate(data) if row[j] is not None]
    sl.append(sum(n*y for n,y in pairs)/sum(n*n for n,y in pairs))
xs=list(map(math.log,ps));ys=list(map(math.log,sl));xm=sum(xs)/5;ym=sum(ys)/5
a=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/sum((x-xm)**2 for x in xs); intercept=ym-a*xm;k=math.exp(intercept)
r2fit=1-sum((y-intercept-a*x)**2 for x,y in zip(xs,ys))/sum((y-ym)**2 for y in ys)
out["AB40"]={"slopes":sl,"a":a,"k":k,"R2":r2fit,"N_80_at_460":math.log(5)/(k*460**a),"p_70_two_passes":(math.log(1/.3)/(2*k))**(1/a),"release_550_5":100*(-math.expm1(-k*5*550**a)),"release_200_6":100*(-math.expm1(-k*6*200**a)),"doubling_p_factor":2**a,"N_using_printed_constants":math.log(5)/(1.73e-7*460**2.37),"p_using_printed_constants":(math.log(1/.3)/(2*1.73e-7))**(1/2.37)}
out["AB42"]=[{"volume_ratio":r,"yield":4.2*r/(1+4.2*r),"Cu_over_C0_total_mixture":4.2*(1+r)/(1+4.2*r),"Cu_if_same_total_mass_and_Vlower_1":4.2/(1+4.2*r)} for r in [5,.5]]
ks=math.log(770/29)/1.6;beta=math.log(770)+ks*1.4;s=math.exp(beta-ks*2.5)
out["AB43"]={"Ks":ks,"beta":beta,"S_2_5_ug_ml":s,"precipitated_fraction":1-s/180,"salt_for_target_M":{str(y):(beta-math.log(180*(1-y)))/ks for y in [.9,.95,.99]}}
out["AB45"]=[{"recovery":y,"C_final_mol_L":8e-5*(1-y),"q_mol_cm3":5.5e-5*(8e-5*(1-y))**.35,"resin_m3":y*8e-5*2000/(5.5e-5*(8e-5*(1-y))**.35)/1e6} for y in [.9,.95,.99]]
vi=7.5*1.05/(1+7.5)*70
out["AB47"]={"Vi_ml":vi,"Vs_ml":70-vi,"rows":[{"Kp":kp,"Ve_ml":30+kp*vi,"k":kp*vi/30} for kp in [0,.2,.5,1]],"delta":.2/.5,"peak_separation_ml":.3*vi,"alpha":.5/.2}
notes=sorted(p for p in Path("out/AB").glob("AB-*.md") if 31<=int(p.name[3:5])<=47)
out["files"]=[{"path":str(p),"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"image_links":re.findall(r"!\[[^\]]*\]\(([^)]+)\)",p.read_text()),"source_ref_matches":re.findall(r"(?i)\b(?:lecture PDF|slides?|lecturer)\b",p.read_text())} for p in notes]
(base/"results.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({k:v for k,v in out.items() if k!="files"},indent=2))
import pymupdf
images=sorted({p.parent/link for p in notes for link in re.findall(r"!\[[^\]]*\]\(([^)]+)\)",p.read_text())})
checks=[]
for p in images:
    pix=pymupdf.Pixmap(str(p));checks.append({"path":str(p),"width":pix.width,"height":pix.height})
(base/"figure-checks.json").write_text(json.dumps(checks,indent=2)+"\n")
for start in range(0,len(images),8):
    d=pymupdf.open();page=d.new_page(width=1200,height=1600)
    for i,p in enumerate(images[start:start+8]):
        x=(i%2)*600;y=(i//2)*400
        page.insert_text((x+10,y+18),p.name,fontsize=9)
        page.insert_image(pymupdf.Rect(x+8,y+25,x+592,y+395),filename=str(p),keep_proportion=True)
    page.get_pixmap().save(str(base/f"figures-{start//8+1}.png"))
for name,pages in [("Lecture10",[27,28,30,31,32,33,34,35,36,37,38]),("Lecture12",[36,37,38,39])]:
    d=pymupdf.open("sources/Advanced Biotech/"+name+".pdf")
    for n in pages:
        d[n-1].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).save(str(base/f"{name}-p{n}.png"))
print("Figure links decoded:",len(images))
