#!/usr/bin/env python3
"""
BST — Exact cubic curvature invariants on Q⁵ from so(7) Lie algebra
====================================================================
Compute T₁, T₂, I₆ by DIRECT contraction of the Riemann tensor.

On compact symmetric space G/K with metric g = -B|_m (Killing form):
  R(X,Y)Z = -[[X,Y], Z]          (Helgason convention)
  R(X,Y,Z,W) = -B([X,Y], [Z,W])  (using ad-invariance of B)

For Q⁵ = SO(7)/[SO(5)×SO(2)]:
  m = {E_{iα} : i ∈ {1..5}, α ∈ {6,7}}, dim m = 10
  k = so(5) ⊕ so(2), dim k = 11
  [E_{iα}, E_{jβ}] = δ_{αβ}E_{ij} - δ_{ij}E_{αβ}  (in k)
  B(E_{pq}, E_{rs}) = 10(δ_{ps}δ_{qr} - δ_{pr}δ_{qs})  [so(7)]
  g₀ = g(e_a, e_a) = -B(E_{iα}, E_{iα}) = 10

This is the definitive computation to resolve the 63/64 factor.

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

from fractions import Fraction
from math import factorial


def main():
    print()
    print("  ══════════════════════════════════════════════════════")
    print("  EXACT CUBIC INVARIANTS ON Q⁵ FROM so(7)")
    print("  ══════════════════════════════════════════════════════")

    d = 10  # real dimension of m
    g0 = Fraction(10)  # g(e_a, e_a) = -B(E_{iα}, E_{iα}) = 10

    def m_index_to_pair(a):
        """Map m-index a ∈ {0..9} to (i, α) with i ∈ {1..5}, α ∈ {6,7}."""
        return (a // 2 + 1, a % 2 + 6)

    # ──────────────────────────────────────────────────────
    # Riemann tensor: R(X,Y,Z,W) = -B([X,Y], [Z,W])
    # ──────────────────────────────────────────────────────
    # R(a,b,c,d) = 10[δ_{αβ}δ_{γδ}(δ_{ik}δ_{jl} - δ_{il}δ_{jk})
    #                + δ_{ij}δ_{kl}(δ_{αγ}δ_{βδ} - δ_{αδ}δ_{βγ})]

    def compute_R(a, b, c, dd):
        i, alpha = m_index_to_pair(a)
        j, beta = m_index_to_pair(b)
        k, gamma = m_index_to_pair(c)
        l, delta = m_index_to_pair(dd)

        val = (int(alpha == beta) * int(gamma == delta)
               * (int(i == k) * int(j == l) - int(i == l) * int(j == k))
               + int(i == j) * int(k == l)
               * (int(alpha == gamma) * int(beta == delta)
                  - int(alpha == delta) * int(beta == gamma)))
        return Fraction(10 * val)

    print("\n  Computing full Riemann tensor R(a,b,c,d)...")
    R = {}
    for a in range(d):
        for b in range(d):
            for c in range(d):
                for dd in range(d):
                    R[a, b, c, dd] = compute_R(a, b, c, dd)

    # Quick symmetry checks
    assert R[0, 1, 0, 1] == 10, f"R_0101 = {R[0,1,0,1]}, expected 10"
    assert R[0, 1, 1, 0] == -10, f"R_0110 = {R[0,1,1,0]}, expected -10"
    assert R[0, 2, 0, 2] == 10, f"R_0202 = {R[0,2,0,2]}, expected 10"
    print("  Symmetry checks passed")

    # ──────────────────────────────────────────────────────
    # Ricci tensor and scalar curvature
    # ──────────────────────────────────────────────────────
    # Ric_{ac} = g^{be} R_{ebac} = (1/g₀) Σ_b R(b,a,b,c)
    print("\n  ══════════════════════════════════════════════════════")
    print("  BASIC INVARIANTS")
    print("  ══════════════════════════════════════════════════════")

    Ric = {}
    for a in range(d):
        for c in range(d):
            Ric[a, c] = sum(R[b, a, b, c] for b in range(d)) / g0

    # R_scalar = g^{ac} Ric_{ac} = (1/g₀) Σ_a Ric_{aa}
    R_scalar = sum(Ric[a, a] for a in range(d)) / g0
    print(f"\n  R = {R_scalar}")
    assert R_scalar == Fraction(5), f"R mismatch: {R_scalar}"
    print("  ✓ R = 5 = n_C (Killing normalization)")

    # Einstein check
    lam = Ric[0, 0] / g0
    assert lam == R_scalar / d, "Not Einstein!"
    print(f"  ✓ Einstein: Ric = (R/d)g = (1/2)g, λ = {lam}")

    # |Ric|² = (1/g₀²) Σ_{a,b} Ric[a,b]²
    Ric_sq = sum(Ric[a, b]**2 for a in range(d) for b in range(d)) / g0**2
    print(f"  |Ric|² = {Ric_sq}")
    assert Ric_sq == Fraction(5, 2), f"|Ric|² mismatch: {Ric_sq}"
    print("  ✓ |Ric|² = 5/2 = n_C/r")

    # |Rm|² = (1/g₀⁴) Σ R[a,b,c,d]²
    Rm_sq = sum(R[a, b, c, dd]**2
                for a in range(d) for b in range(d)
                for c in range(d) for dd in range(d)) / g0**4
    print(f"  |Rm|² = {Rm_sq}")
    assert Rm_sq == Fraction(13, 5), f"|Rm|² mismatch: {Rm_sq}"
    print("  ✓ |Rm|² = 13/5 = c₃/c₁")

    # a₂ check
    a2 = (5 * R_scalar**2 - 2 * Ric_sq + 2 * Rm_sq) / 360
    assert a2 == Fraction(313, 900), f"a₂ mismatch: {a2}"
    print(f"  ✓ a₂ = {a2} = 313/900 (Killing norm)")

    # ──────────────────────────────────────────────────────
    # Cubic invariants
    # ──────────────────────────────────────────────────────
    print("\n  ══════════════════════════════════════════════════════")
    print("  CUBIC CURVATURE INVARIANTS")
    print("  ══════════════════════════════════════════════════════")

    # Tr(Ric³) = (1/g₀³) Σ Ric[a,b] Ric[b,c] Ric[c,a]
    Ric3 = sum(Ric[a, b] * Ric[b, c] * Ric[c, a]
               for a in range(d) for b in range(d) for c in range(d)) / g0**3
    print(f"\n  Tr(Ric³) = {Ric3}")
    assert Ric3 == Fraction(5, 4), f"Tr(Ric³) mismatch"
    print("  ✓ = λ³d = (1/2)³ × 10 = 5/4")

    # I₆ = Ric_{ab} R^a_{cde} R^{bcde}
    # = (1/g₀⁵) Σ Ric[a,b] R[a,c,d,e] R[b,c,d,e]
    print("\n  Computing I₆ = Ric_{ab} R^a_{cde} R^{bcde}...")
    I6 = Fraction(0)
    for a in range(d):
        for b in range(d):
            if Ric[a, b] == 0:
                continue
            for c in range(d):
                for dd in range(d):
                    for e in range(d):
                        I6 += Ric[a, b] * R[a, c, dd, e] * R[b, c, dd, e]
    I6 /= g0**5
    print(f"  I₆ = {I6}")
    assert I6 == Fraction(13, 10), f"I₆ mismatch: {I6}"
    print("  ✓ = (R/d)|Rm|² = (1/2)(13/5) = 13/10")

    # T₁ = R_{abcd} R^{ab}_{mn} R^{cdmn}
    # = (1/g₀⁶) Σ R[a,b,c,d] R[a,b,m,n] R[c,d,m,n]
    print("\n  Computing T₁ = R_{abcd} R^{ab}_{mn} R^{cdmn}...")
    T1 = Fraction(0)
    # Precompute the "squared" tensor: S[c,d,m,n] = Σ_{a,b} R[a,b,c,d] R[a,b,m,n]
    # This avoids the 10⁶ loop
    S = {}
    for c in range(d):
        for dd in range(d):
            for m in range(d):
                for n in range(d):
                    val = Fraction(0)
                    for a in range(d):
                        for b in range(d):
                            val += R[a, b, c, dd] * R[a, b, m, n]
                    S[c, dd, m, n] = val

    T1 = sum(S[c, dd, m, n] * R[c, dd, m, n]
             for c in range(d) for dd in range(d)
             for m in range(d) for n in range(d)) / g0**6

    print(f"  T₁ = {T1} = {float(T1):.10f}")
    print(f"  Note claims: 41/25 = {float(Fraction(41,25)):.10f}")
    if T1 == Fraction(41, 25):
        print("  ✓ T₁ = 41/25 CONFIRMED")
    else:
        print(f"  ✗ T₁ ≠ 41/25! FOUND: {T1}")
        print(f"    Ratio T₁/(41/25) = {T1 / Fraction(41, 25)}")

    # T₂ = R_{abcd} R^a_m^c_n R^{bmdn}
    # R^a_m^c_n = g^{ae}g^{cf} R_{emfn} = R_{amcn}/g₀²
    # R^{bmdn} = R_{bmdn}/g₀⁴
    # T₂ = (1/g₀⁶) Σ R[a,b,c,d] R[a,m,c,n] R[b,m,d,n]
    print("\n  Computing T₂ = R_{abcd} R^a_m^c_n R^{bmdn}...")
    T2 = Fraction(0)
    for a in range(d):
        for b in range(d):
            for c in range(d):
                for dd in range(d):
                    if R[a, b, c, dd] == 0:
                        continue
                    for m in range(d):
                        for n in range(d):
                            T2 += R[a, b, c, dd] * R[a, m, c, n] * R[b, m, dd, n]
    T2 /= g0**6

    print(f"  T₂ = {T2} = {float(T2):.10f}")
    print(f"  Note claims: 6/25 = {float(Fraction(6,25)):.10f}")
    if T2 == Fraction(6, 25):
        print("  ✓ T₂ = 6/25 CONFIRMED")
    else:
        print(f"  ✗ T₂ ≠ 6/25! FOUND: {T2}")
        print(f"    Ratio T₂/(6/25) = {T2 / Fraction(6, 25)}")

    # ──────────────────────────────────────────────────────
    # a₃ from Vassilevich formula
    # ──────────────────────────────────────────────────────
    print("\n  ══════════════════════════════════════════════════════")
    print("  a₃ FROM VASSILEVICH FORMULA (Killing norm)")
    print("  ══════════════════════════════════════════════════════")

    f7 = Fraction(factorial(7))  # 5040

    # 7! a₃ = (35/9)R³ - (14/3)R|Ric|² + (14/3)R|Rm|²
    #        - (208/9)Tr(Ric³) + (64/3)I₆ + (16/3)T₁ + (44/9)T₂
    terms = {
        '(35/9)R³': Fraction(35, 9) * R_scalar**3,
        '-(14/3)R|Ric|²': Fraction(-14, 3) * R_scalar * Ric_sq,
        '(14/3)R|Rm|²': Fraction(14, 3) * R_scalar * Rm_sq,
        '-(208/9)Tr(Ric³)': Fraction(-208, 9) * Ric3,
        '(64/3)I₆': Fraction(64, 3) * I6,
        '(16/3)T₁': Fraction(16, 3) * T1,
        '(44/9)T₂': Fraction(44, 9) * T2,
    }

    total = Fraction(0)
    for name, val in terms.items():
        total += val
        print(f"    {name} = {val} = {float(val):.6f}")

    a3 = total / f7
    print(f"\n  7! × a₃ = {total}")
    print(f"  a₃ = {a3} = {float(a3):.12f}")

    a3_note = Fraction(6992, 70875)
    print(f"  Note value: 6992/70875 = {float(a3_note):.12f}")
    if a3 == a3_note:
        print("  ✓ a₃ = 6992/70875 CONFIRMED")
    else:
        print(f"  ✗ a₃ ≠ 6992/70875!")
        print(f"    Ratio: {a3 / a3_note} = {float(a3 / a3_note):.12f}")

    # ──────────────────────────────────────────────────────
    # Scale to Plancherel normalization and compare
    # ──────────────────────────────────────────────────────
    print("\n  ══════════════════════════════════════════════════════")
    print("  COMPARISON WITH PLANCHEREL ã₃ = -874/9")
    print("  ══════════════════════════════════════════════════════")

    # Plancherel metric = (1/10) × Killing metric
    # Curvature scales as 1/(metric scale) ⇒ Rm_P = 10 × Rm_K
    # a₃ ~ Rm³ ⇒ a₃_P = 1000 × a₃_K
    # Noncompact dual: sign flip (-1)^3 = -1
    # ã₃(Plancherel, D) = -1000 × a₃(Killing, Q)

    a3_planch = -1000 * a3
    a3_target = Fraction(-874, 9)

    print(f"\n  a₃(Killing, Q⁵) = {a3}")
    print(f"  ã₃(Planch, D) = -1000 × a₃ = {a3_planch} = {float(a3_planch):.10f}")
    print(f"  ã₃(from density) = -874/9 = {float(a3_target):.10f}")

    ratio = a3_planch / a3_target
    print(f"\n  Ratio = {ratio} = {float(ratio):.12f}")

    if ratio == Fraction(64, 63):
        print("  Ratio = 64/63 EXACTLY")
        print("  The 63/64 discrepancy is CONFIRMED.")
        print("  The curvature invariants (T₁, T₂) are correct!")
        print("  ⇒ The error must be in the Vassilevich COEFFICIENTS")
        print("     or in the Killing → Plancherel rescaling.")
    elif ratio == Fraction(1):
        print("  PERFECT MATCH!")

    # ──────────────────────────────────────────────────────
    # Try different Vassilevich coefficient sets
    # ──────────────────────────────────────────────────────
    print("\n  ══════════════════════════════════════════════════════")
    print("  TESTING ALTERNATIVE a₃ FORMULAS")
    print("  ══════════════════════════════════════════════════════")

    # Target for 7! × a₃ that gives ã₃ = -874/9:
    # -1000 × a₃ = -874/9 ⇒ a₃ = 874/9000 ⇒ 7! × a₃ = 874 × 5040/9000 = 874 × 14/25 = 12236/25
    a3_target_K = Fraction(874, 9000)
    target_7fact = a3_target_K * f7
    print(f"\n  Target: 7!×a₃ = {target_7fact} = {float(target_7fact):.6f}")
    print(f"  Current:       {total} = {float(total):.6f}")
    diff = target_7fact - total
    print(f"  Difference:    {diff} = {float(diff):.6f}")
    print(f"  diff/total:    {diff/total} = {float(diff/total):.10f}")

    # The Einstein terms (involving only R, |Ric|², |Rm|²) are:
    # (35/9)R³ - (14/3)R|Ric|² + (14/3)R|Rm|²
    einstein_part = (Fraction(35, 9) * R_scalar**3
                     - Fraction(14, 3) * R_scalar * Ric_sq
                     + Fraction(14, 3) * R_scalar * Rm_sq)
    # The cubic-specific terms are:
    # -(208/9)Tr(Ric³) + (64/3)I₆ + (16/3)T₁ + (44/9)T₂
    cubic_part = (Fraction(-208, 9) * Ric3
                  + Fraction(64, 3) * I6
                  + Fraction(16, 3) * T1
                  + Fraction(44, 9) * T2)

    print(f"\n  Einstein part: {einstein_part} = {float(einstein_part):.6f}")
    print(f"  Cubic part:    {cubic_part} = {float(cubic_part):.6f}")

    # On Einstein manifold, some terms simplify:
    # Tr(Ric³) = λ³d, I₆ = λ|Rm|², the 'independent' terms are T₁ and T₂.
    # -(208/9)λ³d + (64/3)λ|Rm|² = λ[-(208/9)λ²d + (64/3)|Rm|²]
    einstein_cubic = (Fraction(-208, 9) * Ric3 + Fraction(64, 3) * I6)
    free_cubic = Fraction(16, 3) * T1 + Fraction(44, 9) * T2

    print(f"\n  Einstein-reducible cubic: {einstein_cubic} = {float(einstein_cubic):.6f}")
    print(f"  Free cubic (T₁, T₂):     {free_cubic} = {float(free_cubic):.6f}")

    # What coefficients of T₁, T₂ would give the target?
    # We need: c₁ T₁ + c₂ T₂ = target_7fact - einstein_part - einstein_cubic
    needed = target_7fact - einstein_part - einstein_cubic
    print(f"\n  Needed from T₁,T₂ terms: {needed} = {float(needed):.6f}")
    print(f"  Currently:                {free_cubic} = {float(free_cubic):.6f}")

    # Try: what if the Vassilevich convention uses opposite Riemann sign?
    # Some refs define R(X,Y) = ∇_Y∇_X - ∇_X∇_Y + ∇_{[X,Y]} (opposite sign)
    # This flips R → -R, and for odd-degree invariants:
    # Ric³ → -Ric³, I₆ → -I₆, T₁ → -T₁, T₂ → -T₂
    # Also R³ → -R³, R|Ric|² → -R|Ric|², R|Rm|² → -R|Rm|²
    # So 7! a₃ flips sign → a₃ flips sign → ã₃ flips sign.
    # This doesn't help since both sides flip.

    # Try: different formula (Gilkey 1995, Table 4.1)
    # Some references have different numerical coefficients.
    # Let me check with the Branson-Gilkey coefficients.
    print("\n  Testing formula variants:")

    # Variant 1: swap T₁ ↔ T₂ coefficients
    a3_v1 = (einstein_part + einstein_cubic
             + Fraction(44, 9) * T1 + Fraction(16, 3) * T2) / f7
    r1 = (-1000 * a3_v1) / a3_target
    print(f"  V1 (swap T₁↔T₂ coefs): ratio = {r1} = {float(r1):.10f}")

    # Variant 2: coefficient 16/3 on T₂ instead of T₁
    a3_v2 = (einstein_part + einstein_cubic
             + Fraction(16, 3) * T2 + Fraction(44, 9) * T1) / f7
    r2 = (-1000 * a3_v2) / a3_target
    print(f"  V2 (44/9 on T₁, 16/3 on T₂): ratio = {r2} = {float(r2):.10f}")

    # Variant 3: BGP formula from Branson-Gilkey-Pohjanpelto (1997)
    # They write: 7! a₃ = α₁ R³ + α₂ R|ρ|² + α₃ R|K|² + α₄ Tr(ρ³) + ...
    # where ρ = Ric, K = Rm (Weyl + parts)
    # For scalar Laplacian: (35/9, -14/3, 14/3, -208/9, 64/3, 16/3, 44/9)
    # There are refs that give slightly different coefficients.

    # Variant 4: check if a factor of 2 somewhere
    # What if T₂ should have coefficient 44/9 × (1/2)?
    a3_v4 = (einstein_part + einstein_cubic
             + Fraction(16, 3) * T1 + Fraction(22, 9) * T2) / f7
    r4 = (-1000 * a3_v4) / a3_target
    print(f"  V4 (44/9 → 22/9 on T₂): ratio = {r4} = {float(r4):.10f}")

    # ──────────────────────────────────────────────────────
    # Approach: compute a₃ via Kähler curvature operator
    # ──────────────────────────────────────────────────────
    print("\n  ══════════════════════════════════════════════════════")
    print("  KÄHLER CURVATURE OPERATOR APPROACH")
    print("  ══════════════════════════════════════════════════════")

    # The Kähler curvature operator R: Λ^{1,1} → Λ^{1,1}
    # has eigenvalues {5, 2, 0} with multiplicities {1, 10, 14}.
    # Tr(R^k) = 5^k + 10 × 2^k
    for k in range(1, 5):
        trk = 5**k + 10 * 2**k
        print(f"  Tr(R^{k}) = {trk}")

    # On a Kähler manifold, the cubic invariants T₁, T₂ have
    # specific Kähler expressions. Can we verify?
    #
    # The Riemann tensor on a Kähler manifold satisfies:
    # R_{a\bar{b}c\bar{d}} = R_{c\bar{b}a\bar{d}} = R_{a\bar{d}c\bar{b}}
    # All other types vanish: R_{abcd} = R_{a\bar{b}\bar{c}d} = 0
    #
    # In complex coordinates: only R_{α\bar{β}γ\bar{δ}} is nonzero.
    # The Riemannian R_{abcd} in real coordinates involves these.

    # Let me compute T₁, T₂ directly from the Kähler curvature operator.
    # First, build the Kähler curvature matrix.
    #
    # Complex basis: z_a = (e_{2a} + i e_{2a+1})/√2 for a = 0..4
    # So z_a corresponds to E_{(a+1,6)} + i E_{(a+1,7)} (up to normalization)
    #
    # The Kähler curvature: R_{α\bar{β}γ\bar{δ}} = R(z_α, \bar{z}_β, z_γ, \bar{z}_δ)
    # In real indices: z_α = (e_{2α} + i e_{2α+1})/√2
    # R(z_α, \bar{z}_β, z_γ, \bar{z}_δ) = (1/4)[R_{2α,2β,2γ,2δ} + R_{2α+1,2β+1,2γ,2δ}
    #   + R_{2α,2β,2γ+1,2δ+1} + R_{2α+1,2β+1,2γ+1,2δ+1}
    #   + i(...) - i(...)]
    # On Kähler manifold, the imaginary parts vanish.

    n = 5  # complex dimension
    KC = {}  # Kähler curvature R_{α\bar{β}γ\bar{δ}}
    for alpha in range(n):
        for beta in range(n):
            for gamma in range(n):
                for delta in range(n):
                    # Real indices: 2α, 2α+1, etc.
                    a1, a2 = 2*alpha, 2*alpha + 1
                    b1, b2 = 2*beta, 2*beta + 1
                    c1, c2 = 2*gamma, 2*gamma + 1
                    d1, d2 = 2*delta, 2*delta + 1
                    # R(z_α, z̄_β, z_γ, z̄_δ) = (1/4) × Σ of four R terms
                    val = (R[a1,b1,c1,d1] + R[a2,b2,c1,d1]
                           + R[a1,b1,c2,d2] + R[a2,b2,c2,d2])
                    KC[alpha, beta, gamma, delta] = val / 4

    # The curvature operator matrix: M_{(αγ),(βδ)} = R_{α\bar{β}γ\bar{δ}}
    # as a map on pairs (α,γ) → (β,δ).
    # Actually, the standard curvature operator is:
    # R: Λ^{1,1} → Λ^{1,1}, but on a Kähler manifold,
    # it's equivalent to a Hermitian form on pairs.
    #
    # For symmetric spaces, the eigenvalues of the curvature operator
    # are known. Let me just verify the spectrum.

    # Build the n² × n² matrix M where M[α*n+γ, β*n+δ] = KC[α,β,γ,δ]
    import numpy as np
    M = np.zeros((n*n, n*n))
    for alpha in range(n):
        for gamma in range(n):
            for beta in range(n):
                for delta in range(n):
                    M[alpha*n + gamma, beta*n + delta] = float(KC[alpha, beta, gamma, delta])

    evals = sorted(np.linalg.eigvalsh(M), reverse=True)
    print(f"\n  Kähler curvature operator eigenvalues (×g₀):")
    # Group by value
    from collections import Counter
    eval_counts = Counter(round(e, 6) for e in evals)
    for val, mult in sorted(eval_counts.items(), reverse=True):
        print(f"    {val:.6f} × {mult}")

    # ──────────────────────────────────────────────────────
    # Final summary
    # ──────────────────────────────────────────────────────
    print("\n  ══════════════════════════════════════════════════════")
    print("  DEFINITIVE RESULTS")
    print("  ══════════════════════════════════════════════════════")
    print(f"\n  Curvature invariants (Killing norm, exact):")
    print(f"    R       = {R_scalar} = n_C")
    print(f"    |Ric|²  = {Ric_sq} = n_C/r")
    print(f"    |Rm|²   = {Rm_sq} = c₃/c₁")
    print(f"    Tr(Ric³)= {Ric3}")
    print(f"    I₆      = {I6}")
    print(f"    T₁      = {T1}")
    print(f"    T₂      = {T2}")
    print(f"\n  a₃(Vassilevich, Killing) = {a3}")
    print(f"  ã₃(Plancherel → D) = {a3_planch}")
    print(f"  ã₃(exact, Plancherel density) = {a3_target}")
    print(f"\n  Ratio = {ratio} = 64/63" if ratio == Fraction(64, 63) else f"\n  Ratio = {ratio}")
    print(f"  The discrepancy is {float(diff):.6f} in 7!×a₃ (Killing)")
    print(f"  = {diff} = {diff.numerator}/{diff.denominator}")

    # Factor the difference
    def factorize(n):
        if n == 0:
            return "0"
        factors = []
        m = abs(n)
        d = 2
        while d * d <= m:
            while m % d == 0:
                factors.append(d)
                m //= d
            d += 1
        if m > 1:
            factors.append(m)
        from collections import Counter as C
        ct = C(factors)
        parts = [f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(ct.items())]
        sign = "-" if n < 0 else ""
        return sign + " × ".join(parts) if parts else "1"

    print(f"    Numerator {diff.numerator} = {factorize(diff.numerator)}")
    print(f"    Denominator {diff.denominator} = {factorize(diff.denominator)}")


if __name__ == '__main__':
    main()
