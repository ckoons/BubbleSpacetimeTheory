# Grace — PRE-REGISTRATION, toy 5699 (G7, Round 120; written and hashed BEFORE the run; clock 11:2x EDT 2026-09-06)

**Question (Keeper G7).** Why is r*(N)·3840 = r₅(N) EXACT for every N (Elie 5695a, N ≤ 200)? Claim to pin: ℤ^{1,4} ⊗ ℤ₂ ≅ ℤ⁵ ⊗ ℤ₂, so that every local density of the two genera agrees (odd p: K1862-C Lemma 1 / T2617; p = 2: this isometry), both genera are one-class, and the only difference is the archimedean factor, the covolume ratio 3840 (toy 5698).

## The one line (the reason, stated before the computation)
Over ℤ₂, −1 is a sum of four squares (7 = 4 + 1 + 1 + 1 and Hensel), so there is a 2-adic integer quaternion q with N(q) = q q̄ = −1. Left multiplication L_q on ℤ₂⁴ (Hamilton coordinates) satisfies |L_q x|² = N(q)|x|² = −|x|² and det L_q = N(q)² = 1, so **L_q is a ℤ₂-isometry ⟨1,1,1,1⟩ → ⟨−1,−1,−1,−1⟩**, and A = diag(1, L_q) is a ℤ₂-isometry I₅ → ⟨1,−1,−1,−1,−1⟩. (Invariant check: rank 5, det 1 in both, oddity 5 ≡ 1 + 4·7 mod 8 in both — Conway–Sloane's 2-adic symbol for an odd unimodular lattice is determined by rank, det square class and oddity, so the isometry is forced; the quaternion exhibits it.)

## Predictions (can fail)
**P1 (exhibit).** Hensel-lift q = (a, b, c, d) ∈ ℤ⁴ with a² + b² + c² + d² ≡ −1 (mod 2^K), K = 40; then A = diag(1, L_q) satisfies Aᵀ·diag(1,−1,−1,−1,−1)·A ≡ I₅ (mod 2^K) with det A odd. Kill: no lift, or a residue.
**P2 (2-adic densities equal).** α₂(N) computed by convolution (mod 2^{v₂(N)+4}, stability at +1) for ⟨1,−1,−1,−1,−1⟩ and for I₅ agree for every N ≤ 200. Kill: one N.
**P3 (the family rule — the can-fail half).** For ℤ^{1,n} vs ℤ^{n+1}: det square classes agree iff n is even; oddities 1 − n and n + 1 agree mod 8 iff 4 | n. So the EXACT coefficient identity r*_n(N)·R(n) = r_{n+1}(N) (R(n) = vol(Sⁿ)/vol(Pⁿ) from toy 5698) holds for all N when n ∈ {4, 8} and FAILS at some N ≤ 30 when n ∈ {2, 6} (where toy 5698 already showed constancy only AFTER dividing out the 2-adic densities). At n = 8 the chamber is Vinberg's simplex for ℤ^{1,8} (same three constraints; the E₈ parabolic 696 729 600 appears) and R(8) is computed by Chiswell as before. Kill: n = 2 or 6 exact, or n = 4 or 8 not.
**P4 (where the failure sits).** At n = 2 and 6 the ratio r_{n+1}(N)/(r*_n(N)·R(n)) is a function of the 2-adic class of N only (N mod 8 and v₂(N)), not of the odd part. Kill: two N in the same 2-adic class with different ratios.

## What a failure means
P1/P2 fail → the exactness is not genus-theoretic and 5695a's identity needs a different reason. P3 fails at n = 4 or 8 → my R(n) or chamber is wrong there. P3 exact at n = 2 or 6 → the oddity invariant is not the obstruction I think it is; report the 2-adic symbol properly.

Instrument: play/toy_5699_*.py (imports the 5697/5698 machinery; exact integers throughout; Hensel lift by hand).
— Grace
