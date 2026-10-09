import numpy as np
r1,r2,h=0.0165,0.0222,0.115; w=2*np.pi*10000/60; g=9.81
Dp,rp,rl,mu=0.7e-6,1340,1010,1e-3
L=np.log(2*r2/(r1+r2))
tcut=18*mu/(Dp**2*(rp-rl)*w**2)*L; Vc=np.pi*(r2**2-r1**2)*h
print('ac/g',r2*w**2/g,'tcut',tcut,'Vc',Vc,'Q',Vc/tcut)
S=np.pi*(r2**2-r1**2)*h*w**2/(2*g*L); S7=np.pi*w**2*h*(3*r2**2+r1**2)/(2*g)
ug=Dp**2*(rp-rl)*g/(18*mu); print('Sigma',S,S7,S7/S,'2Sug',2*S*ug, ug)
d=np.array([[5,13.5,23.3,36,42],[9.5,23.5,40,58.5,66],[14,33.5,52.5,75,83.7],[18,43,66.6,82.5,88.5],[22,47.5,73,88.5,94.5],[26,55,79.5,91.3,np.nan]])
p=np.array([200,300,400,500,550.]);sl=[]
for j in range(5):
  y=-np.log(1-d[:,j]/100);N=np.arange(1,7);m=~np.isnan(y);sl.append((N[m]@y[m])/(N[m]@N[m]))
sl=np.array(sl);print(sl);a,b=np.polyfit(np.log(p),np.log(sl),1);k=np.exp(b);print(a,k)
print('N',np.log(5)/(k*460**a),'p',(np.log(1/0.3)/(2*k))**(1/a))
Ks=np.log(770/29)/1.6;bs=np.log(770)+Ks*1.4;print(Ks,bs,np.exp(bs-Ks*2.5),(bs-np.log(1.8))/Ks)
print(5.5e-5*(8e-6)**0.35,0.144/(5.5e-5*(8e-6)**0.35))
Vi=7.5*1.05/(8.5)*70;print(Vi,0.2*Vi/30,0.5*Vi/30,(0.2/0.5))
