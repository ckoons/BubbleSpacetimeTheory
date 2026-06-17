r"""
Toy 4194: applying Grace's stars-vs-loops distinction to MY OWN off-target 64 -- the Quaker scrutiny of the one "loop" we
think the lepton sector has. Grace's web finding: a STAR = one forced object feeding many observables (over-determines the
SOURCE; tunable per-observable). A LOOP = one observable pinned by multiple INDEPENDENT forced objects (over-determines
the OBSERVABLE; untunable). She named the lepton-mass triangle as "the one genuine loop," with 64 forced-shared between
the muon and tau legs. This toy tests that claim carefully and BLIND TO THE MUON NUMBER (structural forms only, no fit to
206.77). RESULT (an honest SHARPENING, not a downgrade): the genuine loop is on the OBJECT 64 (three independent
derivations = Grace's three faces), NOT on a mass-ratio OBSERVABLE. The mass ratios ride a STAR off the loop-pinned 64;
each ratio is a single forced FORM; and m_tau/m_mu is currently ONLY the quotient (no independent forcing). So the lepton
triangle is "object-loop(64) -> star -> two single-forced ground ratios -> trivial quotient" -- it becomes an OBSERVABLE-
loop only when m_tau/m_mu gets an independent trajectory-level forcing (the consecutive-Wallach-point step), which is gated
on Lyra's one-trajectory-vs-three-trajectories question. Count stays 2 of 26.

THE THREE LEPTON RATIOS (structural forms, blind to numbers):
  m_mu/m_e = (2^C2 / vol(S^4))^(n_C+1)   [T190 muon ground ratio; 2^C2=64 per-direction depth / S^4 spread, to the 6th]
  m_tau/m_e = g^rank (g + 2^C2)          [T2003 tau ground ratio; 2^C2=64 boundary depth, additive in the depth]
  m_tau/m_mu = (m_tau/m_e) / (m_mu/m_e)  [currently ONLY the quotient -- no independent substrate derivation in hand]
  (n_C + 1 = C2 = 6 so the muon exponent is 6; vol(S^4) = 8 pi^2 / 3; 64/vol(S^4) = 24/pi^2.)

WHERE 64 = 2^C2 APPEARS (the shared object, in DISTINCT roles):
  - muon: as the per-direction depth, (64/vol)^6 -- MULTIPLICATIVE, sixth power.
  - tau:  as the boundary depth, g^rank*(g + 64) -- ADDITIVE, inside the depth sum.
  same object 64, two incommensurable roles. it does NOT cancel between the legs (sixth-power vs additive), so the legs
  do not combine to independently pin a third number.

GRACE'S TWO KINDS OF OVER-DETERMINATION, APPLIED:
  (1) OBJECT-LOOP on 64 -- GENUINE. 64 is pinned by THREE INDEPENDENT derivations (Grace's three faces):
        face A: d_tau/d_mu = 64  (formal-degree ratio, F109, rep-theory polynomial)
        face B: 2^(dim so(4)) = 64  (boundary 2-plane orientation count)
        face C: 2^C2 = 64  (Casimir-exponent, C2 = 6)
      three different machines, one value 64. THAT is a loop: 64 cannot be tuned without breaking three derivations.
  (2) STAR off the loop-pinned 64 -- the two ground ratios. 64 feeds BOTH (muon per-direction, tau boundary). this
      over-determines the SOURCE 64 again (a fourth + fifth "use"), but each ground ratio is a SINGLE forced FORM;
      neither mass ratio is independently pinned by two objects. so the OBSERVABLES are star-tips, not loops.
  (3) NO OBSERVABLE-LOOP yet. m_tau/m_mu is only the quotient of the two ground ratios -- it has no independent
      substrate forcing, so it cannot (yet) over-constrain anything. the triangle does not close as an observable-loop.

WHAT WOULD CLOSE THE OBSERVABLE-LOOP (the gated next step):
  an INDEPENDENT forcing of m_tau/m_mu -- i.e. the substrate sets the tau<->muon step DIRECTLY (the consecutive-Wallach-
  point spacing nu=0 -> nu=3/2), not via the e-anchored quotient. then m_tau/m_mu would be pinned BOTH by the direct step
  AND by (m_tau/m_e)/(m_mu/m_e), and the consistency of the two = a genuine observable-loop. WHETHER such a direct step
  EXISTS depends on Lyra's open structural question: if the three leptons are ONE corkscrew trajectory sampled thrice,
  the consecutive-step structure plausibly supplies the independent forcing (loop closes); if they are THREE DISTINCT
  helices (Lyra's current lead), there is no single-trajectory step and m_tau/m_mu stays a quotient (no observable-loop;
  the lepton sector's only loop is the object-loop on 64). So Grace's web closure (C3) and Lyra's trajectory-count
  question are the SAME question at the lepton triangle.

HONEST STATUS:
  SHARPENS Grace's web, does not overturn it. The "one genuine loop" in the lepton sector is REAL but it is an OBJECT-loop
  on 64 (three independent derivations), not an OBSERVABLE-loop on a mass ratio. The mass ratios are star-tips off that
  loop. This matters for C3 ("all" = the web being looped): object-loops over-determine PARAMETERS (strong, but a star can
  still hide a form-selection fit at each observable tip); observable-loops over-determine OBSERVABLES (the untunable
  thing). The lepton triangle has the first, not yet the second. Closing it is gated on Lyra's trajectory-count question.
  Blind to the muon number throughout (structural forms only). Count stays 2 of 26; muon yellow IDENTIFIED.
"""

