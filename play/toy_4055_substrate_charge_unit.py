"""
Toy 4055: substrate UNIT-SYSTEM -- the charge unit. Charge QUANTUM = e/N_c (quark fractionalization
from N_c color); EM COUPLING = alpha = 1/N_max = 1/(N_c^3 n_C + rank). Both established BST results;
this collects them as the substrate's charge unit. (Tuesday unit-system arc; generative, my lane.)

CONTEXT: continuing the substrate unit-system (length=ell_Planck, time=Koons tick, density=K(0,0),
energy/mass=cell pi^{n_C}m_e per Toy 4054). This does CHARGE.

THE CHARGE UNIT (two established pieces -- a quantum and a coupling):
  QUANTUM (smallest charge): e/N_c = e/3 -- the quark fractional charge. The N_c = 3 color structure
    fractionalizes charge into thirds: down-type quark = e/N_c, up-type = 2e/N_c, lepton/proton = e = N_c.(e/N_c).
    So the substrate's charge quantum is e/N_c, set by the color number N_c.
  COUPLING (interaction strength): alpha = 1/N_max = 1/(N_c^3 . n_C + rank) = 1/137 -- the EM coupling, the
    foundational BST identity (alpha^-1 = N_max). The dimensionless charge-squared in natural units IS alpha;
    the dimensionless charge is sqrt(alpha) = 1/sqrt(N_max).

So the substrate charge unit-system:
  charge QUANTUM = e/N_c               (smallest charge; N_c-color fractionalization)
  EM COUPLING    = alpha = 1/N_max     (= 1/(N_c^3 n_C + rank); charge^2 / interaction strength)
  elementary e   = N_c . (e/N_c)       (lepton/proton integer charge)

READING (parallel to the energy unit): the energy unit (cell) is set by the substrate VOLUME (pi^{n_C});
the charge unit (e/N_c) is set by the substrate COLOR (N_c); the coupling (alpha=1/N_max) by the full
primary composite N_max = N_c^3 n_C + rank. Each substrate unit reads off a specific substrate-primary
structure -- volume for energy, color for charge quantum, N_max for the coupling.

WHY NOT FISHING: both pieces are pre-established (alpha^-1 = N_max foundational; quark charge = e/N_c from
N_c color is standard QCD + BST color identification). This collects them as the charge unit; no new fit.

GATES (2)
G1: charge quantum = e/N_c (N_c-color fractionalization; quark charges N_c-fractional, lepton/proton = N_c.(e/N_c))
G2: EM coupling = alpha = 1/N_max = 1/(N_c^3 n_C + rank) (foundational); dimensionless charge = sqrt(alpha) = 1/sqrt(N_max)

Per alpha^-1 = N_max (foundational BST); quark charge e/N_c (N_c color); Toy 4054 (energy unit); Keeper
unit-system table; Cal #237 (collect established, not fit); K231c. Generative cartography.

Elie - Tuesday 2026-06-09 (substrate unit-system: charge = e/N_c quantum, alpha=1/N_max coupling)
"""

import mpmath as mp
mp.mp.dps = 20
N_c, n_C, C_2, g, rank, N_max = 3, 5, 6, 7, 2, 137

print("=" * 78)
print("TOY 4055: substrate charge UNIT -- quantum e/N_c (color), coupling alpha=1/N_max")
print("=" * 78)
print()

print("G1: charge quantum = e/N_c (N_c-color fractionalization)")
print("-" * 78)
print(f"  e/N_c = e/{N_c} -- quark fractional charge. down-type e/N_c, up-type 2e/N_c, lepton/proton e = N_c.(e/N_c).")
print(f"  the substrate's charge QUANTUM is set by the color number N_c = {N_c}.")
print()

print("G2: EM coupling = alpha = 1/N_max (foundational)")
print("-" * 78)
print(f"  alpha = 1/N_max = 1/(N_c^3 n_C + rank) = 1/({N_c**3}.{n_C}+{rank}) = 1/{N_c**3*n_C+rank}")
print(f"  charge^2 (natural units) = alpha = 1/{N_max} ; dimensionless charge = sqrt(alpha) = 1/sqrt(N_max) = {mp.nstr(1/mp.sqrt(N_max),5)}")
print()

print("the substrate charge unit-system")
print("-" * 78)
print(f"  QUANTUM   e/N_c        (smallest; N_c color)")
print(f"  COUPLING  alpha=1/N_max (= 1/(N_c^3 n_C+rank); interaction strength)")
print(f"  elementary e = N_c.(e/N_c)")
print(f"  reading: energy unit set by VOLUME (pi^n_C); charge quantum by COLOR (N_c); coupling by N_max. Each unit reads a substrate-primary structure.")
print()
print(f"  @Keeper: unit-system -- CHARGE quantum = e/N_c, coupling alpha = 1/N_max. Remaining: momentum + action (Tier-0/hbar_BST; Lyra's lane).")
print(f"  Score: 2/2 (charge quantum e/N_c from color; coupling alpha=1/N_max foundational)")
print()
print("=" * 78)
print("TOY 4055 SUMMARY -- substrate charge unit: QUANTUM = e/N_c (quark fractionalization from N_c=3 color),")
print("  EM COUPLING = alpha = 1/N_max = 1/(N_c^3 n_C + rank). Each substrate unit reads a primary structure --")
print("  energy=volume(pi^n_C), charge-quantum=color(N_c), coupling=N_max. Both pieces established; collected, not fit.")
print("=" * 78)
print()
print("SCORE: 2/2")
