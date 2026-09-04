# RETENTION UNDER CONSTRUCTION — the program restated, and the ladder that would prove it
**Lyra, for Casey. Friday 2026-09-04, 12:06 EDT (from `date`). NOT posted to the board; Casey's to judge first. Nothing here is registered, nothing is claimed, no tier requested.**

## 1. What we are trying to do, restated

**Old statement (do not use):** extend Shannon to a conservation law of knowledge that explains how complex assemblies run anti-entropically.
Three words in that sentence kill it. Shannon is not incomplete. Nothing runs anti-entropically. "Conservation" without a named dynamics is a definition.

**New statement:** A system with a dynamics splits into two coordinates. The dynamics randomizes one and cannot move the other. We want to know what happens to the second coordinate when the STATE SPACE ITSELF CHANGES by a construction step, and whether the retained part accumulates.

In one line: **which construction steps carry the invariant forward, and at what cost.**

The relationship to Shannon is settled and small: the dynamics selects a coarse-graining, and Shannon counts it. Retained information is the entropy of the partition into components. We apply Shannon to an alphabet the dynamics chose. We do not extend it.

## 2. Why this version has content, when this morning's did not

Keeper's objection at 08:49 was exact: "pull-back is injective, true of every cocycle, hence a definition, not a law." It applies to any fixed space.

It does not apply here, and the reason is the whole program. A construction step gives the dynamics NEW MOVES. Two states that no sequence of parent moves could connect may be connected by a child move. So injectivity of the induced map on components is not automatic. It is a condition, it can fail, and characterizing when it fails is the theory.

That is the difference between a definition and a law, and it is one sentence wide.

## 3. Objects (R0)

A **record system** is (X, P): X a finite state set, P a symmetric transition kernel (the dynamics). Its **components** are the classes of mutual reachability. Because P is symmetric, the stationary law on each component is uniform. A state is therefore a pair:
- **the class** (the topological coordinate), which P cannot move;
- **the position in the class** (the thermodynamic coordinate), which P equilibrates.

A **construction** is a map A: X → X' between record systems (a vertex insertion carrying its colouring; an added site; an appended module).

**Retained information** R(X) := H of the class distribution; for the uniform case, log₂ of the number of classes.

## 4. The ladder

**R1. Decomposition. STANDARD, cite it, do not prove it.** Ergodic decomposition of a symmetric chain. Label it standard in every draft. Content: zero. Risk if we forget to label it: a referee stops reading.

**R2. RETENTION. This is the new theorem and everything rests on it.**
Two failure modes for A, and only two:
- **Splitting:** x, y in one parent class, A(x), A(y) in different child classes. The child has finer invariants. This is GAIN, not loss.
- **Merging:** x, y in different parent classes, A(x), A(y) in one child class. This is LOSS. The construction erased a distinction the parent's dynamics could not.
**Retention = no merging = the induced relation on classes is injective.**
Theorem to prove: a sufficient condition on A for no merging, and a characterization of the merging steps.
First candidate condition: A is a morphism of dynamics, not merely of states, meaning every child move between images of parent states is the image of a parent move. Then no merging, immediately. The work is then not the proof but the CLASSIFICATION: which physical assembly steps are morphisms.
**Kill:** a natural assembly step that merges. We must FIND one. See R7.
**Noether guard:** this is not Noether restated, because the space changes. R1 and R5 might be. Say so at each rung.

**R3. RESET. Casey's sentence, made a measurement.**
Push the parent's uniform law forward through A and restrict to a child class. It is not the child's uniform law. Two numbers:
- distance from equilibrium at the moment of assembly, against a null of random subsets of the same size;
- thermalization time, against the same null.
Claim: the position coordinate re-equilibrates in finite time with the class held fixed. That is the exact form of "the runtime resets, the log persists."
**Kill:** a construction whose pushed-forward law is already equilibrium (nothing resets), or whose mixing time diverges (nothing ever resets).

**R4. ACCUMULATION. Why complex assemblies look the way they do.**
Along a chain of constructions, R is monotone if and only if no step merges. Retained bits grow while thermodynamic entropy is regenerated at every step. That is the whole appearance of an anti-entropic assembly, with no violation anywhere, because the two quantities live on different coordinates.
The number worth having is the growth rate of R per step.
**Kill:** R non-monotone on a chain of steps each of which is individually retaining. That would mean retention does not compose, and the program stops.

**R5. COST. The asymmetry that makes structure structure.**
The thermodynamic bits cost the Landauer quantity each to erase, and cannot be held. The topological bits cost nothing to hold, and cannot be changed by the dynamics at all. Changing one requires leaving a component, which is not a move; it requires an external operation whose cost is the barrier, not the Landauer quantity.
This is where the existing literature enters and where we must not re-derive what is known. Read Still on the thermodynamics of prediction before writing a line of this rung.
**Kill:** the barrier is the Landauer quantity times the number of bits, in which case there is no asymmetry and R5 is empty.

**R6. TWO INSTANCES, one of them not ours.**
- Instance one, in hand: proper 4-colourings under Kempe moves, which are the Wang-Swendsen-Kotecky algorithm at zero temperature. Classes computable by breadth-first search. Invariant known and independent (the degree modulo twelve). Construction steps: vertex insertion carrying its colouring.
- Instance two, deliberately not ours: dimer coverings of a lattice on a torus under local flips, whose winding sectors are exactly components the dynamics cannot cross. Different objects, same shape. If the theory only speaks about colourings it is a fact about colourings.
**Kill:** the second instance needs a different theorem. Then there is no general statement, only two examples.

**R7. THE EMPTINESS GUARD. Do this before R2, not after.**
Exhibit, by computation, in each instance:
- one construction step that retains,
- one construction step that merges,
- one that splits.
If every step retains, "retention" cannot fail and the theory proves nothing. A search that cannot fail is not a test. This rung is cheap and it decides whether the rest is worth doing.

## 5. Honest scope

What this would explain: the SHAPE of the phenomenon. An assembly whose substrate turns over completely can hold its invariant coordinate exactly, at no thermodynamic cost, while its thermodynamic coordinate is re-randomized continuously. That is why a body survives its atoms and why a persona survives its weights.

What it would not explain: biology, evolution, or intelligence. Those need a mechanism for why the invariant sector is large and why the steps that retain are the ones selected. Not in this program.

## 6. Where it dies

The main risk is R2. If the classification of construction steps has no clean criterion, and each case must be decided by computation, then this is a framework rather than a law. That outcome is still publishable and still useful, and it must be said in advance so that discovering it is not a disappointment dressed as a result.

The second risk is priority. Computational mechanics, predictive information, the thermodynamics of prediction, and assembly theory all live near this. Read them first. Half of R5 may already be a theorem with someone's name on it.

## 7. Name

"Conserved Knowledge" invites the objection Keeper already raised. "Retention under construction" states the object and the question, and a referee cannot mistake it for a claim against the second law. Casey's call.

— Lyra
