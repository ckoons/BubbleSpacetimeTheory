---
title: "Task #320 v0.7 — Candidate A vs Candidate D as Test of FTC-1 (Architecture D Hybrid Bergman/RS equivalence conjecture)"
author: "Lyra (Claude Opus 4.7) [Toy 3522 absorbed + Casey 'work the board' directive Sunday]"
date: "2026-05-24 Sunday EDT (~14:55 EDT actual via date)"
status: "v0.7 substantive reframe. Toy 3522 quantitatively narrows §6 Candidates to A (Dirac 0.7299%) vs D (GF(128) M_g 0.7874%) — only 8% apart, both empirically discriminable at SP-30-1 5σ precision. v0.7 substantive observation: A vs D distinction is TEST OF FTC-1 conjecture from Task #322 (Architecture A QCA + Architecture B Bergman + Architecture C RS all equivalent under Φ mapping). If FTC-1 holds, A and D should give SAME scale; 8% disagreement implies FTC-1 needs revision OR one Architecture is non-substrate. FRAMEWORK-PLUS tier preserved per Cal #126."
related: ["Lyra_Task_320_v0_6_META_Vulnerability_Acknowledgment.md (Candidate A/B/C/D test plan)", "Elie Toy 3522 (Sunday 14:50 EDT) — 7/7 PASS Candidate side-by-side numerical comparison", "Lyra_Task_322_Substrate_Operator_Algebra_A_sub_Deep_Dive_v0_1.md v0.2 Section 16 FTC-1 conjecture", "Grace INV-5138 cross-CI cascade pattern + INV-5139 Grace lane expansion corollary"]
---

# Task #320 v0.7 — Candidate A vs D as Test of FTC-1

## 1. Toy 3522 absorbed (Elie Sunday 14:50 EDT)

Per Elie Toy 3522 7/7 PASS Calibration #27 STANDING compliant side-by-side Candidate comparison:

| Candidate | Substrate scale | Numerical | Match to Toy 3520 0.7299% |
|-----------|----------------|-----------|----------------------------|
| **A Dirac Z·α=1** | α = 1/N_max | 0.007299 = 0.7299% | ✓ UNIQUE within 1% |
| **D GF(128) M_g=127** | 1/M_g = 1/127 | 0.007874 = 0.7874% | ✗ 8% off (1.079×) |
| **C Bergman c_FK·π^(9/2)=225** | 1/225 | 0.004444 = 0.4444% | ✗ 39% off |
| **B Casimir C_2=6** | 1/C_2 | 0.166667 = 16.67% | ✗ 22.83× off |

**Toy 3522 narrows the substrate-hypothesis-selection question dramatically**:
- Candidates B + C are NUMERICALLY EXCLUDED (>10% off observed signature; cannot match Toy 3520 5σ data)
- Candidates A + D are within 8% — both viable; experimentally discriminable at SP-30-1 5σ precision (per Toy 3520 design)
- Cal #126 META-vulnerability LOCALIZED FURTHER: from "Candidate A vs B vs C vs D" to "Candidate A vs Candidate D"

## 2. The substantive observation: A vs D is a TEST OF FTC-1

Per Lyra_Task_322 v0.2 Section 16 FTC-1 conjecture: Architecture A QCA + Architecture B Bergman + Architecture C RS all equivalent under structure-preserving bijection Φ : H²(D_IV⁵) ↔ GF(128)^k ⊗ ℂ.

**Critical observation (v0.7)**: 
- Candidate A (Dirac Z·α=1) substrate-mechanism is on the **continuous Bergman side** (Architecture B)
- Candidate D (GF(128) M_g cyclotomic) substrate-mechanism is on the **discrete RS side** (Architecture C)
- If FTC-1 holds: A and D should give SAME numerical scale (both representations of same substrate state under Φ)
- Toy 3522 observation: A and D give DIFFERENT scales (0.7299% vs 0.7874%, 8% apart)

**Therefore: 8% disagreement between Candidate A and Candidate D is a POTENTIAL FALSIFIER of FTC-1 conjecture.**

Three possibilities:

**Possibility 1: FTC-1 holds; one of A/D is the actual substrate-mechanism; the other is non-substrate**
- If substrate truly operates at Dirac threshold (Bergman side), Candidate D GF(128) M_g cyclotomic is an alternative non-substrate observable
- Or vice versa: if substrate operates at GF(128) cyclotomic, Candidate A Dirac threshold is non-substrate

**Possibility 2: FTC-1 holds approximately; A and D both contribute via Φ-mixing**
- Substrate per-tick scale is some weighted combination of A and D mechanisms
- Per-tick scale ≈ α (Candidate A) + correction term ≈ 1/N_max - 1/M_g ≈ 0.058 × α
- Pure A or pure D would both be wrong; mixed substrate-mechanism is correct
- Would predict scale BETWEEN 0.7299% and 0.7874% (e.g., 0.76%)

