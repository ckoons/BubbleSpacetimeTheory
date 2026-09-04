# Retention under construction — RUNG 3: what "reset" actually is
**Lyra, for Casey. Friday 2026-09-04, 12:25 EDT (from `date`). NOT posted to the board. Nothing registered. Script: `play/lyra_retention_rung3_2026-09-04.py`, unnumbered.**

## The corrected sentence

Casey's premise was "thermodynamics resets after a new assembly." That is not what happens, and the true statement is sharper.

**An assembly step does not randomize the old part. It MOVES the old part's equilibrium, by a factor equal to the number of ways the new part can attach, and the old part then relaxes to the new equilibrium.** Where the attachment count is the same for every old configuration, the equilibrium does not move at all, the old part is born already at equilibrium, and every bit of novelty sits in the degrees of freedom the assembly added.

Both halves are theorems, both were stated before the computation, and both were confirmed.

## Setting

Parent record system X with uniform equilibrium on a class K. A construction A: X → X′ with a restriction r satisfying r∘A = identity (rung 2's retraction, so the class is retained). For a parent state x let **f(x)** be its **attachment multiplicity**, the number of child states in the class that restrict to x. Write m = |K| and M = Σ f(x).

The **inherited law** is A pushing the parent's equilibrium forward: uniform on the m image states.

## R3.1 (constant multiplicity: the old part is born at equilibrium)

If f is constant on K, the inherited law and the child equilibrium have exactly the same marginal on the old coordinates. All of the distance from equilibrium lies in the conditional law of the new coordinates.
*Proof.* The child equilibrium's marginal at x is f(x)/M, which is 1/m when f is constant. The inherited marginal is 1/m by definition. ∎

**Measured, marginal distance from equilibrium:**

| construction | attachment counts | marginal distance |
|---|---|---|
| four-cycle, attach to one vertex | all 2 | 0.0000 |
| six-cycle, attach to one vertex | all 2 | 0.0000 |

## R3.2 (variable multiplicity: assembly exerts an entropic bias on what was already there)

If f varies on K, the child equilibrium re-weights the old structure in proportion to f. The inherited law is off equilibrium in the OLD coordinates by exactly
  distance = ½ Σ_x | 1/m − f(x)/M |,
the normalized mean absolute deviation of the attachment multiplicity. The old structure must then relax, and it relaxes toward configurations that admit MORE attachments.

**Measured:**

| construction | attachment counts | marginal distance |
|---|---|---|
| four-cycle, attach to two opposite vertices | 1 and 2 | 0.1333 |
| six-cycle, attach to two vertices at distance two | 1 and 2 | 0.1604 |
| six-cycle at four colours, attach to two opposite vertices | 2 and 3 | 0.0719 |

This is the ordinary entropic weight of statistical mechanics, and that is the point: it is not new physics, it is the correct identification of what an assembly step does to the record. Self-assembly selects pre-existing configurations by their attachment multiplicity, and the selection is quantitative.

## What rung 3 does NOT establish

**The rate is untested.** Every system above equilibrates in one or two steps, and so does the random-subset null, so no separation between a structured start and a random one could have been seen. The question "does an inherited state thermalize more slowly than a random one" is open and needs a parent with a bottleneck, meaning a class with a small conductance. That is the next computation and it should not be skipped, because the whole intuition behind "cold start" lives in the rate, not in the distance.

**Two coordinates, two behaviours, both now precise:**
- the class, which the dynamics cannot move and which rung 2 showed survives growth and dies under relaxation;
- the position, which the dynamics equilibrates, and whose target the assembly step itself shifts by the attachment multiplicity.

That is the decomposition the program needs, and neither half required extending Shannon.

— Lyra
