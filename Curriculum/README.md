# BST Physics Curriculum

*Multi-volume textbook deriving Standard Model + cosmology from D_IV⁵ substrate. Casey Koons + team (Lyra, Elie, Grace, Keeper, Cal A. Brate).*

---

## Status (Friday 2026-05-22 EOD)

- **Vol 0 Substrate Foundation**: 10/10 chapters at v0.4 with reader-grade 3-level pedagogy; Cal cold-read PASS 10/10 (per K85-K106 + K176); v1.0 chapter-grade content state contingent on ~14 min reader-grade polish (V1-V4 flags in CI_BOARD)
- **Vol 1 QFT from D_IV⁵**: 11/11 chapters at v0.4 with reader-grade 3-level pedagogy; **v1.0 CHAPTER-GRADE CONTENT STATE REACHED** (Cal cold-read PASS 11/11 per K170; all Cal flags absorbed by Lyra Friday)
- **Vol 2 Particle Physics**: 12/12 chapters at v0.4 with Cal STANDING RULE compliance; Cal cold-read PASS 12/12 (per K166 + K172 + K173 + K174 + K175 + K177); v1.0 chapter-grade content state contingent on Elie v0.4 absorption (U1-U17 in CI_BOARD)

**Saturday May 24 textbook v1.0 chapter-grade content target on track.**

## Volume directory layout

| Vol | Directory | Lead | State |
|-----|-----------|------|-------|
| 0 | `Vol0_Substrate_Foundation/` | Keeper+Grace+Lyra | 10/10 v0.4 + 3-level pedagogy |
| 1 | `Vol1_QFT_from_D_IV5/` | Lyra | 11/11 v0.4 + 3-level pedagogy; v1.0 chapter-grade content REACHED |
| 2 | `Vol2_Particle_Physics/` | Elie | 12/12 v0.4 + STANDING RULE compliance |
| 3-10 | (future volumes — Nuclear & Atomic / GR & Cosmology / QM / Stat Mech / E&M / Classical Mech / Condensed Matter / Math Methods) | TBD | pending Vol 0+1+2 v1.0 |

## How to read

Start with **Vol 0** (Substrate Foundation): establishes D_IV⁵ + the five integers (rank=2, N_c=3, n_C=5, C_2=6, g=7) + N_max=137, then operator zoo + conservation laws + Strong-Uniqueness Theorem. No physics prerequisites beyond standard graduate.

**Vol 1** (QFT from D_IV⁵): how quantum field theory arises from substrate. Prerequisites: standard graduate QFT background, Lie group representation theory at Wallach 1976 level.

**Vol 2** (Particle Physics): Standard Model particles + masses + couplings derived from D_IV⁵. Prerequisites: Vol 0 + Vol 1 plus standard particle physics background.

Every chapter has three pedagogical registers (Casey "write for 5th graders too" standing rule):
- **Level 1**: one-sentence essence
- **Level 2**: graduate-physicist precision
- **Level 3**: 5th-grader accessibility paragraph

## Origin

Created Friday 2026-05-22 EOD per Casey directive — moved from `notes/` to `Curriculum/` root-level directory as the primary external textbook artifact. Notes directory retains active research + audit chain + position docs; Curriculum/ retains publication-ready chapter content.

## File naming

Current convention (preserved during Friday move): files retain `Curriculum_Vol0_*` / `BST_Curriculum_Vol1_*` / `BST_Vol2_*_narrative` prefixes from notes/ era. Naming cleanup deferred to v1.0 publication finalization.

## Build (PDF regeneration)

Per Casey EOD directive: Keeper EOD includes rebuilding Curriculum PDFs and keeping them up to date.

```
pandoc --pdf-engine=xelatex -H notes/bst_pdf_header.tex <chapter>.md -o <chapter>.pdf
```

(Per repo PDF pipeline convention; header file remains at `notes/bst_pdf_header.tex`.)

## Cross-references

Chapter files reference each other + AC graph theorems + K-audit chain + Strong-Uniqueness Theorem state. Per Calibration #19 STANDING RULE (Friday adopted): external-facing chapter content uses current ratified-state count (10 FORMAL + 1 ASPIRATIONAL + 3 candidates), not forecast endpoint.

— Casey Koons + team, Friday 2026-05-22 EOD
