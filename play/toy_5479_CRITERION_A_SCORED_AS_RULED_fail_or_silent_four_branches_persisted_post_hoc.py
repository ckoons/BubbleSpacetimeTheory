# TOY 5479 -- criterion (a) scored per Keeper's R82 ruling. RAN INLINE, persisted post-hoc.
from fractions import Fraction as F
rho=(F(5,2),F(3,2),F(1,2))
NONC=[(1,-1,0),(1,0,-1),(1,0,0),(1,0,1),(1,1,0)]
def q_of(lam):
    lp=tuple(lam[k]+rho[k] for k in range(3))
    ps=[sum(lp[k]*F(b[k]) for k in range(3)) for b in NONC]
    if any(p==0 for p in ps): return None
    return sum(1 for p in ps if p<0)
spinor=lambda c:(F(c),F(1,2),F(1,2))
for name,f in [("A+",lambda e:F(e)-F(5,2)),("A-",lambda e:-F(e)-F(5,2)),
               ("B+",lambda e:-F(e)),("B-",lambda e:F(e)-F(5))]:
    q=q_of(spinor(f(2)))
    print("  %s: c(E0=2)=%s -> %s"%(name,f(2),"WALL (P4 silent)" if q is None else "q=%d"%q))
print("SCORE (a): FAIL-OR-SILENT under every surviving map; mode family-dependent; CLOSED.")
