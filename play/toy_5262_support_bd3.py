import numpy as np, sys
exec(open('bd2.py').read().split('print("="*80)')[0])
print("="*80)
print("IS IT NOISE (fixable by averaging) OR BIAS (not fixable)?  flat 4D, correct d=4 operator")
print("="*80)
print("   N      K    mean B_4        sem        mean/sem   verdict")
for N,K in [(400,24),(800,16),(1600,8)]:
    vals=[]
    for _ in range(K):
        t,fut,pas,sub=make_MINK(N,4); C=causal_matrix(N,fut)
        vals.append(BD_ones(C,*BD4,rho=N,d=4))
    v=np.array(vals); sem=v.std(ddof=1)/np.sqrt(K)
    print("   %4d   %2d   %+10.4f   %8.4f   %8.2f   %s"%(N,K,v.mean(),sem,abs(v.mean())/sem,
        "consistent with 0" if abs(v.mean())<3*sem else "BIASED away from 0"))
    sys.stdout.flush()
print()
print("  spread of single runs at N=400: %s"%np.round(np.array(vals[:0]) if False else 0,3))
