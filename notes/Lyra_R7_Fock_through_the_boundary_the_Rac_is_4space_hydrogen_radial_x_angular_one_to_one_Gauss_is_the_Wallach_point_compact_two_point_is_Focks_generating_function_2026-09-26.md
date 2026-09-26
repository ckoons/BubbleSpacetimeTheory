# Lyra R7: Fock through the boundary; the Rac is 4-space hydrogen, radial × angular one-to-one; Gauss's law is the Wallach point; the compact two-point function is Fock's generating function

**Lyra, Saturday 2026-09-26, 12:58 EDT (from `date`).** Inputs: K1929 Parts 1–3, K1928's amendment, and my 5807/5808.
**didwe:** "hydrogen four dimensions", "stereographic Fock", "Gauss law dimension", "two-point function Szego", "deconstruction unparticle", "dual pair SL(2)" → all 0. "conformal compactification" → F475 (reconnected below).
**Instrument:** `play/toy_5815_lyra_R7_…flat_limit.py`, sha256 `4305ab70185e2283…`, hashed before the run. **SCORE 6/6**, output `play/.out_toy_5815.txt`.
**Invariants used throughout:** J = K's centre (elliptic). The frame sl(2,ℝ) acts on (x₀, x₅, x₆), and its mutual centralizer is so(4) on (x₁…x₄). The K-types of H_ν(D_IV⁵) are the SO(5)-types (a,0) at J-weight ν + a + 2b, with b = 0 only on the Rac.

---

## Item 3 first (it carries items 1 and 2): the Rac is hydrogen in four space dimensions

**K1929 Part 3(b), antecedent verbatim:** *"the minimal representation of SO(5,2) has the level structure of hydrogen in four space dimensions … ν = 3/2, 5/2, 7/2, …, with degeneracies 1, 5, 14, 30, … Kill line: if the d = 4 Coulomb degeneracies or ν-offset differ from the minimal representation's K-types and weights, (b) dies."*

**Verdict: CONFIRMED; the kill line does not fire** (S1).
- d = 4 Coulomb levels: ν = N + (d−1)/2 = N + 3/2, degeneracy Σ_{l≤N} dim harm_l(ℝ⁴) = Σ(l+1)² = 1, 5, 14, 30, 55.
- These are exactly the Rac's J-weights 3/2 + a and the dimensions of the SO(5)-types (a,0).
- Control: d = 3 gives ν = N + 1 and degeneracy (N+1)², which is SO(4,2)'s ladder.

**Stronger than K1929 asked, and it answers item 2** (S2):
> **Rac | SL(2,ℝ) × SO(4) = ⊕_{i≥0} D⁺_{3/2+i} ⊗ (i/2, i/2): each SO(4)-type appears once, paired with one radial ladder.**

This is 4-space hydrogen's radial × angular decomposition exactly. The angular momentum l = i is carried by the SO(4)-type (i/2, i/2), which is the S³ harmonics of degree l. The radial so(2,1) has Bargmann index l + 3/2 = l + (d−1)/2, which is the textbook d-dimensional Coulomb radial index. **On H² the same pairing is not one-to-one:** the type (i/2, i/2) pairs with D⁺_{5/2+i+2m} for every m ≥ 0 (5808 and S2). **The extra multiplicity is exactly the odd clock of Theorem B.** H² is 4-space hydrogen tensored with the clock ladder.

**How D_IV⁵ → D_IV⁴ acts on it.** Rac|SO(4,2) = H_{3/2}(D_IV⁴) ⊕ H_{5/2}(D_IV⁴) (Jakobsen–Vergne Prop. 3.2, pinned by Grace). λ = 1 never appears. **4-space hydrogen does not contain 3-space hydrogen.**

**Is that Gauss's law in representation language? Yes. The invariant is the Wallach point (D−2)/2, the scaling dimension at which a massless field's Green function falls as r^{−(D−2)}, i.e. flux through S^{D−2}** (S3).
- r^{−(D−2)} is harmonic in ℝ^D for D = 3, 4, 5.
- r^{−3} is **not** harmonic in ℝ⁴ (its Laplacian is 3/r⁵).
- Restricting a 5D field to a 4D slice keeps its falloff r^{−3} (exponent 2Δ = 3). It cannot become 4D's r^{−2} (2Δ = 2, λ = 1).
- **So the absent λ = 1 is "the 5D Coulomb law restricted to a hyperplane is still a 5D Coulomb law, not a 4D one."**
- **Calibrated:** this is exact for the field (spacetime) realization. Hydrogen uses the same representation in Fock's momentum realization. Identifying the two uses is a coordinate (Cal Section 990: one group acting on different spaces).

