---
title: "Lecture 7 — Mixing"
spine: "D_IV⁵: QM, GR and the SM — the derivations, tiered"
author: "Keeper, for Casey Koons and the team"
date: "2026-09-11 — v0.1"
sources: "Rounds 47–61 (K1791–K1810; folded into the rubric 2026-08-22); T2519 (skeleton, rank-1 alignment); T2530 (λ = 1/√20 blind, 2026-07-29; Gatto); T2547 (CP existence); the partial-isometry condition; K1808/K1810 (the order — Cayley–Hamilton on the generation space; K1810 is Keeper's own six-correction walk-back of K1808); the sealed negative (K1800: five series hashed before filing); K1002 → 08-22 (V_cb value retired, position kept); K1801 and K1809 (the curated layer's three λ's; count over ranking; smallest-of-N); K1635 (mixing is not radial); K1799 (the Q⁵ parity fold is a projector, spectrum {0,1}); PDG 2024 Rev 12 (first-row unitarity 0.9984 ± 0.0007; λ = 0.22501 ± 0.00068; A = 0.826 ± 0.015; |V_cb| exclusive (39.77 ± 0.46)×10⁻³)"
tier_line: "DERIVED: the skeleton; λ = 1/√20, blind; CP existence; flavour universality as the partial-isometry condition (CKM = U_up†U_down the forced survivor); THE ORDER — |V_ub| one power of λ below |V_cb|, zero-knob. INPUT: the corner's value (a coordinate, not an invariant); δ_CP's magnitude; |V_cb| (value retired, position kept); A. FIRED AND LOST: five sealed series for the corner value. LIVE FALSIFIER: first-row unitarity. NOT CLAIMED: the exact mixing values beyond λ; any 'smallest-of-N' form without N reported."
---

# Lecture 7 — Mixing

## The question

Why do quarks of different generations mix the way they do — and what exactly did the geometry predict before anyone looked?

When a quark changes flavour under the weak force it can land in any generation, with amplitudes collected in the CKM matrix: nearly diagonal, with a small first-to-second element $\lambda \approx 0.22$, a smaller second-to-third of order $\lambda^2$, and a first-to-third smaller still. The Standard Model takes all four of its mixing parameters as inputs. This lecture reports what the object fixes about them — one value, one *order*, and the structural reason the matrix has the shape it has — and it reports, with the same care, five formulas we sealed in an envelope that all turned out wrong.

## For the reader in a hurry

Quarks come in three families, and when one changes family the odds fall off steeply: the jump from the first family to the third is much rarer than from the second to the third. We asked the shape two things. How big is the first mixing angle? It said $1/\sqrt{20}$, on a dated day in July before we compared, and the measured value agrees to a third of a percent. How much rarer is the far jump than the near one? It said *exactly one step rarer* — a statement with no dial in it, because you cannot tune an order. What the shape did not tell us is the size of the far jump itself. We wrote down five candidate formulas, sealed them by hash, opened the envelope, and all five missed. We publish that next to the prediction.

## The skeleton, and why the matrix is a product

Generation space is three-dimensional (Lecture 6). The weak current, in the object's own terms, is a map between the up-type and down-type generation modules, and the geometry fixes its *skeleton*: a rank-one alignment on the leading stratum (T2519) — the matrix is nearly the identity because the first-stratum states of the two modules are aligned.

The next fact is the one that turns a texture into the CKM matrix. Flavour universality — the weak force couples all three generations with the same strength — is, in this language, the **partial-isometry condition**: the current $V = A^\dagger J B$ is unitary exactly when it couples all three equally. Given unitarity, the only survivor is $V = U_{\text{up}}^\dagger U_{\text{down}}$, the product of the two diagonalising rotations. That the CKM matrix is a *product of two unitaries* is usually a definition; here it is what falls out of universality.

Two things the mixing is *not*, both proved and both useful: it is not radial (K1635 — a purely radial mechanism gives $10.2\%$ and is dead), and it is not carried by the parity fold of the quadric (K1799 — that fold is a projector with spectrum $\{0, 1\}$ and has no scale of its own; a whole class of "the fold sets the angle" readings dies with it).

## The Cabibbo angle, blind

On the down-type module the geometry produces a texture with a zero in the (1,1) place, and diagonalising it gives

$$\tan\theta_C \;=\; \sqrt{\frac{m_d}{m_s}}\,,$$

