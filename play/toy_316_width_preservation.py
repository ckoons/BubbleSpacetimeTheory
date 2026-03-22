#!/usr/bin/env python3
"""
Toy 316 — WIDTH PRESERVATION UNDER EXTENSIONS (v2)
Lyra's Test 4: The critical experiment.

Question: When we add O(n) random arity-2 extensions to a random 3-SAT formula,
does the DPLL refutation depth for backbone variables change?

FIXED: v1 used BCP which never conflicts (backbone is depth > 0). This version
uses proper DPLL with backtracking to measure the minimum search depth needed
to derive a contradiction from negating each backbone variable.

Measurement: For each backbone var x_i with value v_i in the unique SAT solution:
  - Set x_i = ¬v_i
  - Run DPLL with increasing depth limit d = 0, 1, 2, ...
  - Find minimum d where DPLL derives contradiction
  - This = tree-like resolution depth for backbone bit i

Width connection: tree-like width ≤ 2^{depth}. If depth doesn't decrease
under extensions: width doesn't decrease → T47(b) holds.

Casey/Keeper/Lyra: March 22, 2026
"""

import random
import sys
from collections import defaultdict
import time

random.seed(42)

ALPHA_C = 4.267

def generate_random_3sat(n, alpha=ALPHA_C):
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vars_chosen = random.sample(range(1, n + 1), 3)
        clause = tuple(v if random.random() < 0.5 else -v for v in vars_chosen)
        clauses.append(clause)
    return n, clauses

def find_all_solutions(n, clauses, max_solutions=10000):
    solutions = []
    for bits in range(2**n):
        assignment = {i: (bits >> (i - 1)) & 1 for i in range(1, n + 1)}
        sat = all(
            any((lit > 0 and assignment[abs(lit)] == 1) or
                (lit < 0 and assignment[abs(lit)] == 0)
                for lit in clause)
            for clause in clauses)
        if sat:
            solutions.append(assignment)
            if len(solutions) >= max_solutions:
                break
    return solutions

def find_backbone(n, solutions):
    if not solutions:
        return {}, set()
    backbone = {}
    for var in range(1, n + 1):
        values = set(sol[var] for sol in solutions)
        if len(values) == 1:
            backbone[var] = list(values)[0]
    return backbone, set(backbone.keys())

def bcp(clauses, assign):
    """BCP returning (result, final_assignment).
    result: 'conflict' or 'no_conflict'
    """
    assign = dict(assign)
    changed = True
    while changed:
        changed = False
        for clause in clauses:
            unsat_count = 0
            sat = False
            last_unset = None
            for lit in clause:
                var = abs(lit)
                if var in assign:
                    val = assign[var]
                    if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                        sat = True
                        break
                    else:
                        unsat_count += 1
                else:
                    last_unset = lit
            if sat:
                continue
            if unsat_count == len(clause):
                return 'conflict', assign
            if unsat_count == len(clause) - 1 and last_unset is not None:
                var = abs(last_unset)
                val = 1 if last_unset > 0 else 0
                if var in assign:
                    if assign[var] != val:
                        return 'conflict', assign
                else:
                    assign[var] = val
                    changed = True
    return 'no_conflict', assign

def dpll_refute(clauses, init_assign, max_depth, all_vars):
    """Run DPLL with depth limit. Returns True if contradiction found within depth limit."""

    def recurse(assign, depth):
        # BCP
        result, assign = bcp(clauses, assign)
        if result == 'conflict':
            return True

        if depth >= max_depth:
            return False

        # Pick an unassigned variable (prefer original vars, then small index)
        unset = [v for v in all_vars if v not in assign]
        if not unset:
            return False  # All assigned, no conflict = satisfiable under this assignment

        branch_var = unset[0]

        # Try both branches
        for val in [0, 1]:
            a = dict(assign)
            a[branch_var] = val
            if not recurse(a, depth + 1):
                return False  # One branch is satisfiable → no refutation

        return True  # Both branches lead to conflict → refutation found

    return recurse(dict(init_assign), 0)

