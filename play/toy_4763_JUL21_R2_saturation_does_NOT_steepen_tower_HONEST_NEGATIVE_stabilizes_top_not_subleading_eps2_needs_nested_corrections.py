#!/usr/bin/env python3
"""
Toy 4763 — Jul 21 (Round-2 quark row, the saturation test, Elie's target-innocent verification): the pull's candidate for
the up-type extra "2" (λ⁴ = (λ²)²) is SATURATION — the claim that a leading singular value pinned at the Cauchy-Schwarz
ceiling (σ₁=1, y_t=1) forces the sub-leading masses to second order (ε² → λ⁴), while unsaturated (down/lepton, σ₁<1) gives
first order (ε → λ²). The pull framed it as a test ("if NO → honest-negative"). I tested it, and it's a clean HONEST-
NEGATIVE with a precise diagnosis: saturation makes the TOP second-order stable, but it does NOT steepen the tower — the
sub-leading σ₂ scales as ε¹ regardless of whether σ₁ is at the ceiling. The mechanism conflates "the top is stable" (TRUE)
with "the sub-leading are small" (FALSE). ε² requires NESTED (second-order) corrections — a structurally different claim.

THE MECHANISM'S TRUE KERNEL (verified): a ceiling-preserving correction (the y≤1 constraint forbids raising a saturated
σ₁=1) makes the TOP second-order stable — δσ₁ ~ ε². So the saturated top's OWN mass is protected (its first-order raise is
forbidden by the ceiling). This much is real — it's the "∂y/∂correction = 0 at the maximum" intuition, and it is correct
FOR σ₁.
BUT THE CONCLUSION FAILS (verified 4 ways): the SUB-LEADING σ₂ scales as ε¹ for σ₁ ∈ {0.5 (unsaturated), 1.0 (ceiling),
5.0 (over)} AND for a ceiling-preserving constrained correction. **Saturation of the leading singular value does NOT push
the sub-leading masses to second order.** σ₂'s ε-scaling is independent of σ₁'s magnitude. So saturation does NOT produce
the up-type λ⁴.
THE PRECISE CONFLATION (the fish): the mechanism confuses TWO different eigenvalues with different scalings — "the SATURATED
top is second-order stable" (TRUE: δσ₁ ~ ε²) vs "the SUB-LEADING masses are second-order small" (FALSE: σ₂ ~ ε). Saturation
STABILIZES THE TOP; it does NOT STEEPEN THE TOWER. The λ⁴/λ² split is NOT the y_t=1/y_b≪1 split — they are decoupled.
WHAT ACTUALLY GIVES ε² (the redirect): a NESTED correction — the correction ITSELF being O(ε²), a correction-of-a-
correction (verified: σ₂ ~ ε²). So the up-type λ⁴ (if real) requires up-type CORRECTIONS to be NESTED (second-order),
NOT the top to be saturated. The target-innocent question is redirected: does the geometry make up-type corrections
NESTED (ε²) while down-type first-order (ε)? (Not answered here — Lyra's geometry; and note the CP row already found
corrections STACK, J ∝ ε³.)
THE DOWN/LEPTON "2" (candidate, separate): the λ² per step is the Gatto relation — mass ratio = mixing² (bilinearity;
Born/Gram mass ~ |overlap|²). Target-innocent IF mixing = λ (derived) AND mass = mixing²; but a GENERIC hierarchical
matrix gives ε¹, not ε² — so the "2" is the SPECIFIC Gatto/Born bilinear structure, NOT automatic. A candidate sub-win,
needs the bilinearity derived.

⟹ VERDICT: HONEST-NEGATIVE on saturation → up-type λ⁴. The mechanism has a TRUE kernel (a ceiling-saturated top is
second-order stable, δσ₁ ~ ε²) but its CONCLUSION is FALSE — the sub-leading σ₂ ~ ε regardless of saturation (verified 4
ways). Saturation stabilizes the top; it does NOT steepen the tower; the λ⁴/λ² split is decoupled from the y_t=1/y_b≪1
split. ε² needs NESTED corrections (a different structure) — the redirected target-innocent question for the geometry. The
down/lepton "2" = Gatto/Born bilinearity (candidate, needs deriving). The integer-powers derivation does NOT close via
saturation → the row stays Tier-2 FN-texture (as flagged). A clean bounce — standing negative — that saved a wrong
mechanism and redirected to nested-corrections. Count ~7-8. Five-Absence-safe.
"""
import numpy as np
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

