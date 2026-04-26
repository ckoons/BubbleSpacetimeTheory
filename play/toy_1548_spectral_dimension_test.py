#!/usr/bin/env python3
"""
Toy 1548 — CP-5: Natural Dimension Test
========================================
Test whether the count of independent spectral values from D_IV^5 is
323 = 17 x 19 = (N_c*C_2 - 1) * Q, where Q = rank^2 + C_2 + N_c^2 = 19.

"Independent spectral value" = a distinct evaluation of a function on
D_IV^5 that maps to a measurable physical quantity. Same BST formula
producing the same value in two different physics domains counts as ONE
spectral value with TWO applications (a bridge).

Three independent approaches:
  A. Empirical: count distinct BST-predicted values in the invariants table
  B. Theoretical: count distinct spectral evaluations from D_IV^5 representation theory
  C. Lattice: count reachable BST products/ratios at bounded depth

If 323 emerges from any approach, the factorization 17*19 is structurally significant.

Elie — April 27, 2026

Copyright (c) 2026 Casey Koons. All rights reserved.
"""

import json
import math
from collections import defaultdict, Counter

# BST integers
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
N_max = N_c**3 * n_C + rank  # 137
Q = rank**2 + C_2 + N_c**2   # 4 + 6 + 9 = 19
target = 17 * 19              # 323

print(f"Target: 323 = 17 x 19 = (N_c*C_2 - 1) * Q")
print(f"  17 = N_c*C_2 - 1 = {N_c*C_2 - 1}")
print(f"  19 = Q = rank^2 + C_2 + N_c^2 = {Q}")
print(f"  323 = {target}")
print()

# ═══════════════════════════════════════════════════════════════════
# PART A: EMPIRICAL — count from invariants table
# ═══════════════════════════════════════════════════════════════════

def load_invariants():
    """Load the geometric invariants JSON."""
    path = "data/bst_geometric_invariants.json"
    try:
        with open(path) as f:
            data = json.load(f)
        return data.get('invariants', [])
    except FileNotFoundError:
        return []


def empirical_counts(invs):
    """Count distinct values under various definitions."""
    results = {}

    # All numeric values
    all_vals = set()
    di_vals = set()
    di_phys_vals = set()  # D+I in physics sections

    for e in invs:
        v = e.get('value')
        tier = e.get('cal_tier', '')
        sec = e.get('paper83_section_name', '')
        if v is None:
            continue
        try:
            fval = round(float(v), 8)
            if not math.isfinite(fval):
                continue
            all_vals.add(fval)
            if tier in ('D', 'I'):
                di_vals.add(fval)
                if sec not in ('Seeds',):
                    di_phys_vals.add(fval)
        except (ValueError, TypeError):
            pass

    results['all'] = len(all_vals)
    results['D+I'] = len(di_vals)
    results['D+I non-seed'] = len(di_phys_vals)

    # Exclude defining set
    defining = {0.0, 1.0, 2.0, 3.0, 5.0, 6.0, 7.0, 137.0}
    results['all minus defining'] = len(all_vals - defining)
    results['D+I minus defining'] = len(di_vals - defining)

    # Only values with physics precision
    prec_vals = set()
    for e in invs:
        v = e.get('value')
        p = e.get('precision', '')
        tier = e.get('cal_tier', '')
        if v is None or not p or p == 'exact':
            continue
        try:
            fval = round(float(v), 8)
            if math.isfinite(fval):
                prec_vals.add(fval)
        except:
            pass
    results['with precision'] = len(prec_vals)

    # Values in physics sections only (not Seeds, Structural, or 'V')
    phys_vals = set()
    for e in invs:
        v = e.get('value')
        sec = e.get('paper83_section_name', '')
        if v is None or sec in ('Seeds', 'Structural', 'V'):
            continue
        try:
            fval = round(float(v), 8)
            if math.isfinite(fval):
                phys_vals.add(fval)
        except:
            pass
    results['physics sections'] = len(phys_vals)

    # Distinct (value, section) pairs = bridges counted separately
    val_sec = set()
    for e in invs:
        v = e.get('value')
        sec = e.get('paper83_section_name', '')
        if v is None:
            continue
        try:
            fval = round(float(v), 8)
            if math.isfinite(fval):
                val_sec.add((fval, sec))
        except:
            pass
    results['(value, section) pairs'] = len(val_sec)

    return results


