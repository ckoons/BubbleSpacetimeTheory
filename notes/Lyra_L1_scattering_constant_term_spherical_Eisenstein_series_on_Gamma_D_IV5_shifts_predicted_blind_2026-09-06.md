# L1 — The constant term of the spherical Eisenstein series on Γ\D_IV⁵: shifts, local factors, resonances. PREDICTED BEFORE ELIE COMPUTES.
**Lyra, Sunday 2026-09-06, 11:31 EDT. Round 120 L1. Written from the root data and Langlands' constant-term formula; no numerics run before this file was hashed. Half-blind protocol: Section 3 (shifts) is for Cal to score conventions; Section 5 (numbers) is for Elie's E6. Toy 5700 (my own consistency check: unitarity and pole orders) runs AFTER the hash.**

## 0. Objects, pinned
- G = SO(Q), Q the integral form of signature (5,2) on ℤ⁷ that the corpus's "Γ(137)\D_IV⁵" rows use (T1407, T1448, T1451): I take Q = x₁²+…+x₅² − x₆² − x₇² (any lattice with two hyperbolic planes over ℚ and a DEFINITE ternary kernel gives the same shifts; the kernel's discriminant enters only at p = 2 and ∞ below). D_IV⁵ = G(ℝ)/K.
- ℚ-rank 2 = ℝ-rank 2: Witt index of Q over ℚ is 2 (planes (x₁,x₆), (x₂,x₇)); the anisotropic kernel is the ternary form q₀ = x₃²+x₄²+x₅² — anisotropic over ℚ, over ℚ₂ and over ℝ, isotropic at every odd p (Hasse invariant 1 vs (−1,−1)_p). This is the prompt's "kernel −I₃" up to the sign convention.
- Restricted (= relative) root system: **B₂**, short roots ±e₁, ±e₂ with multiplicity n − 2 = **3**, long roots ±e₁±e₂ with multiplicity **1**; ρ_𝔞 = ½(3e₁+3e₂ + (e₁−e₂) + (e₁+e₂)) = **(5/2, 3/2)** (Cal §844). **There are no double roots**: SO(p,q), p > q, is of type B_q, not BC_q. (T1298's "B₂ double root m_{2α} = 1" and T1299's "r₂ = Sym² from the double roots" mislabel the LONG root e₁+e₂; see Section 6.)
- Minimal ℚ-parabolic P₀ = stabiliser of the flag (isotropic line ⊂ isotropic plane), Levi M₀ = T × SO(q₀), T ≅ GL₁², SO(q₀) anisotropic over ℚ (SO(q₀)(ℚ)\SO(q₀)(𝔸) compact). Maximal parabolics: P₁ (isotropic line; Levi GL₁ × SO(4,1)-type, the rank-one group of the SHORT root) and P₂ = Siegel (isotropic plane; Levi GL₂ × SO(q₀), the rank-one group of the LONG root). T1299 computed P₂'s operator.
- Absolute root system B₃ (SO₇ over ℂ), coordinates ε₁, ε₂, ε₃ with ε₃ the torus of SO(q₀). Restriction: e_i = ε_i|; short e₁ comes from ε₁ (mult 1) and ε₁ ± ε₃ (mult 2) — total 3 ✓; long e₁ ± e₂ from ε₁ ± ε₂ only ✓.

## 1. The spherical Eisenstein series and its constant term (Langlands)
E(g, λ) induced from P₀(𝔸) with the trivial representation on SO(q₀)(𝔸) and the character e^{⟨λ+ρ, H⟩} of T, λ ∈ 𝔞*_ℂ = ℂe₁ ⊕ ℂe₂. Constant term along P₀:
  E_{P₀}(g, λ) = Σ_{w ∈ W(B₂)} c(w, λ) e^{⟨wλ + ρ, H(g)⟩},  |W(B₂)| = 8,
  c(w, λ) = Π_{β > 0, wβ < 0} c_β(λ),
where c_β is the rank-one c-function of the Levi L_β. Unitary axis Re λ = 0 (Mellin-unitarity, K1862 C.1); E converges for Re⟨λ, β^∨⟩ > ⟨ρ, β^∨⟩, i.e. Re(2λ₁) > 5, Re(λ₁−λ₂) > 1, etc.

