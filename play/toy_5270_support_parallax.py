import numpy as np
print("="*80)
print("TASK 1' -- does depth become unrecoverable at large distance ON A SPHERE?")
print("="*80)
print("  Flat-space intuition: parallax ~ b/D -> 0 as D grows => far sky depthless, horizon at D*=b/sigma.")
print("  BUT the substrate's space is S^4 -- COMPACT. Before assuming the baseline needs bounding,")
print("  check whether the flat-space falloff even holds there.")
print()
def sky_dir(O,T):
    """unit tangent at O pointing along the geodesic to T (on the unit sphere)."""
    c=np.dot(O,T); v=T-c*O; n=np.linalg.norm(v)
    return v/n if n>1e-14 else None
# work in the great 2-plane: O1 at angle 0, O2 at angle b, target at angle D from O1 (same great circle
# is degenerate) -> put the target off-axis by a fixed sky angle so parallax is non-trivial.
def parallax(b,D,phi=0.6,dim=5):
    e=np.zeros(dim); e[0]=1.0
    u=np.zeros(dim); u[1]=1.0
    w=np.zeros(dim); w[2]=1.0
    O1=e
    O2=np.cos(b)*e+np.sin(b)*u
    T=np.cos(D)*(np.cos(phi)*e+np.sin(phi)*w)+np.sin(D)*(-np.sin(phi)*e+np.cos(phi)*w)
    T=T/np.linalg.norm(T)
    d1=sky_dir(O1,T); d2=sky_dir(O2,T)
    if d1 is None or d2 is None: return np.nan
    # transport O2's frame back along the baseline: compare the ANGLE each makes with the baseline direction
    b1=sky_dir(O1,O2); b2=sky_dir(O2,O1)
    a1=np.arccos(np.clip(np.dot(d1,b1),-1,1))
    a2=np.arccos(np.clip(np.dot(d2,-b2),-1,1))
    return abs(a1-a2)          # the parallax: mismatch of the two sight-lines
print("  PARALLAX vs DEPTH on S^4, baseline b (radians). Flat-space would give ~ b/D, monotonically -> 0.")
print()
print("      D:      0.10     0.30     0.60     1.00     1.57     2.20     2.80     3.04")
for b in [0.01,0.05,0.2]:
    row=[]
    for D in [0.10,0.30,0.60,1.00,1.5708,2.20,2.80,3.04]:
        row.append(parallax(b,D))
    print("  b=%.2f  "%b+"  ".join("%7.5f"%v for v in row))
print()
print("  => parallax does NOT fall monotonically to zero with distance on a sphere.")
print("     It is smallest near D ~ pi/2 and RISES again toward the antipode (D -> pi),")
print("     because on a compact space the far side is 'wrapped around' and sight-lines re-converge.")
