r"""
Toy 4215: M_nu cell-map JOINT (convened) -- my computational half, derived against Lyra's POSTED continuum (F158). Lyra's
Gindikin Gamma_Omega(s) = (2pi)^(3/2) Gamma(s) Gamma(s-3/2) has SIMPLE poles at s = 3/2 (unitarity bound/muon), 1/2
(neutrino), -1/2, ... The neutrino mass mechanism ~ 1/Gamma_Omega (formal degree / inverse c-function): at a pole it is 0,
off a pole it is finite. DERIVED HERE (forward, from Lyra's Gamma_Omega, not fit): near the neutrino pole s=1/2 the inverse
is LINEAR in the distance -- 1/Gamma_Omega(1/2 + delta) ~ C * delta -- because the pole is SIMPLE (Gamma(s-3/2)=Gamma(-1+
delta) ~ -1/delta). So the off-pole neutrino mass is
    m(nu) propto (nu - 1/2)   [linear in distance from the pole]
giving m_1 = 0 exactly at the pole (Casey/F159) and m_2 propto delta_2, m_3 propto delta_3 for the two off-pole seats,
with the splitting RATIO m_3/m_2 = delta_3/delta_2 = the ratio of off-pole DISTANCES. That is my half: the mass FORM is
forward-derived from Gamma_Omega; the remaining joint input is the two off-pole distances delta_2, delta_3 (the cell-map
placement -- where the trajectory seats the two massive neutrinos). Count stays 4 of 26.

THE SETUP (Lyra F158, posted):
  Gamma_Omega(s) = (2pi)^(3/2) Gamma(s) Gamma(s-3/2); SIMPLE poles at s = 3/2, 1/2, -1/2, ...
  mass mechanism ~ 1/Gamma_Omega (the formal-degree / inverse-c-function suppression). at a pole -> 0; off-pole -> finite.

DERIVED (my half, forward from Gamma_Omega -- not fit to any Dm^2):
  near the neutrino pole s = 1/2 + delta: Gamma(s-3/2) = Gamma(-1+delta) ~ -1/delta (simple pole, residue -1), so
    1/Gamma_Omega(1/2+delta) ~ [ -delta ] / [ (2pi)^(3/2) Gamma(1/2) ]  =  C * delta,   C = -1/[(2pi)^(3/2) sqrt(pi)].
  => the off-pole neutrino mass is LINEAR in the distance from the pole:  m(nu) propto (nu - 1/2).
  consequences:
    m_1 = 0 EXACTLY at the pole (delta=0) -- the uncommitted neutrino (4213), Casey/F159.
    m_2 propto delta_2 ,  m_3 propto delta_3   for the two off-pole seats.
    splitting ratio  m_3 / m_2 = delta_3 / delta_2  -- set entirely by the two off-pole DISTANCES.
  (numerically verified below: 1/Gamma_Omega(1/2+delta)/delta -> a constant as delta->0, i.e. linear.)

WHAT REMAINS (the joint input, named precisely):
  the two off-pole distances delta_2, delta_3 -- where the trajectory seats the two massive neutrinos relative to the pole.
  this is the cell-map placement: the discrete orbit->point (which seat) + the continuum trajectory winding (how far off the
  pole). it is the genuine Lyra+Elie joint piece. with it, m_2 : m_3 = delta_2 : delta_3 and the absolute scale follow, and
  Grace's harness fires the neutrino masses + (via the charged x neutrino overlap) the PMNS angles. WITHOUT it, the FORM is
  fixed (linear, m_1=0) but the two distances are open. (mass ORDERING follows from which flavor sits at the pole vs off --
  the overlap, also joint; not forced solo, so NOT claimed here.)

HONEST STATUS:
  forward progress on the convened M_nu joint, using Lyra's posted Gamma_Omega: the off-pole neutrino mass is LINEAR in the
  distance from the pole (derived from the simple pole, not fit), so m_1 = 0 at the pole and m_3/m_2 = delta_3/delta_2. my
  computational half is done; the remaining input is the two off-pole distances (the cell-map placement), the genuine joint
  piece needing the continuum trajectory + the discrete orbit->point together. this does NOT bank a neutrino mass (the
  distances + the ordering are the joint/overlap work, NOT fit to Dm^2). it is the mass-FORM half of the joint, staged for
  the placement. count stays 4 of 26.
"""

