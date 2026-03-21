#!/usr/bin/env python3
"""
Toy 291 — Probe Hierarchy: Isotropy Under Stronger Methods
===========================================================

Toy 290: UP sees perfect isotropy (1.000) at all alpha. Zero bits from any
direction. The SO(2) conservation law holds perfectly for the weakest probe.

Question: does isotropy survive stronger polynomial probes?

Hierarchy (weakest to strongest):
  UP    — unit propagation (baseline, reproduces Toy 290)
  FL    — failed literal: try both values of each unset var, detect contradictions
  DPLL2 — depth-2 DPLL: branch twice with UP, take intersection of leaves
  DPLL3 — depth-3 DPLL: branch three times (n <= 18 only)
  BP    — belief propagation: iterative message-passing marginals

For each probe level P and each direction d = (variable, value):
  bits(P, d) = number of variables determined beyond the forced one
  isotropy(P) = 1/(1+CV) where CV = std/mean of bits across directions
  backbone_recall(P) = fraction of backbone vars identified (n <= 18)

If stronger probes maintain isotropy -> conservation law is robust,
  the Theta(n) charge bound applies to practical solvers.
If isotropy drops -> hierarchy of symmetry breaking measured in Shannons.

AC connection: the breaking point IS proof complexity, measured in bits.
Casey: "The information is locked in the correlations."
Lyra: "Where does the symmetry finally break?"
"""

import numpy as np
from collections import defaultdict
import random
import time
import sys

# ── Parameters ────────────────────────────────────────────────────────
SIZES = [12, 14, 16, 18, 20]
ALPHAS = [3.0, 3.5, 4.0, 4.267, 4.5, 5.0]
N_INSTANCES = 30
BACKBONE_MAX_N = 18       # vectorized 2^n enumeration limit
DPLL3_MAX_N = 18           # depth-3 gets expensive
BP_ITERS = 80
BP_DAMP = 0.3
BP_THRESH = 0.90           # marginal cutoff for "determined"
SEED = 42


# ── Instance generation ───────────────────────────────────────────────

def gen_3sat(n, alpha, rng):
    """Random 3-SAT with clause/variable ratio alpha."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = rng.sample(range(1, n + 1), 3)
        clauses.append(tuple(v * rng.choice([-1, 1]) for v in vs))
    return clauses


# ── Backbone (vectorized) ────────────────────────────────────────────

def compute_backbone(clauses, n):
    """Vectorized exhaustive backbone. Returns (backbone_dict, n_solutions)."""
    N = 2 ** n
    bits = np.arange(N, dtype=np.int32)
    var_vals = [(bits >> v) & 1 for v in range(n)]  # var v+1 values

    sat = np.ones(N, dtype=bool)
    for clause in clauses:
        clause_sat = np.zeros(N, dtype=bool)
        for lit in clause:
            v = abs(lit) - 1
            if lit > 0:
                clause_sat |= var_vals[v].astype(bool)
            else:
                clause_sat |= ~var_vals[v].astype(bool)
        sat &= clause_sat

    n_sol = int(np.sum(sat))
    if n_sol == 0:
        return None, 0

    backbone = {}
    for v in range(n):
        vals = var_vals[v][sat]
        if np.all(vals):
            backbone[v + 1] = True
        elif not np.any(vals):
            backbone[v + 1] = False
    return backbone, n_sol


# ── Probe Level 0: Unit Propagation ──────────────────────────────────

def up(clauses, n, assign):
    """Unit propagation. Returns (assignment_dict, contradiction_bool)."""
    a = dict(assign)
    changed = True
    while changed:
        changed = False
        for cl in clauses:
            unset = []
            sat = False
            for lit in cl:
                v = abs(lit)
                if v in a:
                    if (lit > 0) == a[v]:
                        sat = True
                        break
                else:
                    unset.append(lit)
            if sat:
                continue
            if len(unset) == 0:
                return a, True  # contradiction
            if len(unset) == 1:
                lit = unset[0]
                v = abs(lit)
                if v not in a:
                    a[v] = (lit > 0)
                    changed = True
    return a, False


def probe_up(clauses, n, var, val):
    """Force var=val, run UP. Return assignment or None."""
    a, c = up(clauses, n, {var: val})
    return None if c else a


# ── Probe Level 1: Failed Literal ────────────────────────────────────

def probe_fl(clauses, n, var, val):
    """Failed literal: UP + try each unset var both ways.
    If one direction contradicts, the other is forced.
    If both agree on a third variable, it's forced too."""
    a, c = up(clauses, n, {var: val})
    if c:
        return None

    changed = True
    rounds = 0
    while changed and rounds < n:
        changed = False
        rounds += 1
        for y in range(1, n + 1):
            if y in a:
                continue
            at, ct = up(clauses, n, {**a, y: True})
            af, cf = up(clauses, n, {**a, y: False})

            if ct and cf:
                return None  # both contradict
            elif ct:
                a[y] = False
                a, c = up(clauses, n, a)
                if c:
                    return None
                changed = True
                break
            elif cf:
                a[y] = True
                a, c = up(clauses, n, a)
                if c:
                    return None
                changed = True
                break
            else:
                # Variables forced identically in both branches
                for z in range(1, n + 1):
                    if z not in a and z in at and z in af and at[z] == af[z]:
                        a[z] = at[z]
                        changed = True
                if changed:
                    a, c = up(clauses, n, a)
                    if c:
                        return None
                    break
    return a


