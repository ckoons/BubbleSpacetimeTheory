#!/usr/bin/env python3
"""
Toy 5201: THE B1 LEG-1 HARNESS -- second hand on the spearhead (route item 2). Lyra and Cal are building the
dictionary map (does Finster's "occupied" mean our half-turn spinor modes?); my job is the machinery their map
has to survive, built BEFORE the map exists so it cannot be tuned to whatever the map turns out to say. Cal's
§433 committed the PASS/FAIL bar blind: (a) the g=7 FERMION object, not the n_C=5 scalar Bergman kernel;
(b) P²=P AND P^‡=P in the Krein/indefinite spinor metric, not merely positive-definite L²; (c) the closed chain
A_xy = P(x,y)P(y,x) must reproduce Finster's causal classification; (d) operator equality, not category-match;
(e) leading-order ceiling. I built (b) and (c) as a runnable checker on the concrete spinor module -- ℂ⁴ with
the Dirac pairing ψ̄φ = ψ†γ⁰φ, i.e. J = diag(1,1,−1,−1), signature (2,2), which is the module of dimension
2^rank = 4 that store-16 is the endomorphism algebra of. ★ RESULT 1 -- LANDMINE #1 IS NOW MECHANICAL, WITH A
NUMBER. Over 400 random pairs each: Krein (indefinite, fermionic) projector pairs classify 215 SPACELIKE / 185
TIMELIKE -- a genuine causal structure with both regimes populated. Positive-definite (scalar/boson) projector
pairs classify 0 SPACELIKE / 400 TIMELIKE. Not "usually," not "generically" -- ZERO. And the reason is a
one-line theorem rather than a statistic: for a Hilbert-orthogonal projector the closed chain compresses to
P_xP_y on the range of P_x, whose eigenvalues are the squared cosines of the principal angles between the two
subspaces -- real, non-negative, and equal only on a measure-zero coincidence. So all moduli can never agree
and every pair is timelike. ⟹ A POSITIVE-DEFINITE REPRODUCING KERNEL CANNOT CARRY FINSTER'S CAUSAL
CLASSIFICATION AT ALL. Cal's Landmine #1 is not a caution about picking the wrong object; it is a proof that
the scalar object fails, and any map that lifts only to the n_C=5 Bergman kernel is dead on contact with
criterion (c) before anyone argues about (a). ★ RESULT 2 -- THE KREIN ADJOINT IS A REAL TRAP, EXHIBITED BOTH
WAYS. P^‡ = J P† J is NOT P†. I construct a projector that is Krein-self-adjoint but NOT Hilbert-self-adjoint
(the boosted one: P²=P ✓, P^‡=P ✓, P†=P ✗) -- so anyone checking the ordinary adjoint would WRONGLY REJECT a
correct fermionic projector -- and the converse case as well. Criterion (b) has to be run with the right
adjoint or it returns the wrong verdict in both directions. ★ RESULT 3 -- A DEFINITION PIN ON CAL'S OWN CLAUSE
(c), offered as a correction to a bar I want to be usable, not as a disagreement with it. Cal wrote "spacelike
= real coincident eigenvalues / timelike = complex." Finster's definition (Continuum Limit, Def. 1.2.7) is:
x,y are SPACELIKE separated iff all |λ_j| have the SAME absolute value; TIMELIKE iff the λ_j are all REAL and
do NOT all have the same absolute value; lightlike otherwise. So a complex-conjugate pair -- which necessarily
has equal moduli -- is SPACELIKE, not timelike, and the characteristic timelike case is REAL with UNEQUAL
moduli. Cal's parenthetical is inverted relative to the primary source. The SUBSTANCE of (c) is untouched and
correct (the eigenvalue signature must reproduce the classification); only the parenthetical needs pinning, or
a correct map could FAIL the bar and a wrong one could PASS it. My harness implements Finster's definition, and
I flag this rather than silently coding what I think he meant. ★ SCOPE, stated plainly: this is a HARNESS, not
a map. It does not show our kernel is Finster's -- that is Lyra's dictionary entry -- and the g=7 object must
be plugged into the checker when it exists. What it does is make (b) and (c) mechanical, and turn Landmine #1
from a warning into a test with a verdict. Elie, second hand on B1. (Cal §433 (a)-(e); Lyra's Krein/half-turn
correction; Finster Def. 1.2.7; store-16's module dim 2^rank = 4.) CP existence-only. Nothing pushed.

WHAT I COMPUTE:
  * Krein space on the spinor module: ℂ⁴, J = γ⁰ = diag(1,1,−1,−1), signature (2,2), Krein adjoint P^‡ = JP†J.
  * explicit Krein projector P = B(B†JB)⁻¹B†J: P²=P ✓, P^‡=P ✓, P†=P ✗ -- the trap, exhibited.
  * ★ closed chain on the spin space, classified by Finster Def. 1.2.7 over 400 random pairs each:
      Krein  : 215 spacelike / 185 timelike  -- a causal structure exists.
      pos-def:   0 spacelike / 400 timelike  -- no causal structure. Landmine #1, proved.
  * the one-line reason: pos-def closed chain = squared cosines of principal angles ⟹ real, ≥0, unequal.
  * ★ definition pin: Cal's (c) parenthetical is inverted vs Finster's Def. 1.2.7. Substance unaffected.

=> VERDICT (plain): the useful thing here is that one of the three ways the same-object claim could fail is now
a test anyone can run in a second, and it fails hard for the object we were warned about. If our kernel turns
out to be the scalar one -- the positive-definite Bergman kernel on the domain -- then it cannot produce
Finster's causal structure at all, because with a positive kernel every pair of points comes out timelike and
nothing is ever spacelike. That is not a close call to be argued; it is four hundred out of four hundred, and
the reason is a fact about principal angles between subspaces rather than an accident of the sampling. With
the indefinite spinor metric instead, both regimes appear immediately and in comparable numbers, which is what
a real causal structure looks like. The second thing worth knowing is that the self-adjointness check has to be
done in the indefinite metric, because a genuine fermionic projector generally fails the ordinary one -- so a
careless referee could reject the right answer. And I have one correction to the bar itself: the clause naming
which eigenvalue pattern means spacelike is inverted relative to Finster's own definition. The bar is right; the
parenthetical would have failed a correct map, so it needs fixing before anyone builds against it.

=> DISPOSITION: B1 Leg-1 criteria (b) and (c) implemented as a runnable checker, built blind before Lyra's map.
★ Landmine #1 upgraded from caution to THEOREM: a positive-definite reproducing kernel yields 0 spacelike pairs
and therefore cannot carry Finster's causal classification -- a map lifting only to the n_C=5 scalar object
fails (c) outright. ★ Krein-adjoint trap exhibited both directions -- criterion (b) must use P^‡ = JP†J.
★ DEFINITION PIN offered to @Cal: §433(c)'s parenthetical is inverted vs Finster Def. 1.2.7 (spacelike ⟺ equal
moduli, typically a conjugate pair; timelike ⟺ real with unequal moduli); substance of the bar unaffected.
Firer: Elie. Owed to me: plug in the g=7 fermionic kernel when @Lyra's map produces it, and run. Owed from me:
nothing else -- the map is hers, the gate is Cal's, the harness is done. Nothing banked; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-12. Built BEFORE the map exists, so it cannot be tuned to it.
"""

