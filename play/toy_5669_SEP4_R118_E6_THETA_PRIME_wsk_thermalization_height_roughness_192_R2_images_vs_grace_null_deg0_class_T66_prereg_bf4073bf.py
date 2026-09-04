#!/usr/bin/env python3
"""E6 (Θ′): WSK thermalization of the height roughness W from the 192 R2-images vs Grace's 200 null subsets, deg-0 class of T(6,6)."""
import json, os, glob, math, random, time, hashlib
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(glob.glob(os.path.join(HERE, 'toy_5663_SEP4_*.py'))[0]).read().split("# ================================================================== SPHERE CONTROLS")[0]
ns = {"__file__": "x"}; exec(compile(src, "t5663", "exec"), ns)
torus, canon = ns["torus"], ns["canon"]
t0 = time.time(); T = torus(6, 6); NV = 36
LVEC = {1: (1, 0), 2: (0, 1), 3: (-1, -1)}
HEX = {(1, 0): (1.0, 0.0), (0, 1): (-0.5, math.sqrt(3) / 2), (-1, -1): (-0.5, -math.sqrt(3) / 2)}
def hexv(v): return (v[0] * HEX[(1, 0)][0] + v[1] * HEX[(0, 1)][0], v[0] * HEX[(1, 0)][1] + v[1] * HEX[(0, 1)][1])
# BFS height (single-valued on the deg-0 class); roughness in hex metric
adj = T.adj; sigma = T.sigma
def roughness(f):
    h = [None] * NV; h[0] = (0, 0); st = [0]
    while st:
        u = st.pop()
        for w in adj[u]:
            if h[w] is None:
                s = sigma[(u, w)]; L = LVEC[f[u] ^ f[w]]; h[w] = (h[u][0] + s * L[0], h[u][1] + s * L[1]); st.append(w)
    pts = [hexv(x) for x in h]; mx = sum(p[0] for p in pts) / NV; my = sum(p[1] for p in pts) / NV
    return sum((p[0] - mx) ** 2 + (p[1] - my) ** 2 for p in pts) / NV
def ktot(f):
    tot = 0
    for a in range(4):
        for b in range(a + 1, 4):
            seen = [False] * NV
            for v in range(NV):
                if seen[v] or f[v] not in (a, b): continue
                tot += 1; st = [v]; seen[v] = True
                while st:
                    u = st.pop()
                    for w in adj[u]:
                        if not seen[w] and f[w] in (a, b): seen[w] = True; st.append(w)
    return tot
def wsk_step(f, rng):
    a, b = rng.sample(range(4), 2)
    seen = [False] * NV
    for v in range(NV):
        if seen[v] or f[v] not in (a, b): continue
        comp = []; st = [v]; seen[v] = True
        while st:
            u = st.pop(); comp.append(u)
            for w in adj[u]:
                if not seen[w] and f[w] in (a, b): seen[w] = True; st.append(w)
        if rng.random() < 0.5:
            for u in comp: f[u] = a + b - f[u]
# class law of W
rows = json.load(open(os.path.join(HERE, '.e5_5663_rows_T6x6.json')))
reps = rows['reps']; R = rows['rows']
Wclass = []
for h, r in zip(reps, R):
    if r['deg'] == 0: Wclass.append(round(roughness(list(bytes.fromhex(h))), 9))
Wclass.sort(); n0 = len(Wclass); print(f"class law of W on {n0} deg-0 reps: median {Wclass[n0//2]:.4f} mean {sum(Wclass)/n0:.4f} min {Wclass[0]:.4f} max {Wclass[-1]:.4f}  [{time.time()-t0:.0f}s]", flush=True)
qs = [Wclass[int(n0 * q)] for q in (0.2, 0.4, 0.6, 0.8)]
def binof(w): return sum(1 for q in qs if w > q + 1e-12)
pclass = [0.0] * 5
for w in Wclass: pclass[binof(w)] += 1.0 / n0
print(f"  quantile bins {['%.3f' % q for q in qs]}; class bin masses {['%.3f' % p for p in pclass]}")
def tv(ws):
    p = [0.0] * 5
    for w in ws: p[binof(w)] += 1.0 / len(ws)
    return 0.5 * sum(abs(p[i] - pclass[i]) for i in range(5))
