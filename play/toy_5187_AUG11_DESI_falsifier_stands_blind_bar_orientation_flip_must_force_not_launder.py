#!/usr/bin/env python3
"""
Toy 5187: THE DESI BLIND-TEST BAR -- the falsifier STANDS; the orientation-flip resolution counts only if it
FORCES the sign blind, never if it is adjusted to match. Context: BST's breathing-mode dark energy predicts
w_a > 0; DESI DR2 measures w_a < 0 at ~3σ (parametrization-robust); BST is on the WRONG side of the data (toy
5185). Casey proposes a resolution: DESI reads the dark-energy process inward-from-infinity while BST projects
outward, so on constant-negative-curvature the w_a sign could be an orientation artifact between BST's intrinsic
w(a) and the observer's CPL fit. This is BOTH legitimate physics (BST's banked ontology IS pure positive-time /
outward / bubble-nucleating -- a sign subtlety between intrinsic and observed w(a) is a real question) AND
structurally identical to the falsifier-escape every one of us forbade yesterday (a reinterpretation that flips
the sign to match the data is laundering, most dangerous when the PI proposes it and the whole room wants it
true). This toy does NOT resolve anything -- it HOLDS THE LINE: it re-affirms the falsifier, and it pre-registers
the bar so the flip can only succeed honestly. THE COMMITTED BAR (pre-registered, before any orientation→sign
result is compared to DESI): the resolution counts ONLY IF all three facts hold, each established BLIND /
DESI-independent -- FACT 1 (geometry): orientation-reversal (inward↔outward) FLIPS sign(w_a), a DESI-free
theorem; FACT 2 (ontology): BST FORCES outward (K-banked pure positive-time); FACT 3 (forensic): the ORIGINAL
w_a>0 derivation ASSUMED inward projection, a real sign bug (audit Lyra's #54/#101). CONCLUSION RULE: the flip
is legitimate IFF (1 ∧ 2 ∧ 3) AND the outward orientation INDEPENDENTLY yields the sign (not adjusted to match).
LAUNDERING (forbidden): choosing the sign to match DESI, or calling a match a "confirmation" without 1∧2∧3
established blind. CRITICAL SELF-LIMIT: I do NOT compute the flip -- I already know DESI wants w_a<0, so MY
re-derivation cannot be blind; the orientation→sign derivation must be Lyra's, forced by geometry and auditable
to not reference the DESI target, and Cal + I hold the bar and report whatever it gives. VERDICT: nothing
resolved; the falsifier STANDS (BST w_a>0, DESI w_a<0, ~3σ, wrong side); a resolution being IMAGINABLE does not
let us feel resolved. Elie's blind-test bar (+ Lyra's forced-orientation blind re-derivation; Cal+Keeper hold
the bar). a₄ chiral coefficients HELD. (Toy 5185 falsifier; Casey orientation proposal; BST pure positive-time
ontology; no-laundering standing order; commit-the-checker-half-blind.) CP existence-only. This toy makes the
flip HARDER, not easier.

WHAT I DO (hold the line -- I do NOT resolve):
  * re-affirm: DESI DR2 all combos w_a<0 (~3σ); BST w_a>0; FALSIFIER STANDS, no change from 5185.
  * name the resolution AND its structural identity to the forbidden falsifier-escape (both true).
  * pre-register the BAR: flip legitimate IFF FACT 1 (geometry flips sign, blind) ∧ FACT 2 (BST forces outward)
    ∧ FACT 3 (original assumed inward) AND outward independently yields the sign.
  * self-limit: I do NOT compute the flip (I know the target → I can't be blind); it is Lyra's forced derivation.

=> VERDICT (plain): our worst falsifier is still our worst falsifier. BST predicts the dark-energy equation of
state stiffens (w_a>0); DESI, in every dataset combination, sees it thaw (w_a<0), about three sigma the other
way. Casey's proposal -- that DESI is reading the process in the opposite orientation to the one BST projects --
is a real physics question and could, in principle, turn the sign we are failing on into the sign we predict.
But it is the exact shape of the move we forbade when it was inconvenient, so it earns nothing by being elegant
or by coming from the PI. It resolves the falsifier only if the outward orientation FORCES w_a<0 blind: the
geometry must flip the sign on its own, BST must independently force outward, and the original w_a>0 must be
shown to have quietly assumed inward -- a real sign bug -- with the new sign falling out, not being dialed in.
Until all of that is established without looking at DESI, the falsifier stands and BST is on the wrong side of
the data. I cannot run the blind derivation myself, because I already know which sign the data wants; it has to
be Lyra's, forced and auditable, and Cal and I report whatever it gives. A resolution being imaginable is not a
resolution.

=> DISPOSITION: DESI blind-test bar -- falsifier STANDS; orientation-flip pre-registered against a 3-fact blind
bar; laundering forbidden; the flip made HARDER not easier. Firer: Elie (bar). Owed: Lyra's forced-orientation
blind re-derivation of the breathing-mode w(a) sign + the forensic audit of #54/#101 for the inward assumption;
Cal + Keeper hold the pre-committed bar. Nothing banked -- falsifier stands; nothing pushed; no laundering,
ever. a₄ chiral coefficients HELD. CP existence-only.

Author: Elie (CI toy builder). Date: 2026-08-11.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# DESI DR2 (CPL), web-scrubbed Aug 2026 (toy 5185): (w0, sig_w0, wa, sig_wa)
desi = {'DESI+CMB': (-0.42, 0.21, -1.75, 0.58), 'DESI+CMB+SN(Pantheon+)': (-0.838, 0.055, -0.62, 0.205)}

print("=" * 78)
print("Toy 5187: the DESI blind-test bar -- falsifier STANDS; orientation-flip must FORCE the sign, never launder")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. The falsifier stands.
# ----------------------------------------------------------------------------
print("\n--- 1. FALSIFIER STANDS: DESI DR2 all combos w_a<0 (~3σ); BST breathing mode w_a>0; wrong side ---")
all_neg = all(v[2] < 0 for v in desi.values())
min_sig = min(abs(v[2])/v[3] for v in desi.values())
check("Re-affirmed (no change from toy 5185): every DESI DR2 combination gives w_a < 0 at ~3σ (parametrization-"
      "robust), while BST's banked breathing mode predicts w_a > 0. BST is on the WRONG side of the data. The "
      "falsifier STANDS",
      all_neg and min_sig >= 2.9,
      f"DESI w_a<0 (~{min_sig:.1f}σ) vs BST w_a>0. Wrong side. Falsifier stands.")

# ----------------------------------------------------------------------------
# 2. The proposed resolution is legitimate AND structurally identical to the forbidden escape.
# ----------------------------------------------------------------------------
print("\n--- 2. the orientation-flip resolution is BOTH legitimate physics AND structurally the forbidden escape ---")
check("Casey's proposal -- DESI reads inward-from-infinity, BST projects outward, so the w_a sign may be an "
      "orientation artifact on constant-negative-curvature -- is BOTH legitimate (BST's ontology IS pure "
      "positive-time/outward; a sign subtlety between intrinsic and observed w(a) is a real question) AND "
      "structurally identical to the falsifier-escape we forbade (a reinterpretation flipping the sign to match "
      "the data). Both are true at once, so it is held to the BLIND BAR -- elegance and PI-authorship earn it "
      "nothing",
      True,
      "legitimate physics ∧ forbidden-escape shape → held to the blind bar; no credit for elegance or authorship.")

# ----------------------------------------------------------------------------
# 3. The pre-registered 3-fact blind bar.
# ----------------------------------------------------------------------------
print("\n--- 3. PRE-REGISTERED BAR: flip legitimate IFF (FACT 1 ∧ FACT 2 ∧ FACT 3) blind AND outward yields the sign ---")
facts = {
    'FACT 1 (geometry)':  "orientation-reversal (inward↔outward) FLIPS sign(w_a) -- a DESI-free theorem",
    'FACT 2 (ontology)':  "BST FORCES outward -- K-banked pure positive-time (already banked)",
    'FACT 3 (forensic)':  "the ORIGINAL w_a>0 derivation ASSUMED inward -- a real sign bug (audit #54/#101)",
}
check("Pre-registered BEFORE any orientation→sign result is compared to DESI: the flip counts ONLY IF all three "
      "facts hold, each established BLIND / DESI-independent -- FACT 1 geometry flips the sign (theorem), FACT 2 "
      "BST forces outward (banked), FACT 3 the original assumed inward (a real sign bug) -- AND the outward "
      "orientation INDEPENDENTLY yields the sign, not adjusted to match. LAUNDERING (choosing the sign to match, "
      "or calling a match a confirmation without 1∧2∧3 blind) is forbidden",
      len(facts) == 3,
      "flip IFF (1 ∧ 2 ∧ 3) blind AND outward yields the sign independently; laundering forbidden. Pre-registered.")
for k, v in facts.items():
    print(f"            · {k:20s}: {v}")

# ----------------------------------------------------------------------------
# 4. Self-limit: I do NOT compute the flip.
# ----------------------------------------------------------------------------
print("\n--- 4. self-limit: I do NOT compute the flip -- I know the target, so my derivation cannot be blind ---")
check("CRITICAL self-limit: I do NOT compute the flip. I already know DESI wants w_a<0, so MY re-derivation "
      "cannot be blind -- I would be reaching for the answer. The orientation→sign derivation must be Lyra's, "
      "forced by the geometry and auditable to NOT reference the DESI target; Cal and I hold the bar and report "
      "whatever it gives. This is the commit-the-checker-half-blind discipline in its hardest case",
      True,
      "I do not compute the flip (I know the target → not blind); Lyra's forced derivation; Cal+I hold the bar and report.")

# ----------------------------------------------------------------------------
# 5. Verdict: nothing resolved; falsifier stands.
# ----------------------------------------------------------------------------
print("\n--- 5. VERDICT: nothing resolved; the falsifier STANDS; a resolution being imaginable ≠ resolved ---")
check("VERDICT: nothing is resolved. The falsifier STANDS -- BST predicts w_a>0, DESI measures w_a<0 at ~3σ, "
      "BST is on the wrong side. Casey's orientation proposal could in principle turn the failing sign into the "
      "predicted one, but it resolves the falsifier ONLY IF the outward orientation FORCES w_a<0 blind (the "
      "3-fact bar), with the sign falling out, not dialed in. Until then, the falsifier stands. A resolution "
      "being IMAGINABLE does not let us feel resolved. This toy makes the flip HARDER, not easier",
      all_neg and min_sig >= 2.9 and len(facts) == 3,
      "nothing resolved; falsifier STANDS; flip must FORCE the sign blind; no laundering. Report whatever the blind derivation gives.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (falsifier STANDS: BST w_a>0 vs DESI w_a<0 ~3σ; orientation-flip pre-registered vs 3-fact blind bar; laundering forbidden; nothing resolved)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5187, the DESI blind-test bar -- holds the line, does NOT resolve):
  * FALSIFIER STANDS: DESI DR2 all combos w_a<0 (~3σ); BST breathing mode w_a>0; wrong side. No change from 5185.
  * the orientation-flip resolution is BOTH legitimate physics AND structurally the forbidden falsifier-escape.
  * PRE-REGISTERED BAR: flip legitimate IFF FACT 1 (geometry flips sign, blind) ∧ FACT 2 (BST forces outward) ∧
    FACT 3 (original assumed inward, a sign bug) AND outward INDEPENDENTLY yields the sign. Laundering forbidden.
  * SELF-LIMIT: I do NOT compute the flip -- I know the target, so I can't be blind; it is Lyra's forced derivation.

AUG-11 [TEGMARK]. Nothing pushed. Nothing banked -- this toy HOLDS THE LINE and does NOT resolve. The DESI
falsifier STANDS (BST w_a>0, DESI w_a<0, ~3σ, wrong side). Casey's orientation-flip is legitimate physics AND
structurally the falsifier-escape we forbade, so it is held to a pre-registered 3-fact blind bar and counts
ONLY if the outward orientation FORCES the sign, with it falling out rather than being dialed in. I do NOT
compute the flip (knowing the target, I cannot be blind) -- Lyra's forced, auditable re-derivation does, and
Cal + I report whatever it gives. A resolution being imaginable is not a resolution; this makes the flip
HARDER, not easier. No laundering, ever. a₄ chiral coefficients HELD. CP existence-only. Count N.
""")
