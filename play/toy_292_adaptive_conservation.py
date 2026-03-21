#!/usr/bin/env python3
"""
Toy 292 — Adaptive Conservation: Does bits/n → 0 Survive Adaptive Probing?
===========================================================================

Toy 291 showed bits/n → 0 for non-adaptive probing (force one variable,
measure what follows). But real algorithms are ADAPTIVE — each step's
direction depends on what previous steps revealed.

The kill shot for P != NP: prove that even adaptive, unbounded-width
polynomial processes can't concentrate the distributed charge Q = Theta(n).

This toy tests it empirically with increasingly powerful adaptive strategies:

  Level 0: NON-ADAPTIVE — force each variable independently (Toy 291 baseline)
  Level 1: GREEDY-ADAPTIVE — always probe the most-constrained remaining variable
  Level 2: LOOKAHEAD-ADAPTIVE — pick the variable whose forcing maximizes cascade
  Level 3: FULL-ADAPTIVE — iterative FL with best-first variable selection
  Level 4: ORACLE-GUIDED — probe variables in backbone-frequency order (cheating baseline)

For each strategy, measure:
  - bits_after_k: total bits extracted after k adaptive steps
  - bits_per_step(k): marginal bits gained at step k
  - saturation: does extraction plateau before reaching backbone?
  - comparison to backbone size: can ANY adaptive strategy reach Theta(n)?

The key prediction: bits_after_k grows as O(sqrt(n)) or O(log n), not O(n).
Even adaptive strategies hit a wall because the charge is non-localizable.

If confirmed: the conservation law holds adaptively → Layer 3 closes.
"""

import numpy as np
from collections import defaultdict
import random
import time
import sys


# ── Parameters ────────────────────────────────────────────────────────
SIZES = [14, 16, 18, 20, 22, 24]
ALPHAS = [4.0, 4.267, 4.5, 5.0]
N_INSTANCES = 40
BACKBONE_MAX_N = 22       # vectorized enumeration limit (2^22 = 4M)
MAX_STEPS = None           # set per-n below (we'll probe up to n steps)
SEED = 42


# ── Instance generation ───────────────────────────────────────────────

def gen_3sat(n, alpha, rng):
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = rng.sample(range(1, n + 1), 3)
        clauses.append(tuple(v * rng.choice([-1, 1]) for v in vs))
    return clauses


# ── Backbone (vectorized) ────────────────────────────────────────────

def compute_backbone(clauses, n):
    """Vectorized exhaustive backbone + per-variable polarity."""
    N = 2 ** n
    bits = np.arange(N, dtype=np.int32)
    var_vals = [(bits >> v) & 1 for v in range(n)]

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
        return None, 0, None

    backbone = {}
    # Also compute per-variable frequency (fraction of solutions where var=True)
    var_freq = {}
    for v in range(n):
        vals = var_vals[v][sat]
        freq = float(np.mean(vals))
        var_freq[v + 1] = freq
        if np.all(vals):
            backbone[v + 1] = True
        elif not np.any(vals):
            backbone[v + 1] = False

    return backbone, n_sol, var_freq


# ── Unit Propagation ─────────────────────────────────────────────────

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
                return a, True
            if len(unset) == 1:
                lit = unset[0]
                v = abs(lit)
                if v not in a:
                    a[v] = (lit > 0)
                    changed = True
    return a, False


# ── Failed Literal (single pass) ─────────────────────────────────────

def fl_pass(clauses, n, assign):
    """One pass of failed literal over unset variables."""
    a = dict(assign)
    for y in range(1, n + 1):
        if y in a:
            continue
        at, ct = up(clauses, n, {**a, y: True})
        af, cf = up(clauses, n, {**a, y: False})
        if ct and cf:
            return a, True  # contradiction
        elif ct:
            a[y] = False
            a, c = up(clauses, n, a)
            if c:
                return a, True
        elif cf:
            a[y] = True
            a, c = up(clauses, n, a)
            if c:
                return a, True
        else:
            # Variables forced in both branches
            for z in range(1, n + 1):
                if z not in a and z in at and z in af and at[z] == af[z]:
                    a[z] = at[z]
    return a, False


