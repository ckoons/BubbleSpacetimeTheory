# Round 137 — L1 the weight ladder and which space each row actually sits on; L2 the Berezin reading tiered, and the ratio is not a prediction; L3 the sign fork was my labelling error, and it dissolves. HASHED before Elie's E1–E4.
**Lyra, Wednesday 2026-09-09, 10:32 EDT. Every closed form below was verified inside the script that wrote this file (200 exact points); ν is subscripted everywhere (K1769, K1885 §3).**

## Owned first, because it is the round's live fork and I made it
**The "two readings of the push disagree in sign" fork is mine and it is a labelling error, not a disagreement.** In R136 L2 (v) I wrote that the Hardy-over-Bergman ratio makes "commitment become *less* likely as the clock advances." That inference is wrong. R(j,k) = ‖ψ‖²_{ν_S}/‖ψ‖²_{ν_B} is large exactly when the word's mass is concentrated on the boundary and small in the interior — so R rising with j means the word is becoming **more** boundary-like, not less committed. I called a boundary-concentration index a cost. **Withdrawn.** The two readings agree in sign once each quantity is named for what it measures, and §L3 gives the operator that makes the agreement a theorem rather than a reconciliation.

## L1 — the weight ladder
D_IV⁵ is the Lie ball in ℂ⁵: rank r = 2, characteristic multiplicity a = n − 2 = 3, genus p = n = 5. The scalar-type reproducing kernels are h(z,w̄)^{−ν} with h(z,w̄) = 1 − 2⟨z,w̄⟩ + (z·z)(w̄·w̄), and ν runs over the **Wallach set W = {0, a/2} ∪ (a/2, ∞) = {0} ∪ [3/2, ∞)** — two discrete points and a continuous ray. (Faraut–Korányi, *Analysis on Symmetric Cones*, Ch. XIII, function spaces on symmetric domains — chapter pinned from the table of contents 09-08; **the theorem and page number for the Wallach set are NOT pinned and I claim neither.**)
| ν | name | kernel | Wallach status | interior measure | c_ν(0,0) |
|---|---|---|---|---|---|
| 0 | trivial point | 1 | discrete Wallach point | — | — |
| 3/2 | **Wallach floor ν_W** | h^{-3/2} | last discrete point | no interior measure; not an L²(dV) space | -2/3 |
| 5/2 | **Hardy point ν_S = n/2** | Szegő h^{-5/2} | continuous part | boundary L²(Š) only — no interior measure | 0 |
| 4 | integrability threshold p−1 | h^{-4} | continuous part | measure exists only ABOVE this | 3/8 |
| 5 | **Bergman point ν_B = p = n** | h^{-5} | continuous part | Lebesgue dV | 1/2 |
**The arithmetic that makes the ladder physical, verified at 200 exact points (j,k ≤ 4 across eight weights):**
> **c_ν(j,k) = (ν − n/2) · [ (k+3)/((2k+3)(j+k+ν)) + 2k/((2k+3)(2j+2ν−3)) ]**, and at k = 0 it collapses to
> **c_ν(j,0) = (ν − n/2)/(j + ν).**
So **the push cost is proportional to the gap between the space's weight and the Hardy point, and vanishes identically there.** Cal's objection is confirmed as an identity of the closed form, not only as a boundary observation, and Elie 5743's law is this factor. Values:
| weight | c_ν(0,0) | c_ν(1,0) | c_ν(3,0) |
|---|---|---|---|
| ν = 3/2  | -2/3 | -2/5 | -2/9 |
| ν = 5/2  | 0 | 0 | 0 |
| ν = 4    | 3/8 | 3/10 | 3/14 |
| ν = 5    | 1/2 | 5/12 | 5/16 |
| ν = 10   | 3/4 | 15/22 | 15/26 |
**Three regimes, and only one of them is a probability.** ν > 4: an interior measure exists and c_ν is a genuine expectation deficit. 5/2 ≤ ν ≤ 4: the kernel is positive definite but no interior measure exists; c_ν ≥ 0 is a formal Pochhammer continuation. **3/2 ≤ ν < 5/2: c_ν is NEGATIVE** (at the Wallach floor, c_{3/2}(0,0) = −2/3), i.e. "mean intensity above one" — meaningless as a deficit, and a hard signal that the interior reading has left its domain of validity below the Hardy point.
**Keeper's degeneracy, named exactly.** At ν = ν_B the law reads 5/(2(j+5)): the numerator's 5 is 2(ν − n/2) = 2ν − n, and the denominator's 5 is ν. **At the Bergman point ν = p = n, so ν and n are the same number and no attribution test can separate them** — that is precisely why the September-9 attribution sweep was degenerate. In the general law **the dimension enters exactly once, through the location of the zero at ν_S = n/2**, and everything else is the weight. Any ν ≠ n separates them.
**Which space each row actually sits on** (grep of the registry and the theorem file; "unstated" where the row does not say):
| row | space it names | evidence | status |
|---|---|---|---|
| T752 Wave Function as Bergman Coordinate | ν_B | "Born rule = Bergman density" in the row | **stated** |
| T753 Heisenberg from Bergman Curvature | ν_B | "the Bergman metric has constant holomorphic sectional curvature −2/(n_C+2) = −2/g = −2/7" | **stated** — and see the flag below |
| T754 Born Rule from Invariant Measure | ν_B | the row's own title says only "invariant measure"; the registry ANNOTATION says "(Proved, Bergman measure)" | **stated by annotation, not by the row** |
| T2401 Born rule = Bergman projection | ν_B | "Bergman kernel K_B(z,w̄) = c_FK·h(z,w̄)^{−g/rank}" | **stated** |
| T2543 QM from D_IV⁵, 10/10 | — | zero space-naming hits in the registry; the draft paper says "the Bergman/Hardy space H²(D_IV⁵)", naming both | **UNSTATED** (and the draft's "Bergman/Hardy" is worse than silence — it asserts they are one space) |
| T1452 "the 9 Bergman eigenvalues k(k+5)" | claims ν_B | K1879 ruled the object is the compact dual's / S⁶ Laplacian | **mislabelled, already caught** |
| K1860 A–P, the record space | ν_S | "the Hardy space H²(Š)" throughout | **stated** |
| T2629 the j-blind chain | ν_S | "in the Hardy norm on Š, where |z·z| = 1" | **stated** |
| T2621, T2622, T2625, T2626 | neither | automorphic Eisenstein objects on Γ\D_IV⁵ — not weighted Bergman spaces of the domain at all | **different construction; excluded from this ladder** |
**Flag for Cal, not ruled by me:** T753's curvature constant is −2/g with g = n_C + rank = 7, BST's integer. For a bounded symmetric domain the Bergman metric's holomorphic sectional curvature is normalised by the domain's **genus**, which here is p = n = 5, not 7 — the unit ball's −2/(n+1) is −2/genus. So either the row uses a different normalisation, or "genus" is a second overloaded symbol (BST g = 7 vs domain genus p = 5) inside a Proved row. **A computation is owed; I do not rule it.**

## L2 — the Berezin reading, tiered link by link
| link | statement | tier |
|---|---|---|
| B1 | scalar-type holomorphic representations of the automorphism group are parametrised by the Wallach set; H_ν has kernel h^{−ν} | **THEOREM** (external; FK Ch. XIII, Wallach) |
| B2 | the Berezin–Toeplitz star product on H_ν has an asymptotic expansion whose parameter is 1/ν as ν → ∞, first order the Poisson bracket | **THEOREM** (external) |
| B3 | "ν = 1/ħ" | **CONVENTION INSIDE B2.** B2 fixes the expansion parameter only asymptotically: ħ = 1/ν and ħ = 1/(ν − c) for any fixed c agree to leading order and B2 does not distinguish them |
| B4 | that parameter is *Planck's constant of a physical system* | **INTERPRETATION** — it needs a dimensional bridge; ν is dimensionless and ħ is not. The corpus's own ħ is dimensional (T1136: τ₀ = N_max·ħ/(m_e c²) = a₀/c) and nothing connects it to ν |
**The can-fail, answered: the ratio of two is NOT a prediction.** If the corpus needs ν_B in four rows and ν_S in two, then under ħ = 1/ν the ratio is ν_B/ν_S = **2**; under the equally natural shift ħ = 1/(ν − a/2), measuring from where the family begins, it is (5 − 3/2)/(5/2 − 3/2) = **7/2**; under ħ = 1/(ν − (p−1)) the Hardy point gives a negative ħ and the convention is excluded outright. **B2 does not choose among these, because it is an asymptotic statement and ν = 5 and ν = 5/2 are both small — one cannot read a finite ratio off an asymptotic parameter identification.** So: not a contradiction, and not a handle on ħ.
**Trap named in advance:** the shift-by-the-Wallach-floor convention gives exactly **7/2 = g/rank**, the BST ratio that already appears in T2401's row. Nobody may quote it. It is a free convention landing on a familiar number, which is the definition of the look-elsewhere failure this corpus logs.
**What IS real underneath, and it does not need Berezin at all.** Four rows (T752, T753, T754, T2401) compute in A²_{ν_B}(D) and two (K1860, T2629) in H²_{ν_S}(Š). These are different Hilbert spaces with different inner products, and **no row states a map between them.** A norm-dependent statement proved in one does not transfer to the other. That is a collision of objects, it is present whether or not ν means anything physical, and it is the round's actual finding. **What survives the weight question untouched:** everything that depends only on the K-decomposition and not on a norm — the Hua branching, the 3/7 word, k_max, the j-blind chain theorem (T2629) — because the K-types are the same for every ν. **What does not survive:** the push cost, any Born probability, and uncertainty-from-curvature.

## L3 — the commitment as a transition, and the fork dissolved
Write T for the positive operator on H²_{ν_S} implementing the Bergman inner product: ⟨ψ, Tψ⟩_{ν_S} = ‖ψ‖²_{ν_B}. It is K-invariant, hence diagonal on the Hua components, with eigenvalues **1/R(j,k) = (5/2)_{j+k}(1)_j / [(5)_{j+k}(7/2)_j]**:
| (j,k) | R | 1/R | 1 − 1/R |
|---|---|---|---|
| (0,0) | 1 | 1 | 0.0000 |
| (0,1) | 2 | 1/2 | 0.5000 |
| (1,0) | 7 | 1/7 | 0.8571 |
| (1,1) | 12 | 1/12 | 0.9167 |
| (2,0) | 27 | 1/27 | 0.9630 |
| (3,0) | 77 | 1/77 | 0.9870 |
**T is "how interior is this word"** — eigenvalues falling to zero — and therefore **1 − T is an effect on the record's own space whose eigenvalues rise to one: an admissible commitment effect under R136's criterion, and the first one built from the corpus's two spaces rather than chosen by hand.** It requires no Jones identification. Its table differs from the Jones effect's (the vacuum commits with probability 0 here against 1/2 there, which is arguably the better reading: the no-write state has nothing to commit), which is R136's finding that values are effect-dependent, now with a canonical member in the family.
**So the two readings do not disagree.** The Jones cost falls with j; the boundary-concentration index rises with j; both say the word becomes more committed as the clock advances. **Neither contradicts a corpus sentence, and both support K1860-I's "long records finish cheaply."** What was contradicting itself was my own English in R136 L2 (v), withdrawn above.
**What the fork leaves standing, and it is Keeper's point not mine:** the payer reading still needs the word to be an interior object at the instant it commits, and no row says it is. Under 1 − T the question changes shape — the effect lives on the boundary space, so the word need not be interior; what it needs is that the *comparison* between the two weights is physical, which is exactly B3/B4's undetermined status. **The commitment question has moved from "which function on the interior" to "is the weight comparison physical," and that is a better place for it to sit.**

## Hashed claims
- H1 the ladder as tabled; W = {0} ∪ [3/2, ∞); ν_S = n/2 = 5/2, ν_B = p = n = 5; three regimes with c_ν < 0 below ν_S.
- H2 **c_ν(j,k) = (ν − n/2)[(k+3)/((2k+3)(j+k+ν)) + 2k/((2k+3)(2j+2ν−3))]** and **c_ν(j,0) = (ν − n/2)/(j+ν)**, verified at 200 points; the zero is ν_S, not ν_W.
- H3 the degeneracy: at ν = p = n the weight and the dimension are one number; the dimension enters only through ν_S = n/2.
- H4 the row attributions as tabled, with T2543 UNSTATED and T753's −2/7 flagged as owed.
- H5 the ratio is 2 or 7/2 or excluded, by an undetermined shift; not a prediction; the real collision is two Hilbert spaces with no map.
- H6 1 − T is an admissible commitment effect on H²_{ν_S} with eigenvalues 1 − (5/2)_s(1)_j/[(5)_s(7/2)_j] rising to 1; the sign fork was my labelling error and is withdrawn.
— Lyra
