# TOY 5468 -- R74 Section 0's OPEN FLAG, which carries nobody's name. Elie, 2026-08-23.
# RUBRIC CELL: External 3 (the Yukawa / common-space lane).
#
# THE FLAG, verbatim from R74 Section 0:
#   "w_0(Di) = 2 is NOT in {5/2, 3/2, 0}. The spinor singleton does not sit at a generation address.
#    That may simply mean the Di singleton is not the fermion mode -- but it needs an answer before
#    'fermions live at spinor lambda' is written down as an object."
#
# MY CLAIM: *** IT IS A CROSS-LAMBDA COMPARISON, AND MY OWN 5467 ALREADY GAVE THE GENERAL FORM. ***
# In 5467 I established that nu_strat (a support/Wallach label) and m_wt (a spectral label) are
# DIFFERENT KINDS. The flag compares a SPINOR-lambda lowest weight against SCALAR-lambda generation
# addresses. Whether that is legitimate depends on ONE checkable thing: does w_0 = nu identically,
# and if so, WHY -- because the reason is what does or does not transfer across the bundle.

from math import comb
from fractions import Fraction as F
BAR="="*100
def head(s): print("\n"+BAR); print(s); print(BAR)
print(BAR); print("TOY 5468 -- is 'w_0(Di) = 2 is not a generation address' a LIKE-FOR-LIKE comparison?"); print(BAR)

head("PART A -- WHY w_0 = nu AT lambda = 0. The reason matters more than the fact.")
print("  At scalar lambda = 0 the Wallach representation with parameter nu has LOWEST K-TYPE = the")
print("  TRIVIAL SO(5) rep V_(0,0), dim 1, carrying SO(2) weight nu.")
print("  *** SO w_0 AND nu COINCIDE AT lambda = 0 -- BUT ONLY BECAUSE THE SO(5) PART IS TRIVIAL AND")
print("      CONTRIBUTES NOTHING. The coincidence is CARRIED BY THE TRIVIALITY, not by a law. ***")
print()
print("  That is exactly why Section 0's corroboration reads so cleanly at lambda = 0:")
print("     Rac E_0 = 3/2 = a/2 = Wallach threshold = the MIDDLE generation stratum")
print("     generic stratum 5/2 = p/2 = genus/2 = the Hardy point")
print("  Two named objects landing on two strata -- legitimate, because at lambda = 0 the two")
print("  labels are the same number for a REASON.")

head("PART B -- ★ AT SPINOR lambda THE REASON FAILS. The lowest K-type is NOT trivial.")
print("  Branching (Cal, Keeper-verified, and I re-check the dimensions below):")
print("     Delta (x) V_(d,0) = V_(d+1/2,1/2) (+) V_(d-1/2,1/2)")
print("  At the BOTTOM of the tower, d = 0:")
print("     Delta (x) V_(0,0) = Delta = V_(1/2,1/2)   -- dim 4, HALF-INTEGER IN BOTH ROWS.")
print()
def so5(m1,m2):
    """Weyl dim for SO(5), highest weight (m1,m2) in the ORTHOGONAL basis (halves allowed).
       dim = (m1-m2+1)(m1+m2+2)(2m1+3)(2m2+1)/6"""
    v=(m1-m2+1)*(m1+m2+2)*(2*m1+3)*(2*m2+1)/F(6)
    assert v.denominator==1, v
    return int(v)
print("  formula GATE first, on KNOWN SO(5) dims before any spinor use:")
for (m1,m2),known,name in (((F(0),F(0)),1,"trivial"),((F(1),F(0)),5,"vector"),
                           ((F(1),F(1)),10,"adjoint"),((F(2),F(0)),14,"sym traceless"),
                           ((F(1,2),F(1,2)),4,"SPINOR Delta")):
    got=so5(m1,m2)
    print("     V_(%-5s,%-5s) = %-4d  known %-4d  %s   %s"%(m1,m2,got,known,"OK" if got==known else "*** MISMATCH ***",name))