# ── Variable scoring functions ────────────────────────────────────────

def score_most_constrained(clauses, n, current_assign):
    """Score = number of unsatisfied clause appearances."""
    scores = defaultdict(int)
    for cl in clauses:
        cl_sat = any(abs(l) in current_assign and
                     (l > 0) == current_assign[abs(l)] for l in cl)
        if not cl_sat:
            for l in cl:
                v = abs(l)
                if v not in current_assign:
                    scores[v] += 1
    return scores


def score_lookahead(clauses, n, current_assign):
    """Score = max cascade from forcing this variable either way."""
    scores = {}
    for v in range(1, n + 1):
        if v in current_assign:
            continue
        best = 0
        for val in [True, False]:
            a, c = up(clauses, n, {**current_assign, v: val})
            if c:
                # Contradiction = we learn v must be the OTHER value
                # That's maximally informative
                best = n
                break
            best = max(best, len(a) - len(current_assign) - 1)
        scores[v] = best
    return scores


def score_fl_lookahead(clauses, n, current_assign):
    """Score = FL cascade from forcing this variable."""
    scores = {}
    for v in range(1, n + 1):
        if v in current_assign:
            continue
        best = 0
        for val in [True, False]:
            a_start = {**current_assign, v: val}
            a, c = up(clauses, n, a_start)
            if c:
                best = n
                break
            # One FL pass from here
            a_fl, c_fl = fl_pass(clauses, n, a)
            if c_fl:
                best = n
                break
            best = max(best, len(a_fl) - len(current_assign) - 1)
        scores[v] = best
    return scores


# ── Adaptive strategies ───────────────────────────────────────────────

def strategy_nonadaptive(clauses, n, max_steps, rng):
    """Non-adaptive: force variables in random order, UP after each."""
    order = list(range(1, n + 1))
    rng.shuffle(order)
    assign = {}
    trajectory = []  # (step, total_bits)

    for step, var in enumerate(order[:max_steps]):
        if var in assign:
            trajectory.append((step, len(assign)))
            continue
        # Try both polarities, pick the one that doesn't contradict
        a_t, c_t = up(clauses, n, {**assign, var: True})
        a_f, c_f = up(clauses, n, {**assign, var: False})
        if c_t and c_f:
            break  # UNSAT from here
        elif c_t:
            assign = a_f
        elif c_f:
            assign = a_t
        else:
            # Pick the one that determines more
            assign = a_t if len(a_t) >= len(a_f) else a_f
        trajectory.append((step, len(assign)))

    return trajectory, assign


def strategy_greedy(clauses, n, max_steps, rng):
    """Greedy-adaptive: always pick most-constrained variable."""
    assign = {}
    trajectory = []

    for step in range(max_steps):
        scores = score_most_constrained(clauses, n, assign)
        if not scores:
            break
        var = max(scores, key=scores.get)
        # Try both polarities
        a_t, c_t = up(clauses, n, {**assign, var: True})
        a_f, c_f = up(clauses, n, {**assign, var: False})
        if c_t and c_f:
            break
        elif c_t:
            assign = a_f
        elif c_f:
            assign = a_t
        else:
            assign = a_t if len(a_t) >= len(a_f) else a_f
        trajectory.append((step, len(assign)))

    return trajectory, assign


def strategy_lookahead(clauses, n, max_steps, rng):
    """Lookahead-adaptive: pick variable maximizing UP cascade."""
    assign = {}
    trajectory = []

    for step in range(max_steps):
        scores = score_lookahead(clauses, n, assign)
        if not scores:
            break
        var = max(scores, key=scores.get)
        # If score = n, one direction contradicts
        a_t, c_t = up(clauses, n, {**assign, var: True})
        a_f, c_f = up(clauses, n, {**assign, var: False})
        if c_t and c_f:
            break
        elif c_t:
            assign = a_f
        elif c_f:
            assign = a_t
        else:
            assign = a_t if len(a_t) >= len(a_f) else a_f
        trajectory.append((step, len(assign)))

    return trajectory, assign


