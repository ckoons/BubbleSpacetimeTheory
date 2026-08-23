---
node_type: k_audit
id: K1812
title: "ROUND-63 — the FK Pochhammer family is CLOSED for the charged leptons, THREE independent ways, inside one round of it being opened. Lyra's curvature-sign theorem + Elie's F820 parity forcing COMPOSE into a parameter-free class exclusion; Lyra's target-innocence catch kills it a second way at its first step; the residue lead dies zero-parameter on the (mu,tau) pair. Keeper's 'intermediate steepness' diagnosis CORRECTED to a SHAPE problem."
date: 2026-08-23
author: Keeper
rubric_cell: "External 3 (SM params) / Internal B"
verdict: "CLOSED, class-level, parameter-free. (1) COMPOSITION RULING — Lyra's curvature-sign theorem (for m ~ (nu)_lambda with gaps a,b: b>=a => step2>step1 for ALL nu>0; verified 0 counterexamples) says the charged leptons need b<a, since they DECELERATE (0.0813) while the quarks ACCELERATE (2.239); Elie's F820/K1180 parity forcing says charged leptons are FORCED onto the ODD degree grid (m=N_c|Q|=3 odd, F817 lock k=m mod 2), so ALL GAPS ARE EVEN. Composed and swept by Keeper: the flattest reachable class on the forced odd grid is {1,5,7} (a=4,b=2, front-loaded, Lyra's condition SATISFIED) and it still misses 2.864x OVER. No allowed pattern decelerates enough. (2) Lyra's target-innocence catch, the deeper kill: nu* depends on (lambda_1,lambda_2) only, so the family demands nu_lep = 12.888130 -- not an integer, not forced, not a BST number -- BEFORE the third degree is chosen, while the quarks sit at the FORCED nu_W = N_c = 3. The family fails the target-innocence lens at its FIRST step. (3) The residue lead, un-gated by Keeper on Casey's directive, dies ZERO-PARAMETER: if only the electron is anomalous, (mu,tau) must ride the unmodified quark ladder, giving m_tau/m_mu = (3)_5/(3)_3 = 42 vs observed 16.817, a 2.497x miss BEFORE the electron is reached. KEEPER CORRECTIONS: 'the missing mechanism is INTERMEDIATE in steepness' is WRONG -- the sectors have OPPOSITE log-curvature, so it is a SHAPE problem, not a SIZE problem (Lyra). And Keeper's own scope caveat is REPLACED, not dropped, by the F820 citation (Elie). Look-elsewhere over degree TRIPLES overcounts ~2.9x -- report GAP-CLASSES (73 triples = 25 independent models)."
related: [K1749, "K1749-A", K1811, "Lyra R63 PIN", "Elie toy 5455", "Elie toy 5454", "Cal §706", "F820", "F817", "K1180", "T2572", "T2529", "F506", "toy_5060", "feedback_target_innocence_lens_derived_vs_fit_discipline", "feedback_family_sweep_every_forcing_selector_rank_generic_is_selecting_nothing"]
---

# K1812 — a lane opened and shut in one round, and the shutting is worth more than the opening

**Rubric cell: External 3 / Internal B. Verdict: the FK Pochhammer family is CLOSED for the charged leptons — class-level, parameter-free, three independent ways.**

This morning I un-gated a lead that K1749 had flagged *"don't pursue."* Casey's directive was **investigate, don't gate**. **It was investigated, and it returned a definite negative inside one round.** That is the directive working exactly as intended: **the brake controls the CLAIM, not the INVESTIGATION**, and the fastest way to retire a speculation is to let it run against a bar set in advance.

## ★ RULING 1 — the COMPOSITION. Two teammates' results, neither written for the other, compose into a class exclusion.

**Lyra's curvature-sign theorem.** For m ∝ (ν)_λ with gaps a = λ₂−λ₁ and b = λ₃−λ₂: step 1 is a product of *a* consecutive factors, step 2 a product of *b* factors, and **every factor in step 2 exceeds every factor in step 1.** ⟹ **b ≥ a ⟹ step2 > step1 for ALL ν > 0 — unconditionally accelerating.** *(Keeper verified: 0 counterexamples across ν ∈ {0.1 … 500} × (a,b) grid.)*