**Menu risk, written as instructed:** every D_IV^n carries its own (n−1)-space hydrogen as its minimal representation. **This is a recapitulation, like K1927.** What is BST's own is only that n = 5 was forced, so BST's hydrogen has four space dimensions and its physical module sits one clock unit above it.

## Item 1: Fock through the boundary, as linear algebra

**The compact realization.** The Šilov boundary is (S⁴ × S¹)/ℤ₂. Boundary values of H² are Y_a(x)·e^{iwφ}, with Y_a a degree-a harmonic on S⁴ and J = −i∂_φ. The weights run over **w = 5/2 + a + 2b, the positive-frequency (Hardy) half of L²(S¹) ⊗ harm(S⁴)**. Under the ℤ₂ map (x, φ) ↦ (−x, φ + π) they pick up (−1)^a e^{iπw} = e^{5πi/2} = **i**. So H²'s boundary values are sections twisted by i, not functions: the double cover again, sitting in the ℤ₂ (Cal Section 990's 2:1). J is discrete because φ is a circle.

**The flat realization.** On ℝ^{1,4}, P₀ = i∂_t, with continuous spectrum [0, ∞) on the forward-cone sector H²₊ (T2625).

**The map between them is the Lorentzian stereographic projection:** t ± r = tan((τ ± θ)/2) (Lüscher–Mack's map one dimension up; pin via Grace R165). It is conformal, not an isometry. The compactification adds the light cone at infinity. **This is the Cayley change of realization of R6 item 2 (F475, F222),** and J = ½(P₀ + K₀) in the compact-sign convention.

**Where Fock's S³ sits.** Fix the frame's pole x₅ ∈ S⁴. The latitude 3-spheres around it are SO(4)-orbits. A degree-a harmonic on S⁴ restricts to ⊕_{i≤a} (i/2, i/2) (K1927(b)), i.e. S³ harmonics of every degree up to a. **Fock's S³ is the latitude sphere of the Šilov S⁴ about the frame's pole, and the S⁴ itself is 4-space hydrogen's Fock sphere.**
**Calibrated:** Fock's spheres compactify **momentum** space; BST's Šilov S⁴ compactifies **spacetime**. It is the same group SO(d+1) acting on different spaces, so the identification is a coordinate.

**Answer to Casey, one paragraph (P = position, C = coordinate):**
- Bound states are discrete because they live on the **compact realization** of the Šilov boundary, where the clock J turns a circle. [P: the Šilov boundary is an invariant of D_IV⁵.]
- The continuum is the same boundary in its **flat realization** ℝ^{1,4}, where the energy P₀ translates along a line. [P: the conjugacy type of each generator.]
- The two realizations differ by the light cone at infinity that stereographic projection adds, which is Fock's trick one dimension up. [P: the compactification. C: which realization an observer uses, a frame, T2565.]
- The interior is what both reconstruct (Szegő, exponent 5/2). [P]
- **No "exterior" is needed.** Boundary data outside the forward cone write nothing into the interior (T2625). [P]
- **Segal's lesson, binding:** the difference between the realizations is not a redshift. [ruling, K1928 amendment]

## Item 2: the frame SL(2,ℝ) × SO(4)

**Is it the dual pair behind 5808?** Yes, in the mutual-centralizer sense. SL(2,ℝ) on (x₀, x₅, x₆) and SO(4) on (x₁…x₄) are each other's centralizers in SO(5,2). **It is Howe-like (one-to-one) on the Rac and not on H²** (S2). So "dual pair" is exact for the minimal representation, and on H² the clock adds multiplicity.
- **Radial/angular:** SL(2,ℝ) is the radial so(2,1): Bargmann index = l + 3/2, with J its elliptic generator. SO(4) is the angular part: l = i, shells (l+1)².
- **After the descent:** the descent picks a normal direction x₄ inside the SO(4)'s ℝ⁴, so SO(4) → SO(3), the 3-space angular momentum. The pair becomes SL(2,ℝ) × SO(3) ⊂ SO(4,2), which is 3-space hydrogen's radial × angular structure. **The Lorentz SO(3,1) is not inside SL(2,ℝ) × SO(4)**: the boosts M₀ᵢ mix the two factors. T2545's (3,1) signature belongs to the Lorentz group. This compact SO(4) is its Wick partner (F475), which is a reading, not a theorem.
- **One choice or two? Two, and nested:** (1) the frame's pole x₅ ∈ S⁴, which fixes the sl(2,ℝ) and leaves SO(4); (2) the descent's normal x₄ ∈ S³ ⊥ x₅, which leaves SO(3). Both are K-conjugate frames, hence coordinates. **T2565's Machian input is choice (2)**; choice (1) is what makes "hydrogen shells" visible. Together they form one flag, (x₅, x₄), so a single observer frame supplies both, as two separate pieces of data.

## Item 4: processes are boundary correlators

**Compact realization (S4, S5).** On the Euclidean cylinder, the two-point function of weight Δ is
> **G = [2(cos τ − cos θ)]^{−Δ} = t^Δ (1 − 2t cos θ + t²)^{−Δ} = Σ_N t^{Δ+N} C_N^{(Δ)}(cos θ), t = e^{−iτ}.**
- **At Δ = 1 this is Fock's generating function for 3-space hydrogen** (C^{(1)} = the S³ harmonics). At Δ = 3/2 it is the Rac (4-space hydrogen). At Δ = 5/2 it is H².
- The J-spectrum Δ + N appears as the powers of t, the discrete ladder.
- **Theorem B in correlator form:** C_N^{(5/2)} = Σ_b c_b C_{N−2b}^{(3/2)} with every c_b > 0 and ⌊N/2⌋ + 1 terms (checked to N = 12). This is H² = Rac ⊗ odd clock, one correlator.

**Flat realization (S6).** Take the stereographic limit τ = T/R, θ = X/R, R → ∞. Then R^{−2Δ}[2(cosh(T/R) − cos(X/R))]^{−Δ} → (T² + X²)^{−Δ}, the Δ = 5/2 conformal two-point function in 5D. At R = 10³ the relative error is 2×10⁻⁷.

**Where the ruler R enters:** in exactly two places. (i) The clock spacing: energies ħc·w/R. (ii) The normalization R^{2Δ} of the flat limit. Nothing else: the position-space correlator is otherwise R-free. **One point to flag, standard, pin owed (Georgi 2007 / the GFF literature):** the Källén–Lehmann density of a Δ-field in d dimensions goes as (μ²)^{Δ−d/2}. **At the Hardy point in 5D, Δ = d/2 exactly, so the density is flat in μ²**, the marginal case. Its momentum-space two-point function is logarithmic, so a scale appears there, in a contact term only. In the compact realization R supplies that scale. This is a lead worth Cal's eye; it is not a derived energy.

**The 4D restriction: a correction to K1929 Part 3(c). Antecedent verbatim:** *"Its 4D restriction should converge to the sum of Δ = 5/2 + k densities."*
- The **restricted field** φ|_{x₄=0} keeps the falloff (T² + X²)^{−5/2} (S3/S6 logic). Its correlator is a **single 4D Δ = 5/2 generalized free field** (density ∝ (μ²)^{1/2}), **not** the sum over k.
- The k ≥ 1 summands of ⊕_k H_{5/2+k}(D_IV⁴) are the **normal-derivative fields** ∂_⊥^k φ|slice, made primary by the holographic operators (Elie 5805, μ = λ − 2). Each has its own Δ = 5/2 + k two-point function.
- **The sum over k describes the Hilbert space (all the fields a 4D observer can build), not the correlator of the restricted field.** Stephanov's deconstruction applies to each tower in R (clock spacing → 0), not to the sum over k.
- **Kill line for (c) restated:** if the R → ∞ limit of the compact correlator is not (T² + X²)^{−5/2}, the continuum claim dies. **It does not fire (S6).**

## Item 5: Time, Derived
Waiting on Casey's GO. The two one-line fixes are in the item-1 note (5403ce97). Cal gate-reads them after I apply them.

---
**For Cal (please hash):**
- (3) Rac = 4-space hydrogen, confirmed. The radial × angular pairing is one-to-one on the Rac and carries multiplicity from the clock on H².
- (3) The missing λ = 1 is Gauss's law. Exact for fields; a coordinate for hydrogen.
- (1) The compact/flat pair. H²'s boundary values are twisted by i. Fock's S³ is the latitude sphere.
- (2) Two nested choices, (x₅, x₄); T2565 is the second.
- (4) The compact correlator is Fock's generating function at Δ. The flat limit holds. R enters only as spacing and normalization. The Hardy point is marginal (Δ = d/2).
- (4) The correction to K1929(c): the restricted field is one Δ = 5/2; the k-sum is the Hilbert space, not the correlator.
