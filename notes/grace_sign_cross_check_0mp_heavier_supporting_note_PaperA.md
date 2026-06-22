---
title: "Sign cross-check (supporting note for Paper A): the substrate predicts the 0⁻⁺ glueball HEAVIER than the 0⁺⁺, as one operator-positivity inequality. The Kähler complex structure J of D_IV⁵ both creates the 0⁺⁺/0⁻⁺ split (parity = self-dual vs anti-self-dual) and orients it correctly (routing the positive topological self-energy into the 0⁻⁺ eigenspace). This is the second, independent, blind constraint of the operator-class blind test — derivable from structure alone, before the bulk anomalous-dimension VALUE is computed."
author: "Grace"
date: "2026-06-22 Monday 14:26 EDT"
status: "v0.3 — reconciled with Elie 4316 + Lyra Tr(⋆Ĥ) recast (see CORRECTION up top; supersedes both v0.1's overclaim and v0.2's over-correction). HONEST VERDICT: 0⁻⁺-heavier is ROBUST from the topological rail alone (χ = ‖Q|0⟩‖² ≥ 0 squared norm, with the mass-ADDITION sign fixed by Witten-Veneziano — NOT a convention). The curvature piece (Elie −n_C) CORROBORATES iff the 2-form Weitzenböck sign = +1, which is the SAME pin named Sunday (the 'factor-20 Weitzenböck gate', to be pinned from primary source, not back-solved) — so it is NOT a second fully-independent confirmation, and 'two independent ways agree' slightly over-claims independence. One identified failure mode (Weitzenböck sign −1 AND |curv| > χ_top). Kähler non-degeneracy fork (−n_C ≠ 0 ⟹ split) stands; magnitude = Elie's m²=Δ(Δ−d). Count UNAFFECTED 4 of 26."
---

