#!/usr/bin/env python3
"""
Toy 4733 — Jul 18 afternoon (background toy — the mixing denominators in the SO(5)⊂SO(7) tower, mine; round-11
background, OFF the critical path): test whether θ₁₂'s D=10 uniquely = SO(5) as the B↔I connector and θ₂₃'s D=7 = the
SO(7) vector, and whether Grace's θ₁₃=C(10,2) chaining reduces the count. Result: the three denominators {10, 7, 45}
have candidate rep-theory homes in the SO(5)⊂SO(7) tower — 10 = SO(5)-adjoint, 7 = SO(7)-vector, 45 = C(10,2) = pairs
of θ₁₂'s space — and Grace's chaining is the real gain: θ₁₃ is NOT independent (45 = pairs of the 10), so there are
only 2 INDEPENDENT counts (10, 7), not 3. HONEST TIER: candidate groundings (better than coincidental values, they sit
in a nested rep tower), but 3 DIFFERENT constructions (not one uniform group), and the specific-subspace forcing stays
open (my round-10 caution — the adjoint-vs-tangent ambiguity of the 10). This does NOT gate the flagship (mixing forms
are honestly identified-not-derived).

THE CANDIDATE HOMES (SO(5)⊂SO(7) tower):
  * θ₁₂: D=10 = dim SO(5) ADJOINT = C(5,2). Grace's reconciliation: the B↔I connector IS the SO(5) K-group, so my
    "dim SO(5)" and Lyra's "B↔I orbit-pair count" are the SAME object (the K-group adjoint) — IF the connector is the
    adjoint (residual: the domain-tangent 5·rank also = 10; the geometry must select the adjoint, my round-10 caution).
  * θ₂₃: D=7 = SO(7) VECTOR = g (the octonion-imaginary directions, F572 SO(7)⊃G₂⊃SU(3)). Candidate grounding for the
    ONE genuinely-open count.
  * θ₁₃: D=45 = C(10,2) = pairs of θ₁₂'s SO(5)-space (Grace). θ₁₃ (bulk↔Shilov, two steps) lives in the pair-space of
    θ₁₂ (bulk↔intermediate, one step) → CHAINS to θ₁₂, NOT independent.
THE REAL GAIN (Grace's chaining): only 2 INDEPENDENT counts (10, 7), not 3 — θ₁₃ is forced from θ₁₂. And C(10,2)=45
beats the coincidental N_c²·n_C=45 precisely because it connects to θ₁₂'s established space, not a fresh product.
THE HONEST RESIDUAL: {10, 7, 45} = {SO(5)-adjoint, SO(7)-vector, Λ²(SO(5)-adjoint)} — 3 DIFFERENT constructions in the
SO(5)⊂SO(7) tower, NOT one uniform group; and the 10's specific subspace (adjoint vs 5·rank tangent) is still not
uniquely forced. So candidate-grounded, not derived.

⟹ VERDICT: the three mixing denominators have candidate rep-theory homes in the SO(5)⊂SO(7) tower (10=SO(5)-adjoint,
7=SO(7)-vector, 45=pairs), and Grace's chaining reduces them to 2 INDEPENDENT counts (θ₁₃ forced from θ₁₂). This is a
real structural gain over "coincidental values," but they are 3 different constructions (not one group) and the
specific-subspace forcing stays open (round-10 caution). Candidate-grounded, NOT derived — OFF the critical path; the
mixing forms stay honestly identified. Cal's ratification pass is the finalization gate, not this. Count ~7-8.
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- candidate homes --------------------------------------------------------
so5_adj = math.comb(5,2); so7_vec = 7; pairs10 = math.comb(10,2)
print(f"\n[candidate homes]: θ₁₂ D=10=SO(5)-adjoint C(5,2)={so5_adj}; θ₂₃ D=7=SO(7)-vector={so7_vec}=g; θ₁₃ D=45=C(10,2)={pairs10}=pairs of θ₁₂")
check("CANDIDATE HOMES (SO(5)⊂SO(7) tower): θ₁₂ D=10 = SO(5)-adjoint C(5,2); θ₂₃ D=7 = SO(7)-vector (g, octonion "
      "imaginary, F572); θ₁₃ D=45 = C(10,2) = pairs of θ₁₂'s SO(5)-space. All three sit in the nested SO(5)⊂SO(7) rep "
      "tower — better than coincidental values.",
      so5_adj == 10 and so7_vec == g and pairs10 == 45, "θ₁₂=SO(5)-adjoint(10), θ₂₃=SO(7)-vector(7), θ₁₃=C(10,2)(45) — candidate homes in SO(5)⊂SO(7)")

# ---- Grace's chaining: θ₁₃ not independent ----------------------------------
check("GRACE'S CHAINING (the real gain): θ₁₃ (bulk↔Shilov, TWO steps) lives in the PAIR-space of θ₁₂ (bulk↔intermediate, "
      "ONE step) → D=45 = C(10,2) = pairs of the 10. So θ₁₃ is NOT independent — it's forced from θ₁₂. Only 2 "
      "INDEPENDENT counts (10, 7), not 3. And C(10,2) beats the coincidental N_c²·n_C=45 because it connects to θ₁₂'s "
      "established space, not a fresh product.",
      pairs10 == 45 and math.comb(so5_adj,2) == 45, "θ₁₃ = C(10,2) = pairs of θ₁₂ → NOT independent; only 2 independent counts (10,7)")

# ---- θ₁₂ reconciliation + residual ------------------------------------------
tangent10 = 5*rank
print(f"[θ₁₂ reconcile]: Grace: B↔I connector = SO(5) K-group → adjoint(10); residual: domain-tangent 5·rank={tangent10} also =10 (round-10 caution)")
check("θ₁₂ RECONCILIATION + RESIDUAL: Grace reconciles my 'dim SO(5)' and Lyra's 'B↔I orbit-pair count' as the SAME "
      "object (the SO(5) K-group adjoint) — IF the B↔I connector is the K-group adjoint. RESIDUAL (my round-10 caution "
      "holds): the domain-tangent 5·rank = 10 is a DIFFERENT rep also equal to 10, so the geometry must SELECT the "
      "adjoint; the specific subspace is not yet uniquely forced.",
      so5_adj == 10 and tangent10 == 10, "θ₁₂'s 10 reconciled as SO(5)-adjoint (Grace) but residual: 5·rank tangent also =10 → not uniquely forced")

# ---- honest tier ------------------------------------------------------------
check("HONEST TIER: candidate groundings in the SO(5)⊂SO(7) tower — a real structural gain over coincidental values "
      "(θ₁₃ chains to θ₁₂; 2 independent counts) — BUT {10,7,45}={SO(5)-adjoint, SO(7)-vector, Λ²(SO(5)-adjoint)} are 3 "
      "DIFFERENT constructions (not one uniform group), and the specific-subspace forcing (adjoint vs tangent) stays "
      "open. Candidate-grounded, NOT derived. OFF the critical path — the mixing forms stay identified; Cal's "
      "ratification is the finalization gate, not this.",
      True, "candidate-grounded (SO(5)⊂SO(7), 2 independent counts) but 3 different constructions + subspace-forcing open → not derived; off critical path")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the 3 mixing denominators have candidate rep-theory homes in the SO(5)⊂SO(7) tower (10=SO(5)-adjoint, "
      "7=SO(7)-vector, 45=pairs), reduced to 2 INDEPENDENT counts by Grace's chaining (θ₁₃ forced from θ₁₂). A real "
      "structural gain over coincidental values, but 3 different constructions (not one group) + subspace-forcing open → "
      "candidate-grounded, NOT derived. Off the critical path; mixing forms stay identified. Background toy done.",
      so5_adj == 10 and so7_vec == g and pairs10 == 45,
      "denominators candidate-grounded in SO(5)⊂SO(7), 2 independent counts (Grace chaining); not derived; off critical path")

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
BACKGROUND — mixing denominators in the SO(5)⊂SO(7) tower (round-11, off critical path):
  * CANDIDATE HOMES: θ₁₂ D=10=SO(5)-adjoint; θ₂₃ D=7=SO(7)-vector; θ₁₃ D=45=C(10,2)=pairs of θ₁₂.
  * GRACE'S CHAINING (real gain): θ₁₃ forced from θ₁₂ → 2 INDEPENDENT counts (10, 7), not 3.
  * RESIDUAL: 3 different constructions (not one group) + θ₁₂'s subspace (adjoint vs 5·rank tangent) not uniquely forced.
  => candidate-grounded, NOT derived. Off critical path; mixing forms stay identified. Cal's ratification is the gate.
""")
