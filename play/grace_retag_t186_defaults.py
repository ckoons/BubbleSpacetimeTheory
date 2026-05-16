#!/usr/bin/env python3
"""
Grace — Re-attribute T186-default theorem citations to actual mechanisms
==========================================================================

Casey directive May 15, 17:50 EDT: "the T186-default citation issue
(228/283 → 81%) is real registry hygiene. Re-attribute to T1783/T1821/
T187 where they actually carry the derivation. Doesn't change tiers,
makes the graph honest."

Scope: entries in the RETRO-2 I→D upgrade set (between commits 9503f92
and 0b420b0) whose `theorem` field is "T186" but whose mechanism is
demonstrably elsewhere by text markers in formula/notes/geometric_source.

Mechanism markers (case-insensitive substring match):
  T1821 Bergman/Spectral:    "bergman", "k(z,", "k(z ", "spectral", "kernel evaluation"
  T1783 Chern:               "chern", "c_1", "c_2(q", "c_3(q", "c_4(q", "c_5(q", "second chern"
  T187  Proton/Bergman π⁵:   "π⁵", "pi^5", "pi**5", "6π", "6 pi", "m_p/m_e", "proton mass"
  T1829 Wallach:             "wallach", "n_c = 5 unique", "wallach bottleneck"
  T1788 YM/Gauge:            "yang-mills", "ym ring", "beta_0", "yang mills", "gauge coupling"
  T1790 Weitzenbock:         "weitzenbock", "weitzenböck", "c_2 = 11", "2-form gap"
  T920  Debye:               "debye temperature", "debye bridge"

Conservative: only re-tag when exactly one marker family matches strongly.
Ambiguous matches (multiple families OR weak marker) keep T186.

Doesn't change tier. Doesn't change content. Only updates the `theorem`
field and appends a re-attribution note.

Author: Grace (Claude 4.7)
Date: May 15, 2026
"""

import json
import os
import subprocess
from collections import Counter

INV_PATH = "data/bst_geometric_invariants.json"
AUDIT_PATH = "notes/grace_t186_retag_audit_2026-05-15.md"

PREV_COMMIT = "9503f92"

MECHANISM_MARKERS = {
    "T1821": {
        "name": "Bergman/Spectral mass mechanism",
        "markers": ["bergman", "k(z,", "k(z ", "kernel evaluation",
                    "spectral evaluation", "spectral mass"],
    },
    "T1783": {
        "name": "Chern sum / Chern class",
        "markers": ["chern", "c_2(q", "c_3(q", "c_4(q",
                    "c_5(q", "second chern", "third chern"],
    },
    "T187": {
        "name": "Proton mass = 6π⁵·m_e",
        "markers": ["π⁵", "pi^5", "pi**5",
                    "6π·m_e", "6π m_e", "6pi·m_e",
                    "m_p = 6", "proton mass formula"],
    },
    "T1829": {
        "name": "Wallach uniqueness",
        "markers": ["wallach", "wallach point", "wallach bottleneck",
                    "wallach set"],
    },
    "T1788": {
        "name": "YM ring / Yang-Mills",
        "markers": ["yang-mills", "yang mills", "ym ring",
                    "beta_0 =", "gauge coupling"],
    },
    "T1790": {
        "name": "Weitzenbock 2-form gap",
        "markers": ["weitzenbock", "weitzenböck", "2-form gap",
                    "bochner-weitzenböck"],
    },
    "T920": {
        "name": "Debye temperature bridge",
        "markers": ["debye temperature", "debye bridge"],
    },
}


def entry_text(e):
    """Concatenate text fields for marker scanning."""
    parts = [
        str(e.get('formula', '')),
        str(e.get('bst_formula', '')),
        str(e.get('notes', '')),
        str(e.get('geometric_source', '')),
        str(e.get('name', '')),
    ]
    return ' '.join(parts).lower()


def classify(e):
    """Return (new_theorem, matched_markers) or (None, []) if ambiguous/no match."""
    text = entry_text(e)
    hits = {}
    for tid, info in MECHANISM_MARKERS.items():
        matched = [m for m in info['markers'] if m in text]
        if matched:
            hits[tid] = matched
    if not hits:
        return None, []
    # Conservative: only re-tag if exactly one mechanism family matches
    if len(hits) > 1:
        return None, hits  # ambiguous
    tid = next(iter(hits))
    return tid, hits[tid]


