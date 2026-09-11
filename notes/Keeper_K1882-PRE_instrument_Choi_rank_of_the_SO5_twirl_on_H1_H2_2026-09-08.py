import numpy as np
from scipy.stats import special_ortho_group as SO
rng=np.random.default_rng(3)
# H_1 = C^5 (g acts directly); H_2 = traceless symmetric 5x5 (g M g^T), dim 14
def basis_H2():
    B=[]
    for i in range(5):
        for j in range(i,5):
            M=np.zeros((5,5)); 
            if i==j: M[i,i]=1
            else: M[i,j]=M[j,i]=1/np.sqrt(2)
            B.append(M)
    # project out trace: use basis of traceless part
    B=np.array([b.flatten() for b in B])       # 15 x 25
    tr=np.eye(5).flatten()/np.sqrt(5)
    B=B-np.outer(B@tr,tr)
    U,s,Vt=np.linalg.svd(B,full_matrices=False)
    return Vt[:14]                               # 14 orthonormal vectors in R^25
def rep_H2(g,V):
    G=np.kron(g,g)                               # action on flattened M: g M g^T
    return V@G@V.T                               # 14x14
def choi_rank(d,rep,n=4000):
    C=np.zeros((d*d,d*d))
    for _ in range(n):
        U=rep(SO.rvs(5,random_state=rng))
        v=U.flatten()                            # vec(U) ; Choi of ρ->UρU^T is |vecU><vecU|
        C+=np.outer(v,v)
    C/=n
    s=np.linalg.svd(C,compute_uv=False)
    return int((s>1e-3*s[0]).sum()), s[:3], s[-3:]
r1=choi_rank(5,lambda g:g)
print("H_1: Choi rank",r1[0],"(expect 25); top sv",r1[1].round(4),"tail",r1[2].round(4))
V=basis_H2()
r2=choi_rank(14,lambda g:rep_H2(g,V))
print("H_2: Choi rank",r2[0],"(expect 196); top sv",r2[1].round(4),"tail",r2[2].round(4))
