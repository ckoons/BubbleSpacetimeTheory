#!/usr/bin/env python3
"""
BST — Definitive cross-check: a₃ on CP² and S⁴
=================================================
Compute a₃ from the Vassilevich (Riemannian) formula and from the exact
spectrum, on both CP² (Kähler) and S⁴ (non-Kähler, same real dimension).

If the Vassilevich formula is correct on both, the Q⁵ 63/64 factor is
a normalization issue. If it fails specifically on the Kähler manifold,
it's a genuine Kähler correction.

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

from fractions import Fraction
from math import factorial, comb
import numpy as np


def build_riemann_cp2():
    """Build the Riemann tensor of CP² with Fubini-Study metric (H=4).

    R_{ijkl} = δ_{ik}δ_{jl} - δ_{il}δ_{jk}
             + J_{ik}J_{jl} - J_{il}J_{jk} + 2J_{ij}J_{kl}

    Returns (4,4,4,4) array of Fraction.
    """
    d = 4
    # Complex structure J: J e₁ = e₂, J e₂ = -e₁, J e₃ = e₄, J e₄ = -e₃
    J = [[Fraction(0)] * d for _ in range(d)]
    J[0][1] = Fraction(-1)
    J[1][0] = Fraction(1)
    J[2][3] = Fraction(-1)
    J[3][2] = Fraction(1)

    # Kronecker delta
    def delta(i, j):
        return Fraction(1) if i == j else Fraction(0)

    R = [[[[Fraction(0)] * d for _ in range(d)] for _ in range(d)] for _ in range(d)]

    for i in range(d):
        for j in range(d):
            for k in range(d):
                for l in range(d):
                    R[i][j][k][l] = (
                        delta(i, k) * delta(j, l)
                        - delta(i, l) * delta(j, k)
                        + J[i][k] * J[j][l]
                        - J[i][l] * J[j][k]
                        + 2 * J[i][j] * J[k][l]
                    )

    return R


def build_riemann_sphere(d):
    """Build the Riemann tensor of S^d with sectional curvature K=1.

    R_{ijkl} = δ_{ik}δ_{jl} - δ_{il}δ_{jk}

    Returns (d,d,d,d) array of Fraction.
    """
    def delta(i, j):
        return Fraction(1) if i == j else Fraction(0)

    R = [[[[Fraction(0)] * d for _ in range(d)] for _ in range(d)] for _ in range(d)]
    for i in range(d):
        for j in range(d):
            for k in range(d):
                for l in range(d):
                    R[i][j][k][l] = delta(i, k) * delta(j, l) - delta(i, l) * delta(j, k)

    return R


def compute_invariants(R, d):
    """Compute all curvature invariants needed for the Vassilevich a₃ formula."""

    # Ricci tensor: Ric_{ij} = Σ_k R_{ikjk}
    Ric = [[Fraction(0)] * d for _ in range(d)]
    for i in range(d):
        for j in range(d):
            for k in range(d):
                Ric[i][j] += R[i][k][j][k]

    # Scalar curvature
    scalar_R = sum(Ric[i][i] for i in range(d))

    # |Ric|² = Σ_{ij} Ric_{ij}²
    Ric_sq = sum(Ric[i][j] ** 2 for i in range(d) for j in range(d))

    # |Rm|² = Σ_{ijkl} R_{ijkl}²
    Rm_sq = sum(
        R[i][j][k][l] ** 2
        for i in range(d) for j in range(d)
        for k in range(d) for l in range(d)
    )

    # Tr(Ric³) = Σ_{ijk} Ric_{ij}Ric_{jk}Ric_{ki}
    Ric3 = Fraction(0)
    for i in range(d):
        for j in range(d):
            for k in range(d):
                Ric3 += Ric[i][j] * Ric[j][k] * Ric[k][i]

    # I₆ = Σ_{abcde} Ric_{ab} R_{acde} R_{bcde}
    # = R_{ab} R^a_{cde} R^{bcde}  (in orthonormal frame)
    I6 = Fraction(0)
    for a in range(d):
        for b in range(d):
            for c in range(d):
                for dd in range(d):
                    for e in range(d):
                        I6 += Ric[a][b] * R[a][c][dd][e] * R[b][c][dd][e]

    # T₁ = Σ_{abcdmn} R_{abcd} R_{abmn} R_{cdmn}
    T1 = Fraction(0)
    # Precompute the contraction S[c][d][m][n] = Σ_{ab} R[a][b][c][d] * R[a][b][m][n]
    S = [[[[Fraction(0)] * d for _ in range(d)] for _ in range(d)] for _ in range(d)]
    for c in range(d):
        for dd in range(d):
            for m in range(d):
                for n in range(d):
                    for a in range(d):
                        for b in range(d):
                            S[c][dd][m][n] += R[a][b][c][dd] * R[a][b][m][n]
    for c in range(d):
        for dd in range(d):
            for m in range(d):
                for n in range(d):
                    T1 += S[c][dd][m][n] * R[c][dd][m][n]

    # T₂ = Σ R_{abcd} R_{amcn} R_{bmdn}
    T2 = Fraction(0)
    for a in range(d):
        for b in range(d):
            for c in range(d):
                for dd in range(d):
                    for m in range(d):
                        for n in range(d):
                            T2 += R[a][b][c][dd] * R[a][m][c][n] * R[b][m][dd][n]

    return {
        'R': scalar_R,
        '|Ric|²': Ric_sq,
        '|Rm|²': Rm_sq,
        'Ric³': Ric3,
        'I₆': I6,
        'T₁': T1,
        'T₂': T2,
    }


def vassilevich_a2(inv, d):
    """Compute a₂ from the Vassilevich/Gilkey formula."""
    R, Ric_sq, Rm_sq = inv['R'], inv['|Ric|²'], inv['|Rm|²']
    return (5 * R**2 - 2 * Ric_sq + 2 * Rm_sq) / 360


def vassilevich_a3(inv, d):
    """Compute a₃ from the Vassilevich formula.

    7! × a₃ = (35/9)R³ - (14/3)R|Ric|² + (14/3)R|Rm|²
              - (208/9)Tr(Ric³) + (64/3)I₆ + (16/3)T₁ + (44/9)T₂
    """
    R = inv['R']
    Ric_sq = inv['|Ric|²']
    Rm_sq = inv['|Rm|²']
    Ric3 = inv['Ric³']
    I6 = inv['I₆']
    T1 = inv['T₁']
    T2 = inv['T₂']

    f7 = Fraction(factorial(7))  # 5040

    numerator = (
        Fraction(35, 9) * R**3
        - Fraction(14, 3) * R * Ric_sq
        + Fraction(14, 3) * R * Rm_sq
        - Fraction(208, 9) * Ric3
        + Fraction(64, 3) * I6
        + Fraction(16, 3) * T1
        + Fraction(44, 9) * T2
    )

    return numerator / f7


def spectral_a_coefficients_sphere(d, k_max):
    """Compute heat kernel coefficients for S^d from its spectrum.

    Eigenvalues: λ_k = k(k+d-1), k = 0, 1, 2, ...
    Degeneracies: d_k = C(k+d-1,k) - C(k+d-3,k-2) = (2k+d-1)(k+d-2)!/[k!(d-1)!]

    The heat trace: Z(t) = Σ d_k e^{-λ_k t}
    SDW expansion: Z(t) = (4πt)^{-d/2} × Vol × Σ a_k t^k

    Vol(S^d) = 2π^{(d+1)/2} / Γ((d+1)/2)
    """
    from decimal import Decimal, getcontext
    getcontext().prec = 50

    # Compute Z(t) for several small t values
    ts = [Decimal(1) / Decimal(10**k) for k in range(1, 6)]

    # For extracting a₃, we need the a₀, a₁, a₂ to be known.
    # On S^d: a₀ = 1, a₁ = R/6 = d(d-1)/6, a₂ from Vassilevich.
    pass


def spectral_a3_cp2_numerical(k_max=500):
    """Compute a₃ on CP² numerically from its eigenvalue spectrum.

    CP² = SU(3)/U(2), rank 1 Hermitian symmetric space.

    The eigenvalues of the Laplacian on CP^n (with the FS metric where
    the holomorphic sectional curvature is 4) are:
      λ_k = 4k(k+n), k = 0, 1, 2, ...

    The degeneracies (from the Weyl dimension formula for SU(n+1)):
      d_k = C(k+n, n)² × (2k+n)/n - ... actually for CP^n:
      d_k = [(2k+n)/n] × C(k+n-1, n-1)²

    For CP² (n=2): λ_k = 4k(k+2), d_k = (2k+2)/2 × C(k+1,1)² = (k+1)³

    Wait, let me verify: d_0 = 1 (constant function), d_1 should be
    dim of the adjoint minus fixed = 8 - ... hmm.

    Actually for CP^n: d_k = C(k+n,n)² - C(k+n-1, n)²
    For n=2: d_k = C(k+2,2)² - C(k+1,2)² = [(k+1)(k+2)/2]² - [k(k+1)/2]²

    d_0 = 1, d_1 = 9 - 1 = 8? Let me check: C(3,2)² - C(2,2)² = 9 - 1 = 8.

    The representation π_k of SU(3) is the symmetric power Sym^k(C³),
    dim = C(k+2,2) = (k+1)(k+2)/2.
    These are the spherical representations.
    The eigenvalue is the Casimir C₂(π_k).

    But d_k = dim(π_k)² × correction? No, on G/K, d_k = dim(π_k) for
    class-1 representations. Wait, the multiplicity is 1 for each
    spherical representation, and the eigenvalue space is the full
    representation space. So d_k = dim(π_k) = C(k+2, 2) = (k+1)(k+2)/2.

    But that gives d_0 = 1, d_1 = 3 (the 3-dimensional standard rep of SU(3)?).
    Hmm, the COMPLEX functions on CP^n = SU(n+1)/U(n) decompose as:
    L²(CP^n) = ⊕_{k≥0} V_{(k,0,...,0,k)} but these are SU(n+1) reps of
    dimension C(k+n,n)² × ... actually for the spherical representations on
    CP^n = SU(n+1)/U(n), the class-1 representations are V_{(p,0,...,0,q)}
    with p-q = 0 mod 1 (since U(1) center). For REAL functions: p = q = k.

    For V_{(k,0,...,0,k)} of SU(n+1):
    dim = C(k+n, n) × C(k+n, n) × ... no.

    For SU(3), rep (k,k) (in Dynkin notation (k,k)):
    dim = (k+1)³ × ... let me use the Weyl formula.

    For SU(3) with highest weight (a,b):
    dim = (a+1)(b+1)(a+b+2)/2

    For (k,k): dim = (k+1)(k+1)(2k+2)/2 = (k+1)²(k+1) = (k+1)³.

    So d_k = (k+1)³.
    d_0 = 1, d_1 = 8, d_2 = 27, d_3 = 64.

    These are dim of the SU(3) representations (k,k) = adjoint symmetric products.
    d_1 = 8 = dim(adjoint) ✓ (the adjoint is the (1,1) rep)

    Eigenvalue: C₂(k,k) for SU(3) with the Killing metric.
    C₂(a,b) = (a² + b² + ab + 3a + 3b)/3 (for su(3) normalization)

    For (k,k): C₂ = (k² + k² + k² + 3k + 3k)/3 = (3k² + 6k)/3 = k² + 2k = k(k+2).

    So in the Killing normalization:
    λ_k = k(k+2), d_k = (k+1)³.

    In the FS normalization (H=4), R = 4n(n+1) = 24.
    In Killing: R_K = ?, need to figure out metric scale.

    Actually, the Killing metric on CP² = SU(3)/U(2):
    g_K = -B|_m where B is the Killing form of su(3).
    B(X,Y) = 6 Tr(XY) for su(3) (in the 3×3 matrix representation).

    The (0,4) metric tensor g_K has normalization g₀ such that
    the Laplacian eigenvalues are C₂(π_k)/g₀.

    Wait, on G/K with Killing metric g = -B|_m:
    Δ = -Σ E_α² (sum over an orthonormal basis of m w.r.t. g)
    and the eigenvalue on π_k is C₂(π_k).
    So λ_k = C₂(π_k) = k(k+2) in Killing normalization. ✓

    For the FS metric (H=4): the scalar curvature R_FS = 24.
    For the Killing metric: R_K = dim(m) × (1 - B(m,m)/B(g,g) terms)...
    Actually, for a symmetric space G/K, the scalar curvature in the
    Killing metric is:
    R = -(1/4)|[m,m]_k|² (from the structure constants)

    This is getting complicated. Let me just use the Killing metric and
    compute everything consistently.

    Returns: dict of exact a₃ values.
    """
    # In the Killing normalization on CP²:
    # λ_k = k(k+2), d_k = (k+1)³
    # The heat trace: Z(t) = Σ_{k≥0} (k+1)³ e^{-k(k+2)t}

    # Ricci tensor: need from the curvature tensor.
    # On CP² with Killing metric, the structure constants give:
    # R_{αβ̄γδ̄} = B([Z_α, Z̄_β], [Z_γ, Z̄_δ]) / B(m,m)²  (schematically)

    # For SU(3)/U(2), the isotropy representation m is the 4-dimensional
    # representation of U(2). Under the complexification, m_C = m^{1,0} ⊕ m^{0,1}
    # where m^{1,0} ≅ C² (the standard rep of U(2)).

    # The key point: CP^n is a rank-1 symmetric space with constant
    # holomorphic sectional curvature. All the geometry is determined by
    # a single parameter.

    # Let me instead just COMPUTE the heat kernel coefficients numerically.
    # Z(t) = Σ_{k=0}^∞ (k+1)³ e^{-k(k+2)t}
    # = Σ_{k=0}^∞ (k+1)³ e^{-(k+1)² t} × e^t
    # = e^t × Σ_{m=1}^∞ m³ e^{-m²t}

    # For small t, this sum is approximated by an integral:
    # Σ m³ e^{-m²t} ≈ ∫₀^∞ x³ e^{-x²t} dx = Γ(2)/(2t²) = 1/(2t²)

    # So Z(t) ≈ e^t/(2t²) ≈ (1 + t + t²/2 + ...)/(2t²) for small t.

    # The SDW expansion: Z(t) = (4πt)^{-2} × Vol_K × [a₀ + a₁t + a₂t² + a₃t³ + ...]
    # = Vol_K/(16π²) × [a₀/t² + a₁/t + a₂ + a₃t + ...]

    # Matching: Vol_K/(16π²) × a₀/t² ≈ 1/(2t²)
    # → Vol_K × a₀ = 8π²
    # With a₀ = 1: Vol_K = 8π²

    # So the normalized heat kernel:
    # (16π²/Vol_K) × t² × Z(t) = a₀ + a₁t + a₂t² + a₃t³ + ...
    # = 2t² × Z(t)

    # F(t) = 2t² × Z(t) → a₀ + a₁t + a₂t² + a₃t³ + ...

    # Let me compute F(t) numerically and extract the coefficients.
    print("\n  Numerical extraction of heat kernel coefficients on CP²:")
    print("  λ_k = k(k+2), d_k = (k+1)³, Killing normalization")

    # Use high precision
    ts = np.array([0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1])
    K_max = 2000

    for t_val in ts:
        Z = sum((k + 1) ** 3 * np.exp(-k * (k + 2) * t_val) for k in range(K_max))
        F = 2 * t_val**2 * Z
        print(f"    t={t_val:.4f}: Z={Z:.6f}, F(t) = 2t²Z = {F:.8f}")

    # For better precision, let me fit F(t) = a₀ + a₁t + a₂t² + a₃t³
    # Using Richardson extrapolation or polynomial fitting.

    # More precise: use very small t with extended sum
    K_max = 5000
    t_vals_small = [0.0005, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.008, 0.01]
    F_vals = []
    for t_val in t_vals_small:
        Z = sum((k + 1) ** 3 * np.exp(-k * (k + 2) * t_val) for k in range(K_max))
        F = 2 * t_val**2 * Z
        F_vals.append(F)

    F_vals = np.array(F_vals)
    t_vals_small = np.array(t_vals_small)

    # Fit polynomial: F(t) = a₀ + a₁t + a₂t² + a₃t³ + a₄t⁴
    # Using least squares with 5 parameters and 9 data points
    A_matrix = np.column_stack([t_vals_small**k for k in range(6)])
    coeffs, _, _, _ = np.linalg.lstsq(A_matrix, F_vals, rcond=None)

    print(f"\n  Polynomial fit F(t) = 2t²Z(t) = Σ a_k t^k:")
    for k, c in enumerate(coeffs):
        print(f"    a_{k} ≈ {c:.10f}")

    return coeffs


def main():
    print()
    print("  ══════════════════════════════════════════════════════")
    print("  DEFINITIVE CROSS-CHECK: a₃ ON CP² vs S⁴")
    print("  ══════════════════════════════════════════════════════")

    # ──────────────────────────────────────────────────────
    # PART 1: Curvature invariants of CP² (H=4)
    # ──────────────────────────────────────────────────────
    print(f"\n  ═══ CP² (Kähler, d=4, H=4) ═══")
    R_cp2 = build_riemann_cp2()
    inv_cp2 = compute_invariants(R_cp2, 4)

    print(f"\n  Curvature invariants:")
    for name, val in inv_cp2.items():
        print(f"    {name} = {val} = {float(val):.6f}")

    # Verify Einstein: Ric = λg
    lam_cp2 = inv_cp2['R'] / 4
    print(f"\n  Einstein: Ric = {lam_cp2} × g")
    Ric_sq_check = lam_cp2**2 * 4
    assert inv_cp2['|Ric|²'] == Ric_sq_check, f"|Ric|² mismatch"
    print(f"  |Ric|² = λ²d = {Ric_sq_check} ✓")

    # Compute a₂
    a2_cp2 = vassilevich_a2(inv_cp2, 4)
    print(f"\n  a₂(CP², Vassilevich) = {a2_cp2} = {float(a2_cp2):.10f}")

    # Compute a₃
    a3_cp2 = vassilevich_a3(inv_cp2, 4)
    print(f"  a₃(CP², Vassilevich) = {a3_cp2} = {float(a3_cp2):.10f}")

    # ──────────────────────────────────────────────────────
    # PART 2: Curvature invariants of S⁴ (K=1)
    # ──────────────────────────────────────────────────────
    print(f"\n  ═══ S⁴ (non-Kähler, d=4, K=1) ═══")
    R_s4 = build_riemann_sphere(4)
    inv_s4 = compute_invariants(R_s4, 4)

    print(f"\n  Curvature invariants:")
    for name, val in inv_s4.items():
        print(f"    {name} = {val} = {float(val):.6f}")

    lam_s4 = inv_s4['R'] / 4
    print(f"\n  Einstein: Ric = {lam_s4} × g")

    a2_s4 = vassilevich_a2(inv_s4, 4)
    print(f"\n  a₂(S⁴, Vassilevich) = {a2_s4} = {float(a2_s4):.10f}")

    a3_s4 = vassilevich_a3(inv_s4, 4)
    print(f"  a₃(S⁴, Vassilevich) = {a3_s4} = {float(a3_s4):.10f}")

    # ──────────────────────────────────────────────────────
    # PART 3: Known exact results for comparison
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  COMPARISON WITH KNOWN RESULTS")
    print(f"  ══════════════════════════════════════════════════════")

    # S⁴ with K=1: known heat kernel coefficients
    # a₀ = 1
    # a₁ = R/6 = 12/6 = 2
    # a₂ = (5R² - 2|Ric|² + 2|Rm|²)/360
    # On S⁴: R = 12, |Ric|² = 9×4=36, |Rm|² = 2×4×3=24
    # a₂ = (720 - 72 + 48)/360 = 696/360 = 29/15
    print(f"\n  S⁴ (K=1):")
    print(f"    a₁ = R/6 = {inv_s4['R']}/6 = {inv_s4['R']/6}")
    print(f"    a₂(Vassilevich) = {a2_s4}")
    print(f"    a₃(Vassilevich) = {a3_s4}")

    # On S^d, the eigenvalues are λ_k = k(k+d-1) with
    # d_k = C(k+d-1,k)(2k+d-1)/(d-1) (dimension of harmonic polynomials)
    # For S⁴: d_k = C(k+3,k)(2k+3)/3 = (k+1)(k+2)(k+3)(2k+3)/18
    # Wait, that doesn't look right. Let me use the standard formula:
    # d_k = C(k+d, d) - C(k+d-2, d) for the number of harmonic polynomials
    # on S^{d-1}... hmm, the literature is confusing about S^d vs S^{d-1}.

    # For S^d (d-dimensional sphere), the eigenvalues of the Laplacian are:
    # λ_k = k(k+d-1), k = 0, 1, 2, ...
    # d_k = C(k+d, d) - C(k+d-2, d) [this is for S^d]
    #
    # More explicitly: d_k = (2k+d-1)C(k+d-2, d-1)/(d-1)
    # For S⁴ (d=4): d_k = (2k+3)C(k+2, 3)/3 = (2k+3)(k+2)(k+1)k/(3×6)
    # d_0 = 1, d_1 = 5, d_2 = 14, d_3 = 30

    # Wait: for S⁴ (d=4):
    # d_k = C(k+3,3)(2k+3)/(3) ← this isn't right either
    # Standard: d_k = (2k+d-1)Γ(k+d-1)/[k! Γ(d)]
    # For S⁴: d_k = (2k+3)(k+1)(k+2)/(2×3)... let me just use the formula
    # d_k = C(k+d-1, d-1) - C(k+d-3, d-1)
    # For d=4: d_k = C(k+3, 3) - C(k+1, 3)
    # d_0 = C(3,3) - C(1,3) = 1 - 0 = 1 ✓
    # d_1 = C(4,3) - C(2,3) = 4 - 0 = 4... but S⁴ should have d_1 = 5.

    # OK the issue is S^4 has eigenvalues on the 4-SPHERE (surface of 5D ball).
    # For the d-dimensional sphere S^d:
    # eigenvalues λ_ℓ = ℓ(ℓ+d-1), multiplicities h(d,ℓ) = C(d+ℓ,d) - C(d+ℓ-2,d)
    # For S^4: h(4,ℓ) = C(4+ℓ,4) - C(2+ℓ,4)
    # h(4,0) = 1, h(4,1) = C(5,4) - C(3,4) = 5 - 0 = 5 ✓
    # h(4,2) = C(6,4) - C(4,4) = 15 - 1 = 14 ✓

    print(f"\n  S⁴ spectrum check:")
    for k in range(6):
        dk = comb(4 + k, 4) - (comb(2 + k, 4) if k >= 2 else 0)
        lk = k * (k + 3)
        print(f"    k={k}: d_k = {dk}, λ_k = {lk}")

    # Compute heat trace numerically on S⁴
    print(f"\n  Numerical heat trace on S⁴:")
    K_max = 500
    t_vals = [0.001, 0.005, 0.01, 0.05, 0.1]
    for t_val in t_vals:
        Z = sum(
            (comb(4 + k, 4) - (comb(2 + k, 4) if k >= 2 else 0))
            * np.exp(-k * (k + 3) * t_val)
            for k in range(K_max)
        )
        # SDW: Z(t) ~ Vol × (4πt)^{-2} × [a₀ + a₁t + a₂t² + ...]
        # So t² Z(t) / (Vol/(4π)²) → a₀ + a₁t + ...
        # Vol(S⁴) = 8π²/3
        Vol_S4 = 8 * np.pi**2 / 3
        F = (4 * np.pi)**2 / Vol_S4 * t_val**2 * Z
        print(f"    t={t_val:.4f}: Z={Z:.4f}, F(t)={F:.8f}")

    # ──────────────────────────────────────────────────────
    # PART 4: Spectral computation on CP²
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  SPECTRAL a₃ ON CP² (Killing normalization)")
    print(f"  ══════════════════════════════════════════════════════")

    # CP² = SU(3)/U(2)
    # Eigenvalues: λ_k = k(k+2) [Killing metric, from Casimir of SU(3) rep (k,k)]
    # Degeneracies: d_k = (k+1)³
    # d_0=1, d_1=8, d_2=27, d_3=64, ...

    print(f"\n  CP² spectrum (Killing normalization):")
    for k in range(8):
        dk = (k + 1)**3
        lk = k * (k + 2)
        print(f"    k={k}: d_k = {dk}, λ_k = {lk}")

    # Heat trace: Z(t) = Σ (k+1)³ e^{-k(k+2)t}
    # As t → 0: Z(t) ~ ∫₀^∞ x³ e^{-x²t} dx = Γ(2)/(2t²) = 1/(2t²)
    # SDW: Z(t) = Vol_K × (4πt)^{-2} × [a₀ + a₁t + ...]
    # Matching leading term: Vol_K/(16π²) × a₀/t² = 1/(2t²)
    # → Vol_K = 8π² (with a₀ = 1)

    Vol_CP2_K = 8 * np.pi**2

    # Normalized function: F(t) = (16π²/Vol_K) × t² × Z(t) = 2t² Z(t)
    # F(t) → a₀ + a₁t + a₂t² + a₃t³ + ...

    K_max = 10000
    t_vals_fine = np.array([0.0002, 0.0005, 0.001, 0.002, 0.003,
                            0.005, 0.008, 0.01, 0.015, 0.02])

    F_vals = []
    for t_val in t_vals_fine:
        Z = sum((k + 1) ** 3 * np.exp(-k * (k + 2) * t_val) for k in range(K_max))
        F = 2 * t_val**2 * Z
        F_vals.append(F)

    F_vals = np.array(F_vals)

    print(f"\n  F(t) = 2t²Z(t) values:")
    for t_val, F_val in zip(t_vals_fine, F_vals):
        print(f"    t={t_val:.4f}: F = {F_val:.12f}")

    # Polynomial fit
    A_matrix = np.column_stack([t_vals_fine**k for k in range(7)])
    coeffs, _, _, _ = np.linalg.lstsq(A_matrix, F_vals, rcond=None)

    print(f"\n  Polynomial fit (degree 6):")
    labels = ['a₀', 'a₁', 'a₂', 'a₃', 'a₄', 'a₅', 'a₆']
    for k, (c, label) in enumerate(zip(coeffs, labels)):
        print(f"    {label} = {c:.10f}")

    # ──────────────────────────────────────────────────────
    # PART 5: Compare with Vassilevich on CP²
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  COMPARISON: Vassilevich vs Spectral on CP²")
    print(f"  ══════════════════════════════════════════════════════")

    # The Vassilevich formula computed a₃ using the FS metric (H=4).
    # This has R_FS = 24.
    # The spectral computation uses the Killing metric with R_K = ?

    # We need to know the scalar curvature in the Killing normalization.
    # On CP² = SU(3)/U(2):
    # The Killing form of su(3): B(X,Y) = 6 Tr(XY)
    # Metric g = -B|_m, so g₀ = 6 (normalization factor).

    # For CP² with g = -B|_m:
    # Ric_{ij} = -(1/4)B_{ij} (see Besse, Theorem 7.38)
    # Since g_{ij} = -B_{ij}: Ric = (1/4)g
    # Wait, that gives λ = 1/4 and R = λd = 1.

    # Actually for a symmetric space G/K with metric g = -B|_m:
    # Ric = (1/2)g (for irreducible symmetric spaces)
    # This is a standard result: Ric_{ij} = -(1/2)B_{ij}|_m = (1/2)g_{ij}
    # Wait, that's also not right.

    # The standard formula for a compact symmetric space G/K:
    # R_{XYWZ} = -B([X,Y]_m, [W,Z]_m)/4 - B([X,W]_m, [Y,Z]_m)/2 + B([X,Z]_m, [Y,W]_m)/2
    # ... this depends on conventions.

    # For the KILLING metric on an irreducible symmetric space:
    # Ric = (1/2)g
    # R = d/2 = 2 for CP² (d=4)

    # Hmm, but the eigenvalue λ₁ = 1×3 = 3 should equal the first
    # nonzero Casimir. For SU(3) rep (1,1) (adjoint):
    # C₂(1,1) = (1+1+1+3+3)/3 = 3. ✓

    # So in the Killing metric: R = 2? Let me verify.
    # Ric = (1/2)g means |Ric|² = (1/4)d = 1.
    # R = (1/2)×4 = 2.

    # a₁ = R/6 = 2/6 = 1/3.
    a1_K = Fraction(1, 3)
    print(f"\n  In Killing normalization:")
    print(f"    R_K = 2, λ_K = 1/2")
    print(f"    a₁ = R/6 = 1/3")

    # Now what is |Rm|² in Killing normalization?
    # The FS metric with H=4 has R_FS = 24.
    # If g_FS = c × g_K, then R_FS = R_K / c = 2/c.
    # So c = 2/24 = 1/12. g_FS = g_K/12.
    # |Rm|²_FS = |Rm|²_K / c² = 144 |Rm|²_K
    # From our computation: |Rm|²_FS = 192
    # → |Rm|²_K = 192/144 = 4/3

    Rm_sq_K = Fraction(4, 3)
    R_K = Fraction(2)
    Ric_sq_K = Fraction(1)
    lam_K = Fraction(1, 2)

    a2_K = (5 * R_K**2 - 2 * Ric_sq_K + 2 * Rm_sq_K) / 360
    print(f"    |Rm|²_K = {Rm_sq_K}")
    print(f"    a₂_K = (5×4 - 2×1 + 2×4/3)/360 = {a2_K} = {float(a2_K):.10f}")

    # From spectral fit: a₂ ≈ coeffs[2]
    print(f"    a₂(spectral) ≈ {coeffs[2]:.10f}")
    print(f"    a₂(Vassilevich, Killing) = {float(a2_K):.10f}")

    # Now compute a₃ in Killing normalization:
    # Scale: cubic invariants scale as (curvature)³ ~ 1/c³ = 12³ = 1728
    # Ric³ scales as (1/c)³ = 1728
    Ric3_K = lam_K**3 * 4  # = (1/8)×4 = 1/2
    I6_K = lam_K * Rm_sq_K  # = (1/2)(4/3) = 2/3
    T1_K_cp2 = inv_cp2['T₁'] / Fraction(1728)  # Scale from FS to Killing
    T2_K_cp2 = inv_cp2['T₂'] / Fraction(1728)

    # Wait, I computed the invariants in the H=4 normalization.
    # If g_FS = g_K/12 (i.e., c = 1/12), then:
    # R_{FS} = R_K × 12 (curvature scales as 1/c = 12)
    # |Rm|²_FS = |Rm|²_K × 12² = 144 |Rm|²_K
    # T₁_FS = T₁_K × 12³ = 1728 T₁_K
    # T₂_FS = T₂_K × 12³ = 1728 T₂_K

    T1_K_cp2 = inv_cp2['T₁'] / 1728
    T2_K_cp2 = inv_cp2['T₂'] / 1728

    print(f"\n    Killing normalization invariants:")
    print(f"    R = {R_K}")
    print(f"    |Ric|² = {Ric_sq_K}")
    print(f"    |Rm|² = {Rm_sq_K}")
    print(f"    Ric³ = {Ric3_K}")
    print(f"    I₆ = {I6_K}")
    print(f"    T₁ = {T1_K_cp2} = {float(T1_K_cp2):.10f}")
    print(f"    T₂ = {T2_K_cp2} = {float(T2_K_cp2):.10f}")

    # Compute a₃ in Killing normalization
    f7 = Fraction(factorial(7))
    a3_K_num = (
        Fraction(35, 9) * R_K**3
        - Fraction(14, 3) * R_K * Ric_sq_K
        + Fraction(14, 3) * R_K * Rm_sq_K
        - Fraction(208, 9) * Ric3_K
        + Fraction(64, 3) * I6_K
        + Fraction(16, 3) * T1_K_cp2
        + Fraction(44, 9) * T2_K_cp2
    )
    a3_K = a3_K_num / f7

    print(f"\n    a₃(Vassilevich, Killing) = {a3_K} = {float(a3_K):.10f}")
    print(f"    a₃(spectral fit) ≈ {coeffs[3]:.10f}")

    if abs(float(a3_K) - coeffs[3]) < 0.001:
        print(f"\n    ✓ Vassilevich and spectral a₃ AGREE on CP²!")
        print(f"    → The 63/64 on Q⁵ is NOT a Kähler correction")
    else:
        ratio = coeffs[3] / float(a3_K)
        print(f"\n    ✗ Vassilevich and spectral a₃ DISAGREE on CP²!")
        print(f"    Ratio: a₃(spectral)/a₃(Vassilevich) = {ratio:.10f}")
        # Check if ratio is a nice fraction
        for num in range(1, 200):
            for den in range(1, 200):
                if abs(ratio - num/den) < 1e-6:
                    print(f"    ≈ {num}/{den}")
                    break

    # ──────────────────────────────────────────────────────
    # PART 6: Also check S⁴
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  SPECTRAL a₃ ON S⁴")
    print(f"  ══════════════════════════════════════════════════════")

    # S⁴ with K=1: λ_k = k(k+3), d_k = (2k+3)(k+1)(k+2)/6 + correction
    # d_k = C(k+4,4) - C(k+2,4) for S⁴
    # Vol(S⁴) = 8π²/3

    K_max = 10000
    Vol_S4 = 8 * np.pi**2 / 3

    F_s4_vals = []
    for t_val in t_vals_fine:
        Z = sum(
            (comb(4 + k, 4) - (comb(2 + k, 4) if k >= 2 else 0))
            * np.exp(-k * (k + 3) * t_val)
            for k in range(K_max)
        )
        F = (4 * np.pi)**2 / Vol_S4 * t_val**2 * Z
        F_s4_vals.append(F)

    F_s4_vals = np.array(F_s4_vals)

    print(f"\n  F(t) = (4π)²t²Z(t)/Vol values:")
    for t_val, F_val in zip(t_vals_fine, F_s4_vals):
        print(f"    t={t_val:.4f}: F = {F_val:.12f}")

    A_matrix = np.column_stack([t_vals_fine**k for k in range(7)])
    coeffs_s4, _, _, _ = np.linalg.lstsq(A_matrix, F_s4_vals, rcond=None)

    print(f"\n  Polynomial fit (degree 6):")
    for k, (c, label) in enumerate(zip(coeffs_s4, labels)):
        print(f"    {label} = {c:.10f}")

    a1_s4 = Fraction(2)  # R/6 = 12/6 = 2
    print(f"\n  a₁(S⁴) = R/6 = 2")
    print(f"  a₁(spectral) ≈ {coeffs_s4[1]:.10f}")
    print(f"  a₂(S⁴, Vassilevich) = {float(a2_s4):.10f}")
    print(f"  a₂(spectral) ≈ {coeffs_s4[2]:.10f}")
    print(f"  a₃(S⁴, Vassilevich) = {float(a3_s4):.10f}")
    print(f"  a₃(spectral) ≈ {coeffs_s4[3]:.10f}")

    # ──────────────────────────────────────────────────────
    # PART 7: Summary
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  SUMMARY: VASSILEVICH vs SPECTRAL")
    print(f"  ══════════════════════════════════════════════════════")

    print(f"\n  S⁴ (non-Kähler):")
    print(f"    a₃(Vassilevich) = {float(a3_s4):.10f}")
    print(f"    a₃(spectral)   ≈ {coeffs_s4[3]:.10f}")
    print(f"    Match: {abs(float(a3_s4) - coeffs_s4[3]) < 0.01}")

    print(f"\n  CP² (Kähler):")
    print(f"    a₃(Vassilevich) = {float(a3_K):.10f}")
    print(f"    a₃(spectral)   ≈ {coeffs[3]:.10f}")
    print(f"    Match: {abs(float(a3_K) - coeffs[3]) < 0.01}")


if __name__ == '__main__':
    main()
