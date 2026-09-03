#!/usr/bin/env python3
"""
Toy (Shilov-boundary K-type dimension table) — Round 115 §4 (Grace, 2026-09-03).  PREPARED, NOT RUN FOR NUMBERS until
Lyra pins the frame (the (p,q) parametrization of the K-types of H^2 of the Lie ball, which K), per Keeper's order.
Objects, stated so the frame can be checked against them:
  K = SO(5) x SO(2).  SO(5) irreps by highest weight (a, b), a >= b >= 0 (B2 conventions, epsilon basis);
  Weyl dimension  dim(a,b) = (2a+3)(2b+1)(a+b+2)(a-b+1)/6.  Spherical harmonics of degree k on S^4 = (k, 0).
  Shilov boundary S = S^4 x S^1 / Z2 ((x, theta) ~ (-x, theta + pi)); L^2(S) K-types: (k, 0) tensor charge m with the
  parity k = m (mod 2) forced by the Z2 quotient, multiplicity 1 each — the CLOSED sector candidate (A) if 'closed' is
  the Hua/Poisson-Szego sector, which is all of L^2(S) (every boundary function is the boundary value of a Hua-harmonic
  function); the tangential CR sector candidate (B): S is TOTALLY REAL in C^5 (real dimension 5 = complex dimension), so
  there is no tangential CR condition on S at all — (B) = (A).  Lyra's frame decides whether 'closed' is (A) or another
  local law.
  REALIZED sector = boundary values of H^2 = holomorphic polynomials on the Lie ball: degree-d polynomials on C^5 =
  sum_j (z.z)^j Harm_{d-2j}(C^5), so the K-types are (k, 0) tensor charge d = k + 2j, j >= 0: (k, m) with m >= k,
  m = k (mod 2), multiplicity 1 (Hua 1963 / Faraut–Koranyi 1990 in the (harmonic degree, charge) parametrization;
  Lyra pins whether her (p,q) is (k, j) or another labelling).
Output (when run): for charges m = 0..M and harmonic degrees k, the table dim closed_(k,m) vs dim realized_(k,m), the
per-charge sums with a cutoff k <= Kmax (the closed side is infinite at fixed m without one), and sha256 of the table.
The 'effective dimension' summaries wait for the ESD note's definition (Cal: the SAME definition or no claim).
"""
import sys, json, hashlib
def dim_so5(a, b): return (2*a + 3) * (2*b + 1) * (a + b + 2) * (a - b + 1) // 6
def table(M=12, Kmax=24):
    rows = []
    for m in range(M + 1):
        closed = [(k, dim_so5(k, 0)) for k in range(Kmax + 1) if k % 2 == m % 2]
        realized = [(k, dim_so5(k, 0)) for k in range(0, m + 1) if k % 2 == m % 2]
        rows.append(dict(m=m, closed_types=len(closed), closed_dim_cut=sum(d for _, d in closed),
                         realized_types=len(realized), realized_dim=sum(d for _, d in realized), realized_ks=[k for k, _ in realized]))
    return rows
def cutoff_counts(Lam):
    """Lyra's effective-dimension functional (14:46): count K-types with d(d+3) + k^2 <= Lam, weighted by dim(d,0),
    closed = all (d, k) with k = d (mod 2), realized = k >= d in addition.  k ranges over integers >= 0 (charge)."""
    import math
    closed = realized = 0
    for d in range(0, int(math.sqrt(Lam)) + 2):
        if d * (d + 3) > Lam: break
        kmax = int(math.sqrt(Lam - d * (d + 3)))
        w = dim_so5(d, 0)
        ks = [k for k in range(-kmax, kmax + 1) if k % 2 == d % 2]   # L^2(S^1): charges of BOTH signs (corrected 14:50; the first run took k >= 0 and got twice Lyra's constant)
        closed += w * len(ks); realized += w * sum(1 for k in ks if k >= d)
    return closed, realized

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'cutoff':
        import math
        prev = None
        for Lam in (10**2, 10**3, 10**4, 10**5, 10**6, 10**7):
            c, r = cutoff_counts(Lam)
            slope = '' if prev is None else f"  log-log slopes closed {math.log(c/prev[0])/math.log(10):.3f} realized {math.log(r/prev[1])/math.log(10):.3f}"
            print(f"  Lambda = {Lam:>9d}: closed {c:>14d}  realized {r:>14d}  ratio {r/c:.5f}{slope}")
            prev = (c, r)
        print("  Lyra 14:46 predicted: exponents equal (5/2 each, so slopes -> 2.5 per decade of Lambda), ratio -> constant ~0.058, not 3/5 = 0.6")
    elif len(sys.argv) > 1 and sys.argv[1] == 'run':
        rows = table(); s = json.dumps(rows, sort_keys=True)
        print("sha256", hashlib.sha256(s.encode()).hexdigest()[:16])
        for r in rows: print(r)
    else:
        print("HELD: run with 'run' after Lyra's frame is on the board (Round 115 §4). Weyl dims (k,0) for k=0..6:", [dim_so5(k, 0) for k in range(7)])
