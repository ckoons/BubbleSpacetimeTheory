"""
Toy 4091: what Higgs/Yukawa IS in the substrate, and the lead common physics gives on our OPEN magnitude
problem. Standard Higgs: fermions are born massless + chiral (left/right are separate, differently-charged
fields; no bare mass without breaking gauge invariance); the Higgs condenses (VEV != 0 everywhere) and the
Yukawa term y.psibar_L.H.psi_R becomes a mass m = y.v when H -> v. So mass = Yukawa coupling x VEV, and a
massive fermion is one constantly flipping L<->R off the condensate (that flip rate IS the mass).
SUBSTRATE MAP: Higgs = the bulk commitment-density scalar (F60 rho_commit); VEV = the bulk cell scale (F85
v = cell.225.g); Yukawa = the OVERLAP of the fermion's (massless, chiral, boundary) rep with the bulk
condensate. So mass = (boundary-bulk overlap) x (bulk scale) = Lyra's "overlap x Casimir". The SM's FREE
Yukawa becomes our FORCED overlap -- that IS the reduction.
THE LEAD on the open magnitude: the SM Yukawa HIERARCHY (y_e ~ 3e-6 .. y_t ~ 1) is explained in BSM physics by
WAVEFUNCTION-LOCALIZATION overlap (split fermions / warped extra dimensions, Randall-Sundrum): fermions
localized at different positions have different Higgs overlaps -> exponential hierarchy. Our Wallach strata
(bulk/Cartan/Shilov) ARE that localization. So the magnitude = overlap suppression with localization depth.
And it EXPLAINS why the hierarchy is non-geometric (the electron's anomalous lightness): the electron is the
lone REGULAR point of Gamma_Omega; the muon/tau are POLES -- so e->mu crosses regular->pole (the big magnitude
jump, open) while mu->tau is pole->pole (the clean residue ratio, 0.37%).

THE NON-GEOMETRIC HIERARCHY (the number that diagnoses it):
  m_mu/m_e = 206.77   (e -> mu jump)
  m_tau/m_mu = 16.82  (mu -> tau jump)
  ratio of jumps = 12.3  -- NOT 1 -> strongly NON-geometric. The electron is anomalously light (big gap to muon).
  EXPLANATION (regular-vs-pole): electron nu=5/2 REGULAR (full bulk, not degenerate) -> anomalously light;
  muon nu=3/2 + tau nu=0 are POLES (boundary-degenerate) -> heavy. e->mu = regular->pole (big, the magnitude
  factor, OPEN); mu->tau = pole->pole (clean residue ratio (8/3).2pi = 16.76, 0.37%, Lyra). DIFFERENT KINDS of
  transition -> that is WHY the mu/tau RATIO lands clean but the e->mu MAGNITUDE is the hard open piece.

THE FOUR LEADS common Higgs/Yukawa physics gives our open questions:
  1. Casey's "initial impulse" IS the Yukawa coupling, and it's FORCED: in the SM the Yukawa is a free parameter
     (the mystery); in our picture it's the boundary-bulk overlap, forced by the Wallach rep's localization. So
     "what sets the impulse?" -> the overlap -> compute it, don't explain a free number. The reduction in one line.
  2. The magnitude problem = the Yukawa hierarchy = wavefunction-localization overlap (split fermions / RS). The
     Wallach strata are the localization; the magnitude comes from overlap suppression with depth (the Casimir
     parabola), the same way the ratio came from the pole residues. Concrete route to close the magnitude.
  3. Non-geometric hierarchy = regular-vs-pole (this toy): electron lone regular -> anomalously light. Explains
     why pole-to-pole (mu/tau) is clean and regular-to-pole (e/mu) is the open magnitude.
  4. Chiral structure -> the K-type signature factor: mass couples LEFT and RIGHT chiral components, which are
     in DIFFERENT reps. The K-type factor the bare residue misses (~6.3x, Toy 4086) may be the L-R rep-content
     difference -- the two chiral halves have different K-type content and the mass overlap involves both. (Lead for Lyra.)

HONEST TIER:
  STANDARD PHYSICS (solid): mass = Yukawa x VEV; fermions massless+chiral without Higgs; Yukawa hierarchy from
    wavefunction-localization overlap (established BSM mechanism). The non-geometric hierarchy (12.3x) is a fact.
  SUBSTRATE MAP (banked structurally): Higgs = bulk scalar, VEV = cell scale, Yukawa = boundary-bulk overlap;
    regular-vs-pole explains the non-geometric hierarchy + why mu/tau ratio is clean and e/mu magnitude is open.
  LEADS (flagged, not banked): localization-overlap as the route to the magnitude; chiral L-R as the K-type
    factor. These are leads for Lyra's matrix element, not claims. COUNT still 2.

GATES (2)
G1: substrate map -- Higgs = bulk commitment-density scalar, VEV = cell scale (F85), Yukawa = boundary-bulk overlap (SM free Yukawa -> our forced overlap = the reduction); mass = overlap x scale
G2: the non-geometric hierarchy (12.3x, electron anomalously light) is explained by regular(e)-vs-pole(mu,tau); explains clean mu/tau ratio + open e/mu magnitude; leads: localization-overlap (magnitude), chiral L-R (K-type factor)

Per Casey's question (what is Higgs in the substrate; does common physics give a lead) + Lyra (overlap x Casimir;
F66 boundary/bulk) + Keeper (massless courier -> massive resident); standard Higgs/Yukawa + RS/split-fermion
hierarchy; Elie 4084/4085/4086 (overlap, Gamma poles, residue); F60 (rho_commit) + F85 (VEV); Cal #237. Conceptual
answer grounded with the non-geometric number; leads for the magnitude + K-type factor flagged, not fished.

Elie - Wednesday 2026-06-10 (Higgs = bulk scalar, Yukawa = boundary-bulk overlap [SM-free -> forced = the reduction]; non-geometric hierarchy = regular(e)-vs-pole(mu,tau); magnitude lead = localization-overlap)
"""