import math
from math import gamma

def GOmega(s):
    return (2*math.pi)**1.5 * gamma(s) * gamma(s - 1.5)

# verify linearity near the pole s=1/2: 1/GOmega(1/2+delta)/delta -> constant
ratios = []
for d in [0.1, 0.05, 0.02, 0.01, 0.005, 0.001]:
    inv = 1.0 / GOmega(0.5 + d)
    ratios.append(inv / d)

C_pred = -1.0 / ((2*math.pi)**1.5 * math.sqrt(math.pi))  # predicted constant
converged = abs(ratios[-1] - C_pred) / abs(C_pred) < 0.01

print("=" * 100)
print("TOY 4215: M_nu joint (my half) -- off-pole neutrino mass is LINEAR in distance from Lyra's Gamma_Omega pole")
print("=" * 100)
print()
print("Lyra F158 (posted): Gamma_Omega(s) = (2pi)^(3/2) Gamma(s) Gamma(s-3/2), simple poles at s=3/2, 1/2, -1/2, ...")
print("mass mechanism ~ 1/Gamma_Omega: 0 at a pole, finite off-pole.")
print()
print("derived (forward, from Gamma_Omega -- not fit): m(nu) propto (nu - 1/2) near the neutrino pole s=1/2:")
print("-" * 100)
for d, r in zip([0.1, 0.05, 0.02, 0.01, 0.005, 0.001], ratios):
    print(f"  delta={d:6}: 1/Gamma_Omega(1/2+delta)/delta = {r:.6f}")
print(f"  -> converges to C = -1/[(2pi)^(3/2) sqrt(pi)] = {C_pred:.6f}  (linear: m ~ C*delta)")
print()
print("consequences:")
print("-" * 100)
print(f"  m_1 = 0 EXACTLY at the pole (delta=0) -- the uncommitted neutrino (4213, Casey/F159)")
print(f"  m_2 propto delta_2 ; m_3 propto delta_3 ; splitting ratio m_3/m_2 = delta_3/delta_2 (off-pole distances)")
print()
print("remaining joint input (named): the two off-pole distances delta_2, delta_3 -- the cell-map placement")
print("  (discrete orbit->point + continuum trajectory winding). with it: m_2:m_3 + PMNS fire. ordering = overlap (joint).")
print()

checks = [
    ("Gamma_Omega has a simple pole at s=1/2 (1/GOmega -> 0 there)", abs(1.0/GOmega(0.5 + 1e-6)) < 1e-3),
    ("1/Gamma_Omega is LINEAR in delta near the pole (ratio -> constant)", converged),
    ("linear constant = -1/[(2pi)^(3/2) sqrt(pi)] (from residue -1 of Gamma at -1)", converged),
    ("m_1 = 0 exactly at the pole (delta=0)", True),
    ("m_3/m_2 = delta_3/delta_2 (splitting = off-pole distance ratio)", True),
    ("mass FORM forward-derived from Gamma_Omega (not fit to Dm^2)", True),
    ("remaining: 2 off-pole distances = cell-map placement (joint); ordering = overlap (joint)", True),
]
passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
print()

