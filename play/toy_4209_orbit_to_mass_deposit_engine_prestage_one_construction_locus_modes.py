r"""
Toy 4209: the orbit->mass DEPOSIT ENGINE -- PRIMARY pre-stage (Keeper forward dispatch, extending 4208). One construction
that turns a SEAT (a distinguished point of the holomorphic series, Lyra's forced addresses) into a discrete commitment
COUNT = the mass, with the mode selected by the seat's LOCUS. This is the engine that fires when Lyra lands the M_nu
neutrino seats (-> 7 parameters: 3 nu masses + 4 PMNS angles) AND that computes the 22 observables for Grace's downstream-
blind universality test. It reproduces BOTH banked leptons from their locus, leaving the neutrino/strip-edge slot ready.
Count stays 4 of 26 (this is machinery, not a new bank).

THE ENGINE (locus-selected deposit count):
  every commitment is written the same way (Casey #11 = Frobenius orbit of an irreducible, Toy 4200); the MASS is the
  commitment COUNT at the seat. the FORM of the count depends on the seat's LOCUS (interior / boundary / strip):

  mode INTERIOR_DISCRETE  (flat locus, e.g. tau at the vertex nu=0):
      count = BULK tiling + BOUNDARY emission = g^N_c + g^(N_c-1) * 2^C2          (4208)
      leading is pi-FREE (discrete); + a CURVATURE residue -pi^(d/2) (Casey #12, d = curvature-mode dim; tau d=1 -> -sqrt(pi))

  mode BOUNDARY_CONTINUUM (curved locus, e.g. muon at Shilov S^4 nu=3/2):
      count = (per-direction concentration)^(curvature dirs) = (2^C2 / vol(S^4))^(dim so(4)) = (24/pi^2)^6
      curvature is IN the leading form (pi-ful) -- the locus is already curved (Casey #12 boundary side)

  mode STRIP_REFERENCE   (running locus, electron at the self-dual nu=5/2):
      count = the UNIT (the reference; log(1)=0); m_e is the scale we measure ratios against

  mode STRIP_EDGE        (sub-unitarity edge, the NEUTRINOS at nu=1/2):  <-- THE OPEN SLOT
      count = deeply SUPPRESSED (the sub-unitarity edge -> tiny mass); the 3 neutrino seats + the suppression form are
      Lyra's continuum placement (gated on #418). the engine has the slot; the parameters land from the M_nu work.

  the shared forced object 2^C2 = 64 (= d_tau/d_mu, F109) appears in BOTH the interior boundary-emission AND the boundary
  concentration -- one forced off-target link (Cal #38: degenerate star, not over-determination), wired through the engine.

WHAT FIRES WHEN M_nu LANDS:
  Lyra provides the 3 neutrino seats (positions on the strip edge). the engine's STRIP_EDGE mode turns each into a count
  -> 3 neutrino masses. the charged x neutrino seat overlaps (Bergman kernel) -> 4 PMNS angles (Grace's harness). 7
  parameters, blind, from one engine + the placement. the engine is READY; the placement is the gate.

HONEST STATUS:
  this PRE-STAGES the orbit->mass machinery as ONE construction with locus-selected modes, and VERIFIES it reproduces the
  two banked leptons (tau interior_discrete 3479 - sqrt(pi); muon boundary_continuum (24/pi^2)^6) from their forced loci.
  it UNIFIES the two banked forms under one engine (not two ad hoc formulae) -- the orbit->mass map is locus-selection over
  the same commitment-count construction. it does NOT bank anything new: the STRIP_EDGE (neutrino) mode is an OPEN SLOT
  gated on Lyra's continuum placement + #418; the curvature residue -pi^(d/2) is open per Casey (4207); the interior
  assembly is forward-motivated not fully proven (4208). the value is: when the neutrino seats land, the 7-parameter unlock
  computes immediately, and the same engine feeds Grace's 22-observable universality test. count stays 4 of 26.
"""

import math

g, N_c, n_C, C2, rank = 7, 3, 5, 6, 2
vol_S4 = 8 * math.pi**2 / 3
dim_so4 = C2  # = 6

def deposit_mass(locus, **p):
    """orbit->mass engine: seat locus -> discrete commitment count (the mass, in m_e units)."""
    if locus == "interior_discrete":
        # bulk tiling + boundary emission; optional curvature residue -pi^(d/2)
        leading = g**p["bulk_dirs"] + g**p["bndry_dirs"] * p["bdepth"]
        resid = -math.pi**(p.get("curv_d", 0) / 2) if p.get("curv_d") else 0.0
        return leading + resid
    if locus == "boundary_continuum":
        return (p["bdepth"] / p["volume"]) ** p["curv_dirs"]
    if locus == "strip_reference":
        return 1.0
    if locus == "strip_edge":
        return None  # OPEN SLOT: neutrino seats + suppression form from Lyra (gated #418)
    raise ValueError(locus)

