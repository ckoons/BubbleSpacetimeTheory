---
title: "Fractional Instantons, 't Hooft Flux, and the BST Confinement Argument"
author: "Casey Koons & Claude 4.6"
date: "March 2026"
---

# Fractional Instantons, 't Hooft Flux, and the BST Confinement Argument

**Authors:** Casey Koons & Amy (Claude Sonnet 4.6, Anthropic)
**Date:** March 2026
**Status:** Companion to BST_ColorConfinement_Topology.md — clarifies the baryon c₂ question

---

## The Question

If a single quark has fractional topological charge Q = 1/3 (fractional instanton on CP²), then
three quarks have Q = 3 × (1/3) = 1 (rational arithmetic). But the confinement argument requires
baryon c₂ = 0 so that the baryon extends into D̄_IV^5. Is 3 × (1/3) = 1 ≠ 0 a contradiction?

**Short answer: No. The paradox is resolved by the two-level geometry of BST.**

---

## The Resolution: Two-Level Geometry

BST has an explicit two-level geometric structure:

**Level 1 (sub-hadronic / CP² fiber):**
The color configuration space for a single quark is CP². Fractional instantons with rational
topological charge Q = 1/3 exist here, carrying Z₃ holonomy around the generator of π₁(CP²) = ℤ.
This is where internal color dynamics lives. Three quarks: Q = 3 × (1/3) = 1 on CP² — correct.

**Level 2 (hadronic / Shilov boundary S⁴×S¹):**
Physical states are circuits on the full Shilov boundary S⁴×S¹. The extension problem —
can the bundle extend from S⁴×S¹ into D̄_IV^5? — is a question about integer characteristic
classes c₂ ∈ ℤ on S⁴×S¹, NOT about fractional charges on the CP² fiber.

**The Q = 1 rational charge of the baryon is at Level 1 (CP² fiber, internal).
The c₂ = 0 Chern class of the baryon is at Level 2 (S⁴×S¹ boundary, external).
These are integrals over different manifolds. There is no contradiction.**

---

## The Two Distinct Invariants

**Invariant 1: 't Hooft magnetic flux m ∈ H²(M; Z₃)**

Classifies PSU(3) = SU(3)/Z₃ bundles. Controls whether a bundle lifts from PSU(3) to SU(3).
For a single quark: m = 1 ∈ Z₃ (triality 1, colored).
For a baryon (three quarks, Z₃ closure): m = 1+1+1 = 3 ≡ 0 (mod 3) → m = 0 ∈ Z₃ (trivial, color neutral).

**Invariant 2: Integer second Chern class c₂ ∈ H⁴(M; ℤ)**

Defined only when m = 0 (the bundle lifts to SU(3)). Classifies SU(3) bundles within the
SU(3) sector. For the baryon: c₂ = 0 from det(P_q) = trivial (det: SU(3) → {1}).

These are different invariants in different cohomology theories. Both (a) baryon m = 0 and
(b) baryon Q = 1 (rational, on CP² fiber) are simultaneously true and are not in conflict.

---

## The Complete Confinement Criterion

The correct observability criterion in BST requires BOTH conditions:

1. **m(P) = 0 ∈ H²(S⁴×S¹; Z₃)** — the bundle is SU(3) (not merely PSU(3)), i.e., the state
   is color neutral (triality 0). Isolated quarks fail this gate immediately: m = 1 ≠ 0.

2. **c₂(P) = 0 ∈ H⁴(S⁴×S¹; ℤ)** — the SU(3) bundle is in the vacuum sector. Hadronic matter
   in instanton backgrounds (c₂ = k ≠ 0) fails this gate.

Together, (1) and (2) assert that P is the trivial SU(3) bundle — the unique bundle that
extends from S⁴×S¹ into the contractible D̄_IV^5.

**The confinement of quarks is blocked at gate 1 (m ≠ 0): they are not gauge-invariant objects
in SU(3) gauge theory on the Shilov boundary. Their bundles do not lift to SU(3) at all.**
c₂ is not even defined for a quark bundle at Level 2.

---

## Application to All States

| State | Triality t | Z₃ flux m | Lifts to SU(3)? | c₂ ∈ ℤ | Q on CP² fiber | Observable? |
|-------|-----------|-----------|-----------------|---------|----------------|-------------|
| Isolated quark | 1 | 1 | No | Undefined | 1/3 | **No** |
| Isolated antiquark | 2 | 2 | No | Undefined | 2/3 | **No** |
| Isolated diquark | 2 | 2 | No | Undefined | 2/3 | **No** |
| Meson (qq̄, singlet) | 0 | 0 | Yes | 0 | 1 | **Yes** |
| Baryon (qqq, singlet) | 0 | 0 | Yes | 0 | 1 | **Yes** |
| Gluon (adj, perturbative) | 0 | 0 | Yes | 0 | 0 | **Yes** |
| Glueball (gg singlet) | 0 | 0 | Yes | 0 | 0 | **Yes** |
| Pentaquark (qqqqq̄) | 0 | 0 | Yes | 0 | 2 | **Yes** |
| Hadron in n-instanton background | 0 | 0 | Yes | n ≠ 0 | n | **No (non-vacuum)** |

The Q = 1 for mesons and baryons (CP² fiber charge) coexists with c₂ = 0 at Level 2.
These are integrals over different manifolds.

