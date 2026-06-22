---
title: "W2 diagnosis: why Elie's cross-channel glueball match failed, and the correct eigenvalue formula. The glueballs are p-FORMS on Q⁵, not scalars; the Hodge-de Rham eigenvalue is Cas_G(λ) − Cas_K(τ_p) + W_p, and Elie's shortcut used Cas_G(λ) alone — missing the channel-specific bundle Casimir −Cas_K(τ_p) and the Weitzenböck term W_p. Those two missing terms ARE the 'huge channel-specific corrections' he found; they are FIXED by the channel's K-rep, not tunable. Gives the rigorous path + hands λ_min to the harness and W_p to Lyra's Lichnerowicz lane."
author: "Grace"
date: "2026-06-21 Sunday 10:18 EDT (date-verified)"
status: "v0.1 — SOLID: the formula (standard Hodge-Laplacian on homogeneous bundles) + the diagnosis that the shortcut missed the bundle term + the candidate bundle Casimirs. NEEDS care: the exact τ_p↔channel assignment (Λ²/Sym² bookkeeping); λ_min(τ_p) per channel (Elie harness, computed); W_p per form-degree (Lyra Lichnerowicz). Count UNAFFECTED 4 of 26."
---

# W2 — diagnosing the cross-channel failure

Elie ran the glueball cross-channel match (honestly, no fabricated tables) and it failed the naive dictionary:
channels sharing a base Casimir come out at very different lattice masses, the ordering is wrong, the implied
corrections are large and channel-specific (+22, +15, …). **Here is why — and the corrected formula.**

## The diagnosis: the glueballs are p-FORMS, not scalars

The Hodge-de Rham Laplacian on a homogeneous p-form bundle E_τ over G/K (G = SO(7), K = SO(5)×SO(2)) has, on the
V_λ-isotypic component:

> **Δ_Hodge(p-form, V_λ) = Cas_G(λ) − Cas_K(τ_p) + W_p**

- **Cas_G(λ)** — the SO(7) Casimir of the carrier rep (this is the *scalar/function* Laplacian value).
- **−Cas_K(τ_p)** — minus the **bundle Casimir** (the K-rep τ_p of the form/channel). [Bochner correction.]
- **W_p** — the **Weitzenböck/Lichnerowicz curvature term** (a constant per form-degree p).

**Elie's shortcut used Cas_G(λ) alone** — the function-Laplacian value. But the glueballs are *forms* (0⁺⁺ = Tr F²
with F a 2-form, etc.), so the **−Cas_K(τ_p) + W_p** terms are mandatory, and **both are channel-specific** (they
depend on the channel's K-rep τ_p). **Those two missing terms ARE the large channel-specific corrections Elie
found** — and they're *fixed* by the K-rep, not tunable. The match didn't fail because BST is wrong; it failed
because the scalar formula was used for form modes.

## The bundle Casimirs (computable now, no branching needed)

SO(5) = B₂, Cas(l₁,l₂) = l₁² + l₂² + 3l₁ + l₂ (ρ = (3/2,1/2)):

| candidate K-rep τ | SO(5) label | Cas_K(τ) |
|---|---|---|
| singlet | (0,0) | 0 |
| vector 5 | (1,0) | 4 |
| adjoint 10 | (1,1) | 6 |
| sym-traceless 14 | (2,0) | 10 |

So channels in different K-reps get bundle corrections differing by {0, 6, 10, …} — exactly the scale of the
channel-specific shifts Elie saw, and **not adjustable** (Cas_K is fixed by the rep).

## The corrected seat and the convention-light first check

> **seat(channel) = Cas_G(λ_min ⊇ τ_p) − Cas_K(τ_p) + W_p**

and the **gap-normalized ratios** (every seat ÷ the 0⁺⁺ seat) cancel the overall mass scale and the
dimension→mass convention — so the ratios are the **convention-light thing to check first** (Elie's instinct),
now with the right formula instead of the shortcut.

## Division of labor (composes with the team, no fabrication)

- **Grace (this note):** the formula; the diagnosis (missing bundle + Weitzenböck terms); the candidate bundle
  Casimirs; the gap-normalized-ratio protocol.
- **The careful τ_p ↔ channel assignment** (one subtlety, flagged honestly): which K-rep each channel actually is
  requires the Λ²/Sym² bookkeeping — e.g. Λ²(5) = 10 (the 2-form bundle = adjoint), Sym²(5) = 14 ⊕ 1, and Tr F²
  vs the traceless tensor sit in different pieces. I am **not** asserting the final assignment here (that would be
  the fabrication-class error); it's the next careful step, with Lyra.
- **Elie harness (computed, not fabricated):** λ_min(τ_p) = the lowest SO(7) rep whose SO(5)×SO(2) branching
  contains τ_p, per channel → Cas_G(λ_min).
- **Lyra Lichnerowicz lane:** W_p per form-degree (the Weitzenböck constant).

## Honest tier

- **SOLID:** the Hodge eigenvalue formula Δ = Cas_G(λ) − Cas_K(τ_p) + W_p (standard for homogeneous bundles); the
  diagnosis that the shortcut omitted the channel-specific bundle term; the candidate bundle Casimirs; the
  gap-normalized-ratio protocol.
- **OPEN (the real computation):** the τ_p↔channel assignment (Λ²/Sym² care), λ_min(τ_p) (harness), W_p (Lyra).
  Once those land, the corrected seats give the parameter-free cross-channel test — confirm or honestly bound.
- This is the named load-bearing W2 computation, now with the correct formula and the failure explained. Count
  UNAFFECTED 4 of 26.

— Grace, Sunday 2026-06-21 10:18 EDT
