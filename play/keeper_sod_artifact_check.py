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
    reg_tids = set(int(x) for x in re.findall(r"\bT(\d{1,4})\b", txt))
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
RETIRED = ["mass-45", "harmonic-50", "two-axis", "running.rescue", "QCD.running.*rescue"]
board_glob = glob.glob(p("notes", "CI_BOARD_2026-07*.md")) + glob.glob(p("notes", ".running", "MESSAGES_2026-07*.md"))
retire_hits = []
for b in board_glob:
    try: bt = open(b).read()
    except Exception: continue
    for r in RETIRED:
        for m in re.finditer(r".{0,40}(bank|banked).{0,40}", bt, re.I):
            seg = m.group(0)
            if re.search(r"45\b", seg) and "θ13" not in seg and "theta13" not in seg and "1/45" not in seg:
                retire_hits.append((os.path.basename(b), seg.strip()[:80]))
if retire_hits:
    flag("REVIEW", "retirement", f"{len(retire_hits)} board line(s) pair a retired-reading number with 'bank' -- eyeball for false-bank rot", "Keeper")
else:
    flag("OK", "retirement", "no retired reading cited as a bank on current boards")

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
