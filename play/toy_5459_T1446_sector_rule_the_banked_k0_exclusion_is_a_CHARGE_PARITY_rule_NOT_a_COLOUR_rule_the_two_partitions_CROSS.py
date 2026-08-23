# TOY 5459 -- T1446 CONTENT AUDIT, the computable half only (R66 line 42).
# Elie, 2026-08-23. Rubric cell: External 3 / flavor. NO CKM VALUES COMPUTED -- sector is DO-NOT-WORK.
# This is mode structure on S^4 x S^1 and nothing else.
#
# THE QUESTION (R66 Section 1): is T1446's coloured/colourless sector rule DERIVED FROM THE GEOMETRY,
# or ASSIGNED TO FIT? Keeper: "the subtraction must FOLLOW from the coloured sector's spectral-mode
# structure and CANNOT be applied to the colourless one."
#
# MY ANGLE: the corpus ALREADY HAS a k=0-exclusion mechanism, banked and target-innocent --
# F820's parity lock. So I do not need to invent one. I need only ask whether the banked one
# PRODUCES T1446's partition. That is decidable arithmetic.

from fractions import Fraction as F
BAR="="*100
def head(s): print("\n"+BAR); print(s); print(BAR)
print(BAR)
print("TOY 5459 -- does the BANKED k=0-exclusion mechanism give T1446's COLOURED/COLOURLESS split?")
print("  Scope: mode structure only. NO CKM value is computed anywhere in this file.")
print(BAR)

# ---------------------------------------------------------------- Part A
head("PART A -- the S^4 mode structure T1446 asserts (verify it exists and is what is claimed)")
print("  Shilov boundary of D_IV^5 (T186, banked): S^{n_C-1} x S^1 = S^4 x S^1.")
print("  Modes: spherical degree k on S^4, SO(2) charge weight m on S^1.")
print("  dim H_k(S^4) = C(k+4,4) - C(k+2,4):")
from math import comb
for k in range(0,7):
    d = comb(k+4,4) - (comb(k+2,4) if k>=2 else 0)
    tag = "  <- the CONSTANT mode: this is the one T1444 subtracts" if k==0 else ""
    print("     k=%d   dim = %-4d %s"%(k,d,tag))
print("  (k=1 -> 5 = SO(5) vector ; k=2 -> 14 = symmetric traceless 5x5. Structure confirmed.)")

# ---------------------------------------------------------------- Part B
head("PART B -- the BANKED k=0 exclusion mechanism: F820 + F817, read from the primary today")
print("  F820 (Lyra, 2026-08-05, K1180, verified in file earlier this session):")
print("     m = N_c*|Q|  (T2470 charge = SO(2) weight ; T2521 quantized in units of 1/N_c)")
print("  F817 parity lock: a mode survives  <=>  k = m (mod 2).")
print("  ==> k=0 is AVAILABLE to a sector  <=>  m is EVEN.")
print()
SECTORS=[("down-quark",  F(1,3), True ),
         ("up-quark",    F(2,3), True ),
         ("charged lep", F(1,1), False),
         ("neutrino",    F(0,1), False)]
Nc=3
print("   sector         Q      m = N_c|Q|   parity   grid      k=0 available?   coloured?")
banked={}
for name,Q,col in SECTORS:
    m=Nc*abs(Q); assert m.denominator==1; m=int(m)
    par = "odd" if m%2 else "even"
    grid = "{1,3,5}" if m%2 else "{0,2,4}"
    k0 = (m%2==0)
    banked[name]=k0
    print("   %-14s %-6s %-12d %-8s %-9s %-16s %s"
          %(name,str(Q),m,par,grid,"YES" if k0 else "NO -- EXCLUDED","yes" if col else "no"))
print("\n   *** The banked mechanism excludes k=0 exactly for ODD m: down-quarks and charged leptons. ***")