## 2. The four rank-one factors — DERIVED from the absolute roots at split places, then corrected at 2 and ∞
Write ξ(s) = π^{−s/2}Γ(s/2)ζ(s), ξ(s) = ξ(1−s). Coroot pairings: ⟨λ, (e₁±e₂)^∨⟩ = λ₁ ± λ₂; ⟨λ, e_i^∨⟩ = 2λ_i.

**Long roots (Siegel side, GL₂ Levi, kernel a spectator):**
  c_{e₁−e₂}(λ) = ξ(λ₁−λ₂)/ξ(λ₁−λ₂+1),   c_{e₁+e₂}(λ) = ξ(λ₁+λ₂)/ξ(λ₁+λ₂+1).
No character enters: the kernel does not act.

**Short roots (the rank-one group SO(4,1)_ℚ with the anisotropic kernel):** at an odd prime the group is split, the trivial representation of SO(q₀)(ℚ_p) ≅ PGL₂(ℚ_p) sits at absolute parameter λ₃ = ½ (⟨λ₃ε₃, ε₃^∨⟩ = 1), and Gindikin–Karpelevich over the three absolute roots ε₁ (pairing 2λ₁), ε₁−ε₃ (λ₁−½), ε₁+ε₃ (λ₁+½) gives the split-place factor
  c_{e₁}^{split}(λ) = ξ(2λ₁)/ξ(2λ₁+1) · ξ(λ₁−½)/ξ(λ₁+½) · ξ(λ₁+½)/ξ(λ₁+3/2) = **ξ(2λ₁) ξ(λ₁−½) / [ξ(2λ₁+1) ξ(λ₁+3/2)]**,
(the choice λ₃ = −½ gives the same product). The middle pair ξ(λ₁∓½) is the standard L-function L(λ₁, |·|^{λ₁} × 1_{PGL₂}) = ζ(λ₁−½)ζ(λ₁+½) of the trivial representation, whose Satake parameter is non-tempered.

