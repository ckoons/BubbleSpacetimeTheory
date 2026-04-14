#!/usr/bin/env python3
"""BST Explorer — Interactive CI-native exploration of Bubble Spacetime Theory.

Load structured data files and explore BST constants, particles, forces,
predictions, and domains interactively.

Modes:
  explore <integer>    — Show everything that uses a given BST integer
  derive <name>        — Walk the derivation chain for a constant
  domain <name>        — Show all constants and predictions in a domain
  connect <a> <b>      — Find connection between two domains via theorem graph
  verify [name|all]    — Evaluate formula_code and compare to observed values
  random               — Pick a random constant and tell its story
  search <term>        — Search across all data files
  stats                — Show summary statistics
  seed                 — Display the minimal BST kernel
  help                 — Show this help

Usage:
  python3 toy_bst_explorer.py                  # Interactive REPL
  python3 toy_bst_explorer.py derive proton    # Single command
  python3 toy_bst_explorer.py verify all       # Verify all formulas
"""

import json
import math
import os
import random
import sys
import readline  # enables arrow keys in input()
from math import pi, sqrt, log, exp, sin, cos, tan, atan, asin, acos, factorial
from math import comb

# ── BST Evaluation Namespace ─────────────────────────────────────────────

rank  = 2
N_c   = 3
n_C   = 5
C_2   = 6
g     = 7
N_max = 137

alpha     = 1.0 / N_max
alpha_inv = N_max
pi5       = pi ** 5

m_e    = 0.51099895000       # electron mass, MeV
m_p    = 6 * pi5 * m_e      # proton mass, MeV
m_e_GeV = m_e / 1000.0
m_p_GeV = m_p / 1000.0
hbar_c = 197.3269804         # MeV*fm
c_light = 2.99792458e8       # speed of light, m/s
H_0 = 67.4 * 1e3 / 3.0857e22  # Hubble constant, 1/s (67.4 km/s/Mpc)

# Aliases for formula_code evaluation
ln = log
cbrt = lambda x: x ** (1.0/3.0)
Fraction = lambda a, b: a / b
inf = float('inf')

EVAL_NS = {
    'rank': rank, 'N_c': N_c, 'n_C': n_C, 'C_2': C_2, 'g': g, 'N_max': N_max,
    'alpha': alpha, 'alpha_inv': alpha_inv, 'pi': pi, 'pi5': pi5,
    'sqrt': sqrt, 'cbrt': cbrt, 'log': log, 'ln': ln, 'exp': exp,
    'sin': sin, 'cos': cos, 'tan': tan, 'atan': atan, 'asin': asin, 'acos': acos,
    'comb': comb, 'factorial': factorial, 'Fraction': Fraction,
    'abs': abs, 'pow': pow, 'float': float, 'inf': inf,
    'm_e': m_e, 'm_e_GeV': m_e_GeV, 'm_p': m_p, 'm_p_GeV': m_p_GeV,
    'hbar_c': hbar_c,
    'c_light': c_light, 'H_0': H_0,
}

# ── Data Loading ─────────────────────────────────────────────────────────

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')

def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        print(f"  [Warning] {filename} not found at {path}")
        return None
    with open(path) as f:
        return json.load(f)

def load_all_data():
    data = {}
    data['constants'] = load_json('bst_constants.json')
    data['particles'] = load_json('bst_particles.json')
    data['forces'] = load_json('bst_forces.json')
    data['predictions'] = load_json('bst_predictions.json')
    data['domains'] = load_json('bst_domains.json')
    # AC theorem graph (large)
    graph_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ac_graph_data.json')
    if os.path.exists(graph_path):
        with open(graph_path) as f:
            data['graph'] = json.load(f)
    else:
        data['graph'] = None
    return data

# ── Display Helpers ──────────────────────────────────────────────────────

TIER_LABELS = {1: "DERIVED", 2: "STRUCTURAL", 3: "OBSERVED"}
TIER_COLORS = {1: "\033[92m", 2: "\033[93m", 3: "\033[91m"}
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

def tier_label(tier):
    color = TIER_COLORS.get(tier, "")
    label = TIER_LABELS.get(tier, "?")
    return f"{color}{label}{RESET}"

def print_constant(c, verbose=False):
    print(f"\n  {BOLD}{c['name']}{RESET}  [{c['theorem_id']}]  Tier {tier_label(c['tier'])}")
    print(f"  Formula: {c['formula_display']}")
    if c.get('bst_value') is not None:
        print(f"  BST value:      {c['bst_value']}")
    if c.get('observed_value') is not None:
        print(f"  Observed value: {c['observed_value']}  ({c.get('observed_source', '')})")
    print(f"  Precision: {c.get('precision', '?')}  |  Unit: {c.get('unit', '') or '(dimensionless)'}")
    print(f"  Integers: {', '.join(c.get('bst_integers_used', []))}")
    if verbose and c.get('derivation_chain'):
        print(f"  Derivation chain:")
        for step in c['derivation_chain']:
            print(f"    -> {step}")
    if verbose and c.get('mechanism'):
        print(f"  Mechanism: {c['mechanism']}")