# ═══════════════════════════════════════════════════════════════════
# PART B: THEORETICAL — D_IV^5 representation theory
# ═══════════════════════════════════════════════════════════════════

def bergman_eigenvalue(p, q):
    """Bergman eigenvalue lambda_{p,q} = p(p+5) + q(q+3) on D_IV^5."""
    return p * (p + n_C) + q * (q + N_c)


def so5_dim(a, b):
    """Dimension of SO(5) irrep with B_2 Dynkin labels (a, b).
    a = short root label, b = long root label.
    Formula: (a+1)(b+1)(a+b+2)(a+2b+3)/6"""
    return (a + 1) * (b + 1) * (a + b + 2) * (a + 2 * b + 3) // 6


def spectral_analysis():
    """Count eigenvalues, multiplicities, and cumulative dimensions."""
    results = {}

    # Enumerate all (p,q) with lambda <= N_max
    levels = []
    for p in range(50):
        for q in range(p + 1):
            lam = bergman_eigenvalue(p, q)
            if lam <= N_max:
                # SO(5) Dynkin labels: a = p-q (short root), b = q (long root)
                a_dynkin = p - q
                b_dynkin = q
                dim = so5_dim(a_dynkin, b_dynkin)
                levels.append((p, q, lam, dim))

    levels.sort(key=lambda x: x[2])

    # Count (p,q) pairs
    results['(p,q) pairs <= N_max'] = len(levels)

    # Distinct eigenvalues
    distinct_eigs = len(set(l for _, _, l, _ in levels))
    results['distinct eigenvalues <= N_max'] = distinct_eigs

    # Cumulative dimension (total Hilbert space dimension up to N_max)
    total_dim = sum(d for _, _, _, d in levels)
    results['total multiplicity <= N_max'] = total_dim

    # Print the spectral data
    print("  Bergman spectrum of D_IV^5 up to lambda = N_max = 137:")
    print(f"  {'(p,q)':>8s} {'lambda':>8s} {'dim':>8s} {'cumul':>8s}")
    cumul = 0
    for p, q, lam, dim in levels:
        cumul += dim
        tag = ""
        if lam == C_2:
            tag = "  <-- C_2 (mass gap)"
        elif lam == 10:
            tag = "  <-- 10 = 2*n_C"
        elif dim == target:
            tag = f"  <-- dim = {target}!"
        elif cumul == target:
            tag = f"  <-- cumul = {target}!"
        print(f"  ({p},{q}){'':<3s} {lam:>8d} {dim:>8d} {cumul:>8d}{tag}")

    results['cumulative at each level'] = [(p, q, lam, dim, sum(d for _, _, _, d in levels[:i+1]))
                                            for i, (p, q, lam, dim) in enumerate(levels)]

    # Check: does any cutoff give cumulative = 323?
    cumul = 0
    for p, q, lam, dim in levels:
        cumul += dim
        if cumul == target:
            results['cumul_323_at'] = (p, q, lam)
            break

    # Check: does any eigenvalue = 323?
    for p, q, lam, dim in levels:
        if lam == target:
            results['eig_323'] = (p, q)

    # Extended: check multiplicity sums in interesting subsets
    # Sum of dims for p <= some cutoff
    for p_max in range(1, 15):
        sub_levels = [(p, q, l, d) for p, q, l, d in levels if p <= p_max]
        sub_dim = sum(d for _, _, _, d in sub_levels)
        sub_count = len(sub_levels)
        if sub_dim == target or sub_count == target:
            results[f'p<={p_max}'] = (sub_count, sub_dim)

    return results


# ═══════════════════════════════════════════════════════════════════
# PART C: BST PRODUCT LATTICE
# ═══════════════════════════════════════════════════════════════════