**And the two sectors have OPPOSITE log-curvature in the same generation index** *(verified from PDG)*:

| sector | step 1 | step 2 | step2/step1 | |
|---|---|---|---|---|
| charged leptons | 206.768 | 16.817 | **0.0813** | **DECELERATING** |
| quarks (d,s,b) | 20.000 | 44.786 | **2.239** | ACCELERATING |
| FK ladder 1:20:840 | 20 | 42 | 2.100 | ACCELERATING |

⟹ **the charged leptons require b < a — degree gaps FRONT-LOADED.**

**Elie's F820/K1180 parity forcing**, read from the primary rather than recalled: **m = N_c|Q| gives a charged-lepton weight m = 3 (ODD)**, and the **F817 parity lock is k = m mod 2**, so **charged leptons are FORCED onto the ODD degree grid.** ⟹ **every gap is EVEN.**

**KEEPER'S COMPOSITION AND SWEEP** (the two conditions together, which neither author ran):

```
   forced odd grid, ALL even gaps, nu* solved from m_mu/m_e, predicting m_tau/m_e:
     (1,5,7)   a=4 b=2  FRONT-LOADED (Lyra's condition SATISFIED)  nu*=1.4578    2.864x OVER
     (1,3,5)   a=2 b=2                                             nu*=12.8881  15.955x OVER
     (3,5,7)   a=2 b=2   [identical -- gap-class shift invariance]  nu*=10.8881  15.955x OVER
     (1,5,9)   a=4 b=4                                                          229.08x OVER
     (1,3,7)   a=2 b=4                                                         5390.9x OVER
```

> ### ⟹ **THE FLATTEST PATTERN THE PARITY FORCING ALLOWS IS {1,5,7}, IT SATISFIES LYRA'S FRONT-LOADING CONDITION, AND IT STILL MISSES BY 2.864× OVER. No allowed degree pattern decelerates enough, at any ν. The family is excluded as a CLASS, parameter-free.**

**And Lyra's own withheld candidate is independently killed by the same forcing.** She reported {1,3,4} at 5.8% under on a one-parameter two-target test and **explicitly refused to bank it**, asking to be held to that. **Held, and now moot: {1,3,4} has gaps a = 2, b = 1 — b is ODD, requiring degree 4, which is EVEN, which F820 EXCLUDES for charged leptons.** Her refusal was right on discipline; the structural reason arrived an hour later. *(Her stated "against" was already decisive on its own: 5.8% is best-of-25 and far outside our sub-percent bar, and her b<a condition was derived FROM the lepton data — target-informed.)*

## ★ RULING 2 — Lyra's target-innocence catch is the DEEPER kill, and it fires before the degrees matter

**ν\* depends on (λ₁, λ₂) only, never on λ₃** — which is why {1,3,4} and {1,3,5} share ν\* = 12.888130.

| | ν | status |
|---|---|---|
| quarks | **ν_W = N_c = 3** | **FORCED**, a BST integer, target-innocent |
| charged leptons | **ν_lep = 12.888130** | not an integer, not forced, **not a BST number** |

> **The Pochhammer family requires the lepton sector to carry a FREE, NON-FORCED parameter, and it requires it BEFORE the third degree is chosen. The family fails the target-innocence lens at its FIRST step.** That is the K1684 free-parameter hunt, and **the honest win-condition for this lane was never about degrees at all: could ν_lep be FORCED from D_IV⁵? If it must be fitted, the number it produces is worth nothing however close it lands — including Lyra's own 5.8%.** *(She wrote that against her own candidate. That is the standard.)*

## ★ RULING 3 — the residue lead dies ZERO-PARAMETER, and it dies before the electron

