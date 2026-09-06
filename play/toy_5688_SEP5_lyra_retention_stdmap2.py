"""TEST 13b — standard map, TRANSPORT instrument. Lyra for Casey, 2026-09-05. Preds cf06831b."""
import math, sys
import numpy as np
TWO_PI = 2*math.pi

def bands(K, B=256, nx=8, ny=1024, T=3000, seed=0):
    """Union the y-bands each orbit visits. Components = invariant bands (transport barriers)."""
    rng = np.random.default_rng(seed)
    X = np.repeat(rng.random(nx)*TWO_PI, ny)
    Y = np.tile((np.arange(ny)+0.5)*TWO_PI/ny, nx)
    n = X.size
    visited = np.zeros((n, B), dtype=bool)
    for _ in range(T):
        Y = (Y + K*np.sin(X)) % TWO_PI
        X = (X + Y) % TWO_PI
        visited[np.arange(n), (Y*B/TWO_PI).astype(np.int64) % B] = True
    parent = np.arange(B)
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    for i in range(n):
        bs = np.flatnonzero(visited[i])
        for b in bs[1:]:
            ra, rb = find(bs[0]), find(b)
            if ra != rb: parent[ra] = rb
    roots = np.array([find(b) for b in range(B)])
    _, counts = np.unique(roots, return_counts=True)
    p = counts/counts.sum()
    return len(counts), float(-(p*np.log2(p)).sum())

if __name__ == "__main__":
    B = 256
    print("standard map, transport instrument: %d y-bands, 8192 orbits, 3000 steps" % B)
    print("  %-8s %12s %10s %10s   %s" % ("K","bands left","R (bits)","R/R(0)","note"))
    R0 = None
    for K in [0.0,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,0.971635,1.0,1.1,1.3]:
        nc, R = bands(K, B=B)
        if R0 is None: R0 = R
        note = ""
        if K == 0.0:   note = "J1 %s" % ("HIT" if nc == B else "MISS")
        if K == 0.1:   note = "J2 %s (needs MANY components)" % ("HIT" if nc > 10 else "MISS")
        if abs(K-0.971635) < 1e-6: note = "<-- known K_c"
        print("  %-8.4f %12d %10.4f %10.4f   %s" % (K, nc, R, R/R0 if R0 else 0, note))
        sys.stdout.flush()
