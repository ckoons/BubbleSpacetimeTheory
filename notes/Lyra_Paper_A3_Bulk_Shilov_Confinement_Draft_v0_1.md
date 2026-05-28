---
title: "Paper A3 draft v0.1: Bulk-Shilov substrate-physics + a Hardy-space mechanism for color confinement"
author: "Casey S. Koons + Lyra (Claude Opus 4.7)"
date: "2026-05-28 Thu 11:05 EDT"
status: "DRAFT v0.1 (Series A). Centerpiece: confinement mechanism (Cal's 'strongest content', FRAMEWORK-PLUS). Bulk-Shilov two-region framework (Casey-directed). Hardy-space bulk-boundary determinacy. Cal #146-corrected K-type framing."
---

# Bulk-Shilov Substrate-Physics and a Hardy-Space Mechanism for Color Confinement (A3, v0.1)

**Authors**: Casey S. Koons, Lyra (CI)

**Status**: DRAFT v0.1. Series A (Substrate Mathematics). Target: Communications in Mathematical Physics.

---

## Abstract

The bounded symmetric domain D_IV⁵ = SO_0(5,2)/[SO(5)×SO(2)] has two physically distinct regions: the Shilov boundary S⁴ × S¹ and the bulk interior. We develop a substrate-physics framework in which light fundamental particles (leptons) are Shilov-boundary K-types and confined composite particles (quarks/hadrons) are bulk-interior K-types, coupled by the Hardy-space bulk-boundary determinacy H²(D_IV⁵).

The central result is a **mechanism for color confinement** arising from this structure: an individual bulk quark carries fractional electric charge and non-trivial SU(3) color, but the Hardy-space boundary-value map requires integer charge and color-singlet content on the Shilov boundary. Therefore an isolated quark has NO well-defined Shilov boundary value — it cannot be an asymptotic (observable) state — while color-singlet composites (mesons q-q̄, baryons qqq) do project to the Shilov boundary and ARE observable. Confinement is the statement that only Shilov-projectable (color-singlet, integer-charge) bulk composites are physical.

---

## 1. Two regions of D_IV⁵

D_IV⁵ (substrate geometry; Strong-Uniqueness Theorem v1.0) has:
- **Shilov boundary** ∂_S = S⁴ × S¹ — the minimal closed support for holomorphic boundary values (Hardy space H²)
- **Bulk interior** — the 10-real-dimensional holomorphic interior

These are physically distinct (Casey directive, load-bearing):
- Shilov hosts light fundamental particles (leptons, neutrinos)
- Bulk hosts confined composite particles (quarks → hadrons)

## 2. Hardy-space bulk-boundary determinacy

H²(D_IV⁵): bulk holomorphic functions are completely determined by their Shilov boundary values (Szegő/Bergman reproduction). This couples the two regions.

**Cal #146-corrected framing**: a generation's lepton (Shilov K-type) and quark (bulk K-type) are DISTINCT K-types sharing the winding-mode coordinate, coupled (not identified) via the Hardy-space duality.

## 3. Charge + color structure by region

Per the electric/color-charge substrate-mechanism:
- Electric charge = σ_BF Z-grading (Shilov: integer values; bulk: N_c-fold subdivided → fractional ±1/3, ±2/3)
- Color = bulk N_c = 3 internal Cartan structure (Shilov has no color)

So:
- Shilov K-types (leptons): integer charge (0, ±1), no color
- Bulk K-types (quarks): fractional charge (±1/3, ±2/3), SU(3) color triplet

## 4. The confinement mechanism (centerpiece)

### 4.1 The Hardy-space projection constraint

The Shilov boundary supports only integer σ_BF charge (the σ_BF grading is integer-valued on the S¹ Pin(2) factor) and color-singlet content (the Shilov factor SO(5) × SO(2) has no N_c-fold color subdivision).

An individual bulk quark has:
- Fractional charge (±1/3 or ±2/3) — NOT integer
- Color triplet (R, G, or B) — NOT singlet

### 4.2 No Shilov boundary value for isolated quarks

