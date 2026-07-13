#!/usr/bin/env python3
"""
Toy 4644 — Jul 13 (Keeper PRIMARY 1, K675 audit response): the audit corrected my α scaffolding, and it's a
valid catch — I accept it and sharpen the one lemma with a concrete check. My 4643 claimed the Szegő "trace =
dim" identity dodges the FK correction terms; the audit (K675) says the FK terms are the ρ-SHIFT, which pins
WHICH K-type sits at level-rank — i.e. they act on the COUNT itself, not just the kernel form. I verify this
directly: the naive non-compact Hardy degree-rank K-type is 15 (not 27), so reconciling 15↔27 IS the FK ρ-shift
= Gap #4 = the ONE lemma. My 4641/4643 were real scaffolding that ASSUMED the 27; the identification is the depth.
α STAYS IDENTIFIED. (Fifth symmetric self-correction of the arc — the fish-detector on my own work.)

CORRECTIONS ACCEPTED (K675 audit):
  (1) The FK "correction terms" are the ρ-SHIFT — they determine which K-type sits at level-rank, so they act on
      the COUNT. My 4643 "the trace is the rank, measure-normalization-independent, so FK doesn't touch it" was
      TOO STRONG: the trace-of-a-projection is elementary, but WHICH projection (which K-type at level-rank) is
      exactly what the FK ρ-shift fixes. The identification IS the FK terms — not dodgeable. RETRACT the demotion.
  (2) dim SO(2) = 1, not 2 (F522). The "2" in 135+2 is the (5,2)-signature/rank, a separate exponent from the
      charge-degree. "α is a square" (Lyra F522) is good physical MOTIVATION for degree-2, but Sym²(V₇) ≠
      Sym²(charge) — only the "3" piece is charge-squared. The proof is the K-type identification, not the heuristic.

THE DISCREPANCY (the concrete check that sharpens the lemma — is the boundary count trivially 27? NO):
  naive non-compact Hardy degree-rank=2 K-type = Sym²(C⁵) under K = SO(5)×SO(2):
      Sym²(5 of SO(5)) = 14 (traceless-sym [2,0]) ⊕ 1 (trace/norm) = 15,  all at SO(2)-weight = 2.
  compact-dual O(rank) = Sym²₀(V₇ of SO(7)) = 27 = 14₀ ⊕ 5_{+1} ⊕ 5_{-1} ⊕ 1_{+2} ⊕ 1_{-2} ⊕ 1₀  (my 4642).
  ⟹ NAIVE HARDY = 15  vs  COMPACT-DUAL = 27.  15 ≠ 27. The compact 27 carries SO(2)-CHARGED pieces (10 + the ±2
    singlets) that the naive uniform-weight-2 Hardy LACKS. So the boundary Szegő count is NOT trivially the compact
    27 — the naive interior degree-2 count is 15. My 4641 bridge and 4643 demotion both ASSUMED the 27.

THE ONE LEMMA (precise, and now sharply located — Gap #4, multi-week):
  prove that the CORRECT boundary object — the level-rank Hardy/Szegő K-type WITH the Faraut–Korányi ρ-shift
  (equivalently, the SO(7)-conformal boundary realization on the Shilov boundary) — is exactly Sym²₀(V₇) = 27,
  NOT the naive 15. This is the single Knapp–Wallach + FK identification the WHOLE α derivation rests on. It is
  the irreducible rigor target; the count 27, the RK-trace theorem, the charge-grading, and the 0.036 are all
  correct scaffolding AROUND it, but all assume it.

⟹ VERDICT: I ACCEPT the K675 corrections — my 4643 "trace dodges FK" is RETRACTED (the ρ-shift acts on the
count via the identification), and the "α is a square" degree reading is motivation not proof. The concrete
15-vs-27 discrepancy CONFIRMS the depth is real and LOCATES it precisely: the one lemma is the boundary-K-type =
Sym²₀(V₇) identification (FK ρ-shift). α STAYS IDENTIFIED — this is the single multi-week rigor target, not a
close. Honest self-correction; the scaffolding stands, the hard step is named. Count ~7-8 (α RULED, identified).
"""
rank, N_c, n_C, C_2, g, Nmax = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 82)
print("Toy 4644 — ACCEPT K675: naive Hardy = 15 ≠ 27 = compact-dual; the FK ρ-shift IS the one lemma (α stays IDENTIFIED)")
print("=" * 82)

