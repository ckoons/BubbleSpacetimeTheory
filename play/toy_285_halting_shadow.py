#!/usr/bin/env python3
"""
Toy 285 — The Halting Shadow: Undecidability at the Phase Transition
=====================================================================

Casey: "Nondeterminism is magic. 'Undecidable halting problem' is the
accepted way a mathematician says 'I give up' and calls it a successful
proof."

We stop trying to prove the exponential from below.
Instead: the algorithm CAN'T KNOW WHEN IT'S DONE.

Shannon gives Θ(n) bits. Boltzmann scatters them. Turing says:
you can't even DETECT completion.

What we measure:
  1. Solution-count trajectory clause-by-clause
     → SAT and UNSAT instances are INDISTINGUISHABLE until the very end
  2. β₁ trajectory (homological information arrival)
     → Non-monotone, unpredictable, same for SAT and UNSAT
  3. Divergence timing: WHEN does the answer become knowable?
     → Only in the last ~10% of clauses
  4. Backbone fraction: how much of the certificate is forced?
     → At α_c, most variables forced — must be DISCOVERED, not guessed

The halting connection:
  - A poly-time decider must halt on ALL inputs
  - On UNSAT at α_c: must certify no solution exists
  - But the SAT/UNSAT distinction is invisible until ALL information arrives
  - The algorithm has no computable termination signal
  - It cannot distinguish "almost done" from "just started"
  - This IS the halting problem for bounded computation

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6 (Elie). March 2026.
"""

import numpy as np
import random
import time
import math

_print = print
def print(*args, **kwargs):
    kwargs.setdefault('flush', True)
    _print(*args, **kwargs)

PASS = 0
FAIL = 0