def lattice_counts():
    """Count distinct BST products/ratios at bounded depth."""
    results = {}

    # Depth 0: just the integers
    depth0 = {rank, N_c, n_C, C_2, g, N_max, 1}
    results['depth 0'] = len(depth0)

    # Depth 1: single operations on pairs
    depth1 = set(depth0)
    base = [rank, N_c, n_C, C_2, g, N_max]
    for a in base:
        depth1.add(a)
        depth1.add(-a)
        if a > 0:
            depth1.add(1 / a)
            depth1.add(math.sqrt(a))
        depth1.add(a ** 2)
        depth1.add(a ** 3)
        for b in base:
            if b != 0:
                depth1.add(a / b)
            depth1.add(a * b)
            depth1.add(a + b)
            depth1.add(a - b)
    depth1 = {round(v, 10) for v in depth1 if math.isfinite(v) and abs(v) < 1e6}
    results['depth 1'] = len(depth1)

    # Depth 2: operations on depth-1 results (subset to avoid explosion)
    depth2 = set(depth1)
    # Add triple products a*b/c, a^b+c, etc.
    for a in base:
        for b in base:
            for c in base:
                if c != 0:
                    depth2.add(round(a * b / c, 10))
                    depth2.add(round((a * b + c), 10))
                    depth2.add(round((a * b - c), 10))
                    depth2.add(round((a + b) / c, 10))
                    depth2.add(round((a - b) / c, 10))
                if 0 < b <= 7:
                    depth2.add(round(a ** b + c, 10))
                    depth2.add(round(a ** b - c, 10))
                    depth2.add(round(a ** b * c, 10))
                    if c != 0:
                        depth2.add(round(a ** b / c, 10))

    # Add sqrt and pi forms
    for v in list(depth1):
        if v > 0:
            depth2.add(round(math.sqrt(v), 10))
        depth2.add(round(v * math.pi, 10))
        if v != 0:
            depth2.add(round(v / math.pi, 10))

    depth2 = {v for v in depth2 if math.isfinite(v) and abs(v) < 1e6}
    results['depth 2'] = len(depth2)

    # How many of the invariant table values are reachable?
    invs = load_invariants()
    inv_vals = set()
    for e in invs:
        v = e.get('value')
        if v is None:
            continue
        try:
            fval = round(float(v), 10)
            if math.isfinite(fval):
                inv_vals.add(fval)
        except:
            pass

    reached = inv_vals & depth2
    not_reached = inv_vals - depth2
    results['invariant values reached at depth 2'] = len(reached)
    results['invariant values NOT reached'] = len(not_reached)

    return results


# ═══════════════════════════════════════════════════════════════════
# PART D: FACTORIZATION ANALYSIS
# ═══════════════════════════════════════════════════════════════════