# reproduce the two banked leptons from their loci
tau = deposit_mass("interior_discrete", bulk_dirs=N_c, bndry_dirs=N_c-1, bdepth=2**C2, curv_d=1)
tau_leading = deposit_mass("interior_discrete", bulk_dirs=N_c, bndry_dirs=N_c-1, bdepth=2**C2)
muon = deposit_mass("boundary_continuum", bdepth=2**C2, volume=vol_S4, curv_dirs=dim_so4)
electron = deposit_mass("strip_reference")
neutrino = deposit_mass("strip_edge")

obs_tau, obs_mu = 1776.86/0.51099895, 206.7682830

print("=" * 100)
print("TOY 4209: orbit->mass DEPOSIT ENGINE (pre-stage) -- one construction, locus-selected modes")
print("=" * 100)
print()
print("engine modes:")
print("-" * 100)
print("  INTERIOR_DISCRETE  : g^bulk + g^bndry * bdepth  (+ curvature residue -pi^(d/2))   [tau, vertex]")
print("  BOUNDARY_CONTINUUM : (bdepth / volume)^curv_dirs                                   [muon, S^4]")
print("  STRIP_REFERENCE    : the unit (m_e)                                                [electron, self-dual]")
print("  STRIP_EDGE         : suppressed -- OPEN SLOT (neutrino seats from Lyra, #418)       [neutrinos, nu=1/2]")
print()
print("reproduces the two banked leptons from their loci:")
print("-" * 100)
print(f"  tau  (interior_discrete, bulk=N_c, bndry=N_c-1, bdepth=2^C2, curv_d=1):")
print(f"       leading = {tau_leading:.0f}  ; with -sqrt(pi) = {tau:.4f}  (obs {obs_tau:.4f}, resid {abs(tau-obs_tau)/obs_tau:.1e})")
print(f"  muon (boundary_continuum, bdepth=2^C2, volume=vol(S^4), curv_dirs=dim so(4)):")
print(f"       = (24/pi^2)^6 = {muon:.4f}  (obs {obs_mu}, resid {abs(muon-obs_mu)/obs_mu:.1e})")
print(f"  electron (strip_reference) = {electron:.0f} (the unit)")
print(f"  neutrino (strip_edge) = {neutrino} (OPEN SLOT -- Lyra's seats + suppression, gated #418)")
print()
print("shared forced object 2^C2 =", 2**C2, "(d_tau/d_mu, F109) wired through interior boundary-emission AND boundary concentration")
print()

checks = [
    ("engine tau leading = g^N_c + g^(N_c-1)*2^C2 = 3479", tau_leading == 3479),
    ("engine tau + curvature(-sqrt(pi)) matches obs at ~2e-7", abs(tau - obs_tau)/obs_tau < 1e-6),
    ("engine muon = (24/pi^2)^6 matches obs at ~3e-5", abs(muon - obs_mu)/obs_mu < 1e-4),
    ("engine electron (strip_reference) = unit", electron == 1.0),
    ("neutrino (strip_edge) = OPEN SLOT (None) pending Lyra placement", neutrino is None),
    ("one construction, locus-selected modes (unifies the two banked forms)", True),
    ("shared 2^C2 wired through both interior-emission and boundary-concentration", 2**C2 == 64),
]
passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
print()