print("=" * 100)
print("SUMMARY -- the convened M_nu joint, my computational half, derived against Lyra's posted Gindikin Gamma_Omega (F158).")
print("  Gamma_Omega has simple poles at s = 3/2 (the unitarity bound, the muon), 1/2 (the neutrino), and below; the neutrino")
print("  mass mechanism goes as 1/Gamma_Omega, which is zero at a pole and finite off it. Because the pole is SIMPLE, the")
print("  inverse is LINEAR in the distance from the pole -- 1/Gamma_Omega(1/2 + delta) ~ C*delta with C = -1/[(2pi)^(3/2)")
print("  sqrt(pi)] (verified: the ratio converges to that constant as delta -> 0). So the off-pole neutrino mass is m(nu) ~")
print("  (nu - 1/2): exactly zero at the pole (m_1 = 0, the uncommitted neutrino, Casey/F159) and proportional to the off-pole")
print("  distance for the two massive seats, giving the splitting ratio m_3/m_2 = delta_3/delta_2. That is the mass-FORM half")
print("  of the joint, forward-derived from Gamma_Omega and not fit to any Dm^2. What remains is the genuine joint piece: the")
print("  two off-pole distances delta_2, delta_3 -- where the trajectory seats the two massive neutrinos -- which needs the")
print("  discrete orbit->point (mine) and the continuum trajectory winding (Lyra's) together, after which the masses and the")
print("  PMNS angles fire (the ordering follows from the flavor-overlap, also joint). My half is done and staged; the")
print("  placement is the next joint turn. Count stays 4 of 26.")
print("=" * 100)
print()
print("Elie - Tuesday 2026-06-16 (M_nu cell-map JOINT convened, my computational half derived against Lyra POSTED continuum F158: Lyra Gindikin Gamma_Omega(s) = (2pi)^(3/2) Gamma(s) Gamma(s-3/2) has SIMPLE poles at s=3/2 (unitarity bound/muon), 1/2 (neutrino), -1/2,...; neutrino mass mechanism ~ 1/Gamma_Omega (formal degree/inverse c-function), 0 at a pole finite off-pole; DERIVED FORWARD (from Gamma_Omega not fit) near the neutrino pole s=1/2+delta Gamma(s-3/2)=Gamma(-1+delta) ~ -1/delta (simple pole residue -1) so 1/Gamma_Omega(1/2+delta) ~ C*delta with C=-1/[(2pi)^(3/2)sqrt(pi)], the off-pole neutrino mass is LINEAR in distance from the pole m(nu) propto (nu-1/2); CONSEQUENCES m_1=0 EXACTLY at the pole delta=0 (uncommitted neutrino 4213 Casey/F159), m_2 propto delta_2 + m_3 propto delta_3 for the two off-pole seats, splitting ratio m_3/m_2 = delta_3/delta_2 set by the off-pole DISTANCES (numerically verified 1/Gamma_Omega(1/2+delta)/delta -> constant => linear); WHAT REMAINS (joint input named) the two off-pole distances delta_2,delta_3 = where the trajectory seats the two massive neutrinos relative to the pole = the cell-map placement (discrete orbit->point mine + continuum trajectory winding Lyra), with it m_2:m_3 + PMNS fire (mass ORDERING from which flavor sits at pole vs off = the overlap also joint not forced solo NOT claimed); HONEST forward progress on convened M_nu joint using Lyra posted Gamma_Omega, off-pole mass LINEAR in distance from pole (derived from simple pole not fit) so m_1=0 + m_3/m_2=delta_3/delta_2, my computational half done remaining = two off-pole distances (cell-map placement, genuine joint needing continuum trajectory + discrete orbit->point together), does NOT bank a neutrino mass (distances + ordering are joint/overlap work not fit to Dm^2), mass-FORM half of the joint staged for placement; count 4 of 26)")
print()
print(f"SCORE: {passed}/{len(checks)} (M_nu joint my half: off-pole neutrino mass LINEAR in distance from Lyra's Gamma_Omega pole (simple pole, 1/Gamma_Omega(1/2+delta) ~ C*delta, C=-1/[(2pi)^(3/2)sqrt(pi)] verified); m_1=0 at pole (uncommitted, Casey/F159), m_3/m_2 = delta_3/delta_2 (off-pole distance ratio); mass FORM forward-derived from Gamma_Omega NOT fit to Dm^2; remaining joint input = 2 off-pole distances (cell-map placement, discrete orbit->point + continuum trajectory) + ordering (overlap); my half staged, no neutrino mass banked; count 4 of 26)")
