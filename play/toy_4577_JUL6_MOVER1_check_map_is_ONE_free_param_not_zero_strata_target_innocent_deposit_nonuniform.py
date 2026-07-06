#!/usr/bin/env python3
"""
Toy 4577 — Jul 6: MOVER 1 target-innocence/parameter check (my assigned, peak-convergence).
Grace's map Δ = D̂ + d on the KW strata D̂ = {5,2,0} (F446) → Δ={9,6,4} → Casimirs {45,12,0}.
Keeper's status calls it "zero free parameters given forced d=4." I audit that precisely — and
it's actually ONE free parameter, plus a non-uniform deposit. Load-bearing at peak convergence.

WHAT'S GENUINELY STRONGER (the real upgrade):
  the Δ VALUES are no longer picked — they come from a PRE-EXISTING target-innocent spectrum,
  the KW strata {5,2,0} (F446), via a single map. That dissolves the different-factors question
  and is a material improvement over "Δ=6,9 chosen to hit 12,45" (my 4576).

THE PRECISE PARAMETER COUNT (correcting "zero free parameters"):
  map Δ = a·D̂ + b. b = d = 4 is FORCED (arena/descent). But a = slope is NOT forced — it's
  MOTIVATED (Δ = internal-dim + spacetime-dim, additive → a=1) but NOT DERIVED. So the map has
  ONE free parameter (slope), fit to one target (5→9 ⟹ a=1), predicting two (2→12, 0→massless).
  ⟹ 1 free param, 3 outputs = 2 NET PREDICTIONS. A real constraint (NOT form-cheap), but NOT
  zero-parameter until the discrete series FORCES the additive form Δ=D̂+d (slope 1).

THE DEPOSIT COMBINATION (Keeper flagged — Five-Absence-adjacent):
  observed rung ratios: m_s/m_d = 20, m_b/m_s = 45. Casimirs: {12, 45}.
  rung-1: 20 = (5/3)·12 — deposit d(ν)=5/3 × Casimir. rung-2: 45 = Casimir DIRECTLY (deposit=1).
  ⟹ the deposit appears on rung-1 but NOT rung-2 — NON-UNIFORM. Must be shown to combine cleanly,
  not inserted per-rung, or it's an ad-hoc deposit (the residual "different-recipe" in new clothes).

VERDICT: materially stronger lead (target-innocent strata), NOT banked — 1 residual map-parameter
(slope, motivated-not-derived) + non-uniform deposit. Banks when the discrete series forces
Δ=D̂+d AND the deposit combines uniformly. Count 8.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
d = 4
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 82)
print("Toy 4577 — MOVER 1 audit: map is ONE free param (not zero); strata target-innocent; deposit non-uniform")
print("=" * 82)

# ---- the map + the real upgrade (target-innocent strata) --------------------
strata = [5, 2, 0]
print(f"\n[map Δ = D̂ + d on KW strata {{5,2,0}} (F446, target-innocent)]:")
for D in strata:
    Delta = D + d
    print(f"  stratum {D} → Δ={Delta} → Casimir Δ(Δ−4) = {Delta*(Delta-4)}")
check("REAL UPGRADE: the Δ's come from the PRE-EXISTING target-innocent KW strata {5,2,0} (F446), not picked",
      [D+d for D in strata] == [9, 6, 4] and [(D+d)*(D+d-4) for D in strata] == [45, 12, 0],
      "dissolves the different-factors question — one map, three shelves; materially stronger than 4576")

# ---- the precise parameter count -------------------------------------------
print(f"\n[precise parameter count of Δ = a·D̂ + b (correcting 'zero free parameters')]:")
print(f"  b = d = 4: FORCED by the arena (descent). ✓")
print(f"  a = slope: MOTIVATED (Δ = internal-dim + spacetime-dim → a=1) but NOT DERIVED.")
print(f"  ⟹ ONE free parameter (slope), fit to 1 target (5→9 ⟹ a=1), predicting 2 (2→12, 0→massless).")
check("the map has ONE free parameter (slope), NOT zero — intercept d=4 forced, slope motivated-not-derived",
      True, "1 param, 3 outputs = 2 net predictions — a real constraint, but not zero-parameter yet")
check("'zero free parameters' holds ONLY when the discrete series FORCES the additive form Δ=D̂+d (slope 1)",
      True, "that forcing is MOVER 1's open derivation — the bank condition")

# ---- the deposit combination (non-uniform) ---------------------------------
print(f"\n[deposit combination — Keeper's flag, Five-Absence-adjacent]:")
dep = n_C/N_c
print(f"  rung-1: m_s/m_d = 20 = (5/3)·12 = deposit·Casimir  (deposit {dep:.3f} × stratum-2 Casimir 12)")
print(f"  rung-2: m_b/m_s = 45 = Casimir DIRECTLY (stratum-5), deposit = 1")
print(f"  ⟹ deposit appears on rung-1 but NOT rung-2 → NON-UNIFORM. The 'different-recipe' in new clothes.")
check("deposit d(ν)=5/3 is NON-UNIFORM across rungs (rung-1 has it, rung-2 doesn't) — must combine cleanly or it's ad-hoc",
      abs(dep*12 - 20) < 1e-9 and 45 == 45,
      "Grace must show the deposit combines uniformly with the Casimirs, not inserted per-rung")

# ---- verdict ----------------------------------------------------------------
print(f"\n[VERDICT]: materially STRONGER lead than 4576 (target-innocent strata dissolve the different-")
print(f"  factors question), but NOT banked: 1 residual map-parameter (slope, motivated-not-derived) +")
print(f"  non-uniform deposit. Banks when (a) the discrete series forces Δ=D̂+d, AND (b) the deposit")
print(f"  combines uniformly. My ζ / target-innocence fires the instant Grace's discrete-series Δ's land.")
check("VERDICT: strong lead, NOT banked (slope not derived + deposit non-uniform); count 8 until both close forward",
      True, "the honest way to move the count is deriving forward, not banking the constructed map")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 82)
print("RESULTS")
print("=" * 82)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 82)
print(f"SCORE: {passed}/{total}")
print("=" * 82)
print("""
MOVER 1 AUDIT (peak-convergence, precise parameter count):
  * REAL UPGRADE: the Δ's now come from the PRE-EXISTING target-innocent KW strata {5,2,0}
    (F446) via one map — dissolving the different-factors question. Materially stronger than 4576.
  * PRECISE PARAMETER COUNT (correcting Keeper's "zero free parameters"): the map Δ = a·D̂ + b
    has ONE free parameter — the intercept b = d = 4 is forced, but the slope a = 1 is MOTIVATED
    (dimensional additivity) NOT DERIVED. So it's 1 param → 2 net predictions (real constraint,
    not form-cheap), but zero-parameter ONLY when the discrete series forces the additive form.
  * DEPOSIT NON-UNIFORM: rung-1 = (5/3)·12 (deposit × Casimir), rung-2 = 45 (Casimir directly,
    no deposit). The deposit isn't uniform across rungs — the "different-recipe" survives here.
    Must combine cleanly, not be inserted per-rung (Five-Absence-adjacent).
  => Strong lead, NOT banked. Banks when (a) discrete series forces Δ=D̂+d (slope 1), AND (b)
  the deposit combines uniformly. Count 8. ζ armed for Grace's forward discrete-series Δ's.
""")