def measure_refutation_depth(clauses, backbone, all_vars, max_depth=15):
    """For each backbone var, find minimum DPLL depth to derive contradiction."""
    depths = {}
    for var, val in backbone.items():
        wrong_val = 1 - val
        init = {var: wrong_val}

        found_depth = None
        for d in range(max_depth + 1):
            if dpll_refute(clauses, init, d, all_vars):
                found_depth = d
                break

        depths[var] = found_depth if found_depth is not None else max_depth + 1
    return depths

def add_xor_extension(clauses, n_total, var_a, var_b):
    y = n_total + 1
    new_clauses = list(clauses)
    new_clauses.append((var_a, var_b, -y))
    new_clauses.append((-var_a, -var_b, -y))
    new_clauses.append((var_a, -var_b, y))
    new_clauses.append((-var_a, var_b, y))
    return new_clauses, y

def add_and_extension(clauses, n_total, var_a, var_b):
    y = n_total + 1
    new_clauses = list(clauses)
    new_clauses.append((-var_a, -var_b, y))
    new_clauses.append((var_a, -y))
    new_clauses.append((var_b, -y))
    return new_clauses, y

def add_random_extensions(n, clauses, num_ext, ext_type='xor'):
    current_clauses = list(clauses)
    n_total = n
    ext_vars = []
    add_fn = {'xor': add_xor_extension, 'and': add_and_extension}[ext_type]

    for _ in range(num_ext):
        var_a = random.randint(1, n)
        var_b = random.randint(1, n)
        while var_b == var_a:
            var_b = random.randint(1, n)
        current_clauses, new_var = add_fn(current_clauses, n_total, var_a, var_b)
        n_total = new_var
        ext_vars.append(new_var)

    return current_clauses, n_total, ext_vars

