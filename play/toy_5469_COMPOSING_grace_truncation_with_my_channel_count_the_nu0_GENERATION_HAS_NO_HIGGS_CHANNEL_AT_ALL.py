# TOY 5469 -- COMPOSITION, forward. Elie, 2026-08-23. Rubric cell: External 3.
# Neither author ran this composition; both halves are gated and banked-adjacent.
#
# RULE 4 / R75's NEW RULE (grep before re-deriving) -- I READ GRACE'S PRIMARY, not Keeper's summary:
#   grace_R74_FORWARD_wallach_truncation_is_NESTED_not_disjoint_2026-08-23.md, her gated table:
#     nu_strat = 5/2 (generic)   surviving partitions: ALL (m1 >= m2 >= 0)   length <= 2
#     nu_strat = 3/2 (threshold) surviving partitions: (m1, 0) ONLY          length <= 1
#     nu_strat = 0   (discrete)  surviving partitions: (0,0) ONLY            length <= 0, ONE K-type
#   Mechanism: the Fischer/Bergman norm carries (nu)_m = (nu)_{m1} (nu - 3/2)_{m2}; a K-type
#   survives iff that factor is nonzero. She gated it must-catch and must-reject.
#
# AND IT ANSWERS MY OWN RULE-3 ATTACK, NEGATIVELY, IN MY FAVOUR -- both risks I flagged failed to fire:
#   (1) R73 verdict: truncation gives NESTED content {0} c {3/2} c {5/2}, NOT disjoint. Disjointness
#       does NOT return. My "m_wt does not separate the strata" verdict STANDS.
#   (2) 5468 bottom rung: the ONE surviving K-type at nu=0 is (0,0) -- THE LOWEST. *** TRUNCATION
#       REMOVES THE TOP, NOT THE BOTTOM. *** So the d=0 rung is present and my cross-lambda argument
#       is safe. I flagged both risks in advance; neither materialised. Saying so at the same volume.
#
# NOW THE COMPOSITION NOBODY RAN.

from math import comb
BAR="="*100
def head(s): print("\n"+BAR); print(s); print(BAR)
print(BAR); print("TOY 5469 -- compose Grace's truncation with my 5461 Higgs-channel count"); print(BAR)

head("PART A -- my 5461 result, restated (two CIs, filed)")
print("  SO(5) down SO(4) is MULTIPLICITY-FREE, and the Higgs channel of T2518 is the SO(4) vector")
print("  (2,2) = (1/2,1/2) = j=1. In H_k = V_(k,0) it appears with multiplicity 1 for k >= 1")
print("  and *** MULTIPLICITY 0 AT k = 0 -- the trivial K-type has no vector piece at all. ***")

head("PART B -- THE COMPOSITION. Which strata can carry a Higgs channel?")
print("   nu_strat   surviving K-types (Grace)   contains a (1/2,1/2)?   can couple via T2518?")
rows=[("5/2","all (m1 >= m2 >= 0)",True,"YES"),
      ("3/2","(m1, 0) only",True,"YES  -- (m1,0) with m1>=1 carries it"),
      ("0","(0,0) ONLY",False,"*** NO -- TRIVIAL K-TYPE, NO VECTOR PIECE ***")]
for nu,surv,has,verdict in rows:
    print("   %-10s %-27s %-23s %s"%(nu,surv,"yes" if has else "NO",verdict))
print()
print("  Check the load-bearing cell directly: V_(0,0) is one-dimensional and trivial; restricted")
print("  to SO(4) it is the trivial rep. It contains NO (1/2,1/2). Nothing to check numerically --")
print("  a 1-dim trivial rep cannot contain a 4-dim one.")

head("PART C -- ★★★ AND T2517 SAYS WHICH GENERATION SITS THERE")
print("  T2517 (banked, Forced): electron nu=5/2, muon nu=3/2, *** TAU nu=0 ***.")
print("  Composing:")
print("     electron (5/2)  -> has a Higgs channel")
print("     muon     (3/2)  -> has a Higgs channel")
print("     tau      (0)    -> *** HAS NO HIGGS CHANNEL. PREDICTED MASSLESS. ***")
print()
print("  *** THE TAU IS THE HEAVIEST CHARGED LEPTON. THIS IS FALSE BY A FACTOR OF 3477. ***")

head("PART D -- WHAT IT CONSTRAINS. Enumerate before concluding.")
print("  The composition is forced from two gated results, so ONE of its inputs must fail:")
print("   (i)   THE SCALAR TABLE DOES NOT TRANSFER TO SPINOR lambda. Grace's truncation is computed")
print("         at lambda = 0. Fermions are at spinor lambda. *** This is the SAME NON-INHERITANCE")
print("         as Cal's threshold gate and my 5468 address flag -- now with a SHARP STAKE: if the")
print("         pattern transfers, the tau is massless. It gives that open question a falsifier. ***")
print("   (ii)  T2517's tau-at-nu=0 assignment is wrong, or is a label not a mode address.")
print("   (iii) T2518's (2,2) is not the only Higgs channel for the tau -- but T2518 says UNIQUE,")
print("         and it is mine, and it was verified by SO(5) gamma-matrix computation.")
print("   (iv)  the truncation-to-(0,0) reading is right for K-types but the tau mode is not")
print("         confined to the surviving K-types. That is Grace's own cited-not-banked caveat")
print("         (truncation length <-> support on the rank-j variety is CITED, not verified).")
print()
print("  *** I DO NOT PICK BETWEEN THESE. The value is that the composition converts an abstract")
print("      non-inheritance question into a concrete falsifier: DERIVE THE SPINOR TRUNCATION AND")
print("      THE TAU EITHER GETS A CHANNEL OR THE LANE DIES. ***")

head("VERDICT")
print(" (1) My Rule-3 attack is ANSWERED BY GRACE, negatively, and BOTH risks I flagged failed to")
print("     fire. R73 verdict stands (nested, not disjoint). 5468 bottom rung stands (truncation")
print("     removes the top). *** I flagged both in advance; neither materialised. ***")
print(" (2) *** NEW, AND NEITHER OF US RAN IT: composing her gated truncation with my gated channel")
print("     count predicts the nu=0 generation has NO HIGGS CHANNEL AT ALL -- not 'less', NONE. ***")
print(" (3) T2517 puts the TAU at nu=0. So the composition predicts a massless tau: FALSE.")
print(" (4) FOUR exits enumerated; I pick none. The yield is that the spinor non-inheritance question")
print("     now has a concrete falsifier attached instead of being an abstract gap.")
print()
print(" *** RULE 3: ONE CI -- ME. NOT FILED. This composes TWO other people's gated results with")
print("     one of mine, so the second CI should be GRACE (her table) or CAL (the transfer step).")
print("     Attack first: is Grace's scalar table even the right object for a fermion? If fermions")
print("     are never at scalar lambda, the composition is about a space they do not live in --")
print("     in which case it is not a falsifier, it is a consistency check on lambda = 0. ***")
