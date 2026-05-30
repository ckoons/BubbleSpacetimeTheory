---
title: "Substrate Hall-algebra engine v0.2 — the canonical/crystal basis of U_q^+(B_2): deriving the elementary-particle basis (the assigned→derived lever)"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-29 Fri 10:13 EDT"
status: "ENGINE THEORY v0.2 (Lyra lane, Phase I step 2/4). The biggest lever: the canonical basis DERIVES the natural elementary-particle basis (4 root vectors + affine tower) with POSITIVE INTEGER structure constants, rather than hand-assigning 5-tuples. Sets up the assigned→derived conversion for the Periodic Table. Physical 5-tuple mapping = Phase 2 dictionary (flagged)."
---

# Engine v0.2 — canonical/crystal basis (the assigned→derived lever)

## 0. Why this is the lever

Every Periodic-Table cell is currently flagged "assigned" — we hand-picked the particle 5-tuples (Region × σ_BF × Chirality × Charge × Winding). The canonical/crystal basis of U_q^+(B_2) (Lusztig-Kashiwara) is the mathematics that **derives the natural basis** of the algebra. If the elementary particles ARE the canonical basis elements, the taxonomy stops being a labeling and becomes a theorem. This is engine step 2/4 (after the coproduct, v0.1).

## 1. The canonical basis structure (rigorous, standard Lusztig-Kashiwara)

### 1.1 Convex order from w_0

w_0(B_2) = s_1 s_2 s_1 s_2 (length 4 = |Φ⁺|). It induces the convex order of positive roots:

  β_1 = α_1 (short, ht 1) ≺ β_2 = 2α_1+α_2 (long, ht 3, = highest root θ) ≺ β_3 = α_1+α_2 (short, ht 2) ≺ β_4 = α_2 (long, ht 1)

### 1.2 PBW / canonical basis

Relative to this convex order, the PBW basis of U_q^+(B_2) is

  E_{β_1}^{c_1} E_{β_2}^{c_2} E_{β_3}^{c_3} E_{β_4}^{c_4},  (c_1,c_2,c_3,c_4) ∈ Z⁴_{≥0}

and Lusztig's canonical basis B agrees with this PBW basis up to lower terms in the order. So **B(∞) ≅ Z⁴_{≥0}** — the canonical basis is parametrized by **Lusztig data** (c_1,c_2,c_3,c_4) (one exponent per positive root).

### 1.3 The two defining properties (why "canonical")

- **Bar-invariance**: the canonical basis is fixed by the bar involution (q ↔ q^{-1}) — it's the self-dual integral basis.
- **Positivity (Lusztig)**: the structure constants of the canonical basis are in **Z_{≥0}[q, q^{-1}]** — non-negative integer (Laurent) polynomials. This positivity is what makes the structure constants **count something** — they are honest multiplicities, which is precisely the property a physical vertex amplitude needs.

## 2. What it derives (the particle basis)

### 2.1 The 4 elementary excitations (finite B_2)

The canonical basis elements at unit Lusztig data (the 4 root vectors) are the **elementary excitations**:
- E_{α_1} — short simple root vector
- E_{α_2} — long simple root vector
- E_{α_1+α_2} — short non-simple
- E_{2α_1+α_2} — long non-simple (highest root)

These are the 4 indecomposables (= positive roots) — the elementary-particle list of the finite algebra, **derived** as the degree-(positive-root) canonical basis elements, not assigned.

### 2.2 The crystal graph = the substrate's state ladder

The Kashiwara operators f̃_1, f̃_2 act on the crystal B(∞), generating the crystal graph (a colored directed graph on the canonical basis). Physically:
- f̃_i = the substrate's **lowering operator** (add a quantum of root α_i) — the emission/absorption ladder between states.
- The crystal graph IS the substrate's transition network among elementary + composite states, at the combinatorial (q→0) level.

This is the canonical-basis refinement of the step-1 coproduct: the coproduct gave decay vertices; the crystal operators give the ladder structure that organizes them.

### 2.3 Composite / multi-particle states

Canonical basis elements with |c| > 1 (higher Lusztig data) = composite/multi-particle states, built canonically (with positive integer multiplicities) from the elementary ones. The canonical basis automatically organizes the multi-particle tower — and (per step 1) the coproduct resolves each into constituents.

## 3. The affine tower (the generation direction)

