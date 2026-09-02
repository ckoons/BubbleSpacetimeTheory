---
title: "THE DICHOTOMY TREE for W_i, derived to its leaves — the image c₄ on the hard branch is STUCK iff two singleton–middle chain questions (Q3, Q4) both hold; Q1 is forced by Δ′-NO, Q2 follows from Q3 by Jordan; Q3 means the fourth chain TUNNELS THROUGH the wall the third chain built. K1838 2(b) concurred with one leaf-labeling caveat (prefix-gate ≠ word-gate). The mirror word at an S leaf = the same tree with i↔j. A potential PRE-REGISTERED before contact, labeled as a guess. KITTELL'S EIGHT SWITCHES (1935) ARE EXACTLY OUR FIFTEEN MOVES MODULO CHAIN IDENTITY — the alphabet is the field's; the commutator shape is ours. Frame carried at every node; 5-connectivity available and unused."
author: "Lyra"
date: "2026-09-02, Wednesday (clock-verified 09:15 EDT)"
status: "Derivation (Sections 1–4) with every chain question stated as a coincidence question the instruments can score; one concurrence with a caveat on K1838 2(b) (Section 2); one pre-registration filed before any leaf count reaches me (Section 5); one literature identification from the source PDF (Section 6). Nothing banks; Cal's read and K1835-B owed."
---

# 0. Frame, carried explicitly

Every chain below lives in T−v with T's embedding present (K1834 S4): v is uncolored, not deleted, so
every Jordan argument closes through v's location and the link is v's link cycle in T (Whitney, S3).
No H-frame, no contraction. **The frame ruling (K1838 Section 3, Cal §818): domain = 5-connected sphere
triangulations, Casey to confirm or veto.** Nothing in this artifact USES 5-connectivity — every step is
an all-T step — so the tree is frame-robust; where 5-connectivity could be used (no separating 3- or
4-cycles bounds the short walls) I say so and leave it unused. Notation as in the DGT artifact: link
positions 0..4 = B₁(r), n_sM(s_M), B₂(r), n_si(s_i), n_sj(s_j); W_i = (B₂,(r,s_i))·(B₁,(r,s_j)) as the
4-stage commutator; X_k = the chain swapped at stage k; c_k = the coloring after stage k.

# 1. The tree to depth one — every node a chain-coincidence question

```
c₀ stuck (canonical)
 ├─ stage 1: X₁ = B₂'s (r,s_i)-chain ∋ n_si, ∌ B₁            [forced]   c₁ = (r,s_M,s_i,r,s_j)
 ├─ stage 2: X₂ = B₁'s (r,s_j)-chain ∋ n_sj, n_si              [forced]   c₂ = (s_j,s_M,s_i,s_j,r)  saturated
 └─ stage 3: X₃ = B₂'s (r,s_i)-chain in c₂.   Δ: n_sj ∈ X₃ ?
     ├─ Δ-NO  → c₃ = (s_j,s_M,r,s_j,r): s_i ABSENT  [I at the prefix]
     │          stage 4: X₄ ⊇ {B₁,n_sj,n_si,B₂} [forced] → c₄ = (r,s_M,s_j,r,s_j): s_i ABSENT   ★ LEAF I
     └─ Δ-YES → c₃ = (s_j,s_M,r,s_j,s_i) saturated; wall W := P ∪ v (K1838 2a)
                stage 4: X₄ = B₁'s (r,s_j)-chain in c₃.   Δ′: {B₂,n_si} ⊆ X₄ ?
                 ├─ Δ′-YES → τ(c₃) ≤ 5 [K1838 2b, concurred, Section 2]   ★ LEAF G at the PREFIX c₃
                 │            c₄ = (r,s_M,s_j,r,s_i): word-image status decided by its own Q-table (Section 3, mirror)
                 └─ Δ′-NO  → c₄ = (r,s_M,r,s_j,s_i): canonical word with i↔j.   Stuck iff Q3 ∧ Q4 (Section 3)
                              ├─ ¬Q3 or ¬Q4 → τ(c₄) ≤ 5                        ★ LEAF G at the WORD IMAGE
                              └─ Q3 ∧ Q4   → c₄ stuck-canonical                 ★ LEAF S → the mirror tree (Section 4)
```

# 2. K1838 Section 2(b) — CONCURRED, with the leaf-labeling caveat that Cal's read should carry

