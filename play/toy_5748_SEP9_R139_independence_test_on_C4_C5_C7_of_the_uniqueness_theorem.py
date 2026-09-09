#!/usr/bin/env python3
"""Toy 5748 — R139 E1: the Independence Test on criteria C4, C5, C7. Side A must be root-data computable with no BST integer."""
import json, math
from fractions import Fraction as F
import numpy as np
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
def domains(maxdim=12, maxrank=99):
    out=[]
    for p in range(1,13):
        for q in range(p,13):
            if p*q<=maxdim and min(p,q)<=maxrank: out.append((f"I_{{{p},{q}}}", p*q, min(p,q), p+q))
    for n in range(2,13):
        d=n*(n-1)//2
        if d<=maxdim and n//2<=maxrank and d>0: out.append((f"II_{n}", d, n//2, 2*n-2))
    for n in range(1,13):
        d=n*(n+1)//2
        if d<=maxdim and n<=maxrank: out.append((f"III_{n}", d, n, n+1))
    for n in range(1,13):
        if n<=maxdim and 2<=maxrank: out.append((f"IV_{n}", n, 2, n))
    if 16<=maxdim: out.append(("V(E6)",16,2,12))
    if 27<=maxdim: out.append(("VI(E7)",27,3,18))
    return out
def isprime(m):
    if m<2: return False
    for i in range(2,int(m**0.5)+1):
        if m%i==0: return False
    return True
print("C4 — 'GF(2^g) cyclotomic Reed-Solomon compatibility (Mersenne g=7)'")
print("  READING (i), as written: side A is 2^7 - 1 = 127, prime? -> the expression contains NO domain.")
verdicts=set()
for name,d,r,g in domains(): verdicts.add(isprime(2**7-1))
print(f"   verdict over all {len(domains())} candidate domains with dim <= 12: {verdicts} — identical for every one")
sc("C4-i", verdicts=={True} and len(verdicts)==1, True, "the verdict does not depend on the domain: as written, C4 discriminates NOTHING")
print("  READING (ii), honest: side A = 2^genus - 1 is prime, genus from root data")
passers=[(n,d,r,g) for (n,d,r,g) in domains() if isprime(2**g-1)]
print(f"   D_IV_5: genus 5, 2^5-1 = 31, prime = {isprime(31)}  <- PASSES on the honest reading")
print(f"   D_I_(1,5): genus 6, 2^6-1 = 63 = 9*7, prime = {isprime(63)}  <- still fails")
print(f"   domains passing (dim <= 12): {len(passers)} -> {[n for n,_,_,_ in passers][:14]}")
sc("C4-ii", isprime(31) and not isprime(63) and len(passers)>=8, True, f"honest C4 survives for D_IV^5 but is WEAK: {len(passers)} domains pass, not one")
print("C5 — 'five BST primary integers forced by structure'")
print("   Side A would have to be a root-data quantity that yields {rank, N_c, n_C, C_2, g}. Every route to it imports the integers")
print("   it is meant to force (C_2 = rank*N_c and g = n_C + rank are DEFINITIONS). No BST-integer-free side A exists.")
sc("C5", True, False, "EMPTY, not failed: the criterion is the conclusion restated")
print("C7 — 'c_FK = (N_c*n_C)^2 / pi^((g+rank)/rank) reproduces the classical Faraut-Koranyi volume'")
def volIV(n): return math.pi**n/(2**(n-1)*math.factorial(n))
print(f"   side A, classical: Vol(D_IV^n) = pi^n / (2^(n-1) n!). Checks with no BST input:")
print(f"     n=1 (the disc): formula {volIV(1):.6f} vs pi = {math.pi:.6f}")
print(f"     n=2 (bidisc under the Cartan map, Jacobian 4): formula {volIV(2):.6f} vs pi^2/4 = {math.pi**2/4:.6f}")
rng=np.random.default_rng(139); acc=0; tot=0
for c in range(10):
    w=rng.uniform(-1,1,(6_000_000,5))+1j*rng.uniform(-1,1,(6_000_000,5))
    rr=(np.abs(w)**2).sum(1); ww=(w*w).sum(1); acc+=int(((rr<1)&(np.abs(ww)**2-2*rr+1>0)).sum()); tot+=len(w)
mc=acc/tot*(2.0**10)
print(f"     n=5 Monte Carlo: {acc}/{tot} accepted in a box of volume 2^10 -> Vol = {mc:.6f} vs formula {volIV(5):.6f}  ({abs(mc/volIV(5)-1)*100:.2f}% apart)")
row=(3*5)**2/math.pi**4.5
print(f"   the power of pi the volume actually requires is n = 5 (the DIMENSION, a domain invariant), not (g+rank)/rank = 9/2")
print(f"   the row's expression = 225/pi^4.5 = {row:.6f};  the true volume = {volIV(5):.6f};  factor {row/volIV(5):.2f} apart")
sc("C7", abs(mc/volIV(5)-1)<0.03 and abs(row/volIV(5)-1)>1, True, "side A is BST-free and gives exponent n = 5; the row's 9/2 is built from g AND misses the volume by 8.17x")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'c4_passers':[n for n,_,_,_ in passers],'vol_mc':mc,'vol_formula':volIV(5),'row_expr':row}, open('.record_5748.json','w'), indent=1)
