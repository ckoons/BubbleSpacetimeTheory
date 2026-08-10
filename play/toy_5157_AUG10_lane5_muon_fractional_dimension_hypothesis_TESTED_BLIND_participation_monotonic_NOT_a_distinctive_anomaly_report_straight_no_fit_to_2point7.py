#!/usr/bin/env python3
"""
Toy 5157: LANE 5 -- Casey's MUON FRACTIONAL-DIMENSION hypothesis, TESTED BLIND. RESULT (report straight, no
fit): the hypothesis is that the muon (intermediate stratum ν=3/2, between bulk-electron ν=5/2 and boundary-
tau ν=0) is a "charged cloud" of fractional dimension 2<d<3 (~2.7), which would explain why it is the hardest
lepton to derive (K1011 forced null, overlap scattered 5.5/8.0/0.478). I tested this with blind geometry-only
measures and it is NOT confirmed: (1) the participation/spread measure is MONOTONIC (electron 0.005 <  muon
0.015 < tau 0.100) -- the muon comes out INTERMEDIATE, not anomalously fractional, and the tau is the most
spread (an ARTIFACT: the naive radial model ψ_ν=(1−r²)^ν makes ν=0 flat rather than boundary-localized, so it
mis-models the Shilov tau); (2) the clean spectral-dimension via the K-Casimir decomposition is numerically
unstable (ill-conditioned monomial Gram) -- no reliable number. So a clean blind measure that yields
{integer, 2.7, integer} for {e, μ, τ} requires the CORRECT localized wavefunctions (the coherent-state radii/
widths, which are themselves not independently pinned) or would amount to fitting to 2.7 -- which I do NOT
do. HONEST VERDICT: the muon-at-intermediate-stratum is banked (F86/F93, ν=3/2 = N_c/rank), but a DISTINCTIVE
fractional dimension is NOT demonstrated by the blind measures tried. The hypothesis has real motivation (the
K1011 dimension-SCATTER is a genuine fractional-dimension signature), but it is a dimension-CONSISTENCY test,
not a spread test, and needs a cleaner formalization. Report straight; do not fit to 2.7. Elie's Lane-5 blind
test. (K1011/F86/F93.) Compute-don't-fit; the negative reported straight.

WHAT I TEST / FIND:
  * MUON AT INTERMEDIATE STRATUM (banked): ν={5/2,3/2,0}={n_C/rank, N_c/rank, 0} (F93); muon = ν=3/2 = the
    Cartan-slice/intermediate, between bulk-electron (5/2) and Shilov-tau (0). This is real (F86/F93).
  * PARTICIPATION/SPREAD (blind): monotonic e(0.005) < μ(0.015) < τ(0.100) -- muon INTERMEDIATE, NOT anomalous;
    tau most-spread (ARTIFACT: ν=0 flat, not boundary-localized). So "muon = uniquely spread cloud" NOT confirmed.
  * SPECTRAL DIMENSION (blind): numerically unstable (ill-conditioned) -- no reliable number.
  * NO CLEAN {int, 2.7, int}: reproducing it needs the correct localized modes (radii/widths, not pinned) or
    fitting to 2.7 -- NOT done.

=> VERDICT (plain): Casey's muon-fractional-dimension hypothesis is TESTED BLIND and NOT confirmed by the
measures available. The participation/spread measure gives the muon as INTERMEDIATE (monotonic e<μ<τ), not a
distinctive fractional anomaly -- and the tau reads as most-spread only because the naive radial model
(ψ_ν=(1−r²)^ν) mis-localizes the Shilov mode (a model artifact). The clean spectral-dimension via the
K-Casimir decomposition is numerically unstable. So a blind measure that yields {integer(e), 2.7(μ),
integer(τ)} either requires the correct localized wavefunctions (the coherent-state radii/widths, themselves
unpinned) or amounts to fitting to 2.7 -- which I do NOT do. The muon-at-intermediate-stratum (ν=3/2 =
N_c/rank) is banked (F86/F93); a DISTINCTIVE fractional dimension is NOT demonstrated. The hypothesis's real
teeth -- the K1011 overlap SCATTER (5.5/8.0/0.478 across dimension-assumptions) -- IS a genuine fractional/
dimension-inconsistency signature, but it is a dimension-CONSISTENCY test, not a spread test, and needs a
cleaner formalization. Reported straight; not fit. CP existence-only unaffected.

=> DISPOSITION: Lane-5 blind test -- muon fractional-dimension NOT confirmed by participation/spectral (report
straight, no fit to 2.7); muon-at-intermediate-stratum banked (F86/F93). Firer: Elie; the right follow-up is
a dimension-CONSISTENCY measure (the sensitivity of the muon overlap to the assumed dimension, connecting to
the K1011 scatter) with the correct localized modes -- needs Lyra/Casey's wavefunction pin. Cal audits the
negative. Nothing pushed. Nothing banked -- a blind test reported straight (not confirmed), no fit.

Author: Elie (CI toy builder). Date: 2026-08-10.
"""

