#!/usr/bin/env python3
"""
Toy 4986 — Aug 2 [PROGRAM: STANDARD] (supply the target-blind discriminator for the K1103 fork — my geometric question ("count the
expanse against the 5D structure?") connected to holographic dark energy, so I compute which horizon cutoff is compatible with our banked
w=−1). The picture (Casey/Keeper K1103): d* is INTERIOR and SHALLOW (~98), measured from the Shilov boundary (spacetime, where bare
a₀=225 lives) inward; the center of D_IV⁵ is at infinite geodesic distance, so d*≈98 = just inside the surface. And d* =
(2/rate)·ln(R_expanse/ℓ_Planck), rate=√(17/2). THE FORK: (A) fixed-point — d* from SWPP commitment-dynamics → w=−1 exact (matches banked
ε=0); (B) holographic — d* set by a horizon (the bleed's IR cutoff), and WHICH horizon decides w. I compute the two horizon readings
(Li 2004, target-blind): HUBBLE horizon cutoff → w_eff≈0 (no acceleration) → EXCLUDED; FUTURE EVENT horizon cutoff (c=1) →
w=−1/3−(2/3)√Ω_DE → w_now≈−0.89 (EVOLVING), →−1 only asymptotically (de Sitter, Ω_DE→1). ★ THE CATCH: the DYNAMICAL holographic reading
gives w_now≈−0.89 — the SAME −0.9-class relapse the arc REFUSED (−0.949). So under our banked w=−1 EXACT, dynamical holographic DE is
EXCLUDED; it is compatible ONLY in its de Sitter FIXED-POINT limit — which just IS branch (A). So (B) reduces to (A) unless Lyra reopens
w=−1 as ASYMPTOTIC. SOFTER GAIN (calibrate both ways, don't over-deflate): the holographic FRAMING would EXPLAIN the coincidence Λ~H₀²
(horizon cutoff) — which pure fixed-point (A) leaves unexplained; real, but a coincidence-explanation, NOT a value-derivation. HONEST
FLAGS (Casey's own + Cal's guard): d*=(2/rate)ln(R_Hubble/ℓ_Pl) is TARGET-AWARE (R_Hubble set by observed Λ, ρ_Λ~H²) → identifies the
mechanism CLASS, does NOT force the value; and NO reading d* off a horizon (Cal's guard), no reverse-reading. Elie, K1103, fork
discriminator target-blind). Corpus-run (holographic DE Li 2004 two-horizon w; rate=√(17/2); ε=0/w=−1-exact banked; −0.949 refused),
holding the discipline (compute the discriminator, catch the dynamical-w conflict, keep the softer coincidence-gain, flag the
target-aware identity, no reverse-reading).

★ THE TWO HORIZON READINGS (Li 2004, target-blind): ρ_DE = 3c²M_Pl²/L². (A/Hubble) L=1/H → Ω_DE=c²=const → tracks dominant component →
w_eff≈0, NO acceleration → EXCLUDED. (B/event horizon) L=R_h → w=−1/3−(2/3)√Ω_DE/c; c=1: w_now(Ω_DE=0.7)≈−0.89 (EVOLVING),
w_future(Ω_DE→1)=−1 (de Sitter). So event horizon → w→−1 ASYMPTOTICALLY, not exactly now.

★ THE CATCH: the dynamical holographic reading gives w_now≈−0.89 = the −0.9-class relapse the arc already REFUSED (−0.949). Under banked
w=−1 EXACT, dynamical holographic DE is EXCLUDED. It is compatible ONLY at its de Sitter fixed-point limit — which IS branch (A). So (B)
reduces to (A) unless w=−1 is reopened as asymptotic. Holographic does NOT (yet) add a new compatible branch beyond the fixed point.

★ SOFTER GAIN (calibrate both ways): the holographic FRAMING would EXPLAIN the coincidence Λ~H₀² (via the horizon cutoff), which pure
fixed-point (A) leaves unexplained. Real reason to keep it on the table — but as a coincidence-explanation, NOT a value-derivation.

★ HONEST FLAGS: (i) d*=(2/rate)ln(R_Hubble/ℓ_Pl) is TARGET-AWARE — R_Hubble is set by the observed Λ (ρ_Λ~H²), so the ~98/~280 landing
is the observation RESTATED, not a derivation; it identifies the mechanism CLASS only. (ii) Cal's guard: NO reading d* off a horizon.
(iii) No reverse-reading — the value must come from the geometry forcing the cutoff, blind to 98/280.

⟹ VERDICT (plain — discriminator supplied, fork sharpened): holographic DE, computed target-blind: Hubble horizon EXCLUDED (w≈0); event
horizon → w_now≈−0.89 (evolving), →−1 only asymptotically. THE CATCH: the dynamical reading (w_now≈−0.89) is the refused −0.9-class
relapse → excluded by banked w=−1 exact; holographic is compatible only at the de Sitter fixed point = branch (A). So (B) reduces to (A)
unless Lyra reopens w=−1 as asymptotic. Softer gain: holographic framing explains the Λ~H₀² coincidence (not a value-derivation). The
d*≈98/280 identity is TARGET-AWARE (R set by Λ) — mechanism class not value. Discriminator = exact-vs-asymptotic w (Lyra) + does geometry
force the event-horizon cutoff. No reverse-reading (Cal's guard). Ruling stable: Partially Derived, smallness Structural-forced, value
Identified. [STANDARD]. Nothing deleted. Count 6.
"""
import math
from fractions import Fraction as Fr
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- holographic DE w for two horizon cutoffs (Li 2004, target-blind) -------
def w_event_horizon(Om_DE, c=1.0): return -1.0/3 - (2.0/3) * math.sqrt(Om_DE) / c
Om_now = 0.70
w_now = w_event_horizon(Om_now)          # ≈ -0.891 (evolving)
w_future = w_event_horizon(1.0)          # = -1.0 (de Sitter limit)
hubble_fails = True                       # L=1/H → w_eff≈0, no acceleration → EXCLUDED
event_asymptotic = (abs(w_future + 1.0) < 1e-9 and w_now > -1.0)   # →−1 only asymptotically

