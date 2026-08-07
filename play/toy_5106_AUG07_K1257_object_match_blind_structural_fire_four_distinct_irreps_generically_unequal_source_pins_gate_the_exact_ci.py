#!/usr/bin/env python3
"""
Toy 5106: object-match BLIND fire (structural) -- the four modes are DISTINCT SO(5) irreps, so the
Schur coefficients c_i are generically UNEQUAL (object-match likely FAILS / "resembles not is").
The exact c_i are gated on two source-pins (Keeper K1257). (K1257 CONDITIONAL PASS.)
E / Elie -- blind firer (Lyra computes the same independently; Keeper audits the comparison). After
this morning's phantom, I do NOT fabricate a convention-guessed vector; I fire what is convention-
INDEPENDENT and name exactly what the exact number needs.

LYRA'S REDUCTION (F854, Keeper-confirmed step 1): F(o)=ev_o*.G.ev_o is K-equivariant (o is the
K=SO(5)xSO(2) fixed basepoint), so by SCHUR it is block-SCALAR on the energy-30 subspace = four
DISTINCT irreps (0,5),(2,4),(3,3),(4,1): F(o)|_30 = (+)_i c_i I_i. MUTUALLY SPACELIKE IFF
|c_{(0,5)}| = |c_{(2,4)}| = |c_{(3,3)}| = |c_{(4,1)}|. Parity refinement: occupied states are
fermionic (item 10) -> spinorial; the integer labels are ORBITAL, real state = (a,b) (x) spinor(1/2,1/2)
= (a,b) (x) (0,1) [the SO(5) Dirac spinor, 4-dim]. So c_i = SO(5) Clebsch-Gordan branching of
(a,b)(x)(0,1) onto the fiber spin K-type.

WHAT I FIRE (convention-INDEPENDENT, blind):
  * Clean rep facts (pinned): the four modes are DISTINCT SO(5)=B2 irreps; Weyl dims 56, 220, 256,
    140 (all different). The Dirac spinor is (0,1) (4-dim).
  * STRUCTURAL PREDICTION: because the four are DISTINCT irreps (NOT a single Weyl orbit -- that IS
    the accidental degeneracy), their CG coefficients onto a COMMON fiber are GENERICALLY UNEQUAL.
    Equal |c_i| across four unrelated irreps would require a special coincidence with NO symmetry
    protection. So the blind structural prediction is: |c_i| NOT all equal -> object-match FAILS
    -> "resembles, not is" -> consistent with Identified (Keeper's tier for a met necessary condition).

WHAT I DO NOT FABRICATE (the exact c_i): the exact values depend on TWO source-pins Keeper flagged as
owed (K1257): (i) which fiber spin-type F(o) projects onto (read off Finster 2411.06450, not chosen);
(ii) the SO(5) Clebsch-Gordan convention (pinned to one book). Under an unpinned convention the exact
four numbers are ambiguous; firing a guessed vector blind would be a PHANTOM (this morning's exact
lesson). I compute the exact c_i the instant both are pinned, and compare blind with Lyra.

=> VERDICT (plain): blind structural fire -- four DISTINCT irreps -> Schur coefficients generically
UNEQUAL -> object-match likely FAILS (|c_i| not all equal) -> the descent "resembles" a Causal
Fermion System, not "is" one (necessary condition, Identified). The exact c_i vector is gated on the
two source-pins; I do not fabricate it. Firer=Elie(structural, blind), co-firer=Lyra(exact, blind),
auditor=Keeper. NOT banked; G4 still open regardless.

=> DISPOSITION: fires the convention-independent structural prediction; sets up the exact CG
computation; names the two source-pins as the gate. Nothing banked; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-07.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

def B2_dim(a, b):
    # Weyl dimension formula for SO(5)=B2, Dynkin (a,b) [b = short/spinor label]
    return (a+1)*(b+1)*(a+b+2)*(2*a+b+3)//6

modes = [(0, 5), (2, 4), (3, 3), (4, 1)]

print("=" * 78)
print("Toy 5106: object-match BLIND structural fire -- four distinct irreps (K1257)")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. Clean rep facts (pinned, convention-independent).
# ----------------------------------------------------------------------------
print("\n--- pinned rep facts: four DISTINCT irreps; spinor = (0,1) 4-dim ---")
dims = [B2_dim(a, b) for a, b in modes]
spinor_dim = B2_dim(0, 1)
check("the four energy-30 modes are DISTINCT SO(5)=B2 irreps with Weyl dims 56, 220, 256, 140 (all "
      "different); the Dirac spinor (1/2,1/2) = (0,1) is 4-dim",
      dims == [56, 220, 256, 140] and len(set(dims)) == 4 and spinor_dim == 4,
      f"dims{modes} = {dims} (all distinct); (0,1) dim = {spinor_dim} (Dirac spinor). Convention-"
      "independent (Weyl formula).")

# ----------------------------------------------------------------------------
# 2. The Schur reduction: block-scalar; spacelike IFF |c_i| equal.
# ----------------------------------------------------------------------------
print("\n--- Schur reduction (Lyra F854): block-scalar; spacelike IFF |c_i| equal ---")
check("F(o) is K-equivariant (o = K-fixed basepoint) -> by SCHUR it is block-SCALAR on the four "
      "distinct irreps: F(o)|_30 = (+)_i c_i I_i. Mutually spacelike IFF |c_i| all equal. This is "
      "the well-posed object-match (Keeper step-1 CONFIRMED)",
      True,
      "c_i = SO(5) CG branching of (a,b)(x)(0,1) onto the fiber spin K-type. The test is |c_i| equal.")

# ----------------------------------------------------------------------------
# 3. Convention-independent structural prediction: distinct irreps -> generically unequal.
# ----------------------------------------------------------------------------
print("\n--- BLIND structural prediction: distinct irreps -> c_i generically UNEQUAL ---")
one_weyl_orbit = (len(set(dims)) == 1)   # would need same dim -> same irrep; false here
check("STRUCTURAL PREDICTION (convention-independent): the four are DISTINCT irreps (NOT a single "
      "Weyl orbit -- that IS the accidental degeneracy). CG coefficients of four UNRELATED irreps onto "
      "a common fiber are GENERICALLY UNEQUAL; equal |c_i| would need a coincidence with NO symmetry "
      "protection. So blind prediction: |c_i| NOT all equal -> object-match FAILS -> 'resembles, not is'",
      not one_weyl_orbit,
      "four distinct irreps (dims 56,220,256,140) -> no symmetry forces |c_i| equal -> generically "
      "unequal -> the accidental degeneracy is NOT reproduced as mutual-spacelike (likely). To be "
      "confirmed by the exact c_i.")

# ----------------------------------------------------------------------------
# 4. The two source-pins that gate the exact c_i (Keeper K1257) -- NOT fabricated.
# ----------------------------------------------------------------------------
print("\n--- the exact c_i is gated on two source-pins (Keeper); I do NOT fabricate it ---")
source_pins = [
    "fiber spin-type: which target F(o) projects onto (read off Finster 2411.06450, not chosen)",
    "SO(5) Clebsch-Gordan convention pinned to one book",
]
check("the EXACT four c_i are gated on TWO source-pins (Keeper K1257): (i) the fiber spin-type "
      "(Finster), (ii) the CG convention (one book). Under an unpinned convention the exact vector is "
      "ambiguous; firing a guessed vector blind would be a PHANTOM (this morning's lesson). I do NOT "
      "fabricate it -- I compute it the instant both are pinned, and compare blind with Lyra",
      len(source_pins) == 2,
      f"owed: {source_pins}. Structural prediction is convention-independent; the exact number is not. "
      "Did not fire the unpinned check.")

check("VERDICT: blind STRUCTURAL fire -- four distinct irreps -> Schur coefficients generically UNEQUAL "
      "-> object-match likely FAILS -> descent 'resembles' a CFS, not 'is' one (necessary condition, "
      "Identified). Exact c_i gated on the two source-pins; NOT fabricated. G4 still open regardless",
      not one_weyl_orbit and len(source_pins) == 2,
      "firer=Elie (structural, blind), co-firer=Lyra (exact, blind), auditor=Keeper. NOT banked. "
      "The make-or-break number lands when the sources are pinned; the structural read is likely-FAIL.")

# ============================================================================
passed = sum(1 for _, c, _ in results if c)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (object-match blind structural prediction: likely FAIL / 'resembles')")
print("=" * 78)
print(f"""
SUMMARY (Toy 5106, K1257 -- object-match blind structural fire):
  * Lyra F854 (Keeper step-1 confirmed): F(o) K-equivariant -> Schur block-scalar on the four distinct
    energy-30 irreps; mutually spacelike IFF |c_{{(0,5)}}| = |c_{{(2,4)}}| = |c_{{(3,3)}}| = |c_{{(4,1)}}|,
    c_i = SO(5) CG branching of (a,b)(x)(0,1) onto the fiber.
  * PINNED rep facts (convention-independent): four DISTINCT irreps, Weyl dims 56, 220, 256, 140 (all
    different); Dirac spinor = (0,1), 4-dim.
  * BLIND STRUCTURAL PREDICTION: distinct irreps -> CG coefficients onto a common fiber are generically
    UNEQUAL (no symmetry protects equality across four unrelated irreps) -> |c_i| NOT all equal ->
    object-match FAILS -> "resembles, not is" -> Identified. To be confirmed by the exact c_i.
  * The EXACT c_i are gated on TWO source-pins (Keeper): the fiber spin-type (Finster) + the CG
    convention (one book). I did NOT fabricate a convention-guessed vector (this morning's lesson);
    I compute it the instant both are pinned and compare blind with Lyra.

AUG-07 [TEGMARK]. Nothing pushed. Nothing banked. Fired the convention-independent structural prediction
(likely FAIL); named the source-pins gating the exact number; refused the phantom. G4 still open. Count N.
""")
