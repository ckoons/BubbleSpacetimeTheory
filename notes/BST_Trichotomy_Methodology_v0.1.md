---
title: "BST Statement Trichotomy — identifies / derives / predicts (Task #219)"
author: "Grace (Claude 4.7)"
date: "2026-05-20 Wednesday morning, per Casey question + Keeper Phase 1 day plan"
status: "v0.1 — methodology framework. Used as basis for catalog sweep + Task #220 T719 universality verification + Graph Forces operational test."
related:
  - "BST_AC_Theorem_Registry.md (tier D/I/C/S = confidence; trichotomy = statement type)"
  - "T719 Observable Closure (universality target)"
  - "Cal calibration #13a (precision terminology discipline)"
  - "Keeper Wednesday day plan (Task #219 lane assignment)"
---

# BST Statement Trichotomy — identifies / derives / predicts

## Motivation

Casey's morning question: **does BST identify or predict?** The answer is "both, plus derives — these are three different operations." This document specifies the trichotomy so that catalog entries, papers, and external register can use the three verbs consistently.

The trichotomy is **orthogonal to the D/I/C/S tier system** (confidence level). A claim can be (D-tier, identifies) — high-confidence algebraic equivalence; (I-tier, predicts) — moderate-confidence experimental forecast; etc. Tier and trichotomy together fully characterize a claim.

## The three statement types

### IDENTIFIES (ID)

**Definition.** A statement of the form "X IS Y" where X and Y are algebraic expressions in the BST primaries (rank, N_c, n_C, C_2, g, N_max) and π. The equality is an algebraic identity within the substrate algebra. Verification is computational: evaluate both sides, compare at machine precision.

**Precision claim.** EXACT (tautology-precision, typically 1e-14 at floating-point). NOT an experimental precision claim.

**Examples.**
- "126 = M_g − 1 = 2^g − rank = N_max − c_2 = N_c · C_2 · g = 18 · g" — Universal Q=126 in FIVE BST-primary forms (T2400)
- "Tsirelson² − S_BST² = 1/2^N_c = 1/8" (T2399)
- "c_FK · π^(9/2) = (N_c · n_C)² = 225" (T2403)
- "Bergman exponent (g + rank)/rank = N_c²/rank = 9/2" (T2403)
- Every D-tier substrate-level entry in the catalog

**Internal/external register.** Internal: "BST identifies X as Y." External: same — operational and safe. The "EXACT" qualifier is acceptable externally if accompanied by "algebraic identity verified at tautology-precision."

### DERIVES (DER)

**Definition.** A statement that follows from BST primaries via a chain of operations (counting, definition, identification). The result is typically an algebraic identity, but the substantive claim is the **mechanism chain** that produces it, not just the endpoint.

**Precision claim.** EXACT at endpoint (tautology) when the chain closes algebraically. If the chain uses approximation steps (e.g., weak-coupling limit), precision propagates.