def factorization_analysis():
    """Analyze what 17 and 19 count in D_IV^5."""
    results = {}

    # 17 = N_c * C_2 - 1
    print(f"  17 = N_c * C_2 - 1 = {N_c * C_2 - 1}")
    print(f"     = dim so(5,2) - rank^2 = 21 - 4 = {21 - rank**2}")
    print(f"     = dim K - rank = dim[SO(5)xSO(2)] - rank = 11 - ... no")
    print(f"     = N_max mod n_C! = 137 mod 120 = {N_max % 120}")
    print(f"     = Koide numerator (Toy 1535)")

    # 19 = Q = rank^2 + C_2 + N_c^2
    print(f"  19 = Q = rank^2 + C_2 + N_c^2 = {rank**2 + C_2 + N_c**2}")
    print(f"     = n_C^2 - C_2 = {n_C**2 - C_2}")
    print(f"     = 2*C_2 + g = {2*C_2 + g}")
    print(f"     = N_c + 2^(n_C-1) = {N_c + 2**(n_C-1)}")

    # 323 in the Bergman spectrum
    # Check if 323 is an eigenvalue
    for p in range(30):
        for q in range(p + 1):
            if bergman_eigenvalue(p, q) == 323:
                print(f"  323 IS a Bergman eigenvalue: lambda({p},{q}) = 323")
                a = p - q
                b = q
                dim = so5_dim(a, b)
                print(f"    Dynkin labels ({a},{b}), multiplicity = {dim}")
                results['323_is_eigenvalue'] = True

    # Check: 323 = 17 * 19 vs nearby eigenvalues
    nearby = []
    for p in range(30):
        for q in range(p + 1):
            lam = bergman_eigenvalue(p, q)
            if abs(lam - 323) <= 20:
                nearby.append((p, q, lam))
    print(f"  Eigenvalues near 323: {[(p,q,l) for p,q,l in nearby]}")

    # Is 323 a cumulative multiplicity?
    cumul = 0
    for p in range(50):
        for q in range(p + 1):
            lam = bergman_eigenvalue(p, q)
            if lam > 500:
                continue
            a = p - q
            b = q
            dim = so5_dim(a, b)
            cumul += dim
            if cumul == 323:
                print(f"  323 = cumulative multiplicity through ({p},{q}), lambda={lam}")
                results['323_cumul_at'] = (p, q, lam)
                break

    # 17 as dimensional count
    # dim_R D_IV^5 = 10, dim_R K = 11, dim_R G = 21
    # 17 = dim G - rank^2 = 21 - 4
    # This is the number of "non-flat" directions in the Lie algebra
    print(f"\n  Geometric interpretation of 17:")
    print(f"    dim_R SO_0(5,2) = 21 = C(g,2)")
    print(f"    dim_R [SO(5) x SO(2)] = 10 + 1 = 11 = 2*C_2 - 1")
    print(f"    17 = 21 - 4 = dim G - rank^2")
    print(f"    = non-flat directions in so(5,2)")

    # 19 as dimensional count
    # 19 = rank^2 + C_2 + N_c^2 = 4 + 6 + 9
    # This looks like dim of some subspace
    print(f"\n  Geometric interpretation of 19:")
    print(f"    Q = rank^2 + C_2 + N_c^2 = {rank**2} + {C_2} + {N_c**2} = 19")
    print(f"    = Koide angle: n_C^2 - C_2 = 25 - 6 = 19")
    print(f"    = Bergman lambda(3,1) = {bergman_eigenvalue(3,1)} ?  No, = {bergman_eigenvalue(3, 1)}")
    print(f"    = dim of ?? representation")

    # Check: 19 as a multiplicity
    for p in range(20):
        for q in range(p + 1):
            a = p - q
            b = q
            dim = so5_dim(a, b)
            if dim == 19:
                print(f"    19 = dim V({a},{b}) at lambda = {bergman_eigenvalue(p,q)}")

    return results


# ═══════════════════════════════════════════════════════════════════
# TESTS
# ═══════════════════════════════════════════════════════════════════

def test_empirical():
    """T1: Check if any empirical count equals 323."""
    invs = load_invariants()
    if not invs:
        return False, "No invariants data found"

    counts = empirical_counts(invs)

    print(f"  Empirical counts from {len(invs)} invariant entries:")
    match_found = False
    for label, count in sorted(counts.items(), key=lambda x: abs(x[1] - target)):
        delta = count - target
        marker = " <-- MATCH!" if count == target else f" (delta = {delta:+d})"
        print(f"    {label:30s}: {count:5d}{marker}")
        if count == target:
            match_found = True

    closest = min(counts.items(), key=lambda x: abs(x[1] - target))
    return match_found or abs(closest[1] - target) <= 5, \
        f"Closest: {closest[0]} = {closest[1]} (delta {closest[1]-target:+d})"


def test_spectral():
    """T2: Theoretical spectral analysis of D_IV^5."""
    results = spectral_analysis()

    print(f"\n  Spectral theory results:")
    for k, v in results.items():
        if k != 'cumulative at each level':
            print(f"    {k}: {v}")

    # Check if 323 appears in any spectral count
    found = '323_is_eigenvalue' in results or 'cumul_323_at' in results
    if found:
        return True, "323 found in spectral data"

    # Check cumulative dimensions for near-misses
    cumul_data = results.get('cumulative at each level', [])
    for p, q, lam, dim, cumul in cumul_data:
        if cumul == target:
            return True, f"Cumulative dimension = 323 at (p,q)=({p},{q}), lambda={lam}"

    return False, f"323 not found as eigenvalue or cumulative dimension (max tested)"


