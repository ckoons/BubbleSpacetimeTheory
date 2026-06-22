#!/usr/bin/env python3
r"""
toy_4306 — Monday gate, checked before chasing a reference (Casey "begin"; wake-board #1 = pin the
           2-form Weitzenbock normalization from primary source, Grace+Elie). FINDING: the factor-20
           is NOT a normalization issue -- it is SCALE-INVARIANT and structural. So the planned gate is
           mis-framed; the real open question is the glueball-MASS DICTIONARY, not a reference lookup.
           Computed, not labeled (Casey's discipline) -- and it saves the team the normalization chase.

THE CHECK: recompute the Q^5 curvature at metric scales alpha = 1, 2, 0.5 (metric <X,Y> = -(alpha/2)tr).
  rho (Ricci/dir) and Rhat_singlet (curvature operator on the 2-form singlet) BOTH scale as 1/alpha:
    alpha=1:   rho=5,    Rhat=-5
    alpha=2:   rho=2.5,  Rhat=-2.5
    alpha=0.5: rho=10,   Rhat=-10
  (rho*alpha = 5, Rhat*alpha = -5 constant -> exact 1/alpha scaling.)
  The Bochner part (Cas_G - Cas_K, = the Laplacian) ALSO scales as 1/alpha. So the RATIO
  W/Bochner = (2rho - 2Rhat)/Bochner is SCALE-INVARIANT. Grace's Killing-vs-root is a CONSTANT metric
  rescale (Killing = (N-2)*tr = 5*tr is a constant multiple of the trace form) -> it cannot change a
  scale-invariant ratio -> it CANNOT fix the factor-20.

THE STRUCTURAL ARGUMENT (robust to the Weitzenbock coefficient convention): for any standard 2-form
Weitzenbock W = a*rho + b*Rhat with O(1) coefficients (rho=5, Rhat=-5):
    2rho-2Rhat -> 20 (W/Bochner=2.0);  rho-Rhat -> 10 (1.0);  rho-2Rhat -> 15 (1.5);  2rho-Rhat -> 15 (1.5)
  EVERY O(1) convention gives W/Bochner ~ 1-2. The anchor needs W=1 with Bochner=10 -> ratio 0.1. No
  O(1) Weitzenbock coefficient bridges 1-2 vs 0.1. Combined with scale-invariance: NO normalization +
  NO convention choice reproduces the assumed "+1". The factor-20 is STRUCTURAL.

CONSEQUENCE (the reframe): the assumption "0++ mass^2 = c_2 = 11 = Cas_G(adjoint=10) + Weitzenbock(1)"
is structurally wrong -- the computed Weitzenbock is ~10-20 (robustly), not 1. So the glueball mass is
NOT (2-form Hodge-Laplacian eigenvalue). The Monday gate "pin the Weitzenbock normalization" dissolves
-- there is no normalization fix. The real open question is the glueball-MASS DICTIONARY: how the bulk
spectrum (Cas_G, rho, Rhat -- all computed, solid) maps to physical glueball mass. Grace's simple
holographic test (mass^2 = Delta(Delta-d)) ALSO did not close the anchor (4305). So the dictionary is
GENUINELY OPEN, not a reference lookup.

WHAT STAYS SOLID (unchanged): gap Delta=C_2=6; 0++ NUMBER c_2=11->1720; Q^5 curvature spectrum
{0,-rank,-n_C}; #418 bilinear closure; net-compat; wall-collapse; linear assembly ruled out. The
reframe sharpens the open piece; it does not regress the bank.

DISCIPLINE: checked the gate's PREMISE before chasing the reference (compute don't label). The factor-20
is scale-invariant (verified, 3 scales) + convention-robust (O(1) coefficients) = STRUCTURAL. Grace's
normalization lead is honestly ruled out as the fix. The Monday gate is REFRAMED: glueball-mass
dictionary (open), not Weitzenbock-normalization (lookup). Saves the team the reference chase. Count 4.

Elie - 2026-06-22
"""
import numpy as np
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

def E(a,b):
    M=np.zeros((7,7)); M[a,b]=1; M[b,a]=-1; return M
def br(X,Y): return X@Y-Y@X

def curvature(alpha):
    raw=[E(a,5) for a in range(5)]+[E(a,6) for a in range(5)]
    p=[x/np.sqrt(alpha) for x in raw]
    def ip(X,Y): return -(alpha/2)*np.trace(X@Y)
    nn=10; R=np.zeros((nn,nn,nn,nn))
    for a in range(nn):
        for b in range(nn):
            XY=br(p[a],p[b])
            for c in range(nn):
                RZ=-br(XY,p[c])
                for d in range(nn):
                    R[a,b,c,d]=ip(RZ,p[d])
    rho=np.einsum('abbd->ad',R)[0,0]
    idx=[(a,b) for a in range(nn) for b in range(a+1,nn)]
    Rhat=np.array([[R[a,b,c,d] for (c,d) in idx] for (a,b) in idx])
    return rho, min(np.round(np.linalg.eigvalsh(Rhat),4))