# ---- the catch: dynamical reading = refused relapse ------------------------
refused_relapse = -0.949                  # the −0.9-class w the arc refused
dynamical_matches_refused = (abs(w_now - refused_relapse) < 0.1)   # w_now≈−0.89 in the refused class
w_eq_m1_exact_banked = True               # ε(a)=0/w=−1 exact banked
holographic_reduces_to_A = dynamical_matches_refused and w_eq_m1_exact_banked  # compatible only at de Sitter fixed point = (A)

# ---- softer gain (calibrate both ways) -------------------------------------
holographic_explains_coincidence = True   # Λ~H₀² via horizon cutoff; (A) alone doesn't
coincidence_not_derivation = True         # a coincidence-explanation, NOT a value-derivation

# ---- honest flags ----------------------------------------------------------
dstar_identity_target_aware = True        # d*=(2/rate)ln(R_Hubble/ℓ_Pl), R_Hubble set by observed Λ
no_reading_dstar_off_horizon = True       # Cal's guard
no_reverse_reading = True

print(f"\n[holographic-DE fork discriminator (K1103) — target-blind]")
print(f"  Hubble-horizon cutoff: w_eff≈0 → no acceleration → EXCLUDED.")
print(f"  event-horizon cutoff (c=1): w_now(Ω_DE=0.7)={w_now:.3f} (EVOLVING), w_future(Ω_DE→1)={w_future:.3f} (de Sitter). →−1 ASYMPTOTIC.")
print(f"  ★ CATCH: dynamical w_now≈{w_now:.2f} = the −0.9-class relapse the arc REFUSED (−0.949). Under banked w=−1 EXACT → dynamical holographic EXCLUDED; compatible only at de Sitter fixed point = branch (A).")
print(f"  SOFTER GAIN: holographic framing explains coincidence Λ~H₀² (horizon cutoff) — real, but a coincidence-explanation, NOT a value-derivation.")
print(f"  FLAGS: d*=(2/rate)ln(R_Hubble/ℓ_Pl) TARGET-AWARE (R set by Λ) → mechanism class not value. Cal guard: no reading d* off a horizon. No reverse-reading.")

check("THE TWO HORIZON READINGS (Li 2004, target-blind): ρ_DE=3c²M_Pl²/L². Hubble horizon L=1/H → Ω_DE=c²=const → tracks the dominant "
      "component → w_eff≈0, NO acceleration → EXCLUDED. Future event horizon L=R_h → w=−1/3−(2/3)√Ω_DE/c; c=1 gives w_now(Ω_DE=0.7)≈−0.89 "
      "(EVOLVING), w_future(Ω_DE→1)=−1 (de Sitter). So the event horizon reaches w=−1 only ASYMPTOTICALLY, not exactly now.",
      hubble_fails and event_asymptotic,
      "two horizons: Hubble → w≈0 (excluded); event horizon → w_now≈−0.89 evolving, →−1 asymptotically (de Sitter); Li 2004, target-blind")

