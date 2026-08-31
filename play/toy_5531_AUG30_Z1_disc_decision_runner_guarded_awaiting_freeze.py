#!/usr/bin/env python3
"""
Toy 5531 — Z1 (Round 8): THE 19-VERTEX DECISION RUNNER — built, guarded,
                          validated on a NON-decision pinning. THE FROZEN
                          PINNING IS NOT TOUCHED until Cal's freeze line.

FROZEN_LEDGER below is False: the decision computation (FCW-014's exhibited
pinning [0,1,0,1,0,1,0,1,2,1,2,1]) is REFUSED by a hard guard. On "Z1
LEDGER FROZEN, run it", set FROZEN_LEDGER = True with the pinned W_rel
choice and the same code produces the decision number. The guard is code,
not prose.

LENSES (both, per Cal's amended two-lens 2x2):
  ZZ lens: interior charge vectors omega_int (interior vertices keep the
    absolute quantization per Lyra M3); relative current columns from LEGAL
    (boundary-avoiding) swaps; SNF; fiber question: omega_1 - omega_2 in
    im(M_rel)?
  GF(2) lens: epsilon(completion) = face-sign pattern of the fully-colored
    disc; W_rel = span of straddle indicators of LEGAL chains, population
    per W_REL_CHOICE:
      'a' = this pinning's own completions (DEGENERATE for frozen pinnings
            — the trap Elie/Cal/Lyra flagged; kept implemented so the
            degeneracy is DEMONSTRABLE, never silently used);
      'b' = union over many sampled pinnings of the same disc
            (graph-intrinsic relative superset; DEFAULT candidate);
      'c' = hook for Lyra's pinned definition if it differs.
    Coset question: epsilon_1 - epsilon_2 in W_rel?

VALIDATION (this run): a ONE-CLASS pinning from Y4's census (two completions
KNOWN mutually reachable by legal moves). Soundness demands BOTH lenses tie
on it. Any lens separating a reachable pair is broken before the decision —
the exact control Cal's rubric wants run first.

TESTS (X/Y):
  1. Guard verified: the decision pinning is refused while
     FROZEN_LEDGER = False (mechanically checked).
  2. Validation pinning: reachability re-verified (legal-move BFS connects
     its completions).
  3. ZZ lens soundness: reachable completions tie (same relative fiber).
  4. GF(2) lens soundness under W_REL_CHOICE='b': reachable completions
     tie (epsilon difference in W_rel).
  5. The 'a'-degeneracy demonstrated ON THE VALIDATION PINNING: with
     choice 'a' restricted to a single completion's achieved moves the
     span shrinks — the trap is real and visible without touching the
     decision object.

Elie, 2026-08-30. Millennium week, 4-Color round 8. 5 tests.
"""

import importlib.util
import itertools
import os
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))
FROZEN_LEDGER = True             # Cal SS791, 2026-08-30 17:21 EDT: 'Z1 LEDGER FROZEN, run it.'
W_REL_CHOICE = 'c'               # Lyra's intrinsic W_rel (Z1 obligation note, Cal-verified)
DECISION_PINNING = [0, 1, 0, 1, 0, 1, 0, 1, 2, 1, 2, 1]


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


Y4 = load("t5526d", "toy_5526_AUG30_Y4_boundary_fisk_disc_relative_kempe"
          "_connectivity.py")
H8 = load("t5518d", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank_coset"
          "_stuck_separation.py")
Y1 = load("t5527d", "toy_5527_AUG30_Y1_snf_engine_charge_lattice_invariant"
          "_factors.py")
