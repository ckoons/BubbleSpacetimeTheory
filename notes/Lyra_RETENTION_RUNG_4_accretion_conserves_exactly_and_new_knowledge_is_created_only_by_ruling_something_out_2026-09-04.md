# Retention under construction — RUNG 4: accumulation, and why accretion cannot do it
**Lyra, for Casey. Friday 2026-09-04, 13:02 EDT (from `date`). NOT posted to the board. Nothing registered. Script: `play/lyra_retention_rung4_2026-09-04.py`, unnumbered.**

## 0. My own rung-4 statement was wrong, and the correction is the result

The ladder said "retained bits are monotone along a chain if and only if no step merges." That is false. Merging is necessary but not sufficient for a drop, because a child can lose old classes and gain new ones in the same step. Worse, monotonicity was the wrong question. The right one is **accumulation: can a construction step CREATE retained information?** In rung 2 every one of 4,860 retaining constructions left the class count unchanged. Growth preserved the bit and never added one. That is what needed explaining.

## 1. The theorem

**Theorem (accretion).** Let G′ = G + v, where v is one new vertex with any neighbourhood N(v). Let X_ext be the set of proper colourings of G that extend over v. Then the Kempe classes of G′ correspond bijectively to the **connected components of the parent's move graph restricted to X_ext**.

*Proof.* (i) Two child colourings agreeing on V(G) are connected: if v carries colour j in one and t in the other, both j and t avoid every colour on N(v), so no neighbour of v is coloured j or t, the {j,t}-component containing v is {v} alone, and one swap moves v from j to t leaving everything else fixed. (ii) A parent move between two states of X_ext lifts: swap the child component containing the parent component, then correct v by (i). (iii) A child move restricts to a composition of parent moves, by the retraction argument of rung 2. ∎

**Corollary 4.1 (total steps conserve exactly).** If every parent colouring extends, then X_ext = X, the class map is a **bijection**, and the retained information is neither increased nor decreased. **Accretion that accepts every prior configuration cannot create knowledge, ever, for any attachment set and any extension rule.**

**Corollary 4.2 (creation requires exclusion).** The class count rises exactly when deleting the inextensible states disconnects a parent class. New retained information is created only by a step that **rules something out**.

## 2. The exhibit: nothing becomes one bit

Parent: the prism with one vertex removed. 18 colourings, **1 Kempe class, 0 bits retained**.
The returning vertex attaches to three vertices and **forbids 6 of the 18** parent colourings.
Child: the prism. 12 colourings, **2 Kempe classes, 1 bit retained**.
Components of the parent's move graph restricted to the 12 surviving states: **2**. The theorem's prediction, confirmed.

A bit was created. It was created by exclusion, and by nothing else.

## 2b. Corollary 4.1 checked exhaustively (the search was running before the proof existed)

Every parent on five and six vertices, every total single-vertex attachment, three and four colours:

| parents | total attachments tested | class count rose |
|---|---|---|
| 667 (five vertices, three colours) | 12,020 | 0 |
| 21,886 (six vertices, three colours) | 639,302 | 0 |
| 727 (five vertices, four colours) | 18,490 | 0 |

669,812 total constructions, not one creation. The corollary says the outcome was impossible, so this is a check on the proof rather than evidence for the claim, and it is reported as such.

## 3. What this says for the program

**A write is a refusal.** An assembly step that can accommodate every prior configuration leaves no record of anything. A step that rejects some prior configurations can cut a class in two, and the resulting bit is then permanent under the dynamics and, by rung 2, survives all further growth. Shannon's own definition of information as the reduction of possibility arrives here as a theorem about ergodic classes rather than as a definition.

This also corrects the intuitive picture the program started with. Complex assemblies do not accumulate retained structure by accretion. They accumulate it by **selective** accretion, and the amount created at a step is bounded by how much the exclusion fragments what was previously reachable.

## 4. Scope and what is owed

- The theorem is proved for **one added vertex in a graph-colouring system**. It is a concrete instance, not the general framework. The general statement, in terms of a retraction and a set of admissible states, is the obvious guess and is not proved here.
- Rung 3's **rate is still owed**: every system enumerated so far mixes in one or two steps, so no structured start has yet been shown to thermalize more slowly than a random one.
- **Splitting has still never been exhibited** as a separate phenomenon. In the accretion theorem it appears only through exclusion, and whether it can occur with a total step is open.
- A chain of steps has not been run. The growth rate of retained bits per step, which is the quantity rung 4 was supposed to deliver, needs the chain and a family with room to grow.

## 5. Error kept

I designed two searches for class creation that required the construction to be total. By Corollary 4.1 such a search cannot succeed. Both returned zero, and the zero meant nothing. Same failure as this morning's: the instrument was built so that the interesting outcome was impossible. The proof is what caught it, not the data.

— Lyra