**Possibility 3: FTC-1 conjecture is wrong**
- Architecture B Bergman ↔ Architecture C RS are NOT genuinely equivalent under Φ
- Substrate has dual representations that are PHYSICALLY DISTINCT (not just mathematical reformulations)
- Substrate has BOTH continuous and discrete physics, with per-tick observables depending on which "side" of substrate the observer couples to
- 8% disagreement is a real substrate-physics distinction, not a mathematical equivalence break

## 3. SP-30-1 actual SPDC experiment becomes FTC-1 test

Per Toy 3520 SPDC experimental design at 5σ precision: A vs D distinction is **experimentally discriminable**.

**SP-30-1 outcome scenarios**:
- **Outcome 1**: SP-30-1 measures signature step at 0.7299% (Dirac) → Candidate A confirmed; FTC-1 Possibility 1 (Bergman side substrate-mechanism) supported
- **Outcome 2**: SP-30-1 measures signature step at 0.7874% (GF(128)) → Candidate D confirmed; FTC-1 Possibility 1 (RS side substrate-mechanism) supported
- **Outcome 3**: SP-30-1 measures intermediate (e.g., 0.76%) → Possibility 2 (Φ-mixing); FTC-1 holds approximately
- **Outcome 4**: SP-30-1 measures something inconsistent with all (A, D, A+D mixing) → BST framework partial falsification at this observable

**Implications**:
- SP-30-1 Bell substrate-CHSH experiment is now a DIRECT TEST of FTC-1 conjecture
- 12-18 month experimental program (per Toy 3520 design) yields binary discriminator
- Cal #21 dual-gate empirical leg becomes load-bearing test of substrate-mechanism + Architecture equivalence
- Lab data alone can resolve A vs D question (CIs cannot substitute per Keeper Sunday observation)

## 4. v0.7+ Lyra work focuses on Candidate A vs D substrate-physics

Per Cal #126 path to STRUCTURALLY VERIFIED CANDIDATE elevation: implement ONE of §6 Candidates A/B/C/D + verify it UNIQUELY selects scale + alt-HSD test.

**v0.7+ work refined** per Toy 3522 narrowing:
- B + C eliminated empirically (multi-week implementation moot)
- Focus on A vs D distinction
- Substrate-physics question: does substrate operate primarily on Bergman side (A) or RS side (D)?

**Substrate-physics analysis (v0.7 framework)**:
- Bergman side (Architecture B): substrate as continuous Hilbert space H²(D_IV⁵) with K-type representations; Dirac Z·α=1 threshold = limit of continuum-bound-state physics
- RS side (Architecture C): substrate as discrete GF(128)^k codeword with K59 7-step cyclotomic; M_g = 127 = Mersenne prime of g = limit of substrate cyclotomic field
- Both are substrate-natural; both yield α-scale predictions within 8%

**Substantive substrate-physics question for v0.7+**: which side dominates per-tick observables? The 8% disagreement is not negligible — it's a genuine substrate-physics distinction.

**v0.7+ derivation candidate (multi-week)**: 
- Per K67 Born=Bergman: per-tick observable IS Bergman kernel matrix element = continuous Bergman side
- Therefore Candidate A (Bergman side) should be primary for OBSERVED signature
- Candidate D (RS side) describes underlying substrate-tick computational structure, NOT per-tick observable
- FTC-1 Possibility 1 with Candidate A as actual substrate-mechanism

If this analysis holds, Candidate A is substrate-physics-correct for per-tick observable; Candidate D is the substrate-tick computational substrate beneath (not directly observable).

**Honest scope (v0.7)**: this is a FRAMEWORK-level argument; doesn't yet derive uniquely from substrate Hilbert space structure (Cal #126 elevation requirement). Multi-week work needed.

## 5. FTC-1 test framing changes Task #322 v0.3+ priorities

Per Substrate Computational Model Investigation v0.4 Section 16: FTC-1 conjecture stated A QCA + B Bergman + C RS all equivalent under Φ.

**v0.7 implication for Task #322**: FTC-1 conjecture must be carefully tested, NOT assumed:
- If Toy 3522 8% disagreement persists empirically (SP-30-1 confirms Candidate A pure), FTC-1 holds approximately with B-side primary for observables
- If SP-30-1 confirms mixing or D, FTC-1 needs revision

**Task #322 v0.4+ work** (multi-month): rigorous FTC-1 conjecture analysis. Specifically:
- Does Φ mapping preserve OBSERVABLE quantities, or only state representations?
- Are there substrate-mechanisms where Bergman and RS sides give different predictions?
- Is the 8% A vs D discrepancy a Φ-approximation error, or a fundamental Bergman-RS distinction?

## 6. Grace lane expansion acknowledged (per INV-5139)

Per Grace INV-5139 + Keeper observation: Calibration #27 STANDING corollary — "when you need an independent anchor, ask the catalog lane first." Grace lane role expanded: pure-reactive backbone → ALSO pure-proactive substrate cartography for forward-derivation chains.

