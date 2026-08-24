# TOY 5477 -- map-pin control, 18-map sweep. RAN INLINE ~07:30, persisted post-hoc same morning.
# *** STATUS: VOID (toy 5478 / Keeper's audit) -- the must-catch conflated measure degeneration
# with lambda+rho singularity. Kept on disk as the record of WHAT ran, per Keeper's request. ***
from fractions import Fraction as F
rho=(F(5,2),F(3,2),F(1,2))
NONC=[(1,-1,0),(1,0,-1),(1,0,0),(1,0,1),(1,1,0)]
def pairings(lam):
    lp=tuple(lam[k]+rho[k] for k in range(3))
    return sorted(sum(lp[k]*F(b[k]) for k in range(3)) for b in NONC)
def q_of(lam):
    ps=pairings(lam)
    if any(p==0 for p in ps): return None
    return sum(1 for p in ps if p<0)
scalar=lambda c:(F(c),F(0),F(0)); spinor=lambda c:(F(c),F(1,2),F(1,2))
print("VOIDED SWEEP (record): legs were Wallach{0,3/2}->walls (CONFLATION), Hardy off-wall, q(Hardy)=0")
for s in [F(0),F(1,2),F(1),F(3,2),F(2),F(5,2),F(3),F(7,2),F(4)]:
    for sg in (1,-1):
        cmap=lambda e0: sg*F(e0)-s if sg==1 else -F(e0)+s
        onw=lambda c: q_of(scalar(c)) is None
        ok=(onw(cmap(0)) and onw(cmap(F(3,2))) and not onw(cmap(F(5,2))) and q_of(scalar(cmap(F(5,2))))==0)
        if ok: print("  survivor (void): c = %sE0 - %s"%("+" if sg==1 else "-",s))
print("Unique survivor was c = E0 - 5/2. VOID: its must-catch tested the wrong reduction notion.")
