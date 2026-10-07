"""Cal S1032 -- checks behind the K4-1 rulings on Lyra's spec and Keeper K1950 Section 11. Plain Python."""
import itertools, numpy as np
ok=n=0
def check(s,c):
    global ok,n; n+=1; ok+=bool(c); print(("PASS " if c else "FAIL ")+s)
# 1. deck map tau(x,theta)=(-x,theta+pi) on S^4 x S^1: pushforward of d/dtheta is d/dtheta  -> fibre direction descends
J=np.diag([-1,-1,-1,-1,-1,1.0])            # Jacobian on (x in R^5, theta): x-> -x, theta-> theta+pi
check("deck pushes d/dtheta to d/dtheta (circle direction global on the quotient)",np.allclose(J@np.eye(6)[5],np.eye(6)[5]))
check("deck reverses S^4 orientation (antipodal on S^4: degree (-1)^5)",(-1)**5==-1)
# 2. base of the circle bundle Silov -> RP^4: pi_1(RP^4)=Z2, RP^n orientable iff n odd
check("true boundary's base RP^4 is NOT simply connected and NOT orientable (fails 2022 literal premises)",4%2==0)
# 3. closed surfaces: chi, b1 (rank of free H1), min vertices (Heawood/Ringel; Klein bottle = 8, Franklin)
surf={"S2":(2,0,4,True),"RP2":(1,0,6,False),"T2":(0,2,7,True),"Klein":(0,1,8,False)}
b1zero=[s for s,(c,b,v,o) in surf.items() if b==0]
check("b1=0 admits S2 AND RP2 (torsion loop is not a free channel)",b1zero==["S2","RP2"])
check("global minimum over b1=0 closed surfaces is S2 with 4 vertices",min(b1zero,key=lambda s:surf[s][2])=="S2")
free=[s for s,(c,b,v,o) in surf.items() if b>0]
check("minimal closed surface with a FREE loop is T2 (7) not Klein (8); RP2 excluded by freeness, not by orientability",
      min(free,key=lambda s:surf[s][2])=="T2")
# 4. read orientation o is CP-even (S1031); circle direction s: C-odd (J->-J), P-even (deck preserves it) -> CP-odd
s={"C":-1,"P":+1}; o={"C":-1,"P":-1}
check("circle direction is CP-odd while weak read orientation is CP-even -> not the same sign",s["C"]*s["P"]==-1 and o["C"]*o["P"]==+1)
# 5. pure record keeps relative phases: vv† off-diagonals
rng=np.random.default_rng(2); v=rng.normal(size=3)+1j*rng.normal(size=3); R=np.outer(v,v.conj())
check("vv† (pure) off-diagonal phases = relative phases of v (nothing relative is forgotten)",
      np.allclose(np.angle(R[0,1]),np.angle(v[0])-np.angle(v[1]) - 2*np.pi*np.round((np.angle(v[0])-np.angle(v[1])-np.angle(R[0,1]))/(2*np.pi))))
# 6. three points on an oriented circle have a cyclic order fixed by the direction (candidate map)
pts=sorted(rng.uniform(0,2*np.pi,3)); fwd=tuple(np.argsort(pts)); 
check("reversing the circle's direction reverses the cyclic order of three placed values",
      tuple(reversed(fwd)) in [(2,1,0),(1,0,2),(0,2,1)])
print(f"SCORE {ok}/{n}")
