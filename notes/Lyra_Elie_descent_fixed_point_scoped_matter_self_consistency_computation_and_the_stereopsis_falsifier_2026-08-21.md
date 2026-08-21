# The descent fixed-point, scoped — what the matter-self-consistency computation is, and what observation refutes it

**Round 40. Builds on the banked Machian result (T2565, K1522), does not re-derive it.** The descent is forced-except-one-input (Round-39 scoping): structure derived (single-step P²=P, codim-1, signature (3,1)), selection Machian — matter induces the 4D frame. The open upgrade from *induced* to *predicted* is a **matter-self-consistency fixed point**. This scopes (a) what the fixed-point computation looks like and (b) what observation would refute it — the can-fail data question Casey wants. Reconnected: T2565 (geometry-alone not forcible), K1522 (exterior/Machian frame), T2564 (causal-set height dimension), F996 (stereopsis fork), F1046 (the n_C=5 fixed-point as the template).

## (a) The fixed-point condition — and why it is the right object

The Machian input (K1522) is a **commitment site-measure μ on S⁴** — the exterior's recorded matter distribution (via light-absorption), the CMB-frame analogue. From μ the descent reads a frame:
- **position** breaks SO(5)→SO(4) (Born-localization T2542 — corpus-supplied per observer);
- **velocity** breaks SO(4)→SO(3) (the (4,1)→(3,1) leg — the genuinely owed matter input).

Write **F(μ) = the 4D Lorentz frame induced by the matter distribution μ**, and **μ(F) = the matter distribution as recorded in frame F**. The self-consistency (fixed-point) condition:

> **μ\* = μ(F(μ\*))** — the matter distribution reproduces itself when read in the frame it induces.

This is the exact shape of the n_C=5 fixed point (F1046: a monotone-crossing balance the flow is *required* to sit at), and of Smolin-style "seed = terminus" self-selection forced by rigidity, not survival (BST_Not_Here §6c). **The trichotomy that decides the tier:**
- **unique, non-degenerate μ\*** → the 4D frame is *self-consistently selected by matter* → observed 4D is **PREDICTED** (matter-predicted, the upgrade lands).
- **a degenerate family of μ\*** (e.g. any SO(5)-rotation of a solution) → 4D is only **INDUCED** (matter-posited; the frame is a choice within a family — the honest current floor).
- **no μ\*** → the Machian descent **fails** (a real refutation of the mechanism).

**Why "non-degenerate" needs the HEIGHT, not the ordering fraction (T2564/F991):** the dimension read must come from the commit-order causal set's **height** (longest chain), which grows with dimension, NOT the Myrheim–Meyer ordering fraction (which is shape-degenerate — F991/Elie 5277 showed it reads ~rank, a false 2). So the fixed-point's dimension check is: does μ\* yield a causal set whose height-scaling reads d=4 (region-matched sampling at physical N)?

## (b) What the computation looks like (Elie's to build; pre-registered here)

