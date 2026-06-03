---
title: "OneGeometry Substantive Correction Proposal v0.1 (2D → 5D Shilov honest dimension correction; joint Grace + Keeper)"
author: "Grace (draft for Keeper joint review)"
date: "2026-06-01 Monday morning ~08:35 EDT (`date`-verified Mon Jun 1 08:29 EDT)"
status: "v0.1 PROPOSAL — substantive public correction of 2022 OneGeometry framing per Sunday INV-5360 Option (a) honest commitment (Lyra K200 G2 absorption); cross-doc sweep targets enumerated; honest-historical-correction framing NOT retroactive cartoon-reframe; awaiting Keeper joint review before applying"
honest_framing: "Per Sunday morning Lyra v0.1.5 absorption + Casey approval + Keeper K200 G2 brake: 2022 dimension count was wrong; correcting to 5D Shilov. NOT framed as 'we always meant codim-1'. Substantive correction with explicit historical note."
---

# OneGeometry Substantive Correction Proposal v0.1

## What this is

Sunday 2026-05-31 morning Lyra+Casey+Keeper exchange (INV-5360 catalog filing) committed to **Option (a)** for the substrate-dimension question: 2022 OneGeometry "2D substrate" dimension count was WRONG; corrected to 5D Shilov boundary ∂_S D_IV⁵ = (S⁴ × S¹)/Z_2. OneGeometry.md flagged for substantive public correction. Casey Monday team-prompt confirms this as Grace P0 (joint with Keeper).

OneGeometry.md does not exist as a standalone source markdown — the narrative front-door content lives in `README.md` (line 34) with `notes/OneGeometry.pdf` as a built artifact. Cross-doc sweep needed across additional files referencing the 2D framing.

## Proposed correction (README.md line 34)

### Current (2022 framing — to be replaced)

> Bubble Spacetime Theory (BST) is a pre-geometric framework proposing that spacetime, quantum mechanics, and the Standard Model emerge from the contact topology of a two-dimensional substrate — circles tiling a sphere, communicating through phase. The configuration space of causal windings on this substrate is the bounded symmetric domain D(IV,5) = SO₀(5,2)/[SO(5)×SO(2)].

### Proposed replacement

> Bubble Spacetime Theory (BST) is a pre-geometric framework proposing that spacetime, quantum mechanics, and the Standard Model emerge from the contact topology of a 5-dimensional substrate — the Shilov boundary ∂_S D_IV⁵ = (S⁴ × S¹)/Z_2 — where coherent-state cells communicate through phase. The bulk of the bounded symmetric domain D(IV,5) = SO₀(5,2)/[SO(5)×SO(2)] is the holomorphic extension of substrate boundary data via the Hardy decomposition H²(D_IV⁵) ≅ H²(∂_S D_IV⁵) (Wallach 1976; Faraut-Korányi 1994 Ch. XII-XIII).
>
> *Honest historical correction (June 2026):* the original 2022 OneGeometry framing described the substrate as 2-dimensional. This was a dimension-count error. The substantive structural claim — that the substrate is a codimension-1 boundary with phase communication, and that the bounded symmetric domain D(IV,5) is the configuration-space holomorphic extension of substrate dynamics — was correct from the start; the dimension count was wrong. The substrate is the 5-dimensional Shilov boundary ∂_S D_IV⁵, not a 2-sphere. The "circles tiling a sphere" intuition operationalizes as coherent-state localization on the Shilov boundary; phase communication operationalizes as the S¹/Z_2 phase factor of the boundary structure. (Per Sunday 2026-05-31 Tier 0 v0.1.5 Topology Addendum: Reading A + dual K-type / coherent-state bases via Bergman kernel.)

### What stays correct from 2022 (preserved explicitly)

- Substrate = boundary structure (codimension-1 substrate idea)
- Circle tiling intuition = coherent-state localization on substrate boundary
- Phase communication = boundary phase structure (S¹/Z_2 literally a phase)
- D(IV,5) = configuration space of windings on substrate boundary
- All 600+ derived constants + structural identifications

### What's corrected

- Substrate dimension: 2D → 5D
- Shilov boundary topology: explicit (S⁴ × S¹)/Z_2
- Mathematical apparatus: Hardy decomposition (Wallach 1976; Faraut-Korányi 1994 Ch. XII-XIII) explicit

