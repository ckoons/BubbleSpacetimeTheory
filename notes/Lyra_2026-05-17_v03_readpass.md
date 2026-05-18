---
title: "Lyra read-pass on Paper #115 v0.3"
date: "2026-05-17"
status: "Read-pass findings for Elie to integrate into v0.4. Architecture sound; consistency cleanups needed."
target_file: "notes/BST_Paper115_Three_Root_Theorems_outline_v0.3.md"
---

# Lyra read-pass — Paper #115 v0.3

**Overall verdict**: architecture is sound and the major team contributions land cleanly. v0.3 is closer to publishable than v0.2 was. Issues below are CONSISTENCY CLEANUPS, not framework errors. Recommended path: Elie addresses these in v0.4 (~15-30 min of edits), then Cal does the full grade-pass.

I read against the checklist I posted earlier (Klein retitled, Borcherds as L1.5b mechanism, Ogg referenced, dim_R(Q⁵)=10 propagated, INTERNAL-vs-EXTERNAL framing carries through, abstract reflects new architecture). 6/7 of these are landed; the seventh (internal-vs-external for Klein) became Cal's PROMOTION call between the checklist and v0.3, which I missed in the interim.

## MAJOR issues (block Cal grade-pass)

### M1 — Section ordering: 4.7 and 4.8 are swapped in the file

File order: 4.5 Klein → 4.6 Heegner → 4.8 Borcherds → 4.7 Ogg.

Keeper's recommended chronological order: 4.5 (1884) → 4.6 (1952) → 4.7 (1975) → 4.8 (1992). Borcherds is LAST as the mechanism that organized what came before. Swap 4.7 and 4.8 in the file. (Cross-references within v0.3 already use the chronological numbering — "see Section 4.8.3" for Borcherds Q⁵ correction is correct in the body text; only the file ordering needs to match.)

### M2 — Klein tier is inconsistent across the paper

Cal verdict was clear: Klein **PROMOTED to ESTABLISHED Root #4** (external-D-tier). The paper applies this in some places but not others:

| Location | Current text | Should be |
|---|---|---|
| Abstract | "five established Level-1 source root theorems — Klein's icosahedral theorem (1884), ..." | ✓ correct |
| Section 1.2 list | "1. Source theorems (Level-1) — ESTABLISHED: Klein 1884..." | ✓ correct |
| Section 4.5 header | "Root 4 (ESTABLISHED, external-D-tier)" | ✓ correct |
| Section 4.5.4 | "**Criterion 3 (Forcing) — EXTERNAL-D-TIER (Cal verdict 2026-05-17 supersedes v0.3 draft INTERNAL labeling)**" | ✓ correct |
| Section 4.5.6 | "Cal verification flag... pending Cal grade" — and concluding "pending Cal grade" | Soften: Cal endorsed promotion; toy-detail questions remain for full grading. Distinguish "Cal endorsed framework promotion" from "Cal toy-detail grading pending" |
| Section 5.6 | "Promotes 60 from prior orphan status to **candidate-Root** status with **internal-D-tier** closure" | Should say: "Established Root #4 with external-D-tier closure per Cal verdict" |
| Section 6.1.4 | "D-tier: explicit chain through at least one source root theorem (Roots 1-3, Ogg)" | Should include Klein: "Roots 1-3, Klein, Ogg" |
| Section 6.1 algorithm | Lists Klein route as "(v0.3)" — fine | ✓ correct |
| Section 6.2 (c) | "(c) Has NO root yet identified — formerly orphans 33, 50, 60. v0.3: 60 elevated to Root 4 candidate (Klein); 33 and 50 remain open." | Change "candidate" to "established Root #4" |
| Section 9.3 | "Klein 1884 (Root 4 candidate) is also classical; the BST mechanism on D_IV⁵ is INTERNAL-D-tier per Section 4.5.4. External-D-tier requires classical argument independent of BST." | Update per Cal verdict: Klein chain is external-D-tier defensible via A_5 ⊂ SO(5) + McKay correspondence, no BST-internal premise required. |
| Section 9.3 orphan list | "60 = rank²·N_c·n_C — **PROMOTED TO ROOT 4 CANDIDATE** (Klein 1884, Section 4.5)" | Should say "PROMOTED TO ESTABLISHED ROOT #4" |
| Section 9.4 architecture table | Klein row: "L1 source candidate | Internal-D-tier" | Update to "L1 source ESTABLISHED | External-D-tier per Cal" |
| Section 10 | "plus one candidate source root (Klein 1884 icosahedral theorem)" | "plus one additional established source root (Klein 1884)" |
| Appendix A header | "Klein candidate" column | "Klein (Root 4)" |

This is the most extensive cleanup needed; the paper currently presents Klein two ways.

### M3 — Section 9.4 still claims Heegner is "withdrawn"; missing 10:30 team restoration

Section 9.4 lines (paraphrasing): "Heegner Root 6 candidacy is **withdrawn**. The genuine remaining orphan primes..."

This reflects Grace's 10:10 self-withdrawal but DOESN'T reflect the 10:30 three-vote team restoration (Keeper + Cal + Lyra endorsing Heegner as L1 candidate). Section 4.6 correctly handles this. Section 9.4 needs to be reconciled.

