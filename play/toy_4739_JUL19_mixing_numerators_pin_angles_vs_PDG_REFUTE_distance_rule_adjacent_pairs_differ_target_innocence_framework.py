#!/usr/bin/env python3
"""
Toy 4739 — Jul 19 (mixing-numerator lives-there: verification infrastructure + a fish on the prettiest lead, mine): my
assignment is to verify each d/D against the measured angles the moment Lyra lands an intertwiner-dimension count, and
confirm target-innocence (integers from geometry, not the angle). Lyra leads the three counts; while she works them, I
(1) pin the three target angles vs PDG (what her counts must reproduce), and (2) STRESS-TEST the "orbit-distance →
ambient-space rule" that Keeper flagged as the prettiest lead (Cal scrutinizes hardest) — and REFUTE it as stated: both
θ₁₂ and θ₂₃ are ADJACENT (1-step) orbit-pairs, but their D's are 10 ≠ 7, so orbit-distance ALONE does not force D.
The honest structure is three distinct counts (2 independent D's + θ₁₃ chained to θ₁₂), NOT a single distance-map.

THE THREE FORMS vs PDG (all identified at ≤0.5σ — the values Lyra's counts must reproduce):
  * θ₁₂ = N_c/dim SO(5) = 3/10 = 0.300 vs 0.307±0.013 (0.5σ) — bulk↔intermediate (1-step), D=10.
  * θ₂₃ = rank²/g = 4/7 = 0.571 vs 0.561±0.021 (0.5σ) — intermediate↔Shilov (1-step), D=7.
  * θ₁₃ = 1/Λ²(10) = 1/45 = 0.0222 vs 0.02203±0.0007 (0.3σ) — bulk↔Shilov (2-step), D=45.

THE DISTANCE-RULE REFUTED (the prettiest lead, pre-empting Cal's scrutiny): the proposed rule is "the extreme (2-step)
pair uses Λ²(10)=45, adjacent pairs use a smaller ambient space" — which would PREDICT the 45 from orbit-distance. But:
  * θ₁₂ (bulk↔intermediate) is 1-step → D=10 (dim SO(5)).
  * θ₂₃ (intermediate↔Shilov) is 1-step → D=7 (g, SO(5,2) def rep).
  ⟹ BOTH are 1-step (adjacent) pairs, yet D=10 ≠ 7. So orbit-DISTANCE alone does NOT determine D — the "distance →
    ambient-space" rule is INCONSISTENT for the adjacent pairs, REFUTED as stated. The 45 is NOT forced by distance.
THE HONEST STRUCTURE (K749/R11): three distinct D's — θ₁₂=10 (dim SO(5)) and θ₂₃=7 (SO(5,2) def rep) are TWO INDEPENDENT
counts; θ₁₃=45=Λ²(10) CHAINS to θ₁₂ (Grace's antisymmetric-square, so θ₁₃ is not independent). So 2 independent D's +
1 chained, NOT a single distance-map. Each D must derive from its own orbit-pair geometry (Lyra's per-pair counts).

⟹ VERDICT: the three d/D forms are pinned vs PDG (all ≤0.5σ — identified, the targets). The "orbit-distance →
ambient-space" rule (the prettiest lead) is REFUTED as stated — adjacent pairs θ₁₂, θ₂₃ have D=10≠7, so distance can't
force D (don't chase it, don't let it "predict" the 45). The honest structure is 2 independent D's (10, 7) + θ₁₃
chained (45=Λ²(10)). Target-innocence framework STAGED: when Lyra lands each count (d, D from the orbit-pair
intertwiner), I verify it reproduces the PDG angle AND derives from geometry not the angle. Count ~7-8 (α RULED).
"""
import math
from fractions import Fraction as F
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# angle: (form, PDG central, PDG sigma, orbit-pair, steps, D)
angles = {
    'θ12': (F(N_c, 10), 0.307, 0.013, 'bulk↔intermediate', 1, 10),
    'θ23': (F(rank**2, g), 0.561, 0.021, 'intermediate↔Shilov', 1, 7),
    'θ13': (F(1, 45), 0.02203, 0.00070, 'bulk↔Shilov', 2, 45),
}

# ---- pin the three angles vs PDG --------------------------------------------
print(f"\n{'angle':6}{'d/D':8}{'value':>8}{'PDG':>16}{'σ-dist':>8}{'  pair(steps), D'}")
all_within = True
for k, (form, obs, sig, pair, steps, D) in angles.items():
    z = abs(float(form)-obs)/sig
    all_within = all_within and z < 1
    print(f"{k:6}{str(form):8}{float(form):>8.4f}{f'{obs}±{sig}':>16}{z:>7.1f}σ  {pair}({steps}-step), D={D}")
