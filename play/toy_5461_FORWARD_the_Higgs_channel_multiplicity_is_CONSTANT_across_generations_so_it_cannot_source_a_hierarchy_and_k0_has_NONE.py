# TOY 5461 -- FORWARD (R68 Rule 1). Elie, 2026-08-23. Tier-1: up-masses, saturation not FK.
# Rubric cell: External 3 (SM params) / up sector.
#
# RULE 1 COMPLIANCE, stated up front: this does NOT start from a number. It starts from an object
# (the Higgs channel of T2518), COUNTS what that object gives across the forced addresses, and only
# then looks at what the count implies. No target was consulted to build the count.
#
# RULE 4 -- RECONNECTED FIRST, from the registry and my own prior toy:
#   T2514: the top saturates the Shilov boundary; y_t = 1 EXACTLY, by CAUCHY-SCHWARZ SATURATION of
#          the fermion<->Higgs-boundary overlap (y = 1 iff the modes are parallel).
#   T2518 (mine, K773): the physical Yukawa vertex is the OPPOSITE-CHIRALITY BILINEAR
#          top_L (x) top_R = (2,1)(x)(1,2) = (2,2) of SO(4) = SU(2)_L x SU(2)_R -- the UNIQUE Higgs channel.
#   F820:  up-type sits on the EVEN parity grid k in {0,2,4} (m = N_c|Q| = 2, F817 lock k = m mod 2).
#   Toy 5060 (mine, 08-05): the even-grid FK ladder does NOT reproduce the top-heavy up masses.
#          It left an explicit OPEN STRUCTURAL CALL: is the up-tower (a) OFF the ladder, or
#          (b) at {0,2,4} but saturation-overridden? "A structural call for Lyra/team."
#   NOT USED: T2092's y_t = 1 - 1/n_C^3. That form is number-first and Rule 1 forbids originating from it.
#
# THE FORWARD QUESTION: how many (2,2) Higgs channels does each forced address carry?
# Count first. Interpret after.

from math import comb
BAR="="*100
def head(s): print("\n"+BAR); print(s); print(BAR)
print(BAR); print("TOY 5461 -- FORWARD COUNT: the (2,2) Higgs-channel multiplicity across the forced grid")
print("  No number is targeted. Object -> count -> look."); print(BAR)

def dim_Hk(k):   # degree-k harmonics on S^4 = SO(5) irrep (k,0), symmetric traceless rank k
    return comb(k+4,4) - (comb(k+2,4) if k>=2 else 0)

head("PART A -- the branching SO(5) -> SO(4), verified by dimension before it is used")
print("  Object: H_k(S^4) = SO(5) irrep (k,0) = symmetric traceless rank-k tensors on R^5.")
print("  Branching rule used: H_k|_{SO(4)} = (+)_{j=0..k} [symmetric traceless rank j of SO(4)]")
print("  and symmetric traceless rank j of SO(4) = SU(2)xSU(2) is the irrep (j/2, j/2), dim (j+1)^2.")
print("\n  *** VERIFY IT BEFORE USING IT: sum_{j=0..k} (j+1)^2 must equal dim H_k(S^4). ***")
print("   k    dim H_k(S^4)   sum_{j<=k}(j+1)^2   match?")
ok=True
for k in range(0,9):
    lhs=dim_Hk(k); rhs=sum((j+1)**2 for j in range(0,k+1))
    m = (lhs==rhs); ok = ok and m
    print("   %-4d %-14d %-19d %s"%(k,lhs,rhs,"yes" if m else "*** NO ***"))
print("\n  *** BRANCHING GATE: %s ***"%("PASS -- the rule reproduces every dimension, proceed"
      if ok else "FAIL -- rule wrong, nothing below is read"))
if not ok: raise SystemExit

