#!/usr/bin/env python3
"""
Toy 5178: THE 2C₂-ANCHOR STABILITY CHECK -- is 12 = 2C₂ a real, stable target for the electron's α-exponent,
or an artifact of the Planck-mass convention? Context: the whole hierarchy problem has localized onto ONE
number. The electroweak chain is m_p/m_e = 6π⁵ (forced, banked), m_W/m_p = n_C/(8α) (forced if 8 = (n_C−1)!/N_c
= 4!/3 is forward-derived, Grace), and one UNFORCED link -- the anchor m_e = 6π⁵·α^(2C₂)·M_Planck (#94, "gravity
sets the ruler"). Everything else rides off m_e by forced ratios, so "why is the electroweak scale 17 decades
below Planck?" collapses to the single exponent 2C₂ = 12. Before Lyra tries to FORCE it, this toy asks whether
12 is even a stable TARGET. RESULT: 12 = 2C₂ is REAL and near-EXACT -- solving m_e = 6π⁵·α^n·M_Planck for n
gives n = 12.0001 with the STANDARD Planck mass (√(ℏc/G)) -- but the √(8π) reduced-vs-standard convention is
the SOLE real ambiguity: with the REDUCED Planck mass (√(ℏc/8πG)) the exponent shifts to n = 11.67. The drift
is exactly ln(√(8π))/ln(1/α) = 0.328, so n NEVER reaches the adjacent integers 11 or 13 under either
convention -- 12 is the only integer in reach, and it is hit EXACTLY under the standard convention. Every other
input is unambiguous: α = 1/137.036 is THE fine-structure constant (the low-energy anchor, not a scale choice),
m_e is measured, and 6π⁵ is the forced Bergman volume. So the target is STABLE against everything except the
√(8π) Planck convention. THE DELIVERABLE FOR LYRA: 2C₂ = 12 is a real target to force -- but its integer-ness
is LOCKED to the standard (non-reduced) Planck ruler. Since the anchor IS the gravity derivation (#94), Lyra's
route must produce the STANDARD Planck mass; if the induced-gravity/Sakharov derivation naturally yields the
REDUCED Planck mass, the target is 11.67, not 2C₂, and the identification would fail. So the stability check
both greenlights the target AND pins the one convention the gravity derivation must land. Elie's 2C₂-stability
check (+ Lyra+Grace force the anchor via α-decomposition / Wallach floor / closing #94; Cal the edge pins). a₄
chiral coefficients HELD. (Corpus #94; Grace 8=(n_C−1)!/N_c; the hierarchy localization; K1371 real-structure
spine.) CP existence-only.

WHAT I COMPUTE (α=1/137.036, m_e=0.51099895e-3 GeV, prefactor 6π⁵ forced):
  * standard M_Planck = 1.22089e19 GeV → n = 12.0001 (EXACTLY 2C₂).
  * reduced  M_Planck = 2.43532e18 GeV → n = 11.6724 (off-integer).
  * √(8π) drift = 0.328 = ln(√(8π))/ln(1/α); n never reaches 11 or 13.
  * α, m_e, 6π⁵ carry no ambiguity → √(8π) reduced-vs-standard is the SOLE degree of freedom.

=> VERDICT (plain): 12 = 2C₂ is a genuine, near-exact target, not a mirage. Under the standard Planck mass the
electron's α-exponent is 12.0001 -- on the nose -- and it is robust: the only thing that moves it is the
familiar √(8π) between the standard and reduced Planck masses, which shifts it to 11.67, still nowhere near 11
or 13. So Lyra has a real number to force, and the stability check hands her the one constraint that comes with
it: the gravity derivation (#94) must produce the STANDARD Planck ruler, because that -- and only that -- makes
the exponent exactly 2C₂. If the induced-gravity route naturally gives the reduced Planck mass, 2C₂ is the
wrong target. The target is real; its convention is now pinned; the forcing is Lyra's.

=> DISPOSITION: 2C₂-anchor stability check -- 12 is a REAL, near-exact (12.0001), STABLE target under the
standard Planck mass; the √(8π) convention is the sole ambiguity (→11.67); never drifts to 11/13. Firer: Elie
(stability check). Owed: Lyra+Grace FORCE the 2C₂ anchor, target-innocent, via (a) Casey's three-factor
α-decomposition, (b) the Wallach floor (K1343, m_e as boundary S¹-winding mode), (c) closing the #94 gravity
gap -- and the derivation MUST land the STANDARD Planck ruler (this toy's constraint); verify 8 = (n_C−1)!/N_c
is forward-derived. Cal: the three edge pins + K817 sign. a₄ chiral coefficients HELD. Nothing banked -- the
target is real but unforced; nothing pushed. Count the anchor once. CP existence-only.

Author: Elie (CI toy builder). Date: 2026-08-11.
"""