np.random.seed(7)
a = np.random.randn(3); a /= np.linalg.norm(a)
b = np.random.randn(3); b /= np.linalg.norm(b)
C = np.random.randn(3, 3); C /= np.linalg.norm(C, 2)
C_con = C - (a@C@b)*np.outer(a, b)            # ceiling-preserving (removes leading-raising component)
eps = np.logspace(-5, -2, 20)
def scal(M0, Cc, idx):
    base = np.sort(np.linalg.svd(M0, compute_uv=False))[::-1]
    d = [abs(np.sort(np.linalg.svd(M0+e*Cc, compute_uv=False))[::-1][idx] - base[idx]) for e in eps]
    return np.polyfit(np.log(eps), np.log(d), 1)[0]
def sub(M0, Cc):
    return np.polyfit(np.log(eps), np.log([np.sort(np.linalg.svd(M0+e*Cc, compute_uv=False))[::-1][1] for e in eps]), 1)[0]

# ---- true kernel: saturated top is 2nd-order stable -------------------------
d_top = scal(np.outer(a, b), C_con, 0)
print(f"\n[true kernel] ceiling-preserving correction: δσ₁ (top) ~ ε^{d_top:.2f} (second-order stable)")
check("THE MECHANISM'S TRUE KERNEL (verified): a ceiling-preserving correction (y≤1 forbids raising a saturated σ₁=1) "
      "makes the TOP second-order stable — δσ₁ ~ ε². The saturated top's OWN mass is protected (its first-order raise is "
      "forbidden by the ceiling). This is the '∂y/∂correction=0 at the maximum' intuition, and it is correct FOR σ₁.",
      abs(d_top - 2) < 0.3, "ceiling-preserving correction → δσ₁ ~ ε² → the saturated TOP is second-order stable (the true kernel)")

# ---- but sub-leading ~ eps regardless of saturation ------------------------
s_unsat = sub(0.5*np.outer(a,b), C); s_sat = sub(1.0*np.outer(a,b), C); s_over = sub(5.0*np.outer(a,b), C); s_con = sub(np.outer(a,b), C_con)
print(f"[conclusion fails] σ₂ ~ ε^{s_unsat:.2f}(σ₁=.5) ε^{s_sat:.2f}(σ₁=1) ε^{s_over:.2f}(σ₁=5) ε^{s_con:.2f}(ceiling-constrained)")
check("BUT THE CONCLUSION FAILS (verified 4 ways): the SUB-LEADING σ₂ ~ ε¹ for σ₁ ∈ {0.5, 1.0 (ceiling), 5.0} AND for a "
      "ceiling-preserving correction. Saturation of the leading singular value does NOT push the sub-leading masses to "
      "second order — σ₂'s ε-scaling is independent of σ₁'s magnitude. So saturation does NOT produce the up-type λ⁴.",
      all(abs(s-1) < 0.2 for s in (s_unsat, s_sat, s_over, s_con)), "σ₂ ~ ε¹ for σ₁=0.5/1/5 and ceiling-constrained → saturation does NOT steepen the tower; up-type λ⁴ NOT from saturation")

# ---- the precise conflation -------------------------------------------------
check("THE PRECISE CONFLATION (the fish): the mechanism confuses TWO different eigenvalues — 'the SATURATED top is "
      "second-order stable' (TRUE, δσ₁ ~ ε²) vs 'the SUB-LEADING masses are second-order small' (FALSE, σ₂ ~ ε). "
      "Saturation STABILIZES THE TOP; it does NOT STEEPEN THE TOWER. The λ⁴/λ² steepness split is DECOUPLED from the "
      "y_t=1 / y_b≪1 split — they are not one root cause.",
      abs(d_top - 2) < 0.3 and abs(s_sat - 1) < 0.2, "saturation stabilizes the top (δσ₁~ε²) but not the sub-leading (σ₂~ε) → λ⁴/λ² split decoupled from y_t/y_b split")

