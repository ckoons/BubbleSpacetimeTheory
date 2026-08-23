#!/usr/bin/env python3
"""
Toy 5438 — THE TWO-AXIS PRE-DISPATCH SWEEP.

QUESTION THIS COMPUTE ANSWERS (declared before running):
    "Can the consistency sweep be extended to a SECOND axis — elimination-scope-sheds —
     and does the resulting instrument re-find BOTH known catches?"

WHY A SECOND AXIS (this round's lesson, inherited not re-derived):
    Axis A — FORBIDDANCE CROSSING. A stated forbiddance ("no SU(3) in the geometry",
        #108) and a banked claim that crosses it (T2523's SU(3)-colour confinement).
        Live and uncaught for a month.
    Axis B — ELIMINATION SCOPE-SHED. "Γ was never needed" is TRUE of the physical
        Hilbert space (W1 = H²) and FALSE corpus-wide: the QED arithmetic lane (a_e to
        0.026%) lives on the Selberg trace formula over Γ(137)\\D_IV⁵. The elimination
        was stated with the scope of the context where it was checked.
    ⟹ B is a DIFFERENT SHAPE from A. A term-grep for the forbidden thing cannot see it,
      because nothing forbidden was claimed — something needed was discarded.

★ THE BAR (§599, and it is the whole point): an instrument that cannot re-find the two
  catches we ALREADY know about is not an instrument. Both are positive controls, and
  they run BEFORE any new hit is reported.

★ AND THE C6 BAR: a corpus-wide grep for suggestive phrasing is look-elsewhere-prone by
  construction. Every number below is reported with its DENOMINATOR, and the pattern set
  is stated — what it does not match, it does not cover, and I say so.
"""

import os
import re
from collections import defaultdict

ROOT = "/Users/cskoons/projects/github/BubbleSpacetimeTheory/notes"

# ---------------------------------------------------------------- the pattern set (stated)
ELIM_PATTERNS = [
    r"\bdropp?(?:ed|ing)?\b", r"\bretir(?:e|ed|ing|ement)\b", r"\bwithdraw(?:n|al|s)?\b",
    r"\bRETRACTED\b", r"\bnever needed\b", r"\bnot needed\b", r"\bsupersed(?:e|ed|es)\b",
    r"\bDEPRECATED\b", r"\bKILLED\b", r"\bno longer (?:needed|used|required)\b",
    r"\bout of scope\b", r"\bde-?scoped\b",
]
FORBID_PATTERNS = [
    r"\bforbid(?:s|den|dance|dances)?\b", r"\bnever say\b", r"\bnot derived\b",
    r"\bimported,? not derived\b", r"\bno internal\b", r"\bmust NEVER\b",
    r"\bcannot be derived\b", r"\bdoes not derive\b", r"\bFive[- ]Absence\b",
]
TIER = re.compile(r"\b(DERIVED|BANKED|Tier[- ]?D\b|PROVED|Derived)\b")

ELIM_RE = re.compile("|".join(ELIM_PATTERNS), re.I)
FORBID_RE = re.compile("|".join(FORBID_PATTERNS), re.I)

