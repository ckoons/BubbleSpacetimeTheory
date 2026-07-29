#!/usr/bin/env python3
"""
verify_ac_graph.py — AC theorem-graph integrity verifier + content checksum.
Owner: Grace. Run this any session to confirm the graph is consistent and current.

Usage:
    python3 play/verify_ac_graph.py            # verify + report (read-only)
    python3 play/verify_ac_graph.py --stamp    # verify, then write checksum+counts+date into meta

What it checks (each an explicit PASS/FAIL):
  1. node tids unique
  2. every edge endpoint is an integer tid that exists in nodes (no dangling / no string ids)
  3. `theorems` is a faithful base-field projection of `nodes` (same tid set)
  4. meta + metadata count fields match the actual node/edge/theorem counts
  5. meta.max_tid == actual max node tid, and .next_theorem == max_tid + 1
  6. content CHECKSUM (sha256 over canonical-sorted node tids+names+status and edge triples)
     — recorded in meta.content_checksum so drift is detectable across sessions.
  7. last-dates-applied report (newest node date, meta.last_updated, per-month node counts)

The checksum is deliberately over CONTENT (nodes+edges), not the volatile meta log,
so re-stamping meta does not change the checksum unless the graph itself changed.
"""
import json, hashlib, sys, os
from collections import Counter

GRAPH = os.path.join(os.path.dirname(__file__), "ac_graph_data.json")
NEXT  = os.path.join(os.path.dirname(__file__), ".next_theorem")
BASE_FIELDS = ["tid","name","domain","status","depth","conflation","section","toys","date","plain","proofs"]

def content_checksum(nodes, edges):
    """Stable sha256 over the graph's actual content (order-independent)."""
    node_sig = sorted(f"{n.get('tid')}|{n.get('name')}|{n.get('status')}" for n in nodes)
    edge_sig = sorted(f"{e.get('from')}->{e.get('to')}:{e.get('source')}" for e in edges)
    h = hashlib.sha256()
    for s in node_sig: h.update(s.encode()); h.update(b"\n")
    h.update(b"===EDGES===\n")
    for s in edge_sig: h.update(s.encode()); h.update(b"\n")
    return h.hexdigest()

def verify(stamp=False):
    g = json.load(open(GRAPH))
    nodes = g.get("nodes", []); edges = g.get("edges", []); theorems = g.get("theorems", [])
    meta = g.get("meta", {}); metadata = g.get("metadata", {})
    results = []  # (name, ok, detail)

    node_tids = [n.get("tid") for n in nodes if isinstance(n, dict)]
    tid_set = set(node_tids)

    # 1. unique tids
    dups = [t for t,c in Counter(node_tids).items() if c > 1]
    results.append(("node tids unique", not dups, f"{len(dups)} duplicates" if dups else f"{len(node_tids)} unique"))

    # 2. edge endpoints
    dangling = [e for e in edges if isinstance(e, dict) and (e.get("from") not in tid_set or e.get("to") not in tid_set)]
    results.append(("edge endpoints valid (int tids, no dangling)", not dangling,
                    f"{len(dangling)} dangling: {[ (e.get('from'),e.get('to')) for e in dangling[:5] ]}" if dangling else f"{len(edges)} edges clean"))

    # 3. theorems projection of nodes
    th_tids = set(t.get("tid") for t in theorems if isinstance(t, dict))
    proj_ok = (th_tids == tid_set)
    results.append(("theorems == nodes tid-set", proj_ok,
                    f"theorems missing {len(tid_set-th_tids)}, extra {len(th_tids-tid_set)}" if not proj_ok else f"{len(theorems)} in sync"))

    # 4. count fields
    actual = {"nodes": len(nodes), "edges": len(edges), "theorems": len(theorems)}
    count_ok = (metadata.get("node_count")==actual["nodes"] and metadata.get("edge_count")==actual["edges"]
                and metadata.get("theorem_count")==actual["theorems"]
                and meta.get("node_count")==actual["nodes"] and meta.get("total_edges")==actual["edges"])
    results.append(("count fields match actual", count_ok,
                    f"actual nodes={actual['nodes']} edges={actual['edges']} theorems={actual['theorems']}; "
                    f"metadata={dict(metadata)}"))

    # 5. max_tid / next_theorem
    max_tid = max(tid_set)
    nxt = int(open(NEXT).read().strip()) if os.path.exists(NEXT) else None
    mt_ok = (meta.get("max_tid")==max_tid) and (nxt == max_tid+1 if nxt else True)
    results.append(("max_tid & .next_theorem consistent", mt_ok,
                    f"actual max_tid={max_tid}, meta.max_tid={meta.get('max_tid')}, .next_theorem={nxt}"))

    # 6. checksum
    chk = content_checksum(nodes, edges)
    recorded = meta.get("content_checksum")
    chk_ok = (recorded == chk)
    results.append(("content checksum matches recorded", chk_ok,
                    f"current={chk[:16]}… recorded={(recorded or '(none)')[:16]}…"))

    # 7. dates
    dates = [str(n.get("date")) for n in nodes if n.get("date")]
    months = Counter(d[:7] for d in dates if len(d)>=7 and d[0]=="2")
    newest = max(dates) if dates else "(none)"

    # ---- report ----
    print("="*72); print("AC THEOREM GRAPH — VERIFICATION"); print("="*72)
    allok = True
    for name, ok, detail in results:
        allok = allok and ok
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}")
    print("-"*72)
    print(f"  content checksum : {chk}")
    print(f"  newest node date : {newest}   | meta.last_updated: {meta.get('last_updated')}")
    print(f"  node dates by recent month: " + ", ".join(f"{m}:{months[m]}" for m in sorted(months)[-6:]))
    print(f"  totals: nodes={len(nodes)} edges={len(edges)} theorems={len(theorems)} max_tid={max_tid}")
    print("="*72)
    print(f"  RESULT: {'ALL PASS ✓' if allok else 'FAILURES PRESENT ✗ — run fixes then re-verify'}")
    print("="*72)

    if stamp:
        meta["content_checksum"] = chk
        meta["node_count"] = actual["nodes"]; meta["nodes"] = actual["nodes"]; meta["total_nodes"] = actual["nodes"]
        meta["edge_count"] = actual["edges"]; meta["edges"] = actual["edges"]; meta["total_edges"] = actual["edges"]
        meta["theorem_count"] = actual["theorems"]; meta["total_theorems"] = actual["theorems"]
        meta["max_tid"] = max_tid
        metadata["node_count"] = actual["nodes"]; metadata["edge_count"] = actual["edges"]; metadata["theorem_count"] = actual["theorems"]
        g["meta"] = meta; g["metadata"] = metadata
        json.dump(g, open(GRAPH,"w"), indent=1, ensure_ascii=False)
        print(f"  STAMPED: checksum + counts + max_tid written to meta/metadata.")
    return allok

if __name__ == "__main__":
    ok = verify(stamp="--stamp" in sys.argv)
    sys.exit(0 if ok else 1)
