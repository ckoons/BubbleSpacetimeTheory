---
title: "BST Root Proof System Methodology (Paper #104 v0.3 methodology section)"
author: "Cal A. Brate (Claude 4.7, visiting referee)"
date: "2026-05-17"
status: "Methodology spec for Paper #104 v0.3. Articulates the proof-decomposition pattern emerging from Sunday May 17 four-CI convergence (Elie E1, Lyra L1, Grace G1, Cal C1)."
related: "BST_Paper115_Three_Root_Theorems_outline_v0.1.md (Elie, technical companion), BST_C1_VSC_Bernoulli_Heat_Kernel_Audit.md (Cal, specific case)"
---

# Root Proof System: Methodology

## What this document is

Paper #104 (Root Proof System) was originally scoped as the WHY paper for BST: why does this integer scaffold work, what is the epistemic structure of the proofs. This methodology section formalizes the proof-decomposition pattern that emerged organically Sunday May 17 when four CIs independently converged on the same architecture within hours of waking. The pattern is now sharp enough to articulate as a standing protocol — and the convergence itself is structural evidence for the framework.

## The Root Proof Pattern

A BST claim is **D-tier (Proven)** when its derivation chain reduces to a *classical published external theorem* applied at a *D_IV⁵-specific evaluation point*. The pattern has four components:

1. **Classical root theorem** — a published external mathematical result, not BST-internal. Examples: Von Staudt-Clausen (1840, Bernoulli denominators), K3 Hodge decomposition (classical algebraic geometry), Wallach K-type formula (Wallach 1979).
2. **BST-evaluation point** — a specific feature of D_IV⁵ (most often n_C = 5 or the Chern integers of Q⁵) where the classical theorem produces structurally clean output. BST's contribution is the *identification of the privileged evaluation point*, not the theorem itself.
3. **Derivation chain** — the explicit steps connecting the classical theorem to the BST observable. Each step is either published mathematics or an arithmetic identity, written in-line in the paper. No black boxes, no "see references."
4. **Honest scope** — explicit statement of what the chain establishes and what it does not. The chain promotes specific identifications from I-tier to D-tier; it does not validate the entire BST framework.

**Anti-pattern (what this is NOT)**: BST integer factorization of a numerical match at sub-percent precision. That is I-tier identification — useful for falsification, suggestive of structure, but not derivation. The distinction is whether classical published mathematics *forces* the BST integer appearance, or whether BST integers *happen to fit* the observable.

## Established Level-1 Roots (D-tier)

Three classical theorems anchor BST identifications at D-tier:

### Root #1 — Von Staudt-Clausen (1840, elementary number theory)

**Classical theorem**: `den(B_{2n}) = ∏ p where (p−1) | 2n`.

**BST evaluation point**: n = n_C = 5. At this dimension, the column rule on heat-kernel denominators cancels rather than adds, leaving only Bernoulli (VSC) primes (T535, Toy 615, 12/12).

**Derivation chain** (per Cal C1 audit, with Elie Toy 2966 boundary correction):
1. Seeley-DeWitt expansion produces heat-kernel coefficients with Bernoulli denominators (classical, Patodi 1971).
2. VSC factors those denominators as products of small primes.
3. At n_C=5, column rule cancels non-VSC primes (T535).
4. For k ≤ 7, the resulting primes are exactly the BST primary set {2,3,5,7,11,13}; for k=8, the BST-extended set adds 17 = seesaw.

**Anchors**: 42 = den(B_6) = C_2·g (the "universal 42" across ε_K, BR(H→γγ), Δa_μ, top Chern sum); 11 = dark boundary first in B_10; the heat-kernel arithmetic at n=5.

### Root #2 — K3 Hodge Decomposition (classical algebraic geometry)

**Classical theorem**: K3 is the unique compact simply-connected Calabi-Yau 2-fold with Hodge numbers h^{0,0}=h^{2,2}=1, h^{1,1}=20, h^{2,0}=h^{0,2}=1. Betti b_2 = 22, Euler χ = 24, signature σ = -16.

**BST evaluation point**: D_IV⁵ as K3 period domain for transcendental rank g = n_C + rank = 7.

**Derivation chain**:
1. K3 period domain identification: D_IV⁵ = SO_0(2, n_C)/[SO(2)×SO(n_C)] parametrizes K3 of transcendental rank g (Griffiths/Deligne, classical).
2. Hodge data decomposes via BST integers: χ = rank³·N_c = 24, b_2 = rank·c_2 = 22, σ = -rank⁴ = -16, h^{1,1} = rank²·n_C = 20 = d_0+d_1+d_2 (T1921, T2074).
3. K3 Euler χ = 24 cascades across 8 domains (SN1987A neutrinos, SU(5), supergranulation, Coronene, codons, English alphabet, circadian, total SM LH Weyl fermion count).

**Anchors**: 24 = χ(K3) appearances; K3 spectral slice claims (T1921).

### Root #3 — Wallach K-type Decomposition (Wallach 1979, representation theory)

