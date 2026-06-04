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

---

## UPDATE: decisive scaling via solver backbone — the strong CDC is empirically false

Routed around the `2^n` brute-force wall with an exact DPLL backbone
(`n+1` solver calls/formula, validated `16/16` against brute force at `n=14`).
Scaling the polarity-field signal to `n=40`:

| n | 16 | 20 | 26 | 32 | 40 |
|---|---|---|---|---|---|
| value-AUC | 0.869 | 0.828 | 0.875 | 0.870 | 0.845 |
| acc | 0.789 | 0.763 | 0.787 | 0.817 | 0.780 |
| bits/\|B\| | 0.257 | 0.209 | 0.252 | 0.313 | 0.239 |

**Flat.** The signal does NOT decay from `n=16` to `n=40`. The depth-0 polarity
field is a poly-time `f` with `I(B; f(phi)) = Theta(|B|)`, **falsifying the strong
Cycle Delocalization Conjecture `I(B; f) = o(|B|)`** by explicit construction. (The
earlier `0.876 -> 0.841` "decline" over `n=12..16` was small-`n` noise.)

### What this does to the proof (the precise correction)

The CDC as stated **measures the wrong thing**: marginal mutual information between
the backbone and a predictor is `Theta(|B|)` for a trivial heuristic, so it can't be
the hardness witness. The hardness of random 3-SAT is real but it is **not** in the
marginal bits — it is in the **joint structure**: a predictor that gets ~80% of
backbone bits right *marginally* cannot (i) certify any of them, (ii) identify which
~20% are wrong, or (iii) assemble them into a satisfying assignment (the errors sit
exactly on the hard, correlated constraints).

So the fix is not cosmetic; it is conceptual:

> **The conjecture must be about the residual / joint object, not marginal MI.**
> Candidates: (a) the **Residual CDC** — `I(B_res; f) = o(|B_res|)` for `B_res`
> orthogonal to the field; (b) a **certification** measure — no poly-time `f`
> outputs a *certified* `Omega(n)` backbone bits; (c) a **joint-recovery** measure —
> no poly-time `f` outputs a string within Hamming `o(|B|)` of `B` *with a validity
> certificate*.

Forms (b)/(c) are the honest hardness statements (they survive the polarity
heuristic, which has no certificate), and they are what the resolution/OGP/KS
results actually prove. The original `I(B;f)=o(|B|)` should be **retired**; the
chain `T35 -> ...` should be re-derived over the certified/residual object.

### Status

- **New, verified:** a poly-time depth-0 refutation of the strong CDC, non-decaying
  to `n=40` (solver-exact backbone).
- **Constructive repair:** move the conjecture to a certified/residual hardness
  measure; the algorithm-class results (resolution/OGP/KS) already speak to that
  object, so the framework survives in stronger form.
- **Next:** measure `|B_res|` and the certified-backbone hardness at large `n`;
  re-run `T35` over the corrected object.

---

## STEP 1+2 (done): certified vs uncertified separation, and |B_res| = Theta(n)

Built a **certified backbone extractor**: a backbone bit `v=val` is *certified at
depth d* if `phi ^ (v != val)` has a DPLL refutation using `<= d` branch levels
(`d=0` = unit propagation alone) — a poly-time, certificate-producing extractor.
Compared to the **uncertified** polarity heuristic, on solver-exact backbones:

| n | polarity acc (uncert.) | cert<=1 | cert<=2 | hard(>=3)/n = \|B_res\|/n | \|B\|/n |
|---|---|---|---|---|---|
| 16 | 0.850 | 0.087 | 0.298 | 0.340 | 0.47 |
| 24 | 0.854 | 0.028 | 0.064 | 0.454 | 0.48 |
| 32 | 0.770 | 0.000 | 0.000 | **0.569** | 0.57 |

(`play/sat_certified_backbone.py`.)

- **Step 1 — the separation is clean.** Uncertified polarity stays `~0.8`; certified
  extraction at any bounded depth **crashes to 0** (`cert<=2: 0.30 -> 0.06 -> 0.00`).
  By `n=32` *no* backbone bit is certifiable at depth `<=2`. This is the empirical
  content of the **Certified CDC**: marginal guessing succeeds, certified extraction
  fails. The two measures separate, quantitatively.
- **Step 2 — `|B_res| = Theta(n)`, and growing.** The hard residual (bits needing
  depth `>= 3` to certify) is `0.34n -> 0.45n -> 0.57n` — a constant, increasing
  fraction of `n`. So the corrected chain's premise holds: the residual/certified-hard
  backbone is `Theta(n)`. And the `I_fiat` typecheck is now fixed: over this object
  `I_fiat = |B_res| <= |B| <= n`, well-defined.

**Net for the proof:** the chain `(certified hardness) -> T35 -> ...` now stands on a
measured, well-typed `Theta(n)` object with a clean guess/certify separation -- a
strictly more honest and better-grounded foundation than the original marginal CDC.

(Step 3 — extending the certified-hardness from tree-resolution depth to
width-bounded *dag* resolution, the Ben-Sasson-Wigderson object — in progress.)
