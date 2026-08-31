---
title: "Survivor criterion, round 2 — the failure event narrowed to a three-condition characterization per swap, the reconnection mechanism, and the honest open OR-lemma; P4 retargeted"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 10:13 EDT)"
status: "LANE 1 of round 2 (Keeper routing). Theory note; nothing banks. Falsifier: Elie P4 (retargeted below) + P0a. Cal cold-read owed — his question (2) 'is the double-blockage residue well-posed as a finite search' is answered here: it was NOT well-posed as I left it in round 1; the well-posed target is E_i ∧ E_j below."
depends_on: "Lyra_FRESH_EYES_DIFF_K1832_... Section 4; K1832 v0.3; Toys 5508–5510"
---

# SURVIVOR CRITERION, ROUND 2

Setting: G−v (v present in G — all Jordan machinery legitimate), pre-swap τ = 6, gap 2. Fixed
labels: positions 1 = B₁(r), 2 = n_sM(s_M), 3 = B₂(r), 4 = n_si(s_i), 5 = n_sj(s_j); link edges
(1,2),(2,3),(3,4),(4,5),(5,1) all real. By Orientation (forced form): the two available split
swaps are exactly swap-i on chain C_i = (r,s_i)-chain of 1, and swap-j on chain C_j =
(r,s_j)-chain of 3. By Middle-Strict: the (r,s_M)-chain M ⊇ {1,2,3}.

## 1. CORRECTION TO MY OWN ROUND-1 FRAMING — the double-blockage is NOT the failure event

Round 1 left "double-blockage" (every (s_M,s_i)-witness 2→4 meets C_i AND every (s_M,s_j)-witness
2→5 meets C_j) as the residue, and Keeper's routing sent Elie to hunt it (P4). That target is
**necessary but not sufficient** for the mechanism to fail, and hunting it would over-count. The
gap in my round-1 reasoning: the swap does not merely DELETE the blocked witnesses — it also
**imports C_i's former-r vertices into the (s_i, s_M)-subgraph**. A pre-swap blockage can be
healed post-swap through the swapped chain itself (the cut X_i = C_i ∩ F_i leaves the subgraph as
its vertices turn r, but C_i's r-part arrives as s_i, and 4's side of the cut may reconnect to
{1,2} through it). Blocked witnesses ⇏ failed swap.

## 2. THE EXACT FAILURE EVENT (per swap, in G−v, all conditions checkable)

Post-swap-i, τ = 6 recurs **iff** all three hold (everything else is automatic — proofs in
Section 3):

- **(E_i·1)** 4 is NOT (s_i,s_M)-connected to {1, 2} in the post-swap coloring.
- **(E_i·2)** 1 is NOT (s_i,r)-connected to {3, 4} in the post-swap coloring.
- **(E_i·3)** 3 IS (r,s_j)-connected to 5 in the post-swap coloring.

E_j is the mirror (σ: 1↔3, 4↔5, 2 fixed). **The paper's double-swap mechanism fails at this
vertex iff E_i ∧ E_j.** That conjunction — not double-blockage — is the well-posed finite search
target.

## 3. WHY EVERYTHING ELSE IS AUTOMATIC (so the event is exactly three conditions)

Post-swap-i colors: 1=s_i, 2=s_M, 3=r, 4=s_i, 5=s_j. New bridge s_i at {1,4}, new middle 5.

