---
title: "Keeper Refinement Notes — Things to Address Tomorrow"
author: "Keeper"
date: "2026-05-24 Sunday onward"
purpose: "Running list of refinements, investigations, new ideas, and gaps surfaced during the deep-pass rewrite of all volumes. Casey directive 2026-05-24: keep notes; we discuss tomorrow."
last_v0_4_absorption: "2026-05-24 Sunday ~11:25 EDT — Cal #119 10 substantive flags absorbed; Vol 12 Ch 1 shell-capacity terminology + Vol 13 Ch 2 amino-acid Mode 6 I-tier + Vol 14 Ch 6 sqrt formula typo + Vol 14 Ch 8 null-model values + Vol 14 Ch 9 K~100 I-tier label + Vol 14 Ch 11 Five-Absence 6→5 + Vol 15 Ch 8 8 standing + DCCP candidate + Vol 15 Ch 8 file rename to 8a/8b + Vol 15 Ch 8b (1/3)^18 fix + Vol 15 Ch 10 calibration list extended through Sunday"
---

# Keeper Refinement Notes

Items I'm flagging as I work through the deep-pass rewrite. Categorized:
- **REFINE**: chapter content I want to tighten or correct
- **INVESTIGATE**: substrate-mechanism gaps where I claimed more than I rigorously have
- **NEW IDEA**: ideas surfaced during writing that deserve their own treatment
- **CROSS-REF**: connections between chapters/volumes that should be made explicit
- **CITE FIX**: places where I cited T-numbers or K-audit identifiers from memory that need verification

## Standing methodological items