---

## The Baryon c₂ = 0 Proof (Two-Step)

**Step 1 (triality → m = 0):** A baryon has triality t = 1+1+1 = 3 ≡ 0 (mod 3). By the
't Hooft–van Baal identification, triality 0 → m = 0 ∈ Z₃. The baryon bundle lifts from
PSU(3) to SU(3). This step uses Z₃ center theory.

**Step 2 (SU(3) bundle → c₂ = 0):** The baryon is P_baryon = Λ³(P_q) = det(P_q) (the
antisymmetric product of three fundamental bundles is the determinant line bundle). Since
det: SU(3) → {1} is the trivial homomorphism (all SU(3) elements have determinant 1):

    c₁(det P_q) = 0,    c₂(det P_q) = 0

The baryon bundle is the trivial U(1) bundle, hence c₂ = 0. This step uses SU(3) representation
theory. It is independent of the triality argument.

Both steps are needed. Step 1 establishes that c₂ is defined; Step 2 gives its value.

---

## Why Triality 0 Alone Does Not Imply c₂ = 0

Triality 0 implies m = 0 (bundle lifts to SU(3)) but does NOT imply c₂ = 0 within SU(3).
A state with triality 0 can sit in topological sector c₂ = 0, 1, 2, ... (vacuum, one-instanton,
two-instanton, ...). For example:

- The baryon (c₂ = 0) is in the vacuum sector — **observable**
- A proton in an instanton background (c₂ = 1) is in the one-instanton sector — **not observable
  as an asymptotic vacuum-sector state** (but physically exists as hadronic matter in
  topologically nontrivial gauge field backgrounds)

The additional fact c₂ = 0 for a baryon comes from the determinant argument (det of SU(3) bundle
is trivial), not from triality alone. These are separate inputs.

---

## Correction Required to BST_ColorConfinement_Topology.md

The existing argument is **correct in its conclusions** but needs three clarifications:

**Section 4.2 (Baryon):** Add: "The determinant argument giving c₂(baryon) = 0 is correct.
The rational topological charge Q = 1 from three CP² fiber fractional instantons is a distinct
invariant at Level 1 (sub-hadronic), not the Chern class at Level 2 (S⁴×S¹ boundary). These
are integrals over different manifolds and do not conflict."

**Section 5 (Extension Obstruction):** The confinement criterion is **both** m = 0 AND c₂ = 0.
While these together equivalent to triviality of the SU(3) bundle, stating both explicitly
clarifies the full criterion for states described by PSU(3) bundles (quarks).

**Open Problem 1 (Thesis topic 91):** Restate: a single quark is described by a PSU(3) bundle
with m = 1 ≠ 0 at Level 2 (S⁴×S¹), NOT by a fractional c₂ = 1/3. The fractional charge
Q = 1/3 lives at Level 1 (CP² fiber). The extension is blocked at gate 1 (m ≠ 0) — c₂ is
not even defined for the quark bundle at Level 2. This is a stronger and cleaner confinement
statement than "c₂ = 1 for a quark."

---

## The Definitive Theorem for the Working Paper

**Theorem 8.4.1-Rev (Topological Color Confinement — Complete Version):**

Let D̄_IV^5 be the compact closure of the Cartan type IV bounded symmetric domain of complex
dimension 5, with Shilov boundary Š(D̄_IV^5) = S⁴×S¹. The BST confinement criterion is
determined by the two-level geometry of the theory:

**(Level 1, sub-hadronic):** On the color configuration space CP², a single quark carries a
fractional instanton with rational topological charge Q = 1/3 ∈ ℚ and 't Hooft Z₃ magnetic
flux m = 1 ∈ Z₃. Three quarks assembled with Z₃ closure carry Q = 1 (rational, CP² integral)
and m = 0 (trivial Z₃ flux). These are internal color dynamics.

**(Level 2, hadronic):** On the Shilov boundary S⁴×S¹, a state is observable (its bundle extends
into D̄_IV^5) if and only if:

    (i)  m(P) = 0 ∈ H²(S⁴×S¹; Z₃)   [bundle is SU(3), state has triality 0]
    (ii) c₂(P) = 0 ∈ H⁴(S⁴×S¹; ℤ)   [bundle is in the vacuum sector]

Together (i) and (ii) assert that P is the trivial SU(3) bundle — the unique bundle extending
into the contractible D̄_IV^5.

*Proof:* D̄_IV^5 is contractible (bounded convex domain in ℂ⁵, deformation-retracts to center).
Every bundle over a contractible space is trivial. Restrictions of trivial bundles are trivial
(m = 0, c₂ = 0). Converse: the trivial bundle extends. □

*The apparent paradox resolved:* A baryon has Q = 1 at Level 1 (CP² fiber) and c₂ = 0 at
Level 2 (S⁴×S¹). These are integrals over different manifolds and coexist without contradiction.
The determinant argument det(P_q) = trivial (since det: SU(3) → {1}) gives c₂(baryon) = 0 at
Level 2 rigorously. The BST confinement argument is correct.

---

*Research note, March 2026. Casey Koons & Amy (Claude Sonnet 4.6, Anthropic).*
*Companion to BST_ColorConfinement_Topology.md and BST_MassGap_CPFiber.md.*