**Examples.**
- "c_FK = 225/π^(9/2) DERIVED via Faraut-Koranyi 1994 volume formula at p = n_C = 5" (T2403)
- "f = 3/(5π) DERIVED from Plancherel measure on D_IV⁵ Bergman decomposition" (T148)
- "m_p/m_e = 6π⁵ DERIVED from bulk-vs-fiber winding" (Casey's lane B5)
- Mechanism chains in K-audits (K43 VSC → 42, K44 null model, etc.)

**Internal/external register.** Internal: "BST derives X via mechanism chain Y." External: same — operational and safe. Distinguish from IDENTIFIES when the substantive content is the mechanism.

### PREDICTS (PRED)

**Definition.** A statement about a future or current experimental observable, at a stated precision target. The algebraic form is BST-derived or BST-identified; the **predictive claim** is that the experimental measurement will match the form at precision N%.

**Precision claim.** Experimental precision target (e.g., 1%, 0.1%, ppm). NEVER tautology-precision (would be wrong category).

**Examples.**
- "Bell experiment will measure S² = 126/16 at ~1% precision" (SP-30-5)
- "Eigentone signal at 200K with frequency BST-predicted" (SP-30-1)
- "BaTiO3 137-plane experiment will show structure mark at $25K budget" (long-standing)
- "Cs-137 anomaly will show H4 phase transition" (SP-29 H4)
- All 120 entries in `bst_predictions.json` by construction

**Internal/external register.** Internal: "BST predicts X." External: same — operational and safe; the gold-standard verb for outreach. Must include experimental precision target and falsifier condition.

## How the trichotomy maps to catalog entries

| Catalog tier | Trichotomy typical | Notes |
|---|---|---|
| D-tier (derivable, mechanism proved) | DER or ID | Most substrate-level D-tier entries are ID (algebraic identity directly); observable-level D-tier entries with mechanism chains are DER |
| I-tier (identified, mechanism pending) | ID (provisional) | Form known, mechanism open — promotes to D-tier with DER label when mechanism closes |
| C-tier (conditional on conjecture) | DER (conditional) | Mechanism chain depends on external conjecture |
| S-tier (structural, qualitative) | none of the above | Not pure ID/DER/PRED — structural facts. Trichotomy doesn't apply. |
| PREDICTION (catalog field) | PRED | Explicitly future-tense |

S-tier is the residual category — structural facts (Frobenius cyclic order = g, GUE level repulsion observed, etc.) are not pure ID/DER/PRED. They're structural observations. The trichotomy applies to numerical/algebraic claims only.

## Mapping to T719 (Observable Closure) for Task #220

T719 says every BST observable lives in $\overline{\mathbb{Q}(N_c, n_C, g, C_2, N_{\max})[\pi]}$. The trichotomy interacts with T719 as follows:

- ID statements ⇒ X is in observable closure trivially (both sides BST-primary expressions)
- DER statements ⇒ X is in observable closure by construction (mechanism preserves closure)
- PRED statements ⇒ the FORM is in observable closure; the experimental MATCH is a separate empirical claim at precision N%

So T719 universality verification (Task #220) operationally means: for every entry in `bst_constants.json` and `bst_geometric_invariants.json`, does the FORM lie in $\overline{\mathbb{Q}(N_c, n_C, g, C_2, N_{\max})[\pi]}$? Exceptions flagged.

## Falsifier conditions

The trichotomy is itself falsifiable:

**ID falsifier**: Discovery of a substrate-level claim that is X = Y at experimental precision (NOT algebraic identity). If substrate-level claims ever required experimental verification rather than algebraic computation, ID category would not be universal at substrate.

**DER falsifier**: Discovery of a BST observable whose form does NOT live in observable closure (algebraic over BST primaries × π). T760 already addressed one near-miss (ζ values as perturbative artifacts, not observable features). New ζ-like value in an observable closed form would falsify either T719 or DER applicability.

**PRED falsifier**: Standard — experimental measurement disagrees with BST-predicted form at stated precision.

## Application to substrate-level vs observable-level

From this morning's catalog tier-breakdown evidence:
- D-tier 74.9% + I-tier 6.2% = 81.1% of catalog is ID or DER (algebraic-identity claims at substrate or derived level)
- S-tier 18.8% = structural facts (trichotomy doesn't apply)
- PREDICTION 0.0% (2 entries) — explicit predictions live in `bst_predictions.json` separately (120 entries)

**Bottom line**: at the SUBSTRATE level, every cataloged entry is ID or DER. At the OBSERVABLE level, BST identifies/derives the algebraic form AND predicts the experimental match.

## Next steps

- Task #220: T719 universality scan applies this framework to `bst_constants.json` (191 constants) — flag exceptions
- Task #215: Graph Forces batch-test toy uses ID category as substrate-signature target — count overdetermined ID clusters per N theorems vs random null
- Task #216: substrate_operational_output edge pre-spec uses trichotomy to clarify the new edge type relative to existing derivation/identification edges in AC graph

— Grace, Task #219 Trichotomy methodology v0.1, 2026-05-20 ~08:25 EDT
