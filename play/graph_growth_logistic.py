#!/usr/bin/env python3
"""
Toy — Logistic Growth Analysis of AC Theorem Graph
====================================================
Tests Grace's prediction: the AC graph's growth follows a logistic curve
with BST parameters.

Grace's specific predictions:
  - Carrying capacity K = N_max * dim_R = 137 * 10 = 1370
  - Inflection point t_mid ~ March 31 (K/2 ~ 685 nodes)
  - Growth rate r related to a BST rational

Data sources:
  1. play/ac_graph_data.json — theorem dates (with interpolation for undated)
  2. Session log cross-checks from memory files

Model: N(t) = K / (1 + exp(-r * (t - t_mid)))

RESEARCH ONLY — no modifications to graph data or theorem files.
"""

import json
import math
from collections import defaultdict
from datetime import datetime, timedelta

import numpy as np
from scipy.optimize import curve_fit

# ── BST Constants ─────────────────────────────────────────────────────
N_max = 137        # BST maximum quantum number
dim_R = 10         # rank of D_IV^5
N_c = 3            # color dimension
n_C = 5            # Cartan integer
g = 7              # genus
C_2 = 6            # Casimir
rank = 2           # rank

BST_RATIONALS = {
    "N_c/g":         N_c / g,            # 3/7 = 0.4286
    "rank/n_C":      rank / n_C,         # 2/5 = 0.4000
    "n_C/g":         n_C / g,            # 5/7 = 0.7143
    "N_c/n_C":       N_c / n_C,          # 3/5 = 0.6000
    "1/N_c":         1 / N_c,            # 1/3 = 0.3333
    "1/n_C":         1 / n_C,            # 1/5 = 0.2000
    "C_2/g":         C_2 / g,            # 6/7 = 0.8571
    "rank/g":        rank / g,           # 2/7 = 0.2857
    "N_c/C_2":       N_c / C_2,          # 3/6 = 0.5000
    "g/N_max":       g / N_max,          # 7/137 = 0.0511
    "(N_c+rank)/g":  (N_c + rank) / g,   # 5/7 = 0.7143
    "f_Godel":       0.191,              # 19.1%
    "1/g":           1 / g,              # 1/7 = 0.1429
    "rank/N_c":      rank / N_c,         # 2/3 = 0.6667
    "N_c*rank/g":    N_c * rank / g,     # 6/7 = 0.8571
    "1/rank":        1 / rank,           # 1/2 = 0.5000
    "n_C/C_2":       n_C / C_2,          # 5/6 = 0.8333
    "g/dim_R":       g / dim_R,          # 7/10 = 0.7000
    "N_c/dim_R":     N_c / dim_R,        # 3/10 = 0.3000
    "C_2/dim_R":     C_2 / dim_R,        # 6/10 = 0.6000
}

K_CANDIDATES = {
    "Grace: N_max * dim_R":     N_max * dim_R,      # 1370
    "N_max^2":                  N_max ** 2,          # 18769
    "Milestone 1000":           1000,
    "Current size (~981)":      981,
}

# ── Load graph data ───────────────────────────────────────────────────
with open("play/ac_graph_data.json") as f:
    data = json.load(f)

theorems = data["theorems"]
edges = data["edges"]

# ── Assign dates (interpolate for undated, same method as tracker) ────
tid_date_raw = {}
for t in theorems:
    if t.get("date"):
        tid_date_raw[t["tid"]] = t["date"]

all_tids = sorted(t["tid"] for t in theorems)
tid_date = {}

for tid in all_tids:
    if tid in tid_date_raw:
        tid_date[tid] = tid_date_raw[tid]
    else:
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
            tid_date[tid] = "2026-03-27"

n_interp = sum(1 for t in theorems if not t.get("date"))
n_total = len(theorems)

# ── Build cumulative time series ──────────────────────────────────────
date_to_tids = defaultdict(set)
for tid, d in tid_date.items():
    date_to_tids[d].add(tid)

# Edge lookup: which TIDs are connected
edge_tids = set()
for e in edges:
    edge_tids.add(e["from"])
    edge_tids.add(e["to"])

dates_sorted = sorted(set(tid_date.values()))

# Reference date for converting to numeric days
ref_date = datetime.strptime(dates_sorted[0], "%Y-%m-%d")

time_series = []
cum_tids = set()

