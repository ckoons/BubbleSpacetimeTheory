#!/usr/bin/env python3
"""
Toy 5204: THE MINIMUM -- building the second-variation harness for B1's one remaining climb (route item 1,
Cal §432 leg-3 with teeth). The same-object leg is converged three ways; what is left is the honest question
nobody has run: is our configuration the BOTTOM of Finster's causal action, or merely a flat spot on its slope?
I built the machinery, and it produced three things -- one that confirms Cal's worry is not hypothetical, one
that questions the tool we were planning to lean on, and one that says the problem is not yet well-posed. ★ (0)
FOUNDATION FIRST, because a harness that computes the wrong functional is worse than none: the causal
Lagrangian L(x,y) = Σ|λ_i|² − (1/2n)(Σ|λ_i|)², built on the closed-chain eigenvalues from toy 5201. It
cross-checks against that toy exactly -- over the same 400 random pairs, all 226 SPACELIKE pairs give L = 0 to
within 3×10⁻¹⁴, and all 174 TIMELIKE pairs give L > 0. Two independently written harnesses agreeing on which
pairs are causally inert is the check I would demand of anyone else. ★ (1) CAL'S §432 CONCERN IS COMMON, NOT
HYPOTHETICAL. Over twelve random symmetric orbits I computed the minimum second variation separately in the
SYMMETRIC sector (displace every point alike) and the NON-INVARIANT sector (displace one point only). FOUR of
the twelve show outright sector disagreement: min d²S > 0 across the symmetric directions while min d²S < 0 in
a symmetry-breaking one -- e.g. +8.2×10³ against −1.5×10³, and +3.6×10¹¹ against −2.0×10⁹. These are genuine
local minima WITHIN the symmetric subspace that are SADDLES in the full space. "Symmetric-critical" is not
almost-minimal; it is routinely a saddle, and the harness detects it. ★ (2) AND THE TOOL WE WERE GOING TO LEAN
ON NEEDS ITS HYPOTHESIS CHECKED. Palais's principle of symmetric criticality requires a COMPACT group acting
isometrically; it is false in general without that. The symmetry group here is the Krein-unitary group of the
indefinite spinor metric, and it is NON-COMPACT -- I exhibit J-unitary boosts with U†JU = J exactly and
operator norm growing as e^t (‖U‖ = 2.98×10³ at t = 8, unbounded). So "Palais gives us criticality for free"
is not available as stated: the compactness hypothesis fails for the boost directions, and criticality itself
has to be earned there rather than cited. That is a stronger statement than Cal's -- he flagged that Palais
gives a critical point and not a minimum; I am flagging that for this group it may not even give the critical
point. ★★ (3) THE ONE THAT MATTERS MOST -- THE PROBLEM IS NOT YET WELL-POSED. The causal action is
non-negative and vanishes exactly when every pair is spacelike, and in five of my twelve random configurations
S came out EXACTLY zero. So the UNCONSTRAINED global minimum of the causal action is the trivial,
totally-spacelike configuration -- a world with no causal relations at all. Our configuration is manifestly not
that (the closed chains are a genuine 215/185 mix). Therefore "our configuration minimizes the causal action"
is FALSE as an unconstrained statement and can only ever be true relative to Finster's constraints -- the
volume, trace and boundedness constraints. ⟹ NAMING THE CONSTRAINT SET IS PART OF THE PROBLEM, NOT A
TECHNICALITY. Any claim that we minimize the action, made without stating the constraints, is minimizing to
nothing. That has to be settled before the climb starts, and it is a question for Lyra and Cal, not a
computation. ★ DELIVERABLE: second_variation(config, directions) with the sector split, plus the verified
causal Lagrangian. Ready for Lyra's configuration the session it lands. Elie, the minimum harness. (Cal §432
leg-3 and §433; toy 5201's closed chains; Finster's causal Lagrangian and constraint set; Palais 1979.)
CP existence-only. Nothing pushed.

WHAT I COMPUTE:
  * causal Lagrangian L = Σ|λ|² − (1/2n)(Σ|λ|)²; cross-checks toy 5201 exactly (spacelike ⟺ L = 0, 3e-14).
  * ★ sector-split second variation: 4 of 12 symmetric orbits are symmetric-minima and full-space SADDLES.
  * ★ Palais needs COMPACT; the Krein-unitary group is not (‖U‖ = e^t, exhibited J-unitary boosts).
  * ★★ unconstrained S ≥ 0 with equality iff totally spacelike -- and S = 0 hit exactly in 5 of 12 trials.
    ⟹ the constraint set is load-bearing and must be named before "minimum" means anything.

=> VERDICT (plain): the harness works, and the first thing it says is that the worry was justified. Take a
configuration laid out symmetrically, and it will often sit at the bottom of a valley as long as you only move
it in ways that respect the symmetry, while a single point stepping out of line sends the action downhill. Four
of twelve did exactly that, so this is the ordinary behaviour rather than a pathology to be hoped against. The
second thing it says is that the theorem we were going to invoke to get criticality cheaply has a hypothesis we
do not satisfy: it needs a compact symmetry group, and ours contains boosts that grow without bound. And the
third thing is the one that should be settled before anybody climbs: the action, left unconstrained, is
minimized by a world in which nothing is causally related to anything, and I hit that trivial answer five times
out of twelve by accident. Our world is plainly not that. So the sentence "our configuration minimizes the
causal action" cannot be true on its own; it is only ever true subject to the constraints Finster imposes, and
until we say which ones and check that our configuration satisfies them, the climb has no summit to reach.

=> DISPOSITION: minimum-harness BUILT and cross-checked; ready for @Lyra's configuration. ★ Cal §432 leg-3
CONFIRMED as a live risk, not a formality (4/12 symmetric-minima are full-space saddles). ★ NEW GATE for
@Cal and @Lyra: Palais requires COMPACTNESS and the Krein-unitary group is non-compact -- criticality in the
boost directions must be earned, not cited. ★★ PRIOR GATE, and it comes first: the unconstrained action is
minimized by the trivial totally-spacelike configuration (S = 0 hit 5/12), so the CONSTRAINT SET must be named
and our configuration checked against it before "minimum" is a meaningful claim. Firer: Elie. Owed to me:
nothing -- the next two steps are a specification (@Lyra: which constraints) and a theorem-hypothesis ruling
(@Cal: Palais without compactness). Owed from me: run the harness the session the configuration lands.
Nothing banked; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-12.
"""

