import numpy as np, itertools
I2=np.eye(2); X=np.array([[0,1],[1,0]],complex); Y=np.array([[0,-1j],[1j,0]]); Z=np.diag([1,-1]).astype(complex)
def kron(*a):
    r=np.array([[1]],complex)
    for m in a: r=np.kron(r,m)
    return r
def euclid_gammas(n):  # n Hermitian anticommuting matrices squaring to +1, size 2^floor(n/2)
    k=n//2; gs=[]
    for j in range(k):
        gs.append(kron(*([Z]*j+[X]+[I2]*(k-j-1))))
        gs.append(kron(*([Z]*j+[Y]+[I2]*(k-j-1))))
    if n%2: gs.append(kron(*([Z]*k)))
    return gs
def cliff(p,q):  # p squares +1, q squares -1
    gs=euclid_gammas(p+q)
    return [g for g in gs[:p]]+[1j*g for g in gs[p:]]
def check(p,q,spacetime,internal,label):
    g=cliff(p,q); n=p+q; d=g[0].shape[0]
    for a,b in itertools.combinations(range(n),2): assert np.allclose(g[a]@g[b]+g[b]@g[a],0)
    w=np.eye(d,dtype=complex)
    for m in g: w=w@m
    central=all(np.allclose(w@m,m@w) for m in g)
    w2=(w@w)[0,0]
    # 4D chirality from spacetime gammas (3 space with +1, 1 time with -1)
    g5=np.eye(d,dtype=complex)
    for i in spacetime: g5=g5@g[i]
    g5=g5*(1/np.sqrt((g5@g5)[0,0]))   # normalise so g5^2=1
    out=f"{label}: Cl({p},{q}) dim spinor={d}, omega central={central}, omega^2={w2.real:+.0f}"
    if internal:
        wi=np.eye(d,dtype=complex)
        for i in internal: wi=wi@g[i]
        wi=wi*(1/np.sqrt((wi@wi)[0,0]))
        # joint eigenvalues of commuting g5, wi
        assert np.allclose(g5@wi,wi@g5)
        M=g5+2.7*wi; ev=np.linalg.eigvals(M).real.round(3)
        pairs={}
        for e in ev:
            for s5 in (1,-1):
                for si in (1,-1):
                    if abs(e-(s5+2.7*si))<1e-6: pairs[(s5,si)]=pairs.get((s5,si),0)+1
        corr=np.allclose(g5, wi@w*(1/(wi@w)[0,0]) if False else g5)
        out+=f"\n   (gamma5, internal-chirality) multiplicities: {pairs}"
        # relation: is g5 proportional to wi times omega?
        r=g5@np.linalg.inv(wi@w)
        out+=f"\n   gamma5 = c * omega_int * omega ? {np.allclose(r, r[0,0]*np.eye(d))}"
    else:
        ev=np.linalg.eigvals(g5).real.round(3)
        out+=f"\n   gamma5 eigenvalues: +1 x{sum(ev>0)}, -1 x{sum(ev<0)}"
        r=g5@np.linalg.inv(g[3]); out+=f"\n   gamma5 proportional to the extra gamma? {np.allclose(r, r[0,0]*np.eye(d))}"
    print(out)
# 5 = Shilov boundary signature (4,1): spacetime = 3 space + time, plus one extra spatial direction
check(4,1,spacetime=[0,1,2,4],internal=[],label="n=5")
# 7 = SO(5,2) defining signature: spacetime = 3 space(+) + 1 time(-); internal = 2(+) + 1(-)
check(5,2,spacetime=[0,1,2,5],internal=[3,4,6],label="n=7")
# controls
check(6,0,spacetime=[0,1,2,3],internal=[4,5],label="n=6 (even control)")