TSTEPS = 60
def run_set(starts, chains, seed):
    rng = random.Random(seed); series = [[] for _ in range(TSTEPS + 1)]
    for s in starts:
        for _ in range(chains):
            f = list(s); series[0].append(roughness(f))
            for t in range(1, TSTEPS + 1):
                wsk_step(f, rng); series[t].append(roughness(f))
    return [tv(ws) for ws in series]
images = json.load(open(os.path.join(HERE, '.e6_T_R2_images.json')))['images']
W0 = sorted(roughness(list(g)) for g in images)
print(f"S (R2 images): {len(images)}; W at t=0: median {W0[len(W0)//2]:.4f} mean {sum(W0)/len(W0):.4f} (class median {Wclass[n0//2]:.4f}); K_tot mean {sum(ktot(list(g)) for g in images)/len(images):.2f}", flush=True)
tvS = run_set(images, 100, 1)
print(f"TV_S(t): {['%.3f' % x for x in tvS[:12]]} ... t=30 {tvS[30]:.3f} t=60 {tvS[60]:.3f}  [{time.time()-t0:.0f}s]", flush=True)
null = json.load(open(os.path.join(HERE, '.e6_null_subsets_T66.json')))
nh = hashlib.sha256(json.dumps(null, sort_keys=True).encode()).hexdigest()[:16]
print(f"null file: K={null['K']} m0={null['m0']} m1={null['m1']} sha256 {nh}")
tvN = []; W0N = []
for k, S in enumerate(null['subsets']):
    S = [tuple(s) for s in S]; W0N.append(sorted(roughness(list(s)) for s in S)[len(S)//2])
    tvN.append(run_set(S, 5, 1000 + k))
    if k % 50 == 49: print(f"   null {k+1}/{len(null['subsets'])} [{time.time()-t0:.0f}s]", flush=True)
def pct(xs, q): xs = sorted(xs); return xs[min(len(xs) - 1, int(q * len(xs)))]
def tA(curve): return next((t for t, x in enumerate(curve) if x <= 0.25), None)
print("\nRESULTS")
for t in (0, 1, 2, 3, 5, 10, 20, 40, 60):
    col = [c[t] for c in tvN]; print(f"  t={t:2d}: TV_S {tvS[t]:.3f} | null median {pct(col,0.5):.3f}  5% {pct(col,0.05):.3f}  95% {pct(col,0.95):.3f}")
null95_0 = pct([c[0] for c in tvN], 0.95)
cold = tvS[0] > null95_0
print(f"  (Θ′-0) cold start: TV_S(0) = {tvS[0]:.3f} vs null 95th pct {null95_0:.3f} -> {'ABOVE (held)' if cold else 'INSIDE (killed)'}; W0 median S {W0[len(W0)//2]:.4f} vs null-subset medians median {pct(W0N,0.5):.4f} [{pct(W0N,0.05):.4f}, {pct(W0N,0.95):.4f}] vs class {Wclass[n0//2]:.4f}")
tAS = tA(tvS); tAN = [tA(c) for c in tvN]; tAN_def = [x for x in tAN if x is not None]
print(f"  (Θ′-t) t_A(S) = {tAS}; null t_A: median {pct(tAN_def,0.5) if tAN_def else None}, 5% {pct(tAN_def,0.05) if tAN_def else None}, 95% {pct(tAN_def,0.95) if tAN_def else None}, undefined {tAN.count(None)}/{len(tAN)}")
inside = tAS is not None and tAN_def and pct(tAN_def, 0.05) <= tAS <= pct(tAN_def, 0.95)
print(f"  K-b: t_A(S) inside the null band -> {'FIRES (no cold-start content in the mixing time)' if inside else 'does not fire'}")
json.dump({"tvS": tvS, "tvN": tvN, "W0_S": W0, "null_sha": nh, "tA_S": tAS, "tA_null": tAN}, open(os.path.join(HERE, ".e6_theta_prime_results.json"), "w"))
print(f"[{time.time()-t0:.0f}s]")