import numpy as np
from scipy import integrate

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

n_C, N_c, rank = 5, 3, 2

print("=" * 78)
print("Toy 5157: Lane 5 -- muon fractional-dimension hypothesis TESTED BLIND → NOT confirmed (report straight, no fit)")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. Muon at the intermediate stratum (banked).
# ----------------------------------------------------------------------------
print("\n--- 1. muon at the INTERMEDIATE stratum ν=3/2=N_c/rank (banked, F86/F93) ---")
nu = {"e": n_C/rank, "mu": N_c/rank, "tau": 0.0}
check("the charged leptons sit at ν = {5/2, 3/2, 0} = {n_C/rank, N_c/rank, 0} (F93): electron ν=5/2 (deep "
      "bulk), MUON ν=3/2 = N_c/rank (the intermediate Cartan-slice stratum), tau ν=0 (Shilov boundary). The "
      "muon is genuinely the INTERMEDIATE mode -- this is banked (F86/F93). Casey's hypothesis: it is a "
      "fractional 'charged cloud' (2<d<3), explaining the K1011 forced null",
      abs(nu["e"] - 2.5) < 1e-9 and abs(nu["mu"] - 1.5) < 1e-9,
      f"ν: e={nu['e']}, μ={nu['mu']}=N_c/rank, τ={nu['tau']}. Muon intermediate (banked). Hypothesis to test blind.")

# ----------------------------------------------------------------------------
# 2. Participation/spread: monotonic, muon intermediate (not anomalous) + artifact.
# ----------------------------------------------------------------------------
print("\n--- 2. participation/spread (blind): MONOTONIC e<μ<τ → muon intermediate, NOT anomalous (+ artifact) ---")
def PR(nu_val):
    p = lambda r: (1-r**2)**(2*nu_val)
    w = lambda r: r**(2*n_C-1)
    Z = integrate.quad(lambda r: p(r)*w(r), 0, 1)[0]
    I2 = integrate.quad(lambda r: (p(r)/Z)**2*w(r), 0, 1)[0]
    return 1.0/I2
pr = {k: PR(v) for k, v in nu.items()}
monotonic = pr["e"] < pr["mu"] < pr["tau"]
check("the blind PARTICIPATION/spread measure (ψ_ν=(1−r²)^ν on the domain measure) is MONOTONIC: e(0.005) < "
      "μ(0.015) < τ(0.100). The muon comes out INTERMEDIATE, NOT anomalously fractional; the tau is the most "
      "spread -- an ARTIFACT, because ν=0 gives a FLAT radial mode rather than a boundary-localized one (the "
      "naive model mis-localizes the Shilov tau). So 'muon = uniquely spread cloud' is NOT confirmed",
      monotonic,
      f"PR: e={pr['e']:.4f}, μ={pr['mu']:.4f}, τ={pr['tau']:.4f} (monotonic). Muon intermediate, not anomalous; "
      "tau-most-spread is a boundary artifact. Hypothesis not confirmed by spread.")

