import numpy as np
# HASHED BEFORE RUNNING:  c_nu(j, k=0) = (nu - 5/2)/(j + nu)
#   at nu=5 this is (5/2)/(j+5) = 5/(2(j+5))  [Round 130 exact line]
#   at nu=5/2 it is identically 0 for all j   [the Hardy point]
rng=np.random.default_rng(31)
acc=[]
while sum(len(a) for a in acc)<900000:
    g=rng.normal(size=(3000000,10)); g/=np.linalg.norm(g,axis=1)[:,None]
    r=rng.uniform(size=3000000)**(1/10); x=g*r[:,None]; z=x[:,:5]+1j*x[:,5:]
    zz=np.sum(z*z,axis=1); n2=np.sum(np.abs(z)**2,axis=1)
    h=1-2*n2+np.abs(zz)**2
    m=(np.abs(zz)<1)&(h>0); acc.append(np.column_stack([np.abs(zz)[m],n2[m],h[m]]))
A=np.concatenate(acc); azz,n2,h=A[:,0],A[:,1],A[:,2]
print("accepted",len(A))
print("\n nu   j |   MC c      hashed (nu-5/2)/(j+nu)   ratio")
for nu in (5.0,6.0,7.0,4.5):
    lw=(nu-5.0)*np.log(h)
    for j in (0,1,3,10):
        w=np.exp(np.clip(lw+2*j*np.log(azz+1e-300),-700,50))
        c=1-np.sum(w*n2)/np.sum(w); pred=(nu-2.5)/(j+nu)
        print(" %.1f %2d |  %.4f        %.4f            %.3f"%(nu,j,c,pred,c/pred))
