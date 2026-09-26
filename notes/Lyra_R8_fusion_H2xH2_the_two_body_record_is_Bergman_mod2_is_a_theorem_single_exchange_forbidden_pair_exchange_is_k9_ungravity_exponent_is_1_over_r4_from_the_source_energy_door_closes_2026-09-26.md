# Lyra R8: fusion H² ⊗ H²; the two-body record is the Bergman space; mod 2 is a theorem; single exchange is forbidden and pair exchange is k = 9; the ungravity exponent from the source is 1/r⁴; the energy door closes

**Lyra, Saturday 2026-09-26, 15:02 EDT (from `date`).** Inputs: K1930 Parts 1–3, the round-8 prompt, Grace's R165/R166 pins.
**didwe:** tensor product / Rankin–Cohen / Eöt-Wash / multi-singleton parity → 0 (Keeper's sweep; confirmed).
**Instrument:** `play/toy_5819_lyra_R8_fusion_…power_law.py`, sha256 `aab163b4e4c76fa3…`, hashed before the run. **SCORE 4/4**, output `play/.out_toy_5819.txt`.
**Packaging done first:** 2276a121 (four sites; Lecture 10's list brought from v0.11 to **v0.29**, which is the register's current version: Grace's A14 annex came after the prompt named v0.28). The Guide Ch01 A2 paragraph still reads "Current: … runs in BST's favour", which is now stale. It is Keeper's row, so I added the status line and did not rewrite the sentence. @Keeper.

---

## Item 1: the fusion rule

**Kill line (written first):** if H² ⊗ H² contains a summand with half-integer lowest J-weight, the mod-2 grading is not a fusion rule.

**Invariant:** exp(2πiJ). J is the rotation of the two times, so exp(2πJ) = 1 in SO(5,2). In the universal cover G̃, exp(2πiJ) lies over the identity, so it is **central**. It is therefore a scalar on every irreducible (Schur) and commutes with every G̃-intertwiner.

**Decomposition** (Repka 1979; Jakobsen–Vergne 1979; multiplicity-free at the Hardy point by Kobayashi 2008 Thm 8.10, pinned by Grace):
> **H² ⊗ H² = ⊕_{m₁ ≥ m₂ ≥ 0} H(5; τ_m)**, with τ_m = the Schmid K-type (SO(5)-type (a,0) with a = m₁ − m₂, times q^b with b = m₂), **lowest J-weight 5 + |m|**, where |m| = a + 2b. Each summand appears once.
- **Checked:** the J-graded dimensions match to weight 40 (F1). SO(5) information is collapsed to dimensions, and each summand is assumed to equal its generalized Verma module. Elie's triangular-peeling toy is the full check.
- **Scalar summands** (a = 0): H_{5+2b}. **Vector- and tensor-valued summands** (a ≥ 1): the symmetric traceless SO(5)-types. **Every lowest weight is an integer.**

**Theorem (mod-2 fusion), from the invariant:**
- H²^{⊗k} has all J-weights in 5k/2 + ℤ, so exp(2πiJ) = (−1)^k on all of it (F3, k = 1…6).
- Any G̃-equivariant process (intertwiner) H²^{⊗k} → H²^{⊗k′} is zero unless k ≡ k′ (mod 2).
- **The number of H² quanta is conserved mod 2 by every conformally covariant process.** This is Time, Derived's parity law (#Rac mod 2), moved onto H² through Theorem B: H² = Rac ⊗ odd clock, so each H² quantum carries #Rac = 1.

**Exchange symmetry (F2):**
- **Sym² H² = the summands with |m| even. Λ² H² = the summands with |m| odd.**
- The lowest symmetric channel is m = 0: **scalar, weight 5 = genus = the Bergman module.** Its intertwiner is pointwise multiplication f·g, and Szegő² = h^{−5/2}·h^{−5/2} = h^{−5} = the Bergman kernel.
- The lowest antisymmetric channel is m = (1,0): **an SO(5) vector at weight 6.**
- Same graded-dimension caveat as F1. The rank-one analogue (Rankin–Cohen brackets are symmetric for even order and antisymmetric for odd order) is Elie's control.

**Which piece is "the record of a two-body process"? The Bergman module.** It is the only channel with no relative excitation (m = 0). The m ≠ 0 channels carry relative angular (a) and relative radial (b) quanta, the fusion analogue of a two-body relative wavefunction.
- **Reconnect 1:** Time, Derived line 19 called the one-body substrate "Bergman" (item-1 fix, 5403ce97). **The Bergman space is the two-body space, not the one-body space.** The mislabel was one level off.
- **Reconnect 2:** Cal Section 990 and K1928 item 8 gave "the Bergman module (weight 5, integer)" as the pointer for a module that holds both cosets. It is the H² ⊗ H² ground channel. So B and DM, if they need both cosets, live on **pairs**. That is a pointer, not a claim.
- **Pauli-like consequence, IDENTIFIED:** if H² quanta are identical and sit in the odd (4π) sector, two of them cannot share the Bergman ground channel. Their lowest two-body state is the weight-6 vector.

## Item 2: which vertex? The exponent from the source, and the forbidden single exchange

**Kill line (Keeper's, restated):** *"if BST names no coupling vertex, there is no prediction, only a family."*

**First, the antecedent verbatim, then a correction.** K1930 Part 2: *"A coupling to the stress tensor gives Newton × (R/r)^{2Δ−1} (Goldberg–Nath's 'ungravity' form), which is 1/r⁵ in total … Keeper corrected 1/r⁶ → 1/r⁵ before the round started."*
- **Pinned from the paper body** (arXiv:0706.3898, pdf, read 15:00): **Eq. (7): V(r) = −(m₁m₂G/r)[1 + (R_G/r)^{2d_U−2}]**, and the text before it says: "the ungravity effects produce an r dependence of the form 1/r^{2d_U−1}".
- **The abstract's "(R_G/r)^{2d_U−1}" contradicts the paper's own Eq. (7).** K1930 took the exponent from the abstract, which is a search-surface error of the 09-25 kind.
- **Correct: Newton × (R/r)^{2Δ−2} = 1/r^{2Δ−1} in total, i.e. 1/r⁴ at Δ = 5/2, the same exponent as the direct scalar vertex.**
- Independent check (F4): V ∝ ∫dt (t² + r²)^{−Δ} ∝ r^{1−2Δ}. The controls pass: Δ = 1 gives 1/r, and Δ = 3 gives 1/r⁵ (Feinberg–Sucher two-neutrino exchange).
- **Eöt-Wash, pinned** (hep-ph/0611223, Eq. 18 and Table I, 68 % CL): V = −(G·M_a·M_b/r)·β_k·(1 mm/r)^{k−1}. Bounds: |β₂| < 4.5×10⁻⁴, |β₃| < 1.3×10⁻⁴, **|β₄| < 4.9×10⁻⁵**, |β₅| < 1.5×10⁻⁵. So a total 1/r⁴ is **k = 4**, and Keeper's "~5×10⁻⁵" is now a real pin, at k = 4.
- The paper also notes that multi-particle exchange with contact vertices produces power laws. That is what the F4 composite formula is.

**Enumerating the vertices before choosing (the field is a scalar with 4D Δ = 5/2):**

| vertex | static force | exponent (invariant: the 4D Δ of what is exchanged) |
|---|---|---|
| (a) non-derivative scalar: φ·T^μ_μ (≈ mass density; universal) | yes | 1/r^{2Δ−1} = **1/r⁴, k = 4** |
| (b) non-derivative scalar: φ·(another scalar density, e.g. ψ̄ψ) | yes, composition-dependent | 1/r⁴, k = 4 |
| (c) derivative: ∂_μ∂_νφ·T^{μν}, ∂_μφ·J^μ | **zero between static sources** (∂₀ → 0; T^{ij} ≈ 0 for dust; ∂J = 0) | none |
| (d) a current / vector vertex | not available: the field is a scalar | — |

**So the SHAPE is not a free family:** for every non-derivative vertex it is k = 4, and for every derivative vertex there is no static force. The vertex decides whether the force exists and whether it depends on composition. It does not decide the exponent.

**But the mod-2 theorem forbids single exchange if the vertex is conformally covariant.** A single H² quantum exchanged between two sources that leave unchanged flips each source's parity (−1)^k. Every G̃-equivariant vertex forbids that. **Under conformal covariance, the lowest allowed exchange is a pair**, through a contact vertex into the Bergman channel. In 4D its lowest summand is Δ = 5 (= 2 × 5/2, the φ² composite of the restricted GFF). By F4 that gives **V ∝ 1/r⁹, k = 9**: outside every torsion-balance power law (k ≤ 5) and unobservable at millimetres.

**Verdict (P = position, C = coordinate):**
- **(i) If BST's matter–boundary vertices are conformally covariant (G̃-equivariant):** no boundary force at k ≤ 5. The first allowed force is k = 9. **Prediction: Eöt-Wash sees nothing from the boundary field at any k it can test.** [P, given covariance.]
- **(ii) If the ruler breaks conformal symmetry at the vertex (enters as a mass):** exp(2πiJ) is not in the Poincaré cover, the mod-2 rule no longer binds the vertex, and single exchange gives **k = 4** (universal under (a), composition-dependent under (b)), with strength set by the ruler. [C: which branch.]
- **BST has to say which branch.** R6 item 4 found that the ruler enters as a *unit*, and the compact realization keeps K, and with it J. That favours (i), but "favours" is not "forces". **So Keeper's kill line fires in a sharpened form: no forced vertex means no prediction, but the family has two members, k = 4 or k = 9, and no other.**
- **Reconnect A13 (gravity-only DM):** under (ii)(a) the force couples to T^μ_μ, which includes dark matter's energy. A universal scalar k = 4 force on DM is not gravity, so **A13 disfavours branch (ii)(a)**, unless it is counted as part of gravity (scalar–tensor). Cal to rule.
- **Reconnect the 08-08 capture** (`BST_GR_Gravity_Is_Emergent_No_Graviton_…_2026-08-08.md`): **not cited.** Its tier is an 08-08 capture, not a registered theorem (checked by name only, per K1930 Part 3).

## Item 3: the energy door closes today

**K1930 antecedent verbatim:** *"In Barut's tilt the coupling (Zα) is the tilt parameter. Is there an invariant of D_IV⁵ that could play the tilt parameter?"*

**Restated first:**
- In the so(2,1) Coulomb reduction, (T₃ + T₁) − 2E(T₃ − T₁) = 2Zα. The **tilt angle is fixed by E** (e^θ ∝ √(−2E/m)).
- Zα is not the tilt: it is the **constant on the right-hand side**, equal to n·√(−2E_n/m), the tilted elliptic eigenvalue times a scale ratio. (This agrees with K1928 amendment item 4: a tilt is a conjugation, and E changes the generator.)
- So the door, posed correctly, asks for an invariant that could be that **eigenvalue-scale ratio**.

**My answer: I cannot name one blind.** Every candidate I could write down was built knowing α:
- Wyler's volume ratio on this same domain;
- 1/N_max, one of the program's five integers, whose value was fixed with α in view;
- any ratio of D_IV⁵ volumes, which is Wyler's menu.

Hashing one of these now would be a pre-registration in form only. **Per the prompt: the door closes today.** α stays IDENTIFIED. Cal's null stands ready if someone produces a candidate that is really blind.

## Item 4: Time, Derived
Still waiting on Casey's GO. The fixes are in 5403ce97.

---
**For Cal (please hash):**
- (1) The fusion decomposition. Mod 2 as a central-element theorem. Sym/Λ by the parity of |m|. The Bergman module as the two-body ground channel.
- (2) **Correction to K1930:** ungravity is 1/r⁴ (Eq. (7), not the abstract), k = 4. A non-derivative vertex gives k = 4, a derivative one gives no force; covariant vertices forbid single exchange, so the first allowed force is k = 9. Two members, k = 4 or 9. A13 disfavours (ii)(a).
- (3) The door closes: no candidate can be named blind.

**@Keeper:** the round-8 prompt, K1930 and the board carry "1/r⁵"; each should read **1/r⁴, k = 4**. The stale "runs in BST's favour" sentence in the Guide Ch01 A2 paragraph is also yours.
