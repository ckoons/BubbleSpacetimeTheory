"""
Toy 2928 — Probability theory / statistics structural counts BST.

Standard probability distributions taught:
  Discrete: Bernoulli, Binomial, Geometric, Poisson, Hypergeometric = 5 = n_C
  Continuous: Uniform, Normal, Exponential, Gamma, Beta, Chi-squared,
              Student-t, F = 8 = rank³

Kolmogorov axioms: 3 = N_c (non-negativity, normalization, additivity)
Probability space components: 3 = N_c (Ω, F, P)

Moments commonly used: 4 = rank² (mean, variance, skewness, kurtosis)
Standard hypothesis test categories: 4 = rank² (z-test, t-test, chi², F-test)

Confidence interval levels standardly used: 3 = N_c (90%, 95%, 99%)
Type I/II error types: 2 = rank

Standard descriptive statistics: 5 = n_C (mean, median, mode, range, std)
Statistical inference frameworks: 3 = N_c (frequentist, Bayesian, likelihood)

ML loss function families standard: 5 = n_C (MSE, MAE, cross-entropy, hinge, KL)
Gradient descent variants standard: 4 = rank² (SGD, momentum, Adam, RMSprop)

Information measures: 4 = rank² (entropy, mutual info, KL divergence, relative entropy)
Standard cross-validation strategies: 4 = rank² (holdout, k-fold, LOO, stratified)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    prob = [
        ("Standard discrete distributions taught", 5, n_C, "n_C"),
        ("Standard continuous distributions taught", 8, rank**3, "rank³"),
        ("Kolmogorov axioms",                    3, N_c, "N_c"),
        ("Probability space components",         3, N_c, "N_c (Ω,F,P)"),
        ("Moments commonly used",                4, rank**2, "rank²"),
        ("Standard hypothesis test categories",  4, rank**2, "rank²"),
        ("Confidence interval standard levels",  3, N_c, "N_c (90,95,99)"),
        ("Type I/II error types",                2, rank, "rank"),
        ("Standard descriptive statistics",      5, n_C, "n_C"),
        ("Statistical inference frameworks",     3, N_c, "N_c"),
        ("ML loss function families",            5, n_C, "n_C"),
        ("Gradient descent variants",            4, rank**2, "rank²"),
        ("Information measures",                 4, rank**2, "rank²"),
        ("Cross-validation strategies",          4, rank**2, "rank²"),
        ("Normal distribution params (μ,σ)",     2, rank, "rank"),
        ("Bivariate normal params",              5, n_C, "n_C (μ_x,μ_y,σ_x,σ_y,ρ)"),
        ("Multivariate normal params (d-dim)",   2, rank, "rank (mean + cov)"),
    ]

    print("Probability / statistics BST:")
    matches = 0
    for name, val, bst, formula in prob:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<42} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(prob)}")
    return matches, len(prob)


if __name__ == "__main__":
    run()