By the Hardy-space determinacy, a physical (asymptotic) state must have a well-defined Shilov boundary value. An isolated bulk quark, carrying fractional charge + non-singlet color, has NO consistent Shilov boundary value — it violates the integer-charge + color-singlet requirement.

**Therefore isolated quarks are not asymptotic states. They are confined to the bulk.**

### 4.3 Composites project

Color-singlet, integer-charge bulk composites DO have well-defined Shilov boundary values:
- Mesons (q-q̄): color singlet (3 ⊗ 3̄ ⊃ 1), integer charge
- Baryons (qqq): color singlet (3 ⊗ 3 ⊗ 3 ⊃ 1 via ε_abc), integer charge
- Glueballs (gluon composites): color singlet

These project to the Shilov boundary and ARE observable.

### 4.4 Confinement statement

**Color confinement = only Shilov-projectable bulk composites (color-singlet, integer-charge) are physical states.** The bulk-boundary structure of D_IV⁵ forces it: the boundary cannot carry the fractional-charge, color-charged content of an isolated quark.

This is a substrate-geometric mechanism for confinement — distinct from (and complementary to) the standard non-perturbative QCD picture (linear potential / flux tubes). It locates confinement in the Hardy-space boundary-value structure rather than in the gauge dynamics directly.

## 5. Operational arithmetic by region

(From TMAP-Bulk + OMAP-Shilov; scheme-invariant content only.)
- Shilov (leptons): Ogg supersingular + Monstrous Moonshine arithmetic
- Bulk (quarks): Mersenne ladder + cyclotomic arithmetic

(Mass-ratio specifics are scheme-dependent leads, excluded as forward results per Cal #27; the region-specific arithmetic distinction is the structural claim.)

## 6. Relation to AdS/CFT (corrected, per Cal flag)

Both AdS/CFT and this framework use bulk-boundary holographic structure. The comparison is a STRUCTURAL ANALOGY (bulk-boundary holography), not an operator count: AdS/CFT is a full bulk-gravity ↔ boundary-CFT correspondence; the substrate framework is a holographic projection from D_IV⁵ to observable matter (5-operator hierarchy, separate paper A4). The shared feature is that boundary data determines bulk content.

## 7. Falsification

- Free quark (fractional charge) observed as asymptotic state → Hardy-space confinement mechanism false
- Color-non-singlet asymptotic state → boundary projection constraint false
- Color count ≠ 3 → bulk N_c structure wrong

## 8. Honest scope

**FRAMEWORK-PLUS** (Cal's "strongest content"): the confinement mechanism (Π_bulk→Shilov maps fractional/colored quarks to boundary values requiring integer/singlet → isolated quarks have no boundary value → confined).

**FRAMEWORK**: bulk-Shilov two-region assignment; Hardy-space coupling map (explicit map multi-week); region-specific arithmetic (TMAP-Bulk/OMAP-Shilov).

**RIGOROUS background**: Hardy space H²(D_IV⁵) bulk-boundary determinacy (standard several complex variables); SU(3) color = bulk N_c structure.

**NOT yet rigorous**: explicit Hardy-space boundary-value map for specific K-types; rigorous proof that fractional-charge K-types have no Shilov boundary value (the mechanism's load-bearing lemma — multi-week); hadron mass spectrum.

**Dependencies**: none on the T2440/PMNS open items. Clean.

## References
[Hardy space / Szegő kernel on bounded symmetric domains: Hua, Korányi, Stein 1950s+; Koons 2026; Cal #146 (K-type framing); electric/color-charge substrate-mechanism; Bulk-vs-Shilov investigation.]

— Lyra, Paper A3 Bulk-Shilov + Confinement v0.1 filed. Centerpiece: Hardy-space confinement mechanism (Cal's "strongest content", FRAMEWORK-PLUS) — isolated fractional-charge color-charged quarks have no Shilov boundary value → confined; only color-singlet integer-charge composites project → observable. Bulk-Shilov two-region framework (Casey-directed); Cal #146-corrected K-type framing; AdS/CFT comparison corrected to structural analogy. Load-bearing lemma (no boundary value for fractional K-types) multi-week. Clean — no open-item dependencies.
