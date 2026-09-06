#!/usr/bin/env python3
"""Toy 5704b — E6, Cal's blind hold (2332e3a8): short-root factor in the SPLIT form g_S(z) = xi(2z) xi(z-1/2) / [xi(2z+1) xi(z+3/2)]
(Lyra's naive formula = Cal's hold), scored against L1 Section 5's kills: pole set on Re z = -1/4, -1; the comb; orders at
z = 1/2 and 3/2 in Re z > 0 (double pole = kill). Same instrument as 5704; Lyra's JL form alongside for the same points."""
import mpmath as mp, numpy as np, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); mp.mp.dps = 30
xi = lambda s: mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
GC = lambda s: 2 * (2 * mp.pi) ** (-s) * mp.gamma(s)
Lam = lambda s: GC(s + mp.mpf(1) / 2) * mp.zeta(s + mp.mpf(1) / 2) * mp.zeta(s - mp.mpf(1) / 2) * (1 - 2 ** (mp.mpf(1) / 2 - s))
fS = lambda l: xi(2 * l) / xi(2 * l + 1) * Lam(l) / (2 ** (mp.mpf(1) / 2 - l) * Lam(l + 1))          # Lyra (JL)
gS = lambda z: xi(2 * z) * xi(z - mp.mpf(1) / 2) / (xi(2 * z + 1) * xi(z + mp.mpf(3) / 2))         # Cal / split
def order(f, z0):
    ds = [mp.mpf(10) ** (-k) for k in (3, 4, 5, 6)]; ms = []
    for th in (0, 1, 2, 3):
        vals = [abs(f(z0 + d * mp.exp(1j * th))) for d in ds]
        ms.append(-(mp.log(vals[-1]) - mp.log(vals[0])) / (mp.log(ds[-1]) - mp.log(ds[0])))
    return round(float(sum(ms) / 4), 3)
gam = [mp.im(mp.zetazero(n)) for n in range(1, 6)]; sp = 2 * mp.pi / mp.log(2)
pts = {'-1/4+i g1/2': mp.mpc(-0.25, gam[0] / 2), '-1+i g1': mp.mpc(-1, gam[0]), 'comb k=1': mp.mpc(-0.5, sp), 'comb k=2': mp.mpc(-0.5, 2 * sp), 'z=0': mp.mpc(0), 'z=1/2': mp.mpc(0.5), 'z=3/2': mp.mpc(1.5), 'z=-1/2': mp.mpc(-0.5), 'i g1': mp.mpc(0, gam[0]), '1/4+i g1/2 (zero?)': mp.mpc(0.25, gam[0] / 2)}
print(f"{'point':22s} {'order Lyra(JL)':>16s} {'order Cal(split)':>18s}")
out = {}
for k, z in pts.items():
    oL, oC = order(fS, z), order(gS, z); out[k] = (oL, oC); print(f"{k:22s} {oL:16.3f} {oC:18.3f}")
print("\nreading: order +1 = simple pole, +2 = double pole, 0 = regular, -1 = simple zero")
print("Cal's split form: double pole at z = 1/2 in Re z > 0 ->", "KILL fires (L1 Section 5: 'a double pole anywhere in Re lambda > 0')" if abs(out['z=1/2'][1] - 2) < 0.05 else "no double pole")
print("Cal's split form: comb at -1/2 + 2 pi i k/ln 2 ->", "ABSENT" if abs(out['comb k=1'][1]) < 0.05 else "present")
print("Lyra's JL form: comb present ->", abs(out['comb k=1'][0] - 1) < 0.05, "; z = 1/2 regular (order 0):", abs(out['z=1/2'][0]) < 0.05, "; positive-chamber pole at z = 3/2:", out['z=3/2'])
# unitarity on the axis for both, |c(it)|
ax = [abs(fS(mp.mpc(0, t))) for t in (3.3, 11.1)], [abs(gS(mp.mpc(0, t))) for t in (3.3, 11.1)]
print("|c(it)| on the axis: Lyra", [mp.nstr(v, 8) for v in ax[0]], " Cal", [mp.nstr(v, 8) for v in ax[1]])
json.dump({k: list(v) for k, v in out.items()}, open(os.path.join(HERE, '.poles_5704b.json'), 'w'), indent=1)