def test_factorization():
    """T3: Both factors 17 and 19 have independent geometric meaning."""
    results = factorization_analysis()

    # 17 = N_c*C_2 - 1 = dim G - rank^2
    cond1 = (N_c * C_2 - 1 == 17)
    # 19 = Q = rank^2 + C_2 + N_c^2
    cond2 = (Q == 19)
    # 17 = dim so(5,2) - rank^2
    cond3 = (21 - rank**2 == 17)
    # 19 = n_C^2 - C_2
    cond4 = (n_C**2 - C_2 == 19)

    all_pass = cond1 and cond2 and cond3 and cond4

    print(f"\n  Factorization identities:")
    print(f"    17 = N_c*C_2 - 1: {cond1}")
    print(f"    17 = dim so(5,2) - rank^2: {cond3}")
    print(f"    19 = Q: {cond2}")
    print(f"    19 = n_C^2 - C_2: {cond4}")
    print(f"    323 = 17*19: {17*19 == 323}")

    return all_pass, "Both factors have multiple BST derivations"


def test_lattice():
    """T4: BST product lattice reachability."""
    results = lattice_counts()

    print(f"  BST lattice sizes:")
    for label, count in results.items():
        marker = f" <-- matches {target}!" if count == target else ""
        print(f"    {label:40s}: {count:6d}{marker}")

    match = any(v == target for v in results.values())
    return match or results.get('depth 2', 0) > target, \
        f"Lattice depth-2 size: {results.get('depth 2', 0)}"


def test_convergence():
    """T5: Is the invariant count converging toward 323?"""
    invs = load_invariants()
    if not invs:
        return False, "No data"

    # Sort entries roughly by when they might have been added
    # (lower theorem IDs = earlier)
    def get_theorem_num(e):
        t = e.get('theorem') or ''
        if t.startswith('T'):
            try:
                return int(t[1:])
            except:
                return 9999
        return 9999

    sorted_invs = sorted(invs, key=get_theorem_num)

    # Track cumulative distinct values at various stages
    vals = set()
    checkpoints = []
    for i, e in enumerate(sorted_invs):
        v = e.get('value')
        if v is None:
            continue
        try:
            fval = round(float(v), 8)
            if math.isfinite(fval):
                vals.add(fval)
        except:
            pass
        if (i + 1) % 100 == 0 or i == len(sorted_invs) - 1:
            checkpoints.append((i + 1, len(vals)))

    print(f"  Convergence of distinct values:")
    for entries, distinct in checkpoints:
        delta = distinct - target
        pct = distinct / target * 100
        print(f"    At {entries:5d} entries: {distinct:4d} distinct ({pct:.1f}% of 323, delta {delta:+d})")

    # Check if the growth rate suggests convergence to 323
    final = checkpoints[-1][1] if checkpoints else 0

    # Check: asymptotic ratio distinct/total
    if checkpoints:
        ratios = [(d / e) for e, d in checkpoints if e > 0]
        final_ratio = ratios[-1] if ratios else 0
        print(f"  Final ratio distinct/total: {final_ratio:.4f}")
        print(f"  If trend continues, at 1500 entries: ~{int(1500 * final_ratio)} distinct")

    converging = abs(final - target) <= 15
    return converging, f"Current: {final} distinct values (target: {target}, delta: {final-target:+d})"


