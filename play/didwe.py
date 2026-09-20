#!/usr/bin/env python3
"""
didwe — "did we do this before?"  Query the BST Approaches Register.
====================================================================
Reads notes/.running/approaches_register.jsonl (built by
play/keeper_approaches_register.py) and answers a topic query two ways:

  1. grep layer (always): every row where ALL query terms appear in any field
     (id, lane, title, approach, reason, evidence, file); ranked by term hits.
  2. --semantic: the top grep-scored rows (or a whole --lane) are handed to a
     local/remote model which names the nearest prior approaches BY ID and says
     in one line why each is the same ground or not. The model may only cite
     ids that are in the rows it was given (checked).

Every hit prints its outcome and source file: the file is the ruling, the row
is the pointer. Read the file before acting on a row.

Model-agnostic: same env/flags as the register builder (APPROACHES_API,
APPROACHES_ENDPOINT, APPROACHES_MODEL, APPROACHES_API_KEY).

Usage:
  python3 play/didwe.py "parity fold projector"
  python3 play/didwe.py "critical line dilation" --semantic
  python3 play/didwe.py --lane "RH" --outcome RETRACTED
  python3 play/didwe.py "Nyman Beurling" --any        # match ANY term instead of ALL
"""
import argparse, json, os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "notes", "BST_Approaches_Register.jsonl")
FIELDS = ["id", "lane", "rubric_cell", "title", "approach", "reason", "evidence", "file", "outcome", "keywords"]

def load():
    if not os.path.exists(REG):
        sys.exit(f"no register at {os.path.relpath(REG, ROOT)}; build it with play/keeper_approaches_register.py")
    with open(REG, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]

def score(row, terms, any_mode):
    blob = " ".join(str(row.get(k, "")) for k in FIELDS).lower()
    hits = [t for t in terms if t in blob]
    if any_mode:
        return len(hits)
    return len(hits) if len(hits) == len(terms) else 0

def fmt(r, width=110):
    flag = " ⚠VERIFY_FAIL" if r.get("verify") else ""
    unst = " UNSTABLE(" + r.get("outcome2", "") + ")" if r.get("unstable") else ""
    line1 = f"{r['id']:<10} {r['date']}  {r.get('coarse',''):<5} {r.get('outcome',''):<16}{unst}{flag}  [{r.get('rubric_cell','')} · {r.get('lane','')}]"
    line2 = f"    approach: {r.get('approach','')[:width]}"
    line3 = f"    reason:   {r.get('reason','')[:width]}"
    kw = f"    keywords: {', '.join(r['keywords'])}" if r.get("keywords") else None
    line4 = f"    file:     {r['file']}"
    am = f"    amends:   {', '.join(r['amends'])}" if r.get("amends") else None
    return "\n".join(x for x in (line1, line2, line3, kw, am, line4) if x)

def call_model(api, endpoint, model, key, system, user, timeout=180):
    msgs = [{"role": "system", "content": system}, {"role": "user", "content": user}]
    if api == "ollama":
        url = endpoint.rstrip("/") + "/api/chat"
        body = {"model": model, "stream": False, "think": False,
                "options": {"temperature": 0, "num_ctx": 16384}, "messages": msgs}
        hdr = {"Content-Type": "application/json"}
    else:
        url = endpoint.rstrip("/") + "/v1/chat/completions"
        body = {"model": model, "temperature": 0, "messages": msgs}
        hdr = {"Content-Type": "application/json"}
        if key: hdr["Authorization"] = "Bearer " + key
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=hdr)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        resp = json.load(r)
    c = resp["message"]["content"] if api == "ollama" else resp["choices"][0]["message"]["content"]
    c = re.sub(r"<think>.*?</think>", "", c, flags=re.S)
    if "</think>" in c: c = c.split("</think>")[-1]          # some models emit the close tag only
    return c.strip()

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?", default="")
    ap.add_argument("--lane", help="regex on the lane label")
    ap.add_argument("--outcome", help="filter, e.g. RETRACTED or CLOSED_NEGATIVE,PARKED")
    ap.add_argument("--any", action="store_true", help="match ANY term (default ALL)")
    ap.add_argument("--semantic", action="store_true")
    ap.add_argument("--top", type=int, default=40, help="rows handed to the model in --semantic")
    ap.add_argument("--api", default=os.environ.get("APPROACHES_API", "ollama"), choices=["ollama", "openai"])
    ap.add_argument("--endpoint", default=os.environ.get("APPROACHES_ENDPOINT", "http://localhost:11434"))
    ap.add_argument("--model", default=os.environ.get("APPROACHES_MODEL", "qwen3:30b-a3b"))
    ap.add_argument("--key", default=os.environ.get("APPROACHES_API_KEY", ""))
    args = ap.parse_args()
    rows = load()
    if args.lane:
        rows = [r for r in rows if re.search(args.lane, r.get("lane", ""), re.I)]
    if args.outcome:
        keep = set(args.outcome.split(","))
        rows = [r for r in rows if r.get("outcome") in keep]
    STOP = {"the","and","for","with","from","that","this","one","two","not","are","was","its","into","than","then","over","under","all","any","our","out","how","why","what","does","did","do","we","did","a","an","of","in","on","to","is","it","as","at","by","or","be"}
    terms = [t.lower() for t in re.findall(r"[\w\-–ζα-ω]+", args.query) if len(t) > 1 and t.lower() not in STOP]
    if not terms and args.query.strip():
        sys.exit("query has only stop-words; name the method/object (e.g. 'Nyman Beurling', 'parity fold')")
    scored = [(score(r, terms, args.any), r) for r in rows] if terms else [(1, r) for r in rows]
    hits = sorted([(s, r) for s, r in scored if s > 0], key=lambda x: (-x[0], x[1]["date"]))
    print(f"register: {len(load())} rows; after filters: {len(rows)}; hits: {len(hits)}  (query terms: {terms})\n")
    for _, r in hits[: args.top if args.semantic else 200]:
        print(fmt(r)); print()
    if not args.semantic or not hits:
        return
    given = hits[: args.top]
    table = "\n".join(f"{r['id']} | {r['date']} | {r.get('outcome','')} | {r.get('lane','')} | {r.get('approach','')} | {r.get('reason','')} | kw: {', '.join(r.get('keywords', []))}"
                      for _, r in given)
    system = ("You are checking whether a proposed research direction was already tried. You are given rows "
              "(id | date | outcome | lane | approach | reason) from a register of prior audits. Name the rows that cover the SAME "
              "ground as the query, closest first, and for each give one line: same ground / adjacent / fresh spin possible, and why. "
              "Cite ONLY ids from the rows given. If none cover it, say 'no prior row covers this'. Be terse.")
    out = call_model(args.api, args.endpoint, args.model, args.key, system, f"QUERY: {args.query}\n\nROWS:\n{table}")
    ids_given = {r["id"] for _, r in given}
    cited = set(re.findall(r"\b(K\d+(?:-[A-Z])?|§\d{3,4}|[A-Z]\d+(?:_[A-Za-z]?\d+)?)\b", out))
    bad = [c for c in cited if c not in ids_given and re.match(r"K\d+|§", c)]
    print("=" * 78 + "\nSEMANTIC PASS (model-drafted; verify each cited file before acting):\n" + out)
    if bad:
        print(f"\n⚠ model cited ids not in the rows it was given (ignore these): {sorted(bad)}")

if __name__ == "__main__":
    main()
