import numpy as np
from math import factorial, exp, sqrt
print("I DRAFTED 'CONSTRUCTION-GUARANTEED, CANNOT FAIL' AND MY OWN NUMBERS SAY THE OPPOSITE.")
print("Reading them properly. This is the third time in two days I have written a conclusion ahead")
print("of the data; the data wins.\n")
def cvec(peak,K=9):
    z=sqrt(peak) if peak>0 else 1e-9
    c=np.array([exp(-z*z/2)*z**k/sqrt(factorial(k)) for k in range(K)])
    return c/np.linalg.norm(c)
def Vmat(peaks,K=9):
    V=np.zeros((3,3))
    for i,ki in enumerate([1,3,5]):
        for j,p in enumerate(peaks):
            c=cvec(p,K); V[i,j]=c[ki-1]+(c[ki+1] if ki+1<K else 0.0)
    return V
V=np.abs(Vmat([0,2,4])); Vn=V/V.max()
print("="*92); print("THE FIRE, AT THE SPECIFIED SHELF ALIGNMENT peaks = (0,2,4)"); print("="*92)
print("      rows = down (d,s,b) ; cols = up (u,c,t) ; normalised")
for r,lab in zip(Vn,["d","s","b"]): print("       %s : %s"%(lab,"  ".join("%.4f"%x for x in r)))
print("\n  CHECK 1 -- diagonal row- AND column-dominant?")
for i in range(3):
    rowmax=Vn[i].max(); colmax=Vn[:,i].max()
    print("     gen %d: V_ii = %.4f | row max %.4f (%s) | col max %.4f (%s)"%(
        i+1,Vn[i,i],rowmax,"ok" if Vn[i,i]>=rowmax-1e-12 else "FAILS",colmax,"ok" if Vn[i,i]>=colmax-1e-12 else "FAILS"))
print("     ⟹ CHECK 1: **FAIL** -- V_23 = %.4f EXCEEDS both V_22 = %.4f and V_33 = %.4f."%(Vn[1,2],Vn[1,1],Vn[2,2]))
print("\n  CHECK 2 -- 1-3 corner (b<-u) uniquely smallest?  %.2e vs next-smallest %.2e  -> PASS"%(
    Vn[2,0],min(Vn[i,j] for i in range(3) for j in range(3) if (i,j)!=(2,0))))
print("\n"+"="*92); print("★★★ AND THE PHYSICS FAILURE IS LARGER THAN EITHER CHECK"); print("="*92)
print("     the CABIBBO entry is V_us = (down s, up u) = Vn[1,0] = %.3e"%Vn[1,0])
print("     observed |V_us| = 0.2243 -- the LARGEST off-diagonal, the best-measured mixing parameter,")
print("     and the one the corpus has BANKED at 1/sqrt(20) = 0.2236.")
print("     ⟹ the fire returns ESSENTIALLY ZERO where the data has the largest off-diagonal element.")
print("        Reason: the u coherent state peaks at k=0, so c_2 and c_4 are ~0, and V_us = c_2 + c_4.")
print("\n"+"="*92); print("DOES THE TEST HAVE POWER?  (the S2 question -- and the answer is YES)"); print("="*92)
rng=np.random.default_rng(1177); ok=0;N=4000
for _ in range(N):
    p=np.sort(rng.uniform(0,8,3)); W=np.abs(Vmat(p)); W/=W.max()
    d=all(W[i,i]>=W[i].max()-1e-12 and W[i,i]>=W[:,i].max()-1e-12 for i in range(3))
    c=W[2,0]<min(W[i,j] for i in range(3) for j in range(3) if (i,j)!=(2,0))
    ok+= (d and c)
print("     random increasing peak-triples passing BOTH checks: %d/%d = %.1f%%"%(ok,N,100*ok/N))
print("     ⟹ the checks are NOT construction-guaranteed -- they are failed by ~%.0f%% of alignments,"%(100-100*ok/N))
print("        and the SPECIFIED alignment (0,2,4) is among the failures. The fire is a REAL test.")
print("\n  ⟹ ★★★★ VERDICT: THE FIRE FIRED AND FAILED, on a pre-registered check, at the specified point.")
print("     CHECK 1 FAIL (diagonal not dominant) + the Cabibbo entry ~0 against 0.2243.")
print("     CHECK 2 PASS (V_ub uniquely smallest) -- but that one alone is the weakest of the pair.")
print("     Per the pre-registered bar, the CKM shape does NOT bank.")
