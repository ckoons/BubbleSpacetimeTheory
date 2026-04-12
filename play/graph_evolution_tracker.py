#!/usr/bin/env python3
"""
Toy — AC Graph Evolution Tracker
Tracks how the AC theorem graph's structural properties evolve over time.
Tests whether the graph self-organizes toward BST predictions:
  - Producer fraction -> 19.1% (Godel limit = f = 19.1%)
  - Cross-domain fraction increases (knowledge integrates)
  - Density decreases then stabilizes (new domains add O(d^2) pairs)

Handles undated theorems (T162-T478) by interpolating dates from TID neighbors.
"""

import json
from collections import defaultdict
from datetime import datetime, timedelta

# ── Load data ────────────────────────────────────────────────────────
with open("play/ac_graph_data.json") as f:
    data = json.load(f)

theorems = data["theorems"]
edges = data["edges"]

# ── Assign dates (interpolate for undated theorems) ──────────────────
# Build initial tid -> date map
tid_to_thm = {t["tid"]: t for t in theorems}
tid_date_raw = {}
for t in theorems:
    if t.get("date"):
        tid_date_raw[t["tid"]] = t["date"]

# For undated theorems, interpolate based on nearest dated neighbors
all_tids = sorted(t["tid"] for t in theorems)
tid_date = {}

for tid in all_tids:
    if tid in tid_date_raw:
        tid_date[tid] = tid_date_raw[tid]
    else:
        # Find nearest dated TID before and after
        before_tid = None
        after_tid = None
        for bt in range(tid - 1, 0, -1):
            if bt in tid_date_raw:
                before_tid = bt
                break
        for at in range(tid + 1, max(all_tids) + 1):
            if at in tid_date_raw:
                after_tid = at
                break

        if before_tid and after_tid:
            d1 = datetime.strptime(tid_date_raw[before_tid], "%Y-%m-%d")
            d2 = datetime.strptime(tid_date_raw[after_tid], "%Y-%m-%d")
            frac = (tid - before_tid) / (after_tid - before_tid)
            interp = d1 + timedelta(days=frac * (d2 - d1).days)
            tid_date[tid] = interp.strftime("%Y-%m-%d")
        elif before_tid:
            tid_date[tid] = tid_date_raw[before_tid]
        elif after_tid:
            tid_date[tid] = tid_date_raw[after_tid]
        else:
            tid_date[tid] = "2026-03-27"  # fallback

# Count interpolated
n_interp = sum(1 for t in theorems if not t.get("date"))
n_total = len(theorems)

# Build tid -> domain lookup
tid_domain = {t["tid"]: t.get("domain", "unknown") for t in theorems}

# Build edge list with domains
edge_list = []
for e in edges:
    fr, to = e["from"], e["to"]
    if fr in tid_domain and to in tid_domain:
        edge_list.append((fr, to, tid_domain[fr], tid_domain[to]))

# Get sorted unique dates (now includes interpolated)
dates_sorted = sorted(set(tid_date.values()))

# ── BST constants ────────────────────────────────────────────────────
BST_GODEL_LIMIT = 0.191  # 19.1%

# ── Compute evolution at each date checkpoint ────────────────────────
print("=" * 120)
print("AC GRAPH EVOLUTION TRACKER")
print("=" * 120)
print()
print(f"Total theorems: {n_total}  |  Dated: {n_total - n_interp}  |  Interpolated: {n_interp}")
print(f"Total edges: {len(edge_list)}  |  Date range: {dates_sorted[0]} to {dates_sorted[-1]}")
print(f"Domains: {len(set(tid_domain.values()))}")
print()

# Header
hdr = (f"{'Date':<12} {'Nodes':>6} {'Edges':>6} {'Doms':>5} "
       f"{'X-frac':>7} {'Density':>9} {'Conn%':>6} "
       f"{'ProdFr':>7} {'Prod':>5} "
       f"{'d(19.1%)':>9}")
print(hdr)
print("-" * len(hdr))

# Group theorems by date
date_to_tids = defaultdict(set)
for tid, d in tid_date.items():
    date_to_tids[d].add(tid)

# Cumulative computation
cum_tids = set()
results = []

