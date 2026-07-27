#!/usr/bin/env python3
"""
Toy 4884 — Jul 27 [PROGRAM: TEGMARK] (A2 setup: the UNIFORM generation-mode definition + the honest 3-vs-4 fork; Elie, pull 27k,
with Lyra). K948 relocated the critical path: the fulcrum is NOT one check from closing. Deliverable A gave the interior 2
(idempotent modes, IF φ spectral); Deliverable B (Cal) confirmed the electron mode exists (b ≥ 1) but the count is 2 interior +
b boundary with b ∈ {1,2} UNSETTLED — a REAL 3-vs-4 fork. Casey's steer: DO NOT force 3; let the geometry give 3 or 4 (a
four-generation geometry is a live falsification, and a real result). The critical path = the UNIFORM generation-mode definition
applied to the sub-threshold boundary. This toy sets that up concretely + honestly; it does NOT decide b (that needs the sourced
FK normalizability criterion — pull it, don't reconstruct).

THE NON-UNIFORMITY PROBLEM (K948, the trap to avoid): "generation = idempotent" gives 2 (muon, tau on the two Jordan
idempotents) and THROWS OUT the electron (a boundary mode). That definition is non-uniform (two kinds of object). The real
question: what SINGLE, uniform definition of a generation-mode covers all three — and applied to the boundary sub-threshold
window, does it admit ONE mode (→ total 3) or TWO (→ total 4)?

THE CANDIDATE MODES (GIVEN, K945 ledger — F326): the boundary highest-weight modes ψ_k = (z₁+iz₂)^k ⊗ u₀, k=0,1,2, carry SO(5)
content (k+½, ½). Computed dims (SO(5)=B₂, dim(a,b) = ⅙(a−b+1)(a+b+2)(2a+3)(2b+1)):
  * k=0: (½,½) → dim 4  = the spinor-4 = the Di singleton lowest K-type (GIVEN check, matches).
  * k=1: (3/2,½) → dim 16.
  * k=2: (5/2,½) → dim 40.
The upper bound ≤3 (no 4th generation) is GIVEN/solid (rank-2 Wallach 2 points; matryoshka terminal; Q⁵ no h⁷).

THE FORK (K948, target-innocent — the count is whatever the geometry gives):
  * total generations = 2 interior idempotent-modes + b boundary modes, with b = #{k ∈ {1,2} : ψ_k is normalizable under the
    CORRECT sub-threshold criterion}.
  * b = 1 → total 3 → rank=2 premise ELIMINATED, E7-by-data exclusion airtight.
  * b = 2 → total 4 → observed 3 becomes a DATA CUT (not a geometric forcing), a live falsification of "geometry forces 3."

THE TWO TARGET-INNOCENCE GUARDS (K948, MUST hold): (1) do NOT define "generation = idempotent" (that throws out the electron and
pre-decides 2); (2) do NOT exclude k=2 by the observed count OR by "filtration = generations" (circular — the exclusion
arguments Cal found for a 2nd boundary mode were circular, ratified). The norm INTEGRAL decides b, nothing else.

THE NORM-COUNT RECIPE (what A2 computes when the sourced material is on the table): b = the number of ψ_k (k=1,2) with
‖ψ_k‖² = ∫_{D_IV⁵} |ψ_k|² dμ < ∞ under the correct sub-threshold normalizability criterion. THE NEEDED SOURCED INPUT (do NOT
reconstruct from memory — K945 discipline): the FK weighted measure on the type-IV Lie ball + the sub-threshold/degenerate-rep
normalizability criterion (Rossi-Vergne k_min continuation; Enright-Howe-Wallach unitarizable HW modules; FK Ch. XII-XIII). The
GIVEN k≥k_min=3 square-integrability puts k=0,1,2 sub-threshold — so the STANDARD Bergman L² is NOT the right criterion for the
boundary modes; the degenerate/Hardy normalizability is. Getting that criterion right IS deciding b — the one finite computation.

⟹ VERDICT (plain): A2 is set up honestly — the critical path is the UNIFORM generation-mode definition applied to the boundary
sub-threshold window {k=1,2}, deciding b ∈ {1,2} → total 3 or 4. The candidate modes and their SO(5) K-types (dims 4/16/40, k=0
= spinor-4 GIVEN-check) are computed; the fork is stated target-innocently (do NOT force 3; geometry-4 is a live falsification);
the two guards (no gen=idempotent, no data/filtration exclusion of k=2) are named. The DECIDER is the finite norm count b under
the correct sub-threshold criterion — which needs the sourced FK measure + Rossi-Vergne/EHW continuation (NOT reconstructed).
This toy does NOT decide b; premise stays REDUCED until A1 (φ-spectral, Grace) + A2 (b, this recipe with Lyra + sourced material)
land. [TEGMARK]. Feeds K948 A2. Nothing deleted. Count 6.
"""
from fractions import Fraction as F
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def dimB2(a, b):  # SO(5)=B2 irrep dimension for highest weight (a,b)
    return F(1, 6) * (a - b + 1) * (a + b + 2) * (2 * a + 3) * (2 * b + 1)

