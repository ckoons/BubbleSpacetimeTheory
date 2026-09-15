import numpy as np
b=369.82; sc=0.11; rng=np.random.default_rng(1)
bc=np.array([0,0,b])  # direction irrelevant under isotropic sigma
def frac(sig,truth,n=200000):
    x=truth+rng.normal(size=(n,3))*sig; v=sig**2+sc**2
    c2c=((x-bc)**2).sum(1)/v; c20=(x**2).sum(1)/v; d=c20-c2c
    A14=c2c<=7.815; B14=(c2c>=14.156)|((c20<=7.815)&(sig<b/2)); C14=~A14&~B14
    A15=(c2c<=7.815)&(d>=3.84); Adec=A15&(c20>=7.815); B15=c2c>=14.156; C15=~A15&~B15
    return dict(v14_A=A14.mean(),v14_B=B14.mean(),v14_C=C14.mean(),v15_A=A15.mean(),v15_Adec=Adec.mean(),v15_B=B15.mean(),v15_C=C15.mean())
print("chi2_3(b_CMB,0) at 166 =",round(b**2/(166**2+sc**2),3))
for sig in (166,132,100,98.3):
    print(sig,"P1 true ",{k:round(v,3) for k,v in frac(sig,bc).items()})
    print(sig,"no boost",{k:round(v,3) for k,v in frac(sig,0*bc).items()})
print("bars: decisive-A", round(b/7.815**0.5,2), " B-from-null", round(b/14.156**0.5,2))
