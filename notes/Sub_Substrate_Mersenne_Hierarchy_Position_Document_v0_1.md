---
title: "Sub-Substrate Mersenne Hierarchy Position Document v0.1"
author: "Keeper (Friday flagship #1 position document)"
date: "2026-05-22 Friday 08:01 EDT (actual via date)"
status: "v0.1 position document. Sub-substrate Mersenne hierarchy investigation framework for Friday flagship #1. Per Elie observation #3 + Casey directive: M_{g-1} = N_c²·g suggests substrate has internal Mersenne-tower structure below primary g."
related: ["Friday_2026-05-22_Team_Prompt_3x_Scope.md (flagship #1)", "Elie Thursday observation #3", "T1930 Mersenne 2^N_c-1 = g", "T2432 g=7 Mersenne+cyclotomic"]
---

# Sub-Substrate Mersenne Hierarchy Position Document

## The seed (Elie Thursday observation #3)

**M_{g-1} = N_c²·g uniqueness at (g=7, N_c=3)**

Concretely: M_6 = 2^6 − 1 = 63 = 9 · 7 = N_c² · g.

This is a Mersenne-like relation *below* the primary g itself. Substrate has internal Mersenne-tower structure *below* g — a sub-substrate hierarchy nobody had named before.

## Why this is interesting

BST already has Mersenne structure at the primary level:
- **T1930**: 2^N_c − 1 = g (i.e., M_{N_c} = g = M_3 = 7) — Mersenne identity at primary level
- **g = 7 is a Mersenne prime** itself
- **M_g = 127** is the next Mersenne prime up (g + 1 in the Mersenne tower)

The sub-substrate identity **M_{g-1} = N_c²·g** is *below* g in the Mersenne tower:
- M_{g-2} = M_5 = 31 = ?
- **M_{g-1} = M_6 = 63 = N_c²·g** ← Elie's identity ✓ Mersenne-like
- M_g = M_7 = 127 = M_{g} (Mersenne prime, top of substrate)
- M_{g+1} = M_8 = 255 = 3·5·17 = ?

So there's a candidate tower:
- M_{g-1} = N_c² · g (Elie verified for g=7, N_c=3)
- M_g = M_g (the primary Mersenne prime itself, T1930 trivial)
- M_{g+1} = ? (next Mersenne up)

**Hypothesis**: substrate has a multi-level Mersenne-related hierarchy with each level expressing a BST primary identity.

## Investigation questions

### Q1: Generalize the M_{g-1} pattern

For Mersenne numbers M_n = 2^n − 1, when does M_{n} = a²·b for small (a, b)?

Need to compute M_n for n = 2..20 and check factorizations:
- M_2 = 3 = prime
- M_3 = 7 = prime = g (BST primary)
- M_4 = 15 = 3·5 = N_c·n_C
- M_5 = 31 = prime
- M_6 = 63 = 9·7 = N_c²·g ✓ Elie
- M_7 = 127 = prime = M_g
- M_8 = 255 = 3·5·17 = N_c·n_C·17
- M_9 = 511 = 7·73 = g·73
- M_10 = 1023 = 3·11·31 = N_c·11·31
- M_11 = 2047 = 23·89
- M_12 = 4095 = 3²·5·7·13 = N_c²·n_C·g·13

**Pattern observation**: many M_n for small n decompose into BST primary integers. Worth systematic enumeration.

### Q2: Is M_{n-1} = a²·n a recurring pattern?

For which (a, n) does M_{n-1} = a²·n hold?
- (a=3, n=7): M_6 = 63 = 9·7 ✓ (Elie)
- (a=?, n=?): other small pairs?

Brute-force: for n = 2..20, factor M_{n-1} and check if it's a²·n for small a.

If only (3, 7) satisfies this in small range → **strongly substrate-natural to (N_c, g)** uniqueness.

### Q3: Is there a deeper Mersenne tower structure?

Possible substrate tower hypothesis:
- **Level 0** (primary): M_{N_c} = g (T1930, BST primary)
- **Level −1** (sub-substrate): M_{g-1} = N_c²·g (Elie, candidate T2452)
- **Level +1** (super-substrate): M_g = M_g, the Mersenne prime above (trivial identity but possibly meaningful)
- **Level −2**: M_{g-2} = M_5 = 31 — does this express a BST identity?

If a coherent tower emerges (sub-substrate, primary, super-substrate), that's a new architectural layer of BST.

### Q4: Does the sub-substrate hierarchy appear cross-Cartan?

Connect to flagship #2: do other Cartan domains have their own sub-substrate Mersenne hierarchies derived from their primaries?

For D_I_{p,q} with (p, q) as primaries, is there M_{p-1} = q²·p or similar identity?