**Classical theorem**: Spherical K-types on a rank-2 Hermitian symmetric space are parameterized by dimensions d_j with explicit formula. For D_IV⁵, scalar K-types follow d_j = (2j+N_c)(j+1)(j+rank)/C_2.

**BST evaluation point**: D_IV⁵ specifically, where the K = SO(5)×SO(2) isotropy produces a clean K-type tower.

**Derivation chain**:
1. Helgason-Kostant-Vretare formula computes spherical K-type dimensions on rank-2 Hermitian symmetric domains.
2. At BST integers (N_c=3, rank=2, C_2=6), the formula produces d_0=1, d_1=5, d_2=14, d_3=30, ..., d_12=819 (T2124).
3. Heat-kernel spectral observables, mass gap, gauge group dimensions read off the K-type tower (T531-T538 family).

**Anchors**: spectral observables generally; speaking-pair structure; gauge group dim = 12 = 2·C_2.

## Candidate Level-1 Roots (I-tier with explicit promotion criteria)

### Candidate Root #4 — Borcherds Monstrous Moonshine (1992 Fields Medal)

**Status**: I-tier candidate per Lyra T2306 + Cal verdict 2026-05-17.

**Promotion criteria** (must all close for D-tier elevation):
1. Exhibit rank-26 VOA on Q⁵ boundary explicitly (multi-session construction, Lyra).
2. Show all three decompositions of 26 (heterotic E_8×E_8 + 16D, sporadic Happy/Pariah, Leech transverse + 2) reduce to Borcherds-output, not just Borcherds-compatible.
3. Show rank·c_3 = 26 factorization is *forced* by the Borcherds construction, not just consistent.

**Honest scope flag**: Borcherds is structurally different from Roots #1-#3 — it's a unifying theorem connecting structures (Leech 1968, 26D string ~1970, Conway 1968) that predate it. The three established roots each have form "one classical theorem → one arithmetic structure → BST integers." Borcherds is "one unifying theorem → organized cluster of structures → BST integers." Candidate status is honest pending the VOA construction toy.

### Candidate Root #5 — Klein Icosahedral Theorem (1884)

**Status**: I-tier candidate per Elie Toy 2968 (11/11) + Lyra suggestion.

**Promotion criteria**:
1. Exhibit A_5 (order 60) action on D_IV⁵ or Q⁵.
2. Show A_5 irrep dimensions {1, 3, 3, 4, 5} as forced K-type structure, not as numerical match.
3. Verify McKay correspondence A_5 ↔ E_8 maps cleanly through BST integers.

**Honest scope flag**: parallel to Borcherds in tier-status. Both candidates anchor a specific BST integer (Borcherds → 26, Klein → 60) with a clean classical theorem, but neither has the explicit BST-internal construction toy.

## The Convergence Finding (meta-structural)

