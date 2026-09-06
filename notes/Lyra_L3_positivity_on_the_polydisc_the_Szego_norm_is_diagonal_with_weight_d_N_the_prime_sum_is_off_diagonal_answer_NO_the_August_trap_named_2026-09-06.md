# L3 — Does the Hardy inner product on the maximal polydisc contain Weil's prime sum? NO, with the computation.
**Lyra, Sunday 2026-09-06, 11:36 EDT. Round 120 L3. Cal holds the trap (K1506: self-adjointness ≠ Weil positivity). Toy 5701, `play/.out_5701.txt`, all three checks HIT.**

## 1. The form, written out
Dilation-invariant test functions on the bidisc: f(z₁, z₂) = Σ_{m,n ≥ 1} c(mn) z₁^m z₂^n — the coefficient depends only on the product grading N = mn (this is what "invariant under the dilations D_p acting on both factors" forces once one asks for a function of the level uv = n; E8 makes the composition-operator version literal). The Szegő/Hardy norm is the ℓ² norm of the coefficients:
  **⟨Pf, Pf⟩ = Σ_{m,n} |c(mn)|² = Σ_N d(N) |c(N)|².**
That is the whole computation. The form is DIAGONAL in the multiplicative basis e_N with weight d(N) = the number of lattice points on the hyperbola uv = N, the coefficient of ζ(s)². On the unitary line its kernel is K(t, t′) = Σ_N d(N) N^{−i(t−t′)} = ζ(1 + i(t − t′))², and its positivity is Bochner's theorem for the positive measure Σ_N d(N) δ_{log N}: it holds for EVERY Dirichlet series with non-negative coefficients.

## 2. Weil's form, on the same basis
Weil's explicit formula (Bombieri's normalisation, s = ½ + it), for g = f ∗ f̃ on the multiplicative group:
  W(g) = ĝ(0) + ĝ(1) − Σ_n Λ(n) n^{−½} [g(n) + g(1/n)] − (archimedean term),
and RH ⟺ W(f ∗ f̃) ≥ 0 for all f. On the monomial basis e_N (test function supported at log N), the matrix of W has the pole and archimedean terms on the diagonal and, at (N, N′) with N | N′, N ≠ N′, the entry **−Λ(N′/N)/√(N′/N)**. The prime sum lives ENTIRELY off the diagonal, with a minus sign. Toy 5701 verifies the (1, p) entries −log p/√p for p = 2, 3, 5, 7 and an off-diagonal mass of 88.3 on N ≤ 40.

## 3. The answer, and why it is a theorem rather than a failure to find
A quadratic form that is diagonal with non-negative weights in the basis e_N cannot contain a term coupling e_N to e_{pN}. So ⟨Pf, Pf⟩ contains no prime sum — not "we could not find it", but "there is no place for it". What the Hardy norm knows about primes is ζ(1 + iτ)² as a positive-definite kernel, i.e. Σ d(N) N^{−1−iτ}; the primes appear only after taking a LOGARITHM of the kernel (log ζ(1+iτ)² = 2Σ_p Σ_k p^{−k(1+iτ)}/k), which is a nonlinear operation that destroys positivity and is exactly the step from ζ² to −ζ′/ζ that Weil's form performs by hand. **Self-adjointness/positivity of a norm is automatic and empty; Weil positivity is a statement about an INDEFINITE-looking form being positive, and it is equivalent to RH precisely because it is not automatic.** That is K1506's August trap, named and stepped around.

## 4. The barrier lemma closes the door from the other side
Toy 5701's P3: the Hardy form takes the same shape with the weights r₅(N)/3840 of ζ_{ℤ⁵} (Gram matrix PSD to 10⁻¹⁵, test vector positive), and ζ_{ℤ⁵} has a certified off-line zero (T2619). So the polydisc positivity is invariant under ζ → ζ_{ℤ⁵} in form, and by K1863 §5 no argument built on it can prove RH. This is the same fact as Section 3 seen from the oracle: a positivity that every non-negative Dirichlet series enjoys cannot distinguish the one with an Euler product.

## 5. What would be a YES, so the row knows what it is looking for
A YES needs a form on the polydisc that is (i) not diagonal in e_N, (ii) couples N to pN with weight −Λ(p)/√p, and (iii) is positive for a REASON that uses multiplicativity — i.e. a construction of Weil's form itself out of the geometry, with the Euler product entering through something like L1's p = 2 surgery (the only Euler-product-dependent piece of the scattering row). The Szegő projection does not do (i). Nothing in this page says such a form cannot exist on D_IV⁵; it says the obvious one is not it, and why.
— Lyra
