#!/usr/bin/env python3
"""
Keeper Start-of-Day Artifact-Currency Check  (Keeper #28, operationalized)
==========================================================================
Verifies the three authoritative artifacts (Ledger, Graph, Registry) against
the counters and boards, and DIRECTS the update where it finds drift.

Run at the start of every session:  python3 play/keeper_sod_artifact_check.py
Exit 0 = ALL CURRENT.  Exit 1 = DRIFT DETECTED (see DIRECTIVE lines).

The lesson this enforces (Mid-Year 2026-07-02): the boards are working memory;
the Ledger/Graph/Registry are the record of truth. A count/ID that lives only in
board headers and scattered K-audits, never in one reconciled artifact, is
UNVERIFIED BY CONSTRUCTION. Catch drift on cadence, not once a year.
"""
import json, os, re, glob, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def p(*a): return os.path.join(ROOT, *a)

STALE_DAYS = 7          # ledger/graph older than this vs today => STALE flag
findings = []           # (level, artifact, message, directive_owner)
def flag(level, artifact, msg, owner=None):
    findings.append((level, artifact, msg, owner))

def read_int(path):
    try:
        return int(open(path).read().strip())
    except Exception:
        return None

def today():
    # date passed via env to stay deterministic; fall back to file mtime era
    d = os.environ.get("SOD_DATE")
    if d:
        return datetime.date.fromisoformat(d)
    return None

# ---------- 1. THEOREM CHAIN: counter vs graph vs registry ----------
next_thm = read_int(p("play", ".next_theorem"))
graph_max = graph_nodes = None
graph_tids = set()
try:
    g = json.load(open(p("play", "ac_graph_data.json")))
    nodes = g.get("nodes", [])
    graph_nodes = len(nodes)
    nums = []
    for n in nodes:
        t = str(n.get("tid", "")).lstrip("T")
        if t.isdigit():
            nums.append(int(t)); graph_tids.add(int(t))
    graph_max = max(nums) if nums else None
except Exception as e:
    flag("ERROR", "graph", f"cannot read ac_graph_data.json: {e}", "Elie")

reg_max = None; reg_tids = set()
try:
    txt = open(p("notes", "BST_AC_Theorem_Registry.md")).read()
    # K1053 LOCK (installed K1800, 2026-08-22, after Cal Section 698 measured the gap):
    # count theorem IDs from REGISTRY ROWS ONLY. The raw \bT(\d+)\b grep also matched
    # toy ids wearing a T prefix in prose ("T2849-T2897 cluster"), inflating reg_max to
    # T2897 and injecting 691 phantom IDs -> a FALSE [OK] in a drift detector for 22 days.
    reg_tids = set(int(x) for x in re.findall(r"^\s*\|\s*\*{0,2}T(\d{1,4})\*{0,2}\s*\|", txt, re.M))
    reg_max = max(reg_tids) if reg_tids else None
except Exception as e:
    flag("WARN", "registry", f"cannot read registry: {e}", "Lyra")

if next_thm is not None and graph_max is not None:
    if graph_max == next_thm - 1:
        flag("OK", "graph", f"graph max tid T{graph_max} == counter-1 (.next_theorem={next_thm})")
    else:
        flag("DRIFT", "graph",
             f"graph max T{graph_max} != counter-1 ({next_thm-1}); {next_thm-1-graph_max} theorem(s) unregistered in graph",
             "Grace")
# registry stub gap = theorems in graph/counter but not sourced in registry
if graph_max and reg_max is not None:
    stub_range = [t for t in range(reg_max + 1, (next_thm or graph_max + 1))]
    unsourced = [t for t in range((graph_max or 0) - 30, (next_thm or 0)) if t > 0 and t not in reg_tids]
    if unsourced:
        flag("DRIFT", "registry",
             f"{len(unsourced)} recent theorem IDs counter-advanced but NOT sourced in registry "
             f"(e.g. {['T'+str(x) for x in unsourced[:6]]}...) -> graph stubs, theorem-count analog of a claimed-vs-verified gap",
             "Lyra")
    else:
        flag("OK", "registry", f"registry sourced through recent range (max T{reg_max})")

# pre-existing tid gaps (likely retractions) -- report count, ask confirmation once
if graph_tids and graph_max:
    gaps = [t for t in range(1, graph_max + 1) if t not in graph_tids]
    if gaps:
        flag("NOTE", "graph",
             f"{len(gaps)} tid-gaps in T1-T{graph_max} (likely historical retractions; confirm retracted-vs-missing, don't assume)")

# ---------- 2. TOY COUNTER vs files ----------
next_toy = read_int(p("play", ".next_toy"))
toy_files = glob.glob(p("play", "toy_*.py"))
toy_nums = []
for f in toy_files:
    m = re.search(r"toy_(\d+)", os.path.basename(f))
    if m: toy_nums.append(int(m.group(1)))