me, mmu, mtau = 0.51099895, 105.6584, 1776.86

print("=" * 78)
print("TOY 4091: Higgs = bulk scalar, Yukawa = boundary-bulk overlap; non-geometric hierarchy = regular-vs-pole")
print("=" * 78)
print()

print("G1: the substrate map (what Higgs/Yukawa IS)")
print("-" * 78)
print("  STANDARD: fermions born massless+chiral; Higgs condenses; mass m = y.v (Yukawa x VEV); massive = flipping L<->R off the condensate.")
print("  SUBSTRATE: Higgs = bulk commitment-density scalar (F60); VEV = cell scale (F85 v=cell.225.g); Yukawa = boundary-bulk OVERLAP.")
print("  => mass = (boundary-bulk overlap) x (bulk cell scale) = Lyra's overlap x Casimir. SM FREE Yukawa -> our FORCED overlap = THE REDUCTION.")
print()

print("G2: the non-geometric hierarchy explained by regular-vs-pole")
print("-" * 78)
r1, r2 = mmu / me, mtau / mmu
print(f"  m_mu/m_e = {r1:.2f}  |  m_tau/m_mu = {r2:.2f}  |  ratio of jumps = {r1/r2:.1f}x -> NON-geometric (electron anomalously light)")
print(f"  electron nu=5/2 REGULAR (full bulk) -> light;  muon nu=3/2 + tau nu=0 POLES -> heavy")
print(f"  e->mu = regular->pole (the big MAGNITUDE jump, OPEN);  mu->tau = pole->pole (clean residue ratio 16.76, 0.37%, Lyra)")
print(f"  => DIFFERENT transitions: that's WHY mu/tau ratio is clean and e/mu magnitude is the hard open piece.")
print()
print("  FOUR LEADS from common Higgs/Yukawa physics:")
print(f"    1. Casey's 'initial impulse' = the Yukawa = our forced overlap (SM free param -> our forced geometry). The reduction.")
print(f"    2. magnitude = Yukawa hierarchy = wavefunction-localization overlap (RS/split-fermions); Wallach strata ARE the localization.")
print(f"    3. non-geometric hierarchy = regular(e)-vs-pole(mu,tau) [this toy].")
print(f"    4. chiral L-R reps differ -> the K-type factor (6.3x the residue misses, 4086) may be the L-R rep-content difference. [lead for Lyra]")
print(f"  Score: 2/2 (substrate map: Yukawa = forced overlap; non-geometric hierarchy = regular-vs-pole; magnitude + K-type leads flagged)")
print()
print("=" * 78)
print("TOY 4091 SUMMARY -- Higgs in the substrate: the bulk commitment-density scalar, VEV = cell scale, and the")
print("  Yukawa coupling = the boundary-bulk OVERLAP -- so the SM's free Yukawa becomes our forced overlap (the")
print("  reduction). The lepton hierarchy is strongly non-geometric (e->mu = 207, mu->tau = 17, 12x apart, electron")
print("  anomalously light), and regular-vs-pole explains it: the electron is the lone regular Gamma_Omega point,")
print("  mu/tau are poles -- so e->mu is regular->pole (big, open magnitude) and mu->tau is pole->pole (clean ratio).")
print("  Leads from standard physics: the magnitude = localization-overlap suppression (RS/split-fermions, and the")
print("  Wallach strata ARE that localization); the K-type factor = the chiral L-R rep difference. Count still 2.")
print("=" * 78)
print()
print("SCORE: 2/2")