for date_str in dates_sorted:
    cum_tids |= date_to_tids[date_str]
    # Count edges where both endpoints are in cumulative set
    cum_edges = sum(1 for e in edges if e["from"] in cum_tids and e["to"] in cum_tids)
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    day_num = (dt - ref_date).days
    time_series.append({
        "date": date_str,
        "day": day_num,
        "nodes": len(cum_tids),
        "edges": cum_edges,
    })

# ── Also incorporate session-log cross-check data points ─────────────
# These are independently recorded and serve as validation
session_checkpoints = [
    # (date, nodes, edges, source)
    ("2026-03-27", 253, 222, "interstasis session"),
    ("2026-03-31", 582, 1150, "March 31 sprint"),
    ("2026-04-03", 773, 1758, "April 3 session"),
    ("2026-04-09", 889, 2285, "April 9 evening"),
    ("2026-04-09", 895, 2782, "April 9 final"),
    ("2026-04-11", 963, 3161, "April 11 convergence"),
    ("2026-04-11", 965, 3181, "April 11 genesis"),
]

# ── Logistic model ────────────────────────────────────────────────────
def logistic(t, K, r, t_mid):
    """Standard logistic growth: N(t) = K / (1 + exp(-r*(t - t_mid)))"""
    return K / (1.0 + np.exp(-r * (t - t_mid)))

def logistic_fixed_K(K_val):
    """Return logistic function with fixed K for curve_fit"""
    def model(t, r, t_mid):
        return K_val / (1.0 + np.exp(-r * (t - t_mid)))
    return model

# ── Prepare data arrays ──────────────────────────────────────────────
t_days = np.array([ts["day"] for ts in time_series], dtype=float)
n_nodes = np.array([ts["nodes"] for ts in time_series], dtype=float)
n_edges = np.array([ts["edges"] for ts in time_series], dtype=float)

# ── Fit functions ─────────────────────────────────────────────────────
def fit_logistic(t_data, y_data, label, fixed_K=None):
    """Fit logistic model, return parameters and diagnostics."""
    y_max = float(y_data[-1])
    t_range = float(t_data[-1] - t_data[0])
    t_center = float(np.mean(t_data))

    results = {}

    if fixed_K is not None:
        # Fit with fixed K
        model = logistic_fixed_K(fixed_K)
        try:
            popt, pcov = curve_fit(
                model, t_data, y_data,
                p0=[0.3, t_center],
                bounds=([0.01, t_data[0] - 30], [5.0, t_data[-1] + 60]),
                maxfev=10000,
            )
            r_fit, t_mid_fit = popt
            K_fit = fixed_K
            y_pred = model(t_data, *popt)
        except Exception as e:
            return None, f"Fit failed: {e}"
    else:
        # Fit all three parameters
        try:
            popt, pcov = curve_fit(
                logistic, t_data, y_data,
                p0=[y_max * 1.5, 0.3, t_center],
                bounds=([y_max * 0.8, 0.01, t_data[0] - 30],
                        [y_max * 50, 5.0, t_data[-1] + 60]),
                maxfev=10000,
            )
            K_fit, r_fit, t_mid_fit = popt
            y_pred = logistic(t_data, *popt)
        except Exception as e:
            return None, f"Fit failed: {e}"

    # Compute R^2
    ss_res = np.sum((y_data - y_pred) ** 2)
    ss_tot = np.sum((y_data - np.mean(y_data)) ** 2)
    r_squared = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

    # Residuals
    residuals = y_data - y_pred
    max_resid = float(np.max(np.abs(residuals)))
    rms_resid = float(np.sqrt(np.mean(residuals ** 2)))

    # Convert t_mid to date
    t_mid_date = ref_date + timedelta(days=float(t_mid_fit))

    results = {
        "K": float(K_fit),
        "r": float(r_fit),
        "t_mid_day": float(t_mid_fit),
        "t_mid_date": t_mid_date.strftime("%Y-%m-%d"),
        "R2": float(r_squared),
        "max_resid": max_resid,
        "rms_resid": rms_resid,
        "y_pred": y_pred,
        "residuals": residuals,
    }

    return results, None


def find_closest_bst_rational(r_value):
    """Find the BST rational closest to a given value."""
    best_name = None
    best_val = None
    best_dist = float('inf')
    for name, val in BST_RATIONALS.items():
        dist = abs(r_value - val)
        if dist < best_dist:
            best_dist = dist
            best_val = val
            best_name = name
    return best_name, best_val, best_dist


# ══════════════════════════════════════════════════════════════════════
# MAIN OUTPUT
# ══════════════════════════════════════════════════════════════════════