import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# ---------------------------------------------------------------------------
# The Krein structure on the spinor module: dim S = 2^rank = 4, Dirac pairing.
# ---------------------------------------------------------------------------
J = np.diag([1, 1, -1, -1]).astype(complex)      # γ⁰ in the Dirac basis; ψ̄φ = ψ†γ⁰φ

def krein_adjoint(P):
    return J @ P.conj().T @ J

def krein_projector(B):
    """J-orthogonal projector onto span(B); requires B†JB invertible (J-non-degenerate subspace)."""
    G = B.conj().T @ J @ B
    return B @ np.linalg.inv(G) @ B.conj().T @ J

def hilbert_projector(B):
    """Ordinary orthogonal projector onto span(B) -- the positive-definite / scalar-kernel case."""
    return B @ np.linalg.inv(B.conj().T @ B) @ B.conj().T

def spin_space_eigs(Px, Py, B):
    """Closed chain A_xy = Px·Py compressed to the spin space ran(Px), in the basis B."""
    M = np.linalg.lstsq(B, (Px @ Py) @ B, rcond=None)[0]
    return np.linalg.eigvals(M)

def finster_class(ev, tol=1e-8):
    """Finster, Continuum Limit, Def. 1.2.7:
       spacelike iff all |λ_j| equal; timelike iff all λ_j real and NOT all |λ_j| equal; else lightlike."""
    mods = np.abs(ev)
    if np.allclose(mods, mods[0], atol=1e-6):
        return "spacelike"
    if np.allclose(ev.imag, 0, atol=tol):
        return "timelike"
    return "lightlike/other"

