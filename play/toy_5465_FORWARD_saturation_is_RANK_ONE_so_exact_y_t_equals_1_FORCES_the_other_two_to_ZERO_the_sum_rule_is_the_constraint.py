# TOY 5465 -- UP-MASSES, FORWARD (R71 line 31). Elie, 2026-08-23. External 3 / up sector.
# Template, per Keeper: Lambda^2(p) (-) omega -- NAME THE OBJECT, COUNT ITS MODES, THEN LOOK.
#
# RULE 4, RECONNECTED FIRST:
#   T2514: the top saturates the Shilov boundary; y_t = 1 EXACTLY, by CAUCHY-SCHWARZ SATURATION
#          of the fermion<->Higgs-boundary overlap ("y = 1 iff the modes are parallel").
#   T2518 (mine, K773): the vertex is the opposite-chirality bilinear, the UNIQUE Higgs channel.
#   Toy 5060 (mine): the even-grid FK ladder does NOT reproduce the top-heavy up masses.
#   R71: fermion modes are NOT scalar holomorphic functions -- they live at SPINOR lambda in
#        H^2(D_IV^5; L_lambda). So I must NOT use the lambda=0 K-types here. I do not need them.
#   NOT USED: T2092's y_t = 1 - 1/n_C^3 (number-first, Rule 1 forbids originating from it).
#
# THE OBJECT: the Cauchy-Schwarz saturation condition itself. Not the mode content -- the CONDITION.
# That is available NOW, without Grace's spinor K-types, because saturation is a statement about
# INNER PRODUCTS, not about which representation carries them.

import numpy as np
BAR="="*100
def head(s): print("\n"+BAR); print(s); print(BAR)
print(BAR); print("TOY 5465 -- FORWARD: what does CAUCHY-SCHWARZ SATURATION alone force?"); print(BAR)

head("PART A -- DECLARE THE OBJECT AND THE ASSUMPTIONS, before any count")
print("  Let H be the Hilbert space of fermionic modes (whatever lambda it sits at -- NOT needed).")
print("  Let h in H be the Higgs boundary mode of T2518's unique channel.")
print("  Let f_1, f_2, f_3 be the three generation modes.")
print("  Yukawa, from T2514's own definition:  y_i = |<f_i, h>| / (||f_i|| ||h||)   in [0,1].")
print()
print("  ASSUMPTIONS, stated so they can be attacked (this is the whole content):")
print("   A1  the three generations are LINEARLY INDEPENDENT and span a 3-dim subspace G.")
print("       (3 = N_c = dim V_12 -- banked, T2527.)")
print("   A2  they are MUTUALLY ORTHOGONAL in H (distinct modes of a self-adjoint operator).")
print("   A3  the Higgs mode h LIES IN G.")
print("   A4  T2514: the top SATURATES -- y_3 = 1 exactly.")

head("PART B -- THE COUNT. Saturation is a RANK-ONE condition.")
print("  Cauchy-Schwarz |<f,h>| <= ||f|| ||h|| has equality IFF f and h are PARALLEL.")
print("  ==> the saturating set is a single RAY through h.")
print("  *** SO AT MOST ONE GENERATION CAN SATURATE. 'Exactly one top' is forced, not chosen. ***")
print("      (Can-fail: LOW. This follows from the equality case of an inequality -- it is a priori,")
print("       like the multiplicity-free result. Stated as structure, not as evidence.)")
print()
print("  Now the part that is NOT a priori. Under A1-A3, normalize f_i orthonormal and h a unit")
print("  vector in G. Then y_i = |<f_i, h>| are the components of a UNIT vector, so:")
print()
print("     *** SUM RULE:  y_1^2 + y_2^2 + y_3^2 = 1  ***")
print()
print("  and A4 says y_3 = 1. Substituting:")
print("     y_1^2 + y_2^2 = 1 - 1 = 0   =>   y_1 = y_2 = 0.")