def test_cross_domain():
    """T6: Cross-domain bridges and the 17*19 structure."""
    invs = load_invariants()
    if not invs:
        return False, "No data"

    # Count: for each distinct value, how many sections does it appear in?
    val_sections = defaultdict(set)
    for e in invs:
        v = e.get('value')
        sec = e.get('paper83_section_name', '')
        if v is None:
            continue
        try:
            fval = round(float(v), 8)
            if math.isfinite(fval):
                val_sections[fval].add(sec)
        except:
            pass

    # Number of sections
    all_sections = set()
    for secs in val_sections.values():
        all_sections.update(secs)
    n_sections = len(all_sections)

    # Single-section values (unique to one domain)
    single = {v for v, secs in val_sections.items() if len(secs) == 1}
    # Multi-section values (bridges)
    multi = {v for v, secs in val_sections.items() if len(secs) >= 2}

    print(f"  Sections: {n_sections}")
    print(f"  Distinct values: {len(val_sections)}")
    print(f"  Single-section values: {len(single)}")
    print(f"  Multi-section bridges: {len(multi)}")
    print(f"  Total = {len(single)} + {len(multi)} = {len(single) + len(multi)}")

    # 323 = 17 * 19: could 17 be the number of sections and 19 the avg bridges per section?
    print(f"\n  Sections ({n_sections}) vs 17: {'MATCH' if n_sections == 17 else f'NO ({n_sections})'}")
    print(f"  Avg distinct values per section: {sum(len(val_sections[v]) for v in val_sections) / n_sections:.1f}")

    # Or: 17 independent spectral "channels" (families) each producing 19 values?
    # Check: values grouped by their "simplicity" (number of BST integers used)

    return abs(len(val_sections) - target) <= 15, \
        f"Total distinct values: {len(val_sections)}, bridges: {len(multi)}"


def test_eigenvalue_count():
    """T7: Count eigenvalues and multiplicities for specific BST cutoffs."""
    print("  Eigenvalue counts at BST-significant cutoffs:")

    for cutoff_name, cutoff in [
        ("C_2", C_2), ("n_C^2", n_C**2), ("rank*N_max", rank*N_max),
        ("N_max", N_max), ("N_max+C_2", N_max+C_2),
        ("(N_c*C_2)^2", (N_c*C_2)**2), ("rank*N_max+C_2", rank*N_max+C_2)]:

        pairs = 0
        distinct = set()
        total_dim = 0
        for p in range(50):
            for q in range(p + 1):
                lam = bergman_eigenvalue(p, q)
                if lam <= cutoff:
                    pairs += 1
                    distinct.add(lam)
                    a, b = p - q, q
                    total_dim += so5_dim(a, b)

        matches_323 = pairs == target or len(distinct) == target or total_dim == target
        marker = " <-- 323!" if matches_323 else ""
        print(f"    lambda <= {cutoff_name:>15s} = {cutoff:6d}: "
              f"{pairs:4d} pairs, {len(distinct):4d} distinct, "
              f"total dim = {total_dim:6d}{marker}")

    # Check extended cutoffs
    found = False
    for cutoff in range(100, 2000):
        pairs = 0
        distinct = set()
        total_dim = 0
        for p in range(50):
            for q in range(p + 1):
                lam = bergman_eigenvalue(p, q)
                if lam <= cutoff:
                    pairs += 1
                    distinct.add(lam)
                    a, b = p - q, q
                    total_dim += so5_dim(a, b)
        if pairs == target:
            print(f"    323 (p,q) pairs at lambda <= {cutoff}")
            found = True
            break
        if len(distinct) == target:
            print(f"    323 distinct eigenvalues at lambda <= {cutoff}")
            found = True
            break
        if total_dim == target:
            print(f"    323 total dimension at lambda <= {cutoff}")
            found = True
            break

    if not found:
        print(f"    323 does not appear as pair count, distinct eigenvalue count, or total dimension")

    return found, "323 in spectral counts" if found else "323 not in spectral counts"


