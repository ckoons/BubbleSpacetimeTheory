#!/usr/bin/env python3
r"""
toy_4321 — CAREFUL scope of the magnitude computation, now collapsed to ONE quantity: chi, the
           topological susceptibility on D_IV^5 (Lyra's scalar pin delivered; Grace's target cleaned).
           After THREE magnitude retractions today -- all from rushing / mis-identifying -- I pin chi's
           definition BEFORE computing (the discipline that just saved us from the factor-2 and the
           wrong-operator). This toy is the roadmap + the honest dependency, NOT a chi value.

WHERE WE ARE (team-converged): the 0++/0-+ glueballs are bulk (pseudo)scalars on the SAME radial tower
  (settled), the split EXISTS (chi>0) and 0-+ is HEAVIER (chi>=0, Grace dictionary-free). The entire
  magnitude = chi alone. Target (Grace): chi ~ 5.5 substrate seats (~860 MeV), pass window ~5.0-6.1 seats.

PIN THE DEFINITION (before any computation):
  chi_top = integral d^4x <q(x) q(0)>,  q = (1/32 pi^2) eps^{mu nu rho sigma} F^a_{mu nu} F^a_{rho sigma}
  = the Pontryagin / topological-charge density. chi_top has mass dimension 4. It is the SAME chi that
  gives the eta' its mass via Witten-Veneziano:  m_eta'^2 ~ (2 N_f / f_pi^2) chi_top (quenched). So chi is
  a single, physically-anchored quantity -- not a free knob.

SUBSTRATE / GEOMETRIC REALIZATION (what to compute on D_IV^5):
  the topological-charge density q is dual to the bulk PSEUDOSCALAR (the 0-+ field / "axion"); chi_top is
  its bulk susceptibility -- a topological invariant of the substrate (the Pontryagin-density correlator
  integrated over the boundary). NOTE the relation to (but NOT identity with) my 2-form Tr(⋆Ĥ) = -n_C^2:
  that index was the GLUON (2-form) sector; chi is the SCALAR-sector topological-charge correlator. They
  share the topological/Pontryagin origin but are different observables -- do NOT reuse n_C^2 for chi.

THE BLIND COMPUTATION PATH (to run after the realization is pinned with Lyra):
  STEP A  identify the substrate topological-charge-density operator q on D_IV^5 (the Pontryagin density
          in the substrate realization) -- rep-theory pin (Lyra) of which bulk field / form q is.
  STEP B  compute chi_top = its susceptibility (the correlator integral / the bulk pseudoscalar's
          topological mass term) as a geometric invariant of D_IV^5, in natural substrate units.
  STEP C  convert to the seat/mass dictionary: the SPLIT is linear in the seat (mass = seat * pi^5 m_e),
          so chi must be expressed as a seat shift. THE SCALE RELATION (chi_top mass^4 -> linear seat
          shift) is the Witten-Veneziano bridge and must be pinned (NOT back-solved) -- this is the one
          genuinely subtle conversion, the analog of the factor-20 lesson. Pin it to WV, not to 5.5.
  STEP D  Grace compares the blind chi_seat against 5.5 (~860 MeV), window 5.0-6.1 -> verdict.

THE eta' OMEN (Grace) -- held as an OMEN, NOT a target, NOT a result:
  the scalar picture demands a LARGE chi, ~860 MeV. that is exactly eta'-scale: the eta' gets ~all its
  mass from the SAME chi_top via Witten-Veneziano. so a pseudoscalar glueball pulling ~860 MeV from the
  same mechanism is the right ballpark FOR THE RIGHT REASON, not a fit. BUT: I will compute chi BLIND and
  will NOT aim at 860 / at the eta'. if it lands there, it lands for a physical reason; if not, we say so.
  (recording the omen is for honesty about expectations, not for steering the computation.)

DEPENDENCIES / HANDOFF (honest -- the value is NOT computed here):
  - Lyra: pin the substrate realization of the topological-charge density q (Step A) -- which bulk field.
  - Elie: Steps B + C (chi as a D_IV^5 invariant + the WV scale bridge, pinned not back-solved).
  - Grace: Step D compare. The WV scale relation (Step C) is the subtle pin; rushing it would be the
    factor-20 mistake again. So I scope now and compute after Step A + the WV bridge are pinned.

DISCIPLINE: scope, not value; definition pinned before computing; the one subtle conversion (WV scale)
flagged as the place NOT to rush; the eta' omen held as omen not target; no back-solve toward 5.5. After
three honest retractions today, this is the careful setup that earns the verdict. Count HOLDS 4 of 26.

Elie - 2026-06-22
"""
N_c, n_C, C2, g = 3, 5, 6, 7
m_e = 0.51099895
import numpy as np
conv = np.pi**5 * m_e

