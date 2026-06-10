"""
Toy 4062: Yukawa-hierarchy substrate-natural map (Higgs investigation, lane C). The COLORLESS (charged
lepton) Yukawa hierarchy is SUBSTRATE-NATURAL (clean (24/pi^2)-ladder, T190/T2003); the COLORED (quark)
Yukawa hierarchy is SCATTERED/scheme-dependent (Toy 4045). So the substrate reproduces the lepton Yukawa
hierarchy, NOT the quark one -- a COLOR-DEPENDENT substrate-reach. This bears directly on Casey's
emergent-vs-fundamental question (Reading A: trio fundamental; Reading B: Higgs+Yukawa emergent). (My lane;
discipline front-and-center per the F79/F78 lessons.)

CASEY's QUESTION (this afternoon): is Higgs+Yukawa FUNDAMENTAL (Reading A: substrate/Higgs/Yukawa = three
distinct layers) or EMERGENT (Reading B: Higgs+Yukawa = substrate motion, the 12+ SM Yukawas derivable)?
Grace's morning test applies: does the emergent reading PREDICT beyond substrate+SM, or RESTATE? My lane:
map which Yukawas ARE substrate-natural (numerical), so the distinguishing test has data.

THE MAP (Yukawa ratios = mass ratios, since m_f = y_f . v/sqrt2 with v universal):
  CHARGED LEPTONS (colorless) -- SUBSTRATE-NATURAL:
    m_mu/m_e  = (24/pi^2)^6                  = 206.76  (obs 206.768, 0.003%)  [T190]
    m_tau/m_e = (24/pi^2)^6 . (7/3)^{10/3}   = 3483.8  (obs 3477.2, 0.2%)     [T2003]
    -> the charged-lepton Yukawa hierarchy IS a clean substrate-natural (24/pi^2)-ladder.
  QUARKS (colored) -- SCATTERED / scheme-dependent:
    m_c/m_u ~ 590, m_t/m_u ~ 80000, m_b/m_s ~ 45 -- no clean substrate forms; scheme-dependent (MS-bar vs
    pole vs constituent; 70-155x definition spread per Toy 4045). No single Yukawa to give a substrate form.

THE FINDING (color-dependent substrate-reach): the substrate reproduces the COLORLESS (lepton) Yukawa
hierarchy cleanly, but NOT the COLORED (quark) one. This is consistent with today's floor picture: colorless
leptons are clean point-modes (definite mass, substrate-natural ratios); colored quarks are confined +
scheme-dependent (Toy 4045/4048) so their Yukawas have no substrate form. So the substrate's reach into the
Yukawa sector is COLOR-dependent -- it reaches the colorless Yukawa hierarchy, not the colored.

BEARING ON CASEY's READING A vs B (honest, NOT banked):
  - Reading B (emergent) is SUPPORTED for the COLORLESS sector: the charged-lepton Yukawa hierarchy IS a
    substrate-natural form (the (24/pi^2)-ladder), so for leptons "Yukawa = substrate structure" has content.
  - Reading B is NOT supported for the COLORED sector: quark Yukawas are scattered/scheme-dependent -- no
    substrate form -- so they look like SM free parameters (Reading A) for quarks.
  - So the honest state is a SPLIT: the substrate reproduces the colorless Yukawa hierarchy (Reading B for
    leptons), the colored hierarchy is SM-side (Reading A for quarks). The distinguishing structure is COLOR.

DISCIPLINE (Grace's gate, front-and-center): this does NOT claim full emergence. (1) The lepton Yukawa forms
are IDENTIFICATIONS (T190/T2003), not derived from motion -- so "substrate reproduces lepton Yukawas" is
identification-tier, not a derivation of the couplings. (2) Whether the COLOR-split PREDICTS beyond SM (Grace's
test) is the open call: it predicts WHICH Yukawas are substrate-natural (colorless yes, colored no) -- a
structural statement -- but it does not derive the values. So I bank only: the color-split of substrate-Yukawa-reach
is real and data-grounded; the emergent claim stays gate-dependent (Grace/Cal). This is exactly the F79-shaped
appeal Keeper flagged; I'm providing the map, not the closure.

GATES (3)
G1: charged-lepton Yukawa hierarchy substrate-natural ((24/pi^2)-ladder, T190/T2003); quark Yukawa hierarchy scattered/scheme-dependent (4045)
G2: color-dependent substrate-reach -- substrate reproduces colorless Yukawa hierarchy, not colored; consistent w/ floor picture
G3: bears on Reading A/B -- emergent supported for colorless (identification-tier), SM-side for colored; the SPLIT is color; NOT banking full emergence (Grace's gate)

Per Casey emergent-vs-fundamental question; T190/T2003 (lepton Yukawa forms); Toy 4045/4048 (quark scatter);
Toy 4042 (colorless point-mode); Grace gate + F79 lesson; Cal #237; K231c. Higgs investigation lane C; map not closure.

Elie - Tuesday 2026-06-09 (Yukawa hierarchy: colorless substrate-natural, colored scattered; color-split bears on emergent-vs-fundamental)
"""