# ── Probe Level 2-3: Depth-limited DPLL ──────────────────────────────

def probe_dpll(clauses, n, var, val, depth):
    """Depth-limited DPLL. Branch on most-constrained variable.
    Return intersection of all leaf assignments (forced regardless of choices)."""
    def _rec(assign, d):
        a, c = up(clauses, n, assign)
        if c:
            return []
        if d >= depth:
            return [a]
        unset = [v for v in range(1, n + 1) if v not in a]
        if not unset:
            return [a]
        # Most constrained variable
        counts = defaultdict(int)
        for cl in clauses:
            cl_sat = any(abs(l) in a and (l > 0) == a[abs(l)] for l in cl)
            if not cl_sat:
                for l in cl:
                    if abs(l) not in a:
                        counts[abs(l)] += 1
        if not counts:
            return [a]
        bv = max(counts, key=counts.get)
        return (_rec({**a, bv: True}, d + 1) +
                _rec({**a, bv: False}, d + 1))

    leaves = _rec({var: val}, 0)
    if not leaves:
        return None
    # Intersection: variables with same value in ALL leaves
    result = {}
    for v in range(1, n + 1):
        vals = set()
        all_have = True
        for leaf in leaves:
            if v in leaf:
                vals.add(leaf[v])
            else:
                all_have = False
                break
        if all_have and len(vals) == 1:
            result[v] = vals.pop()
    return result


# ── Probe Level 4: Belief Propagation ─────────────────────────────────

def probe_bp(clauses, n, var, val):
    """BP marginals. Variables with P > threshold or P < 1-threshold are 'determined'."""
    m = len(clauses)
    vc = defaultdict(list)  # var -> [(clause_idx, sign)]
    for ci, cl in enumerate(clauses):
        for lit in cl:
            vc[abs(lit)].append((ci, 1 if lit > 0 else -1))

    marg = np.full(n + 1, 0.5)
    marg[var] = 1.0 if val else 0.0

    # Cavity messages mu[v][ci]
    mu = {}
    for v in range(1, n + 1):
        mu[v] = {ci: marg[v] for ci, _ in vc[v]}

    for _it in range(BP_ITERS):
        old = marg.copy()

        # Clause-to-var: eta[ci][v] = P(clause ci unsat ignoring v)
        eta = {}
        for ci, cl in enumerate(clauses):
            eta[ci] = {}
            for lit in cl:
                v = abs(lit)
                p_unsat = 1.0
                for lit2 in cl:
                    v2 = abs(lit2)
                    if v2 == v:
                        continue
                    pv2 = mu[v2].get(ci, marg[v2])
                    p_false = (1.0 - pv2) if lit2 > 0 else pv2
                    p_unsat *= np.clip(p_false, 1e-10, 1 - 1e-10)
                eta[ci][v] = p_unsat

        # Var-to-clause and marginals
        for v in range(1, n + 1):
            if v == var:
                continue
            lr = 0.0
            for ci, sign in vc[v]:
                e = np.clip(eta[ci].get(v, 0.5), 1e-10, 1 - 1e-10)
                if sign > 0:
                    lr += -np.log(1.0 - e)
                else:
                    lr += np.log(1.0 - e)
            p = 1.0 / (1.0 + np.exp(np.clip(-lr, -50, 50)))
            marg[v] = BP_DAMP * old[v] + (1 - BP_DAMP) * p
            marg[v] = np.clip(marg[v], 0.001, 0.999)

            for ci, sign in vc[v]:
                e = np.clip(eta[ci].get(v, 0.5), 1e-10, 1 - 1e-10)
                if sign > 0:
                    lr_c = lr + np.log(1.0 - e)
                else:
                    lr_c = lr - np.log(1.0 - e)
                pc = 1.0 / (1.0 + np.exp(np.clip(-lr_c, -50, 50)))
                mu[v][ci] = BP_DAMP * mu[v].get(ci, 0.5) + (1 - BP_DAMP) * pc
                mu[v][ci] = np.clip(mu[v][ci], 0.001, 0.999)

        if np.max(np.abs(marg[1:] - old[1:])) < 1e-6:
            break

    result = {var: val}
    for v in range(1, n + 1):
        if v == var:
            continue
        if marg[v] > BP_THRESH:
            result[v] = True
        elif marg[v] < 1 - BP_THRESH:
            result[v] = False
    return result


