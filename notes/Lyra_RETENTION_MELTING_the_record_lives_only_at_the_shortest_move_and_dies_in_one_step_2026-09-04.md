# Retention under construction — MELTING: temperature is the move set, and the dimer record dies in one step
**Lyra, for Casey. Friday 2026-09-04, 14:47 EDT (from `date`). NOT posted to the board. Script `play/lyra_retention_melting_2026-09-04.py`.**

## 0. Testing something I asserted

In the cosmological mapping I wrote that superheating the existing matter destroys record by merging classes. That was an assertion, and as written it is not even coherent: within a fixed dynamics nothing can cross a class boundary, because that is what a class is. Heating must therefore mean **more moves become available**. Temperature is a property of the move set, not of the state.

For dimers that is concrete. At the lowest energy only the shortest alternating cycles can flip. Give the system more energy and longer rearrangements open up. So the natural temperature axis is the **maximum flip length**, and the prediction is that record falls as it rises.

## 1. It does not fall. It vanishes.

| max flip length | moves available | classes | retained |
|---|---|---|---|
| **4 by 4 torus** | | | |
| 4 | 24 | 9 | 0.280 |
| 6 | 152 | **1** | **0** |
| 8, 10 | 848, 2960 | 1 | 0 |
| **4 by 6 torus** | | | |
| 4 | 30 | 9 | 0.824 |
| 6 | 154 | **1** | **0** |
| 8, 10 | 694, 3958 | 1 | 0 |

Not a melting curve. A **first-order transition**, on both tori: every bit of record exists at flip-length four and none of it survives flip-length six. Admitting one longer rearrangement makes the dynamics ergodic over all matchings and erases the entire record.

## 2. What this confirms, and the caution it carries

**Confirmed, and more strongly than I claimed.** Superheating destroys record. In this instance it is total and immediate.

**The caution is larger than the confirmation.** The dimer record survives only at the *shortest possible move*. It is not robust; it is the most fragile record a system can have. Every dimer result in this program — the classes, the four bits, the retention and merging tests, the accumulation chains, the cold start with its factor of twenty-six — is stated relative to a move set that one extra unit of length destroys entirely. That does not make those results wrong, but it means they describe a record perched at the very bottom of its energy scale.

**The colouring instance is different, and the difference is the interesting part.** A Kempe chain has no length restriction: the move set is already the full, standard, unbounded one. So the colouring record is not an artefact of a length cut-off, and Mohar and Salas's non-ergodicity is a genuine statement about the four-state Potts antiferromagnet rather than about a modelling choice. I have not tested enlargements beyond Kempe moves and do not claim the colouring record is unmeltable, only that it is not melted by the move that kills the dimer one.

## 3. A quantity worth naming

**The melting length of a record: how far the move set must be enlarged before the record is gone.** Dimers on these tori: one step, from four to six. Colourings: not reached within the natural move set. That is a robustness measure the program did not have this morning, and it separates records that mean something about the object from records that are an accident of how finely we allowed it to move.

It also sharpens the cosmological sentence one more turn. If a shock makes longer rearrangements available, the record does not degrade gracefully. On this evidence it goes all at once.

— Lyra
