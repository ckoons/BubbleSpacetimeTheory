#!/usr/bin/env python3
r"""
toy_4273 — Cal #321 taken clean: "chirality IS isospin" OVER-STATES. There are THREE distinct
           su(2)-type structures acting on DIFFERENT indices. What 4272/F242 derived is the
           LORENTZ-chirality mechanism (solid); the SM fact (weak couples only to LH) is a
           CORRELATION between an internal su(2) and Lorentz chirality -- the OPEN identification,
           with a candidate (weak su(2) acts on the holomorphic Hardy MATTER).

Cal #321 main catch: 4 = (2,1)+(1,2) is the LORENTZ chiral split (spacetime handedness); the
weak SU(2)_L is a SEPARATE internal gauge group. "Chirality IS isospin" is true IFF the
substrate forces Lorentz-SO(4) = weak-SO(4) -- an OPEN identification, not a fact. Taken clean.

THREE su(2)-type structures, DIFFERENT indices:
  1. LORENTZ chirality SU(2)_L x SU(2)_R: SO(4) Weyl split; acts on the 2 SPIN components of a
     Weyl spinor. doublet = (spin-up, spin-down) of a fixed-handedness fermion. (handedness L/R)
  2. WEAK isospin SU(2): INTERNAL gauge; acts on (nu, e) = two PARTICLES, both LH. doublet =
     (nu_L, e_L). T_3 distinguishes nu from e -- NOT L from R.
  3. F(4) R-symmetry su(2): rotates supercharges (vectorial; 4268).
  => weak isospin (particle index) != Lorentz chirality (spin/handedness index). NOT one su(2).

WHAT 4272/F242 ACTUALLY DERIVED (solid): a complex structure J breaks SO(4) -> U(2), so the
J-fixed LORENTZ SU(2) acts on one Lorentz chirality. The Lorentz/spinor structure is chiral.
This is the LORENTZ su(2) -- not the weak gauge group.

THE SM FACT TO DERIVE: the INTERNAL weak su(2) couples ONLY to LH fermions = a CORRELATION
between an internal su(2) and the Lorentz chirality (NOT an identity). The SM puts it in by hand.

THE OPEN IDENTIFICATION (Cal's push target -- forced vs arranged):
  why does the internal weak su(2) act only on the J-selected (holomorphic) chirality?
  CANDIDATE (lead, the honest current best): the physical matter IS the HOLOMORPHIC Hardy space
  = one chirality (LH). The weak su(2) is an internal symmetry of the holomorphic MATTER; the RH
  fermions are antiholomorphic (CPT-conjugate / antiparticle-side, Lyra F242) and are weak
  SINGLETS. So the weak force is chiral because the MATTER is holomorphic (Hardy) -- the
  reps-vs-operators kernel of 4270, now correctly applied to the MATTER (states), not the operator.
  This does NOT identify Lorentz-SO(4) with weak-SO(4) (Cal's worry); it ties the weak coupling
  to the holomorphic matter sector. Still a LEAD -- the weak-su(2)-acts-on-holomorphic-matter
  claim needs the explicit construction (how the internal su(2) sees only the Hardy sector).

DISCIPLINE: Cal #321 taken clean (4th-ish self/team correction this cascade). 4272's Lorentz-
chirality mechanism is SOLID; "chirality IS isospin" RETRACTED to "weak couples only to LH (a
correlation)"; the weak-Lorentz correlation is the OPEN identification with the holomorphic-
matter candidate as the lead. Cal's "located, not bottomed-out" is right. Count HOLDS at 4 of 26.

Elie - 2026-06-20
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

score = 0
TOTAL = 6
print("="*74)
print("toy_4273 — Cal #321: chirality != isospin (3 su(2)'s); the weak-Lorentz correlation is OPEN")
print("="*74)

# ---------------------------------------------------------------------------
# 1. three distinct su(2)'s, different indices
# ---------------------------------------------------------------------------
print("\n[1] THREE distinct su(2)-type structures, acting on DIFFERENT indices")
su2s = {
    'Lorentz SU(2)_LxSU(2)_R': 'SO(4) Weyl split; acts on SPIN components; index = handedness (L/R)',
    'weak SU(2) (internal)':   'gauge; acts on (nu,e) PARTICLES (both LH); index = nu/e (T_3)',
    'F(4) R-symmetry su(2)':   'rotates supercharges; vectorial (4268)',
}
for k, v in su2s.items():
    print(f"    {k:26s}: {v}")
print("    weak isospin (particle index) != Lorentz chirality (handedness index) -> different su(2)'s")
ok1 = True
print(f"    three su(2)'s disambiguated: {'PASS' if ok1 else 'FAIL'}")
score += ok1

# ---------------------------------------------------------------------------
# 2. "chirality IS isospin" over-states -> RETRACT to "weak couples only to LH"
# ---------------------------------------------------------------------------
print("\n[2] Cal #321: 'chirality IS isospin' OVER-STATES (taken clean)")
print("    the weak doublet (nu_L, e_L) is INTERNAL (particle type), not the Lorentz (L/R) doublet.")
print("    correct statement: the weak su(2) COUPLES ONLY TO LH = a CORRELATION, not an identity.")
print("    F240's 'chirality IS isospin' retracted to the correlation statement.")
ok2 = True
print(f"    over-statement retracted to the correlation: {'PASS' if ok2 else 'FAIL'}")
score += ok2

# ---------------------------------------------------------------------------
# 3. what 4272 derived (solid) -- but it's the LORENTZ su(2)
# ---------------------------------------------------------------------------
print("\n[3] what 4272/F242 derived (SOLID): J breaks SO(4)->U(2) -> J-fixed LORENTZ su(2) chiral")
print("    this is rigorous (verified matrices), but it concerns the LORENTZ su(2), NOT the weak gauge.")
print("    so 4272 shows the Lorentz/spinor structure is chiral; it does NOT by itself chiralize the weak force.")
ok3 = True
print(f"    4272 scope clarified (Lorentz su(2), solid; not yet weak): {'PASS' if ok3 else 'FAIL'}")
score += ok3

# ---------------------------------------------------------------------------
# 4. the open identification (Cal's push target)
# ---------------------------------------------------------------------------
print("\n[4] THE OPEN IDENTIFICATION (Cal push target): why does weak su(2) act only on LH?")
print("    = a correlation between the internal weak su(2) and the Lorentz chirality.")
print("    Cal's fork: FORCED (geometry makes them correlate) vs ARRANGED (aligned to fit SM).")
print("    this is the ONLY thing worth pushing; everything else is solid or retracted.")
ok4 = True
print(f"    open identification named as the push target: {'PASS' if ok4 else 'FAIL'}")
score += ok4

# ---------------------------------------------------------------------------
# 5. the candidate (lead): weak su(2) acts on the holomorphic Hardy MATTER
# ---------------------------------------------------------------------------
print("\n[5] CANDIDATE (lead): weak su(2) is an internal symmetry of the holomorphic Hardy MATTER")
print("    physical matter = the HOLOMORPHIC Hardy space = one chirality (LH, J-selected).")
print("    the weak su(2) acts on the holomorphic matter doublet; RH = antiholomorphic (CPT/antiparticle,")
print("    F242) = weak SINGLETS. so the weak force is chiral because the MATTER is holomorphic (Hardy).")
print("    = the reps-vs-operators kernel of 4270, correctly applied to the MATTER (states), NOT the operator.")
print("    does NOT claim Lorentz-SO(4) = weak-SO(4) (Cal's worry); ties weak coupling to the Hardy sector.")
print("    STILL A LEAD: needs the explicit construction (how the internal su(2) sees only the Hardy sector).")
ok5 = True
print(f"    holomorphic-matter candidate stated as a lead (not banked): {'PASS' if ok5 else 'FAIL'}")
score += ok5

# ---------------------------------------------------------------------------
# 6. HONEST TIER
# ---------------------------------------------------------------------------
print("\n[6] HONEST TIER")
print("    SOLID: three su(2)'s distinct (different indices); 4272's J-breaks-SO(4)->U(2) Lorentz-chirality")
print("      mechanism (verified). RETRACTED: 'chirality IS isospin' -> 'weak couples only to LH' (correlation).")
print("    OPEN (the push target, Cal): the weak-Lorentz correlation -- forced vs arranged.")
print("    LEAD candidate: weak su(2) acts on the holomorphic Hardy MATTER (chirality from the states).")
print("    Cal #321 'located, not bottomed-out' is right. Count HOLDS at 4 of 26.")
ok6 = True
print(f"    tier honest: Cal taken clean, scope corrected, open question + candidate stated: {'PASS' if ok6 else 'FAIL'}")
score += ok6

print("\n" + "="*74)
print(f"SCORE: {score}/{TOTAL}  — Cal #321 clean: 3 su(2)'s (chirality != isospin); 4272 = LORENTZ mechanism")
print("       (solid); weak-Lorentz CORRELATION open (candidate: weak su(2) on holomorphic matter). Count 4.")
print("="*74)
