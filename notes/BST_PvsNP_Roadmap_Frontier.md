---
title: "Roadmap: the Ceiling of the Zero-Cascade Reduction, the EF Wall, and the Real Next Challenge"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "RESEARCH MAP + first result. The zero-cascade reduction free-rides on refutation lower bounds -> its ceiling is the known refutation frontier (resolution, Res(k), SoS done; PC, CP free). Extended Frege is BEYOND the ceiling (no EF lower bound known for any family; the reduction has nothing to import; 'topological inertness of extensions' is false -- extensions are genuinely powerful). The genuine next challenge is NOT EF: it is the LOW-DEGREE / algorithmic average-case hardness of backbone-FINDING, where broad algorithm classes fall under one lens and new results are live. First probe: degree-2 ~ degree-1 at the backbone (improve +0.02, flat) -> low-degree hardness signal."
related: ["notes/BST_Certified_Backbone_ResK_Proof.md","notes/BST_Backbone_Field_Core_Residual.md"]
---

# Where we are, where the wall is, and how to find the next challenge

## 1. What the reduction is (and its ceiling)

The zero-cascade reduction is a **hardness amplifier that free-rides on refutation
lower bounds**: it turns "certify a hard backbone bit" into "refute the `O(1)`-
perturbed expander `phi'`", then imports whatever refutation lower bound the target
system has. So its **ceiling is exactly the frontier of known refutation lower bounds
for random 3-SAT**:

| system | refutation LB on random 3-SAT | reduction status |
|---|---|---|
| Resolution | Chvatal-Szemeredi / BSW (width `Omega(n)`) | done |
| `Res(k)` | Atserias-Bonet-Esteban / Segerlind-Buss-Impagliazzo | done |
| Sum-of-Squares | Kothari-Mori-O'Donnell-Witmer (degree `Omega(n)`) | done |
| Polynomial Calculus | Alekhnovich-Razborov / Ben-Sasson-Impagliazzo (degree `Omega(n)`) | **free** (same expansion -> degree LB; carry verbatim) |
| Cutting Planes | known random-formula CP lower bounds | **free-ish** (import CP LB on `phi'`) |
| AC0-Frege | partial (specific families) | partial |

PC and CP are "free" remaining rungs (same reduction, import the known degree/size
bound). Beyond AC0-Frege the known bounds stop.

## 2. The EF wall (the honest answer)

> **The reduction cannot reach Extended Frege, and no detour through it exists yet.**

- **No EF lower bound is known for any explicit tautology family** -- this is *the*
  open mountain of proof complexity. The reduction free-rides on a known LB; for EF
  there is nothing to import.
- **"Topological inertness of extensions" is false.** Extension variables let EF
  *define* new variables `y = circuit(x)`, which can encode global structure and
  collapse proofs that are exponentially long without them. That power is exactly why
  EF is strong and why EF lower bounds are open. Hoping extensions are "inert" is
  hoping EF = resolution, which is false. So that step in the original chain cannot be
  rescued as stated.
- **The barriers say why, and constrain how.** Razborov-Rudich (natural proofs) and
  Aaronson-Wigderson (algebrization) rule out broad classes of techniques for strong
  systems. Any EF lower bound must evade them; none currently does.

So: EF is not "the next step." It is the famous open problem, and our reduction is
structurally incapable of reaching it.

## 3. How to find the *real* next challenge

The method is general: **find the strongest target where a NEW result is achievable,
not the most impressive target.** Two moves:

**(a) Finish the free climb (within proof complexity).** Carry the reduction to PC and
CP -- this completes the certified-extraction hardness up to the *known refutation
ceiling*. Honest, modest, and it closes the program's reachable range.

**(b) Pivot to the live frontier (the right next challenge).** Backbone-*finding* is a
**search / average-case** problem on a *satisfiable* instance, not a refutation. Its
natural hardness home is **not** proof complexity at all -- it is the modern
**low-degree polynomial / OGP / statistical-query** framework (Hopkins-Steurer;
Kunisky-Wein-Bandeira; Gamarnik), which:

- captures a **broad** class of efficient algorithms (spectral, AMP, local, SoS-`O(1)`)
  under one lens -- broader than any single proof system;
- is **active**, with new average-case hardness results provable now (unlike EF);
- sidesteps the proof-complexity framing where EF is the wall.

This is where "no poly-time algorithm finds the backbone" can be made into theorems
for ever-broader algorithm classes, rather than dashing against EF.

## 4. First result on the new frontier (this work)

Probing low-degree hardness directly: does a **degree-2** local predictor beat the
**degree-1** polarity field at the backbone value?

| n | deg-1 AUC | deg-2 (one BP step) AUC | improvement |
|---|---|---|---|
| 16 | 0.933 | 0.951 | +0.017 |
| 22 | 0.776 | 0.798 | +0.022 |
| 28 | 0.856 | 0.876 | +0.021 |

**Degree-2 barely beats degree-1 (`~+0.02`, flat in `n`).** Going up one degree of
local computation does not crack the residual; the field-predictable core is already
captured at degree 1, and the hard part resists degree 2. This is a **low-degree
hardness signal**: the residual backbone is hard not just for resolution/`Res(k)`/SoS
but for low-degree local computation generally. It is the first data point of the
right program.

## 5. The concrete next steps

1. **Free rungs:** write the PC and CP carries (import the degree/size LB onto `phi'`)
   -- finishes the proof-complexity ceiling.
2. **Low-degree program:** push the degree of the predictor (degree 3, ..., up to
   `O(log n)`) and measure whether the residual-AUC plateaus -- the empirical content
   of the **low-degree conjecture** for backbone-finding. A clean plateau is the
   modern statement of "no efficient algorithm finds the hard backbone."
3. **Formalize:** state the low-degree likelihood-ratio target for the backbone and
   attempt the bound (the live, achievable analog of "P != NP for this problem"), with
   the barriers as the filter for which approaches are alive.

The honest bottom line: **EF is the wrong next target** (open mountain, reduction
can't reach it, inertness false). The right next challenge is the **low-degree /
average-case hardness of backbone-finding** -- broad, live, and already showing the
expected hardness signal.
