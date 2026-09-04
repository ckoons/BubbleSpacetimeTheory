# Retention under construction — RUNG 6: the second instance, and what it takes away
**Lyra, for Casey. Friday 2026-09-04, 13:43 EDT (from `date`). NOT posted to the board. Scripts `play/lyra_retention_dimer{,_constructions}_2026-09-04.py`.**

## 1. The instance

Perfect matchings of a torus grid, moved by flipping an alternating four-cycle. Different objects from colourings, a different dynamics, and **no colour group at all**, so any class structure here is automatically free of the gauge worry that dogged the first instance.

| torus | matchings | classes | retained | largest class |
|---|---|---|---|---|
| 4 by 4 (lattice faces only) | 272 | 17 | 4.087 bits | 132 |
| 4 by 6 (lattice faces only) | 3,108 | 15 | 3.907 bits | 1,456 |

This is the non-degenerate record space the program needed: four bits, carried by classes of over a thousand states, with real interiors.

**The invariant is the winding number**, and on the 4 by 6 torus it separates the classes exactly. On 4 by 4 it does **not**: unflippable configurations sit alone, so the classes are strictly finer than the topological invariant. Anyone identifying "the record" with "the topological charge" should note that the dynamics can see more than the topology does.

**A caution about the move set.** With lattice faces only, the 4 by 4 torus has 17 classes; allowing every alternating four-cycle, which adds the ones that wrap the torus, it has 9. The record is a property of the pair, states and dynamics, and changing the permitted moves changes what is retained. That is a modelling choice and must be declared, not assumed.

## 2. The test, and the demotion

Construction: add two new vertices joined to each other, join one to a set S and the other to a set T, and map each parent matching to itself plus the new pair. This is total and injective, the exact analogue of the colouring construction.

| attachment | parent classes | child classes | merged? |
|---|---|---|---|
| S and T of size 1 | 9 | 9 | no |
| S and T of size 2 | 9 | 9 | no |
| **S and T of size 3** | **9** | **6** | **YES** |
| both joined to the same vertex | 9 | 9 | no |

**Growth destroyed a record.** Nine classes became six under a total construction.

**What this takes away.**
- "Adding structure cannot destroy a record" is **false as a general sentence**. I used it all day as the mechanism of rung 2. It is true only when the construction admits a retraction of the dynamics, which is the hypothesis the theorem actually carries.
- Rung 4's Corollary 4.1, that a total step gives a bijection on classes and can never create or destroy, is likewise **a colouring fact, not a record fact**. Here the step is total and the class count falls.

**What survives, unchanged.** The retraction theorem itself, R2.2, is stated with its hypothesis and is untouched: where a retraction exists, nothing merges. In colourings restriction is always available, because a colouring restricted to a subgraph is still a colouring, and that is why 669,812 accretions never merged. In dimers restriction is only defined when the new pair is matched to itself, so once the new vertices can be matched into the host the retraction breaks. The lightly attached cases still retain, so the hypothesis is sufficient and not necessary: its failure permits merging without compelling it.

## 3. What rung 6 was for

It was for exactly this. Two sentences I had been treating as results about records were results about colourings, and one theorem was general all along because it had been stated with the right hypothesis. The program is better for the loss.

**Corrected headline set:**
1. A construction that admits a retraction of the dynamics cannot destroy a record. Otherwise it can, and does.
2. A write is a refusal. **Status: proved for colourings, untested here.** The dimer analogue of the accretion theorem is now known to be false, so the creation claim must be re-derived in this instance rather than assumed.
3. A bit costs a cut, and the price is the forgetting rate. Instance-independent, since it rests only on connectivity and Cheeger.
4. A cold start scales with what the assembly fixed. Untested here.

## 4. Owed

Items 2 and 4 above, in the dimer instance. The 6 by 6 torus, at 90,176 matchings, is enumerable but was skipped today. And a third instance is not needed until these two are settled.

— Lyra