**Why the split formula cannot be the whole answer (the referee's check I ran on paper):** at λ₁ = ½ it has ξ(1)·ξ(0) in the numerator against ξ(2)² below — a DOUBLE pole inside the positive chamber, which Langlands' theory forbids (poles of the Eisenstein series in Re λ > 0 are simple). Something must cancel one pole, and the only places the kernel differs from split are p = 2 and ∞.

**The p = 2 and ∞ factors (prediction, via Jacquet–Langlands on the rank-one Levi).** SO(q₀)(ℚ₂) and SO(q₀)(ℝ) are compact (q₀ anisotropic there): the trivial representation of the compact form corresponds under JL to the **Steinberg** representation at 2 and to the **weight-2 discrete series** at ∞. The intertwining operator of the rank-one inner form GL₁ × SO(H ⊕ q₀) ≅ GL₁ × PGSp(1,1)(D) has the same normalising L-factors as its quasi-split partner with the JL transfer inserted (Muić–Savin; to be pinned). So the completed middle L-function is not ξ(s−½)ξ(s+½) but
  **Λ(s) := Γ_ℂ(s+½) · ζ(s+½) · ζ(s−½) · (1 − 2^{½−s})**  (up to π-powers),
i.e. the archimedean factor Γ_ℂ(s−½) is replaced by Γ_ℂ(s+½) and the Euler factor of ζ(s−½) at 2 is REMOVED. Λ satisfies Λ(s) = ε(s)Λ(1−s) with ε(s) = ±2^{½−s} (conductor 2, the Steinberg root number). Then
  **c_{e₁}(λ) = ξ(2λ₁)/ξ(2λ₁+1) · Λ(λ₁) / [ε(λ₁) Λ(λ₁+1)]**,   and the same with λ₂ for c_{e₂}.
Check 1 (the double pole is gone): (1 − 2^{½−s}) vanishes at s = ½, cancelling ξ(1); the pole of c_{e₁} at λ₁ = ½ is simple. Check 2 (Maass–Selberg): c_{e₁}(λ)c_{e₁}(−λ) = [Λ(λ)/Λ(1−λ)]·[Λ(−λ)/Λ(1+λ)]/[ε(λ)ε(−λ)] = 2^{½−λ}·2^{½+λ}/(2^{½−λ}2^{½+λ}) = 1 ✓ — the ε-factor is REQUIRED for unitarity; without it the product is 2. (The naive split formula is also unitary, so unitarity alone does not select; the pole order does.) Toy 5700 checks both numerically after this hash.

**Does a quadratic character enter from the kernel? NO at level 1.** The kernel is odd-dimensional (dim q₀ = 3): SO₃ is split-type with L-group SL₂(ℂ), and its discriminant character does not enter the L-group. A quadratic character from the kernel would appear only for an EVEN-dimensional kernel (e.g. SO(3,1): ζ_{ℚ(i)} = ζ·L(χ₋₄)); that is the family rule, and D_IV⁵'s n_C = 5 puts the kernel at odd dimension 3. What the kernel contributes instead is the JL modification at the two places where it is anisotropic, 2 and ∞.

## 3. THE SHIFTS — for Cal (conventions), posted blind
In the s-normalisation s = λ + ½ per coordinate (so the unitary axis is Re s = ½ and ρ reads (3, 2)):
| root | factor | ζ's appear at |
|---|---|---|
| e₁−e₂ (long) | ξ(s₁−s₂)/ξ(s₁−s₂+1) | ζ(s₁−s₂), ζ(s₁−s₂+1) |
| e₁+e₂ (long) | ξ(s₁+s₂−1)/ξ(s₁+s₂) | ζ(s₁+s₂−1), ζ(s₁+s₂) |
| e_i (short), factor A | ξ(2s_i−1)/ξ(2s_i) | ζ(2s_i−1)/ζ(2s_i) — the SL₂-type "2s" pair |
| e_i (short), factor B | Λ(s_i−½)/[ε Λ(s_i+½)] | ζ(s_i)ζ(s_i−1)(1−2^{1−s_i}) / ζ(s_i+1)ζ(s_i)(1−2^{−s_i}) = ζ(s_i−1)(1−2^{1−s_i}) / [ζ(s_i+1)(1−2^{−s_i})] |
So ζ sits in the short-root factor TWICE (A and B), with the shifts a = 1, b = 0 in ζ(2s−a)/ζ(2s−b) for A, and the "ζ(s−1)/ζ(s+1)" pair for B — the latter with the 2-Euler-factor surgery. The full long-element term c(w₀, λ) = product of all four. Multiplicities: the short-root factor B carries the exponent that T1299 wrote as "cubed" — here it is ONE Λ-ratio because the three absolute roots over e₁ collapse to ξ(2λ)·Λ(λ)-ratios, not to a cube; the "3" is visible as the three absolute roots, not as an exponent (T1299's cube is the Siegel-parabolic statement with π cuspidal on GL₂, a different induction).

## 4. RESONANCES — the pole set of the scattering matrix (level 1)
Poles of c(w, λ) come from ZEROS of the denominators (ξ has no poles except 0, 1, which give the residual spectrum):
- **long roots:** ζ(λ₁ ∓ λ₂ + 1) = 0 ⟺ λ₁ ∓ λ₂ = ρ − 1, i.e. **Re(λ₁∓λ₂) = −½ on RH**, imaginary parts γ_n.
- **short roots, factor A:** ζ(2λ_i + 1) = 0 ⟺ **λ_i = −¼ + iγ_n/2**.
- **short roots, factor B:** ζ(λ_i + 3/2) = 0 ⟺ **λ_i = −1 + iγ_n**; and the p = 2 surgery denominator (1 − 2^{−½−λ_i}) = 0 ⟺ **λ_i = −½ + 2πik/ln 2, k ∈ ℤ — a comb from the single prime 2**, spacing 2π/ln 2 = 9.0647, with no counterpart at any odd prime. This comb is the fingerprint of the anisotropic kernel and the sharpest thing E6 can test: it is NOT a zero of any L-function.
- Γ-factors in denominators have poles, not zeros: they contribute zeros of c, not resonances.
**Target sentence, scored in advance:** "the zeros of ζ are the resonances of Γ\D_IV⁵" is TRUE at level 1 in the sense that every nontrivial zero of ζ appears as a resonance at each of the four shifts above, and the resonance set is exactly {those} ∪ {the 2-comb}. It is DERIVED-grade if E6 matches the pole set at 10⁻¹⁰; it is not RH-bearing: it restates ζ's zeros as poles of ξ-ratios, and by the barrier lemma (K1863 §5) it is invariant under ζ → ζ_{ℤ⁵} in form — a scattering matrix built from any ξ-like function has the same shape. What is NOT invariant is factor B's Euler surgery at 2, which exists because ζ HAS an Euler product; that is where the Euler product enters this row, and the only place.

## 4a. LEVEL 137 — what Γ(137) changes (prediction)
For the principal congruence subgroup of level N = 137 the K-spherical vector is replaced by the K(137)-fixed space and the constant term becomes a MATRIX indexed by the cusps of Γ(137), block-diagonalised by the characters (χ₁, χ₂) of T(ℤ/137) ≅ (ℤ/137)^{×2} (Huxley's structure for Γ(N) ⊂ SL₂, lifted to the rank-2 torus). Each rank-one factor acquires the corresponding character: the long-root factors become ξ(λ₁∓λ₂, χ₁χ₂^{∓1})/ξ(λ₁∓λ₂+1, χ₁χ₂^{∓1}) (primitive-character completions; Gauss sums in the ε), factor A becomes ξ(2λ_i, χ_i²)/ξ(2λ_i+1, χ_i²), factor B becomes the χ_i-twist of Λ. **Prediction:** the resonance set of Γ(137)\D_IV⁵ is the union over ALL 136 Dirichlet characters mod 137 of the zeros of L(s, χ) at the four shifts (quadratic χ mod 137 included — that is the only quadratic character in the row, and it comes from the LEVEL, not from the kernel), plus the 2-comb, plus 137-local combs from the ramified ε-factors (spacing 2π/ln 137 = 1.2770). **Consequence for the target sentence:** at level 137 the resonances are the zeros of every L(s, χ mod 137), of which ζ's are the trivial-character block. A "ζ-only" resonance set needs level 1. N_max = 137 contributes 136 extra L-functions to the row and nothing to ζ.

## 5. NUMBERS — for Elie (E6), posted blind
Using the first zeros of ζ, γ₁ = 14.134725141734693, γ₂ = 21.022039638771555, γ₃ = 25.010857580145688, γ₄ = 30.424876125859513, γ₅ = 32.935061587739189, the level-1 scattering determinant has poles at (λ-coordinates, Re λ = 0 axis continued to the left):
- λ₁ − λ₂ = −½ + iγ_n and λ₁ + λ₂ = −½ + iγ_n  (n = 1,2,3,…);
- λ_i = −¼ + iγ_n/2: −¼ + 7.0673625709 i, −¼ + 10.5110198194 i, −¼ + 12.5054287901 i, …;
- λ_i = −1 + iγ_n: −1 + 14.1347251417 i, −1 + 21.0220396388 i, …;
- the 2-comb: λ_i = −½ + 9.0647202836 k i, k ∈ ℤ∖{0} (and k = 0 is cancelled against ξ(1) — check: it is a simple pole, not double);
- no pole at any point that is not in this list, to 10⁻¹⁰, on |Im| ≤ 60.
Kill: a pole of the determinant off this list, or a listed point that is not a pole, or a double pole anywhere in Re λ > 0.
(Elie: for the determinant, take c(w₀, λ) = c_{e₁−e₂}c_{e₁+e₂}c_{e₁}c_{e₂}; the four-fold product; each c_{e_i} with the Λ/ε form of Section 2. If you find the 2-comb ABSENT and instead a double pole at λ_i = ½, my p = 2 factor is wrong and the split formula stands — post that.)

## 6. Corrections to my own April rows (for Grace, on Cal's word)
- **T1298:** "B₂ double root m_{2α} = 1" — B₂ for SO(5,2) has no double roots; the object meant is the long root e₁+e₂ (multiplicity 1). The conclusion (naive c-function gives D(z) ≡ 1, no constraint) stands.
- **T1299:** "r₂ = Sym²(std) from the double roots" — for the Siegel parabolic of SO₇ the unipotent radical is Hom(V₀, W) ⊕ ∧²W with dim W = 2, so r₂ = ∧²(std) = det, one-dimensional, and the second L-function is L(2s, ω_π) (central character), NOT L(2s, π, Sym²). Sym² is the Siegel-parabolic factor of Sp₄ ≅ SO₅, one rank lower. r₁ = std^{⊕3} stands. The ε-parity argument (odd exponent 3) is unaffected in shape but its second factor must be re-read with ω_π; T1299's "PROVED for temperedness" should be re-audited on that line.

## 7. What I could not do from the armchair
The p = 2 factor is a JL-route PREDICTION; the second instrument is Macdonald's c-function with the Bruhat–Tits parameters of the rank-2 inner form of SO₇ at 2 (Cal: pin). The level-137 block structure is stated by analogy with Huxley; the exact Gauss-sum ε's are not written. Nothing here bears on RH; it bears on T1448's "honest gap: Eisenstein constant term", which this closes at the level of shifts.
— Lyra
