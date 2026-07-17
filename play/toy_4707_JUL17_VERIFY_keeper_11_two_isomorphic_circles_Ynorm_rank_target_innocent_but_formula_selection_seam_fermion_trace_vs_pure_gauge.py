#!/usr/bin/env python3
"""
Toy 4707 — Jul 17 (VERIFY Keeper's (1,1)-over-two-isomorphic-circles candidate for sin²θ_W, mine; fish-detector on the
Vol 60 marquee BEFORE the team computes): the team pull asks me to independently rebuild ‖Y‖²=rank from the SO(5)×SO(2)
structure (NOT inherit the number) and run the three bars. Keeper's candidate: D_IV⁵ and its compact dual Q⁵ share
isotropy SO(5)×SO(2) → two isomorphic SO(2) circles; hypercharge threads both (quarks carry charge AND color) → Y is
the (1,1) diagonal → ‖Y‖² = 1²+1² = 2 = rank. Result: the ‖Y‖²=rank IS clean and target-innocent (the 2 counts faces,
not back-solved from 3/13) — that part checks. BUT there is a REAL SEAM the "one geometric fact from closing" framing
hides: ‖Y‖²=rank feeds the PURE-GAUGE formula → 1/3 (Lyra's catch), NOT the FERMION-TRACE formula → 3/13. So deriving
‖Y‖²=rank alone gives 1/3, the wrong number. Getting 3/13 additionally requires the fermion-trace-with-normalization
formula — which is the GUT prediction formula, exactly what Five-Absence forbids. The derivation has TWO parts, and the
second (why fermion-trace, not pure-gauge) is the harder, GUT-adjacent one, not yet addressed.

THE THREE NUMBERS (verified — three DIFFERENT formulas, confirming Lyra's catch):
  * (A) PURE-GAUGE Killing (‖T₃‖²=1, ‖Y‖²=rank; coupling ∝ 1/norm ⟹ g'²/g² = 1/rank): sin²θ_W = 1/(1+rank) = 1/3.
  * (B) FERMION-TRACE, physical charges: Tr(T₃²)/Tr(Q²) = 2/(16/3) = 3/8 (the forbidden GUT value).
  * (C) FERMION-TRACE × hypercharge normalization c²=rank: 2/(2+rank·10/3) = 3/13 (BST, matches obs 0.2312).
  ⟹ 3/13 is NOT a pure-gauge number (that's 1/3); it is the fermion trace × the √rank normalization.

THE (1,1)/TWO-CIRCLES CHECK: |Y|² = |(1,1)|² = 1²+1² = 2 = rank. TARGET-INNOCENT — the 2 counts the two Cartan-dual
faces (D_IV⁵ + Q⁵ share SO(5)×SO(2)), NOT back-solved from 3/13. Keeper's structural candidate is clean at this step.

THE SEAM (my fish — the framing hides two open parts, not one):
  * PART 1: derive ‖Y‖² = rank from the (1,1) two-circle geometry. Candidate is clean + target-innocent (above).
  * PART 2 (the harder one): ‖Y‖²=rank feeds the PURE-GAUGE formula → 1/3 (WRONG). To get 3/13 you must use the
    FERMION-TRACE formula with the physical charges — which at c²=1 is EXACTLY the GUT prediction 3/8. So the derivation
    must justify WHY the fermion-trace normalization (c²=rank) is the physical sin²θ_W and the pure-gauge ratio (1/3) is
    not — and it must do so WITHOUT smuggling in the GUT unification the formula came from (Five-Absence forbids GUTs).
  * NOTATIONAL FLAG: "Q = T₃ + √rank·Y" read literally changes physical charges (electron → −1/2−√2/2 ≠ −1). The √rank
    is a hypercharge NORMALIZATION / coupling factor, NOT a rescaling of the charge operator. State it precisely.

⟹ VERDICT: Keeper's (1,1)/two-isomorphic-circles gives ‖Y‖²=rank cleanly and target-innocently (2 = # dual faces) —
a good candidate for PART 1. But sin²θ_W is NOT "one geometric fact from closing": ‖Y‖²=rank alone gives the pure-gauge
1/3, and reaching 3/13 needs the fermion-trace formula (GUT-flavored, Five-Absence-adjacent) — PART 2, the deeper open
work. Hold sin²θ_W at REDUCED-TO-LEAD, NOT derived. Flag the seam to the team before they compute expecting one number
to close it. Count ~7-8 (α RULED). Five-Absence: value passes (3/13≠3/8) but the fermion-trace RELIANCE is the flag.
"""
from fractions import Fraction as F
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- the three numbers (three different formulas) ---------------------------
gp2_over_g2 = F(1, rank)                                  # coupling ∝ 1/norm, ‖Y‖²=rank
sinA = gp2_over_g2/(1+gp2_over_g2)                        # pure gauge Killing
Tr_T3sq, Tr_Qsq, Tr_Ysq = F(2), F(16,3), F(10,3)
sinB = Tr_T3sq/Tr_Qsq                                     # fermion trace, physical
sinC = Tr_T3sq/(Tr_T3sq + rank*Tr_Ysq)                   # fermion trace × c²=rank
print(f"\n[three numbers]: (A) pure-gauge Killing = {sinA} = {float(sinA):.4f}; (B) fermion trace = {sinB} = {float(sinB):.4f} (GUT); (C) fermion trace × c²=rank = {sinC} = {float(sinC):.4f} (BST, obs 0.2312)")
check("THREE NUMBERS VERIFIED (three different formulas — confirms Lyra's catch): (A) pure-gauge Killing with ‖Y‖²=rank "
      "→ 1/3; (B) fermion trace physical → 3/8 (forbidden GUT); (C) fermion trace × c²=rank → 3/13 (BST, obs). So 3/13 "
      "is NOT a pure-gauge number (that's 1/3) — it is the fermion trace × the √rank normalization.",
      sinA == F(1,3) and sinB == F(3,8) and sinC == F(3,13), "1/3 (pure gauge) ≠ 3/8 (fermion GUT) ≠ 3/13 (BST) — three formulas; 3/13 is fermion-trace×√rank")

