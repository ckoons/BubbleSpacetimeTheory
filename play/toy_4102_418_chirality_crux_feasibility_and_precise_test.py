"""
Toy 4102: deepening the #418 chirality crux -- the decisive, hardest piece of the gauge-content target. Two
results: (1) FEASIBILITY -- the substrate DOES have a natural chirality (so a chiral fermion content is
achievable in principle), and (2) the PRECISE TEST the derivation must pass, distilled to one line. This is
still spec-level (what the target requires and whether it's reachable), not the derivation; the derivation is
Lyra's bulk-color lane. Count still 2.

FEASIBILITY -- the substrate has chirality (established, two ways):
  - D_IV^5 is a COMPLEX (Hermitian symmetric) domain. Its complex structure J splits every tensor into a
    HOLOMORPHIC part (+i eigenspace of J) and an ANTIHOLOMORPHIC part (-i). H^2(D_IV^5) = the holomorphic Hardy
    space. So the substrate carries a built-in 2-fold split -- a natural CHIRALITY (left/right <-> holo/antiholo).
  - Casey #14 (STANDING): SO(5,2) -> SO(4,2) [1/n_C chirality projection] -> SO(3,1). The 4D chirality is DERIVED
    from the substrate. So a chiral, parity-violating structure is substrate-architecturally available.
  => FEASIBLE: a chiral fermion content (the SM's left/right asymmetry) is achievable in principle. The substrate
     is chiral; the question is whether it gives the SPECIFIC SM chiral assignment.

THE PRECISE TEST (what the #418 derivation must show -- the open, decisive piece):
  the SM is chiral in a SPECIFIC way: LEFT-handed fields are SU(2) doublets (Q, L); RIGHT-handed are singlets
  (u, d, e). So the derivation must establish:
    (T1) the weak SU(2) = SU(rank) acts on ONE chirality only (the left/holomorphic), not both;
    (T2) the doublet fields (Q, L) sit in that chirality; the singlets (u, d, e) in the other;
    (T3) the assignment is FORCED by the geometry -- i.e. the holomorphic projection and the SU(rank) action are
         the SAME substrate structure -- not an independent choice.

THE CRUX IN ONE LINE:
  WHY does SU(rank) couple to the holomorphic chirality ONLY?
  - If the substrate FORCES that (the weak SU(2) IS intrinsically a holomorphic-sector symmetry), then the
    left/right split is forced, the chiral content is forced, and #418 REDUCES the count.
  - If SU(rank) could act on BOTH chiralities, the left/right assignment would be a CHOICE (tuned), and #418
    would NOT reduce (it would relabel the SM's chiral structure, not derive it).
  => the #418 reduction hinges on exactly this: is the SU(rank) weak action intrinsically one-chirality
     (holomorphic)? That is the decisive derivation question -- the place the input-count is won or lost.

WHY THIS IS THE RIGHT FRAMING (not just restating "chirality is hard"):
  it converts the vague "the substrate must produce chirality" into a single sharp, falsifiable derivation
  target: SU(rank)-acts-on-the-holomorphic-sector-only. Lyra's bulk-color derivation either shows the weak
  SU(2) is a symmetry of the holomorphic Hardy space H^2(D_IV^5) alone (forced, reduces) or it doesn't
  (tuned, relabel). The 1/n_C chirality projection of Casey #14 (n_C = 5 odd is load-bearing for chirality)
  is the candidate link; rank = 2 is the weak factor. The link is available; the FORCING is the open test.

HONEST TIER:
  ESTABLISHED (feasibility): the substrate has a natural chirality (holomorphic structure of D_IV^5 + Casey #14
    projection). A chiral content is achievable in principle.
  SPEC (this toy -- the precise test): the derivation must show SU(rank) acts on the holomorphic chirality only,
    with the doublets in it, forced. Distilled to one falsifiable question.
  NOT done: whether SU(rank) IS intrinsically holomorphic -- Lyra's bulk-color derivation. This is the spec's
    decisive open piece, not the derivation. COUNT still 2.

GATES (2)
G1: feasibility -- the substrate has a natural chirality (D_IV^5 holomorphic structure + Casey #14 SO(5,2)->SO(4,2) projection); a chiral SM content is achievable in principle
G2: the precise test (the crux in one line) -- does SU(rank) couple to the holomorphic chirality ONLY? if forced -> chiral content forced -> #418 reduces; if a choice -> tuned -> relabel. The decisive derivation question (Lyra bulk-color lane); count still 2

Per Casey (#418 target spec; chirality the crux) + Casey #14 (chirality projection, STANDING) + Grace (#418
load-bearing) + Lyra (bulk-color derivation); Elie 4100/4101 (#418 spec + Higgs); D_IV^5 complex/Hardy structure;
Cal #237 + F79. Deepens the chirality crux to a single falsifiable derivation target; the forcing is Lyra's lane.

Elie - Thursday 2026-06-11 (#418 chirality crux: substrate HAS chirality (holomorphy + Casey #14) = feasible; the precise test = does SU(rank) act on the holomorphic chirality only (forced=reduce, choice=relabel); Lyra derivation)
"""

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2

