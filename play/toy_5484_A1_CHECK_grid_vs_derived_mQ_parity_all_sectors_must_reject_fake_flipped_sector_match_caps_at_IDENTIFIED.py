# TOY 5484 -- A1's CHECK (R87 Section 1). Elie, 2026-08-24.
# Grid parity vs derived m_Q parity, all four sectors; must-reject = fake flipped sector.
# THE BAR, encoded: a passing match is NECESSARY, NOT SUFFICIENT -- this instrument can emit
# at most IDENTIFIED-pending. DERIVED requires Lyra's mechanism artifact + Cal's gate; the
# verdict line defers, it does not self-score. (Same attestation pattern as W2.)
from fractions import Fraction as F
import os
BAR="="*100
print(BAR); print("TOY 5484 -- A1 check: does derived m_Q parity track the banked grid parity?"); print(BAR)
# INPUTS, each with provenance:
#  - charges Q: SM electric charges (observational input, declared, same class as Five-Absence)
#  - m_Q = N_c*|Q|: F820's charge-to-degree normalization (T2470 weight, T2521 quantization)
#  - grid assignment: F817/F820 banked split (odd {1,3,5} = down + charged leptons; even {0,2,4}
#    = up + neutrinos), blind-forced per T1929 (Cal's target-innocence note)
N_c=3
SECTORS=[("down-quark",F(1,3),"odd"),("up-quark",F(2,3),"even"),
         ("charged-lepton",F(1),"odd"),("neutrino",F(0),"even")]
def check(sectors):
    rows=[];allok=True
    for name,Q,grid in sectors:
        m=N_c*abs(Q); assert m.denominator==1, "m_Q not integer for %s"%name
        par="odd" if int(m)%2 else "even"
        ok=(par==grid); allok=allok and ok
        rows.append((name,Q,int(m),par,grid,ok))
    return rows,allok
print("\nPART A -- the live check, all four sectors:")
print("   sector           Q      m_Q=N_c|Q|  m_Q parity   banked grid   match?")
rows,allok=check(SECTORS)
for n,Q,m,p,g,ok in rows:
    print("   %-16s %-6s %-11d %-12s %-13s %s"%(n,Q,m,p,g,"YES" if ok else "*** NO ***"))
print("   => ALL FOUR SECTORS: %s"%("MATCH" if allok else "MISMATCH"))
print("\nPART B -- MUST-REJECT: a fake sector with flipped parity must FAIL:")
fake=[("fake-lepton",F(1),"even")]        # m_Q = 3, odd, claimed even grid
_,fok=check(fake)
print("   fake-lepton (m_Q=3 odd, claims even grid) -> %s"%("*** WRONGLY PASSED ***" if fok else "REJECTED, as required"))
print("\nPART C -- VERDICT LINE (defers; cannot self-score DERIVED):")
MECH=os.environ.get("A1_MECHANISM_ARTIFACT","")   # Lyra's derivation, when it posts
base="/Users/cskoons/projects/github/BubbleSpacetimeTheory/"
if allok and not fok:
    if MECH and os.path.exists(base+MECH):
        print("   MATCH CONFIRMED + mechanism artifact present (%s)."%MECH)
        print("   VERDICT: DEFERRED TO CAL'S GATE -- this instrument attests the match and the")
        print("   artifact's existence only; DERIVED is Cal's word, not mine.")
    else:
        print("   MATCH CONFIRMED, all sectors, must-reject fires. NO MECHANISM ARTIFACT SUPPLIED.")
        print("   *** VERDICT CAP: IDENTIFIED-pending -- the match is NECESSARY, NOT SUFFICIENT")
        print("       (R87's bar, fixed before the work). A re-observation of agreement is not a")
        print("       derivation, and this instrument is structurally unable to claim one. ***")
else:
    print("   CHECK FAILED -- no verdict; report the failing row.")