# ── Measurement ───────────────────────────────────────────────────────

def measure_probe(clauses, n, probe_fn, backbone=None):
    """Run probe from all 2n directions. Return metrics dict."""
    bits_list = []
    contradictions = 0
    bb_found = set()

    for var in range(1, n + 1):
        for val in [True, False]:
            result = probe_fn(clauses, n, var, val)
            if result is None:
                contradictions += 1
                continue
            bits = len(result) - 1
            bits_list.append(bits)
            if backbone:
                for bv, bval in backbone.items():
                    if bv in result and result[bv] == bval:
                        bb_found.add(bv)

    if not bits_list:
        return {'iso': 1.0, 'mean_bits': 0, 'std_bits': 0,
                'contra': contradictions / (2 * n), 'bb_recall': 0}

    arr = np.array(bits_list, dtype=float)
    mean_b = float(np.mean(arr))
    std_b = float(np.std(arr))
    if mean_b < 1e-10:
        iso = 1.0  # vacuously isotropic
    else:
        cv = std_b / mean_b
        iso = 1.0 / (1.0 + cv)

    bb_rec = len(bb_found) / len(backbone) if backbone else None
    return {'iso': iso, 'mean_bits': mean_b, 'std_bits': std_b,
            'contra': contradictions / (2 * n), 'bb_recall': bb_rec}


# ── Main experiment ───────────────────────────────────────────────────

