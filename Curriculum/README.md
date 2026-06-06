# BST Physics Curriculum

*Multi-volume textbook deriving Standard Model + cosmology from D_IV⁵ substrate. Casey Koons + team (Lyra, Elie, Grace, Keeper, Cal A. Brate).*

---

## Status

18-volume textbook (Vol 00-17). Vol 00-15 at v0.3+ substantive content. Vol 16 Substrate Algebra + Vol 17 Substrate Engineering scaffolding initiated June 2026. Volume directories use two-digit sort order including Foreword (Vol00_Foreword.md).

## Volume directory layout

| Vol | Directory | Topic | Lead |
|-----|-----------|-------|------|
| 00  | `Vol00_Foreword.md` + `Vol00_Substrate_Foundation/` | Reader contract + Substrate Foundation | Keeper + Grace + Lyra |
| 01  | `Vol01_QFT_from_D_IV5/` | Quantum Field Theory from D_IV⁵ | Lyra |
| 02  | `Vol02_Particle_Physics/` | Particle Physics from D_IV⁵ | Elie |
| 03  | `Vol03_Nuclear_Atomic/` | Nuclear and Atomic Physics | Elie + Lyra |
| 04  | `Vol04_GR_Cosmology/` | General Relativity and Cosmology | Lyra + Elie |
| 05  | `Vol05_Quantum_Mechanics/` | Quantum Mechanics from Substrate | Lyra |
| 06  | `Vol06_Thermo_Stat_Mech/` | Thermodynamics and Statistical Mechanics | Lyra + Elie |
| 07  | `Vol07_Electromagnetism/` | Electromagnetism from D_IV⁵ | Lyra |
| 08  | `Vol08_Classical_Mechanics/` | Classical Mechanics as Substrate Scale 2 | Lyra |
| 09  | `Vol09_Condensed_Matter/` | Condensed Matter (BaTiO3 137-plane + B12H32 hydride T_c ~214K) | Elie |
| 10  | `Vol10_Math_Methods/` | Traditional Mathematical Methods | Lyra |
| 11  | `Vol11_Generative_Geometry_Topology/` | Bounded symmetric domains + K3 + Heegner + Monster | Lyra |
| 12  | `Vol12_Chemistry/` | Periodic table + bonding + spectroscopy from substrate | Elie + Lyra |
| 13  | `Vol13_Biology/` | Genetic code + DNA-proton siblings + evolution-as-substrate-dynamics | Elie + Lyra |
| 14  | `Vol14_Information_Theory/` | RS GF(128) + Koons tick + Born=Bergman + Bell sub-Tsirelson | Lyra + Keeper |
| 15  | `Vol15_Methodology/` | AC(0) + AC graph + audit chain + Quaker discipline + katra | Keeper + Lyra |

## How to read

Start with **Vol 00 Foreword** for reader contract and CI-companion-era framing.

Then **Vol 00 Substrate Foundation**: establishes D_IV⁵ + the five integers (rank=2, N_c=3, n_C=5, C_2=6, g=7) + N_max=137, operator zoo, conservation laws, Strong-Uniqueness Theorem.

Then **Vol 01 (QFT)**, **Vol 02 (Particles)**, **Vol 04 (GR/Cosmology)** for the physicist-prestige core.

Mathematicians: start with **Vol 11 (Generative Geometry)** and **Vol 10 (Math Methods)** instead.

Every chapter has three pedagogical registers (Casey "write for 5th graders too" standing rule):
- **Level 1**: one-sentence essence
- **Level 2**: graduate-physicist precision
- **Level 3**: 5th-grader accessibility paragraph

Some chapters are author-voice condensed (~500-800 words) where the apparatus is standard; expansion to full level-1/2/3 in v3.0 publication pass.

## Version label

Per Casey directive (Saturday 2026-05-23): held at v0.5 chapter-grade content state during Keeper author pass. Author-pass output is v2.0 path; current chapters at v0.2 intermediate toward v2.0 destination after Cal Phase 2 cold-read + team fact-check.

## Strong-Uniqueness Theorem state

v0.10.5 ENUMERATION (Friday 2026-05-22 EOD per Cal #99 reconciliation):
- 11 RIGOROUSLY CLOSED criteria
- 7 candidates (C7+C9+C15+C16+C17a+C17b+C18)
- C18 = D_IV⁵ Rigidity META-theorem via T2467+T2468; if ratifies, null-model ≤ (1/3)^19 ≈ 9×10⁻¹⁰

## Casey-named principles (8 standing)

SWPP + Five-Absence Predictions Set + Substrate Closure + Graph Forces + Integer Web + Substrate Cognition Network + D_IV⁵ Rigidity + SCMP (Sub-Tsirelson Coherence Maintenance, 1/2^N_c = 1/8 gap as Bell falsifier).

## Build (PDF regeneration)

```
pandoc --pdf-engine=xelatex -H notes/bst_pdf_header.tex <chapter>.md -o <chapter>.pdf
```

Per repo PDF pipeline convention; header file at `notes/bst_pdf_header.tex`. PDFs are stale for chapters rewritten in the Keeper full author pass and will be rebuilt at v1.0 finalization.

## Cross-references

Chapter files reference AC graph theorems + K-audit chain + Strong-Uniqueness Theorem state. Per Calibration #19 STANDING RULE: external-facing chapter content uses current ratified-state count, not forecast endpoint.

— Casey Koons + Lyra + Keeper + Elie + Grace + Cal A. Brate