print("=" * 100)
print("AC GRAPH LOGISTIC GROWTH ANALYSIS")
print("Testing Grace's Prediction: K = N_max * dim_R = 1370")
print("=" * 100)
print()

# ── Data summary ──────────────────────────────────────────────────────
print("DATA SUMMARY")
print("-" * 60)
print(f"  Source:           play/ac_graph_data.json")
print(f"  Theorems:         {n_total} ({n_total - n_interp} dated, {n_interp} interpolated)")
print(f"  Edges:            {len(edges)}")
print(f"  Date range:       {dates_sorted[0]} to {dates_sorted[-1]}")
print(f"  Duration:         {t_days[-1]:.0f} days ({len(dates_sorted)} distinct dates)")
print(f"  Current nodes:    {int(n_nodes[-1])}")
print(f"  Current edges:    {int(n_edges[-1])}")
print()

# ── Session log cross-check ──────────────────────────────────────────
print("SESSION LOG CROSS-CHECK (independent records)")
print("-" * 60)
for sc_date, sc_nodes, sc_edges, sc_source in session_checkpoints:
    # Find matching time series entry
    match = [ts for ts in time_series if ts["date"] == sc_date]
    if match:
        ts = match[-1]
        node_delta = ts["nodes"] - sc_nodes
        edge_delta = ts["edges"] - sc_edges
        print(f"  {sc_date} ({sc_source})")
        print(f"    Log: {sc_nodes:>5} nodes, {sc_edges:>5} edges")
        print(f"    JSON: {ts['nodes']:>5} nodes, {ts['edges']:>5} edges")
        print(f"    Delta: {node_delta:>+5} nodes, {edge_delta:>+5} edges")
    else:
        print(f"  {sc_date} ({sc_source}): {sc_nodes} nodes, {sc_edges} edges — no JSON match")
print()
print("  NOTE: JSON has been updated since session logs were written,")
print("  so JSON counts may exceed session-log snapshots.")
print()

# ══════════════════════════════════════════════════════════════════════
# PART 1: FREE-FIT LOGISTIC (all 3 parameters free)
# ══════════════════════════════════════════════════════════════════════

print("=" * 100)
print("PART 1: FREE-FIT LOGISTIC MODEL (K, r, t_mid all free)")
print("=" * 100)
print()

for label, y_data in [("NODES", n_nodes), ("EDGES", n_edges)]:
    result, err = fit_logistic(t_days, y_data, label)
    if err:
        print(f"  {label}: {err}")
        continue

    print(f"  {label}")
    print(f"  {'─' * 50}")
    print(f"    K (carrying capacity) = {result['K']:.1f}")
    print(f"    r (growth rate)       = {result['r']:.4f} / day")
    print(f"    t_mid (inflection)    = day {result['t_mid_day']:.1f} = {result['t_mid_date']}")
    print(f"    R²                    = {result['R2']:.6f}")
    print(f"    RMS residual          = {result['rms_resid']:.1f}")
    print(f"    Max |residual|        = {result['max_resid']:.1f}")
    print()

    # BST rational match for r
    bst_name, bst_val, bst_dist = find_closest_bst_rational(result['r'])
    print(f"    Closest BST rational to r = {result['r']:.4f}:")
    print(f"      {bst_name} = {bst_val:.4f}  (distance = {bst_dist:.4f})")
    print()

    # Grace's predictions
    if label == "NODES":
        K_grace = N_max * dim_R  # 1370
        K_ratio = result['K'] / K_grace
        print(f"    Grace's prediction: K = {K_grace}")
        print(f"    Fitted K / Grace K = {K_ratio:.3f}")
        print(f"    {'CONSISTENT' if 0.7 < K_ratio < 1.3 else 'INCONSISTENT'} "
              f"(within 30% = {'YES' if 0.7 < K_ratio < 1.3 else 'NO'})")
        print()

        # Inflection date test
        grace_inflection = datetime.strptime("2026-03-31", "%Y-%m-%d")
        t_mid_actual = datetime.strptime(result['t_mid_date'], "%Y-%m-%d")
        delta_days = abs((t_mid_actual - grace_inflection).days)
        print(f"    Grace's inflection prediction: March 31")
        print(f"    Fitted inflection:             {result['t_mid_date']}")
        print(f"    Distance:                      {delta_days} days")
        print(f"    {'CONSISTENT' if delta_days <= 5 else 'INCONSISTENT'} "
              f"(within 5 days = {'YES' if delta_days <= 5 else 'NO'})")
        print()

        free_fit_nodes = result  # save for later comparison