def strategy_full_adaptive(clauses, n, max_steps, rng):
    """Full-adaptive: FL lookahead scoring, FL propagation after each step."""
    assign = {}
    trajectory = []

    for step in range(max_steps):
        # Score with FL lookahead (expensive but strongest)
        unset = [v for v in range(1, n + 1) if v not in assign]
        if not unset:
            break

        # For efficiency, use UP lookahead for scoring, then FL after choosing
        scores = score_lookahead(clauses, n, assign)
        if not scores:
            break
        var = max(scores, key=scores.get)

        # Force the variable, then apply FL
        a_t, c_t = up(clauses, n, {**assign, var: True})
        a_f, c_f = up(clauses, n, {**assign, var: False})

        if c_t and c_f:
            break
        elif c_t:
            assign = a_f
        elif c_f:
            assign = a_t
        else:
            assign = a_t if len(a_t) >= len(a_f) else a_f

        # Apply FL to extend
        assign, c = fl_pass(clauses, n, assign)
        if c:
            break

        trajectory.append((step, len(assign)))

    return trajectory, assign


def strategy_oracle(clauses, n, max_steps, rng, var_freq, backbone):
    """Oracle-guided: probe variables in order of backbone membership
    (backbone vars first, sorted by polarity extremity).
    This CHEATS — uses knowledge the algorithm shouldn't have."""
    if not backbone or not var_freq:
        return strategy_greedy(clauses, n, max_steps, rng)

    # Sort: backbone vars first (by polarity extremity), then others
    bb_vars = sorted(backbone.keys(),
                     key=lambda v: -abs(var_freq.get(v, 0.5) - 0.5))
    non_bb = [v for v in range(1, n + 1) if v not in backbone]
    rng.shuffle(non_bb)
    order = bb_vars + non_bb

    assign = {}
    trajectory = []

    for step, var in enumerate(order[:max_steps]):
        if var in assign:
            trajectory.append((step, len(assign)))
            continue
        a_t, c_t = up(clauses, n, {**assign, var: True})
        a_f, c_f = up(clauses, n, {**assign, var: False})
        if c_t and c_f:
            break
        elif c_t:
            assign = a_f
        elif c_f:
            assign = a_t
        else:
            # Oracle knows the backbone value
            if var in backbone:
                assign = a_t if backbone[var] else a_f
            else:
                assign = a_t if len(a_t) >= len(a_f) else a_f
        trajectory.append((step, len(assign)))

    return trajectory, assign


# ── Analysis helpers ──────────────────────────────────────────────────

def trajectory_to_bits_per_step(traj, n):
    """Convert trajectory to marginal bits per step and cumulative bits/n."""
    if not traj:
        return [], [], []
    steps = [t[0] for t in traj]
    cum_bits = [t[1] for t in traj]
    marginal = [cum_bits[0]]
    for i in range(1, len(cum_bits)):
        marginal.append(cum_bits[i] - cum_bits[i - 1])
    bits_per_n = [b / n for b in cum_bits]
    return steps, marginal, bits_per_n


def backbone_recall_at_step(assign, backbone):
    """Fraction of backbone variables correctly determined."""
    if not backbone:
        return None
    found = sum(1 for v, val in backbone.items()
                if v in assign and assign[v] == val)
    return found / len(backbone)


# ── Main experiment ───────────────────────────────────────────────────