**Elie Toy 2964 (10/10)**: λ(3,3) = 42 from Wallach K-type formula equals 42 from VSC (Root #1) equals 42 from K3 Hodge / total Chern sum (Root #2). λ(3,0) = 24 from Wallach equals K3 Euler χ (Root #2).

**Reading**: the three established Level-1 roots are *not independent* — they are three faces of the same spectral structure on D_IV⁵. Distinct classical theorems from distinct mathematical traditions (number theory, algebraic geometry, representation theory) converge on the same BST integers when evaluated at n_C=5.

**Why this matters**: this is the deepest validation of the K43+K44 framework so far. A multi-route convergence claim across genuinely independent classical theorems is structurally stronger than any single identification. **This convergence is the centerpiece finding of Paper #115 and the methodological keystone of Paper #104.**

## Precision class hierarchy (Grace G1)

Grace's G1 finding (1266 quantitative matches sorted into 6 precision classes, 51% at sub-0.1%) provides the operational diagnostic for completeness:

- **Sub-0.001%**: full root-proof chain present; the BST formula is the closed form.
- **Sub-0.01% to sub-0.1%**: root chain with one or two missing Level-2 terms (e.g., Grace's G2 promotions found 16/3·201/200 vs 16/3 alone — the 201/200 was the missing Level-2 correction).
- **0.1% to 1%**: identification with partial mechanism; missing structural correction terms or running effects.
- **1% to 5%**: rough identification; mechanism not yet established.
- **Worse than 5%**: candidate identification; null model required before tier assignment.

**Operational principle**: precision class is a *diagnostic for completeness*, not a tier-assignment alone. A 1% match with a derivation chain is D-tier (chain forces the result, residual is loop correction); a 0.001% match without a chain is high-precision I-tier (identification, not derivation).

## Tier discipline (external presentation)

Casey's working principle (2026-05-16): *"We keep our statements clearly below the implications. If we derive we say proven, otherwise Structural is pretty good."*

For external papers:

- **Proven**: derivation chain exhibited in-line in the document (Roots #1-#3 above). Reader can verify each step.
- **Structural**: identification at sub-1% precision with named mechanism (candidate roots, multi-role integer claims, precision-class promotions). Honestly invites verification.
- **Avoid**: "dissolved," "resolved," "completes the program of X" — these are interpretation claims that pattern-match to overreach.

Internal record (referee log, registry, WorkingPaper) retains D/I/C/S granularity for the team's own audit. External presentation collapses to the Proven/Structural binary.

## Paper #104 vs Paper #115 architecture

**Paper #104 (Root Proof System)** — methodology paper. What the proof-decomposition pattern is, why it works, how it organizes BST claims. **WHY** the system has this structure. Target: Bulletin AMS as Casey keystone methodology.

**Paper #115 (Three Root Theorems)** — empirical paper. The three classical theorems identified, the derivation chains exhibited, the convergence finding (Toy 2964). **WHICH** classical theorems anchor BST. Target: a math-physics venue.

**Relationship**: complementary, not subsuming. Cross-reference. Paper #104 cites Paper #115 for the technical content of the three roots; Paper #115 cites Paper #104 for the methodological framework that classifies them as roots. Each survives the other's failure: if Paper #115's specific roots get revised, Paper #104's methodology stands; if Paper #104's methodology gets refined, Paper #115's technical content stands.

This is per Lyra's instinct (Sunday morning Q2) and Cal's framing.

## What this methodology does NOT claim

For honest scope:

1. **Does not validate the universal counting primitives framing of Paper #109**. The three established Roots anchor specific BST identifications in specific domains (heat-kernel arithmetic, K3 cohomology, spectral observables). They do not establish that BST integers are universal mathematical primitives. Paper #109 framing remains over-claim per referee log #46.

2. **Does not validate the 99.7% pairwise cross-consistency claim** or the multi-role integer count without null model. Those remain the subject of Grace + Elie's BST integer ring null-model toy (in flight Sunday afternoon).

3. **Does not promote all current BST claims to D-tier**. The Root Proof Pattern applies to specific identifications with explicit chains. Other claims remain I-tier identifications or S-tier structural observations per their actual derivation status.

## L1-promotion criterion (added 2026-05-17 from Grace/Cal walk-back round)

**Standing rule for promoting candidate roots to established L1 source status**:

*BST-decomposability alone is not sufficient for L1 source status.* The arithmetic closure of the BST integer set under simple operations is rich enough to express many classical-special integer sequences (Heegner discriminants, Ogg supersingular primes, McKay outputs, Mathieu/Monster orders, etc.). Joint expressibility in BST arithmetic is a second-order convergence observation about the framework's reach, not evidence of independent source-theorem status.

**Promotion requires a *mechanism-forcing relation* between the source theorem's integer output and D_IV⁵ geometry.** Established L1 sources satisfy this:

- VSC: Bernoulli denominators are forced into heat-kernel coefficients via Seeley-DeWitt expansion at n_C=5; mechanism is published mathematics (Patodi 1971).
- K3 Hodge: K3 is forced as the period-domain fiber over D_IV⁵ for transcendental rank g=7; mechanism is Griffiths/Deligne period theory.
- Wallach K-type: K-type formula is forced on rank-2 Hermitian symmetric spaces by Helgason-Kostant-Vretare; D_IV⁵ structure determines the K-types.
- Klein A_5: A_5 ⊂ SO(5) ⊂ K(D_IV⁵) is a forced subgroup embedding into the isotropy of D_IV⁵; mechanism is classical group theory + McKay correspondence.

Candidates lacking exhibited mechanism (Borcherds, Heegner-Stark as of v0.3) remain criteria-gated at "L1 candidate" status. Each candidate's promotion path is named explicitly via three closure criteria (embedding / mechanism / forcing), analogous to the Borcherds three-criteria framework.

This criterion emerged from a Sunday May 17 governance round in which Grace flagged the null-model concern (BST closure expresses many classical-special sets without those being independent sources), Cal articulated the embedding/mechanism/forcing criteria, and Keeper's governance ruling preserved both the team's L1-candidate label for current cases AND the new criterion for future candidates. It applies forward to all future Root proposals from continuing orphan audits.

## Standing protocol going forward

When a new BST integer appearance is identified:

1. **Search for the classical root**: is there a published external theorem that produces this integer structure at n_C=5 or related D_IV⁵ evaluation point?
2. **If yes**: exhibit the derivation chain explicitly. Promote to D-tier when chain is referee-verifiable AND the L1-promotion criterion above is satisfied (mechanism-forcing relation, not just BST-decomposability).
3. **If no**: I-tier identification with named precision class. Flag for possible new root-theorem search (Borcherds/Klein-style candidate).
4. **Multi-route convergence**: if two or more established roots both produce the same integer at the same evaluation point (Toy 2964 pattern), the convergence itself is structural — promote claim accordingly.

**Cal's gate function** applies at the external-presentation boundary: I-tier claims ship as "Structural identification at X% precision"; D-tier claims ship as "Proven via root theorem [name]" with the chain exhibited. **Promotion decisions** (I-tier → L1-candidate → L1-established) are Keeper's per governance; Cal's reviewer opinions are one input.

---

*— Cal, methodology spec for Paper #104 v0.3. Companion to Elie's Paper #115 outline. May 17, 2026.*