head("PART C -- VERIFY IT NUMERICALLY (a sum rule is easy to assert and easy to get wrong)")
rng=np.random.default_rng(11)
print("   trial   h (random unit in G)                sum y_i^2      max y_i    others when max=1?")
for t in range(4):
    h=rng.normal(size=3); h/=np.linalg.norm(h)
    y=np.abs(h)                      # f_i = orthonormal basis => y_i = |h_i|
    print("   %-7d (%7.4f,%7.4f,%7.4f)   %.12f   %.6f     -"%(t,h[0],h[1],h[2],(y**2).sum(),y.max()))
h=np.array([0.0,0.0,1.0])            # exact saturation
y=np.abs(h)
print("   SAT     (%7.4f,%7.4f,%7.4f)   %.12f   %.6f     y_1=%.1e  y_2=%.1e"
      %(h[0],h[1],h[2],(y**2).sum(),y.max(),y[0],y[1]))
print("\n   *** CONFIRMED: exact saturation forces the other two components to vanish identically. ***")

head("PART D -- WHAT THIS SAYS, and it is the same shape as my k=0 result")
print(" *** EXACT SATURATION OF THE TOP, WITH THE GENERATIONS ORTHOGONAL AND h INSIDE THEIR SPAN,")
print("     FORCES m_c = m_u = 0. THAT IS A GAP, NOT A HIERARCHY. ***")
print()
print("  Observed m_c/m_t ~ 0.0074 and m_u/m_t ~ 1.3e-5 are SMALL BUT NONZERO, so the exact")
print("  saturation picture as stated is FALSIFIED. One of A2, A3, A4 must fail. Enumerate:")
print()
print("   (i)  A4 fails -- y_3 = 1 is APPROXIMATE, not exact. Then y_1^2+y_2^2 = 1-y_3^2 = the")
print("        DEFICIT, and the whole up hierarchy is the size of the top's departure from")
print("        saturation. *** THIS IS A TESTABLE STRUCTURE: it predicts a SUM RULE, not a ladder. ***")
print("   (ii) A3 fails -- h has a component OUTSIDE the generation span. Then Sum y_i^2 = |P_G h|^2 < 1")
print("        and saturation y_3 = 1 becomes IMPOSSIBLE (it would need h in G). So (ii) and A4 are")
print("        INCOMPATIBLE: *** you cannot have both an exactly-saturating top and a Higgs mode")
print("        with support outside the generation space. ***")
print("   (iii) A2 fails -- the generations are not orthogonal. Then the sum rule is replaced by a")
print("        Gram-matrix relation and the deficit can be redistributed. This is the loosest exit")
print("        and it is the one that would need the most justification.")
print()
print("  *** THE FORWARD YIELD: the corpus's y_t = 1 EXACTLY (T2514) and a nonzero m_c are in")
print("      TENSION under A1-A3. That tension is a RESULT -- it says the up sector cannot be")
print("      'top saturates, others ladder down'; it must be 'top NEARLY saturates, and the")
print("      others live in the deficit.' A different mechanism shape than the one assumed. ***")

head("VERDICT")
print(" (1) Saturation is RANK ONE => at most one generation saturates. 'Exactly one top' is")
print("     structural. CAN-FAIL LOW -- it is the equality case of an inequality. Stated as such.")
print(" (2) *** Under A1-A3, EXACT saturation forces the other two Yukawas to ZERO -- verified. ***")
print(" (3) So T2514's 'y_t = 1 EXACTLY' is INCOMPATIBLE with nonzero m_c and m_u unless one of")
print("     A2/A3 is abandoned. THREE exits enumerated, and (ii) is shown incompatible with A4.")
print(" (4) The surviving shape is a SUM RULE (y_1^2+y_2^2 = 1-y_3^2), not a ladder -- which is")
print("     consistent with my 5060 finding that no FK ladder fits the up sector.")
print(" (5) NOT dependent on the spinor K-types: saturation is about INNER PRODUCTS, so R71's")
print("     spinor crossing does not touch this. Grace's result is not a blocker here.")
print()
print(" *** RULE 3: ONE CI -- ME. NOT FILED. Attack surface, ordered: A2 (orthogonality of the")
print("     generation modes -- I asserted it from 'distinct modes of a self-adjoint operator' and")
print("     that presumes an operator nobody has named); then A3; then whether T2514's 'exactly'")
print("     is load-bearing in its source or was always shorthand. I would attack A2 first. ***")
print("     Nothing banked. CP existence-only.")