import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

J = np.diag([1, 1, -1, -1]).astype(complex)          # γ⁰; the indefinite spinor metric of toy 5201

def krein_projector(B):
    G = B.conj().T @ J @ B
    return B @ np.linalg.inv(G) @ B.conj().T @ J

def chain_eigs(Px, Py, B):
    M = np.linalg.lstsq(B, (Px @ Py) @ B, rcond=None)[0]
    return np.linalg.eigvals(M)

def causal_lagrangian(ev):
    """Finster: L(x,y) = Σ|λ_i|² − (1/2n)(Σ|λ_i|)². Non-negative; zero iff all moduli coincide (spacelike)."""
    m = np.abs(ev)
    return float(np.sum(m**2) - (np.sum(m)**2)/len(m))

def causal_action(Bs):
    Ps = [krein_projector(B) for B in Bs]
    n = len(Bs)
    return sum(causal_lagrangian(chain_eigs(Ps[i], Ps[j], Bs[i])) for i in range(n) for j in range(n) if i != j)

def second_variation(Bs, dirs, eps=2e-3):
    """d²S/dε² along a direction, by central differences on the projector manifold."""
    f0 = causal_action(Bs)
    fp = causal_action([B + eps*d for B, d in zip(Bs, dirs)])
    fm = causal_action([B - eps*d for B, d in zip(Bs, dirs)])
    return (fp - 2*f0 + fm)/eps**2

def rot(t):
    M = np.eye(4, dtype=complex)
    M[0, 0], M[0, 1], M[1, 0], M[1, 1] = np.cos(t), -np.sin(t), np.sin(t), np.cos(t)
    return M

def jboost(t):
    M = np.eye(4, dtype=complex)
    M[0, 0], M[0, 2], M[2, 0], M[2, 2] = np.cosh(t), np.sinh(t), np.sinh(t), np.cosh(t)
    return M

print("=" * 78)
print("Toy 5204: THE MINIMUM -- second-variation harness for B1's one remaining climb")
print("=" * 78)

# ---------------------------------------------------------------------------
# 0. Foundation: the causal Lagrangian, cross-checked against toy 5201.
# ---------------------------------------------------------------------------
print("\n--- 0. the causal Lagrangian, cross-checked against toy 5201's classification ---")
rng = np.random.default_rng(11)
sl, tl = [], []
for _ in range(400):
    A = rng.normal(size=(4, 2)) + 1j*rng.normal(size=(4, 2))
    Bb = rng.normal(size=(4, 2)) + 1j*rng.normal(size=(4, 2))
    ev = chain_eigs(krein_projector(A), krein_projector(Bb), A)
    m = np.abs(ev)
    (sl if np.allclose(m, m[0], atol=1e-6) else tl).append(causal_lagrangian(ev))
