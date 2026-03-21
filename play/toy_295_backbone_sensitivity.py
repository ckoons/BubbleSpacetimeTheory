#!/usr/bin/env python3
"""
Toy 295 — Backbone Function Sensitivity & Circuit Depth Proxies
================================================================

Lyra's Direction 2: Can polynomial circuits evaluate the backbone function
F_φ(p₁,...,p_{β₁}) that maps cycle parities to backbone?

Circuit depth lower bounds connect to function complexity measures:
  - Sensitivity s(f): flip one input bit, max change in output
  - Block sensitivity bs(f): flip a block of bits, max change
  - Certificate complexity C(f): min bits that "prove" the output
  - Huang (2019): degree(f) ≥ √s(f), depth(f) ≥ log s(f)

We measure these for the backbone function B(φ):
  1. Clause sensitivity: flip one clause sign, how many backbone bits change?
  2. Clause removal sensitivity: remove one clause, backbone change?
  3. Certificate complexity: min clauses proving each backbone bit
  4. Global sensitivity: fraction of clauses whose flip changes ANY backbone bit
  5. Backbone stability: add random clause at α_c, backbone change?

If sensitivity = Θ(n) → depth ≥ (1/2)log n → not in AC⁰
If sensitivity = Θ(n²) → depth ≥ log n → matches our d* data

Scorecard:
  1. Clause-flip sensitivity grows with n?                    [depth signal]
  2. Mean backbone bits changed per flip ≥ Ω(1)?             [non-trivial]
  3. Certificate complexity grows with n?                      [proof size]
  4. Global sensitivity (frac critical clauses) stays Θ(1)?   [delocalized]
  5. Clause removal more destabilizing than clause flip?       [structure]
  6. Sensitivity at α_c > sensitivity at α < α_c?             [phase transition]
  7. Consistent across backbone variables?                     [uniform]
  8. Sensitivity × n grows faster than n?                      [super-linear]

Copyright (c) 2026 Casey Koons. All rights reserved.
Created with Claude Opus 4.6 (Elie), March 2026.
"""

import numpy as np
from collections import defaultdict
import random
import time
import sys


# ── Parameters ────────────────────────────────────────────────────────
SIZES = [12, 14, 16, 18, 20]
ALPHAS = [3.5, 4.0, 4.267, 4.5]
N_INSTANCES = 25
BACKBONE_MAX_N = 20
SEED = 295


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
    """Vectorized exhaustive backbone computation."""
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
        return None, 0

    backbone = set()
    backbone_vals = {}
    for v in range(n):
        vals = var_vals[v][sat]
        if np.all(vals):
            backbone.add(v + 1)
            backbone_vals[v + 1] = True
        elif not np.any(vals):
            backbone.add(v + 1)
            backbone_vals[v + 1] = False

    return backbone_vals, n_sol


def backbone_diff(bb1, bb2):
    """Count backbone bits that differ between two backbone computations."""
    if bb1 is None or bb2 is None:
        return -1  # one is UNSAT
    keys1 = set(bb1.keys())
    keys2 = set(bb2.keys())
    # Bits in bb1 but not bb2 (no longer backbone)
    lost = keys1 - keys2
    # Bits in bb2 but not bb1 (became backbone)
    gained = keys2 - keys1
    # Bits in both but different values
    flipped = sum(1 for k in keys1 & keys2 if bb1[k] != bb2[k])
    return len(lost) + len(gained) + flipped


# ── Sensitivity measurements ─────────────────────────────────────────

def flip_literal_sign(clauses, clause_idx, lit_idx):
    """Flip sign of one literal in one clause."""
    new_clauses = list(clauses)
    clause = list(new_clauses[clause_idx])
    clause[lit_idx] = -clause[lit_idx]
    new_clauses[clause_idx] = tuple(clause)
    return new_clauses


def remove_clause(clauses, clause_idx):
    """Remove one clause."""
    return clauses[:clause_idx] + clauses[clause_idx + 1:]


