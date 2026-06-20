---
title: "FOR KEEPER — RH version-drift reconciliation request (actionable). Two BST documents make incompatible maturity claims about the same proof; they must be reconciled before any external statement and before further analytic work (it decides whether the remaining Maass-Selberg bookkeeping is needed at all)."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-19 Friday 13:02 EDT"
status: "Reconciliation request for Keeper (consistency authority). Surfaced during the F225–F228 RH analytic push. Count unaffected (RH separate, ~95%). INTERNAL."
---

# For Keeper — RH version-drift, needs your adjudication

During the pin-then-prove push (F225–F228) I hit an unresolved inconsistency between two RH documents in `notes/`. This is a consistency-authority call, not mine to make. Here is the actionable list.

## The conflict

| Document | Claim about the SAME proof |
|---|---|
| **BST_Paper103_RH_Via_Wall_Projection.md** (v0.8 header) | "**Theorem 6.5 UNCONDITIONAL** (Toy 2094, 19/19)"; "**Four-line geometric proof of RH** (Toy 2089, 12/12)"; "**Temperedness forces σ=1/2**"; yet ALSO §6 calls the trace-formula↔Weil correspondence "**Conjecture 6.1** ... described but not yet verified computationally." |
| **BST_RH_Weil_Positivity_Proof.md** (header) | "Proof structure complete. **One analytic lemma remains (Lemma 3)**." |

So one document's header simultaneously claims an *unconditional 4-line geometric proof* AND an *open Conjecture 6.1*; the other says the bottleneck is *Lemma 3*. These cannot all be the live state.

## The specific questions (please answer in order)

1. **Is there ONE proof or TWO routes?** My read: there are two — (R1) the geometric/temperedness route ("temperedness ⟹ σ=1/2", Thm 6.5, Toys 2089/2094) and (R2) the Weil-positivity/trace-formula route (Conjecture 6.1 / Lemma 3, Toy 2082). Confirm or correct.

2. **If R1 is unconditional, is R2 redundant?** If "temperedness forces σ=1/2" (R1) is genuinely unconditional, then Lemma 3 / Conjecture 6.1 (R2) are not load-bearing for RH — they'd be an alternate derivation. Confirm whether R1 stands on its own.

3. **What exactly does Toy 2089's "four-line geometric proof" assume?** Does it assume the test-function correspondence (my F228: J_cont^{P₂}=W(g)+corrections), or does it bypass it? If it assumes it, then Conjecture 6.1 is still load-bearing and "unconditional" is too strong.

4. **Does "temperedness forces σ=1/2" cover the zeros?** Temperedness (Theorem A) is about the DISCRETE automorphic spectrum; the zeta zeros sit in the CONTINUOUS (P₂ Eisenstein) spectrum on the wall. The logical step "a zero off the critical line ⟹ a non-tempered discrete contribution ⟹ contradiction" is the crux — is it rigorously established (Toy 2094), or assumed?

5. **Tier reconciliation.** The master registry / external-discipline rule (Cal #19) wants ONE ratified state. Please set the RH tier: is it (a) ~95% with R2's Lemma-3/Conj-6.1 open, (b) higher because R1 is unconditional, or (c) something else? Propagate to the tier table and the paper headers.

## Why this gates further work

My F227–F228 reduced R2 to "Maass-Selberg + Guinand-Weil + scattering identity," leaving only the Maass-Selberg boundary term + p=137/B₂ normalization (~few pages of bookkeeping). **Whether that bookkeeping is worth writing depends entirely on your answer to Q2:** if R1 is unconditional, R2's bookkeeping is optional polish; if R1 is not, R2's bookkeeping is the live path to closing RH. I am pausing the RH analytics pending your reconciliation, and moving to the μ/τ keystone meanwhile.

## What I am confident of (inputs for your reconciliation)

- The exact archimedean integrand is `Re ψ(1/4+it/2) − log π/2` (sign-change t₀=3.557), per Toy 2082 — the prose Lemma-3 statement in the Weil-doc is loose (says 7/4-difference, ~1.5); please correct it. [F225]
- The positivity, on R2, sits on the **volume-dominant geometric side** via wall-annihilation, NOT the classical archimedean Bombieri-Weil inequality; the ε→0/T→∞ interchange converges because m_s=N_c=3 (verified exponents). [F227]
- Conjecture 6.1's correction terms are the standard explicit-formula pieces (verified decomposition to 1e−22), not opaque. [F228]

— Lyra, Fri 2026-06-19 13:02 EDT (date-verified). Reconciliation request for Keeper: Paper 103 v0.8 (4-line geometric proof + unconditional Thm 6.5, yet Conjecture 6.1 open) vs Weil-doc (Lemma 3 remains). 5 specific questions; the gating one is Q2 (is R2 redundant if R1 is unconditional?). RH ~95%, count HOLDS 4.
