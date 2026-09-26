# Lyra R6 items 2–5: three times on H²; the Cayley transform is a change of realization, not a conjugation; the D_IV⁵ / D_IV⁴ table; the gap is the ruler; the Szegő exponent is the ground weight

**Lyra, Saturday 2026-09-26, 11:42 EDT (from `date`).** This follows item 1 (5403ce97). Ground weights are quoted per module: **5/2 on H², 3/2 on the Rac.**
**didwe:** "Cayley transform" → F475/F222 (known; no registry row); "Szego kernel exponent" → 0; "mass gap ruler" → K1714 (the KK gap, not Clay's; the same statement, extended here).
**Instrument:** `play/toy_5808_lyra_R6_three_times_on_H2_…py`, sha256 `b02df51a52e06a2c…`, hashed before the run. **SCORE 6/6**, output `play/.out_toy_5808.txt`. R6 is a weak check (it only confirms λ > 0 on every summand). The continuous spectra of P₀ and D on D⁺_λ are quoted from standard SL(2,ℝ) theory, not computed.

---

## Item 2: the three times on H²

**Kill line (written first):** if H² restricted to the sl(2,ℝ) has a summand that is not a positive discrete series, then "elliptic time is discrete, parabolic time is continuous" fails on that summand.

**Invariant:** the sl(2,ℝ) = so(2,1) on the coordinates (x₀, x₅, x₆) (Keeper's coordinates, K1928 Part 3). It contains K's centre J = M₀₆. Its commutant in so(5,2) is so(4) (rotations of x₁…x₄). Conjugacy type is the sign of −det in the 2×2 picture.

**The decomposition (R4, exact to J-weight 40):**
> **H²(D_IV⁵) | SL(2,ℝ) × SO(4) = ⊕_{i, m ≥ 0} D⁺_{5/2 + i + 2m} ⊗ (i/2, i/2).**

Every summand is a positive discrete series with lowest weight at least 5/2 (the item-1 ground weight). Its SO(4) partner is a hydrogen shell. On each D⁺_λ (standard; realized on L²((0, ∞), p^{2λ−1} dp)):

| type (invariant) | element | spectrum on each D⁺_λ | on H² |
|---|---|---|---|
| elliptic | J = M₀₆ (the clock) | λ + ℤ≥0, discrete | **5/2 + ℤ≥0**, multiplicity Σ_i (i+1)²(⌊(w − 5/2 − i)/2⌋ + 1) |
| parabolic | P₀ | (0, ∞), absolutely continuous; no invariant vector | (0, ∞), infinite multiplicity, **no gap** |
| hyperbolic | D | ℝ, absolutely continuous | ℝ |

**The D_IV⁴ summands (R5, k = 0..3):** H_{5/2+k}(D_IV⁴) = ⊕_{i,m} D⁺_{5/2+k+i+2m} ⊗ (SO(3)-type i). This sl(2,ℝ) lies inside the 4D conformal so(4,2), because dropping x₄ leaves x₀, x₅, x₆ intact. The same three spectra appear, with the elliptic floor raised by k.

**What this says in words:** one Hilbert space carries three times. The clock (elliptic) has a **floor, 5/2, and steps**. The boundary energy (parabolic) has **a floor at 0, no steps and no gap**. Scale (hyperbolic) has neither. **The gap is a property of the elliptic time only.**

### The Cayley transform: a correction to how the prompt states it
**No operator carries J to P₀ by conjugation.** J is elliptic (−det = −1) and P₀ is parabolic (−det = 0), and type is invariant under every real conjugation (R1). The complex Cayley element c = (1/√2)[[1, i], [i, 1]] maps J to **i·H, with H hyperbolic**, not to P₀ (R2). This is the standard fact that Cayley takes the compact Cartan to i times the split Cartan.
**What the Cayley transform does:** it changes the *realization*. It takes the bounded disc (domain) to the upper half-plane (tube), and H² on the domain to the Hardy space H²₊ on the tube over the future cone. In the tube realization the clock is expressed as **J = ½(P₀ + K₀)** (R3, in the sign convention where that combination is elliptic; with the opposite sign of K₀ it is hyperbolic, which is Keeper's first-run slip, kept as the control). **J is a combination of the boundary energy and its conformal partner, not a conjugate of the boundary energy.** This is the precise form of "F475: Cayley = Wick rotation". The registry's missing Cayley row (Grace) should carry this wording.

### Reconnects
- **T2625 (Three-Sector Theorem) is the parabolic picture.** L²(ℝ^{1,4}) = H²₊ ⊕ H²₋ ⊕ spacelike. **H² (the domain) ≅ H²₊ (the tube, via Cayley)** is exactly the sector where P₀ ≥ 0 and Fourier support lies in the closed forward cone (Paley–Wiener). Two positivity statements are one statement in two realizations:
  - J ≥ 5/2 on the domain (the arrow, Time, Derived Section 3);
  - P₀ ≥ 0 on the tube.
  They differ only in that J has a floor above zero and P₀ does not.
- **Time, Derived Sections 2–3:** "the arrow is the positivity of J's spectrum" stands. It is realized on the boundary as T2625's H²₊. The ground weight is 5/2 on H² (item 1's fix).
- **T2629 (the clock row):** the chain law is winding-blind. Consistent with the table: the clock reading is the elliptic eigenvalue, and the laws that act do so through the sl(2,ℝ)'s D⁺ structure, which does not see the SO(4) label.
- **The ledger picture:** tick = begin-time. The elliptic generator's eigenvalues become energies only after a length is supplied: E = ħc·w/R, with w ∈ 5/2 + ℤ. So the tick is ħ/E = R/(c·w). The only length available is the ruler (item 4). Λ = 3H²Ω_Λ is untouched; it is an identity (K1919).

## Item 3: D_IV⁵ vs D_IV⁴, the table Casey asked for

P = position (invariant of the domain or representation); C = coordinate (depends on a choice).

| row | D_IV⁵ | D_IV⁴ | P/C |
|---|---|---|---|
| group | SO₀(5,2) | SO₀(4,2) = the 4D conformal group | P |
| dim_ℂ / dim_ℝ / rank / genus | 5 / 10 / 2 / 5 | 4 / 8 / 2 / 4 | P |
| Šilov boundary | (S⁴ × S¹)/ℤ₂ = compactified ℝ^{1,4}, dim 5 | (S³ × S¹)/ℤ₂ = compactified ℝ^{1,3}, dim 4 | P |
| real form at a Šilov point | Lorentzian (1,4), 2:1 (Q_u = Q_{−u}, Cal Section 990) | Lorentzian (1,3), 2:1 | P |
| Wallach set | {0} ∪ [3/2, ∞) | {0} ∪ [1, ∞) (= Δ ≥ (d−2)/2, Mack 1977, pin owed) | P |
| minimal representation | Rac: 5D massless scalar, J-floor 3/2 | ladder: 4D massless scalar, J-floor 1 = **hydrogen's representation** | P (the identification "hydrogen = this rep" is C, Cal Section 990) |
| Hardy weight dim/rank | **5/2** (half-integer: the double cover is forced) | 2 (integer: no double cover forced) | P |
| Bergman weight = genus | 5 | 4 | P |
| J-lattice of H² | 5/2 + ℤ≥0 | 2 + ℤ≥0 | P |
| SO(n−1)-types of H² | (i/2, i/2), dim n² (the hydrogen shells) | SO(3) spin i, dim 2i + 1 | P (but generic to every SO(n)-scalar theory, Cal Section 990) |
| restriction tower | H²₅ | SO(4,2) = ⊕_k H_{5/2+k}(D_IV⁴) (JV 1979; checked, K-characters) | — | P |
| meaning of k | normal-derivative order into x₄ = the KK index | — | P (the tower); C ("KK" as a physical reading) |
| holographic operators | H_{5/2}(D⁵) → H_{5/2+k}(D⁴), k-th normal derivative with Gegenbauer coefficients (Kobayashi–Pevzner; Labriet 2203.00009). **Parameter pin owed (Grace); Elie builds k = 0,1,2.** | — | P |
| Szegő kernel | h(z,w)^{−5/2} | h(z,w)^{−2} | P (item 5) |
| what is lost going down | the choice of which spatial direction becomes normal. The geometry does not force it: T2565, **Machian** | — | C (by T2565's theorem: a frame) |

**Similarities:** both are rank 2 with the same sl(2,ℝ) spine and the same three times. Hydrogen's shell pattern appears in both.
**Differences:** the Hardy weight's parity: 5/2 is half-integer, 2 is integer. Hydrogen is D_IV⁴'s minimal representation and is not in D_IV⁵'s H². Going down costs a frame choice that BST does not force.

## Item 4: the gap is where the scale enters. In BST that is the ruler, entering as a unit, not as a mechanism.

**Kill line (written first):** if no BST object breaks SO(4,2) to Poincaré × scale, then BST's 4D continuum is scale-free and every mass is the ruler times a number.

**Invariant:** among the three times, only the elliptic one has a gap (item 2). A gap in the **parabolic** energy, a Minkowski mass gap, needs the spectrum of P² bounded away from 0. On every H_{5/2+k}(D_IV⁴) that spectrum is **[0, ∞), continuous**: these are generalized free fields ("unparticles"; Georgi pin owed). SO(4,2) forbids a gap, because D rescales P².

**The candidates, each tested:**
1. **The ruler R (the one input):** it enters as the radius of the compact picture. The elliptic energies become (ħc/R)·w, with **gap (5/2)ħc/R** on H² and 1·ħc/R for D_IV⁴'s ladder. This breaks D and P and keeps K. It is the Einstein-static-universe gap, **K1714's KK gap, not Clay's.** As R → ∞ it closes.
2. **The tick:** tick = ħ/E is derived from J's eigenvalue once R is given (item 2). It is not a second scale.
3. **The Machian descent:** it picks a frame, breaking Lorentz boosts down to the observer's rest frame. It breaks no scale, so it cannot make a gap.

**Verdict: the present state, stated honestly.** Nothing in BST breaks SO(4,2) → Poincaré × scale as a mechanism. The one dimensionful object is the ruler. It produces a gap only in the elliptic (compact) picture, with value (5/2)ħc/R, which is a KK gap. **Every Minkowski mass in BST is the ruler times a number.** The kill line fires as written. This is not new; it is K1714 plus the one-input statement, now in representation language.

**The open question that would change this:** is there a BST reason to read the elliptic time J as physical time at the particle scale, as Segal did? Segal's chronometric cosmology is the precedent, and its redshift-law tests are pin owed: a menu risk, and the refutations must be pinned too. If yes, masses are J-eigenvalues in units ħc/R, and the gap 5/2 is physical. If no, the gap is at the cosmological radius.

## Item 5: "writing reality on the surface". The Szegő exponent is the ground weight.

**Invariant:** the Szegő (Hardy) kernel of the Lie ball is **S(z, w) = c · h(z, w)^{−dim/rank} = h^{−5/2}**, with h the generic norm, h(z,w) = 1 − 2 z·w̄ + (z·z)(w̄·w̄). This is Faraut–Korányi, standard; pin owed. **The exponent of the boundary-to-interior map is the J-ground weight of item 1.** "Writing on the surface" (the Szegő reproduction from the Šilov boundary) and "the interior clock's floor" are one number, 5/2.

**Which boundary data determine an interior state:** exactly the part of L²(Šilov) that lies in **T2625's H²₊**: positive energy, Fourier support in the forward cone. The Szegő projection sends the H²₋ and spacelike sectors to zero. **One line for the table: boundary data outside the forward cone write nothing into the interior.** This rhymes with Casey's "a winding that does not close writes no value". That is a lead, not a derivation.

**The 2:1 (Cal Section 990):** u and −u give the same real form. H² still distinguishes them, by the phase e^{iπJ} = ±i (J ∈ 5/2 + ℤ). The half-turn that the real forms cannot see is exactly the half-integer weight: **the double cover lives in the 2:1.**

**Can fail:** if a committed quantity has no boundary value in H²₊ (T2626: no survivor at a Šilov point, Howe–Moore), the "write = boundary value" reading breaks. That check is still owed.

---
**For Cal (please hash):**
- (2) H² = ⊕ D⁺_{5/2+i+2m} ⊗ (i/2, i/2). Only the elliptic time has a gap.
- (2) Cayley is a change of realization, J = ½(P₀ + K₀), not a conjugation; conjugation sends J to i·(hyperbolic).
- (3) The table, with every row marked P or C.
- (4) The kill line fires: the gap is the ruler's KK gap (5/2)ħc/R.
- (5) The Szegő exponent 5/2 is the ground weight; data outside H²₊ write nothing.

**For Grace:** Faraut–Korányi (Szegő = h^{−dim/rank}); the Gegenbauer parameter in Labriet/Kobayashi–Pevzner for n = 5 → 4.
**For Elie:** toy 5808 is the matrix/character level; the discrete-vs-continuous level-spacing toy is yours.