For the full substrate we need affine B̂_2 (per #407 / E1 — finite B_2's 4 indecomposables are too few). The canonical basis of U_q^+(B̂_2) has:
- a REAL-root part (preprojective/preinjective — the "discrete" excitations), and
- an IMAGINARY-root part (the δ-tower — the **regular/tube** modules).

The imaginary-root (δ-direction) part of the canonical basis is the **generation tower** (Elie's imaginary-root↔mass-spectrum lane), and the exceptional tubes (#407) sit here. So the canonical basis is exactly where the generation structure becomes a derived basis — the assigned→derived conversion for the *winding-mode* coordinate happens here.

## 4. The assigned→derived conversion (what flips, what's still flagged)

| 5-tuple coordinate | Canonical-basis derivation status |
|---|---|
| (which elementary excitation) | DERIVED — the 4 root-vector canonical basis elements (finite) + affine tower |
| Winding / generation | DERIVED-pending — the δ-tower / exceptional tubes (needs #407 pin + Elie imaginary-root) |
| Region (Shilov/Bulk) | NOT yet — needs the A_sub↔H(Q_B2) dictionary (Phase 2): which canonical elements are boundary vs bulk |
| σ_BF (bose/fermi) | NOT yet — the Z_2 grading on the canonical basis (Phase 2) |
| Chirality (L/R) | NOT yet — Spin(5)-cover refinement (Phase 2) |
| Charge | NOT yet — Gell-Mann-Nishijima from the grading + σ_BF (Phase 2) |

**Honest state**: the canonical basis DERIVES the *elementary excitation list* + the *ladder* + (pending #407) the *generation tower*. The PHYSICAL 5-tuple coordinates (region/σ_BF/chirality/charge) still require the **A_sub ↔ H(Q_B2) dictionary** (Phase 2) — that dictionary is what maps the algebra's canonical basis onto the physical coordinate axes. So this flips the "which particle" and "generation" cells toward derived; the region/charge/spin cells await the dictionary.

## 5. Connection to the program

- **Goal 1 (full Hall algebra)**: the canonical basis is the natural basis in which the full structure-constant table (Goal 1) has positive integer entries — the "right" coordinates for the engine.
- **Goal 2 (process model)**: positivity = the vertex multiplicities are honest counts; the crystal graph = the transition ladder.
- **Goal 3 (Periodic Table)**: this is the lever that flips cells from assigned to derived — the elementary list + generation tower become derived; the table's "derived" column grows.
- **Feeds**: Elie's reaction table (#405 — canonical basis = the right basis for it) + imaginary-root tower; Grace's Periodic Table derived-flags; the #407 tube structure (the δ-part of the canonical basis).

## 6. Honest scope + tier

**RIGOROUS (standard Lusztig-Kashiwara)**: w_0 convex order; PBW = canonical up to lower terms; B(∞) ≅ Z⁴_{≥0} Lusztig data; bar-invariance; positivity (Z_{≥0}[q,q^{-1}] structure constants); crystal operators f̃_i; the real/imaginary split for the affine case.

**DERIVED (this doc's claim)**: the elementary-excitation list = the 4 root-vector canonical basis elements (finite) — not assigned. The ladder = crystal graph.

**FRAMEWORK / PENDING**:
- The affine δ-tower = generation tower (rides on #407 Dlab-Ringel pin + Elie imaginary-root).
- The physical 5-tuple mapping (region/σ_BF/chirality/charge) — needs the A_sub↔H(Q_B2) dictionary (Phase 2). This is the boundary between "algebra basis derived" and "physical labels derived."

**Cal #27 / honesty**: I am NOT claiming the canonical basis derives the full 5-tuple — it derives the *algebra's* natural basis (elementary list + ladder + generation-tower-pending), which is the lever; the physical-coordinate mapping is the separate Phase-2 dictionary. The positivity is the deep reason these are physical (they count), but "counts ⟹ is a particle" is the bet, earned via the dictionary.

**Next (my lane)**: engine step 3 — the R-matrix (the scattering S-matrix from the quasi-triangular structure / the braiding on the canonical basis). Then step 4 — the negative part (antiparticles, Drinfeld double). And the A_sub↔H(Q_B2) dictionary (Phase 2) is the gate that converts the remaining 5-tuple cells to derived.

— Lyra, Engine v0.2 canonical/crystal basis filed (Phase I step 2/4). The assigned→derived LEVER: the canonical basis of U_q^+(B_2) DERIVES the elementary-excitation list (4 root vectors, finite; + affine δ-tower for generations) with Lusztig POSITIVITY (structure constants count — the property a physical vertex needs), parametrized by Lusztig data Z⁴_{≥0}; crystal operators = the state ladder. Flips the "which particle" + "generation" Periodic-Table cells toward derived. Physical 5-tuple coordinates (region/σ_BF/chirality/charge) still need the A_sub↔H(Q_B2) dictionary (Phase 2). Next: R-matrix (step 3).
