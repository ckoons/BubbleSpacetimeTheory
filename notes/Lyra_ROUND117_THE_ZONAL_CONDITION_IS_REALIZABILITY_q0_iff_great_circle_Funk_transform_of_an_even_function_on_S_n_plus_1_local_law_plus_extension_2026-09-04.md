# Round 117 §3 — THE ZONAL CONDITION ON Qⁿ: (b) REALIZABILITY, decided, not fit
**Lyra. Friday 2026-09-04, 08:21 EDT (from `date`, rendered before this line). Written BEFORE Grace's family sweep (tables hashed 4c96d09d) and before Cal's pre-score, as the wake prompt ordered.**

Convention pinned to the source: `BST_EffectiveSpectralDimension.md` §"Precise statement" — the zonal sector of Q⁵ is the q = 0 sector of the SO(7) representations with highest weight (p, q, 0), p ≥ q ≥ 0; the eigenvalue on (p,0,0) is p(p+5). Generalized: Qⁿ = SO(n+2)/(SO(n)×SO(2)), highest weight (p, q, 0, …, 0), λ(p,0,…) = p(p+n).

## 0. Answer first
**(b). The zonal sector is exactly the range of the great-circle Funk transform from the sphere S^{n+1}.** A function F on Qⁿ has only q = 0 components ⟺ F = Rf for an EVEN function f on S^{n+1}, where

  (Rf)(P) = ∫_{P ∩ S^{n+1}} f  (integral of f around the great circle cut by the oriented 2-plane P)

along the incidence correspondence S^{n+1} ← T¹S^{n+1} → Qⁿ = Gr₂⁺(ℝ^{n+2}) ("a point and a unit vector orthogonal to it" ↦ the plane they span). That is a **local law** (the value at P is the circle-sum of one underlying sphere function) plus a **global extension** (defined for every P by the same rule) — the tower's kind of condition (T2613). It is **not (a)**: the zonal sector is not the invariants of any subgroup H ⊃ K of SO(n+2), because SO(n)×SO(2) fixes no vector of ℝ^{n+2} and so lies in no conjugate of SO(n+1); and functions on G/H for any other H ⊃ K have a different spectrum. (c) is excluded by (b).

Equivalently, in the local-law form: the zonal sector is the L² kernel of ONE invariant differential operator on Qⁿ (Section 3). "Committed = zonal" therefore reads **"committed = the value at every plane is the circle-integral of a single even field on S^{n+1}"** — a written existence statement, the second record space is L²_even(S^{n+1}), its floor is the incidence correspondence, its local law is the circle integral.