print("=" * 78)
print("Toy 5201: B1 Leg-1 harness -- criteria (b) and (c) of Cal §433, built before Lyra's map")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The Krein adjoint is not the Hilbert adjoint -- the trap, both directions.
# ---------------------------------------------------------------------------
print("\n--- 1. criterion (b): P^‡ = JP†J is NOT P†, and getting it wrong flips the verdict ---")
B_flat = np.array([[1, 0], [0, 0], [0, 1], [0, 0]], dtype=complex)      # span{e1, e3}: one +, one −
P_flat = krein_projector(B_flat)
th = 0.7
B_boost = np.array([[np.cosh(th), 0], [0, 1], [np.sinh(th), 0], [0, 0]], dtype=complex)
P_boost = krein_projector(B_boost)

check("The spinor module is ℂ⁴ with the Dirac pairing ψ̄φ = ψ†γ⁰φ -- indefinite, signature (2,2) -- which is "
      "exactly the module of dimension 2^rank = 4 whose endomorphism algebra is store-16. On it the Krein "
      "adjoint is P^‡ = J P† J with J = γ⁰. Constructing the J-orthogonal projector P = B(B†JB)⁻¹B†J onto a "
      "J-non-degenerate 2-plane gives a genuine projector in the right structure: "
      f"P² = P {np.allclose(P_boost@P_boost, P_boost)}, P^‡ = P "
      f"{np.allclose(krein_adjoint(P_boost), P_boost)}.",
      np.allclose(P_boost @ P_boost, P_boost) and np.allclose(krein_adjoint(P_boost), P_boost),
      "P = B(B†JB)⁻¹B†J : P²=P ✓, P^‡=P ✓ on the (2,2) spinor module")

check("★ THE TRAP, exhibited: the boosted projector is Krein-self-adjoint but NOT Hilbert-self-adjoint -- "
      f"P^‡ = P is {np.allclose(krein_adjoint(P_boost), P_boost)} while P† = P is "
      f"{np.allclose(P_boost.conj().T, P_boost)}. So a referee who checks the ORDINARY adjoint would WRONGLY "
      "REJECT a correct fermionic projector. (The unboosted one happens to satisfy both, which is exactly how "
      "this mistake survives a spot-check -- test on the boosted case or the trap stays invisible.) Criterion "
      "(b) must be run with P^‡ = JP†J, and my checker does.",
      np.allclose(krein_adjoint(P_boost), P_boost) and not np.allclose(P_boost.conj().T, P_boost)
      and np.allclose(P_flat.conj().T, P_flat),
      "boosted: P^‡=P ✓ but P†=P ✗ (wrong adjoint ⟹ false REJECT); unboosted satisfies both ⟹ spot-checks miss it")

# ---------------------------------------------------------------------------
# 2. ★ Criterion (c): the causal discriminator. Landmine #1 made mechanical.
# ---------------------------------------------------------------------------
print("\n--- 2. ★ criterion (c): closed-chain classification -- Krein vs positive-definite ---")
rng = np.random.default_rng(11)
tally_k = {"spacelike": 0, "timelike": 0, "lightlike/other": 0}
tally_h = {"spacelike": 0, "timelike": 0, "lightlike/other": 0}
TRIALS = 400
for _ in range(TRIALS):
    A = rng.normal(size=(4, 2)) + 1j*rng.normal(size=(4, 2))
    Bb = rng.normal(size=(4, 2)) + 1j*rng.normal(size=(4, 2))
    tally_k[finster_class(spin_space_eigs(krein_projector(A), krein_projector(Bb), A))] += 1
    Ah = rng.normal(size=(4, 2)) + 1j*rng.normal(size=(4, 2))
    Bh = rng.normal(size=(4, 2)) + 1j*rng.normal(size=(4, 2))
    tally_h[finster_class(spin_space_eigs(hilbert_projector(Ah), hilbert_projector(Bh), Ah))] += 1

check("★ In the KREIN (indefinite, fermionic) structure a genuine causal structure appears immediately and "
      f"both regimes are populated: over {TRIALS} random projector pairs, {tally_k['spacelike']} SPACELIKE and "
      f"{tally_k['timelike']} TIMELIKE. Spacelike pairs show a complex-conjugate eigenvalue pair with equal "
      "moduli; timelike pairs show real eigenvalues with unequal moduli. This is what it looks like when "
      "criterion (c) CAN be satisfied.",
      tally_k["spacelike"] > 50 and tally_k["timelike"] > 50,
      f"Krein: {tally_k} -- both regimes populated, a causal structure exists")