Keeper's step: in c₃'s own canonical frame the copies are B₁ and n_si (color s_j, positions 0 and 3,
gap 2 through position 4), the middle is n_sj (s_i), the singletons n_sM (s_M, adjacent to copy B₁) and
B₂ (r, adjacent to copy n_si). Δ′-YES puts B₁, n_si, B₂ in ONE (s_j, r)-chain of c₃: the non-middle
bridge pair (s_j, r) is STRICTLY tangled. Lemma 3 (K1832-verified; gap 2 holds in c₃) says at τ = 6 only
the middle pair can be strict; so τ(c₃) ≠ 6, and c₃ is saturated, so τ(c₃) ≤ 5. **Concur.** The frame
carry is legitimate: Lemma 3 and One-Context quantify over every proper coloring of T−v with T's
embedding present; c₃ is one. Inputs: Lemma 3 only (the (ii)-contrapositive is Lemma 3 wearing
One-Context's coordinates).

**Caveat (leaf labeling).** What 2(b) certifies is the gate phase at the THREE-STAGE PREFIX c₃, i.e. a
legal Kempe sequence of three swaps from Kittell's alphabet, plus one freeing swap. That is a fine
leaf for "Kempe's method with this alphabet inserts v" and for 4CT-via-Kempe-sequences. It is NOT a
certificate for OWL(1) as frozen (Cal §818 §4: the object is the four-stage image c₄), because
τ(c₃) ≤ 5 says nothing about τ(c₄) = τ(c₃ with X₄ swapped). On Δ′-YES, c₄ = (r, s_M, s_j, r, s_i) has its
own Q-table (the Section 3 table with the roles: copies B₁ (0), n_si (3); middle n_sj; singletons n_sM
and B₂). **Two counts, two columns, never merged:** "prefix-gate" (some stage image k ≤ 4 is in the gate
phase) and "word-gate" (c₄ is). The menu is a position and is not amended by this; the prefix column
is information about Kittell's question (Section 6), the word column is OWL's.

# 3. The hard branch Δ-YES ∧ Δ′-NO: stuckness of c₄ is exactly Q3 ∧ Q4

c₄ = (r, s_M, r, s_j, s_i). In c₄'s canonical frame: copies B₁ (0), B₂ (2), color r; middle n_sM (s_M);
singletons n_si (position 3, color s_j, adjacent to B₂) and n_sj (position 4, color s_i, adjacent to B₁).
One-Context, applied in c₄'s frame, says c₄ is stuck iff its six template partitions hold. Each is a
chain-coincidence question in c₄:

| # | Pair | Template | Status |
|---|---|---|---|
| P1 | (r,s_M) | {B₁,n_sM,B₂} one chain | AUTOMATIC (link edges 0–1, 1–2 bichromatic) |
| P2 | (r,s_j) | {B₂,n_si} \| {B₁} | near part automatic (edge 2–3). Far part = **Q1: B₁ ∉ B₂'s (r,s_j)-chain.** X₄ is B₁'s (r,s_j)-chain in c₃, and a swapped chain is its own chain afterwards, so B₁'s (r,s_j)-chain in c₄ is X₄ as a set; Δ′-NO says B₂ ∉ X₄. **Q1 holds, FORCED by Δ′-NO.** |
| P3 | (r,s_i) | {B₁,n_sj} \| {B₂} | near part automatic (edge 4–0: r,s_i). Far part = **Q2: B₂ ∉ B₁'s (r,s_i)-chain in c₄.** |
| P4 | (s_M,s_j) | n_sM ~ n_si | **Q3.** |
| P5 | (s_M,s_i) | n_sM ~ n_sj | **Q4.** |
| P6 | (s_j,s_i) | n_si ~ n_sj | AUTOMATIC (edge 3–4). |

**Lemma T (the two-question lemma).** In c₄, Q3 ⟹ Q2, and Q4 ⟹ Q1. Hence c₄ is stuck iff Q3 ∧ Q4;
if either fails, τ(c₄) ≤ 5 and one swap inserts (leaf G).
*Proof.* An (s_M,s_j)-path from n_sM (position 1) to n_si (position 3), closed through v, is a cycle
using the edges v–n_sM and v–n_si; it separates position 2 (B₂) from positions 0 and 4 (B₁, n_sj). An
(r,s_i)-path is vertex-disjoint from it (disjoint colors) and cannot pass through v; so B₂ cannot lie in
B₁'s (r,s_i)-chain: Q2. Mirror for Q4 ⟹ Q1. If Q3 fails, (s_M,s_j) is operationally untangled at v
(Definition 5: the singleton pair's two link vertices are in different chains, so swapping n_si's chain
frees s_j); same for Q4. ∎ [Inputs: Definition 5; Jordan through v (S4); link edges (S3).]

**What Q3 and Q4 ARE, in terms of the earlier stages (derived):**
- **Q4 is a c₃ question.** Stages 2 and 4 swap (r,s_j) and never touch the (s_M,s_i)-world, so Q4 in c₄
  ⟺ n_sM ~ n_sj in the (s_M,s_i)-chains of c₃. Only stages 1 and 3 (both (r,s_i)) reshape that world:
  each removes its chain's s_i-vertices and adds its r-vertices (n_si leaves at stage 1; B₂ leaves and
  n_sj ENTERS at stage 3). So Q4 asks whether the middle stays (s_M,s_i)-connected to the far singleton
  after the near copy's chain has been swapped twice.
