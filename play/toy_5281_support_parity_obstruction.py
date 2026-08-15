import numpy as np
rng=np.random.default_rng(1560)
print("MY RANDOM SEARCH WAS A BAD INSTRUMENT -- it failed to find C conj(C) = -I even at n=2 and 4,")
print("where solutions DO exist. Random sampling of U(n) is not an optimiser. Replaced with the exact")
print("determinant obstruction (verified numerically) plus explicit constructions.\n")
print("THE OBSTRUCTION: for ANY unitary C, det(C conj(C)) = det(C) conj(det C) = |det C|^2 = +1.")
print("But det(-I_n) = (-1)^n. So C conj(C) = -I needs (-1)^n = +1, i.e. n EVEN.\n")
print("   n    det(C conj(C)) over 20000 random unitaries        det(-I_n)   quaternionic J possible?")
for n in [2,3,4,5]:
    ds=[]
    for _ in range(20000):
        A=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        U,_,Vh=np.linalg.svd(A); C=U@Vh
        ds.append(np.linalg.det(C@C.conj()))
    ds=np.array(ds)
    print("  %3d    mean %+.6f%+.6fi   max|dev from 1| %.2e        %+d        %s"%(
        n,ds.real.mean(),ds.imag.mean(),np.abs(ds-1).max(),(-1)**n,"YES" if n%2==0 else "NO -- IMPOSSIBLE"))
print("\nEXPLICIT CONSTRUCTIONS for even n (the symplectic form):")
for n in [2,4]:
    k=n//2
    C=np.block([[np.zeros((k,k)),np.eye(k)],[-np.eye(k),np.zeros((k,k))]]).astype(complex)
    print("   n=%d :  ||C conj(C) + I|| = %.2e   => quaternionic structure EXISTS"%(n,np.abs(C@C.conj()+np.eye(n)).max()))
print("\nAND real structures (J^2=+1) exist in EVERY dimension -- C = I gives plain conjugation:")
for n in [2,3,4,5]:
    C=np.eye(n,dtype=complex)
    print("   n=%d :  ||C conj(C) - I|| = %.2e   => real structure EXISTS; its commutant in SU(n) is SO(%d)"%(
        n,np.abs(C@C.conj()-np.eye(n)).max(),n))