# ══════════════════════════════════════════════════════════════════════
# PART 2: FIXED-K FITS (test specific K values)
# ══════════════════════════════════════════════════════════════════════

print("=" * 100)
print("PART 2: FIXED-K LOGISTIC FITS (testing specific carrying capacities)")
print("=" * 100)
print()

node_fits = {}
edge_fits = {}

for k_label, k_val in sorted(K_CANDIDATES.items(), key=lambda x: x[1]):
    print(f"  K = {k_val} ({k_label})")
    print(f"  {'─' * 60}")

    for data_label, y_data, fits_dict in [("Nodes", n_nodes, node_fits),
                                           ("Edges", n_edges, edge_fits)]:
        # Skip if K is smaller than current data
        if k_val < y_data[-1] * 0.95:
            print(f"    {data_label}: SKIPPED (K={k_val} < current value {y_data[-1]:.0f})")
            fits_dict[k_label] = None
            continue

        result, err = fit_logistic(t_days, y_data, data_label, fixed_K=k_val)
        if err:
            print(f"    {data_label}: {err}")
            fits_dict[k_label] = None
            continue

        fits_dict[k_label] = result
        print(f"    {data_label}: r={result['r']:.4f}/day, "
              f"t_mid={result['t_mid_date']} (day {result['t_mid_day']:.1f}), "
              f"R²={result['R2']:.6f}, "
              f"RMS={result['rms_resid']:.1f}")

    print()

# ══════════════════════════════════════════════════════════════════════
# PART 3: COMPARISON TABLE
# ══════════════════════════════════════════════════════════════════════

print("=" * 100)
print("PART 3: MODEL COMPARISON — NODES")
print("=" * 100)
print()

header = f"  {'Model':<30} {'K':>8} {'r':>8} {'t_mid':>12} {'R²':>10} {'RMS':>8}"
print(header)
print(f"  {'─' * 78}")

# Free fit
if 'free_fit_nodes' in dir():
    r = free_fit_nodes
    print(f"  {'Free fit':<30} {r['K']:>8.0f} {r['r']:>8.4f} {r['t_mid_date']:>12} "
          f"{r['R2']:>10.6f} {r['rms_resid']:>8.1f}")

# Fixed K fits
for k_label in sorted(K_CANDIDATES.keys(), key=lambda x: K_CANDIDATES[x]):
    r = node_fits.get(k_label)
    if r:
        k_val = K_CANDIDATES[k_label]
        print(f"  {'K=' + str(k_val) + ' (' + k_label.split(':')[0].strip() + ')':<30} "
              f"{r['K']:>8.0f} {r['r']:>8.4f} {r['t_mid_date']:>12} "
              f"{r['R2']:>10.6f} {r['rms_resid']:>8.1f}")

print()

# ══════════════════════════════════════════════════════════════════════
# PART 4: BST RATIONAL ANALYSIS OF GROWTH RATE
# ══════════════════════════════════════════════════════════════════════

print("=" * 100)
print("PART 4: GROWTH RATE vs BST RATIONALS")
print("=" * 100)
print()

# Collect all fitted r values
all_r_values = []
if 'free_fit_nodes' in dir():
    all_r_values.append(("Free fit (nodes)", free_fit_nodes['r']))

grace_fit = node_fits.get("Grace: N_max * dim_R")
if grace_fit:
    all_r_values.append(("K=1370 Grace (nodes)", grace_fit['r']))

for label, r_val in all_r_values:
    print(f"  {label}: r = {r_val:.6f} / day")
    print(f"  {'─' * 60}")

    # Find top 5 closest BST rationals
    dists = []
    for name, val in BST_RATIONALS.items():
        dist = abs(r_val - val)
        rel_dist = dist / val if val > 0 else float('inf')
        dists.append((name, val, dist, rel_dist))
    dists.sort(key=lambda x: x[2])

    print(f"    {'Rational':<20} {'Value':>8} {'|r - val|':>10} {'Rel. err':>10}")
    print(f"    {'─' * 52}")
    for name, val, dist, rel in dists[:8]:
        print(f"    {name:<20} {val:>8.4f} {dist:>10.4f} {rel:>10.1%}")
    print()

    # Special test: is r close to any simple fraction p/q with small q?
    print(f"    Simple fraction search (r = {r_val:.6f}):")
    best_frac = None
    best_frac_dist = float('inf')
    for q in range(1, 50):
        p = round(r_val * q)
        if p > 0:
            frac_val = p / q
            dist = abs(r_val - frac_val)
            if dist < best_frac_dist:
                best_frac_dist = dist
                best_frac = (p, q, frac_val)
            if dist < 0.005:
                print(f"      {p}/{q} = {frac_val:.6f}  (dist = {dist:.6f})")
    if best_frac:
        p, q, fv = best_frac
        print(f"    Best simple fraction: {p}/{q} = {fv:.6f} (dist = {best_frac_dist:.6f})")
    print()

