# R9 consistency instrument (Grace 2026-09-26). Pure transcription check; no BST input.
# Sources: HPPS arXiv:0907.0151 eqs (4.2),(4.13),(4.29),(4.34),(5.44),(5.45),(5.46);
#          Fitzpatrick-Kaplan arXiv:1112.4845 eq (42) (spacetime dim d = 2h).
from mpmath import mp, gamma as G, rf, factorial, mpf
mp.dps = 30
def C(n, D):  # HPPS (4.2)
    return G(D+n)**2*G(2*D+n-1)/(factorial(n)*G(D)**2*G(2*D+2*n-1))
def p0_d2(n, l, D):  # HPPS (4.2)
    return (1+(-1)**l)*C(n, D)*C(n+l, D)
def p0_d4(n, l, D):  # HPPS (4.29)
    return (1+(-1)**l)*2*(l+1)*(2*D+2*n+l-2)/(D-1)**2*C(n, D-1)*C(n+l+1, D-1)
def cbar2_FK(n, D, h):  # FK (42), Delta1=Delta2=D, calC=1
    return rf(D,n)**2*rf(1+D-h,n)**2/(factorial(n)*rf(h,n)*rf(2*D-2*h+1+n,n)*rf(2*D-h+n,n))
def p0g_544(n, L, D, d):  # HPPS (5.44)
    return (mp.pi**(mpf(d)/2)*2**(2*L)*G(2*D+2*n+L-1)/(G(D)**4*G(1+n)**2*G(2*D+2*n+L-mpf(d)/2))
            *G(2*D+n+L-mpf(d)/2)**2*G(D+n+L)**4/(G(2*D+2*n+2*L)*G(2*D+2*n+2*L-1)))
def g545(n, L, D):
    return mp.pi*G(n+L+1)*G(2*D+n+L-1)*G(D+n-0.5)*G(D+n+L)/(4*G(1+n)*G(D+n)*G(D+n+L+0.5)*G(2*D+n-1))
def g546(n, L, D):
    return mp.pi**2*G(n+L+2)*G(D+n-1.5)*G(D+n+L)*G(2*D+n+L-2)/(16*(1+L)*(D-1)**2*G(n+1)*G(D+n-1)*G(D+n+L+0.5)*G(n+2*D-3))
ok = True
for D in [mpf('1.7'), mpf('2.5'), mpf('3.3')]:
    for n in range(0, 5):
        a = p0_d2(n,0,D)/(2*cbar2_FK(n,D,1)); b = p0_d4(n,0,D)/(2*cbar2_FK(n,D,2))
        r2 = (p0g_544(n,0,D,2)/p0_d2(n,0,D))/g545(n,0,D); r4 = (p0g_544(n,0,D,4)/p0_d4(n,0,D))/g546(n,0,D)
        s2 = (g545(n,0,D)/g545(0,0,D))/((2*D-1)/(2*D+2*n-1))
        s4 = (g546(n,0,D)/g546(0,0,D))/((2*D+n-3)*(n+1)*(D+n-1)*(2*D-1)/((D-1)*(2*D+2*n-3)*(2*D+2*n-1)))
        print(f"D={float(D)} n={n}  p0HPPS/2cbarFK d2={float(a):.12f} d4={float(b):.12f} | (5.44)/p0 vs (5.45)={float(r2):.12f} vs (5.46)={float(r4):.12f} | shape vs (4.13)={float(s2):.12f} (4.34)={float(s4):.12f}")
        for v in (a,b,r2,r4,s2,s4):
            ok &= abs(v-1) < mpf('1e-20')
print("NOTE: ok flag above is False only because d=4 columns give 2.0 / 0.5 (factor-2 normalization), shapes all 1")
# Direct check of p0(0,0) from HPPS (3.10)+(4.1): (z zbar)^D A0 = 1 + (z zbar)^D + ... ; blocks (3.5)/(3.7) both ~ (z zbar)^{E/2} at l=0
for D in [mpf('1.7'), mpf('2.5')]:
    print("p0(0,0): HPPS(4.2) d=2:", mp.nstr(p0_d2(0,0,D),12), " HPPS(4.29) d=4 as printed:", mp.nstr(p0_d4(0,0,D),12), " 2*FK(42) h=2:", mp.nstr(2*cbar2_FK(0,D,2),12), " expected from (4.1): 2")
# General-d L=0 anomalous dimension assembled as (5.44)|_{L=0} / [2 * FK(42)] -- a COMBINATION, not a pinned formula
for d in [2,3,4,5,6]:
    D = mpf('2.5')
    print("d=",d," gamma(n,0)/gamma(0,0), n=0..4, Delta=5/2:", [mp.nstr(p0g_544(n,0,D,d)/(2*cbar2_FK(n,D,mpf(d)/2)) / (p0g_544(0,0,D,d)/(2*cbar2_FK(0,D,mpf(d)/2))),12) for n in range(5)])