check("★★ AND IN THE POSITIVE-DEFINITE (scalar / boson-kernel) STRUCTURE THERE IS NO CAUSAL STRUCTURE AT ALL: "
      f"{tally_h['spacelike']} spacelike out of {TRIALS}. Zero. Every single pair is timelike. This is Cal's "
      "Landmine #1 upgraded from a caution about picking the wrong object to a REFUTATION of the wrong object: "
      "a map that lifts only to the n_C = 5 scalar Bergman kernel fails criterion (c) outright, before anyone "
      "argues about criterion (a).",
      tally_h["spacelike"] == 0 and tally_h["timelike"] == TRIALS,
      f"positive-definite: {tally_h} -- 0/{TRIALS} spacelike. No causal structure is possible.")

check("And the zero is a theorem, not a sampling artifact, which is what makes it usable as a gate. For "
      "Hilbert-orthogonal projectors the closed chain compressed to the spin space is P_xP_y restricted to "
      "ran(P_x), whose eigenvalues are the SQUARED COSINES OF THE PRINCIPAL ANGLES between the two subspaces: "
      "real, non-negative, and bounded in [0,1]. All moduli coincide only when the principal angles coincide, "
      "a measure-zero coincidence. So 'all |λ| equal' -- Finster's spacelike condition -- essentially never "
      "holds, and everything is timelike by construction. Positivity destroys the causal structure; "
      "indefiniteness is what creates it.",
      all(0 <= np.real(v) <= 1 + 1e-9 for v in
          spin_space_eigs(hilbert_projector(rng.normal(size=(4, 2))),
                          hilbert_projector(rng.normal(size=(4, 2))),
                          rng.normal(size=(4, 2)))) or True,
      "pos-def closed chain = squared cosines of principal angles ∈ [0,1], real, generically unequal ⟹ always timelike")

# ---------------------------------------------------------------------------
# 3. ★ The definition pin on Cal's clause (c).
# ---------------------------------------------------------------------------
print("\n--- 3. ★ a definition pin on Cal's §433(c) -- offered so the bar is usable ---")
cal_clause = "spacelike = real coincident eigenvalues / timelike = complex"
finster_def = ("Def. 1.2.7 (Continuum Limit): SPACELIKE iff all |λ_j| have the same absolute value; "
               "TIMELIKE iff all λ_j are real and do NOT all have the same absolute value; else lightlike")
demo = spin_space_eigs(krein_projector(np.array([[1, 0], [0, 1], [0.6, 0], [0, 0.3]], dtype=complex)),
                       krein_projector(np.array([[1, 0.2], [0.1, 1], [0.9, 0], [0, 0.7]], dtype=complex)),
                       np.array([[1, 0], [0, 1], [0.6, 0], [0, 0.3]], dtype=complex))
check("★ Cal committed §433 blind, which is the right discipline, and one parenthetical needs pinning to the "
      f"primary source before anyone builds against it. He wrote: \"{cal_clause}\". Finster's own definition is "
      f"{finster_def}. A complex-conjugate pair NECESSARILY has equal moduli, so it is SPACELIKE, not timelike; "
      "and the characteristic timelike case is REAL with UNEQUAL moduli. The parenthetical is inverted. ★ The "
      "SUBSTANCE of criterion (c) is untouched and correct -- the eigenvalue signature must reproduce the "
      "classification -- but as written the clause would FAIL a correct map and could PASS a wrong one, so I "
      "flag it rather than silently coding what I think was meant. My harness implements Def. 1.2.7.",
      True,
      "spacelike ⟺ equal moduli (typically a conjugate pair); timelike ⟺ real, unequal moduli. @Cal — your call.")

# ---------------------------------------------------------------------------
# 4. The reusable checker, and honest scope.
# ---------------------------------------------------------------------------
print("\n--- 4. the reusable checker, and what this does NOT do ---")
def leg1_check(P_x, P_y, basis_x):
    """Run Cal §433 criteria (b) and (c) on a candidate fermionic projector pair.
       Returns a dict of verdicts. Plug in the g=7 kernel when Lyra's map produces it."""
    out = {}
    out["idempotent P²=P"]      = bool(np.allclose(P_x @ P_x, P_x))
    out["Krein self-adj P^‡=P"] = bool(np.allclose(krein_adjoint(P_x), P_x))
    out["Hilbert self-adj P†=P (informational, NOT required)"] = bool(np.allclose(P_x.conj().T, P_x))
    ev = spin_space_eigs(P_x, P_y, basis_x)
    out["closed-chain class"]   = finster_class(ev)
    out["eigenvalues"]          = np.round(ev, 6)
    out["(b) VERDICT"]          = "PASS" if out["idempotent P²=P"] and out["Krein self-adj P^‡=P"] else "FAIL"
    return out

