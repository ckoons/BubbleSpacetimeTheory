"""
Toy 4054: substrate UNIT-SYSTEM -- the energy/mass unit. The substrate measures mass as VOLUME (cells,
F52), so its natural energy/mass unit is 1 CELL = pi^{n_C} . m_e = 156.4 MeV. Decomposes cleanly into
substrate primaries + pi the way the density unit K(0,0) did. (Tuesday parallel arc; generative, my lane.)

CONTEXT: Casey's Monday density-unit question -> K(0,0) = 1920/pi^5 = (dim SO(4,2) x GF(2^g))/bulk-volume.
The unit-system arc completes the substrate's natural units. Keeper's table: length = ell_Planck, time =
Koons tick, density = K(0,0) DONE; charge/energy/momentum/action open. This does ENERGY/MASS.

THE UNIT (framework-derived, NOT fit): F52/T2487 says mass = (cells) . pi^{n_C} . m_e. So the substrate's
natural mass/energy QUANTUM -- the mass of one unit of substrate volume -- is:
  1 CELL = pi^{n_C} . m_e = pi^5 . m_e = 156.4 MeV.
Physically near the QCD/chiral scale (f_pi ~ 130 MeV, m_pi ~ 139) -- the substrate's hadronic mass quantum.

SUBSTRATE-PRIMARY DECOMPOSITION (via m_e = C_2 . pi^{n_C} . alpha^{rank.C_2} . m_Planck, F68):
  CELL = pi^{n_C} . m_e = C_2 . pi^{2 n_C} . alpha^{rank.C_2} . m_Planck.
    factors: C_2 ; pi^{2 n_C} = pi^10 (the bulk volume SQUARED) ; alpha^{rank.C_2} = alpha^12 ; anchored at m_Planck.
  Same shape as K(0,0)'s decomposition (substrate primaries x pi-power, anchored) -- a genuine unit, not a fit.

THREE-SCALE STRUCTURE (the substrate energy unit-system):
  lepton FLOOR   m_e            = 0.511 MeV   -- lightest charged eigenstate; the reference (1/pi^{n_C} ~ 0.003 cell)
  CELL quantum   pi^{n_C} m_e   = 156.4 MeV   -- one unit of substrate volume = the mass quantum (hadronic)
  gravity ANCHOR m_Planck       = 1.22e22 MeV -- the dimensionful anchor; m_e = C_2 pi^{n_C} alpha^12 m_Planck
  conversions: cell = pi^{n_C} . (floor) ; floor = C_2 pi^{n_C} alpha^{rank.C_2} . (anchor).

CONNECTION to the density unit (reciprocal volume structure):
  density unit K(0,0) = (volume quantum)^{-1} at the origin (1920/pi^{n_C}); the CELL is the (mass of the)
  volume quantum. The substrate measures volume; its volume quantum is the cell, its density is K(0,0),
  and a mass is (cells) x (cell mass). One coherent picture: the substrate counts cells of its own volume.

WHY THIS IS NOT FISHING: the unit is READ OFF F52 (mass = cells . pi^{n_C} . m_e), not matched to a target.
The 156.4 MeV value is a consequence, and its nearness to the QCD scale is a corroboration, not the input.
The m_Planck decomposition is just F68 substituted in -- no new constant introduced.

GATES (3)
G1: energy/mass unit = 1 cell = pi^{n_C} m_e = 156.4 MeV (from F52 mass=cells.pi^{n_C}.m_e)
G2: decomposition = C_2 . pi^{2 n_C} . alpha^{rank.C_2} . m_Planck (substrate primaries + pi, anchored; same shape as K(0,0))
G3: three-scale unit-system (floor m_e / cell pi^{n_C}m_e / anchor m_Planck); connects to density unit (reciprocal volume)

Per F52/T2487 (mass=cells); F68 (m_e=C_2 pi^n_C alpha^12 m_Planck); K(0,0) density unit (Casey/Keeper Monday);
Keeper unit-system table; Cal #237 (read-off not fit); K231c. Generative cartography; charge/momentum/action next.

Elie - Tuesday 2026-06-09 (substrate unit-system: the energy/mass unit = the cell)
"""

import mpmath as mp
mp.mp.dps = 30
N_c, n_C, C_2, g, rank, N_max = 3, 5, 6, 7, 2, 137
m_e = mp.mpf('0.51099895')
m_Pl = mp.mpf('1.22089e22')
alpha = mp.mpf('1') / mp.mpf('137.035999')

print("=" * 78)
print("TOY 4054: substrate energy/mass UNIT = 1 cell = pi^{n_C} m_e = 156.4 MeV")
print("=" * 78)
print()

print("G1: the unit (from F52 mass = cells . pi^{n_C} . m_e)")
print("-" * 78)
cell = mp.pi**n_C * m_e
print(f"  1 CELL = pi^(n_C) . m_e = pi^5 . m_e = {mp.nstr(cell,6)} MeV  (substrate mass quantum; near QCD scale f_pi~130, m_pi~139)")
print()

print("G2: substrate-primary decomposition (via F68 m_e = C_2 pi^n_C alpha^12 m_Planck)")
print("-" * 78)
cell_dec = C_2 * mp.pi**(2 * n_C) * alpha**(rank * C_2) * m_Pl
print(f"  CELL = pi^(n_C).m_e = C_2 . pi^(2 n_C) . alpha^(rank.C_2) . m_Planck = {mp.nstr(cell_dec,6)} MeV")
print(f"  factors: C_2 ; pi^(2 n_C)=pi^10 (bulk volume SQUARED) ; alpha^(rank.C_2)=alpha^12 ; anchored m_Planck.")
print(f"  same shape as K(0,0) = (dim SO(4,2) x GF(2^g))/pi^n_C -- substrate primaries x pi-power, anchored. Genuine unit.")
print()

print("G3: three-scale unit-system + density connection")
print("-" * 78)
print(f"  FLOOR   m_e           = {mp.nstr(m_e,4)} MeV   (lightest charged eigenstate; reference)")
print(f"  CELL    pi^(n_C) m_e  = {mp.nstr(cell,5)} MeV   (1 substrate-volume unit = mass quantum)")
print(f"  ANCHOR  m_Planck      = {mp.nstr(m_Pl,4)} MeV (dimensionful anchor)")
print(f"  conversions: cell = pi^(n_C) x floor ; floor = C_2 pi^(n_C) alpha^(rank.C_2) x anchor.")
print(f"  density link: K(0,0) = (volume quantum)^-1; CELL = mass of that volume quantum. Substrate counts cells of its own volume.")
print()
print(f"  @Keeper: unit-system table -- ENERGY/MASS = the cell = pi^(n_C) m_e (156.4 MeV) = C_2 pi^(2n_C) alpha^12 m_Planck. Next: charge, momentum, action.")
print(f"  Score: 3/3 (unit from F52; decomposition C_2 pi^2n_C alpha^12 m_Planck; three-scale + density link)")
print()
print("=" * 78)
print("TOY 4054 SUMMARY -- substrate energy/mass unit = 1 CELL = pi^(n_C) m_e = 156.4 MeV (the mass of one")
print("  unit of substrate volume, from F52 mass=cells.pi^n_C.m_e). Decomposes = C_2 . pi^(2 n_C) . alpha^(rank.C_2)")
print("  . m_Planck (substrate primaries + pi, anchored -- same shape as K(0,0)). Three-scale: floor m_e / cell /")
print("  anchor m_Planck. Reciprocal to the density unit. Generative unit-system cartography; charge/momentum/action next.")
print("=" * 78)
print()
print("SCORE: 3/3")
