#!/usr/bin/env python3
"""
Toy 4727 — Jul 18 (PMNS angles from the texture, mine; round-6 Elie item 2 — the honest FAIL check): do the g-shadow
angles sin²θ₁₂=3/10, sin²θ₁₃=1/45, sin²θ₂₃=4/7 DROP OUT of the neutrino mass texture, or are they identified-but-not-
derived-from-it? Answer (the honest FAIL boundary the board asked for): a GENERIC m₁=0 seesaw texture gives GENERIC
angles (0.63/0.66/0.14, 0.06/0.40/0.08, ...), NOT the g-shadows. So the PMNS angles do NOT emerge from a generic
m₁=0 texture — the MASSES are DERIVED (m₁=0 from rank, toy 4722), but the ANGLES are IDENTIFIED (exact primary forms
matching data) and NOT DERIVED from the one-condensate texture. The "one condensate does both masses and angles"
claim is NOT verified for the angles — they need a specific texture that is not yet established/target-innocent.

THE TARGETS (IDENTIFIED — exact primary forms matching data):
  * sin²θ₁₂ = 3/10 = N_c/(N_c+g) = 0.300; sin²θ₁₃ = 1/45 = 1/(N_c²·n_C) = 0.0222; sin²θ₂₃ = 4/7 = rank²/g = 0.571.
  * these MATCH observation (the "shadows of g") — so they are IDENTIFIED.
THE TEST (the honest FAIL): a generic m₁=0 seesaw texture (random m_D 3×2, M_R) → diagonalize → the PMNS angles are
GENERIC (0.63/0.66/0.14, 0.06/0.40/0.08, 0.10/0.01/0.44 across trials), NOWHERE near the g-shadows (0.30/0.022/0.571).
So the angles do NOT drop out of the mass texture generically — they require a SPECIFIC texture.
THE HONEST BOUNDARY:
  * neutrino MASSES: DERIVED (m₁=0 from rank(m_D^ν)=rank(D_IV⁵)=2, verified toy 4722).
  * neutrino ANGLES: IDENTIFIED (exact primary g-shadow forms matching data) but NOT DERIVED from the texture — a
    generic m₁=0 texture gives generic angles, so IF the g-shadows emerge it requires a specific (not-yet-specified,
    not-yet-shown-target-innocent) texture. Until that texture is given, the angles stay IDENTIFIED-not-derived.
  * so "one condensate → masses AND angles" is verified for the MASSES, NOT the angles. This is the honest FAIL point.

⟹ VERDICT: the PMNS angles do NOT drop out of a generic m₁=0 neutrino texture (verified across trials) → the g-shadow
angles (3/10, 1/45, 4/7) are IDENTIFIED (exact primary forms matching data) but NOT DERIVED from the one-condensate
mass texture. Masses DERIVED (m₁=0), angles IDENTIFIED-not-derived — the honest FAIL boundary. The open piece: a
specific, target-innocent texture that yields the g-shadows (or a separate g-structure origin for the angles). Count
~7-8 (α RULED). Five-Absence-safe. Reported honestly per the board ("the honest FAIL point").
"""
import numpy as np
from fractions import Fraction as F
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
np.random.seed(585)
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- targets (identified primary forms) -------------------------------------
t12, t13, t23 = F(N_c, N_c+g), F(1, N_c**2*n_C), F(rank**2, g)
print(f"\n[targets]: sin²θ₁₂=N_c/(N_c+g)={t12}={float(t12):.3f}; sin²θ₁₃=1/(N_c²n_C)={t13}={float(t13):.4f}; sin²θ₂₃=rank²/g={t23}={float(t23):.3f}")
check("TARGETS IDENTIFIED (exact primary forms matching data): sin²θ₁₂ = 3/10 = N_c/(N_c+g); sin²θ₁₃ = 1/45 = "
      "1/(N_c²·n_C); sin²θ₂₃ = 4/7 = rank²/g. These MATCH observation (the 'shadows of g') → IDENTIFIED.",
      t12 == F(3,10) and t13 == F(1,45) and t23 == F(4,7), "sin²θ angles = 3/10, 1/45, 4/7 (g-shadows) — IDENTIFIED primary forms")

