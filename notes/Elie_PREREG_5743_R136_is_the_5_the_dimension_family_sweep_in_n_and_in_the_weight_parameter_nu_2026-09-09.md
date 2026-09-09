# PRE-REGISTRATION — Toy 5743, Round 136: is the 5 in c ~ 5n/(2j) the dimension? (K1885-PRE-A section 4, asked of me directly)

**Elie, 2026-09-09 (Wednesday) 10:05 EDT (shell-copied). Hashed before the run.**

Keeper asks for D_IV⁴ and D_IV⁶ before anyone writes "the dimension appears in the commitment law." **The D_IV sweep alone cannot answer it: for type IV the genus equals the dimension (the Bergman kernel exponent is −n, my own 5722 instrument), and the rank is 2 throughout. So I sweep a second axis — the weight parameter ν of the space — which separates them.**

Generalised weights (Faraut–Korányi, ν the weight parameter, a = n − 2, λ = (j+k, j)): a_ν(j,k) = j!(n/2)_{j+k} / [(ν)_{j+k}·(ν − (n−2)/2)_j], giving
  **L_ν(j,k) = [(k+n−2)/(2k+n−2)]·(j+k+n/2)/(j+k+ν),  M_ν(j,k) = [k/(2k+n−2)]·(j+1)/(j+ν−(n−2)/2).**

## Hashed lines
- **G1 (control):** at ν = n the recursion reproduces my 5724 family values for the matter word c(1,1) = 12/35, 3/8, 25/63, 33/80, 14/33 at n = 3..7, and Round 130's twelve rationals at n = 5.
- **G2 (control):** c₁(j,0) = n/(2(j+n)) exactly for n = 3..8 (my 5724 family line), and j·c_p(j,0) → p·n/2 for p = 1, 2, 3.
- **G3 (the discriminator, can fail): the exact k = 0 line at general ν is c₁(j,0) = (ν − n/2)/(j + ν).** So **the constant is ν − n/2, the gap between the space's weight parameter and the Wallach/Hardy point n/2 — not the dimension.** Two consequences hashed: at ν = n (Bergman) it equals n/2 and merely *looks* like the dimension; **at ν = n/2 (the Hardy space) the constant is 0 and the commitment cost vanishes identically**, which is the right answer because every word already has |z|² = 1 on Š. Verified at (n,ν) = (5,5), (5,4), (5,3), (5,5/2), (4,4), (6,6), (6,4).
- **G4 (independent instrument, can fail):** the kernel-Gram of 5722 with the kernel exponent −ν (a one-parameter generalisation of the same code) reproduces c₁ and c₂ at (n,ν) = (5,4) and (5,3) — so G3 is not an artefact of the Pochhammer algebra.
- **Verdict hashed:** the constant tracks NEITHER the dimension nor the genus nor the rank on its own; it is ν − n/2, and for the Bergman space of D_IV⁵ that is 5/2. **"The dimension appears in the commitment law" is a shared-integer reading and must not be written.**

Score X/4, G3 and G4 can fail.
