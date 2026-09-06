# Cal's independent instrument: 5-dim Epstein zeta Z(s)=sum' (x.x)^{-s}, completed Lambda(s)=pi^{-s}Gamma(s)Z(s)
# Chowla-Selberg/theta split: Lambda(s) = sum' [G(s,pi N)(pi N)^{-s} + G(5/2-s,pi N)(pi N)^{s-5/2}] r5(N) + 1/(s-5/2) - 1/s
from mpmath import mp, mpf, mpc, pi, gammainc, fabs, quad, exp
mp.dps = 40
M=120
# r5 via theta^5
th=[0]*(M+1); 
import math
for k in range(-11,12):
    if k*k<=M: th[k*k]+=1
r=th[:]
for _ in range(4):
    new=[0]*(M+1)
    for i,a in enumerate(r):
        if a==0: continue
        for j,b in enumerate(th):
            if b and i+j<=M: new[i+j]+=a*b
    r=new
assert r[1:7]==[10,40,80,90,112,240], r[1:7]
def Lam(s):
    s=mpc(s); tot=mpc(0)
    for N in range(1,M+1):
        if r[N]==0: continue
        z=pi*N
        tot+= r[N]*( gammainc(s,z)*z**(-s) + gammainc(mpf(5)/2-s,z)*z**(s-mpf(5)/2) )
    return tot + 1/(s-mpf(5)/2) - 1/s
s0=mpc('2.5035899876435054856','14.279995705512019903')
print("Lambda at Elie's refined zero :", mp.nstr(fabs(Lam(s0)),5))
print("FE check |Lam(s)-Lam(5/2-s)| at 1.9+7i:", mp.nstr(fabs(Lam(mpc(1.9,7))-Lam(mpc(0.6,-7))),5))
for d in (0.01,0.001,1e-4,-1e-4):
    print(" offset re",d, mp.nstr(fabs(Lam(s0+d)),5), " offset im",d, mp.nstr(fabs(Lam(s0+1j*d)),5))
# TS point as published (halved), Im from their digit string
sTS=mpc('2.503589987643505','14.2799570551201725')
print("Lambda at Travenec-Samaj published point (halved):", mp.nstr(fabs(Lam(sTS)),5))
# Z on real axis sanity: Z(4)= sum r5/N^4 direct
Zdirect=sum(mpf(r[N])/mpf(N)**4 for N in range(1,M+1))
from mpmath import gamma
print("Z(4) direct(truncated)", mp.nstr(Zdirect,12), " via Lambda", mp.nstr(Lam(4)*pi**4/gamma(4),12))
