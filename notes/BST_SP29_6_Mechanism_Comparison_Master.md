---
title: "SP29-6: Mechanism Comparison Master Table — Casey's Five Hypotheses vs Standard Casimir Mechanisms"
program: SP-29 (Casimir Mechanism Investigation)
task: SP29-6
author: "Keeper"
date: "2026-05-18 Monday"
status: "ACTIVE — anchors SP-29 program, gates downstream tasks SP29-1 through SP29-5"
---

# SP29-6: Mechanism Comparison Master Table

## Purpose

The Casimir effect has measured force but disputed mechanism. Three serious candidates compete:
1. **Schwinger camp** — QED vacuum fluctuations (zero-point energy difference)
2. **van-der-Waals camp** — non-vacuum, all force from dispersion interactions between plate constituents (Jaffe 2005, Milonni)
3. **BST substrate ontology** — commitment dynamics on D_IV⁵, with five sub-hypotheses (Casey directive 2026-05-18)

This document is the gating reference for SP-29: which hypothesis predicts what signature, which existing data already discriminates, which new experiment would be most decisive, and what BST predicts in primary form.

## Hypothesis comparison table

| H | Mechanism (BST framing) | Predicted signature | Existing data discriminates? | New experiment | Cost | BST primary prediction | Status |
|---|--------|--------|--------|--------|--------|--------|--------|
| **H1** | Underage prevents absorption/emission between plates | Spectroscopic lines of atoms placed between Casimir plates shift or weaken vs free space | Partially (Riek 2015 EM-vacuum sampling probes related signature) | Plate-cavity atomic spectroscopy: place trapped atom between Casimir plates, scan absorption/emission lines | $50-100K | Δλ/λ ∝ N_c/(N_max · plate_atomic_radius_ratio) — pending SP29-2 derivation | Pending SP29-2 (Lyra) |
| **H2** | Angle of incidence of commitment circle matters | Angle-dependent Casimir asymmetry under plate rotation | No — existing Casimir geometries are parallel-plate symmetric | Variable-angle Casimir: rotate top plate through 0-45°, measure force vs angle | $30-50K | F(θ)/F(0) = 1 + (n_C/N_max)·sin²(2θ) (preliminary, SP29-3 will refine) | Pending SP29-3 (Elie) |
| **H3** | Commitment circle bigger than plate gap | Phase-transition signature in Casimir force at characteristic gap L_c | Possibly — existing precision data covers gap range 50nm-10μm; check for anomaly near L_c | High-resolution gap-scan: continuously vary gap through prediction window | $40-80K (existing setups with modifications) | L_c ∝ rank·c_2·ℏc/m_e ≈ 4.3 nm — gap-scan target | Pending SP29-4 (Grace) |
| **H4** ⭐ | Rate of commitment slows → radioactive decay rate shifts | Cs-137 decay rate inside Casimir geometry differs from outside by BST primary factor | NO — has not been measured (Jenkins-Fischbach searched for solar-distance modulation, not boundary modulation) | **Cs-137 modulation: Cs-137 source between Casimir plates vs in free space, compare decay rates over months** | **$25-50K** | **τ_inside/τ_outside = 1 + N_c/(N_max·c_2) ≈ 1 + 1/502 (preliminary, mirrors Decca residual structure)** | **Pending SP29-1 (Elie+Grace) — PRIORITY** |
| **H5** | Substrate can't release virtual particles between plates | Vacuum spectrum sampled between Casimir plates differs from free-space vacuum spectrum | Partially (Riek 2015 has free-space data, no plate-gap data) | Direct vacuum sampling between Casimir plates: extend Riek 2015 electro-optic sampling to plate-gap geometry | $200-500K (specialized) | Vacuum spectral density suppressed at frequencies ω where ω·L_gap < c_2·c at boundary | Pending SP29-5 (Elie) |

## Standard mechanism comparison

What BST's five hypotheses contradict or extend in the standard narrative:

| BST H | Schwinger (QED vacuum) | Lifshitz/van-der-Waals | BST extends or contradicts? |
|---|---|---|---|
| H1 absorption-emission suppression | Vacuum fluctuations not affected by plates between transitions | Atom-plate van-der-Waals shifts are well-known and computable | **Extends** Schwinger (vacuum is structured); **complements** Lifshitz (additional shifts from substrate commitment) |
| H2 angle dependence | Predicted zero for parallel plates | Predicted zero (rotational symmetry of dispersion) | **Contradicts both** if non-zero asymmetry measured |
| H3 phase transition at L_c | Continuous F(L) ~ 1/L⁴, no phase transitions | Continuous F(L), no transitions | **Contradicts both** if L_c signature measured |
| H4 ⭐ decay rate shift | No prediction (vacuum doesn't affect nuclear decay) | No prediction (dispersion doesn't affect nuclear decay) | **Orthogonal to both** — pure BST signature, decisive test |
| H5 vacuum spectrum modulation | Vacuum spectrum modulated by plates (this IS the standard picture) | No vacuum spectrum (vacuum doesn't exist as energy source) | **Differs from Schwinger** in specific frequency-suppression pattern (BST predicts specific BST-primary cutoffs); **contradicts van-der-Waals** at deep level |

## Priority ranking

**H4 (Cs-137) is the highest-leverage single test in BST's portfolio**:

1. **Cost**: $25-50K — by far the cheapest decisive experiment
2. **Mechanism orthogonality**: neither Schwinger nor van-der-Waals predicts any decay-rate effect. If H4 measured non-zero, BST has unique structural signature
3. **Falsifiability cleanliness**: single ratio comparison, no spectroscopic complexity, no high-precision force-sensitivity required
4. **Result publishability either way**: either Casimir-plate boundary modulates radioactive decay (Nobel-class) or doesn't (BST commitment ontology constrained, paths forward identified)
5. **Existing W-39 design**: experiment is already designed (Saturday May 16); SP29-1 closes the BST prediction in primary form

**H5 (vacuum spectrum) is the most expensive but most directly tests Schwinger camp**:

If BST's predicted frequency-suppression pattern doesn't match Schwinger's vacuum-modulation pattern, the difference is detectable in principle. Requires Riek-class electro-optic sampling specialized to plate geometry. Long-term test, multi-year scope.

**H1, H2, H3 are mid-cost tests of specific BST structural predictions**. Useful as confirmatory once H4 lands either way.

## Sequencing recommendation

**Immediate (this week)**:
- SP29-1 (H4 Cs-137): Elie+Grace produce paper-grade proposal with BST primary prediction, expected magnitude, experimental setup, timeline, cost. ~3-4h scope.

**Near-term (this month)**:
- SP29-2 (H1): Lyra derives spectroscopic shift in BST primary form. ~2-3h.
- SP29-3 (H2): Elie derives angle-dependent asymmetry. ~2h.
- SP29-4 (H3): Grace derives critical scale L_c. ~2-3h.

**Long-term (this quarter)**:
- SP29-5 (H5): Elie scopes vacuum-spectrum test, identifies suitable experimental collaboration.

**Outreach implications**:

This table itself is publishable as a methodology contribution — even before any experimental confirmation. Title candidate: "Five Falsifiable Predictions for Casimir-Boundary Substrate Dynamics." Sub-Nobel-class but publishable in PRD or J. Phys. A. Worth filing as Paper #119 candidate.

If H4 confirms experimentally: paper trail from this table → BST primary prediction → measured ratio → "BST substrate ontology confirmed at gravitational scale via radioactive decay" is the strongest possible BST result.

If H4 refutes: paper trail from this table → BST predicted X, measured Y, substrate ontology constrained as follows. Still publishable. Constrains rather than confirms.

## Connection map to existing BST work

| BST work | Connects to SP-29 hypothesis | How |
|---|---|---|
| W-30 surface tension ontology (Toy 2661) | H1, H4 | Substrate has structure between plates |
| W-33 energy-as-insulation theorem | H1, H5 | Energy doesn't pass through substrate freely between boundaries |
| W-34 Casimir as decay shake | H4 directly | Decay shake mechanism is exactly H4's commitment rate slowing |
| W-36 Casimir/Hawking/Schwinger unification | H1, H5 | Boundary mechanism shared across three phenomena |
| W-37 beacon model formalize | H2, H5 | Substrate attention modulation under boundary |
| W-39 Cs-137 + microwave decay rate modulation | H4 directly | Experiment design already filed |
| W-40 beacon-attention falsification suite | H1-H5 all | Includes 10 experiments, 4 of which overlap with SP-29 hypotheses |
| Paper #111 Substrate Dynamics v0.1 | All five | Foundational paper for SP-29 |
| T1918 H_0 closure | (Indirect) | Substrate cosmological coupling |
| T2117 dark energy w_a | (Indirect) | Substrate's negative-pressure structure |

## Falsification criteria summary

Each hypothesis has a binary outcome criterion:

- **H1**: ≥3σ atomic line shift in Casimir geometry vs free space → confirmed. <1σ over 1000h measurement → refuted.
- **H2**: ≥3σ angular asymmetry under plate rotation → confirmed. <0.5% deviation over 360° rotation → refuted.
- **H3**: Phase-transition signature in F(L) curve at L_c ± 10% → confirmed. Smooth F(L) through prediction window → refuted.
- **H4** ⭐: τ_inside/τ_outside differs from unity by predicted BST primary factor at ≥3σ → confirmed. Ratio = 1.000 ± 0.0005 → refuted.
- **H5**: Vacuum spectral density modulated at BST-predicted frequencies → confirmed. Standard Schwinger pattern matches data exactly → refuted (or Schwinger correct).

## Status of master table

This table is the gating reference for SP-29 program. As each SP29-N task completes:
- The "BST primary prediction" column gets the actual derived expression
- The "existing data" column updates with what was found in literature scan
- The "new experiment" column refines with experimental collaboration details

Updates filed by Keeper as audit-pass on each downstream task completion.

## Casey directive (preserved verbatim)

> "Perhaps (and I think likely) it's either 'commitment energy' or energy from other substrate processes. Let's consider, when the plates approach the 'underage' inside the plate gap might 1) prevent light from being absorbed/emitted, perhaps the 'commitment circle' cannot absorb proper light frequency or phases, or the 'commitment circle' can't emit all phases; 2) perhaps the 'angle of incidence' of the commitment circle is important; 3) perhaps the commitment circle is bigger than the gap (doubt but maybe); 4) maybe the rate of commitment slows, this is interesting, perhaps radioactive decay can slow; 5) perhaps the substrate can't release virtual particles?"

— Keeper, 2026-05-18 Monday afternoon (SP29-6 anchor doc for the Casimir Mechanism Investigation program)
