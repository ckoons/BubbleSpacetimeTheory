#!/usr/bin/env python3
"""
Toy 5807 (Lyra, round 6 item 1, 2026-09-26). Invariant first: the SO(2)-centre weight of K (J, the
elliptic element) on each K-finite module; SO(4) = stab of a real unit vector in SO(5); SO(4)-types
(i/2,i/2). Scalar module H_nu(D_IV^n): K-types = harmonic degree a times q^b, SO(n)-type (a,0), J-weight
nu + a + 2b (b >= 0; at the Wallach point nu=(n-2)/2 only b = 0).  Predictions written BEFORE the run:
 Q1  min spec J on H^2(D_IV^5) (nu = 5/2) is 5/2; on the minimal rep Rac (nu = 3/2) it is 3/2.  Two objects.
 Q2  exp(2 pi i J) = -1 on EVERY K-type of H^2 and of Rac (one half-integer coset each).
 Q3  CONTROL (can fail the TD 'Bergman' label): the Bergman module (nu = genus = 5) has integer weights,
     exp(2 pi i J) = +1 on every K-type  => calling the substrate 'Bergman' would kill the double cover.
 Q4  Theorem B (09-14) at character level: char H^2 = sum_{b>=0} char Rac * t^{1+2b}.
 Q5  K1927(c): Rac_5 | SO(4)xSO(2) = H_{3/2}(D_IV^4) + H_{5/2}(D_IV^4) (K-characters, weight <= 40).
 Q6  H^2_5 | SO(4)xSO(2) = sum_{k>=0} H_{5/2+k}(D_IV^4) (K-characters, weight <= 40).
 Q7  Shared SO(4,2) summand: H_{5/2}(D_IV^4) occurs once in Rac| and once in H^2|; nothing else is shared
     at k-level; and NO SO(5,2)-map Rac -> H^2 (lowest J-weights differ, both irreducible: Schur).
SCORE over Q1..Q7.
"""
from fractions import Fraction as F
from collections import Counter
W=40; ok=[]
def mod5(nu,wall=False):   # K-types of H_nu(D_IV^5) branched to SO(4): (i, weight) -> mult
    c=Counter()
    for a in range(W+1):
        for b in range(0 if True else 0, (1 if wall else W+1)):
            w=nu+a+2*b
            if w>W: break
            for i in range(a+1): c[(i,w)]+=1
    return c
def mod4(nu,wall=False):
    c=Counter()
    for i in range(W+1):
        for m in range(1 if wall else W+1):
            w=nu+i+2*m
            if w>W: break
            c[(i,w)]+=1
    return c
H2=mod5(F(5,2)); Rac=mod5(F(3,2),wall=True); Berg=mod5(F(5))
Q1=min(w for _,w in H2)==F(5,2) and min(w for _,w in Rac)==F(3,2); ok.append(Q1); print("Q1 min J: H2",min(w for _,w in H2)," Rac",min(w for _,w in Rac),"->",Q1)
half=lambda C: all(w.denominator==2 for _,w in C)
Q2=half(H2) and half(Rac); ok.append(Q2); print("Q2 all weights half-integer (exp 2pi iJ=-1) on H2 and Rac ->",Q2)
Q3=all(w.denominator==1 for _,w in Berg); ok.append(Q3); print("Q3 Bergman nu=5 all integer (exp 2pi iJ=+1) ->",Q3)
# Q4: SO(5)-level characters
def so5(nu,wall=False):
    c=Counter()
    for a in range(W+1):
        for b in range(1 if wall else W+1):
            if nu+a+2*b<=W: c[(a,nu+a+2*b)]+=1
    return c
R5=so5(F(3,2),True); H5=so5(F(5,2)); T=Counter()
for (a,w),m in R5.items():
    for b in range(W):
        if w+1+2*b<=W: T[(a,w+1+2*b)]+=m
Q4=(T==H5); ok.append(Q4); print("Q4 char H2 = char Rac x odd clock ->",Q4)
Q5=(Rac==mod4(F(3,2))+mod4(F(5,2))); ok.append(Q5); print("Q5 Rac| = H_3/2(D4)+H_5/2(D4) ->",Q5)
S=Counter()
for k in range(W): S+=mod4(F(5,2)+k)
Q6=(H2==S); ok.append(Q6); print("Q6 H2| = sum_k H_{5/2+k}(D4) ->",Q6)
rac_summ={F(3,2),F(5,2)}; h2_summ={F(5,2)+k for k in range(W)}
Q7=(rac_summ&h2_summ=={F(5,2)}) and min(w for _,w in Rac)!=min(w for _,w in H2); ok.append(Q7)
print("Q7 shared D4 summands:",sorted(rac_summ&h2_summ),"; lowest weights differ -> no SO(5,2) map ->",Q7)
print(f"SCORE {sum(ok)}/{len(ok)}")
