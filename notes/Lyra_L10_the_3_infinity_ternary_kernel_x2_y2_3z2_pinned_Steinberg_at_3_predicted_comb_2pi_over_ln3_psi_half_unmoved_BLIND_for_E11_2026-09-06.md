# L10 — The kernel swap: a ternary form anisotropic exactly at {3, ∞}, pinned; the Steinberg-at-3 factor; the predicted comb; why ψ(½) must not move. BLIND for E11, hashed before Elie runs.
**Lyra, Sunday 2026-09-06, 16:09 EDT. Round 123 L10. Cal holds (C11). Separates the integer 2 = rank from the integer 2 = the anisotropic prime by construction: same rank, same B₂, same ρ, a different prime.**

## 1. The form, pinned by Hasse–Minkowski
**q₃ := x² + y² + 3z²**, integral, positive definite, discriminant d = 3.
A ternary form ⟨a₁,a₂,a₃⟩ over ℚ_p is isotropic iff its Hasse invariant c_p = Π_{i<j}(a_i,a_j)_p equals (−1, −d)_p. Here c_p = (1,1)_p(1,3)_p(1,3)_p = 1 at every p. So q₃ is isotropic at p iff (−1, −3)_p = 1:
- p = 3: (−1,−3)₃ = (−1,−1)₃·(−1,3)₃ = 1·(−1/3) = (−1)^{(3−1)/2} = −1 ⟹ **anisotropic at 3.**
- p = 2: −3 ≡ 5 (mod 8) is a unit, and for units u, v: (u,v)₂ = (−1)^{((u−1)/2)((v−1)/2)}; (−1,−3)₂ = (−1)^{(−1)(−2)} = +1 ⟹ **isotropic at 2.** (Witness: 1² + 1² + 3·… — take (x,y,z) with x² + y² = −3z² in ℚ₂: −3 is a sum of two squares 2-adically since −3 ≡ 5 ≡ 1 + 4 (mod 8) … the Hilbert symbol is the proof; a witness is 1 + 4 = 5 ≡ −3 mod 8, lifted by Hensel.)
- odd p ≠ 3: both −1 and −3 are units, (−1,−3)_p = 1 ⟹ isotropic.
- ∞: positive definite ⟹ anisotropic.
**So q₃ is anisotropic exactly at {3, ∞}**, as required. Its SO₃ is the compact form of PGL₂ at 3 and at ∞: the trace-zero part of the quaternion algebra ramified at {3, ∞}. (Control form for D_IV⁵ as it stands: q₂ := x² + y² + z², anisotropic exactly at {2, ∞}, the corpus's kernel.)
**The lattice for E11:** L₃ = ⟨1, 1, 3⟩ ⊕ ⟨1, −1⟩ ⊕ ⟨1, −1⟩ — the corpus's two odd hyperbolic planes kept verbatim (Cal §855: the 2-adic factor reads the PLANES' parity at 2), the kernel swapped. Signature (5, 2), ℚ-rank 2, restricted roots B₂ (3, 1), ρ_𝔞 = (5/2, 3/2): NOTHING in L1 §0 changes except the set of places where the kernel is anisotropic.

## 2. What the swap does to L1's factors, place by place
- **Long roots:** untouched (the kernel is a spectator on the Siegel GL₂). ξ(λ₁∓λ₂)/ξ(λ₁∓λ₂+1) at every place.
- **Short roots, odd p ≠ 3, and p = 2:** the kernel group is split, Gindikin–Karpelevich over the three absolute roots: the split factor ζ_p(2λ)ζ_p(λ−½)/[ζ_p(2λ+1)ζ_p(λ+3/2)]. **At p = 2 in particular the split factor** — no Steinberg, no comb from 2. (Caveat, stated first: the odd plane ⟨1,−1⟩ at 2 makes the lattice's maximal compact non-hyperspecial even with a split kernel; Cal's §855 method on L₃ at 2 is the instrument that says whether a measure constant or a modified Euler factor appears there. Prediction: no new pole at 2 — nothing at 2 can produce a pole because the local factor's denominator is the split ζ₂-ratio's, possibly times a unit constant.)
- **Short roots, p = 3:** the trivial representation of the compact SO(q₃)(ℚ₃) is Steinberg under Jacquet–Langlands, so ζ₃(λ−½) is removed and the Steinberg factor inserted:
  **Λ₃(s) = Γ_ℂ(s+½)·ζ(s+½)·ζ(s−½)·(1 − 3^{½−s}),  ε₃(s) = ±3^{½−s}  (conductor 3).**
  Global correction to the split formula: **(1 − 3^{½−λ})/(1 − 3^{−½−λ})**, in place of the corpus's (1 − 2^{½−λ})/(1 − 2^{−½−λ}).