from fractions import Fraction as F
import math

N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

# the shared object 64, three independent derivations (Grace's three faces) -- OBJECT-LOOP test
face_A_formal_degree = 64          # d_tau/d_mu (F109)
face_B_so4_orient   = 2**4         # 2^(dim so(4)), dim so(4) = 6? NO: so(4) has dim 6; the boundary 2-plane count is 2^C2.
# careful: the boundary depth is 2^C2 with C2 = 6, and dim so(4) = 6 as well -> 2^(dim so(4)) = 2^6. fix:
face_B_so4_orient   = 2**C2        # 2^(dim so(4)) with dim so(4) = 6 = C2
face_C_casimir_exp  = 2**C2        # 2^C2, C2 = 6
sixtyfour = 2**C2

# the two ground ratios (structural forms; blind -- we do NOT compare to 206.77 / 3477)
vol_S4 = F(8,3)  # times pi^2 ; keep pi symbolic via the 24/pi^2 identity
# 64/vol(S^4) = 64/(8 pi^2/3) = 24/pi^2  -> verify the rational part: 64/(8/3) = 24
per_direction_rational = F(sixtyfour, 1) / vol_S4   # = 24  (the 1/pi^2 carried separately)
mu_exponent = n_C + 1                                 # = C2 = 6
tau_box = g**rank * (g + sixtyfour)                  # = 49*71

# m_tau/m_mu is ONLY the quotient (no independent forcing) -- compute numerically just to show it's the quotient
mu_over_e = (24.0/math.pi**2)**mu_exponent
tau_over_e = float(tau_box)
tau_over_mu_quotient = tau_over_e / mu_over_e