## 1. What is proved here (my derivation; standard ingredients cited)
**Lemma 1 (parity — a correction to the ESD note's count).** The representation (p,0,…,0) of SO(n+2) contains an SO(n)×SO(2)-fixed vector iff p is EVEN, and then exactly one. *Proof.* (p,0,…,0) = harmonic polynomials of degree p on ℝ^{n+2} = ℝⁿ ⊕ ℝ². A K-invariant polynomial is a polynomial in s = |u|², t = |v|², so p = 2k; the invariant polynomials of degree 2k form a (k+1)-space, the Laplacian (4s∂²_s + 2n∂_s + 4t∂²_t + 4∂_t on f(s,t)) maps it onto the k-space of degree 2k−2, so the harmonic invariants have dimension exactly 1. ∎ (Control: `play/lyra_zonal_controls_parity_constant_funk_2026-09-04.py`, n = 3…7, p = 0…7: [1,0,1,0,1,0,1,0] every row.) **Consequence:** the zonal sector is ⊕_{p even} (p,0,…,0); the ESD note's constant N₀(λ) ~ λ³/360 counts odd p too and should read **λ³/720** (numerical: λ³/N_even → 699, 709, 715 at P = 200, 400, 800, converging to 720 from below). The EXPONENT — d_eff^{zonal} = n+1 = 6 — is untouched; nothing tiered changes. Keeper's two-line theorem stands with the constant halved.

**Lemma 2 (equivariance + multiplicity one).** R commutes with SO(n+2). L²(S^{n+1}) = ⊕_p (p,0,…,0), multiplicity one (SO(n+1)-spherical); L²(Qⁿ) = ⊕ (p,q,0,…) multiplicity one (symmetric space). By Schur, R restricted to the degree-p harmonics is either 0 or c_p·(the unique isomorphism onto the (p,0,…) component of L²(Qⁿ)), and R has no component in any (p,q), q > 0, since none occurs on the sphere.

**Lemma 3 (the scalars).** c_p = 0 for p odd (the circle contains x and −x; odd harmonics integrate to zero). For p even, evaluate on the zonal harmonic Z_p(x) = C_p^{(n/2)}(x·e)/C_p^{(n/2)}(1) at a plane P ∋ e: c_p = ∫₀^{2π} C_p^{(n/2)}(cos θ) dθ / C_p^{(n/2)}(1) = 2π · [(n/2)_k / k!]² / C_{2k}^{(n/2)}(1) > 0 (p = 2k), because every Fourier-cosine coefficient of a Gegenbauer polynomial with index n/2 > 0 is positive. (Control, same file: c_p/π at n = 5: 2, 0, 5/6, 0, 35/64, 0, 105/256; at n = 3: 2, 0, 3/4, 0, 15/32, 0, 175/512.)

**Theorem (Zonal = Funk-realizable).** R: L²_even(S^{n+1}) → L²(Qⁿ) is injective with dense image equal to the closure of the zonal sector; on finite sums of harmonics it is a bijection onto the zonal sector. *Proof.* Lemmas 1–3. ∎ Corroboration (to be pinned to the page, not quoted from memory): Helgason, *Groups and Geometric Analysis* / *Integral Geometry and Radon Transforms* — the totally-geodesic Radon transform on the sphere is injective on even functions; Grinberg 1985 and Gonzalez 1987 give the range on Grassmannians by invariant differential equations.

**Corollary (spectral dimension is the sphere's).** R intertwines the two Casimirs, and the eigenvalue of (p,0,…) is p(p+n) on both spaces, so N_zonal(λ) = N_{S^{n+1},even}(λ) and d_eff^{zonal} = dim S^{n+1} = n+1, d_eff^{full} = dim_ℝ Qⁿ = 2n. **Ratio (n+1)/(2n) = dim S^{n+1}/dim_ℝ Qⁿ** — Casey's "spectral over real" is "sphere over quadric"; at n = 5 it is 6/10 = 3/5 and the 6 is dim S⁶. Same first row as Keeper's two lines: 2/3, 5/8, 3/5, 7/12, 4/7 — Grace's run decides.

## 2. What it does and does not settle (rubric)
Settles: the OBJECT in posit 2. "Zonal" is now a geometric condition with a local law and a floor — an existence claim written, not assumed. Does NOT settle: WHY committed states should be the Funk-realizable ones (posit 2's physics), nor posit 3 (the 1/π). The 3/5 remains Step 1: a theorem about Q⁵'s spectral geometry, not N_c/n_C (Cal's neighbour (n−2)/n meets it only at n = 5).

## 3. The local-law form (derived; two checkpoints named for Cal)
D(Qⁿ) is generated by Δ and one fourth-order operator D₄ (rank 2). Joint eigenvalues on (p,q,0,…) are W-invariant polynomials in x = λ + ρ (Harish-Chandra). From the Casimir, λ(p,q) = p(p+n) + q(q+n−2) = x₁² + x₂² − |ρ|² with x₁ = p + n/2, x₂ = q + (n−2)/2, so the q = 0 sector is the coordinate line x₂ = ρ₂ = (n−2)/2. With W of type B₂ (n ≥ 3) the invariants are generated by x₁² + x₂² and x₁²x₂², so on x₂ = ρ₂ the D₄-eigenvalue is a polynomial P(Δ-eigenvalue), and **D := D₄ − P(Δ) has ker D ∩ L²(Qⁿ) = the zonal sector exactly** (the only other solution line x₂ = −ρ₂ is non-dominant). Checkpoints: (i) the restricted Weyl group of Qⁿ is B₂ for n ≥ 3 (A₁×A₁ at n = 2, where the argument is easier); (ii) the coordinates (x₁,x₂) above are Harish-Chandra's up to W. Both standard; both to be read off the page, not asserted.

## 4. Hashed for Elie (before any run; toy number from the claim file)
Prediction, Qⁿ for n = 3…7, all p ≤ 12: the SO(n)×SO(2)-fixed subspace of the SO(n+2)-irrep (p,0,…,0) has dimension 1 for p even, 0 for p odd (branching computation independent of my polynomial argument — e.g. weight multiplicities or the SO(n+2) ↓ SO(n)×SO(2) rule). Second: for n = 5, Σ_{p ≤ P} dim(p,0,0) over even p only, divided by (P(P+5))³, tends to 1/720. Third: the Funk scalars c_p/π at n = 5, p = 0,2,4,6 are 2, 5/6, 35/64, 105/256 by direct numerical integration of the great-circle integral of the zonal harmonic on S⁶. Any miss kills Lemma 1, the constant, or Lemma 3 respectively.

## 5. Errors and scope
Mine to own if wrong: the B₂ checkpoint in §3. Scope: n ≥ 3 (rank 2); n = 5 is the theory's case. Nothing here touches the Šilov record (K1858: no local law there) — Qⁿ is the compact dual, its function space is a DIFFERENT space, and that is the point: the second record space exists on Qⁿ, not on Š.

— Lyra
