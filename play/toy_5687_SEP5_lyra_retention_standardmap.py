"""TEST 13 — the Chirikov standard map as a non-combinatorial record system.
Lyra for Casey, 2026-09-05. Predictions efe0eff8, registered before launch.
x' = x + y' (mod 2pi),  y' = y + K sin x (mod 2pi).  K_c = 0.971635 (last KAM torus).
"""
import math, sys
import numpy as np

TWO_PI = 2*math.pi

def components_for(K, N, samples=3):
    """Coarse-grain to an NxN grid; connect cells joined by the map or its inverse."""
    parent = np.arange(N*N)
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb: parent[ra] = rb
    offs = [(i+0.5)/samples for i in range(samples)]
    for gi in range(N):
        for gj in range(N):
            src = gi*N + gj
            for ox in offs:
                for oy in offs:
                    x = (gi+ox)*TWO_PI/N; y = (gj+oy)*TWO_PI/N
                    # forward
                    yn = (y + K*math.sin(x)) % TWO_PI
                    xn = (x + yn) % TWO_PI
                    union(src, int(xn*N/TWO_PI)*N + int(yn*N/TWO_PI))
                    # inverse: x_p = x - y ; y_p = y - K sin(x_p)
                    xp = (x - y) % TWO_PI
                    yp = (y - K*math.sin(xp)) % TWO_PI
                    union(src, int(xp*N/TWO_PI)*N + int(yp*N/TWO_PI))
    roots = np.array([find(i) for i in range(N*N)])
    _, counts = np.unique(roots, return_counts=True)
    p = counts/counts.sum()
    R = float(-(p*np.log2(p)).sum())
    return len(counts), R

if __name__ == "__main__":
    Ks = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.9716,1.0,1.2,1.5,2.0]
    for N in (64,128,256):
        print("\n=== grid N=%d  (H1 control: K=0 must give exactly %d components, R=%.4f) ==="
              % (N, N, math.log2(N)))
        print("  %-8s %10s %10s %10s" % ("K","components","R (bits)","R/R(0)"))
        R0 = None
        for K in Ks:
            nc, R = components_for(K, N)
            if R0 is None: R0 = R
            flag = ""
            if K == 0.0:
                flag = "  <-- H1 %s" % ("HIT" if nc == N and abs(R-math.log2(N))<1e-9 else "MISS (nc=%d)"%nc)
            if abs(K-0.9716) < 1e-6: flag = "  <-- K_c"
            print("  %-8.4f %10d %10.4f %10.4f%s" % (K, nc, R, R/R0 if R0 else 0, flag))
            sys.stdout.flush()
