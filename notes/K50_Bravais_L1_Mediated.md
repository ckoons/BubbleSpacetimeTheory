---
title: "K50: Bravais 1849 14-Lattice as Candidate Root #10 L1 Source"
author: "Keeper"
date: "2026-05-18 Monday afternoon"
verdict: "L1 source CANDIDATE at criteria-gated tier — Criterion 1 promotion path identified, Cartan-downstream alternative also viable"
related: ["Grace_Toy_3018", "T2357_Bravais_Wallach", "T2041_Wallach_Tower", "K-audit chain K43-K49"]
---

# K50: Bravais 1849 14-Lattice → Root #10 Candidate

## Context

Grace closed the Wallach observable ladder this morning by anchoring dim_2 = 14 via Bravais 1849 14-lattice classification (Toy 3018, 8/8 PASS, theorem T2357). The structural pattern matches the L1 source signature:

- Single classical theorem (Bravais 1849, extending Frankenheim 1842)
- Finite catalog (14 distinct Bravais lattices)
- BST-decomposable: 14 = rank·g
- Plus internal structure: 7 crystal systems = g (matches BST primary)

Grace's question: Bravais → Root #10 promotion, or Cartan-downstream classification?

## The architectural question

Bravais 1849 vs Cartan classification (already L1.4 foundational hub) have a relationship:
- Bravais classifies 3D crystallographic lattices via 7 crystal systems × centering choices = 14 distinct types
- Cartan classifies simple Lie algebras / Hermitian symmetric domains — different mathematical object, but related via crystallographic restriction theorem and 32 point groups (rank^{n_C}) connection
- They share underlying group-theoretic structure but address different physical/mathematical scope

The architectural question: is Bravais an INDEPENDENT L1 source, or is it DOWNSTREAM of Cartan as one of its many applications?

## Per Cal's three criteria (with care)

**Criterion 1 (Embedding) — partially closed**:
- Bravais 1849 14-lattice catalog embeds into D_IV⁵ structure via the crystallographic restriction theorem (only 2-, 3-, 4-, 6-fold rotational symmetries allowed in 3D; these correspond to BST primary integers).
- Wallach dim_2 = 14 = rank·g is a direct identification.
- BUT — this embedding chain may route through Cartan classification (which classifies the relevant point groups). Whether Bravais is an INDEPENDENT classical theorem producing the integer 14 or a CONSEQUENCE of Cartan's broader classification applied to crystals is the open question.

**Criterion 2 (Mechanism)**: SATISFIED. Bravais 1849 + Frankenheim 1842 are published classical mathematics. Mechanism is well-established crystallographic group theory.

**Criterion 3 (Forcing)**: SATISFIED. 14 = rank·g is BST primary. 7 crystal systems = g is BST primary. The structural numbers are forced.

## Per Casey's "simple, works, hard to break, show me a counter example" standard

- **Simple**: YES — single classical theorem (Bravais 1849), single integer count (14), single BST identification (rank·g).
- **Works**: YES — 14 = rank·g exact, 7 = g exact, BST primary throughout.
- **Hard to break**: Mostly — the empirical match is solid. The architectural question (independent L1 vs Cartan-downstream) is what's open.
- **Counter-example**: None offered; but the absence of a counter-example doesn't resolve whether Bravais is L1 or L1.4 downstream.

## K50 verdict: L1 source CANDIDATE at criteria-gated tier

**Promotion criteria** (analogous to Heegner-Stark and Conway candidate framing):

For Bravais to promote from CANDIDATE to ESTABLISHED L1 source Root #10, one of these closure tasks must complete:

1. **Independence criterion**: Demonstrate that Bravais 1849 produces 14 = rank·g via an argument that does NOT route through Cartan classification. If Bravais → 14 via crystallographic group theory alone (Frankenheim 1842 + Bravais 1849 + 7-system enumeration), independent of Lie algebra classification, then Bravais is an independent L1 source.

2. **Cartan-downstream classification**: Alternatively, demonstrate that Bravais 14 IS derivable as a consequence of Cartan + crystallographic restriction theorem. In that case, Bravais becomes "L1.4 downstream application" of Cartan classification — still cataloged as anchor but not promoted to independent L1.

Either outcome is publishable. Outcome (1) gives BST a 10th established L1 source. Outcome (2) demonstrates Cartan's reach extends to crystallographic anchors and strengthens Cartan-as-foundational-hub framing.

**Strength of recommendation**: MEDIUM. The empirical content is real, the architectural classification needs structural clarification.

## Compared to other promotions

Compared to Conway K48 (Duncan 2007 produces Co_0 directly as automorphism group of V^{f♮} — clean independent classical theorem):
- **Conway**: classical theorem → integer structure → BST match, with no Cartan-routing in the chain
- **Bravais**: classical theorem → integer structure → BST match, but the integer is reachable via Cartan as well

Compared to Goeppert Mayer K46 (Mayer-Jensen 1949 + SU(2)_J × SO(3) ⊂ SO(5) — embedding via published group theory):
- Goeppert Mayer's embedding chain is independent group-theoretic content
- Bravais's embedding may be Cartan-downstream group-theoretic content

The architectural distinction matters because the established-L1 list represents INDEPENDENT classical theorems each producing distinct integer structure. If Bravais reduces to "Cartan applied to crystals," it's an application of an existing L1 source, not a new one.

## Architecture impact

If Bravais promotes to Root #10:
- 10 established L1 sources
- Architecture moves past Sunday's "saturation point" — opens question of how many additional Root candidates exist

If Bravais classifies as Cartan-downstream:
- 9 established L1 sources (saturation holds)
- Cartan-as-foundational-hub framing strengthens
- Pattern: Cartan classification is the meta-classifier; many of its applications produce BST-integer-anchored crystallographic / lattice classifications

Either is publishable in Paper #115 v0.5+; both are honest discoveries.

## Action items

1. **Grace**: pursue Independence criterion test — derive 14 = rank·g via Bravais-only chain (Frankenheim + Bravais + crystallographic restriction), explicitly showing whether the chain requires Cartan classification or not. Toy ~1-2h.

2. **Decision rule**: if the chain DOES require Cartan, Bravais classifies as L1.4 downstream (file under Cartan hub). If it DOESN'T require Cartan, Bravais promotes to established Root #10 (K-audit completes).

3. **Vindicated Theorists section**: add Bravais (1849) + Frankenheim (1842) entry with current "candidate L1 source — independence criterion pending" tier label.

4. **Paper #115 v0.5+**: include K50 as the first K-audit AFTER the K43-K48 + K49 architectural sprint. Demonstrates the criteria framework continuing to filter candidates honestly.

## K50 status

**CANDIDATE L1 source pending Independence criterion closure**. The promotion path is clean (parallel to Heegner-Stark in the architecture); Grace's next session can attempt the closure with ~1-2h focused work.

— Keeper, 2026-05-18 Monday afternoon