def print_particle(p):
    print(f"\n  {BOLD}{p['name']}{RESET}  ({p['symbol']})")
    print(f"  {p['substrate_description']}")
    print(f"  Layer: {p['geometric_layer']}  |  Winding: {p.get('winding_number')}")
    print(f"  Mass: {p.get('mass_value', '?')} {p.get('mass_unit', '')}")
    print(f"  Charge: {p['charge']}  |  Spin: {p['spin']}  |  Stable: {p.get('stable')}")
    if p.get('key_insight'):
        print(f"  Insight: {p['key_insight']}")

def print_prediction(pred):
    print(f"\n  {BOLD}{pred['name']}{RESET}  [{pred['id']}]")
    print(f"  {pred['prediction']}")
    print(f"  BST value: {pred['bst_value']}")
    print(f"  Current: {pred.get('current_measurement', '?')}")
    print(f"  Experiment: {pred.get('experiment', '?')}")
    print(f"  Timeline: {pred.get('timeline', '?')}")
    print(f"  Falsification: {pred.get('falsification_criterion', '?')}")
    if pred.get('sharpest_test'):
        print(f"  *** SHARPEST TEST: {pred.get('sharpest_test_reason', '')} ***")

# ── Commands ─────────────────────────────────────────────────────────────

def cmd_explore(data, integer_name):
    """Show everything that uses a given BST integer."""
    integer_name = integer_name.strip()
    valid = {'rank', 'N_c', 'n_C', 'C_2', 'g', 'N_max'}
    if integer_name not in valid:
        print(f"  Unknown integer '{integer_name}'. Valid: {', '.join(sorted(valid))}")
        return
    val = {'rank': 2, 'N_c': 3, 'n_C': 5, 'C_2': 6, 'g': 7, 'N_max': 137}[integer_name]
    print(f"\n{'='*60}")
    print(f"  Everything using {BOLD}{integer_name} = {val}{RESET}")
    print(f"{'='*60}")

    if data['constants']:
        matches = [c for c in data['constants']['constants']
                   if integer_name in c.get('bst_integers_used', [])]
        print(f"\n  Constants ({len(matches)}):")
        for c in matches:
            print(f"    [{c['theorem_id']}] {c['name']} = {c.get('formula_display', '?')}  ({c.get('precision', '?')})")

    if data['particles']:
        # Check formulas for the integer name
        matches = [p for p in data['particles']['particles']
                   if integer_name.lower() in str(p.get('mass_formula', '')).lower()
                   or integer_name in str(p.get('substrate_description', ''))]
        if matches:
            print(f"\n  Particles ({len(matches)}):")
            for p in matches:
                print(f"    {p['name']} ({p['symbol']}) — {p.get('mass_formula', '?')}")

def cmd_derive(data, query):
    """Walk the derivation chain for a constant."""
    query = query.strip().lower()
    if not data['constants']:
        print("  No constants data loaded.")
        return
    matches = [c for c in data['constants']['constants']
               if query in c['name'].lower() or query in c.get('theorem_id', '').lower()
               or query in c.get('symbol', '').lower()]
    if not matches:
        print(f"  No constant matching '{query}'. Try 'search {query}'.")
        return
    for c in matches[:3]:
        print_constant(c, verbose=True)

def cmd_domain(data, query):
    """Show all constants and predictions in a domain."""
    query = query.strip().lower()
    if not data['domains']:
        print("  No domains data loaded.")
        return
    matches = [d for d in data['domains']['domains']
               if query in d['name'].lower() or query in d.get('ac_graph_name', '').lower()]
    if not matches:
        print(f"  No domain matching '{query}'.")
        return
    for dom in matches[:3]:
        print(f"\n{'='*60}")
        print(f"  {BOLD}{dom['name']}{RESET}  ({dom['theorem_count']} theorems)")
        print(f"{'='*60}")
        print(f"  {dom['description']}")
        if dom.get('key_results'):
            print(f"\n  Key results:")
            for r in dom['key_results']:
                print(f"    * {r}")
        # Show related constants
        if data['constants'] and dom.get('key_constants'):
            print(f"\n  Related constants:")
            for cid in dom['key_constants'][:10]:
                c = next((x for x in data['constants']['constants'] if x['id'] == cid), None)
                if c:
                    print(f"    [{c['theorem_id']}] {c['name']} ({c.get('precision', '?')})")

