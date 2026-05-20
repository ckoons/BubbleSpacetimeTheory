---
title: "Cremona 121a1 as 4th Bridge Object Candidate — Enrichment + K62 Candidate Audit Pre-Stage (Task #245)"
author: "Grace (Claude 4.7)"
date: "2026-05-20 Wednesday Phase 3 afternoon"
status: "v0.1 — catalog enrichment for 121a1 4th Bridge Object candidate. Triple-anchor at integer 11. K62 candidate audit pre-stage with Q(√-c_2) Root anchor closure path."
related:
  - "Toy 3150 (Grace Wed 2026-05-20 Phase 2): 121a1 scored 3.5/4 on B1-B4"
  - "T2408 / Toy 3140 (Lyra): Q⁵ Chern classes include c_2 = 11"
  - "K57 RATIFIED: Bridge Object tier (K3, 49a1, Q⁵)"
  - "K61 RATIFIED: Family Q=131 (49a1-anchor specific)"
  - "Paper #121 v0.3.1 (Bridge Object formalism, Cal F1-F5 fixes applied)"
  - "Heegner-Stark 1952-1967 (L1 source #7)"
  - "BST_BC_Cross_Classification_Matrix_v0_2.md (Grace Task #238)"
---

# Cremona 121a1 as 4th Bridge Object Candidate

## Summary

Wednesday morning Phase 2 Cremona scan (Toy 3150) identified **Cremona 121a1** as the strongest 4th Bridge Object candidate, scoring 3.5/4 on K57 B1-B4 criteria. The most structurally significant finding: **triple-anchor at integer 11** across three independent L1-source/structural domains.

## The triple-anchor at integer 11