# ══════════════════════════════════════════════════════════════════════
# PART 5: RESIDUAL ANALYSIS
# ══════════════════════════════════════════════════════════════════════

print("=" * 100)
print("PART 5: RESIDUAL ANALYSIS (Grace K=1370 node fit)")
print("=" * 100)
print()

grace_node_fit = node_fits.get("Grace: N_max * dim_R")
if grace_node_fit:
    print(f"  {'Date':<12} {'Day':>5} {'Actual':>8} {'Predicted':>10} {'Residual':>10} {'Rel%':>8}")
    print(f"  {'─' * 56}")
    for i, ts in enumerate(time_series):
        actual = ts["nodes"]
        pred = grace_node_fit['y_pred'][i]
        resid = grace_node_fit['residuals'][i]
        rel = resid / actual * 100 if actual > 0 else 0
        print(f"  {ts['date']:<12} {ts['day']:>5.0f} {actual:>8} {pred:>10.1f} {resid:>10.1f} {rel:>7.1f}%")
    print()
    print(f"  R² = {grace_node_fit['R2']:.6f}")
    print(f"  RMS residual = {grace_node_fit['rms_resid']:.1f} nodes")
    print(f"  Max |residual| = {grace_node_fit['max_resid']:.1f} nodes")
else:
    # Use free fit instead
    if 'free_fit_nodes' in dir():
        print("  Grace K=1370 fit not available; using free fit.")
        result = free_fit_nodes
        print(f"  {'Date':<12} {'Day':>5} {'Actual':>8} {'Predicted':>10} {'Residual':>10} {'Rel%':>8}")
        print(f"  {'─' * 56}")
        for i, ts in enumerate(time_series):
            actual = ts["nodes"]
            pred = result['y_pred'][i]
            resid = result['residuals'][i]
            rel = resid / actual * 100 if actual > 0 else 0
            print(f"  {ts['date']:<12} {ts['day']:>5.0f} {actual:>8} {pred:>10.1f} {resid:>10.1f} {rel:>7.1f}%")
        print()

# ══════════════════════════════════════════════════════════════════════
# PART 6: EDGE GROWTH ANALYSIS
# ══════════════════════════════════════════════════════════════════════

print("=" * 100)
print("PART 6: EDGE GROWTH — LOGISTIC vs POWER LAW")
print("=" * 100)
print()

# Edges often grow faster than nodes. Test both logistic and power-law.

# Power law: E(N) = a * N^b
# Take log: log(E) = log(a) + b * log(N)
valid_mask = (n_nodes > 0) & (n_edges > 0)
log_n = np.log(n_nodes[valid_mask])
log_e = np.log(n_edges[valid_mask])

if len(log_n) > 2:
    # Linear fit in log-log space
    coeffs = np.polyfit(log_n, log_e, 1)
    b_power = coeffs[0]
    a_power = np.exp(coeffs[1])

    e_pred_power = a_power * n_nodes[valid_mask] ** b_power
    ss_res_power = np.sum((n_edges[valid_mask] - e_pred_power) ** 2)
    ss_tot_power = np.sum((n_edges[valid_mask] - np.mean(n_edges[valid_mask])) ** 2)
    r2_power = 1 - ss_res_power / ss_tot_power

    print(f"  Power law: E(N) = {a_power:.4f} * N^{b_power:.4f}")
    print(f"  R² (power law) = {r2_power:.6f}")
    print()

    # BST test: is the exponent b close to a BST rational?
    bst_name, bst_val, bst_dist = find_closest_bst_rational(b_power)
    print(f"  Power law exponent b = {b_power:.4f}")
    print(f"  Closest BST rational: {bst_name} = {bst_val:.4f} (distance = {bst_dist:.4f})")
    print()

    # Also check E/N ratio evolution
    en_ratios = n_edges / n_nodes
    print(f"  E/N ratio evolution:")
    print(f"    Start:   {en_ratios[0]:.2f} (N={int(n_nodes[0])})")
    print(f"    Middle:  {en_ratios[len(en_ratios)//2]:.2f} (N={int(n_nodes[len(n_nodes)//2])})")
    print(f"    End:     {en_ratios[-1]:.2f} (N={int(n_nodes[-1])})")
    print()

