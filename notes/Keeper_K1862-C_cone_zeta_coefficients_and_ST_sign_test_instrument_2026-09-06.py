import numpy as np, math
NMAX = 20000; P = 20000
def primes(n):
    s = bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
PR = primes(P); PRset=set(PR)
def density_conv(N, p, k, signs):
    q = p**k
    dt = np.int64 if q <= 2**14 else np.float64
    sq = np.zeros(q, dtype=dt); xs = np.arange(q, dtype=np.int64); np.add.at(sq, (xs*xs)%q, 1)
    negsq = np.roll(sq[::-1], 1); dist = np.zeros(q, dtype=dt); dist[0]=1
    for s in signs:
        vec = sq if s>0 else negsq
        full = np.convolve(dist, vec); dist = full[:q].copy(); dist[:q-1] += full[q:]
    return float(dist[N%q]) / float(q)**4
def leg(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
def alpha_odd(N, p):
    # unimodular 5-variable form, det=1, odd p: recursion  a(p^e u) = 1 - p^-4 + p^-3 a(p^{e-2} u) (e>=2); e=1: 1-p^-4; e=0: 1+leg(N,p)/p^2
    e=0; m=N
    while m%p==0: m//=p; e+=1
    if e==0: return 1 + leg(m,p)/p**2
    if e==1: return 1 - p**-4
    return (1 - p**-4) + p**-3 * alpha_odd(N//(p*p), p)
# validate recursion against convolution
ok=True
for p in (3,5,7):
    for N in [p, 2*p, p*p, 3*p*p if p!=3 else 2*p*p, p**3, 5*p**3 if p!=5 else 2*p**3, p**4]:
        for signs in ((1,1,1,1,1),(1,-1,-1,-1,-1)):
            e=0; m=N
            while m%p==0: m//=p; e+=1
            c = density_conv(N,p,e+1,signs); r = alpha_odd(N,p)
            if abs(c-r) > 1e-12: ok=False; print("MISMATCH", p, N, signs, c, r)
print("recursion validated against convolution (p=3,5,7; e<=4; both forms):", ok)
# b(N) for the indefinite form (2-adic by convolution, odd by recursion)
b = np.zeros(NMAX+1)
for N in range(1, NMAX+1):
    v = density_conv(N, 2, ((N & -N).bit_length()-1)+3, (1,-1,-1,-1,-1))
    m=N
    for p in PR[1:]:
        if p*p>m and m>1 and m in PRset:
            v*=alpha_odd(N,m); m=1; break
        if m%p==0:
            v*=alpha_odd(N,p)
            while m%p==0: m//=p
        if m==1: break
    # remaining primes not dividing N: product over p<=P of (1+leg/p^2)
    b[N]=v
# Euler product over p not dividing N, vectorized via QR tables
qr = {}
for p in PR[1:]:
    t = np.zeros(p, dtype=np.int8); t[(np.arange(1,p)**2)%p] = 1; qr[p]=t
Ns = np.arange(NMAX+1)
logprod = np.zeros(NMAX+1)
for p in PR[1:]:
    r = Ns % p
    chi = np.where(r==0, 0, np.where(qr[p][r]==1, 1, -1))
    logprod += np.log1p(chi/p**2)   # chi=0 (p|N) contributes 0: alpha already applied
b *= np.exp(logprod)
print("b(1..12):", np.round(b[1:13],5))
pairs=[(3,5),(3,7),(5,7),(3,11),(5,11),(7,11),(9,5),(3,25),(2,3),(2,5),(4,3)]
print("multiplicativity b(mn)/(b(m)b(n)) for coprime m,n:", [round(b[m*n]/(b[m]*b[n]),3) for m,n in pairs])
# Soundararajan-Thorne sign test
def chi_from(smap, dflt):
    ch = np.ones(NMAX+1)
    for n in range(2, NMAX+1):
        m=n; val=1.0
        for p in PR:
            if p*p>m: break
            while m%p==0: m//=p; val*= smap.get(p, dflt)
        if m>1: val*= smap.get(m, dflt)
        ch[n]=val
    return ch
ns = Ns.astype(float)
bmax = b[1:].max(); print("max b =", round(bmax,4), " min b =", round(b[1:].min(),4), " argmin", int(np.argmin(b[1:]))+1)
for name, smap, dflt in [("all -1 (Liouville)", {}, -1), ("+1 at 2", {2:1}, -1), ("+1 at 3", {3:1}, -1), ("+1 at 2,3", {2:1,3:1}, -1),
                         ("+1 at 2,3,5", {2:1,3:1,5:1}, -1), ("-1 at 2 only", {2:-1}, 1), ("-1 at 3 only", {3:-1}, 1), ("-1 at 2,3", {2:-1,3:-1}, 1),
                         ("+1 at p≡1(4)", {p:1 for p in PR if p%4==1}, -1), ("+1 at p≡3(4)", {p:1 for p in PR if p%4==3}, -1),
                         ("+1 at p≡1(4) and 2", {**{p:1 for p in PR if p%4==1}, 2:1}, -1)]:
    ch = chi_from(smap, dflt)
    line = f"{name:24s}"
    for sigma in (1.1, 1.25, 1.5, 2.0):
        S = float(np.sum(b[1:]*ch[1:]/ns[1:]**sigma)); tail = bmax*NMAX**(1-sigma)/(sigma-1)
        flag = "  <<< NEGATIVE beyond crude tail" if S + tail < 0 else ""
        line += f" | s={sigma}: {S: .4f} (tail<{tail:.4f}){flag}"
    print(line)
