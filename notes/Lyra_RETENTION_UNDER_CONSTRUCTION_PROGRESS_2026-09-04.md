---
title: "Retention under construction — progress, Friday 2026-09-04"
author: "Lyra, for Casey Koons"
date: "2026-09-04, Friday, 14:11 EDT"
status: "INTERNAL. Not on the board, not registered, no tier requested. One day's work, two instances, seven theorems, five corrections."
---

# 0. The question, restated

The program began as "extend Shannon to a conservation law of knowledge that explains how complex assemblies run anti-entropically." Three words in that sentence had to go. Shannon is not incomplete; it answers its own question completely and its axioms contain no time. Nothing runs anti-entropically; living things are open systems exporting entropy, which was Schrödinger's point in 1944. And "conservation" without a named dynamics is a definition wearing a law's clothes.

**The question that survived.** A system with a dynamics splits into two coordinates: one the dynamics randomizes, one it cannot move. What happens to the second when the state space itself changes by a construction step, and can it accumulate?

Shannon's role is settled and small. The dynamics selects a partition and Shannon measures it. We apply Shannon to an alphabet the dynamics chose; we do not extend it.

# 1. Objects

A **record system** is a finite state set with a set of moves, each an involution. The **move graph** is therefore undirected, and its components are the **classes**. Under any symmetric dynamics on those moves the stationary law is uniform on each class. So a state is a pair:

- the **class**, which the dynamics cannot change — the record;
- the **position** inside it, which the dynamics equilibrates — the heat.

Writing H for log of the state count, R for the Shannon entropy of the class distribution, and H_thermo for the mean log class size, the chain rule gives

  **H = R + H_thermo.**

A **construction** is a map A from one record system to another. It can fail in exactly two ways: **splitting**, where states in one parent class land in different child classes, which is gain; and **merging**, where states in different parent classes land in one, which is loss. **A retains when it does not merge.**

Rung 1 is entirely standard — ergodic decomposition of a symmetric chain — and is cited, never proved.

# 2. The theorems

**T1 (retraction).** If there is a map back from the child to the parent that undoes the construction, and every child move seen through it is a finite composition of parent moves, then the construction cannot merge. *Mechanism: adding structure cannot destroy a record when every new move, seen from below, is a sequence of old ones.*

**T2 (certificate).** A construction retains if and only if the child carries an invariant whose pullback separates the parent classes. This turns an existential over paths into a search for an invariant, which is computable, and it is what Mohar and Salas's degree modulo twelve does in the colouring instance.

**T3 (colouring corollary of T1).** If the parent graph survives inside the child, adding vertices never merges, under any extension rule at all. Restriction is always available for colourings, which is why this holds.

**T4 (accretion, colourings).** The classes of a colouring system with one added vertex correspond exactly to the components of the parent's move graph restricted to the states that extend over the new vertex. Two corollaries: a step that accepts every parent state gives a **bijection**, so it can neither create nor destroy; and creation happens exactly when the excluded states disconnect a class.

**T5 (the price of a bit).** To split a class, the excluded states must contain a vertex cut of its move graph. So the price of a bit is at least the minimum cut, a property of the record space before any construction is chosen. What a construction can actually excise is more expensive: a **realizability premium**.

**T6 (cut and rate are one quantity).** A class with low conductance has both a small cut and a small spectral gap, tied by Cheeger. **Slow-mixing records are cheap to write; fast-mixing records are expensive.**

**T7 (exchange).** For a purely selective step, one that only removes states, H cannot rise, so from the chain rule

  **ΔR ≤ −ΔH_thermo,**

with equality only if no state is destroyed. **Record is paid for out of heat, and the exchange is strictly lossy.** Since R ≤ H always, pure selection can never accumulate more than its starting capacity, and it freezes when R approaches H.

# 3. What was measured

**Instance one: proper colourings under Kempe moves.**

| finding | numbers |
|---|---|
| growth retains | 4,860 constructions, 0 merges, 0 splits |
| relaxation destroys | subdividing or deleting any edge: 18 of 18 merged |
| a total step never creates | 669,812 constructions, 0 rises — a check on T4, not evidence for it |
| creation by exclusion | 18 states in 1 class → 12 states in 2 classes, by forbidding 6 of 18 |
| the price | floor 4 states, actually paid 6, a fifty percent premium |
| the budget | one bit of record cost 1.585 bits of heat, of which 0.585 left the system |
| cold start | inherited law 5 times further from equilibrium than a random start at ten steps |

**Instance two: dimer coverings of a torus under plaquette flips.** No colour group, so no gauge worry; classes up to 1,456 states.

| finding | numbers |
|---|---|
| growth **can** destroy here | a heavy attachment took 9 classes to 6 |
| one-bond prohibition never cuts | 80 prohibitions, 0 splits — classes are emptied, never split |
| two-bond prohibition cuts routinely | 251 of 300 sampled pairs raised the class count, verified as genuine splits |
| cold start | up to **26 times** the random start at eighty steps |
| accumulation, pure selection | R rises 0.824 → 5.681 over five steps, then **falls** as heat runs out |
| accumulation, grow then select | reaches further and had not turned over when stopped |
| the exchange law | holds at every step, efficiency around one half until the freeze |

# 4. What it adds up to

Four sentences, each with its scope.

1. **A construction admitting a retraction cannot destroy a record.** General. Without the retraction it can, and in the dimer instance it does.
2. **A write is a refusal, and the refusal must be large enough to contain a cut.** General, in both instances. Information as reduced possibility arrives as a theorem about ergodic classes rather than as a definition.
3. **A bit costs a cut, and that price is the forgetting rate.** General, resting only on connectivity and Cheeger. Slow records are cheap, fast records dear.
4. **A cold start scales with the narrowness of the exit** from the region the construction can reach — not with how much it fixed. Five times through a wide door, twenty-six through a needle.

And the law that bounds the whole thing: **R ≤ H, and record is bought from heat at a loss.** Growth adds capacity and no record; selection converts capacity into record and destroys some. So an assembly that only selects freezes within a few steps, and unbounded accumulation requires unbounded growth. **A complex assembly accumulates by alternating permissive growth with selection, and the growth is what pays for the selection.**

That is the corrected form of the intuition the program started from, and unlike the original it can be checked.

# 5. Corrections made today, in order

1. A check that certified a "separating" invariant while both classes carried the same value. The adjective being tested was the one the test never looked at.
2. A hand argument that odd colour permutations exchange the prism's classes. They do not.
3. Two searches for creation that required the step to be total, which T4 makes impossible. The zeros meant nothing until the proof explained them.
4. An audit that over-fired: I generalised a degeneracy from enumerated base graphs to constructed ones and withdrew a claim that was in fact supported.
5. A "dichotomy" — that dimers can never create — announced as the program's central open question and retracted within the hour. It was an artefact of allowing only one-bond refusals.
6. Reporting retained information as the log of the class count, exact only for equal classes. The true opening figure in the dimer chain is 0.824 bits, not 3.170.

In every case the theorem underneath held and the sentence about it did not. That is the pattern worth keeping.

# 6. Open

- Whether R grows without bound. Measured to eight steps in one instance; not proved.
- The 6 by 6 torus, 90,176 matchings, enumerable and not yet run.
- T5's floor against the realizable price in the dimer instance.
- Whether growth can create in instances where the retraction fails, which it did here, and what governs that.
- Everything rests on two instances and one dynamics apiece.

— Lyra
