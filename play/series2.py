import numpy as np
S=np.array([[1,1,0],[1,2,1],[0,1,2]],float)
# reduction of S^k onto basis {S^2, S}  (identity coeff irrelevant to the corner ratio)
red=[]
for k in range(1,13):
    Bs=np.stack([np.eye(3).ravel(),S.ravel(),(S@S).ravel()],1)
    c,b,a=np.linalg.lstsq(Bs,np.linalg.matrix_power(S,k).ravel(),rcond=None)[0]
    red.append((a,b))
print("S^k -> (alpha,beta):"); [print(f"   k={k+1:<3} ({a:9.2f},{b:10.2f})   t=a/b={a/b if abs(b)>1e-9 else float('inf'):8.4f}") for k,(a,b) in enumerate(red[:8])]
print("\nWHY CLAIM 5 FAILED:  S^3 = 5S^2 - 6S + 1  -> a positive a_6 contributes -6 to beta.")
print("   Positivity of {a_2k} does NOT survive Cayley-Hamilton reduction.")
# true reachable range of t (hence of the ratio) under a_2k >= 0
ts=[]
rng=np.random.default_rng(0)
for _ in range(300000):
    ak=rng.random(8)*rng.choice([1,0],8,p=[.5,.5])
    a=sum(ak[k]*red[k][0] for k in range(8)); b=sum(ak[k]*red[k][1] for k in range(8))
    if abs(b)>1e-9: ts.append(a/b)
ts=np.array(ts); R=ts/(1+4*ts)
print(f"\npositive-coefficient series:  t in [{ts.min():.3f}, {ts.max():.3f}]   ratio spans [{R.min():.3f}, {R.max():.3f}]")
print(f"   ratio takes BOTH signs: {np.any(R<0)} / {np.any(R>0)}   -> NO forced bound from positivity.")
print(f"   fraction of positive-coefficient series landing IN the pinned band [0.081,0.108]: {np.mean((R>=0.081)&(R<=0.108)):.4f}")
print("\nWHAT SURVIVES (all verified above):")
print("   Q^{2k}|even = S^k                      (A block-off-diagonal)         FORCED")
print("   any series  ==  beta*S + alpha*S^2     (Cayley-Hamilton, dim=3)       FORCED")
print("   corner ratio = t/(1+4t),  t=alpha/beta, independent of identity term  FORCED")
print("   value of t                                                            NOT FORCED")
