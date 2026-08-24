# TOY 5491 -- WALL ATLAS v0.2: THE Z3 REGISTRY SWEEP (adopted watch instrument, R92).
# Elie, 2026-08-24. The parity wall k = m_wt (mod 2) audits the corpus's banked grid claims
# MECHANICALLY, instead of waiting for a collision to trip over one.
# DISCIPLINE: (1) planted-fixture control GATES the read; (2) COVERAGE IS COUNTED -- the
# digit-width lesson: report what the parser understood vs what mentions grids at all.
import re, glob, os
from fractions import Fraction as F
BAR="="*100
print(BAR); print("TOY 5491 -- Z3 registry sweep: off-parity (k, m_wt) claims"); print(BAR)
NOTES="/Users/cskoons/projects/github/BubbleSpacetimeTheory/notes"
N_c=3
# The banked parity law (5484-gated): sector m_wt = N_c*|Q|; grid parity must equal m parity.
# AMENDMENT v0.3 (R93, granted lane), reasons stated per-change:
#  - WORD-BOUNDARY QUALIFIED DICTIONARY: bare 'up'/'down'/'nu' matched inside 'coupling',
#    'group', prose. Only qualified sector tokens remain; bare short tokens are OUT.
#  - ANY-BRACE AWARENESS: a line with >= 2 brace-sets OF ANY KIND (incl. non-numeric like
#    {1,a,a^2}) is AMBIGUOUS -> bucket. v0.2.2 only counted numeric sets, so {1,a,a^2} lines
#    mis-attached their sector to the surviving numeric grid.
#  - CLAIM-vs-DISCUSSION CLASSIFIER (heuristic, LABELLED as such): discussion markers route a
#    hit to the discussion list; only claim-class hits enter the adjudicable list.
SECTOR_PATS=[(r"\bdown[- ](?:quark|type|tower|sector)s?\b",1),
             (r"\bup[- ](?:quark|type|tower|sector)s?\b",2),
             (r"\bcharged[- ]leptons?\b",3),
             (r"\bleptons?\b",3),
             (r"\bneutrinos?\b",0)]
SECTOR_M={"down-quark":1,"up-quark":2,"charged lepton":3,"neutrino":0}  # legacy names for fixture text
ANY_BRACE=re.compile(r"\{[^{}]{1,24}\}")
DISCUSS=re.compile(r"\b(vs|versus|hypothesis|if|would|not|fails?|wrong|misalign\w*|retir\w*|negative|closed|dead|instead of|rather than|placed .* and)\b",re.I)
ODD={"1,3,5","{1,3,5}"}; EVEN={"0,2,4","{0,2,4}"}
GRID_PAT=re.compile(r"\{\s*([0-9])\s*,\s*([0-9])\s*,\s*([0-9])\s*\}")
def grid_parity(trip):
    ps={int(x)%2 for x in trip}
    return None if len(ps)>1 else ps.pop()   # mixed-parity grid = malformed, flag separately
# ---------------- CONTROL: planted fixture must be caught, real F820 rows must pass
head=lambda s:(print("\n"+BAR),print(s),print(BAR))
head("CONTROL (gates the read)")
# AMENDMENT v0.2.1, reason stated: the first run returned 929 hits -- an ATTACHMENT-BY-
# PROXIMITY storm (a line stating BOTH grids correctly got every sector x grid cross-product
# scored; K1181's own correct title was the first "violation"). The instrument committed the
# week's collision-#25 class internally, and my control was too weak to catch it: it had no
# multi-grid must-reject. FIX: pair each sector word with its NEAREST grid by character
# distance, dedupe, and add the must-reject below. Amended BEFORE any hit was adjudicated.
# AMENDMENT v0.2.2, reason stated: nearest-by-character still mis-attaches at word
# boundaries ("leptons" in a dual-grid line lands nearer the wrong grid). The fix is not a
# smarter guess -- it is REFUSING TO GUESS: only SINGLE-GRID lines are scored mechanically;
# multi-grid lines go to a needs-human-read bucket, counted and listed, never scored.
def violations_in(line):
    grids=GRID_PAT.findall(line)
    allbr=ANY_BRACE.findall(line)
    if len(grids)!=1 or len(allbr)>1: return [],0,0,(len(allbr)>1 or len(grids)>1)
    trip=grids[0]; gp=grid_parity(trip)
    if gp is None: return [],0,1,False
    low=line.lower()
    pars={m%2 for pat,m in SECTOR_PATS if re.search(pat,low)}
    v=[(mp_,trip) for mp_ in pars if mp_!=gp]
    return v,len(pars)-len(v),0,False
