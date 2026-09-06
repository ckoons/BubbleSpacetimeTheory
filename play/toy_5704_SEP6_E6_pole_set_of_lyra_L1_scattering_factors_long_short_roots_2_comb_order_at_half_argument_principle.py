#!/usr/bin/env python3
"""Toy 5704 — E6: pole set of Lyra's L1 factors (be29f1dc), prereg e7e7e17e."""
import mpmath as mp, numpy as np, json, os, time
t0 = time.time(); HERE = os.path.dirname(os.path.abspath(__file__)); mp.mp.dps = 30; score = []
def sc(name, ok, detail=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {name}  {detail}", flush=True)
xi = lambda s: mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
GC = lambda s: 2 * (2 * mp.pi) ** (-s) * mp.gamma(s)
Lam = lambda s: GC(s + mp.mpf(1) / 2) * mp.zeta(s + mp.mpf(1) / 2) * mp.zeta(s - mp.mpf(1) / 2) * (1 - 2 ** (mp.mpf(1) / 2 - s))
eps = lambda s: 2 ** (mp.mpf(1) / 2 - s)
fL = lambda x: xi(x) / xi(x + 1)
fS = lambda l: xi(2 * l) / xi(2 * l + 1) * Lam(l) / (eps(l) * Lam(l + 1))
gam = [mp.im(mp.zetazero(n)) for n in range(1, 51)]
def pole_at(f, z0):
    """Newton on 1/f from z0 + small offset; returns (location, order estimate)."""
    z = mp.findroot(lambda z: 1 / f(z), z0 + mp.mpc('1e-4', '1e-4'), tol=1e-24, maxsteps=60)
    return z
def order(f, z0):
    ds = [mp.mpf(10) ** (-k) for k in (3, 4, 5, 6)]; ms = []
    for th in (0, 1, 2, 3):
        vals = [abs(f(z0 + d * mp.exp(1j * th))) for d in ds]
        ms.append(-(mp.log(vals[-1]) - mp.log(vals[0])) / (mp.log(ds[-1]) - mp.log(ds[0])))
    return float(sum(ms) / 4)
print("P1 long-root poles at -1/2 + i gamma_n", flush=True)
errL = [abs(pole_at(fL, mp.mpc(-0.5, g)) - mp.mpc(-0.5, g)) for g in gam]
ordL = [order(fL, mp.mpc(-0.5, g)) for g in gam[:5]]
sc("P1", max(errL) < 1e-10 and all(abs(o - 1) < 0.02 for o in ordL), f"max |Delta| = {mp.nstr(max(errL), 2)}; orders {np.round(ordL, 3).tolist()}")
print("P2 short-root poles at -1/4 + i gamma/2 and -1 + i gamma", flush=True)
errA = [abs(pole_at(fS, mp.mpc(-0.25, g / 2)) - mp.mpc(-0.25, g / 2)) for g in gam]
errB = [abs(pole_at(fS, mp.mpc(-1, g)) - mp.mpc(-1, g)) for g in gam]
ordA = [order(fS, mp.mpc(-0.25, g / 2)) for g in gam[:3]]; ordB = [order(fS, mp.mpc(-1, g)) for g in gam[:3]]
sc("P2", max(errA) < 1e-10 and max(errB) < 1e-10 and all(abs(o - 1) < 0.02 for o in ordA + ordB), f"max |Delta| A {mp.nstr(max(errA), 2)}, B {mp.nstr(max(errB), 2)}; orders A {np.round(ordA,3).tolist()} B {np.round(ordB,3).tolist()}")
print("P3 the 2-comb", flush=True)
sp = 2 * mp.pi / mp.log(2); comb = {}
for kk in [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]:
    z0 = mp.mpc(-0.5, kk * sp); z = pole_at(fS, z0); comb[kk] = (abs(z - z0), order(fS, z0))
o0 = order(fS, mp.mpc(-0.5, 0))
sc("P3", all(v[0] < 1e-10 and abs(v[1] - 1) < 0.02 for v in comb.values()) and abs(o0) < 0.02, f"spacing {mp.nstr(sp, 12)}; max |Delta| {mp.nstr(max(v[0] for v in comb.values()), 2)}; orders k=1..5 {[round(comb[k][1],3) for k in (1,2,3,4,5)]}; order at k=0: {o0:.3f}")
print("P4 cancellations: lambda = i gamma_n not a pole; order at 1/2", flush=True)
oi = [order(fS, mp.mpc(0, g)) for g in gam[:10]]; oh = order(fS, mp.mpf(1) / 2)
print(f"  orders at i*gamma_n (n<=10): {np.round(oi, 3).tolist()};  order at lambda = 1/2: {oh:.4f};  f_S(1/2 + 1e-8) = {mp.nstr(fS(mp.mpf(1)/2 + mp.mpf('1e-8')), 8)}")
sc("P4", all(abs(o) < 0.02 for o in oi) and abs(oh) < 0.02, "i*gamma_n regular; lambda=1/2 order 0 (my reading) — Lyra's 'simple pole' sentence is the thing tested")
print("P5 argument principle on -1.2 < Re < 0.8, 0.1 < Im < 30", flush=True)
s1, s2, t1, t2, h = -1.2, 0.8, 0.1, 30.0, 0.02
nR = int((t2 - t1) / h); nT = int((s2 - s1) / h)
pts = [mp.mpc(s2, t1 + (t2 - t1) * k / nR) for k in range(nR + 1)] + [mp.mpc(s2 - (s2 - s1) * k / nT, t2) for k in range(1, nT + 1)] + [mp.mpc(s1, t2 - (t2 - t1) * k / nR) for k in range(1, nR + 1)] + [mp.mpc(s1 + (s2 - s1) * k / nT, t1) for k in range(1, nT + 1)]
ph = np.unwrap(np.angle(np.array([complex(fS(p)) for p in pts]))); w = (ph[-1] - ph[0]) / (2 * np.pi); mx = float(np.max(np.abs(np.diff(ph))))
nz = sum(1 for g in gam if g < 60) + 3; npo = sum(1 for g in gam if g < 60) + sum(1 for g in gam if g < 30) + 3
sc("P5", abs(w - (nz - npo)) < 0.1, f"winding {w:.4f} (max step {mx:.2f}); predicted zeros {nz} - poles {npo} = {nz - npo}")
print(f"\nSCORE {sum(score)}/{len(score)}   [{time.time()-t0:.0f}s]")
json.dump({'errL_max': mp.nstr(max(errL), 3), 'errA_max': mp.nstr(max(errA), 3), 'errB_max': mp.nstr(max(errB), 3), 'comb': {k: [mp.nstr(v[0], 3), v[1]] for k, v in comb.items()}, 'order_half': oh, 'orders_igamma': oi, 'winding': float(w), 'score': f"{sum(score)}/{len(score)}"}, open(os.path.join(HERE, '.poles_5704.json'), 'w'), indent=1)