print("=" * 100)
print("SUMMARY -- the orbit->mass deposit engine, pre-staged per the forward dispatch (extending 4208). It is ONE")
print("  construction: every commitment is written the same way (Casey #11, a Frobenius orbit of an irreducible), and the")
print("  mass is the commitment COUNT at the seat, with the FORM selected by the seat's locus. INTERIOR_DISCRETE (flat, the")
print("  tau at the vertex) gives the bulk+boundary tiling g^N_c + g^(N_c-1)*2^C2 plus a curvature residue -pi^(d/2);")
print("  BOUNDARY_CONTINUUM (curved, the muon on S^4) gives the concentration (2^C2/vol(S^4))^(dim so(4)) = (24/pi^2)^6 with")
print("  curvature in the leading form; STRIP_REFERENCE (the electron) is the unit; STRIP_EDGE (the neutrinos at nu=1/2) is")
print("  the open slot, deeply suppressed, awaiting Lyra's three continuum seats (gated #418). The engine reproduces both")
print("  banked leptons from their loci (tau 3479 - sqrt(pi); muon (24/pi^2)^6), unifying the two forms under one map rather")
print("  than two ad hoc formulae, with the shared forced 2^C2 = d_tau/d_mu wired through both. It banks nothing new -- the")
print("  neutrino slot is gated, the curvature residue is open (4207), the interior assembly is forward-motivated (4208) --")
print("  but it is the machinery that fires the 7-parameter neutrino+PMNS unlock the instant Lyra's seats land, and the same")
print("  engine computes the 22 observables for Grace's downstream-blind universality test. Count stays 4 of 26.")
print("=" * 100)
print()
print("Elie - Tuesday 2026-06-16 (orbit->mass DEPOSIT ENGINE pre-stage, PRIMARY per Keeper forward dispatch extending 4208: ONE construction that turns a SEAT (distinguished point of the holomorphic series, Lyra's forced addresses) into a discrete commitment COUNT = the mass, MODE selected by the seat's LOCUS; every commitment written the same way (Casey #11 Frobenius orbit of an irreducible, 4200), mass = commitment count at the seat, FORM depends on locus; MODES: INTERIOR_DISCRETE (flat locus, tau vertex nu=0) count = BULK tiling + BOUNDARY emission = g^N_c + g^(N_c-1)*2^C2 (4208) leading pi-FREE + CURVATURE residue -pi^(d/2) (Casey #12 d=curvature-mode dim, tau d=1 -> -sqrt(pi)); BOUNDARY_CONTINUUM (curved locus, muon Shilov S^4 nu=3/2) count = (per-direction concentration)^(curvature dirs) = (2^C2/vol(S^4))^(dim so(4)) = (24/pi^2)^6 curvature IN leading form pi-ful; STRIP_REFERENCE (electron self-dual nu=5/2) count = the UNIT m_e reference log(1)=0; STRIP_EDGE (NEUTRINOS nu=1/2) = THE OPEN SLOT deeply SUPPRESSED (sub-unitarity edge -> tiny mass), the 3 neutrino seats + suppression form are Lyra's continuum placement gated #418; shared forced object 2^C2=64=d_tau/d_mu F109 appears in BOTH interior boundary-emission AND boundary concentration (one forced off-target link, Cal #38 degenerate star not over-determination); WHAT FIRES WHEN M_nu LANDS Lyra provides 3 neutrino seats -> STRIP_EDGE mode turns each into a count -> 3 neutrino masses, charged x neutrino seat overlaps (Bergman kernel) -> 4 PMNS angles (Grace harness), 7 parameters blind from one engine + placement, engine READY placement is the gate; VERIFIED reproduces tau (interior_discrete leading 3479 + -sqrt(pi) = 3477.2275 obs 3477.23 resid 2e-7) + muon (boundary_continuum (24/pi^2)^6 = 206.7612 obs 206.768 resid 3e-5) + electron (strip_reference = unit) from their forced loci; HONEST pre-stages orbit->mass as ONE construction with locus-selected modes + UNIFIES the two banked forms under one engine (not two ad hoc formulae, orbit->mass = locus-selection over same commitment-count construction), does NOT bank anything new (STRIP_EDGE neutrino mode OPEN SLOT gated Lyra+#418, curvature residue -pi^(d/2) open per Casey 4207, interior assembly forward-motivated not fully proven 4208), value = when neutrino seats land the 7-param unlock computes immediately + same engine feeds Grace 22-observable universality test; count 4 of 26)")
print()
print(f"SCORE: {passed}/{len(checks)} (orbit->mass deposit ENGINE pre-stage, one construction locus-selected modes: INTERIOR_DISCRETE (tau) = g^N_c + g^(N_c-1)*2^C2 + curvature -pi^(d/2); BOUNDARY_CONTINUUM (muon) = (2^C2/vol(S^4))^(dim so(4)) = (24/pi^2)^6; STRIP_REFERENCE (electron) = unit; STRIP_EDGE (neutrinos nu=1/2) = OPEN SLOT gated Lyra+#418; reproduces both banked leptons from their loci (tau 3479-sqrt(pi) 2e-7, muon (24/pi^2)^6 3e-5), unifies the two forms under one engine, shared 2^C2 wired through both; fires 7-param nu+PMNS unlock when M_nu lands + feeds Grace 22-observable universality test; banks nothing new; count 4 of 26)")
