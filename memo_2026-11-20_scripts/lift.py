import numpy as np, itertools
exec(open('chirality.py').read().split('# 5 = Shilov')[0])
def sectors(g, spacetime, internal):
    d=g[0].shape[0]; w=np.eye(d,dtype=complex)
    for m in g: w=w@m
    g5=np.eye(d,dtype=complex)
    for i in spacetime: g5=g5@g[i]
    g5=g5/np.sqrt((g5@g5)[0,0])
    wi=np.eye(d,dtype=complex)
    for i in internal: wi=wi@g[i]
    wi=wi/np.sqrt((wi@wi)[0,0])
    pairs={}
    for v in np.linalg.eig(g5+2.7*wi)[1].T:
        pairs[(round((v.conj()@g5@v).real),round((v.conj()@wi@v).real))]=pairs.get((round((v.conj()@g5@v).real),round((v.conj()@wi@v).real)),0)+1
    return w[0,0], pairs, w
g=cliff(5,2); st=[0,1,2,5]; it=[3,4,6]
w0,p0,w=sectors(g,st,it)
gm=[-m for m in g]                     # the inequivalent irrep
w1,p1,_=sectors(gm,st,it)
print("irrep A: omega =",np.round(w0,6),"sectors",p0)
print("irrep B: omega =",np.round(w1,6),"sectors",p1)
# pin lift of the deck map modelled as -1 on all 7 directions = product of all gammas = omega
P=w
print("P = omega is a scalar on the irrep:", np.allclose(P, P[0,0]*np.eye(8)))
# KK check: what 1/R would the BST clock tick give if the S^1 circumference were the tick length?
hbar=1.054571817e-34; c=299792458; me=9.1093837139e-31; eV=1.602176634e-19
L=137*hbar/(me*c); print("tick length N_max*hbar/(m_e c) = %.3e m -> hbar c/L = %.2f keV (bound: > 1.5 TeV)"%(L, hbar*c/L/eV/1e3))
lP=1.616255e-35; Rmax=hbar*c/(1.5e12*eV); print("R must be < %.2e m = %.1e Planck lengths"%(Rmax,Rmax/lP))