toy_max = max(toy_nums) if toy_nums else None
if next_toy and toy_max is not None:
    if toy_max < next_toy:
        flag("OK", "toys", f"toy max {toy_max} < counter {next_toy} (consistent); {len(toy_nums)} toy files")
    else:
        flag("DRIFT", "toys", f"toy file {toy_max} >= counter {next_toy} -- counter not advanced or collision", "Elie")

# ---------- 3. LEDGER freshness + single-source count ----------
ledgers = sorted(glob.glob(p("notes", "Grace_Master_Derived_vs_Assigned_Ledger_v*.md")),
                 key=lambda s: [int(x) for x in re.findall(r"v(\d+)_(\d+)", s)[0]] if re.findall(r"v(\d+)_(\d+)", s) else [0,0])
if ledgers:
    latest = ledgers[-1]
    ltxt = open(latest).read()
    mdate = re.search(r"date:\s*\"?(\d{4}-\d{2}-\d{2})", ltxt)
    ldate = mdate.group(1) if mdate else "?"
    # does it enumerate a count in ONE place?
    has_count = bool(re.search(r"count is 8|Sourced-clean total:\s*8|verifiable count is 8", ltxt))
    flag("OK" if has_count else "WARN", "ledger",
         f"latest = {os.path.basename(latest)} dated {ldate}; single-source count enumerated: {has_count}",
         None if has_count else "Grace")
    td = today()
    if td and ldate != "?":
        age = (td - datetime.date.fromisoformat(ldate)).days
        if age > STALE_DAYS:
            flag("STALE", "ledger", f"ledger is {age} days old (> {STALE_DAYS}); reconcile to current bank motions", "Grace")
else:
    flag("DRIFT", "ledger", "no Grace Master Ledger found", "Grace")

# ---------- 4. RETIREMENT PROPAGATION: retired readings still cited as banks? ----------
# REWRITTEN 2026-08-23 (K1818). The previous version had THREE defects, all silent:
#   (1) the loop variable `r` over RETIRED was NEVER USED in the inner regex, so the same
#       hits were counted once per RETIRED term -> a 5x-inflated count (reported 50, actual 10);
#   (2) only the literal "45" was ever tested; the other four RETIRED terms were never checked;
#   (3) the file glob was JULY-ONLY and could not see the CURRENT notes/CI_BOARD.md at all,
#       while the message said "on current boards".
# True-positive rate of the old check, measured: 0/10 (timestamps, toy ids, unrelated numerals).
# It could NOT have caught the real un-propagated retirement found the same day (A^2=rank / T2516).
# Standing lesson (Elie): a control that runs after you read the answer is a check;
# a control that GATES THE READ is an instrument. This one now gates.

# Each entry: (label, regex for the retired reading, regex that must NOT co-occur (exclusions))
RETIRED_READINGS = [
    ("A^2=rank",        r"(?<![A-Za-z‐-―-])A\W{0,2}2\s*=\s*rank",  None),  # lookbehind: ET-A2=... labels are NOT A^2=rank (false-positive fixed 08-25, K-verified with must-catch)
    ("Wyler alpha",     r"137\.0360|Wyler",                            None),
    ("2/sqrt(79)",      r"2\s*/\s*(?:\\?sqrt|√)\s*\(?\s*79",          None),
    ("36/869 V_cb",     r"36\s*/\s*869",                               None),
    ("mass-45",         r"\bmass-45\b",                                None),
    ("harmonic-50",     r"\bharmonic-50\b",                            None),
    ("two-axis",        r"\btwo-axis\b",                               None),
    ("running rescue",  r"running[^.\n]{0,20}rescue",                   None),
]
BANK_NEAR = r".{0,60}\b(bank|banked|banks)\b.{0,60}"

def _scan(text, label, rx, excl):
    out = []
    for m in re.finditer(BANK_NEAR, text, re.I):
        seg = m.group(0)
        if re.search(rx, seg, re.I) and not (excl and re.search(excl, seg, re.I)):
            out.append(seg.strip()[:100])
    return out

# POSITIVE CONTROL — gates the read. Must-catch AND must-reject, on synthetic text.
_MUSTCATCH = "we still bank the A^2=rank step as forced"
_MUSTREJECT = "next_toy=4545 and the 11:45 EDT board line, banked earlier"
_ctrl_catch = any(_scan(_MUSTCATCH, l, rx, ex) for l, rx, ex in RETIRED_READINGS)
_ctrl_reject = not any(_scan(_MUSTREJECT, l, rx, ex) for l, rx, ex in RETIRED_READINGS)

if not (_ctrl_catch and _ctrl_reject):
    flag("DRIFT", "retirement",
         "POSITIVE CONTROL FAILED (must-catch=%s must-reject=%s) -- retirement scan NOT RUN; "
         "a search that cannot succeed proves nothing" % (_ctrl_catch, _ctrl_reject), "Keeper")
