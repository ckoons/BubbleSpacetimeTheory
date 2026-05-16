#!/usr/bin/env python3
"""
Grace — Revert exactly the 73 RETRO-2 auto_* + status=structural items D → S
=============================================================================

Casey directive May 15, 17:50 EDT.

Out of: T1.7 RETRO-2 sample-audit (MESSAGES_2026-05-15.md Grace 17:35).

Predicate (precise):
  Entry is in the I→D delta between commits 9503f92 (pre-RETRO-2) and
  0b420b0 (post-RETRO-2 snapshot), AND its symbol starts with "auto_",
  AND its status field equals "structural", AND its current tier is "D".

This restricts the revert to the 73 RETRO-2 promotions specifically.
Pre-existing auto_+structural+D entries (~360 of them, tagged D in earlier
passes) are NOT touched by this script — Casey explicitly said "the 73".
Whether those pre-existing entries should also revert is a separate
decision.

What this does:
  1. Load both commits' data/bst_geometric_invariants.json
  2. Compute the I→D upgrade set (283 items)
  3. Filter to symbol=auto_* AND status=structural (the 73)
  4. Verify each is currently tier=D
  5. Restore Elie's lost Hilbert_Q5 entries from Toy 2255 (gone in earlier
     git checkout — out of scope for the revert, separate restoration)
  6. Revert the 73: tier D → S, annotate notes
  7. Write back JSON, save audit table

Author: Grace (Claude 4.7)
Date: May 15, 2026 — second attempt, properly scoped
"""

import json
import os
import subprocess

INV_PATH = "data/bst_geometric_invariants.json"
AUDIT_PATH = "notes/grace_revert_audit_2026-05-15.md"

PREV_COMMIT = "9503f92"   # pre-RETRO-2
CURR_COMMIT = "0b420b0"   # post-RETRO-2 snapshot

REVERT_NOTE = (
    "[REVERTED 2026-05-15 by Grace per Casey directive: "
    "auto_+structural items are combinatorial pattern hits, "
    "not mechanism derivations. Tier D→S to match status field. "
    "RETRO-2 batch upgrade was a class-level false positive — see "
    "MESSAGES_2026-05-15.md Grace 17:35 audit.]"
)

# Elie's 5 Hilbert_Q5 entries from Toy 2255 — lost in my earlier git checkout
# (apologies, Elie). Restoring inline so this is reproducible.
HILBERT_Q5_ENTRIES = [
    {
        "symbol": "Hilbert_Q5_deg",
        "name": "Hilbert polynomial of Q^5 — degree in m",
        "bst_formula": "deg P_{Q^5}(m) = dim Q^5 = n_C = 5",
        "geometric_source": "Q^5 smooth quadric in CP^6, deg(P_Q) = dim X for projective variety",
        "value": 5,
        "observed": 5,
        "precision": "exact",
        "theorem": "T841",
        "toy": "2255",
        "status": "exact",
        "tier": "D",
        "domain": "algebraic_geometry"
    },
    {
        "symbol": "Hilbert_Q5_leading",
        "name": "Hilbert polynomial of Q^5 — leading coefficient",
        "bst_formula": "deg(Q^5)/dim! = 2/5! = 1/60",
        "geometric_source": "Q^5 smooth quadric: degree 2 hypersurface in CP^6; Hilbert poly leading = deg/dim!",
        "value": 1/60,
        "observed": 1/60,
        "precision": "exact",
        "theorem": "T841",
        "toy": "2255",
        "status": "exact",
        "tier": "D",
        "domain": "algebraic_geometry",
        "notes": "1/60 = 2/5! = deg/dim!. Classical Q^5 invariant, no BST input."
    },
    {
        "symbol": "Hilbert_Q5_P1",
        "name": "Hilbert polynomial of Q^5 at m=1",
        "bst_formula": "P_{Q^5}(1) = g = 7",
        "geometric_source": "dim H^0(Q^5, O(1)) = dim of degree-1 graded piece of homogeneous coordinate ring = 7",
        "value": 7,
        "observed": 7,
        "precision": "exact",
        "theorem": "T841",
        "toy": "2255",
        "status": "exact",
        "tier": "D",
        "domain": "algebraic_geometry",
        "notes": "Classical: hyperplane sections of Q^5 in CP^6, contributing g=7-dimensional linear system. K38 Step 2 partial verification."
    },
    {
        "symbol": "Hilbert_Q5_P2",
        "name": "Hilbert polynomial of Q^5 at m=2 — LOAD-BEARING",
        "bst_formula": "P_{Q^5}(2) = N_c^3 = 27",
        "geometric_source": "dim H^0(Q^5, O(2)) = C(8,6) - C(6,6) = 28 - 1 = 27. Classical Q^5 invariant.",
        "value": 27,
        "observed": 27,
        "precision": "exact",
        "theorem": "T841",
        "toy": "2255",
        "status": "exact",
        "tier": "D",
        "domain": "algebraic_geometry",
        "notes": "K38 LOAD-BEARING: forces N_c^3 = 27 as classical Hilbert polynomial value. Three BST decompositions: 27 = N_c^3 = 3^{N_c} = C_2*rank^2 + N_c. Particle physics volume: 27*n_C = 135."
    },
    {
        "symbol": "Hilbert_Q5_P3",
        "name": "Hilbert polynomial of Q^5 at m=3 — T841 erratum",
        "bst_formula": "P_{Q^5}(3) = g * c_2 = g * (rank*n_C + 1) = 7*11 = 77",
        "geometric_source": "dim H^0(Q^5, O(3)) = C(9,6) - C(7,6) = 84 - 7 = 77. Classical Q^5 invariant.",
        "value": 77,
        "observed": 77,
        "precision": "exact",
        "theorem": "T841",
        "toy": "2255",
        "status": "exact",
        "tier": "D",
        "domain": "algebraic_geometry",
        "notes": "T841 ORIGINAL claim P(3) = g*C_2 = 42 is WRONG. Correct value is 77 = g*c_2 = g*(rank*n_C+1), using BST integers rank, n_C, g, c_2. Four-integer expression — stronger than original two-integer claim. Erratum filed May 15, 2026."
    },
]