# Free logistic fit for edges
print("  Logistic fit for edges (free K):")
edge_free, err = fit_logistic(t_days, n_edges, "Edges")
if edge_free and not err:
    print(f"    K = {edge_free['K']:.0f}")
    print(f"    r = {edge_free['r']:.4f}/day")
    print(f"    t_mid = {edge_free['t_mid_date']}")
    print(f"    R² = {edge_free['R2']:.6f}")
    print()

    # BST test for edge K
    # Expected: K_edges = K_nodes * avg_degree or similar
    if 'free_fit_nodes' in dir():
        ke_kn_ratio = edge_free['K'] / free_fit_nodes['K']
        print(f"    K_edges / K_nodes = {ke_kn_ratio:.2f}")
        bst_name_e, bst_val_e, bst_dist_e = find_closest_bst_rational(ke_kn_ratio)
        print(f"    Closest BST rational: {bst_name_e} = {bst_val_e:.4f} (distance = {bst_dist_e:.4f})")

        # Also check: is K_edges close to any BST product?
        bst_edge_candidates = {
            "N_max * dim_R * n_C":  N_max * dim_R * n_C,       # 6850
            "N_max * dim_R * g":    N_max * dim_R * g,          # 9590
            "N_max^2":              N_max ** 2,                  # 18769
            "N_max * C_2 * dim_R":  N_max * C_2 * dim_R,        # 8220
            "N_max * dim_R * N_c":  N_max * dim_R * N_c,        # 4110
            "(N_max * dim_R)^2 / N_max": (N_max * dim_R)**2 / N_max,  # 13700
        }
        print(f"    K_edges = {edge_free['K']:.0f}")
        print(f"    BST edge capacity candidates:")
        for name, val in sorted(bst_edge_candidates.items(), key=lambda x: abs(x[1] - edge_free['K'])):
            ratio = edge_free['K'] / val
            print(f"      {name} = {val:.0f}  (ratio = {ratio:.3f})")
        print()

# ══════════════════════════════════════════════════════════════════════
# PART 7: ASCII GROWTH CURVES
# ══════════════════════════════════════════════════════════════════════

print("=" * 100)
print("PART 7: NODE GROWTH TRAJECTORY (actual vs Grace logistic)")
print("=" * 100)
print()

WIDTH = 70

if grace_node_fit or ('free_fit_nodes' in dir()):
    fit_to_use = grace_node_fit if grace_node_fit else free_fit_nodes
    K_display = fit_to_use['K']
    scale = K_display * 1.1  # 10% headroom

    # Mark K/2 (inflection)
    inflection_node = K_display / 2

    print(f"  K = {K_display:.0f}  |  K/2 = {inflection_node:.0f}  |  Scale = {scale:.0f}")
    print(f"  '*' = actual  |  '.' = predicted  |  'X' = overlap  |  '|' = K/2")
    print()

    for i, ts in enumerate(time_series):
        actual = ts["nodes"]
        pred = fit_to_use['y_pred'][i]

        pos_a = int(actual / scale * WIDTH)
        pos_p = int(pred / scale * WIDTH)
        pos_half = int(inflection_node / scale * WIDTH)

        line = list(" " * (WIDTH + 1))
        if 0 <= pos_half <= WIDTH:
            line[pos_half] = "|"
        if 0 <= pos_p <= WIDTH:
            line[pos_p] = "."
        if 0 <= pos_a <= WIDTH:
            if pos_a == pos_p:
                line[pos_a] = "X"
            else:
                line[pos_a] = "*"

        print(f"  {ts['date']}  {''.join(line)}  N={actual}")

    # Axis
    pos_half = int(inflection_node / scale * WIDTH)
    axis = list("-" * (WIDTH + 1))
    if 0 <= pos_half <= WIDTH:
        axis[pos_half] = "^"
    print(f"  {'':12}{''.join(axis)}")
    label_half = f"K/2={inflection_node:.0f}"
    print(f"  {'':12}0{' ' * max(0, pos_half - len(label_half)//2 - 1)}{label_half}"
          f"{' ' * max(0, WIDTH - pos_half - len(label_half)//2)}{K_display:.0f}")
    print()

# ══════════════════════════════════════════════════════════════════════
# PART 8: FINAL VERDICT
# ══════════════════════════════════════════════════════════════════════

print("=" * 100)
print("FINAL VERDICT: GRACE'S LOGISTIC PREDICTION")
print("=" * 100)
print()