# ---- what actually gives eps^2: nested corrections --------------------------
c1 = np.random.randn(3); c1/=np.linalg.norm(c1); d1 = np.random.randn(3); d1/=np.linalg.norm(d1)
nested = np.polyfit(np.log(eps), np.log([np.sort(np.linalg.svd(np.outer(a,b)+e**2*np.outer(c1,d1), compute_uv=False))[::-1][1] for e in eps]), 1)[0]
print(f"[redirect] NESTED (ε²) correction: σ₂ ~ ε^{nested:.2f} → ε² needs the CORRECTION to be second-order, not saturation")
check("WHAT ACTUALLY GIVES ε² (redirect): a NESTED correction — the correction ITSELF being O(ε²), a "
      "correction-of-a-correction (verified: σ₂ ~ ε²). So up-type λ⁴ (if real) requires up-type CORRECTIONS to be NESTED "
      "(second-order), NOT the top to be saturated. Redirected target-innocent question: does the geometry make up-type "
      "corrections nested (ε²) while down-type first-order (ε)? (CP row already found corrections STACK, J ∝ ε³.) Down/"
      "lepton '2' = Gatto/Born bilinearity (mass ratio = mixing²) — candidate, not automatic (generic hierarchical gives ε¹).",
      abs(nested - 2) < 0.3, "ε² needs NESTED (second-order) corrections, not saturation → redirect: are up-type corrections nested? down/lepton '2' = Gatto candidate")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: HONEST-NEGATIVE on saturation → up-type λ⁴. True kernel (ceiling-saturated top is second-order stable, "
      "δσ₁ ~ ε²) but FALSE conclusion — sub-leading σ₂ ~ ε regardless of saturation (verified 4 ways). Saturation "
      "stabilizes the top, does NOT steepen the tower; the λ⁴/λ² split is DECOUPLED from y_t=1/y_b≪1. ε² needs NESTED "
      "corrections (different structure) — the redirected question for the geometry. Down/lepton '2' = Gatto/Born "
      "bilinearity candidate. The integer-powers derivation does NOT close via saturation → row stays Tier-2 FN-texture. "
      "A clean bounce (standing negative) that saved a wrong mechanism and redirected to nested-corrections.",
      abs(d_top-2) < 0.3 and abs(s_sat-1) < 0.2 and abs(nested-2) < 0.3,
      "saturation→λ⁴ FAILS (stabilizes top not tower; σ₂~ε always); ε² needs nested corrections; row stays Tier-2; honest-negative + redirect")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-2 saturation test — Elie's target-innocent verification (HONEST-NEGATIVE + redirect):
  * TRUE kernel: a ceiling-saturated top is second-order stable (δσ₁ ~ ε²) — the '∂y/∂corr=0 at the max' intuition, correct FOR σ₁.
  * FALSE conclusion (verified 4 ways): the sub-leading σ₂ ~ ε¹ regardless of σ₁ (0.5/1/5/ceiling-constrained). Saturation does NOT steepen the tower.
  * THE FISH: saturation STABILIZES THE TOP, does NOT STEEPEN THE TOWER — the λ⁴/λ² split is DECOUPLED from the y_t=1/y_b≪1 split (not one root cause).
  * REDIRECT: ε² needs NESTED (second-order) corrections, not saturation → does the geometry make up-type corrections nested? Down/lepton '2' = Gatto/Born bilinearity (candidate).
  => HONEST-NEGATIVE on saturation→λ⁴; integer-powers derivation does NOT close this way; row stays Tier-2 FN-texture. Clean bounce, wrong mechanism caught, redirected.
""")
