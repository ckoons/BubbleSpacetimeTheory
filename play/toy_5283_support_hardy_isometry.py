import numpy as np
from math import gamma
rng=np.random.default_rng(2555)
print("="*90); print("THE HARDY TEST -- is the bulk->boundary map a genuine norm-preserving isometry?")
print("="*90)
print("Shilov boundary S = (S^4 x S^1)/Z_2: points z = e^{i th} x, x real on S^4.")
print("Harmonic decomposition of the bulk polynomials: Sym^d(C^5) = (+)_k Q^k H_{d-2k}, Q = sum z_j^2.\n")
def rand_shilov(N):
    th=rng.uniform(0,2*np.pi,N); x=rng.normal(size=(N,5)); x/=np.linalg.norm(x,axis=1)[:,None]
    return th,x
th,x=rand_shilov(200000); z=np.exp(1j*th)[:,None]*x
Q=(z**2).sum(axis=1)
print("(1) THE STRUCTURAL KEY: Q restricted to the Shilov boundary.")
print("    max |Q(z) - e^{2i th}| over 200000 boundary points = %.2e   => Q|_S = e^{2i th}, MODULUS 1."%np.abs(Q-np.exp(2j*th)).max())
print()
harms={1:lambda v: v[...,0],
       2:lambda v: v[...,0]*v[...,1],
       3:lambda v: v[...,0]*v[...,1]*v[...,2],
       4:lambda v: v[...,0]*v[...,1]*v[...,2]*v[...,3]}
print("(2) BOUNDARY NORM of the block Q^k H_m -- does it depend on k?")
print("      m   k      ||Q^k h||^2_{L2(S)}    ||h||^2_{L2(S^4)}    ratio")
for m in (1,2,3):
    hx=harms[m](x); base=np.mean(np.abs(hx)**2)
    for k in (0,1,2,3):
        f=(Q**k)*harms[m](z)
        nb=np.mean(np.abs(f)**2)
        print("      %d   %d       %.6f              %.6f          %.6f"%(m,k,nb,base,nb/base))
print("    => INDEPENDENT OF k, and equal to the S^4 norm: |Q|=1 on the boundary contributes nothing.")
print()
print("(3) ORTHOGONALITY: do distinct blocks land on ORTHOGONAL boundary functions?")
blocks=[(m,k) for m in (1,2,3) for k in (0,1,2)]
V=np.array([( (Q**k)*harms[m](z) ) for (m,k) in blocks])
V=V/np.sqrt(np.mean(np.abs(V)**2,axis=1))[:,None]
Gm=np.abs(V.conj()@V.T)/V.shape[1]
off=Gm-np.diag(np.diag(Gm))
print("    max off-diagonal overlap over %d blocks = %.4f   (diagonal = 1)"%(len(blocks),off.max()))
print("    => the restriction map preserves orthogonality => INJECTIVE, norm-preserving BLOCKWISE.")
print()
print("(4) ★ BUT WHICH BULK NORM?  The BERGMAN norm of the block Q^k H_m (my 5243 result):")
print("       ||Q^k h||^2_G = ||h||^2 / (2^{|lam|} (nu)_lam),  lam = (m+k, k),  (nu)_lam = (nu)_{lam1}(nu-a/2)_{lam2}, a = n_C-2 = 3")
def poch(a,n): 
    r=1.0
    for i in range(n): r*=(a+i)
    return r
nu=2.5
print("      m   k    lam       2^{|lam|}(nu)_lam    Bergman/boundary ratio")
vals=[]
for m in (1,2,3):
    for k in (0,1,2,3):
        lam=(m+k,k); fac=2**(sum(lam))*poch(nu,lam[0])*poch(nu-1.5,lam[1])
        vals.append(fac)
        print("      %d   %d   (%d,%d)      %14.4f        %.3e"%(m,k,lam[0],lam[1],fac,1/fac))
print("    spread across these blocks: %.4g  to  %.4g  =>  a factor of %.3e"%(min(vals),max(vals),max(vals)/min(vals)))
print("    ⟹ THE BERGMAN NORM DEPENDS ON k; THE BOUNDARY NORM DOES NOT. So the map")
print("       BERGMAN H^2 -> L^2(Shilov) IS **NOT** AN ISOMETRY -- it is off by 2^{|lam|}(nu)_lam,")
print("       which varies by ~7 orders over just these twelve blocks.")
print("       The isometry holds for the HARDY norm, where it is TRUE BY DEFINITION (the Hardy norm")
print("       IS the boundary L^2 norm). Those are DIFFERENT Hilbert spaces.")
print()
print("(5) ★★ AND THE MAP IS NOT ONTO -- the image is the NON-NEGATIVE-FREQUENCY half.")
print("    Q^k H_m -> e^{i(m+2k)th} h(x): the boundary frequency is n = m + 2k >= m >= 0.")
print("    Boundary L^2(S) contains e^{in th} h_m(x) for ALL n of the right parity, INCLUDING n < 0.")
N=8
img=sum(1 for m in range(N+1) for k in range(N+1) if m+2*k<=N)
tot=sum(1 for m in range(N+1) for n in range(-N,N+1) if (n-m)%2==0 and abs(n)<=N)
print("    counting modes up to cutoff %d:  holomorphic image %d   full boundary %d   fraction reached %.3f"%(N,img,tot,img/tot))
print("    ⟹ ISOMETRY *INTO*, NOT ONTO. And the missing half is exactly the NEGATIVE frequencies --")
print("       i.e. the one-sidedness IS the positive-spectrum condition = the ARROW OF TIME.")
