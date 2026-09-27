---
node_type: k_audit
id: K1935
title: "Round 13 closed: the fourth wall is COMPLETE internally (records closed at every helicity: Elie 5830/5832, Cal Section 1006) and PRICED externally; Lyra's price list ranks D_IV⁴'s own singletons cheapest (0 scales, 1 posit, one coupling number per vertex channel). NEW (Keeper, hashed by this commit before any teammate reads it): the universal cover of SO(4,2) has TWO central characters — the clock χ_t = e^{2πiΔ} and the spatial 2π rotation χ_s = (−1)^{2(j₁+j₂)}. Every 4D massless ladder has χ_t = χ_s (spin-statistics), so every product of them does too. Every 4D piece of H² has χ_t = −1, χ_s = +1. ⟹ NO conformally covariant vertex connects H² to any number of 4D massless particles. Lyra's 'fermion-odd' rule (χ_t alone) is necessary, not sufficient."
date: 2026-09-27
author: Keeper
instrument: inline enumeration in the round-13 close (to be retained by Elie as a toy with controls); premises listed below for Cal to break
rubric_cell: "Ext-4 Recover GR/spacetime; Internal — mechanism open (coupling of the physical module to 4D massless matter)"
---

# K1935 — Round 13 closed; a second central character; round 14

## Part 1 — Round 13 rulings (Lyra R13 ed6b6d40; Elie 5832 9/9 + toy_541 fix 2e13ce7f; Cal Sections 1006–1008; Grace register v0.34 16d8d371)
1. **The fourth wall is COMPLETE internally.** Records carry no massless 4D representation at ANY helicity (Elie 5830: helicity 1 via |2a2⟩; 5832: helicities 2 and 4; Cal Section 1006: the vector |2j a2⟩ sits in the lowest K-type at every helicity and decays at rate 1 against the 3 required). Lyra retracted R12's edge reading, and Cal owned his single-chamber check. **@Grace: register v0.34's "helicity 1 pending Cal" is now RULED.**
2. **Priced externally:** the only route is a KK circle, at a second length (1/R > 30.8 GeV from g−2; > 1.5 TeV from colliders). Every BST radius is excluded.
3. **Lyra's price list** (R13): (i) a KK circle = one length plus posits (a 5D vector for helicity 1); (ii) **D_IV⁴'s own singletons posited on the sub-domain = 0 scales, 1 posit, one coupling number per vertex channel (the cheapest)**; (iii) the descent and (iv) a J-commuting commit supply nothing; (v) a J-breaking commit = a second clock, which contradicts Time, Derived's single generator. **Linear coupling of (ii) is impossible** (Cal Section 1001).
4. **"Massless quanta are act-like (non-tempered); records are tempered":** true, and both halves are theorems. **But Cal: it holds in every theory, so it is a sorting, a reading, not evidence.** Keeper concurs.
5. **Time, Derived v1.4: FULL PASS** (Cal Section 1008).
6. **Zenodo: CLEARED to publish** (Cal Section 1007). The staging is complete (bb5f9785); Casey's edit of Part B is the last step.
7. **toy_541 fixed** (Elie): g_A is marked E7 FIRED and excluded (50 quantities, 16/16), and the "FREE PARAMETERS: 0" box is corrected. CLAUDE.md is restated from the output.

## Part 2 — The second central character (Keeper; premises stated so Cal can break them)
**Lyra's rule (R13, restated verbatim):** *"On 4D massless ladders, clock parity IS fermion parity: z = e^{2πiΔ} = (−1)^{2j} … So H² (z = −1) can couple covariantly to a product of 4D singletons only if that product has an odd number of half-integer-helicity factors … Every covariant H²–4D vertex is fermion-odd."*

**What it uses:** one central element, the clock loop exp(2πJ), acting by χ_t = e^{2πiΔ}.

**What it leaves out:** π₁(SO(4)×SO(2)) = ℤ₂ × ℤ. The universal cover of SO(4,2) therefore has a SECOND central element, the spatial 2π rotation, acting by χ_s = (−1)^{2(j₁+j₂)}. Both are central, both are multiplicative under tensor products, and both must be respected by any covariant intertwiner.

**The enumeration (Keeper, 09-27, inline; Elie retains it as a toy):**
- Every 4D massless ladder (Δ = j + 1, SO(4) spin (j,0) or (0,j), j = 0 … 4) has χ_t = χ_s. That is the spin-statistics link.
- Every product of up to four ladders has (χ_t, χ_s) ∈ {(+1,+1), (−1,−1)}.
- Every K-type of every 4D summand of H² (H_{5/2+k}(D_IV⁴); K-types (l/2, l/2), weight 5/2 + k + l + 2m) has (χ_t, χ_s) = (−1, +1): an odd clock with integer spin.
- **The two sets are disjoint. So no conformally covariant vertex connects H² to any number of 4D massless particles.**

**Premises, for Cal to break (the kill lines):**
- (P1) The spatial 2π rotation is central in the relevant cover and acts by (−1)^{2(j₁+j₂)} on (j₁, j₂).
- (P2) H²'s 4D summands carry only integer j₁ + j₂. Scalar H² restricts to scalar SO(4,2) modules with harmonic K-types (Lyra R5–R8; K1927).
- (P3) The vertex is required to be covariant under the SAME SO(4,2) (the shared clock, Cal Section 1001).
- If P2 fails anywhere (a half-integer-spin piece of H² in 4D), or the relevant group is a quotient in which χ_s is trivial, the rule weakens back to Lyra's.

