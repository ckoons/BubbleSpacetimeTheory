#!/usr/bin/env python3
"""
lexicon.py — the Casey ↔ corpus concept index (Keeper, 2026-10-09; design: Casey).

A document store with a multikey alias index, on disk as JSONL, POINTERS ONLY.
It grows organically from communication misses: every time a phrase of Casey's
made a CI ask "which / what?", the phrase becomes an alias of the concept it
turned out to mean, with pointers into the corpus and a hash per anchor.

  python3 play/lexicon.py "<message text>"          # look up every alias in the text (≤ 5 lines)
  python3 play/lexicon.py --add                      # append a document interactively (JSON on stdin)
  python3 play/lexicon.py --check                    # hash-check every anchor; print STALE ones
  python3 play/lexicon.py --control                  # positive control: Wednesday 10-07's misses must all hit

It POINTS, it does not RULE: a hit means "read this first", never "this is settled".
"""
import sys, json, re, hashlib, os, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DB = os.path.join(HERE, "casey_lexicon.jsonl")
BUDGET = 5

SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-")

def norm(s):
    s = unicodedata.normalize("NFKD", s).translate(SUP).lower()
    s = re.sub(r"[^a-z0-9\s/^*-]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def load():
    docs = []
    if os.path.exists(DB):
        for line in open(DB, encoding="utf-8"):
            line = line.strip()
            if line:
                docs.append(json.loads(line))
    index = {}
    for d in docs:
        for a in d.get("aliases", []):
            index.setdefault(norm(a), []).append(d["id"])
    return docs, index

def sha_of(path):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        return None
    return hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]

def anchor_state(a):
    s = sha_of(a["file"])
    if s is None:
        return "MISSING"
    return "OK" if s == a.get("sha") else "STALE"

def lookup(text, docs, index):
    t = " " + norm(text) + " "
    hits = {}
    for key, ids in index.items():
        if (" " + key + " ") in t or (len(key) >= 12 and key in t):
            for i in ids:
                hits[i] = max(hits.get(i, 0), len(key))
    byid = {d["id"]: d for d in docs}
    ranked = sorted(hits, key=lambda i: -hits[i])
    return [byid[i] for i in ranked]

def fmt(d):
    anchors = " ".join(f"{a['file'].split('/')[-1][:38]}[{anchor_state(a)}]" for a in d["anchors"][:3])
    return f"{d['id']:<22} {d['status'][:70]:<70} → {anchors}"

def main(argv):
    docs, index = load()
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__); return 0
    if argv[0] == "--add":
        d = json.load(sys.stdin)
        for k in ("id", "aliases", "anchors", "status", "meant", "read_as"):
            assert k in d, f"missing {k}"
        for a in d["anchors"]:
            a["sha"] = sha_of(a["file"])
        with open(DB, "a", encoding="utf-8") as f:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
        print("added", d["id"]); return 0
    if argv[0] == "--check":
        bad = 0
        for d in docs:
            for a in d["anchors"]:
                st = anchor_state(a)
                if st != "OK":
                    bad += 1; print(f"{st:<8} {d['id']:<22} {a['file']}")
        print(f"{len(docs)} documents, {sum(len(d['anchors']) for d in docs)} anchors, {bad} not OK")
        return 1 if bad else 0
    if argv[0] == "--control":
        probes = ["BST is unique in that the theory claims a central role for observation",
                  "Relativity does not matter at the tiniest scales in bst",
                  "the rainbow of information in a non-moving photon",
                  "electrons are 2D",
                  "at 10^-122 scale we only see the next position as a cloud of possibilities",
                  "writing the 'next' natural number",
                  "the fourth face is a 'timeless' checksum",
                  "the interior of D_IV^5 is discrete composed of rationals",
                  "protons, baryons and other particles sit on the exterior",
                  "the electron and proton read the same Shilove circle from different sides",
                  "the hydrogen atom shells are the first/best expression of alpha",
                  "Plank is the boundary ruller",
                  "I said the tick is 10^-120"]
        miss = 0
        for p in probes:
            h = lookup(p, docs, index)
            print(("HIT " if h else "MISS") + f"  {p[:60]:<60} → {', '.join(d['id'] for d in h[:3])}")
            miss += not h
        print(f"CONTROL: {len(probes)-miss}/{len(probes)} hit"); return 1 if miss else 0
    text = " ".join(argv)
    hits = lookup(text, docs, index)
    if not hits:
        print("lexicon: no prior ground for this phrasing (add the miss with --add once resolved)"); return 0
    print(f"lexicon: prior ground ({min(len(hits), BUDGET)} of {len(hits)}) — POINTS, does not rule")
    for d in hits[:BUDGET]:
        print("  " + fmt(d))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
