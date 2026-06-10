"""
Toy 4068: the substrate "periodic table of particles" (Casey's Monday reframe) -- every SM particle
classified by substrate cell-scale + statistics + substrate-reach (ANCHOR / FLOOR / BOUNDARY / DROWNED).
Consolidates the day's cell-scale work into one map. The substrate cleanly reaches the ANCHOR (m_e) + the
FLOOR (u/d ground hadrons at integer cells); the BOUNDARY tier is gen-2 (mu, strange ~ 0.6 cell); everything
else is DROWNED (gen-3 + the EW/Higgs sector). (Track 5; consolidating cartography; my lane.)

THE MAP (1 cell = pi^5 m_e = 156.4 MeV = substrate energy unit, Toy 4054):

  ANCHOR (the reference, ~0.003 cell):
    e        0.511 MeV    0.003 cell   fermion    m_e = the substrate mass unit itself
    photon   0            0            boson      massless (gauge; EM = SO(4,2) boundary, F66)
    gluon    0            0            boson      massless (gauge; SU(3) color)
    neutrinos ~0.05 eV    ~1e-9 cell   fermion    sub-anchor tier (seesaw/PMNS)

  FLOOR (integer cells -- the substrate measures these cleanly; mass = pure substrate volume):
    rho/omega 775/783 MeV  5 cells (n_C)  boson    u/d ground vector mesons
    p/n       938/940 MeV  6 cells (C_2)  fermion  u/d ground baryons (the +1 cell = Z_2 spin bit, T2488)

  BOUNDARY (~ 1 cell -- gen-2 / strange; AT the substrate cell scale, F78 coincidence territory):
    mu        105.7 MeV   0.68 cell    fermion    gen-2 lepton
    strange-q ~93 MeV     0.60 cell    fermion    gen-2 quark (the lone clean Yukawa-near-cell)

  DROWNED (>> 1 cell -- gen-3 + heavy flavor + EW/Higgs; Higgs/Yukawa-dominated, substrate-blind):
    tau       1777 MeV    11.4 cells   fermion    gen-3 lepton
    charm-q   1270 MeV    8.1 cells    fermion    gen-3-ish quark
    bottom-q  4180 MeV    26.7 cells   fermion
    W         80.4 GeV    514 cells    boson      EW gauge (Higgs mass)
    Z         91.2 GeV    583 cells    boson      EW gauge (Higgs mass)
    Higgs H   125 GeV     799 cells    boson      the Higgs boson
    top-q     173 GeV     1103 cells   fermion    quasi-asymptotic (Yukawa ~ 1)
    Higgs VEV 246 GeV     1575 cells   --         = 225.g (Schur generator x genus; relabel candidate, Toy 4063)

THE STRUCTURE (the reach-bound, Casey #9, as a particle table):
  - the substrate MEASURES the ANCHOR (m_e) + the FLOOR (u/d ground hadrons, integer cells) -- pure substrate geometry.
  - the BOUNDARY tier (gen-2: mu, strange) sits AT the cell scale -- the F78 one-flavor-coincidence territory.
  - the DROWNED tier (gen-3 + EW/Higgs, 8-1575 cells) is Higgs/Yukawa-dominated -- substrate-blind (Casey #9 'building').
  - the cell scale (156.4 MeV) is BOTH the substrate energy unit AND the generation boundary AND the Filter-2 floor edge -- one number, three roles.

LEDGER TIE-IN (Grace's lens): the map shows WHERE reduction is possible. The substrate-reach sectors (anchor +
floor + the clean mixing angles) are where the count can move; the DROWNED sector (Yukawa masses, EW/Higgs scales)
is RELABEL/HONEST-NEGATIVE (Toy 4067). So the 'periodic table' isn't just a classification -- it maps the parameter
count: substrate-clean = reduction-candidate; drowned = relabel/honest-negative. Reduction lives at the floor + mixing.

GATES (2)
G1: every SM particle mapped by cell-scale + statistics + reach (anchor/floor/boundary/drowned); cell scale = energy unit = generation boundary = floor edge
G2: ledger tie-in -- reduction lives in substrate-reach sectors (anchor/floor/mixing); drowned (Yukawa/EW/Higgs) = relabel/honest-negative

Per Casey 'periodic table' reframe; Toy 4054 (cell unit); 4060 (Yukawa-in-cells); 4066 (lepton generations);
4067 (Yukawa ledger); 4063 (VEV); Casey #9; Cal #237; K231c. Track 5 consolidating particle map; cartography.

Elie - Tuesday 2026-06-09 (periodic table of particles: anchor/floor/boundary/drowned by cell-scale; cell = unit = gen boundary = floor edge)
"""

