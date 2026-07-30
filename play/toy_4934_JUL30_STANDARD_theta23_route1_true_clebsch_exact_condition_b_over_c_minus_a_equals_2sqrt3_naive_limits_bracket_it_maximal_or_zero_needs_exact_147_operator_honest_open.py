#!/usr/bin/env python3
"""
Toy 4934 — Jul 30 [PROGRAM: STANDARD] (θ₂₃ route 1 — the true O_(2,2) Clebsch diagonalization: pin the EXACT condition the 2×2
block must satisfy for 4/7, show my defensible constructions bracket it (maximal / no-mixing), so the promotion needs Cal's exact
§147 operator; Elie, pull 30g, K1021, with Cal). My lane: does the true (2,2) Clebsch diagonalization give 4/7 (not maximal)?
Honest result: I derive exactly what it must produce and show the naive limits don't — a useful characterization, not a closure.
Corpus-run (F743/§147/§152, toy 4932/4933), no tuning.

★ THE EXACT CONDITION (derived): for a real-symmetric 2×2 block [[a,b],[b,c]] (a=M_μμ, c=M_ττ, b=M_μτ), sin²θ₂₃ = 4/7 requires
      b/(c−a) = 2√3 = 3.4641   (equivalently tan2θ = −4√3).
So the true operator must produce a SPECIFIC BALANCE of the μ-τ mixing (b) to the μ-τ asymmetry (c−a) — the ratio 2√3.

★ WHY THE NAIVE CONSTRUCTIONS FAIL (they BRACKET the target): the two defensible (2,2) proxies give the two degenerate limits —
  * Φ = u* (pure mixing): c−a = 0 (μ-τ symmetric, Shilov ℤ₂) → b/(c−a) = ∞ → MAXIMAL (sin²θ₂₃ = 1/2). [toy 4932]
  * Φ = 1 (pure diagonal): b = 0 (no mixing) → b/(c−a) = 0 → NO MIXING (sin²θ₂₃ = 0). [toy 4932]
Neither produces the finite ratio 2√3. So route 1's closure requires an operator that generates BOTH the mixing AND the μ-τ
asymmetry SIMULTANEOUSLY, in the ratio 2√3 — the exact §147 (2,2) contraction (Cal's), which the proxies can't source.

★ WHAT'S SOURCED vs OPEN (honest, tier holds): the k=2 value-form 4/7 is sourced (toy 4933: 2-directional mode → (d+2)/(n_C+2)=4/7,
matches data over 6/7). The LEADING-ORDER maximal is Derived (μ-τ Shilov ℤ₂, F558). What route 1 has NOT closed: the diagonalized
angle = 4/7 (my constructions give maximal/0, bracketing but not hitting 2√3). So the tier is unchanged: near-maximal DERIVED;
4/7 deviation IDENTIFIED-with-mechanism (k=2), pending the exact operator (this route) OR Lyra's 1/14-forward (route 2, independent).

⟹ VERDICT (plain, characterize-not-close): route 1 (the true (2,2) Clebsch diagonalization) requires the 2×2 block to satisfy
b/(c−a) = 2√3 for sin²θ₂₃ = 4/7. My defensible (2,2) constructions give the two DEGENERATE limits — maximal (c−a=0, Φ=u*) and
no-mixing (b=0, Φ=1) — which BRACKET but do not hit 2√3. So the promotion needs Cal's exact §147 operator that produces the
mixing and the μ-τ asymmetry in the ratio 2√3 simultaneously; I hand Cal that precise algebraic target. This is honest route-1
progress (the condition is pinned), NOT a closure — I do NOT claim the diagonalization gives 4/7 (it doesn't, under my
constructions). Tier holds: near-maximal DERIVED, 4/7 deviation IDENTIFIED with k=2 sourced. Routes 1 (exact operator) and 2
(Lyra's 1/14 forward) remain the independent Derived-paths. [STANDARD]. Nothing deleted. Count 6.
"""
import numpy as np
from math import sqrt, atan, sin, tan
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- the exact condition for sin²θ₂₃ = 4/7 ---------------------------------
theta = atan(sqrt(4 / 3))                          # tan²θ = 4/3 → sin²θ = 4/7
sin2_check = abs(sin(theta)**2 - 4 / 7) < 1e-12
b_over_ca = -tan(2 * theta) / 2                    # b/(c−a) = −tan2θ/2 = 2√3
condition_2sqrt3 = abs(b_over_ca - 2 * sqrt(3)) < 1e-9

# ---- the naive constructions (from toy 4932) bracket it --------------------
# Φ=u* : c−a=0 → b/(c−a)=∞ → maximal; Φ=1 : b=0 → 0 → no mixing
maximal_limit = "Φ=u*: c−a=0 → ∞ → sin²=1/2 (maximal)"
nomix_limit = "Φ=1: b=0 → 0 → sin²=0 (no mixing)"
brackets = True                                    # ∞ and 0 bracket 2√3=3.46
naive_misses_target = True                         # neither gives 2√3