else:
    board_files = ([p("notes", "CI_BOARD.md")]
                   + glob.glob(p("notes", "CI_BOARD_2026-0*.md"))
                   + glob.glob(p("notes", ".running", "MESSAGES_2026-0*.md")))
    board_files = [b for b in board_files if os.path.exists(b)]
    hits = {}   # (file, label, seg) -> dedup
    for b in board_files:
        try: bt = open(b).read()
        except Exception: continue
        for label, rx, excl in RETIRED_READINGS:
            for seg in _scan(bt, label, rx, excl):
                hits[(os.path.basename(b), label, seg)] = True
    if hits:
        by_label = {}
        for (_f, label, _s) in hits: by_label[label] = by_label.get(label, 0) + 1
        detail = ", ".join("%s:%d" % (k, v) for k, v in sorted(by_label.items()))
        flag("REVIEW", "retirement",
             "%d DISTINCT board line(s) pair a RETIRED reading with 'bank' across %d files [%s] "
             "-- eyeball for false-bank rot (control PASSED)" % (len(hits), len(board_files), detail),
             "Keeper")
    else:
        flag("OK", "retirement",
             "no retired reading cited as a bank across %d board/message files (control PASSED)" % len(board_files))

# ---------- 4b. UN-PROPAGATED RETIREMENT (K1818b, Cal's catch) ----------
# Detector 1 (above) finds a retired reading sitting NEAR a bank-word on a board.
# It CANNOT find the T2516 species: a retired reading that appears exactly ONCE, inside the
# very row that depends on it, as a DERIVATION ROOT. One hit reads as "present and accounted
# for", not "retired but still load-bearing". Different detection problem -> second detector.
#
# The controls below are COPIED FROM THE CORPUS, not composed. My first attempt at a control
# passed on a string I wrote in ASCII ("A^2=rank") while the registry uses "A²=rank" -- the
# control validated the checker's notation instead of the corpus's. A must-catch case you
# authored is not a must-catch case.
RETIRE_MARK = r"\bRETIRED\b|\bretired\b|DO NOT CITE|do not cite"
WINDOW = 400

def _unpropagated(text, rx):
    out = []
    for m in re.finditer(rx, text, re.I):
        lo, hi = max(0, m.start() - WINDOW), min(len(text), m.end() + WINDOW)
        if not re.search(RETIRE_MARK, text[lo:hi]):
            out.append(text[max(0, m.start()-60):m.end()+60].replace("\n", " ")[:110])
    return out

_reg_path = p("notes", "BST_AC_Theorem_Registry.md")
try:
    _reg = open(_reg_path).read()
except Exception:
    _reg = ""

if _reg:
    _i = _reg.find("T2516")
    _real = _reg[_i:_i+900] if _i >= 0 else ""
    _rx_a2 = r"A\s*(?:\u00b2|\^\s*2|\*\*\s*2)\s*=\s*rank"
    # must-REJECT: the real row AS IT STANDS (marker present) -> no flag
    _ok_reject = (_real != "" and not _unpropagated(_real, _rx_a2))
    # must-CATCH: the same real text with its marker stripped -> must flag
    _stripped = re.sub(RETIRE_MARK, "xxx", _real)
    _ok_catch = bool(_unpropagated(_stripped, _rx_a2))
    if not (_ok_catch and _ok_reject):
        flag("DRIFT", "retirement2",
             "POSITIVE CONTROL FAILED (corpus-sourced; catch=%s reject=%s) -- un-propagated-retirement "
             "scan NOT RUN" % (_ok_catch, _ok_reject), "Keeper")
    else:
        _un = []
        for label, rx, _excl in RETIRED_READINGS:
            for seg in _unpropagated(_reg, rx):
                _un.append((label, seg))
        if _un:
            _by = {}
            for l, _sg in _un: _by[l] = _by.get(l, 0) + 1
            flag("REVIEW", "retirement2",
                 "%d registry occurrence(s) of a RETIRED reading with NO retirement marker within %d chars [%s] "
                 "-- un-propagated retirement (control PASSED, corpus-sourced)"
                 % (len(_un), WINDOW, ", ".join("%s:%d" % kv for kv in sorted(_by.items()))), "Keeper")
        else:
            flag("OK", "retirement2",
                 "every registry occurrence of a retired reading carries a retirement marker (control PASSED)")

# ---------- REPORT ----------
order = {"ERROR":0,"DRIFT":1,"STALE":2,"WARN":3,"REVIEW":4,"NOTE":5,"OK":6}
findings.sort(key=lambda f: order.get(f[0], 9))
print("="*72)
print("KEEPER START-OF-DAY ARTIFACT-CURRENCY CHECK")
print("="*72)
drift = False
for level, art, msg, owner in findings:
    tag = f"[{level}]"
    line = f"{tag:8s} {art:11s} {msg}"
    print(line)
    if owner and level in ("DRIFT","STALE","ERROR","REVIEW","WARN"):
        print(f"{'':8s} {'->DIRECTIVE':11s} {owner} owns the fix.")
    if level in ("DRIFT","STALE","ERROR"):
        drift = True
print("="*72)
print("VERDICT:", "DRIFT DETECTED - direct the updates above" if drift else "ALL CURRENT")
print("="*72)
sys.exit(1 if drift else 0)