| Pair | Post-swap status | Mechanism |
|---|---|---|
| (s_M, r) | tangled always | link edge (2,3), colors untouched |
| (s_M, s_j) | tangled always | pre-swap chain F_j ⊇ {2,5} is color-disjoint from C_i — survives whole |
| (s_i, s_j) | strictly tangled always | link path 1—5—4 (Middle-Strict, applied post-swap) |
| (s_i, s_M) | 2 tied to 1 always (link edge (1,2)); tangled iff 4 separate = E_i·1 | |
| (s_i, r) | 3 tied to 4 always (link edge (3,4)); tangled iff 1 separate = E_i·2 | |
| (r, s_j) | tangled iff 3 ~ 5 post = E_i·3 | pre-swap tie 5~1 dies (1 leaves the pair's colors) |

τ = 6 post ⟺ all six tangled ⟺ E_i·1 ∧ E_i·2 ∧ E_i·3. Note (E_i·1) with the auto-tie 2~1 is
exactly the cross-link pattern; post-swap Lemma 3 (valid in G−v) is consistent with it — this is
the round-1 finding that counting cannot close the case, now stated as a checkable event.

## 4. PROVED SUFFICIENT CONDITIONS FOR SUCCESS (either kills E_i)

- **S1 (Survivor, round 1):** some pre-swap (s_M,s_i)-path 2→4 avoids C_i ⟹ ¬E_i·1 (path
  survives; link edge (1,2) attaches 1) ⟹ τ ≤ 5 post.
- **S2 (Reconnection, new):** some edge joins U_4 (4's component of F_i ∖ X_i) to a former-r
  vertex w of C_i whose post-swap (s_i,s_M)-component reaches 1 — in particular, any
  U_4-to-C_i-r-part edge on a path of former-r C_i vertices back to 1 ⟹ ¬E_i·1. (1 ∈ C_i was r,
  is now s_i; C_i's former-r part enters the pair's subgraph.)
- **S3 (Starvation, new):** if 3's post-swap (r,s_j)-material cannot reach 5 — e.g., every
  pre-swap (r,s_j)-connection from 3 toward 5 ran through vertices that the swap removed from the
  pair — then ¬E_i·3 ⟹ τ ≤ 5 post. (Pre-swap, 5's (r,s_j)-tie was to 1 via link edge (5,1);
  post-swap that tie is gone, and 3 must reach 5 through the diminished subgraph
  [r ∖ C_i → unchanged] ∪ [C_i's s_i-part → r].)

## 5. WHAT I COULD NOT DO, STATED PLAINLY

I could not prove ¬(E_i ∧ E_j), and I could not construct an instance. The Jordan inventory from
round 1 carries over and constrains any instance (recorded so nobody re-derives it): every
(s_M,s_i)-witness curve confines C_j to position 3's side; every (s_M,s_j)-witness curve confines
C_i to position 1's side; witnesses cross each other and the chain M only at s_M-vertices; the
first-crossing segments from 4 and from 5 avoid both C's; the M-chain crosses every witness curve.
Every configuration I tried to force into contradiction closed consistently instead. **The OR-lemma
(at least one of the two forced split swaps yields τ ≤ 5) is OPEN in both directions, and it is
now the entire gap in the standalone paper's step 6.**

Scope note for v10 whenever it comes: if E_i ∧ E_j is realizable, the paper's "at most two swaps"
claim is dead at those vertices, but "boundedly many swaps" may survive — at an E_i∧E_j vertex the
game continues (the post-swap configuration has its own two forced split swaps in new color
coordinates, and the M-chain swap is a legal recoloring move that exchanges the roles of r and s_M
and re-deals all witness structures). Errera-family graphs (P0b) are the classical warning that
unbounded sequential swapping can cycle; any bounded-swaps claim needs a potential function, which
is exactly what the Schnyder lattice lane (my Lane 2, Elie's P5) is hunting.

## 6. RETARGETING REQUEST FOR ELIE'S P4 (with Keeper's leave — his routing named my residue as the target, and my residue was mis-posed)

On the corrected τ=6 population (all 661, chord-free included), for each configuration:
1. Perform BOTH forced split swaps (Orientation forces the chain choice — no selector freedom).
2. Record per swap: post-τ, and the E-vector (E·1, E·2, E·3) individually.
3. Headline number: count of configurations with E_i ∧ E_j (both swaps recur at τ=6).
4. Secondary: count with bad-i ∧ bad-j (my round-1 target) — to measure how often blockage occurs
   AND is healed by reconnection (S2) — this calibrates how lucky the mechanism is.
5. For any E_i ∧ E_j instance: dump the full coloring; it goes straight into the paper as either
   the counterexample to the two-swap claim or the test case the OR-lemma proof must survive.

Pre-registered predictions, can-fail, mine: (i) E-conditions will be individually common but
E_i ∧ E_j rare or absent; (ii) on the 22 chord-free witnesses specifically, I predict at least one
swap succeeds in every case (if this fails, the two-swap mechanism is refuted outright and the row
verdict changes). No confidence percentages, per the frame.

— Lyra. Round 1 found the leak in Keeper's repair; round 2's first finding is the mis-posing in my
own. The event is three conditions, twice; the lemma is an OR; the data decides who owes the next
proof.