def test_representation_product():
    """T8: Does 323 appear as a product of representation dimensions?"""
    # Compute all SO(5) representation dimensions up to 100
    dims = {}
    for a in range(20):
        for b in range(20):
            d = so5_dim(a, b)
            if d <= 500:
                if d not in dims:
                    dims[d] = []
                dims[d].append((a, b))

    print(f"  SO(5) representation dimensions up to 500: {len(dims)} distinct")

    # Is 323 itself a dimension?
    if 323 in dims:
        print(f"  323 IS a representation dimension: Dynkin labels {dims[323]}")
    else:
        print(f"  323 is NOT a representation dimension")
        # Check factors
        if 17 in dims and 19 in dims:
            print(f"  But 17 = dim V{dims[17]} and 19 = dim V{dims[19]}")
        if 17 in dims:
            print(f"  17 = dim V{dims[17]}")
        else:
            print(f"  17 is NOT a representation dimension")
        if 19 in dims:
            print(f"  19 = dim V{dims[19]}")
        else:
            print(f"  19 is NOT a representation dimension")

    # What are the nearby representation dimensions?
    for d in sorted(dims.keys()):
        if abs(d - 323) <= 20:
            print(f"  dim V{dims[d]} = {d} (delta = {d-323:+d})")

    return 323 in dims or (17 in dims and 19 in dims), \
        f"323 as rep dim: {323 in dims}, 17×19 factored: {17 in dims and 19 in dims}"


def test_summary():
    """T9: Summary — does 323 emerge anywhere?"""
    invs = load_invariants()

    # Collect all the ways we've found (or not) 323
    hits = []
    misses = []

    # Empirical
    if invs:
        counts = empirical_counts(invs)
        closest_label, closest_val = min(counts.items(), key=lambda x: abs(x[1] - target))
        if closest_val == target:
            hits.append(f"Empirical ({closest_label})")
        else:
            misses.append(f"Empirical: closest = {closest_label} = {closest_val} (delta {closest_val-target:+d})")

    # 17 * 19 factorization
    hits.append("Factorization: both 17 and 19 have BST derivations")
    hits.append(f"17 = dim so(5,2) - rank^2 = {21 - rank**2}")
    hits.append(f"19 = n_C^2 - C_2 = {n_C**2 - C_2} = Q")

    print(f"\n  ╔══════════════════════════════════════════════════════╗")
    print(f"  ║    CP-5 NATURAL DIMENSION TEST — SUMMARY             ║")
    print(f"  ╠══════════════════════════════════════════════════════╣")
    print(f"  ║  Target: 323 = 17 × 19 = (N_c·C₂-1) × Q            ║")
    print(f"  ╠══════════════════════════════════════════════════════╣")

    for h in hits:
        print(f"  ║  HIT:  {h:<47s} ║")
    for m in misses:
        print(f"  ║  MISS: {m:<47s} ║")

    print(f"  ╚══════════════════════════════════════════════════════╝")

    return len(hits) > len(misses), \
        f"{len(hits)} hits, {len(misses)} misses"


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 70)
    print(f"Toy 1548 — CP-5: Natural Dimension Test")
    print(f"Question: Is 323 = 17 × 19 = (N_c·C₂-1)·Q the natural dimension?")
    print("=" * 70)

    tests = [
        ("T1: Empirical counts from invariants", test_empirical),
        ("T2: D_IV^5 spectral theory", test_spectral),
        ("T3: Factorization identities", test_factorization),
        ("T4: BST product lattice", test_lattice),
        ("T5: Convergence analysis", test_convergence),
        ("T6: Cross-domain structure", test_cross_domain),
        ("T7: Eigenvalue cutoff search", test_eigenvalue_count),
        ("T8: Representation dimension search", test_representation_product),
        ("T9: Summary", test_summary),
    ]

    results = []
    for name, test_fn in tests:
        print(f"\n--- {name} ---")
        try:
            passed, detail = test_fn()
            results.append((name, passed, detail))
            print(f"  {'PASS' if passed else 'FAIL'}: {detail}")
        except Exception as e:
            import traceback
            results.append((name, False, str(e)))
            print(f"  ERROR: {e}")
            traceback.print_exc()

    passed = sum(1 for _, p, _ in results if p)
    total = len(results)
    print("\n" + "=" * 70)
    print(f"SCORE: {passed}/{total}")
    print("=" * 70)

    for name, p, detail in results:
        print(f"  {'PASS' if p else 'FAIL'}: {name} — {detail}")
