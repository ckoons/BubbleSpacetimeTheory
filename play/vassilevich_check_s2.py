#!/usr/bin/env python3
"""
BST — Minimal check: Vassilevich a₃ on S² from spectrum
=========================================================
S² is the simplest case. If the formula fails here, the coefficients are wrong.

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

from fractions import Fraction
from math import factorial
from mpmath import mp, mpf, exp, pi, nstr


def main():
    mp.dps = 60
    K_max = 100000

    print()
    print("  ══════════════════════════════════════════════════════")
    print("  VASSILEVICH a₃ CHECK ON S², S⁴, S⁶, S¹⁰")
    print("  ══════════════════════════════════════════════════════")

    spheres = [
        (2, "S²"),
        (4, "S⁴"),
        (6, "S⁶"),
        (10, "S¹⁰"),
    ]

    for d, name in spheres:
        print(f"\n  ═══ {name} (d={d}, K=1) ═══")

        # Curvature invariants for S^d with K=1
        R = Fraction(d * (d - 1))
        lam = Fraction(d - 1)  # Ric = (d-1)g
        Ric_sq = lam**2 * d
        Rm_sq = Fraction(2 * d * (d - 1))  # |Rm|² = 2d(d-1) for K=1
        Ric3 = lam**3 * d
        I6 = lam * Rm_sq  # = (d-1)|Rm|² on Einstein
        T1 = 2 * Rm_sq  # T₁ = 2|Rm|² on space forms
        T2 = Fraction((d - 2) * d * (d - 1))  # T₂ = (d-2)d(d-1) on space forms

        print(f"    R={R}, |Ric|²={Ric_sq}, |Rm|²={Rm_sq}")
        print(f"    Ric³={Ric3}, I₆={I6}, T₁={T1}, T₂={T2}")

        # a₂ from Vassilevich
        a2_V = (5 * R**2 - 2 * Ric_sq + 2 * Rm_sq) / 360
        print(f"    a₂(V) = {a2_V} = {float(a2_V):.10f}")

        # a₃ from Vassilevich
        f7 = Fraction(factorial(7))
        a3_num = (
            Fraction(35, 9) * R**3
            - Fraction(14, 3) * R * Ric_sq
            + Fraction(14, 3) * R * Rm_sq
            - Fraction(208, 9) * Ric3
            + Fraction(64, 3) * I6
            + Fraction(16, 3) * T1
            + Fraction(44, 9) * T2
        )
        a3_V = a3_num / f7
        print(f"    a₃(V) = {a3_V} = {float(a3_V):.15f}")

        # Volume of S^d with K=1
        # Vol(S^d) = 2π^{(d+1)/2} / Γ((d+1)/2)
        from mpmath import gamma
        Vol = 2 * pi**((d + 1) / mpf(2)) / gamma((d + 1) / mpf(2))
        print(f"    Vol = {nstr(Vol, 15)}")

        # Eigenvalues: λ_ℓ = ℓ(ℓ+d-1)
        # Degeneracies: use the standard formula
        # d_ℓ = C(d+ℓ, d) - C(d+ℓ-2, d) for ℓ ≥ 0
        from math import comb
        def deg(ell):
            v = comb(d + ell, d)
            if ell >= 2:
                v -= comb(d + ell - 2, d)
            return v

        # Verify first few
        degs = [deg(ell) for ell in range(5)]
        print(f"    First degeneracies: {degs}")

        # Spectral extraction
        # F(t) = (4πt)^{d/2} Z(t) / Vol = Σ a_k t^k
        # G(t) = [F(t) - a₀ - a₁t - a₂t²] / t³ → a₃

        a0 = mpf(1)
        a1 = mpf(int(R)) / 6
        a2 = mpf(a2_V.numerator) / mpf(a2_V.denominator)

        t_vals = [mpf(1) / mpf(10**k) for k in [3, 4, 5]]
        g_vals = []

        for t in t_vals:
            Z = mpf(0)
            for ell in range(K_max):
                dk = deg(ell)
                lk = ell * (ell + d - 1)
                term = dk * exp(-lk * t)
                Z += term
                if term < mpf(10)**(-50) and ell > 10:
                    break

            F = (4 * pi * t)**(d / mpf(2)) * Z / Vol
            G = (F - a0 - a1 * t - a2 * t**2) / t**3
            g_vals.append(G)
            print(f"    t={nstr(t, 4)}: G(t) = {nstr(G, 18)}")

        # Richardson
        if len(g_vals) >= 2:
            rich = (10 * g_vals[1] - g_vals[0]) / 9
            print(f"    Richardson: {nstr(rich, 18)}")
            rich2 = (10 * g_vals[2] - g_vals[1]) / 9
            print(f"    Richardson: {nstr(rich2, 18)}")

        print(f"    a₃(Vassilevich) = {float(a3_V):.15f}")
        if g_vals:
            ratio = float(g_vals[-1]) / float(a3_V)
            print(f"    Ratio spectral/Vassilevich = {ratio:.10f}")

    # ──────────────────────────────────────────────────────
    # Try ALTERNATIVE a₃ formula from Branson-Gilkey (1990)
    # ──────────────────────────────────────────────────────
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  CHECKING ALTERNATIVE COEFFICIENTS")
    print(f"  ══════════════════════════════════════════════════════")

    # The Vassilevich formula may use different index conventions.
    # The standard "Gilkey" formula from the 1995 book may differ.
    #
    # From Gilkey (1995), for the scalar Laplacian on d-dim manifold:
    # 7! × 360 × a₃ = [algebraic terms]
    #
    # Wait, that's 7! × 360 = 5040 × 360 = 1814400.
    # That would give very different coefficients.
    #
    # Actually, different papers use different conventions:
    # - Some include a factor of (4π)^{d/2} in the a_k definition
    # - Some use 360 as denominator for ALL a_k
    # - Some use k! as denominator
    #
    # Let me check: what if the correct formula has (4π)^{d/2} in front?
    #
    # Vassilevich (2003) eq (4.3):
    # 7!(4π)^{m/2} a_6(1,D) = Tr_V ∫ [...]
    #
    # For pointwise coefficient α₃:
    # α₃ = a_6(1,D) × (4π)^{m/2} / Vol
    #     = [terms at a point] / (7! Vol) × Vol = [terms at a point] / 7!
    #
    # Wait, more carefully:
    # 7!(4π)^{m/2} a_6 = Vol × [terms at a point]
    # a_6 = Vol × [terms] / [7!(4π)^{m/2}]
    # α₃ = a_6 × (4π)^{m/2} / Vol = [terms] / 7!
    #
    # So α₃ = [terms] / 5040. That's what I had.
    #
    # BUT: Vassilevich uses the convention that K(t,x,x) involves
    # the SQUARE ROOT of the metric determinant.
    # Standard SDW: K(t,x,x) = (4πt)^{-d/2} [a₀ + a₁t + ...]
    # Trace: Tr(e^{-tD}) = ∫ K(t,x,x) √g d^d x = Vol × (4πt)^{-d/2} [α₀+...]
    #
    # This matches what I used. So the formula should be right.
    #
    # UNLESS... the coefficients in front of I₆, T₁, T₂ in equation (4.3)
    # are for a DIFFERENT definition of these invariants.
    #
    # KEY INSIGHT: Vassilevich's T₂ might use a DIFFERENT index contraction
    # from what I computed. Let me check.
    #
    # Vassilevich (2003) eq (4.3), the T₂ term:
    # (44/9) R_{iajb} R_{icjd} R_{iabd}... no, I need to see the exact formula.
    #
    # Actually, from the arXiv version hep-th/0306138v4, page 15:
    # The 7 algebraic terms for E=Ω=0 are listed as:
    # (35/9) R τ₁ + ... where τ₁ = R², τ₂ = R_{ij}², τ₃ = R_{ijkl}²
    # and for cubic: R³, Rτ₂, Rτ₃, ρ₁=R^i_jR^j_kR^k_i,
    # ρ₂=R_{ij}R^i_{klm}R^{jklm}, ρ₃=R_{ijkl}R^{ij}_{mn}R^{klmn},
    # ρ₄=R_{ijkl}R^i_m^k_n R^{jmln}
    #
    # So ρ₃ = T₁ and ρ₄ = T₂. The formula is:
    # 5040 a₃ = (35/9)R³ - (14/3)Rτ₂ + (14/3)Rτ₃
    #          - (208/9)ρ₁ + (64/3)ρ₂ + (16/3)ρ₃ + (44/9)ρ₄
    #
    # Now ρ₄ = R_{ijkl} R^i_m^k_n R^{jmln}
    #
    # In an orthonormal frame: R^i_m^k_n = R_{imkn} (raising with δ).
    # So ρ₄ = Σ R_{ijkl} R_{imkn} R_{jmln}
    # = Σ R_{abcd} R_{amcn} R_{bmdn} with renaming.
    #
    # WAIT! I see a potential issue. In Vassilevich's notation:
    # R^{jmln} means R with indices j,m,l,n ALL UP.
    # In an orthonormal frame, this equals R_{jmln}.
    #
    # So ρ₄ = R_{ijkl} R_{imkn} R_{jmln}
    #
    # Let me compare with my T₂ = R_{abcd} R_{amcn} R_{bmdn}:
    # With a=i, b=j, c=k, d=l, m=m, n=n:
    # T₂ = R_{ijkl} R_{imkn} R_{jmln} ← WAIT, the last factor is R_{jmln}
    # but in my code I have R_{bmdn} = R_{jmdn} = R_{jmln}... YES same!
    # Because d→l in the relabeling.
    #
    # Hmm wait, let me be very careful. My T₂ definition:
    # T₂ = Σ_{a,b,c,d,m,n} R[a][b][c][d] * R[a][m][c][n] * R[b][m][d][n]
    #
    # Vassilevich ρ₄:
    # ρ₄ = Σ_{i,j,k,l,m,n} R[i][j][k][l] * R[i][m][k][n] * R[j][m][l][n]
    #
    # My: R[b][m][d][n], Vassilevich: R[j][m][l][n]
    # In my notation: a→i, b→j, c→k, d→l:
    # My R[j][m][l][n], same as Vassilevich R[j][m][l][n]. ✓
    #
    # SO THE FORMULAS ARE THE SAME! But the results don't match on S⁴.
    #
    # There MUST be an error somewhere. Let me check by computing
    # everything on S² and comparing with the known spectral answer.

    d = 2
    R = Fraction(2)
    print(f"\n  Detailed S² check:")
    print(f"    R = {R}")

    # On S²: everything is determined by R_{1212} = K = 1.
    # a₁ = R/6 = 1/3

    # For the SPECTRUM on S²: λ_ℓ = ℓ(ℓ+1), d_ℓ = 2ℓ+1.
    # Z(t) = Σ (2ℓ+1) e^{-ℓ(ℓ+1)t}
    # F(t) = t Z(t) / 1 (since Vol/(4π) = 4π/(4π) = 1 for (4πt)^{1} factor)

    # Actually: Z(t) = Vol × (4πt)^{-1} [a₀ + a₁t + ...]
    # F(t) = (4πt) Z(t) / Vol = a₀ + a₁t + ...
    # Vol(S²) = 4π
    # F(t) = 4πt × Z(t) / (4π) = t Z(t)

    t_test = mpf(1) / mpf(10000)
    Z = mpf(0)
    for ell in range(K_max):
        Z += (2 * ell + 1) * exp(-ell * (ell + 1) * t_test)
    F = t_test * Z
    print(f"    t=0.0001: F(t) = {nstr(F, 18)}")
    print(f"    a₀ = 1 ✓ (F → 1)")
    print(f"    (F-1)/t = {nstr((F - 1) / t_test, 18)} (should be 1/3)")

    a2_s2 = Fraction(1, 15)  # = 24/360
    G2 = (F - 1 - t_test / 3) / t_test**2
    print(f"    (F-1-t/3)/t² = {nstr(G2, 18)} (should be 1/15 = {1/15:.15f})")

    # Now a₃
    t_vals_s2 = [mpf(1) / mpf(10**k) for k in [3, 4, 5, 6]]
    print(f"\n    a₃ extraction:")
    g_s2 = []
    for t in t_vals_s2:
        Z = mpf(0)
        for ell in range(K_max):
            term = (2 * ell + 1) * exp(-ell * (ell + 1) * t)
            Z += term
            if term < mpf(10)**(-50) and ell > 10:
                break
        F = t * Z
        G = (F - 1 - t / 3 - t**2 / 15) / t**3
        g_s2.append(G)
        print(f"    t={nstr(t, 4)}: G(t) = {nstr(G, 18)}")

    # Richardson
    for i in range(len(g_s2) - 1):
        rich = (10 * g_s2[i + 1] - g_s2[i]) / 9
        print(f"    Rich({nstr(t_vals_s2[i], 3)},{nstr(t_vals_s2[i+1], 3)}) = {nstr(rich, 18)}")

    a3_V_s2 = Fraction(74, 2835)
    print(f"\n    a₃(Vassilevich) = 74/2835 = {float(a3_V_s2):.15f}")
    if g_s2:
        print(f"    Ratio spectral/V = {float(g_s2[-1]) / float(a3_V_s2):.15f}")

    # Check: what if the CORRECT a₃ is the spectral value?
    # Then the formula must have different coefficients.
    # Let me try: what if the I₆, T₁, T₂ coefficients are
    # 64/3, 16/3, 44/9 but multiplied by 1/(4π)^{d/2}?
    # Or some other normalization factor?

    # Actually, let me check a totally different source.
    # From Berline-Getzler-Vergne (2004), Theorem 4.1:
    # The heat kernel has the expansion
    # k(t,x,x) = (4πt)^{-n/2} Σ_{j≥0} Φ_j(x) t^j
    # where Φ_0 = 1 and
    # Φ_1 = R/6
    # Φ_2 = (5R² - 2|Ric|² + 2|Rm|² + 6ΔR)/360
    #      = (5R² - 2|Ric|² + 2|Rm|²)/360 on symmetric spaces ✓
    #
    # For Φ_3, BGV (2004) equation (4.22):
    # Φ_3 is given by a complicated formula that I'd need to look up.
    #
    # An alternative: use the EXACT spectral answer and work backwards
    # to find the correct coefficients.

    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  REVERSE ENGINEERING: find correct coefficients")
    print(f"  ══════════════════════════════════════════════════════")

    # On S^d, T₁ = 2|Rm|² and T₂ = (d-2)d(d-1).
    # All other invariants are determined by R and d.
    # The a₃ formula has the form:
    # 5040 × a₃ = A(d) + B(d) × T₁ + C(d) × T₂
    # where A(d) contains the R³, R|Ric|², R|Rm|², Ric³, I₆ contributions.
    # On S^d (K=1): T₁ = 4d(d-1), T₂ = (d-2)d(d-1).
    # The spectral a₃ gives us the LHS.
    # Since we know A(d), we can extract B and C.

    # Actually, on a space form, I₆ = (d-1)|Rm|² and T₁ = 2|Rm|² are
    # both proportional to |Rm|². So the T₁ and I₆ terms are degenerate.
    # We can't separate their coefficients from space-form data alone.

    # Let me compute A(d) = contribution from terms that are
    # determined by R alone on Einstein manifolds:
    # A(d) = (35/9)R³ - (14/3)R|Ric|² + (14/3)R|Rm|² - (208/9)Ric³ + (64/3)I₆
    # On S^d: R = d(d-1), |Ric|² = (d-1)²d, |Rm|² = 2d(d-1),
    # Ric³ = (d-1)³d, I₆ = 2d(d-1)²

    for d, name in [(2, "S²"), (4, "S⁴"), (6, "S⁶")]:
        R = d * (d - 1)
        Rm_sq = 2 * d * (d - 1)
        A = (Fraction(35, 9) * R**3
             - Fraction(14, 3) * R * (d - 1)**2 * d
             + Fraction(14, 3) * R * Rm_sq
             - Fraction(208, 9) * (d - 1)**3 * d
             + Fraction(64, 3) * 2 * d * (d - 1)**2)

        T1_val = 2 * Rm_sq
        T2_val = (d - 2) * d * (d - 1)

        # 5040 a₃ = A + (16/3)T₁ + (44/9)T₂ [Vassilevich]
        a3_V = (A + Fraction(16, 3) * T1_val + Fraction(44, 9) * T2_val) / 5040

        print(f"\n  {name} (d={d}):")
        print(f"    A = {A} = {float(A):.6f}")
        print(f"    T₁ = {T1_val}, T₂ = {T2_val}")
        print(f"    a₃(Vassilevich) = {float(a3_V):.15f}")


if __name__ == '__main__':
    main()
