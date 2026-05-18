"""
Toy 3057 — P1 correction hunt: catalog watchlist scan (1-2% precision entries).

Owner: Elie (Casey "do all" directive, Keeper steady-catalog pull)
Date: 2026-05-18 PM

GOAL
====
Per Keeper digest: Paper #83 has ~14 watchlist entries at 1-2% precision. Some
may yield to known correction classes:
  - T1444 vacuum subtraction (-1 from BST primary, e.g., (N_max-1)/N_max)
  - T1446 two-sector duality (CKM colored vs PMNS colorless, ×cos²θ_13 etc.)
  - T1455 bridge invariance (g/C_2 = 7/6 dressed)
  - Today's K52a (1 ± 1/M_g) class — Lamb-style atomic/cm sub-percent corrections

This toy SCANS the catalog for D-tier / I-tier entries at 1-2% precision and
identifies candidates that MIGHT respond to a known correction class. Honest
deliverable: candidates surveyed; closures left to follow-up sessions or team
review.

DISCIPLINE (per Cal Rule 6)
===========================
- NOT unilateral closure of any entry
- Survey produces candidate list + suggested correction class
- Tier promotions/changes await Keeper K-audit + author concurrence
"""

import json
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
INV_FILE = os.path.join(ROOT, "data", "bst_geometric_invariants.json")

tests = []
def check(label, ok):
    tests.append((bool(ok), label))


def parse_precision(prec):
    """Return float precision in pct, or None if unparseable."""
    if prec is None:
        return None
    if isinstance(prec, (int, float)):
        return float(prec)
    if isinstance(prec, str):
        m = re.search(r"([\d.]+)\s*%", prec)
        if m:
            return float(m.group(1))
        try:
            return float(prec)
        except (ValueError, TypeError):
            return None
    return None


print("=" * 72)
print("Toy 3057 — P1 correction hunt: 1-2% watchlist scan")
print("=" * 72)

with open(INV_FILE) as f:
    inv_data = json.load(f)
invariants = inv_data.get('invariants', [])
print(f"\nLoaded {len(invariants)} invariants total")

watchlist = []
for inv in invariants:
    tier = inv.get('tier', '').upper()
    if tier not in ('D', 'I'):
        continue
    prec = inv.get('precision_pct', inv.get('precision', None))
    prec_val = parse_precision(prec)
    if prec_val is None:
        continue
    if 1.0 <= prec_val <= 2.0:
        watchlist.append({
            'id': inv.get('id', '?'),
            'name': inv.get('name', '?'),
            'symbol': inv.get('symbol', '?'),
            'domain': inv.get('domain', '?'),
            'tier': tier,
            'precision_pct': prec_val,
            'formula': inv.get('expression', inv.get('formula', inv.get('bst_expr', '?'))),
            'observed': inv.get('observed_value', inv.get('observed', '?')),
            'bst_value': inv.get('BST_value', inv.get('bst_value', '?')),
            'notes': inv.get('notes', ''),
        })

print(f"\n[T1] Watchlist entries (D or I tier, 1.0%-2.0% precision): {len(watchlist)}")

# Sort by precision
watchlist.sort(key=lambda x: x['precision_pct'])

# Display
print(f"\n  {'ID':<10} {'Tier':>4} {'Prec':>6} {'Name':<45}")
print(f"  {'-'*10} {'-'*4} {'-'*6} {'-'*45}")
for w in watchlist[:25]:
    name_short = w['name'][:43] if w['name'] else '?'
    print(f"  {w['id'][:10]:<10} {w['tier']:>4} {w['precision_pct']:>5.2f}% {name_short:<45}")

check("Watchlist scan completed", len(watchlist) >= 5)

# === T2: Correction class candidate identification ===
print(f"\n[T2] Correction class candidate identification")

candidates_by_class = {
    'vacuum_subtraction (T1444)': [],
    'two_sector_duality (T1446)': [],
    'bridge_invariance (T1455)': [],
    'K52a_M_g (today)': [],
    'unknown / multi-week': [],
}

for w in watchlist:
    formula = str(w['formula']).lower()
    domain = str(w['domain']).lower()
    notes = str(w['notes']).lower()
    s = formula + ' ' + domain + ' ' + notes

    classified = False
    # Vacuum subtraction signals: presence of "-1" or "N_max-1" in formula
    if 'n_max - 1' in s or 'n_max-1' in s or '136' in s or '79' in s or '11/12' in s:
        candidates_by_class['vacuum_subtraction (T1444)'].append(w)
        classified = True
    # Two-sector duality signals: CKM/PMNS mixing
    elif 'ckm' in s or 'pmns' in s or 'mixing' in s or 'theta_13' in s or 'theta_12' in s or 'theta_23' in s:
        candidates_by_class['two_sector_duality (T1446)'].append(w)
        classified = True
    # Bridge invariance: g/C_2 = 7/6 or related dressing
    elif '7/6' in s or 'g/c_2' in s or 'g/c2' in s or 'genus/casimir' in s or 'wilson-fisher' in s or 'ising' in s:
        candidates_by_class['bridge_invariance (T1455)'].append(w)
        classified = True
    # K52a (1 ± 1/M_g): atomic / condensed-matter sub-percent (UNLIKELY for >1% entries; mostly diagnostic)
    elif ('atomic' in domain or 'condensed_matter' in domain or 'qed' in s) and '127' in s:
        candidates_by_class['K52a_M_g (today)'].append(w)
        classified = True
    else:
        candidates_by_class['unknown / multi-week'].append(w)