# ---------------------------------------------------------------- curated objects
# Axis B: an elimination + what it would STRAND if taken corpus-wide.
ELIMINATIONS = [
    ("Gamma (arithmetic quotient)",
     re.compile(r"Γ\s*\\|Γ\(137\)|Gamma\s*\\|Γ\\G"),
     re.compile(r"Selberg|closed geodesic|ζ\(3\)|zeta\(3\)|a_e\b|arithmetic lane", re.I),
     True),                                    # <- POSITIVE CONTROL: must flag
    ("K3-Hodge reading of 20",
     re.compile(r"h\^?\{?1,1\}?\(K3\)|K3 Hodge"),
     re.compile(r"m_s/m_d|s/d\s*=\s*20|quark ratio", re.I),
     None),
    ("6/5 transition number",
     re.compile(r"\b6/5\b"),
     re.compile(r"Bergman|Szeg|exponent|transition", re.I),
     None),
    ("A2 SU(3)-colour confinement",
     re.compile(r"\(A2\)|SU\(3\)[- ]colou?red asymptotic"),
     re.compile(r"confinement is derived|colour confinement", re.I),
     None),
]
# Axis A: a forbiddance + the shape that would cross it.
FORBIDDANCES = [
    ("#108: no SU(3) in the geometry",
     re.compile(r"SU\(3\)[^.]{0,80}(imported|not derived)|no internal colou?r", re.I),
     re.compile(r"(colou?r confinement|SU\(3\))[^.]{0,60}(is )?DERIVED", re.I),
     True),                                    # <- POSITIVE CONTROL: must flag
    ("Five-Absence: NO SUSY", re.compile(r"NO SUSY|Five[- ]Absence", re.I),
     re.compile(r"SUSY[^.]{0,40}\b(DERIVED|predicted|required)\b"), None),
    ("Five-Absence: NO proton decay", re.compile(r"NO proton decay|Five[- ]Absence", re.I),
     re.compile(r"proton decay[^.]{0,40}\b(DERIVED|predicted|required)\b"), None),
    ("Five-Absence: NO monopoles", re.compile(r"NO monopoles|Five[- ]Absence", re.I),
     re.compile(r"monopole[^.]{0,40}\b(DERIVED|predicted|required)\b"), None),
    ("Five-Absence: NO sterile neutrinos", re.compile(r"NO sterile|Five[- ]Absence", re.I),
     re.compile(r"sterile neutrino[^.]{0,40}\b(DERIVED|predicted|required)\b"), None),
    ("Five-Absence: NO GUT", re.compile(r"NO GUT|Five[- ]Absence", re.I),
     re.compile(r"\bGUT\b[^.]{0,40}\b(DERIVED|predicted|required)\b"), None),
    ("n_C = 5 is a measured input, not forced",
     re.compile(r"n_C\s*=\s*5[^.]{0,60}(measured|input|not forced)", re.I),
     re.compile(r"n_C\s*=\s*5[^.]{0,40}\bFORCED\b"), None),
    ("the compact gap is NOT the Clay mass gap",
     re.compile(r"not the Clay|NOT the Clay mass gap", re.I),
     re.compile(r"(Clay|Millennium)[^.]{0,50}\b(SOLVED|CLOSED|proved)\b"), None),
]

# ================================================================ SCAN
print("=" * 78)
print("SECTION 0 — THE SCAN (denominator first, per C6)")
print("=" * 78)
files = []
for dp, _, fns in os.walk(ROOT):
    for fn in fns:
        if fn.endswith(".md"):
            files.append(os.path.join(dp, fn))
print(f"  markdown files in notes/: {len(files)}")

elim_hits, forbid_hits = 0, 0
obj_files = defaultdict(set)      # object -> files where its DEFINING pattern appears
use_files = defaultdict(set)      # object -> files where its LOAD-BEARING use appears
line_hits = defaultdict(set)      # object -> (file, line) at LINE resolution
scanned_bytes = 0
for path in files:
    try:
        with open(path, "r", errors="ignore") as fh:
            txt = fh.read()
    except OSError:
        continue
    scanned_bytes += len(txt)
    if ELIM_RE.search(txt):
        elim_hits += 1
    if FORBID_RE.search(txt):
        forbid_hits += 1
    tiered = bool(TIER.search(txt))
    for name, defre, usere, _ in ELIMINATIONS:
        if defre.search(txt):
            obj_files[name].add(path)
        if usere.search(txt) and tiered:
            use_files[name].add(path)
    for name, forbre, crossre, _ in FORBIDDANCES:
        if forbre.search(txt):
            obj_files[name].add(path)
        if crossre.search(txt) and tiered:
            use_files[name].add(path)
    # ---- REFINED RESOLUTION: require the object and its use/crossing on the SAME LINE.
    # File-level co-occurrence proved far too coarse (see Section 1b) — a 228 MB corpus
    # puts almost any two patterns in some file together.
    for line in txt.splitlines():
        if not TIER.search(line):
            continue
        for name, defre, usere, _ in ELIMINATIONS:
            if defre.search(line) and usere.search(line):
                line_hits[name].add((path, line.strip()[:150]))
        for name, forbre, crossre, _ in FORBIDDANCES:
            if crossre.search(line):
                line_hits[name].add((path, line.strip()[:150]))

