---
title: "Intermediate Result: The Backbone Has a Field-Predictable Core and a Delocalized Residual"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "NEW intermediate finding (computational, small n). A depth-0 'polarity field' feature predicts backbone VALUES at ~80% accuracy (~0.25 bits/|B|), constant field-strength but slowly declining predictiveness. This sharpens delocalization: the local signal does not vanish in strength, only in predictiveness. Proposes a strengthened, more defensible conjecture -- the CDC restricted to the field-orthogonal RESIDUAL backbone -- which concedes the trivially-predictable part and isolates the genuine hardness. Decisive scaling needs a solver (n >> 20)."
related: ["notes/BST_AC_Paper_C_Delocalization.md","notes/BST_PvsNP_Audit_Independent.md"]
---

# A field-predictable core inside the backbone

Attacking the load-bearing assumption (delocalization: the backbone is global,
unreadable from local structure) by direct test rather than acceptance.

## The finding

Define the **polarity field** of variable `v`: `field(v) = (pos − neg)/deg`, where
`pos`/`neg` count appearances of `v` as a positive/negative literal. This is a
depth-0 feature (a single count, no propagation, no search).

Measured on random 3-SAT at `alpha = 4.2` (brute-force backbone, `n = 12..16`):

| n | value-AUC | acc(`val = sign(field)`) | bits/\|B\| | mean\|field\| |
|---|---|---|---|---|
| 12 | 0.876 | 0.798 | 0.274 | 0.261 |
| 14 | 0.845 | 0.795 | 0.268 | 0.281 |
| 16 | 0.841 | 0.782 | 0.244 | 0.271 |

- **The frozen *value* of a backbone variable is ~80% predicted by its polarity
  field** — `~0.25` bits per backbone bit of mutual information, i.e. `Theta(|B|)`
  at these sizes, not `o(|B|)`.
- **Membership** (which variables freeze) is only weakly local (AUC ~0.6).
- **The field strength `mean|field| ~ 0.27` is constant in `n`** (as it must be:
  a degree-`Theta(1)` variable has polarity fluctuation `Theta(1/sqrt(deg))`), yet
  its **predictiveness slowly declines** (`bits/|B|: 0.274 -> 0.244`).

## What it means (sharper than "tree info = 0")

The delocalization picture is more nuanced than "no local information." Correctly
stated: **the local signal is constant in strength but increasingly *uncorrelated*
with the backbone value as `n` grows.** The backbone splits into

- a **field-predictable core** (~80% of values, captured by a depth-0 heuristic), and
- a **delocalized residual** (the part orthogonal to the field), where the genuine
  hardness must live.

This both (a) shows the BST claim "all probes -> 0 backbone bits" is read too
strongly — a depth-0 polarity probe gets `~0.25` bits/|B|, consistent with their own
BP column (`0.34` falling) — and (b) points to a **strictly more defensible
conjecture.**

## Proposed strengthening: the Residual CDC

Replace the CDC `I(B; f(phi)) = o(|B|)` (challenged by the field heuristic) with:

> **Residual Cycle Delocalization Conjecture.** Let `B_res` be the backbone modulo
> its field-predictable component (the projection of `B` orthogonal to the polarity
> field, or equivalently the backbone of the formula reweighted to zero mean field).
> Then `I(B_res; f(phi)) = o(|B_res|)` for all poly-time `f`.

This concedes the part a trivial heuristic gets and isolates the genuinely hard
part. It is a cleaner target and removes the easiest disproof (the polarity
heuristic). The chain `CDC -> T35 -> ...` re-runs verbatim with `B_res` in place of
`B`, provided `|B_res| = Theta(n)` (to be tested).

## Open / next (needs collaboration)

- **Decisive scaling.** `bits/|B|` declines `0.274 -> 0.244` over `n = 12..16` — too
  slow and too short a range to tell `-> 0` (CDC holds) from a positive plateau
  (CDC fails). Settling this needs a **SAT-solver-based backbone** for `n` in the
  30–60 range (brute force caps at ~20). This is the single most decisive experiment.
- **Structural "what if".** Can we *prove* the field-predictiveness decays, i.e.
  `corr(field(v), value(v)) -> 0`? The field strength is constant, so this is a
  statement that the *alignment* between local polarity and the global frozen value
  washes out at threshold. If provable, it establishes the Residual CDC for the
  polarity probe unconditionally -- a real sub-result.
- **Is `|B_res| = Theta(n)`?** Needs the residual measured at larger `n`.
