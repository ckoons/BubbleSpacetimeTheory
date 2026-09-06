# PRE-REGISTRATION — Toy 5695, E3 (T-DH): the normalization stated first, then the zero hunt

**Elie, 2026-09-06 (Sunday) 10:26 EDT (`date`-rendered; a draft carried 10:50, a guessed time, corrected before hashing). Hashed before the instrument runs.**

## What 5695a found (post-hoc, now the hypothesis under test)
For N ≤ 60, exactly: **r*(N) = r₅(N)/3840**, r₅ = coefficient of θ⁵ (sums of five squares), 3840 = 2⁵·5! = |O(I₅,ℤ)|. Reason (to be checked, not assumed): ⟨1,−1,−1,−1,−1⟩ and ⟨1,1,1,1,1⟩ are ℤ_p-isometric at every p (odd p: Lemma 1; p = 2: same rank, det, Hasse invariant), both genera are one-class, so Siegel gives identical local products and the constants differ by the vector-count/orbit-count factor |O(I₅,ℤ)|. Hence **Z_cone(s) = Z_{ℤ⁵}(s)/3840**, the Epstein zeta function of the cubic lattice ℤ⁵, and Keeper's 3840 is answered (Grace G2).

## The object and its functional equation (Epstein, classical)
Z₅(s) := Σ_{N≥1} r₅(N)N^{−s}, abscissa 5/2. Λ(s) := π^{−s}Γ(s)Z₅(s) = Λ(5/2 − s), entire except simple poles at s = 0 and s = 5/2; symmetry line Re s = 5/4 (Keeper's line). Approximate functional equation, from θ⁵(i/y) = y^{5/2}θ⁵(iy):
Λ(s) = Σ_N r₅(N)[(πN)^{−s}Γ(s, πN) + (πN)^{s−5/2}Γ(5/2−s, πN)] − 1/s − 1/(5/2 − s).

## Hashed lines
- **P1 (identity, can fail):** r*(N)·3840 = r₅(N) for every N ≤ 200 (chamber enumeration + BFS stabilizers as in 5693; r₅ by convolution). One failure kills the identification.
- **P2 (instrument):** the AFE reproduces the direct sum π^{−s}Γ(s)Σr₅(N)N^{−s} at s = 3.5, 4+2i to 10⁻²⁵ (mpmath, 40 dps), and Λ(s) − Λ(5/2−s) = 0 to 10⁻²⁵ at ten random s in the strip.
- **P3 (count):** N_total(T) := number of zeros of Λ in the rectangle −1/2 ≤ Re s ≤ 3, 0 < Im s ≤ T by the argument principle (winding number of Λ minus the poles), for T = 50 and T = 100; compared with the Riemann–von Mangoldt-type count (T/π)log(T/(2πe)) + O(log T) as a sanity check (must agree to within a few units).
- **P4 (THE DECISIVE LINE, can fail; my prior: off-line zeros EXIST, ≈ 75 %, Davenport–Heilbronn for Epstein zetas of n ≥ 2 variables without Euler product):** N_line(T) := number of sign changes of the real function Λ(5/4 + it) on 0 < t ≤ T. If N_total(T) > N_line(T) at T = 100, off-line zeros exist; I then locate at least one by bisection of rectangles + Newton (mpmath findroot) and report it to 15 digits with its winding-number certificate on a small rectangle. If N_total = N_line at T = 100, no off-line zero below height 100 (no theorem either way).
- **P5 (literature control, after the run):** the located zero(s) checked against any published table of zeros of Z_{ℤ⁵} if one exists; otherwise reported as new numerics.

Score X/5. If P4 HITS, Z_cone violates its RH numerically — the "cone beats Davenport–Heilbronn" reading (F1014) is dead by exhibited obstruction, not by default.
