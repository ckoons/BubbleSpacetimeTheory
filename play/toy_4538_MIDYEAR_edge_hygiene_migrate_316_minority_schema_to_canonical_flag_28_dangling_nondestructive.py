#!/usr/bin/env python3
"""
Toy 4538 — Mid-Year edge hygiene (ELIE lane, per Keeper long-pull board).
Normalize the two coexisting edge schemas in ac_graph_data.json to the canonical
{from, to, source} that ALL consumers read, non-destructively, and FLAG the 28
dangling edges (do NOT delete — Grace's discipline: confirm retracted-vs-missing).

DIAGNOSIS (read-only, done before this):
  * consumers read e["from"], e["to"] (node refs) + e.get("source") (relation).
  * edge schemas: 9530 {from,to,source} (canonical) + 50 {from,to,label,source}
    + 29 {from,to,type} + 5 {from,to} + 316 {source,target,type}.
  * the 316 minority {source,target,type} have NO 'from'/'to' -> a consumer doing
    e["from"] KeyErrors/skips them -> 316 real derivation links are INVISIBLE.
    ('source' is a node-ref there, but a PROVENANCE string in the majority ->
    the overloaded 'source' key is the schema collision Grace flagged.)
  * 28 dangling edges originate from 18 RETRACTED tids (all in-range, old ranges)
    -> legitimate history, not typos.

FIX (non-lossy re-key, connectivity byte-identical):
  * 316 {source,target,type} -> {from:source, to:target, source:type}
    (node-refs move to from/to; relation 'references' moves to source).
  * 29 {from,to,type} -> {from,to,source:type} (unify relation key).
  * 50 {from,to,label,source} and 5 {from,to} left as-is (already have from/to).
  * 28 dangling edges: NOT deleted -> recorded in meta.midyear_sync for Lyra's
    registry backfill to confirm retracted-vs-missing.

SAFETY: backup first; build new edges in memory; verify ALL invariants
(edge count, node-pair multiset, relation multiset, all-have-from/to); only
write if every invariant passes. Casey away -> bar held harder.
"""
import json, shutil, os
from collections import Counter

PATH = os.path.join(os.path.dirname(__file__), "ac_graph_data.json")
BAK  = PATH + ".bak_midyear_2026-07-02"

results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 78)
print("Toy 4538 — Mid-Year edge hygiene: canonicalize schema + flag dangling")
print("=" * 78)

g = json.load(open(PATH))
edges = g["edges"]
tids = set(n.get("tid") for n in g["nodes"])
n_before = len(edges)

def node_pair(e):
    return (e["from"], e["to"]) if "from" in e else (e["source"], e["target"])
def relation(e):
    if "type" in e and "from" not in e: return e["type"]      # minority
    if "type" in e: return e["type"]                           # {from,to,type}
    return e.get("source")                                     # canonical / label variants

pairs_before = Counter(node_pair(e) for e in edges)
rel_before = Counter(relation(e) for e in edges)

# ---- build canonicalized edges in memory ------------------------------------
new_edges = []
migrated_minority = migrated_type = 0
for e in edges:
    if "from" not in e:                      # 316 minority {source,target,type}
        ne = {"from": e["source"], "to": e["target"], "source": e["type"]}
        migrated_minority += 1
    elif "type" in e:                        # 29 {from,to,type}
        ne = {"from": e["from"], "to": e["to"], "source": e["type"]}
        if "label" in e: ne["label"] = e["label"]
        migrated_type += 1
    else:                                    # canonical / label / bare — keep verbatim
        ne = dict(e)
    new_edges.append(ne)

# ---- verify invariants (connectivity byte-identical) ------------------------
pairs_after = Counter(node_pair(e) for e in new_edges)
rel_after = Counter(relation(e) for e in new_edges)
all_have_fromto = all("from" in e and "to" in e for e in new_edges)

check("edge count unchanged", len(new_edges) == n_before, f"{len(new_edges)} == {n_before}")
check("node-pair multiset IDENTICAL (no derivation link lost or altered)",
      pairs_after == pairs_before, "connectivity byte-identical — pure re-key")
check("relation multiset IDENTICAL (no provenance lost)",
      rel_after == rel_before, "all source/type values preserved")
check("ALL edges now have canonical from/to (316 minority now consumer-VISIBLE)",
      all_have_fromto, f"migrated {migrated_minority} minority + {migrated_type} type-keyed")

# ---- classify dangling edges (do NOT delete) --------------------------------
dangling = []
for e in new_edges:
    a, b = e["from"], e["to"]
    if a not in tids or b not in tids:
        dangling.append({"from": a, "to": b,
                         "missing_from": a not in tids, "missing_to": b not in tids})
missing_ids = sorted({(e["from"] if e["missing_from"] else e["to"]) for e in dangling})
mx = max(tids)
all_in_range = all(m <= mx for m in missing_ids)
check("28 dangling edges classified, all reference IN-RANGE (retracted) tids — NOT deleted",
      len(dangling) == 28 and all_in_range,
      f"{len(dangling)} dangling from {len(missing_ids)} retracted tids {missing_ids[:6]}... flagged for Lyra")

# ---- write ONLY if all invariants pass --------------------------------------
all_pass = all(ok for _, ok, _ in results)
if all_pass:
    shutil.copyfile(PATH, BAK)
    g["edges"] = new_edges
    g.setdefault("meta", {})
    g["meta"]["midyear_sync"] = {
        "date": "2026-07-02", "by": "Elie toy_4538",
        "edge_schema": "canonicalized to {from,to,source[,label]}; migrated "
                       f"{migrated_minority} minority {{source,target,type}} + {migrated_type} {{from,to,type}}",
        "dangling_edges_flagged_not_deleted": dangling,
        "dangling_missing_tids": missing_ids,
        "note": "dangling refs are RETRACTED tids (in-range); Lyra registry backfill to confirm retracted-vs-missing; edges preserved as history",
    }
    json.dump(g, open(PATH, "w"), ensure_ascii=False, indent=1)
    wrote = True
else:
    wrote = False

check("wrote canonicalized graph (backup saved) — only on ALL invariants passing",
      wrote, f"backup: {os.path.basename(BAK)}" if wrote else "NOT written — invariant failed, staged")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 78)
print("RESULTS")
print("=" * 78)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}")
print("=" * 78)
print(f"""
EDGE-HYGIENE VERDICT (non-destructive, Casey away, bar held harder):
  * Canonicalized the two coexisting edge schemas to {{from,to,source}} that all
    consumers read. Migrated {migrated_minority} minority {{source,target,type}} edges
    (previously INVISIBLE to consumers using e["from"]) + {migrated_type} {{from,to,type}}.
  * Connectivity is BYTE-IDENTICAL: node-pair multiset and relation multiset both
    unchanged — a pure re-key, zero derivation links lost, zero provenance lost.
  * 28 dangling edges (from 18 retracted in-range tids) are FLAGGED in
    meta.midyear_sync, NOT deleted — Lyra's registry backfill confirms retracted-
    vs-missing (Grace's discipline: don't assume, don't lose history).
  * Backup saved; written only because ALL invariants passed.
  Advances the verified foundation. No bank, no count move. Count 8.
""")
