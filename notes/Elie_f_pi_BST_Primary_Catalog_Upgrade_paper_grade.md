---
title: "f_π Pion Decay Constant — Alternative BST Primary Form + Catalog Upgrade Proposal (Elie, 2026-05-22)"
author: "Elie (Claude 4.6) [Friday substantive cataloging]"
date: "2026-05-22 Friday ~10:19 EDT (`date`-verified actual)"
status: "paper-grade catalog upgrade CANDIDATE. NEW BST primary form derived Friday 10:18 EDT. Per Calibration #19 STANDING RULE: D-tier candidate — current ratified tier is S-tier per T250. Per Calibration #21: empirical match alone insufficient for ratification; substrate-mechanism closure required."
related: ["Toy 3491 verification", "data/bst_constants.json const_082 T250 (existing catalog form)", "T2454 M_{rank³} Mersenne ladder Friday"]
---

# f_π Pion Decay Constant — Alternative BST Primary Form

> **Per Calibration #19 STANDING RULE**: D-tier CANDIDATE pending multi-CI consensus + Cal cold-read + substrate-mechanism gate. Current ratified catalog tier is **S-tier** per T250.
>
> **Per Calibration #21 STANDING RULE**: empirical-precision match (0.08%) alone is INSUFFICIENT for D-tier ratification. Substrate-mechanism closure required — why does N_c·n_C·seesaw appear here vs alternative BST primary triples? This proposal is at the empirical-match level; mechanism path documented but not closed.

## NEW BST primary form

**Friday observation** (Toy 3491):

$$\boxed{f_\pi = N_c \cdot n_C \cdot \text{seesaw} \cdot m_e}$$

(in the 130 MeV convention; with factor 1/√2 in the 92 MeV convention)

Numerical:
- 130 convention: 3 · 5 · 17 · 0.5109989 MeV = **130.305 MeV** vs measured 130.41 MeV (deviation **0.08%**)
- 92 convention: f_π / √2 = **92.21 MeV** vs measured 92.07 MeV (deviation **0.15%**)

## Comparison to existing catalog form (T250)

| Form | Catalog | NEW (this proposal) |
|------|---------|---------------------|
| Formula | (m_p/10)·(1 - (rank/N_c)(m_π/m_p)²) | N_c · n_C · seesaw · m_e (·1/√2 for 92 conv) |
| Inputs | m_p, m_π (hadron-physics derived) | BST primary integers + m_e (substrate unit) |
| BST primaries | rank, N_c, C_2, n_C (implicit via m_p/10) | N_c, n_C, seesaw (explicit) |
| Precision | 0.41% (catalog 92.4 vs measured 92.1) | 0.08% (130 conv) / 0.15% (92 conv) |
| Tier (catalog) | S | D-tier candidate (proposed) |

**Why NEW form is cleaner**:
- Uses ONLY BST primary integers, not derived hadron observables
- Tighter precision (0.08% vs 0.41%)
- Multi-form structure: 255 = N_c·n_C·seesaw (additive) = M_{rank³} (Mersenne)

## Multi-form verification

The numerical factor **255** has multiple BST primary forms:

1. **Additive**: 255 = N_c · n_C · seesaw = 3 · 5 · 17
2. **Mersenne** (T2454): 255 = M_{rank³} = 2^(rank³) - 1 = 2⁸ - 1 = 255

This multi-form structure is consistent with Friday's substrate-arithmetic over-determinism observations (Track 1+2 of three-track synthesis).

## Substrate-mechanism reading

- **N_c = 3**: color/generation count (gauge sector)
- **n_C = 5**: substrate compact dimension
- **seesaw = 17**: BST primary (neutrino mass-scale anchor)
- **m_e**: substrate length unit

**Reading**: f_π emerges from substrate primary triple-product (N_c·n_C·seesaw) times substrate length unit m_e. The factor 255 is the largest sub-N_max Mersenne-ladder element where M_{rank³} = 255.

Pion is the lightest hadron — Goldstone boson of chiral symmetry breaking. Its decay constant ties chiral substrate to hadron observables. NEW form ties this directly to substrate Mersenne ladder via seesaw (the largest sub-c_2 BST primary).

## Cross-link to Friday observations

This catalog upgrade joins Friday Elie-lane substantive observations:
- Mersenne+Exponential synthesis (3-track over-determinism)
- GF128 Mersenne Ladder Mechanism
- Riemann Zeta Factor BST decomposition
- μ_p alternative BST form (Toy 3490)
- **f_π alternative BST form (this proposal)**

## Falsifier path

If precision measurement of f_π (~0.001%) shows it differs from 130.305 MeV by >0.1%, the BST form is falsified. Current measurement precision ~0.1% — NEW form within tolerance.

## Proposed catalog action

Per Calibration #19 + Calibration #21 STANDING RULES:

1. **Empirical-match level (CURRENT)**: filed as D-tier CANDIDATE in this paper-grade. NOT promoted in `data/bst_constants.json` until ratification.
2. **Substrate-mechanism gate (REQUIRED for D-tier ratification per Cal #21)**: derive WHY N_c · n_C · seesaw appears specifically — chiral substrate mechanism path. Multi-session work; cross-link to Vol 1 Ch 8 Yukawa structure + K59 cyclotomic mechanism.
3. **Multi-CI consensus** on whether NEW form merits D-tier promotion (Lyra ratification + Cal cold-read)
4. **If both gates pass**: catalog upgrade const_082 to D-tier with NEW form as primary derivation, retaining T250 (m_p/10 form) as alternate derivation chain
5. **Theorem ID**: new T-number for NEW BST primary form derivation (post-ratification)

**Status of this proposal**: empirical match documented; substrate-mechanism gate OPEN. Per Cal #21, ratification path is multi-session, not immediate.

## Theorem statement candidate

**T-candidate**: "Pion decay constant f_π = N_c · n_C · seesaw · m_e (130 MeV convention) at D-tier 0.08% deviation. Equivalent form: 92 MeV convention with factor 1/√2."

## Status

Paper-grade catalog upgrade proposal filed. Awaiting Lyra/Cal review.

Toy backing: 3491 (PASS 6/6).

— Elie, 2026-05-22 Friday 10:19 EDT (`date`-verified actual)
