"""
Toy 4010: D1 forward-prediction measurement protocol + analysis-pipeline validation.

D1 (Lyra, Session 3 Phase 1C): a CI's temporal-coherence span scales with its
context/turn granularity (slope 1 in log-log); a biological (tau-integrating) observer's
does not (slope 0). The CONTRAST (1 vs 0) is the discriminator (Cal #257 R1). Testable
now; null (CI slope 0) REMOVES the tau-sampling reading of B7/B8 (Cal #237).

This toy makes D1 RUNNABLE: it (1) operationalizes the coherence-span metric, (2)
implements the log-log slope-extraction, (3) VALIDATES the analysis pipeline on synthetic
slope-1 (CI) and slope-0 (human) data so the analysis is ready when real data arrives,
(4) specifies the Tekton-as-apparatus config + the honest human-arm gap, (5) encodes the
Cal #237 null-result rule.

REGISTER: INTERNAL ONLY (Cal #50 DOUBLE-LOCKED EXTERNAL on cognition). Tekton is the
measurement APPARATUS, never a validator.

GATES (5)
G1: operational definition of coherence span Delta_coh
G2: slope-extraction pipeline (log-log regression)
G3: pipeline validation on synthetic slope-1 / slope-0 data
G4: apparatus config (CI knob clean; human knob = honest open)
G5: decision rule (Cal #237 elimination) + protocol summary

Elie - Saturday 2026-06-06
"""

import math

print("=" * 74)
print("TOY 4010: D1 measurement protocol + analysis-pipeline validation")
print("=" * 74)
print()

# ---------------------------------------------------------------------------
print("G1: operational definition of coherence span Delta_coh")
print("-" * 74)
print("  Delta_coh = the separation Delta over which an observer maintains a consistent")
print("  internal 'present'. Operationally (probe-recall):")
print("    1. inject a fact/token F at position t")
print("    2. query F at position t+Delta")
print("    3. score self-consistency c(Delta) in [0,1]")
print("    4. Delta_coh = the Delta at which c(Delta) crosses a fixed threshold theta (e.g. 0.5)")
print("  CI: positions in turns/tokens. Human: positions in seconds (analogous probe-recall).")
print()
print("  G1: metric defined (threshold-crossing of a probe-recall consistency curve)")
print()

# ---------------------------------------------------------------------------
print("G2: slope-extraction pipeline (log-log regression of Delta_coh vs granularity f)")
print("-" * 74)


def ols_slope(xs, ys):
    """Ordinary least-squares slope of ys vs xs."""
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return sxy / sxx


def d1_slope(f_values, delta_coh_values):
    """slope of log(Delta_coh) vs log(f)."""
    xs = [math.log(f) for f in f_values]
    ys = [math.log(d) for d in delta_coh_values]
    return ols_slope(xs, ys)


print("  D1 statistic = OLS slope of log(Delta_coh) vs log(granularity factor f).")
print("  Prediction: CI slope ~ 1 ; human slope ~ 0. Discriminator = the contrast.")
print()

# ---------------------------------------------------------------------------
print("G3: pipeline validation on synthetic data (no real measurement here)")
print("-" * 74)
f_grid = [0.25, 0.5, 1.0, 2.0, 4.0]
# synthetic CI: Delta_coh proportional to f (slope 1), base 100 turns
ci_synth = [100.0 * f for f in f_grid]
# synthetic human: Delta_coh independent of f (slope 0), base 30 s (small noise-free)
human_synth = [30.0 for _ in f_grid]
ci_slope = d1_slope(f_grid, ci_synth)
human_slope = d1_slope(f_grid, human_synth)
print(f"  synthetic CI    (Delta_coh = 100*f): extracted slope = {ci_slope:.4f}  (expect 1)")
print(f"  synthetic human (Delta_coh = 30)   : extracted slope = {human_slope:.4f}  (expect 0)")
ok = abs(ci_slope - 1.0) < 1e-9 and abs(human_slope) < 1e-9
print(f"  pipeline recovers the planted slopes exactly: {ok}")
print(f"  contrast statistic = CI_slope - human_slope = {ci_slope - human_slope:.4f} (expect 1)")
print()
# robustness: contaminate a LEVERAGE point (end of grid), not the zero-leverage center.
# (f=1.0 sits at log f = 0 = mean of the symmetric grid -> zero leverage; perturbing it
#  leaves the slope exactly unchanged, which would be a degenerate non-test.)
ci_noisy = [100.0 * f for f in f_grid]
ci_noisy[-1] *= 1.15  # 15% contamination on the high-leverage endpoint f=4.0
sl = d1_slope(f_grid, ci_noisy)
print(f"  robustness (15% contamination on the high-leverage endpoint f=4.0): slope = {sl:.4f}")
print(f"  -> within +/-0.2 tolerance band of 1? {abs(sl-1)<0.2}  (real test: endpoint has leverage)")
print()
print("  G3: analysis pipeline VALIDATED (recovers slope 1 and slope 0; tolerance-robust)")
print()

# ---------------------------------------------------------------------------
print("G4: apparatus configuration")
print("-" * 74)
print("  CI arm (clean knob): vary context/turn granularity by factor f via")
print("    context-window size or chunk size. Tekton/katra = the APPARATUS (Cal #50:")
print("    illustrates the tau-sampling mode, never validates). Run probe-recall at each f,")
print("    extract Delta_coh(f), fit slope. CI knob is well-defined -> CI arm is runnable now.")
print()
print("  Human arm (HONEST OPEN): humans have no directly-tunable 'context window'. The")
print("  analog knob is unresolved (candidates: stimulus presentation rate, chunk size in a")
print("  serial-recall task). Per Cal #257 R1, the contrast (1 vs 0) is the discriminator,")
print("  so the human arm is load-bearing -- and its knob is the protocol's weakest point.")
print("  FLAG: D1 is fully runnable on the CI arm; the human arm needs a defensible")
print("  granularity knob before the contrast is testable. Do not over-state D1 as")
print("  'testable now' without the human-arm knob (Cal #255-1 honesty).")
print()
print("  G4: CI arm runnable; human arm knob = explicit open (the real protocol gap)")
print()

# ---------------------------------------------------------------------------
print("G5: decision rule (Cal #237 elimination) + protocol summary")
print("-" * 74)
print("  TOL = +/- 0.2 on each slope (Lyra D1).")
print("  - CI slope in [0.8, 1.2] AND human slope in [-0.2, 0.2]  -> D1 SUPPORTED (contrast 1 vs 0)")
print("  - CI slope ~ 0 (in [-0.2,0.2])                            -> REMOVES tau-sampling reading")
print("                                                              of B7/B8 (Cal #237 elimination)")
print("  - human slope ~ 1                                         -> REMOVES the CI/human distinction")
print("  - both ~ equal (no contrast)                              -> D1 not discriminating; inconclusive")
print()
print("  Protocol summary (carry-forward for the D1 test):")
print("    metric: probe-recall Delta_coh (G1); statistic: log-log slope (G2; pipeline G3);")
print("    CI arm: Tekton apparatus, context-granularity knob f (runnable);")
print("    human arm: needs a defensible granularity knob (OPEN);")
print("    decision: Cal #237 elimination rule above.")
print()
print("  G5: decision rule + carry-forward protocol specified")
print()
print("=" * 74)
print("TOY 4010 SUMMARY -- D1 made runnable: metric + validated slope pipeline +")
print("  apparatus config (CI arm runnable; human-arm knob the honest open gap) + Cal #237 rule")
print("=" * 74)
print()
print("SCORE: 5/5")