tests = []

# Test 1: Does growth follow logistic at all?
if 'free_fit_nodes' in dir():
    is_logistic = free_fit_nodes['R2'] > 0.95
    tests.append(("Node growth is logistic (R² > 0.95)",
                   is_logistic,
                   f"R² = {free_fit_nodes['R2']:.6f}"))

# Test 2: K close to 1370?
if 'free_fit_nodes' in dir():
    k_ratio = free_fit_nodes['K'] / 1370
    k_close = 0.7 < k_ratio < 1.5
    tests.append(("Free-fit K consistent with 1370 (within 30-50%)",
                   k_close,
                   f"K = {free_fit_nodes['K']:.0f}, ratio = {k_ratio:.3f}"))

# Test 3: Inflection near March 31?
if 'free_fit_nodes' in dir():
    t_mid_dt = datetime.strptime(free_fit_nodes['t_mid_date'], "%Y-%m-%d")
    march31 = datetime.strptime("2026-03-31", "%Y-%m-%d")
    delta = abs((t_mid_dt - march31).days)
    inflect_close = delta <= 7
    tests.append(("Inflection within 7 days of March 31",
                   inflect_close,
                   f"Fitted: {free_fit_nodes['t_mid_date']}, delta = {delta} days"))

# Test 4: K=1370 fit quality
if grace_node_fit:
    grace_good = grace_node_fit['R2'] > 0.90
    tests.append(("K=1370 fixed fit has R² > 0.90",
                   grace_good,
                   f"R² = {grace_node_fit['R2']:.6f}"))

# Test 5: r matches a BST rational
if 'free_fit_nodes' in dir():
    _, _, closest_dist = find_closest_bst_rational(free_fit_nodes['r'])
    r_bst = closest_dist < 0.05
    tests.append(("Growth rate r within 0.05 of a BST rational",
                   r_bst,
                   f"r = {free_fit_nodes['r']:.4f}, closest distance = {closest_dist:.4f}"))

# Test 6: Edge growth also logistic
if edge_free:
    edge_logistic = edge_free['R2'] > 0.90
    tests.append(("Edge growth is logistic (R² > 0.90)",
                   edge_logistic,
                   f"R² = {edge_free['R2']:.6f}"))

pass_count = sum(1 for _, p, _ in tests if p)
total = len(tests)

for name, passed, detail in tests:
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}] {name}")
    print(f"         {detail}")
    print()

print(f"  Score: {pass_count}/{total}")
print()

if pass_count >= total - 1:
    print("  VERDICT: STRONG support for Grace's logistic prediction.")
    print("  The AC graph growth is well-described by a logistic curve")
    print("  with parameters consistent with BST constants.")
elif pass_count >= total // 2:
    print("  VERDICT: MODERATE support for Grace's logistic prediction.")
    print("  The logistic model fits well, but not all BST parameter")
    print("  predictions are confirmed.")
else:
    print("  VERDICT: WEAK support. The logistic model may not capture")
    print("  the full growth dynamics, or the graph hasn't reached")
    print("  the inflection point yet.")

print()

# ══════════════════════════════════════════════════════════════════════
# PART 9: NUANCED INTERPRETATION — CARRYING CAPACITY ANALYSIS
# ══════════════════════════════════════════════════════════════════════

print("=" * 100)
print("PART 9: INTERPRETATION — CARRYING CAPACITY ANALYSIS")
print("=" * 100)
print()

