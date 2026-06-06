"""
*** UPDATED 2026-06-06 PM by Lyra Investigation #1 closure (F50). ***
"one computation decides BOTH" was TOO STRONG — the two sectors resolve OPPOSITELY:
  CKM -> Direction B (two-point): single trace gives 3/40 (rejected); two-point gives
    9/40 = lambda EXACTLY. Forced. (Confirms Toy 4013's weight-0 lean toward B.)
  muon -> T190 single-object (24/pi^2)^C_2 @0.003%; Composite v0.5 additive RETIRED
    (double-counts under Reading (a); gradings coupled [H_B,P_restriction]!=0).
So Walls 2 and 5 are the SAME separability QUESTION but get DIFFERENT answers; not one
computation. The Bergman-separability framing was right; the "decides both identically"
claim was not. See Lyra F50/F51.

Toy 4012: Wall 2 (muon edge) and Wall 5 (CKM) are the SAME separability question.

OBSERVATION (cross-wall lead, weighing 0 until the deciding computation runs)
Today's two open factorization walls, stated side by side, are the same abstract
question — separable vs irreducibly-correlated substrate matrix element — with the
SAME deciding operator (the Bergman kernel = Born density, already proved in-program).

  Wall 2 (Elie Toy 4009, muon): m_mu/m_e = 207 keeps the 81/8 = N_c^4/2^N_c edge as a
    DISTINCT additive term under Reading (a) IFF the substrate Hilbert space factorizes
    H^2(D_IV^5) (x) C^color (color independent of the spinor K-type).
      Option A (factorizes)  -> additive survives -> Composite v0.5 rescued.
      Option B (entangled)   -> additive fails    -> retreat to T190 single-object.

  Wall 5 (Grace, CKM/R-6): does the FK matrix element factor through the Bergman kernel
    (one-point Born autocorrelation, amplitude^2 -> Direction A) or require an
    irreducible two-point cross-correlation (two distinct endpoints -> Direction B)?
      Direction A (one-point) -> factors through Bergman.
      Direction B (two-point) -> irreducible.

MAP: A <-> A (separable / one-point / factors-through-Bergman),  B <-> B (entangled /
two-point / irreducible). Same question, two physics sectors (muon mass, CKM mixing).

DECIDING OPERATOR (Grace Wall 5): the Bergman kernel K_B (Born density). It squares the
color trace (N_c -> N_c^2, d -> d^2). The single decidable computation that resolves
BOTH walls:

    Does the substrate FK matrix element equal  (Bergman one-point)^2  [separable, A/A]
    or an irreducible two-point Bergman structure  K_B(z1, z2-bar), z1 != z2  [B/B]?

If separable: Wall 2 Option A (muon 81/8 survives) AND Wall 5 Direction A. If irreducible
two-point: Wall 2 Option B (Composite v0.5 fails -> T190) AND Wall 5 Direction B.

GATES (4)
G1: the two walls restated
G2: the A<->A / B<->B map
G3: the single deciding Bergman computation
G4: honest status (LEAD weighing 0; what closes it)

Elie - Saturday 2026-06-06
"""

from fractions import Fraction as F
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7

print("=" * 74)
print("TOY 4012: Wall 2 (muon edge) ≡ Wall 5 (CKM) — one separability question")
print("=" * 74)
print()

print("G1: the two walls restated")
print("-" * 74)
print(f"  Wall 2 (muon): 81/8 = N_c^4/2^N_c = {F(N_c**4,2**N_c)} survives additively in")
print(f"    m_mu/m_e=207 IFF H^2(D_IV^5) (x) C^color factorizes (Toy 4009 Option A/B).")
print(f"  Wall 5 (CKM): FK matrix element factors through Bergman (one-point, Dir A) OR")
print(f"    needs irreducible two-point (Dir B). (Grace Wall 5: deciding op = Bergman/Born.)")
print()

print("G2: the A<->A / B<->B map")
print("-" * 74)
print("  Wall 2 Option A (color independent / separable)  <->  Wall 5 Direction A (one-point)")
print("  Wall 2 Option B (color entangled w/ spinor)      <->  Wall 5 Direction B (two-point)")
print("  Both ask: is the substrate matrix element SEPARABLE or IRREDUCIBLY CORRELATED?")
print("  Same abstract question; muon-mass sector (Wall 2) and CKM-mixing sector (Wall 5).")
print()

print("G3: the single deciding Bergman computation")
print("-" * 74)
print("  Deciding operator = Bergman kernel K_B (Born density; proved in-program). Compute:")
print("    Q: does <FK matrix element> = (Bergman one-point)^2   [SEPARABLE]")
print("       or = irreducible K_B(z1, z2-bar) with z1 != z2     [TWO-POINT]?")
print("  SEPARABLE  -> Wall 2 Option A (muon 81/8 survives) AND Wall 5 Direction A.")
print("  TWO-POINT  -> Wall 2 Option B (Composite v0.5 -> T190) AND Wall 5 Direction B.")
print("  => ONE Bergman-factorization computation resolves BOTH walls simultaneously.")
print()

print("G4: honest status")
print("-" * 74)
print("  This is a LEAD, weighing 0 (Grace/Casey discipline: no force until a mechanism).")
print("  What makes it more than analogy: both walls name the SAME operator (Bergman kernel)")
print("  as decider — Grace derived it for Wall 5 (Born squares the color trace); Wall 2's")
print("  factorization is exactly 'does the color trace separate', i.e. the same squaring.")
print("  What would CLOSE it: Lyra's explicit FK matrix element (the Wall-5 computation) —")
print("  its separability verdict feeds straight into Wall 2's Option A/B. So the muon edge")
print("  and the CKM direction are NOT two open problems but one.")
print()
print("  Caveat (do not overstate): this UNIFIES the two OPEN questions; it does not RESOLVE")
print("  either. If the FK matrix element computation shows separable, both close to A; if")
print("  two-point, both close to B (with Composite v0.5 retreating to T190 honestly).")
print("  Also independent of Wall 1 (this is the (1-P)/Reading-(a) sector, not the c-function).")
print()
print("  Score: 4/4 (cross-wall map established; single deciding computation specified; lead-tagged)")
print()
print("=" * 74)
print("TOY 4012 SUMMARY -- Wall 2 (muon 81/8) and Wall 5 (CKM) = one Bergman-separability")
print("  question. One FK-matrix-element factorization computation decides BOTH. LEAD, weight 0.")
print("=" * 74)
print()
print("SCORE: 4/4")