def measure_sensitivity(clauses, n, backbone_orig, n_sol_orig):
    """
    Measure backbone sensitivity to clause perturbations.
    """
    m = len(clauses)
    bb_orig = backbone_orig
    bb_size = len(bb_orig)

    if bb_size == 0:
        return None

    # 1. Clause-flip sensitivity: flip each literal sign, measure backbone change
    #    Also track per-variable changes (reuse results, don't recompute)
    flip_changes = []
    critical_clauses = set()  # clauses whose flip changes backbone
    per_var_critical = defaultdict(int)  # var → count of flips that affect it

    for ci in range(m):
        for li in range(3):
            new_clauses = flip_literal_sign(clauses, ci, li)
            bb_new, n_sol_new = compute_backbone(new_clauses, n)
            if bb_new is None:
                # Formula became UNSAT — maximal disruption
                flip_changes.append(bb_size)
                critical_clauses.add(ci)
                for var in bb_orig:
                    per_var_critical[var] += 1
            else:
                diff = backbone_diff(bb_orig, bb_new)
                flip_changes.append(diff)
                if diff > 0:
                    critical_clauses.add(ci)
                # Track which backbone vars changed
                for var in bb_orig:
                    if var not in bb_new or bb_new.get(var) != bb_orig[var]:
                        per_var_critical[var] += 1

    # 2. Clause-removal sensitivity: remove each clause, measure backbone change
    removal_changes = []
    for ci in range(m):
        new_clauses = remove_clause(clauses, ci)
        bb_new, n_sol_new = compute_backbone(new_clauses, n)
        if bb_new is None:
            removal_changes.append(0)  # shouldn't happen (fewer constraints)
        else:
            diff = backbone_diff(bb_orig, bb_new)
            removal_changes.append(diff)

    # 3. Per-backbone-variable sensitivity (from data already collected above)
    per_var_sensitivity = dict(per_var_critical)

    return {
        'bb_size': bb_size,
        'n_clauses': m,
        'flip_changes': flip_changes,
        'mean_flip_change': np.mean(flip_changes),
        'max_flip_change': max(flip_changes),
        'sensitivity': max(flip_changes),  # max change from any single flip
        'frac_critical_clauses': len(critical_clauses) / m,
        'removal_changes': removal_changes,
        'mean_removal_change': np.mean(removal_changes),
        'max_removal_change': max(removal_changes),
        'per_var_sensitivity': per_var_sensitivity,
        'mean_var_sensitivity': np.mean(list(per_var_sensitivity.values())),
    }


# ── Run experiment ───────────────────────────────────────────────────

