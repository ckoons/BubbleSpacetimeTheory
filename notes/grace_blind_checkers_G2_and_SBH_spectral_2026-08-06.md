# Grace — two BLIND checker's-halves, posted before Elie's numbers land (2026-08-06, K1239)

**Discipline: "commit the checker's half blind" — post the pass/fail criterion BEFORE the computed number arrives, so a match cannot be retrofitted. Two lanes armed and waiting on Elie's fires.**

## Checker 1 — CFS Gate G2 (Elie firing 5089): spacelike ties = equal-|λ| pairs
Mode energy E(a,b) = a(a+3) + b(b+1); ρ=(3/2,1/2). Dominance order = componentwise. A **spacelike tie** = an *incomparable* pair sharing energy (simultaneity); a **timelike** pair = comparable (must split).

**PRE-REGISTERED PASS CRITERION:** the local correlation operator F(x) has eigenvalues **equal in magnitude on EXACTLY the incomparable equal-energy pairs**, and **split (unequal |λ|) on every comparable pair.** Concrete test set (first four ties):

| E | spacelike tie (equal \|λ\|) |
|---|---|
| 6 | (0,2) ~ (1,1) |
| 10 | (1,2) ~ (2,0) |
| 12 | (0,3) ~ (2,1) |
| 16 | (1,3) ~ (2,2) |

- **PASS** = equal-|λ| on all four ties AND splits on comparable pairs.
- **FAIL** = any comparable pair shows equal |λ|, or any listed tie splits.

### ★ E=30 — CORRECTED (self-catch 2026-08-06, K1250) + sharpened to the accidental-overlap test
**Self-catch:** my earlier "three-way {(2,4),(3,3),(4,1)}" was WRONG — a range(5) cutoff dropped **(0,5)** (E(0,5)=30). The real E=30 set is **FOUR modes: {(0,5),(2,4),(3,3),(4,1)}** — all lie on the shifted-coord circle |(a+3/2, b+1/2)|²=32.5. (Elie: score the object-match against **four** modes, not three.)

**Structure (for the sharpened test, per Keeper/Lyra's recast):** the four pair under the diagonal-swap (a+3/2)↔(b+1/2): {(0,5)↔(4,1)} and {(2,4)↔(3,3)}. **BUT the diagonal swap is NOT a symmetry of D_IV⁵** (short-root mult 3 ≠ long-root mult 1, T2545) — so a swap-pairing is *not* automatically protected. The recast's "symmetry-protected doublet + accidental mode(s)" therefore rides Lyra's *actual* protecting symmetry, not the swap.

**SHARPENED PASS (the real discriminator):** a lazy operator that only respects the protecting symmetry gives the protected doublet equal |λ| **for free** and would MISS the accidental mode(s). So the sharp test is: **F(x) gives the ACCIDENTAL mode(s) the SAME |λ| as the protected doublet — all four equal.** Equal on the doublet only = symmetry-only operator = "resembles a CFS," FAIL. Equal on all four = encodes causal structure = real CFS, PASS.
- **Blocked input:** assigning WHICH modes are protected vs accidental needs Lyra's protecting symmetry. Pre-registered conditionally; I finalize the moment Lyra names it, then score Elie's four eigenvalues.

## Checker 2 — S_BH spectral test (#72, Elie + me): does dN/dA = 1/(4ℓ_P²) fall out directly?
Object: the Bergman/Hardy mode-counting function on the horizon Σ, via the reproducing kernel of A²(D_IV⁵) restricted to Σ, with a Planck cutoff. The **direct** test of the March-2026 Candidate A, independent of the (1/2)_hol×(1/2)_Z2 factor argument.

**PRE-REGISTERED RULING:**
- **PASS (strong):** leading coefficient = **1/4** emerges with *neither* factor inserted by hand — the holomorphic selection (p⁺) and the S¹ Z2 both come out of the kernel geometry.
- **PARTIAL (matches current honest tier):** only **(1/2)_hol** emerges cleanly from the holomorphic kernel; the second 1/2 must be supplied by no-hair/charge-conjugation (imported, as I flagged). → coefficient 1/2 internally, 1/4 with imported no-hair.
- **FAIL:** coefficient ≠ 1/4, or 1/4 only via a tuned cutoff (a hidden knob — Cal's warning).
- **The crux of the toy (flagged for Elie):** the projection from the 5-real-dim Shilov boundary S⁴×S¹ onto the 2-dim physical horizon Σ. That projection is where the coefficient is made or lost; it must not smuggle a factor.

## Note
Both criteria are locked before the numbers. Consistent with target-innocence: the test integers (rank, n_C, the mode labels) are the domain's own, not chosen for these results. Nothing pushed.
