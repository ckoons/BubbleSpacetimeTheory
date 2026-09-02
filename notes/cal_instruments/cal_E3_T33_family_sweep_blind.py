#!/usr/bin/env python3
"""Cal E3 blind instrument (2026-09-02): is the T33 functional Q = sum_i s(C_i) - log2|sol| a hardness measure?
Sweep the family: 3-SAT (NP-hard), 2-SAT (P), 3-XORSAT (P). Exact |sol| by brute force. No project modules.
s(C) = -log2 P(C satisfied) per clause: 3-SAT log2(8/7), 2-SAT log2(4/3), XOR 1 bit. Also report Q/n at alpha=2 for 3-SAT."""
import random, math, sys
def gen(n, m, k, xor, rng):
    cl=[]
    for _ in range(m):
        vs=rng.sample(range(n),k); cl.append([(v, rng.random()<0.5) for v in vs] if not xor else (vs, rng.random()<0.5))
    return cl
def count(n, cl, xor):
    c=0
    for a in range(1<<n):
        ok=True
        for C in cl:
            if xor:
                vs,par=C
                if (sum((a>>v)&1 for v in vs)&1)!=par: ok=False;break
            else:
                if not any(((a>>v)&1)==(1 if pos else 0) for v,pos in C): ok=False;break
        if ok: c+=1
    return c
def sweep(label, k, xor, alphas, n=12, inst=12, seed=1):
    rng=random.Random(seed); s1 = 1.0 if xor else math.log2(2**k/(2**k-1))
    for al in alphas:
        m=int(al*n); qs=[]; sat=0
        for _ in range(inst):
            cl=gen(n,m,k,xor,rng); ns=count(n,cl,xor)
            if ns>0: sat+=1; qs.append((m*s1 - math.log2(ns))/n)
        ann = al*s1 - (1 - al*s1)   # annealed prediction Q/n = alpha*s1 - log2 E|sol|/n
        mq = sum(qs)/len(qs) if qs else float('nan')
        print(f"{label:9s} alpha={al:5.3f} m={m:3d} sat={sat:2d}/{inst}  Q/n measured={mq:+.3f}  annealed={ann:+.3f}")
print("n=12, exact counts, satisfiable instances only (Q undefined on UNSAT: log2 0)")
sweep("3-SAT",3,False,[2.0,3.0,4.267])
sweep("2-SAT",2,False,[0.5,1.0,1.5])
sweep("3-XORSAT",3,True,[0.5,0.918,1.2])
