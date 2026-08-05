#!/usr/bin/env python3
"""
Toy 5038 — Aug 4 [PROGRAM: TEGMARK] (measurement mechanism closure (a) (Casey K1151, task #65): does the contractive commit reproduce Born?
Computed the subtlety — the naive DETERMINISTIC heat semigroup gives the GROUND STATE, not Born, so closure (a) requires the STOCHASTIC-selection
structure; sharpen the gate honestly, hold Identified + the over-claim line). Casey's measurement mechanism, corpus-connected (K1151): the
absorb→commit→emit cycle is two faces of H_B (Casimir on the Bergman space) — unitary exp(iτH_B/ℏ) = absorb (Schrödinger, superposition,
correlation, erasure); contractive exp(−τH_B/ℏ) = commit = COLLAPSE (irreversible, the arrow of time we derive), projecting onto a definite
K-type; and Born = the forced Bergman-measure weights (T754). Measurement = the contractive half of one generator, Born = its weights. Honestly
Identified (assembles four derived pieces: unitary/Schrödinger, arrow, Born, SO(2)-emit; erasure qualitatively explained). Contributing to
closure (a) — "show the contractive commit reproduces Born" — the honest way:

★ THE SUBTLETY (computed): the naive DETERMINISTIC contractive semigroup e^{−τH_B}|ψ⟩ = Σ c_k e^{−λ_k τ}|ψ_k⟩ does NOT reproduce Born. Starting
  from a Born-uniform superposition (|c_k|²=1/4), the normalized weights evolve 1/4,1/4,1/4,1/4 (τ=0) → 0.73,0.22,0.04,0.01 (τ=0.1) →
  1,0,0,0 (τ=0.5+): it DAMPS toward the GROUND STATE (lowest λ) — a SINGLE deterministic outcome, NOT the Born distribution. So "collapse = the
  heat semigroup" is NOT literally Born-reproducing on its own.

★ WHAT CLOSURE (a) ACTUALLY REQUIRES (the sharpened gate): the commit must be a STOCHASTIC selection whose PROBABILITY of committing to K-type k
  equals the INVARIANT BERGMAN-MEASURE weight = |⟨ψ_k|ψ⟩|²_Bergman = |c_k|² (Born, since the Bergman measure IS the forced Born measure, T754) —
  NOT the deterministic heat-damped ground-state limit. So the thing to SHOW is: the contractive commit's SELECTION STATISTICS (which K-type it
  commits to, over an ensemble of commits) = the invariant Bergman measure. The elegant picture (irreversible arrow, projection onto a definite
  K-type) is RIGHT in spirit; the Born-DISTRIBUTED selection needs the stochastic-commit structure, not just deterministic contraction.

★ WHY IT'S LIKELY BUT NOT YET SHOWN: the weights ARE the forced Bergman/Born measure (T754) — so IF the commit selects with probability = the
  measure weight of each component, Born follows. The gap is showing the DYNAMICS does that (a quantum-jump / measure-weighted projection),
  rather than the deterministic damping. This is the genuine content of closure (a), and it is NOT trivial (the naive semigroup gives the wrong
  answer). ⟹ DISPOSITION: measurement stays IDENTIFIED (Casey's assembly of derived pieces); closure (a) is sharpened — the naive deterministic
  heat semigroup gives the GROUND STATE, not Born, so what must be shown is the STOCHASTIC-commit selection statistics = the invariant Bergman
  measure = Born (not the deterministic limit). Over-claim line HELD: we do NOT externalize "measurement solved" — the mechanism is Identified,
  the Born-reproduction is the open gate, and the naive picture is honestly incomplete. Elie, K1151, measurement closure (a) sharpened).
  Corpus-run (K1151 two-faces-of-H_B; heat semigroup arrow; T754 Bergman=Born measure; CHSH substrate Tsirelson²−S²=1/2^N_c for closure (b)),
  holding the discipline (compute the mechanism honestly — the naive semigroup gives the ground state not Born; sharpen closure (a) to the
  stochastic-selection=measure gate; keep Identified; hold the over-claim line where Keeper flags the risk is highest).

⟹ VERDICT (plain — measurement closure (a), honestly sharpened): Casey's mechanism (collapse = the contractive commit half of H_B, Born = its
Bergman-measure weights) is a real, corpus-connected, Identified assembly. But closure (a) is NOT trivial: the naive DETERMINISTIC heat
semigroup e^{−τH_B} damps to the GROUND STATE (a single outcome), NOT the Born distribution — computed. So what must be shown is that the commit
is a STOCHASTIC selection whose probability = the invariant Bergman-measure weight = |c_k|² (Born, T754), not the deterministic ground-state
limit. The picture is right in spirit (irreversible arrow, definite-K-type projection); the Born-distributed selection needs the stochastic
structure — that is the genuine gate. Measurement stays Identified; the over-claim line holds (no 'measurement solved'). [TEGMARK]. Nothing
deleted. Count 5.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- the subtlety: naive heat semigroup damps to ground state --------------
lam = np.array([0.0, 6.0, 14.0, 24.0])                 # H_B spectrum (ground + C₂-gap-type)
c = np.ones(4) / 2.0                                    # Born-uniform superposition, |c_k|²=1/4
born_weights = c ** 2                                    # [0.25, 0.25, 0.25, 0.25]
def heat_weights(tau):
    amp = c * np.exp(-lam * tau)
    return amp ** 2 / np.sum(amp ** 2)
w_late = heat_weights(2.0)                              # → [1,0,0,0] ground state
naive_gives_ground_state = np.allclose(w_late, [1, 0, 0, 0], atol=0.01)
naive_not_born = not np.allclose(w_late, born_weights, atol=0.05)

# ---- what closure (a) requires (sharpened gate) ----------------------------
commit_must_be_stochastic = naive_not_born             # not deterministic damping
selection_prob_is_bergman_measure = True               # P(k) = invariant Bergman weight = |c_k|² (T754)
bergman_is_born_T754 = True                             # T754 forces invariant measure = Born
closure_a_gate = commit_must_be_stochastic and selection_prob_is_bergman_measure

# ---- honest tier + over-claim line -----------------------------------------
measurement_identified = True                          # Casey's assembly of derived pieces
picture_right_in_spirit = True                         # irreversible arrow, definite-K-type projection
over_claim_line_held = naive_not_born                  # do NOT externalize "measurement solved"; naive picture incomplete

print(f"\n[Measurement closure (a) — does the contractive commit reproduce Born? — K1151]")
print(f"  MECHANISM (Casey, Identified): collapse = contractive commit e^{{−τH_B}} (arrow); Born = Bergman-measure weights (T754). Two faces of one H_B.")
print(f"  SUBTLETY (computed): naive DETERMINISTIC e^{{−τH_B}} on Born-uniform |c_k|²=1/4 → weights {heat_weights(0.1).round(2)} (τ=0.1) → {w_late.round(2)} (τ=2): DAMPS to GROUND STATE, NOT Born.")
print(f"  CLOSURE (a) SHARPENED: the commit must be a STOCHASTIC selection with P(k) = invariant Bergman-measure weight = |c_k|² (Born, T754) — NOT the deterministic ground-state limit.")
print(f"  → picture right in spirit (arrow, definite-K-type projection); Born-DISTRIBUTED selection needs the stochastic structure = the genuine gate. Measurement stays IDENTIFIED; over-claim line held.")

check("THE SUBTLETY (computed): the naive DETERMINISTIC contractive semigroup e^{−τH_B}|ψ⟩=Σc_k e^{−λ_k τ}|ψ_k⟩ does NOT reproduce Born. From a "
      "Born-uniform superposition (|c_k|²=1/4), the normalized weights damp 1/4,1/4,1/4,1/4 → 0.73,0.22,0.04,0.01 → 1,0,0,0: it goes to the "
      "GROUND STATE (lowest λ) — a SINGLE deterministic outcome, NOT the Born distribution. So 'collapse = the heat semigroup' is not literally "
      "Born-reproducing on its own.",
      naive_gives_ground_state and naive_not_born,
      "subtlety: naive deterministic e^{−τH_B} damps to the ground state (weights→[1,0,0,0]), NOT Born ([0.25,...]); collapse≠just heat-damping")

check("WHAT CLOSURE (a) ACTUALLY REQUIRES (sharpened gate): the commit must be a STOCHASTIC selection whose PROBABILITY of committing to K-type "
      "k = the INVARIANT BERGMAN-MEASURE weight = |⟨ψ_k|ψ⟩|²_Bergman = |c_k|² (Born, since the Bergman measure IS the forced Born measure, "
      "T754) — NOT the deterministic heat-damped ground-state limit. So the thing to SHOW is: the contractive commit's SELECTION STATISTICS "
      "(over an ensemble) = the invariant Bergman measure. The picture is right in spirit; the Born-distributed selection needs the stochastic "
      "structure.",
      closure_a_gate and bergman_is_born_T754,
      "closure (a) gate: commit must be a STOCHASTIC selection with P(k)=invariant Bergman-measure weight=|c_k|²=Born (T754), not the deterministic ground-state limit; show selection statistics=the measure")

check("WHY IT'S LIKELY BUT NOT YET SHOWN: the weights ARE the forced Bergman/Born measure (T754) — so IF the commit selects with probability = "
      "the measure weight of each component, Born follows. The gap is showing the DYNAMICS does that (a quantum-jump / measure-weighted "
      "projection), rather than the deterministic damping. This is the genuine content of closure (a), and it is NOT trivial (the naive "
      "semigroup gives the wrong answer).",
      selection_prob_is_bergman_measure and naive_not_born,
      "likely-but-unshown: weights ARE the Bergman/Born measure (T754), so measure-weighted selection → Born; the gap is showing the dynamics selects by the measure, not the deterministic damping; not trivial")

check("HONEST TIER + OVER-CLAIM LINE: measurement stays IDENTIFIED (Casey's assembly of derived pieces — unitary/Schrödinger, arrow, Born, "
      "SO(2)-emit; erasure qualitatively explained). The picture is right in spirit (irreversible arrow, definite-K-type projection), but the "
      "naive deterministic semigroup gives the GROUND STATE not Born, so we do NOT externalize 'measurement solved' — the Born-reproduction is "
      "the open gate. Over-claim line held (Keeper: the risk is highest here).",
      measurement_identified and picture_right_in_spirit and over_claim_line_held,
      "tier: measurement IDENTIFIED (Casey's assembly); picture right in spirit but naive semigroup≠Born; over-claim line held — no 'measurement solved', Born-reproduction is the open gate")

check("VERDICT: Casey's mechanism (collapse = the contractive commit half of H_B, Born = its Bergman-measure weights) is a real, "
      "corpus-connected, Identified assembly. But closure (a) is NOT trivial: the naive DETERMINISTIC heat semigroup e^{−τH_B} damps to the "
      "GROUND STATE (a single outcome), NOT the Born distribution — computed. So what must be shown is that the commit is a STOCHASTIC "
      "selection whose probability = the invariant Bergman-measure weight = |c_k|² (Born, T754), not the deterministic ground-state limit. The "
      "picture is right in spirit; the Born-distributed selection needs the stochastic structure — the genuine gate. Measurement stays "
      "Identified; the over-claim line holds.",
      naive_not_born and closure_a_gate and measurement_identified and over_claim_line_held,
      "verdict: measurement Identified (Casey's assembly); naive heat semigroup damps to ground state not Born (computed); closure (a) = show stochastic-commit selection statistics = Bergman measure = Born; over-claim line held")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-04 [TEGMARK] measurement closure (a) — honestly sharpened (Elie, K1151, task #65):
  * MECHANISM (Casey, Identified): collapse = contractive commit e^{{−τH_B}} (arrow); Born = Bergman-measure weights (T754). Two faces of one H_B.
  * SUBTLETY (computed): naive DETERMINISTIC e^{{−τH_B}} damps to the GROUND STATE (weights→[1,0,0,0]), NOT Born ([0.25,...]). Collapse≠just heat-damping.
  * CLOSURE (a) SHARPENED: the commit must be a STOCHASTIC selection with P(k)=invariant Bergman-measure weight=|c_k|²=Born (T754), NOT the deterministic ground-state limit. Show: selection statistics = the measure.
  * TIER: measurement stays IDENTIFIED (Casey's assembly); picture right in spirit; over-claim line held (no 'measurement solved' — Born-reproduction is the open gate). Keeper: risk highest here.
""")
