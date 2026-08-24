# TOY 5485 -- BOOK-DAY ITEM 2/5 INSTRUMENT. Elie, 2026-08-24.
# Consumes: the DECIDED map family (A or B) + Lyra's reading-ledger path (must resolve on disk).
# Emits: the PRE-REGISTERED consequence table -- written NOW, before any quote lands, so the
# reading cannot be scored after the fact. Attestation-gated per the W2/A1 pattern.
import os, sys
from fractions import Fraction as F
BAR="="*100
rho=(F(5,2),F(3,2),F(1,2))
NONC=[(1,-1,0),(1,0,-1),(1,0,0),(1,0,1),(1,1,0)]
def q_of(c):
    lp=(F(c)+rho[0],F(1,2)+rho[1],F(1,2)+rho[2])
    ps=[sum(lp[k]*F(b[k]) for k in range(3)) for b in NONC]
    if any(p==0 for p in ps): return None
    return sum(1 for p in ps if p<0)
# ---- PRE-REGISTERED CONSEQUENCES (from R82's ruled four-branch table + toy 5479; frozen here)
CONSEQ={
 "A": dict(maps="c = +-E0 - 5/2", fermion_c=("-1/2","-9/2"), q=("WALL","WALL"),
      a_mode="SILENCE -- P4: every E0=2 fermion ON a wall; the chamber formula is silent on the SM",
      wall_finding="*** FIRES -- my 5477-era ON-WALL structural finding gets its final label: REAL.",
      followup="the SM fermions sit AT reduction points like the singletons; that is a new structural fact needing an owner"),
 "B": dict(maps="c = -E0 | E0 - 5", fermion_c=("-2","-3"), q=(q_of(-2),q_of(-3)),
      a_mode="NAMED LOSS -- P3.i: all positive-energy fermions one parity; no chirality split",
      wall_finding="DIES -- final label: artefact of the dead 5477 pin, as recorded in 5478/5479",
      followup="(a) closes as the flat pre-registered loss; no reduction-point structure claimed"),
}
def fire(family, ledger):
    base="/Users/cskoons/projects/github/BubbleSpacetimeTheory/"
    if not (ledger and os.path.exists(base+ledger)):
        raise RuntimeError("REFUSED: family decision requires Lyra's reading-ledger on disk; %r does not resolve"%ledger)
    if family not in CONSEQ:
        raise RuntimeError("REFUSED: family must be 'A' or 'B', got %r -- a third reading is a FINDING, route to Keeper, do not force it into this table"%family)
    C=CONSEQ[family]
    print("ATTESTATION: family %s decided per ledger %s"%(family,ledger))
    print("  maps: %s ; fermion c(E0=2) = %s ; q = %s"%(C["maps"],C["fermion_c"],C["q"]))
    print("  (a) FAILURE MODE, final : %s"%C["a_mode"])
    print("  WALL FINDING, final     : %s"%C["wall_finding"])
    print("  FOLLOW-UP               : %s"%C["followup"])
    print("  c_conv CROSS-CHECK      : *** SLOT -- requires Grace's confirmation against her")
    print("                            c_conv = 3/2 chain; NOT computed here (her object, her check)")
if __name__=="__main__":
    print(BAR); print("TOY 5485 -- family-decision instrument: SELF-TESTS (live fire held for the ledger)"); print(BAR)
    try: fire("A","notes/DOES_NOT_EXIST.md"); print("  [FAIL] T1")
    except RuntimeError as e: print("  [PASS] T1 refusal without ledger: %s"%str(e)[:60])
    try: fire("C","notes/CI_BOARD.md"); print("  [FAIL] T2")
    except RuntimeError as e: print("  [PASS] T2 third-reading refused as a FINDING: %s"%str(e)[:60])
    print("  T3/T4 fixture renders (CI_BOARD as stand-in path, loudly not a ledger):")
    for fam in ("A","B"):
        print("  --- FIXTURE family %s ---"%fam); fire(fam,"notes/CI_BOARD.md")
    print(BAR)
    print("PRE-REGISTERED AND HELD. Live fire = fire(<family>, <BOOKDAY_LEDGER path>) when Lyra posts.")
    print("The consequence table above is FROZEN as of this file's mtime -- before any quote landed.")
