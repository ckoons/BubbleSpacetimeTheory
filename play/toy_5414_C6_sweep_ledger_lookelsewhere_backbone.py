#!/usr/bin/env python3
"""
Toy 5414 — C6 quantitative backbone: why 'pre-register or sweep' is load-bearing (Grace, Round 28).

Cal §654 added C6 to the reading quality bar: every reading either PRE-REGISTERS its (object, verb)
pair + expected form, OR is reported inside the FULL SWEEP (nulls alongside hits). Casey's alarm:
"30 readings × 20 targets at 1% is a dozen chance matches — and each passes 'target-innocent'
individually. Per-reading honesty is blind to the look-elsewhere."

This toy QUANTIFIES it (data/rigor lane) and gives the ledger the derivation phase needs:
 (1) an UNCONSTRAINED reading ('any BST-rational, denom≤Q, at 1%') covers ~all of [0,1] → worthless;
 (2) the FISHING look-elsewhere (N_formulas × N_targets pairings) is Casey's 'dozen';
 (3) PRE-REGISTRATION collapses the pool to ONE forced form → E[chance] = N·2ε (0.6, not 12);
 (4) the SWEEP metric: report (N attempted, H hit) and test H vs Binomial(N, 2ε), nulls alongside hits.

Reconnected: T830 (10^50 look-elsewhere correction, Grace), T1932 (denominator-density null), the
retired (1/8)^22 (independence over-count) — this formalizes that discipline as a per-derivation gate.

SCORE: 4/4 (unconstrained-is-worthless shown; fishing = Casey's dozen; pre-reg collapse 12→0.6;
             binomial sweep metric + ledger format).
"""
import math
from math import comb

def farey_count(Q):
    """#{p/q in [0,1], gcd(p,q)=1, q<=Q} ≈ 3Q²/π² (asymptotic Farey length)."""
    return 3*Q**2/math.pi**2

def coverage(Q, eps):
    """Fraction of [0,1] within ±eps of SOME denom-≤Q rational (union bound, capped at 1)."""
    return min(1.0, farey_count(Q)*2*eps)

def binom_tail(N, H, p):
    """P(X >= H) under Binom(N, p)."""
    return sum(comb(N, k)*p**k*(1-p)**(N-k) for k in range(H, N+1))

def main():
    print("="*84)
    print("Toy 5414 — C6 sweep-ledger: the look-elsewhere backbone for the derivation phase")
    print("="*84)

    # (1) unconstrained reading is worthless
    print("\n(1) UNCONSTRAINED pool ('any denom≤Q rational at tolerance ε') — coverage of [0,1]:")
    ok1 = True
    for Q in (10, 20, 40):
        for eps in (0.01, 0.001):
            cov = coverage(Q, eps)
            tag = "≈GUARANTEED match → WORTHLESS" if cov > 0.5 else "a real constraint"
            print(f"    Q={Q:>2}, ε={eps:<5}: {farey_count(Q):>5.0f} rationals, coverage={cov:.3f}  {tag}")
    # the load-bearing fact: denom≤20 at 1% covers essentially all of [0,1]
    if coverage(20, 0.01) < 0.99:
        ok1 = False
    print("    ⟹ denom≤20 at 1% covers ~all of [0,1]: an unconstrained 'match' carries ZERO information.")

    # (2) the fishing look-elsewhere = Casey's dozen
    print("\n(2) FISHING (no pre-registration): N_formulas × N_targets pairings, each at ±ε:")
    Nf, Nt, eps = 30, 20, 0.01
    E_fish = Nf*Nt*2*eps
    print(f"    {Nf} formulas × {Nt} targets × 2ε(={2*eps}) = E[chance matches] = {E_fish:.0f}")
    print(f"    ⟹ that IS Casey's 'dozen chance matches' — {E_fish:.0f} expected by pure luck. Each passes")
    print("       per-reading 'target-innocent'; the defect is the 600 uncommitted pairings, invisible per-reading.")
    ok2 = abs(E_fish - 12) < 1e-9

    # (3) pre-registration collapses the pool to ONE forced form
    print("\n(3) PRE-REGISTERED: the (object,verb) forces ONE form BEFORE the value → pool = 1, p = 2ε:")
    E_prereg = Nf*2*eps
    print(f"    {Nf} committed predictions × 2ε = E[chance] = {E_prereg:.1f}  (NOT {E_fish:.0f})")
    print(f"    ⟹ C6 buys the collapse {E_fish:.0f} → {E_prereg:.1f}: naming the address before the value turns")
    print("       600 fishing comparisons into 30 committed ones. THAT is why C6 is the load-bearing criterion.")
    ok3 = abs(E_prereg - 0.6) < 1e-9

    # (4) the sweep persuasiveness metric
    print("\n(4) SWEEP metric — report (N attempted, H hit); test H vs Binomial(N, p=2ε), nulls ALONGSIDE hits:")
    p = 2*eps
    ok4 = True
    for N, H in [(30, 12), (30, 25), (30, 2), (50, 30)]:
        pv = binom_tail(N, H, p)
        verdict = "SIGNAL" if pv < 1e-3 else ("weak" if pv < 0.05 else "consistent with CHANCE")
        print(f"    N={N}, H={H}: E[chance]=N·2ε={N*p:.1f}, p(≥H)={pv:.2e} → {verdict}")
    # sanity: 2/30 hits is consistent with chance; 12/30 is signal
    if not (binom_tail(30, 2, p) > 0.05 and binom_tail(30, 12, p) < 1e-3):
        ok4 = False
    print("    ⟹ a sweep with mostly-NULL results (H≈N·2ε) is honest evidence of NO signal; H≫N·2ε (tiny")
    print("       p-value) is FAR more persuasive than a handful of cherry-picked hits with the misses hidden.")

    print("\nTHE C6 LEDGER FORMAT (enforce in the derivation phase):")
    print("  per reading: (object, verb, pre-registered form, target, ε, HIT/MISS) — address BEFORE value.")
    print("  aggregate:   (N attempted, H hit, E[chance]=N·2ε, binomial p-value) — nulls printed with hits.")
    print("  A reading is admissible under C6 iff it is EITHER pre-registered OR in the full sweep. No cherry-picks.")

    score = sum([ok1, ok2, ok3, ok4])
    print(f"\nSCORE: {score}/4  ({'PASS' if score == 4 else 'PARTIAL'})")
    print("Reconnect: T830 (10^50 look-elsewhere), T1932 (denom-density null), retired (1/8)^22 (independence")
    print("over-count). C6 makes the look-elsewhere a PER-DERIVATION gate, not a post-hoc afterthought.")

if __name__ == "__main__":
    main()