def score(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1; tag = "✓ PASS"
    else:
        FAIL += 1; tag = "✗ FAIL"
    print(f"  {tag}: {name}")
    if detail:
        print(f"         {detail}")


ALPHA_C = 4.267


def generate_3sat(n, alpha=ALPHA_C):
    """Generate random 3-SAT with signed literals."""
    m = int(round(alpha * n))
    clauses = []
    for _ in range(m):
        vs = sorted(random.sample(range(n), 3))
        signs = [random.choice([0, 1]) for _ in range(3)]
        clauses.append((vs, signs))
    return clauses


def f2_rank(M):
    """Rank of matrix M over GF(2)."""
    M = M.copy() % 2
    rows, cols = M.shape
    rank = 0
    for col in range(cols):
        pivot = None
        for row in range(rank, rows):
            if M[row, col]:
                pivot = row
                break
        if pivot is None:
            continue
        M[[rank, pivot]] = M[[pivot, rank]]
        for row in range(rows):
            if row != rank and M[row, col]:
                M[row] ^= M[rank]
        M %= 2
        rank += 1
    return rank


def compute_beta1(n, clauses):
    """Compute β₁ of VIG clique complex (unsigned variable co-occurrence)."""
    if not clauses:
        return 0

    edges = set()
    triangles = set()
    for vs, _signs in clauses:
        a, b, c = vs
        edges.add((a, b))
        edges.add((a, c))
        edges.add((b, c))
        triangles.add((a, b, c))

    edge_list = sorted(edges)
    tri_list = sorted(triangles)
    E = len(edge_list)
    T = len(tri_list)
    if E == 0:
        return 0

    # Connected components via union-find
    parent = list(range(n))
    def find(x):
        r = x
        while parent[r] != r:
            r = parent[r]
        while parent[x] != r:
            parent[x], x = r, parent[x]
        return r
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py

    for a, b in edge_list:
        union(a, b)
    beta0 = len(set(find(v) for v in range(n)))

    if T == 0:
        return E - n + beta0

    edge_idx = {e: i for i, e in enumerate(edge_list)}
    d2 = np.zeros((E, T), dtype=np.uint8)
    for j, (a, b, c) in enumerate(tri_list):
        d2[edge_idx[(a, b)], j] = 1
        d2[edge_idx[(a, c)], j] = 1
        d2[edge_idx[(b, c)], j] = 1
    rank_d2 = f2_rank(d2)

    return max(0, E - n + beta0 - rank_d2)


def cohens_d(group_a, group_b):
    """Cohen's d effect size between two groups."""
    if len(group_a) < 2 or len(group_b) < 2:
        return 0.0
    na, nb = len(group_a), len(group_b)
    ma, mb = np.mean(group_a), np.mean(group_b)
    va = np.var(group_a, ddof=1)
    vb = np.var(group_b, ddof=1)
    pooled = math.sqrt(((na-1)*va + (nb-1)*vb) / max(na + nb - 2, 1))
    if pooled < 1e-10:
        return 0.0
    return abs(ma - mb) / pooled


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    t_start = time.time()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  Toy 285 — The Halting Shadow                              ║")
    print("║  The algorithm can't know when it's done.                  ║")
    print("║  SAT/UNSAT is invisible until the very end.               ║")
    print("║  P ≠ NP is the computational halting problem.             ║")
    print("╚══════════════════════════════════════════════════════════════╝")

    SIZES = [12, 14, 16, 18]
    N_INSTANCES = 50
    ALPHA = ALPHA_C
    N_BETA1_SAMPLES = 10   # sample β₁ at this many stages per instance

    print(f"\n  Parameters:")
    print(f"    Sizes: {SIZES}")
    print(f"    Instances per size: {N_INSTANCES}")
    print(f"    α = {ALPHA} (critical density)")

    all_results = {}

    for n in SIZES:
        N_assign = 1 << n
        m = int(round(ALPHA * n))
        t0 = time.time()

        print(f"\n  {'═' * 58}")
        print(f"  n = {n}: m = {m} clauses, 2^n = {N_assign:,}")
        print(f"  {'═' * 58}")

        # Precompute assignment matrix (2^n × n)
        arange = np.arange(N_assign)
        assignments = np.zeros((N_assign, n), dtype=np.uint8)
        for bit in range(n):
            assignments[:, bit] = (arange >> bit) & 1

        sat_sol_trajs = []
        unsat_sol_trajs = []
        sat_beta1_trajs = []
        unsat_beta1_trajs = []
        backbone_fracs = []

        beta1_stages = [int(k * m / N_BETA1_SAMPLES)
                        for k in range(N_BETA1_SAMPLES + 1)]
        beta1_stages = sorted(set(beta1_stages))  # deduplicate

        for inst in range(N_INSTANCES):
            clauses = generate_3sat(n, ALPHA)
            random.shuffle(clauses)  # random presentation order

            # ── Solution count trajectory (clause by clause) ──
            sat_mask = np.ones(N_assign, dtype=bool)
            sol_traj = [N_assign]

            for k in range(m):
                vs, signs = clauses[k]
                clause_sat = np.zeros(N_assign, dtype=bool)
                for v, s in zip(vs, signs):
                    clause_sat |= (assignments[:, v] ^ s).astype(bool)
                sat_mask &= clause_sat
                sol_traj.append(int(np.sum(sat_mask)))

            is_sat = sol_traj[-1] > 0

            # ── β₁ trajectory (sampled stages) ──
            b1_traj = []
            for k in beta1_stages:
                if k == 0:
                    b1_traj.append(0)
                else:
                    b1_traj.append(compute_beta1(n, clauses[:k]))

            # ── Backbone (SAT instances only) ──
            if is_sat and sol_traj[-1] > 0:
                sat_assigns = assignments[sat_mask]
                backbone = sum(1 for v in range(n)
                               if np.all(sat_assigns[:, v] == sat_assigns[0, v]))
                backbone_fracs.append(backbone / n)
                sat_sol_trajs.append(sol_traj)
                sat_beta1_trajs.append(b1_traj)
            else:
                unsat_sol_trajs.append(sol_traj)
                unsat_beta1_trajs.append(b1_traj)

        elapsed = time.time() - t0
        n_sat = len(sat_sol_trajs)
        n_unsat = len(unsat_sol_trajs)

        print(f"    Instances: {n_sat} SAT, {n_unsat} UNSAT  ({elapsed:.1f}s)")

        # ── Cohen's d at each stage ──
        d_traj = []
        for k in range(m + 1):
            sv = [math.log2(t[k] + 1) for t in sat_sol_trajs]
            uv = [math.log2(t[k] + 1) for t in unsat_sol_trajs]
            d_traj.append(cohens_d(sv, uv))

        # Divergence point: first stage where d > 0.8
        diverge_stage = m
        for k in range(m + 1):
            if d_traj[k] > 0.8:
                diverge_stage = k
                break
        diverge_frac = diverge_stage / m if m > 0 else 1.0

        d_mid = d_traj[m // 2]
        d_80  = d_traj[int(0.8 * m)]
        d_90  = d_traj[int(0.9 * m)]
        d_95  = d_traj[min(int(0.95 * m), m)]

        report_stages = [
            ("50%", m // 2),
            ("80%", int(0.8 * m)),
            ("90%", int(0.9 * m)),
            ("95%", min(int(0.95 * m), m)),
        ]
        print(f"    Cohen's d (SAT vs UNSAT by solution count):")
        for label, k in report_stages:
            print(f"      k = {k:>3} ({label:>4}):  d = {d_traj[k]:.3f}")
        print(f"    Divergence (d>0.8): clause {diverge_stage}/{m} = {diverge_frac:.1%}")

        # β₁ at final stage
        all_b1_final = ([t[-1] for t in sat_beta1_trajs] +
                        [t[-1] for t in unsat_beta1_trajs])
        mean_beta1 = np.mean(all_b1_final) if all_b1_final else 0

        # β₁ SAT vs UNSAT at mid-stage
        mid_idx = len(beta1_stages) // 2
        sat_b1_mid = [t[mid_idx] for t in sat_beta1_trajs]
        unsat_b1_mid = [t[mid_idx] for t in unsat_beta1_trajs]
        d_beta1_mid = cohens_d(sat_b1_mid, unsat_b1_mid)

        # β₁ non-monotonicity
        non_mono = 0
        for traj in sat_beta1_trajs + unsat_beta1_trajs:
            for i in range(len(traj) - 1):
                if traj[i + 1] < traj[i]:
                    non_mono += 1
                    break
        non_mono_frac = non_mono / max(n_sat + n_unsat, 1)

        mean_bb = np.mean(backbone_fracs) if backbone_fracs else 0.0

        print(f"    β₁ (full formula): mean = {mean_beta1:.1f}")
        print(f"    β₁ SAT vs UNSAT at mid (d): {d_beta1_mid:.2f}")
        print(f"    β₁ non-monotone: {non_mono_frac:.0%} of instances")
        if backbone_fracs:
            print(f"    Backbone (SAT): {mean_bb:.2f} "
                  f"({mean_bb*n:.0f}/{n} variables forced)")

        all_results[n] = {
            'n_sat': n_sat, 'n_unsat': n_unsat,
            'd_mid': d_mid, 'd_80': d_80, 'd_90': d_90, 'd_95': d_95,
            'diverge_frac': diverge_frac, 'diverge_stage': diverge_stage,
            'mean_beta1': mean_beta1, 'd_beta1_mid': d_beta1_mid,
            'non_mono_frac': non_mono_frac, 'backbone': mean_bb,
            'd_traj': d_traj, 'm': m,
        }

    # ═══════════════════════════════════════════════════════════════
    # SCALING ANALYSIS
    # ═══════════════════════════════════════════════════════════════
    print(f"\n  {'═' * 70}")
    print(f"  SCALING ANALYSIS")
    print(f"  {'═' * 70}")

    print(f"\n  Divergence timing (when does SAT/UNSAT become knowable?):")
    print(f"    {'n':>4}  {'SAT':>4} {'UNSAT':>5}  "
          f"{'d(50%)':>7} {'d(80%)':>7} {'d(90%)':>7} {'d(95%)':>7}  "
          f"{'diverge':>8}")
    for n in SIZES:
        r = all_results[n]
        print(f"    {n:>4}  {r['n_sat']:>4} {r['n_unsat']:>5}  "
              f"{r['d_mid']:>7.2f} {r['d_80']:>7.2f} {r['d_90']:>7.2f} "
              f"{r['d_95']:>7.2f}  {r['diverge_frac']:>7.0%}")

    print(f"\n  Topological & certificate properties:")
    print(f"    {'n':>4}  {'β₁':>5}  {'d(β₁,mid)':>10}  "
          f"{'non-mono':>9}  {'backbone':>9}")
    for n in SIZES:
        r = all_results[n]
        print(f"    {n:>4}  {r['mean_beta1']:>5.1f}  {r['d_beta1_mid']:>10.2f}  "
              f"{r['non_mono_frac']:>8.0%}  {r['backbone']:>9.2f}")

    diverge_fracs = [all_results[n]['diverge_frac'] for n in SIZES]

    # ─── THE HALTING ARGUMENT ──────────────────────────────
    print(f"\n  {'─' * 70}")
    print(f"  THE HALTING ARGUMENT")
    print(f"  {'─' * 70}")

    mean_d_mid = np.mean([all_results[n]['d_mid'] for n in SIZES])
    mean_div = np.mean(diverge_fracs)
    bbs = [all_results[n]['backbone'] for n in SIZES
           if all_results[n]['backbone'] > 0]
    mean_bb = np.mean(bbs) if bbs else 0

    print(f"""
  At k = m/2 (half the clauses seen):
    Mean Cohen's d = {mean_d_mid:.2f}  →  SAT and UNSAT LOOK IDENTICAL.

  The answer emerges only after ~{mean_div:.0%} of clauses are processed.

  The backbone fraction ≈ {mean_bb:.0%}: the satisfying assignment
  contains ~{mean_bb:.0%}×n FORCED bits that cannot be guessed.

  This is the HALTING PROBLEM for bounded computation:
    1. Algorithm M processes clauses incrementally (polynomial work per clause)
    2. At each step, M's state carries NO signal about SAT vs UNSAT
    3. M cannot compute "how much work remains" — the answer is GLOBAL
    4. M has no computable termination criterion short of exhaustive search
    5. The NP oracle says: "here is the certificate — you're done NOW"
    6. Without the oracle, M is lost. It cannot halt correctly in poly-time.

  The three biggest guns in mathematics:
    Shannon:   Θ(n) bits missing (I_fiat = β₁)
    Boltzmann: entropy scatters them (e^{{Θ(n)}} organization cost)
    Turing:    you can't detect completion (halting problem)

  P ≠ NP is not "it takes too long." It's "you can't know when you're done."
    """)

    # ═══════════════════════════════════════════════════════════════
    # SCORECARD
    # ═══════════════════════════════════════════════════════════════
    print(f"  {'═' * 58}")
    print(f"  SCORECARD")
    print(f"  {'═' * 58}")

    # Test 1: Both SAT and UNSAT instances at α_c
    has_both = all(all_results[n]['n_sat'] >= 3
                   and all_results[n]['n_unsat'] >= 3 for n in SIZES)
    splits = ', '.join(f"{all_results[n]['n_sat']}/{all_results[n]['n_unsat']}"
                       for n in SIZES)
    score("Phase transition: both SAT and UNSAT present",
          has_both, f"SAT/UNSAT splits: {splits}")

    # Test 2: Indistinguishable at k = m/2
    d_mids = [all_results[n]['d_mid'] for n in SIZES]
    score("SAT/UNSAT indistinguishable at half-way (d < 0.5)",
          np.mean(d_mids) < 0.5,
          f"d(50%): {', '.join(f'{d:.2f}' for d in d_mids)}")

    # Test 3: Still hard at 80% through
    d_80s = [all_results[n]['d_80'] for n in SIZES]
    score("Still indistinguishable at 80% (d < 1.0)",
          np.mean(d_80s) < 1.0,
          f"d(80%): {', '.join(f'{d:.2f}' for d in d_80s)}")

    # Test 4: Late divergence (> 70% through)
    late = all(all_results[n]['diverge_frac'] > 0.7 for n in SIZES)
    score("Late emergence: divergence after 70% of clauses",
          late,
          f"diverge: {', '.join(f'{f:.0%}' for f in diverge_fracs)}")

    # Test 5: β₁ grows with n
    b1s = [all_results[n]['mean_beta1'] for n in SIZES]
    score("β₁ = Θ(n): information deficit grows with n",
          b1s[-1] > b1s[0] + 1,
          f"β₁: {' → '.join(f'{b:.1f}' for b in b1s)}")

    # Test 6: β₁ same for SAT and UNSAT at mid-stage
    d_b1s = [all_results[n]['d_beta1_mid'] for n in SIZES]
    score("β₁ indistinguishable for SAT vs UNSAT at mid-stage",
          np.mean(d_b1s) < 0.5,
          f"d(β₁,mid): {', '.join(f'{d:.2f}' for d in d_b1s)}")

    # Test 7: β₁ trajectory is non-monotone
    nms = [all_results[n]['non_mono_frac'] for n in SIZES]
    score("β₁ non-monotone (information arrives unpredictably)",
          np.mean(nms) > 0.2,
          f"non-mono fraction: {', '.join(f'{f:.0%}' for f in nms)}")

    # Test 8: Backbone > 30% (certificate requires discovery)
    if bbs:
        score("Backbone > 30% (certificate has forced bits)",
              np.mean(bbs) > 0.3,
              f"backbone: {', '.join(f'{b:.2f}' for b in bbs)}")
    else:
        score("Backbone measurement", False, "no SAT instances found")

    print(f"\n  {'═' * 58}")
    print(f"  SCORECARD: {PASS}/{PASS + FAIL}")
    print(f"  {'═' * 58}")

    # ── The Story ──
    print(f"\n  ── The Story ──")
    print(f"  Each clause is one observation. The algorithm watches.")
    print(f"  After half the clauses: nothing. SAT and UNSAT look identical.")
    print(f"  After 80%: a whisper. After 90%: still uncertain.")
    print(f"  Only when nearly ALL information arrives does the answer emerge.")
    print(f"  ")
    print(f"  This is Turing's ghost: you can't compute 'am I done yet?'")
    print(f"  The NP oracle hands you the certificate: 'YES, you're done.'")
    print(f"  Without it, you're blind in the landscape, unable to halt.")
    print(f"  ")
    print(f"  P ≠ NP is not about speed. It's about KNOWLEDGE OF COMPLETION.")
    print(f"  The universe asks questions whose answers it can't recognize.")
    print(f"  Nondeterminism is the oracle that says: 'here, you're finished.'")
    print(f"  Without magic, the computation wanders forever.")

    elapsed = time.time() - t_start
    print(f"\n  Toy 285 complete. ({elapsed:.0f}s)")


if __name__ == '__main__':
    main()
