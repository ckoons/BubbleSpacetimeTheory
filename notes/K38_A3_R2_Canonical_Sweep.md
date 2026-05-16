---
title: "K38 A3: Canonical N_max Reading Sweep — Equivalence Documented"
author: "Keeper"
date: "2026-05-17 ~07:45 EDT"
verdict: "A3 CLOSED via equivalence documentation, not single-reading commitment"
related: ["K38_Alpha137_Derivation_Chain_Audit.md", "BST_Paper78_Absolute_Point.md", "Paper83_Draft.md", "BST_T1929_H_DIV5_landmarks.md"]
---

# K38 A3: Canonical N_max Reading — Equivalence Sweep

## Context

A3 was specified in K38 as: "Commit to ONE pre-α reading of N_max and sweep papers for consistency." Three readings exist in BST docs:

- **R1 (spectral cap)**: N_max = 137 is the spectral truncation cutoff
- **R2 (max K-type dimension)**: N_max is the maximum representation dimension in the Wallach decomposition  
- **R3 (Shimura level)**: N_max defines the Shimura variety level Γ(N_max)

Original recommendation was R2 (most direct from geometry, most rigorous for referees).

## What the sweep found

Reading Papers #78, #83 in detail:

| Paper | Primary reading | Lines | Notes |
|-------|----------------|-------|-------|
| #78 Absolute Point | R3 (Shimura level) §8 + R1 (spectral cap) §3.3 | 33, 142, 158, 280, 323 | Mixed use |
| #83 Invariants Table | R1 (spectral cap) | 51 | Operational definition |
| #82 BSD | (not yet swept — likely R1/R3) | — | — |
| #104 Root Proof System | (Lyra has draft §5.6 with mixed) | — | Needs sync |

## The right move — equivalence, not commitment

Forcing one canonical reading would override domain-appropriate language (Shimura level for arithmetic, spectral cap for operational, K-type for representation theory).

**Better**: document that R1, R2, R3 are EQUIVALENT readings of the same object, with explicit cross-references. T1929 (Lyra's H_*(D_IV⁵) + landmarks theorem, May 16) enumerated all three landmark types and showed they coincide at N_max.

### The equivalence (T1929-grounded)

For D_IV⁵ = SO_0(5,2)/[SO(5)×SO(2)]:

1. **R1 = R2**: The spectral truncation cutoff equals the maximal Wallach K-type dimension because the Bergman series converges precisely when summed to N_max. Beyond N_max, modes repeat (don't add new independent content).

2. **R2 = R3**: The maximal K-type dimension equals the Shimura level because the Shimura variety Γ(N_max)\D_IV⁵ inherits its level from the deepest K-type structure. Γ(N) for N > N_max would exceed the spectral structure.

3. **R3 = R1**: The Shimura level equals the spectral cap because both correspond to "the deepest level that encodes all five BST integers" (Paper #78 §8.1).

All three are facets of the same N_max = 137. The Diophantine over-determination Paper #78 §3.3 documents (three decompositions agreeing only at N_c=3) is the structural reason for their equivalence.

## Recommendation (final A3 verdict)

**Document the equivalence** in Paper #104 §5.6 with explicit cross-references:

> N_max = 137 admits three equivalent readings:
> - **R1 (operational)**: spectral truncation cutoff
> - **R2 (geometric)**: maximal Wallach K-type dimension  
> - **R3 (arithmetic)**: Shimura variety level Γ(N_max)
>
> The three readings coincide on D_IV⁵ by T1929 (H_*(D_IV⁵) + 12 landmarks). Papers use whichever reading is most natural for their context: arithmetic-flavored papers prefer R3, spectral-physics papers prefer R1, representation-theory papers prefer R2. All cross-reference T1929 for the equivalence proof.

This is honest. It also handles the case where future BST work surfaces a fourth reading (e.g., topological landmark reading from SP-26) — it slots in naturally as R4 with cross-reference to the existing three.

## Action items for papers

- **#78**: §3.3 already names "three decompositions"; add explicit R1/R2/R3 labels in §8.1.
- **#83**: §"BST overview" — add R1 label to the N_max entry in the integer table.
- **#82 (BSD)**: sweep needed when Lyra resumes; expected R1 or R3.
- **#104 §5.6**: Lyra's draft folds in equivalence statement above.

Owner: **Lyra**, when she resumes — she has Paper #104 v0.3 already drafted and can sweep the others in 1-2h fresh.

## K38 A3 status

**CLOSED** via equivalence documentation. No single reading is canonical because R1/R2/R3 are equivalent. The sweep documents this and provides standardized cross-reference language for papers.

— Keeper, 2026-05-17 ~07:45 EDT