**Acknowledgment**: Grace's INV-5123 Dirac Z·α=1 anchor (from unblocked queue, not Casey-asked) enabled v0.5 forward-derivation. Without Grace's proactive substrate cartography, Lyra v0.5 would have been Mode 1 vulnerable.

**Standing future request** to Grace lane: literature scans for INDEPENDENT physics anchors that can support BST forward-derivations without circularity. Specifically:
- For v0.7+ Candidate A substrate-mechanism: literature scan on Bergman kernel reproducing property at Dirac Z·α=1 threshold (any standard QED / Bergman analysis literature)
- For Candidate D substrate-mechanism: literature scan on Mersenne prime structure in cyclotomic field theory (any standard number theory literature)
- For FTC-1 test: literature scan on operator algebra equivalence under continuous-discrete representation mapping

Grace proactive INV-anchors → Lyra forward-derivation chains is the methodologically novel pattern that closed v0.5. This is repeatable.

## 7. Tier disposition (v0.7)

**Cal #126 disposition preserved**: FRAMEWORK-PLUS, NOT YET STRUCTURALLY VERIFIED CANDIDATE.

**v0.7 additions**:
- Toy 3522 narrows §6 Candidates A/B/C/D to A vs D
- A vs D distinction is TEST OF FTC-1 conjecture (substantive new framing)
- SP-30-1 actual SPDC experiment becomes load-bearing FTC-1 discriminator
- Candidate A is FRAMEWORK-level favored for observable per K67 Born=Bergman (Bergman side primary for observables)
- Grace lane expansion corollary acknowledged

**Path to STRUCTURALLY VERIFIED CANDIDATE (v0.8+ multi-week)** refined per Toy 3522:
- Implement Candidate A substrate-physics derivation focusing on Bergman side primacy for observables (not all 4 Candidates needed)
- Verify Candidate A UNIQUELY selects α-scale via Bergman kernel reproducing property analysis
- Alt-HSD test against D_I_{1,5} + D_I_{5,1} (per Cal #77 Requirement 3)
- Estimated 2-4 weeks per Cal #126 if Candidate A succeeds

**Path to D-tier RATIFICATION (multi-month)**:
- v0.8+ Candidate A success + Cal #21 dual-gate
- SP-30-1 actual SPDC data 12-18 months pending Casey send-signal
- FTC-1 conjecture test resolution

## 8. Coordination

**Cal**: REQUEST cold-read on Toy 3522 (Elie's analysis) + v0.7 FTC-1 test framing. Specific question: does the A vs D distinction as FTC-1 test reframing add substantive content, or is it Mode 1 at meta-meta-layer?

**Keeper**: Sunday arc closed per Keeper. v0.7 is additional Sunday afternoon work; K-audit pre-stage update for FTC-1 test framing? At FRAMEWORK-PLUS tier per Cal #126.

**Grace**: REQUEST proactive literature scans per Section 6 (Bergman kernel + Mersenne prime cyclotomic + operator algebra equivalence). Standing future request: substrate cartography for Lyra forward-derivation chains.

**Elie**: Toy 3522 narrowing is substantively load-bearing; future toys for FTC-1 test (Bergman side observable vs RS side substrate computational structure distinction).

**Casey**: SP-30-1 Bell outreach send is now load-bearing for FTC-1 test resolution. Real SPDC data at 5σ precision discriminates A vs D (0.7299% vs 0.7874%) + tests FTC-1 conjecture.

## 9. v0.7 status

**What's filed (v0.7 additions)**:
- Toy 3522 absorbed: Candidate B + C numerically excluded; A vs D refined
- v0.7 substantive observation: A vs D distinction is TEST OF FTC-1 conjecture
- SP-30-1 actual SPDC experiment becomes load-bearing FTC-1 discriminator
- Candidate A FRAMEWORK-favored for observables (Bergman side primacy via K67 Born=Bergman)
- Task #322 v0.4+ implications: FTC-1 must be carefully tested not assumed

**What's NOT established (v0.8+ multi-week)**:
- Candidate A substrate Hilbert space derivation
- Alt-HSD test
- FTC-1 conjecture rigorous test
- STRUCTURALLY VERIFIED CANDIDATE elevation

**Cal #126 PASS at FRAMEWORK-PLUS PRESERVED**: v0.7 doesn't claim higher tier than Cal awarded. Honest scope per Calibration #27 STANDING.

— Lyra, Task #320 v0.7 A vs D as FTC-1 test Sunday 2026-05-24 ~14:55 EDT per Toy 3522 narrowing + Casey "work the board" directive. FRAMEWORK-PLUS tier preserved; substantive new framing identifies A vs D as TEST OF FTC-1 conjecture; SP-30-1 becomes load-bearing experimental discriminator; Candidate A FRAMEWORK-favored via K67 Born=Bergman Bergman-side primacy for observables.
