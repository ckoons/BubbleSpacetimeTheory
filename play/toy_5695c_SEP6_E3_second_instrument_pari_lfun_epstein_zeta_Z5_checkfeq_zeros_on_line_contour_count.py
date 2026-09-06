#!/usr/bin/env python3
"""Toy 5695c — E3 second instrument (independent code path): PARI/GP lfun (Dokchitser's algorithm) via cypari2 on
Lambda(s) = 4^{s/2} Gamma_C(s) Z5(s) = 2 pi^{-s} Gamma(s) Z5(s), k = 5/2, conductor 4, root number 1, residue 2 at s = 5/2."""
import cypari2, numpy as np, math, time, json, os
t0 = time.time(); HERE = os.path.dirname(os.path.abspath(__file__))
pari = cypari2.Pari(); pari.default("realprecision", 38)
X = 6000; Bx = math.isqrt(X); th = np.zeros(X + 1, dtype=np.int64)
for x in range(-Bx, Bx + 1):
    if x * x <= X: th[x * x] += 1
r5 = th.copy()
for _ in range(4): r5 = np.convolve(r5, th)[:X + 1]
pari("R5 = [" + ",".join(str(int(v)) for v in r5[1:]) + "]")
pari("L = lfuncreate([R5, 0, [0,1], 5/2, 4, 1, 2])")
print("lfuncheckfeq (log10 defect):", pari("lfuncheckfeq(L)"))
print("Lambda_PARI(1.25) =", pari("lfunlambda(L, 1.25)"), " Z5(4) =", pari("lfun(L, 4)"))
print("Z5(4) direct (X=6000) =", float((r5[1:] * np.arange(1, X + 1) ** -4.0).sum()))
zl = pari("lfunzeros(L, 60)")
print(f"on-line zeros below 60 (lfunzeros): {len(zl)}  first: {[round(float(z), 4) for z in zl[:12]]}  [{time.time()-t0:.0f}s]", flush=True)
pari("""wind(s1, s2, t1, t2, h) = {
  my(pts = List(), nR = ceil((t2-t1)/h), nT = ceil((s2-s1)/h), tot = 0, prev, cur, d, mx = 0);
  for(k=0, nR, listput(pts, s2 + I*(t1 + (t2-t1)*k/nR)));
  for(k=1, nT, listput(pts, s2 - (s2-s1)*k/nT + I*t2));
  for(k=1, nR, listput(pts, s1 + I*(t2 - (t2-t1)*k/nR)));
  for(k=1, nT, listput(pts, s1 + (s2-s1)*k/nT + I*t1));
  prev = arg(lfunlambda(L, pts[1]));
  for(i=2, #pts, cur = arg(lfunlambda(L, pts[i])); d = cur - prev; while(d > Pi, d -= 2*Pi); while(d < -Pi, d += 2*Pi); if(abs(d) > mx, mx = abs(d)); tot += d; prev = cur);
  [round(tot/(2*Pi)), mx]; }""")
for T in (30, 60):
    w = pari(f"wind(-1/2, 3, 1/10, {T}, 1/10)"); print(f"contour count [-1/2,3]x(0.1,{T}]: {w}  [{time.time()-t0:.0f}s]", flush=True)
json.dump({'checkfeq': str(pari("lfuncheckfeq(L)")), 'zeros_on_line_60': [float(z) for z in zl]}, open(os.path.join(HERE, '.epstein_5695c.json'), 'w'), indent=1)
print(f"[{time.time()-t0:.0f}s]")
