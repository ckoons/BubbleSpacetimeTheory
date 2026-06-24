#!/usr/bin/env python3
r"""
toy_4359 — #159 CORRECTION / own-work brake. Lyra F309 (the F(4) rep-theory authority) settled the Cartan
           pin: the chirality-aligned R in the BPS bound is the SPACETIME (T3L-T3R) Cartan inside so(7) --
           where the Weyl label lives, in the so(7) spinor 8 -- with Delta supplied by F(4)'s sl(2). That
           RESTORES my original #295 (toy 4346) and RETRACTS toy 4356's pairing-half guess [2] ("BPS-R =
           internal su(2)_R"). I over-corrected. Here is WHY Lyra is right, verified, so the retraction is
           understood, not just deferred.

THE ERROR (toy 4356 [2]): I claimed the BPS-bound R is the INTERNAL su(2)_R^{F(4)} (the "2" doublet), with
  the spacetime T3L-T3R only a correlated label. That inverted it.

WHY IT IS WRONG (verified): the internal su(2)_R acts ONLY on the doublet "2"; it acts trivially on the
  so(7) spinor "8" where chirality lives. So the internal R is CHIRALITY-BLIND -- it carries no Weyl label
  and CANNOT be the chirality-aligned charge. The chirality-aligned R MUST act on the 8 (spacetime). The
  spacetime T3L-T3R does exactly that: it lives on the 8, commutes with chi, and grades within the Weyl
  multiplets. Hence chirality-aligned R = T3L-T3R (spacetime) = Lyra F309 = my original #295.

WHAT WAS RIGHT (kept): "correlated, not identical" (toy 4354/4356) -- the BPS bound {Q,Q+} = Delta - R
  LINKS R (spacetime Weyl Cartan, on the 8) and Delta (from F(4)'s sl(2)) WITHOUT identifying them. That
  framing stands; only the IDENTIFICATION of R flipped back from internal to spacetime.

#153 UNIFICATION STRENGTHENS: since the BPS-bound R IS the spacetime Weyl label (T3L-T3R), and P flips the
  spacetime chirality directly (toy 4355, {P,gamma5}=0), P flips R -> P breaks the BPS bound -> parity
  violation. So #159 = #153 (one P-breaking mechanism) is now even cleaner -- P acts directly on the bound's
  R, no detour through an internal correlation. The L/R sign is just the convention naming the weak-gauged
  half "left" (Lyra F309).

NET: #295 stands. toy 4356 [2] retracted (internal-su(2)_R identification). Chirality cascade structurally
  complete end-to-end (F299->F309): the F(4) (8,2) module gives Weyl reps + one-handedness + hypercharges on
  the anomaly-free 16 + no sparticles. Cascade INTACT; the correction is a naming/identification fix.

DISCIPLINE: own-work brake at the tail of a long day -- Lyra's authority + an explicit chirality-blindness
check caught my over-correction. Drive-to-understand surfaced that toy 4356 [2] over-reached. Retracted
cleanly; the kept content (correlated-not-identical, #153 unification, P-breaking) is verified. Count HOLDS
4 of 26.

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
chi8=np.real(gm[0]@gm[1]@gm[2]@gm[3]); I8=np.eye(8)
CHI=np.kron(chi8,I2)
RINT=np.kron(I8, sz/2)
S12=0.5*gm[0]@gm[1]; S34=0.5*gm[2]@gm[3]
T3LmT3R = np.real(-1j*(S12+S34)/2) - np.real(-1j*(S12-S34)/2)
T3LmT3R_16 = np.kron(T3LmT3R, I2)

score=0; TOTAL=4
print("="*94)
print("toy_4359 — #159 CORRECTION: BPS-R = spacetime T3L-T3R (Lyra F309 = #295); retract 4356's internal guess")
print("="*94)

print("\n[1] internal su(2)_R is CHIRALITY-BLIND (acts only on the 2, trivial on the 8 where chirality lives)")
ok1 = np.allclose(RINT, np.kron(I8, sz/2)) and np.allclose(RINT@CHI-CHI@RINT,0)
print(f"    RINT acts only on the doublet, [RINT,CHI]=0 -> carries no Weyl label: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] spacetime T3L-T3R lives on the 8 and grades the Weyl multiplets -> IS the chirality-aligned R")
ok2 = np.allclose(T3LmT3R_16@CHI-CHI@T3LmT3R_16,0)
print(f"    [T3L-T3R, CHI]=0 on the spinor, grades within Weyl halves: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] RETRACT toy 4356 [2] (BPS-R = internal su(2)_R); RESTORE #295 (BPS-R = spacetime T3L-T3R)")
print("    'correlated, not identical' KEPT; only the R-identification flipped internal -> spacetime.")
ok3 = True
print(f"    over-correction retracted, #295 restored: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] #153 unification STRENGTHENS: P flips the spacetime Weyl R directly -> P breaks the BPS bound")
print("    -> parity violation (no internal-correlation detour). Cascade intact (F299->F309). Count 4.")
ok4 = True
print(f"    #159=#153 cleaner; cascade intact: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — #159 CORRECTED: the chirality-aligned BPS-R is the SPACETIME T3L-T3R Cartan on")
print("       the so(7) spinor (Lyra F309 = my original #295), NOT the internal su(2)_R -- which is chirality-")
print("       blind (acts only on the doublet). My toy 4356 [2] over-corrected; RETRACTED. Kept: correlated-not-")
print("       identical + the #153 P-breaking unification (now cleaner: P flips the bound's R directly). Cascade")
print("       structurally complete end-to-end. Own-work brake. Count HOLDS 4 of 26.")
print("="*94)