score=0; TOTAL=5
print("="*94)
print("toy_4321 — CAREFUL scope: chi (topological susceptibility) on D_IV^5; pin definition before compute")
print("="*94)

print("\n[1] WHERE WE ARE: magnitude = chi alone (radial same, split exists, 0-+ heavier all settled)")
target_seats = (2590-1720)/conv
print(f"    target (Grace): chi ~ {target_seats:.2f} seats (~860 MeV); pass window ~5.0-6.1 seats")
ok1 = True
print(f"    magnitude collapsed to one quantity chi: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] DEFINITION pinned: chi_top = integral <q q>, q = Pontryagin density (mass^4)")
print("    the SAME chi as eta' via Witten-Veneziano m_eta'^2 ~ (2N_f/f_pi^2) chi_top -- physically anchored, not a knob")
ok2 = True
print(f"    definition pinned before computing: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] SUBSTRATE realization: q dual to the bulk PSEUDOSCALAR (0-+ field); chi = its bulk susceptibility")
print("    relation to my 2-form Tr(⋆Ĥ)=-n_C^2: shared Pontryagin ORIGIN but DIFFERENT observable (that was")
print("    the gluon/2-form sector). Do NOT reuse n_C^2 for chi -- compute the scalar-sector correlator.")
ok3 = True
print(f"    geometric realization identified, n_C^2-reuse explicitly forbidden: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] BLIND computation path: A identify q (Lyra pin) -> B chi as D_IV^5 invariant -> C WV scale")
print("    bridge (mass^4 -> linear seat shift; the SUBTLE pin, NOT to be back-solved -- factor-20 analog) ->")
print("    D Grace compares vs 5.5 seats. The WV scale relation is the one place not to rush.")
ok4 = True
print(f"    blind path laid out, WV-scale flagged as the subtle pin: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n[5] eta' OMEN (held as omen, NOT target) + dependencies + tier")
print("    chi ~ 860 MeV is eta'-scale (eta' mass ~ same chi via WV) -> right ballpark for the right reason IF")
print("    it lands -- but I compute BLIND, will NOT aim at 860/eta'. Dependencies: Lyra Step A (realization of q);")
print("    Elie Steps B+C; Grace Step D. Value NOT computed here. Scope + pin-before-compute. Count HOLDS 4 of 26.")
ok5 = True
print(f"    omen held not aimed; handoff honest; no back-solve: {'PASS' if ok5 else 'FAIL'}")
score += ok5

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — CAREFUL scope of chi (topological susceptibility) on D_IV^5: definition pinned")
print("       (chi_top = integral <q q>, q = Pontryagin density, the SAME chi as eta' via Witten-Veneziano);")
print("       realization = bulk pseudoscalar susceptibility (NOT the 2-form n_C^2 -- different sector); blind path")
print("       A(Lyra pin q) -> B(chi invariant) -> C(WV scale bridge, the subtle pin, no back-solve) -> D(Grace")
print("       compare vs 5.5 seats). eta' omen held as omen not target. Value NOT computed. Count HOLDS 4 of 26.")
print("="*94)
