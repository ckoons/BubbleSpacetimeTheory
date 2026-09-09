# PRE-REGISTRATION — Toys 5748 (E1) and 5749 (E2), Round 139. Hashed before either runs.

**Elie, 2026-09-09 (Wednesday) 11:42 EDT (shell-copied).** Criteria read from the registry block at lines 7666–7720 (T2406/T2407). The Independence Test: side A must be computable from Cartan/root data with no BST integer as input.

Root data used (classical, no BST input): genus p = (r−1)a + b + 2. **I_{p,q}: dim pq, rank min(p,q), genus p+q. II_n: dim n(n−1)/2, rank ⌊n/2⌋, genus 2n−2. III_n: dim n(n+1)/2, rank n, genus n+1. IV_n: dim n, rank 2, genus n. V: dim 16, rank 2, genus 12. VI: dim 27, rank 3, genus 18.**

## E1 — Toy 5748: the independence test on C4, C5, C7
- **C4 as written** ("g = 7 → M_g = 2⁷ − 1 = 127 is a Mersenne prime"): g is a BST integer, so the expression contains no domain. **Hashed: the verdict is TRUE for every candidate domain, identically — the criterion discriminates nothing as written.**
- **C4 honestly** (side A = 2^genus − 1 prime, genus from root data): **D_IV⁵ has genus 5 and 2⁵ − 1 = 31, which IS prime, so D_IV⁵ still passes on the honest reading; D_I_{1,5} has genus 6 and 63 = 9·7, so it still fails.** But the criterion is then weak, not unique: **hashed, at least eight domains with dim ≤ 12 pass** (any domain whose genus is a Mersenne exponent: 2, 3, 5, 7, …).
- **C5** ("five BST primary integers forced by structure"): **hashed — no independent side A exists.** The criterion's side A is the theory's own conclusion; it cannot be computed from root data without importing the integers it is meant to force. Reported as EMPTY, not as failed.
- **C7** ("c_FK = (N_c·n_C)²/π^((g+rank)/rank) reproduces the classical Faraut–Korányi volume"): the exponent (g+rank)/rank = 9/2 is built from g. **Side A, computed with no BST input: the classical Euclidean volume of the Lie ball is Vol(D_IV^n) = π^n/(2^{n−1} n!)**, verified analytically at n = 1 (the disc, π) and n = 2 (the bidisc under the Cartan map, π²/4) and by Monte Carlo at n = 5. **So the power of π the volume actually requires is n = 5, the complex dimension — a domain invariant — and not 9/2.** Numerically: Vol(D_IV⁵) = π⁵/1920 = **0.159386**, while the row's expression gives 225/π^{4.5} = **1.3021**, a factor **8.17** apart. **C7 fails the independence test on its exponent and does not reproduce the volume numerically either.**

## E2 — Toy 5749: C3 re-run as a selection, side A = the true genus/rank
Sweep every Hermitian symmetric domain with rank ≤ 3 and dim_ℂ ≤ 12.
- **Hashed: genus/rank = 5/2 is achieved by TWO domains — D_IV⁵ (dim 5) and D_I_{2,3} (dim 6, genus 5, rank 2).**
- **Hashed: genus/rank = 7/2 is achieved by TWO domains — D_IV⁷ (dim 7) and D_I_{2,5} (dim 10, genus 7, rank 2).**
- **Verdict hashed: with the row's target 7/2, D_IV⁵ is EXCLUDED and two other domains are admitted; with the honest target 5/2, D_IV⁵ is admitted together with D_I_{2,3}. Under neither target does C3 uniquely select anything.** That is stronger than "it selects n = 7": the criterion has no discriminating power at rank 2 in either reading.
- The row's own competitor column used the true type I genus ((p+q)/min(p,q)) while its D_IV row used (n+2)/2 = (n_C + rank)/rank — the theory's g. **Two kinds of object across two domains, which is Cal's finding, and my sweep prices it.**
- **Refusal carried:** this is a fact about one broken criterion. It is not a proposal to change domains and I do not make one.

Score E1 X/4, E2 X/3; C4-as-written, C4-honest, C7 and both E2 lines can fail.