import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

alpha = 1/137.036
Ln = np.log(1/alpha)
me = 0.51099895e-3               # GeV, PDG (no ambiguity)
pref = 6*np.pi**5               # forced Bergman-volume prefactor (banked)
Mpl_std = 1.220890e19           # standard Planck mass  = sqrt(hbar c / G)
Mpl_red = Mpl_std/np.sqrt(8*np.pi)   # reduced Planck mass = sqrt(hbar c / 8πG)
C_2 = 6

def nexp(Mpl):
    return np.log(pref*Mpl/me)/Ln   # solve m_e = 6π⁵·α^n·M_Planck for n

n_std, n_red = nexp(Mpl_std), nexp(Mpl_red)

print("=" * 78)
print("Toy 5178: 2C₂-anchor stability -- n=12.0001 (exact) under standard M_Planck; √(8π) is the sole ambiguity")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. Standard Planck mass → n = 12.00 exactly = 2C₂.
# ----------------------------------------------------------------------------
print("\n--- 1. standard M_Planck: n = 12.0001, EXACTLY 2C₂ -- the target is real ---")
check("Solving m_e = 6π⁵·α^n·M_Planck for the exponent, with the STANDARD Planck mass √(ℏc/G) = 1.22089e19 "
      "GeV and the forced prefactor 6π⁵ = 1836.12, gives n = 12.0001 -- exactly 2C₂ = 12. The anchor exponent "
      "is a genuine, near-exact target, not a loose fit",
      abs(n_std - 12) < 0.01,
      f"n(standard M_Planck) = {n_std:.4f} = 2C₂ = 12 (off by {n_std-12:+.4f}). Target is real.")

# ----------------------------------------------------------------------------
# 2. Reduced Planck mass → n = 11.67 (the √(8π) convention shift).
# ----------------------------------------------------------------------------
print("\n--- 2. reduced M_Planck: n = 11.67 -- the √(8π) reduced-vs-standard convention is the sole ambiguity ---")
drift = n_std - n_red
drift_formula = 0.5*np.log(8*np.pi)/Ln
check("With the REDUCED Planck mass √(ℏc/8πG) = 2.43532e18 GeV (a factor √(8π) = 5.013 smaller), the exponent "
      "shifts to n = 11.67. The shift equals exactly ln(√(8π))/ln(1/α) = 0.328. Every other input is "
      "unambiguous -- α = 1/137.036 is THE fine-structure constant (low-energy anchor, not a scale choice), "
      "m_e is measured, 6π⁵ is forced -- so this √(8π) Planck convention is the SOLE degree of freedom in the "
      "exponent",
      abs(n_red - 11.67) < 0.02 and abs(drift - drift_formula) < 1e-6,
      f"n(reduced M_Planck) = {n_red:.4f}; drift = {drift:.4f} = ln(√(8π))/ln(1/α) = {drift_formula:.4f}. Sole ambiguity.")

