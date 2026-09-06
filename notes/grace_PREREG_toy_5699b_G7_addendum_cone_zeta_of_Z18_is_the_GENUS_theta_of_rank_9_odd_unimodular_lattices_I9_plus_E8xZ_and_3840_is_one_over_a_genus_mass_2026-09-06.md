# Grace — toy 5699b addendum (G7). Post-hoc reading declared for N ≤ 12; PRE-REGISTERED (hashed before the run) for 13 ≤ N ≤ 20. Clock 11:3x EDT 2026-09-06.

## What 5699 found (P3 MISS at n = 8, the informative miss)
5699 P1/P2 HIT (the quaternion isometry; 2-adic densities equal to N = 200). P3: exact coefficient identity r*_n(N)·R(n) = r_{n+1}(N) held at n = 4, failed at n = 2, 6 as predicted, and FAILED at n = 8 (predicted to hold). At n = 8 the ratio R(8) = vol(S⁸)/vol(P⁸) came out **2786918400/17**, and
  17/2786918400 = 1/(2⁹·9!) + 1/(2·696729600) = 1/|O(I₉)| + 1/|O(E₈ ⊕ ℤ)| = mass of the genus of odd unimodular lattices of rank 9,
which has TWO classes (Kneser: I_m is one-class iff m ≤ 8). My P3 assumed the definite side was one-class at n = 8; it is not. Post-hoc reading, declared: for 4 | n the two forms are ℤ_p-isometric at every p (odd p: T2617; p = 2: oddity 1 − n ≡ n + 1 mod 8 iff 4 | n, and the quaternion construction block-wise), so Siegel–Weil gives
  **r*_n(N) = Σ_{L ∈ genus(I_{n+1})} r_L(N)/|O(L)|**  (the cone-zeta of ℤ^{1,n} is the UNNORMALISED GENUS THETA of the odd unimodular lattices of rank n + 1),
and R(n) = 1/mass(genus(I_{n+1})). At n = 4 the genus is {I₅} alone, so **3840 = |O(ℤ⁵)| is Siegel's mass formula, not an accident** — my 10:11 "n = 4 accident" wording is corrected: the |W(B_{n+1})| reading fails at n = 2, 6 because the 2-adic data differ there (R(n) is not a mass), and generalises correctly as 1/mass(genus) along 4 | n. Both sentences of the morning stand ("covolume ratio", "not a BST integer"); the name of the integer at n = 4 is |O(ℤ⁵)| by theorem.

## Pre-registered (can fail), 13 ≤ N ≤ 20, n = 8
**Q1.** r*_8(N) = r₉(N)/(2⁹·9!) + r_{E₈⊕ℤ}(N)/(2·|W(E₈)|) exactly, where r_{E₈⊕ℤ}(N) = Σ_{k∈ℤ} r_{E₈}(N − k²), r_{E₈}(0) = 1, r_{E₈}(m) = 240 σ₃(m). Kill: one N.
**Q2 (post-hoc check, N ≤ 12, same formula)** — declared, not blind.
**Q3.** The same genus formula at n = 4 reduces to r₅(N)/3840 (one class) — consistency, N ≤ 30.
Instrument: play/toy_5699b_*.py.
— Grace
