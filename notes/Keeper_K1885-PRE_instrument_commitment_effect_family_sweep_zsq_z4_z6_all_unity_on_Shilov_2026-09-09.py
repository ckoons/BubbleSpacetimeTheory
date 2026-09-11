import numpy as np
rng=np.random.default_rng(17)
acc=[]
while sum(len(a) for a in acc)<400000:
    g=rng.normal(size=(2000000,10)); g/=np.linalg.norm(g,axis=1)[:,None]
    r=rng.uniform(size=2000000)**(1/10); x=g*r[:,None]; z=x[:,:5]+1j*x[:,5:]
    zz=np.sum(z*z,axis=1); n2=np.sum(np.abs(z)**2,axis=1)
    m=(np.abs(zz)<1)&(1-2*n2+np.abs(zz)**2>0); acc.append(z[m])
z=np.concatenate(acc); zz=np.sum(z*z,axis=1); n2=np.sum(np.abs(z)**2,axis=1)
print("accepted",len(z))
print(" On the Shilov boundary z=e^{it}x, x in S^4 real: |z|^2 =",
      float(np.abs(np.exp(1j*0.7)*np.array([.3,.4,.5,.5,.5]))@np.abs(np.exp(1j*0.7)*np.array([.3,.4,.5,.5,.5]))))
print("\n j  k |  c1=1-<|z|^2>   c2=1-<|z|^4>   c3=1-<|z|^6>   (all three effects =1 on S-hat)")
for (j,k) in [(0,0),(1,0),(2,0),(3,0)]:
    w=np.abs(zz)**(2*j)
    c1=1-np.sum(w*n2)/np.sum(w); c2=1-np.sum(w*n2**2)/np.sum(w); c3=1-np.sum(w*n2**3)/np.sum(w)
    print("%2d %2d |   %.4f        %.4f        %.4f"%(j,k,c1,c2,c3))
print("\n exact k=0 line for c1 is 5/(2(j+5)):", [round(5/(2*(j+5)),4) for j in range(4)])
