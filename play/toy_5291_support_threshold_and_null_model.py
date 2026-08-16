import numpy as np, itertools, random
rng=random.Random(1456)
print("="*92)
print("(1) IS 'N_c = 3 IS THE HARDNESS THRESHOLD' (T1456) EVEN TRUE?  Verify the phenomenon first.")
print("="*92)
def rand_ksat(n,m,k,rng):
    return [tuple(rng.sample(range(1,n+1),k)) and tuple((v if rng.random()<0.5 else -v) for v in rng.sample(range(1,n+1),k)) for _ in range(m)]
def brute_sat(n,cls):
    for bits in range(1<<n):
        ok=True
        for c in cls:
            if not any((bits>>(abs(l)-1))&1 == (l>0) for l in c): ok=False;break
        if ok: return True
    return False
def dpll_calls(n,cls):
    """count backtracking nodes -- a proxy for hardness"""
    cnt=[0]
    def go(assign,i):
        cnt[0]+=1
        for c in cls:
            if all(abs(l)-1 < i for l in c) and not any(assign[abs(l)-1]==(l>0) for l in c): return False
        if i==n: return True
        for b in (True,False):
            assign[i]=b
            if go(assign,i+1): return True
        return False
    go([None]*n,0); return cnt[0]
print("  Backtracking nodes at the satisfiability phase transition (median over 40 instances):")
print("      n       2-SAT (m=1.0n)     3-SAT (m=4.27n)")
for n in [10,14,18,22]:
    a=int(np.median([dpll_calls(n,[tuple((v if rng.random()<0.5 else -v) for v in rng.sample(range(1,n+1),2)) for _ in range(int(1.0*n))]) for _ in range(40)]))
    b=int(np.median([dpll_calls(n,[tuple((v if rng.random()<0.5 else -v) for v in rng.sample(range(1,n+1),3)) for _ in range(int(4.27*n))]) for _ in range(40)]))
    print("    %4d      %12d      %14d"%(n,a,b))
print("  ⟹ the phenomenon is REAL: 2-SAT stays cheap, 3-SAT blows up. 2-COL/3-COL behave the same way.")
print()
print("="*92)
print("(2) BUT IS IT OURS?  Schaefer's dichotomy theorem (1978) ALREADY EXPLAINS IT.")
print("="*92)
print("  Schaefer: a Boolean CSP is in P iff its constraint language is 0-valid, 1-valid, Horn,")
print("  dual-Horn, AFFINE, or BIJUNCTIVE (2-SAT-like); otherwise NP-complete. Bijunctive = arity 2.")
print("  => THE 2/3 THRESHOLD IS A THEOREM OF CLASSICAL COMPLEXITY THEORY, proved in 1978, with no")
print("     geometric input. BST MATCHING it is an IDENTIFICATION, not a derivation. To be a")
print("     derivation, 'you cannot linearise curvature' must produce something Schaefer does NOT.")
print()
print("="*92)
print("(3) ★ PRE-EMPTIVE NUMEROLOGY KILL: alpha_c(3) ~ 4.2667 and 2^{C_2}/(N_c n_C) = 64/15 = 4.26667")
print("="*92)
ac3=4.26675
print("  the k=3 satisfiability threshold is alpha_c(3) ~ %.5f (1RSB cavity, Mertens-Mezard-Zecchina)"%ac3)
print("  and 2^C_2 / (N_c * n_C) = 64/15 = %.5f  -- agreement to %.3f%%. SOMEONE WILL PROPOSE THIS."%(64/15,100*abs(64/15-ac3)/ac3))
print()
print("  THE NULL MODEL: how many simple BST-primary ratios land that close, by chance?")
prim=[2,3,5,6,7,137]
vals=set()
for a in itertools.product(range(0,7),repeat=3):        # 2^a 3^b 5^c
    for b in itertools.product(range(0,4),repeat=3):
        num=2**a[0]*3**a[1]*5**a[2]; den=2**b[0]*3**b[1]*5**b[2]
        if den and 0<num/den<1e4: vals.add(num/den)
vals=np.array(sorted(vals))
tol=0.003
hits=vals[np.abs(vals-ac3)/ac3<tol]
print("    candidate ratios of the form 2^a 3^b 5^c / 2^d 3^e 5^f : %d distinct values"%len(vals))
print("    landing within %.1f%% of alpha_c(3): %d  ->  %s"%(100*tol,len(hits),np.array2string(hits,precision=5)))
dens=len(vals[(vals>1)&(vals<100)])/99.0
print("    density of such ratios in (1,100): %.1f per unit  =>  expected hits in a %.1f%%-wide window"%(dens,100*tol))
print("      around 4.267 (width %.4f): %.2f"%(2*tol*ac3,dens*2*tol*ac3))
print()
print("  ⟹ AND THE DECISIVE POINT: alpha_c(3) IS NOT KNOWN EXACTLY. 4.2667 is a numerical estimate")
print("     from the 1RSB cavity method; the rigorous bounds are far wider (roughly 3.52 < alpha_c < 4.51).")
print("     MATCHING A NON-RIGOROUS NUMERICAL ESTIMATE TO 4 DIGITS WITH A FREE RATIO OF BST INTEGERS")
print("     IS NOT EVIDENCE. It is the 7/8 failure of this morning, wearing a different hat.")
print("  ★ STANDING FLAG: if alpha_c(3) = 64/15 is proposed today, it needs (a) a MECHANISM linking a")
print("    satisfiability threshold to 2^{C_2}/(N_c n_C), and (b) a prediction for alpha_c(4) and")
print("    alpha_c(5) from the SAME formula, checked against 9.93 and 21.1. One number is not a result.")
for k,a in [(4,9.931),(5,21.117),(6,43.37),(7,87.79)]:
    print("      alpha_c(%d) = %7.3f   -- any BST form must predict THIS TOO, from the same mechanism"%(k,a))