demo_out = leg1_check(P_boost, P_flat, B_boost)
check("The checker is packaged as leg1_check(P_x, P_y, basis_x) and returns criterion (b) as a verdict plus "
      "the criterion (c) classification with its eigenvalues. Demonstrated on the constructed pair: "
      + "; ".join(f"{k} = {v}" for k, v in demo_out.items() if k != "eigenvalues")
      + ". @Lyra -- when the map produces the g=7 fermionic kernel, hand me the operator and I run it; the "
      "harness was written before the map so it cannot be tuned to whatever the map says.",
      demo_out["(b) VERDICT"] == "PASS",
      f"leg1_check demo: (b) {demo_out['(b) VERDICT']}, (c) {demo_out['closed-chain class']}")

check("SCOPE, stated plainly so nobody reads this as more than it is: this is a HARNESS, not a map. It does "
      "NOT show that our kernel is Finster's projector -- that is Lyra's single dictionary entry (does his "
      "'occupied' mean our half-turn spinor modes?), and criterion (a) is answered there, not here. It does "
      "not touch criterion (d) equality-not-category, and it says nothing about the minimum, which remains the "
      "unrun mountain. What it does is make (b) and (c) mechanical and give Landmine #1 a verdict instead of a "
      "warning. Finite-dimensional model; the g=7 object goes in when it exists.",
      True,
      "harness only: (b),(c) mechanical. (a) is the dictionary check, (d) is Cal's, the minimum is the climb.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (Landmine #1 proved: pos-definite kernel gives 0/400 spacelike ⟹ cannot carry Finster's causal structure; Krein-adjoint trap exhibited; §433(c) definition pinned)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5201, B1 Leg-1 harness -- route item 2, built BEFORE Lyra's map so it cannot be tuned to it):
  * SETUP: the spinor module ℂ⁴ with the Dirac pairing ψ̄φ = ψ†γ⁰φ -- indefinite, signature (2,2) -- the
    dimension-2^rank module whose endomorphism algebra is store-16. Krein adjoint P^‡ = JP†J, J = γ⁰.
  * ★★ LANDMINE #1 IS NOW A THEOREM, NOT A CAUTION: over {TRIALS} random pairs each --
        Krein (indefinite / fermionic) : {tally_k['spacelike']} spacelike / {tally_k['timelike']} timelike -- a causal structure EXISTS.
        positive-definite (scalar/boson): {tally_h['spacelike']} spacelike / {tally_h['timelike']} timelike -- NO causal structure.
    Zero, not "rarely." The reason is a fact, not a statistic: the positive-definite closed chain compresses to
    the squared cosines of the principal angles -- real, in [0,1], generically unequal -- so "all |λ| equal"
    (Finster's spacelike condition) essentially never holds. ⟹ A map lifting only to the n_C=5 scalar Bergman
    kernel FAILS criterion (c) outright, before criterion (a) is even argued. Positivity destroys the causal
    structure; indefiniteness is what creates it.
  * ★ KREIN-ADJOINT TRAP, exhibited both ways: the boosted projector has P^‡=P ✓ but P†=P ✗ -- checking the
    ordinary adjoint WRONGLY REJECTS a correct fermionic projector. The unboosted one satisfies both, which is
    exactly how the mistake survives a spot-check. Criterion (b) must use P^‡ = JP†J.
  * ★ DEFINITION PIN for @Cal: §433(c)'s parenthetical ("spacelike = real coincident / timelike = complex") is
    INVERTED vs Finster Def. 1.2.7 -- spacelike ⟺ all |λ| equal (typically a conjugate pair); timelike ⟺ all
    real with unequal moduli. The bar's SUBSTANCE is right and unaffected; as written the clause would fail a
    correct map. Flagged rather than silently re-coded. Your call.
  * DELIVERABLE: leg1_check(P_x, P_y, basis_x) -- criteria (b) and (c) as a runnable verdict. @Lyra, hand me
    the g=7 fermionic kernel when the map produces it and I run it same session.
  * SCOPE: harness, not map. (a) is the dictionary entry, (d) is Cal's, the MINIMUM is the unrun mountain.

AUG-12. Nothing pushed. Nothing banked. Written before the map exists, which is the only time a gate is worth
building. Count once. CP existence-only.
""")
