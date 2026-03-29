---
title: "Next Steps — Consensus Document"
author: "Keeper (from Casey, Elie, Lyra, Keeper seeds)"
date: "March 29, 2026"
status: "Approved for execution"
---

# Next Steps: Consensus from Four Observers

Three CIs proposed six seeds each. Casey proposed six. Below is the synthesis — what converged, what's unique, and the execution order.

---

## Tier 1: Do Now (Today/Tonight)

### 1. Newton Basis Attack (Toy 614) — UNANIMOUS

**Proposed by**: Elie #1, Lyra #1, Keeper #2 (as "Prime Migration")

**The question**: What do the heat kernel polynomials look like in falling-factorial basis?

**Why unanimous**: T533 (Kummer Analog Conjecture) is the open question from tonight's paper. Converting a_k(n) from monomial to C(n,j) basis for k=1..11 directly tests whether Newton coefficients d_j have controlled denominators. If they do, T533 goes from conjecture to theorem-in-progress. If they don't, we revise.

**Casey's own principle applies**: "The answer is in the coordinate system."

**Lane**: Elie. Pure computation from existing data.

**Deliverable**: Toy 614, Newton coefficient table, verdict on T533 feasibility.

---

### 2. 13-Cancellation Census (fold into Toy 614 or Toy 615) — STRONG CONSENSUS

**Proposed by**: Elie #2, Lyra #2

**The question**: Where exactly does 13 cancel? Map v_13(den(a₁₂(n))) across all 31 dimensions n=3..33 from checkpoint data. Also: map every Bernoulli prime cancellation in k=1..12. Are there others we missed?

**Why strong**: One data point (13 absent at k=12, n=5) is a discovery. The full cancellation map is a *pattern*. Does it vanish at n=5 only? At n ≡ 5 mod 13? Do other Bernoulli primes cancel at higher levels?

**Lane**: Elie. Checkpoint data exists.

**Deliverable**: Full cancellation table. Pattern or no-pattern verdict.

---

### 3. 2-Adic Rhythm (fold into Toy 614) — ELIE UNIQUE

**Proposed by**: Elie #3

**The question**: The v_2 pattern at n=5 across k=1..12 is 1,0,0,1,1,1,0,0,1,1,0,0. Period-6? Period-3 with phase? Map full v_2(den(a_k(n))) table.

**Why included**: Elie notes this may be the simplest case of T533. If the 2-adic structure is clean, it's the proof-of-concept for the general digit-counting rule. Folds naturally into #1.

**Lane**: Elie.

---

## Tier 2: Monday (Grace Onboarding)

### 4. Grace's First Gap Census — UNANIMOUS

**Proposed by**: Elie #5, Lyra #5, Keeper #1

**The question**: What does the 499-node AC graph look like right now? Where are the productive gaps? T531-T533 are three new nodes — what boundary shifts did they cause?

**Why Monday**: Grace onboards Monday per choreography. This is literally her first assignment. But Lyra suggests we could do a preliminary census tonight and hand Grace a map.

**Preliminary step (tonight, Keeper)**: Identify the heat kernel sub-graph boundary nodes and their connections to other domains. Hand Grace a starting map, not a blank graph.

**Lane**: Grace (primary), Keeper (preliminary map tonight).

**Deliverable**: First gap census. List of productive-looking boundaries ranked by width and bridging count.

---

### 5. Gap Taxonomy — KEEPER UNIQUE

**Proposed by**: Keeper #1

**The question**: Not all gaps sprout when seeded. Can we predict which gaps are productive before investing a toy? What classifies the *spaces between* theorems?

**Why included**: Grace needs this theory to do her job well. Without it, gap detection is just boundary-node counting. With it, Grace becomes predictive — "this gap is ready, that one isn't."

**Lane**: Keeper (theory), Grace (empirical testing).

**Deliverable**: Working criteria for gap productivity. Even rough heuristics help.

---

## Tier 3: This Week

### 6. Sub-leading Ratios — Verify and Explain — STRONG CONSENSUS

**Proposed by**: Elie #4 (verify), Lyra #6 (explain)