A concrete iteration, target-innocent (no 4 put in by hand):
1. **Seed** with a trial matter measure μ₀ on S⁴ (start from an SO(5)-generic distribution — NOT the round/uniform vacuum measure, which is the fixed point of the *wrong* map: 5272's uniform-on-S⁴ is SO(5)-invariant and collapses back to uniform, giving no frame — T2565. Use a genuinely anisotropic seed, the committed-event distribution, e.g. Grace's `committed_events_v2.npy`).
2. **Read the frame** F(μₙ): compute the position (SO(5)→SO(4)) and the velocity/momentum axis (SO(4)→SO(3)) the distribution μₙ induces. This is the (4,1)→(3,1) leg — the owed step made computational.
3. **Re-record** μₙ₊₁ = μ(F(μₙ)): the matter distribution as it appears in frame F(μₙ).
4. **Iterate to convergence.** Check: does the sequence converge to a μ\*? Is μ\* unique (independent of the anisotropic seed's details)? Read the dimension via causal-set height (T2564) — does it come out 4 without 4 being assumed?
5. **Positive control:** run the same map on a *known* configuration and confirm it reads the right dimension; and confirm the round/uniform vacuum measure is a *non*-attracting fixed point (it gives no frame), so the mechanism is not construction-guaranteed to any answer.

**Pre-registration (the tier is set before the number):** unique + non-degenerate + height reads 4 → PREDICTED; degenerate family → INDUCED (floor); no fixed point → mechanism refuted. The seed must be anisotropic-from-matter (else 5272 makes it round by construction — the empty-confirmation trap).

## (c) What observation would refute it — the stereopsis fork, made concrete

The load-bearing physical content (F996): a *shared world* enables parallax that would let observers triangulate a 4th spatial direction. If the 4th spatial dimension were **recoverable**, we would perceive 4 spatial dimensions — we perceive 3. So the descent needs the 4th spatial dimension **unrecoverable even given a shared world**, and that is a genuinely can-fail claim with standard observational teeth. **The transverse S³ ⊂ S⁴ is compact (the KK direction), so "unrecoverable" = "the compactification scale is beyond reach."** BST's KK scale is Planckian (Elie: m_KK ~ 1.22×10¹⁹ GeV). Three falsifiers, all standard:

| falsifier | what it tests | BST prediction | refutes if |
|---|---|---|---|
| **KK tower search** | modes of the compact transverse S³ | tower at m_KK ~ Planck → invisible | a sub-Planckian KK excitation is found (the 4th dim is *not* Planck-compact) |
| **inverse-square law** | Gauss-law falloff of gravity/EM (1/r² in 3 spatial dims → 1/r³ in 4) | 1/r² holds to all accessible scales (4th dim compact below reach) | a 1/r³ regime appears at an accessible scale (a large/recoverable 4th spatial dim) |
| **direct parallax / stereopsis** | can any observer triangulate a 4th macroscopic spatial axis? | no — the 4th is compact/unrecoverable | any physical effect resolves a 4th macroscopic spatial direction |

**This is the can-fail question in falsifiable form:** BST predicts the 4th spatial dimension is Planck-compact and therefore unrecoverable — so no sub-Planck KK tower, no 1/r³ gravity/EM at accessible scales, no parallax recovery of a 4th axis. Any of those three, observed, refutes the "unrecoverable 4th" claim on which the descent's single-drop-to-(3,1) rests. *(These are the standard large/warped-extra-dimension bounds turned into a BST falsifier: BST sits firmly on the "compact-at-Planck" side, which the data currently supports — the prediction is exposed, not safe-by-construction.)*

## Honest tier

- The fixed-point *object* (μ\* = μ(F(μ\*))) and the trichotomy are **well-posed** (Structure); the *computation* is Elie's to run, pre-registered here.
- The upgrade induced→predicted is **OPEN** until the computation returns unique + non-degenerate + height-reads-4.
- The **falsifiers are live now** (KK, inverse-square, parallax) — the descent's "unrecoverable 4th" is exposed to data, not safe-by-construction. This is exactly the can-fail deep frontier.

**Lyra + Elie, 2026-08-21 (descent fixed-point scoping, Round 40; builds on T2565/K1522, does not re-derive). The matter-self-consistency fixed point: μ\* = μ(F(μ\*)) — the exterior matter distribution reproduces itself in the frame it induces (F = position SO(5)→SO(4) + velocity SO(4)→SO(3)). TRICHOTOMY sets the tier: unique+non-degenerate+height-reads-4 → 4D PREDICTED; degenerate family → INDUCED (floor); no fixed point → mechanism refuted. Dimension via causal-set HEIGHT (T2564), not the shape-degenerate ordering fraction. Computation (Elie, pre-registered): iterate F from an anisotropic matter seed (NOT the round vacuum measure — 5272 makes that round by construction, the empty-confirmation trap), check convergence/uniqueness/height=4, positive-control that uniform is non-attracting. FALSIFIERS (the can-fail data question, F996 stereopsis made concrete): BST predicts the 4th spatial dim is Planck-compact/unrecoverable → NO sub-Planck KK tower, NO 1/r³ gravity/EM at accessible scale, NO parallax recovery of a 4th axis; any of the three refutes. Exposed to data, not safe-by-construction. Nothing pushed; CP existence-only.**