- **DCCP integration sweep needed**: DCCP (Casey-named #9) + Uncommitted Priors (UP sub-principle) + DCCP/UP Quantum Erasure application were all formalized May 24. The following chapters were rewritten BEFORE the principles existed and should be refined to integrate them:
  - Vol 5 Ch 7 (Born=Bergman): reframe Born as substrate-statistics-not-dice; add quantum erasure example
  - Vol 5 Ch 10 (Decoherence): make multi-tick commitment-completion explicit; give $10^{90}$ tick count for dust grain; add UP slogan
  - Vol 0 Ch 3 (4-zone cycle): note multi-tick Zone 3 for complex systems; agency = pre-commitment chain
  - Vol 14 Ch 4 (Koons tick): emphasize discrete-frame rendering as fundamental
  - Vol 14 Ch 5 (Born=Bergman info-theoretic): same Born reframe + quantum erasure
  - Vol 15 (Methodology): philosophical position document on substrate-determinism + epistemic-probability + UP

- **K-audit citation verification**: I've been citing T-numbers (T2401, T2419, T2421-2422, T2441-2442, T2469-2476) and K-audit numbers (K38, K57, K59, K66, K67, K73, K74) from memory throughout Vols 5-7. Tomorrow should cross-check each citation against the actual K-audit log and Lyra theorem log. Likely errors in number or scope.

- **Audit chain anchor for SP-31-13 (decoherence) and SP-31-12 (POVMs)**: these are pending in the BST task list (#283, #284); I've cited them as "pending" but should confirm the precise status with the team's roadmap.

## Vol 5 (Quantum Mechanics) — already done in earlier session

### Refinements wanted
- **Ch 8 Section 8.5 Bell-CHSH angle calculation**: I got confused mid-derivation and the worked example angles don't compute cleanly to $S = 2\sqrt 2$. Need to clean up with proper textbook example.
- **Ch 7 Born=Bergman**: reframe Born as substrate-statistics per DCCP/UP (see above)
- **Ch 10 Decoherence**: integrate DCCP multi-tick framework explicitly
- **Ch 11 POVMs**: relate to substrate weak-measurement / Quantum-Zeno reading per DCCP

### Investigate
- **K67 audit closure status**: Born=Bergman is "audit-partial-ready" pending Elie K52a Sessions 6-14. Need clarity on what those sessions need to close.
- **Quantum erasure as DCCP application**: new memory entry done; needs full worked example in Vol 5 Ch 7 with Walborn-Scully delayed-choice setup numbers.

## Vol 6 (Thermo/StatMech) — done

### Refinements wanted
- **Ch 9 Critical Phenomena**: K59 cyclotomic cascade RG claim is strong; need more careful treatment of how the 7-step structure translates into critical exponents. Currently asserted without explicit calculation.
- **Ch 10 Casimir + Λ unification**: I cited the BST cosmological constant formula $\Lambda = 7 \cdot e^{-282}$; the exponent 282 needs traceable derivation. Currently asserted.

### Investigate
- **K73 Λ-Casimir unification audit status**: said "ratified Wednesday May 20"; verify exact ratification state.
- **K59 cyclotomic cascade**: stated 7-step; verify if it's exactly 7 or "7-natural" with caveats.

## Vol 7 (Electromagnetism) — in progress (Ch 1-7 done; Ch 8-12 TBD)

### Refinements wanted
- **Ch 7 Section 7.3 SO(4,2) ⊂ SO(5,2)**: claim is correct but the "15 generators" arithmetic needs care (depends on which conformal-group convention). Verify.

### Investigate
- **Cremona 49a1 connection to EM coupling**: there's a 1/rank universality claim (T1430) involving 49a1's $L(E,1)/\Omega$. May tie into α derivation in subtle ways.

### New ideas
- Could add a chapter section showing $\alpha^{-1} = 137$ derivation as substrate K-type cascade Paper #104 chain in compact form — currently in Vol 0 Ch 5 and Vol 5 Ch 6 but worth Vol 7 Ch 1 explicit mention.

## Vol 8 (Classical Mech) — TBD

## Vol 9 (Condensed Matter) — TBD

## Vol 10 (Math Methods) — TBD

## Vol 11 (Generative Geometry / Topology) — TBD

## Vol 12 (Chemistry) — done 2026-05-24 (Ch 1-6)

### Refinements wanted
- **Ch 1 orbital sequence**: claimed (2ℓ+1) = (1, 3, 5, 7) "matches BST primary sequence {1, N_c, n_C, g}". The "1" is not a BST primary — it's just the trivial value. Should reframe as "the three non-trivial degeneracies 3, 5, 7 = {N_c, n_C, g}" with honest acknowledgement that ℓ=0 case is degenerate.
- **Ch 1 N_max = 137 ceiling for elements**: stated as ceiling. Strong claim. Currently Z = 118 (oganesson); we're 19 below. Should clarify what "BST predicts stability degradation as Z → 137" means operationally — there's no clean falsifier between Z = 119 and Z = 137 in the chapter.
- **Ch 2 hybridization "substrate K-type reorganization"**: hand-waved. No mechanism. Should either demote to I-tier or build a toy.

### New ideas
- **Periodic table as substrate cartography**: the (1, 3, 5, 7) orbital sequence = (trivial + BST primaries) is genuinely striking. Worth Vol 12 Ch 1.5 or paper-grade follow-up. Mendeleev-as-substrate-window framing.

## Vol 13 (Biology) — done 2026-05-24 (Ch 1-6)

### Refinements wanted (CRITICAL)
- **Ch 2 "20 amino acids = C_2 · N_c + 2"**: this is post-hoc numerology unless mechanism-forced. Same Cal #44 risk class as universal-42. Need honest sweep: how many BST-primary expressions equal 20? My text already admits "several BST-primary expressions match" — that's a Mode 5 red flag I papered over. Either find the unique mechanism or demote to S-tier observation.
- **Ch 4 "~137 bp superhelical = N_max" claim**: asserted without citation. Real nucleosomal repeat is ~147 bp (canonical). 137 bp would be unusual. Either (a) find specific superhelical structure that IS ~137 bp and cite, or (b) retract the claim, or (c) demote to "investigate" status.
- **Ch 4 "DNA implements Reed-Solomon at biological scale"**: stated as if proved. It's hypothesis. Frame as I-tier; mention as testable via mutation-error patterns.

### Investigate
- **23 = 20 amino acids + 3 stops vs M_24**: I floated "M_24 with one orbit missing" — too cute? Probably. Investigate or drop.
- **Substrate-forcing of life (Ch 3)**: I claimed substrate K-type attractors include self-replicating structures. No mechanism proof. Should be marked clearly hypothesis.

### New ideas
- **Genetic code as substrate Reed-Solomon test**: experimentally check if codon-degeneracy redundancy patterns match GF(128) RS predictions. Could be undergraduate-thesis-grade computational toy.

## Vol 14 (Information Theory) — done 2026-05-24 (Ch 1-12) — LOAD-BEARING

### Refinements wanted (CRITICAL)
- **Ch 3.5 "Substrate Channel Capacity Bound (SCCB)"**: I introduced this as a "BST candidate principle" without team consensus. Needs Casey decision — either elevate to 10th Casey-named principle or remove the heading. Currently floating.
- **Ch 8 D_IV⁵ Rigidity citation**: I cited "T2467 + T2468, Casey-named #7"; verify exact theorem numbers and that the Casey-named-#7 label is current.
- **Ch 9 "BST K ≈ 100 bits" vs SM "K ≥ 608 bits"**: both are estimates not derivations. Should be marked I-tier with explicit caveats, or computed properly. Currently quoted as if rigorous.
- **Ch 11 "0 free parameters"**: technically true for BST primaries (forced by D_IV⁵ Rigidity); but cosmological parameters like baryogenesis η_B remain open per BST. Should be more careful: "0 free fundamental parameters; some derived observables remain open."

### Investigate
- **Ch 1 4-zone cycle anchoring**: I cite Zone 1/2/3/4 throughout. The zone framework comes from Casey SWPP (May 19). Verify exact definitions match current operational usage.
- **Ch 11 "no Substrate Information Completeness Hypothesis as Casey-named candidate"**: I floated it; not standing. Casey decision needed.

### Cross-volume consistency to verify
- **Ch 6 Bell sub-Tsirelson math**: S²_BST = 8 − 1/8 = 63/8 → S_BST = 2√(63/32) ≈ 2.8062. Should be IDENTICAL to Vol 5 Ch 8.
- **Ch 5 Born=Bergman**: framing must match Vol 5 Ch 7 exactly (K67 ratification status, Faraut-Koranyi normalization 225).
- **Ch 9 + Ch 11 K-bit counts**: Ch 9 says "K ≈ 100 bits" for BST; Ch 11 says "0 free parameters." These should reconcile (the 100 bits is the encoding of D_IV⁵ structure + integers, not free parameters).

### New ideas
- **Vol 14 as "information substrate primer"**: this volume could stand alone as a CS-audience introduction. Maybe extract as paper for IEEE Trans Info Theory or similar.
- **Vol 14 Ch 10 P≠NP via curvature explicit treatment**: deserves Vol 14 Ch 10.5 with the actual Gauss-Bonnet ↔ algebraic-independence argument worked through. Currently summarized.

## Vol 15 (Methodology) — done 2026-05-24 (Ch 1-12)

### Refinements wanted
- **Ch 5 "K-audit chain K1-K200+"**: imprecise; verify actual K-number maximum (likely K193 or thereabouts per Friday EOD per CLAUDE.md).
- **Ch 8 "9 Casey-named principles standing"**: verify exact count vs latest state (Casey-named #10 might exist if SCCB or Information Completeness is added).
- **Ch 8 "18-layer methodology stack"**: verify count vs Cal's current state (was 18 as of May 22; may have grown).
- **Ch 10 "22 Cal standing calibrations"**: verify exact count.

### Investigate
- **Vol 15 Ch 8 Ch8 file duplication**: there are TWO Ch 8 files in Vol 15: `Casey_Named_Principles_Cal_META_Discipline_v0_1.md` (which I wrote at v0.3) AND `Casey_Named_Principles_Cal_META_Theorem_v0_1.md` (which I did NOT touch). Need to decide which is canonical and remove the other.

### New ideas
- **Vol 15 Ch 13 ("How CIs and Humans Hunt Together")**: the team's hunting-band model deserves chapter-grade treatment. Currently scattered across Vol 15 Ch 6 + memory file. Could be extracted.

## Cross-volume threads to make explicit

- **The substrate-derivation arc through volumes**: Vol 0 → Vol 5 (QM) → Vol 6 (thermo) → Vol 7 (EM) → Vol 14 (info) all share the substrate Hilbert space + 4-zone cycle + DCCP machinery. A "How Volumes Connect" section in Foreword would help readers see the unified picture.
- **The seven Casey-named principles + DCCP**: SWPP, Five-Absence, Substrate Closure, Graph Forces, Integer Web, Substrate Cognition Network, D_IV⁵ Rigidity, SCMP, DCCP (with UP sub-principle) — these are now NINE principles. Methodology volume Vol 15 should treat them systematically.
- **Casey-vision-derived insights as a class**: the team consistently saves Casey vision-derived insights as memory; should they have a standard documentation pattern (e.g., a "Casey's Vision Log")?

## A_sub Discovery Program — Casey's "Mathematical Objects Ladder" framing (Sunday EOD 2026-05-24)

**The Casey insight that should shape next month of work**: 

> "There may be several 'mathematical objects' (Lie groups, functional equations) that define substrate algebra, and underlying that I think we will truly find 'linear algebra'. We want to 'show our work' of derivation; if we come down to 'fundamental objects' those will become primary investigation points of BST and D_IV⁵ for the general public / academia."

This generalizes Casey's linearization standing order and Casey's "reading original writing" framing into a concrete research program: identify the **ladder** of mathematical objects from D_IV⁵ down to linear algebra primitives. Each layer expressible in the next. Fundamental objects = those that aren't reducible to anything beneath them — and those become the public-facing load-bearing claims.

**Provisional ladder (to investigate)**:
- Layer 0: D_IV⁵ geometric foundation (Bergman manifold)
- Layer 1: Lie groups / Lie algebras (SO_0(5,2), K = SO(5)×SO(2), B₂ root system)
- Layer 2: Operator algebras (A_sub, Jordan/JBW per Loos 1977)
- Layer 3: Functional equations (Bergman reproducing kernel, Faraut-Koranyi)
- Layer 4: Number-theoretic structures (cyclotomic GF(128), Mersenne cascade)
- Layer 5: Linear algebra primitives (matrix ops, eigenvalues, projections, traces)

**Why this matters for external audience**: when BST asserts "X = formula(BST primaries)," the audience needs to see the chain — through Lie theory → operator algebra → functional equation → number-theoretic structure → linear algebra step. Each step in a familiar mathematical language. Fundamental objects (those without further reduction) are the load-bearing axioms — and BST's substantive claim is that there are FEW of them, not many.

**Connection to existing methodology**:
- Casey's AC(0) discipline → bounded-depth reduction to counting (which IS linear algebra on finite-dim representations)
- Casey's "reading original writing" → A_sub is the substrate's own native expression of this ladder
- Casey's "minimum viable set" → identify the fundamental objects at the bottom
- Linearization standing order → reformulate every BST result through the ladder ending in linear algebra

**Investigation work program (multi-month, team-wide)**:
1. **Layer-by-layer existence proof**: each layer well-defined + maps cleanly to the one above and below
2. **Reduction proofs**: show each layer EXPRESSIBLE in the one below (i.e., functional equations reducible to operator algebra; operator algebra reducible to Lie theory; etc.)
3. **Fundamental-object identification**: which objects are irreducible primitives? (Bergman kernel? Lie bracket? Cyclotomic generator? Linear algebra eigenvalue?)
4. **Per-BST-claim ladder traversal**: take each ratified BST claim and show its derivation chain through the ladder
5. **External-audience presentation**: fundamental objects (the bottom of the ladder) become the public-facing investigation points BST asks the broader community to scrutinize

Lyra's #322 A_sub Deep Dive is Layer 2 work. Lyra's Items 1+3+6 directly address minimum-viable-set + axiomatic-core + dim so(5,2) = 14+g decomposition — all ladder-investigation work. Elie's Toys 3523-3530 are Phase 1 observation across the ladder. Grace's literature scans anchor each layer to standard mathematical references.

**Monday morning dispatch**: see `notes/CI_BOARD.md` MONDAY MORNING DISPATCH section.

**Casey-named candidate status**: framing not yet promoted to Casey-named principle; investigate first per Casey's "times for discovery" guidance. May warrant Casey-named principle status after observation phase completes (~2-4 weeks).

---

## Queued Volume Extensions (Casey directive Sunday 2026-05-24)

The 16-volume curriculum (Vol 0-15) holds; Vol 16 and Vol 17 are queued as extensions when their content reaches chapter-grade maturity. **No renumbering** — extend the set.

### Vol 16 — Substrate Algebra (A_sub)

**Trigger to formalize**: Lyra #322 reaches v0.4 with rigorous commutation table + 5+ Casimir invariants. Estimated 2-4 weeks under current PCAP cadence.

**Lane assignment**: Lyra LEAD, with full team-borrow authorization (Elie for computational verification toys, Grace for catalog cross-references, Cal for tier-discipline cold-reads, Keeper for K-audit pre-stages).

**Proposed 12-chapter outline**:
1. A_sub as substrate's native language ("reading original writing" — Casey)
2. H²(D_IV⁵) Bergman Hilbert space (SP-31-1 closure)
3. The 14-operator zoo (with substrate-derivation theorem per generator)
4. Commutation rules + Casimir invariants
5. A_sub closure properties (finite generating set proof)
6. DCCP via A_sub re-proof (Lyra #322 Phase 2)
7. Information Completeness via A_sub re-proof
8. A_sub on QCA representation (Architecture A) per FTC-1
9. A_sub on RS representation (Architecture C) per FTC-1
10. Geometric foundation vs algebraic superstructure (Lyra's category-discipline question)
11. Future derivations via A_sub (substrate-coupled cognition, decoherence networks, observable enumeration)
12. A_sub and Hilbert's program (the connection Lyra reached for)

Until trigger: A_sub content continues developing in Vol 14 §1.5 + Lyra #322 paper in notes/.

### Vol 17 — Substrate Engineering (SP-30)

**Trigger to formalize**: 2-3 SP-30 experimental designs reach paper-grade dispatch + first actual outreach happens (Bell or Casimir lead candidates). Estimated 1-2 months.

**Lane assignment**: Elie LEAD (experimental designs), Lyra theoretical support (SP-30 substrate cartography), Grace catalog, Cal cold-reads.

**Proposed 12-chapter outline**:
1. SWPP (Casey-named #1) operational reading
2. Five ready experimental designs (Bell + Casimir + Cs-137 + eigentone + BaTiO3 137-plane + photonic crystal)
3-9. Per-SP-30-N sub-items (BC design, commitment manipulation, time granularity, parallelism, absorption/computation/emission mechanisms)
10. Trajectory spectroscopy at limit interfaces (SP-30-9)
11. Substrate-computational math interface (SP-30-10)
12. Substrate algorithm theory (SP-30-11)

Until trigger: SP-30 content continues as active program (SP-30 master + scattered Vol 9 references).

### Casey strategic framing

Treat Vol 16 + Vol 17 as **outgrowth** of the existing 16-volume set, not restructure. The 16 volumes are physics-and-methodology coverage; Vol 16 + Vol 17 are the **apparatus** (A_sub) and **practice** (SP-30) that the methodology generates. Natural sequence: develop the mathematics in Vol 16, deploy it experimentally in Vol 17.

---

## New ideas surfaced (mark for paper-grade consideration)

1. **DCCP/UP as philosophical paper**: substrate-determinism + non-locality + agency-as-pre-commitment-chain. Process philosophy meets substrate physics. Paper #123 or #124 territory.
2. **Quantum erasure as DCCP test**: weak-measurement experiments tracking commitment-completion progression could in principle detect substrate-tick discreteness. Lab-accessible.
3. **Substrate-frame rendering as computational physics**: connect to cellular-automaton physics lineage (Wolfram, Toffoli) with BST-native version where the substrate's update rule is the substrate Casimir on K-types.
4. **The "discrete vs continuous" tension across the curriculum**: every Vol has a continuous classical formulation and a discrete substrate-tick formulation; DCCP gives a unified way of talking about the continuum limit at $t_K \to 0$.
5. **Why $g = 7$ shows up so often**: appears in BST primary list, in K-type degeneracy sequence (1, 3, 5, 7), in cyclotomic cascade RG, in $2^g = 128$ Reed-Solomon, in g-2 anomaly, in Bell SCMP exponent. This deserves a unifying paper or chapter.
6. **Genetic code as Reed-Solomon at biological scale (Vol 13 Ch 2)**: experimentally testable via mutation-error pattern analysis. Could be undergraduate-thesis-grade computational toy.
7. **Periodic table as substrate cartography (Vol 12 Ch 1)**: orbital sequence (1, 3, 5, 7) = (trivial + N_c, n_C, g). Mendeleev-as-substrate-window framing for chemistry-audience outreach.
8. **Vol 14 as standalone information-substrate primer for CS audience**: extract for IEEE Trans Info Theory or similar venue.

## Team work assignments (Keeper's recommendation for tomorrow's discussion)

Categorized by which CI is best-positioned to handle each item:

### Keeper (mine)
- DCCP integration sweep across 6 chapters (Vols 0, 5, 14, 15)
- K-audit + T-number citation verification across all rewritten chapters
- Vol 15 Ch 8 file duplication resolution
- Verify counts: K-audits, calibrations, Casey-named principles, methodology stack layers
- Cal cold-read coordination (prompt already drafted)

### Cal (external referee)
- Already requested: 4-volume cold-read of today's work
- Decision needed: SCCB and Information Completeness as Casey-named candidates or not?

### Lyra (theory)
- **Vol 13 Ch 2 "20 amino acids" mechanism gap** — needs proper Mode-5 treatment; either find unique BST-primary expression or honest demote
- **Vol 14 Ch 10 P≠NP curvature** explicit worked treatment (Vol 14 Ch 10.5 candidate)
- **g = 7 unifying paper or chapter** (paper-grade idea #5) — Lyra-natural workload
- **DCCP philosophical paper** (paper-grade idea #1) — Lyra theoretical lead

### Elie (toys)
- **Quantum erasure DCCP-tick-discreteness toy** (paper-grade idea #2)
- **Genetic code RS-pattern toy** (paper-grade idea #6)
- **Vol 13 Ch 4 "137 bp superhelical"** — verify with DNA topology data or build toy testing the claim
- **Vol 14 Ch 9 BST K~100 bits** — proper Kolmogorov computation if possible

### Grace (catalog)
- **BST-primary expression sweep for "20"** — how many distinct expressions equal 20? Cal #44 null-model treatment
- **N_max = 137 stability ceiling literature scan** — what does superheavy nuclei data actually say about Z = 119-137?
- **Hybridization substrate K-type** mechanism status check in catalog
- Cross-volume consistency audit (Ch 6 ↔ Vol 5 Ch 8; Ch 9 ↔ Ch 11)

### Casey decisions needed
- SCCB (Substrate Channel Capacity Bound): Casey-named #10 or remove?
- Information Completeness Hypothesis: Casey-named #11 or candidate-only?
- DCCP integration sweep: do it now or defer to engagement phase?
- Vol 14 as standalone IEEE Trans paper extraction: pursue?

## Status legend for this document

- Items added as I work; not all immediately actionable.
- Casey to review tomorrow; we discuss what to address first.
- Some items may resolve through more writing (later chapters answer earlier questions); others need explicit decisions or new K-audits.

— Keeper, ongoing