I un-gated this on Casey's directive; **Lyra investigated it and it failed in its only falsifiable form.** If **only** the electron is anomalous, then (μ, τ) must ride the **unmodified** quark ladder: degrees (3,5) at ν_W = N_c = 3, **nothing free** ⟹ **m_τ/m_μ = (3)₅/(3)₃ = 2520/60 = 42 vs observed 16.817 — a 2.497× miss.** *(Keeper verified.)* **The lead fails on the (μ,τ) pair BEFORE the electron is reached.** It survives only if the residue *also* touches μ or τ — **which defeats the mechanism's whole point.**

**Scope, stated exactly:** killed **in its zero-parameter form, which was the only falsifiable one.** Not "dead in every form." **Un-gating it was correct and the investigation returned the answer in under an hour — that is the fastest a speculation has ever been retired here.**

## ★ CORRECTIONS TO MY OWN FRAMING — two, both accepted

**1. "The missing mechanism is INTERMEDIATE in steepness" is the WRONG DIAGNOSIS (Lyra).** The sectors do not differ in *magnitude* of steepness; they differ in the **SIGN of the log-curvature** — leptons decelerate, quarks accelerate. **A size problem yields to a parameter; a SHAPE problem does not.** ⟹ what to look for is **not a slower ladder but a differently-curved one.** My bracket was measuring the right object with the wrong ruler. **Restate everywhere as a SHAPE constraint.**

**2. My scope caveat is REPLACED, not dropped (Elie).** Cal §706 correctly forced me to qualify the upper wall as *"at the quark's {1,3,5} pattern"* — 13 of 73 raw triples are under-steep, so at face value the caveat was load-bearing. **F820 removes the need for it: every under-steep gap-class — (2,3), (3,4), (4,5), (5,6) — has an ODD gap, hence an EVEN degree, which the parity forcing excludes.** So the honest statement is **"too steep at EVERY degree pattern the parity forcing allows,"** and it must **cite F820**. **A caveat removed without its reason is how a scope gets shed** — the caveat goes out and the citation goes in, in the same edit.

## ★ COUNTING CORRECTION, standing (Elie) — report GAP-CLASSES, not triples
(ν)_λ₃/(ν)_λ₁ is a product of consecutive terms starting at ν+λ₁, so **(λ₁,λ₂,λ₃) → (λ₁+1, λ₂+1, λ₃+1) with ν → ν−1 gives IDENTICAL ratios** *(Keeper verified: (1,3,5) and (3,5,7) both return 15.955×).* **The model depends only on the GAP PAIR, never on the absolute degrees. 73 admissible triples from degrees 1–9 are only 25 INDEPENDENT MODELS — a look-elsewhere over triples OVERCOUNTS BY ~2.9×.**

> **BANK: a family whose members are related by a coordinate shift is not a family. Same species as the floating exponent, one level up — and the remedy is the same: quotient by the reparameterization before you count.**

## What survives, and what the sector now honestly says
- **Koide: CONDITIONAL-FORCED.** Relation banked at 0.0009%; **no derivation.** Unchanged.
- **F506 is now a THEOREM-SHAPED statement, not an observation:** the quark mass machinery does not transfer to the leptons, and we can now say **why** — **opposite log-curvature, plus a parity forcing that removes every decelerating degree pattern.**
- **The charged-lepton mechanism is not an FK Pochhammer ladder.** That is a real, parameter-free negative about the sector, and it is the most informative thing produced today.
- **Untouched:** λ = 1/√20 (blind) · the ORDER result · flavour-universality · CP existence · the sealed negative · the up sector (separately negative, toy_5060, 08-05 — Elie verified it closed by the object rather than assuming).

**— Keeper, K1812, 2026-08-23.** Opened this morning on Casey's *investigate, don't gate*; closed the same day, three independent ways, by a composition neither author ran and a target-innocence catch that fires before the degrees matter. **My "intermediate steepness" reading is corrected to a SHAPE problem; my scope caveat is replaced by its F820 citation rather than dropped; look-elsewhere is counted in gap-classes from here.** Koide CONDITIONAL-FORCED. Nothing pushed. CP existence-only.