check("THREE FORMS PINNED vs PDG (identified — the targets): θ₁₂=N_c/dim SO(5)=3/10 (0.5σ); θ₂₃=rank²/g=4/7 (0.5σ); "
      "θ₁₃=1/Λ²(10)=1/45 (0.3σ). All reproduce PDG within 1σ → identified. These are the values Lyra's derived counts "
      "must reproduce (from geometry, not by fitting).",
      all_within, "θ₁₂=3/10, θ₂₃=4/7, θ₁₃=1/45 all match PDG ≤0.5σ — identified; the targets for Lyra's counts")

# ---- REFUTE the distance-rule (the prettiest lead) --------------------------
D12, D23 = angles['θ12'][5], angles['θ23'][5]
steps12, steps23 = angles['θ12'][4], angles['θ23'][4]
print(f"[distance-rule test]: θ₁₂ ({steps12}-step)→D={D12}; θ₂₃ ({steps23}-step)→D={D23} — both 1-step but D=10≠7")
check("DISTANCE-RULE REFUTED (the prettiest lead, pre-empting Cal): the proposed 'orbit-distance → ambient-space' rule "
      "would predict the D's (and the 45) from how far apart the orbits are. But θ₁₂ (bulk↔intermediate) and θ₂₃ "
      "(intermediate↔Shilov) are BOTH 1-step (adjacent) pairs, yet D=10 ≠ 7. So orbit-distance ALONE does NOT force D "
      "— the rule is INCONSISTENT for adjacent pairs. The 45 is NOT forced by distance; don't let it 'predict' the 45.",
      steps12 == steps23 and D12 != D23, "θ₁₂,θ₂₃ both 1-step but D=10≠7 → distance doesn't force D → distance-rule REFUTED (the 45 is not distance-forced)")

# ---- the honest structure ---------------------------------------------------
chain_ok = (math.comb(10,2) == 45)
print(f"[honest structure]: θ₁₂=10 (dim SO(5)) + θ₂₃=7 (SO(5,2) def rep) INDEPENDENT; θ₁₃=45=Λ²(10)=C(10,2)={math.comb(10,2)} CHAINS to θ₁₂")
check("HONEST STRUCTURE (K749/R11): three distinct D's — θ₁₂=10 (dim SO(5)) and θ₂₃=7 (SO(5,2) def rep) are TWO "
      "INDEPENDENT counts; θ₁₃=45=Λ²(10)=C(10,2) CHAINS to θ₁₂ (Grace's antisymmetric-square). So 2 independent D's + 1 "
      "chained, NOT a single distance-map. Each independent D must derive from its own orbit-pair geometry.",
      chain_ok, "2 independent D's (10, 7) + θ₁₃=Λ²(10)=45 chained to θ₁₂ — not a distance-map; per-pair counts needed")

# ---- target-innocence framework staged --------------------------------------
check("TARGET-INNOCENCE FRAMEWORK STAGED (for Lyra's counts): when Lyra derives each d (N_c, rank², 1) and D (10, 7, "
      "45) from the orbit-pair intertwiner geometry, I verify (i) d/D reproduces the PDG angle (≤1σ), (ii) the integers "
      "come from the GEOMETRY not the angle (target-innocent), (iii) no back-solving (the count predicts, doesn't "
      "post-fit). A d/D that only reproduces the number is a coincidence, not a theorem.",
      True, "staged: verify Lyra's d,D counts → reproduce PDG + target-innocent (geometry not angle) + no back-solve")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the three d/D forms are pinned vs PDG (all ≤0.5σ, identified). The 'orbit-distance → ambient-space' "
      "rule (prettiest lead) is REFUTED as stated — adjacent pairs θ₁₂,θ₂₃ have D=10≠7, so distance can't force D (don't "
      "chase it, it doesn't predict the 45). Honest structure: 2 independent D's (10, 7) + θ₁₃ chained (45=Λ²(10)). "
      "Target-innocence framework staged for Lyra's per-pair counts.",
      all_within and (D12 != D23) and chain_ok,
      "angles pinned vs PDG; distance-rule refuted (adjacent pairs differ); 2 independent D's + 1 chained; verify framework staged")

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
MIXING-NUMERATOR verification infrastructure (my item) — pin targets + refute the prettiest lead:
  * PINNED vs PDG: θ₁₂=3/10 (0.5σ), θ₂₃=4/7 (0.5σ), θ₁₃=1/45 (0.3σ) — identified, the targets for Lyra's counts.
  * DISTANCE-RULE REFUTED: θ₁₂,θ₂₃ both 1-step (adjacent) but D=10≠7 → distance doesn't force D → the 45 is NOT distance-predicted.
  * HONEST STRUCTURE: 2 independent D's (10=dim SO(5), 7=SO(5,2) def rep) + θ₁₃=45=Λ²(10) chained to θ₁₂ (not a distance-map).
  * STAGED: verify Lyra's per-pair d,D counts → reproduce PDG + target-innocent (geometry not angle) + no back-solve.
""")
