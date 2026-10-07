"""Cal S1033 -- checks behind the K4-2 kill lines (write event). Plain Python, exact (fractions)."""
from fractions import Fraction as Fr
import itertools
ok=n=0
def check(s,c):
    global ok,n; n+=1; ok+=bool(c); print(("PASS " if c else "FAIL ")+s)
# 1. free e + gamma -> e is kinematically forbidden: s = m^2 + 2 m w > m^2 for any w > 0 (electron rest frame, c=1)
m=Fr(1)
check("free-electron one-photon absorption forbidden: s = m^2+2mw != m^2 for w in {1e-6,1,10} (units of m)",
      all(m*m+2*m*Fr(w) != m*m for w in (Fr(1,10**6),Fr(1),Fr(10))))
# recoil must go somewhere: required third-body momentum transfer for a bound electron is real; the record/boundary
# would have to carry 4-momentum if no third body is named.
# 2. QED vertex count decoy: electron spin 2 x photon helicity 2 = 4 in-states (the '4 = 2x2' KL-W1 rejects without a map)
check("generic vertex in-state count 2x2 = 4 (decoy)",2*2==4)
# 3. E1 control content: l -> l', m -> m' allowed iff |l'-l| = 1 and |m'-m| <= 1 ; count transitions from l=1,m=0
allowed=[(lp,mp) for lp in range(0,4) for mp in range(-lp,lp+1) if abs(lp-1)==1 and abs(mp)<=1]
print("E1 targets from (l=1,m=0):",allowed)
check("E1 from (1,0): 4 targets = (0,0) + three (2,m) -- another 3 (the Δm values)",len(allowed)==4)
# 4. the threes on the table: seven K4 (S1030) + write-event generics
threes=["K4 cycle rank","Hamiltonian cycles","perfect matchings","degree","face size","faces per vertex","|S4/V4|",
        "photon spin-1 m states (2 physical, 3 off-shell)","Δm values","3-vector components","energy + two angles","spatial D"]
check("at least 12 threes on the table: 'a 3 appears' has can-fail count 0",len(threes)>=12)
# 5. coordinate-freeness: the three components of a 3-vector are COORDINATES (basis-dependent); S3 acting on them is a
# signed-permutation subgroup of SO(3) that exists only after a frame is chosen. A rotation mixes them continuously.
import math
c,s=math.cos(0.3),math.sin(0.3); v=(1.0,0.0,0.0); Rv=(c*v[0]-s*v[1],s*v[0]+c*v[1],v[2])
check("a rotation changes the 'three values' of one momentum continuously (values are coordinates, not a word)",Rv!=v)
print(f"SCORE {ok}/{n}")
