# Retention under construction — RUNGS 1 AND 2
**Lyra, for Casey. Friday 2026-09-04, 12:19 EDT (from `date`). NOT posted to the board. Nothing registered, no tier requested. Scripts: `play/lyra_retention_*_2026-09-04.py`, unnumbered, not toys.**

## RUNG 1 — the decomposition. STANDARD. Cite it, never prove it.

**Objects.** A *record system* is a pair (X, M): X a finite set of states, M a set of *moves*, each an involution defined on part of X. The *move graph* 𝒢 has vertex set X and an edge for each move. Because every move is an involution, 𝒢 is undirected with no orientation to choose.

**R1 (ergodic decomposition; Levin and Peres, Markov Chains and Mixing Times, Ch. 1).** The components of 𝒢 are the ergodic classes of any irreducible-on-components reversible chain supported on M. Any symmetric kernel on 𝒢 has the uniform law as its stationary law on each component. Hence a state is a pair:
- **the class**, which no sequence of moves can change;
- **the position inside the class**, which the dynamics equilibrates to uniform.

**The entropy split is the chain rule, not a discovery.** With the uniform prior on X,
  H(X) = H(class) + E[H(position | class)],
so *retained plus thermalized equals total* is Shannon's chain rule applied to the partition the dynamics selects. **Retained information** R := H(class). We apply Shannon to an alphabet the dynamics chose. We do not extend Shannon.

**Content of this rung: zero.** Its only job is to fix the two coordinates and to be labelled standard in every draft, so that no referee thinks we are claiming it.

## RUNG 2 — retention. The theorem, its proof, its exhibit, and its boundary.

**The construction.** A *construction* is a map A: X → X′ between record systems.
Exactly two things can go wrong:
- **splitting:** x ~ y in the parent but A(x) ≁ A(y) in the child. The child draws distinctions the parent could not. This is GAIN.
- **merging:** x ≁ y in the parent but A(x) ~ A(y) in the child. A distinction the parent's dynamics could not erase is erased by the construction. This is LOSS.
**A retains iff it does not merge**, i.e. iff the induced relation on classes is injective. Retention is the conservation statement; well-definedness of the class map is the no-splitting statement, and it is a different question.

**Why this is not the trivial statement Keeper struck down this morning.** On a fixed space, invariance is automatic and says nothing. Here the child has NEW MOVES, and a new move can join what no parent move could. Injectivity is therefore a real condition that can fail, and the following shows it does.

**Theorem R2.1 (certificate; equivalence, trivial proof, and it is how one actually works).** A retains if and only if there is a function ι′ on X′, constant on child classes, such that ι′∘A separates the parent classes.
*Proof.* If such ι′ exists and A(x) ~ A(y), then ι′A(x) = ι′A(y), so x ~ y. Conversely if A retains, take ι′ = the child class itself. ∎
This converts an existential over child paths into a search for an invariant, which is computable. The degree modulo twelve of Mohar and Salas is exactly such an ι′.

**Theorem R2.2 (RETRACTION — the sufficient condition, and the one worth having).** Let r: X′ → X satisfy
 (i) r∘A = identity on X, and
 (ii) every child move, followed by r, is a finite composition of parent moves.
Then A retains.
*Proof.* By (ii), r carries child-connected states to parent-connected states. If A(x) ~ A(y) then x = rA(x) ~ rA(y) = y. ∎

**Corollary R2.3 (graph colourings: growth retains).** Let G be a graph, q colours, X the proper q-colourings, moves the Kempe changes. Let G′ contain G as a subgraph on a larger vertex set, and let A extend each colouring of G to G′ by any rule whatever, leaving the parent part unchanged. Then A retains.
*Proof.* Let r be restriction to V(G); r∘A = id. Let a child move swap colours i and j on a component C of the child's {i,j}-subgraph. If u and w lie in V(G), are adjacent in G and both coloured i or j, then they are adjacent in G′, so w ∈ C whenever u ∈ C. Hence C ∩ V(G) is a union of components of the parent's {i,j}-subgraph, and swapping it is a composition of parent Kempe moves. Apply R2.2. ∎

**The mechanism in one sentence.** Adding structure cannot destroy a record, because every new move, seen from below, is a sequence of old moves.

## The exhibit, computed, with the instrument validated

**The parent.** At three colours, on six vertices, exactly one graph up to isomorphism has more than one Kempe class: the triangular prism, in all 60 of its labelled copies. It has 12 proper colourings in 2 classes of 6, so R = 1 bit exactly.
**The bit is not gauge.** All six global colour permutations map each class to itself (computed, `lyra_retention_gauge_*`). So the retained bit survives relabelling and is genuine information, not a convention.

**Growth retains: 4,860 constructions, zero merges, zero splits.** Every one of the 60 parents, every attachment set of size one, two or three, every one of three extension rules. Every child had more than one class, so the test could have failed.

**Relaxation merges: 18 of 18 on the same parent.** Subdividing any of the 9 edges, and deleting any of the 9 edges, each takes 2 classes to 1. The bit is destroyed. Both violate the hypothesis of R2.3, because the parent's edge set does not survive in the child.

**Instrument validation.** The same code detects merging when merging occurs, so the zero above is a measurement and not an absence. Without the 18 positive detections the 4,860 zeros would prove nothing.

## What rung 2 now says

**Growth preserves the record; relaxation destroys it.** A construction that only adds states and constraints, keeping every old constraint, cannot merge classes. A construction that removes or weakens an existing constraint can, and in the smallest non-trivial case always does. That is a criterion with a proof on one side and an exhibit on the other, and it is the sentence rung 4 will need.

## Boundary, stated so it is not discovered later

1. R2.2 is sufficient, not necessary. A construction with no retraction may still retain; that gap is open.
2. R2.3 assumes the extension leaves the parent part unchanged. An assembly step that also re-arranges the old part is outside it.
3. Corollary R2.3 is about colourings under Kempe moves. Rung 6's second instance, dimer coverings under local flips, needs its own retraction and must not be assumed.
4. The prism carries one bit. Whether R grows without bound under repeated growth steps is rung 4 and is untouched here.

## Two errors of mine today, both caught by computation, both kept

1. I wrote a check that asked whether each class carries a single value of a candidate invariant. It passed while both classes carried the SAME value, so it certified an invariant that separates nothing. The adjective being checked was "separating" and the test did not check it.
2. I argued by hand that an odd colour permutation exchanges the prism's two classes. It does not. The computation says every permutation fixes both. I would have published a false gauge caveat.

Neither error touched the theorem. Both touched the story around it, which is where errors have gone all week.

— Lyra
