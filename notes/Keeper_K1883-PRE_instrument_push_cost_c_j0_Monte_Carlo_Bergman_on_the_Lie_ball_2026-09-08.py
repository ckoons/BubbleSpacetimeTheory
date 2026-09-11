import numpy as np
rng=np.random.default_rng(5)
def ball_uniform(n):
    # uniform in the unit ball of C^5 = R^10
    g=rng.normal(size=(n,10)); g/=np.linalg.norm(g,axis=1)[:,None]
    r=rng.uniform(size=n)**(1/10)
    x=g*r[:,None]; return x[:,:5]+1j*x[:,5:]
acc=[]
while sum(len(a) for a in acc)<400000:
    z=ball_uniform(2000000)
    zz=np.sum(z*z,axis=1); n2=np.sum(np.abs(z)**2,axis=1)
    m=(np.abs(zz)<1)&(1-2*n2+np.abs(zz)**2>0)
    acc.append(z[m])
z=np.concatenate(acc); zz=np.sum(z*z,axis=1); n2=np.sum(np.abs(z)**2,axis=1)
print("accepted",len(z),"acceptance ~",len(z)/(2000000*len(acc)),"(expect 1/16 = 0.0625)")
print(" j   c(j,0) MC     5/(2(j+5))   Lyra")
lyra={0:0.5,1:5/12,2:5/14}
for j in range(0,7):
    w=np.abs(zz)**(2*j)
    c=1-np.sum(w*n2)/np.sum(w)
    print("%2d   %.4f       %.4f     %s"%(j,c,5/(2*(j+5)),("%.4f"%lyra[j]) if j in lyra else ""))