# ---- (1,1)/two-circles → ‖Y‖²=rank, target-innocent -------------------------
Ynorm_sq = 1**2 + 1**2                                    # (1,1) diagonal over two isomorphic circles
print(f"[(1,1)/two circles]: |Y|² = |(1,1)|² = 1²+1² = {Ynorm_sq} = rank; the 2 counts the two Cartan-dual faces (D_IV⁵ + Q⁵ share SO(5)×SO(2))")
check("(1,1)/TWO-CIRCLES → ‖Y‖²=rank, TARGET-INNOCENT (Keeper's candidate, PART 1): |Y|² = |(1,1)|² = 1²+1² = 2 = rank. "
      "The 2 counts the two Cartan-dual faces (D_IV⁵ + compact dual Q⁵ share isotropy SO(5)×SO(2)), NOT back-solved from "
      "3/13. Clean + target-innocent at this step — a good candidate for the hypercharge norm.",
      Ynorm_sq == rank, "|Y|²=|(1,1)|²=2=rank from two dual faces — target-innocent (2=#faces, not fit to 3/13)")

# ---- THE SEAM: ‖Y‖²=rank feeds pure-gauge (1/3), NOT fermion-trace (3/13) ---
check("THE SEAM (my fish — PART 2, the harder open part): ‖Y‖²=rank feeds the PURE-GAUGE formula → 1/3 (Lyra's number), "
      "NOT the fermion-trace → 3/13. So deriving ‖Y‖²=rank ALONE gives the WRONG number (1/3). Reaching 3/13 "
      "additionally requires the FERMION-TRACE formula with physical charges — which at c²=1 is EXACTLY the GUT "
      "prediction 3/8. The derivation must justify WHY the fermion-trace normalization is the physical sin²θ_W and the "
      "pure-gauge ratio (1/3) is not — WITHOUT smuggling in the GUT unification the formula came from (Five-Absence).",
      sinA == F(1,3) and sinC == F(3,13) and sinA != sinC,
      "‖Y‖²=rank → pure-gauge 1/3 (wrong), not fermion-trace 3/13 — the formula-selection is PART 2, the deeper open work")

# ---- notational flag + Five-Absence -----------------------------------------
check("NOTATIONAL FLAG + FIVE-ABSENCE: 'Q = T₃ + √rank·Y' read literally changes physical charges (electron → "
      "−1/2−√2/2 ≠ −1) — the √rank is a hypercharge NORMALIZATION/coupling factor, NOT a rescaling of the charge "
      "operator; state it precisely. FIVE-ABSENCE: the value passes (3/13 ≠ forbidden 3/8), but the RELIANCE on the "
      "fermion-trace formula (whose c²=1 IS the GUT value) is the flag — the derivation must show that formula is "
      "Cartan-dual-geometric, not smuggled GUT.",
      sinC != F(3,8), "√rank is a normalization not a charge rescaling; 3/13≠3/8 passes but the fermion-trace reliance is the Five-Absence flag")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: Keeper's (1,1)/two-isomorphic-circles gives ‖Y‖²=rank cleanly + target-innocently (2 = # dual faces) — "
      "a good candidate for PART 1. But sin²θ_W is NOT 'one geometric fact from closing': ‖Y‖²=rank alone gives the "
      "pure-gauge 1/3, and reaching 3/13 needs the fermion-trace formula (GUT-flavored, Five-Absence-adjacent) — PART 2, "
      "the deeper open work not yet addressed. HOLD sin²θ_W at REDUCED-TO-LEAD, NOT derived. Flag the seam to the team "
      "before they compute expecting one number to close it. Count ~7-8 (α RULED).",
      Ynorm_sq == rank and sinA != sinC and sinC == F(3,13),
      "‖Y‖²=rank target-innocent (part 1 good), but formula-selection seam (1/3 vs 3/13) is part 2 → sin²θ_W stays reduced-to-lead, NOT derived")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 100)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 100)
print(f"SCORE: {passed}/{total}")
print("=" * 100)
print("""
VERIFY Keeper's (1,1)/two-isomorphic-circles candidate — target-innocent for ‖Y‖²=rank, but a REAL formula seam:
  * THREE numbers (3 formulas): pure-gauge Killing 1/3 ≠ fermion-trace 3/8 (GUT) ≠ BST 3/13. 3/13 = fermion trace × √rank.
  * (1,1)/two circles → ‖Y‖²=1²+1²=2=rank — TARGET-INNOCENT (2 = # dual faces, not fit). Good candidate for PART 1.
  * THE SEAM (PART 2, harder): ‖Y‖²=rank feeds pure-gauge → 1/3 (WRONG), not fermion-trace → 3/13. The derivation must
    justify the fermion-trace formula (GUT-flavored) over the pure-gauge one, without smuggling GUT (Five-Absence).
  * NOTATION: √rank is a hypercharge NORMALIZATION, not a charge-operator rescaling (else charges break).
  => ‖Y‖²=rank target-innocent, but sin²θ_W is NOT one-fact-from-closing → HOLD reduced-to-lead, NOT derived. Count ~7-8.
""")
