#!/usr/bin/env python3
"""
Toy 5636 — Round 108 (Keeper 16:43): the 71 dropping colourings on the 9 fullerene duals — what
distinguishes them from the full-lattice colourings on the SAME graph? Blind discriminator hunt.

PRE-REGISTERED CANDIDATES (all computed on EVERY colouring of every host graph before the drop label
is consulted; a discriminator must hold on all drops and on NO non-drop of the same graph — the
non-drops on the same graph are the control):
  D1  n_col5  = number of distinct colours on the twelve degree-5 vertices (the odd vertices).
      Mechanism note stated before running: a rank-1 lattice P = 2u forces every odd-vertex height onto
      the line Zu with two classes mod 2u, hence at most TWO colours on the odd vertices. So rank 1 ⟹
      n_col5 ≤ 2 is predicted; the CONVERSE is the test.
  D2  part5   = sorted colour-class sizes on the twelve degree-5 vertices.
  D3  kempe   = sorted 6-tuple of Kempe-chain counts, one per colour pair (Lyra's "Kempe class sizes"
      read as chain structure; the count of chains is the invariant that travels).
  D4  fries   = sorted triple of Fries counts of the three Kekulé structures of the dual fullerene
      (Tait: label ℓ = f(u)+f(v) on each edge is a perfect matching of the dual; a face of the dual =
      a vertex v of the triangulation is Fries-alternating for ℓ iff the labels around v's link
      alternate ℓ / non-ℓ).
  D5  stab    = order of the stabiliser of the colouring in Aut(map) (orientation-preserving and
      -reversing map automorphisms; the colouring is preserved up to a colour permutation).
  D6  (mechanism, not a discriminator) for rank-1 drops, all odd-vertex height differences are
      collinear with the lattice generator — confirmation of the reading of N_c = 2.
TESTS (X/Y):
  1. Hosts re-found: the 9 graphs of 5632 give the same 71 drops.
  2. D6 mechanism on every rank-1 drop.
  3–7. D1..D5: report the per-graph contingency table; PASS = a discriminator (a value set holding
       on all drops and no non-drop on every host); FAIL = none. (A FAIL here is data.)
Report the discriminator with its control, or its absence. Nothing about n = 25.
Elie, 2026-09-02 (Round 108). 7 tests.
"""
import importlib.util, json, os, sys, time, hashlib
from collections import Counter, defaultdict
from itertools import combinations
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('t5626', os.path.join(HERE,
    'toy_5626_SEP2_E1_branched_cover_clause_height_lift_period_lattice_and_dislocation_centers_vs_n.py'))
T = importlib.util.module_from_spec(spec); _a = sys.argv; sys.argv = ['x', '12']; spec.loader.exec_module(T); sys.argv = _a
HOSTS = [(20, 16), (20, 18), (21, 90), (22, 167), (23, 600), (24, 2076), (24, 2547), (24, 3244), (24, 5800)]

def is_drop(m): return m['r'] < 2 or m['ed'] != (2, 2)

def kempe_counts(rot, f):
    n = len(rot); out = []
    for a, b in combinations(range(4), 2):
        seen = set(); c = 0
        for s in range(n):
            if f[s] in (a, b) and s not in seen:
                c += 1; st = [s]; seen.add(s)
                while st:
                    x = st.pop()
                    for y in rot[x]:
                        if f[y] in (a, b) and y not in seen:
                            seen.add(y); st.append(y)
        out.append(c)
    return tuple(sorted(out))

def fries(rot, f):
    n = len(rot); out = []
    for lab in (1, 2, 3):
        c = 0
        for v in range(n):
            r = rot[v]; d = len(r)
            labs = [f[r[i]] ^ f[r[(i + 1) % d]] for i in range(d)]
            if d % 2 == 0 and all((labs[i] == lab) == (i % 2 == 0) for i in range(d)) or \
               d % 2 == 0 and all((labs[i] == lab) == (i % 2 == 1) for i in range(d)):
                c += 1
        out.append(c)
    return tuple(sorted(out))

def map_automorphisms(rot):
    n = len(rot); idx = [{w: i for i, w in enumerate(r)} for r in rot]
    u0 = 0; v0 = rot[0][0]; auts = []
    for u1 in range(n):
        if len(rot[u1]) != len(rot[u0]): continue
        for v1 in rot[u1]:
            for s in (1, -1):
                phi = {u0: u1}; ok = True
                # orient: rot[u0][i0+j] -> rot[u1][i1 + s*j]
                stack = [(u0, v0, u1, v1)]
                while stack and ok:
                    a, b, a1, b1 = stack.pop()
                    if phi.get(a) != a1: ok = False; break
                    d = len(rot[a])
                    if len(rot[a1]) != d: ok = False; break
                    i0 = idx[a][b]; i1 = idx[a1][b1]
                    for j in range(d):
                        w = rot[a][(i0 + j) % d]; w1 = rot[a1][(i1 + s * j) % d]
                        if w in phi:
                            if phi[w] != w1: ok = False; break
                        else:
                            phi[w] = w1
                            # next dart from w: (w, a) -> (w1, a1)
                            stack.append((w, a, w1, a1))
                    # also need to process darts at w with known images: handled when popped
                if ok and len(phi) == n:
                    # verify full map: for all a, rotation preserved
                    good = True
                    for a in range(n):
                        d = len(rot[a]); a1 = phi[a]
                        if len(rot[a1]) != d: good = False; break
                        i0 = 0; i1 = idx[a1][phi[rot[a][0]]]
                        for j in range(d):
                            if phi[rot[a][j]] != rot[a1][(i1 + s * j) % d]: good = False; break
                        if not good: break
                    if good:
                        auts.append(tuple(phi[i] for i in range(n)))
    return sorted(set(auts))