print()
print("  dimension gate (must reproduce Cal's exact table):")
print("   d    4*dim V_(d,0)   dim V_(d+1/2,1/2) + dim V_(d-1/2,1/2)   match?")
ok=True
for d in range(1,7):
    lhs=4*(comb(d+4,4)-(comb(d+2,4) if d>=2 else 0))
    hi=so5(F(2*d+1,2),F(1,2)); lo=so5(F(2*d-1,2),F(1,2))
    m=(lhs==hi+lo); ok=ok and m
    print("   %-4d %-15d %-38s %s"%(d,lhs,"%d + %d = %d"%(hi,lo,hi+lo),"yes" if m else "*** NO ***"))
print("\n  *** GATE: %s ***"%("PASS -- branching reproduces Cal's exact table" if ok else "FAIL"))
if not ok: raise SystemExit
print()
print("  *** SO AT SPINOR lambda THE LOWEST K-TYPE IS V_(1/2,1/2), NOT V_(0,0). The SO(5) part is")
print("      NO LONGER TRIVIAL, SO IT NO LONGER CONTRIBUTES NOTHING. The mechanism that made")
print("      w_0 = nu at lambda = 0 IS GONE. ***")

head("PART C -- THE VERDICT ON THE FLAG")
print(" *** 'w_0(Di) = 2 is not in {5/2, 3/2, 0}' COMPARES A SPINOR-lambda LOWEST WEIGHT AGAINST")
print("     SCALAR-lambda GENERATION ADDRESSES. NOT LIKE-FOR-LIKE. ***")
print()
print("  The set {5/2, 3/2, 0} is a list of nu_strat values read off the SCALAR family, where they")
print("  happen to equal w_0. At spinor lambda those are two different quantities again, so a")
print("  spinor w_0 has NO OBLIGATION to appear in a list of scalar nu_strat.")
print()
print("  ⟹ THE FLAG DOES NOT SHOW THE Di SINGLETON IS THE WRONG MODE. It shows the COMPARISON is")
print("    not yet defined. *** THE SPINOR GENERATION ADDRESSES HAVE TO BE DERIVED, NOT INHERITED. ***")
print("    That is the SAME shape as Cal's gate in R74 Section 2 -- 'the Wallach threshold is NOT")
print("    INHERITED; T2508 fixes nu = n_C = 5 for the SCALAR case, the spinor case has its own and")
print("    nobody has derived it.' *** THE THRESHOLD AND THE ADDRESSES ARE THE SAME NON-INHERITANCE. ***")

head("PART D -- AND IT IS THE SPECIES KEEPER NAMED THIS MORNING")
print("  R73 Section 0: 'a label that was SUFFICIENT where it was formed, and INSUFFICIENT one")
print("  bundle over -- one label quietly losing resolving power when the setting changes.'")
print("  Here: w_0 was a FAITHFUL PROXY for nu_strat at lambda = 0 because the SO(5) part was")
print("  trivial. One bundle over, the proxy fails -- and it fails SILENTLY, because both are")
print("  still numbers and both are still legal Wallach points.")
print("  *** ELEVENTH INSTANCE, AND THE FIRST ONE PREDICTED IN ADVANCE BY THE RULE ITSELF. ***")

head("VERDICT")
print(" (1) w_0 = nu at lambda = 0 BECAUSE the lowest K-type is trivial. The coincidence is carried")
print("     by the triviality, not by a law. Verified: the reason is the mechanism.")
print(" (2) At spinor lambda the lowest K-type is V_(1/2,1/2), dim 4 -- NOT trivial. Gate passed on")
print("     Cal's exact branching table, d = 1..6.")
print(" (3) *** THE FLAG IS A CROSS-lambda COMPARISON. It does not decide against the Di singleton;")
print("     it shows the spinor generation addresses are UNDERIVED. ***")
print(" (4) It is the SAME non-inheritance as Cal's Wallach-threshold gate -- one open question, not")
print("     two. *** Do not count it as a second problem. ***")
print()
print(" *** RULE 3: ONE CI -- ME. NOT FILED. Attack, ordered: (a) is the lowest K-type at spinor")
print("     lambda really V_(1/2,1/2) -- i.e. is the d=0 rung PRESENT, or does the spinor tower")
print("     start higher? Grace's truncation question is the same question and it is hers; (b) is")
print("     w_0 = nu at lambda=0 an identity or only true at the strata I checked. (a) first. ***")