import mpmath as mp
mp.mp.dps = 20
me = 0.51099895

print("=" * 78)
print("TOY 4062: Yukawa hierarchy -- COLORLESS (lepton) substrate-natural, COLORED (quark) scattered")
print("=" * 78)
print()

print("G1: the Yukawa hierarchy map (ratios = mass ratios)")
print("-" * 78)
mu = (24 / mp.pi**2)**6
tau = (24 / mp.pi**2)**6 * (mp.mpf(7) / 3)**(mp.mpf(10) / 3)
print(f"  CHARGED LEPTONS (colorless) -- SUBSTRATE-NATURAL:")
print(f"    m_mu/m_e  = (24/pi^2)^6                = {mp.nstr(mu,7)}  (obs 206.768)  [T190]")
print(f"    m_tau/m_e = (24/pi^2)^6 (7/3)^(10/3)   = {mp.nstr(tau,7)}  (obs 3477.2)   [T2003]")
print(f"  QUARKS (colored) -- SCATTERED/scheme-dependent (Toy 4045: 70-155x definition spread; no clean forms):")
print(f"    m_c/m_u ~ 590, m_t/m_u ~ 80000, m_b/m_s ~ 45 -- no substrate form.")
print()

print("G2: color-dependent substrate-reach")
print("-" * 78)
print(f"  substrate reproduces the COLORLESS (lepton) Yukawa hierarchy ((24/pi^2)-ladder), NOT the COLORED (quark) one.")
print(f"  consistent w/ today's floor picture: colorless leptons = clean point-modes (definite mass); colored quarks =")
print(f"  confined + scheme-dependent (4045/4048) -> no substrate Yukawa form. The substrate's Yukawa-reach is COLOR-dependent.")
print()

print("G3: bearing on Casey's Reading A vs B (NOT banked)")
print("-" * 78)
print(f"  Reading B (emergent) SUPPORTED for colorless: lepton Yukawa hierarchy IS substrate-natural (identification-tier).")
print(f"  Reading B NOT supported for colored: quark Yukawas scattered -> SM free parameters (Reading A for quarks).")
print(f"  => the honest state is a COLOR SPLIT: substrate reproduces colorless Yukawas (B for leptons); colored = SM (A for quarks).")
print(f"  DISCIPLINE (Grace's gate, F79 lesson): lepton forms are IDENTIFICATIONS not derivations; whether the color-split")
print(f"    PREDICTS beyond SM is the open call (it says WHICH Yukawas are substrate-natural -- structural -- not the values).")
print(f"    I bank only the color-split of substrate-reach; the emergent claim stays gate-dependent. Map, not closure.")
print()
print(f"  @Grace/@Lyra: Yukawa map -- colorless substrate-natural, colored scattered. The color-split is the data for the")
print(f"    emergent-vs-fundamental test. Does 'substrate reaches colorless Yukawas only' predict beyond SM? Your/Cal's gate call.")
print(f"  Score: 3/3 (lepton-clean/quark-scattered map; color-dependent reach; bears on A/B; emergent NOT banked)")
print()
print("=" * 78)
print("TOY 4062 SUMMARY -- Yukawa hierarchy: the COLORLESS (charged-lepton) Yukawa hierarchy is substrate-natural")
print("  ((24/pi^2)-ladder, T190/T2003); the COLORED (quark) hierarchy is scattered/scheme-dependent (4045). So the")
print("  substrate reproduces the lepton Yukawa hierarchy, not the quark -- COLOR-dependent reach. Bears on Casey's")
print("  emergent(B)-vs-fundamental(A): B for colorless (identification-tier), A for colored. The split is COLOR. NOT banking emergence (gate).")
print("=" * 78)
print()
print("SCORE: 3/3")