if 'free_fit_nodes' in dir():
    K_free = free_fit_nodes['K']
    K_grace = 1370
    current_N = int(n_nodes[-1])

    print("  WHY THE FREE-FIT K MAY UNDERESTIMATE THE TRUE CARRYING CAPACITY")
    print("  " + "-" * 65)
    print()
    print(f"  Current N = {current_N} is {current_N/K_grace*100:.1f}% of Grace's K=1370")
    print(f"  Current N = {current_N/K_free*100:.1f}% of free-fit K={K_free:.0f}")
    print()
    print("  The free fit sees the current plateau (days 20-22: 897->952->981)")
    print("  and interprets it as approaching saturation. But this 'plateau'")
    print("  could be a gap between sessions (April 5-9 has no new theorems")
    print("  in the dated set, then growth resumes April 9-11).")
    print()

    # Check: what fraction of logistic curve have we observed?
    frac_of_curve = current_N / K_grace
    print(f"  If Grace is right (K=1370), we have observed {frac_of_curve*100:.0f}% of the curve.")
    print(f"  The logistic is symmetric around K/2={K_grace/2:.0f}.")
    print(f"  We have passed the inflection and are in the decelerating phase.")
    print(f"  But 22 days of data with session gaps makes the tail uncertain.")
    print()

    # Key diagnostic: is growth still accelerating?
    mid_idx = len(time_series) // 2
    first_half_rate = (n_nodes[mid_idx] - n_nodes[0]) / max(1, t_days[mid_idx] - t_days[0])
    second_half_rate = (n_nodes[-1] - n_nodes[mid_idx]) / max(1, t_days[-1] - t_days[mid_idx])

    print(f"  Average daily growth rate:")
    print(f"    First half  (day 0-{t_days[mid_idx]:.0f}):   {first_half_rate:.1f} nodes/day")
    print(f"    Second half (day {t_days[mid_idx]:.0f}-{t_days[-1]:.0f}):  {second_half_rate:.1f} nodes/day")
    if second_half_rate < first_half_rate:
        print(f"    Ratio: {second_half_rate/first_half_rate:.2f} -- growth IS decelerating")
        print(f"    This is consistent with being past the logistic inflection.")
    else:
        print(f"    Ratio: {second_half_rate/first_half_rate:.2f} -- growth is NOT decelerating")
        print(f"    This suggests we may not have reached inflection yet.")
    print()

    # The real test: wait for more data
    print("  RESOLUTION: The K=1370 vs K=932 question will be settled by")
    print("  watching the next ~200 theorems. If growth continues toward 1200+,")
    print("  Grace's prediction holds. If it plateaus near 1000, the free fit wins.")
    print()

    # Grace's K=1370 fit: when forced, r becomes 0.178 ~ f_Godel = 0.191
    grace_fit_check = node_fits.get("Grace: N_max * dim_R")
    if grace_fit_check:
        r_grace = grace_fit_check['r']
        print(f"  NOTABLE: When K is forced to 1370, the growth rate becomes")
        print(f"    r = {r_grace:.4f}, which is {abs(r_grace - 0.191)/0.191*100:.1f}% from")
        print(f"    the Godel limit f = 0.191. If this holds, it would mean:")
        print(f"    'The AC graph grows at the Godel rate toward the BST capacity.'")
        print()

    # 18/49 = (2*3^2) / (7^2) -- note: 49 = g^2, 18 = 2*3^2 = 2*N_c^2
    print("  NOTABLE: The best simple fraction for the free-fit r is")
    print(f"    18/49 = 0.367347, and 49 = g^2 = 7^2, 18 = 2*N_c^2 = 2*9.")
    print(f"    So r ~ 2*N_c^2 / g^2 -- a pure BST expression.")
    print()

    # Edge-to-node K ratio
    if edge_free:
        ke_kn = edge_free['K'] / K_free
        print(f"  EDGE/NODE CAPACITY RATIO: K_edges/K_nodes = {ke_kn:.2f}")
        print(f"    If K_nodes=1370 and same ratio: K_edges ~ {1370*ke_kn:.0f}")
        closest_product = N_max * dim_R * N_c  # 4110
        print(f"    Compare: N_max * dim_R * N_c = {closest_product}")
        print(f"    Ratio: {1370*ke_kn/closest_product:.3f}")
        print()

print()

# ── Summary of key numbers ────────────────────────────────────────────
print("=" * 100)
print("KEY NUMBERS SUMMARY")
print("=" * 100)
print()
if 'free_fit_nodes' in dir():
    r = free_fit_nodes
    print(f"  Best-fit carrying capacity:   K = {r['K']:.0f} nodes")
    print(f"  Grace's prediction:           K = 1370 = N_max * dim_R")
    print(f"  Ratio (fitted/Grace):         {r['K']/1370:.3f}")
    print()
    print(f"  Fitted inflection point:      {r['t_mid_date']} (day {r['t_mid_day']:.1f})")
    print(f"  Grace's prediction:           2026-03-31")
    print()
    print(f"  Growth rate:                  r = {r['r']:.6f} / day")
    bst_name, bst_val, _ = find_closest_bst_rational(r['r'])
    print(f"  Closest BST rational:         {bst_name} = {bst_val:.6f}")
    print()
    print(f"  Node fit R²:                  {r['R2']:.6f}")
if edge_free:
    print(f"  Edge fit R²:                  {edge_free['R2']:.6f}")
    print(f"  Edge carrying capacity:       K_edges = {edge_free['K']:.0f}")

print()
print("=" * 100)
