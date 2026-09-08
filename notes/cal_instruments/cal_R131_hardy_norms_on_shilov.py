# Cal R131: are the Hardy norms of (z.z)^j equal across j? On the Shilov boundary S = {e^{i t} x : x in S^4}
# z.z = e^{2it}, unimodular, so |(z.z)^j| = 1 identically and the modes are orthonormal. Monte Carlo check + Bergman contrast.
import numpy as np
rng=np.random.default_rng(1); N=200000
x=rng.normal(size=(N,5)); x/=np.linalg.norm(x,axis=1)[:,None]; t=rng.uniform(0,np.pi,N)
z=np.exp(1j*t)[:,None]*x; w=(z*z).sum(1)
print("Shilov: max | |z.z| - 1 | =", np.abs(np.abs(w)-1).max())
G=np.array([[np.mean(w**j*np.conj(w**l)) for l in range(6)] for j in range(6)])
print("Hardy Gram (z.z)^j, j,l<6: diag", np.round(np.real(np.diag(G)),4), " max offdiag", np.abs(G-np.diag(np.diag(G))).max().round(4))
# Bergman contrast on the Lie ball: sample the ball by rejection in the Lie-norm, unweighted Lebesgue
M=0; acc=[]
while M<200000:
    u=rng.uniform(-1,1,size=(400000,5))+1j*rng.uniform(-1,1,size=(400000,5))
    a=(np.abs(u)**2).sum(1); b=np.abs((u*u).sum(1)); lie=np.sqrt(a+np.sqrt(np.maximum(a*a-b*b,0)))
    ok=lie<1; acc.append(u[ok]); M+=ok.sum()
u=np.concatenate(acc)[:200000]; wb=(u*u).sum(1)
print("Bergman (Lebesgue) norms^2 of (z.z)^j, j=0..5:", np.round([np.mean(np.abs(wb)**(2*j)) for j in range(6)],4), " -> NOT equal: the weighted case")
