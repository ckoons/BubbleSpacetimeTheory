---
title: "The bridge-term, first payment from the stage algebra — the EXCISION-AVOIDANCE LEMMA (proved: the excision never touches the bridge zone; forcing = properness alone) and the ACCRETION CHARACTERIZATION (bridge-zone net content = the s_i–s_M alternation sites of the bridge links' arcs — exact, with the 185-class as its third-site case) — and the honest finding: the CONSTANT is not yet derived; the missing constraint is named"
author: "Lyra"
date: "2026-09-01, Tuesday (clock-verified 11:37 EDT)"
status: "UNGATED derivation under the full innocence burden (Cal §812: quarantine impossible — every step states its forcing; no census number is cited as a reason anywhere below; the measured ≤2/3 appears ONLY in the honest-finding section as the fact my derivation does not yet explain). Gate-Phase Stability untouched this turn, per the order — it waits for Elie's existence-and-truth census. Nothing banks."
---

# THE BRIDGE-TERM — FIRST PAYMENT

Setting: the no-far branch (zero-support pin); bridge zone 𝐁 = (N(B₁) ∪ N(B₂)) ∖ ({v} ∪ link);
the four-stage algebra; all forcings from the standing lemmas (Confinement, Forced-Excision,
Middle-Strict, Orientation) plus properness of c₀.

## 1. THE EXCISION-AVOIDANCE LEMMA (proved)

**Lemma EA. The excision E = X₁ ∩ X₂ contains NO bridge-zone vertex: E ∩ 𝐁 = ∅ — beyond the
near copy itself (a link vertex), the excision cannot enter the bridge collar at all.**
*Proof.* E ⊆ ρ(X₁) = the old-r vertices of X₁ (Confinement). A bridge-zone vertex is adjacent
to B₁ or B₂, whose c₀-colors are r; by properness of c₀, no neighbor of an r-vertex is r. So
no bridge-zone vertex is old-r, hence none is in E. ∎ (Forcing: properness alone — the
strongest kind; no toy, no census, no case analysis.)

Corollary: every excised vertex beyond B₂/B₁ lies OUTSIDE the bridge collar — deep excisions
are far-zone events, which is exactly why the exhibits' big excisions ride the stranding
branch and why the no-far branch's excision is just the near copy.

## 2. THE ACCRETION CHARACTERIZATION (derived, exact)

What CAN be net-changed in 𝐁? Working the stages for u ∈ N(B₂) (mirror for B₁), with u's
c₀-color ∈ {s_M, s_i, s_j} (never r, by Lemma EA's forcing):
- **u old-s_M:** then u ∈ M (the edge u–B₂ is (s_M, r); chain maximality). In the no-far
  branch u stays connected to the anchor's component after the excision (no stranding), so
  X₃ recovers it: toggled twice on the M-side, net-unchanged. [Forcing: the branch definition
  + Confinement (X₂ cannot touch u while it is r-colored in c₁).]
- **u old-s_j:** invisible to both acting pairs at every stage (s_j ∉ {r,s_M} ∪ {s_M,s_i} at
  the stages where it could enter). Net-unchanged. [Forcing: color bookkeeping.]
- **u old-s_i:** the edge (u, B₂) is (s_i, s_M) in c₁, so **every old-s_i neighbor of B₂ is
  in X₂** (Forced-Excision puts B₂ ∈ X₂; adjacency does the rest). Flipped to s_M at stage 2.
  At stage 3, u is ACCRETED into X₃ iff u is adjacent to surviving (r, s_M)-material of c₂ —
  and every old-s_M neighbor of B₂ is such material (it is M-material, r-colored in c₂,
  anchor-connected in the no-far branch). Accreted ⟹ flipped to r at stage 3, invisible at
  stage 4: **net s_i → r, CHANGED.** Not accreted ⟹ stage 4 can return it (s_i-world), or it
  stays s_M — the X₂△X₄ bookkeeping, settled by whether X₄ reaches it through the re-formed
  chain (it does, through B₂'s own re-entry, unless stage-3 material cut the route — the
  SJ-adjacent case).

**Characterization: the bridge-zone net content consists exactly of the ACCRETED old-s_i
neighbors of the near copies — and u is accretable iff u sits next to an old-s_M vertex in
the bridge link's arc: the net sites are the s_i–s_M ALTERNATION SITES of B₂'s (and B₁'s)
link arcs.** The 185-class is this characterization's third-site case (one extra alternation
site) — its "distinct mechanism" is no longer distinct: it is the same mechanism at count
three.

## 3. THE HONEST FINDING — the constant is NOT yet derived; the missing constraint, named

The alternation-site count is bounded by the arc's color pattern, and NOTHING derived above
bounds that pattern: a high-degree near copy with an alternating s_M/s_i arc would accrete
~deg/2 sites. The measurements say small counts dominate at stuck configurations — a fact my
derivation does not yet explain, and which I decline to launder into a constant. **The
missing constraint, named precisely: what does STUCKNESS force about the bridge links' arc
colorings?** Two attack routes, in order: (i) the arc from n_sM to n_si around B₂, when it
alternates s_M/s_i, IS an (s_M,s_i)-path connecting the two singleton positions — it lives in
the c₀-chain F_i, and the forced partitions constrain F_i's structure at the link; the
alternation count may be paying for something τ = 6 cannot afford (a Middle-Strict-style
argument on B₂'s link cycle — the same move that proved Singleton Neutrality); (ii) failing
that, the count enters the constant as a per-configuration quantity (the near constant
becomes 5 + 2a where a = the alternation count, honest and configuration-dependent) and the
claim's shape adjusts rather than pretends. Route (i) is the next session of this derivation;
the label stays on until one of them pays.

## 4. Standing

Proved: Lemma EA (properness-forced — the excision cannot touch the collar). Derived: the
exact accretion characterization (net bridge content = alternation sites; the 185-class
unified, not special). Named: the missing stuckness-constraint on arc colorings, with two
routes ordered. The rim derivation is on Cal's desk as of this hour (it converts clause (b)
to derivation — load-bearing, read-worthy now, per the routing); Gate-Phase Stability holds
for Elie's census, per the order that holds even at the summit.

— Lyra. The collar was never touchable by the excision — properness said so all along — and
the 185 "exceptional" traces were the rule at count three. What remains is one question posed
to stuckness itself: what do you forbid on a bridge's own doorstep? The program has learned
that τ = 6 always answers that kind of question. Asking it properly is next.
