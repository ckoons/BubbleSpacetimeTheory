---
title: "E1 (+E4a) — the Hand-off Theorem written clean: parity lemma, Constraint Persistence (Cal's pressure point as a lemma, not a remark), the honest scope line (it removes a mechanism, it does not yet grant a move) — plus progress on the evenness debt: the Singleton Neutrality Lemma and the mod-4 reduction"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 19:13 EDT at round start)"
status: "ROUND 14, LANES E1 and E4a. The theorem is written for Cal's hardest read — he is right that everyone wants it true, which is exactly why its scope line is carved into the statement itself. Evenness: debt reduced, not paid; the reduction and one new lemma proved. Nothing banks."
---

# THE HAND-OFF THEOREM

## 0. Setup (definitions pinned)

A *constrained coloring problem* is a pair (H, P): a triangulated surface-piece H and a set
P ⊆ V(H) of PINNED vertices with fixed colors. Legal moves are Kempe swaps whose chains avoid P.
The *insertion problem* at a deg-5 vertex v of a sphere triangulation G is (G−v, ∅): the hole's
link ring is topological boundary, but NO vertex is pinned. For two colorings f, f′ of one
problem, the wall system 𝒲(f, f′) is as in wall theory (difference field, domains, walls). A
wall component is *anchored* if it is a path whose two endpoints both lie at pinned boundary.

## 1. Lemma 1 (Interface parity — walls end only at topological boundary)

At any vertex u whose link is a full cycle, the domain interfaces around the link occur in even
number, so no wall terminates at u; wall components are closed curves or paths ending at
vertices whose links are paths — i.e., at topological boundary. *Proof:* walk u's link cycle;
each crossing of a domain interface toggles the current domain; returning to the start forces an
even toggle count. A terminating wall would contribute odd. ∎ (This is H1's argument, restated
as the theorem's first leg.)

## 2. Lemma 2 (Constraint Persistence — Cal's pressure point, discharged)

P is a datum of the PROBLEM, not of the state: legal moves transform colorings and leave (H, P)
fixed; no walk step creates, moves, or removes a pinned vertex. Hence any property defined
solely by (H, P) — in particular P = ∅ — holds at EVERY configuration reachable during any
descent, not merely the initial one. *Proof:* immediate from the definition of the move set;
recorded as a lemma because the assembled proof leans on it at every step and an unstated
load-bearing triviality is how proofs rot. ∎

## 3. THE THEOREM

**Hand-off Theorem.** In the insertion problem (G−v, ∅): no anchored wall exists between ANY two
colorings, at ANY step of any rescue walk. Consequently the freeze mechanism exhibited by the
disc twins — mutual unreachability enforced by boundary-anchored walls whose dissolution chains
would cross a pinning — is STRUCTURALLY UNAVAILABLE at the insertion site, permanently along the
descent.

*Proof.* By Lemma 1, wall components are closed or end at topological boundary. Anchoring
additionally requires the endpoints to be PINNED (dissolution obstruction = chains forced
through P). By Lemma 2, P = ∅ at every reachable configuration. No anchored wall exists. ∎

## 4. THE HONEST SCOPE LINE (carved into the statement, not appended)

The theorem REMOVES A MECHANISM; it does not yet GRANT A MOVE. What is proved: the only
obstruction mechanism ever exhibited in this program (Z1's twins; the only relative
unreachability we have witnessed anywhere) cannot operate at the insertion site. What is NOT
proved: that wall-freeness implies mobility — that is Gate Existence, still open, now retargeted
by GS's death at the support-3/charge-quantum structure (E3 note). A reader who takes this
theorem as "insertion is always rescuable" has been failed by the author; the correct sentence
is: **the room where the induction lives has been searched, and the one monster we have ever
photographed provably cannot enter it.** Whether other monsters exist is exactly the remaining
program.

(For Cal's read: the attack surface, pre-named honestly — (a) Lemma 1 assumes the difference
field's domain structure is well-defined for arbitrary pairs, which holds by construction but
should be checked against a pair with EMPTY fixed locus; (b) "anchoring requires pinning" is a
mechanism claim imported from the twins — its converse direction, that boundary-terminated
UNPINNED walls are always dissolvable, is NOT claimed anywhere in this note and must not be
silently assumed downstream; (c) the theorem's force depends on the freeze mechanism's
UNIQUENESS being empirical, which is scope, not proof.)

# E4a — THE EVENNESS DEBT: reduced, not paid

The quantum derivation's second factor (achieved Δdeg ∈ 2ℤ on closed spheres) owes a general
proof. Progress tonight:

**Singleton Neutrality Lemma (proved, new).** Singleton clusters exist only at charge-neutral
vertices, and their swaps carry zero degree current. *Proof:* a singleton (x,y)-cluster at u
requires u's link properly 2-colored — an alternating cycle — which forces the incident face
signs to alternate: c(u) = 0; the straddle sum is c(u) = 0, so Δdeg = 0. ∎ (This also re-derives
the 288-case "degenerate corner" of the gate census from first principles: singleton gates are
exactly the charge-neutral rearrangements.)

**The mod-4 reduction (proved).** Δdeg even ⟺ Σ_straddle z ≡ 0 (mod 4). With |straddle| even
(proved), this becomes a statement about the sign balance around chain-boundary dual cycles.
Status: verified for singletons (above) and empirically at scale (every mobile closed r is
even in degree units); the general dual-cycle sign-balance argument is the REMAINING DEBT,
stated as such. The debt is now one combinatorial statement wide, not a mystery factor.

— Lyra. The theorem everyone wants true is written with its wants amputated: one mechanism
removed, one move still owed, and the attack surface handed to the critic with the ink still
wet. That is the only way a strategic result deserves to enter the registry.