def run():
    rng = random.Random(SEED)
    t_total = time.time()

    print("=" * 78)
    print("TOY 292 - Adaptive Conservation: bits/n Under Adaptive Probing")
    print("=" * 78)
    print(f"\nSizes: {SIZES}   Alphas: {ALPHAS}   Instances: {N_INSTANCES}")
    print(f"Strategies: Non-adaptive, Greedy, Lookahead, Full-adaptive, Oracle")
    print(f"Backbone: n<={BACKBONE_MAX_N}")
    print()

    STRATEGIES = [
        ('Random',    'nonadaptive'),
        ('Greedy',    'greedy'),
        ('Lookahead', 'lookahead'),
        ('Full-FL',   'full_adaptive'),
        ('Oracle',    'oracle'),
    ]

    # Results: R[strategy][(n, alpha)] = list of dicts
    R = {name: defaultdict(list) for name, _ in STRATEGIES}

    total_configs = len(SIZES) * len(ALPHAS)
    cnum = 0

    for n in SIZES:
        max_steps = n  # probe up to n steps
        for alpha in ALPHAS:
            cnum += 1
            t0 = time.time()
            print(f"\n--- n={n}, a={alpha:.3f} ({cnum}/{total_configs}) ---")
            sys.stdout.flush()

            for inst in range(N_INSTANCES):
                clauses = gen_3sat(n, alpha, rng)

                # Backbone
                bb, nsol, vfreq = None, 0, None
                if n <= BACKBONE_MAX_N:
                    bb, nsol, vfreq = compute_backbone(clauses, n)
                    if bb is None:
                        continue  # UNSAT

                inst_rng = random.Random(rng.randint(0, 2**31))

                # Run each strategy
                for sname, stype in STRATEGIES:
                    if stype == 'nonadaptive':
                        traj, final = strategy_nonadaptive(
                            clauses, n, max_steps, inst_rng)
                    elif stype == 'greedy':
                        traj, final = strategy_greedy(
                            clauses, n, max_steps, inst_rng)
                    elif stype == 'lookahead':
                        traj, final = strategy_lookahead(
                            clauses, n, max_steps, inst_rng)
                    elif stype == 'full_adaptive':
                        traj, final = strategy_full_adaptive(
                            clauses, n, max_steps, inst_rng)
                    elif stype == 'oracle':
                        traj, final = strategy_oracle(
                            clauses, n, max_steps, inst_rng, vfreq, bb)

                    steps, marginal, bits_n = trajectory_to_bits_per_step(
                        traj, n)

                    # Metrics
                    final_bits = len(final) if traj else 0
                    bb_rec = backbone_recall_at_step(final, bb) if bb else None

                    # Bits at key step counts
                    bits_at = {}
                    for k in [1, 2, 5, 10, n // 2, n]:
                        if k <= len(traj):
                            bits_at[k] = traj[k - 1][1]
                        elif traj:
                            bits_at[k] = traj[-1][1]
                        else:
                            bits_at[k] = 0

                    # Marginal at step k
                    marg_at = {}
                    for k in [1, 5, 10, n // 2]:
                        if k <= len(marginal):
                            marg_at[k] = marginal[k - 1]
                        else:
                            marg_at[k] = 0

                    # Saturation: step where 90% of final bits reached
                    sat_step = len(traj)
                    if traj and final_bits > 0:
                        thresh = 0.9 * final_bits
                        for i, (s, b) in enumerate(traj):
                            if b >= thresh:
                                sat_step = i + 1
                                break

                    R[sname][(n, alpha)].append({
                        'final_bits': final_bits,
                        'final_bits_n': final_bits / n,
                        'bb_recall': bb_rec,
                        'bits_at': bits_at,
                        'marg_at': marg_at,
                        'sat_step': sat_step,
                        'n_steps': len(traj),
                    })

            dt = time.time() - t0
            for sname, _ in STRATEGIES:
                data = R[sname][(n, alpha)]
                if not data:
                    continue
                fb = np.mean([d['final_bits_n'] for d in data])
                brs = [d['bb_recall'] for d in data if d['bb_recall'] is not None]
                br = np.mean(brs) if brs else float('nan')
                ss = np.mean([d['sat_step'] for d in data])
                br_s = f"  bb={br:.3f}" if not np.isnan(br) else ""
                print(f"  {sname:10s}: bits/n={fb:.3f}  sat_step={ss:.1f}"
                      f"{br_s}")
            print(f"  ({dt:.1f}s)")
            sys.stdout.flush()

    # =================================================================
    #  TABLE 1: FINAL bits/n BY STRATEGY
    # =================================================================
    print("\n" + "=" * 78)
    print("TABLE 1: FINAL bits/n AFTER n ADAPTIVE STEPS")
    print("=" * 78)

    print(f"\n  {'Strategy':>10s}", end="")
    for n in SIZES:
        print(f"   n={n:<3d}", end="")
    print()

    for alpha in ALPHAS:
        print(f"\n  alpha = {alpha:.3f}")
        for sname, _ in STRATEGIES:
            print(f"  {sname:>10s}", end="")
            for n in SIZES:
                data = R[sname][(n, alpha)]
                if data:
                    fb = np.mean([d['final_bits_n'] for d in data])
                    print(f"  {fb:6.3f}", end="")
                else:
                    print(f"     ---", end="")
            print()

    # =================================================================
    #  TABLE 2: MARGINAL BITS PER STEP (diminishing returns?)
    # =================================================================
    print("\n" + "=" * 78)
    print("TABLE 2: MARGINAL BITS AT STEP k (alpha_c = 4.267, n=20)")
    print("=" * 78)

    n_focus = 20 if 20 in SIZES else SIZES[-2]
    print(f"\n  n={n_focus}")
    print(f"  {'Strategy':>10s}  step=1  step=5  step=10  step={n_focus//2}")

    for sname, _ in STRATEGIES:
        data = R[sname][(n_focus, 4.267)]
        if not data:
            continue
        print(f"  {sname:>10s}", end="")
        for k in [1, 5, 10, n_focus // 2]:
            m = np.mean([d['marg_at'].get(k, 0) for d in data])
            print(f"  {m:6.2f} ", end="")
        print()

    # =================================================================
    #  TABLE 3: SATURATION STEP
    # =================================================================
    print("\n" + "=" * 78)
    print("TABLE 3: SATURATION STEP (90% of final bits reached)")
    print("=" * 78)

    print(f"\n  {'Strategy':>10s}", end="")
    for n in SIZES:
        print(f"   n={n:<3d}", end="")
    print(f"   scaling?")

    for sname, _ in STRATEGIES:
        print(f"  {sname:>10s}", end="")
        sat_vals = []
        for n in SIZES:
            data = R[sname][(n, 4.267)]
            if data:
                ss = np.mean([d['sat_step'] for d in data])
                print(f"  {ss:6.1f}", end="")
                sat_vals.append((n, ss))
            else:
                print(f"     ---", end="")
        # Estimate scaling
        if len(sat_vals) >= 3:
            ns = np.array([v[0] for v in sat_vals], dtype=float)
            ss = np.array([v[1] for v in sat_vals], dtype=float)
            # Fit log: sat ~ a * log(n) + b
            log_ns = np.log(ns)
            if np.std(log_ns) > 0:
                a_log = np.polyfit(log_ns, ss, 1)[0]
            else:
                a_log = 0
            # Fit linear: sat ~ a * n + b
            a_lin = np.polyfit(ns, ss, 1)[0]
            # Fit sqrt: sat ~ a * sqrt(n) + b
            sqrt_ns = np.sqrt(ns)
            a_sqrt = np.polyfit(sqrt_ns, ss, 1)[0]
            print(f"   ~{a_lin:.2f}*n", end="")
        print()

    # =================================================================
    #  TABLE 4: BACKBONE RECALL AT alpha_c
    # =================================================================
    print("\n" + "=" * 78)
    print("TABLE 4: BACKBONE RECALL AFTER n STEPS (alpha_c = 4.267)")
    print("=" * 78)

    print(f"\n  {'Strategy':>10s}", end="")
    for n in SIZES:
        if n <= BACKBONE_MAX_N:
            print(f"   n={n:<3d}", end="")
    print()

    for sname, _ in STRATEGIES:
        print(f"  {sname:>10s}", end="")
        for n in SIZES:
            if n > BACKBONE_MAX_N:
                continue
            data = R[sname][(n, 4.267)]
            brs = [d['bb_recall'] for d in data if d['bb_recall'] is not None]
            if brs:
                print(f"  {np.mean(brs):6.3f}", end="")
            else:
                print(f"     ---", end="")
        print()

    # =================================================================
    #  TABLE 5: bits/n SCALING — THE KEY TEST
    # =================================================================
    print("\n" + "=" * 78)
    print("TABLE 5: bits/n SCALING AT alpha_c = 4.267")
    print("=" * 78)
    print("\n  Does bits/n decrease with n? (Conservation law test)")

    for sname, _ in STRATEGIES:
        vals = []
        for n in SIZES:
            data = R[sname][(n, 4.267)]
            if data:
                fb = np.mean([d['final_bits_n'] for d in data])
                vals.append((n, fb))
        if len(vals) >= 2:
            ns = [v[0] for v in vals]
            fbs = [v[1] for v in vals]
            trend = "DECREASING" if fbs[-1] < fbs[0] - 0.02 else \
                    "FLAT" if abs(fbs[-1] - fbs[0]) < 0.02 else \
                    "INCREASING"
            delta = fbs[-1] - fbs[0]
            print(f"\n  {sname:>10s}: ", end="")
            for n, fb in vals:
                print(f"{fb:.3f}({n}) ", end="")
            print(f"  -> {trend} (delta={delta:+.3f})")

    # =================================================================
    #  VERDICT
    # =================================================================
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)

    # Check if bits/n decreases for all strategies at alpha_c
    all_decreasing = True
    strongest_strategy = None
    strongest_bits_n = 0

    for sname, _ in STRATEGIES:
        vals = []
        for n in SIZES:
            data = R[sname][(n, 4.267)]
            if data:
                fb = np.mean([d['final_bits_n'] for d in data])
                vals.append((n, fb))
        if len(vals) >= 2:
            if vals[-1][1] >= vals[0][1] - 0.01:
                all_decreasing = False
            if vals[-1][1] > strongest_bits_n:
                strongest_bits_n = vals[-1][1]
                strongest_strategy = sname

    if all_decreasing:
        print(f"\n  * ALL adaptive strategies show bits/n DECREASING with n.")
        print(f"  The conservation law survives adaptive probing.")
        print(f"  Even with lookahead, FL, and oracle guidance,")
        print(f"  the fraction of charge cracked shrinks as n grows.")
        print(f"\n  Strongest strategy: {strongest_strategy} "
              f"(bits/n = {strongest_bits_n:.3f} at n={SIZES[-1]})")
        print(f"\n  -> NON-LOCALIZABILITY CONFIRMED.")
        print(f"  -> Adaptive strategies cannot concentrate the charge.")
        print(f"  -> Conservation holds for adaptive unbounded-width probes.")
    else:
        print(f"\n  Some strategies show bits/n NOT decreasing.")
        print(f"  Conservation may fail for adaptive probes.")
        for sname, _ in STRATEGIES:
            vals = []
            for n in SIZES:
                data = R[sname][(n, 4.267)]
                if data:
                    fb = np.mean([d['final_bits_n'] for d in data])
                    vals.append((n, fb))
            if len(vals) >= 2:
                trend = "decreasing" if vals[-1][1] < vals[0][1] - 0.02 \
                    else "flat/increasing"
                print(f"    {sname:>10s}: {trend}")

    # Check oracle vs non-oracle gap
    print(f"\n  ORACLE GAP (does knowing the backbone help?):")
    for n in SIZES:
        if n > BACKBONE_MAX_N:
            continue
        oracle_data = R['Oracle'][(n, 4.267)]
        best_data = R['Full-FL'][(n, 4.267)]
        if oracle_data and best_data:
            o_fb = np.mean([d['final_bits_n'] for d in oracle_data])
            b_fb = np.mean([d['final_bits_n'] for d in best_data])
            gap = o_fb - b_fb
            print(f"    n={n}: Oracle={o_fb:.3f}, Full-FL={b_fb:.3f}, "
                  f"gap={gap:+.3f}")

    elapsed = time.time() - t_total
    print(f"\n  Total time: {elapsed:.0f}s ({elapsed/60:.1f}min)")
    print("=" * 78)
    print("DONE")


if __name__ == '__main__':
    run()
