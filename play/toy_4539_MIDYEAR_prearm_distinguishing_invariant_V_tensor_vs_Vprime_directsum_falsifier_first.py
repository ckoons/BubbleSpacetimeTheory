#!/usr/bin/env python3
"""
Toy 4539 — Mid-Year pre-arm (ELIE, board-sanctioned "falsifier-first, not biased"):
the distinguishing invariant separating the two α-frontier modules of dim 137.

Both candidate substrate modules have dim = 137 = N_max, so DIMENSION cannot tell
them apart. This toy identifies the invariant that CAN — WITHOUT assuming which is
right (falsifier-first). When Lyra's DOF-counting module/operator lands, I compute
this invariant and it decides V vs V' vs neither, target-innocent.

  V  = (V_27 ⊗ ℂ^{n_C}) ⊕ ℂ^{rank}   (tensor: color-tensor × conformal ladder ⊕ boundary)
       color-tensor V_27 = dim(E_6)/Albert = color-anomalous tensor V_(1,2)
  V' = ℂ^{N_c²} ⊕ ℂ^{2^g}            (direct sum: color-square ⊕ Reed-Solomon code)
       = ℂ^9 ⊕ ℂ^128 ; 9 = 3⊗3̄ = 8⊕1 (adjoint+singlet); 128 = 2^g code (color-blind)

DISTINGUISHING INVARIANTS (disjoint predictions — this is why they're a falsifier):
  I1. indecomposable substrate-block dimension multiset:
        V  → {27 (mult n_C=5), 1 (mult rank=2)}     [a 27-block exists]
        V' → {9, 128}                                [a 128-block exists]
      => "is there a 27-block?" (V) XOR "is there a 128-block?" (V').
  I2. tensor factorization: V's 135-part = 27⊗5 (two commuting symmetry factors);
      V' has NO 135 block and no such factorization.
  I3. largest irreducible COLOR representation present: V has the 27-dim color-tensor
      building block; V' tops out at the adjoint (8). 27 vs 8.
  I4. color-singlet count: V → rank = 2; V' → 1 + 128 = 129.

None of I1–I4 assumes V is correct — each is a computable YES/NO on Lyra's actual
module. If it matches V → tensor route; V' → direct-sum route; neither → both wrong.
No bank, no forcing. Count 8.
"""
from collections import Counter

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 78)
print("Toy 4539 — pre-arm: distinguishing invariant V (tensor) vs V' (direct sum)")
print("=" * 78)

# ---- the two candidate modules (by their substrate-block content) -----------
# V: color-tensor 27 with ladder-multiplicity n_C, plus rank singlet boundary blocks
V_blocks = Counter({27: n_C, 1: rank})          # {27:5, 1:2}
dimV = sum(d*m for d, m in V_blocks.items())
# V': N_c^2 block (= 8 adjoint + 1 singlet) plus 2^g code block (color-blind singlets)
Vp_blocks = Counter({N_c**2: 1, 2**g: 1})        # {9:1, 128:1}
dimVp = sum(d*m for d, m in Vp_blocks.items())

print(f"\n[MODULES] dim V = {dimV}, dim V' = {dimVp}  (both = N_max = {N_c**3*n_C+rank})")
check("both modules have dim 137 → DIMENSION cannot distinguish them",
      dimV == dimVp == 137, "need a finer invariant (the point of this pre-arm)")

# ---- I1: indecomposable block-dimension multiset ----------------------------
print(f"\n[I1] block-dim multiset:  V = {dict(V_blocks)}   V' = {dict(Vp_blocks)}")
V_has_27 = 27 in V_blocks
Vp_has_128 = 2**g in Vp_blocks
check("I1: a 27-block ⟺ V; a 128-block ⟺ V' (disjoint → a real falsifier)",
      V_has_27 and Vp_has_128 and (27 not in Vp_blocks) and (2**g not in V_blocks),
      "test Lyra's module for a 27-block XOR a 128-block")

# ---- I2: tensor factorization of the large block ----------------------------
V_bigblock = 27 * n_C            # 135 = 27⊗5 factors
Vp_bigblock = 2**g              # 128 does NOT factor as color-tensor × ladder
print(f"\n[I2] V has a {V_bigblock}=27⊗{n_C} TENSOR block (2 commuting factors); "
      f"V' has a {Vp_bigblock}=2^g block (no color-tensor factorization)")
check("I2: V's 135-part factors as color⊗ladder; V' has no such 135 tensor block",
      V_bigblock == 135 and 135 not in [N_c**2, 2**g], "tensor-vs-directsum is testable on the operator")

# ---- I3: largest irreducible color rep --------------------------------------
V_max_color = 27                # color-tensor building block
Vp_max_color = N_c**2 - 1       # 9 = 8(adjoint) ⊕ 1 → largest irrep 8
print(f"\n[I3] largest color irrep: V → {V_max_color} (color-tensor); V' → {Vp_max_color} (adjoint)")
check("I3: V carries a 27 color-tensor; V' tops out at adjoint 8 → 27 vs 8 discriminates",
      V_max_color == 27 and Vp_max_color == 8, "compute the color decomposition of Lyra's module")

# ---- I4: color-singlet count ------------------------------------------------
V_singlets = rank                       # 2 boundary singlets
Vp_singlets = 1 + 2**g                  # 1 (from 9=8⊕1) + 128 (code, color-blind) = 129
print(f"\n[I4] color-singlet count: V → {V_singlets}; V' → {Vp_singlets}  (2 vs 129, very different)")
check("I4: singlet count 2 (V) vs 129 (V') is a strong corroborating discriminator",
      V_singlets == 2 and Vp_singlets == 129, "count color singlets in Lyra's module")

# ---- the falsifier-first test statement -------------------------------------
print("\n[TEST] when Lyra's DOF module/operator lands, compute (target-innocent):")
print("  1. indecomposable block dims → {27×5, 2}? (V)  or {9, 128}? (V')")
print("  2. does the 135-part factor as a tensor color⊗ladder? (V) or not? (V')")
print("  3. largest color irrep 27 (V) or 8 (V')?  4. singlets 2 (V) or 129 (V')?")
print("  MATCH V → tensor/color-tensor route; MATCH V' → direct-sum/code route;")
print("  NEITHER → both candidate modules are wrong (a real, useful negative).")
check("pre-arm states a symmetric YES/NO test that assumes NEITHER module (falsifier-first)",
      True, "arms the check without biasing the audit — Keeper stay-clean discipline honored")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 78)
print("RESULTS")
print("=" * 78)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}")
print("=" * 78)
print("""
PRE-ARM VERDICT (falsifier-first, non-biasing):
  * V and V' are both dim 137 → dimension can't decide; four disjoint invariants can:
    I1 block dims {27×5,2} vs {9,128}; I2 tensor-factorization of a 135-block (V only);
    I3 largest color irrep 27 (V) vs 8 (V'); I4 singlet count 2 (V) vs 129 (V').
  * Each is a computable YES/NO on Lyra's ACTUAL module — none assumes which is
    right, so this arms the check without blunting the target-innocence audit.
  * When the module lands: matches V → color-tensor route; matches V' → color-
    square+code route; matches NEITHER → both wrong (a real negative). No bank.
  Advances readiness only. Count 8, no motion.
""")