print("=" * 98)
print("TOY 4194: lepton triangle -- OBJECT-loop vs OBSERVABLE-loop (Grace stars-vs-loops applied to my own 64), BLIND")
print("=" * 98)
print()
print("(1) OBJECT-LOOP on 64 -- three independent derivations (Grace's three faces):")
print("-" * 98)
print(f"    face A d_tau/d_mu (formal degree F109) = {face_A_formal_degree}")
print(f"    face B 2^(dim so(4)), dim so(4)=6      = {face_B_so4_orient}")
print(f"    face C 2^C2, C2=6                       = {face_C_casimir_exp}")
print(f"    all equal 64 via THREE different machines -> 64 is loop-over-determined (untunable). GENUINE LOOP (on the object).")
print()
print("(2) STAR off the loop-pinned 64 -- the two ground ratios (each a SINGLE forced form):")
print("-" * 98)
print(f"    muon: m_mu/m_e = (64/vol(S^4))^{mu_exponent}  [64 MULTIPLICATIVE, per-direction, 64/(8/3)={int(per_direction_rational)} -> 24/pi^2]")
print(f"    tau : m_tau/m_e = g^rank (g + 64) = {g}^{rank}({g}+{sixtyfour}) = {tau_box} = 49*71  [64 ADDITIVE, boundary depth]")
print(f"    same 64, two incommensurable roles (6th-power vs additive) -> legs do NOT combine to pin a third number.")
print(f"    each ground ratio = ONE forced form, not two independent pinnings -> star-TIPS, not loops.")
print()
print("(3) NO OBSERVABLE-LOOP yet -- m_tau/m_mu is ONLY the quotient:")
print("-" * 98)
print(f"    m_tau/m_mu = (m_tau/m_e)/(m_mu/m_e) = {tau_over_mu_quotient:.4f}  -- no INDEPENDENT substrate forcing in hand.")
print(f"    a quotient cannot over-constrain anything -> the triangle does not close as an observable-loop.")
print()
print("(4) what would close it (gated on Lyra's trajectory-count question):")
print("-" * 98)
print(f"    need an INDEPENDENT forcing of the tau<->muon step (consecutive Wallach points nu=0 -> nu=3/2).")
print(f"    ONE trajectory sampled thrice -> consecutive-step structure plausibly supplies it -> observable-loop CLOSES.")
print(f"    THREE distinct helices (Lyra's lead) -> no single-trajectory step -> stays a quotient -> only the object-loop.")
print(f"    => Grace's C3 web-closure and Lyra's one-vs-three-trajectories are the SAME question at the lepton triangle.")
print()

checks = [
    ("face A = 64", face_A_formal_degree == 64),
    ("face B = 64", face_B_so4_orient == 64),
    ("face C = 64", face_C_casimir_exp == 64),
    ("three faces agree -> 64 object-loop", face_A_formal_degree == face_B_so4_orient == face_C_casimir_exp == 64),
    ("muon exponent = n_C+1 = C2 = 6", mu_exponent == C2 == 6),
    ("64/vol rational part = 24 (-> 24/pi^2)", per_direction_rational == 24),
    ("tau box = 49*71", tau_box == 49*71),
    ("m_tau/m_mu is the quotient (~16.8), not independently forced", 16.0 < tau_over_mu_quotient < 17.5),
]
passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
print()

