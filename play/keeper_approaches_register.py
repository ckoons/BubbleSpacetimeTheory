#!/usr/bin/env python3
"""
Keeper Approaches Register — "did we do this before?"  (pilot 2026-09-19)
=========================================================================
Builds notes/BST_Approaches_Register.md (+ a JSONL sidecar) from the corpus:
one row per audit / ruling / note, recording the APPROACH examined, its
OUTCOME, the ruling id, the date, a one-line reason, and a VERBATIM evidence
phrase — with the source file on every row so any row can be checked.

Why an instrument and not a hand-kept list: the June K-audit registry stopped
at K290 and went stale silently. This one is DERIVED from the files that ruled,
and the SOD checker can flag any ruling without a row.

Two layers:
  deterministic  — id, author, date, file, title, verdict tokens (regex; no model)
  model-drafted  — lane, approach, outcome, reason, amends, evidence (local LLM)

Model-drafted fields are DRAFTS until verified. Built-in verification:
  * `evidence` must occur verbatim in the source text (hallucination guard;
    a row failing this is marked VERIFY_FAIL and its outcome is not trusted).
  * outcome must be from the fixed vocabulary.
  * --controls FILE: expected (id, outcome) pairs; mismatches reported.

Model-agnostic: --api ollama (default, http://localhost:11434) or
--api openai (any OpenAI-compatible /v1/chat/completions, incl. routers).
Env: APPROACHES_API, APPROACHES_ENDPOINT, APPROACHES_MODEL, APPROACHES_API_KEY.

Usage:
  python3 play/keeper_approaches_register.py --selftest
  python3 play/keeper_approaches_register.py --lane-filter <RH regex> --controls play/keeper_approaches_controls_RH.tsv
  python3 play/keeper_approaches_register.py --lane-filter 'RH|Riemann|zeta' --limit 5 --dry-run
  python3 play/keeper_approaches_register.py --lane-filter 'RH|Riemann|zeta|critical.line|T1299|T1448|Eisenstein|harvest|dilation'
  python3 play/keeper_approaches_register.py            # full corpus (cached; only changed files hit the model)

Cache: notes/.running/approaches_register_cache.jsonl keyed by file sha256,
so the nightly run costs only the new/changed files.
"""
import argparse, glob, hashlib, json, os, re, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES = os.path.join(ROOT, "notes")
CACHE = os.path.join(NOTES, ".running", "approaches_register_cache.jsonl")
OUT_MD = os.path.join(NOTES, "BST_Approaches_Register.md")
OUT_JSONL = os.path.join(NOTES, "BST_Approaches_Register.jsonl")   # versioned sidecar read by play/didwe.py

DEFAULT_SOURCES = ["notes/Keeper_K*.md", "notes/cal_*.md", "notes/Cal_*.md", "notes/Lyra_*.md"]
OUTCOMES = ["CLOSED_POSITIVE", "CLOSED_NEGATIVE", "CONDITIONAL", "RETRACTED",
            "WITHDRAWN", "PARKED", "OPEN", "AMENDMENT"]
COARSE = {"CLOSED_NEGATIVE": "STOP", "RETRACTED": "STOP", "WITHDRAWN": "STOP",
          "CLOSED_POSITIVE": "DONE", "AMENDMENT": "AMEND"}          # everything else → LIVE
# Fixed lane vocabulary = the rubric scorecard (notes/BST_Completeness_Rubric_and_Roadmap.md Section 2) + one process cell.
RUBRIC = ["E1 Postulates", "E2 Derive QM", "E3 Derive SM params", "E4 Recover GR / spacetime", "E5 New predictions",
          "IA Forced object", "IB Everything a reading", "IC Commitment ontology", "ID Forced, not fitted",
          "IE Complete & falsifiable (Millennium / math-complete)", "R1 Red-team", "R2 Outreach packet",
          "P0 Process / hygiene / ledger (no science claim)"]
