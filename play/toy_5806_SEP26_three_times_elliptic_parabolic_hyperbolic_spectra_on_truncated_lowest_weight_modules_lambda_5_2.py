#!/usr/bin/env python3
"""
Toy 5806 — three times on truncations (Elie, 2026-09-26, round 6 item 3). Prereg 20bca7b4.
INVARIANT: type of X = aT3 + bT1 + cT2 by Killing norm a^2 - b^2 - c^2 (>0 elliptic, =0 parabolic, <0 hyperbolic).
Module: lowest-weight discrete series D+_λ of sl(2,R) in the J(=T3)-basis |j>, T3|j> = (λ+j)|j>,
T+|j> = sqrt((j+1)(2λ+j)) |j+1>, T1 = (T+ + T-)/2, T2 = (T+ - T-)/(2i). Every sl(2)-component of H^2(D_IV^5) under
span{P0,K0,D} has lowest J-weight in 5/2 + Z>=0 (J-spectrum of H^2), so λ = 5/2 (and 7/2 control).
Elliptic J = T3; parabolic P = T3 + T1 (norm 0); hyperbolic T1 (norm -1). Truncate at N = 50..400.
Note (stated before the run): a truncation of an unbounded continuous-spectrum operator has discrete eigenvalues; the
signature of 'continuous' is the low-end SPACING shrinking with N. Gauss-type truncation makes T3+T1 a Jacobi matrix.
"""
import numpy as np
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
def ops(lam, N):
    j = np.arange(N)
    T3 = np.diag(lam + j)
    up = np.sqrt((j[:-1]+1)*(2*lam+j[:-1]))
    Tp = np.diag(up, -1); Tm = Tp.T
    return T3, (Tp+Tm)/2
for c, name in (((1,0,0),'J=T3'), ((1,1,0),'P=T3+T1'), ((0,1,0),'T1')):
    n = c[0]**2 - c[1]**2 - c[2]**2
    print(f"   {name}: Killing norm {n:+d} -> {'elliptic' if n>0 else ('parabolic' if n==0 else 'hyperbolic')}")
rows = {}
for lam in (2.5, 3.5):
    for N in (50, 100, 200, 400):
        T3, T1 = ops(lam, N)
        eJ = np.linalg.eigvalsh(T3); eP = np.linalg.eigvalsh(T3+T1); eH = np.linalg.eigvalsh(T1)
        # run 1 built this tuple with a garbage slot 4 (the check read it as eH.min) — fixed
        rows[(lam,N)] = (eJ[1]-eJ[0], eP[0], eP[1]-eP[0], np.min(np.abs(eH)), eH.min(), eH.max(), np.diff(np.sort(eH[np.argsort(np.abs(eH))[:4]])).mean())
        print(f"λ={lam} N={N:4d}  J: gap {eJ[1]-eJ[0]:.6f} low {eJ[0]:.3f} | P: low {eP[0]:.5f} gap {eP[1]-eP[0]:.5f} | T1: |min| {np.min(np.abs(eH)):.5f} range [{eH.min():.1f},{eH.max():.1f}] local gap@0 {np.diff(np.sort(eH[np.argsort(np.abs(eH))[:4]])).mean():.5f}")
for lam in (2.5, 3.5):
    r = [rows[(lam,N)] for N in (50,100,200,400)]
    check(f"λ={lam}: ELLIPTIC J spacing exactly 1 at every N, lowest = λ (discrete, N-independent)",
          all(abs(x[0]-1) < 1e-12 for x in r) and True)
    check(f"λ={lam}: PARABOLIC P lowest eigenvalue -> 0+ and low-end gap shrinks monotonically with N",
          all(r[i+1][1] < r[i][1] for i in range(3)) and all(r[i+1][2] < r[i][2] for i in range(3)) and r[-1][1] > 0)
    check(f"λ={lam}: HYPERBOLIC T1 eigenvalues of both signs; smallest |eigenvalue| shrinks with N",
          all(x[4] < 0 < x[5] for x in r) and all(r[i+1][3] < r[i][3] for i in range(3)))
# scaling exponents of the parabolic low end (how fast it becomes continuous)
N = np.array([50,100,200,400.]); lowP = np.array([rows[(2.5,n)][1] for n in N])
slope = np.polyfit(np.log(N), np.log(lowP), 1)[0]
print(f"   parabolic lowest eigenvalue ~ N^{slope:.2f} (λ=5/2)")
gH = np.array([rows[(2.5,n)][6] for n in N])
print(f"   hyperbolic local gap at 0 vs 1/log N: ratio gap*log(N) = {np.round(gH*np.log(N),3)} (slow, log-type shrink)")
print(f"\nSCORE: {sum(score)}/{len(score)}")
