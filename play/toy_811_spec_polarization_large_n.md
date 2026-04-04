# Toy 811 Spec: BH(3) Polarization at Large n

**Author**: Keeper (spec), Elie (implementation)
**Date**: April 4, 2026
**Purpose**: Empirical test of the Polarization Lemma for T812 (BH(3) Backbone Conditional)

---

## Goal

Test whether the intermediate fraction (variables with 0 < H(x_i | φ SAT) < δ) converges to 0 as n → ∞ for random 3-SAT at α_c ≈ 4.267.

Toy 356 showed 21% intermediate at n=12-20. Arikan polarization is asymptotic — we need larger n to see if intermediates vanish.

## Method

Use **survey propagation** (SP) to estimate marginal entropies at large n:

1. Generate random 3-SAT at α_c = 4.267 for n ∈ {100, 200, 500, 1000, 2000}
2. Run SP to convergence (or flag non-convergence)
3. Compute H(x_i | φ SAT) for each variable via SP messages
4. Classify: frozen (H < 0.01), intermediate (0.01 ≤ H < δ), free (H ≥ δ) with δ = 0.1
5. Record fraction in each category per n

## Tests (8 total)

| # | Test | PASS criterion |
|---|------|---------------|
| T1 | SP convergence rate | SP converges for ≥ 80% of instances at each n |
| T2 | Frozen fraction | frozen > 0.3 at all n (BH(3) empirically holds) |
| T3 | Intermediate decreasing | intermediate fraction decreases monotonically with n |
| T4 | Intermediate scaling | intermediate ∝ n^{-β} for β > 0 (power-law vanishing) |
| T5 | Free fraction stable | free fraction converges to constant (0.15-0.20) |
| T6 | Backbone vs first moment | backbone ≥ n - 0.176n = 0.824n (theoretical ceiling) |
| T7 | BST discriminator | free fraction → 0.176 (Shannon) or 0.191 (Reality Budget)? |
| T8 | Bimodality | H distribution becomes more bimodal with increasing n |

## Key output

- Table: n, frozen%, intermediate%, free%, SP_convergence_rate
- Plot: intermediate fraction vs n (log-log if power-law)
- Plot: H distribution histogram at n=100 and n=2000

## Expected result

If Arikan polarization extends to OR on expanders: intermediate → 0 as n → ∞. This would be strong empirical evidence for the Polarization Lemma, closing BH(3) empirically.

If intermediate does NOT decrease: the gap in BH(3) is real and a different approach (Ding-Sly-Sun extension) is needed.

## Dependencies

- T70, T71, T72, T812
- Toy 356 (baseline at small n)
- Toy 357 (large-n free fraction)

## Notes

- Survey propagation is O(n × iterations) — should be feasible at n=2000
- If SP doesn't converge, use belief propagation as fallback
- SAT instances can be generated with standard random k-SAT generators
- At α_c, ~50% of instances are SAT — use only SAT instances for H measurement