head("PART B -- THE COUNT. Multiplicity of the Higgs channel (2,2) = (1/2,1/2) = j=1.")
print("  T2518: the vertex is top_L (x) top_R = (2,1)(x)(1,2) = (2,2). In (j_L, j_R) labels that is")
print("  (1/2, 1/2), which is the j = 1 symmetric-traceless-rank-1 piece = the SO(4) VECTOR.")
print("\n   address k    SO(4) content (j/2,j/2), j=0..k        multiplicity of (1/2,1/2)")
mult={}
for k in range(0,7):
    content=", ".join("(%s,%s)"%(("%d"%(j//2) if j%2==0 else "%d/2"%j),("%d"%(j//2) if j%2==0 else "%d/2"%j)) for j in range(0,k+1))
    m = 1 if k>=1 else 0
    mult[k]=m
    tag=""
    if k in (0,2,4): tag = "   <- FORCED even grid (F820)"
    print("   k=%-10d %-38s %d%s"%(k,content[:37],m,tag))

head("PART C -- WHAT THE COUNT SAYS. Two findings, and neither was targeted.")
print(" (1) *** THE MULTIPLICITY IS CONSTANT AT 1 FOR EVERY k >= 1. ***")
print("     On the forced even grid {0,2,4}:  k=2 -> 1 channel,  k=4 -> 1 channel.")
print("     The two massive up generations carry THE SAME NUMBER of Higgs channels.")
print("     ==> *** CHANNEL MULTIPLICITY CANNOT SOURCE THE UP HIERARCHY. *** Whatever makes")
print("         m_c << m_t, it is not how many ways the generation can couple to the Higgs.")
print("         This is a FORWARD NEGATIVE: it removes a route before anyone spends a day on it.")
print()
print(" (2) *** k = 0 CARRIES ZERO (2,2) CHANNELS. *** Not 'fewer' -- NONE. The constant mode has")
print("     no SO(4) vector piece at all, so it cannot couple through T2518's unique Higgs vertex.")
print("     That is a QUALITATIVE GAP, not a hierarchy: the k=0 member is MASSLESS through this vertex.")

head("PART D -- IT RESOLVES TOY 5060's OPEN STRUCTURAL CALL, and it cuts BOTH ways")
print("  F820 puts BOTH up-quarks AND neutrinos on the even grid starting at k=0.")
print("  The count says the k=0 member gets NO mass from the Higgs vertex. So:")
print()
print("   NEUTRINO  : lightest neutrino MASSLESS. *** AGREES with the banked m_1 = 0 (F619). ***")
print("               And it agrees for a DIFFERENT reason than F619's nu=0 Wallach argument --")
print("               my own 5060 flagged that the FK norm at k=0 is 1, not 0, so 'FK gives zero'")
print("               was never the reason. THIS is a reason: no channel, not a small norm.")
print("   UP-QUARK  : predicts m_u = 0. *** OBSERVED m_u IS NOT ZERO. FALSIFIED for the up sector. ***")
print()
print("  ==> 5060 asked: is the up-tower (a) OFF the ladder, or (b) on {0,2,4} but saturation-overridden?")
print("      *** THE COUNT ANSWERS IT: the up-tower CANNOT have its first generation at k=0 through")
print("          this vertex. Option (b) fails at k=0 specifically -- saturation can override a")
print("          MAGNITUDE, but it cannot manufacture a channel that the decomposition does not")
print("          contain. Either the up-tower starts at k=2, or m_u comes from a different vertex. ***")

head("VERDICT")
print(" (1) Branching gate PASSED (dimensions reproduce for k=0..8) before any count was read.")
print(" (2) FORWARD NEGATIVE: (2,2) multiplicity is CONSTANT = 1 for all k >= 1, so channel counting")
print("     cannot source the up hierarchy. Route removed, forward, before it cost a day.")
print(" (3) FORWARD STRUCTURAL RESULT: k=0 carries ZERO Higgs channels -- a gap, not a hierarchy.")
print("     Agrees with the banked massless lightest neutrino, and for a better reason than the")
print("     'FK norm = 0' story my own 5060 already showed was wrong.")
print(" (4) It resolves 5060's open call against option (b) at k=0: saturation can override a")
print("     magnitude, not manufacture an absent channel.")
print()
print(" *** RULE 3: THIS IS A PARTIAL CLAIM AND IT IS UNCONFIRMED. It needs a SECOND CI before it")
print("     is filed as anything. The branching rule is standard and gate-verified here, but the")
print("     IDENTIFICATION of (2,2) with j=1 and the physical reading of 'no channel => massless'")
print("     are the load-bearing steps and they are exactly what a second reader should attack. ***")
print(" Nothing pushed. Nothing banked. CP existence-only.")