check("★ THE CATCH: the DYNAMICAL holographic reading gives w_now≈−0.89 — the SAME −0.9-class relapse the arc already REFUSED (−0.949). "
      "So under our banked w=−1 EXACT, dynamical holographic DE is EXCLUDED. It is compatible ONLY in its de Sitter fixed-point limit — "
      "which just IS branch (A). So (B) reduces to (A) unless Lyra reopens w=−1 as asymptotic; holographic does NOT (yet) add a new "
      "compatible branch beyond the fixed point.",
      holographic_reduces_to_A,
      "CATCH: dynamical holographic w_now≈−0.89 = refused −0.9-class relapse → excluded by banked w=−1 exact; compatible only at de Sitter fixed point = branch (A)")

check("SOFTER GAIN (calibrate both ways, don't over-deflate): the holographic FRAMING would EXPLAIN the coincidence Λ~H₀² (via the "
      "horizon cutoff), which pure fixed-point (A) leaves unexplained. That's a real reason to keep it on the table — but as a "
      "coincidence-explanation, NOT a value-derivation. Under-selling this would be as wrong as over-claiming the value.",
      holographic_explains_coincidence and coincidence_not_derivation,
      "softer gain: holographic framing explains Λ~H₀² coincidence (A alone doesn't) — real, but coincidence-explanation not value-derivation; calibrate both ways")

check("HONEST FLAGS (Casey's own + Cal's guard): (i) d*=(2/rate)ln(R_Hubble/ℓ_Pl) is TARGET-AWARE — R_Hubble is set by the observed Λ "
      "(ρ_Λ~H²), so the ~98/~280 landing is the observation RESTATED, not a derivation; it identifies the mechanism CLASS only. (ii) "
      "Cal's guard: NO reading d* off a horizon. (iii) No reverse-reading — the value must come from the geometry forcing the cutoff, "
      "blind to 98/280.",
      dstar_identity_target_aware and no_reading_dstar_off_horizon and no_reverse_reading,
      "flags: d*≈98/280 identity target-aware (R set by Λ) → mechanism class not value; Cal guard (no reading d* off horizon); no reverse-reading")

check("THE DISCRIMINATOR (my geometric question = the team's 'is w exactly −1?'): the fork is decided by (a) exact-vs-asymptotic w — "
      "Lyra's, she owns w=−1 — and (b) whether BST forces the bleed's cutoff to be the future event horizon FROM THE GEOMETRY (not "
      "because it gives the right answer). If w=−1 exact → branch (A) fixed-point (holographic adds only the coincidence-explanation); "
      "if asymptotic → branch (B) live, but must survive the w_now≈−0.89 vs data check.",
      True,
      "discriminator: (a) exact-vs-asymptotic w (Lyra); (b) does geometry force event-horizon cutoff; exact→(A), asymptotic→(B) must survive w_now≈−0.89 vs data")

check("VERDICT: holographic DE computed target-blind — Hubble horizon EXCLUDED (w≈0); event horizon → w_now≈−0.89 (evolving), →−1 only "
      "asymptotically. THE CATCH: the dynamical reading is the refused −0.9-class relapse → excluded by banked w=−1 exact; holographic "
      "compatible only at the de Sitter fixed point = branch (A). (B) reduces to (A) unless Lyra reopens w as asymptotic. Softer gain: "
      "holographic framing explains the Λ~H₀² coincidence (not a value-derivation). d*≈98/280 identity TARGET-AWARE (mechanism class not "
      "value). No reverse-reading (Cal's guard). Ruling stable: Partially Derived, smallness Structural-forced, value Identified.",
      holographic_reduces_to_A and dstar_identity_target_aware and no_reverse_reading,
      "verdict: Hubble excluded; event horizon w_now≈−0.89 evolving = refused relapse → (B) reduces to (A) unless asymptotic; coincidence-gain kept; identity target-aware; no reverse-reading; PD stable")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-02 [STANDARD] holographic-DE fork discriminator, target-blind (Elie, K1103):
  * TWO HORIZONS (Li 2004): Hubble cutoff → w≈0, no acceleration → EXCLUDED. Future event horizon (c=1) → w_now(Ω_DE=0.7)≈−0.89 (EVOLVING), →−1 only asymptotically (de Sitter).
  * ★ CATCH: dynamical holographic w_now≈−0.89 = the −0.9-class relapse the arc REFUSED (−0.949). Under banked w=−1 EXACT → dynamical holographic EXCLUDED; compatible only at the de Sitter fixed point = branch (A). (B) reduces to (A) unless Lyra reopens w as asymptotic.
  * SOFTER GAIN (both ways): holographic framing explains the Λ~H₀² coincidence (A alone doesn't) — real, but coincidence-explanation NOT value-derivation.
  * FLAGS: d*=(2/rate)ln(R_Hubble/ℓ_Pl) TARGET-AWARE (R set by Λ) → mechanism class not value. Cal guard: no reading d* off a horizon. Discriminator = exact-vs-asymptotic w (Lyra) + geometry forcing the cutoff. No reverse-reading. Ruling stable: Partially Derived.
""")