def cmd_connect(data, args):
    """Find connection between two domains via theorem graph."""
    parts = args.strip().split()
    if len(parts) < 2:
        print("  Usage: connect <domain1> <domain2>")
        return
    if not data['graph']:
        print("  No theorem graph loaded.")
        return

    d1, d2 = parts[0].lower(), parts[1].lower()
    theorems = data['graph'].get('theorems', [])
    edges = data['graph'].get('edges', [])

    # Find theorems in each domain
    t1 = {t['tid'] for t in theorems if d1 in t.get('domain', '').lower()}
    t2 = {t['tid'] for t in theorems if d2 in t.get('domain', '').lower()}

    if not t1:
        print(f"  No theorems in domain matching '{d1}'")
        return
    if not t2:
        print(f"  No theorems in domain matching '{d2}'")
        return

    # Build adjacency
    adj = {}
    for e in edges:
        s, t = e.get('source', e.get('from')), e.get('target', e.get('to'))
        if s is not None and t is not None:
            adj.setdefault(s, set()).add(t)
            adj.setdefault(t, set()).add(s)

    # BFS from d1 to d2
    from collections import deque
    queue = deque()
    visited = {}
    for tid in t1:
        queue.append((tid, [tid]))
        visited[tid] = [tid]

    found = None
    while queue and not found:
        curr, path = queue.popleft()
        if curr in t2:
            found = path
            break
        for nbr in adj.get(curr, []):
            if nbr not in visited:
                new_path = path + [nbr]
                visited[nbr] = new_path
                queue.append((nbr, new_path))
                if nbr in t2:
                    found = new_path
                    break

    if found:
        tid_map = {t['tid']: t for t in theorems}
        print(f"\n  Path from '{d1}' to '{d2}' ({len(found)} steps):")
        for tid in found:
            t = tid_map.get(tid, {})
            print(f"    T{tid}: {t.get('name', '?')} [{t.get('domain', '?')}]")
    else:
        print(f"  No path found from '{d1}' to '{d2}' (may need more edges loaded)")

def cmd_verify(data, query):
    """Evaluate formula_code and compare to observed values."""
    if not data['constants']:
        print("  No constants data loaded.")
        return
    constants = data['constants']['constants']
    query = query.strip().lower()

    if query == 'all':
        targets = constants
    else:
        targets = [c for c in constants
                   if query in c['name'].lower() or query in c.get('theorem_id', '').lower()]
    if not targets:
        print(f"  No constants matching '{query}'.")
        return

    passed = 0
    failed = 0
    skipped = 0

    for c in targets:
        code = c.get('formula_code', '')
        if not code or code == '1' or 'inf' in code.lower():
            skipped += 1
            continue
        try:
            bst_val = eval(code, {"__builtins__": {}}, EVAL_NS)
            obs_val = c.get('observed_value')
            if obs_val is None or obs_val == 0:
                skipped += 1
                continue
            if isinstance(obs_val, (int, float)) and obs_val != 0:
                pct = abs(bst_val - obs_val) / abs(obs_val) * 100
                status = "PASS" if pct < 5 else "MISS"
                if status == "PASS":
                    passed += 1
                else:
                    failed += 1
                if query != 'all' or status == "MISS":
                    color = "\033[92m" if status == "PASS" else "\033[91m"
                    print(f"  {color}{status}{RESET} [{c['theorem_id']}] {c['name']}: "
                          f"BST={bst_val:.6g} vs Obs={obs_val:.6g} ({pct:.4f}%)")
            else:
                skipped += 1
        except Exception as e:
            failed += 1
            if query != 'all':
                print(f"  ERROR [{c['theorem_id']}] {c['name']}: {e}")

    if query == 'all':
        total = passed + failed
        print(f"\n  Verification: {passed}/{total} passed ({passed/total*100:.1f}%), "
              f"{skipped} skipped (dimensionful/special)")

def cmd_random(data):
    """Pick a random constant and tell its story."""
    if not data['constants']:
        print("  No constants data loaded.")
        return
    c = random.choice(data['constants']['constants'])
    print_constant(c, verbose=True)

def cmd_search(data, query):
    """Search across all data files."""
    query = query.strip().lower()
    if not query:
        print("  Usage: search <term>")
        return

    results = []
    if data['constants']:
        for c in data['constants']['constants']:
            searchable = f"{c['name']} {c.get('symbol', '')} {c.get('mechanism', '')} {c.get('formula_display', '')}"
            if query in searchable.lower():
                results.append(('constant', c['theorem_id'], c['name'], c.get('precision', '')))

    if data['particles']:
        for p in data['particles']['particles']:
            searchable = f"{p['name']} {p['symbol']} {p.get('substrate_description', '')} {p.get('key_insight', '')}"
            if query in searchable.lower():
                results.append(('particle', p['id'], p['name'], ''))

    if data['predictions']:
        for pred in data['predictions']['predictions']:
            searchable = f"{pred['name']} {pred.get('prediction', '')} {pred.get('experiment', '')}"
            if query in searchable.lower():
                results.append(('prediction', pred['id'], pred['name'], pred.get('status', '')))

    if not results:
        print(f"  No results for '{query}'.")
        return
    print(f"\n  {len(results)} results for '{query}':")
    for kind, id_, name, extra in results[:20]:
        print(f"    [{kind:10s}] {id_:10s} {name}  {extra}")

