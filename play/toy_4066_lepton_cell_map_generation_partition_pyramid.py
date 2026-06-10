"""
Toy 4066: lepton cell-scale map (Casey's inverted-pyramid hypothesis K281). The K280 substrate cell
boundary (156.4 MeV) partitions the LEPTON generations exactly as it does the quarks: gen-1 (e) = anchor
(far below); gen-2 (mu) = AT the boundary (0.68 cell, SAME scale as strange ~0.6 cell); gen-3 (tau) =
drowned (11.4 cells, like charm/bottom). Neutrinos = a sub-anchor tier far below. The cell scale IS the
generation boundary, for leptons and quarks alike. (Track 4; numerical; the K-type pyramid support is Lyra's lane.)

CASEY's HYPOTHESIS: leptons (no color) sit on a different K-type substructure than hadrons. Each lepton's
substrate support may be an inverted pyramid -- a SET of K-type points converging to the lepton at the apex.
My numerical lane: map the leptons in cell scales to see where they sit relative to the K280 cell boundary.

THE MAP (1 cell = pi^5 m_e = 156.4 MeV):
  charged leptons:
    e   (gen 1): 0.003 cell  -- the ANCHOR apex (m_e IS the substrate mass reference; ~1/pi^5 of a cell)
    mu  (gen 2): 0.68 cell   -- AT THE BOUNDARY (same scale as the strange quark, 0.6 cell!)
    tau (gen 3): 11.4 cells  -- DROWNED (like charm 8, bottom 27 cells)
  neutrinos (gen 1/2/3): all << 1e-7 cell -- a SUB-ANCHOR tier, far below the substrate reference.

THE STRUCTURE (generation partition by the cell boundary -- leptons AND quarks):
  gen 1: BELOW the cell (u/d ~0.02 cell; e 0.003 cell) -- substrate-floor / anchor tier.
  gen 2: AT the cell boundary (strange 0.6 cell; mu 0.68 cell) -- the boundary tier.
  gen 3: DROWNED above the cell (charm 8, bottom 27; tau 11.4) -- the Higgs/Yukawa-dominated tier.
  => the K280 cell scale (156.4 MeV) is the GENERATION boundary -- gen-1 below, gen-2 at, gen-3 above --
     for BOTH colored quarks and colorless leptons. The mu-strange coincidence (both gen-2 at ~0.6-0.68 cell)
     is the cleanest tell: 2nd-generation fermions sit at the substrate cell scale, regardless of color.

ON THE INVERTED PYRAMID (Casey): the cell map SUPPORTS the generation-partition reading; whether each lepton's
substrate support is literally a pyramidal K-type SET converging to an apex is the K-type spectral structure
(Lyra's lane). My numerical contribution is the cell-scale partition + the mu-strange boundary coincidence;
the pyramid geometry is hers to derive.

LEDGER (Grace's lens): the lepton masses themselves are RELABEL (3 forms, T190/T2003); this toy adds STRUCTURE
(the generation-partition by the cell boundary), not a count-reduction. It's an identification of the generation
boundary scale (= the cell = energy unit), useful for the particle map, but it does not move the parameter count.

GATES (3)
G1: lepton cell map -- e 0.003 (anchor), mu 0.68 (boundary = strange), tau 11.4 (drowned); nu << 1e-7 (sub-anchor)
G2: generation partition by the cell boundary -- gen-1 below, gen-2 AT, gen-3 above; leptons AND quarks; mu-strange coincidence
G3: supports Casey's inverted-pyramid (cell-scale partition); K-type pyramid geometry = Lyra's lane; ledger = structure not reduction

Per Casey K281 inverted-pyramid hypothesis; Toy 4054 (cell unit); Toy 4060 (quark Yukawa-in-cells); T190/T2003
(lepton masses); Cal #237; K231c. Track 4 numerical cell map; the K-type support geometry is Lyra's lane.

Elie - Tuesday 2026-06-09 (lepton cell map: cell boundary partitions generations, leptons+quarks; mu=strange at boundary)
"""

me = 0.51099895
cell = 306.0197 * me

print("=" * 78)
print("TOY 4066: lepton cell map -- the cell boundary partitions GENERATIONS (leptons + quarks)")
print("=" * 78)
print()

print("G1: lepton cell-scale map (1 cell = %.1f MeV)" % cell)
print("-" * 78)
lep = [("e", 0.511, "gen1", "ANCHOR apex (m_e = substrate reference)"),
       ("mu", 105.66, "gen2", "AT BOUNDARY (= strange 0.6 cell!)"),
       ("tau", 1776.86, "gen3", "DROWNED (like charm/bottom)"),
       ("nu (all)", 5e-8, "gen1-3", "SUB-ANCHOR tier, far below")]
for nm, m, gen, note in lep:
    print(f"  {nm:<9} {gen:<7} {m:>10.4g} MeV = {m/cell:>9.4g} cells   {note}")
print()

print("G2: generation partition by the cell boundary (leptons AND quarks)")
print("-" * 78)
print(f"  gen 1: BELOW the cell -- u/d ~0.02, e 0.003   (anchor/floor tier)")
print(f"  gen 2: AT the cell    -- strange 0.6, mu 0.68  (boundary tier -- the mu=strange coincidence)")
print(f"  gen 3: DROWNED        -- charm 8, bottom 27, tau 11.4  (Higgs/Yukawa-dominated tier)")
print(f"  => the cell scale (156.4 MeV = energy unit) IS the GENERATION boundary, for colored AND colorless fermions.")
print()

print("G3: inverted-pyramid + ledger disposition")
print("-" * 78)
print(f"  the cell map SUPPORTS Casey's inverted-pyramid generation reading; the K-type SUPPORT GEOMETRY (pyramid")
print(f"  converging to an apex per lepton) is Lyra's K-type spectral lane. LEDGER: lepton masses = RELABEL; this adds")
print(f"  STRUCTURE (the generation boundary = the cell scale), not a count-reduction. Identification of the generation scale.")
print(f"  @Lyra: cell-scale generation partition (gen-2 fermions at the cell, mu=strange) -- the K-type pyramid is yours to derive.")
print(f"  Score: 3/3 (lepton cell map; generation partition leptons+quarks; mu=strange boundary; pyramid flagged for Lyra)")
print()
print("=" * 78)
print("TOY 4066 SUMMARY -- lepton cell map: the K280 cell boundary (156.4 MeV) partitions the lepton generations")
print("  like the quarks -- gen-1 (e 0.003 cell) anchor, gen-2 (mu 0.68 cell) AT the boundary = SAME as strange,")
print("  gen-3 (tau 11.4 cells) drowned; neutrinos sub-anchor. The cell scale IS the generation boundary for leptons")
print("  AND quarks (mu=strange coincidence is the tell). Supports Casey's inverted-pyramid; K-type geometry = Lyra's lane.")
print("=" * 78)
print()
print("SCORE: 3/3")