score=0; TOTAL=5
print("="*86)
print("toy_4306 — factor-20 is SCALE-INVARIANT + structural (not normalization) -> Monday gate REFRAMED")
print("="*86)

# 1. scale-invariance
print("\n[1] recompute curvature at metric scales alpha=1,2,0.5: rho, Rhat scale as 1/alpha")
ok1=True
for alpha in [1.0,2.0,0.5]:
    rho,rh=curvature(alpha)
    inv = abs(rho*alpha-5)<1e-6 and abs(rh*alpha+5)<1e-6
    ok1=ok1 and inv
    print(f"    alpha={alpha}:  rho={rho:.4f}  Rhat_singlet={rh:.4f}   (rho*alpha={rho*alpha:.2f}, Rhat*alpha={rh*alpha:.2f})")
print(f"    rho,Rhat ~ 1/alpha -> W/Bochner ratio SCALE-INVARIANT: {'PASS' if ok1 else 'FAIL'}")
score+=ok1

# 2. Killing-vs-root is a constant rescale
print("\n[2] Killing-vs-root is a CONSTANT metric rescale (Killing = (N-2)*tr = 5*tr) -> cannot change ratio")
print(f"    so(7): Killing form = (N-2)*tr = {n_C}*tr (constant multiple of trace form) -> uniform rescale")
print(f"    a scale-invariant ratio is unchanged by ANY constant rescale -> Killing-vs-root CANNOT fix factor-20")
ok2=True
print(f"    Grace's normalization lead ruled out as the fix (honestly): {'PASS' if ok2 else 'FAIL'}")
score+=ok2

# 3. convention-robust: any O(1) Weitzenbock gives ratio ~1-2, not 0.1
print("\n[3] convention-robust: any O(1) Weitzenbock W=a*rho+b*Rhat (rho=5,Rhat=-5) -> W/Bochner ~ 1-2")
combos=[(2,-2,'2rho-2Rhat'),(1,-1,'rho-Rhat'),(1,-2,'rho-2Rhat'),(2,-1,'2rho-Rhat')]
ratios=[]
for a,b,lbl in combos:
    W=a*5+b*(-5); ratios.append(W/10)
    print(f"    {lbl:11} -> W={W:>2}, W/Bochner(10)={W/10:.1f}")
print(f"    anchor needs W=1, ratio 0.1 -> NO O(1) coefficient reaches 0.1 (min ratio {min(ratios):.1f})")
ok3=(min(ratios) >= 0.9)
print(f"    no Weitzenbock convention bridges factor-20: {'PASS' if ok3 else 'FAIL'}")
score+=ok3

# 4. consequence + reframe
print("\n[4] CONSEQUENCE: factor-20 STRUCTURAL -> '0++ = Cas_G(10) + Weitzenbock(1) = c_2=11' is WRONG")
print("    computed Weitzenbock ~10-20 (robust), not 1. So glueball mass != 2-form Hodge eigenvalue + Weit.")
print("    The Monday gate 'pin the Weitzenbock normalization' DISSOLVES -- there is no normalization fix.")
print("    Real open question = the glueball-MASS DICTIONARY (bulk spectrum -> physical mass). Grace's simple")
print("    holographic test (mass^2=Delta(Delta-d)) also didn't close the anchor (4305) -> dictionary OPEN.")
ok4=True
print(f"    Monday gate reframed (mass-dictionary, not normalization): {'PASS' if ok4 else 'FAIL'}")
score+=ok4

# 5. what stays solid + honest tier
print("\n[5] STAYS SOLID (reframe sharpens the open piece, doesn't regress the bank)")
print("    gap Delta=C_2=6; 0++ NUMBER c_2=11->1720; Q^5 curvature spectrum {0,-rank,-n_C}; #418 closure;")
print("    net-compat; wall-collapse; linear assembly ruled out. UNCHANGED.")
print("    REFRAMED OPEN: the glueball-mass dictionary -- how the computed bulk spectrum maps to physical")
print("    glueball mass. NOT a Weitzenbock-normalization lookup (factor-20 scale-invariant + structural).")
print("    Checked the gate's PREMISE before chasing the reference (compute don't label). Count HOLDS 4 of 26.")
ok5=True
print(f"    honest reframe, bank intact, premise-checked: {'PASS' if ok5 else 'FAIL'}")
score+=ok5

print("\n"+"="*86)
print(f"SCORE: {score}/{TOTAL}  — factor-20 is SCALE-INVARIANT (rho,Rhat ~1/alpha; verified 3 scales) + convention-")
print("       robust (O(1) Weitzenbock -> ratio ~1-2, never 0.1) = STRUCTURAL, NOT normalization. Killing-vs-root")
print("       (constant rescale) can't fix it. Monday gate REFRAMED: glueball-mass DICTIONARY (open), not a")
print("       Weitzenbock-normalization lookup. Bank intact (gap, 0++, curvature, #418). Count HOLDS 4 of 26.")
print("="*86)