def coarse(o): return COARSE.get(o, "LIVE")
VERDICT_TOKENS = ["CONDITIONAL PASS", "PASS", "FAIL", "RETRACTED", "RETIRED", "WITHDRAWN",
                  "PARKED", "CLEAN NEGATIVE", "SEALED NEGATIVE", "STOP", "CLOSED", "OPEN",
                  "CERTIFIED", "REFUTED"]
SCHEMA = "v2"            # bump when the record fields change; old cache rows are then re-extracted
HEAD_LINES = 60          # lines from the top of the file the model sees
TAIL_LINES = 15          # ...plus the closing lines, where the ruling sentence often sits
HEAD_CHARS = 7000        # hard cap on characters sent

SYSTEM = (
 "You extract ONE record from a research audit or note in a physics/mathematics program. "
 "Reply ONLY with a JSON object with exactly these keys:\n"
 '"rubric_cell": EXACTLY one string from this list — ' + json.dumps(RUBRIC) + ';\n'
 '"lane": short sub-topic label (2-5 words, e.g. "RH / critical line", "CKM mixing", "A9 dipole test");\n'
 '"approach": one sentence: the specific approach, method, or claim that was examined;\n'
 '"outcome": one of CLOSED_POSITIVE (proved/passed/certified), CLOSED_NEGATIVE (refuted/clean negative/fails as a class), '
 "CONDITIONAL (conditional pass, gap named), RETRACTED (a prior claim withdrawn as wrong), WITHDRAWN (author pulled it), "
 "PARKED (set aside, not wrong), OPEN (still undecided), AMENDMENT (this note mainly corrects an earlier audit);\n"
 '"reason": one sentence giving the deciding reason;\n'
 '"amends": list of earlier audit ids this note corrects (e.g. ["K1808"]), empty list if none;\n'
 '"keywords": list of 3-10 NAMED methods, criteria, objects, theorems or ids the text uses or examines, each spelled as the text spells it '
 '(e.g. "Nyman-Beurling criterion", "Epstein zeta", "Selberg trace formula", "T1299", "Weil positivity"); these are the aliases a later search must hit;\n'
 '"evidence": a short phrase copied VERBATIM from the text (5-20 words) that supports the outcome. Copy exactly; do not paraphrase.\n'
 "Prefer the document's own verdict words. If the text is only a plan or a question with no ruling, outcome is OPEN."
)

SYSTEM2 = (
 "A colleague will read this research note. Using ONLY the document's own verdict sentences, answer with JSON "
 '{"outcome": one of ' + "|".join(OUTCOMES) + ', "why": one short sentence quoting the verdict words}. '
 "CLOSED_POSITIVE = proved/passed/certified; CLOSED_NEGATIVE = refuted/clean negative; CONDITIONAL = conditional pass; "
 "RETRACTED = a prior claim withdrawn as wrong; WITHDRAWN = author pulled it; PARKED = set aside; OPEN = undecided; "
 "AMENDMENT = mainly corrects an earlier audit. If several apply, choose the one the document's FINAL status sentence carries."
)

# ---------------------------------------------------------------- deterministic layer
def file_id(path, head):
    base = os.path.basename(path)
    m = re.match(r"Keeper_(K\d+(?:-[A-Z])?)(?:_(K\d+))?", base)
    if m:
        return (m.group(1) + ("+" + m.group(2) if m.group(2) else "")), "Keeper"
    m = re.match(r"[cC]al_(R\d+_C\d+|\S+?)_", base)
    if m:
        s = re.search(r"§(\d{3,4})", head)
        return (("§" + s.group(1)) if s else "cal:" + m.group(1)), "Cal"
    m = re.match(r"Lyra_([A-Z]\d+(?:_[A-Za-z]?\d+)?)", base)
    if m:
        return m.group(1), "Lyra"
    return base[:40], "?"

def file_date(path, head):
    m = re.search(r"(20\d\d-\d\d-\d\d)", os.path.basename(path))
    if m: return m.group(1)
    m = re.search(r'^date:\s*"?(20\d\d-\d\d-\d\d)', head, re.M)
    if m: return m.group(1)
    m = re.search(r"(20\d\d-\d\d-\d\d)", head)
    return m.group(1) if m else time.strftime("%Y-%m-%d", time.localtime(os.path.getmtime(path)))