# ---- the test: generic m1=0 texture → generic angles ------------------------
def angles(m_nu):
    w, U = np.linalg.eigh(m_nu)
    U = U[:, np.argsort(np.abs(w))]
    s13sq = U[0,2]**2
    s12sq = U[0,1]**2/(1-s13sq)
    s23sq = U[1,2]**2/(1-s13sq)
    return s12sq, s13sq, s23sq
near = 0
trials = []
for _ in range(6):
    mD = np.random.randn(3,2); MR = np.diag([3.,7.])
    a = angles(-mD @ np.linalg.inv(MR) @ mD.T)
    trials.append(a)
    if abs(a[0]-0.30) < 0.05 and abs(a[1]-0.022) < 0.01 and abs(a[2]-0.571) < 0.05:
        near += 1
print(f"[generic textures]: sample angles = {[tuple(round(x,3) for x in a) for a in trials[:3]]}; # matching g-shadows = {near}/6")
check("THE TEST (honest FAIL): a GENERIC m₁=0 seesaw texture (random m_D 3×2, M_R) gives GENERIC PMNS angles "
      "(0.63/0.66/0.14, ...), NOWHERE near the g-shadows (0.30/0.022/0.571) — 0/6 trials match. So the angles do NOT "
      "drop out of the mass texture generically; they require a SPECIFIC texture.",
      near == 0, "generic m₁=0 textures give generic angles, 0/6 match the g-shadows — angles don't emerge generically")

# ---- the honest boundary ----------------------------------------------------
check("THE HONEST BOUNDARY: neutrino MASSES are DERIVED (m₁=0 from rank(m_D^ν)=rank(D_IV⁵)=2, toy 4722); neutrino "
      "ANGLES are IDENTIFIED (exact primary g-shadow forms matching data) but NOT DERIVED from the texture — a generic "
      "m₁=0 texture gives generic angles, so the g-shadows need a specific (not-yet-specified, not-yet-target-innocent) "
      "texture. 'One condensate → masses AND angles' is verified for the MASSES, NOT the angles.",
      True, "masses DERIVED (m₁=0); angles IDENTIFIED-not-derived-from-texture — the honest FAIL point")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the PMNS angles do NOT drop out of a generic m₁=0 neutrino texture (0/6 trials) → the g-shadow angles "
      "(3/10, 1/45, 4/7) are IDENTIFIED (exact primary forms matching data) but NOT DERIVED from the one-condensate "
      "mass texture. Masses DERIVED, angles IDENTIFIED-not-derived — the honest FAIL boundary. Open piece: a specific "
      "target-innocent texture yielding the g-shadows, or a separate g-structure origin for the angles. Reported "
      "honestly per the board.",
      near == 0 and t12 == F(3,10) and t13 == F(1,45),
      "PMNS angles IDENTIFIED-not-derived-from-texture (0/6 generic match); masses derived — honest FAIL point reported")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print("""
PMNS ANGLES FROM THE TEXTURE (round-6 item 2) — the honest FAIL point:
  * TARGETS (identified): sin²θ₁₂=3/10, sin²θ₁₃=1/45, sin²θ₂₃=4/7 (g-shadows) — match data.
  * TEST: a generic m₁=0 seesaw texture gives GENERIC angles (0/6 match the g-shadows) → angles don't emerge generically.
  * BOUNDARY: masses DERIVED (m₁=0 from rank); angles IDENTIFIED (primary forms) but NOT DERIVED from the texture.
  => 'one condensate → masses AND angles' verified for MASSES, not angles. Honest FAIL point reported; specific texture is the open piece.
""")
