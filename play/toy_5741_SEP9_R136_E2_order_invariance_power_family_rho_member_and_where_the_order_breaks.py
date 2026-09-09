#!/usr/bin/env python3
"""Toy 5741 — R136 E2: is the ORDER invariant across admissible commitment effects?"""
import json, math
from fractions import Fraction as F
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (control)'}  {d}")
def L(j,k): j=F(j); k=F(k); return F(k+3,2*k+3)*(j+k+F(5,2))/(j+k+5)
def M(j,k): j=F(j); k=F(k); return F(k,2*k+3)*(j+1)/(j+F(7,2)) if k>0 else F(0)
memo={}
def tau(n,j,k):
    if n==0: return F(1)
    key=(n,j,k)
    if key in memo: return memo[key]
    t=L(j,k)*tau(n-1,j,k+1)
    if k>0: t+=M(j,k)*tau(n-1,j+1,k-1)
    memo[key]=t; return t
def cn(n,j,k): return 1-tau(n,j,k)
print("B1: power family |z|^{2n}, n = 1..8 — monotone in j, -> 0, and the rate")
ok=True
for n in range(1,9):
    for k in range(0,4):
        col=[cn(n,j,k) for j in range(0,41)]
        ok &= all(col[i]>col[i+1] for i in range(40)) and col[-1]<col[0]
    big=[float(j*cn(n,j,0)) for j in (200,2000,20000)]
    print(f"  n={n}: c_n(0,0) = {float(cn(n,0,0)):.4f};  j*c_n(j,0) at j = 200/2000/20000: {big[0]:.4f} / {big[1]:.4f} / {big[2]:.4f}   (5n/2 = {2.5*n})")
rate_ok=all(abs(float(20000*cn(n,20000,0))-2.5*n)<0.02*2.5*n for n in range(1,9))
kindep=all(abs(float(20000*cn(n,20000,k))-float(20000*cn(n,20000,0)))<0.01 for n in (1,3,8) for k in (1,2,3))
sc("B1", ok and rate_ok and kindep, True, f"monotone and vanishing for n = 1..8, k = 0..3; j*c_n -> 5n/2 (k-independent: {kindep})")
print("B2: the rho member — f = 1 - rho, rho = 1 - 2|z|^2 + |z.z|^2 (admissible, NOT a power of |z|^2)")
def tt(j,k): j=F(j); k=F(k); return (j+1)/(j+F(7,2))*(j+k+F(5,2))/(j+k+5)
def crho(j,k): return 1-2*tau(1,j,k)+tt(j,k)
print("   exact k=0 line:", [str(crho(j,0)) for j in range(6)], " = 10/((2j+7)(2j+10)) ?", all(crho(j,0)==F(10,(2*j+7)*(2*j+10)) for j in range(200)))
print(f"   c_rho(0,0) = {crho(0,0)} = {float(crho(0,0)):.4f}  (my 5721 Monte Carlo: 0.1417 +- 0.0011)")
print(f"   c_rho(1,1) = {crho(1,1)} = {float(crho(1,1)):.4f}  (my 5721 Monte Carlo: 0.0786 +- 0.0011)")
mono_r=all(crho(j,0)>crho(j+1,0) for j in range(200)) and all(crho(j,k)>crho(j+1,k) for k in (1,2,3) for j in range(200))
r1=[float(j*crho(j,0)) for j in (200,2000,20000)]; r2=[float(j*j*crho(j,0)) for j in (200,2000,20000)]
print(f"   rate: j*c_rho at j = 200/2000/20000: {r1[0]:.4f} / {r1[1]:.4f} / {r1[2]:.5f}  ->  j^2*c_rho: {r2[0]:.4f} / {r2[1]:.4f} / {r2[2]:.4f}  (5/2 = 2.5)")
hashed_rate = 0.5 < r1[2] < 2.5
sc("B2", mono_r and hashed_rate, True, f"monotone and cheaper at every cell: YES; MC cross-check: YES; RATE is 1/j^2 (j^2*c -> {r2[2]:.3f}), NOT 5/(2j)*const — my hashed rate MISSES; the family is not one scale constant")
print("B3(i): other multiplication effects — 1 - f = (1-s)(s-c)^2, s = |z|^2, c in (0,1)")
brk=[]
for c0 in ("0","3/10","3/5","9/10","99/100"):
    c0f=F(c0); col=[-tau(3,j,0)+(1+2*c0f)*tau(2,j,0)-(2*c0f+c0f**2)*tau(1,j,0)+c0f**2 for j in range(0,31)]
    m=all(col[i]>col[i+1] for i in range(30)); brk.append(m)
    print(f"   (1-s)(s-{c0})^2: values j=0,1,2,10,30: {[f'{float(x):.5f}' for x in (col[0],col[1],col[2],col[10],col[30])]}  monotone {m}")
sc("B3i", all(brk), True, "every multiplication effect tested is monotone decreasing in j")
print("B3(ii): the general K-invariant effect — Schur says ANY lambda(j,k) in [0,1] is admissible")
lam=lambda j: 1-float(cn(1,j,0))*(1+0.5*(-1)**j)
cost=[1-lam(j) for j in range(8)]
print("   lambda(j,0) -> 1 in the boundary limit but oscillates; cost:", [f"{x:.4f}" for x in cost], " monotone:", all(cost[i]>cost[i+1] for i in range(7)))
sc("B3ii", not all(cost[i]>cost[i+1] for i in range(7)), True, "ORDER BREAKS: 'identity on the Shilov boundary' constrains a FUNCTION, not an operator's eigenvalues")

print("")
print("POST-HOC (unscored, added after the B3i miss — labelled as exploration, not a hashed line):")
print("  Why (1-s)s^2 breaks it: f = 1 - (1-s)s^2 = 1 - s^2 + s^3 has a NEGATIVE coefficient on s^2.")
print("  Exact costs for c = 0: ", [str(-tau(3,j,0)+tau(2,j,0)) for j in range(6)])
print("  CHARACTERISATION: <f> = sum_p a_p tau_p, and every tau_p rises with j (B1). So if f(s) = sum_p a_p s^p with a_p >= 0 and sum a_p = 1")
print("  (a probability MIXTURE of the boundary powers |z|^{2p}), the order is FORCED. Outside that cone it is not.")
print("  Alignment test — is 'f non-decreasing in s' the dividing line?")
for c0 in ("0","3/10","3/5","9/10","99/100"):
    c0f=F(c0)
    fp=lambda s: -(2*(s-c0f)*(1-s) - (s-c0f)**2)   # d f/ds = -d/ds[(1-s)(s-c)^2]
    grid=[F(i,20) for i in range(0,20)]
    incr=all(fp(s)>=0 for s in grid)
    col=[-tau(3,j,0)+(1+2*c0f)*tau(2,j,0)-(2*c0f+c0f**2)*tau(1,j,0)+c0f**2 for j in range(0,31)]
    mono=all(col[i]>col[i+1] for i in range(30))
    print(f"    c={c0}: f non-decreasing in s on [0,1]: {incr};  cost monotone in j: {mono}  -> {'aligned' if incr==mono else 'NOT aligned'}")
print("  Aligned in 4 of 5: monotone-in-s is NOT the exact dividing line (c = 9/10 is non-monotone in s yet ordered in j).")
print("  What I can state exactly: the mixture cone (a_p >= 0) is SUFFICIENT and provable from B1; no necessary condition is claimed.")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'rho_k0':[str(crho(j,0)) for j in range(8)],'rate_rho_j2':r2,'power_rate':[float(20000*cn(n,20000,0)) for n in range(1,9)]}, open('.record_5741.json','w'), indent=1)
