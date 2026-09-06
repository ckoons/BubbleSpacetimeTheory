# Independent instrument for T2619: Lambda(s) = pi^{-s} Gamma(s) Z_{Z^5}(s), Z = sum' |x|^{-2s} = sum r_5(N) N^{-s}.
# Riemann's split: Lambda(s) = int_1^inf (theta^5(t)-1)(t^s + t^{5/2-s}) dt/t - 1/s - 1/(5/2-s), theta(t)=sum_n e^{-pi n^2 t}.
# Converges for all s (entire apart from the two poles). Evaluate at Elie's certified zero and neighbours; winding on a small box.
from mpmath import mp, mpf, mpc, exp, pi, quad, gamma, log, arg, fsum, nstr
mp.dps = 40
def theta(t):
    s = mpf(1); n = 1
    while True:
        term = 2*exp(-pi*n*n*t)
        if term < mpf(10)**(-mp.dps-5): break
        s += term; n += 1
    return s
def Lam(s):
    f = lambda t: (theta(t)**5 - 1)*(t**s + t**(mpf(5)/2 - s))/t
    I = quad(f, [1, 2, 4, 8, 16, 40, mp.inf])
    return I - 1/s - 1/(mpf(5)/2 - s)
z = mpc('2.5035899876435054856', '14.279995705512019903')
print("Lambda at Elie's zero :", nstr(abs(Lam(z)), 5))
for d in [mpc('0.01',0), mpc(0,'0.01'), mpc('-0.01',0), mpc(0,'-0.01')]:
    print("  neighbour", nstr(d,3), ":", nstr(abs(Lam(z+d)), 5))
# winding number on a 0.02-box around z
pts=[]; h=mpf('0.01'); n=16
corners=[z+mpc(-h,-h), z+mpc(h,-h), z+mpc(h,h), z+mpc(-h,h)]
vals=[]
for i in range(4):
    a,b=corners[i],corners[(i+1)%4]
    for k in range(n):
        vals.append(Lam(a+(b-a)*k/n))
tot=0
for i in range(len(vals)):
    d=arg(vals[(i+1)%len(vals)]/vals[i]); tot+=d
print("winding number on 0.02-box:", nstr(tot/(2*pi),6))
# control: Lambda(s) real on the critical line Re s = 5/4? check symmetry Lam(s) = Lam(5/2 - s)
w = mpc('1.25','7'); print("FE check |Lam(s)-Lam(5/2-s)| at 5/4+7i:", nstr(abs(Lam(w)-Lam(mpf(5)/2-w)),5), " |Lam|=", nstr(abs(Lam(w)),5))
# coefficient control: Z(4) from the Dirichlet series vs Lambda(4)*pi^4/Gamma(4)
import itertools
def r5(N):
    c=0; R=int(N**0.5)+1
    for x in itertools.product(range(-R,R+1),repeat=4):
        t=sum(v*v for v in x)
        if t<=N:
            w2=N-t; w=int(round(w2**0.5))
            if w*w==w2: c += 2 if w>0 else 1
    return c
Zd = fsum(mpf(r5(N))/mpf(N)**4 for N in range(1,61))
print("Z(4) partial N<=60:", nstr(Zd,12), " from Lambda:", nstr(Lam(mpf(4))*pi**4/gamma(4),12))
