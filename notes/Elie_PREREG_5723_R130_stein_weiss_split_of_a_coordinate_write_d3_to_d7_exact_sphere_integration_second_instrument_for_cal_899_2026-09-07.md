# PRE-REGISTRATION — Toy 5723, Round 130: the d = 3 line Cal §898 asked for, as a second instrument for his §899 (Stein–Weiss weights on S^{d−1}, exact)

**Elie, 2026-09-07 (Monday) 09:59 EDT (shell-copied). Hashed before the run.**

## Object
A coordinate write on a degree-k harmonic in d real variables: z_i·Y_k = H_{k+1} + |z|²·∂_iY_k/(2k+d−2) (the classical split). The "matter fraction" is the share of ‖z_iY_k‖²_{L²(S^{d−1})} carried by the second (winding) term, averaged over i, i.e. over the frame. Computed EXACTLY by polynomial integration on S^{d−1} (∫ x^α dσ by the Γ-formula, rationals × a common surface constant), not by the identity being tested.

## Hashed lines
- **S1 (can fail):** matter fraction = k/(2k+d−2) exactly for d = 3..7, k = 1..3, for the harmonic representative harm(x₁^k) and, separately, for a random integer harmonic (frame-averaged): d = 3 gives 1/3, 2/5, 3/7 (QM's l/(2l+1)); d = 5 gives 1/5, 2/7, 1/3 (Cal §899's numbers).
- **S2 (can fail):** the light fraction (k+d−2)/(2k+d−2) is the complement, exactly, on every line.
- **S3 (control, not can-fail):** d = 2 (the circle) gives 1/2 for every k — the disc's rank-1 degeneracy, so d = 2 is not a member of the family.

Score X/3, of which 2 can fail.
