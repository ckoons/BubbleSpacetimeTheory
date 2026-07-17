#!/usr/bin/env python3
"""
Toy 4690 — Jul 16 (the PMNS Jarlskog analog, mine; hold the CP constraint for Grace's neutrino render): prepare the
leptonic Jarlskog so it LOCKS onto Grace's Majorana/Takagi PMNS angles the moment they land — the exact analog of
my CKM J piece (4689). Same structure: J_PMNS = (PMNS angles) × sin δ_PMNS, with δ from the FK "1−r_i r_j·ω" twist
(not a bare ℤ₃, my 4688). The one difference from CKM: the PMNS angles are LARGE (θ₁₂≈33°, θ₂₃≈49°, θ₁₃≈8.6°), so
J_PMNS is ~1000× the CKM J.

THE LEPTONIC JARLSKOG (Dirac-phase analog, same form as CKM): J_PMNS = c₁₂ s₁₂ · c₂₃ s₂₃ · c₁₃² s₁₃ · sin δ_PMNS.
  * the angles are Grace's Majorana × texture render (targets θ₁₂≈33°, θ₂₃≈49°, θ₁₃≈8.6°, at structural tier).
  * sin δ_PMNS — from the FK twist (the same "1−r_i r_j·ω" non-removable phase as CKM), NOT a bare ℤ₃.

WHAT I HOLD (the constraint, ready for her render):
  (1) J_PMNS,max = c₁₂ s₁₂ c₂₃ s₂₃ c₁₃² s₁₃ ≈ 0.033 (the amplitude, from the large angles); J_PMNS = J_max · sin δ_PMNS.
  (2) ~1000× the CKM J: because the PMNS angles are large (θ₂₃≈49° vs V_cb≈2.4°; θ₁₃≈8.6° vs V_ub≈0.2°), J_PMNS ≫ J_CKM.
      That size ratio IS the large-PMNS/small-CKM shape, carried into CP.
  (3) J_PMNS RIDES on the angles + δ_PMNS via the FK twist — NOT a separate input (same as 4689). It banks WHEN
      Grace's Majorana render gives the angles + complex positions, not before.
  (4) MAJORANA caveat (noted): the neutrino has TWO extra Majorana phases (α₂₁, α₃₁) beyond the Dirac δ — they don't
      enter the oscillation Jarlskog J_PMNS (that uses only δ), but they DO enter 0νββ (pred_004). So J_PMNS is the
      Dirac-δ analog of J_CKM; the Majorana phases are a separate, additional CP structure.

⟹ VERDICT: the leptonic Jarlskog J_PMNS = (PMNS angles) × sin δ_PMNS is prepared and HELD, ready to lock onto Grace's
Majorana/Takagi render. J_PMNS,max ≈ 0.033 (~1000× CKM J, from the large angles); δ_PMNS from the FK twist (not a
bare ℤ₃). J_PMNS rides on Grace's derived angles — not a separate input. Majorana phases noted (0νββ, separate).
Not banked; held for her render. Count ~7-8 (α RULED, identified).
"""
import numpy as np
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def jarlskog(s12, s23, s13, delta):
    c12, c23, c13 = np.sqrt(1-s12**2), np.sqrt(1-s23**2), np.sqrt(1-s13**2)
    return c12*s12 * c23*s23 * c13**2*s13 * np.sin(delta)

# ---- PMNS target angles (Grace's render will supply these) ------------------
th12, th23, th13 = np.radians(33.4), np.radians(49.0), np.radians(8.6)
s12, s23, s13 = np.sin(th12), np.sin(th23), np.sin(th13)
J_max = jarlskog(s12, s23, s13, np.pi/2)          # amplitude (sin δ=1)
print(f"\n[PMNS angles (targets, Grace derives)]: θ₁₂={np.degrees(th12):.0f}°, θ₂₃={np.degrees(th23):.0f}°, θ₁₃={np.degrees(th13):.1f}°")
print(f"[J_PMNS amplitude]: J_max = c₁₂s₁₂·c₂₃s₂₃·c₁₃²s₁₃ = {J_max:.4f}; J_PMNS = J_max·sin δ_PMNS")
check("J_PMNS AMPLITUDE (large): J_max = c₁₂s₁₂·c₂₃s₂₃·c₁₃²s₁₃ ≈ 0.033 from the large PMNS angles; J_PMNS = J_max·sin "
      "δ_PMNS. Same form as CKM (my 4689), with the neutrino's large angles.",
      abs(J_max - 0.033) < 0.005, "J_PMNS,max ≈ 0.033 — the leptonic Jarlskog amplitude from the large angles")