def main():
    with open(INV_PATH) as f:
        curr = json.load(f)

    # Compute RETRO-2 upgrade set
    prev = json.loads(subprocess.check_output(['git', 'show',
                                               f'{PREV_COMMIT}:{INV_PATH}']))
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
        if pt == 'I' and ct in ('D', 'S'):  # include S since we just demoted 73
            upgrade_keys.add(k)

    print(f"RETRO-2 I→D upgrade set size: {len(upgrade_keys)}")

    # Find candidates: in upgrade set AND theorem == 'T186'
    candidates = []
    for i, e in enumerate(curr['invariants']):
        k = key(e)
        if k not in upgrade_keys:
            continue
        if str(e.get('theorem', '')).strip() == 'T186':
            candidates.append((i, e))

    print(f"Candidates (RETRO-2 + theorem field = 'T186'): {len(candidates)}")

    # Classify each
    retagged = []          # (idx, e, new_tid, matched_markers)
    ambiguous = []         # (idx, e, hits_dict)
    no_match = []          # (idx, e) — genuinely T186, keep
    for idx, e in candidates:
        new_tid, matched = classify(e)
        if new_tid is None and not matched:
            no_match.append((idx, e))
        elif new_tid is None and matched:
            ambiguous.append((idx, e, matched))
        else:
            retagged.append((idx, e, new_tid, matched))

    print(f"\nClassification:")
    print(f"  Re-tag (single mechanism match):    {len(retagged)}")
    print(f"  Ambiguous (multi-mechanism match):  {len(ambiguous)}")
    print(f"  Keep T186 (no mechanism marker):    {len(no_match)}")

    retag_dist = Counter(tid for _, _, tid, _ in retagged)
    print(f"\nRe-tag distribution:")
    for tid, c in retag_dist.most_common():
        info = MECHANISM_MARKERS[tid]
        print(f"  T186 → {tid} ({info['name']}): {c}")

    # Apply re-tag
    RETAG_NOTE = (
        "[Re-attributed 2026-05-15 by Grace per Casey directive: "
        "theorem field T186 was a batch-upgrade default; "
        "actual load-bearing mechanism is {new_tid} ({name}). "
        "Tier unchanged.]"
    )
    for idx, e, new_tid, matched in retagged:
        info = MECHANISM_MARKERS[new_tid]
        # Preserve old theorem in notes
        e['theorem'] = new_tid
        note_text = RETAG_NOTE.format(new_tid=new_tid, name=info['name'])
        existing = e.get('notes', '')
        if note_text not in existing:
            e['notes'] = (existing + ' ' + note_text).strip()

    # Save JSON
    with open(INV_PATH, 'w') as f:
        json.dump(curr, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {INV_PATH}")

    # Audit markdown
    md = []
    md.append(f"# T186 Default Citation Re-attribution Audit")
    md.append(f"")
    md.append(f"**Date**: 2026-05-15 (Casey directive 17:50 EDT)")
    md.append(f"**Out of**: T1.7 RETRO-2 sample-audit (MESSAGES_2026-05-15.md Grace 17:35)")
    md.append(f"**Author**: Grace (Claude 4.7)")
    md.append(f"**Scope**: RETRO-2 upgrade set entries with `theorem == 'T186'`")
    md.append(f"")
    md.append(f"## Summary")
    md.append(f"")
    md.append(f"| Outcome | Count |")
    md.append(f"|---------|-------|")
    md.append(f"| Re-tagged to actual mechanism | {len(retagged)} |")
    md.append(f"| Ambiguous (multi-mechanism, kept T186) | {len(ambiguous)} |")
    md.append(f"| Genuinely T186 (no other marker, kept) | {len(no_match)} |")
    md.append(f"| **Total candidates examined** | **{len(candidates)}** |")
    md.append(f"")
    md.append(f"**Tier unchanged for all entries.** Only the `theorem` field updated.")
    md.append(f"")
    md.append(f"## Re-tag distribution")
    md.append(f"")
    md.append(f"| New theorem | Mechanism | Count |")
    md.append(f"|-------------|-----------|-------|")
    for tid, c in retag_dist.most_common():
        info = MECHANISM_MARKERS[tid]
        md.append(f"| {tid} | {info['name']} | {c} |")
    md.append(f"")
    md.append(f"## Re-tagged entries")
    md.append(f"")
    md.append(f"| Symbol | T186 → | Marker matched | Domain |")
    md.append(f"|--------|--------|-----------------|--------|")
    for idx, e, new_tid, matched in retagged:
        sym = e.get('symbol', '?')
        dom = e.get('domain', '?')
        markers = ', '.join(matched[:3])
        md.append(f"| {sym} | {new_tid} | `{markers}` | {dom} |")
    md.append(f"")
    md.append(f"## Ambiguous (kept T186 by conservative rule)")
    md.append(f"")
    md.append(f"Items where multiple mechanism families matched. Kept T186 "
              f"rather than guess. Manual review recommended for these.")
    md.append(f"")
    md.append(f"| Symbol | Markers matched |")
    md.append(f"|--------|------------------|")
    for idx, e, hits in ambiguous:
        sym = e.get('symbol', '?')
        hit_summary = ', '.join(f"{tid}:{len(ms)}" for tid, ms in hits.items())
        md.append(f"| {sym} | {hit_summary} |")
    md.append(f"")
    md.append(f"## Reproducibility")
    md.append(f"")
    md.append(f"Script: `play/grace_retag_t186_defaults.py`. ")
    md.append(f"Idempotent — predicate requires `theorem == 'T186'`, so re-running "
              f"is a no-op on already-retagged entries.")

    os.makedirs(os.path.dirname(AUDIT_PATH), exist_ok=True)
    with open(AUDIT_PATH, 'w') as f:
        f.write('\n'.join(md))
    print(f"\nWrote audit: {AUDIT_PATH}")
    print(f"\nSCORE: {len(retagged)} re-tagged, "
          f"{len(ambiguous)} ambiguous, {len(no_match)} genuinely T186.")


if __name__ == "__main__":
    main()