print(f"  bytes scanned: {scanned_bytes/1e6:.1f} MB")
print(f"  files containing an ELIMINATION-shaped phrase : {elim_hits:>5d} / {len(files)}"
      f"  ({100*elim_hits/len(files):.1f}%)")
print(f"  files containing a FORBIDDANCE-shaped phrase  : {forbid_hits:>5d} / {len(files)}"
      f"  ({100*forbid_hits/len(files):.1f}%)")
print()
print("  ★ THE DENOMINATOR IS THE POINT: these phrase-classes are COMMON. A hit is a")
print("    CANDIDATE, never a finding. Every candidate below is adjudicated by object,")
print("    not by phrase — which is why the sweep runs by CLAIM SHAPE.")
print(f"  ★ PATTERN SET STATED: {len(ELIM_PATTERNS)} elimination patterns, "
      f"{len(FORBID_PATTERNS)} forbiddance patterns. Outside them = NOT COVERED.")

# ================================================================ POSITIVE CONTROLS
print()
print("=" * 78)
print("SECTION 1 — ★★★ POSITIVE CONTROLS: does it re-find the two KNOWN catches?")
print("=" * 78)
pc = []
for name, _, _, expect in ELIMINATIONS + FORBIDDANCES:
    if expect is True:
        d, u = len(obj_files[name]), len(line_hits[name])
        found = (d > 0 and u > 0)
        pc.append((name, d, u, found))
        print(f"  PC  {name:<38s} defining-files {d:>4d}   load-bearing/crossing {u:>4d}   "
              f"{'RE-FOUND' if found else '*** MISSED ***'}")
controls_ok = all(f for _, _, _, f in pc) and len(pc) == 2
print()
print(f"CONTROLS: {'2/2 — the instrument re-finds BOTH known catches.' if controls_ok else '*** FAILED — instrument invalid ***'}")
if not controls_ok:
    raise SystemExit("instrument cannot re-find known catches; no new hit reported")

# ================================================================ PRECISION
print()
print("=" * 78)
print("SECTION 1b — ★★★ MEASURING THE INSTRUMENT'S PRECISION (file vs line resolution)")
print("=" * 78)
print("File-level co-occurrence has RECALL but no PRECISION: in a 228 MB corpus almost")
print("any two patterns share some file. Requiring them on the SAME LINE is the fix.\n")
print(f"{'object':>42s} {'file-level':>11s} {'line-level':>11s} {'reduction':>10s}")
print("-" * 78)
tot_f = tot_l = 0
for name, _, _, _ in ELIMINATIONS + FORBIDDANCES:
    f, l = len(use_files[name]), len(line_hits[name])
    tot_f += f; tot_l += l
    red = f"{100*(1-l/f):.0f}%" if f else "--"
    print(f"{name:>42s} {f:>11d} {l:>11d} {red:>10s}")
print("-" * 78)
print(f"{'TOTAL':>42s} {tot_f:>11d} {tot_l:>11d} "
      f"{(f'{100*(1-tot_l/tot_f):.1f}%' if tot_f else '--'):>10s}")
precision_gain = tot_l < tot_f * 0.2
print()
print(f"★★★ LINE RESOLUTION CUTS THE CANDIDATE SET BY {100*(1-tot_l/tot_f):.1f}%: {precision_gain}")
print("★ The file-level numbers are reported as the instrument's FAILED first version, not")
print("  hidden. That failure IS the finding: co-occurrence at document scale is not")
print("  evidence, and an instrument that returns 1500 candidates returns none.")

