# TOY 5478 -- concession + identity + the two-map theorem. RAN INLINE, persisted post-hoc.
from fractions import Fraction as F
from itertools import permutations
rho=(F(5,2),F(3,2),F(1,2))
NONC=[(1,-1,0),(1,0,-1),(1,0,0),(1,0,1),(1,1,0)]
def q_of(lam):
    lp=tuple(lam[k]+rho[k] for k in range(3))
    ps=[sum(lp[k]*F(b[k]) for k in range(3)) for b in NONC]
    if any(p==0 for p in ps): return None
    return sum(1 for p in ps if p<0)
spinor=lambda c:(F(c),F(1,2),F(1,2))
def d_formal(nu): return (F(5,2)-nu)*(1-nu)*(2-nu)*(3-nu)*(4-nu)
assert d_formal(F(0))==60 and d_formal(F(3,2))==F(-15,16) and d_formal(F(5,2))==0
print("d(0)=60, d(3/2)=-15/16, d(5/2)=0 -- Wallach points are NOT d-zeros. 5477 must-catch conceded.")
Z=[F(1),F(2),F(5,2),F(3),F(4)]; W=[F(-1),F(-2),F(-5,2),F(-3),F(-4)]
sols=set()
for perm in permutations(W):
    a=(perm[1]-perm[0])/(Z[1]-Z[0]); b=perm[0]-a*Z[0]
    if all(a*Z[k]+b==perm[k] for k in range(5)): sols.add((a,b))
print("Affine maps d-zeros -> walls: %s  (exactly two: c=-nu, c=nu-5, differing by Lyra's conjugation)"
      %sorted(sols))
for c in [F(0),F(-1),F(-2),F(-4),F(1),F(-6)]:
    assert q_of(spinor(c))+q_of(spinor(F(-5)-c))==5
print("q(c)+q(-5-c)=5 verified off-wall => relative parity branch-independent => (ii) unblocked.")