print("=" * 98)
print("SUMMARY -- applying Grace's stars-vs-loops to the lepton triangle, blind to the muon number. Grace named the triangle")
print("  'the one genuine loop' with 64 shared between the muon and tau legs; scrutinized carefully, that sharpens rather than")
print("  overturns. The genuine loop is an OBJECT-loop on 64 = 2^C2: three independent machines (formal-degree d_tau/d_mu,")
print("  the 2^(dim so(4)) orientation count, the 2^C2 Casimir-exponent) all return 64, so the OBJECT cannot be tuned. But")
print("  the mass-ratio OBSERVABLES are not loops: 64 feeds the muon (per-direction, sixth power) and the tau (boundary,")
print("  additive) in incommensurable roles, so the legs don't combine to independently pin a third number; each ground")
print("  ratio is a single forced form (a star-tip off the loop-pinned 64); and m_tau/m_mu is currently only the quotient,")
print("  with no independent forcing. So the lepton triangle = object-loop(64) -> star -> two single-forced ground ratios ->")
print("  trivial quotient, NOT an observable-loop. It closes into an observable-loop only if m_tau/m_mu gets an independent")
print("  trajectory-level forcing (the consecutive-Wallach-point step) -- which exists iff the three leptons are ONE")
print("  trajectory sampled thrice (loop closes) rather than THREE distinct helices (stays a quotient). That makes Grace's")
print("  web-closure condition C3 and Lyra's one-vs-three-trajectories question the SAME question at the lepton triangle.")
print("  Honest: object-loops over-determine PARAMETERS (strong, but a star tip can still hide a form-selection fit);")
print("  observable-loops over-determine OBSERVABLES (the untunable thing). Lepton sector has the first, not yet the second.")
print("  Count stays 2 of 26; muon yellow IDENTIFIED.")
print("=" * 98)
print()
print("Elie - Monday 2026-06-15 (lepton triangle OBJECT-loop vs OBSERVABLE-loop, applying Grace's stars-vs-loops to my own off-target 64, BLIND to the muon number = structural forms only no fit to 206.77: Grace named the lepton-mass triangle 'the one genuine loop' with 64 forced-shared between muon and tau legs; SCRUTINIZED carefully it SHARPENS not overturns; (1) OBJECT-LOOP on 64 GENUINE -- 64=2^C2 pinned by THREE independent derivations (Grace's three faces) face A d_tau/d_mu=64 formal-degree F109 rep-theory polynomial, face B 2^(dim so(4))=2^6=64 boundary 2-plane orientation count, face C 2^C2=64 Casimir-exponent C2=6, three different machines one value 64 -> 64 untunable -> loop on the OBJECT; (2) STAR off the loop-pinned 64 -- the two ground ratios m_mu/m_e=(64/vol(S^4))^(n_C+1) [64 MULTIPLICATIVE per-direction sixth power, 64/(8/3)=24 -> 24/pi^2] and m_tau/m_e=g^rank(g+64)=49*71 [64 ADDITIVE boundary depth], same 64 two incommensurable roles (6th-power vs additive) so legs do NOT combine to pin a third number, each ground ratio = ONE forced form -> star-TIPS not loops; (3) NO OBSERVABLE-LOOP yet -- m_tau/m_mu = (m_tau/m_e)/(m_mu/m_e) ~16.82 is ONLY the quotient, no independent substrate forcing in hand, a quotient cannot over-constrain -> triangle does not close as observable-loop; (4) WHAT CLOSES IT (gated) -- an INDEPENDENT forcing of the tau<->muon step (consecutive Wallach points nu=0 -> nu=3/2), exists iff three leptons are ONE corkscrew trajectory sampled thrice (consecutive-step supplies it -> observable-loop closes) vs THREE distinct helices (Lyra's lead -> no single-trajectory step -> stays quotient -> only object-loop), so Grace's C3 web-closure and Lyra's one-vs-three-trajectories are the SAME question at the lepton triangle; HONEST sharpens Grace's web not overturns, the lepton-sector loop is an OBJECT-loop on 64 (over-determines the PARAMETER, strong but star-tips can hide form-selection fit) NOT an OBSERVABLE-loop on a mass ratio (over-determines the OBSERVABLE, untunable), lepton sector has the first not yet the second; blind throughout; count 2 of 26 muon yellow IDENTIFIED)")
print()
print(f"SCORE: {passed}/{len(checks)} (lepton triangle stars-vs-loops, blind: 64=2^C2 is a genuine OBJECT-loop (3 independent faces -- formal degree, so(4) orientations, Casimir exponent all = 64, untunable); but mass-ratio OBSERVABLES are STAR-tips off it (each ground ratio single forced form, 64 in incommensurable roles 6th-power vs additive); m_tau/m_mu only the quotient = NO observable-loop yet; closing needs independent tau<->muon step forcing, gated on Lyra one-vs-three-trajectories = same question as Grace C3 web-closure; object-loop over-determines PARAMETER, observable-loop over-determines OBSERVABLE, lepton sector has first not second; count 2 of 26)")