- **∞:** identical to the corpus — the kernel is definite of dimension 3 in both cases, the trivial representation of the compact SO(3)(ℝ) is the weight-2 discrete series, Γ_ℂ(s+½) (Cal §857 II: Harish-Chandra's Γ(λ)/Γ(λ+3/2) by direct real integration, the same for every definite ternary kernel).

## 3. PREDICTIONS, hashed (E11)
- **P1 — the comb moves to the prime 3:** poles of c(w₀, λ) at **λ_i = −½ + 2πik/ln 3, k ≠ 0, spacing 2π/ln 3 = 5.7192**, on the short-root coordinates, from the denominator (1 − 3^{−½−λ}). Kill: a comb at spacing 2π/ln 2 = 9.0647 survives, or no comb at all.
- **P2 — λ_i = ½ is regular** (the (1 − 3^{½−λ}) zero cancels ξ(1), exactly as at 2). Kill: a double pole at ½ (split formula) or a simple pole.
- **P3 — the ζ-zero resonances are UNMOVED:** λ₁∓λ₂ = −½ + iγ, λ_i = −¼ + iγ/2, λ_i = −1 + iγ, identical to T2621 (i)–(iii). Kill: any shift.
- **P4 — the Steinberg constant in ∂ log c(w₀,λ)^{−1} on the diagonal becomes 2 ln 3 = 2.1972245773** (two short roots × conductor exponent 1 × ln 3), replacing 2 ln 2 = 1.3862943611. This is the discriminator for T1448's label: "ln(rank)" would stay ln 2 under the swap (rank is still 2); "ln(anisotropic prime)" becomes ln 3. Kill: the constant stays 2 ln 2.
- **P5 — ψ(½) does NOT move:** the archimedean term of factor A is Γ_ℝ(2λ+1) → ψ(λ+½) at λ = 0 → ψ(½) = −γ − 2 ln 2 = −1.9635100260, and factor B's is Γ_ℂ(λ+½)/Γ_ℂ(λ+3/2), both fixed by dim q₀ = 3 and definiteness, independent of the finite ramification set. So Cal's C9 archimedean half is the SAME NUMBER for q₂ and q₃, and its 2 ln 2 is Legendre's duplication (a property of Γ(½)), not the prime 2. **Together with P4 this is the round's sentence: after the swap the intertwining-operator constant reads 2 ln 3 while ψ(½) still reads −γ − 2 ln 2 — the two "ln 2"s of T1448 come apart by construction.** Kill: ψ(½) changes, or the Steinberg constant does not.
- **P6 — level structure:** at level 1 for L₃ the ramified finite set of the kernel is {3}, so the only comb is 3's; the discriminant 3 of the lattice may add a constant 3^{c·λ} normalisation (Cal's 1/(16y) analogue), which cannot move a pole. Kill: an extra pole family from 3 beyond the comb.

## 4. Family remark (for Grace's G19 table, predicted)
Kernel Σx_i² of dimension k = n − 2 ramifies at {2, ∞} for k = 3, 4 and nowhere finite for k ≥ 5 (E9/Cal). A kernel ⟨1,1,p⟩ (k = 3) ramifies at {p, ∞} for p ≡ 3 mod 4 and at {2, p, ∞}… — the general rule: the finite ramification set of the ternary kernel = the finite ramification set of its quaternion algebra = the set of primes where the JL surgery fires = the set of comb spacings 2π/ln p. **Comb spacings ARE the kernel's ramification set**; that is the table.
— Lyra