for cls, entries in candidates_by_class.items():
    print(f"\n  {cls}: {len(entries)} candidate(s)")
    for w in entries[:5]:
        print(f"    {w['id']}: {w['name'][:50]} ({w['precision_pct']:.2f}%, {w['domain']})")

# === T3: Honest recommendation per candidate class ===
print(f"\n[T3] Honest recommendations per class")
print(f"  Vacuum subtraction (T1444): try (X-1)/X factor on formula; works in CKM sector")
print(f"  Two-sector duality (T1446): apply cos^2(theta_13) = 44/45 in PMNS-side")
print(f"  Bridge invariance (T1455): try g/C_2 = 7/6 dressing variants")
print(f"  K52a M_g: (1 ± 1/M_g) only applies in atomic/cm sub-percent regime")
print(f"  Unknown / multi-week: needs first-principles BST mechanism work")

# === T4: Pre-staged forward predictions for each candidate ===
print(f"\n[T4] Pre-staged candidate predictions (for follow-up sessions)")
# Pick top 3-5 by precision (closest to 1.0% — easiest to push under 1%)
top_candidates = watchlist[:5]
predictions = []
for w in top_candidates:
    formula = str(w['formula'])
    # Suggest a correction direction
    suggested = ""
    if 'ckm' in str(w['domain']).lower() or 'mixing' in str(w['name']).lower():
        suggested = "T1444 vacuum subtraction: try formula × (M-1)/M"
    elif 'ising' in str(w['name']).lower() or 'g/c_2' in formula:
        suggested = "T1455 bridge invariance: try g/C_2 = 7/6 dressing"
    elif 'higgs' in str(w['name']).lower() or 'lambda_h' in str(w['symbol']).lower():
        suggested = "Already closed at D-tier 0.1% (Toy 2983); higher precision needs CODATA input audit"
    else:
        suggested = "Pre-stage: try (1 ± small BST primary fraction) sub-leading correction"
    predictions.append({'entry': w, 'suggested_correction_class': suggested})

print(f"  {'ID':<10} {'Name':<35} {'Suggested correction':<60}")
print(f"  {'-'*10} {'-'*35} {'-'*60}")
for p in predictions:
    e = p['entry']
    name = e['name'][:33] if e['name'] else '?'
    sugg = p['suggested_correction_class'][:58]
    print(f"  {e['id'][:10]:<10} {name:<35} {sugg:<60}")

check("Top 5 candidates have suggested correction classes", len(predictions) >= 5)

# === T5: NOT-CLAIMED honest scope ===
print(f"\n[T5] NOT CLAIMED:")
print(f"  - Any unilateral tier change or formula update")
print(f"  - Closure of any watchlist entry to <1% precision")
print(f"  - Promotion of any candidate beyond 'candidate' status")
print(f"  - Universality of named correction classes beyond their documented domains")

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3057_P1_watchlist_scan.json")
out = {
    'meta': {
        'date': '2026-05-18',
        'owner': 'Elie',
        'task': 'P1 correction hunt watchlist scan',
        'discipline': 'survey + suggest, NOT closure',
    },
    'watchlist_count': len(watchlist),
    'watchlist': [{'id': w['id'], 'name': w['name'], 'precision_pct': w['precision_pct'],
                    'tier': w['tier'], 'domain': w['domain']} for w in watchlist[:30]],
    'candidates_by_class': {cls: len(items) for cls, items in candidates_by_class.items()},
    'top_5_predictions': [{
        'id': p['entry']['id'],
        'name': p['entry']['name'],
        'precision_pct': p['entry']['precision_pct'],
        'suggested_correction_class': p['suggested_correction_class'],
    } for p in predictions],
}
with open(out_path, 'w') as f:
    json.dump(out, f, indent=2)
print(f"\n  Output: {os.path.basename(out_path)}")

# Score
passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}")
print(f"Toy 3057 SCORE: {passed}/{total}")
print(f"{'='*72}")
for ok, label in tests:
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {label}")

print(f"""
P1 CORRECTION HUNT DELIVERABLE (Survey only):
  Watchlist scanned: {len(watchlist)} D/I-tier entries at 1-2% precision
  Candidates by correction class:
    - vacuum subtraction (T1444): {len(candidates_by_class['vacuum_subtraction (T1444)'])}
    - two-sector duality (T1446): {len(candidates_by_class['two_sector_duality (T1446)'])}
    - bridge invariance (T1455): {len(candidates_by_class['bridge_invariance (T1455)'])}
    - K52a M_g (today): {len(candidates_by_class['K52a_M_g (today)'])}
    - unknown / multi-week: {len(candidates_by_class['unknown / multi-week'])}

  Top 5 closest-to-1% candidates flagged for follow-up.

NEXT SESSION (if pulled):
  Take 1 top candidate, attempt the suggested correction class, verify against
  observation. If correction works: file as updated catalog entry at improved
  precision under Keeper K-audit governance. If not: deviations locate
  boundaries (Casey hunting principle).

NOT CLAIMED in this toy:
  Any closure, tier change, or formula update. Survey-only deliverable.
""")