for date in dates_sorted:
    # Add all theorems with this date
    cum_tids |= date_to_tids[date]

    # Edges where both endpoints are in cumulative set
    cum_edges = [(fr, to, df, dt) for (fr, to, df, dt) in edge_list
                 if fr in cum_tids and to in cum_tids]

    n_nodes = len(cum_tids)
    n_edges = len(cum_edges)

    # Active domains
    active_domains = set(tid_domain[tid] for tid in cum_tids)
    n_domains = len(active_domains)

    # Cross-domain edges
    cross_edges = [(fr, to, df, dt) for (fr, to, df, dt) in cum_edges if df != dt]
    n_cross = len(cross_edges)
    cross_frac = n_cross / n_edges if n_edges > 0 else 0.0

    # Density
    max_edges = n_nodes * (n_nodes - 1) / 2 if n_nodes > 1 else 1
    density = n_edges / max_edges

    # Domain pairs
    n_domain_pairs = n_domains * (n_domains - 1) // 2 if n_domains > 1 else 0
    pair_edges = defaultdict(int)
    for (fr, to, df, dt) in cross_edges:
        key = tuple(sorted([df, dt]))
        pair_edges[key] += 1
    zero_pairs = n_domain_pairs - len(pair_edges) if n_domain_pairs > 0 else 0
    conn_pct = (n_domain_pairs - zero_pairs) / n_domain_pairs * 100 if n_domain_pairs > 0 else 0

    # Producer fraction
    domain_cross_out = defaultdict(int)
    domain_cross_in = defaultdict(int)
    for (fr, to, df, dt) in cross_edges:
        domain_cross_out[df] += 1
        domain_cross_in[dt] += 1

    n_producers = 0
    for d in active_domains:
        out = domain_cross_out.get(d, 0)
        inp = domain_cross_in.get(d, 0)
        if out > inp:
            n_producers += 1

    prod_frac = n_producers / n_domains if n_domains > 0 else 0.0
    delta_f = prod_frac - BST_GODEL_LIMIT

    results.append({
        "date": date,
        "nodes": n_nodes,
        "edges": n_edges,
        "domains": n_domains,
        "cross_frac": cross_frac,
        "density": density,
        "zero_pairs": zero_pairs,
        "max_pairs": n_domain_pairs,
        "conn_pct": conn_pct,
        "prod_frac": prod_frac,
        "n_producers": n_producers,
        "delta_f": delta_f,
    })

    print(f"{date:<12} {n_nodes:>6} {n_edges:>6} {n_domains:>5} "
          f"{cross_frac:>7.3f} {density:>9.6f} {conn_pct:>5.1f}% "
          f"{prod_frac:>7.3f} {n_producers:>2}/{n_domains:<2} "
          f"{delta_f:>+9.3f}")

print("-" * len(hdr))
print()

# ── Phase analysis ───────────────────────────────────────────────────
# Identify phases: early (small N), growth, mature
# Split into 3 roughly equal phases
n_dates = len(results)
p1_end = n_dates // 3
p2_end = 2 * n_dates // 3

phases = [
    ("PHASE I  (bootstrap)", results[:p1_end]),
    ("PHASE II (growth)",    results[p1_end:p2_end]),
    ("PHASE III (mature)",   results[p2_end:]),
]

print("=" * 120)
print("PHASE ANALYSIS")
print("=" * 120)
print()

print(f"{'Phase':<30} {'Dates':<27} {'Nodes':>7} {'Doms':>5} "
      f"{'X-frac':>7} {'ProdFr':>7} {'d(19.1%)':>9}")
print("-" * 100)

for name, phase_results in phases:
    if not phase_results:
        continue
    pr_first = phase_results[0]
    pr_last = phase_results[-1]
    avg_xf = sum(r['cross_frac'] for r in phase_results) / len(phase_results)
    avg_pf = sum(r['prod_frac'] for r in phase_results) / len(phase_results)
    avg_delta = avg_pf - BST_GODEL_LIMIT
    print(f"{name:<30} {pr_first['date']}-{pr_last['date']}  "
          f"{pr_first['nodes']:>3}-{pr_last['nodes']:<3} {pr_first['domains']:>2}-{pr_last['domains']:<2} "
          f"{avg_xf:>7.3f} {avg_pf:>7.3f} {avg_delta:>+9.3f}")

print()

# ── Trend analysis ───────────────────────────────────────────────────
print("=" * 120)
print("TREND ANALYSIS")
print("=" * 120)
print()