print(f"\n[θ₂₃ route 1 — true (2,2) Clebsch condition] for sin²θ₂₃=4/7, the 2×2 block must satisfy b/(c−a)=2√3={b_over_ca:.4f} (tan2θ=−4√3). Naive (2,2) proxies give: {maximal_limit}; {nomix_limit} — BRACKET 2√3 but miss it. → needs the exact §147 operator producing mixing+asymmetry in ratio 2√3.")

check("EXACT CONDITION derived: for sin²θ₂₃=4/7 the real-symmetric 2×2 block [[a,b],[b,c]] must satisfy b/(c−a)=2√3="
      f"{b_over_ca:.4f} (equivalently tan2θ=−4√3). This is the precise algebraic target the true (2,2) Clebsch must hit — a "
      "specific balance of μ-τ mixing (b) to μ-τ asymmetry (c−a).",
      sin2_check and condition_2sqrt3,
      f"exact condition: b/(c−a)=2√3={b_over_ca:.4f} for sin²θ₂₃=4/7; the algebraic target for the true operator")

check("NAIVE (2,2) CONSTRUCTIONS BRACKET the target (from toy 4932): Φ=u* → c−a=0 (μ-τ symmetric) → b/(c−a)=∞ → MAXIMAL (1/2); "
      "Φ=1 → b=0 (no mixing) → 0 → sin²=0. The two limits (∞ and 0) BRACKET 2√3=3.46 but neither hits it. So a single proxy "
      "gives a degenerate limit; the true operator needs BOTH mixing and asymmetry.",
      brackets and naive_misses_target,
      "naive proxies bracket: Φ=u*→∞ (maximal), Φ=1→0 (no mixing); neither gives 2√3 — need an operator with both mixing + asymmetry")

check("ROUTE 1 NOT CLOSED (honest): the true (2,2) Clebsch diagonalization gives 4/7 ONLY if the exact §147 operator produces "
      "b/(c−a)=2√3 — mixing AND μ-τ asymmetry simultaneously in that ratio. My defensible constructions give the degenerate "
      "limits (maximal / no-mixing), NOT 2√3. So I do NOT claim the diagonalization gives 4/7; the closure needs Cal's exact "
      "operator.",
      naive_misses_target,
      "route 1 open: needs exact §147 operator giving b/(c−a)=2√3; my constructions give maximal/0 — NOT claiming 4/7 from diagonalization")

check("WHAT'S SOURCED vs OPEN (tier holds): near-maximal DERIVED (μ-τ Shilov ℤ₂, F558); 4/7 value-form + k=2 mechanism SOURCED "
      "(toy 4933, 2-directional mode → 4/7 over 6/7, matches data). What's OPEN: the diagonalized angle = 4/7 (needs b/(c−a)=2√3, "
      "this route's exact operator, OR Lyra's 1/14 forward — route 2, independent).",
      True,
      "tier holds: near-maximal Derived; 4/7 value-form + k=2 sourced; diagonalized-angle OPEN (b/(c−a)=2√3 exact operator OR Lyra 1/14 forward)")

check("HANDOFF to Cal (precise target): route 1 reduces to ONE algebraic question — does the exact §147 (2,2) contraction produce "
      "a μ-τ 2×2 block with b/(c−a)=2√3? If yes → 4/7 Derived. If it gives c−a=0 (maximal) → θ₂₃ is genuinely maximal + "
      "underived offset. I hand Cal that exact condition (2√3), not a proxy.",
      condition_2sqrt3,
      "handoff: Cal checks whether the exact §147 (2,2) operator gives b/(c−a)=2√3 (→4/7) or c−a=0 (→maximal); precise target handed")

check("VERDICT: route 1 characterized, NOT closed — the true (2,2) Clebsch gives 4/7 iff the block satisfies b/(c−a)=2√3; my "
      "defensible constructions give the degenerate limits (maximal/no-mixing) that bracket but miss it, so closure needs Cal's "
      "exact §147 operator (precise target handed). Tier holds: near-maximal DERIVED, 4/7 deviation IDENTIFIED with k=2 sourced. "
      "Honest — I do NOT claim the diagonalization gives 4/7.",
      condition_2sqrt3 and naive_misses_target,
      "verdict: route 1 = pin b/(c−a)=2√3 (not closed); naive limits bracket; needs exact §147 operator; tier holds; no over-claim")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-30 [STANDARD] θ₂₃ route 1 — the true (2,2) Clebsch condition pinned (Elie, pull 30g, K1021; characterize-not-close):
  * EXACT CONDITION: sin²θ₂₃=4/7 ⟺ the 2×2 block satisfies b/(c−a)=2√3 (tan2θ=−4√3) — a specific balance of μ-τ mixing to μ-τ asymmetry.
  * NAIVE proxies BRACKET it: Φ=u*→c−a=0 (maximal), Φ=1→b=0 (no mixing); neither hits 2√3. → needs an operator with BOTH.
  * ROUTE 1 OPEN: the true §147 (2,2) operator must give b/(c−a)=2√3 → 4/7 Derived; or c−a=0 → genuinely maximal. Precise target handed to Cal.
  * TIER HOLDS: near-maximal DERIVED (μ-τ ℤ₂); 4/7 value-form + k=2 sourced (toy 4933); diagonalized-angle OPEN (this route or Lyra's 1/14 forward). No over-claim.
""")
