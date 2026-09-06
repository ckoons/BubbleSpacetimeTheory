"""TEST 10 — how much information does one generation retain?  Lyra for Casey, 2026-09-05."""
import math, itertools
from collections import defaultdict

def H2(p):
    if p <= 0 or p >= 1: return 0.0
    return -p*math.log2(p) - (1-p)*math.log2(1-p)

def brute_force_MI(L, r):
    """Exact I(parent phase ; offspring phase), by enumerating every switch vector.
    POSITIVE CONTROL on the closed form."""
    n = L-1
    D = list(itertools.product([0,1], repeat=n))          # difference coordinate
    pri = 1.0/len(D)
    # transition: D -> D xor d, d_i ~ Bern(r) independent
    P = defaultdict(float)
    for d in itertools.product([0,1], repeat=n):
        w = math.prod(r if b else 1-r for b in d)
        for x in D:
            y = tuple(a ^ b for a, b in zip(x, d))
            P[(x, y)] += pri*w
    py = defaultdict(float)
    for (x, y), p in P.items(): py[y] += p
    mi = 0.0
    for (x, y), p in P.items():
        if p > 0: mi += p*math.log2(p/(pri*py[y]))
    return mi

if __name__ == "__main__":
    print("=== G1 CONTROL: brute-force I(parent;offspring) vs closed form (L-1)(1-H2(r)) ===")
    for L in (3, 5, 7):
        for r in (0.0, 0.01, 0.05, 0.1, 0.25, 0.5):
            bf = brute_force_MI(L, r); cf = (L-1)*(1-H2(r))
            print("  L=%d r=%.2f : brute %9.6f   closed %9.6f   diff %.2e %s"
                  % (L, r, bf, cf, abs(bf-cf), "HIT" if abs(bf-cf) < 1e-12 else "MISS"))
    print("\n=== RETENTION PER GENERATION, per junction (the range Casey asked for) ===")
    print("  %-10s %-10s %-12s %-12s %s" % ("r", "H2(r)", "RETAINED", "CREATED", "genetic distance"))
    for r, tag in [(0.0,"inversion / Y / mtDNA (no recombination)"),
                   (0.001,"~0.1 cM  (~100 kb human)"),
                   (0.01, "~1 cM    (~1 Mb human)"),
                   (0.05, "~5 cM"),
                   (0.10, "~11 cM"),
                   (0.20, "~26 cM"),
                   (0.30, "~46 cM"),
                   (0.50, "unlinked / different chromosomes")]:
        print("  %-10.3f %-10.4f %-12.4f %-12.4f %s" % (r, H2(r), 1-H2(r), H2(r), tag))
    print("\n=== G2: is it zero-sum?  T + N per junction ===")
    for r in (0.0,0.01,0.05,0.1,0.2,0.3,0.5):
        print("  r=%.2f   T=%.6f + N=%.6f = %.6f" % (r, 1-H2(r), H2(r), (1-H2(r))+H2(r)))
    print("\n=== G3/G4: decay over generations, and half-lives ===")
    print("  %-8s %s" % ("r", "  ".join("n=%-6d" % n for n in (1,2,3,5,10,20,50))))
    for r in (0.001,0.01,0.05,0.1,0.2):
        row = []
        for n in (1,2,3,5,10,20,50):
            pn = (1-(1-2*r)**n)/2
            row.append("%-8.4f" % (1-H2(pn)))
        print("  r=%-6.3f %s" % (r, "".join(row)))
    print("\n  %-8s %-22s %-22s %s" % ("r", "correlation half-life", "INFORMATION half-life", "ratio"))
    for r in (0.001,0.01,0.05,0.1,0.2):
        ch = math.log(0.5)/math.log(1-2*r)
        ih = None
        for n in range(1, 100000):
            pn = (1-(1-2*r)**n)/2
            if 1-H2(pn) <= 0.5:
                ih = n; break
        print("  %-8.3f %-22.1f %-22s %s" % (r, ch, ih, "%.2f" % (ih/ch) if ih else "-"))