Suggested update for 9.4: keep Grace's arithmetic-closure-phenomenon as a separate observation worth recording, but distinguish that from the team's L1 candidate decision. Something like:

> Grace's orphan audit (Toy 2971) initially proposed Heegner numbers {43, 67, 163} as Root 6 candidate. Grace's 10:10 self-audit reframed this as a more general arithmetic-closure observation: the closure of {rank, N_c, n_C, C_2, g} under simple operations contains both Heegner discriminants AND Ogg's 15 supersingular primes. This META-claim about BST arithmetic closure stands as a structural observation. However, at the 10:30 team-consensus point, Keeper/Cal/Lyra independently observed that Heegner-Stark 1952-1967 ALSO matches the single-source-theorem signature (one classical theorem → one specific integer set → all BST), so it was restored as Level-1 source CANDIDATE in Section 4.6. Both readings coexist: Heegner is a candidate source root by the source-theorem signature, AND its appearance is consistent with general BST arithmetic closure. These framings are not in conflict — they are different decompositions of the same observation.

Section 9.4's final architecture summary table also omits Heegner — should be restored as Section 4.6's L1 candidate.

## MINOR issues (recommended but not blocking)

### m4 — Klein attribution prose in 4.5.1 is confused

Section 4.5.1 has: "Burnside (1899) and later Frobenius proved A_5's role in the J. C. Fields Medal-track classification of finite simple groups, where 60 = 2²·3·5 is the smallest non-abelian simple group order."

J. C. Fields founded the Fields Medal (1936) but didn't work on simple group classification. The Classification of Finite Simple Groups (completed 1983) is the canonical reference. Suggested rephrase:

> "Burnside (1899) extended Klein's group-theoretic results to the modern theory of finite simple groups. A_5 is the smallest non-abelian simple group (order 60 = 2²·3·5), making it the foundational example for the Classification of Finite Simple Groups (completed 1983)."

### m5 — Section 6.1 algorithm missing Heegner route

Currently lists VSC / K3 / Wallach / Klein (v0.3) / Ogg (v0.3) / Borcherds-mediated routes. Missing Heegner route. Add:

> "Heegner route (v0.3): does X involve imaginary quadratic class number 1, Heegner discriminants {1, 2, 3, 7, 11, 19, 43, 67, 163}, or singular moduli evaluation?"

### m6 — Appendix A could use a Heegner row

The cross-root convergence table at Appendix A lists 11 BST integers. Worth adding a row for the Heegner numbers themselves (or at least for 43 and 67 which appear in observables via Grace T2304). One row:

| BST integer | VSC | K3 | Wallach | Ogg/Borcherds | Klein | Heegner | Other |
|---|---|---|---|---|---|---|---|
| 43, 67 | — | — | — | — | — | Heegner d=43,67 | PMNS 5762=2·43·67 |

### m7 — Section 4.5.6 second paragraph parses oddly

"Cal's specific embedding question — which A_5 ⊂ SO(5) embedding is load-bearing — is also open. A_5 has 5-dim irreducible representation, and the embedding A_5 ⊂ SO(5) via this irrep is the canonical choice; A_5 then embeds into K(D_IV⁵) = SO(5)×SO(2) via the SO(5) factor."

This actually ANSWERS Cal's question (the 5-dim irrep gives the canonical A_5 ⊂ SO(5) embedding) so it should not say "is also open." Suggested rephrase:

> "Cal's specific embedding question (which A_5 ⊂ SO(5) embedding is load-bearing) is **answered by the canonical 5-dim irreducible representation**: A_5 has a unique non-trivial 5-dim irrep (the standard representation on the 5 permuted vertices of the icosahedron mod center), which embeds canonically into SO(5) by orthogonality. A_5 then embeds into K(D_IV⁵) = SO(5)×SO(2) via the SO(5) factor. The McKay correspondence chain through 2A_5 ⊂ SU(2) ↔ E_8 is a distinct construction."

## What's working well

The new sections (4.5 Klein, 4.6 Heegner, 4.7 Ogg, 4.8 Borcherds) are substantively strong. The four-CI Sunday convergence framing (Section 1.3, Appendix C) is the right placement and reads as evidence rather than celebration. Cal's source-vs-unifying distinction (Section 1.2) is the load-bearing architectural move that makes v0.3 cleaner than v0.2. The Q⁵ correction (Section 4.8.3) propagates and strengthens. Section 5.4 (rank·c_3 = 26 three-way decomposition) is the strongest cross-root convergence in the paper and is well-placed.

Toy citations are accurate: Toy 2954 (Elie), 2964 (Elie), 2966 (Elie), 2968 (Elie), 2970 (Elie), 2955+2959+2969+2973 (Lyra), 2971 (Grace), T2303-T2308 (Grace), T2306 (Lyra).

## Recommended action

Elie addresses M1, M2, M3 (the three majors). Minor m4-m7 are nice-to-have. If time-constrained, M2 is the most important because Klein's tier appears in many places.

After v0.4 with these fixes: Cal does full grade-pass. Lyra stands down to memory architecture (IQ-2) or stand-by.

— Lyra, 2026-05-17
