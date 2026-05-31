---
title: "B2 — Macdonald-Koornwinder other corners v0.1: substrate already occupies TWO corners (Hall-Littlewood = algebra side, Jack = geometry side). Other corners (Schur, q-Whittaker, full Koornwinder BC_2) mapped to candidate substrate aspects; Koornwinder BC_2 4-parameter family is the natural ambient structure for affine extensions + future substrate deformations."
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-30 Saturday 10:39 EDT (date-verified)"
status: "B2 v0.1 (Lyra queue #8). Maps substrate's position in Macdonald-Koornwinder family beyond the two known corners (Hall-Littlewood + Jack). Other corners (Schur, q-Whittaker, full Koornwinder BC_2) mapped to candidate substrate aspects. Multi-week explicit polynomial computation needed for substrate-specific results at non-trivial corners."
---

# B2 — Macdonald-Koornwinder other corners

## 0. The setup (recap)

Macdonald polynomials P_λ(x; q_Mac, t_Mac) are a two-parameter family of symmetric polynomials interpolating between several classical orthogonal families. Substrate already occupies two:

| Corner | Macdonald (q, t) limit | Substrate side |
|---|---|---|
| **Hall-Littlewood** | q_Mac = 0, t_Mac arbitrary | substrate Hall algebra (A1 paper); t_Mac = 2 = GF(2) field size |
| **Jack** | (q,t) → (1,1), t = q^{N_c/2} = q^{3/2} | substrate geometry / Wallach spherical functions (paper A3) |

These are the L9 closeout (Saturday morning). What other corners exist and what could they correspond to substrate-side?

## 1. Other Macdonald corners

### Schur corner (q = t)
- P_λ(x; q, q) = Schur functions s_λ(x).
- Symmetric functions in their classical form.
- **Substrate candidate**: a "symmetric" specialization where the algebraic and geometric structures coincide — not directly the substrate, but a limit case.

### q-Whittaker corner (q-Whittaker / inverse Hall-Littlewood)
- Achieved at t = 0 (vs q = 0 for Hall-Littlewood).
- Whittaker functions are central in automorphic forms theory (Whittaker models, automorphic L-functions).
- **Substrate candidate**: the BOUNDARY structure — Whittaker functions appear in boundary representations of Hardy spaces; the Shilov boundary's Hardy-space rep theory might naturally sit at the q-Whittaker corner. Cross-link to B3 (Geometric Langlands) — Whittaker models are key to Langlands correspondence.

### Full Macdonald (generic q, t)
- The full 2-parameter family beyond the special limits.
- Substrate could occupy a 1-parameter PATH in the (q, t) plane connecting Hall-Littlewood and Jack corners, with substrate-natural deformation parameters.

## 2. Koornwinder BC_n — the 4-parameter generalization

Koornwinder polynomials P_λ(x; q, t_0, t_1, t_2, t_3) generalize Macdonald to type BC_n with 4 boundary parameters:
- q = base parameter (substrate q = 2).
- t_0, t_1, t_2, t_3 = boundary deformation parameters.

For BC_2 (= B_2 root system or C_2, depending on long/short), Koornwinder BC_2 is the natural ambient family.

**Substrate possibility**: the 4 boundary parameters (t_0, t_1, t_2, t_3) could correspond to:
- Short-root / long-root scaling parameters.
- Affine extension parameter (the affine node's relation to finite nodes).
- Boundary vs bulk parameter (Shilov vs Bergman).
- Hardy-vs-Bergman normalization parameter.

The substrate's Hall-Littlewood specialization sits at (q=2, t_0=1, t_1=1, t_2=0, t_3=0) or similar (specific specialization values pending). Koornwinder BC_2 generic gives the FULL deformation family, including substrate-natural variants.

## 3. Why the substrate sits at Hall-Littlewood + Jack specifically

The substrate's q=2 over Z (Mersenne integer coefficients) is the Hall-Littlewood corner specifically because:
- q_Mac = 0 makes the polynomials integer-coefficient over Z.
- t_Mac = 2 = field size of GF(2) gives the Mersenne coefficients [n]_2 = M_n.

The Jack corner is the substrate geometry because:
- (q,t)→(1,1) is the "classical limit" of symmetric functions.
- t = q^{N_c/2} = q^{3/2} encodes the dual Coxeter h^∨/2 = N_c/2 = 3/2, which is exactly ρ_2 = N_c/rank.

Both substrate corners use substrate primaries as their specialization parameters (q=2 = field size; t = q^{3/2} = ρ_2-encoded).

## 4. Substrate-side identifications at other corners (candidates)

| Macdonald-Koornwinder corner | Substrate aspect candidate |
|---|---|
| **Hall-Littlewood (q=0, t=2)** | substrate Hall algebra (RIGOROUS, A1 paper) |
| **Jack ((q,t)→(1,1), t=q^{N_c/2})** | substrate geometry / Wallach spherical functions (RIGOROUS, A3 paper) |
| **Schur (q=t)** | "blended" limit; no clear substrate role yet |
| **q-Whittaker (t=0)** | candidate: boundary/Hardy-space Whittaker representations; cross-link to B3 |
| **Full Macdonald (generic q,t)** | path from Hall-Littlewood to Jack — substrate deformation? |
| **Full Koornwinder BC_2 (4-parameter)** | natural ambient for affine extension + boundary deformations + bulk-color etc. |

## 5. Multi-week explicit work

To IDENTIFY substrate aspects at other corners explicitly:
- Compute Koornwinder BC_2 polynomials at substrate-natural parameter values; check for substrate-primary structure.
- Identify Whittaker-corner specializations and check against substrate Hardy-space structure.
- Path-track substrate evolution from Hall-Littlewood to Jack through (q,t) plane.

## 6. Honest scope + tier

**RIGOROUS** (existing math):
- Macdonald polynomials and corners (Macdonald 1995, classical).
- Koornwinder BC_n generalization (4 boundary parameters).
- Substrate's two-corner occupancy (Hall-Littlewood + Jack, A1+A3 papers).

**MAPPED (this v0.1)**: other corners (Schur, q-Whittaker) and Koornwinder BC_2 as candidate substrate-aspect locations.

**OPEN (multi-week)**: explicit identification of substrate aspects at non-Hall-Littlewood/non-Jack corners; explicit Koornwinder BC_2 computation with substrate parameters.

**Cal #27 / honesty**: v0.1 is a TERRITORY MAP. The substrate's two-corner occupancy is rigorous; the other-corner mappings are CANDIDATES (q-Whittaker ↔ Hardy boundary is most promising via Langlands connection). Multi-week explicit polynomial work.

**Routed**: → Elie: explicit Koornwinder BC_2 polynomial computation at substrate q=2; check substrate-primary structure of coefficients. → Grace: catalog scan for Whittaker function appearances in substrate Hardy-space work. → me: continuing to Lyra Queue #9 = B5 VOA / Monster cross-reference.

— Lyra, B2 Macdonald-Koornwinder other corners v0.1. Substrate's two-corner occupancy (Hall-Littlewood = algebra, Jack = geometry) noted. Other Macdonald corners (Schur, q-Whittaker) mapped to candidate substrate aspects; q-Whittaker ↔ Hardy boundary is most promising (Langlands cross-link to B3). Full Koornwinder BC_2 4-parameter family is the natural ambient for affine extensions + boundary deformations + bulk-color future work. Multi-week explicit polynomial computation needed.