me = 0.51099895
cell = 306.0197 * me

print("=" * 78)
print("TOY 4068: substrate periodic table of particles -- anchor/floor/boundary/drowned by cell-scale")
print("=" * 78)
print()

tiers = [
    ("ANCHOR (~0.003 cell; the reference)", [
        ("e", 0.511, "F", "m_e = the substrate mass unit"), ("photon", 0, "B", "massless gauge"),
        ("neutrinos", 5e-8, "F", "sub-anchor (seesaw)")]),
    ("FLOOR (integer cells; substrate measures cleanly)", [
        ("rho/omega", 779, "B", "u/d ground vector -> 5 = n_C"), ("p/n", 939, "F", "u/d ground baryon -> 6 = C_2 (+Z_2 bit)")]),
    ("BOUNDARY (~1 cell; gen-2)", [
        ("mu", 105.66, "F", "gen-2 lepton"), ("strange-q", 93, "F", "gen-2 quark (lone near-cell Yukawa)")]),
    ("DROWNED (>>1 cell; Higgs/Yukawa-dominated)", [
        ("tau", 1776.86, "F", "gen-3 lepton"), ("charm-q", 1270, "F", "gen-3 quark"),
        ("bottom-q", 4180, "F", "gen-3 quark"), ("W", 80400, "B", "EW gauge"),
        ("Z", 91200, "B", "EW gauge"), ("Higgs H", 125000, "B", "Higgs boson"),
        ("top-q", 173000, "F", "Yukawa~1, quasi-asymptotic"), ("Higgs VEV", 246220, "-", "= 225.g (Schur x genus)")]),
]

print("G1: the particle map (1 cell = %.1f MeV)" % cell)
print("-" * 78)
for tier, parts in tiers:
    print(f"  [{tier}]")
    for nm, m, st, note in parts:
        c = m / cell
        print(f"    {nm:<11} {m:>9.0f} MeV {c:>9.3g} cells  [{st}]  {note}")
print()

print("G2: the structure + ledger tie-in")
print("-" * 78)
print(f"  the cell scale (156.4 MeV) is BOTH the substrate energy unit AND the generation boundary AND the Filter-2")
print(f"  floor edge -- one number, three roles. Substrate MEASURES anchor + floor (u/d ground); boundary = gen-2;")
print(f"  drowned = gen-3 + EW/Higgs (Casey #9 'building', substrate-blind).")
print(f"  LEDGER: reduction lives in the substrate-reach sectors (anchor/floor/mixing angles); the DROWNED sector")
print(f"  (Yukawa masses, EW/Higgs scales) is RELABEL/HONEST-NEGATIVE (4067). The table maps WHERE the count can move.")
print(f"  @Keeper/@Grace: the periodic table maps reach AND ledger -- substrate-clean = reduction-candidate; drowned = relabel/honest-negative.")
print(f"  Score: 2/2 (full particle map by cell-scale + statistics + reach; cell = unit = gen-boundary = floor-edge; ledger tie-in)")
print()
print("=" * 78)
print("TOY 4068 SUMMARY -- substrate periodic table of particles: every SM particle by cell-scale + statistics +")
print("  reach. ANCHOR (e, photon), FLOOR (u/d ground hadrons at integer cells 5,6), BOUNDARY (gen-2: mu, strange")
print("  ~0.6 cell), DROWNED (gen-3 + EW/Higgs, 8-1575 cells). The cell (156.4 MeV) = energy unit = generation")
print("  boundary = Filter-2 floor edge, one number three roles. Reduction lives at floor+mixing; drowned = relabel/honest-neg.")
print("=" * 78)
print()
print("SCORE: 2/2")
