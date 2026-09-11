import numpy as np
rng=np.random.default_rng(23)
acc=[]
while sum(len(a) for a in acc)<600000:
    g=rng.normal(size=(2500000,10)); g/=np.linalg.norm(g,axis=1)[:,None]
    r=rng.uniform(size=2500000)**(1/10); x=g*r[:,None]; z=x[:,:5]+1j*x[:,5:]
    zz=np.sum(z*z,axis=1); n2=np.sum(np.abs(z)**2,axis=1)
    m=(np.abs(zz)<1)&(1-2*n2+np.abs(zz)**2>0); acc.append(z[m])
z=np.concatenate(acc); zz=np.abs(np.sum(z*z,axis=1)); n2=np.sum(np.abs(z)**2,axis=1)
print("accepted",len(z),"  max |z|^2 in sample = %.4f (effect must be <=1)"%n2.max())
print("\n  j |   n=1      n=2      n=3      n=5   |  j*c(n=1)  j*c(n=2)  j*c(n=3)")
lw=2*np.log(zz+1e-300)
for j in [0,1,2,4,8,16,32,64]:
    w=np.exp(np.clip(j*lw,-700,0)); W=w.sum()
    cs=[1-np.sum(w*n2**n)/W for n in (1,2,3,5)]
    print("%3d | %7.4f %8.4f %8.4f %8.4f  | %8.3f %9.3f %9.3f"%(j,cs[0],cs[1],cs[2],cs[3],j*cs[0],j*cs[1],j*cs[2]))