def run():
    rng = random.Random(SEED)
    t_total = time.time()

    print("=" * 78)
    print("TOY 291 - Probe Hierarchy: Isotropy Under Stronger Methods")
    print("=" * 78)
    print(f"\nSizes: {SIZES}   Alphas: {ALPHAS}   Instances: {N_INSTANCES}")
    print(f"Probes: UP, FL, DPLL-2, DPLL-3 (n<={DPLL3_MAX_N}), BP")
    print(f"Backbone: n<={BACKBONE_MAX_N}")
    print()

    PROBES = [
        ('UP',     lambda cl, n, v, val: probe_up(cl, n, v, val)),
        ('FL',     lambda cl, n, v, val: probe_fl(cl, n, v, val)),
        ('DPLL-2', lambda cl, n, v, val: probe_dpll(cl, n, v, val, 2)),
        ('DPLL-3', lambda cl, n, v, val: probe_dpll(cl, n, v, val, 3)),
        ('BP',     lambda cl, n, v, val: probe_bp(cl, n, v, val)),
    ]

    R = {name: defaultdict(list) for name, _ in PROBES}
    BB_DATA = defaultdict(list)  # (n, alpha) -> list of (bb_size, n_sol)

    total_configs = len(SIZES) * len(ALPHAS)
    cnum = 0

    for n in SIZES:
        for alpha in ALPHAS:
            cnum += 1
            t0 = time.time()
            tag = f"n={n}, a={alpha:.3f}"
            print(f"\n--- {tag} ({cnum}/{total_configs}) ---")
            sys.stdout.flush()

            for inst in range(N_INSTANCES):
                clauses = gen_3sat(n, alpha, rng)

                # Backbone for small n
                bb = None
                if n <= BACKBONE_MAX_N:
                    bb, nsol = compute_backbone(clauses, n)
                    if bb is not None:
                        BB_DATA[(n, alpha)].append((len(bb), nsol))
                    # bb=None means UNSAT; we still probe but skip bb_recall

                # Run all applicable probes
                for pname, pfunc in PROBES:
                    if pname == 'DPLL-3' and n > DPLL3_MAX_N:
                        continue
                    m = measure_probe(clauses, n, pfunc, backbone=bb)
                    R[pname][(n, alpha)].append(m)

            dt = time.time() - t0
            for pname, _ in PROBES:
                data = R[pname][(n, alpha)]
                if not data:
                    continue
                mb = np.mean([d['mean_bits'] for d in data])
                mi = np.mean([d['iso'] for d in data])
                cr = np.mean([d['contra'] for d in data])
                brs = [d['bb_recall'] for d in data if d['bb_recall'] is not None]
                br_s = f"  bb={np.mean(brs):.3f}" if brs else ""
                print(f"  {pname:7s}: bits={mb:5.2f}  iso={mi:.4f}  "
                      f"contra={cr:.3f}{br_s}")
            print(f"  ({dt:.1f}s)")
            sys.stdout.flush()

    # =================================================================
    #  TABLE 1: ISOTROPY BY PROBE LEVEL
    # =================================================================
    print("\n" + "=" * 78)
    print("TABLE 1: ISOTROPY BY PROBE LEVEL")
    print("=" * 78)

    for pname, _ in PROBES:
        print(f"\n  {pname}")
        print(f"  {'n':>3s} {'a':>6s} {'bits':>7s} {'iso':>8s} "
              f"{'contra':>7s} {'bb_rec':>7s}")
        for n in SIZES:
            for alpha in ALPHAS:
                data = R[pname][(n, alpha)]
                if not data:
                    continue
                mb = np.mean([d['mean_bits'] for d in data])
                mi = np.mean([d['iso'] for d in data])
                cr = np.mean([d['contra'] for d in data])
                brs = [d['bb_recall'] for d in data if d['bb_recall'] is not None]
                if brs:
                    br = np.mean(brs)
                    print(f"  {n:3d} {alpha:6.3f} {mb:7.3f} {mi:8.4f} "
                          f"{cr:7.3f} {br:7.3f}")
                else:
                    print(f"  {n:3d} {alpha:6.3f} {mb:7.3f} {mi:8.4f} "
                          f"{cr:7.3f}     ---")

    # =================================================================
    #  TABLE 2: HIERARCHY AT alpha_c = 4.267
    # =================================================================
    print("\n" + "=" * 78)
    print("TABLE 2: HIERARCHY AT alpha_c = 4.267")
    print("=" * 78)

    header = f"\n  {'Probe':>7s}"
    for n in SIZES:
        header += f"   n={n:<3d}         "
    print(header)
    subhdr = f"  {'':>7s}"
    for _ in SIZES:
        subhdr += f"   bits  iso  bb  "
    print(subhdr)

    for pname, _ in PROBES:
        line = f"  {pname:>7s}"
        for n in SIZES:
            data = R[pname][(n, 4.267)]
            if data:
                mb = np.mean([d['mean_bits'] for d in data])
                mi = np.mean([d['iso'] for d in data])
                brs = [d['bb_recall'] for d in data
                       if d['bb_recall'] is not None]
                br = np.mean(brs) if brs else float('nan')
                if not np.isnan(br):
                    line += f"  {mb:5.2f} {mi:.3f} {br:.2f}"
                else:
                    line += f"  {mb:5.2f} {mi:.3f}  -- "
            else:
                line += f"    ---  ---  ---"
        print(line)

    # =================================================================
    #  TABLE 3: BACKBONE RECALL AT alpha_c
    # =================================================================
    print("\n" + "=" * 78)
    print("TABLE 3: BACKBONE RECALL AT alpha_c = 4.267")
    print("=" * 78)

    bb_sizes = []
    for n in SIZES:
        if n <= BACKBONE_MAX_N:
            bbd = BB_DATA[(n, 4.267)]
            if bbd:
                mean_bb = np.mean([b[0] for b in bbd])
                mean_sol = np.mean([b[1] for b in bbd])
                bb_sizes.append((n, mean_bb, mean_sol))
                print(f"\n  n={n}: mean backbone = {mean_bb:.1f}/{n} vars "
                      f"({mean_bb/n*100:.0f}%),  mean solutions = {mean_sol:.1f}")

    if bb_sizes:
        print(f"\n  {'Probe':>7s}", end="")
        for n, _, _ in bb_sizes:
            print(f"   n={n:<3d}", end="")
        print()
        for pname, _ in PROBES:
            print(f"  {pname:>7s}", end="")
            for n, _, _ in bb_sizes:
                data = R[pname][(n, 4.267)]
                brs = [d['bb_recall'] for d in data
                       if d['bb_recall'] is not None]
                if brs:
                    print(f"  {np.mean(brs):6.3f}", end="")
                else:
                    print(f"     ---", end="")
            print()

    # =================================================================
    #  SYMMETRY BREAKING ANALYSIS
    # =================================================================
    print("\n" + "=" * 78)
    print("SYMMETRY BREAKING ANALYSIS (alpha_c = 4.267)")
    print("=" * 78)

    for n in SIZES:
        print(f"\n  n={n}:")
        for pname, _ in PROBES:
            data = R[pname][(n, 4.267)]
            if not data:
                continue
            mb = np.mean([d['mean_bits'] for d in data])
            sd = np.mean([d['std_bits'] for d in data])
            mi = np.mean([d['iso'] for d in data])

            if mb < 0.01:
                tag = "VACUUM (0 bits -> trivial isotropy)"
            elif mi > 0.95:
                tag = "* ISOTROPIC"
            elif mi > 0.80:
                tag = "~ WEAKLY ANISOTROPIC"
            elif mi > 0.60:
                tag = "! ANISOTROPIC"
            else:
                tag = "!! SYMMETRY BROKEN"

            print(f"    {pname:7s}: bits={mb:5.2f}+-{sd:.2f}  "
                  f"iso={mi:.4f}  {tag}")

    # =================================================================
    #  PHASE TRANSITION OF ISOTROPY
    # =================================================================
    print("\n" + "=" * 78)
    print("ISOTROPY vs ALPHA (n=18)")
    print("=" * 78)

    n_focus = 18
    print(f"\n  {'alpha':>6s}", end="")
    for pname, _ in PROBES:
        if R[pname][(n_focus, ALPHAS[0])]:
            print(f"  {pname:>7s}", end="")
    print()

    for alpha in ALPHAS:
        print(f"  {alpha:6.3f}", end="")
        for pname, _ in PROBES:
            data = R[pname][(n_focus, alpha)]
            if data:
                mi = np.mean([d['iso'] for d in data])
                mb = np.mean([d['mean_bits'] for d in data])
                print(f"  {mi:5.3f}({mb:4.1f})", end="")
        print()

    # =================================================================
    #  VERDICT
    # =================================================================
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)

    # Classify each probe at alpha_c
    vacuum = []
    isotropic = []
    broken = []

    for pname, _ in PROBES:
        all_data = []
        for n in SIZES:
            all_data.extend(R[pname][(n, 4.267)])
        if not all_data:
            continue
        mb = np.mean([d['mean_bits'] for d in all_data])
        mi = np.mean([d['iso'] for d in all_data])
        if mb < 0.01:
            vacuum.append((pname, mb, mi))
        elif mi > 0.90:
            isotropic.append((pname, mb, mi))
        else:
            broken.append((pname, mb, mi))

    if vacuum:
        names = ', '.join(p for p, _, _ in vacuum)
        print(f"\n  Vacuous (0 bits extracted): {names}")
        print(f"    Conservation holds trivially -- probe too weak to test.")

    if isotropic:
        for p, mb, mi in isotropic:
            print(f"\n  * {p}: iso={mi:.4f}, bits={mb:.2f}")
            print(f"    Extracts {mb:.2f} bits per direction, UNIFORMLY.")
            print(f"    Conservation law holds at this probe level.")

    if broken:
        for p, mb, mi in broken:
            print(f"\n  ! {p}: iso={mi:.4f}, bits={mb:.2f}")
            print(f"    Isotropy broken. Some directions are preferred.")
            print(f"    This is where SO(2) -> S_3 symmetry breaking is visible.")

    # The hierarchy boundary
    if isotropic and broken:
        last_iso = isotropic[-1][0]
        first_break = broken[0][0]
        print(f"\n  HIERARCHY BOUNDARY: between {last_iso} and {first_break}")
        print(f"    Methods up to {last_iso} see perfect conservation.")
        print(f"    {first_break} begins to crack the symmetry.")
        iso_bits = isotropic[-1][1]
        brk_bits = broken[0][1]
        print(f"    Bits cracked: {iso_bits:.2f} -> {brk_bits:.2f} "
              f"(+{brk_bits - iso_bits:.2f} bits at the boundary)")
    elif not broken and not isotropic and vacuum:
        print(f"\n  ALL probes extract 0 bits -- conservation is total.")
        print(f"  Even FL and DPLL can't crack a single bit.")
    elif not broken and isotropic:
        print(f"\n  * ALL probes maintain isotropy through the full hierarchy.")
        print(f"  The conservation law holds against FL, DPLL, and BP.")
        print(f"  The Theta(n) charge bound applies to practical solvers.")
    elif broken and not isotropic:
        print(f"\n  ALL non-vacuous probes break isotropy.")
        print(f"  Conservation fails immediately above UP.")

    elapsed = time.time() - t_total
    print(f"\n  Total time: {elapsed:.0f}s ({elapsed/60:.1f}min)")
    print("=" * 78)
    print("DONE")


if __name__ == '__main__':
    run()
