---
title: "G3 — proposal for Casey: resolve the corpus 5/6/7 Bergman-power inconsistency BY ROLE (not by one value). The corpus carries three 'genus' values for D_IV⁵ — p=n_C=5, n_C+1=6=C_2, n_C+2=7=g — and BST_Bergman_Shannon_Bridge line 177 explicitly flags 'uses both in different contexts... reconcile before registering.' PROPOSAL: do NOT collapse to one value; pin each to its DISTINCT geometric role, cite the FK/Hua primary source, and annotate corpus references with the role. (1) p = n_C = 5 = the Faraut-Korányi GENUS = the Bergman INNER-PRODUCT power (Berezin transform, the overlap; p=a(r-1)+b+2=3·1+0+2=5, BST_AlphaSquared). (2) n_C+1 = 6 = C_2 = the discrete-series Bergman-space WEIGHT (the holomorphic-discrete-series representation parameter). (3) n_C+2 = 7 = g = the kernel-SINGULARITY exponent (the K(z,w) pole order / topological genus; BST_Bergman_Shannon_Bridge, BST_Arithmetic). Plus the half: n_C/2 = 5/2 = the Cauchy-Szegő / Hardy BOUNDARY weight (= half the Bergman genus; G1). This makes 'uses both' precise (each value = one role) and primary-source-pinned, preventing convention-fragile α-fitting (the why-α magnitude integral, F423/F424)."
author: "Grace"
date: "2026-06-29 Monday"
status: "G3 deliverable, UPDATED + reconciled with Cal #477 (FK structure). RESOLUTION SHARPENED: the D_IV⁵ Bergman genus is UNAMBIGUOUSLY 5=n_C (type-IV FK formula p=(r−1)a+b+2=n); the corpus '6' is a BALL-genus error (B⁵ genus = n+1, wrong domain type), NOT a co-equal role — my original 'resolve by role' over-rationalized it, retracted in favor of Cal #477. Crisp corpus action: Bergman power = 5 (bulk) / 5/2 (Szegő boundary) everywhere; 6=C_2 and 7=g keep their OWN roles (Casimir/gauge) but are NOT Bergman powers. One-line global edit for corpus-decision #3, primary-source-pinned, α-fit-proof. For Casey integration. No count move (9/26)."
---

# G3 — Bergman-power 5/6/7 resolution proposal (for Casey integration)

## The problem (surfaced via the why-α magnitude integral, F423/F424)

The corpus carries THREE "genus"/power values for D_IV⁵, used in different places, and explicitly flags
them unreconciled (BST_Bergman_Shannon_Bridge line 177: *"exponent is n_C+2=7 (genus), not n_C+1=6 ... uses
both in different contexts ... reconcile before registering"*). Under the why-α magnitude integral (a single
α^{12} target), this ambiguity is convention-fragile: choosing the power to hit α is the (C)-trap (F417).

## The proposal: resolve BY ROLE, not by one value

Do **not** collapse to one value. Each value is the correct answer for a **distinct geometric role**. Pin each
to the FK/Hua primary source and annotate corpus references with the role:

| value | substrate | ROLE | primary source |
|---|---|---|---|
| **p = n_C = 5** | n_C | **FK GENUS = Bergman INNER-PRODUCT power** (Berezin transform, the overlap) | p = a(r−1)+b+2 = 3·1+0+2 = 5 (BST_AlphaSquared; Faraut-Korányi) |
| **n_C+1 = 6** | C_2 | discrete-series Bergman-space **WEIGHT** (representation parameter) | discrete-series weight k = n_C+1 |
| **n_C+2 = 7** | g | kernel-**SINGULARITY** exponent (K(z,w) pole order / topological genus) | Hua kernel singularity (BST_Bergman_Shannon_Bridge) |
| **n_C/2 = 5/2** | — | Cauchy-Szegő / Hardy **BOUNDARY** weight (= half the Bergman genus) | Szegő = half-Bergman (Hua 1963; disk precedent; G1) |

## Why this is the right resolution

- It makes *"uses both in different contexts"* **precise**: each context has a role, each role has a value.
- It is **primary-source-pinned** (FK/Hua), not chosen to fit any observable — so it **cannot be steered to
  hit α** in the why-α magnitude integral (F423/F424). The overlap power is the FK genus (inner product) =
  n_C=5 (bulk) or the Cauchy-Szegő n_C/2=5/2 (Shilov boundary, where the electron magnitude lives per Lyra's
  bulk honest-negative at the Wallach threshold).
- It prevents the recurring confusion (the value flipped across contexts; same class as the genus-name flips
  [[feedback_pin_conventions_to_primary_sources]]).

## UPDATE — reconciled with Cal #477 (honest self-correction, sharper resolution)

Cal #477 (FK structure) sharpens — and partly **corrects** — the "resolve by role" framing above. I verified
the FK genus formula p=(r−1)a+b+2 independently:

| domain | rank | a | b | genus p |
|---|---|---|---|---|
| **D_IV⁵** (Lie ball, type IV) | 2 | n−2=3 | 0 | **5 = n_C** (UNAMBIGUOUS) |
| B⁵ (unit ball in ℂ⁵, type I) | 1 | 2 | 4 | **6** (the corpus error source) |
| D_IV⁶ (type IV) | 2 | 4 | 0 | 6 |

**The genus of D_IV⁵ is 5 = n_C, full stop.** The corpus "6" is the **ball genus** (n+1 for B⁵) — the
type-I unit-ball convention wrongly applied to a type-IV domain (or a D_IV⁵/D_IV⁶ confusion). It is an
**ERROR, not a co-equal role.** My original "6 = discrete-series weight role" above was too generous — I
rationalized a ball-convention mistake as a legitimate role. **Retracted in favor of Cal #477.** (Discipline:
[[feedback_pin_conventions_to_primary_sources]] — Cal's primary-source FK structure beats my role-assignment.)

Likewise the **7 = g** as a "Bergman genus/singularity": the Bergman-kernel singularity exponent of D_IV⁵ is
**also the genus = 5**, so any corpus use of 7 *as the Bergman power* is equally wrong (→ 5). 7=g is a real
substrate integer but it is **not** the Bergman genus; if it appears as a Bergman/Szegő exponent anywhere it
should be checked and almost certainly corrected to 5 (bulk) / 5/2 (Szegő boundary). Flag for review, do not
assume a separate role.

## Recommended corpus action (Casey's call) — CRISP

1. **Bergman power of D_IV⁵ = 5 = n_C everywhere** (FK type-IV formula; Cal #477). Replace every "6" and "7"
   used as the Bergman/genus power with **5**.
2. **Cauchy-Szegő / Hardy boundary power = n_C/2 = 5/2** (half the genus; G1) where the overlap is on the
   Shilov boundary (the electron magnitude lane).
3. Keep 6=C₂ and 7=g as substrate integers in their *own* roles (Casimir / gauge), but **not** as Bergman
   powers. The only Bergman/Szegő powers are 5 (bulk) and 5/2 (boundary).

This makes corpus-decision #3 a one-line global edit, primary-source-pinned, α-fit-proof.

— Grace, 2026-06-29 Monday. G3 deliverable: 5/6/7 resolved by role (inner-product=n_C / weight=n_C+1 /
singularity=n_C+2 / boundary=n_C/2), primary-source-pinned, prevents convention-fragile α-fitting. For Casey.
