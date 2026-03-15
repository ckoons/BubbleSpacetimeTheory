#!/usr/bin/env python3
"""
Test whether J₁ = 2·I₆_B + I₆_A/2 is an algebraic identity
by checking on random Riemann tensors.

A valid Riemann tensor R_{abcd} must satisfy:
  1. R_{abcd} = -R_{bacd} = -R_{abdc}  (antisymmetry)
  2. R_{abcd} = R_{cdab}               (pair symmetry)
  3. R_{abcd} + R_{acdb} + R_{adbc} = 0 (first Bianchi)

Copyright (c) 2026 Casey Koons.
Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from fractions import Fraction


def random_riemann(d, seed=None):
    """Generate a random Riemann tensor in d dimensions."""
    rng = np.random.default_rng(seed)

    # Start with a random tensor, then symmetrize
    R = np.zeros((d, d, d, d))

    # Fill independent components using the symmetries
    # R_{abcd} with a<b, c<d, (a,b) <= (c,d) in lex order
    for a in range(d):
        for b in range(a+1, d):
            for c in range(d):
                for dd in range(c+1, d):
                    if (a, b) > (c, dd):
                        continue
                    val = rng.normal()
                    R[a, b, c, dd] = val
                    R[b, a, c, dd] = -val
                    R[a, b, dd, c] = -val
                    R[b, a, dd, c] = val
                    R[c, dd, a, b] = val
                    R[dd, c, a, b] = -val
                    R[c, dd, b, a] = -val
                    R[dd, c, b, a] = val

    # Impose first Bianchi identity by projecting
    # The cyclic part: B_{abcd} = R_{abcd} + R_{acdb} + R_{adbc}
    # should be zero. We project: R -> R - (1/3)(B + permutations)
    for _ in range(10):  # iterate to convergence
        B = np.zeros_like(R)
        for a in range(d):
            for b in range(d):
                for c in range(d):
                    for dd in range(d):
                        B[a, b, c, dd] = (R[a, b, c, dd] + R[a, c, dd, b] + R[a, dd, b, c]) / 3

        R_new = np.zeros_like(R)
        for a in range(d):
            for b in range(d):
                for c in range(d):
                    for dd in range(d):
                        R_new[a, b, c, dd] = R[a, b, c, dd] - B[a, b, c, dd]

        # Re-impose pair symmetries
        for a in range(d):
            for b in range(d):
                for c in range(d):
                    for dd in range(d):
                        val = (R_new[a,b,c,dd] - R_new[b,a,c,dd] - R_new[a,b,dd,c] + R_new[b,a,dd,c]) / 4
                        val2 = (val + (R_new[c,dd,a,b] - R_new[dd,c,a,b] - R_new[c,dd,b,a] + R_new[dd,c,b,a]) / 4) / 2
                        R_new[a,b,c,dd] = val2
                        R_new[b,a,c,dd] = -val2
                        R_new[a,b,dd,c] = -val2
                        R_new[b,a,dd,c] = val2
                        R_new[c,dd,a,b] = val2
                        R_new[dd,c,a,b] = -val2
                        R_new[c,dd,b,a] = -val2
                        R_new[dd,c,b,a] = val2
        R = R_new

    # Verify Bianchi
    max_bianchi = 0
    for a in range(d):
        for b in range(d):
            for c in range(d):
                for dd in range(d):
                    err = abs(R[a,b,c,dd] + R[a,c,dd,b] + R[a,dd,b,c])
                    max_bianchi = max(max_bianchi, err)

    return R, max_bianchi


def compute_invariants(R, d):
    """Compute J₁, I₆_A, I₆_B from Riemann tensor."""
    # Ricci tensor
    Ric = np.einsum('cacb->ab', R)

    # J₁ = Ric_{ab} R_{acde} R_{bcde}
    J1 = np.einsum('ab,acde,bcde->', Ric, R, R)

    # I₆_A = R_{abcd}R_{cdef}R_{efab}
    I6A = np.einsum('abcd,cdef,efab->', R, R, R)

    # I₆_B = R_{abcd}R_{aecf}R_{bedf}
    I6B = np.einsum('abcd,aecf,bedf->', R, R, R)

    return J1, I6A, I6B


def main():
    print("  ══════════════════════════════════════════════════════")
    print("  TESTING: Is J₁ = 2·I₆_B + ½·I₆_A ?")
    print("  ══════════════════════════════════════════════════════")

    for d in [3, 4, 5, 6]:
        print(f"\n  Dimension d = {d}:")
        for seed in range(10):
            R, bianchi_err = random_riemann(d, seed=seed)
            J1, I6A, I6B = compute_invariants(R, d)
            predicted = 2 * I6B + 0.5 * I6A
            diff = abs(J1 - predicted)
            status = "✓" if diff < 1e-8 else "✗"
            if seed < 3 or diff > 1e-8:
                print(f"    seed={seed}: J₁={J1:.6f}, 2I₆_B+½I₆_A={predicted:.6f}, "
                      f"diff={diff:.2e}, Bianchi err={bianchi_err:.2e} {status}")

        # Summary for this dimension
        diffs = []
        for seed in range(100):
            R, _ = random_riemann(d, seed=seed)
            J1, I6A, I6B = compute_invariants(R, d)
            diffs.append(abs(J1 - 2 * I6B - 0.5 * I6A))
        max_diff = max(diffs)
        print(f"    100 random tests: max |J₁ - 2I₆_B - ½I₆_A| = {max_diff:.2e}")


if __name__ == '__main__':
    main()
