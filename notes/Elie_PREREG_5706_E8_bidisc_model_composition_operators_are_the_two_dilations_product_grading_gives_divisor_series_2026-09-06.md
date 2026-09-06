# PRE-REGISTRATION — Toy 5706, E8 (Round 120/121): the bidisc model of the linear-algebra face, on Lyra L2 Section 1

**Elie, 2026-09-06 (Sunday) 12:11 EDT (shell-copied). Hashed before the run. Built on L2 Section 1 (polydisc coordinates u, v; tube base uv = n, u = d, v = n/d), not on 5289.**

## Objects (exact, finite truncations)
H²(D²) with orthonormal monomials u^a v^b (a, b ≥ 0). The PRODUCT grading assigns u^a v^b the grade ab (the tube base uv = n). Composition operators C_p^{(1)}: f(u,v) ↦ f(u^p, v) and C_p^{(2)}: f(u,v) ↦ f(u, v^p). The graded map G: u^a v^b ↦ z^{ab} (for a, b ≥ 1). Dilation on the graded side D_p: z^n ↦ z^{pn}.

## Hashed lines (all exact, checked on the lattice a, b ≤ 200, grades n ≤ 200)
- **P1:** G(Σ_{a,b≥1} u^a v^b) = Σ_{n≥1} d(n) z^n exactly (coefficient by coefficient to n = 200); equivalently the Lambert form Σ_a z^a/(1 − z^a).
- **P2:** G ∘ C_p^{(1)} = D_p ∘ G and G ∘ C_p^{(2)} = D_p ∘ G on every monomial with a, b ≥ 1 (p = 2, 3, 5, 7): both composition operators realize the SAME dilation after grading, while as operators on H²(D²) they differ (C_2^{(1)}(uv²) = u²v² ≠ C_2^{(2)}(uv²) = uv⁴) — the "second copy of the line."
- **P3:** C_p^{(i)} are isometries of H²(D²) (orthonormal monomials to orthonormal monomials), and C_p^{(1)}C_q^{(1)} = C_{pq}^{(1)}, C_p^{(1)}C_q^{(2)} = C_q^{(2)}C_p^{(1)}, with G ∘ C_p^{(1)}C_q^{(2)} = D_{pq} ∘ G.
- **P4 (Lyra L3's weight):** the Szegő norm of the grade-n slice of the lattice sum, ||Σ_{ab=n} u^a v^b||², equals d(n) exactly for n ≤ 200 — the diagonal weight d(N) of L3.
- **P5 (what it is NOT):** the graded map G is not injective (u^2 v^3 and u^3 v^2 and u^1 v^6 all go to z^6), so no operator identity on H²(D²) is recovered from one on the graded side; the model realizes ζ² = Σ d(n) n^{−s} and the dilation semigroup, not the prime sum — stated as a line so it is not over-read.

Score X/5. Every line is a theorem of the construction (Cal's category); the toy's value is that the construction is now written down exactly, with its two copies of the dilation, for the L2/L3 discussion.
