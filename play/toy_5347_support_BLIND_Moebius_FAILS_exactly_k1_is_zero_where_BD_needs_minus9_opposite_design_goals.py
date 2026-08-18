import numpy as np
from collections import Counter, defaultdict
rng=np.random.default_rng(7)
print("="*104)
print("TOY 5347 -- THE BLIND MOEBIUS TEST: does mu of the derived order give BD's magnitudes?")
print("  *** STEP 1 derives mu's layer-weights with NO reference to BD. *** Tables first.")
print("="*104)

print("\n"+"-"*104)
print("STEP 1 -- mu's LAYER WEIGHTS, DERIVED BLIND (nothing from BD below this line)")
print("-"*104)
print("\n  BD weights by LAYER; mu is defined on PAIRS. The bridge: layer n = pairs with exactly")
print("  k = n-1 elements strictly between. So compute mu as a function of k.")
print("\n  Recursion:  mu(x,y) = -sum_{x <= w < y} mu(x,w),  mu(x,x) = 1.")
print("\nTABLE 1 -- work out the first cases EXACTLY, by hand:")
print("   k = 0 (a LINK, empty interval):")
print("      mu = -[mu(x,x)] = -1                                    *** ALWAYS -1 ***")
print("   k = 1 (exactly one z between):")
print("      z covers x, so mu(x,z) = -1")
print("      mu(x,y) = -[mu(x,x) + mu(x,z)] = -[1 + (-1)] = 0        *** ALWAYS 0 ***")
print("   k = 2 : depends on whether the two are comparable")
print("      chain z1 < z2 : -[1 + (-1) + 0] = 0")
print("      antichain     : -[1 + (-1) + (-1)] = +1")
print("\n  *** BLIND COMMITMENT, POSTED BEFORE OPENING BD: ***")
print("     mu(k=0) = -1 EXACTLY, mu(k=1) = 0 EXACTLY (for EVERY poset, no exceptions),")
print("     mu(k=2) in {0, +1}. If BD's layer-2 coefficient is anything nonzero, THIS ROUTE FAILS,")
print("     and it fails EXACTLY rather than statistically.")

print("\nTABLE 2 -- verify that on BST's own derived order (R x S^4, T2564)")
def build(N,T):
    t=rng.uniform(0,T,N); x=rng.normal(size=(N,5)); x/=np.linalg.norm(x,axis=1,keepdims=True)
    o=np.argsort(t); t=t[o]; x=x[o]
    dth=np.arccos(np.clip(x@x.T,-1,1)); dt=t[None,:]-t[:,None]
    return (dt>0)&(dt>dth)
def mu_by_k(R):
    N=R.shape[0]; mu=np.zeros((N,N),dtype=np.int64); d=defaultdict(Counter)
    for i in range(N):
        mu[i,i]=1
        for j in range(i+1,N):
            if R[i,j]:
                s=1+sum(mu[i,k] for k in range(i+1,j) if R[i,k] and R[k,j])
                mu[i,j]=-s
                k=int(sum(1 for w in range(i+1,j) if R[i,w] and R[w,j]))
                d[k][mu[i,j]]+=1
    return d
d=mu_by_k(build(140,4.0))
print("   k (elements between)   layer n=k+1   mu values observed (count)          unique?")
for k in sorted(d)[:5]:
    items=sorted(d[k].items(), key=lambda p:-p[1])[:4]
    print("   %-22d %-13d %-35s %s"%(k,k+1,str(items),"YES" if len(d[k])==1 else "no"))
print("   ==> k=0 gives -1 uniquely and k=1 gives 0 uniquely, exactly as derived. Confirmed.")

print("\n"+"-"*104)
print("STEP 2 -- NOW open BD")
print("-"*104)
BD=[1,-9,16,-8]
print("   BD 4D layer coefficients (layers 1-4):  %s"%BD)

print("\n"+"-"*104)
print("STEP 3 -- THE COMPARISON")
print("-"*104)
print("   layer n   k    mu (derived blind)      BD (4D)   match?")
mus=["-1 (exact)","0 (exact)","{0,+1}","varies"]
for n in range(1,5):
    ok = "sign only" if n==1 else ("*** FAIL ***" if n==2 else "no")
    print("   %-9d %-4d %-23s %-9d %s"%(n,n-1,mus[n-1],BD[n-1],ok))
print("\n   *** LAYER 2 IS THE KILL: mu = 0 EXACTLY, for every poset. BD needs -9. ***")
print("   Zero is not -9, and no sprinkling, dimension, or normalisation changes it -- the k=1")
print("   cancellation is forced by the recursion itself.")

print("\nTABLE 3 -- WHY it fails, structurally (the lesson worth keeping)")
print("   object   designed to...                                    consequence")
print("   mu       INVERT zeta  -- it is built to CANCEL             alternating sums collapse to 0")
print("   BD       reproduce [] -- it is built NOT to cancel         coefficients must survive")
print("   ==> *** THEY HAVE OPPOSITE DESIGN GOALS. *** mu's whole job is that its alternating sums")
print("       telescope away; BD's whole job is that its layer sum does NOT. Matching them was")
print("       never plausible once stated this way -- which is the value of writing the weights first.")

print("\n"+"="*104)
print("VERDICT -- weights written blind, comparison after")
print("="*104)
print(" (1) *** THE MOEBIUS ROUTE FAILS, EXACTLY AND NOT STATISTICALLY. *** mu(k=1) = 0 for every")
print("     poset by the recursion; BD's layer-2 coefficient is -9. Nothing tunable sits between them.")
print("     Verified computationally on BST's own derived order (Table 2): k=0 -> -1 uniquely,")
print("     k=1 -> 0 uniquely, as derived by hand before BD was opened.")
print()
print(" (2) THE STRUCTURAL REASON, worth banking: *** mu is built to CANCEL (it inverts zeta); BD is")
print("     built NOT to cancel (it must survive to reproduce []). Opposite design goals. ***")
print()
print(" (3) SCOPE, HONESTLY -- and @Keeper asked for exactly this care: my 5346 sweep found mu to be")
print("     the ONLY enumerated object passing all three criteria, and it now fails on the VALUES.")
print("     So the route is closed for every candidate I have found. *** That is NOT the same as")
print("     'exhaustive'. *** I enumerated the graded objects I could name; I cannot certify no")
print("     other exists. Please tier it as 'no surviving candidate', not 'proved impossible'.")
print()
print(" (4) NET ACROSS 5345-5347: fermion parity fails on RANGE (all magnitudes 1); mu fails on")
print("     VALUES (exact zeros where BD needs -9). Two candidates, two different failure modes,")
print("     both found by writing the weights before opening BD. C4 has no surviving route today.")