# ---------------------------------------------------------------- Part C
head("PART C -- THE DECIDING COMPARISON: does that partition equal T1446's?")
print("  T1446 asserts: (a) CKM = COLOURED (quarks)   -> subtraction applies, k=0 EXCLUDED")
print("                 (b) PMNS = COLOURLESS (leptons) -> NO subtraction, k=0 ALLOWED")
t1446={"down-quark":False,"up-quark":False,"charged lep":True,"neutrino":True}  # k0 available?
print("\n   sector         banked F820/F817 k=0    T1446 needs k=0        agree?")
agree=0; disagree=[]
for name,_,_ in SECTORS:
    b="ALLOWED" if banked[name] else "EXCLUDED"
    t="ALLOWED" if t1446[name] else "EXCLUDED"
    ok = banked[name]==t1446[name]
    if ok: agree+=1
    else: disagree.append(name)
    print("   %-14s %-22s %-22s %s"%(name,b,t,"yes" if ok else "*** NO ***"))
print("\n   agreement: %d of 4 sectors.  DISAGREE on: %s"%(agree,", ".join(disagree)))
print()
print("  *** THE TWO PARTITIONS CROSS. Neither refines the other. ***")
print("     F820/F817 partitions by CHARGE PARITY : {down, charged lepton} exclude k=0")
print("                                             {up,   neutrino}       allow   k=0")
print("     T1446     partitions by COLOUR        : {down, up}             exclude k=0")
print("                                             {charged lepton, neutrino} allow k=0")
print("     They agree on down (excluded) and neutrino (allowed) and DISAGREE on the other two.")
print()
print("  ★ WHY COLOUR CANNOT DO THIS WORK: colour enters only as the MULTIPLIER in m = N_c|Q|.")
print("    N_c = 3 is ODD, so parity(m) = parity(3Q) = parity of the charge in units of 1/3.")
print("    A uniform multiplier cannot PARTITION -- it rescales every sector alike. The partition")
print("    is carried entirely by Q. *** COLOUR IS IN THE FORMULA BUT NOT IN THE SPLIT. ***")

# ---------------------------------------------------------------- Part D
head("PART D -- A SECOND FLAG: is T1444's k=0 the SAME OBJECT as T1446's?")
print("  T1444 (registry, read): 'the -1 subtraction = constant eigenmode k=0 excluded from")
print("     MASS GENERATION.'")
print("  T1446 (registry, read): '(a) CKM (colored, S^4 factor): SPECTRAL MODES -> vacuum")
print("     subtraction -1.'  -- and T1446 applies it to MIXING corrections.")
print()
print("  *** A mass-generation exclusion and a mixing-correction exclusion are not obviously the")
print("      same object. T1446 INHERITS T1444's subtraction across that gap without stating a")
print("      bridge. Same name, possibly different object -- today's recurring disease. ***")
print("  I do not claim they differ. I claim the identification is UNSTATED and load-bearing.")

# ---------------------------------------------------------------- verdict
head("VERDICT -- the computable half")
print(" (1) The S^4 x S^1 mode structure is REAL and banked (T186). dim H_0 = 1, the constant mode")
print("     T1444 subtracts, exists as claimed. Nothing wrong with the substrate.")
print()
print(" (2) *** THE CORPUS'S OWN BANKED k=0-EXCLUSION MECHANISM DOES NOT PRODUCE T1446'S RULE. ***")
print("     F820 (m = N_c|Q|) + F817 (k = m mod 2) excludes k=0 for ODD m -- down-quarks AND")
print("     charged leptons -- and allows it for EVEN m -- up-quarks AND neutrinos.")
print("     T1446 needs it excluded for BOTH quarks and allowed for BOTH leptons.")
print("     AGREEMENT: 2 of 4. The partitions CROSS on up-quarks and charged leptons.")
print()
print(" (3) So the most obvious candidate mechanism in our own corpus is ELIMINATED. That does NOT")
print("     prove T1446's rule is assigned -- another mechanism could exist -- but the burden is")
print("     now explicit: *** WHOEVER DEFENDS T1446 MUST NAME A SECTOR RULE THAT IS NOT F820. ***")
print()
print(" (4) SECOND FLAG, independent of (2): T1444's k=0 is stated for MASS GENERATION; T1446")
print("     applies it to MIXING. The bridge is unstated and load-bearing.")
print()
print(" (5) SCOPE, held: no CKM value computed; this is tier/labelling on an existing theorem, not")
print("     a reopening. K1801-A's suspension is unaffected either way -- I am not ruling on the")
print("     adjacency penalty, only reporting that the geometric derivation offered for it does not")
print("     come from the banked parity mechanism. Lyra's call, with Cal's position-vs-value bar.")
print("     Nothing pushed. CP existence-only.")
