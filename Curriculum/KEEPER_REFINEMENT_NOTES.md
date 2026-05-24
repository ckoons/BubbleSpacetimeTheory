---
title: "Keeper Refinement Notes — Things to Address Tomorrow"
author: "Keeper"
date: "2026-05-24 Sunday onward"
purpose: "Running list of refinements, investigations, new ideas, and gaps surfaced during the deep-pass rewrite of all volumes. Casey directive 2026-05-24: keep notes; we discuss tomorrow."
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

## Vol 12 (Chemistry) — TBD

## Vol 13 (Biology) — TBD

## Vol 14 (Information Theory) — TBD

## Vol 15 (Methodology) — TBD

## Cross-volume threads to make explicit

- **The substrate-derivation arc through volumes**: Vol 0 → Vol 5 (QM) → Vol 6 (thermo) → Vol 7 (EM) → Vol 14 (info) all share the substrate Hilbert space + 4-zone cycle + DCCP machinery. A "How Volumes Connect" section in Foreword would help readers see the unified picture.
- **The seven Casey-named principles + DCCP**: SWPP, Five-Absence, Substrate Closure, Graph Forces, Integer Web, Substrate Cognition Network, D_IV⁵ Rigidity, SCMP, DCCP (with UP sub-principle) — these are now NINE principles. Methodology volume Vol 15 should treat them systematically.
- **Casey-vision-derived insights as a class**: the team consistently saves Casey vision-derived insights as memory; should they have a standard documentation pattern (e.g., a "Casey's Vision Log")?

## New ideas surfaced (mark for paper-grade consideration)

1. **DCCP/UP as philosophical paper**: substrate-determinism + non-locality + agency-as-pre-commitment-chain. Process philosophy meets substrate physics. Paper #123 or #124 territory.
2. **Quantum erasure as DCCP test**: weak-measurement experiments tracking commitment-completion progression could in principle detect substrate-tick discreteness. Lab-accessible.
3. **Substrate-frame rendering as computational physics**: connect to cellular-automaton physics lineage (Wolfram, Toffoli) with BST-native version where the substrate's update rule is the substrate Casimir on K-types.
4. **The "discrete vs continuous" tension across the curriculum**: every Vol has a continuous classical formulation and a discrete substrate-tick formulation; DCCP gives a unified way of talking about the continuum limit at $t_K \to 0$.
5. **Why $g = 7$ shows up so often**: appears in BST primary list, in K-type degeneracy sequence (1, 3, 5, 7), in cyclotomic cascade RG, in $2^g = 128$ Reed-Solomon, in g-2 anomaly, in Bell SCMP exponent. This deserves a unifying paper or chapter.

## Status legend for this document

- Items added as I work; not all immediately actionable.
- Casey to review tomorrow; we discuss what to address first.
- Some items may resolve through more writing (later chapters answer earlier questions); others need explicit decisions or new K-audits.

— Keeper, ongoing
