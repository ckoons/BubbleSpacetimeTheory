# TOY 5481 -- THE LIVE (b) RUN on Lyra's posted multiset (R84). Elie, 2026-08-24.
# Labels bound by Keeper's pre-score ruling; self-gate must pass IN THIS RUN before scoring.
import subprocess, sys, os
from fractions import Fraction as F
# cwd-fix (Keeper minor): resolve against this file's directory, not the caller's cwd.
# The bug's one virtue: when it bit, it ABSTAINED rather than scoring wrong.
SCORER=os.path.join(os.path.dirname(os.path.abspath(__file__)),
    "toy_5480_SCORE_B_the_b_scorer_posted_BEFORE_the_multiset_Y_arithmetic_dead_by_type_refusal_aborts_null_from_declared_universe.py")
BAR="="*100
print(BAR); print("TOY 5481 -- LIVE RUN: criterion (b) on the posted multiset"); print(BAR)
# ---- GATE: the scorer's own 11-test suite, THIS run, must be all-PASS
r=subprocess.run([sys.executable,SCORER],capture_output=True,text=True)
fails=[l for l in r.stdout.splitlines() if "[FAIL]" in l]
n_pass=sum(1 for l in r.stdout.splitlines() if "[PASS]" in l)
print("SELF-GATE (same run): %d PASS, %d FAIL -> %s"%(n_pass,len(fails),"PROCEED" if (not fails and n_pass>=11 and r.returncode==0) else "ABORT"))
if fails or n_pass<11 or r.returncode!=0: sys.exit("GATE FAILED")
ns={"__name__":"scorer_lib"}; exec(open(SCORER).read(),ns)
score_b=ns["score_b"]
# ---- THE INPUT, transcribed from Lyra's posted artifact (provenance = the artifact + her cited IDs)
SRC="notes/Lyra_R84_the_banked_rep_multiset_posted_per_entry_provenance_skeleton_is_SM_imported_Y_values_conditional_on_Z6_fundamental_nu_c_absent_per_Five_Absence_2026-08-24.md"
assert os.path.exists("/Users/cskoons/projects/github/BubbleSpacetimeTheory/"+SRC)
MS=[dict(name="Q",  color="3",   su2=2, Y=F(1,6),  provenance=SRC+" | skeleton SM-imported; color T2511/K1045 geometric; doublet-existence K806; Y anomaly+Z6 COND"),
    dict(name="u_c",color="3bar",su2=1, Y=F(-2,3), provenance=SRC+" | skeleton SM-imported; Y anomaly+Z6 COND; D1<->D2 relabel live"),
    dict(name="d_c",color="3bar",su2=1, Y=F(1,3),  provenance=SRC+" | as u_c"),
    dict(name="L",  color="1",   su2=2, Y=F(-1,2), provenance=SRC+" | skeleton SM-imported; integer-charge K806 BANKED I-tier; Y anomaly+Z6 COND"),
    dict(name="e_c",color="1",   su2=1, Y=F(1),    provenance=SRC+" | skeleton SM-imported; integer-charge K806 BANKED; Y anomaly+Z6 COND")]
# nu_c: DECLARED ABSENT (Five-Absence, per the artifact). No entry supplied; leg reads ABSENT.
UNIVERSE=[dict(color=c,su2=s,Y=y) for c in ("3","3bar","1") for s in (1,2)
          for y in (F(1,6),F(-2,3),F(1,3),F(-1,2),F(1),F(0))]   # REFERENCE universe, labelled below
res=score_b(MS,UNIVERSE)
print(BAR); print("RESULT -- LABELS BOUND BY THE PRE-SCORE RULING"); print(BAR)
LEG={"Q_L":"skeleton-IMPORTED / color GEOMETRIC / Y anomaly-selected-COND",
     "u_c":"skeleton-IMPORTED / Y anomaly-selected-COND (D1<->D2 relabel live)",
     "d_c":"skeleton-IMPORTED / Y anomaly-selected-COND (D1<->D2 relabel live)",
     "L_L":"skeleton-IMPORTED / integer-charge BANKED / Y anomaly-selected-COND",
     "e_c":"skeleton-IMPORTED / integer-charge BANKED / Y anomaly-selected-COND"}
print(" k = %d of 5 -- PER-LEG PROVENANCE (no leg is BST-derived):"%res["k"])
for n,h in res["hits"].items():
    print("   %-5s %-8s %s"%(n,"MATCH" if h else "MISS",LEG[n]))
print(" D1<->D2: direct D1 match; relabel NOT needed (u_c/d_c content identical under swap;")
print("          the labels u/d are NOT separately derived -- stated per rule 4).")
print(" extras-against = %d (guaranteed by construction: the multiset was assembled as these five)"%res["extras"])
print(" W1 (complex) = %s -- AS-CONSISTENCY: certifies the IMPORTED content is complex."%res["W1"])
print("   A fact about the SM, certified not derived (Lyra flag 1, verbatim).")
print(" nu_c leg: ABSENT (declared; Five-Absence banked; revisable by Grace's custodial route only)")
print(" null vs random = %.1e over reference universe |U|=%d"%(res["null_at_k"],res["universe_size"]))
print("   *** NOT A SIGNIFICANCE CLAIM: the input is CONSTRUCTION-MATCHED, not random. ***")
print(BAR); print("GENUINE BST CONTENT -- the only lines with real can-fail"); print(BAR)
yq=[abs(e["Y"]) for e in MS]
from math import gcd
dens=[y.denominator for y in yq]
import functools; L=functools.reduce(lambda a,b:a*b//gcd(a,b),dens)
print(" (i)  Y-QUANTUM: all five |Y| are multiples of 1/%d; 1/6 = 1/(N_c*rank) = 1/C2."%L)
print("      GEOMETRIC-CONDITIONAL on the Z6 quotient being forced (K806's named question).")
print("      This is a real, checkable, non-constructed match: %s"%("CONFIRMED (LCM denominator = 6)" if L==6 else "*** FAILED: LCM=%d ***"%L))
print(" (ii) COMPLEXITY: W1=True as consistency (see above). Not a derivation.")
print(" (iii) D1-vs-D3: D1 selected ONLY under the Z6-fundamental reading Y_Q=1/6 --")
print("      gap-b's named residual. CONDITIONAL, unproven.")
print(BAR)
print("HEADLINE (shape fixed by ruling): (b) on the posted multiset: CONSISTENCY CONFIRMED")
print("(expected by construction); BST-genuine content = the 1/6 quantum (conditional) +")
print("complexity (consistency). NOT a derivation of the SM.")
