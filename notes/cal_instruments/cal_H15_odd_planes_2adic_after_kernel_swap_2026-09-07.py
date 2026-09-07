# Cal, H15 (fixed norm rule): 2-adic rank-one intertwining integral on the ODD plane <1,-1> with the swapped kernel K = <1,1,3> (isotropic at 2).
# Shell |v| = 2^mm, j = val q0(u): norm = max(2^mm, 2^{2mm+2-j}) for j <= 2mm+1; = 2^mm for j >= 2mm+2 (mm>=0). mm=-1: j=0 -> 1/2, j>=1 -> 1. mm<=-2: 1.
from fractions import Fraction as F
K=12
def dist_form(k):
    M=1<<k; sq=[0]*M; sq3=[0]*M
    for a in range(M): sq[(a*a)&(M-1)]+=1; sq3[(3*a*a)&(M-1)]+=1
    def conv(a,b):
        c=[0]*M
        for i,x in enumerate(a):
            if x==0: continue
            for j,y in enumerate(b):
                if y: c[(i+j)&(M-1)]+=x*y
        return c
    return conv(conv(sq,sq),sq3)
def zero_count(k): return 1 if k==0 else dist_form(k)[0]
def prim_frac(j):
    if j==0: return F(1)
    total=zero_count(j); nonprim=zero_count(j-2)*8 if j>=2 else 1
    return F(total-nonprim,7*8**(j-1))
ps=[prim_frac(j) for j in range(K+1)]
j0=3; r=ps[j0+1]/ps[j0]
def Pge(j): return ps[j] if j<=K else ps[j0]*r**(j-j0)
def Peq(j): return Pge(j)-Pge(j+1)
N=70; coef={}
def add(e,c): coef[e]=coef.get(e,F(0))+c
add(0,F(1,64)); add(-1,F(7,64)*Peq(0)); add(0,F(7,64)*Pge(1))
for mm in range(0,N+2):
    mu=F(7,8)*F(8)**mm
    for j in range(0,2*mm+2):
        e=max(2*mm+2-j, mm)
        if e<=N: add(e,mu*Peq(j))
    if mm<=N: add(mm,mu*Pge(2*mm+2))
emin=min(coef); s=[coef.get(e,F(0)) for e in range(emin,N+1)]
def minrec(seq):
    for L in range(1,12):
        for start in range(0,12):
            A=[[seq[n-i] for i in range(1,L+1)]+[seq[n]] for n in range(start+L,start+2*L)]; ok=True
            for c in range(L):
                piv=next((r_ for r_ in range(c,L) if A[r_][c]!=0),None)
                if piv is None: ok=False;break
                A[c],A[piv]=A[piv],A[c]; A[c]=[v/A[c][c] for v in A[c]]
                for r_ in range(L):
                    if r_!=c and A[r_][c]!=0: A[r_]=[x-A[r_][c]*w for x,w in zip(A[r_],A[c])]
            if not ok: continue
            rv=[A[i][L] for i in range(L)]
            if all(seq[t]==sum(rv[i-1]*seq[t-i] for i in range(1,L+1)) for t in range(start+2*L,len(seq))):
                return L,start,rv
    return None
L,start,rv=minrec(s)
import sympy as sp
y=sp.symbols('y')
D=1-sum(sp.Rational(rv[i].numerator,rv[i].denominator)*y**(i+1) for i in range(L))
S=sum(sp.Rational(c.numerator,c.denominator)*y**k for k,c in enumerate(s[:start+L+2]))
Npoly=sp.expand(D*S); Npoly=sum(Npoly.coeff(y,k)*y**k for k in range(0,start+L+1))
print("P(val>=j):",[str(p) for p in ps[:6]],"... geometric ratio 1/2 from j=3")
print("c_2^{odd,<1,1,3>} = y^(%d) * N(y)/D(y):  N = %s ;  D = %s"%(emin,sp.factor(Npoly),sp.factor(D)))
z=sp.symbols('z')
c_odd=(y**emin*Npoly/D).subs(y, z/(2*sp.sqrt(2)))
GK=(1-z**2/2)*(1-z/(2*sp.sqrt(2)))/((1-z**2)*(1-sp.sqrt(2)*z))
print("R(z) = c_odd/GK_split (z = 2^{-lambda}; constants/monomials aside) =", sp.factor(sp.simplify(c_odd/GK)))
