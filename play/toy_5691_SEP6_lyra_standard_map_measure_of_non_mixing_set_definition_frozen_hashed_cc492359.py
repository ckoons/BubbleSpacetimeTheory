"""TOY 5691 — Chirikov standard map: MEASURE OF THE NON-MIXING SET, definition frozen.
Lyra, 2026-09-06. Predictions .lyra_predictions_stdmap_measure_2026-09-06.txt, sha256 cc492359,
registered before this file was written. Replaces an unretained diagnostic run quoted in
Paper 2 Section 9a (Keeper 09-06).

DEFINITION: (x0,y0) on a uniform GxG grid of cell centres in [0,2pi)^2. Iterate
x' = x + y' (mod 2pi), y' = y + K sin x with y UNWRAPPED. Non-mixing at horizon T iff
max_{t<=T} |Y_t - Y_0| < 2pi. m(K,T) = fraction non-mixing. Every verdict below is computed
from the run's own values; nothing is typed in.
"""
import math, sys, time
import numpy as np
TWO_PI = 2*math.pi
KC = 0.971635

def measure(K, G, T):
    c = (np.arange(G) + 0.5) * TWO_PI / G
    X, Y = np.meshgrid(c, c, indexing="ij")
    X = X.ravel().copy(); Y = Y.ravel().copy(); Y0 = Y.copy()
    alive = np.ones(X.size, dtype=bool)
    for _ in range(T):
        Y += K*np.sin(X)
        X = (X + Y) % TWO_PI
        alive &= np.abs(Y - Y0) < TWO_PI
    return float(alive.mean())

if __name__ == "__main__":
    G = int(sys.argv[1]) if len(sys.argv) > 1 else 256
    Ts = [300, 1000, 3000, 10000]
    Ks = [0.0, 0.2, 0.5, 0.8, 0.9, 0.95, KC, 1.0, 1.2, 1.5, 2.0, 3.0]
    print("toy 5691: standard map, m(K,T) = measure of the non-mixing set, G=%d (%d orbits)" % (G, G*G))
    print("  %-9s" % "K" + "".join("%12s" % ("T=%d" % T) for T in Ts))
    table = {}
    for K in Ks:
        row = []
        for T in Ts:
            t0 = time.time(); m = measure(K, G, T); row.append(m)
        table[K] = row
        print("  %-9.6f" % K + "".join("%12.4f" % m for m in row) + ("   <-- K_c" if K == KC else ""))
        sys.stdout.flush()
    # verdicts, computed
    p1 = all(m == 1.0 for m in table[0.0])
    p2 = all(m >= 0.999 for K in Ks if K <= KC for m in table[K])
    above = [K for K in Ks if K > KC]
    monoK = all(all(table[above[i]][j] >= table[above[i+1]][j] - 1e-12 for j in range(len(Ts)))
                for i in range(len(above)-1))
    monoT = all(all(table[K][j] >= table[K][j+1] - 1e-12 for j in range(len(Ts)-1)) for K in above)
    p3 = monoK and monoT
    # P4 smoothness on the K grid {1.0,1.2,1.5,2.0,3.0} at each T: no single step > half the total drop
    grid = [1.0, 1.2, 1.5, 2.0, 3.0]
    p4 = True
    for j in range(len(Ts)):
        vals = [table[K][j] for K in grid]
        total = vals[0] - vals[-1]
        steps = [vals[i] - vals[i+1] for i in range(len(grid)-1)]
        if total > 0 and max(steps) > 0.5*total: p4 = False
    for name, ok in [("P1 K=0 control m=1.000 at every T", p1),
                     ("P2 m>=0.999 for all K<=K_c at every T", p2),
                     ("P3 monotone decreasing in K and in T above K_c", p3),
                     ("P4 smooth: no single K-step > half the drop 1.0->3.0", p4)]:
        print("  %s: %s" % (name, "HIT" if ok else "MISS"))
    print("  P5: yesterday's values (0.980/0.653/0.389/0.172 at K=1.2/1.5/2.0/3.0) were NOT predicted; "
          "nearest T by max abs diff:")
    yest = {1.2: 0.980, 1.5: 0.653, 2.0: 0.389, 3.0: 0.172}
    for j, T in enumerate(Ts):
        d = max(abs(table[K][j] - v) for K, v in yest.items())
        print("     T=%-6d max|diff| = %.3f" % (T, d))