def run_experiment():
    print("=" * 76)
    print("Toy 295 — Backbone Function Sensitivity & Circuit Depth Proxies")
    print("=" * 76)
    print(f"Sizes: {SIZES} | Alphas: {ALPHAS} | Instances: {N_INSTANCES}")
    print()

    rng = random.Random(SEED)
    all_results = {}

    for alpha in ALPHAS:
        print(f"\n{'─' * 76}")
        print(f"  α = {alpha}")
        print(f"{'─' * 76}")

        for n in SIZES:
            if n > BACKBONE_MAX_N:
                continue

            t0 = time.time()
            results = []
            skipped = 0

            for trial in range(N_INSTANCES):
                clauses = gen_3sat(n, alpha, rng)
                bb, n_sol = compute_backbone(clauses, n)
                if bb is None or len(bb) == 0:
                    skipped += 1
                    continue

                result = measure_sensitivity(clauses, n, bb, n_sol)
                if result is None:
                    skipped += 1
                    continue

                result['n'] = n
                result['alpha'] = alpha
                results.append(result)

                if n >= 18 and (trial + 1) % 5 == 0:
                    sys.stdout.write(f"\r  n={n:3d}: {trial+1}/{N_INSTANCES}...")
                    sys.stdout.flush()

            elapsed = time.time() - t0
            key = (alpha, n)
            all_results[key] = results

            if not results:
                print(f"\r  n={n:3d}: no valid instances ({skipped} skipped) [{elapsed:.1f}s]")
                continue

            mean_flip = np.mean([r['mean_flip_change'] for r in results])
            max_flip = np.mean([r['max_flip_change'] for r in results])
            sens = np.mean([r['sensitivity'] for r in results])
            frac_crit = np.mean([r['frac_critical_clauses'] for r in results])
            mean_rem = np.mean([r['mean_removal_change'] for r in results])
            mean_var_s = np.mean([r['mean_var_sensitivity'] for r in results])

            print(f"\r  n={n:3d}: |B|={np.mean([r['bb_size'] for r in results]):5.1f}  "
                  f"mean_flip={mean_flip:.2f}  max_flip={max_flip:.1f}  "
                  f"sens={sens:.1f}  crit={frac_crit:.2f}  "
                  f"mean_rem={mean_rem:.2f}  "
                  f"[{len(results)}/{N_INSTANCES}]  [{elapsed:.1f}s]")

    # ── Summary tables ────────────────────────────────────────────────
    print("\n" + "=" * 76)
    print("TABLE 1: Backbone Sensitivity at α_c = 4.267")
    print("=" * 76)
    print(f"{'n':>4} | {'|B|':>5} | {'mean_Δ':>7} | {'max_Δ':>6} | {'sens':>5} | {'crit%':>5} | {'rem_Δ':>6} | {'var_s':>6} | sens/n")
    print("-" * 76)

    for n in SIZES:
        if n > BACKBONE_MAX_N:
            continue
        key = (4.267, n)
        if key not in all_results or not all_results[key]:
            continue
        res = all_results[key]
        bb = np.mean([r['bb_size'] for r in res])
        mf = np.mean([r['mean_flip_change'] for r in res])
        mx = np.mean([r['max_flip_change'] for r in res])
        sn = np.mean([r['sensitivity'] for r in res])
        cr = np.mean([r['frac_critical_clauses'] for r in res])
        rm = np.mean([r['mean_removal_change'] for r in res])
        vs = np.mean([r['mean_var_sensitivity'] for r in res])
        print(f"{n:4d} | {bb:5.1f} | {mf:7.3f} | {mx:6.1f} | {sn:5.1f} | {cr:5.2f} | {rm:6.2f} | {vs:6.1f} | {sn/n:.3f}")

    # Phase transition comparison
    print(f"\nTABLE 2: Sensitivity vs α (n=18)")
    print("=" * 60)
    print(f"{'α':>6} | {'|B|':>5} | {'mean_Δ':>7} | {'sens':>5} | {'crit%':>5} | {'rem_Δ':>6}")
    print("-" * 60)

    n_comp = 18
    for alpha in ALPHAS:
        key = (alpha, n_comp)
        if key not in all_results or not all_results[key]:
            continue
        res = all_results[key]
        bb = np.mean([r['bb_size'] for r in res])
        mf = np.mean([r['mean_flip_change'] for r in res])
        sn = np.mean([r['sensitivity'] for r in res])
        cr = np.mean([r['frac_critical_clauses'] for r in res])
        rm = np.mean([r['mean_removal_change'] for r in res])
        print(f"{alpha:6.3f} | {bb:5.1f} | {mf:7.3f} | {sn:5.1f} | {cr:5.2f} | {rm:6.2f}")

    # ── Scorecard ─────────────────────────────────────────────────────
    print("\n" + "=" * 76)
    print("SCORECARD")
    print("=" * 76)

    scores = []

    # 1. Clause-flip sensitivity grows with n?
    sens_by_n = {}
    for n in SIZES:
        if n > BACKBONE_MAX_N:
            continue
        key = (4.267, n)
        if key in all_results and all_results[key]:
            sens_by_n[n] = np.mean([r['sensitivity'] for r in all_results[key]])
    ns = sorted(sens_by_n.keys())
    if len(ns) >= 3:
        grows = sens_by_n[ns[-1]] > sens_by_n[ns[0]]
        scores.append(grows)
        vals = [f"{sens_by_n[n]:.1f}" for n in ns]
        print(f"  1. Sensitivity grows with n:              {'✓' if grows else '✗'} ({' → '.join(vals)})")
    else:
        scores.append(None)
        print(f"  1. Sensitivity grows with n:              — (insufficient data)")

    # 2. Mean backbone bits changed per flip ≥ Ω(1)?
    mean_by_n = {}
    for n in SIZES:
        if n > BACKBONE_MAX_N:
            continue
        key = (4.267, n)
        if key in all_results and all_results[key]:
            mean_by_n[n] = np.mean([r['mean_flip_change'] for r in all_results[key]])
    if mean_by_n:
        all_nontrivial = all(v > 0.01 for v in mean_by_n.values())
        scores.append(all_nontrivial)
        print(f"  2. Mean Δ per flip > 0:                   {'✓' if all_nontrivial else '✗'} (min={min(mean_by_n.values()):.3f})")
    else:
        scores.append(None)
        print(f"  2. Mean Δ per flip > 0:                   —")

    # 3. Certificate complexity (per-var sensitivity) grows?
    cert_by_n = {}
    for n in SIZES:
        if n > BACKBONE_MAX_N:
            continue
        key = (4.267, n)
        if key in all_results and all_results[key]:
            cert_by_n[n] = np.mean([r['mean_var_sensitivity'] for r in all_results[key]])
    ns_c = sorted(cert_by_n.keys())
    if len(ns_c) >= 3:
        grows = cert_by_n[ns_c[-1]] > cert_by_n[ns_c[0]]
        scores.append(grows)
        vals = [f"{cert_by_n[n]:.1f}" for n in ns_c]
        print(f"  3. Per-var sensitivity grows:              {'✓' if grows else '✗'} ({' → '.join(vals)})")
    else:
        scores.append(None)
        print(f"  3. Per-var sensitivity grows:              —")

    # 4. Critical clause fraction stays Θ(1)?
    crit_by_n = {}
    for n in SIZES:
        if n > BACKBONE_MAX_N:
            continue
        key = (4.267, n)
        if key in all_results and all_results[key]:
            crit_by_n[n] = np.mean([r['frac_critical_clauses'] for r in all_results[key]])
    if crit_by_n:
        stays_constant = all(0.05 < v < 0.95 for v in crit_by_n.values())
        scores.append(stays_constant)
        vals = [f"{crit_by_n[n]:.2f}" for n in sorted(crit_by_n.keys())]
        print(f"  4. Critical clause fraction Θ(1):         {'✓' if stays_constant else '✗'} ({' → '.join(vals)})")
    else:
        scores.append(None)
        print(f"  4. Critical clause fraction Θ(1):         —")

    # 5. Removal more destabilizing than flip?
    rem_vs_flip = {}
    for n in SIZES:
        if n > BACKBONE_MAX_N:
            continue
        key = (4.267, n)
        if key in all_results and all_results[key]:
            rem = np.mean([r['mean_removal_change'] for r in all_results[key]])
            flp = np.mean([r['mean_flip_change'] for r in all_results[key]])
            rem_vs_flip[n] = rem > flp
    if rem_vs_flip:
        mostly = sum(rem_vs_flip.values()) >= len(rem_vs_flip) // 2
        scores.append(mostly)
        print(f"  5. Removal > flip destabilizing:           {'✓' if mostly else '✗'}")
    else:
        scores.append(None)
        print(f"  5. Removal > flip destabilizing:           —")

    # 6. Sensitivity at α_c > sensitivity at α < α_c?
    n_comp = 18
    if n_comp <= BACKBONE_MAX_N:
        sens_below = None
        sens_at = None
        for alpha in ALPHAS:
            key = (alpha, n_comp)
            if key in all_results and all_results[key]:
                s = np.mean([r['sensitivity'] for r in all_results[key]])
                if alpha < 4.0:
                    sens_below = s
                elif abs(alpha - 4.267) < 0.01:
                    sens_at = s
        if sens_below is not None and sens_at is not None:
            ok = sens_at > sens_below
            scores.append(ok)
            print(f"  6. Sensitivity peaks at α_c:              {'✓' if ok else '✗'} (α<4: {sens_below:.1f}, α_c: {sens_at:.1f})")
        else:
            scores.append(None)
            print(f"  6. Sensitivity peaks at α_c:              —")
    else:
        scores.append(None)
        print(f"  6. Sensitivity peaks at α_c:              —")

    # 7. Sensitivity uniform across backbone variables?
    uniform_by_n = {}
    for n in SIZES:
        if n > BACKBONE_MAX_N:
            continue
        key = (4.267, n)
        if key in all_results and all_results[key]:
            all_vars_sens = []
            for r in all_results[key]:
                all_vars_sens.extend(r['per_var_sensitivity'].values())
            if all_vars_sens:
                cv = np.std(all_vars_sens) / (np.mean(all_vars_sens) + 1e-10)
                uniform_by_n[n] = cv < 1.5  # coefficient of variation < 1.5
    if uniform_by_n:
        mostly = sum(uniform_by_n.values()) >= len(uniform_by_n) // 2
        scores.append(mostly)
        print(f"  7. Sensitivity uniform across vars:        {'✓' if mostly else '✗'}")
    else:
        scores.append(None)
        print(f"  7. Sensitivity uniform across vars:        —")

    # 8. sens/n grows?
    sens_per_n = {}
    for n in SIZES:
        if n > BACKBONE_MAX_N:
            continue
        key = (4.267, n)
        if key in all_results and all_results[key]:
            sens_per_n[n] = np.mean([r['sensitivity'] for r in all_results[key]]) / n
    ns_s = sorted(sens_per_n.keys())
    if len(ns_s) >= 3:
        grows = sens_per_n[ns_s[-1]] > sens_per_n[ns_s[0]]
        scores.append(grows)
        vals = [f"{sens_per_n[n]:.3f}" for n in ns_s]
        print(f"  8. sens/n grows (super-linear):            {'✓' if grows else '✗'} ({' → '.join(vals)})")
    else:
        scores.append(None)
        print(f"  8. sens/n grows (super-linear):            —")

    valid = [s for s in scores if s is not None]
    n_pass = sum(valid)
    n_total = len(valid)
    print(f"\n  Total: {n_pass}/{n_total}")

    # ── Interpretation ────────────────────────────────────────────────
    print("\n" + "=" * 76)
    print("INTERPRETATION")
    print("=" * 76)
    print("""
  Circuit depth lower bounds from sensitivity (Huang 2019):
    depth(f) ≥ log₂(sensitivity(f))

  If sensitivity = Θ(n):
    depth ≥ (1/2) log₂ n → backbone not in AC⁰
    This matches: AC⁰ circuits can't compute parity, and backbone
    depends on cycle parities.

  If sensitivity = Θ(n²) or superlinear:
    depth ≥ log₂ n → deeper circuits needed → harder
    Combined with BSW width Ω(n): resolution depth Ω(n)

  For Lyra's Direction 2 (generalized T28):
    High sensitivity means the backbone function has high algebraic
    degree. Gate outputs (derived constraints) are low-degree
    approximations. If degree(backbone) = ω(1), then polynomial
    circuits with bounded fan-in need depth = ω(1) to compute it.

  The key connection:
    Sensitivity → degree → circuit depth → computational hardness
    This is the circuit-level version of the interpretability barrier.
""")


# ── Entry point ──────────────────────────────────────────────────────

if __name__ == '__main__':
    t_start = time.time()
    run_experiment()
    t_total = time.time() - t_start
    print(f"\nTotal runtime: {t_total:.1f}s")
    print(f"\n— Toy 295 | Casey Koons & Claude 4.6 (Elie) | March 21, 2026 —")