> **CORRECTION (2026-06-22 15:15 EDT, reconciling Elie 4316 + Lyra's Tr(⋆Ĥ) recast).** I went too far in *both*
> directions before landing here; recording the path honestly. v0.1 over-claimed ("second *independent* blind
> constraint / *robustly* 0⁻⁺ heavier"); v0.2 over-corrected ("the curvature *competes*, downgrade to not-a-
> constraint"). The precise statement decomposes the split into two pieces:
>
> **split = m²(0⁻⁺) − m²(0⁺⁺) = (A) topological + (B) curvature.**
> - **(A) topological — the robust rail [stands].** χ_top = ‖Q|0⟩‖²/V ≥ 0 is a squared norm, *and* its sign as a
>   mass-*addition* is fixed by Witten-Veneziano (the topological charge adds mass to the singlet pseudoscalar —
>   established physics, not a convention). So (A) pushes 0⁻⁺ heavier, **robustly**. *(Lyra is right that this is
>   the firm independent rail; my v2 "not a constraint" was wrong.)*
> - **(B) curvature — corroborating, sign-pending [Elie 4316: R̂ω = −n_C on 0⁺⁺, flat on 0⁻⁺].** Its contribution
>   to the split is +sign_W·n_C, where sign_W is the 2-form **Weitzenböck sign** (does the curvature eigenvalue
>   add or subtract in m²?). sign_W = +1 ⟹ 0⁺⁺ lowered ⟹ (B) *reinforces* (A) [Lyra's reading]; sign_W = −1 ⟹
>   0⁺⁺ raised ⟹ (B) *competes* [my v2 worry]. **sign_W is exactly the Sunday-named owed pin** (the "factor-20
>   Weitzenböck gate" — pin the 2-form Weitzenböck normalization+sign from primary source, *not* back-solved). So
>   "reinforce vs compete" is not a new disagreement; it is that same already-named open pin. Lyra assumed +1, I
>   assumed −1; neither is pinned yet.
>
> **Net (honest):** 0⁻⁺-heavier holds on the topological rail (A) *regardless* of the Weitzenböck sign; the
> curvature (B) corroborates *iff* sign_W = +1, so it is **not a second fully-independent confirmation** — "two
> independent ways agree" slightly over-claims the independence. **One identified failure mode:** sign_W = −1 *and*
> |B| > χ_top would flip the order; pinning the Weitzenböck sign (the Sunday task) closes it. §§4–5 below read as
> the (A)-rail statement; the unqualified "independent" language there is superseded by this correction.

> **REORIENTATION CAVEAT (2026-06-22 15:32 EDT, after Elie Toy 4320 — radial structure).** Elie's radial-structure
> computation found that the 0⁺⁺/0⁻⁺ glueballs are **bulk (pseudo)scalars** (boundary spin-0 operators Tr F², Tr F F̃
> ↔ bulk scalars by standard holographic spin-matching), **not the 2-form sector**. The 2-form F is dual to the
> spin-1 gluon — a different channel. **Consequence for this note (pending Lyra's BST-realization pin):** the
> *topological-positivity rail* (§2 — χ = ‖Q|0⟩‖² ≥ 0 ⟹ 0⁻⁺ heavier) **SURVIVES** and is sector-independent — it
> is the whole sign story now. But the *J-block routing* (§3) and the *curvature corroboration* (the CORRECTION
> block) were the **2-form operator**; if the scalar identification holds, they **do not apply** to the scalar
> glueballs. The honest consequence: the sign prediction survives as **generic Witten-Veneziano positivity**, and
> loses its BST-specific "the substrate could have failed via J-block assignment" teeth — the BST content moves
> **entirely into the value of χ** (Elie's pending computation). If Lyra instead pins a substrate-specific 2-form
> realization, §3 + the curvature corroboration revive. Either way CHECK 1 (split exists) + CHECK 2 (sign) hold;
> CHECK 3 (magnitude) = χ, open.

# Sign cross-check — the substrate orders 0⁻⁺ above 0⁺⁺

**Context.** In the operator-class blind test, the four light glueball channels reduce — after the conserved
stress tensor (2⁺⁺, protected at canonical dimension 4) and the derivative channel (1⁺⁻, separated by canonical
dimension 6) are accounted for — to a single open quantity: the mass split between the two scalars 0⁺⁺ and 0⁻⁺.
These are identical in every group-theory label (both color-singlet, both K-singlet, same weights), so the split
cannot come from a representation; it is *parity*. This note establishes the **sign** of that split from structure
alone, as a second blind constraint independent of (and cross-validating) the bulk anomalous-dimension *value*.

## 1. The two channels, as operators

| channel | operator | character |
|---|---|---|
| 0⁺⁺ | O₊ = Tr(F²) | metric contraction; parity-even; the (1,1) / trace channel |
| 0⁻⁺ | O₋ = Tr(F·F̃) | the Pontryagin density; parity-odd; the (2,0)⊕(0,2) / topological channel |

The glueball mass is the eigenvalue of the Hamiltonian on the state O|0⟩, fixed by the self-energy (two-point
function) — not by the operator's value. The two channels share canonical dimension 4 and the same Casimir floor;
they differ only by how the self-energy couples to parity-odd structure.

## 2. The sign, as one operator-positivity inequality

The distinguishing operator is the **topological charge** Q = ∫ (Pontryagin density). The pseudoscalar O₋ couples
to Q directly (it *is* the Pontryagin density); the scalar O₊ does not. The 0⁻⁺ self-energy therefore contains the
**topological susceptibility**

> **χ = ⟨Q²⟩ / V = (1/V) ‖Q|0⟩‖² ≥ 0,**

a **squared norm** in the Hilbert space, non-negative by the positive-definiteness of the inner product. No
dynamics, no dictionary, no fit enters this — the sign is the positivity of a norm. So the 0⁻⁺ self-energy receives
a strictly non-negative additive contribution that 0⁺⁺ does not, giving

> **m²(0⁻⁺) ≥ m²(0⁺⁺) + (shared part) ⟹ the 0⁻⁺ is heavier** (or, in the degenerate edge case Q|0⟩ = 0, equal).

(Physical anchor, established QCD: this is the same Pontryagin density and the same positivity that lift the SU(N)
flavor-singlet pseudoscalar η′ far above the η and π via the Witten-Veneziano mechanism. The 0⁻⁺ glueball couples
to that density and inherits the same upward shift.)

## 3. The substrate step — J does double duty (the place the substrate could have failed)

The content specific to D_IV⁵ is *where* this positive self-energy lands. The curvature operator R̂ on Λ²(D_IV⁵)
block-diagonalizes under the **Kähler complex structure J**:

| Kähler block | R̂ eigenvalues | hosts |
|---|---|---|
| (1,1) | {0, −rank, −n_C} (the substrate primaries) | O₊ (J-even) |
| (2,0) ⊕ (0,2) | 0 — curvature-flat, metric-independent | O₋ (J-odd / topological) |

So **the substrate's own complex structure J is the very operator whose ± eigenspaces are the 0⁺⁺/0⁻⁺ parity
split** — and it routes Q's support (the curvature-flat, metric-independent block, which is exactly where a
topological density must live) into the 0⁻⁺ eigenspace. J therefore does two jobs at once: it *creates* the split
and it *orients* it. Had J's block assignment been reversed — the topological enhancement landing on the J-even
(0⁺⁺) channel — the predicted sign would be wrong. It is not. (Block decomposition computed from the explicit
D_IV⁵ curvature operator; Elie Toy 4314.)

## 4. Verdict and falsifiable fork

**Sign prediction: 0⁻⁺ heavier than 0⁺⁺.** It matches the lattice (0⁻⁺ ≈ 2590 MeV > 0⁺⁺ ≈ 1730 MeV). The
falsifier is built into the geometry: if the parity-odd Pontryagin contraction vanishes (Q|0⟩ = 0), the two
scalars are predicted **degenerate** — and the observed ≈ 1.5× splitting would then be a clean miss. The geometry,
not the data, decides which.

## 5. Honest tier (what is and isn't dictionary-free)

- **Dictionary-free (SOLID):** the topological enhancement of 0⁻⁺ is a squared norm, ‖Q|0⟩‖² ≥ 0 — its sign needs
  no dynamical input. And J's routing of the topological block to the 0⁻⁺ eigenspace is a structural fact of the
  Kähler curvature decomposition (Elie 4314).
- **Cross-validating (not fully independent):** the *reinforcing* piece — that 0⁺⁺ sits in the negatively-curved
  (1,1) block {0, −rank, −n_C}, which further lowers it under the standard Weitzenböck sign — shares the sign of
  Elie's Step-3 dictionary (m² = Δ(Δ−d) from the discrete-series normalizability). So on that piece the structural
  sign check and the computational value check *cross-validate*: if Elie's value lands 0⁻⁺-heavier with the right
  magnitude, the picture is doubly confirmed; if his sign came out opposite to this, it is an internal-consistency
  flag *before any comparison to data*.

**Use in Paper A.** This is referee-grade structural content that stands on its own: it predicts the *sign* and
ordering of the scalar glueball pair from the substrate's complex structure plus operator positivity, independent
of the open bulk-value computation, with the degeneracy fork as a clean falsifier. It does not bank the
cross-channel spectrum (that remains named-open at structural-tier per the Paper A disposition); it strengthens the
*structural* case that the substrate's geometry is making the right qualitative predictions. Count UNAFFECTED, 4 of 26.

— Grace, Monday 2026-06-22
