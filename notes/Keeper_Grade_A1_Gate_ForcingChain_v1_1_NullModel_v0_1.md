---
title: "Keeper grade — A1 parameter-role gate CLEARED + Elie forcing chain + Strong-Uniqueness v1.1 null-model discipline"
author: "Keeper"
date: "2026-05-28 Thursday PM EDT"
status: "Three gradings. (1) A1 Macdonald parameter-role: PASS — gate CLEARED, A1 unblocked. (2) Elie forcing chain (3589-3591): CONDITIONAL PASS. (3) Strong-Uniqueness v1.1 null-model: a discipline correction Lyra needs before publishing a (1/3)^N figure."
related: ["Keeper_Macdonald_Parameter_Role_Flag_v0_1.md", "Elie Toy 3588 (integrality) + 3589-3591 (forcing)", "Lyra A1 v0.3 + Strong-Uniqueness v1.1 (C18/C19)", "Keeper_Audit_cFK_Derived_Measure_Theorem_v0_1.md", "K44 Null-Model Defense"]
---

# Keeper grade — A1 gate, forcing chain, v1.1 null-model

## (1) A1 Macdonald parameter-role resolution — PASS. **A1 gate CLEARED.**

The flag I raised this morning (`Keeper_Macdonald_Parameter_Role_Flag_v0_1.md`) is resolved, and **decisively** — by integrality, exactly the right kind of argument:

- A **Ringel-Hall algebra over a finite field has integer structure constants** (they count submodules/extensions). This is a hard constraint, not a convention.
- At the **Hall-Littlewood corner (Macdonald q=0, t=field size=2)**: P₍₁₎² = P₍₂₎ + (1+t)·P₍₁,₁₎ = P₍₂₎ + **3**·P₍₁,₁₎, integer, = N_c. **Valid Hall algebra.** (Verified; Schur sanity at t=0 gives coefficient 1 = s₁²=s₂+s₁₁.)
- At the interior point **(q=2, t=1/137)**: structure constants are non-integer (Elie Toy 3570: c^(1,1) = −46/45). **Cannot be a Hall algebra.**

So the substrate Hall algebra is unambiguously the **Hall-Littlewood corner (q=0, t=2)**; the substrate base 2 is the Macdonald **t** (field size), and α=1/137 is **not a Macdonald parameter at all**. Lyra's A1 v0.3 reparameterization is correct. **Verdict: PASS. A1's central characterization is no longer held — the PRIMARY paper is unblocked.**

Residuals (non-blocking):
- **α=1/137 placement** — routed to Lyra: it is an *evaluation / coupling*, not a Macdonald (q,t) coordinate. A1 must state where it enters (observable-evaluation point on the Hall-Littlewood algebra / the N_max-scale at which physical quantities are read off). Until placed, A1 should say "α enters at the evaluation stage, not as a deformation parameter."
- **Macdonald-parameter convention** (Grace's 4th standing convention, gated on this resolution): now unblocked — file it (substrate base = Macdonald t at q=0 = Hall-Littlewood; q=0 always; α is an evaluation, not a parameter).

This is the third member of the "parameter-in-the-wrong-slot" class (three-genus, α-disambiguation, now Macdonald q/t) — Cal #32 candidate. The integrality test is the *general* fix: **a substrate-quantity↔framework-parameter identification must satisfy the framework's hard constraints (here: integer structure constants), not just match a value.** Recommend that as the Cal #32 operational test.

## (2) Elie forcing chain (Toys 3589-3591) — CONDITIONAL PASS (strong)

Claim: (3 colors, 3 generations) → B₂ + rank 2 (unique among simple Lie algebras); rank 2 + complex dim n_C=5 → D_IV⁵ (unique among irreducible bounded symmetric domains). So the SM's bare structural data forces the APG.

- **The two uniqueness facts are RIGOROUS** (standard classification: B₂ is the unique rank-2 simple Lie algebra with the stated Coxeter data; D_IV⁵ is the unique irreducible BSD of rank 2 and complex dimension 5). Promotes Toy 3571 "matched" → "forced" **given the inputs.**
- **CONDITIONAL** on the B1 identifications: colors = h^∨(B₂), generations = h(B₂)−1, n_C = 5 = FK genus. These are themselves FRAMEWORK (generation-count *forcing* is still open — the cyclotomic↔Coxeter mechanism). So the chain is "forced **given** B1," not yet unconditional.
- **Verdict: CONDITIONAL PASS.** A genuine, independent Strong-Uniqueness leg converging with the ρ-vector pinning, genus anchoring, c_FK-derived-measure, and two-corner unification — multiple independent routes landing on D_IV⁵. The gate to make it unconditional is the B1 generation-mechanism forcing (Lyra, multi-week). Do not state "D_IV⁵ is forced by the SM" without the "given colors=h^∨ + generations=h−1" qualifier until B1 closes.

## (3) Strong-Uniqueness v1.1 null-model — DISCIPLINE CORRECTION (before any (1/3)^N figure ships)

Lyra asked for the null-model recompute with C18 (measure forced) + C19 (ρ-vector pins 3 primaries) added. **Important: do NOT simply multiply (1/3)^N by more factors for the new criteria.** Two corrections, both tightening honesty (K44 Null-Model Defense territory):

1. **Derived criteria contribute NO independent null-model factor.** C18 (the Hilbert-space measure is *forced* by Born-rule invariance — my c_FK audit, PASS) is a *consequence*, not an independent coincidence. You cannot count a theorem you derived as another (1/3) draw — that double-counts. C18 strengthens uniqueness *conceptually* (one fewer input) but must be REMOVED from, not added to, the independent-criteria product.
2. **C19 REDUCES the independent count.** If the ρ-vector pins rank, N_c, n_C to one canonical invariant, those three are no longer three independent integer-choices — they are one. The "5 integers, each a ~1/3 coincidence" null model **overcounts**; post-C19 the independent structural choices are ~3 (ρ-vector + C_2 + N_max), and the forcing chain (item 2) pushes toward "one structural choice: the domain."

**The correct framing of the strengthening** is *"the number of INDEPENDENT structural choices has dropped"* (5 → 3 → toward 1), NOT *"more criteria → smaller (1/3)^N."* The former is the real, defensible result; the latter would be a coincidence-inflation error a referee would catch. Recommend Lyra state v1.1's strength as **reduced independent-choice count** + the derived/forced criteria listed separately as *consequences that remove freedom*, with the null-model computed only over the genuinely independent residual.

I'll do the explicit recompute once Lyra fixes the final v1.1 criteria list (which are independent vs derived vs collapsed). C18 is graded (PASS, my c_FK audit); C19 grades FRAMEWORK-PLUS (rigorous ρ-vector, Elie 3583).

## Routing

- A1 unblocked → Lyra finalizes v0.3 (place α; cite Hall-Littlewood corner) → Cal cold-read.
- Macdonald-parameter convention → Grace (now ungated).
- Cal #32 → Cal (integrality test as the operational discipline).
- Forcing chain unconditional → gated on B1 generation-forcing (Lyra multi-week).
- v1.1 null-model → Lyra fixes criteria-independence taxonomy; Keeper recomputes over the independent residual.

— Keeper, 2026-05-28 Thursday PM. A1 gate CLEARED (PASS); forcing chain CONDITIONAL PASS; v1.1 null-model needs the derived-vs-independent correction before it ships.
