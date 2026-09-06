# PRE-REGISTRATION — Toy 5705, E9 (Round 121): the family rule for the 2-comb, D_IV^n, n = 3…8

**Elie, 2026-09-06 (Sunday) 12:05 EDT (`date` read in its own call, then copied; a draft carried 12:10). Hashed before the run. Keeper's K1864 G prediction is the hypothesis; my discriminant line sharpens his "even n".**

## Objects
For D_IV^n the anisotropic kernel of the minimal ℚ-parabolic is the positive-definite form q₀ = x₁² + … + x_m², m = n − 2 (Lyra L1: n = 5 gives m = 3). The 2-comb in the short-root factor comes from the Jacquet–Langlands modification at the places where q₀ is anisotropic (Steinberg at 2, discrete series at ∞); ∞ is always anisotropic (definite). So the comb is present iff q₀ is anisotropic over ℚ₂.
Instrument: q₀ is isotropic over ℚ₂ iff it has a primitive zero mod 2^k for every k (Hensel from k = 3 for these forms); computed by exhaustive search of primitive solutions of Σx_i² ≡ 0 mod 2^k, k = 3…7, for m = 1…7 — a finite count, no theory assumed. Discriminant character: for even m the kernel's quasi-split form is decided by the discriminant field ℚ(√((−1)^{m/2}·disc q₀)) = ℚ(√((−1)^{m/2})): nontrivial (χ₋₄) iff m ≡ 2 (mod 4); trivial iff m ≡ 0 (mod 4); no character for odd m.

## Hashed lines
- **P1 (anisotropy at 2 by count):** primitive zeros mod 2^k exist for all k ≤ 7 iff m ≥ 5; for m ≤ 4 there is none already at k = 3 (mod 8). So the comb is PRESENT for n = 3, 4, 5, 6 and ABSENT for n = 7, 8 — Keeper's prediction, as a count.
- **P2 (the character, sharpened):** m = 2 (n = 4): χ₋₄; m = 4 (n = 6): trivial (disc = 1, (−1)² = 1); m = 6 (n = 8): χ₋₄; odd m: none. Keeper's "quadratic character only for even n" is right on the parity and coarse on n = 6, where the even kernel carries NO character (its discriminant field is ℚ). Kill for Keeper's line: a character at n = 5 (none by P2). Kill for mine: n = 6 nontrivial — decided by the discriminant, exhibited.
- **P3 (the n = 5 control):** m = 3: no primitive zero mod 8 (three odd squares sum to 3 mod 8, two odd + one even to 2 or 6, one odd + two even to 1 or 5), so the comb at n = 5 is forced — the same fact Lyra used, now as a count.
- **P4 (Hasse–Minkowski cross-check):** the mod-2^k verdict agrees with the Hilbert-symbol criterion for anisotropy of Σ_{i≤m} x_i² over ℚ₂ (m ≤ 4 anisotropic; m ≥ 5 isotropic — every form in ≥ 5 variables over ℚ_p is isotropic).

Score X/4.