def file_title(head):
    m = re.search(r"^#\s+(.+)$", head, re.M)
    if m: return m.group(1).strip()
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', head, re.M)
    return m.group(1).strip() if m else "(no title)"

def verdict_tokens(text):
    found = []
    for t in VERDICT_TOKENS:
        if re.search(r"\b" + re.escape(t) + r"\b", text) and t not in found:
            if t == "PASS" and "CONDITIONAL PASS" in found: continue
            found.append(t)
    return found

def read_head(path):
    """Top HEAD_LINES plus the last TAIL_LINES (verdicts sit at both ends); capped at HEAD_CHARS."""
    with open(path, encoding="utf-8", errors="replace") as f:
        lines = [l.rstrip("\n") for l in f]
    if len(lines) <= HEAD_LINES + TAIL_LINES:
        return "\n".join(lines)[:HEAD_CHARS]
    head = "\n".join(lines[:HEAD_LINES])[:HEAD_CHARS - 1500]
    tail = "\n".join(lines[-TAIL_LINES:])[-1500:]
    return head + "\n[...]\n" + tail

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f: h.update(f.read())
    return h.hexdigest()

# ---------------------------------------------------------------- model layer
def call_model(api, endpoint, model, key, text, timeout=180, system=None):
    msgs = [{"role": "system", "content": system or SYSTEM}, {"role": "user", "content": text}]
    if api == "ollama":
        url = endpoint.rstrip("/") + "/api/chat"
        body = {"model": model, "stream": False, "think": False, "format": "json",
                "options": {"temperature": 0, "num_ctx": 8192}, "messages": msgs}
        hdr = {"Content-Type": "application/json"}
    else:
        url = endpoint.rstrip("/") + "/v1/chat/completions"
        body = {"model": model, "temperature": 0, "messages": msgs,
                "response_format": {"type": "json_object"}}
        hdr = {"Content-Type": "application/json"}
        if key: hdr["Authorization"] = "Bearer " + key
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=hdr)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        resp = json.load(r)
    content = resp["message"]["content"] if api == "ollama" else resp["choices"][0]["message"]["content"]
    content = re.sub(r"<think>.*?</think>", "", content, flags=re.S).strip()
    return json.loads(content)