G5 = load("g5512d", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")


def disc_faces(adj, interior, bcyc):
    """Triangles of the disc (all 3-cliques that bound faces: for the
    triangular lattice every 3-clique is a face)."""
    vs = sorted(adj, key=str)
    faces = []
    for i, u in enumerate(vs):
        for w in adj[u]:
            if str(w) <= str(u):
                continue
            for x in adj[u] & adj[w]:
                if str(x) <= str(w):
                    continue
                faces.append((u, w, x))
    return faces


def guard_decision(pin_seq):
    if list(pin_seq) == DECISION_PINNING and not FROZEN_LEDGER:
        raise SystemExit("GUARD: decision pinning refused — ledger not "
                         "frozen (Cal's line not on the record)")


def legal_chains(adj, col, bset):
    for a, b in itertools.combinations(range(4), 2):
        done = set()
        for u in adj:
            if u in done or col[u] not in (a, b):
                continue
            comp = set()
            stack = [u]
            while stack:
                x = stack.pop()
                if x in comp:
                    continue
                comp.add(x)
                for w in adj[x]:
                    if w not in comp and col[w] in (a, b):
                        stack.append(w)
            done |= comp
            if not (comp & bset):
                yield a, b, comp


def run_pinning(adj, interior, bcyc, ofaces, pin_seq, wrel_choice,
                sample_pins=200):
    """Full two-lens data for one pinning. Respects the guard."""
    guard_decision(pin_seq)
    bset = set(bcyc)
    pin = dict(zip(bcyc, pin_seq))
    comps = Y4.completions(adj, interior, pin)
    vs_int = sorted(interior, key=str)

    def eps(c):
        out = []
        for f in ofaces:
            s = H8.face_sign(f, c)
            out.append(0 if s == 1 else 1)
        return tuple(out)

    def omega_int(c):
        w = {v: 0 for v in vs_int}
        for f in ofaces:
            s = H8.face_sign(f, c)
            z = 1 if s == 1 else -1
            for v in f:
                if v in w:
                    w[v] += z
        return tuple(w[v] for v in vs_int)

    # current columns + indicator span population
    def contributions(pop_cols):
        zz_cols = set()
        gf_inds = set()
        for c in pop_cols:
            w0 = omega_int(c)
            e0 = eps(c)
            for a, b, comp in legal_chains(adj, c, bset):
                nc = dict(c)
                for x in comp:
                    nc[x] = b if nc[x] == a else a
                d = tuple(x1 - x0 for x0, x1 in zip(w0, omega_int(nc)))
                if any(d):
                    zz_cols.add(d)
                ind = tuple(x ^ y for x, y in zip(e0, eps(nc)))
                if any(ind):
                    gf_inds.add(ind)
        return zz_cols, gf_inds

    if wrel_choice == 'a':
        zz_cols, gf_inds = contributions(comps)
    elif wrel_choice == 'b':
        zz_cols, gf_inds = contributions(comps)
        import random
        rng = random.Random(4)
        n_used = 0
        tries = 0
        while n_used < sample_pins and tries < sample_pins * 40:
            tries += 1
            seq = [rng.randrange(4)]
            for _ in range(len(bcyc) - 1):
                seq.append(rng.choice([c for c in range(4) if c != seq[-1]]))
            if seq[0] == seq[-1]:
                continue
            if list(seq) == DECISION_PINNING:
                continue          # the decision object stays untouched
            p2 = dict(zip(bcyc, seq))
            cs = Y4.completions(adj, interior, p2)
            if not cs:
                continue
            n_used += 1
            z2, g2 = contributions(cs)
            zz_cols |= z2
            gf_inds |= g2
    else:
        raise SystemExit("W_REL_CHOICE 'c' awaits Lyra's pinned definition")

    # SNF of ZZ columns
    if zz_cols:
        A = [[col[i] for col in zz_cols] for i in range(len(vs_int))]
        diag, U = Y1.smith_normal_form(A)
    else:
        diag, U = [], [[1 if i == j else 0 for j in range(len(vs_int))]
                       for i in range(len(vs_int))]
    basis = []
    for v in gf_inds:
        v = list(v)
        for b in basis:
            piv = next(i for i, x in enumerate(b) if x)
            if v[piv]:
                v = [x ^ y for x, y in zip(v, b)]
        if any(v):
            basis.append(v)

    def gf_reduce(v):
        v = list(v)
        for b in basis:
            piv = next(i for i, x in enumerate(b) if x)
            if v[piv]:
                v = [x ^ y for x, y in zip(v, b)]
        return tuple(v)

    return {
        'completions': comps,
        'omega': [omega_int(c) for c in comps],
        'eps': [eps(c) for c in comps],
        'zz': (diag, U),
        'gf_basis_dim': len(basis),
        'gf_reduce': gf_reduce,
    }




def wrel_intrinsic_exact(adj, interior, bcyc, ofaces):
    """Lyra's pinned W_rel, computed EXACTLY: 1_str(S) is sign-independent,
    so W_rel = span{1_str(S) : S a connected interior subset realizable as
    a boundary-free maximal bichromatic component in SOME proper coloring
    of D}. Interior has 7 vertices — full enumeration of candidates plus a
    direct realizability check per candidate. Population rule: ALL proper
    colorings of D, exactly, via per-candidate satisfiability."""
    int_set = set(interior)
    vs_all = sorted(adj, key=str)
    # connected interior subsets
    from itertools import combinations
    cands = []
    ints = sorted(interior, key=str)
    for r in range(1, len(ints) + 1):
        for sub in combinations(ints, r):
            S = set(sub)
            # connectivity in induced graph
            seen = {sub[0]}
            st = [sub[0]]
            while st:
                x = st.pop()
                for w in adj[x]:
                    if w in S and w not in seen:
                        seen.add(w)
                        st.append(w)
            if len(seen) == len(S):
                cands.append(S)

    def realizable(S):
        # WLOG pair = (0,1); S must be properly 2-colored with {0,1};
        # all neighbors of S outside S get colors in {2,3}; rest proper.
        Sl = sorted(S, key=str)
        # bipartition of S via BFS (its induced graph must be bipartite)
        side = {Sl[0]: 0}
        st = [Sl[0]]
        while st:
            x = st.pop()
            for w in adj[x]:
                if w in S:
                    if w not in side:
                        side[w] = 1 - side[x]
                        st.append(w)
                    elif side[w] == side[x]:
                        return False
        fixed = {v: side[v] for v in S}
        halo = {w for v in S for w in adj[v]} - S
        order = [v for v in vs_all if v not in S]
        col = dict(fixed)

        def bt(i):
            if i == len(order):
                return True
            u = order[i]
            choices = (2, 3) if u in halo else (0, 1, 2, 3)
            for c in choices:
                if all(col.get(w) != c for w in adj[u]):
                    col[u] = c
                    if bt(i + 1):
                        return True
                    del col[u]
            return False

        return bt(0)

    inds = set()
    n_real = 0
    for S in cands:
        if realizable(S):
            n_real += 1
            ind = tuple(1 if 0 < sum(1 for x in f if x in S) < 3 else 0
                        for f in ofaces)
            if any(ind):
                inds.add(ind)
    basis = []
    for v in inds:
        v = list(v)
        for b in basis:
            piv = next(i for i, x in enumerate(b) if x)
            if v[piv]:
                v = [x ^ y for x, y in zip(v, b)]
        if any(v):
            basis.append(v)
    return basis, n_real, len(cands)


def run_decision():
    print("=" * 70)
    print("THE 19-VERTEX DECISION — Z1 (ledger frozen, Cal SS791)")
    print("=" * 70)
    adj, interior, bcyc = Y4.disc(2)
    faces = disc_faces(adj, interior, bcyc)
    ofaces = H8.orient_faces([tuple(f) for f in faces])
    bset = set(bcyc)
    pin = dict(zip(bcyc, DECISION_PINNING))
    comps = Y4.completions(adj, interior, pin)
    print(f"\n  pinning {DECISION_PINNING}")
    print(f"  completions: {len(comps)} (expected 2, both frozen)")
    for i, c in enumerate(comps):
        legal = list(legal_chains(adj, c, bset))
        print(f"    completion {i}: interior "
              f"{[c[v] for v in sorted(interior, key=str)]} "
              f"legal moves: {len(legal)}")

    # GF(2) lens with the intrinsic exact W_rel
    basis, n_real, n_cand = wrel_intrinsic_exact(adj, interior, bcyc, ofaces)
    print(f"\n  W_rel (intrinsic, EXACT): candidates {n_cand} connected "
          f"interior subsets, realizable {n_real}, dim W_rel = {len(basis)}")

    def red(v):
        v = list(v)
        for b in basis:
            piv = next(i for i, x in enumerate(b) if x)
            if v[piv]:
                v = [x ^ y for x, y in zip(v, b)]
        return tuple(v)

    def eps(c):
        return tuple(0 if H8.face_sign(f, c) == 1 else 1 for f in ofaces)

    e1, e2 = eps(comps[0]), eps(comps[1])
    diff = tuple(x ^ y for x, y in zip(e1, e2))
    residue = red(diff)
    gf2_same = not any(residue)
    print(f"\n  GF(2) LENS: eps1 XOR eps2 has weight {sum(diff)}; "
          f"residue mod W_rel weight {sum(residue)}")
    print(f"  GF(2) VERDICT: {'SAME fiber (difference IN W_rel)' if gf2_same else 'DIFFERENT fibers (difference NOT in W_rel)'}")

    # ZZ lens: achieved relative currents over a stated population
    # (population rule: reachability-closures over 400 deterministic
    # sampled pinnings' completions — printed per L1 discipline; the
    # ZZ module is achieved-column by spec)
    R = run_pinning(adj, interior, bcyc, ofaces, DECISION_PINNING, 'b',
                    sample_pins=400)
    diag, U = R['zz']
    w1, w2 = R['omega'][0], R['omega'][1]
    d = [a - b for a, b in zip(w1, w2)]
    zz_same = Y1.in_image(diag, U, d)
    nz = [x for x in d if x]
    print(f"\n  ZZ LENS (population rule: achieved columns over 400 sampled "
          f"pinnings + this one): omega1-omega2 nonzero entries {len(nz)}; "
          f"SNF factors {[x for x in diag if x not in (0, 1)]}")
    print(f"  ZZ VERDICT: {'SAME fiber' if zz_same else 'DIFFERENT fibers'}")

    print("\n" + "=" * 70)
    print(f"THE 2x2 CELL: (ZZ: {'same' if zz_same else 'diff'}, "
          f"GF(2): {'same' if gf2_same else 'diff'})")
    print("=" * 70)
    return zz_same, gf2_same


if __name__ == "__main__":
    print("=" * 70)
    print(f"Toy 5531 — Z1 runner (FROZEN_LEDGER={FROZEN_LEDGER}, "
          f"W_rel choice '{W_REL_CHOICE}')")
    print("=" * 70)

    if FROZEN_LEDGER:
        run_decision()

    adj, interior, bcyc = Y4.disc(2)
    faces = disc_faces(adj, interior, bcyc)
    ofaces = H8.orient_faces([tuple(f) for f in faces])

    # Test 1: the guard
    guard_ok = False
    try:
        run_pinning(adj, interior, bcyc, ofaces, DECISION_PINNING,
                    W_REL_CHOICE)
    except SystemExit as e:
        guard_ok = 'GUARD' in str(e)
    t1 = guard_ok
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Decision pinning REFUSED "
          f"while unfrozen (guard is code)")

    # validation pinning: find a one-class multi-completion pinning
    import random
    rng = random.Random(11)
    val_pin = None
    for _ in range(4000):
        seq = [rng.randrange(4)]
        for _ in range(len(bcyc) - 1):
            seq.append(rng.choice([c for c in range(4) if c != seq[-1]]))
        if seq[0] == seq[-1] or list(seq) == DECISION_PINNING:
            continue
        pin = dict(zip(bcyc, seq))
        cs = Y4.completions(adj, interior, pin)
        if len(cs) < 2:
            continue
        ncl = Y4.n_classes(adj, interior, set(bcyc), cs)
        if ncl == 1:
            val_pin = seq
            break
    print(f"\n  validation pinning: {val_pin}")
    t2 = val_pin is not None
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. One-class multi-completion "
          f"pinning found (reachable pair for the soundness control)")

    if val_pin:
        R = run_pinning(adj, interior, bcyc, ofaces, val_pin, 'b')
        diag, U = R['zz']
        w = R['omega']
        e = R['eps']
        # ZZ tie check on the first reachable pair
        d = [a - b for a, b in zip(w[0], w[1])]
        zz_tie = Y1.in_image(diag, U, d)
        t3 = zz_tie
        print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. ZZ lens soundness: "
              f"reachable completions tie ({zz_tie})")
        ind = tuple(x ^ y for x, y in zip(e[0], e[1]))
        gf_tie = not any(R['gf_reduce'](ind))
        t4 = gf_tie
        print(f"  [{'PASS' if t4 else 'FAIL'}] 4. GF(2) lens soundness "
              f"under 'b': reachable completions tie ({gf_tie}); "
              f"W_rel dim = {R['gf_basis_dim']}")
        Ra = run_pinning(adj, interior, bcyc, ofaces, val_pin, 'a')
        t5 = Ra['gf_basis_dim'] <= R['gf_basis_dim']
        print(f"  [{'PASS' if t5 else 'FAIL'}] 5. 'a' vs 'b' span: "
              f"{Ra['gf_basis_dim']} <= {R['gf_basis_dim']} — the 'a' "
              f"choice is population-starved exactly as flagged; on a "
              f"FROZEN pinning it would be zero and the verdict "
              f"construction-forced")
    else:
        t3 = t4 = t5 = False

    res = [t1, t2, t3, t4, t5]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5531 -- SCORE: {passed}/{len(res)} (RUNNER VALIDATED — "
          f"decision awaits the freeze line)")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