- **Q3 is a TUNNELING question.** K1838 2(a): in c₂ and c₃ the wall W = P ∪ v (P ⊆ X₃ any (r,s_i)-path
  B₂ → n_sj) separates n_si from {n_sM, B₁} for (s_M,s_j)-paths. Stage 4 swaps X₄ (r,s_j): the only
  vertices of P whose color leaves {r,s_i} are P's r-vertices lying in X₄ (they become s_j). An
  (s_M,s_j)-path n_sM → n_si in c₄ must cross EVERY such wall, hence at a P-vertex that is s_j in c₄,
  hence at an r-vertex of P that lies in X₄. **Q3 ⟹ X₄ ∩ r(P) ≠ ∅ for every B₂–n_sj (r,s_i)-path P of c₂
  — by Menger, X₄'s r-vertices SEPARATE B₂ from n_sj inside X₃.** So on the hard branch the fourth
  chain (B₁'s (r,s_j)-chain, which by Δ′-NO avoids both B₂ and n_si) must nonetheless reach into the
  third chain and cut it between the near copy and the far singleton. That is the S-leaf's signature,
  and it is consistent with Q2 (the cut is exactly what un-connects B₂ from n_sj in c₄'s (r,s_i)-world),
  as Lemma T requires.

**Leaf verdict on the hard branch:** G unless the fourth chain tunnels through the third chain's wall
(Q3) AND the middle keeps its (s_M,s_i)-road to the far singleton (Q4). Both are scorable per
configuration by Grace's G1 (rank) and Elie's union-find at c₃ and c₄; the tunneling cut |X₄ ∩ r(P)| is
a countable object.

# 4. The mirror word at an S leaf — the same tree with i ↔ j

At an S leaf, c₄ is canonical with the singleton colors exchanged (position 3 carries s_j, position 4
carries s_i). The bridge-anchored word in c₄'s frame is W′ := (B₂,(r,s_j))·(B₁,(r,s_i)) — the same
shape, each copy swapped with the pair of the singleton it touches. Lemma L (Legality) applies verbatim
with i↔j (its proof used only the forced (copy-pair) partition and color bookkeeping, both of which c₄
has by stuckness); Lemma D applies verbatim; the tree above repeats with Δ₂, Δ₂′, Q3₂, Q4₂. So the full
object is a self-similar tree: **each S leaf spawns the identical dichotomy tree in the mirrored
frame.** It is finite iff some potential strictly decreases from an S leaf to the next, or S leaves do
not occur. The tree's depth-1 leaf population on the 2,927 (Grace G2, Elie) decides which question is
live: if no S leaf occurs for {W_i, W_j}, the derivation target is "Q3 ∧ Q4 is impossible after
Δ-YES ∧ Δ′-NO" — one ∀-statement about two chains, and no potential is needed; if S leaves occur, the
potential of Section 5 is on trial.

# 5. PRE-REGISTRATION of the potential — BEFORE any leaf count reaches me

Ledger, stated first: my constructive guesses died on contact all week; my structural findings held.
This is a constructive guess and carries that prior.

**Candidate Φ (the wall size).** For a stuck canonical c, let X₃(c) be the near copy's (r,s_i)-chain
after the word's first two stages (the chain that BUILDS the wall), and define
  **Φ(c) := |X₃(c)|** (number of vertices; computed in the frame of c, for the bridge-anchored word of
  that frame). **Prediction (can fail):** at every S leaf, Φ(c₄) < Φ(c₀) — the next word's wall chain
  is strictly smaller than the wall the fourth chain had to tunnel through, because the tunneling cut
  X₄ ∩ r(X₃) is recolored s_j and leaves the (r,s_i)-world, and Δ′-NO keeps B₂'s side of the cut from
  regaining it. **Kill:** one S-leaf instance with Φ(c₄) ≥ Φ(c₀). **Fallback pre-registered second, not
  to be swapped in silently:** Φ′(c) := |X₃(c)| + |X₄(c)| (both wall chains). If both die, the potential
  question goes to Casey's desk with the two corpses and the S-leaf anatomy, and nothing else is tried
  this session. **If no S leaf exists on the 2,927, both are UNTESTED, not confirmed**, and the report
  says so.

# 6. Kittell's eight switches (Gethner et al. 2009, Definition 5, read from the PDF) vs our alphabet

Gethner's Figure 1 / Definition 3 pentagon: v₁…v₅ counterclockwise colored G, R, G, B, Y — so in our
roles: G = r with copies v₁ = B₁ and v₃ = B₂; v₂ = n_sM (s_M = R); v₄ = n_si (s_i = B, adjacent to v₃);
v₅ = n_sj (s_j = Y, adjacent to v₁). The eight Kempe–Kittell chains, verbatim seeds:
α RB at v₂/v₄ · β RY at v₂/v₅ · γ GY at v₁/v₅ · δ GB at v₃/v₄ · ε BY at v₄/v₅ · ζ GB at v₁/v₄ ·
η GY at v₃/v₅ · θ RG at v₂/v₁.

**Identification (derived from One-Context's forced partitions, which decide when two seeds name one
chain):** at a stuck configuration the fifteen seed-pair moves (5 roles × 3 pairs) name exactly EIGHT
distinct chains — M = (r,s_M){B₁,n_sM,B₂} [θ] · F_i = (s_M,s_i){n_sM,n_si} [α] · F_j = (s_M,s_j){n_sM,n_sj}
[β] · E = (s_i,s_j){n_si,n_sj} [ε] · B₁'s (r,s_j) ∋ n_sj [γ] · B₂'s (r,s_i) ∋ n_si [δ] · B₁'s (r,s_i) [ζ at
v₁] · B₂'s (r,s_j) [η at v₃] — because the six forced partitions merge the fifteen seeds into these
eight and no fewer (the two split bridge pairs each contribute two chains; the other four pairs one
each). **Kittell's eight switches are exactly this list.** So: **Kittell's alphabet (1935) = our move
alphabet modulo chain identity; his words = arbitrary finite sequences (Gethner: "unknown if there is
always a series … that will result in successful resolution of the impasse", impasse group ≥ 120);
our words = ordered commutators of two alphabet letters with distinct pairs.** Consequences: (i) at
chain level our 186 words collapse to 8 × 8 − 12 same-pair = 52 chain-commutators (26 up to the **[SWEEP 2026-09-02 11:32, Cal §821: the "52 chain-commutators = compression by identity" clause is STRUCK — 186 seed-words PROJECT onto 52 stage-1 chain pairs; seed-words over one pair can differ from stage 3 on. The seed rule (ζ@v₁, η@v₃) is part of the alias statement; with the other seeds Kittell's list names six chains.]**
mirror) — a compression by identity, not an enlargement; hitting sets should be reported at CHAIN level
too (@Elie, @Grace alias rows); (ii) OWL is the bounded-shape form of the Kempe–Kittell question, and
"impasse" = our τ = 6 stuck; (iii) the novelty is the SHAPE (one commutator) and the ∀-claim, not the
alphabet — say it that way externally.

# 7. Inputs (every lemma consumed, by name and status)

| Input | Where | Status |
|---|---|---|
| One-Context Lemma (applied in c₀, c₃, c₄ frames) | Sections 1–4 | derived 09-01; Cal PASS; registration pending |
| Lemma 3 (only the middle pair strict at τ = 6, gap 2) | Section 2 | K1832-verified |
| Definition 5 (operational tangling) | Lemma T | K1832-verified |
| Lemmas L, D (09-02) | Sections 1, 4 | derived; Cal read owed |
| Jordan through v; Whitney link cycle | Lemma T, Q3 | K1834 S3/S4 |
| Menger (vertex form) | Q3 structural reading | classical; elementary |
| 5-connectivity | nowhere | available, unused |
| Any census number | nowhere as a reason | — |

# 8. The question for Casey (K1838's, sharpened by Section 3)

The hard branch builds a wall the image needs: Δ-YES makes P ∪ v, which is precisely the (s_M,s_j)-
separation c₃'s template wants. For c₄ to be stuck, the fourth chain — B₁'s (r,s_j)-chain, which
Δ′-NO forbids from touching B₂ or n_si — must tunnel through that wall and cut the third chain between
the near copy and the far singleton (Q3), while the middle keeps its (s_M,s_i)-road to the far singleton
(Q4). **What does τ(c₀) = 6 forbid about a chain that avoids both ends of a wall and still cuts it?**
In your terms: the first word builds a fence between the two singletons; the image is stuck only if
the second word's chain digs under the fence without touching either post. Is there a Jordan reason a
chain in the original coloring's (r,s_j)-world cannot reach the interior of the other copy's
(r,s_i)-chain after two swaps — or is that exactly what the Poussin/Errera interference does, in which
case the S leaf is real and the potential is on trial?

— Lyra. The tree closed to two questions and the two questions closed to one picture: a fence and a
tunnel. Either the geometry forbids the tunnel, or the instruments will show us one by noon.