**What it would mean, calibrated both ways:**
- **Not a new loss:** interactions break conformal symmetry anyway, and a vertex that uses a scale (the ruler) is not covariant and not forbidden. So the statement is: **the coupling of BST's physical module to 4D's massless world cannot be conformally covariant. It needs the ruler at the vertex.** That joins walls 1 and 3: the scale enters exactly where the interaction does.
- **Price list (ii) sharpened:** D_IV⁴'s own singletons can be posited, but no covariant vertex couples them to H². So posit (ii) costs its posit AND a scale at every vertex. The "zero numbers" entry becomes "zero new lengths; the ruler at each vertex".
- **In the other direction:** H²'s pieces in 4D are odd-clock, integer-spin objects. That is exactly what a 4D generalized free field of half-integer dimension is, and it is not built from massless quanta. The structure says the physical module is not a composite of 4D massless particles. It is a sorting, and it is exact.

## Part 3 — Round 14
- **Lane A (Cal first, hashed): break or confirm Part 2.** (P1)–(P3), and whether any corpus vertex (Yukawa-shaped readings, K1650–K1653 composites, Time, Derived Section 7's two-singleton composites) is affected.
- **Lane B (Elie): retain the enumeration as a toy with controls:**
  - control 1: two massless ladders DO fuse covariantly into the massless ladders' own composites (χ_t = χ_s preserved);
  - control 2: a half-integer-Δ scalar GFF in 4D is correctly flagged (−1, +1);
  - negative control: dropping χ_s reproduces Lyra's weaker rule.
  - Extend to products of up to 6 factors.
- **Lane C (Lyra): the vertex with the ruler.** If covariance must break at the vertex, what is the MINIMAL breaking? For example, with dilation broken but Lorentz kept, only χ_s might constrain. Whether a selection rule then survives, and which one, is to be DERIVED, not assumed. Name what survives as a selection rule once only Poincaré is kept. Reconnect wall 1 (masses = the ruler × a number).
- **Lane D (Keeper): the four-walls note** gains the price list and Part 2 (after Cal's ruling), then goes to Cal's cold read. Zenodo: Casey publishes.

---

## AMENDMENT 12:55 EDT — Part 2's conclusion was too broad (round 14; an amendment, not a new K-number)
**Antecedent restated (Part 2, verbatim):** *"⟹ NO conformally covariant vertex connects H² to any number of 4D massless particles."*, and its consequence, *"the coupling … cannot be conformally covariant. It needs the ruler at the vertex."*
- **Premises P1–P3 HOLD** (Cal Section 1009, hashed 12:26:39 before anyone read Part 2; Grace pinned P1 from Mack 1977: the centre Γ ≅ ℤ₂ × ℤ, γ₁ the 2π rotation, and SU(2,2) = G̃/⟨γ₁γ₂²⟩; Elie 5834 7/7 read P2 from H²'s restricted character, not from a list).
- **Grace's one line:** in SU(2,2) the clock's full turn and the spatial 2π rotation are the SAME element. Every massless representation, and every product of them, factors through SU(2,2). H²'s pieces do not; they live only on the universal cover. A covariant coupling commutes with that element, which acts as −1 on H² and +1 on anything massless.
- **THE BREAK (Cal; Lyra independently, 5835 run before she read Cal's subject):** the two characters forbid vertices with an **ODD number of H² legs**, not all vertices. Two legs (H² ⊗ H² or H² ⊗ H̄²) carry (+1, +1) and match bosonic products (Cal enumerated to 6 factors).
  - **What is proved:** *H² is never emitted or absorbed singly by any number of massless 4D particles in a conformally covariant coupling.* That is Section 996's mod-2 conservation of H² number, made absolute for covariant couplings.
  - **"The ruler at every vertex"** is proved only for odd-H² vertices. It is conjectural for pair vertices.
  - **My error:** I wrote "any number of massless particles" and did not count the H² legs. That is enumerate-before-therefore, on the leg count.
- **Lyra retracted her R13 "fermion-odd":** with χ_s, a single-H² vertex would have to be fermion-odd (by the clock) AND fermion-even (by spin), so it cannot exist. "Fermion-odd" was half of a contradiction.
- **Pair vertices:**
  - H² ⊗ H² → one massless particle is excluded by lowest weights and spin types (Cal).
  - **The current coupling J·A (H² ⊗ H̄² with a photon) is OPEN.** Cal conjectures temperedness excludes it (a tempered H² ⊗ H̄² against a non-tempered ladder), with the gap in distribution vectors.
- **Lyra's Lane C:**
  - a ruler entering as a compact RADIUS keeps the clock, and both signs survive;
  - only a ruler entering as a Minkowski MASS (breaking J, keeping Poincaré) lifts the clock sign, after which H² couples as a boson.
  - **Exact and BST-specific (odd n):** *an interaction that keeps the clock cannot connect a single H² quantum to the massless world.*
  - **The tension, handed to Cal:** in spectra the ruler enters as a radius (the (5/2)ħc/R gap keeps the clock); at vertices it must enter as a mass (breaking the clock). Nothing in BST yet says which enters where.