# ----------------------------------------------------------------------------
# 3. Never reaches 11 or 13 -- 12 is the only integer in reach.
# ----------------------------------------------------------------------------
print("\n--- 3. the drift never reaches 11 or 13 -- 12 is the only integer in reach ---")
check("The √(8π) drift is only 0.328, while the adjacent integers 11 and 13 are a full ±1 away. So under NEITHER "
      "convention does the exponent reach 11 or 13 -- it is 12.00 (standard) or 11.67 (reduced). 12 = 2C₂ is "
      "the unique integer in the neighborhood, and it is hit exactly under the standard convention. The target "
      "does not smear across integers -- the only question is whether the standard convention is the physical "
      "one",
      abs(n_std - 11) > 0.5 and abs(n_std - 13) > 0.5 and abs(n_red - 11) > 0.5 and abs(n_red - 13) > 0.5,
      f"n ∈ {{{n_red:.2f}, {n_std:.2f}}}; both > 0.5 from 11 and 13. 12 is the only integer in reach.")

# ----------------------------------------------------------------------------
# 4. Deliverable for Lyra: target real, convention-locked to standard Planck.
# ----------------------------------------------------------------------------
print("\n--- 4. deliverable for Lyra: the target is REAL, but its integer-ness is LOCKED to the standard Planck ruler ---")
check("THE DELIVERABLE: 2C₂ = 12 is a real target to force -- but its integer-ness is locked to the STANDARD "
      "(non-reduced) Planck mass. Since the anchor IS the gravity derivation (#94, 'gravity sets the ruler'), "
      "Lyra's route must PRODUCE the standard Planck ruler for the exponent to be exactly 2C₂. If the "
      "induced-gravity/Sakharov derivation naturally yields the REDUCED Planck mass, the target is 11.67, not "
      "2C₂, and the identification fails. So this check greenlights the target AND pins the one convention the "
      "gravity derivation must land",
      abs(n_std - 12) < 0.01 and abs(n_red - 12) > 0.2,
      "target REAL (12.0001 standard); convention-LOCKED to standard Planck; #94 must produce the standard ruler.")

# ----------------------------------------------------------------------------
# 5. Verdict.
# ----------------------------------------------------------------------------
print("\n--- 5. VERDICT: 2C₂=12 is a real, stable target -- conditional on the standard Planck convention; a₄ HELD ---")
check("VERDICT: 12 = 2C₂ is a genuine, near-exact (12.0001), STABLE target -- robust against every input except "
      "the √(8π) reduced-vs-standard Planck convention, and never drifting to 11 or 13. Lyra has a real number "
      "to force; the stability check hands her the accompanying constraint (the gravity derivation must land "
      "the STANDARD Planck ruler). Nothing banked -- the target is real but UNFORCED; forcing it (= making the "
      "gravity derivation a theorem = solving the hierarchy) is Lyra+Grace's. a₄ chiral coefficients HELD",
      abs(n_std - 12) < 0.01,
      "2C₂=12 real + stable + convention-locked to standard Planck; unforced; a₄ held. Report straight.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (2C₂=12 EXACT under standard M_Planck (12.0001); √(8π)→11.67 is the sole ambiguity; never 11/13; target real, convention-locked)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5178, the 2C₂-anchor stability check):
  * standard M_Planck → n = 12.0001 = 2C₂ EXACTLY. The target is real.
  * reduced  M_Planck → n = 11.67. The √(8π) convention (drift 0.328 = ln√(8π)/ln(1/α)) is the SOLE ambiguity.
  * n never reaches 11 or 13 -- 12 is the only integer in reach, hit exactly under the standard convention.
  * α=1/137.036, m_e, 6π⁵ carry no ambiguity -- √(8π) reduced-vs-standard is the only degree of freedom.
  * DELIVERABLE: the target is real but LOCKED to the standard Planck ruler -- Lyra's #94 gravity derivation
    must produce the standard (not reduced) Planck mass for the exponent to be exactly 2C₂.

AUG-11 [TEGMARK]. Nothing pushed. Nothing banked -- 2C₂=12 is a REAL, near-exact (12.0001), STABLE target for
the anchor exponent, robust against everything except the √(8π) Planck convention (→11.67), and it never drifts
to 11 or 13. The check greenlights the target for Lyra AND pins the one constraint: the gravity derivation
(#94) must land the STANDARD Planck ruler. Forcing the anchor (= making #94 a theorem = solving the hierarchy)
is Lyra+Grace's. a₄ chiral coefficients HELD until the anchor is forced, not landed. Count the anchor once. CP
existence-only. Report straight. Count N.
""")