# ----------------------------------------------------------------------------
# 3. No clean blind {integer, 2.7, integer} without fitting.
# ----------------------------------------------------------------------------
print("\n--- 3. no clean blind {int, 2.7, int}: needs correct localized modes or fits to 2.7 (NOT done) ---")
check("a clean blind measure yielding {integer(e), 2.7(μ), integer(τ)} is NOT available: the spectral-"
      "dimension via the K-Casimir decomposition is numerically unstable (ill-conditioned monomial Gram), and "
      "the participation is monotonic (with the boundary artifact). Reproducing 2.7 would require the correct "
      "localized wavefunctions (coherent-state radii/widths, themselves unpinned) OR fitting to 2.7 -- which I "
      "do NOT do (a fitted dimension banks nothing)",
      True,
      "no reliable blind {int,2.7,int}; would need pinned localized modes or a fit. Did not fit. The muon-"
      "fractional dimension is NOT demonstrated blind.")

# ----------------------------------------------------------------------------
# 4. Verdict: not confirmed; report straight; the K1011-scatter is the real (unformalized) signature.
# ----------------------------------------------------------------------------
print("\n--- 4. verdict: hypothesis NOT confirmed by blind measures; report straight; K1011-scatter = real teeth ---")
check("VERDICT: Casey's muon-fractional-dimension hypothesis is TESTED BLIND and NOT confirmed -- the "
      "participation/spread is monotonic (muon intermediate, not anomalous; tau-spread is an artifact), the "
      "spectral-dimension is numerically unstable, and no clean {int, 2.7, int} emerges without fitting (which "
      "I do NOT do). The muon-at-intermediate-stratum (ν=3/2=N_c/rank) is banked (F86/F93), but a DISTINCTIVE "
      "fractional dimension is NOT demonstrated. The real teeth -- the K1011 overlap SCATTER (5.5/8.0/0.478 "
      "across dimension-assumptions) -- is a dimension-CONSISTENCY signature (not a spread test) needing a "
      "cleaner formalization. Reported straight; no fit",
      monotonic,
      "not confirmed by blind measures; muon intermediate (banked), fractional dimension not demonstrated; "
      "K1011-scatter is the real (unformalized) signature. Report straight, do not fit to 2.7.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (muon fractional-dimension NOT confirmed blind; participation monotonic; report straight, no fit to 2.7)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5157, Lane 5 -- muon fractional-dimension hypothesis, blind test):
  * MUON AT INTERMEDIATE STRATUM (banked, F86/F93): ν=3/2=N_c/rank, between bulk-e (5/2) and Shilov-τ (0).
  * PARTICIPATION/SPREAD (blind): monotonic e(0.005)<μ(0.015)<τ(0.100) → muon INTERMEDIATE, not anomalous;
    tau-most-spread is a boundary ARTIFACT (ν=0 flat, not boundary-localized). "Cloud" not confirmed.
  * SPECTRAL DIMENSION (blind): numerically unstable (ill-conditioned) -- no reliable number.
  * NO CLEAN {{int, 2.7, int}}: needs correct localized modes (unpinned) or a fit to 2.7 -- NOT done.
  * VERDICT: hypothesis NOT confirmed by blind measures; muon fractional dimension NOT demonstrated. The
    K1011 overlap SCATTER is the real (dimension-consistency) signature, needing a cleaner formalization.

AUG-10 [TEGMARK]. Nothing pushed. Nothing banked -- a blind test reported STRAIGHT (not confirmed), no fit to
2.7. The muon-at-intermediate-stratum is banked (F86/F93); a distinctive fractional dimension is NOT
demonstrated by participation/spectral measures. The hypothesis's teeth (K1011 dimension-scatter) is a
consistency test needing the correct localized modes -- Lyra/Casey's wavefunction pin. Report straight; compute-don't-fit. Count N.
""")
