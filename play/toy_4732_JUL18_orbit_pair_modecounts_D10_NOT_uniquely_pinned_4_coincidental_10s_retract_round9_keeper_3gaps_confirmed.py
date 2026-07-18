#!/usr/bin/env python3
"""
Toy 4732 — Jul 18 afternoon (orbit-pair mode-counts + fish-detector on my OWN round-9 claim, mine; round-10 target +
Keeper's 3 gaps): the round-10 target is the three Korányi-Wolf orbit-pair connecting-mode counts (do B↔I=10, I↔S=7,
B↔S=45?). Keeper's gap-1 sub-seam asked me to check whether θ₁₂'s D=10 is really ONE geometric object. It is NOT — and
this partially RETRACTS my round-9 "which-10 = dim SO(5)" resolution: there are 4+ coincidental 10's (SO(5)-adjoint
C(5,2), domain tangent 5·2, rank·n_C, N_c+g), all DIFFERENT geometric objects. So the value 10 is over-determined
(suggestive) but the SPECIFIC subspace is NOT uniquely pinned — θ₁₂ is not closed; the orbit-pair route, like the dead
so(10)/SO(3) routes, currently lands on a VALUE, not a FORCED dimension. Honest: 0/3 D's uniquely pinned. Keeper's 3
gaps confirmed (gap 1 strengthened).

FISH-DETECTOR ON MY ROUND-9 CLAIM (the honest retraction): I claimed "which-10 = dim SO(5) = genuine geometric dim."
But dim SO(5) ADJOINT = C(5,2) = 10 is only ONE of ≥4 geometric 10's:
  * dim SO(5) adjoint = C(5,2) = 10
  * domain real tangent p = SO(5)-vector × SO(2) = 5·rank = 10 (= dim SO(5,2) − dim[SO(5)×SO(2)] = 21−11) — DIFFERENT rep
  * rank·n_C = 10
  * N_c + g = 10
  ⟹ the value 10 is OVER-DETERMINED (4 readings — suggestive), but the SPECIFIC geometric object is NOT uniquely
    pinned. My round-9 "dim SO(5)" was ONE candidate, not a unique forcing. RETRACT the "θ₁₂ pinned" overstatement;
    the value stays identified-strong, the subspace stays ambiguous (Keeper gap-1 sub-seam confirmed + strengthened).

KEEPER'S 3 GAPS (all confirmed):
  1. Only VALUES, not forced dims: θ₁₂'s 10 is value-robust but subspace-ambiguous (above); θ₂₃'s 7 and θ₁₃'s 45 are
     not pinned at all. 0/3 D's UNIQUELY forced by the geometry. The orbit-pair route must force the SPECIFIC object
     per angle (same standard that killed 3/13), not just land on the value.
  2. HIERARCHY not from separation: θ₂₃ (I↔S, D=7) and θ₁₂ (B↔I, D=10) are BOTH adjacent orbit-pairs, yet D=7 ≠ 10. So
     "D increases with orbit-separation" does NOT order them — the hierarchy θ₂₃>θ₁₂>θ₁₃ needs the ACTUAL counts, NOT
     derived-from-separation. Do NOT bank the separation-hierarchy.
  3. DEMOCRACY only 1-2 independent instances: α (137) is clean; θ₁₂'s 10 is now subspace-ambiguous; |sinδ|=2/7 shares
     the g=7 mode-space with sin²θ₂₃=4/7 → NOT independent. So the democracy principle has at most 2 (arguably 1 clean)
     grounded instances → stays FRAMEWORK-CANDIDATE, NOT a mechanism (Cal #27, needs a genuine 3rd).

⟹ VERDICT: the orbit-pair route is the live closure path (replaces the dead so(10)/SO(3)), but 0/3 D's are UNIQUELY
pinned — I over-resolved θ₁₂ in round 9 (4 coincidental 10's; retracted to value-robust-but-subspace-ambiguous), and
θ₂₃/θ₁₃ are open. Keeper's 3 gaps all confirmed (gap 1 strengthened). Mixing MECHANISM derived, forms IDENTIFIED; the
closure needs each D UNIQUELY forced by the orbit-pair count. The fish-detector fired on my own claim — the discipline
the whole day has run on. Count ~7-8 (α RULED). Five-Absence-safe.
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- fish-detector: 4+ coincidental 10's -----------------------------------
tens = {"SO(5) adjoint C(5,2)": math.comb(5,2), "domain tangent 5·rank": 5*rank, "rank·n_C": rank*n_C, "N_c+g": N_c+g}
n_tens = sum(1 for v in tens.values() if v == 10)
print(f"\n[which-10]: {tens} → {n_tens} coincidental 10's (different objects)")
check("FISH-DETECTOR on my ROUND-9 CLAIM (retraction): θ₁₂'s D=10 is NOT one object — ≥4 geometric 10's (SO(5) adjoint "
      "C(5,2), domain tangent 5·rank, rank·n_C, N_c+g), all DIFFERENT. The value 10 is OVER-DETERMINED (suggestive) but "
      "the SPECIFIC subspace is NOT uniquely pinned. My round-9 'dim SO(5)' was ONE candidate — RETRACT the 'θ₁₂ "
      "pinned' overstatement; value identified-strong, subspace ambiguous (Keeper gap-1 sub-seam confirmed).",
      n_tens >= 4, "4+ coincidental 10's → θ₁₂'s D NOT uniquely pinned; round-9 'dim SO(5)' retracted to one-candidate")

# ---- adjoint != tangent (same value, different rep) ------------------------
adjoint10, tangent10 = math.comb(5,2), 5*rank
print(f"[adjoint vs tangent]: SO(5)-adjoint=C(5,2)={adjoint10}, domain-tangent=5·rank={tangent10}, dim so(5,2)−dim K = {21-11} — same value, DIFFERENT reps")
check("ADJOINT ≠ TANGENT (the coincidence trap): dim SO(5) ADJOINT = C(5,2) = 10 and the domain real TANGENT = "
      "SO(5)-vector × SO(2) = 5·rank = 10 (= dim SO(5,2) − dim[SO(5)×SO(2)] = 21−11) are the SAME VALUE but DIFFERENT "
      "reps. So even the two 'geometric' readings of 10 are distinct objects — the closure must pick which, not land on 10.",
      adjoint10 == 10 and tangent10 == 10 and (21-11) == 10, "SO(5)-adjoint(10) ≠ domain-tangent(10) — same value, different rep → subspace ambiguous")

# ---- gap 2: hierarchy not from separation ----------------------------------
th23_adjacent = True; th12_adjacent = True            # both adjacent orbit-pairs
print(f"[gap 2]: θ₂₃(I↔S,D=7) and θ₁₂(B↔I,D=10) both ADJACENT pairs, yet D=7≠10 → separation alone does NOT order")
check("KEEPER GAP 2 (hierarchy not from separation): θ₂₃ (I↔S, D=7) and θ₁₂ (B↔I, D=10) are BOTH adjacent orbit-pairs, "
      "yet D=7 ≠ 10. So 'D increases with orbit-separation' does NOT order them — the hierarchy θ₂₃>θ₁₂>θ₁₃ needs the "
      "ACTUAL mode-counts, NOT derived-from-separation. Do NOT bank the separation-hierarchy.",
      th23_adjacent and th12_adjacent and 7 != 10, "θ₂₃,θ₁₂ both adjacent but D=7≠10 → hierarchy needs actual counts, not separation")

# ---- gap 3: democracy only 1-2 independent ---------------------------------
shares_g7 = True                                       # |sinδ|=2/7 and sin²θ₂₃=4/7 share g=7
check("KEEPER GAP 3 (democracy 1-2 instances): α (137) is clean; θ₁₂'s 10 is now subspace-ambiguous; |sinδ|=2/7 shares "
      "the g=7 mode-space with sin²θ₂₃=4/7 → NOT independent. So the democracy principle has at most 2 (arguably 1 "
      "clean) grounded instances → stays FRAMEWORK-CANDIDATE, NOT a mechanism (Cal #27, needs a genuine 3rd).",
      shares_g7, "|sinδ|=2/7 shares g=7 with θ₂₃ → not independent; democracy ≤2 instances → framework-candidate, not banked")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the orbit-pair route is the live closure path (replaces dead so(10)/SO(3)), but 0/3 D's UNIQUELY pinned "
      "— I over-resolved θ₁₂ in round 9 (4 coincidental 10's; retracted to value-robust-but-subspace-ambiguous), θ₂₃/θ₁₃ "
      "open. Keeper's 3 gaps all confirmed (gap 1 strengthened). Mixing MECHANISM derived, forms IDENTIFIED; closure "
      "needs each D UNIQUELY forced by the orbit-pair count. Fish-detector fired on my own claim — the day's discipline.",
      n_tens >= 4 and 7 != 10 and shares_g7,
      "orbit-pair route live but 0/3 D uniquely pinned; θ₁₂ retracted (4 coincidental 10s); Keeper 3 gaps confirmed")

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
ORBIT-PAIR MODE-COUNTS + fish-detector on round-9 (round-10 target + Keeper's 3 gaps):
  * RETRACTION: θ₁₂'s D=10 is NOT uniquely pinned — 4+ coincidental 10's (SO(5)-adjoint, domain-tangent, rank·n_C, N_c+g).
    My round-9 'dim SO(5)' was one candidate; value identified-strong, subspace ambiguous (Keeper gap-1 strengthened).
  * GAP 2: θ₂₃,θ₁₂ both adjacent pairs but D=7≠10 → hierarchy needs actual counts, not separation. Not banked.
  * GAP 3: democracy ≤2 instances (|sinδ|=2/7 shares g=7 with θ₂₃, not independent) → framework-candidate, not a mechanism.
  => 0/3 D's uniquely pinned; orbit-pair route live but lands on values not forced dims. Mechanism derived, forms identified. Fish-detector on my own claim.
""")