def is_discussion(line): return bool(DISCUSS.search(line))
ok=True
v,_,_,_=violations_in("the charged lepton tower sits on the even grid {0,2,4}")
print("  must-catch  planted off-parity lepton@{0,2,4}: %s"%("[PASS] caught" if v else "[FAIL]")); ok=ok and bool(v)
v,c,_,multi=violations_in("ODD grid {1,3,5} = down + charged leptons; EVEN grid {0,2,4} = up + neutrinos")
print("  must-reject dual-grid line -> bucket, 0 scored: %s"%("[PASS]" if (multi and not v) else "[FAIL]")); ok=ok and multi and not v
v,c,_,_=violations_in("the down-quark tower on the odd grid {1,3,5} is banked")
print("  must-pass   correct single-grid line: %d violations %s"%(len(v),"[PASS]" if not v else "[FAIL]")); ok=ok and not v
# v0.3 controls -- the can-fail I filed with the nomination:
K1181=open(NOTES+"/Keeper_K1181_up_mass_FK_negative_but_mixing_rides_addresses_not_masses_grace_gets_the_crossshelf_overlap_matrix_math_2026-08-05.md").readlines()[3]
v,_,_,multi=violations_in(K1181)
print("  must-reject K1181's ACTUAL TITLE (v0.2.0's first false positive): %s"%("[PASS] %s"%("bucketed" if multi else "0 scored") if not v else "[FAIL] still flagged")); ok=ok and not v
v,_,_,multi=violations_in("F876 placed up-type at {1,a,a2} and down-quarks at {1,3,5} -- generic misalignment")
print("  must-reject non-numeric-brace line -> ambiguous bucket: %s"%("[PASS]" if (multi and not v) else "[FAIL]")); ok=ok and (multi and not v)
print("  classifier  'up-type CLOSED as disfavored...{1,3,5}' -> %s [labelled heuristic]"%("discussion" if is_discussion("The up-interior doublet-flip hypothesis is CLOSED as disfavored {1,3,5}") else "claim"))
if not ok: raise SystemExit("control failed; sweep not run")
print("  CONTROL PASSES -- proximity pairing catches the plant and clears the correct dual-grid line.")
# ---------------- THE SWEEP
head("SWEEP: every notes/*.md line containing a 3-element degree set NEAR a sector word")
mention=0; parsed=0; violations=[]; consistent=0; malformed=[]; bucket=[]; discussion=[]
for fp in glob.glob(NOTES+"/*.md"):
    try: txt=open(fp,encoding="utf-8",errors="replace").read()
    except Exception: continue
    for ln,line in enumerate(txt.splitlines(),1):
        if not GRID_PAT.search(line): continue
        if not any(w in line.lower() for w in SECTOR_M): continue
        mention+=1
        v,c,mal,multi=violations_in(line)
        parsed+=len(v)+c; consistent+=c
        if multi: bucket.append((os.path.basename(fp),ln))
        if mal: malformed.append((os.path.basename(fp),ln))
        for mpar,trip in v:
            (discussion if is_discussion(line) else violations).append(
                (os.path.basename(fp),ln,"sector-parity %d"%mpar,trip,line.strip()[:90]))
print("  lines mentioning a degree-set AND a sector word : %d"%mention)
print("  (sector, grid) pairs the parser scored          : %d"%parsed)
print("  consistent with the parity wall                 : %d"%consistent)
print("  mixed-parity (malformed) grids flagged          : %d"%len(malformed))
print("  MULTI-GRID lines -> needs-human-read bucket     : %d (listed in file tail; NEVER scored)"%len(bucket))
print("  discussion-class hits (heuristic, NOT adjudicable) : %d"%len(discussion))
print("  *** CLAIM-CLASS OFF-PARITY CANDIDATES: %d ***"%len(violations))
for f,ln,w,trip,txt in violations[:12]:
    print("    %s:%d  [%s vs {%s}]  %s"%(f,ln,w,",".join(trip),txt))
if len(violations)>12: print("    ... and %d more"%(len(violations)-12))
head("COVERAGE, measured (the measurer measured)")
print("""  IN SCOPE : explicit 3-element brace-sets {a,b,c} on the SAME LINE as a sector word from
             the dictionary {down, up, lepton, charged lepton, neutrino}.
  OUT      : prose grids without braces · cross-line references · nu_strat addresses (T2517's
             {5/2, 3/2, 0} are Wallach parameters, NOT k-degrees -- excluded BY DESIGN; scoring
             them here would be the cross-object disease this atlas exists to catch) · per-mode
             k=..., m=... scalar pairs (v0.3 candidate, needs a subscript-aware parser).
  The coverage numbers above are printed so 'the sweep found N' can never silently mean
  'the sweep looked at everything.'""")
head("VERDICT")
print("""  Off-parity count: %d -- *** CANDIDATES FOR SCREENING, NOT FINDINGS (the Grace-screen
  precedent: co-occurrence cannot distinguish discussion from claim). SAMPLE AUDIT of the top
  hits, run before this label was written, identified the dominant false-positive modes:
    (i)  bare-substring sector tokens -- 'up' matches inside 'coupling'/'group'; 'nu' inside
         ordinary prose. The dictionary needs word boundaries and qualified tokens (v0.3).
    (ii) cross-brace attachment when a line's OTHER brace-set is non-numeric ({1,a,a^2}
         does not match the digit pattern, so its partner grid absorbs the sector word).
    (iii) prose ABOUT grid relationships (papers describing both towers) vs address CLAIMS.
  HONEST LABEL: %d candidates, of which an UNKNOWN number are real; adjudication is per-row
  by owners, and v0.3 (word-boundary dictionary, non-numeric-brace awareness, claim-vs-
  discussion classifier) is specified before any candidate is treated as a finding."""%(len(violations),len(violations)))
print("  Watch-instrument status: LIVE. Rerun = one command; additions to the sector dictionary")
print("  or the pattern are AMENDMENTS with reasons, per the frozen-procedure standard.")