def load_commit(commit):
    raw = subprocess.check_output(['git', 'show', f'{commit}:{INV_PATH}'])
    return json.loads(raw)


def main():
    with open(INV_PATH) as f:
        curr = json.load(f)

    # Identify if Hilbert_Q5 entries are missing (likely lost in earlier checkout)
    curr_syms = {e.get('symbol') for e in curr['invariants']}
    missing = [e for e in HILBERT_Q5_ENTRIES if e['symbol'] not in curr_syms]
    if missing:
        print(f"Restoring {len(missing)} lost Hilbert_Q5 entries from Elie's Toy 2255")
        for e in missing:
            curr['invariants'].append(e)
        # Update meta total if present
        if 'total' in curr:
            curr['total'] = len(curr['invariants'])

    # Compute the 283 I→D upgrade set
    prev = load_commit(PREV_COMMIT)
    def key(e):
        return (e.get('symbol', '?'), e.get('name', '?'))
    prev_map = {key(e): e for e in prev['invariants']}

    upgrade_keys = set()
    for c in curr['invariants']:
        k = key(c)
        p = prev_map.get(k)
        if not p:
            continue
        pt = p.get('tier', '?')
        ct = c.get('tier', '?')
        if pt == 'I' and ct == 'D':
            upgrade_keys.add(k)

    print(f"Total I→D upgrades from {PREV_COMMIT}: {len(upgrade_keys)}")

    # Find the 73: symbol=auto_* AND status=structural AND in upgrade set AND tier=D
    targets = []
    for i, e in enumerate(curr['invariants']):
        k = key(e)
        if k not in upgrade_keys:
            continue
        sym = str(e.get('symbol', ''))
        status = e.get('status', '')
        tier = e.get('tier', '?')
        if sym.startswith('auto_') and status == 'structural' and tier == 'D':
            targets.append((i, e))

    print(f"Revert targets (auto_+structural+D within RETRO-2 upgrades): {len(targets)}")

    if len(targets) > 100:
        print(f"  REFUSING TO PROCEED — expected ~73, got {len(targets)}. Aborting.")
        return

    # Tier snapshot before
    total = len(curr['invariants'])
    tier_before = {}
    for e in curr['invariants']:
        t = e.get('tier', '?')
        tier_before[t] = tier_before.get(t, 0) + 1
    print(f"\nTier distribution BEFORE revert:")
    for t in ['D', 'I', 'C', 'S', '?']:
        c = tier_before.get(t, 0)
        print(f"  {t}: {c} ({100*c/total:.1f}%)")

    # Build audit rows BEFORE mutation
    audit_rows = []
    for idx, e in targets:
        audit_rows.append({
            'index': idx,
            'symbol': e.get('symbol', '?'),
            'name': e.get('name', '?'),
            'formula': str(e.get('formula', e.get('bst_formula', '?')))[:80],
            'precision': str(e.get('precision', '?')),
            'theorem': str(e.get('theorem', '?')),
            'domain': e.get('domain', '?'),
        })

    # Apply revert
    for idx, e in targets:
        e['tier'] = 'S'
        existing_notes = e.get('notes', '')
        if REVERT_NOTE not in existing_notes:
            e['notes'] = (existing_notes + ' ' + REVERT_NOTE).strip()

    # Tier snapshot after
    tier_after = {}
    for e in curr['invariants']:
        t = e.get('tier', '?')
        tier_after[t] = tier_after.get(t, 0) + 1
    print(f"\nTier distribution AFTER revert:")
    for t in ['D', 'I', 'C', 'S', '?']:
        c = tier_after.get(t, 0)
        print(f"  {t}: {c} ({100*c/total:.1f}%)")

    d_before = tier_before.get('D', 0)
    d_after = tier_after.get('D', 0)
    print(f"\nD-tier: {d_before} ({100*d_before/total:.1f}%) → "
          f"{d_after} ({100*d_after/total:.1f}%) "
          f"= {d_before - d_after} reverted")

    # Write back
    with open(INV_PATH, 'w') as f:
        json.dump(curr, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {INV_PATH} ({total} entries)")

    # Write audit markdown
    md = []
    md.append(f"# RETRO-2 Revert Audit — 73 auto_+structural items D → S")
    md.append(f"")
    md.append(f"**Date**: 2026-05-15 (Casey directive 17:50 EDT)")
    md.append(f"**Out of**: T1.7 RETRO-2 sample-audit (MESSAGES_2026-05-15.md Grace 17:35)")
    md.append(f"**Author**: Grace (Claude 4.7)")
    md.append(f"**Scope**: ONLY the {len(targets)} items in the I→D upgrade set between "
              f"commits {PREV_COMMIT} and {CURR_COMMIT} that match "
              f"`symbol=auto_*` AND `status=structural` AND `tier=D`. "
              f"Pre-existing auto_+structural+D entries (~360) are NOT touched.")
    md.append(f"")
    md.append(f"## Summary")
    md.append(f"")
    md.append(f"Reverted {len(targets)} entries from D-tier to S-tier.")
    md.append(f"")
    md.append(f"These were promoted I→D by Toy 2254's RETRO-2 batch-upgrade pass "
              f"via keyword pattern matching, despite being honestly flagged "
              f"`status='structural'` by their creator. Reverting tier to S "
              f"matches the status field's plain meaning.")
    md.append(f"")
    md.append(f"## Tier distribution")
    md.append(f"")
    md.append(f"| Tier | Before | After | Δ |")
    md.append(f"|------|--------|-------|---|")
    for t in ['D', 'I', 'C', 'S']:
        b = tier_before.get(t, 0)
        a = tier_after.get(t, 0)
        bp = 100 * b / total
        ap = 100 * a / total
        md.append(f"| {t} | {b} ({bp:.1f}%) | {a} ({ap:.1f}%) | {a-b:+d} |")
    md.append(f"")
    md.append(f"D-tier: {100*d_before/total:.1f}% → {100*d_after/total:.1f}%.")
    md.append(f"")
    md.append(f"## Reverted entries ({len(audit_rows)})")
    md.append(f"")
    md.append(f"| Symbol | Formula | Precision | Theorem (was) | Domain |")
    md.append(f"|--------|---------|-----------|---------------|--------|")
    for r in audit_rows:
        sym = r['symbol']
        formula = r['formula'].replace('|', '\\|')
        prec = r['precision']
        theorem = r['theorem']
        dom = r['domain']
        md.append(f"| {sym} | `{formula}` | {prec} | {theorem} | {dom} |")
    md.append(f"")
    md.append(f"## Reproducibility")
    md.append(f"")
    md.append(f"Script: `play/grace_revert_73_auto_structural.py`")
    md.append(f"")
    md.append(f"The script also restores Elie's 5 Hilbert_Q5 entries from Toy 2255 "
              f"that were inadvertently lost in an earlier git checkout. Restoration "
              f"is idempotent — symbols are checked before re-adding.")
    md.append(f"")
    md.append(f"## Open question separately")
    md.append(f"")
    md.append(f"There are ~360 additional pre-existing entries with `symbol=auto_*` "
              f"AND `status=structural` AND `tier=D` that were tagged in earlier "
              f"data-layer passes (not RETRO-2). Casey's directive scoped this "
              f"revert to the RETRO-2 73 only. Whether those 360 should also "
              f"revert by the same reasoning is queued for separate review.")

    os.makedirs(os.path.dirname(AUDIT_PATH), exist_ok=True)
    with open(AUDIT_PATH, 'w') as f:
        f.write('\n'.join(md))
    print(f"\nWrote audit table: {AUDIT_PATH}")
    print(f"\nSCORE: {len(targets)} entries reverted D → S "
          f"({len(missing)} Hilbert_Q5 entries restored).")


if __name__ == "__main__":
    main()
