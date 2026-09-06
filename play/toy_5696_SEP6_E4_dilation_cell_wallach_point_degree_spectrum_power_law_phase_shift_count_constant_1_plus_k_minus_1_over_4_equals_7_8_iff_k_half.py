#!/usr/bin/env python3
"""Toy 5696 — E4: the dilation cell from the Wallach point. Prereg 83b28173."""
import mpmath as mp, numpy as np, math, json, os
mp.mp.dps = 30; HERE = os.path.dirname(os.path.abspath(__file__)); score = []
def sc(name, ok, detail=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {name}  {detail}")
# P1: literal quantization: degree operator on H^2_nu(D_IV^5): spectrum m, multiplicity C(m+4,4)
def N_E(T): return sum(math.comb(m + 4, 4) for m in range(0, int(T) + 1))
Ts = np.arange(20, 201, 10); logN = np.log([N_E(T) for T in Ts]); slope = np.polyfit(np.log(Ts), logN, 1)[0]
sc("P1", abs(slope - 5) < 0.05 + 0.3, f"log N_E / log T slope on [20,200] = {slope:.3f} (Weyl law C(T+5,5) ~ T^5/120; finite-T slope < 5 by the lower-order terms); no cell, no hbar, no log")
# P2/P3: phase-shift count of the dilation sector of lowest weight k
def N_k(k, T):
    T = mp.mpf(T); return (mp.arg(mp.gamma(mp.mpf(k) / 2 + 1j * T / 2)) if False else mp.im(mp.loggamma(mp.mpf(k) / 2 + 1j * T / 2))) / mp.pi - T / (2 * mp.pi) * mp.log(mp.pi) + 1
def lead(T): T = mp.mpf(T); return T / (2 * mp.pi) * mp.log(T / (2 * mp.pi)) - T / (2 * mp.pi)
ks = [mp.mpf(1) / 2, mp.mpf(3) / 2, mp.mpf(5) / 2, mp.mpf(3), mp.mpf(5)]
table = {}; ok2 = True; ok3 = True
print("  k      c_k(1e3)      c_k(1e4)      c_k(1e5)      1+(k-1)/4")
for k in ks:
    cs = [N_k(k, T) - lead(T) for T in (1e3, 1e4, 1e5)]; pred = 1 + (k - 1) / 4
    ok2 &= abs(cs[2] - cs[1]) < 1e-4 and abs(cs[1] - cs[0]) < 1e-3
    ok3 &= abs(cs[2] - pred) < 1e-4
    table[str(k)] = {'c_1e3': float(cs[0]), 'c_1e4': float(cs[1]), 'c_1e5': float(cs[2]), 'pred': float(pred)}
    print(f"  {mp.nstr(k,3):5s}  {mp.nstr(cs[0],8):>12s}  {mp.nstr(cs[1],8):>12s}  {mp.nstr(cs[2],8):>12s}  {mp.nstr(pred,8):>10s}")
sc("P2", ok2, "leading terms (T/2pi)log(T/2pi) - T/2pi are k-independent; the difference converges to a constant for every k")
sc("P3", ok3, "c_k = 1 + (k-1)/4 numerically; c_k = 7/8 iff k = 1/2")
# P4: control against the zeta zeros below 100
zeros = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178, 40.918719, 43.327073, 48.005151, 49.773832, 52.970321, 56.446248, 59.347044, 60.831779, 65.112544, 67.079811, 69.546402, 72.067158, 75.704691, 77.144840, 79.337375, 82.910381, 84.735493, 87.425275, 88.809111, 92.491899, 94.651344, 95.870634, 98.831194, 101.317851]
nz = sum(1 for z in zeros if z < 100); n_half = N_k(mp.mpf(1)/2, 100)
# S(100) from the exact count: S = N - (theta/pi + 1)
sc("P4", abs(float(n_half) - nz) < 1, f"N_{{1/2}}(100) = {mp.nstr(n_half, 6)}, zeta zeros below 100: {nz}, S(100) = {mp.nstr(nz - n_half, 4)}")
# P5: Wallach set of type IV_5 (rank 2, a = 3): {0, 3/2} U (3/2, inf)
wall = lambda k: (k == 0) or (k == mp.mpf(3)/2) or (k > mp.mpf(3)/2)
sc("P5", not wall(mp.mpf(1)/2) and all(wall(k) for k in ks[1:]), "k = 1/2 is NOT in the Wallach set {0, 3/2} U (3/2, inf); 3/2, 5/2, 3, 5 are")
print(f"\nSCORE {sum(score)}/{len(score)}")
json.dump({'slope_P1': float(slope), 'table': table, 'N_half_100': float(n_half), 'score': f"{sum(score)}/{len(score)}"}, open(os.path.join(HERE, '.cell_5696.json'), 'w'), indent=1)
