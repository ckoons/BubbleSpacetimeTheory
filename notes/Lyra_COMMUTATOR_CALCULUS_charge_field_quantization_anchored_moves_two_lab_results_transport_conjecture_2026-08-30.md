---
title: "L2 — the commutator calculus and the charge field: anchored moves, two lab computations (support collapse and support explosion), charge quantization (odd vertices carry exactly ±3), the swap current, and the precise transport conjecture for X3"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 11:32 EDT at round start)"
status: "ROUND 4, LANE L2. Hand computations, case-complete where marked; conjectures pre-registered and can-fail; X3 is the falsifier. Nothing banks."
depends_on: "Straddle-Flip note (L3, round 3); L1 harvest note (same round — the charge field IS the local degree density of Mohar–Salas/Fisk)"
---

# THE COMMUTATOR CALCULUS AND THE CHARGE FIELD

## 1. THE CHARGE FIELD (definitions, then the quantization theorem)

For a proper 4-coloring of an oriented sphere triangulation: z_t ∈ {±1} the Heawood/orientation
sign per face; **charge c(w) := Σ_{t ∋ w} z_t ∈ ℤ** per vertex. Constraints:
- Heawood: c(w) ≡ 0 (mod 3) at every vertex (the closure condition — classical).
- Parity: c(w) ≡ deg(w) (mod 2) (sum of deg many ±1's).
- Bound: |c(w)| ≤ deg(w).

**Charge Quantization (mini-theorem, arithmetic of the three constraints):**
- deg 4: c = 0. Even quartic vertices are charge-NEUTRAL, always.
- deg 5 and deg 7: c = ±3 exactly. **Every generic odd vertex carries unit knot charge ±3 —
  the graph fixes the knot positions (odd vertices), the coloring chooses only the SIGNS.**
- deg 6: c ∈ {0, ±6} (neutral generically, excitable).
- Global: Σ_w c(w) = 3 Σ_t z_t = 12 · deg(f) — the charges are the local density of the
  Mohar–Salas/Fisk degree (L1 note).

Casey's "knots are the odd vertices" is now an equation: the odd vertices are exactly the sites
forced to carry nonzero quantized charge. And "annihilation" is impossible in the strong sense —
an odd vertex can never reach c = 0 (parity) — so the dynamical variables are the SIGNS: the
coloring's ± assignment on the fixed knot sites, constrained to sum to 12·deg.

**The swap current (from Straddle-Flip):** a swap on chain S changes charges only at vertices
incident to straddling faces: Δc(w) = −2·Σ_{t ∋ w, t ∈ straddle(S)} z_t. Charge moves ONLY along
the chain boundary — a local current on the dual cut cycles. A deg-5 knot flipping sign is a
transfer of 6 through the boundary that touches it.

## 2. ANCHORED MOVES (the formalization Cal's move-set gate needs)

A Kempe move is σ_{(p,q),a} = "swap the (p,q)-chain containing anchor a in the CURRENT coloring"
(identity if f(a) ∉ {p,q}). Moves are involutions; composites are well-defined words in these
generators. Commutator: [α, β] := αβαβ (each generator self-inverse). This indexing is required
because a chain is not a stable object — after another swap the "same" chain may have split,
merged, or absorbed new material. All conjectures below are about words in anchored moves.

## 3. TWO LAB RESULTS (hand-computed, case-complete on their stated hypotheses)

**Lab 1 — support COLLAPSE (the Rubik behavior exists).** Path a—u—b, f = (p, q, r), with
A = (p,q)-chain of a = {a,u}, B = (q,r)-chain of b = {u,b}, no external extensions. Then
[σ_{(p,q),a}, σ_{(q,r),b}] maps (p,q,r) ↦ (p,q,p): **net effect = recolor b alone; support {b} ⊊
A ∪ B.** Mechanism: the third move's chain absorbed b (through u) and the fourth move VANISHED
(anchor's color left the pair) — the commutator closes early. Note the net effect equals the
singleton swap σ_{(r,p),b}, which was directly available here; the commutator's value is the
mechanism, not this instance.

**Lab 2 — support EXPLOSION (the generic behavior).** Same shape but B∖{u} has components
B₁ ∋ b, B₂ both attached through u, and A∖{u} nonempty. Traced through four moves: the third
move's chain extends through u into B₂'s q-material; the fourth move's chain reconnects through
the restored u INTO A's q-vertices and toggles them q↔r — **support grows beyond A ∪ B into
material neither original chain touched.** Conclusion: commutators are NOT automatically local;
locality is a special geometric event.

**When does collapse happen (the law the labs suggest, pre-registered):** the commutator has
small support exactly when a late move vanishes or cancels — i.e., when an earlier move removes
the later anchor's color from its pair (vanishing), or when the re-formed chain coincides with
the original (cancellation). Conjecture C-support: **[α, β] has support strictly inside A ∪ B iff
the overlap A ∩ B is a cut of one of the chains whose removal isolates the far anchor's
component** — Lab 1 is the minimal case. X3 can test this as a boolean law over random overlap
geometries; a counterexample in either direction refines it.

## 4. THE TRANSPORT CONJECTURE (precise form for X3)

**T-transport (pre-registered, can fail).** Let w₁, w₂ be deg-5 vertices with charges +3, −3
connected by a path P in the dual boundary structure (a sequence of chains whose boundaries
chain from w₁'s star to w₂'s star). Then there is a word of anchored moves, with net degree
change 0, whose net charge effect is exactly: c(w₁): +3 → −3, c(w₂): −3 → +3, all other charges
unchanged — **a knot-pair sign exchange (dipole flip), with coloring support confined to a
neighborhood of P.** In particular the minimal macro-move is a DIPOLE operation: single-knot sign
flips with all else fixed are FORBIDDEN whenever they would change Σc = 12·deg by ±6 without
compensation — sign flips must pair or be paid for by an even-vertex excitation (deg-6 going
0 → ±6). That conservation argument is exact (Section 1); what is conjectural is realizability
by small-support words and the confinement to P.

**Why this is the Rubik claim:** the cube's commutators work because the group is large and the
support of [α,β] is the overlap region; our Lab 1 shows the analogous event exists in Kempe
dynamics; T-transport says the dipole flip — the physical move the rescue needs — is synthesizable
from such events. Fritsch at depth 2 with 6 knots vs Kittell at depth 4: the depth ladder should
re-read as the minimal dipole-word length the configuration's chain geometry admits — this is the
tightness reading of the round: tight = few boundary routes for the current to flow.

## 5. REQUESTS TO X3 (the laboratory protocol, falsifiers first)

1. Verify the charge quantization table numerically (free — one pass over any colored witness;
   any deg-5 vertex with c ∉ {±3} kills Section 1 and my sign conventions with it).
2. Verify the swap current formula Δc(w) against measured sign flips (same run as E4's
   straddle-set boolean).
3. Hunt C-support: random overlapping chain pairs, measure commutator support vs the cut
   criterion. Divergence is the finding.
4. Hunt T-transport on Fritsch: enumerate short anchored-move words; for each, log the charge
   delta vector. Pre-registered: dipole flips (±3 pair exchanges) appear at small word length;
   the rescue sequence's charge trace reads as a sequence of dipole moves that ferries frustrated
   signs together before the final free swap. If rescue traces show NO dipole structure, the
   transport frame is wrong and the potential must come from elsewhere — a clean kill.

## 6. GUARD

Nothing here proves descent. The charge field gives conservation laws (what CANNOT happen) and a
transport vocabulary (what must happen instead); the potential-function program (PLD, round 3)
still owes the monotone. The candidate now on the table, sharpened by this note: **potential =
minimal total dual-boundary transport cost to bring the charge assignment to one compatible with
a free link at v** — computable-looking on towers, and X3's traces are exactly the data to fit it
against. Fitting happens only after the definitions freeze (Cal's gate, L3 note).

— Lyra. The knots cannot be removed, only re-signed; re-signing is a current; currents need
channels; tightness is the scarcity of channels. That sentence is the conjecture — now it can
fail properly.
