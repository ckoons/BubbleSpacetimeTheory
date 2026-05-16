#!/usr/bin/env python3
"""
Grace — Option A wholesale revert on 360 auto_+structural+D ≥2% band
=====================================================================

Casey directive 23:35 EDT, May 15, 2026.

Predicate (precise):
  symbol.startswith('auto_')
  AND status == 'structural'
  AND tier == 'D'
  AND precision >= 2%  (or precision='structural' which exceeds 2% by convention)
  AND NOT in the 73 RETRO-2 set (those already reverted today via grace_revert_73...)

Exclude (flag for individual review):
  - Items with `toy` field populated (existing mechanism toy reference)
  - Items with `theorem` field != 'T186' (non-default mechanism citation)

Action:
  - tier D → S
  - Append revert note
  - Save audit table
  - Save excluded set for individual review

Author: Grace (Claude 4.7)
Date: May 15, 2026
"""

import json
import os
import subprocess

INV_PATH = "data/bst_geometric_invariants.json"
AUDIT_PATH = "notes/grace_revert_360_option_A_2026-05-15.md"

REVERT_NOTE = (
    "[REVERTED 2026-05-15 by Grace per Casey Option A directive: "
    "auto_*+status=structural items with precision >=2% sit in S-tier "
    "territory by team convention (S-tier = >2% or qualitative). "
    "Tier D→S. Headline now reflects honest baseline. Real mechanisms "
    "in this set can be salvaged in SP-25 May 29 sweep.]"
)


def precision_value(prec):
    """Parse precision; return numeric % (99 if 'structural'/unparseable)."""
    p = str(prec).strip()
    if 'structural' in p.lower() or 'qualitative' in p.lower() or 'universal' in p.lower():
        return 99.0  # treat structural as exceeds 2%
    p = p.replace('%','').replace('~','').replace('<','').replace('exact','0.01').replace('sigma','').replace('σ','').strip()
    try:
        return float(p)
    except ValueError:
        return 99.0