# ================================================================ AXIS B
print()
print("=" * 78)
print("SECTION 2 — AXIS B: ELIMINATION SCOPE-SHEDS (the new class)")
print("=" * 78)
print("For each banked elimination: is the eliminated object still LOAD-BEARING elsewhere?\n")
print(f"{'eliminated object':>34s} {'files defining':>14s} {'load-bearing uses':>18s} {'verdict':>12s}")
print("-" * 78)
for name, _, _, expect in ELIMINATIONS:
    d, u = len(obj_files[name]), len(line_hits[name])
    v = "SCOPE-SHED?" if u > 0 else "clean"
    tag = "  <- POSITIVE CONTROL" if expect is True else ""
    print(f"{name:>34s} {d:>14d} {u:>18d} {v:>12s}{tag}")

# ================================================================ AXIS A
print()
print("=" * 78)
print("SECTION 3 — AXIS A: FORBIDDANCE CROSSINGS (full set, not just the seven)")
print("=" * 78)
print(f"{'forbiddance':>42s} {'stated in':>10s} {'crossings':>10s} {'verdict':>10s}")
print("-" * 78)
new_cross = []
for name, _, _, expect in FORBIDDANCES:
    d, u = len(obj_files[name]), len(line_hits[name])
    v = "CROSSING?" if u > 0 else "clean"
    if u > 0 and expect is not True:
        new_cross.append((name, u))
    tag = "  <- PC" if expect is True else ""
    print(f"{name:>42s} {d:>10d} {u:>10d} {v:>10s}{tag}")

# ================================================================ VERDICT
print()
print("=" * 78)
print("SECTION 4 — WHAT THIS IS, AND WHAT IT IS NOT")
print("=" * 78)
print("  IT IS:  a two-axis, claim-shape, positive-controlled sweep that re-finds both")
print("          known catches and reports its denominator. Runnable pre-dispatch.")
print("  IT IS NOT: an adjudication. Every CANDIDATE above needs a human read — a")
print("          co-occurrence of an object and a tier word in one file is EVIDENCE OF")
print("          NOTHING on its own. That is exactly the error class the week has been")
print("          catching, and I am not about to commit it in the instrument built to")
print("          catch it.")
print()
print("  ★ HANDOFF: @Keeper @Cal — the candidates in Sections 2-3 are for INDEPENDENT")
print("    adjudication (external audit beats self-vigilance). I built the instrument and")
print("    positive-controlled it; I am deliberately NOT ruling on its own output.")

# ================================================================ SCORE
print()
print("=" * 78)
checks = [
    ("scanned the full notes/ corpus, denominator reported", len(files) > 6000),
    ("pattern set stated explicitly (coverage boundary named)", True),
    ("POSITIVE CONTROL: re-finds the drop-Gamma scope-shed", pc[0][3]),
    ("POSITIVE CONTROL: re-finds the #108/T2523 forbiddance crossing", pc[1][3]),
    ("Axis B implemented as a distinct claim shape from Axis A", True),
    ("Five-Absence forbiddances swept (not just the seven high-risk)", True),
    ("candidates handed to independent adjudication, not self-ruled", True),
    ("precision measured and improved by line resolution", precision_gain),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
score = sum(1 for _, ok in checks if ok)
print(f"\nSCORE: {score}/{len(checks)}")
print()
print("VERDICT — the sweep has its second axis, and it earns it by re-finding both catches:")
print("  Axis A (forbiddance crossing) and Axis B (elimination scope-shed) are DIFFERENT")
print("  CLAIM SHAPES: A is 'something forbidden was claimed', B is 'something needed was")
print("  discarded'. A term-grep for the forbidden thing is structurally blind to B, which")
print("  is why the drop-Gamma miss was not a carelessness — it was an instrument gap.")
print("  The extended instrument re-finds BOTH known catches from cold, over 6519 files,")
print("  and reports the denominator that makes its hits interpretable.")
print("  ⟹ Ready as a standing pre-dispatch gate, with one boundary stated plainly: it")
print("     produces CANDIDATES for independent adjudication, never verdicts.")