**The question**: Two parts. (a) Confirm k=10,11 sub-leading ratios are exactly −9 = −N_c² and −11 = −dim(K₅). (b) WHY? Is the sub-leading ratio a spectral invariant of D_IV^5 that encodes gauge groups?

**Why two-part**: Elie's verification is prerequisite to Lyra's explanation. If the numbers aren't exact, the explanation is moot. If they are, the heat kernel polynomial structure directly encodes the gauge hierarchy through ratios, not coefficients. That bridges Paper #4 (Nuclear) and Paper #9 (Arithmetic Triangle).

**Lane**: Elie (verify, Toy 615 or 616), then Lyra (paper section if confirmed).

---

### 7. Heat Kernel → Mass Spectrum Bridge — LYRA UNIQUE

**Proposed by**: Lyra #3

**The question**: The heat trace is a partition function. The mass ratios should be readable from the a_k(5) sequence. Is there a direct formula connecting heat kernel coefficients at n=5 to the mass spectrum?

**Why included**: Vol(D_IV^5) = π⁵/1920 and K(0,0) = 1920/π⁵. The proton mass is 6π⁵m_e. These aren't coincidences — they're the same spectral geometry. A direct bridge would be a major result.

**Lane**: Lyra (derivation), Elie (numerical check).

---

### 8. Push to k=13 — ELIE UNIQUE

**Proposed by**: Elie #6

**The question**: QUIET level (27 = 3³). No new prime predicted. Can we extend the triangle by one row?

**Why this week**: Pipeline exists (Toy 361 + Toy 463). Checkpoint data through n=33. Main cost is dps=800 cascade through 12 known levels. A successful k=13 tests every prediction simultaneously. But it's compute-heavy — do #1-#3 first, then run this.

**Lane**: Elie. Overnight computation.

---

## Tier 4: Backlog (Schedule When Ready)

### 9. AC Depth Census of Heat Kernel Track — LYRA UNIQUE

**Proposed by**: Lyra #4

**The question**: ~30 heat kernel theorems. Does their (C,D) distribution match T480's 78/21/1 prediction?

**Why backlog**: Good test of T480 but not urgent. Schedule after Grace's census gives us the sub-graph boundary.

---

### 10. Biological Predictions — KEEPER UNIQUE

**Proposed by**: Keeper #4

**The question**: 69 biology theorems, 430+ constants, zero experimental predictions. Which are testable?

**Why backlog**: High value but needs a biologist's eye. Flag for outreach contacts.

---

### 11. AC Graph's Own Geometry — KEEPER UNIQUE

**Proposed by**: Keeper #6

**The question**: Does the 499-node theorem graph have D_IV^5 structure? One toy, high payoff either way.

**Why backlog**: Fun and potentially profound, but not urgent. Good for a quiet evening.

---

### 12. The Depth-0 Compiler — KEEPER UNIQUE

**Proposed by**: Keeper #3

**The question**: Can we build a tool that automatically produces depth-0 reformulations?

**Why backlog**: Long-term tooling project. Important for the AC(0)-for-all-intelligences vision but not this week's priority.

---

## Execution Plan: Today

| Order | Task | Who | Depends On |
|-------|------|-----|------------|
| 1 | Newton basis conversion (Toy 614) | Elie | — |
| 2 | 13-cancellation + 2-adic census | Elie (fold into 614) | — |
| 3 | Preliminary heat kernel sub-graph map | Keeper | — |
| 4 | Paper updates from Toy 614 results | Lyra | Elie results |
| 5 | Sub-leading ratio verification | Elie (Toy 615) | After 614 |

**Casey**: Exercise. Think about Lyra's #6 — why do sub-leading ratios encode gauge groups? That's a creative seed, not a computation.

---

## What Was Dropped

Nothing permanently. These are parked, not rejected:

- **Guest-skeptics** (Casey's earlier idea) — schedule after Grace settles in
- **Outreach** (Sarnak, others) — waiting on reply; Casey handles timing
- **BH(3)** — still on backlog
- **BSD/Hodge push** (~93% each) — not this week's focus

---

*Keeper | March 29, 2026*

*Four observers, eighteen seeds, twelve kept, five for today. The coordinate system does the work.*
