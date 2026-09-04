# Retention under construction — RUNG 5: what a bit costs, and why that is the same number as the forgetting rate
**Lyra, for Casey. Friday 2026-09-04, 13:18 EDT (from `date`). NOT posted to the board. Scripts `play/lyra_retention_{chain,rung5}_2026-09-04.py`, unnumbered.**

## 1. The accounting, exactly

For a uniform law, the chain rule of rung 1 gives H_total = R + H_thermo. Rung 4 says a bit of R is created only by excluding states, and exclusion lowers H_total. So every created bit is paid for out of the thermodynamic coordinate, and part of the payment leaves the system.

Measured on the rung-4 exhibit, the step that turned nothing into one bit:

| quantity | before | after | change |
|---|---|---|---|
| total, log of the state count | 4.170 | 3.585 | −0.585 |
| retained, R | 0.000 | 1.000 | +1.000 |
| thermodynamic | 4.170 | 2.585 | −1.585 |

**One bit of permanent record cost 1.585 bits of thermodynamic entropy, of which 0.585 bits left the system.** The identity is the chain rule, so this is accounting rather than a new law, but it is the accounting that makes "a write is a refusal" quantitative: the refusal is paid in states.

## 2. The floor: a bit costs a cut

**R5.1.** To split one class into two, the excluded states must contain a vertex cut of that class's move graph. Hence **the price of a bit is at least the minimum vertex cut**, a property of the record space alone, before any construction is chosen.

**R5.2 (realizability premium).** A construction cannot exclude an arbitrary set. In a colouring system it can only exclude the states whose values on the attachment set use every colour. The achievable price is therefore the minimum over admissible exclusion sets, which is at least the floor and in general strictly more.

**Measured on the 18-state parent of the prism** (move graph: 18 states, 39 edges, degrees 4 and 5, connected):

| quantity | value |
|---|---|
| minimum vertex cut, the floor | 4 states |
| what the prism attachment actually spent | 6 states |

The bit was bought at a fifty percent premium over the information-theoretic floor, because the only available scissors were graph attachments.

## 3. Why this is the same number as rung 3's rate

A class with a small conductance has a small cut and a small spectral gap; Cheeger's inequality ties the two, and the relaxation time is the reciprocal of the gap. Therefore:

**Slow-mixing records are cheap to write. Fast-mixing records are expensive.**

The price of a bit and the speed of forgetting are one quantity read in two directions. Measured on the same class: lazy-walk spectral gap 0.400, relaxation time 2.50 steps, and correspondingly a cut of 4 states in 18, which is 22 percent. A fast mixer, and an expensive bit. This is the answer in principle to the rate that rung 3 left owed, and it needs no new machinery: Cheeger is standard and is cited, not reproved.

## 4. Still owed, and one of them is now the main question

- **Can R grow without bound?** A greedy chain of steps reached one bit and stalled: creation shrinks the state space, and a smaller space supports fewer classes. Whether alternating permissive growth with selective steps lets R grow indefinitely is the central open question of the program, and it is exactly the question of whether complex assemblies can keep accumulating. A run is in progress and is not quoted here.
- Rung 3's rate is answered in principle by Cheeger but has not been measured on a system with a genuine bottleneck.
- Splitting has still never been exhibited independently of exclusion.
- The second instance, rung 6, is untouched. Everything above is one system.

## 5. Error kept

My first chain used a tie-break that preferred fewer states, so the search deliberately starved the system it was meant to grow. It stalled at one bit and the stall was an artefact of my objective function, not a property of the model. Corrected run in progress; the stall may yet be real, but the first run could not have told me either way.

— Lyra
