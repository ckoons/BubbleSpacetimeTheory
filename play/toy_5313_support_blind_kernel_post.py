import numpy as np
from math import factorial, exp, sqrt
print("="*92)
print("TRACK 1 -- K1002 BLIND POST, BEFORE ANY COMPARISON")
print("="*92)
print("  ENTRY FORM (Lyra, this round):  V_ij  proportional to  c_{k_i-1}^{(j)} + c_{k_i+1}^{(j)}")
print("     down (odd, FK ladder)  k_i in {1,3,5}   for i = d, s, b")
print("     up   (even, COHERENT)  profile c^{(j)}  for j = u, c, t")
print("     J_W = degree-1 (T1929) -> Wigner-Eckart forces k <-> k+-1.")
print("  KERNEL: c_k^{(j)} = the COHERENT-STATE radial profile, c_k = e^{-|z|^2/2} z^k / sqrt(k!),")
print("     ONE parameter per generation (the coherent location |z_j|^2 = the peak).")
print("  PROVENANCE: standard coherent state; the ONLY additional input is the SHELF ALIGNMENT")
print("     ('up gen-j one degree below down gen-j'), i.e. peak_j = 2(j-1).")
print("  Posted before any comparison, per K1002.")
print()
print("="*92)
print("THE TWO PRE-REGISTERED CHECKS -- and FIRST, can they fail?")
print("="*92)
def cvec(peak,K=9):
    z=sqrt(peak) if peak>0 else 1e-9
    c=np.array([exp(-z*z/2)*z**k/sqrt(factorial(k)) for k in range(K)])
    return c/np.linalg.norm(c)
def Vmat(peaks,K=9):
    down=[1,3,5]; V=np.zeros((3,3))
    for i,ki in enumerate(down):
        for j,p in enumerate(peaks):
            c=cvec(p,K)
            V[i,j]=c[ki-1]+(c[ki+1] if ki+1<K else 0.0)
    return V
print("\n  FIRE with the shelf alignment peaks = (0, 2, 4):")
V=Vmat([0,2,4]); Vn=np.abs(V)/np.abs(V).max()
print("       (rows d,s,b ; cols u,c,t), normalised")
for r,lab in zip(Vn,["d","s","b"]):
    print("        %s : %s"%(lab,"  ".join("%.4f"%x for x in r)))
diag_ok=all(Vn[i,i]>=Vn[:,i].max()-1e-12 for i in range(3)) and all(Vn[i,i]>=Vn[i,:].max()-1e-12 for i in range(3))
corner=Vn[2,0]; others=[Vn[i,j] for i in range(3) for j in range(3) if (i,j)!=(2,0)]
print("\n     CHECK 1 -- does the diagonal PEAK (row- and column-dominant)?  %s"%diag_ok)
print("     CHECK 2 -- is the 1-3 corner (b<-u, gap 5) uniquely smallest? %s  (%.2e vs next %.2e)"%(
    corner<min(others), corner, min(others)))
print()
print("="*92)
print("★★★ BUT NOW THE S2 QUESTION I AM HERE TO ASK: CAN EITHER CHECK FAIL?")
print("="*92)
rng=np.random.default_rng(1177)
passes=0; trials=0; fails=[]
for _ in range(4000):
    peaks=np.sort(rng.uniform(0,8,3))          # ANY increasing peak assignment
    Vr=np.abs(Vmat(peaks)); Vr/=Vr.max()
    trials+=1
    d_ok=all(Vr[i,i]>=Vr[:,i].max()-1e-12 for i in range(3)) and all(Vr[i,i]>=Vr[i,:].max()-1e-12 for i in range(3))
    c_ok=Vr[2,0]<min(Vr[i,j] for i in range(3) for j in range(3) if (i,j)!=(2,0))
    if d_ok and c_ok: passes+=1
    elif len(fails)<3: fails.append((peaks.round(2),d_ok,c_ok))
print("  scan over 4000 RANDOM increasing peak-triples (0..8), same entry form:")
print("     both checks pass in %d/%d = %.1f%% of cases"%(passes,trials,100*passes/trials))
print("  and with the ALIGNMENT DROPPED entirely (all three up states at the SAME peak):")
for p in [1.0,3.0,5.0]:
    Vr=np.abs(Vmat([p,p,p])); Vr/=Vr.max()
    d_ok=all(Vr[i,i]>=Vr[:,i].max()-1e-12 for i in range(3))
    print("     peaks = (%.0f,%.0f,%.0f) -> diagonal-dominant? %s"%(p,p,p,d_ok))
print()
print("  ⟹ ★★★★ THE CHECKS ARE CARRIED BY THE SHELF ALIGNMENT, NOT BY D_IV^5.")
print("     Any increasing peak-triple reproduces the pattern; identical peaks destroy it.")
print("     'peak_j = 2(j-1)' IS diagonal-dominance, restated. Keeper worried the degree-1 bridge")
print("     smuggled it -- it is the ALIGNMENT that does. The Wigner-Eckart step is innocent;")
print("     the alignment is the premise.")
print()
print("  ⟹ SO THE FIRE, AS SPECIFIED, IS CONSTRUCTION-GUARANTEED ON BOTH CHECKS. It cannot fail,")
print("     and by the standing rule a test that cannot fail proves nothing. THE FIRE DOES NOT BANK")
print("     THE CKM SHAPE.")
print()
print("  ★ WHAT WOULD MAKE IT A REAL TEST -- one sentence, and it is @Lyra's to supply:")
print("    DERIVE the peak locations |z_j|^2 from the up-sector saturation (the labeled input), so")
print("    the alignment is an OUTPUT. Then diagonal-dominance is a prediction. As it stands the")
print("    alignment is assumed and the dominance follows trivially.")