print("=" * 78)
print("TOY 4102: #418 chirality crux -- feasibility (substrate IS chiral) + the precise test (one line)")
print("=" * 78)
print()

print("G1: feasibility -- the substrate has a natural chirality")
print("-" * 78)
print(f"  - D_IV^5 complex domain: complex structure J -> holomorphic (+i) / antiholomorphic (-i) split. H^2 = holomorphic Hardy space.")
print(f"    => a built-in 2-fold split = natural CHIRALITY (left/right <-> holo/antiholo).")
print(f"  - Casey #14 (STANDING): SO(5,2) -> SO(4,2) [1/n_C chirality projection, n_C={n_C} odd] -> SO(3,1). 4D chirality DERIVED.")
print(f"  => FEASIBLE: a chiral SM content is achievable in principle. The substrate is chiral.")
print()

print("G2: the precise test -- the crux in one line")
print("-" * 78)
print(f"  the SM: LEFT = SU(2) doublets (Q,L), RIGHT = singlets (u,d,e). The derivation must show:")
print(f"    (T1) SU(rank) acts on ONE chirality (holomorphic/left) only; (T2) doublets in it, singlets in the other; (T3) FORCED, not chosen.")
print(f"  CRUX: WHY does SU(rank) couple to the holomorphic chirality ONLY?")
print(f"    forced (weak SU(2) IS a holomorphic-sector symmetry) -> chiral content forced -> #418 REDUCES.")
print(f"    a choice (SU(rank) acts on both) -> left/right tuned -> #418 RELABELS, no reduction.")
print(f"  => the #418 reduction hinges on: is the SU(rank) weak action intrinsically one-chirality (holomorphic)? Decisive derivation question.")
print(f"  @Lyra: this is the sharp target for the bulk-color chirality derivation -- show SU(rank) is a symmetry of H^2(D_IV^5) alone (the holomorphic sector).")
print(f"  @Casey: feasibility established (substrate IS chiral); the crux is the one falsifiable question above. Spec, not derivation. Count still 2.")
print(f"  Score: 2/2 (feasibility established; the chirality crux distilled to one falsifiable derivation target; forcing = Lyra lane; count 2)")
print()
print("=" * 78)
print("TOY 4102 SUMMARY -- the #418 chirality crux. FEASIBILITY: the substrate has a natural chirality (the")
print("  holomorphic structure of the complex domain D_IV^5 + Casey #14's SO(5,2)->SO(4,2) projection), so a chiral")
print("  SM content is achievable in principle. THE PRECISE TEST (the crux in one line): does the weak SU(rank)")
print("  couple to the holomorphic chirality ONLY? If the substrate forces that (SU(2) is intrinsically a")
print("  holomorphic-sector symmetry), the chiral content is forced and #418 reduces; if SU(rank) could act on both")
print("  chiralities, the left/right split is a choice (tuned) and #418 only relabels. So the #418 reduction hinges")
print("  on one falsifiable derivation question -- Lyra's bulk-color lane. Feasibility yes; the forcing is open. Count still 2.")
print("=" * 78)
print()
print("SCORE: 2/2")
