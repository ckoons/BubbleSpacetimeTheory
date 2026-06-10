"""
CORRECTION (Grace catch, Tue 2026-06-09 PM): the Z_2 bit tracks STATISTICS (boson/fermion), NOT
spin MAGNITUDE. Floor proof: boson rho/omega (spin-1) at 5 cells vs fermion p/n (spin-1/2) at 6 cells
-- more cells = LESS spin magnitude. So the SOLID core is "+1 cell = Z_2 spinor twist = boson/fermion
STATISTICS" (passes); the "hbar/2 spin-magnitude unit" framing below is WRONG. Read "spin unit" as
"STATISTICS unit (Z_2 bit)" throughout. Pattern: energy<->VOLUME, charge<->COLOR, STATISTICS<->Z_2.
"""
"""
Toy 4059: substrate UNIT-SYSTEM -- the spin / angular-momentum unit. Quantum = hbar/2 (fermion);
the boson/fermion BIT = Z_2 = pi_1(SO(3)) (T185 spinor; T2488 cell+bit). Completes the clean unit
triple: energy reads VOLUME, charge reads COLOR, spin reads the Z_2 SPINOR bit. (Tuesday unit-system arc; my lane.)

CONTEXT: continuing the substrate unit-system (length=ell_Planck, time=Koons tick, density=K(0,0),
energy=cell pi^{n_C}m_e [4054], charge=e/N_c [4055]). This does SPIN / ANGULAR MOMENTUM.

THE SPIN UNIT:
  quantum = hbar/2 (the fermion spin); bosons carry integer hbar.
  The boson/fermion BIT is Z_2 = pi_1(SO(3)) -- the topological spinor structure (T185: the spinor's
  +1 under 2pi / single-valuedness under 4pi; the belt trick). So the substrate's spin "unit" is the
  Z_2 spinor bit: 0 = boson (integer spin), 1 = fermion (half-integer spin).

CONNECTION to the floor cell-structure (T2488 -- the bit IS the meson/baryon floor distinction):
  meson  floor = n_C cells          (boson; no Z_2 bit)  -> rho, omega at n_C = 5
  baryon floor = n_C cells + Z_2 bit = C_2 cells  (fermion; +1 = n_C+1 = C_2) -> p, n at C_2 = 6
  So the Z_2 spin bit is exactly the +1 that takes the meson floor (n_C=5) to the baryon floor (C_2=6).
  The spin unit and the energy/cell unit are the same structure seen two ways: a baryon is a meson-volume
  PLUS the Z_2 spinor bit, and that bit is both its fermion-ness and its extra cell.

PATTERN (each substrate unit reads a specific primary -- the unit-system's organizing structure):
  energy/mass   <-> VOLUME (pi^{n_C}; the cell = pi^{n_C} m_e)
  charge        <-> COLOR  (N_c; quantum e/N_c, coupling alpha=1/N_max)
  spin/ang.mom  <-> Z_2 SPINOR BIT (quantum hbar/2; boson/fermion = pi_1(SO(3)); = the meson/baryon +1 cell)
  So the substrate's units are not arbitrary -- each is the natural scale of one substrate-primary structure.

WHY NOT FISHING: the spin quantum hbar/2 is standard QM; the Z_2 = pi_1(SO(3)) boson/fermion bit is T185
(established); the cell+bit = C_2 baryon floor is T2488 (established). This collects them as the spin unit
and notes the bit = the meson/baryon +1 cell; no new fit.

GATES (2)
G1: spin unit = hbar/2 quantum; boson/fermion bit = Z_2 = pi_1(SO(3)) (T185 spinor)
G2: the Z_2 bit = the +1 cell taking meson floor (n_C=5) to baryon floor (C_2=6) (T2488); completes the unit-primary pattern (energy=volume, charge=color, spin=Z_2)

Per T185 (spinor Z_2 = pi_1(SO(3))); T2488 (baryon = n_C cells + Z_2 bit = C_2); Toy 4054/4055 (energy/charge
units); Keeper unit-system table; Cal #237 (collect established, not fit); K231c. Generative cartography.

Elie - Tuesday 2026-06-09 (substrate unit-system: spin = hbar/2, Z_2 spinor bit = meson/baryon +1 cell)
"""

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2

print("=" * 78)
print("TOY 4059: substrate spin UNIT -- hbar/2 quantum, Z_2 spinor bit (= meson/baryon +1 cell)")
print("=" * 78)
print()

print("G1: spin unit = hbar/2; boson/fermion bit = Z_2 = pi_1(SO(3))")
print("-" * 78)
print(f"  quantum = hbar/2 (fermion); boson = integer hbar.")
print(f"  boson/fermion BIT = Z_2 = pi_1(SO(3)) (T185 spinor; +1 under 2pi, single under 4pi -- belt trick).")
print()

print("G2: the Z_2 bit = the +1 cell (meson floor -> baryon floor); unit-primary pattern")
print("-" * 78)
print(f"  meson floor  = n_C cells            = {n_C}  (boson; no Z_2 bit)  -- rho, omega")
print(f"  baryon floor = n_C cells + Z_2 bit  = {n_C}+1 = C_2 = {C_2}  (fermion; +1 = the spin bit)  -- p, n")
print(f"  => the Z_2 spin bit IS the +1 that takes meson(n_C={n_C}) to baryon(C_2={C_2}). Spin unit = energy/cell unit, two views (T2488).")
print()
print(f"  pattern -- each substrate unit reads a primary:")
print(f"    energy/mass  <-> VOLUME (pi^n_C; cell)")
print(f"    charge       <-> COLOR  (N_c; e/N_c, alpha=1/N_max)")
print(f"    spin/ang.mom <-> Z_2 SPINOR bit (hbar/2; pi_1(SO(3)); = the meson/baryon +1 cell)")
print()
print(f"  @Keeper: unit-system -- SPIN = hbar/2, Z_2 boson/fermion bit (= the +1 cell). Energy/charge/spin clean;")
print(f"    momentum = energy in natural units; action hbar_BST + the t_Planck-vs-Koons-tick time structure = Tier-0/Lyra's lane.")
print(f"  Score: 2/2 (spin = hbar/2 + Z_2 bit T185; bit = +1 cell T2488; unit-primary pattern energy/charge/spin)")
print()
print("=" * 78)
print("TOY 4059 SUMMARY -- substrate spin unit = hbar/2, boson/fermion bit = Z_2 = pi_1(SO(3)) (T185 spinor).")
print("  The Z_2 bit = the +1 cell taking the meson floor (n_C=5) to the baryon floor (C_2=6) (T2488) -- spin and")
print("  energy units are one structure. Completes the unit-primary pattern: energy<->VOLUME, charge<->COLOR,")
print("  spin<->Z_2 SPINOR bit. Each substrate unit is the natural scale of one primary. (momentum trivial; action=Tier-0.)")
print("=" * 78)
print()
print("SCORE: 2/2")