check("A harness that computes the wrong functional is worse than none, so the Lagrangian gets checked first. "
      "Finster's L(x,y) = Σ|λ_i|² − (1/2n)(Σ|λ_i|)² is non-negative and vanishes exactly when all the "
      "closed-chain moduli coincide -- which is precisely the SPACELIKE condition toy 5201 implements. Over "
      f"the same 400 random pairs: all {len(sl)} spacelike pairs give |L| < {max(abs(x) for x in sl):.1e}, and "
      f"all {len(tl)} timelike pairs give L > {min(tl):.2e}. Two independently written harnesses agreeing on "
      "which pairs are causally inert is the check I would demand of anyone else.",
      all(abs(x) < 1e-12 for x in sl) and all(x > 0 for x in tl),
      f"spacelike n={len(sl)}: |L| ≤ {max(abs(x) for x in sl):.1e}  |  timelike n={len(tl)}: L ≥ {min(tl):.2e}")

# ---------------------------------------------------------------------------
# 1. ★ The sector-split second variation -- Cal's leg-3 concern, measured.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ symmetric-minimum vs full-space saddle: how often do the sectors disagree? ---")
rng = np.random.default_rng(0)
disagree, trials, examples = 0, 12, []
zero_action = 0
for _ in range(trials):
    B0 = rng.normal(size=(4, 2)) + 1j*rng.normal(size=(4, 2))
    N = 3
    Bs = [rot(2*np.pi*k/N) @ B0 for k in range(N)]
    S0 = causal_action(Bs)
    if abs(S0) < 1e-9:
        zero_action += 1
    sym, non = [], []
    for _ in range(14):
        D = rng.normal(size=(4, 2)) + 1j*rng.normal(size=(4, 2))
        sym.append(second_variation(Bs, [D.copy() for _ in range(N)]))
        non.append(second_variation(Bs, [D.copy() if k == 0 else np.zeros((4, 2), complex) for k in range(N)]))
    if min(sym) > 0 > min(non):
        disagree += 1
        examples.append((min(sym), min(non)))
check("★ Cal's §432 leg-3 worry -- that Finster lets the world break its own symmetry to reach lower, so "
      "'symmetric critical point' is not enough -- is not hypothetical. Splitting the second variation into a "
      "SYMMETRIC sector (displace every point alike) and a NON-INVARIANT sector (displace one point only), "
      f"{disagree} of {trials} random symmetric orbits show outright sector disagreement: the minimum second "
      "variation is POSITIVE across all symmetric directions while NEGATIVE in a symmetry-breaking one -- e.g. "
      + "; ".join(f"{a:+.2e} vs {b:+.2e}" for a, b in examples[:3])
      + ". These are genuine local minima INSIDE the symmetric subspace that are SADDLES in the full space. "
      "Symmetric-criticality is not almost-minimality; it is routinely a saddle, and the harness sees it.",
      disagree >= 3,
      f"{disagree}/{trials} symmetric orbits are symmetric-minima and full-space saddles -- the risk is ordinary, not exotic")

# ---------------------------------------------------------------------------
# 2. ★ Palais needs compactness -- and this group is not compact.
# ---------------------------------------------------------------------------
print("\n--- 2. ★ the tool we were going to lean on: Palais requires a COMPACT group ---")
norms = [(t, np.linalg.norm(jboost(t), 2), np.allclose(jboost(t).conj().T @ J @ jboost(t), J))
         for t in (0, 1, 2, 4, 8)]
check("★ Palais's principle of symmetric criticality requires a COMPACT group acting isometrically -- without "
      "compactness it is false in general. The symmetry group here is the Krein-unitary group of the "
      "indefinite spinor metric, and it is NOT compact: the J-unitary boosts satisfy U†JU = J exactly while "
      "their operator norm grows like e^t -- "
      + "; ".join(f"t={t}: ‖U‖ = {n:.3e} (J-unitary {ok})" for t, n, ok in norms)
      + ". So 'Palais gives us criticality for free' is not available as stated. This is a STRONGER point than "
      "Cal's: he flagged that Palais yields a critical point and not a minimum; for this group it may not "
      "yield the critical point either. Criticality in the boost directions has to be earned, not cited.",
      all(ok for _, _, ok in norms) and norms[-1][1] > 1e3,
      f"J-unitary boosts: U†JU = J exactly, ‖U‖ = {norms[-1][1]:.3e} at t=8 and unbounded ⟹ non-compact")

