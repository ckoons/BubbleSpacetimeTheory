"""TEST 17 — a population of cooperating pairs. Lyra for Casey, 2026-09-05. Preds b354801f.
NO FITNESS FUNCTION. Each individual is a mutual-gating pair carrying a parameter theta (the
protection strength eps) ENCODED IN THE RECORD THAT THETA PROTECTS. Individuals copy at interval T;
junctions whose rate exceeds 1/T scramble before the copy is read. Whatever concentrates does so
because it transmitted, not because anything scored it.
"""
import math, random, sys
from collections import Counter

# theta index -> protection factor eps. theta is encoded in the record itself.
EPS = [1.0, 1e-1, 1e-2, 1e-3, 1e-4]        # 0 = no protection ... 4 = strongest
NTHETA = len(EPS)
THETA_BITS = 3                              # theta stored in 3 junctions (values 0..4 used)

def scramble_prob(eps, T, rate=1.0):
    """A junction carrying theta is gated by the partner, so its effective rate is rate*eps.
    It scrambles during the copy interval iff its rate exceeds 1/T."""
    return 1.0 if rate*eps > 1.0/T else 0.0

def run(T, generations=400, N=2000, mut=0.01, disable_protection=False, seed=0):
    rng = random.Random(seed)
    pop = [rng.randrange(NTHETA) for _ in range(N)]
    hist = []
    for g in range(generations):
        new = []
        for _ in range(N):
            parent = pop[rng.randrange(N)]
            eps = 1.0 if disable_protection else EPS[parent]
            # the theta-bearing junctions scramble if unprotected at this copy interval
            if scramble_prob(eps, T) > 0.0:
                child = rng.randrange(NTHETA)          # theta read from scrambled bits: noise
            else:
                child = parent                          # record held: theta transmitted
            if rng.random() < mut:                      # variation
                child = rng.randrange(NTHETA)
            new.append(child)
        pop = new
        if g % 50 == 0 or g == generations-1:
            c = Counter(pop); hist.append((g, [c.get(k,0)/N for k in range(NTHETA)]))
    return hist

def show(tag, hist):
    print("  %s" % tag)
    for g, fr in hist[-1:]:
        print("     gen %-4d theta distribution %s   top=%d at %.1f%%"
              % (g, " ".join("%.2f" % x for x in fr), max(range(NTHETA), key=lambda k: fr[k]),
                 100*max(fr)))

if __name__ == "__main__":
    print("theta -> eps: %s   (theta is stored in the record that theta protects)" % EPS)
    print("A junction scrambles during the copy interval iff rate*eps > 1/T.\n")
    print("=== P1 NEGATIVE CONTROL: protection disabled for everyone (eps forced to 1) ===")
    for T in (10.0, 1e3, 1e5):
        show("T=%-8g" % T, run(T, disable_protection=True, seed=1))
    print("\n=== P2/P3/P4: theta free ===")
    for T in (2.0, 10.0, 1e2, 1e3, 1e4, 1e5, 1e6):
        h = run(T, seed=1)
        fr = h[-1][1]
        # which theta values actually survive the copy interval at this T?
        surviving = [k for k in range(NTHETA) if EPS[k] <= 1.0/T]
        show("T=%-8g  (theta values that survive one copy interval: %s)" % (T, surviving or "none"), h)
    sys.stdout.flush()