def main():
    # Compute the 73 RETRO-2 set first (so we exclude them — already done)
    PREV_COMMIT = "9503f92"
    prev = json.loads(subprocess.check_output(['git', 'show', f'{PREV_COMMIT}:{INV_PATH}']))
    def key(e):
        return (e.get('symbol', '?'), e.get('name', '?'))
    prev_map = {key(e): e for e in prev['invariants']}
    retro2_upgrade_keys = set()
    for c in json.load(open(INV_PATH))['invariants']:
        k = key(c)
        p = prev_map.get(k)
        if p and p.get('tier','?')=='I' and c.get('tier','?') in ('D','S'):
            retro2_upgrade_keys.add(k)
    print(f"RETRO-2 upgrade set: {len(retro2_upgrade_keys)} (excluded — already handled)")

    with open(INV_PATH) as f:
        inv = json.load(f)

    # Find Option A target set
    targets = []
    excluded_toy = []
    excluded_theorem = []
    for i, e in enumerate(inv['invariants']):
        sym = str(e.get('symbol', ''))
        status = e.get('status', '')
        tier = e.get('tier', '?')
        if not sym.startswith('auto_'): continue
        if status != 'structural': continue
        if tier != 'D': continue
        k = key(e)
        if k in retro2_upgrade_keys: continue  # already reverted today

        prec = precision_value(e.get('precision', ''))
        if prec < 2.0: continue  # sub-2% items kept for individual review

        # Exclusion check: non-default theorem field OR existing toy reference
        theorem = str(e.get('theorem', '')).strip()
        toy = str(e.get('toy', '')).strip()
        if theorem and theorem != 'T186' and theorem != '?' and theorem != '':
            excluded_theorem.append((i, e))
            continue
        if toy and toy not in ('?', 'None', ''):
            excluded_toy.append((i, e))
            continue

        targets.append((i, e))

    print(f"\nOption A target set (eligible for revert): {len(targets)}")
    print(f"  Excluded (non-T186 theorem field): {len(excluded_theorem)}")
    print(f"  Excluded (existing toy reference):  {len(excluded_toy)}")

    # Tier snapshot before
    total = len(inv['invariants'])
    tier_before = {}
    for e in inv['invariants']:
        tier_before[e.get('tier','?')] = tier_before.get(e.get('tier','?'), 0) + 1
    print(f"\nTier dist BEFORE: D={tier_before.get('D',0)} ({100*tier_before.get('D',0)/total:.1f}%), "
          f"I={tier_before.get('I',0)}, C={tier_before.get('C',0)}, S={tier_before.get('S',0)}")

    # Build audit table BEFORE mutation
    audit_rows = []
    for idx, e in targets:
        audit_rows.append({
            'symbol': e.get('symbol', '?'),
            'name': str(e.get('name', '?'))[:50],
            'formula': str(e.get('formula', e.get('bst_formula', '?')))[:60],
            'precision': str(e.get('precision', '?')),
            'theorem': str(e.get('theorem', '?')),
            'domain': e.get('domain', '?'),
        })

    excluded_rows = []
    for idx, e in excluded_theorem + excluded_toy:
        reason = 'non-T186 theorem' if (idx, e) in excluded_theorem else 'has toy ref'
        excluded_rows.append({
            'symbol': e.get('symbol','?'),
            'theorem': str(e.get('theorem','?')),
            'toy': str(e.get('toy','?')),
            'reason': reason,
        })

    # Safety check
    if len(targets) > 400:
        print(f"REFUSING: {len(targets)} targets exceeds safety limit 400. Aborting.")
        return

    # Apply revert
    for idx, e in targets:
        e['tier'] = 'S'
        existing = e.get('notes', '')
        if REVERT_NOTE not in existing:
            e['notes'] = (existing + ' ' + REVERT_NOTE).strip()

    # Tier snapshot after
    tier_after = {}
    for e in inv['invariants']:
        tier_after[e.get('tier','?')] = tier_after.get(e.get('tier','?'), 0) + 1
    print(f"\nTier dist AFTER:  D={tier_after.get('D',0)} ({100*tier_after.get('D',0)/total:.1f}%), "
          f"I={tier_after.get('I',0)}, C={tier_after.get('C',0)}, S={tier_after.get('S',0)}")

    d_before = tier_before.get('D', 0)
    d_after = tier_after.get('D', 0)
    print(f"\nD-tier: {d_before} ({100*d_before/total:.1f}%) → {d_after} ({100*d_after/total:.1f}%) "
          f"= {d_before - d_after} reverted")

    # Write back
    with open(INV_PATH, 'w') as f:
        json.dump(inv, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {INV_PATH}")

    # Audit markdown
    md = []
    md.append(f"# Option A Wholesale Revert — 360 auto_+structural ≥2% band")
    md.append(f"")
    md.append(f"**Date**: 2026-05-15 (Casey Option A approval 23:35 EDT)")
    md.append(f"**Out of**: T1.7 RETRO-2 audit + 360 sample audit follow-up")
    md.append(f"**Predicate**: auto_*+status=structural+D-tier+precision≥2%, NOT in RETRO-2 set")
    md.append(f"**Excluded**: non-T186 theorem field OR existing toy reference (potential real mechanisms)")
    md.append(f"")
    md.append(f"## Summary")
    md.append(f"")
    md.append(f"Reverted **{len(targets)}** entries from D-tier to S-tier.")
    md.append(f"Excluded **{len(excluded_theorem)+len(excluded_toy)}** entries for individual review")
    md.append(f"({len(excluded_theorem)} non-T186 theorem + {len(excluded_toy)} existing toy refs).")
    md.append(f"")
    md.append(f"## Tier distribution")
    md.append(f"")
    md.append(f"| Tier | Before | After | Δ |")
    md.append(f"|------|--------|-------|---|")
    for t in ['D', 'I', 'C', 'S']:
        b = tier_before.get(t, 0)
        a = tier_after.get(t, 0)
        bp = 100*b/total; ap = 100*a/total
        md.append(f"| {t} | {b} ({bp:.1f}%) | {a} ({ap:.1f}%) | {a-b:+d} |")
    md.append(f"")
    md.append(f"D-tier: {100*d_before/total:.1f}% → {100*d_after/total:.1f}%.")
    md.append(f"")
    md.append(f"## Excluded for individual review ({len(excluded_rows)})")
    md.append(f"")
    md.append(f"| Symbol | Theorem | Toy | Reason |")
    md.append(f"|--------|---------|-----|--------|")
    for r in excluded_rows[:40]:
        md.append(f"| {r['symbol']} | {r['theorem']} | {r['toy']} | {r['reason']} |")
    if len(excluded_rows) > 40:
        md.append(f"| ... | ... | ... | (+{len(excluded_rows)-40} more) |")
    md.append(f"")
    md.append(f"## First 50 reverted entries (full list in JSON)")
    md.append(f"")
    md.append(f"| Symbol | Formula | Precision | Domain |")
    md.append(f"|--------|---------|-----------|--------|")
    for r in audit_rows[:50]:
        sym = r['symbol']
        f = r['formula'].replace('|', '\\|')
        md.append(f"| {sym} | `{f}` | {r['precision']} | {r['domain']} |")
    if len(audit_rows) > 50:
        md.append(f"| ... | ... | ... | (+{len(audit_rows)-50} more, full list in commit diff) |")
    md.append(f"")
    md.append(f"## Reproducibility")
    md.append(f"")
    md.append(f"Script: `play/grace_revert_360_option_A.py`")
    md.append(f"Idempotent: predicate requires tier=D, re-running is no-op.")

    os.makedirs(os.path.dirname(AUDIT_PATH), exist_ok=True)
    with open(AUDIT_PATH, 'w') as f:
        f.write('\n'.join(md))
    print(f"\nWrote audit: {AUDIT_PATH}")
    print(f"\nSCORE: {len(targets)} reverted D→S, {len(excluded_rows)} excluded for review")


if __name__ == "__main__":
    main()