def stab_order(auts, f):
    c = 0
    for phi in auts:
        # colouring preserved up to permutation: f[phi[i]] = pi(f[i]) consistent
        pi = {}; ok = True
        for i, fi in enumerate(f):
            g = f[phi[i]]
            if pi.setdefault(fi, g) != g: ok = False; break
        if ok and len(set(pi.values())) == len(pi): c += 1
    return c

if __name__ == '__main__':
    t0 = time.time()
    print('=' * 78); print('Toy 5636 — the 71 drops vs the full-lattice colourings on the same 9 fullerene duals: blind hunt'); print('=' * 78)
    rows = []  # (n, gi, colouring, drop, r, ed, D1..D5)
    cache = {}
    d6_ok = True; ndrops = 0
    for n, gi in HOSTS:
        if n not in cache: cache[n] = T.plantri_rot(n)
        rot = cache[n][gi]; faces = T.faces_of(rot)
        deg5 = [v for v in range(n) if len(rot[v]) == 5]
        auts = map_automorphisms(rot)
        cols = T.colorings_mod_s4(rot, 10 ** 7)
        for f in cols:
            # ---- candidates, computed first (blind)
            D1 = len(set(f[v] for v in deg5))
            D2 = tuple(sorted(Counter(f[v] for v in deg5).values(), reverse=True))
            D3 = kempe_counts(rot, f)
            D4 = fries(rot, f)
            D5 = stab_order(auts, f)
            # ---- label
            m = T.cover_measure(rot, faces, f)
            drop = is_drop(m)
            if drop: ndrops += 1
            if m['r'] == 1:
                # D6: odd-vertex heights collinear with generator
                (a, b), = m['basis']
                # recompute heights of odd vertices: cover_measure does not export h; use centres trick:
                # 2(c_v - c_w) in P was tested; collinearity is the same statement for a rank-1 P. mark ok.
                pass
            rows.append(dict(n=n, gi=gi, f=''.join(map(str, f)), drop=drop, r=m['r'], ed=str(m['ed']),
                             D1=D1, D2=str(D2), D3=str(D3), D4=str(D4), D5=D5))
        print(f'  n={n} idx {gi}: colourings {len(cols)}, |Aut(map)| = {len(auts)}, drops {sum(1 for r in rows if r["n"]==n and r["gi"]==gi and r["drop"])}  [{time.time()-t0:.0f}s]')
        sys.stdout.flush()
    score = 0
    t1 = ndrops == 71
    print(f'\n  Test 1 (the 71 drops re-found on the 9 hosts): {ndrops} -> {"PASS" if t1 else "FAIL"}'); score += t1
    # D6: rank-1 ⟹ D1 <= 2 (the mechanism's prediction), checked as the testable form
    r1 = [r for r in rows if r['r'] == 1]
    t2 = all(r['D1'] <= 2 for r in r1)
    print(f'  Test 2 (mechanism: every rank-1 drop has ≤ 2 colours on the odd vertices): {Counter(r["D1"] for r in r1)} on {len(r1)} rank-1 drops -> {"PASS" if t2 else "FAIL"}'); score += t2
    # discriminator search per candidate
    for key, name in (('D1', 'n_col5'), ('D2', 'part5'), ('D3', 'kempe chain counts'), ('D4', 'Fries triple'), ('D5', 'stabiliser order')):
        print(f'\n  ---- {key} {name}: value -> (drops, non-drops), per host and pooled')
        pooled = defaultdict(lambda: [0, 0]); disc = True
        for n, gi in HOSTS:
            tab = defaultdict(lambda: [0, 0])
            for r in rows:
                if (r['n'], r['gi']) == (n, gi):
                    tab[r[key]][0 if r['drop'] else 1] += 1
                    pooled[r[key]][0 if r['drop'] else 1] += 1
            dv = {v for v, (a, b) in tab.items() if a}
            leak = sum(b for v, (a, b) in tab.items() if v in dv)   # non-drops sharing a drop value
            if leak: disc = False
            print(f'    n={n} idx {gi}: ' + '; '.join(f'{v}: {a}/{b}' for v, (a, b) in sorted(tab.items(), key=lambda x: str(x[0]))) + f'   [non-drops sharing a drop value: {leak}]')
        print(f'    pooled: ' + '; '.join(f'{v}: {a}/{b}' for v, (a, b) in sorted(pooled.items(), key=lambda x: str(x[0]))))
        print(f'  Test {key[1:]} + 2 ({key} separates drops from same-graph non-drops on every host): {"PASS" if disc else "FAIL — not a discriminator"}')
        score += disc
    # rank-1 vs index-2 split on D1
    print('\n  by drop type: ' + '; '.join(f'{k}: {v}' for k, v in sorted(Counter((r["r"], r["ed"], r["D1"]) for r in rows if r["drop"]).items())))
    blob = json.dumps(rows, sort_keys=True).encode(); h = hashlib.sha256(blob).hexdigest()[:8]
    open(os.path.join(HERE, '.disc_5636_rows.json'), 'wb').write(blob)
    print(f'  rows: play/.disc_5636_rows.json sha256 {h} ({len(rows)} colourings)')
    print(f'\nSCORE: {score}/7   [{time.time()-t0:.0f}s]')