the Gatto relation — not imposed, but the geometry's own texture. With the strange-to-down mass ratio at the object's lattice value, $m_s/m_d = \text{rank}^2\, n_C = 20$ — an identified monomial (Grace's tier map), carried by T2530 as its stated input — the Cabibbo angle is

$$\lambda \;=\; \sin\theta_{12} \;=\; \frac{1}{\sqrt{20}} \;=\; 0.22361 .$$

This was obtained on 2026-07-29, dated in the registry (T2530), before the comparison. Against PDG 2024's direct value $0.22501 \pm 0.00068$ it sits at $-2.06\sigma$. Here is the honest part, and it is also the interesting part: with $|V_{ud}| = \sqrt{19/20}$ the first row is *exactly* unitary, while the direct determinations of the first row currently sum to $0.9984 \pm 0.0007$ — $2.3\sigma$ short of unity, a known tension. So the object predicts the unitary value, and the data are $2\sigma$ off it in the direction of a tension the experiments themselves report. Which side we score against is pre-registered, not chosen after; it is Casey's call and it is written down before the next PDG.

An old form of the same angle, $2/\sqrt{79}$, sat at $+0.01\sigma$ on the direct value and lived in the curated chapters for months. It is retired — not because it fits worse, but because its provenance was a vacuum-subtraction step that could be tuned, while $1/\sqrt{20}$ was blind. The lesson is in the memory file: a competitor *count* is target-independent; a *ranking* is not.

## The order — the one thing about the corner the geometry fixes

Why is $|V_{ub}|$ so much smaller than $|V_{cb}|$? This is a standing puzzle in the Standard Model, and the object answers it at the level of *order*.

The generation space is three-dimensional, so by Cayley–Hamilton every power series in the relevant operator collapses to a quadratic. Write $S$ for the even part of the squared mixing generator; its characteristic polynomial is $x^3 - 5x^2 + 6x - 1$, and every series in it reduces to $\beta S + \alpha S^2 + \gamma\cdot 1$. Now read off the matrix elements: $S_{13} = 0$ and $(S^2)_{13} = 1$. The $1$–$3$ corner is *absent* at first order and *opens* at second; the $2$–$3$ subdiagonal opens at first. In rung language, the corner opens two rungs later than the subdiagonal. Therefore

$$|V_{ub}| \;\sim\; \lambda\,|V_{cb}|$$

— **suppressed by exactly one power of $\lambda$** (K1808, corrected and confirmed in K1810). The statement uses no normalisation and no fitted integer. It is a *position* in the matrix, not a coordinate, which is Cal's bar for a derived claim and the reason it has no knob: orders are reparametrisation-invariant, so there is no map to owe and nothing to tune.

The corner *ratio* itself is $t/(1 + 4t)$ for a parameter $t$ that the geometry does not fix — a coordinate, whose value at the integer normalisation lies in $[0.120, 0.190]$. That is the input.

## The envelope

Because the ratio $t/(1+4t)$ is a Möbius bijection, the structure itself could not have failed — any measured corner corresponds to *some* $t$. So the can-fail lived entirely in the candidates for $t$. Five candidate series, motivated by the rails of the construction, were named, written down, and sealed by SHA256 (K1800) *before* they were filed. Then the envelope was opened and each was scored against a band pinned to PDG.

**All five missed** — by factors of $2.3$, $1.9$, $3.0$, $2.9$ and $3.3$ at the nearest edge. Two of the misses are unconditional (pure powers, normalisation-invariant); three are at the integer normalisation. Lyra's structural reading of the failure, stated as a conjecture with its kill condition: the band needs $\beta/\alpha \in [5.3, 8.4]$ and all five candidates are $S^2$-heavy, $\beta/\alpha \leq 1$, so the misses are one-directional; *exhibit any rail-motivated series with $\beta/\alpha \geq 5$* and the conjecture dies.

We count this as the sector's second-best result. The first is the order; the second is that we can say, with a hash to prove it, that five specific ideas about the value were wrong.

## What is input, and one retirement

The corner's value; the magnitude of the CP phase (its *existence* is derived, T2547 — a real domain has no natural phase and a complex one does); the Wolfenstein $A$ (the curated layer's $4/5$ was a candidate with no mechanism, now at $-1.7\sigma$); and $|V_{cb}|$, whose old value $0.044$ is retired at $+9.2\sigma$ against the current exclusive determination — its *position* in the matrix, $A\lambda^2$, is kept, and the inclusive/exclusive split of more than $3\sigma$ in the data is noted rather than exploited.

One methodological retirement belongs in this lecture because it happened here. A curated chapter of the Guide carried, in one section, three mutually inconsistent values of $\lambda$ and a Jarlskog form presented as "the smallest of $N$" with $N$ unreported (K1801, K1809). The honest form of any such claim is *the smallest of $N$ proved conditions plus a measured tiebreaker, with $N$ stated* — and where several integer forms fit a band equally well, the number of competitors is reported, not the winner. $\gamma = \arctan\sqrt{5}$ admits ten such competitors in its band and is not cited as derived.

## Tier line

- **Derived:** the skeleton; flavour universality as the partial-isometry condition; $\lambda = 1/\sqrt{20}$ (blind); CP existence; the order of the corner.
- **Fired and lost, certified:** five sealed series for the corner's value.
- **Input:** the corner's value, $\delta_{CP}$'s magnitude, $A$, $|V_{cb}|$ (position kept).
- **Not claimed:** exact values beyond $\lambda$; any "smallest-of-$N$" without $N$; $\gamma$ or $J$ as derived.

## What would make this lecture wrong

If the first-row unitarity tension resolves *against* unity — the direct determinations confirmed and the sum staying short — then $\lambda = 1/\sqrt{20}$ is wrong as stated. If $|V_{ub}|/|V_{cb}|$ is ever measured as other than one power of $\lambda$, the order is wrong, and the order has no knob to absorb it. Both are checkable against the current PDG in an afternoon, which is the kind of falsifier this program most wants to publish.

## Where to look

The Round 47–61 arc (K1791–K1810), folded into the rubric on 2026-08-22; T2519, T2530, T2547; the sealed-negative hashes in K1800; K1801 and K1809 for the curated-layer corrections; K1635 and K1799 for the two dead mechanisms; PDG 2024 Rev 12, eq 12.7/12.8, for every experimental number quoted here.