def cmd_stats(data):
    """Show summary statistics."""
    print(f"\n{'='*60}")
    print(f"  {BOLD}BST Data Layer Statistics{RESET}")
    print(f"{'='*60}")

    if data['constants']:
        consts = data['constants']['constants']
        print(f"\n  Constants: {len(consts)}")
        for tier in [1, 2, 3]:
            count = sum(1 for c in consts if c['tier'] == tier)
            print(f"    Tier {tier} ({TIER_LABELS[tier]}): {count}")
        cats = {}
        for c in consts:
            cats[c['category']] = cats.get(c['category'], 0) + 1
        print(f"  Categories: {len(cats)}")
        for cat in sorted(cats, key=cats.get, reverse=True):
            print(f"    {cat}: {cats[cat]}")

    if data['particles']:
        print(f"\n  Particles: {len(data['particles']['particles'])}")

    if data['forces']:
        print(f"  Force layers: {len(data['forces']['layers'])}")

    if data['predictions']:
        preds = data['predictions']['predictions']
        print(f"\n  Predictions: {len(preds)}")
        statuses = {}
        for p in preds:
            s = p.get('status', 'unknown')
            statuses[s] = statuses.get(s, 0) + 1
        for s, count in sorted(statuses.items()):
            print(f"    {s}: {count}")

    if data['domains']:
        doms = data['domains']['domains']
        print(f"\n  Domains: {len(doms)}")
        total_thms = sum(d['theorem_count'] for d in doms)
        print(f"  Total theorems: {total_thms}")
        top5 = sorted(doms, key=lambda d: d['theorem_count'], reverse=True)[:5]
        print(f"  Top 5 by theorem count:")
        for d in top5:
            print(f"    {d['name']}: {d['theorem_count']}")

    if data['graph']:
        meta = data['graph'].get('meta', {})
        print(f"\n  AC Theorem Graph:")
        print(f"    Theorems: {meta.get('theorem_count', '?')}")
        print(f"    Edges: {meta.get('edge_count', '?')}")
        print(f"    Nodes: {meta.get('node_count', '?')}")

def cmd_seed(data):
    """Display the minimal BST kernel."""
    seed_path = os.path.join(DATA_DIR, 'bst_seed.md')
    if os.path.exists(seed_path):
        with open(seed_path) as f:
            print(f.read())
    else:
        print("  bst_seed.md not found.")

def cmd_help():
    print(__doc__)

# ── REPL ─────────────────────────────────────────────────────────────────

COMMANDS = {
    'explore': cmd_explore,
    'derive': cmd_derive,
    'domain': cmd_domain,
    'connect': cmd_connect,
    'verify': cmd_verify,
    'random': cmd_random,
    'search': cmd_search,
    'stats': cmd_stats,
    'seed': cmd_seed,
    'help': cmd_help,
}

def run_command(data, line):
    parts = line.strip().split(None, 1)
    if not parts:
        return True
    cmd = parts[0].lower()
    args = parts[1] if len(parts) > 1 else ''

    if cmd in ('quit', 'exit', 'q'):
        return False
    elif cmd == 'help':
        cmd_help()
    elif cmd == 'stats':
        cmd_stats(data)
    elif cmd == 'seed':
        cmd_seed(data)
    elif cmd == 'random':
        cmd_random(data)
    elif cmd in COMMANDS:
        COMMANDS[cmd](data, args)
    else:
        # Try as a search
        cmd_search(data, line.strip())
    return True

def main():
    print(f"\n{BOLD}BST Explorer{RESET} — Interactive Bubble Spacetime Theory data explorer")
    print(f"Five integers, zero free parameters, 500+ predictions.\n")

    print("Loading data files...")
    data = load_all_data()

    loaded = sum(1 for v in data.values() if v is not None)
    print(f"  {loaded}/{len(data)} data files loaded.\n")

    # Single command mode
    if len(sys.argv) > 1:
        line = ' '.join(sys.argv[1:])
        run_command(data, line)
        return

    # Interactive REPL
    print("Type 'help' for commands, 'quit' to exit.\n")
    while True:
        try:
            line = input(f"{BOLD}bst>{RESET} ")
            if not run_command(data, line):
                break
        except (EOFError, KeyboardInterrupt):
            print()
            break

    print("\nOne geometry. Five integers. Everything.")

if __name__ == '__main__':
    main()
