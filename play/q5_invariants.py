#!/usr/bin/env python3
"""
Compute curvature invariants of Q⁵ = SO(5,2)/[SO(5)×SO(2)] in the Killing metric.

Q⁵ = D_IV^5 is a Hermitian symmetric space of rank 2, real dimension 10.
It's the bounded symmetric domain of type IV (Lie ball) in 5 complex dimensions.

The tangent space decomposes under SO(5)×SO(2) as the 10-dim real representation.
As a complex manifold, the holomorphic tangent space is the vector representation
of SO(5,C) tensored with the charge-1 representation of SO(2) ≅ U(1).

For a rank-2 Hermitian symmetric space G/K with G = SO(n,2), K = SO(n)×SO(2):
The Riemann tensor in the Killing metric can be computed from the Lie algebra structure.

Key facts:
- G = SO(5,2), K = SO(5)×SO(2)
- Lie algebra: so(5,2) = k + p, where k = so(5)+so(2), dim p = 10
- Complex structure J on p from the so(2) factor
- R(X,Y)Z = -[[X,Y],Z] for X,Y,Z in p (Cartan's formula for symmetric spaces)
- Killing form B(X,Y) = tr(ad_X ad_Y), restricted to p gives the metric

We use standard matrix realizations.

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

from fractions import Fraction


def main():
    # so(5,2) in 7×7 matrices: preserve eta = diag(1,1,1,1,1,-1,-1)
    # X in so(5,2) means X^T eta + eta X = 0
    # i.e. eta X is skew-symmetric
    #
    # Block form: X = [[A, B], [-B^T, C]] where A in so(5), C in so(2), B is 5×2
    # k = {A,C block}: so(5) + so(2)
    # p = {B block}: 5×2 real matrices = 10-dimensional

    # Basis for p: E_{i,alpha} where i=0..4, alpha=5,6
    # E_{i,alpha} has +1 at (i,alpha) and +1 at (alpha,i) [because of eta signature]
    # Actually let's be careful with the eta signature.

    # For so(p,q) with eta = diag(1,...,1,-1,...,-1), p ones and q minus-ones:
    # X in so(p,q) means X^T eta + eta X = 0
    # Writing X = [[A, B], [C, D]] with A: p×p, D: q×q, B: p×q, C: q×p
    # Then A in so(p), D in so(q), and C = B^T

    # For so(5,2): eta = diag(1,1,1,1,1,-1,-1)
    # X = [[A, B], [B^T, D]] with A in so(5) (5×5 skew), D in so(2) (2×2 skew), B: 5×2 arbitrary
    # k-part: A, D blocks
    # p-part: B block (5×2 = 10 parameters)

    n = 7  # matrix size for so(5,2)
    d_compact = 5  # SO(5)
    d_noncompact = 2  # SO(2)

    # Basis for p: e_{i,a} for i in {0,1,2,3,4}, a in {5,6}
    # Matrix E_{i,a} has: entry (i,a) = 1, entry (a,i) = 1, rest zero
    # (This follows from C = B^T with the eta convention above)

    p_basis = []
    p_labels = []
    for i in range(d_compact):
        for a in range(d_compact, n):
            E = [[Fraction(0)] * n for _ in range(n)]
            E[i][a] = Fraction(1)
            E[a][i] = Fraction(1)
            p_basis.append(E)
            p_labels.append(f"e_{i},{a}")

    dim_p = len(p_basis)
    print(f"  dim p = {dim_p}")

    # Lie bracket [X,Y] = XY - YX (matrix commutator)
    def mat_mul(A, B):
        sz = len(A)
        C = [[Fraction(0)] * sz for _ in range(sz)]
        for i in range(sz):
            for j in range(sz):
                for k in range(sz):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    def mat_sub(A, B):
        sz = len(A)
        return [[A[i][j] - B[i][j] for j in range(sz)] for i in range(sz)]

    def bracket(X, Y):
        return mat_sub(mat_mul(X, Y), mat_mul(Y, X))

    # [p, p] lands in k. For symmetric spaces, R(X,Y)Z = -[[X,Y], Z]
    # projected back to p.
    # The Killing metric on p: B(X,Y) = tr(ad_X ad_Y)
    # For normalization, we need the Killing form.

    # First compute the Killing form restricted to p.
    # B(X,Y) = tr(ad_X . ad_Y) where ad acts on the full Lie algebra.
    # For simplicity, compute ad_X as a matrix on the full Lie algebra basis.

    # Full basis of so(5,2): dim = 7*6/2 = 21
    # k basis: so(5) has 10 generators, so(2) has 1 generator = 11 total
    # p basis: 10 generators
    # Total: 21. Good.

    # k basis: E_{ij} for 0<=i<j<5 (so(5) part) and E_{56} (so(2) part)
    k_basis = []
    k_labels = []
    for i in range(d_compact):
        for j in range(i + 1, d_compact):
            E = [[Fraction(0)] * n for _ in range(n)]
            E[i][j] = Fraction(1)
            E[j][i] = Fraction(-1)
            k_basis.append(E)
            k_labels.append(f"k_{i}{j}")

    # so(2) part: E_{56}
    E56 = [[Fraction(0)] * n for _ in range(n)]
    E56[5][6] = Fraction(1)
    E56[6][5] = Fraction(-1)
    k_basis.append(E56)
    k_labels.append("k_56")

    full_basis = k_basis + p_basis
    full_labels = k_labels + p_labels
    dim_full = len(full_basis)
    print(f"  dim k = {len(k_basis)}, dim p = {dim_p}, dim g = {dim_full}")

    # Compute structure constants: [e_a, e_b] = sum_c f^c_{ab} e_c
    # We need to express brackets in terms of the basis.
    def express_in_basis(M, basis):
        """Express matrix M as linear combination of basis elements."""
        # Use the trace inner product: <A,B> = tr(A^T B)
        # But our basis isn't orthonormal, so solve the linear system.
        # Actually for so(p,q), the standard basis elements are:
        # E_{ij} with (i,j) entry = 1, (j,i) = ±1
        # These are orthogonal under tr(A^T B), with norm 2.
        # Let's just read off coefficients directly.
        coeffs = [Fraction(0)] * len(basis)
        for idx, B in enumerate(basis):
            # Find the "key entry" of B
            for i in range(n):
                for j in range(n):
                    if B[i][j] != 0:
                        key_i, key_j = i, j
                        break
                if B[i][j] != 0:
                    break
            # coefficient = M[key_i][key_j] / B[key_i][key_j]
            coeffs[idx] = M[key_i][key_j] / B[key_i][key_j]
        return coeffs

    # Actually, let me use a simpler approach. Since each basis element has
    # a unique "characteristic entry", I can read off coefficients directly.
    # For k_{ij} (i<j, both < 5): entry (i,j) = 1
    # For k_{56}: entry (5,6) = 1
    # For e_{i,a}: entry (i,a) = 1

    def decompose(M):
        """Decompose M into k-part and p-part."""
        k_coeffs = []
        # so(5) part
        for i in range(d_compact):
            for j in range(i + 1, d_compact):
                k_coeffs.append(M[i][j])
        # so(2) part
        k_coeffs.append(M[5][6])

        p_coeffs = []
        for i in range(d_compact):
            for a in range(d_compact, n):
                p_coeffs.append(M[i][a])

        return k_coeffs, p_coeffs

    # Riemann tensor: R(X,Y,Z,W) = B(-[[X,Y],Z], W) where B is Killing metric on p
    # First compute the Killing metric on p.
    # B(e_a, e_b) = tr(ad_{e_a} ad_{e_b})

    # For efficiency, compute ad action on full basis for each p basis element
    def ad_matrix(X):
        """Compute matrix of ad_X in the full basis."""
        ad = [[Fraction(0)] * dim_full for _ in range(dim_full)]
        for j, ej in enumerate(full_basis):
            comm = bracket(X, ej)
            # Decompose comm in full basis
            k_c, p_c = decompose(comm)
            coeffs = k_c + p_c
            for i in range(dim_full):
                ad[i][j] = coeffs[i]
        return ad

    print("  Computing Killing metric on p...")
    # Killing metric: g_{ab} = tr(ad_{p_a} ad_{p_b}) = sum_k (ad_{p_a})_{ki} (ad_{p_b})_{ki}
    # But this sums over full Lie algebra

    ad_p = []
    for idx in range(dim_p):
        ad_p.append(ad_matrix(p_basis[idx]))

    g_metric = [[Fraction(0)] * dim_p for _ in range(dim_p)]
    for a in range(dim_p):
        for b in range(a, dim_p):
            val = Fraction(0)
            for i in range(dim_full):
                for j in range(dim_full):
                    val += ad_p[a][i][j] * ad_p[b][i][j]
            g_metric[a][b] = val
            g_metric[b][a] = val

    # Print diagonal
    print("  Killing metric diagonal:", [g_metric[i][i] for i in range(dim_p)])

    # Check if metric is proportional to identity (should be for irreducible symmetric space)
    g_diag = g_metric[0][0]
    is_proportional = all(
        g_metric[i][j] == (g_diag if i == j else Fraction(0))
        for i in range(dim_p) for j in range(dim_p)
    )
    print(f"  Metric proportional to identity: {is_proportional}")
    if is_proportional:
        print(f"  g = {g_diag} × delta")

    # Riemann tensor in Killing metric:
    # R(X,Y)Z = -[[X,Y], Z]_p (projection to p)
    # R_{abcd} = g(R(e_a, e_b)e_c, e_d) = -g([[e_a,e_b], e_c]_p, e_d)
    # = -B([[e_a,e_b], e_c], e_d)  [since g = B|_p for Killing metric]
    #
    # But we want the metric-normalized version. If g = lambda * delta,
    # then the unit-normalized basis is f_a = e_a/sqrt(lambda).
    # R_{abcd} in ortho frame = R(f_a,f_b,f_c,f_d) = (1/lambda²) R(e_a,e_b,e_c,e_d)
    # where R(e_a,e_b,e_c,e_d) = -B([[e_a,e_b], e_c], e_d)
    #
    # Actually let's be more careful.
    # Riem(X,Y,Z,W) = g(R(X,Y)Z, W) = -g([[X,Y],Z]_p, W)
    # In ortho frame: R_{abcd} = Riem(f_a,f_b,f_c,f_d)
    # f_a = e_a / sqrt(lambda)
    # R_{abcd} = Riem(e_a,e_b,e_c,e_d) / lambda²
    # = -g([[e_a,e_b],e_c]_p, e_d) / lambda²
    # = -lambda * <[[e_a,e_b],e_c]_p, e_d> / lambda²   [since g=lambda*delta]
    # = -<[[e_a,e_b],e_c]_p, e_d> / lambda

    print("\n  Computing Riemann tensor (ortho frame)...")

    # Precompute [e_a, e_b] for all p basis pairs
    # [p, p] ⊂ k, so result is in k
    pp_bracket_k = {}
    for a in range(dim_p):
        for b in range(dim_p):
            comm = bracket(p_basis[a], p_basis[b])
            k_coeffs, _ = decompose(comm)
            pp_bracket_k[(a, b)] = k_coeffs

    # Now [[e_a,e_b], e_c]: [k, p] -> p
    # [e_a, e_b] = sum_I alpha_I k_I
    # [[e_a,e_b], e_c] = sum_I alpha_I [k_I, e_c]
    # [k_I, e_c] is in p, decompose it

    # Precompute [k_I, e_c] -> p coefficients
    kp_bracket_p = {}
    for I in range(len(k_basis)):
        for c in range(dim_p):
            comm = bracket(k_basis[I], p_basis[c])
            _, p_coeffs = decompose(comm)
            kp_bracket_p[(I, c)] = p_coeffs

    # R_{abcd} = -<[[e_a,e_b],e_c]_p, e_d> / lambda
    # [[e_a,e_b],e_c]_p = sum_I pp_bracket_k[(a,b)][I] * kp_bracket_p[(I,c)]
    # So the d-th component is sum_I pp_bracket_k[(a,b)][I] * kp_bracket_p[(I,c)][d]
    # R_{abcd} = -(1/lambda) * sum_I pp_bracket_k[(a,b)][I] * kp_bracket_p[(I,c)][d]

    lam = g_diag  # the Killing form normalization

    def Riem(a, b, c, d):
        val = Fraction(0)
        ab_k = pp_bracket_k[(a, b)]
        for I in range(len(k_basis)):
            if ab_k[I] != 0:
                val += ab_k[I] * kp_bracket_p[(I, c)][d]
        return -val / lam

    # Verify symmetries on a few elements
    print("  Checking symmetries...")
    ok = True
    for a in range(min(3, dim_p)):
        for b in range(min(3, dim_p)):
            for c in range(min(3, dim_p)):
                for d in range(min(3, dim_p)):
                    r = Riem(a, b, c, d)
                    if r != -Riem(b, a, c, d):
                        print(f"    FAIL antisym1 at {a}{b}{c}{d}")
                        ok = False
                    if r != -Riem(a, b, d, c):
                        print(f"    FAIL antisym2 at {a}{b}{c}{d}")
                        ok = False
                    if r != Riem(c, d, a, b):
                        print(f"    FAIL pair sym at {a}{b}{c}{d}")
                        ok = False
    if ok:
        print("  Symmetries OK (checked 3×3×3×3 block)")

    # Compute curvature invariants
    print("\n  Computing curvature invariants...")
    rng = range(dim_p)

    # Ricci tensor: Ric_{ab} = sum_c R_{acbc}
    Ric = [[Fraction(0)] * dim_p for _ in range(dim_p)]
    for a in rng:
        for b in rng:
            for c in rng:
                Ric[a][b] += Riem(a, c, b, c)

    R_scalar = sum(Ric[a][a] for a in rng)
    print(f"  R = {R_scalar} = {float(R_scalar):.6f}")

    # Check if Einstein
    is_einstein = all(
        Ric[a][b] == (Ric[0][0] if a == b else Fraction(0))
        for a in rng for b in rng
    )
    print(f"  Einstein: {is_einstein}")
    if is_einstein:
        print(f"  Ric = {Ric[0][0]} × g")

    Ric_sq = sum(Ric[a][b] ** 2 for a in rng for b in rng)
    print(f"  |Ric|² = {Ric_sq}")

    Rm_sq = Fraction(0)
    for a in rng:
        for b in rng:
            for c in rng:
                for d in rng:
                    Rm_sq += Riem(a, b, c, d) ** 2
    print(f"  |Rm|² = {Rm_sq}")

    # Ric³
    Ric3 = Fraction(0)
    for a in rng:
        for b in rng:
            for c in rng:
                Ric3 += Ric[a][b] * Ric[b][c] * Ric[c][a]
    print(f"  Ric³ = {Ric3}")

    # I₆_A = R_{abcd} R_{cdef} R_{efab}
    I6A = Fraction(0)
    for a in rng:
        for b in rng:
            for c in rng:
                for d in rng:
                    if Riem(a, b, c, d) == 0:
                        continue
                    for e in rng:
                        for f in rng:
                            I6A += Riem(a, b, c, d) * Riem(c, d, e, f) * Riem(e, f, a, b)
    print(f"  I₆_A = {I6A}")

    # I₆_B = R_{abcd} R_{aecf} R_{bedf}
    I6B = Fraction(0)
    for a in rng:
        for b in rng:
            for c in rng:
                for d in rng:
                    if Riem(a, b, c, d) == 0:
                        continue
                    for e in rng:
                        for f in rng:
                            I6B += Riem(a, b, c, d) * Riem(a, e, c, f) * Riem(b, e, d, f)
    print(f"  I₆_B = {I6B}")

    # Apply the effective a₃ formula
    c1 = Fraction(35, 9)
    c2 = Fraction(-14, 3)
    c3 = Fraction(14, 3)
    c4 = Fraction(-16, 9)
    c5 = Fraction(20, 9)
    c6 = Fraction(-16, 9)

    a3_5040 = (c1 * R_scalar**3 + c2 * R_scalar * Ric_sq
               + c3 * R_scalar * Rm_sq + c4 * Ric3
               + c5 * I6A + c6 * I6B)
    a3 = a3_5040 / 5040

    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  a₃(Q⁵) FROM CORRECTED FORMULA")
    print(f"  ══════════════════════════════════════════════════════")
    print(f"  5040 a₃ = {a3_5040}")
    print(f"  a₃ = {a3} = {float(a3):.10f}")

    # Compare with Plancherel ã₃ = -874/9
    plancherel = Fraction(-874, 9)
    print(f"\n  Plancherel ã₃ = {plancherel} = {float(plancherel):.10f}")
    print(f"  Ratio a₃/ã₃ = {a3 / plancherel if plancherel != 0 else 'N/A'}")

    # Summary
    print(f"\n  ══════════════════════════════════════════════════════")
    print(f"  INVARIANT SUMMARY")
    print(f"  ══════════════════════════════════════════════════════")
    print(f"  R³ = {R_scalar**3}")
    print(f"  R|Ric|² = {R_scalar * Ric_sq}")
    print(f"  R|Rm|² = {R_scalar * Rm_sq}")
    print(f"  Ric³ = {Ric3}")
    print(f"  I₆_A = {I6A}")
    print(f"  I₆_B = {I6B}")


if __name__ == '__main__':
    main()