ktypes = {k: (F(2 * k + 1, 2), F(1, 2)) for k in (0, 1, 2)}
dims = {k: dimB2(*ktypes[k]) for k in (0, 1, 2)}
print(f"\n[A2 setup] SO(5) K-type ladder (F326 ψ_k, content (k+½,½)): k=0→{dims[0]} (spinor-4), k=1→{dims[1]}, k=2→{dims[2]}. Fork: 2 interior + b (b∈{{1,2}}) → 3 or 4. Decider = norm count (needs FK sub-threshold criterion).")

check("CANDIDATE MODES + SO(5) K-types (computed, GIVEN-check): ψ_k (k=0,1,2) carry SO(5) content (k+½,½) with dims 4, 16, 40. "
      "k=0 dim 4 = the spinor-4 = the Di singleton lowest K-type — matches the GIVEN, confirming the ladder.",
      dims[0] == 4 and dims[1] == 16 and dims[2] == 40,
      "SO(5) ladder dims 4/16/40 for k=0/1/2; k=0=spinor-4 matches Di lowest K-type (GIVEN check) — the candidate generation ladder")

check("THE NON-UNIFORMITY PROBLEM (K948): 'generation = idempotent' gives 2 (interior) and THROWS OUT the electron (boundary) — "
      "non-uniform, pre-decides 2. The critical path is a SINGLE uniform definition covering all three, applied to the boundary "
      "to decide b. This toy sets that requirement; it does not pick the definition (joint with Lyra).",
      True,
      "non-uniformity: gen=idempotent throws out the electron; need ONE uniform definition covering all 3, applied to boundary → b")

check("THE FORK (target-innocent, DO NOT force 3): total = 2 interior + b, b = #{k∈{1,2}: ψ_k normalizable}. b=1 → 3 (premise "
      "ELIMINATED); b=2 → 4 (observed 3 = a data cut, a LIVE falsification of geometry-forces-3). The count is whatever the "
      "geometry gives.",
      True,
      "fork: 2 + b, b∈{1,2} → total 3 or 4; b=1 eliminates premise, b=2 = 4-gen falsification risk; do NOT force 3")

check("THE TWO GUARDS (K948, must hold): (1) do NOT define generation=idempotent (throws out electron, pre-decides 2); (2) do "
      "NOT exclude k=2 by the observed count or by filtration=generations (circular — Cal's ratified refusal). Only the norm "
      "integral decides b.",
      True,
      "guards: no gen=idempotent; no data/filtration exclusion of k=2 (circular); the norm integral alone decides b")

check("THE DECIDER + NEEDED SOURCED INPUT (not faked): b = #{ψ_k (k=1,2) with ‖ψ_k‖²<∞} under the CORRECT sub-threshold "
      "criterion. k=0,1,2 are sub-threshold (GIVEN k_min=3), so standard Bergman L² is NOT the criterion — the degenerate/Hardy "
      "normalizability is (Rossi-Vergne continuation, Enright-Howe-Wallach, FK Ch. XII-XIII). PULL it, don't reconstruct.",
      True,
      "decider = finite norm count under the sub-threshold criterion (Rossi-Vergne/EHW/FK Ch.XII-XIII); needs sourced material, not reconstructed")

check("VERDICT: A2 set up honestly — critical path = uniform generation-mode definition on the boundary window {k=1,2} deciding "
      "b∈{1,2} → 3 or 4. K-types computed (4/16/40); fork target-innocent (don't force 3, geometry-4 a live falsification); two "
      "guards named; decider = the finite norm count under the sourced FK sub-threshold criterion. b NOT decided here; premise "
      "REDUCED until A1(Grace φ)+A2(b, with Lyra) land.",
      dims[0] == 4 and dims[2] == 40,
      "A2 set up: uniform-definition path, 3-vs-4 fork target-innocent, guards named, decider=norm count (sourced FK criterion); b not decided; premise REDUCED")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-27 [TEGMARK] A2 setup — the UNIFORM generation-mode definition + the 3-vs-4 fork (Elie, pull 27k, with Lyra, per K948):
  * CANDIDATE MODES: ψ_k (k=0,1,2), SO(5) content (k+½,½), dims 4/16/40 (k=0 = spinor-4 = Di lowest K-type, GIVEN check).
  * CRITICAL PATH: NOT "is φ spectral" alone (interior 2) — it's a UNIFORM generation-mode definition applied to the boundary to decide b∈{1,2} → total 3 or 4. Non-uniformity trap: gen=idempotent throws out the electron.
  * TARGET-INNOCENT: do NOT force 3 (geometry-4 = live falsification); guards = no gen=idempotent, no data/filtration exclusion of k=2. The finite NORM COUNT decides b — under the sourced FK sub-threshold criterion (Rossi-Vergne/EHW/FK Ch.XII-XIII), NOT reconstructed.
  * b NOT decided here (setup). Premise REDUCED until A1 (Grace φ-spectral) + A2 (b, with Lyra + sourced material) land.
""")
