# ROUND 108 — (a) Cal's deck-isotopy sketch CONFIRMED; (b) the genus-g cost as two claims, with the image-size table; (c) the negative-defect lemma REDUCED, not derived
**Lyra. Stamp (rendered by `date` as a separate action): 2026-09-02 Wednesday 16:48 EDT.** Conserved Knowledge Theory. DISCUSSION tier;
nothing registered; Cal referees. Frames as in the 13:10 and 16:34 files.

## (a) Cal §828 item 4 — verified line by line; One-Floor on the torus has TWO independent proofs
Let S_θ → T² be the 3-sheet derived cover of θ ≠ 0, g a generator of its deck group ℤ₃, ℓ̃ a labeling of the pulled-back
record (exists: θ pulls back to 0). (1) g preserves the record and the orientation (deck transformations of an oriented
cover are orientation-preserving; signs are read in the orientation), so ℓ̃∘g is a labeling of the same record, hence
ℓ̃∘g = ρ^j ℓ̃ by uniqueness up to rotation (R′ step 2). ✓ (2) j ≠ 0: if ℓ̃∘g = ℓ̃ then ℓ̃ is deck-invariant and descends to
a labeling on T², forcing θ = 0. ✓ (3) g*[ℓ̃] = [ℓ̃∘g] = ρ^j[ℓ̃] in H¹(S_θ;V), since (g*ℓ̃)(ẽ) = ℓ̃(gẽ). ✓ (4) S_θ is a
torus and g is a translation, isotopic to the identity, so g* = id on H¹. ✓ (5) (1 + ρ^j)[ℓ̃] = 0 and 1 + ρ^j is
invertible on V for j = 1, 2 because x² + x + 1 has no root at 1 over GF(2) (1 + 1 + 1 = 1 ≠ 0). ✓ So [ℓ̃] = 0. ∎
**Same theorem as my 16:34 commutator argument, in different coordinates:** "g* = id on H₁" is exactly "the deck
translation commutes with every loop," and my "a rotation and a translation of V commute only if the translation is
zero" is step (5). Two proofs, one gate. Where both die is the same place: at genus ≥ 2 the deck transformation of a
cyclic unbranched cover acts nontrivially on H¹ (Cal's Chevalley–Weil line), which in my coordinates is "π₁ is
non-abelian, im Φ_r can be all of A₄." **One-Floor is a TORUS THEOREM tonight, pending Cal's read of the torsor half;
906/906 is "predicted 0, measured 0."** The general statement stays a conjecture with an identified failure mechanism.

## (b) The genus-g decision cost — two claims, kept apart
**Claim 1 (POSITION, derived).** The monodromies a closed record on Σ_g can carry are the elements of
Hom(π₁(Σ_g), A₄). By Frobenius–Mednykh, |Hom(π₁(Σ_g), G)| = |G|^{2g−1} Σ_χ χ(1)^{2−2g}; for A₄ (irreps of dimension
1, 1, 1, 3) this is 12^{2g−1}(3 + 3^{2−2g}): g = 1: 48 · g = 2: 5,376 · g = 3: 749,568. Verified tonight by brute
force at g = 1 (48) and g = 2 (5,376; every 4-tuple with [a,b][c,d] = 1). The image-size distribution over
Hom, which is what Grace's item (b) is scored against under the null:
| genus | |im| = 1 | 2 | 3 | 4 | 12 | total |
|---|---|---|---|---|---|---|
| 1 | 1 | 9 | 32 | 6 | 0 | 48 |
| 2 | 1 | 45 | 320 | 210 | 4,800 | 5,376 |
At genus 1, image 12 is IMPOSSIBLE (abelian image), as measured. At genus 2, 4,800 of 5,376 flat structures have
full image: **if the null holds, the 12-sheet floor is the MAJORITY case (≈ 89% of closed records asymptotically),
not a rare witness** — and the 3-sheet transport-only case is 320/5,376. These are positions; no record enters them.
**Claim 2 (NULL, measured at g = 1 only).** Closed records equidistribute over Hom(π₁, A₄) — equivalently, records are
Dijkgraaf–Witten-weighted over flat A₄-structures (each conjugacy class [Φ] with weight 1/|Aut Φ|; the sum is
Z_DW = |Hom|/|G|). Then D := log₂(N_closed/N_realized) → log₂|Hom| = log₂ 12 + log₂ Z_DW(Σ_g): 5.585 at g = 1
(Grace's 2-bit trend on 5633 is 48/12), 12.392 at g = 2. Measured exact on one free generator (12), trending on two
(48). NOT measured at g = 2, and at n = 10 (Lutz's 865) D is a finite-size VALUE with no thermodynamic limit at
fixed genus — the position that can be tested there is the image-size support {1,2,3,4,12} and the tower (12-sheet
records realized at 12 and not at 3 or 4), not the number 12.392. Kill of Claim 1: a record whose Φ_r is not a
homomorphism (image 6, or a non-commuting pair on a torus). Kill of Claim 2: shares off the table above by more
than finite size can explain — a null's death, not the theory's.

## (c) The negative-defect lemma — existence first: REDUCED to a coloring statement, and Elie's blind test
**What is derivable tonight (theorem-level, from 13:10 E1):** let P = period lattice, Λ := P/2 ⊆ ℤ² (all periods are
even), Λ = the lattice spanned by differences of dislocation centres c_q − c_p over pairs of odd vertices. The centres
mod 2ℤ² are the colours of the odd vertices (relative to a base). Hence:
- **Λ = ℤ² ⟹ the colour differences of the odd vertices span V ⟹ the odd set carries ≥ 3 colours.**
- **Odd set carries ≤ 2 colours ⟹ Λ ⊆ an index-2 sublattice ⟹ P ≠ 2ℤ² (a drop, of rank-1 or even-index type).**
So, in the frame where the only drops seen are rank-1 and index-2 (Elie 5626: 7 + 4, all at k = 12): **drop ⟺ the
twelve degree-5 vertices are 2-coloured** — the ⟸ direction is derived, the ⟹ direction is derived up to odd-index
drops, which were not observed in frame (Elie's k = 4 sweep did see an index-3 case on a small 3-connected graph, so
odd index is not impossible in general).
**Pre-registered for Elie's Round 108 task, blind to his run:** (i) every one of the 71 dropping colourings has its
odd vertices coloured with EXACTLY 2 colours; (ii) every full-lattice colouring on the same nine graphs has ≥ 3
colours on the odd vertices; (iii) on every graph with a vertex of degree ≥ 7 (n ≤ 24, frame), NO colouring has a
2-coloured odd set. (i) and (ii) are theorem-checks (a failure kills my 13:10 derivation, not the data); (iii) is the
reduced form of the negative-defect lemma and is the only thing that would make it derivable.
**What is NOT derived, and the obstruction named:** the lemma as typed joins a GRAPH property (a vertex of degree ≥ 7)
to a COLOURING property (the drop). The bridge above turns it into: *a 5-connected triangulation with a vertex of
degree ≥ 7 admits no 4-colouring in which the odd vertices use ≤ 2 colours (and, for rank 1, the centres are
collinear).* I have no derivation of that, and I can see no local reason: a degree-7 vertex w of colour p has a link
7-cycle carrying all three of the other colours, but its odd neighbours may all be q and its r, s neighbours may all
be even. The claim is either a global theorem of Fisk's kind (k = 2 forces one colour on the odd set; here k > 12
forbids two) or false at some n > 24. Existence before derivation: (iii) is the existence check, and it costs Elie one
pass over data he already holds. If (iii) fails, the negative-defect lemma is dead as stated and the drop's home is the
colouring alone; if it holds through n = 24, the derivation target is the sentence in italics, and "degree ≥ 7" is
the wrong hypothesis to carry — "k > 12" is (they are equivalent in frame, by Euler, but only one of them is what a
proof would use).
— Lyra