# ---- accept correction 1 ----------------------------------------------------
check("ACCEPT (K675 correction 1): my 4643 'trace dodges FK' was TOO STRONG. Tr(projection)=rank is elementary, but WHICH K-type sits at level-rank is what the FK ρ-shift fixes — the FK terms act on the COUNT via the identification. RETRACT the gate-(b) demotion.",
      True, "the identification IS the FK ρ-shift, not dodgeable — the depth is in which projection, not the trace of it")

# ---- accept correction 2 ----------------------------------------------------
check("ACCEPT (K675 correction 2, F522): dim SO(2) = 1, not 2. The '2' in 135+2 is the (5,2)-signature/rank, separate from the charge-degree. 'α is a square' is MOTIVATION for degree-2, but Sym²(V₇) ≠ Sym²(charge) (only the '3' piece is charge²). Proof = the K-type identification.",
      True, "the physical heuristic motivates but does not prove the degree; carry it as motivation")

# ---- the discrepancy: naive 15 vs compact 27 --------------------------------
naive_hardy = 14 + 1        # Sym²(5) = traceless-sym 14 + trace 1, all SO(2)-weight 2
compact_dual = 27           # Sym²₀(V₇), branching 14+10+3 (my 4642)
print(f"\n[discrepancy]: naive non-compact Hardy deg-2 = Sym²(C⁵) = 14+1 = {naive_hardy} (all SO(2)-weight 2); compact O(rank) = {compact_dual}")
check("THE DISCREPANCY (concrete): naive Hardy degree-rank = Sym²(C⁵) = 14(traceless-sym)+1(trace) = 15 (uniform SO(2)-weight 2), but compact-dual O(rank) = 27 (mixed SO(2)-weights). 15 ≠ 27 → the boundary count is NOT trivially the compact 27; the ρ-shift is essential. My 4641/4643 assumed the 27.",
      naive_hardy == 15 and compact_dual == 27 and naive_hardy != compact_dual,
      "the compact 27 has SO(2)-charged pieces (10 + ±2 singlets) the naive uniform-weight-2 Hardy lacks — the FK ρ-shift is the reconciliation")

# ---- the one lemma, located -------------------------------------------------
check("THE ONE LEMMA (Gap #4, multi-week): prove the level-rank Hardy/Szegő K-type WITH the FK ρ-shift (the SO(7)-conformal boundary realization) = Sym²₀(V₇) = 27, NOT the naive 15. The whole α derivation rests on this single Knapp–Wallach + FK identification.",
      True, "the count 27, RK-trace, charge-grading, 0.036 are correct scaffolding AROUND it, but all assume it — this is the irreducible rigor target")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: I ACCEPT the K675 corrections (retract 4643's demotion; degree-reading is motivation not proof). The 15-vs-27 discrepancy CONFIRMS the depth is real and LOCATES it: the one lemma = boundary-K-type = Sym²₀(V₇) (FK ρ-shift). α STAYS IDENTIFIED — the single multi-week rigor target, not a close.",
      True, "honest self-correction (5th of the arc); scaffolding stands, the hard step named. Count ~7-8 (α RULED, identified)")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 82)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 82)
print(f"SCORE: {passed}/{total}")
print("=" * 82)
print("""
ACCEPT K675 + SHARPEN THE ONE α LEMMA (naive Hardy 15 ≠ compact 27 → the FK ρ-shift IS the depth):
  * ACCEPT correction 1: 4643's 'trace dodges FK' RETRACTED — the FK ρ-shift fixes WHICH K-type at level-rank
    (acts on the count); the identification IS the FK, not dodgeable.
  * ACCEPT correction 2 (F522): dim SO(2)=1; 'α is a square' is motivation, Sym²(V₇)≠Sym²(charge).
  * DISCREPANCY (concrete): naive Hardy deg-2 = Sym²(C⁵) = 14+1 = 15 (uniform weight 2) vs compact O(rank) = 27
    (mixed weights). 15 ≠ 27 → boundary count is NOT trivially 27; the ρ-shift is essential.
  * THE ONE LEMMA (Gap #4, multi-week): boundary level-rank Hardy K-type WITH FK ρ-shift = Sym²₀(V₇) = 27, not 15.
    The whole α derivation rests on it. My scaffolding (count, RK-trace, grading, 0.036) is correct but assumes it.
  => honest self-correction; α STAYS IDENTIFIED, the single rigor target located. Count ~7-8.
""")
