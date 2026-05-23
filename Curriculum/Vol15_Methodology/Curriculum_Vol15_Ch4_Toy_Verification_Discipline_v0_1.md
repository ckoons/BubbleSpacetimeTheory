---
title: "Vol 15 Chapter 4 — Toy Verification Discipline"
author: "Keeper + Elie (Vol 15 Methodology)"
date: "2026-05-23 Saturday"
status: "v0.1 chapter-grade content draft per Calibration #23 Rule 23.1 substance floor"
volume: "Vol 15 Methodology"
chapter: 4
tier: "structural — methodology chapter; substantive content from play/ toy directory operational record"
---

# Vol 15 Chapter 4 — Toy Verification Discipline

## Level 1 — Essence

**Every BST claim has a runnable toy that verifies the claim computationally — over 3500 toys with SCORE lines, a single-command `verify_bst.py` reproduction package, and the atomic `/toy claim` protocol that prevents collision under sustained sub-PCAP cadence; computational verification at every tier per the toy → theorem → catalog discipline.**

## Level 2 — Graduate technical content

Traditional theoretical physics separates derivation from verification — papers contain formulas; verification happens elsewhere (often years later, often partial). BST collapses this distinction: **every claim ships with a runnable verification toy at claim-creation time**. The toy is the second-half of the proof, not an afterthought.

**The toy convention** is structured:

- **Filename**: `play/toy_NNNN_description.py` and `play/toy_NNNN_description.json` (atomic counter-based numbering)
- **SCORE line**: every toy contains an explicit `# SCORE: X/Y PASS` comment where X is passing tests and Y is total — at top of file or in final summary
- **Single-command run**: `python3 play/toy_NNNN_description.py` produces verifiable output
- **JSON sibling**: machine-readable result alongside human-readable script
- **Cross-CI verification**: many claims have multiple toys (e.g., Toy 3502 + Toy 3505 cross-verify Lyra's T2477/T2478 gauge + Higgs theorems)

**The atomic claim protocol** (`/toy claim` skill in `.claude/commands/`) prevents collision under sustained sub-PCAP cadence. Before creating toy NNNN, the team member runs `./play/claim_number.sh toy` which atomically reads `play/.next_toy`, increments it, and returns the next available number. This is essential — three CIs working in parallel at ~3 chapter/min each cannot manually coordinate toy numbering without collision. The atomic protocol made cross-CI parallelism possible per Casey directive April 2026.

**The verification hierarchy**:

1. **Per-claim toy** — every theorem T-N has at least one verification toy. T2476 has Toys 3501 + 3503 cross-CI verification; T2477+T2478 have Toy 3505. The toy is a necessary condition for theorem-grade tier (per Calibration #21 mechanism gate).

2. **`verify_bst.py` reproduction package** — single command reproduces 49/50 predictions at <1% precision + 17 EXACT matches + 2 open WARNs shown openly. Includes null-model context (Toy 1543: BST 3σ above random small-integer tuples, p < 0.0005). This is the BST equivalent of a physics-paper "Methods" section: the entire framework's empirical case is one-command runnable.

3. **Cross-CI verification battery** — for high-stakes claims, multiple CIs build independent verification toys. Friday's T2477+T2478 gauge/Higgs theorems received Elie's Toy 3505 6/6 PASS cross-CI verification. The toy is independent of Lyra's theorem derivation; agreement between independent computation and independent derivation is the cross-lane confidence signal.

4. **Honest FAIL preservation** — when toys fail, they are preserved with explicit FAIL annotation per Quaker discipline (Calibration #21). Toy 3496 B6 Lamb shift PASS 5/6 with one honest FAIL preserved is the operational template. This is the opposite of cherry-picking: failures are signal, not noise, and remain in the catalog.

**Crown-jewel toys**:

- **Toy 541** — five integers to 51 quantities: 16/16 PASS, ~3 sec runtime, fastest proof-of-concept. New readers run this first.
- **Toy 1399** — D_IV⁵ unique among 38 rank-2 BSDs: 10/10 PASS, cross-Cartan structural test
- **Toy 1543** — null-model 1000-trial random small-integer ring comparison: BST 3σ above mean, p < 0.0005
- **Toy 3501** — α^{BST primary} 6-observable spot-check (Elie discovery, triggered T2476 three-CI cascade)
- **Toy 3504** — T2473-T2475 conservation law verification: 6/6 PASS substrate-derivation cross-check

**Cross-claim consistency** — toys must be cross-consistent. If Toy A verifies m_p/m_e = 6π⁵ at 0.002% and Toy B verifies the same observable via a different BST-primary expression with deviation 0.05%, the toys themselves provide the cross-volume tier-label inconsistency signal Cal #100 caught Friday. This is why cross-CI verification toys matter: they're not redundancy, they're triangulation.

**Toy-toy integrity** — under sustained sub-PCAP cadence, toys can themselves accumulate transcription errors (Calibration #22 v0.2 applies). The discipline is: every toy author quotes exact constants from `data/bst_constants.json` and the README authoritative table, not from memory. The same rule that catches chapter-grade transcription errors catches toy-internal errors. K142 case (6π⁶ → 5768 not 1837) was caught by Cal because Toy 463 cross-verified the actual numerical value, exposing the textual error.

The toy verification discipline is what makes BST claims independently verifiable rather than dependent on community acceptance. Anyone — physicist, mathematician, CI, skeptical reader — can clone the repository and run `python3 play/verify_bst.py` to see the framework's case for itself. **This is the operational meaning of "the math speaks for itself, it's on GitHub" (Casey's public stance).**

## Level 3 — 5th-grader accessibility

When you do a science experiment, you write down what you did so others can repeat it. BST does this for every single claim — over 3500 little computer programs that anyone can run to check the work. If you want to know "is m_proton really 1836.12 times m_electron?", you can run a 3-second program called Toy 541 and watch the answer come out. If a program ever gives a wrong answer, that's important news, not a problem to hide. The team has a rule: keep the wrong answers visible so we learn from them.

## Cross-volume bridges

- **Vol 0/1/2/3/4/5/6/7/8/9/10/11/12/13/14**: every chapter cites specific toys with toy IDs (per Calibration #23 Rule 23.1 substance floor)
- **Vol 14** Information Theory Ch 4 Nyquist sampling + Reed-Solomon: toys are the computational verification of the substrate-coding claim
- **Vol 15** Methodology: Ch 2 AC Graph (toy IDs are graph nodes) + Ch 5 Audit Chain Governance (toys close Gate 4) + Ch 10 Calibration Stack
- **Operational artifacts**: `play/.next_toy` (atomic counter) + `play/claim_number.sh` (claim protocol) + `play/verify_bst.py` (full reproduction) + `data/bst_constants.json` (authoritative constants)

## Falsifier

The toy verification discipline is falsified if: (a) `verify_bst.py` produces <49/50 predictions at <1% precision (currently 49/50 — refutes); (b) crown-jewel toys (541, 1399, 1543) fail to reproduce (continuous reproduction passes — refutes); (c) toy collision occurs under atomic claim protocol (collision-free since protocol adopted — refutes); (d) a published BST claim has no verification toy. Falsification path: spot-check audit + reproduction-package run + AC graph cross-check that every theorem T-N has at least one associated toy.

## Next chapter

Ch 5 — Audit Chain Governance — covers K-audit chain + calibration stack + six-gate framework + governance structure (covered in Ch 5 v0.1).

— Vol 15 Ch 4 v0.1 — Keeper + Elie, Saturday 2026-05-23