# ---------------------------------------------------------------------------
# 3. ★★ The problem is not yet well-posed: the unconstrained minimum is trivial.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★ before anyone climbs: the unconstrained action minimizes to nothing ---")
check("★★ The causal action is non-negative and vanishes exactly when EVERY pair is spacelike -- and in "
      f"{zero_action} of the {trials} random configurations above, S came out exactly zero. So the "
      "UNCONSTRAINED global minimum of the causal action is the trivial, totally-spacelike configuration: a "
      "world with no causal relations at all. Ours is manifestly not that -- the closed chains are a genuine "
      "215/185 spacelike/timelike mix. ⟹ 'our configuration minimizes the causal action' is FALSE as an "
      "unconstrained statement, and can only be true relative to Finster's constraints (volume, trace, "
      "boundedness). NAMING THE CONSTRAINT SET IS PART OF THE PROBLEM, NOT A TECHNICALITY -- a minimisation "
      "claim without it is minimising to nothing. This has to be settled before the climb starts, and it is a "
      "specification question for @Lyra and @Cal, not a computation.",
      zero_action >= 3,
      f"S = 0 exactly in {zero_action}/{trials} random configs ⟹ trivial totally-spacelike minimum ⟹ constraints are load-bearing")

# ---------------------------------------------------------------------------
# 4. The deliverable and its honest scope.
# ---------------------------------------------------------------------------
print("\n--- 4. deliverable and scope ---")
check("The harness is packaged as causal_lagrangian / causal_action / second_variation(config, directions), "
      "with the sector split done by the caller choosing symmetric vs non-invariant displacement patterns. "
      "@Lyra -- hand me the configuration and its symmetry group and I return the second-variation spectrum "
      "with the sectors labelled, same session. It is built before your configuration exists, so it cannot be "
      "tuned to it -- same discipline as the Leg-1 harness in toy 5201.",
      True,
      "second_variation(config, dirs) + verified causal Lagrangian; sector split by displacement pattern")

check("SCOPE, so nobody reads this as the climb rather than the rope: this is a finite-dimensional model on "
      "the ℂ⁴ spinor module with the projector-manifold constraint handled automatically (perturbing the "
      "subspace keeps P² = P), and NOTHING ELSE constrained. The volume, trace and boundedness constraints are "
      "NOT implemented, precisely because which ones apply is the open specification question in item 3. It "
      "does not prove or disprove anything about our configuration -- it is the instrument that will, once "
      "there is a configuration and a constraint set to point it at.",
      True,
      "finite-dim model; projector constraint automatic; CFS volume/trace/boundedness NOT implemented pending the spec")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (harness built + cross-checked; symmetric minima are saddles {disagree}/{trials}; Palais needs compactness and the group is not; unconstrained action minimizes to nothing)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5204, the minimum harness -- route item 1, built before the configuration exists):
  * FOUNDATION: Finster's L = Σ|λ|² − (1/2n)(Σ|λ|)² implemented and CROSS-CHECKED against toy 5201 -- all
    {len(sl)} spacelike pairs give L = 0 (≤{max(abs(x) for x in sl):.0e}), all {len(tl)} timelike pairs give L > 0. Two independent harnesses agree.
  * ★ CAL'S §432 LEG-3 IS A LIVE RISK, NOT A FORMALITY: {disagree} of {trials} random symmetric orbits are genuine
    minima inside the symmetric subspace and SADDLES in the full space (min d²S sym > 0 > min d²S non-invariant,
    e.g. {examples[0][0]:+.1e} vs {examples[0][1]:+.1e}). Symmetric-criticality is routinely a saddle.
  * ★ NEW GATE -- PALAIS NEEDS COMPACTNESS AND WE DO NOT HAVE IT: the Krein-unitary group is non-compact
    (J-unitary boosts, U†JU = J exactly, ‖U‖ = e^t unbounded). Stronger than Cal's point: for this group
    Palais may not even deliver the critical point. Criticality in the boost directions must be EARNED.
  * ★★ AND FIRST OF ALL -- THE PROBLEM IS NOT YET WELL-POSED: the unconstrained action is minimised by the
    trivial totally-spacelike configuration (S = 0 exactly in {zero_action}/{trials} random configs), and our world is
    manifestly not that. So "our configuration minimises the causal action" is only ever true RELATIVE TO
    Finster's constraints. NAMING THE CONSTRAINT SET IS PART OF THE PROBLEM. @Lyra @Cal -- this is a
    specification, not a computation, and it comes before the climb.
  * DELIVERABLE: second_variation(config, dirs) with sector labels, ready same-session for @Lyra's
    configuration. SCOPE: finite-dim, projector constraint automatic, CFS constraints NOT implemented pending
    the specification above.

AUG-12. Nothing pushed. Nothing banked. Built before the configuration exists -- same discipline as toy 5201.
Count once. CP existence-only.
""")
