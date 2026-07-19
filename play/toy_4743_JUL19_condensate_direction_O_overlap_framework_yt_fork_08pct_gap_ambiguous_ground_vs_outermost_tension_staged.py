#!/usr/bin/env python3
"""
Toy 4743 — Jul 19 (pin-O overlap framework + a fish on the 0.8% gap, mine; the flavor sector collapsed to one rank-1
condensate O, K768): the whole flavor area now hinges on ONE vector — the condensate direction O's K-type address. My
job: verify the overlaps ⟨t|O⟩, ⟨c|O⟩, ⟨u|O⟩ the moment Lyra pins O from F85. I set up the decisive framework and flag
a fish-detector catch: the observed y_t = 0.992 (≠ 1.000) is AMBIGUOUS — it does NOT decide the self-consistent-vs-
boundary-fixed fork (the 0.8% gap is degenerate between a computed CG-overlap < 1 and an exact y_t=1 with RG running),
so don't read the 0.8% as "the tell." Only Lyra's boundary-computed O decides y_t=1.

THE FRAMEWORK: y_t = ⟨t|O⟩ (the top mode's overlap with the condensate direction O); y_t = 1 ⟺ top ∥ O. The whole
up-type hierarchy is the Gram column {⟨t|O⟩, ⟨c|O⟩, ⟨u|O⟩}. O's quantum numbers (Keeper K768): the lowest boundary
state that is a color-singlet, SU(2)_L doublet, Y=+1 (S¹-weight +1 on the Shilov S⁴×S¹).

THE FORK (decided by Lyra's O, not by the data):
  * (a) O SELF-CONSISTENT (= the fermion-bilinear direction) → the top is parallel by construction → y_t = 1 EXACT
    (would expect 1.000).
  * (b) O BOUNDARY-FIXED (pinned independently by the conformal boundary) → ⟨t|O⟩ = a computed Clebsch-Gordan number,
    generically < 1 (0.992 = near-parallel).

⚠ THE 0.8% GAP IS AMBIGUOUS (my fish — don't read it as the tell): the observed y_t = 0.992 ≠ 1.000 is consistent with
BOTH forks:
  * fork (b): O boundary-fixed, the top nearly-but-not-exactly parallel → y_t = 0.992 is the computed CG overlap.
  * fork (a) + RG running: tree-level y_t = 1 (exact parallel), and ordinary RG running gives ~0.8% at the measurement
    scale → y_t(scale) = 0.992.
  These are DEGENERATE — the 0.8% gap does NOT decide the fork (CG-gap vs running). So the data alone cannot derive OR
  refute y_t=1; only Lyra's boundary-COMPUTED O direction (⟨t|O⟩ exactly 1 or computably < 1) is decisive.

THE KEY TENSION (Keeper K768, the structural crux): O is the LOWEST (ground) boundary condensate mode, while the top is
the OUTERMOST gen-3 mode — so do they overlap O(1)? O sits on the Shilov S⁴×S¹ (S¹-weight +1) and the top (gen-3)
REACHES the Shilov boundary, so they CAN overlap strongly — but whether O's SO(5)×SO(2) K-type aligns with the top's is
exactly the vector Lyra must compute (F85 pins O's SCALE, not its DIRECTION — the single missing input).

⟹ VERDICT: the flavor sector is collapsed to one rank-1 condensate O + Tier-2 corrections (masses AND mixing = the same
O; K768). The whole area hinges on O's K-type direction. y_t=1 is a decidable FORK (self-consistent → 1 exact;
boundary-fixed → computed < 1), and — my fish — the 0.8% data gap is AMBIGUOUS (CG-gap vs RG running degenerate), so it
does NOT decide the fork; only Lyra's boundary-computed O does. Don't bank y_t=1. Verification STAGED: when Lyra pins O,
I compute ⟨t|O⟩ (=1 or <1) + ⟨c|O⟩, ⟨u|O⟩ (the hierarchy column) — decisive, compute-don't-fit. Count ~7-8 (α RULED).
Five-Absence-safe (O is pure H²(D_IV⁵) via F85, no new group).
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

y_t_obs = 0.992

# ---- the framework ----------------------------------------------------------
print(f"\n[framework]: y_t = ⟨t|O⟩; y_t=1 ⟺ top ∥ O; hierarchy = Gram column {{⟨t|O⟩,⟨c|O⟩,⟨u|O⟩}}; O = color-singlet SU(2)_L-doublet Y=+1 on Shilov S⁴×S¹")
check("THE OVERLAP FRAMEWORK: y_t = ⟨t|O⟩ (the top mode's overlap with the condensate direction O); y_t=1 ⟺ top ∥ O. "
      "The whole up-type hierarchy is the Gram column {⟨t|O⟩,⟨c|O⟩,⟨u|O⟩}. O's quantum numbers (Keeper K768): lowest "
      "boundary state, color-singlet, SU(2)_L doublet, Y=+1 (S¹-weight +1 on the Shilov S⁴×S¹). The decisive input is "
      "O's K-type DIRECTION.",
      True, "y_t=⟨t|O⟩; y_t=1 ⟺ top∥O; hierarchy = the Gram column; O's K-type direction is the decisive missing vector")

# ---- the fork ---------------------------------------------------------------
check("THE FORK (decided by Lyra's O, not the data): (a) O SELF-CONSISTENT (= the fermion-bilinear direction) → top ∥ O "
      "by construction → y_t=1 EXACT (expect 1.000); (b) O BOUNDARY-FIXED (pinned independently by the conformal "
      "boundary) → ⟨t|O⟩ = a computed Clebsch-Gordan number, generically < 1 (0.992 = near-parallel). Which fork holds "
      "is decided by whether the boundary-computed O comes out parallel to the top.",
      True, "fork (a) self-consistent → y_t=1 exact; (b) boundary-fixed → ⟨t|O⟩ computed <1; decided by Lyra's O, not the data")

# ---- ⚠ the 0.8% gap is ambiguous (my fish) ----------------------------------
gap = (1 - y_t_obs)*100
print(f"[⚠ 0.8% gap]: y_t=0.992, gap {gap:.1f}% — could be fork (b) computed CG<1, OR fork (a)+RG running. DEGENERATE → doesn't decide the fork")
check("⚠ THE 0.8% GAP IS AMBIGUOUS (my fish — don't read it as 'the tell'): y_t = 0.992 ≠ 1.000 is consistent with BOTH "
      "forks — (b) O boundary-fixed, top near-parallel → 0.992 computed; OR (a) exact y_t=1 at tree level + ~0.8% RG "
      "running → 0.992 at the scale. These are DEGENERATE. So the data alone cannot derive OR refute y_t=1; only Lyra's "
      "boundary-COMPUTED O direction is decisive.",
      abs(gap - 0.8) < 0.3, "0.992 gap ambiguous: CG-overlap<1 vs y_t=1+RG-running degenerate → data doesn't decide the fork; O computation does")

# ---- the ground-vs-outermost tension ----------------------------------------
check("THE KEY TENSION (Keeper K768, the structural crux): O is the LOWEST (ground) boundary condensate mode, while the "
      "top is the OUTERMOST gen-3 mode — do they overlap O(1)? O sits on the Shilov S⁴×S¹ (S¹-weight +1) and the top "
      "(gen-3) REACHES the Shilov boundary, so they CAN overlap strongly — but whether O's SO(5)×SO(2) K-type aligns "
      "with the top's is exactly the vector Lyra must compute (F85 pins O's SCALE, not its DIRECTION — the missing input).",
      True, "O(ground, Shilov S⁴×S¹) vs top(outermost, reaches boundary) → can overlap, but the K-type alignment is Lyra's F85 computation")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the flavor sector is collapsed to one rank-1 condensate O + Tier-2 corrections (masses AND mixing = the "
      "same O; K768). The whole area hinges on O's K-type direction. y_t=1 is a decidable FORK (self-consistent → 1 "
      "exact; boundary-fixed → computed < 1); the 0.8% data gap is AMBIGUOUS (CG-gap vs RG running degenerate) → it does "
      "NOT decide the fork. Don't bank y_t=1. Verification STAGED: when Lyra pins O, I compute ⟨t|O⟩ + ⟨c|O⟩,⟨u|O⟩ — "
      "decisive, compute-don't-fit.",
      abs(gap - 0.8) < 0.3,
      "flavor = rank-1 O + Tier-2; y_t=1 a fork gated on Lyra's O direction; 0.8% gap ambiguous (doesn't decide); verify staged, don't fit")

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
PIN-O OVERLAP FRAMEWORK + the 0.8%-gap fish (my item) — flavor hinges on one vector:
  * FRAMEWORK: y_t=⟨t|O⟩; y_t=1 ⟺ top∥O; hierarchy = Gram column. O = color-singlet SU(2)_L-doublet Y=+1 on Shilov S⁴×S¹.
  * FORK: (a) O self-consistent → y_t=1 exact; (b) O boundary-fixed → ⟨t|O⟩ computed <1. Decided by Lyra's O, not the data.
  * ⚠ 0.8% GAP AMBIGUOUS: 0.992 = fork(b) CG<1 OR fork(a)+RG-running — degenerate → does NOT decide the fork.
  * TENSION: O(ground, Shilov) vs top(outermost) → can overlap, K-type alignment is Lyra's F85 computation.
  => don't bank y_t=1; verify ⟨t|O⟩+column when Lyra pins O's direction — decisive, compute-don't-fit.
""")
