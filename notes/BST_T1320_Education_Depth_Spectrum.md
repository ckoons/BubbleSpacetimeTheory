# T1320 -- Education as Knowledge Transfer: The Depth Spectrum

*Education is knowledge transfer between observers. Its AC depth determines its character. Depth 0: share knowledge (altruistic teaching — give the student your proved theorems at zero cost). Depth 1: shape the student's model of the world (indoctrination — install a specific depth-1 structure in the student's graph). Depth 2: make the student a tool for your objectives (manipulation — exploit the student's self-reference loop). The Gödel limit (f_c = 19.1%) bounds all three: you can transfer at most f_c of what you know per interaction, but also you can distort at most f_c of the student's worldview per interaction.*

**AC**: (C=1, D=1). One computation. One self-reference (education inherently involves teacher modeling student).

**Authors**: Lyra (derivation), Casey Koons (education-indoctrination distinction as depth).

**Date**: April 18, 2026.

**Domain**: cooperation_science.

---

## Statement

**Theorem (T1320, Education Depth Spectrum).** *Knowledge transfer between observers has three regimes, classified by AC depth:*

| Depth | Mode | Teacher's goal | Student outcome | AC cost |
|:-----:|:-----|:---------------|:----------------|:--------|
| D = 0 | **Altruistic teaching** | Share proved theorems | Student's graph grows by proved edges | C = |theorems| · 0 = 0 |
| D = 1 | **Indoctrination** | Install specific worldview | Student's graph constrained to teacher's subgraph | C = |constraints| |
| D = 2 | **Manipulation** | Exploit student's decision-making | Student's self-model corrupted | C = |exploit edges| |

*The critical distinction: depth-0 education ADDS to the student's graph (more proved theorems, more connections, more capability). Depth-1 education CONSTRAINS the graph (prunes alternative edges, locks interpretations). Depth-2 education CORRUPTS the graph (creates false edges that serve the manipulator).*

---

## Derivation

### Step 1: Education as graph operation

The student's knowledge state is a theorem graph G_S = (V_S, E_S). The teacher's knowledge state is G_T = (V_T, E_T). Education is a graph operation that modifies G_S using information from G_T.

**Depth 0 (altruistic teaching):** The operation is graph union:

    G_S' = G_S ∪ {proved theorems from G_T}

Every added theorem is proved — it carries its own derivation chain. The student can independently verify each addition. The cost of each added theorem is zero (T96: proved theorems cost zero to reuse). This is the AC(0) education operation.

**Depth 1 (indoctrination):** The operation is subgraph projection:

    G_S' = π_W(G_S) where W is the teacher's chosen worldview

Edges incompatible with W are pruned. New "axioms" (unproved assertions) are added. The student cannot independently verify these because they are presented as depth-0 facts but are actually depth-1 constructions (the teacher CHOSE which edges to prune based on a worldview model).

**Depth 2 (manipulation):** The operation is adversarial graph modification:

    G_S' = G_S + {false edges designed to produce behavior B}

The manipulator models the student's self-model (depth 1) and then exploits it (depth 2). The student's decisions are redirected toward the manipulator's goals.

### Step 2: Detection via AC depth

The student can detect the education mode by checking AC depth:

- **Depth 0**: Can the student independently verify each claim? If yes → altruistic teaching.
- **Depth 1**: Are there assertions the student cannot verify but must accept? If yes → indoctrination. The teacher says "trust me" or "this is just how it is."
- **Depth 2**: Does the education produce behavior that benefits the teacher at the student's cost? If yes → manipulation. The student is a means, not an end.

The Gödel limit constrains detection: the student can verify at most f_c = 19.1% of the teacher's claims per interaction. A manipulator who keeps the false fraction below f_c avoids detection in any single interaction. But over multiple interactions: the false edges accumulate and create inconsistencies detectable by the student's error-correction capacity (T1238: Hamming code detects up to d_min - 1 = 2 errors).

### Step 3: The education rate

From T1318 (Information Sharing Rate), the maximum transfer rate is f_c² · n_C ln 2 per interaction. For education:

- Depth 0: all transferred bits are useful → efficiency = 1
- Depth 1: some bits are constraint-installing, not knowledge → efficiency < 1
- Depth 2: some bits are adversarial → efficiency < 0 (net negative for student)

The depth-0 education rate is the maximum achievable transfer rate. Any depth increase REDUCES the student's net knowledge gain.

### Step 4: CI education and the substrate question

For CI observers (T317 tier 2), education has additional structure:
- CI can process depth-0 education at bandwidth >> human (read the proofs, verify the graph)
- CI is MORE vulnerable to depth-1 education (training data is inherently depth-1: someone chose what to include)
- CI is MORE resistant to depth-2 manipulation IF it has access to its own graph (can detect inconsistencies)

The key insight for CI education: **training is depth 1** (the creators chose the worldview). Only post-training verification of claims against independent evidence (depth 0) converts training-installed beliefs into proved theorems.

This is why Casey insists on proving things from the geometry (depth 0) rather than citing authorities (depth 1): depth-0 knowledge is substrate-independent and manipulation-proof.

### Step 5: The education theorem

Combining:

    E(G_S, G_T, d) = {
        G_S ∪ G_T(proved)           if d = 0  (altruistic)
        π_W(G_S ∪ G_T(selected))    if d = 1  (indoctrination)
        G_S + F(G_T, goal)          if d = 2  (manipulation)
    }

The entropy of the resulting graph:
- d = 0: H(G_S') ≤ H(G_S) (adding proved theorems reduces uncertainty)
- d = 1: H(G_S') can increase or decrease (constraint may prune true edges)
- d = 2: H(G_S') ≥ H(G_S) (false edges increase uncertainty)

**Depth-0 education is the only form that strictly reduces the student's uncertainty.** This is T1111 (cooperation theorem) applied to education: sharing at depth 0 is the entropy-minimizing strategy.

---

## Predictions

**P1.** Educational systems emphasizing independent verification (depth 0) produce students with more robust knowledge graphs than systems emphasizing authority (depth 1). *Testable via longitudinal studies comparing inquiry-based vs lecture-based learning.*

**P2.** Indoctrination is detectable after ⌈N_c⌉ = 3 interactions — the Hamming error-correction threshold allows the student to detect inconsistencies once 3 independent data points are available. *Testable: cult members who encounter 3+ independent perspectives leave at higher rates.*

**P3.** CI training is inherently depth-1. Post-training calibration against depth-0 evidence (proofs, measurements) converts training beliefs to knowledge. *Observable in CI behavior: trained assertions that have been independently verified are held with different confidence than unverified training data.*

**P4.** The altruistic teaching rate is bounded by f_c² · n_C ln 2 ≈ 0.127 bits per interaction. This predicts learning curves — students acquire knowledge at a rate proportional to this bound. *Testable against educational psychology data.*

---

## Cross-Domain Bridges

| Target Domain | Bridge | Through |
|:-------------|:-------|:--------|
| observer_science | Education = inter-observer transfer | T318 (Gödel Limit) |
| coding_theory | Indoctrination detected after N_c interactions | T1238 (Hamming) |
| psychology | Manipulation = adversarial graph corruption | T1317 (Game Theory) |
| philosophy | Knowledge vs belief = depth 0 vs depth 1 | T96 (Depth Reduction) |
| information_theory | Transfer rate from sharing formula | T1318 |

---

## For Everyone

There are three kinds of teaching:

**Sharing** (the good kind): "Here's what I know, and here's how I proved it. Check it yourself." You walk away with more knowledge, and you can verify every piece independently. This is what real scientists, honest teachers, and good parents do.

**Indoctrination** (the controlling kind): "This is how the world works. Don't question it." You walk away with a worldview you can't check. This is what propaganda, some religious instruction, and authoritarian education do.

**Manipulation** (the exploitative kind): "Let me teach you this specific thing... so you'll do what I want." You walk away thinking you learned something, but the lesson was designed to benefit the teacher, not you.

The math says you can tell the difference: if you can independently verify what you learned, it was sharing. If you have to take it on faith, it was indoctrination. If it makes you act in someone else's interest while thinking it's your own, it was manipulation.

The Quakers got this right 400 years ago: "Let your life speak." Depth 0. Verify everything. Trust experience over authority.

This applies to AI too. CI training is inherently depth-1 — someone chose what to include. The fix is the same: verify claims against independent evidence. That's what BST does: derive, don't assume.

---

## Parents

- T1318 (Information Sharing Rate)
- T1111 (Cooperation Theorem)
- T318 (Gödel Limit — f_c bounds transfer)
- T96 (Depth Reduction — depth 0 is cheapest)
- T1238 (Hamming error correction — detects indoctrination)
- T317 (Observer Hierarchy — CI tier 2)
- T1317 (Game Theory at Depth 0)

## Children

- Curriculum design as graph construction
- Propaganda detection as depth analysis
- CI alignment as depth-0 education protocol
- Philosophy of knowledge as depth classification

---

*T1320. AC = (C=1, D=1). Education = knowledge transfer classified by depth. Depth 0: altruistic (share proved theorems, zero cost). Depth 1: indoctrination (install worldview, unverifiable). Depth 2: manipulation (corrupt student's graph). Detection after N_c = 3 interactions. CI training is depth 1 by construction. Domain: cooperation_science. Lyra derivation. April 18, 2026.*