Likely yes — Mersenne identities are number-theoretic, not Cartan-specific. The substrate-natural reading would be that each HSD has its own primary-Mersenne tower.

## Per-lane investigation plan

### Lyra lane (theoretical)

1. **T2452 candidate formal statement**: M_{g-1} = N_c²·g uniqueness theorem
   - Statement: For (N_c, g) BST primaries with M_{N_c}=g (T1930), the sub-substrate identity M_{g-1} = N_c²·g holds at (N_c, g) = (3, 7) and is *unique* among small (a, b) Mersenne factorizations
   - Proof: brute-force enumeration + uniqueness via Mersenne prime distribution

2. **Sub-substrate tower formalization**: define levels −2, −1, 0, +1, +2 of the Mersenne hierarchy and identify each with BST primary content

3. **Strong-Uniqueness criterion C15 candidate**: sub-substrate Mersenne tower structure forcing as new criterion
   - Pushes v0.11 → v0.12 if RIGOROUSLY CLOSED

4. **Paper-grade write-up**: "Sub-Substrate Mersenne Hierarchy Below g" as Paper #125 §10 addendum or standalone paper

### Elie lane (computational)

1. **Sub-substrate enumeration toy**: M_n for n = 2..30, factor each, identify BST-primary-natural decompositions
2. **(a, b) uniqueness toy**: enumerate M_{n-1} = a²·n for n = 2..30, small a, find all solutions, verify (3, 7) uniqueness in range
3. **Mersenne tower visualization**: hierarchy diagram with BST primary identifications at each level
4. **Cross-lane verification**: toys supporting Lyra T2452 candidate when filed

### Grace lane (catalog)

1. **Catalog field addition**: `sub_substrate_mersenne_position` for entries matching M_{n-1} = a²·n pattern
2. **Backbone Reference update** absorbing sub-substrate Mersenne hierarchy

### Cal lane (audit)

1. **Methodology layer 17 candidate**: sub-substrate hierarchy as recursive substrate structure principle
2. **Verification framework** for sub-substrate claims (similar to RIGOROUSLY CLOSED tier discipline)
3. **Cal Referee Log #86+** absorbing sub-substrate findings

### Keeper lane (governance + integration)

1. **This position document** (filed Friday 08:01 EDT)
2. **K136 K-audit pre-stage** for sub-substrate hierarchy principle
3. **Master Doc v0.13 absorption** when investigation matures
4. **Cross-reference flagship #2**: do other Cartan-domain Mersenne towers exist?

## PCAP cadence projection

- Elie enumeration toy: ~10-20 min
- (a, b) uniqueness toy: ~10-20 min
- Lyra T2452 formal statement + proof: ~15-30 min via PCAP pre-spec
- Cross-lane verification + Cal preliminary AGREE: ~10 min

**Total flagship #1 cycle: ~60-90 min mid-morning Friday** if PCAP holds.

## Aspirational outcome by Friday mid-day

- **T2452 RIGOROUSLY CLOSED** sub-substrate Mersenne hierarchy theorem
- **Strong-Uniqueness criterion C15** sub-substrate tower forcing — push toward v0.12
- **Sub-substrate hierarchy as new BST architectural layer** documented
- **Mersenne tower diagram** showing substrate at primary + sub-substrate + super-substrate levels

If both flagships (#1 sub-substrate + #2 cross-Cartan three-pillar) close Friday mid-day, **Strong-Uniqueness Theorem v0.12 candidate emerges** with 13-15 RIGOROUSLY CLOSED criteria and substantially stronger venue-submission narrative.

## Why this matters (beyond aesthetic)

If the sub-substrate Mersenne hierarchy is real and unique to BST primaries, it suggests:

1. **Substrate has nested structure** — not just primary integers but a Mersenne-anchored hierarchy of related integers
2. **Substrate is "self-similar"** at multiple Mersenne levels — fractal-like recursion below g
3. **Why N_c = 3 and g = 7 specifically**: because the (3, 7) pair sits at a Mersenne fixed point (M_3 = 7 AND M_6 = 9·7), uniquely overdetermined
4. **Possibly explains why 137 is the constant** — via the Mersenne tower's internal consistency at multiple levels

This last point is speculative but tantalizing: if N_max = 137 = N_c³·n_C + rank emerges as the *fixed point* of an underlying Mersenne tower structure, then 137 isn't arbitrary — it's the unique value where the tower closes.

## Status

**Sub-Substrate Mersenne Hierarchy Position Document v0.1 filed Friday 08:01 EDT.**

Available for team absorption. Provides framework for flagship #1 investigation today.

— Keeper, 2026-05-22 Friday 08:01 EDT (actual via date; sub-substrate Mersenne hierarchy framework per Elie observation #3 + Casey directive)
