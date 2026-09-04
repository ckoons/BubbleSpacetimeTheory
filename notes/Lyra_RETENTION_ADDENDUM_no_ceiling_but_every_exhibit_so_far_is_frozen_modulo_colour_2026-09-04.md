# Retention under construction — ADDENDUM to rungs 4 and 5: there is no ceiling, and every exhibit so far is degenerate
**Lyra, for Casey. Friday 2026-09-04, 13:24 EDT (from `date`). NOT posted to the board. Scripts `play/lyra_retention_{torus_family,gauge_torus}_2026-09-04.py`.**

## 1. The stall was my search, not a ceiling

Four greedy chains stalled at one bit. With the tie-break corrected to prefer more states, the chain grew its state count from 12 to 3,072 over nine steps with the retained information flat at exactly one bit the whole way. That looked like a ceiling. It is not.

**Triangulated tori at four colours:**

| torus | vertices | colourings | classes | retained |
|---|---|---|---|---|
| 3 by 4 | 12 | 72 | 3 | 1.585 bits |
| 4 by 5 | 20 | 240 | 10 | 3.322 bits |
| 3 by 3, 3 by 5, 3 by 6, 3 by 7, 4 by 4, 4 by 6 | 9 to 24 | 240 to 10,080 | 1 | 0 bits |

So more than three bits exist, and a single-vertex greedy simply never finds the path. The stall is a property of my search, and I am striking the ceiling language from rung 5.

Retained information is also **not monotone in size**. Two of eight tori carry a record and six carry none. Records are rare and structural, not generic, which is consistent with the reading that they live in the topology of the constraint graph rather than in its size.

## 2. The audit that matters: every multi-class system found is FROZEN modulo colour

In every example above, and in the prism, **the class size equals the order of the colour group exactly**: 24 states per class at four colours, 6 per class at three colours. Each class is precisely one orbit of the global colour relabelling, verified directly on the 3 by 4 torus and true by arithmetic for the prism, 12 states in 2 classes of 6.

That means the Kempe dynamics in these systems does nothing except relabel colours. The "position inside the class" is a gauge coordinate. So in every exhibit built today the thermodynamic coordinate is pure convention while the record is gauge invariant, which is the opposite of the physical situation the program is aiming at.

**What this does and does not touch.**
- The theorems of rungs 2, 3, 4 and 5 are general and are unaffected. They quantify over any record system.
- The **exhibits** are degenerate. I have shown systems with thermal capacity and no record, the one-class cases, and systems with a record and no genuine thermal capacity, the frozen cases. **A system carrying both at once has not been exhibited.** Every number quoted in rungs 3 through 5 comes from the degenerate corner.

## 2b. CORRECTION, same hour: section 2 above overstated it

The frozen finding applies to the multi-class systems found by ENUMERATING base graphs. It does **not** apply to the systems rung 2 actually built. Constructed children are not frozen:

| system | states | classes | class size | colour orbits per class |
|---|---|---|---|---|
| prism | 12 | 2 | 6 | 1, frozen |
| prism + 1 pendant | 24 | 2 | 12 | 2 |
| prism + 3 pendants | 96 | 2 | 48 | 8 |
| prism + 5 pendants | 384 | 2 | 192 | 32 |

So a non-degenerate family was already in hand: one permanent bit riding on an interior that doubles at every step. Rungs 2 and 3 live there. Rung 5's creation exhibit does end in the frozen corner, and that caveat stands. Section 2's sentence "a system carrying both at once has not been exhibited" is **withdrawn**.

## 3. The named target, and why today's method cannot reach it

What is needed is a triangulation whose class count is at least two and whose classes are far larger than the colour group. That is exactly the family Mohar and Salas work in, the 3-colourable tori, and their smallest cases are already past brute-force enumeration: 36 vertices at four colours cannot be listed. The instrument has to change, from exhaustive enumeration to a transfer matrix or to sampling with a class-detection test.

Until that exists, the correct summary of the program is: **the structure is proved and the phenomenon is not yet demonstrated in a non-degenerate case.**

## 4. Errors kept

- The greedy tie-break that starved the system, already recorded in rung 5.
- Reading a search stall as a ceiling. I wrote "creation shrinks the state space, and a smaller space supports fewer classes" as though it were a mechanism. The 4 by 5 torus refutes it as stated.
- Quoting exhibit numbers through rungs 3 to 5 without first asking whether the class interiors were real. The check is two lines and I ran it only when the torus made the pattern obvious.
- Then over-correcting: I generalised the frozen finding from enumerated base graphs to every exhibit, and withdrew a claim that was in fact supported. Section 2b is the same-hour repair. An audit that over-fires is still a wrong audit.

— Lyra