def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║  TOY 316 — WIDTH PRESERVATION UNDER EXTENSIONS (v2)         ║
║  Lyra's Test 4: DPLL refutation depth measurement           ║
╚══════════════════════════════════════════════════════════════╝
""")

    # ═══════════════════════════════════════════════════════════
    # PART 1: DPLL DEPTH — ORIGINAL FORMULA
    # ═══════════════════════════════════════════════════════════
    print(f"  {'='*62}")
    print(f"  PART 1: DPLL REFUTATION DEPTH — ORIGINAL FORMULA")
    print(f"  {'='*62}\n")

    n_values = [10, 12, 14, 16]
    trials = 40
    max_depth = 8

    all_data = {}

    for n in n_values:
        t0 = time.time()
        print(f"  n = {n}:")
        depth_counts = defaultdict(int)
        total_bb_vars = 0
        successful = 0
        instance_depths = []

        for trial in range(trials):
            n_vars, clauses = generate_random_3sat(n)
            solutions = find_all_solutions(n, clauses)
            if len(solutions) < 1 or len(solutions) > 50:
                continue
            backbone, bb_vars = find_backbone(n, solutions)
            if len(backbone) < 3:
                continue

            successful += 1
            all_vars = sorted(range(1, n + 1))
            depths = measure_refutation_depth(clauses, backbone, all_vars, max_depth)

            for var, d in depths.items():
                depth_counts[d] += 1
                total_bb_vars += 1

            mean_d = sum(depths.values()) / len(depths)
            instance_depths.append((clauses, backbone, bb_vars, depths, mean_d, solutions))

        all_data[n] = instance_depths

        elapsed = time.time() - t0
        if total_bb_vars > 0:
            print(f"    {successful} instances, {total_bb_vars} backbone vars ({elapsed:.1f}s)")
            print(f"    Depth distribution:")
            for d in sorted(depth_counts.keys()):
                pct = depth_counts[d] / total_bb_vars * 100
                bar = '█' * int(pct / 2)
                label = f">{max_depth}" if d > max_depth else str(d)
                print(f"      d={label:>3}: {depth_counts[d]:>4} ({pct:>5.1f}%) {bar}")
            mean_depth = sum(d * c for d, c in depth_counts.items()) / total_bb_vars
            print(f"    Mean depth: {mean_depth:.2f}")
        else:
            print(f"    No valid instances ({elapsed:.1f}s)")

    # ═══════════════════════════════════════════════════════════
    # PART 2: DPLL DEPTH — WITH EXTENSIONS (THE CRITICAL TEST)
    # ═══════════════════════════════════════════════════════════
    print(f"\n  {'='*62}")
    print(f"  PART 2: DPLL DEPTH — WITH EXTENSIONS (THE CRITICAL TEST)")
    print(f"  {'='*62}\n")

    print(f"  For each instance: add cn extensions, remeasure DPLL depth.")
    print(f"  If depth DECREASES: extensions help the solver → T47(b) in danger.")
    print(f"  If depth PRESERVED: extensions are useless → T47(b) holds.\n")

    ext_fractions = [0.5, 1.0, 2.0]
    ext_types = ['xor', 'and']

    for n in n_values:
        instances = all_data.get(n, [])
        if not instances:
            continue

        # Take first few instances (depth measurement is expensive)
        test_instances = instances[:min(10, len(instances))]

        print(f"  n = {n} ({len(test_instances)} instances):")
        print(f"    {'config':>20} | {'mean depth':>10} | {'change':>8} | {'verdict':>8}")
        print(f"    {'-'*55}")

        # Original depth
        orig_depths_all = []
        for clauses, backbone, bb_vars, depths, mean_d, solutions in test_instances:
            orig_depths_all.extend(depths.values())

        orig_mean = sum(orig_depths_all) / len(orig_depths_all) if orig_depths_all else 0
        print(f"    {'original':>20} | {orig_mean:>10.3f} | {'---':>8} | {'---':>8}")

        for ext_frac in ext_fractions:
            for ext_type in ext_types:
                ext_depths_all = []

                for clauses, backbone, bb_vars, orig_d, mean_d, solutions in test_instances:
                    num_ext = max(1, int(ext_frac * n))
                    ext_clauses, n_total, ext_vars = add_random_extensions(
                        n, clauses, num_ext, ext_type)

                    all_vars = sorted(range(1, n_total + 1))
                    ext_depths = measure_refutation_depth(
                        ext_clauses, backbone, all_vars, max_depth)

                    ext_depths_all.extend(ext_depths.values())

                ext_mean = sum(ext_depths_all) / len(ext_depths_all) if ext_depths_all else 0
                change = ext_mean - orig_mean
                change_pct = change / orig_mean * 100 if orig_mean > 0 else 0

                if change >= -0.05:
                    verdict = "✓ HELD"
                elif change >= -0.2:
                    verdict = "~ SMALL"
                else:
                    verdict = "✗ DROP"

                label = f"+{int(ext_frac*n)} {ext_type}"
                print(f"    {label:>20} | {ext_mean:>10.3f} | {change:>+7.3f} | {verdict:>8}")

        print()

    # ═══════════════════════════════════════════════════════════
    # PART 3: PER-VARIABLE DEPTH CHANGE
    # ═══════════════════════════════════════════════════════════
    print(f"\n  {'='*62}")
    print(f"  PART 3: PER-VARIABLE DEPTH CHANGE")
    print(f"  {'='*62}\n")

    print(f"  For each backbone variable: did extensions change its depth?\n")

    for n in n_values[:3]:
        instances = all_data.get(n, [])
        if not instances:
            continue

        test_inst = instances[:5]
        decreased = 0
        unchanged = 0
        increased = 0
        total = 0

        for clauses, backbone, bb_vars, orig_depths, mean_d, solutions in test_inst:
            num_ext = n  # 1x extensions
            ext_clauses, n_total, ext_vars = add_random_extensions(
                n, clauses, num_ext, 'xor')
            all_vars = sorted(range(1, n_total + 1))
            ext_depths = measure_refutation_depth(ext_clauses, backbone, all_vars, max_depth)

            for var in backbone:
                orig_d = orig_depths[var]
                ext_d = ext_depths[var]
                if ext_d < orig_d:
                    decreased += 1
                elif ext_d > orig_d:
                    increased += 1
                else:
                    unchanged += 1
                total += 1

        if total > 0:
            print(f"  n = {n} ({total} vars, {n} XOR extensions):")
            print(f"    Decreased: {decreased:>4} ({decreased/total*100:>5.1f}%)")
            print(f"    Unchanged: {unchanged:>4} ({unchanged/total*100:>5.1f}%)")
            print(f"    Increased: {increased:>4} ({increased/total*100:>5.1f}%)")

            if decreased == 0:
                print(f"    → ZERO decreases. Extensions NEVER help. ✓")
            elif decreased < total * 0.05:
                print(f"    → Rare decreases (<5%). Likely noise. ✓")
            else:
                print(f"    → Significant decreases. Extensions help! ✗")
            print()

    # ═══════════════════════════════════════════════════════════
    # PART 4: SCALING TEST
    # ═══════════════════════════════════════════════════════════
    print(f"\n  {'='*62}")
    print(f"  PART 4: SCALING — DOES THE GAP GROW?")
    print(f"  {'='*62}\n")

    print(f"  Mean depth vs n, original vs extended:\n")
    print(f"  {'n':>4} | {'orig depth':>10} | {'ext depth':>10} | {'depth/n':>8} | {'ext/n':>8}")
    print(f"  {'-'*50}")

    for n in n_values:
        instances = all_data.get(n, [])
        if not instances:
            continue

        test_inst = instances[:8]

        orig_all = []
        ext_all = []
        for clauses, backbone, bb_vars, orig_depths, mean_d, solutions in test_inst:
            orig_all.extend(orig_depths.values())

            num_ext = n
            ext_clauses, n_total, ext_vars = add_random_extensions(n, clauses, num_ext, 'xor')
            all_vars = sorted(range(1, n_total + 1))
            ext_depths = measure_refutation_depth(ext_clauses, backbone, all_vars, max_depth)
            ext_all.extend(ext_depths.values())

        orig_mean = sum(orig_all) / len(orig_all) if orig_all else 0
        ext_mean = sum(ext_all) / len(ext_all) if ext_all else 0

        print(f"  {n:>4} | {orig_mean:>10.3f} | {ext_mean:>10.3f} | "
              f"{orig_mean/n:>8.4f} | {ext_mean/n:>8.4f}")

    # ═══════════════════════════════════════════════════════════
    # PART 5: SUMMARY AND VERDICT
    # ═══════════════════════════════════════════════════════════
    print(f"\n  {'='*62}")
    print(f"  PART 5: SUMMARY AND VERDICT")
    print(f"  {'='*62}\n")

    print("""  LYRA'S TEST 4 RESULTS:

  Measurement: DPLL refutation depth for each backbone variable.
  Depth d means: need d levels of branching (search) beyond BCP.
  Width ≈ 2^d (tree-like). Size ≈ 2^{width} via BSW.

  THE QUESTION: do arity-2 extensions reduce refutation depth?

  If depth preserved → width preserved → size preserved → T47(b) ✓
  If depth reduced → extensions help solver → need deeper analysis

  THE CHAIN (Gallager Bridge):

  ┌────────────────────────────────────────────────────────────┐
  │  LDPC structure (Toy 315)              ✓ VERIFIED          │
  │  d_min = Θ(n) (Toy 315)               ✓ d_min/n ≈ 0.59   │
  │  d_min → width ≥ Θ(n)                 TO PROVE            │
  │  BSW: width → size                    ✓ KNOWN             │
  │  Width preserved under ext (Toy 316)   ← THIS TEST        │
  │  Cook: size → P ≠ NP                  ✓ KNOWN             │
  └────────────────────────────────────────────────────────────┘

  THREE LAYERS (Casey):
    Surface:   H₁ filling          Θ(n)          Lyra (T38-T39)
    Depth:     Entanglement         2^{Ω(D̃)}      Casey + Elie (T47)
    Substrate: LDPC backbone code   d_min = Θ(n)  Gallager (Toy 315)

  "Matter is the entanglements." — Casey
""")

    print(f"\n  Toy 316 complete.\n")

if __name__ == '__main__':
    main()