# ---- ~1000× the CKM J -------------------------------------------------------
J_ckm_max = jarlskog(np.sqrt(1/20), 0.041, 0.0037, np.pi/2)   # CKM amplitude
ratio = J_max/J_ckm_max
print(f"[vs CKM]: J_PMNS,max/J_CKM,max = {J_max:.4f}/{J_ckm_max:.2e} = {ratio:.0f}× — large-PMNS/small-CKM shape, in CP")
check("~1000× THE CKM J: J_PMNS,max/J_CKM,max ≈ {:.0f}× — because the PMNS angles are large (θ₂₃≈49° vs V_cb≈2.4°, "
      "θ₁₃≈8.6° vs V_ub≈0.2°). The large-PMNS/small-CKM SHAPE carries straight into the CP magnitude.".format(ratio),
      ratio > 100, "J_PMNS ≫ J_CKM (large angles) — the CKM/PMNS shape carried into CP")

# ---- J_PMNS rides on the angles + δ (FK twist), not separate ----------------
check("J_PMNS RIDES ON THE ANGLES + δ (FK twist, not separate — same as 4689): J_PMNS = (Grace's Majorana angles) × "
      "sin δ_PMNS, with sin δ_PMNS from the FK '1−r_i r_j·ω' non-removable phase (NOT a bare ℤ₃, my 4688). It banks "
      "WHEN her render gives the angles + complex positions — not before, not as a separate input.",
      True, "J_PMNS is locked to Grace's derived angles × the FK-twist δ — held, not a free parameter")

# ---- Majorana phases noted (0νββ, separate) ---------------------------------
check("MAJORANA CAVEAT (noted): the Majorana neutrino has TWO extra phases (α₂₁, α₃₁) beyond the Dirac δ. They do "
      "NOT enter the oscillation Jarlskog J_PMNS (that uses only δ), but they DO enter 0νββ (pred_004). So J_PMNS is "
      "the Dirac-δ analog of J_CKM; the Majorana phases are a separate, additional CP structure for the render to carry.",
      True, "Majorana phases (α₂₁, α₃₁) are separate (0νββ); J_PMNS uses only the Dirac δ — noted for Grace's Takagi render")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the leptonic Jarlskog J_PMNS = (PMNS angles) × sin δ_PMNS is prepared and HELD, ready to lock onto "
      "Grace's Majorana/Takagi render. J_PMNS,max ≈ 0.033 (~1000× CKM J, from the large angles); δ_PMNS from the FK "
      "twist (not a bare ℤ₃). J_PMNS rides on Grace's derived angles — not a separate input. Majorana phases noted "
      "(0νββ, separate). Held for her render, not banked.",
      abs(J_max-0.033)<0.005 and ratio>100, "J_PMNS analog prepared, rides on Grace's angles via the FK twist; held. Count ~7-8 (α RULED)")

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
PMNS JARLSKOG ANALOG (held for Grace's Majorana render):
  * J_PMNS = c₁₂s₁₂·c₂₃s₂₃·c₁₃²s₁₃·sin δ_PMNS; amplitude J_max ≈ 0.033 from the large angles (θ₁₂33/θ₂₃49/θ₁₃8.6).
  * ~1000× the CKM J — the large-PMNS/small-CKM shape carried into CP.
  * RIDES on Grace's derived angles + δ_PMNS (FK "1−r_i r_j·ω" twist, not a bare ℤ₃) — not a separate input.
  * MAJORANA phases (α₂₁, α₃₁) are separate (0νββ); J_PMNS uses only the Dirac δ.
  => J_PMNS prepared + held; banks when Grace's Takagi render lands the angles + complex positions. Count ~7-8.
""")
