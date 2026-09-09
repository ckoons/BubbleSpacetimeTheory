# Cal R137: Lyra L2 says "the Hua branching, the 3/7 word, k_max and the j-blind theorem depend only on the
# K-decomposition and not on a norm, so they survive the weight question." Elie E4 says the split moves with nu.
# Adjudicate. Reconstruct L_nu, M_nu from Lyra's own c_nu and check against Elie's printed numbers, then ask:
#   (1) is the branching RATIO M/(L+M) j-dependent at nu_B = 5?   (2) does the 3/7 word move?
from fractions import Fraction as F
def L(j,k,nu):  return F(k+3,2*k+3) * F(2*(j+k)+5, 2*(j+k+nu.numerator//nu.denominator if False else 0)+0) if False else F(k+3,2*k+3)*(F(2*(j+k)+5,2)/ (F(j+k)+nu))
def M(j,k,nu):  return F(k,2*k+3)*(F(2*j+2,1)/(F(2*j,1)+2*nu-3))
def c(j,k,nu):  return 1 - L(j,k,nu) - M(j,k,nu)
nuS, nuB = F(5,2), F(5)
print("control vs Lyra's closed form c_nu(j,0) = (nu-5/2)/(j+nu):")
for nu in (F(3,2),nuS,F(4),nuB,F(10)):
    print("  nu=%-4s  c(0,0)=%-8s closed %-8s | c(3,0)=%-8s closed %s" %
          (nu, c(0,0,nu), (nu-F(5,2))/(0+nu), c(3,0,nu), (nu-F(5,2))/(3+nu)))
print("\ncontrol vs Elie E4 split M/(L+M) at (0,1):  nu = 5, 4, 3, 5/2, 2  (he printed .1091 .1250 .1600 .2000 .3000)")
print("  " + "  ".join("%.4f" % (M(0,1,nu)/(L(0,1,nu)+M(0,1,nu))) for nu in (F(5),F(4),F(3),F(5,2),F(2))))
print("\n(1) is the branching RATIO j-dependent?   matter share M/(L+M) at k=1, j=0..4")
for nu,name in ((nuS,"nu_S=5/2 (Hardy)"),(nuB,"nu_B=5 (Bergman)")):
    print("  %-18s" % name, "  ".join("%.5f" % (M(j,1,nu)/(L(j,1,nu)+M(j,1,nu))) for j in range(5)),
          " -> j-blind?", len({M(j,1,nu)/(L(j,1,nu)+M(j,1,nu)) for j in range(5)})==1)
print("\n(2) the three-write word: P(exactly one matter step in the first three writes from the vacuum)")
def word(nu):
    # states carry probability; at each write branch light (j,k+1) or matter (j+1,k-1), renormalised by L+M
    from collections import defaultdict
    st={(0,0,0):F(1)}
    for _ in range(3):
        nxt=defaultdict(F)
        for (j,k,m),p in st.items():
            l,mm = L(j,k,nu), M(j,k,nu); tot=l+mm
            nxt[(j,k+1,m)] += p*l/tot
            if k>0: nxt[(j+1,k-1,m+1)] += p*mm/tot
        st=nxt
    return sum(p for (j,k,m),p in st.items() if m==1)
for nu,name in ((nuS,"nu_S=5/2"),(nuB,"nu_B=5"),(F(4),"nu=4"),(F(10),"nu=10")):
    w=word(nu); print("  %-10s P = %-12s = %.6f    (3/7 = %.6f)" % (name,w,float(w),3/7))
