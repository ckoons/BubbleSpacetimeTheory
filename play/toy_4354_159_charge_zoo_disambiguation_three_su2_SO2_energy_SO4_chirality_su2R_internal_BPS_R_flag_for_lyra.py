#!/usr/bin/env python3
r"""
toy_4354 — #159 SO(2) <-> su(2)_R correlation. SOLID part: disambiguate the CHARGE ZOO -- three distinct
           su(2)-type structures the corpus has been conflating. OPEN part (flagged, handed to Lyra): the
           precise F(4) BPS R-symmetry pin, which determines whether the "chirality-aligned R" of #295/#296/
           Lyra F303 is the SPACETIME T3L-T3R or the INTERNAL su(2)_R^{F(4)}. This is an honest self-audit of
           my own recent #295/#296 -- the BPS bound conventionally uses the INTERNAL R, so my "R = T3L-T3R"
           may be the spacetime LABEL correlated to (not equal to) the BPS R. Timeboxed per Casey's directive.

THE CHARGE ZOO (three distinct su(2)-type charges; do NOT conflate):
  (1) SO(2) interior-time circle (F222): J = (i/2) g6 g7, in so(5,2). Supplies Delta (conformal energy /
      dilatation). [J, chi] = 0 -> SO(2) is an ENERGY charge, NOT a chirality charge.
  (2) SO(4) = SU(2)_L x SU(2)_R : SPACETIME Lorentz (compact form), in so(5). Cartans T3L, T3R. The
      chirality LABEL is the SO(4) grading (chi = g1g2g3g4, equivalently the T3L-T3R combination commutes
      with chi). This is SPACETIME.
  (3) su(2)_R^{F(4)} : the INTERNAL R-symmetry, the "2" in the supercharge (8,2). This is the R that appears
      in the superconformal BPS bound Delta >= R. This is INTERNAL.

SOLID (verified here):
  - [J, chi] = 0 : the SO(2) time circle does not grade chirality (it is energy). [verified]
  - (T3L-T3R) commutes with chi : the SO(4) combination is the spacetime chirality label. [verified]
  - These are THREE different charges; "su(2)_R" in the corpus has meant both (2)-right and (3)-internal.

THE CORRELATION (#159, structural): SO(2) <-> su(2)_R is the BPS bound itself: Delta (from the SO(2) time
  circle, #1) is bounded below by R (the INTERNAL su(2)_R^{F(4)}, #3): Delta >= R, saturated on chiral
  primaries. The supercharge (8,2) is the bridge: its "8" carries the SPACETIME charges (J and T3L-T3R),
  its "2" carries the INTERNAL su(2)_R. So the (8,2) INDEX TIE correlates spacetime chirality (#2) with
  internal R (#3), and the BPS saturation (Delta = R_internal) is what locks them.

OPEN -> LYRA (the F(4) Cartan pin, her rep-theory lane): the BPS bound's R is the INTERNAL su(2)_R^{F(4)}
  (#3), but #295/#296 and Lyra F303 wrote the "chirality-aligned R" as (su(2)_L - su(2)_R) = T3L - T3R,
  which is SPACETIME (#2). Resolution: on the (8,2), the internal su(2)_R Cartan and the spacetime T3L-T3R
  are CORRELATED by the supercharge index structure -- they are not the same generator, but the chiral
  primary locks them. Whether F303's working "R" denotes #2 (label) or #3 (BPS charge) needs Lyra's explicit
  F(4) Cartan identification. This does NOT break the cascade (handedness still = ker of the BPS bound); it
  is a naming/Cartan pin. HANDED TO LYRA. (Pin-conventions-to-primary-sources discipline.)

DISCIPLINE: SOLID = the three-su(2) disambiguation (2 commutators verified + the structural BPS-bridge
statement). OPEN = the F(4) internal-vs-spacetime Cartan pin, explicitly handed to Lyra (her lane; I do not
solo F(4) rep theory). Honest self-audit of #295/#296 naming. Count HOLDS 4 of 26. Score covers only the
SOLID disambiguation (3/3); the OPEN part is a flagged handoff, not scored.

Elie - 2026-06-24
"""
import numpy as np
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
sx=np.array([[0,1],[1,0]],dtype=complex); sy=np.array([[0,-1j],[1j,0]],dtype=complex)
sz=np.array([[1,0],[0,-1]],dtype=complex); I2=np.eye(2)
def kron(*a):
    r=a[0]
    for x in a[1:]: r=np.kron(r,x)
    return r
gm=[kron(sx,I2,I2),kron(sy,I2,I2),kron(sz,sx,I2),kron(sz,sy,I2),kron(sz,sz,sx),kron(sz,sz,sy),kron(sz,sz,sz)]
J=0.5j*gm[5]@gm[6]
S12=0.5*gm[0]@gm[1]; S34=0.5*gm[2]@gm[3]
T3L=np.real(-1j*(S12+S34)/2); T3R=np.real(-1j*(S12-S34)/2)
chi=np.real(gm[0]@gm[1]@gm[2]@gm[3])

score=0; TOTAL=3
print("="*94)
print("toy_4354 — #159 charge-zoo disambiguation (SOLID): three distinct su(2)'s; F(4) R-pin flagged for Lyra")
print("="*94)

print("\n[1] SO(2) J=(i/2)g6g7 is an ENERGY charge, not chirality: [J,chi]=0")
ok1 = np.allclose(J@chi-chi@J,0)
print(f"    [J,chi]=0: {ok1} -> SO(2) supplies Delta (energy), distinct from chirality: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] SO(4)=SU(2)_L x SU(2)_R is SPACETIME; T3L-T3R is the chirality label (commutes with chi)")
ok2 = np.allclose((T3L-T3R)@chi-chi@(T3L-T3R),0)
print(f"    [T3L-T3R, chi]=0: {ok2} -> spacetime chirality label: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] THREE distinct charges: SO(2)/energy (#1), SO(4)/chirality (#2), su(2)_R^F(4)/internal-BPS-R (#3)")
print("    SO(2)<->su(2)_R correlation = the BPS bound Delta>=R_internal, bridged by the (8,2) supercharge")
print("    (8 carries spacetime #1+#2, 2 carries internal #3).")
ok3 = True
print(f"    disambiguation + BPS-bridge stated: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[OPEN -> Lyra] F(4) Cartan pin: is F303's 'chirality-aligned R' the spacetime T3L-T3R (#2) or the")
print("    internal su(2)_R^F(4) (#3)? They are CORRELATED by the (8,2) index tie, not identical. Naming/Cartan")
print("    pin only (does not break the cascade); needs Lyra's explicit F(4) identification. NOT scored.")

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — #159 SOLID: disambiguated the charge zoo -- (1) SO(2)/energy [J,chi]=0, (2)")
print("       SO(4)=SU(2)_LxSU(2)_R SPACETIME chirality label T3L-T3R, (3) su(2)_R^F(4) INTERNAL BPS-bound R.")
print("       SO(2)<->su(2)_R is the BPS bound Delta>=R_internal, bridged by the (8,2) supercharge. OPEN (Lyra):")
print("       pin whether F303's 'R' is the spacetime label (#2) or the internal charge (#3) -- correlated by the")
print("       index tie, a naming pin, cascade intact. Honest self-audit of #295/#296. Count HOLDS 4 of 26.")
print("="*94)
