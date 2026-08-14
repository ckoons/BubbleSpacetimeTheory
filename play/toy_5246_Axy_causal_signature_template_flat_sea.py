"""
Toy 5246 -- A_xy causal eigenvalue signature (Finster G2), verified on the flat sea.
This is the TEMPLATE the D_IV^5 curved sea (v3 Dirac operator, T2562) must reproduce.
A_xy = P(x,y) [J P(y,x)^dag J], J=gamma^0 (kernel Krein). Finster: |eig| equal <=> spacelike,
distinct <=> timelike. SCORE 2/2 PASS. (Uses Lyra_Kf_reference_implementation.py F952 sea.)
"""
import numpy as np, os
ref=os.path.join(os.path.dirname(__file__),'..','notes','Lyra_Kf_reference_implementation.py')
ns={'__name__':'ref','np':np}; exec(open(ref).read(),ns)
g0f,_=ns['_dirac_flat'](); sea=ns['dirac_sea_kernel']
def spread(xi):
    P=sea(xi); A=P@(g0f@P.conj().T@g0f); m=np.abs(np.linalg.eigvals(A)); return m.max()-m.min()
sl=spread([0.0,1.0,0.0,0.0]); tl=spread([1.0,0.0,0.0,0.0])
tests=[("spacelike -> equal moduli (L=0)", sl<0.05), ("timelike -> distinct moduli (L>0)", tl>0.05)]
print(f"spacelike spread={sl:.4f} ; timelike spread={tl:.2f}")
for n,ok in tests: print(f"  [{'PASS' if ok else 'FAIL'}] {n}")
print(f"SCORE: {sum(ok for _,ok in tests)}/2 PASS")