def normalize_ws(s):
    """Formatting-only normalization: markdown emphasis, code ticks, typographic quotes/dashes, whitespace, case.
    Word content is untouched, so a paraphrase still fails the verbatim check."""
    for a, b in (("**", ""), ("*", ""), ("`", ""), ("\u201c", '"'), ("\u201d", '"'), ("\u2018", "'"),
                 ("\u2019", "'"), ("\u2014", "-"), ("\u2013", "-"), ("\u2212", "-")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()

def verify(rec, head):
    """Hard checks on model output. Returns list of failure strings."""
    fails = []
    if rec.get("outcome") not in OUTCOMES:
        fails.append("outcome_vocab:" + str(rec.get("outcome")))
    ev = rec.get("evidence") or ""
    if not ev or normalize_ws(ev) not in normalize_ws(head):
        fails.append("evidence_not_verbatim")
    if not isinstance(rec.get("amends"), list):
        fails.append("amends_not_list")
    if not isinstance(rec.get("keywords"), list) or not rec.get("keywords"):
        fails.append("keywords_missing")
    if rec.get("rubric_cell") not in RUBRIC:
        fails.append("rubric_cell_vocab")
    return fails

# ---------------------------------------------------------------- build
def load_cache():
    c = {}
    if os.path.exists(CACHE):
        with open(CACHE, encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line); c[r["sha"]] = r
                except Exception: pass
    return c

def append_cache(rec):
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    with open(CACHE, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

def build(args):
    files = []
    for pat in (args.sources or DEFAULT_SOURCES):
        files += glob.glob(os.path.join(ROOT, pat))
    files = sorted(set(files))
    lane_re = re.compile(args.lane_filter, re.I) if args.lane_filter else None
    cache = load_cache()
    rows, n_model, n_fail = [], 0, 0
    for path in files:
        head = read_head(path)
        if lane_re and not (lane_re.search(os.path.basename(path)) or lane_re.search(file_title(head))):
            continue
        if args.limit and len(rows) >= args.limit: break
        fid, author = file_id(path, head)
        det = {"id": fid, "author": author, "date": file_date(path, head),
               "file": os.path.relpath(path, ROOT), "title": file_title(head)[:240],
               "verdict_tokens": verdict_tokens(head)}
        h = sha(path) + ":" + SCHEMA
        if h in cache and not args.refresh:
            rec = dict(cache[h]); rec.update(det)
            rec["coarse"] = coarse(rec.get("outcome", "")); rec.setdefault("rubric_cell", ""); rec.setdefault("outcome2", "")
            rec["unstable"] = bool(rec.get("outcome2")) and rec["coarse"] != coarse(rec["outcome2"])
            rec["verify"] = verify(rec, head) if "dry_run" not in rec.get("verify", []) else rec["verify"]
        elif args.dry_run:
            rec = {**det, "sha": h, "lane": "", "approach": "", "outcome": "", "reason": "",
                   "amends": [], "evidence": "", "verify": ["dry_run"], "model": ""}
        else:
            try:
                hint = f"VERDICT WORDS FOUND IN TEXT: {', '.join(det['verdict_tokens']) or '(none)'}"
                prompt = f"FILE: {det['file']}\nID: {fid}  AUTHOR: {author}  DATE: {det['date']}\n{hint}\n\n{head}"
                m = call_model(args.api, args.endpoint, args.model, args.key, prompt)
                fails = verify(m, head)
                if any(f == "evidence_not_verbatim" for f in fails):      # one retry, naming the failure
                    m2 = call_model(args.api, args.endpoint, args.model, args.key,
                                    prompt + "\n\nYOUR PREVIOUS evidence was NOT a verbatim span of the text: "
                                    + json.dumps(m.get("evidence", "")) + ". Copy an exact contiguous span this time.")
                    f2 = verify(m2, head)
                    if "evidence_not_verbatim" not in f2:
                        m, fails = m2, f2
                o2 = {}
                if args.runs >= 2:
                    try:
                        o2 = call_model(args.api, args.endpoint, args.model, args.key, prompt, system=SYSTEM2)
                    except Exception as e:
                        o2 = {"outcome": "", "why": "model_error:" + str(e)[:60]}
            except Exception as e:
                m, fails, o2 = {}, ["model_error:" + str(e)[:80]], {}
            oc1, oc2 = m.get("outcome", ""), o2.get("outcome", "")
            rec = {**det, "sha": h, "rubric_cell": m.get("rubric_cell", ""), "lane": str(m.get("lane", ""))[:60],
                   "coarse": coarse(oc1), "outcome2": oc2, "why2": str(o2.get("why", ""))[:200],
                   "unstable": bool(oc2) and coarse(oc1) != coarse(oc2),
                   "approach": str(m.get("approach", ""))[:300],
                   "outcome": m.get("outcome", ""), "reason": str(m.get("reason", ""))[:300],
                   "amends": m.get("amends", []) if isinstance(m.get("amends"), list) else [],
                   "keywords": [str(k)[:60] for k in m.get("keywords", [])][:12] if isinstance(m.get("keywords"), list) else [],
                   "evidence": str(m.get("evidence", ""))[:200], "verify": fails, "model": args.model}
            append_cache(rec); n_model += 1
        if rec["verify"]: n_fail += 1
        rows.append(rec)
        if args.verbose:
            print(f"[{len(rows)}] {rec['id']:<10} {rec['coarse']:<5} {rec['outcome']:<16}{'UNSTABLE(' + rec['outcome2'] + ') ' if rec.get('unstable') else ''}{'VERIFY_FAIL ' + ','.join(rec['verify']) if rec['verify'] else 'ok':<30} [{rec.get('rubric_cell','')[:22]}] {rec['title'][:60]}", flush=True)
    return rows, n_model, n_fail

def write_outputs(rows, args):
    rows = sorted(rows, key=lambda r: (r.get("rubric_cell", ""), r.get("lane", ""), r["date"], r["id"]))
    os.makedirs(os.path.dirname(OUT_JSONL), exist_ok=True)
    with open(OUT_JSONL, "w", encoding="utf-8") as f:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    stamp = time.strftime("%Y-%m-%d %H:%M %Z")
    by_lane = {}
    for r in rows: by_lane.setdefault(r.get("rubric_cell") or "(no rubric cell)", []).append(r)
    L = ["---", 'title: "BST Approaches Register — did we do this before?"', "author: Keeper (instrument-derived)",
         f"date: {stamp}", f'status: "DERIVED by play/keeper_approaches_register.py; {len(rows)} rows; '
         f'{sum(1 for r in rows if r["verify"])} rows VERIFY_FAIL (evidence not verbatim / vocab) — outcomes on those rows are untrusted"',
         "---", "", "# BST Approaches Register",
         "", "One row per audit / ruling / note. **Model-drafted fields (lane, approach, outcome, reason) are drafts; "
         "the `file` column is the ruling. A row whose evidence phrase is not verbatim in its source is marked VERIFY_FAIL.** "
         "Query: `python3 play/didwe.py \"<topic>\"`.", ""]
    if args.lane_filter:
        L.append(f"Scope of this build: `--lane-filter '{args.lane_filter}'` (pilot). Sources: {', '.join(args.sources or DEFAULT_SOURCES)}.")
        L.append("")
    L.append("**Columns.** `coarse` = STOP (refuted / retracted / withdrawn) · LIVE (open / conditional / parked) · DONE (proved / passed / certified) · AMEND. "
             "`UNSTABLE` = two independent model readings disagree on the coarse label — read the file. `⚠VERIFY_FAIL` = evidence phrase not verbatim — outcome untrusted.")
    L.append("")
    L.append("| rubric cell | lane | id | date | coarse | outcome | approach | reason | keywords | amends | evidence (verbatim) | file |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for lane in sorted(by_lane):
        for r in by_lane[lane]:
            oc = r["outcome"] + (" ⚠VERIFY_FAIL" if r["verify"] else "")
            co = r.get("coarse", "") + (" UNSTABLE" if r.get("unstable") else "")
            cell = lambda s: str(s).replace("|", "\\|").replace("\n", " ")
            L.append(f"| {cell(lane)} | {cell(r.get('lane',''))} | {r['id']} | {r['date']} | {co} | {oc} | {cell(r['approach'])} | {cell(r['reason'])} | "
                     f"{cell(', '.join(r.get('keywords', [])))} | {', '.join(r['amends'])} | {cell(r['evidence'])} | `{r['file']}` |")
    L += ["", f"Counts by outcome: " + ", ".join(f"{k}={v}" for k, v in sorted(
        {o: sum(1 for r in rows if r['outcome'] == o) for o in OUTCOMES + ['']}.items()) if v),
          f"Unstable rows: {sum(1 for r in rows if r.get('unstable'))} / {len(rows)}", ""]
    with open(OUT_MD, "w", encoding="utf-8") as f: f.write("\n".join(L))
    return OUT_MD, OUT_JSONL

# ---------------------------------------------------------------- selftest + controls
def selftest():
    ok = True
    def chk(name, cond):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + name); ok = ok and cond
    chk("id: Keeper K", file_id("notes/Keeper_K1876_RH_ROW_2026-09-07.md", "")[0] == "K1876")
    chk("id: Keeper K-A", file_id("notes/Keeper_K1862-A_cone_2026-09-05.md", "")[0] == "K1862-A")
    chk("id: Keeper K+K", file_id("notes/Keeper_K194_K195_DCCP.md", "")[0] == "K194+K195")
    chk("id: Cal §", file_id("notes/cal_R142_C1_x_2026-09-11.md", "# C1 (§946)")[0] == "§946")
    chk("id: Lyra F", file_id("notes/Lyra_F1012_cone_check.md", "")[0] == "F1012")
    chk("date from filename", file_date("notes/x_2026-09-07.md", "") == "2026-09-07")
    chk("title H1", file_title("---\nx\n---\n# K1 — hello\n## 1") == "K1 — hello")
    chk("tokens", verdict_tokens("VERDICT: CONDITIONAL PASS — RETRACTED later") == ["CONDITIONAL PASS", "RETRACTED"])
    head = "The wall remains unmoved. Tier: ATTEMPT, unchanged."
    chk("verify: verbatim evidence passes", verify({"outcome": "OPEN", "evidence": "Tier: ATTEMPT, unchanged", "amends": [], "keywords": ["x"], "rubric_cell": RUBRIC[0]}, head) == [])
    chk("verify: markdown-bold + en-dash evidence passes", verify({"outcome": "OPEN", "evidence": "the wall remains unmoved – Tier", "amends": [], "keywords": ["x"], "rubric_cell": RUBRIC[0]}, "The **wall** remains unmoved — Tier: ATTEMPT") == [])
    chk("verify: paraphrase fails (negative control)", "evidence_not_verbatim" in verify({"outcome": "OPEN", "evidence": "the tier is unchanged", "amends": []}, head))
    chk("verify: missing keywords fails", "keywords_missing" in verify({"outcome": "OPEN", "evidence": "The wall", "amends": []}, head))
    chk("coarse map", (coarse("RETRACTED"), coarse("OPEN"), coarse("CLOSED_POSITIVE"), coarse("AMENDMENT")) == ("STOP", "LIVE", "DONE", "AMEND"))
    chk("verify: bad vocab fails", any(f.startswith("outcome_vocab") for f in verify({"outcome": "PASS", "evidence": "The wall", "amends": []}, head)))
    print("SELFTEST", "PASS" if ok else "FAIL"); return ok

def run_controls(rows, path):
    """controls file: lines 'ID<TAB>EXPECTED_OUTCOME[,ALT]' ; '#' comments."""
    byid = {r["id"]: r for r in rows}
    n, bad = 0, 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"): continue
            cid, exp = line.split("\t")[:2]; n += 1
            got = byid.get(cid, {}).get("outcome", "(no row)")
            good = got in exp.split(",")
            bad += 0 if good else 1
            print(f"{'CTRL ok  ' if good else 'CTRL MISS'} {cid:<10} expected {exp:<28} got {got}")
    print(f"CONTROLS: {n - bad}/{n} match"); return bad == 0

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sources", nargs="*", help="glob patterns relative to repo root")
    ap.add_argument("--lane-filter", help="regex; only files whose NAME or TITLE matches (pilot scoping)")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--api", default=os.environ.get("APPROACHES_API", "ollama"), choices=["ollama", "openai"])
    ap.add_argument("--endpoint", default=os.environ.get("APPROACHES_ENDPOINT", "http://localhost:11434"))
    ap.add_argument("--model", default=os.environ.get("APPROACHES_MODEL", "qwen3:30b-a3b"))
    ap.add_argument("--key", default=os.environ.get("APPROACHES_API_KEY", ""))
    ap.add_argument("--refresh", action="store_true", help="ignore cache; re-extract")
    ap.add_argument("--runs", type=int, default=2, help="2 = add an independent second reading of the outcome (UNSTABLE flag); 1 = single")
    ap.add_argument("--dry-run", action="store_true", help="deterministic layer only; no model calls")
    ap.add_argument("--controls", help="tab-separated ID<TAB>EXPECTED file; report matches")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        sys.exit(0 if selftest() else 1)
    t0 = time.time()
    rows, n_model, n_fail = build(args)
    md, jl = write_outputs(rows, args)
    print(f"rows={len(rows)} model_calls={n_model} verify_fail={n_fail} secs={time.time() - t0:.0f}")
    print(f"wrote {os.path.relpath(md, ROOT)} and {os.path.relpath(jl, ROOT)}")
    if args.controls:
        sys.exit(0 if run_controls(rows, args.controls) else 2)

if __name__ == "__main__":
    main()