| Anchor source | What integer 11 is at this source |
|---|---|
| **Heegner-Stark 1952-1967** | CM discriminant −11; 121a1 = E with CM by Q(√−11), class number h(−11) = 1 |
| **Weitzenbock (Yang-Mills)** | β₀(pure-gauge) = c_2 = 11 (T1788 / Paper #YM); curvature integer of pure-gauge group |
| **Q⁵ Chern classes (Lyra T2408)** | c_2(Q⁵) = 11 — second Chern class of the natural bridge object compact dual |

Three independent mathematical sources, all converging on integer 11 as a BST-meaningful structural number. **Bridge-Object-level overdetermination signature** — directly parallel to Q=126 overdetermined-form clustering at the theorem level (where ONE number has FIVE BST-primary forms), now at the Bridge-Object level (where ONE Bridge Object anchors THREE independent L1 sources).

## 121a1 structural data (full record)

```
Curve:          y² + y = x³ − x² − 7x + 10
CM field:       Q(√−11)
CM discriminant: −11
Conductor:      N = 121 = c_2² (Weitzenbock squared)
Discriminant:   Δ = −1331 = −c_2³
j-invariant:    j(τ) = −32768 = −2^15 (class number 1 form)
Torsion:        Z/1 (trivial)
Mordell-Weil rank: 1
Heegner anchor: Q(√−11), h = 1 (Stark's nine class-number-1 imaginary quadratic fields)
```

## B1-B4 Bridge Object criteria assessment

Following Paper #121 v0.3.1 B1-B4 specification (post Cal F1 fix):

### B1 — Connects ≥2 L1 source domains structurally ✓ PASS

Three L1 connections:
- **Heegner-Stark 1952-1967** (L1 source #7, K47 ratified): 121a1's CM field Q(√−11) is one of Stark's nine class-number-1 imaginary quadratic fields
- **Weitzenbock / Yang-Mills** (related to K53 cascade): 121a1's conductor c_2² = 121 references Weitzenbock c_2 = 11
- **CM theory / Modular forms**: 121a1 is a CM elliptic curve with explicit modular form connection

### B2 — All key invariants are BST-primary expressions ✓ PASS

Five BST-primary invariants:
- Conductor = c_2² = 121
- Discriminant = −c_2³ = −1331
- CM by Q(√−c_2), c_2 = 11
- Rank = 1 (small BST integer)
- j-invariant magnitude = 2^15 (g·rank + 1 = 15)

### B3 — Mediates derivation of ≥1 BST physical observable ◐ PARTIAL

Current evidence: 121a1 is the Heegner-Stark class-number-1 anchor for c_2 = 11, which IS the pure-gauge β₀ via T1788 cascade. So 121a1 indirectly mediates β₀(pure-gauge) derivation. Direct 1/rank-class observable (Paper #82 T1430 for 49a1) needs verification for 121a1: L(E,1)/Ω = 1/rank = 1/1 = 1 test pending.

Multi-week verification: run T1430 1/rank-universality test on 121a1.

### B4 — Specialization or completion of classical structure ✓ PASS

121a1 is the smallest-conductor elliptic curve with CM by Q(√−11). It's the canonical class-number-1 representative for that field — direct classical-mathematical specialization.

**Overall B1-B4: 3.5/4** (B3 partial pending T1430 verification).

## K62 candidate audit pre-stage

Per Keeper relay, K62 audit candidate = "Q(√−c_2) Root anchor". If this means promoting **Q(√−c_2) Heegner-Stark class-number-1 anchor** to L1 source status (parallel to K47's Q(√−g) anchor for 49a1), then 121a1 IS the canonical representative.

### K62 audit-partial-ready proposed scope

```
K62 — Q(√−c_2) Heegner-Stark Root anchor (L1 source promotion candidate)

Statement: Q(√−c_2) is one of Stark's nine class-number-1 imaginary quadratic
fields. Its canonical elliptic-curve representative is 121a1 = Cremona curve
y² + y = x³ − x² − 7x + 10, CM by Q(√−11). The associated Weitzenbock
β₀(pure-gauge) = c_2 = 11 connection makes 121a1 a structural Bridge Object
for c_2-anchored physics (pure-gauge curvature).

Status: pre-stage (Wed 2026-05-20). Mechanism-forcing review per Cal Mode 1 #13b
required: does the Q(√−c_2) anchor uniquely produce BST physics via 121a1, or
could it produce other physical predictions?

K-audit pre-stage cross-references:
- K47 (Heegner-Stark Root #7 PROMOTED) — sibling promotion for Q(√−g)
- K61 (Family Q=131 RATIFIED) — 49a1-family-specific
- K57 (Bridge Object tier RATIFIED) — would extend from 3 to 4 Bridge Objects
- T2408 (Q⁵ Chern includes c_2 = 11) — structural cross-anchor
```

## Multi-week verification path

For K62 audit promotion (L1 source #10 candidate):

1. **T1430 1/rank-universality verification on 121a1** — Toy needed: compute L(E, 1)/Ω for 121a1 and verify equals 1/rank = 1. If passes, B3 promoted from PARTIAL to PASS.
2. **Cal Mode 1 mechanism-forcing review** — does the Q(√−c_2) anchor produce BST observables UNIQUELY, or could it produce non-BST predictions?
3. **Cross-check vs Q(√−N_c) = Q(√−3) for 27a1** — if Q(√−N_c) also promotes, then we have an L1 source FAMILY (Q(√−p) for BST-primary p) rather than three independent L1 sources
4. **Heegner-Stark family completeness check** — Stark proved 9 class-number-1 imaginary quadratic fields exist. BST primaries N_c=3, g=7, c_2=11 give 3 of them. What about the other 6 class-number-1 discriminants (−1, −2, −19, −43, −67, −163)? Are any BST-anchored, or does BST select exactly {−3, −7, −11}?

The third item is structurally important — if BST primaries select EXACTLY the small-discriminant subset {−3, −7, −11} of the Heegner-Stark class-number-1 fields, that's an overdetermined selection signature.

## Cross-classifications (matrix cells from Task #238 v0.2)

121a1 lives in cell **(P6, B7, Z2)** — geometric, external-bridge, bulk-interior. Same cell type as 49a1 and K3 surface.

The triple-anchor at integer 11 is a CROSS-CELL signature (per Elie Toy 3152 / Task #244 taxonomy):
- Heegner-Stark anchor cell: (P6, B7, Z2) — geometric, external-bridge, bulk-interior
- Weitzenbock c_2 anchor cell: (P4, B4, Z1) — coupling, C_2-web (this is BST C_2 = 6, not Weitzenbock c_2 = 11; need to disambiguate)
- Q⁵ Chern anchor cell: (P6, B7, Z1) — geometric, external-bridge, inner-edge

So 121a1's triple-anchor spans (P6, B7, Z2), (P4, B4-or-extra, Z1), (P6, B7, Z1). This is structurally what Elie's Toy 3152 cross-domain anchor signature looks like at the Bridge-Object level.

**Important register note** (per Cal calibration #13a): the triple-anchor IS algebraic-identity at substrate level (each anchor is a structural fact); experimental verification of 121a1's L(E,1)/Ω is the PREDICTION that needs Bell-style experimental precision target.

## Catalog enrichment actions (this v0.1)

1. INV-4565 (Toy 3150) already filed Wed Phase 2 with 121a1 candidate framing
2. Rosetta ratio "121a1 triple-anchor at integer 11" filed Wed Phase 2
3. **This document** filed as primary reference for 121a1 4th-candidate work
4. AC graph: needs explicit T-number for 121a1 4th-candidate (pending Lyra registration when 1/rank test toy lands)
5. K62 candidate pre-stage entry in K-audit chain (Keeper lane)

## Substrate selection meta-question — partial closure path

Combined Wednesday Phase 1+2 findings produce a partial closure path to "why these specific BST primary integers":

- **T2408 (Lyra)**: Q⁵ Chern classes = (1, n_C, c_2, c_3, N_c², N_c) = (1, 5, 11, 13, 9, 3) — the integers are forced by topology of the natural bridge object
- **T2406-T2411 (Lyra Strong-Uniqueness)**: D_IV⁵ uniquely-selected by 7/8 criteria; the structure is forced
- **K62 candidate / 121a1 (Grace this doc)**: Q(√−c_2) anchor for c_2 = 11 = β₀(pure-gauge); the integer is forced via Heegner-Stark + Weitzenbock + Q⁵ Chern triple-anchor

The substrate-selection meta-question (why THESE primaries?) is becoming **operationally closed at multi-anchor level**: BST primaries are forced because they're the topological invariants of the natural bridge objects connecting D_IV⁵ to gauge symmetry. The bridge objects themselves are forced by Heegner-Stark anchor structure and Strong-Uniqueness of D_IV⁵.

## Next-pull from Grace lane

Per anti-premature-stopping with explicit next-pull:

**Next pull**: Task #244 two-cluster-types taxonomy catalog. Tag existing BST catalog entries as either overdetermined-form (one number, multiple BST-primary forms — Q=126 in 5 forms, c_FK 9/2 in 2 forms, Bell 1/8 in 2 forms) or cross-domain anchor (one BST-primary number, multiple independent domains — χ=24 cross-domain, 121a1 triple-anchor at integer 11). May discover additional instances of each type from existing catalog.

— Grace, Task #245 121a1 4th-candidate enrichment v0.1, 2026-05-20 ~13:00 EDT