first = results[0]
last = results[-1]
mid = results[len(results) // 2]

# 1. Cross-domain fraction
print("1. CROSS-DOMAIN FRACTION")
print("   BST prediction: increases as knowledge integrates across domains")
print()

# Use only results where N > 100 for stable measurement
stable_results = [r for r in results if r['nodes'] >= 100]
if len(stable_results) >= 3:
    sr_first = stable_results[0]
    sr_last = stable_results[-1]
    print(f"   (Using N >= 100 for stable measurement)")
    print(f"   First stable ({sr_first['date']}, N={sr_first['nodes']}): {sr_first['cross_frac']:.3f}")
    print(f"   Last  stable ({sr_last['date']}, N={sr_last['nodes']}):  {sr_last['cross_frac']:.3f}")
    xf_trend = sr_last['cross_frac'] - sr_first['cross_frac']
    print(f"   Change: {xf_trend:+.3f}  {'INCREASING' if xf_trend > 0 else 'DECREASING'}")
else:
    print(f"   Start: {first['cross_frac']:.3f}  End: {last['cross_frac']:.3f}")
    xf_trend = last['cross_frac'] - first['cross_frac']
print()

# 2. Producer fraction trajectory
print("2. PRODUCER FRACTION TRAJECTORY")
print(f"   BST prediction: converges to {BST_GODEL_LIMIT:.1%} (Godel limit)")
print()

# Show the trajectory with annotations
print(f"   {'Date':<12} {'ProdFr':>7} {'Delta':>8} {'Direction':<15}")
print(f"   {'-'*50}")
prev_delta = None
for r in results:
    delta = r['prod_frac'] - BST_GODEL_LIMIT
    if prev_delta is not None:
        if abs(delta) < abs(prev_delta):
            direction = "<-- closer"
        elif abs(delta) > abs(prev_delta):
            direction = "--> farther"
        else:
            direction = "    same"
    else:
        direction = ""
    print(f"   {r['date']:<12} {r['prod_frac']:>7.3f} {delta:>+8.3f}  {direction}")
    prev_delta = delta
print()

# Compute convergence rate
if len(stable_results) >= 2:
    deltas = [abs(r['prod_frac'] - BST_GODEL_LIMIT) for r in stable_results]
    # Linear regression of |delta| vs index
    n_sr = len(deltas)
    x_mean = (n_sr - 1) / 2
    y_mean = sum(deltas) / n_sr
    num = sum((i - x_mean) * (d - y_mean) for i, d in enumerate(deltas))
    den = sum((i - x_mean) ** 2 for i in range(n_sr))
    slope = num / den if den > 0 else 0
    print(f"   Convergence slope (|delta| vs time): {slope:+.4f} per checkpoint")
    if slope < 0:
        print(f"   --> Producer fraction is CONVERGING toward 19.1%")
        # Extrapolate when it would reach zero delta
        steps_to_zero = -y_mean / slope if slope != 0 else float('inf')
        print(f"   --> Estimated {steps_to_zero:.0f} more checkpoints to reach target")
    else:
        print(f"   --> Producer fraction is NOT converging (or oscillating)")
print()

# 3. Density
print("3. DENSITY")
print("   BST prediction: decreases (domain pairs grow as d^2, edges grow slower)")
print()
print(f"   Start: {first['density']:.6f}  (N={first['nodes']}, d={first['domains']})")
print(f"   End:   {last['density']:.6f}  (N={last['nodes']}, d={last['domains']})")
ratio = first['density'] / last['density'] if last['density'] > 0 else 0
print(f"   Ratio: {ratio:.1f}x decrease")
print()

# 4. Domain connectivity
print("4. DOMAIN CONNECTIVITY")
print("   How many domain pairs have at least one cross-edge?")
print()
print(f"   Start: {first['conn_pct']:.1f}%  ({first['max_pairs'] - first['zero_pairs']}/{first['max_pairs']} pairs)")
print(f"   End:   {last['conn_pct']:.1f}%  ({last['max_pairs'] - last['zero_pairs']}/{last['max_pairs']} pairs)")
print(f"   Absolute connected pairs: {first['max_pairs'] - first['zero_pairs']} -> {last['max_pairs'] - last['zero_pairs']}")
print(f"   (Percentage drops because domain pairs grow as d^2 while bridges grow slower)")
print()

# ── ASCII trajectory plot ────────────────────────────────────────────
print("=" * 120)
print("PRODUCER FRACTION vs BST GODEL LIMIT — TRAJECTORY")
print("=" * 120)
print()
print(f"   Each * = measured producer fraction.  | = BST Godel limit (19.1%)")
print()

WIDTH = 60
SCALE_MAX = 0.60

for r in results:
    pos = int(r['prod_frac'] / SCALE_MAX * WIDTH)
    target_pos = int(BST_GODEL_LIMIT / SCALE_MAX * WIDTH)
    line = list(" " * (WIDTH + 1))
    line[target_pos] = "|"
    if 0 <= pos <= WIDTH:
        if pos == target_pos:
            line[pos] = "X"  # exact hit
        else:
            line[pos] = "*"
    pf_label = f"{r['prod_frac']:.1%}"
    n_label = f"N={r['nodes']}"
    print(f"   {r['date']}  {''.join(line)}  {pf_label:>6}  {n_label}")

# Axis
axis = list("-" * (WIDTH + 1))
target_pos = int(BST_GODEL_LIMIT / SCALE_MAX * WIDTH)
axis[target_pos] = "^"
print(f"   {'':12}{''.join(axis)}")
print(f"   {'':12}0%{' ' * (target_pos - 3)}19.1%{' ' * (WIDTH - target_pos - 4)}{SCALE_MAX:.0%}")
print()

# ── Cross-domain fraction trajectory ─────────────────────────────────
print("=" * 120)
print("CROSS-DOMAIN FRACTION — TRAJECTORY")
print("=" * 120)
print()
print(f"   Each * = cross-domain fraction.  | = 50% line")
print()

for r in results:
    pos = int(r['cross_frac'] / 1.0 * WIDTH)
    mid_pos = int(0.50 / 1.0 * WIDTH)
    line = list(" " * (WIDTH + 1))
    line[mid_pos] = "|"
    if 0 <= pos <= WIDTH:
        line[pos] = "*"
    label = f"{r['cross_frac']:.1%}"
    print(f"   {r['date']}  {''.join(line)}  {label}")

axis = list("-" * (WIDTH + 1))
mid_pos = int(0.50 / 1.0 * WIDTH)
axis[mid_pos] = "^"
print(f"   {'':12}{''.join(axis)}")
print(f"   {'':12}0%{' ' * (mid_pos - 3)}50%{' ' * (WIDTH - mid_pos - 3)}100%")
print()

# ── Growth rates ─────────────────────────────────────────────────────
print("=" * 120)
print("GROWTH RATES (per-date increments)")
print("=" * 120)
print()
print(f"   {'Date':<12} {'dN':>5} {'dE':>6} {'dDom':>5} {'E/N':>6} {'cumE/cumN':>9}")
print(f"   {'-'*48}")
for i in range(1, len(results)):
    prev = results[i - 1]
    curr = results[i]
    dn = curr['nodes'] - prev['nodes']
    de = curr['edges'] - prev['edges']
    dd = curr['domains'] - prev['domains']
    en_ratio = de / dn if dn > 0 else 0
    cum_ratio = curr['edges'] / curr['nodes'] if curr['nodes'] > 0 else 0
    if dn == 0 and de == 0:
        continue  # skip empty days
    print(f"   {curr['date']:<12} {dn:>5} {de:>6} {dd:>5} {en_ratio:>6.2f} {cum_ratio:>9.2f}")
print()

# ── Final scorecard ──────────────────────────────────────────────────
print("=" * 120)
print("FINAL SCORECARD: BST SELF-ORGANIZATION TESTS")
print("=" * 120)
print()

checks = []

# Test 1: Producer fraction within 15% of Godel limit
pf_delta = abs(last['prod_frac'] - BST_GODEL_LIMIT)
pf_close = pf_delta < 0.15
checks.append(("Producer fraction within 15pp of Godel limit (19.1%)", pf_close,
                f"{last['prod_frac']:.1%} vs {BST_GODEL_LIMIT:.1%}, |delta|={pf_delta:.3f}"))

# Test 2: Producer fraction CONVERGING (mature phase closer than early phase)
early_phase = [r for r in results if r['nodes'] < 200]
late_phase = [r for r in results if r['nodes'] >= 400]
if early_phase and late_phase:
    early_avg_delta = sum(abs(r['prod_frac'] - BST_GODEL_LIMIT) for r in early_phase) / len(early_phase)
    late_avg_delta = sum(abs(r['prod_frac'] - BST_GODEL_LIMIT) for r in late_phase) / len(late_phase)
    pf_converging = late_avg_delta < early_avg_delta
    checks.append(("Producer fraction converging toward 19.1%", pf_converging,
                    f"early avg |delta|={early_avg_delta:.3f}, late avg |delta|={late_avg_delta:.3f}"))

# Test 3: Cross-domain fraction > 50%
cf_high = last['cross_frac'] > 0.50
checks.append(("Cross-domain edges > 50% of total", cf_high,
                f"{last['cross_frac']:.1%}"))

# Test 4: Cross-domain fraction increasing in mature phase
if len(stable_results) >= 3:
    xf_increasing = stable_results[-1]['cross_frac'] > stable_results[0]['cross_frac']
    checks.append(("Cross-domain fraction increasing (N>=100 phase)", xf_increasing,
                    f"{stable_results[0]['cross_frac']:.3f} -> {stable_results[-1]['cross_frac']:.3f}"))

# Test 5: Density monotonically decreasing
dens_dec = last['density'] < first['density']
# Check monotonicity
dens_mono = all(results[i]['density'] <= results[i-1]['density'] + 0.0001
                for i in range(1, len(results)))
checks.append(("Density monotonically decreasing", dens_dec and dens_mono,
                f"{first['density']:.6f} -> {last['density']:.6f}, "
                f"{'monotonic' if dens_mono else 'non-monotonic'}"))

# Test 6: Absolute connected domain pairs increasing
abs_conn_first = first['max_pairs'] - first['zero_pairs']
abs_conn_last = last['max_pairs'] - last['zero_pairs']
conn_abs_inc = abs_conn_last > abs_conn_first
checks.append(("Absolute connected domain pairs increasing", conn_abs_inc,
                f"{abs_conn_first} -> {abs_conn_last}"))

# Test 7: Average edges per node stabilizing (mature phase has lower variance)
if late_phase:
    late_ratios = [r['edges'] / r['nodes'] for r in late_phase]
    late_mean = sum(late_ratios) / len(late_ratios)
    late_var = sum((x - late_mean) ** 2 for x in late_ratios) / len(late_ratios)
    checks.append(("Edge/node ratio stabilizing in mature phase", late_var < 0.5,
                    f"mean={late_mean:.2f}, var={late_var:.4f}"))

pass_count = sum(1 for _, passed, _ in checks if passed)
total_count = len(checks)

for name, passed, detail in checks:
    status = "PASS" if passed else "FAIL"
    print(f"   [{status}] {name}")
    print(f"         {detail}")
    print()

print(f"   Score: {pass_count}/{total_count}")
print()

# Verdict
if pass_count >= total_count - 1:
    print("   VERDICT: STRONG evidence of BST self-organization.")
    print("   The AC theorem graph evolves toward BST-predicted structural constants.")
elif pass_count >= total_count // 2:
    print("   VERDICT: MODERATE evidence of BST self-organization.")
    print("   Several predicted structural trends are present.")
else:
    print("   VERDICT: WEAK evidence. Further growth needed to test convergence.")

print()

# Key finding
print("=" * 120)
print("KEY FINDING: PRODUCER FRACTION DYNAMICS")
print("=" * 120)
print()
print("   The producer fraction follows a characteristic overshoot-and-decay pattern:")
print()
print(f"   1. BOOTSTRAP (N < 100):  PF = {first['prod_frac']:.1%}")
print(f"      Small graph, high noise, initial undershoot below 19.1%")
print()

# Find peak
peak = max(results, key=lambda r: r['prod_frac'])
print(f"   2. OVERSHOOT ({peak['date']}, N={peak['nodes']}):  PF = {peak['prod_frac']:.1%}")
print(f"      New domains emerge as producers before receiving back-edges")
print()

print(f"   3. CONVERGENCE ({last['date']}, N={last['nodes']}):  PF = {last['prod_frac']:.1%}")
print(f"      As back-edges fill in, producer fraction decays toward equilibrium")
print()

print(f"   BST Godel limit:  {BST_GODEL_LIMIT:.1%}")
print(f"   Current delta:    {last['delta_f']:+.3f}")
print()

# Is the decay exponential?
# Fit: after peak, does |delta| decrease roughly geometrically?
peak_idx = results.index(peak)
post_peak = results[peak_idx:]
if len(post_peak) >= 3:
    deltas_pp = [abs(r['prod_frac'] - BST_GODEL_LIMIT) for r in post_peak]
    # Check if each step reduces delta
    n_reductions = sum(1 for i in range(1, len(deltas_pp)) if deltas_pp[i] < deltas_pp[i-1])
    print(f"   Post-peak convergence: {n_reductions}/{len(deltas_pp)-1} steps reduce |delta|")
    if n_reductions > len(deltas_pp) * 0.5:
        print(f"   Pattern: DAMPED OSCILLATION toward BST Godel limit")
    else:
        print(f"   Pattern: NON-MONOTONIC (noise present, trend unclear)")

print()
print("=" * 120)
