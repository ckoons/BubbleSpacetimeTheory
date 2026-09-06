# PRE-REGISTRATION — Toy 5703, E7 (Round 120): the family sweep ζ_{ℤ^d}, d = 1…9, off-line zeros below T = 40, with Cal §852's two meanings pinned BEFORE the hash

**Elie, 2026-09-06 (Sunday) 11:58 EDT (`date`-rendered, copied). Hashed before the instrument runs. Keeper's 11:23 correction and Cal §852 C1 read first.**

## Object and instrument
Z_d(s) = Σ_{N≥1} r_d(N)N^{−s} (r_d = coefficients of θ^d), Λ_d(s) = π^{−s}Γ(s)Z_d(s) = Λ_d(d/2 − s); abscissa d/2, symmetry line Re s = d/4, poles at 0 and d/2. Rotated-splitting AFE as in 5695b with d/2 in place of 5/2 (y₀ = e^{i(π/2−5/t)}, NT = 4.5t + 60), checked per d by the FE residual (< 10⁻²⁰ at three strip points) and against a 90-digit unrotated reference at one point with t ≈ 20.

## The two meanings (Cal C1), counted separately
- **(a)** zeros in the strip 0 < Re s < d/2 with Re s ≠ d/4;
- **(b)** zeros beyond the abscissa, Re s > d/2.
Search: strips of height 4 in d/4 + 0.05 < Re s < d/2 + 0.6 (right half; mirrors s ↦ d/2 − s supply the left), windings, bisection, Newton, 0.01-box certificate; every located zero classified (a) or (b) by Re s − d/2. The band |Re s − d/4| < 0.05 is not searched and is reported as such. On-line count N_line(40) by sign changes of the real function Λ_d(d/4 + it). Total count N_total(40) by the argument principle on [−1/2, d/2 + 1/2] × (0.1, 40], so that N_total − N_line − 2·(located right-half zeros) = the unlocated remainder (must be 0, or the band).

## Hashed lines
- **P1 (instrument, per d):** FE residual < 10⁻²⁰ and reference agreement < 10⁻²⁰ for every d = 1…9.
- **P2 (controls, theorems/known):** (b)-count = 0 at d ∈ {1, 2, 4, 8} (Euler products do not vanish in their half-plane of absolute convergence; the 2-factors' roots lie on the lines Re s = 1 (d=4) and Re s = 2 (d=8), i.e. on the symmetry line, inside); (a)-count = 0 at d = 1, 2 (RH and GRH(χ₋₄) numerically below 40); (a)-count > 0 at d = 4 and d = 8 (ζ(s)ζ(s−1) and ζ(s)ζ(s−3): the ζ zeros sit on Re s = ½ and 3/2, resp. ½ and 7/2, off the lines 1 and 2) — predicted (a)-counts 12 and 12 (six ζ zeros below 40, each appearing twice); (b)-count ≥ 1 at d = 5 (the certified 2.50359 + 14.27999i, 5695d/e).
- **P3 (the can-fail content, my prior ≈ 60 % each):** (b)-count ≥ 1 below 40 for EACH of d = 3, 6, 7, 9, and (a)-count > 0 for each of them. A d with (b) = 0 and (a) = 0 below 40 is reported as "no witness below 40," not as RH-true.
- **P4 (Keeper's refined barrier list, read as an experiment):** the set of d with NO (b)-zeros below 40 is exactly {1, 2, 4, 8} (the Euler-product cases). This is the barrier lemma's prediction under meaning (b); can fail at any d ∉ {1,2,4,8} with no (b)-zero below 40 — in which case the honest reading is "the barrier is necessary, not sufficient, at this height."
- **P5 (bookkeeping):** at every d the unlocated remainder is 0.

Score X/5. Meaning (a) at d ∈ {4, 8} is a control of the instrument on a theorem, not a test of anything; meaning (b) at d ∈ {1,2,4,8} likewise.
