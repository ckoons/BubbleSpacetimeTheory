# PRE-REGISTRATION — Toy 5694, E2 (T-ST): the Soundararajan–Thorne sign criterion on the cone-zeta, with a RIGOROUS tail

**Elie, 2026-09-06 (Sunday) 10:11 EDT (`date`-rendered; a first draft carried 10:24, a guessed time, corrected before hashing). Hashed before the instrument runs.**

## The theorem, pinned (Thorne, *Analytic properties of Shintani zeta functions*, RIMS Kôkyûroku 1715, Section 4.3, Theorem 4.1, attributed to Soundararajan–Thorne [28], "in preparation" as of that survey — publication status to be pinned by Keeper before any banking)
A(s) = Σ a(n)n^{−s}, real coefficients, abscissa of absolute convergence Re s = 1. If a completely multiplicative χ: ℕ → {±1} has Σ_n a(n)χ(n)n^{−σ} < 0 for some real σ > 1, and a(n₀)χ(n₀) > 0 at the first nonzero coefficient, then A(s) has infinitely many zeros outside the critical strip (the sketch places them near σ − it with Re s = σ > 1, i.e. BEYOND the abscissa — no functional equation used).

## The object
A(s) := Σ_{N≥1} b(N)N^{−s}, b(N) = Π_p α_p(N), α_p the plain local density (lim p^{−4k}#{x mod p^k : Q(x) ≡ N}) of Q = x₀² − x₁² − x₂² − x₃² − x₄². By K1862-A (verified blind in 5693), r*(N) = c·N^{3/2}·b(N), so Z_cone(s) = c·A(s − 3/2): zeros of A with Re s > 1 are zeros of Z_cone with Re s > 5/2, beyond its abscissa. b(N) is bounded above and below by positive constants, so A's abscissa is exactly 1; n₀ = 1, b(1) > 0, χ(1) = 1.

## Instrument (all mine; Keeper's K1862-C script NOT opened)
- Odd p: K1862-C Lemma 1 recursion (5693 verified it against convolution for p ≤ 7); here re-verified at p = 11, 13 for N ≤ 300.
- p = 2: the same singular/primitive split — α₂(N) = prim₂(N) + ⅛·α₂(N/4)·[4 | N] — with prim₂ read off exact convolution (bincount on supports, int64 exact) for N ≤ 1024 at k = e+3, stability at e+4.
- p ∤ 2N, p < P = 10⁵: Π(1 + (N/p)p⁻²) in log form. **Rigorous relative error** of the truncation: |Σ_{p>P} log(1 ± p⁻²)| ≤ 1.0001·Σ_{n>P} n⁻² < 1.0001/P.
- **Uniform bound** B_max := (sup α₂)·Π_{p odd}(1 − p⁻³)⁻¹·Π_{p odd}(1 + p⁻²) = (max_r prim₂(r))/(1 − ⅛) · (7/8)ζ(3) · (4/5)ζ(2)/ζ(4); every factor is a theorem of the recursions (e ≥ 2 factor ≤ 1 + p⁻³·sup, so sup ≤ 1/(1 − p⁻³)).
- **Tail:** Σ_{N>X} b(N)χ(N)N^{−σ} in absolute value ≤ B_max·X^{1−σ}/(σ − 1), X = 10⁶.
- χ: free signs on the 15 primes ≤ 47 (2¹⁵ patterns by a Walsh–Hadamard transform over the v_p-parity classes), times one of four rules on primes > 47: all +1, all −1, +1 iff p ≡ 1 (mod 4), −1 iff p ≡ 1 (mod 4). σ ∈ {1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.5, 1.6}.
- Decision quantity: T(σ,χ) = S_X(σ,χ) + (truncation error bound) + (float bound) + B_max·X^{1−σ}/(σ−1). **T < 0 for any (σ,χ) ⟹ the theorem's hypothesis is met.**

## Hashed lines
- **P1 (control, Keeper's numbers reproduced):** at N ≤ 20,000, σ = 1.1: Liouville partial sum = −0.082 ± 0.003; χ = (+1 on p ≡ 1 mod 4, −1 on p = 2 and p ≡ 3 mod 4): −0.370 ± 0.003; the latter at σ = 1.25: −0.012 ± 0.003.
- **P2 (2-adic structure, can fail):** prim₂(N) := α₂(N) − ⅛α₂(N/4)[4|N] is a function of N mod 8 alone, for every N ≤ 1024 (Hensel from k₀ = 3). If it needs mod 16 or 32 I use that modulus and say so; if no modulus ≤ 64 works, the instrument is not validated and nothing downstream is reported.
- **P3 (odd p, can fail):** Lemma 1 = convolution at p = 11, 13, all N ≤ 300, exactly.
- **P4 (THE DECISIVE LINE, can fail; my prior ≈ 50 %):** some (σ, χ) in the search has T(σ,χ) < 0 at X = 10⁶. If HIT: by Theorem 4.1, A(s) — hence Z_cone — has infinitely many zeros with Re s beyond the abscissa; the χ, σ, S_X, and the three error terms are published in full so anyone can re-add them. If MISS: no theorem (Thorne's ξ⁺ mode); I report the best margin and the X at which the tail bound would cross, as an estimate only.
- **P5 (bookkeeping):** B_max < 4; the Walsh–Hadamard minimum agrees with a direct evaluation of the same χ to 10⁻¹⁰.

Score X/5. P4 is the only line that matters to the row; P1–P3, P5 validate the instrument in both directions before P4 is read.