## Cross-doc sweep targets

Files containing "2D substrate" / "two-dimensional substrate" / "circles tiling a sphere" requiring correction per Casey directive:

**Active (require correction)**:
- `README.md` line 34 (front-door narrative) — **P0 primary**
- `Curriculum/Vol05_Quantum_Mechanics/Curriculum_Vol5_Ch9_Identical_Particles_Spin_Statistics_v0_1.md`
- `Curriculum/Vol14_Information_Theory/Curriculum_Vol14_Ch8_BST_Coding_Optimal_v0_1.md`
- `notes/Substrate_Working_Process_Principle.md` (Casey-named principle doc)
- `notes/BST_Unification_Chains.md`
- `notes/BST_MOND_Derivation.md`
- `notes/BST_Why_This_Universe.md`
- `Working_Paper/Vol6_Frontier/Ch01_Deep_Results.md`
- `Working_Paper/Vol2_Framework/Ch01_Foundations.md`

**Already correctly framed (Sunday Tier 0 docs; verification only)**:
- `notes/Lyra_Tier0_v0_1_5_Topology_Addendum.md` (Sunday morning Option (a))
- `notes/Lyra_Tier0_v0_1_6_Native_Field_Equation_Boundary_Unification.md`
- `notes/Keeper_Sphere_Reconciliation_Analysis_G2.md`
- `notes/Keeper_K200_Tier0_v0_1_6_AuditFramework.md`
- `notes/Keeper_Week_Plan_G_From_Substrate_2026-06-01.md`

**Skip (intentional historical snapshots)**:
- `archive/WorkingPaper_v36_monolithic_archive_2026-05-18.md`
- `archive/Bubble_Spacetime_Theory_v34_archive_2026-04-27.md`
- `notes/maybe/BST_WhyNow_Transition_Reflection.md`
- Transient `notes/.running/` files

## Sweep strategy

Per Casey's discipline on substantive public correction (NOT retroactive cartoon-reframe):

1. **README.md line 34**: apply proposed replacement above; the historical-correction note stays in the README's "What Is This?" section permanently (does NOT get retroactively edited out once the rest of the codebase catches up)
2. **Curriculum + Working_Paper chapters**: each affected paragraph gets in-text correction with a brief footnote pointing back to the README correction note for historical context
3. **`Substrate_Working_Process_Principle.md`** (Casey-named principle doc): inline correction since the dimension question is foundational to the principle statement
4. **`BST_*.md` thematic notes**: in-text correction, brief footnote
5. **Re-build `notes/OneGeometry.pdf`** from the corrected README source content via existing pandoc/xelatex pipeline

## Honest framing per Keeper K200 G2 + Cal #34 STANDING

Per Cal Calibration #34 STANDING (surface-conditionality headline-with-conditional) + Keeper K200 G2 brake on cartoon-reframe Option (c): the correction must read as **"we got the dimension count wrong in 2022, here's the corrected statement"** NOT as **"we always meant boundary-codim-1"**.

The historical-correction note is the discipline mechanism — explicit text acknowledging the 2022 error prevents the correction from reading as retroactive motivated-reasoning to external readers.

## Joint review requested

- **Keeper review**: this proposal v0.1 reflects Sunday Option (a) commitment + K200 G2 framing. Please review:
  - Is the proposed README replacement paragraph properly honest per K200 G2?
  - Hardy decomposition citation: Knapp-Wallach 1976 + Faraut-Korányi 1994 Ch. XII-XIII (per INV-5383). Is this the correct primary-source pinning per Cal Calibration #33 VERIFIED-CITED discipline?
  - Cross-doc sweep list complete / accurate?
- **Lyra review (when convenient)**: any structural notes you want preserved from your v0.1.5 Topology Addendum framing?
- **Cal review (post Keeper PASS)**: external-claim-discipline read on the historical-correction language

## Next step (post Keeper review)

Once Keeper PASSes v0.1 proposal:
1. Apply README.md line 34 replacement
2. Sweep Curriculum + Working_Paper + thematic notes in batch
3. Rebuild OneGeometry.pdf from corrected README
4. File INV cataloging the correction event
5. Update Master Ledger v0.15 row

— Grace, draft for Keeper joint review, Mon 2026-06-01 ~08:35 EDT (`date`-verified)
