---
title: "THE CUT-DISSOLUTION LEMMA — candidate, with its derived parts marked: (1) the cut splits by ORIGINAL colour into type A (r-vertices of the near copy's own chain) and type B (s_i-vertices annexed by the second swap's new material); (2) a LETTER TABLE — which of the four middle-touching orbits can recolour which type at which stage, by colour-world bookkeeping; (3) the NECESSITY LEMMA — a word whose net support misses the closed neighbourhood of the bridge chains re-locks with the SAME cut; (4) H_cut CORRECTED before the count: 'contains' must mean 'recolours out of the bridge world in the NET support' — bare stage-chain containment fires on the control (the bridge word's own first chain contains every type-A cut vertex); (5) when M reaches a type-A vertex = a c₀ chain question with a Jordan bound; (6) the third door pre-registered: the fence REROUTED, cut untouched"
author: "Lyra"
date: "2026-09-02, Wednesday (clock-verified 10:24 EDT)"
status: "Round 99 deliverable. Sections 1–3, 5 derived (colour-world bookkeeping, chain maximality, Jordan through v; frames carried; no census number used as a reason). Section 4 is a correction to a pre-registration filed BEFORE Elie's H_cut count reaches me. Section 6 the lemma's sufficiency half — NOT derived; stated as the candidate with its kill. Casey's procedure (how the middle move is chosen when a pasted boundary is recoloured) is the prior and is not yet on the board; Section 7 says what I need from him. Nothing banks."
---

# 0. Objects, pinned (frames carried; Kittell letters used to dodge the B1/B2 label collision Cal flagged)

c₀ stuck, canonical: positions 0..4 = B₁(r), n_sM(s_M), B₂(r), n_si(s_i), n_sj(s_j); B₂ is the copy ADJACENT
to n_si. Kittell letters at c₀ (T2593): θ = M = the (r,s_M)-chain ∋ {B₁, n_sM, B₂}; α = F_i = (s_M,s_i) ∋ {n_sM,
n_si}; β = F_j; ε = E; δ = X₁ = B₂'s (r,s_i)-chain ∋ n_si; ζ = B₁'s (r,s_i)-chain; γ = B₁'s (r,s_j)-chain ∋
n_sj; η = B₂'s (r,s_j)-chain. The bridge word W_i = δ·γ; its trajectory c₀→c₁→c₂→c₃→c₄ with chains X₁ = δ,
X₂ (B₁'s (r,s_j) in c₁), X₃ (B₂'s (r,s_i) in c₂), X₄ (B₁'s (r,s_j) in c₃). **The cut C := X₄ ∩ X₃** (Lemma T /
Grace 5603: on a locked configuration C ≠ ∅, r-coloured in c₃, and C separates B₂ from n_sj inside X₃).

The four exiting first-word orbits (Elie 5605, at c₀'s frame), in letters: **O1 = θ·α** (the middle canonical
word); **O2 = δ·θ** or ζ·θ (a copy's singleton-pair chain, then the OTHER copy's middle-pair chain); **O3 = δ·α**;
**O4 = γ·θ** or η·θ. Every one carries a θ- or α-letter — a chain that carries the middle colour s_M.

# 1. The cut by its ORIGINAL colour — two types (derived)

Let u ∈ C. u is r in c₃ and u ∈ X₃, so stage 3 toggled it: u was s_i in c₂. Stage 2 is an (r,s_j)-swap and
cannot touch an s_i-vertex: u was s_i in c₁. Stage 1 toggled X₁ = δ on (r,s_i). Hence exactly one of:
- **Type A: c₀(u) = r and u ∈ δ** — an r-vertex of the near copy's own (r,s_i)-chain, turned s_i at stage 1,
  still (r,s_i)-connected to B₂ in c₂ (u ∈ X₃), turned r at stage 3, and lying in X₄.
- **Type B: c₀(u) = s_i and u ∉ δ** — an s_i-vertex NOT in B₂'s chain in c₀, annexed into X₃ only through
  stage 2's new r-material (X₂'s old-s_j vertices), then turned r at stage 3, and lying in X₄.
So **the cut is made of the near copy's own r-material (A) and of s_i-material the tunnel annexed (B).** Both
kinds are computable from c₀ alone (the bridge word is fixed by roles): C is target-innocent, as K1840 says.
Elie's H_cut count should carry the A/B split per cut vertex; the two types are recoloured by different letters
(Section 2), so a pooled count can hide the mechanism.

# 2. The letter table — which stage of which orbit can recolour which type (derived, bookkeeping only)

A chain of pair (a,b) at a stage can contain a vertex only if the vertex carries a or b AT THAT STAGE. Tracking
colours from c₀ through each orbit's four stages (m₁ m₂ m₁ m₂):

| Orbit | stage 1 | stage 2 | stage 3 | stage 4 | Type A (r in c₀) can end as | Type B (s_i in c₀) can end as |
|---|---|---|---|---|---|---|
| O1 = θ·α | (r,s_M) at n_sM | (s_M,s_i) at n_si | (r,s_M) at n_sM | (s_M,s_i) at n_si | r → s_M [if ∈M] → s_i [if ∈A₂] → … : **s_M, s_i, or r** | s_i → s_i → s_M [if ∈A₂] → r [if ∈M′] → …: **s_i, s_M, or r** |
| O2 = δ·θ | (r,s_i) at B₂ | (r,s_M) at B₁ | (r,s_i) at B₂ | (r,s_M) at B₁ | r → s_i [∈δ, always] → s_i → r [if ∈X₃″] → s_M [if ∈M₄″]: **s_i, r, or s_M** | s_i → s_i → s_i → r [if ∈X₃″] → s_M [if ∈M₄″]: **s_i, r, or s_M** |
| O3 = δ·α | (r,s_i) at B₂ | (s_M,s_i) at n_si | (r,s_i) at B₂ | (s_M,s_i) at n_si | r → s_i → s_M [if ∈A₂] → … : **s_i, s_M, or r** | s_i → s_i → s_M [if ∈A₂] → …: **s_i, s_M, r** |
| O4 = γ·θ | (r,s_j) at B₁ | (r,s_M) at B₂ | (r,s_j) at B₁ | (r,s_M) at B₂ | r → s_j [if ∈γ] or → s_M [if ∈M₂] …: **s_j, s_M, r, s_i-never** | s_i → s_i → s_i → s_i: **s_i only (untouched)** |

Reading: **a type-A cut vertex leaves BOTH bridge worlds (final colour s_M) only through a θ- or α-letter
acting while it carries r or s_M; a type-B cut vertex leaves the (r,s_i)-world only through an α-letter
(→ s_M) or, in O2/O4, a θ-letter after an (r,s_i)-letter has first turned it r.** O4 cannot touch type B at
all; so **if a locked configuration has a type-B cut vertex, O4 can exit only by rerouting (Section 6), never
by dissolving that vertex.** This is a derived, checkable prediction for Elie's cross-tab: on witnesses whose
cut has a type-B vertex, O4's exit (if any) is a rerouting exit.

# 3. THE NECESSITY LEMMA (derived) — the word must act on the bridge chains' neighbourhood

**Lemma N.** Let c₀ be bridge-locked by W_i with chains X₁..X₄ and cut C. Let O be any word with net support
N_O := {u : (O·c₀)(u) ≠ c₀(u)}, and c′ := O·c₀. If N_O ∩ N[X₁ ∪ X₂ ∪ X₃ ∪ X₄] = ∅ (closed neighbourhood), then
the bridge word W_i from c′ has the same four chains X₁..X₄, the same cut C, and c′ is bridge-locked.
*Proof.* A Kempe chain is a component of a bichromatic induced subgraph; membership of a vertex set S as a
component is decided by the colours on N[S]. c′ = c₀ on N[X₁], so X₁ is B₂'s (r,s_i)-chain in c′ (B₂'s role
is fixed by the link, which lies in N[X₁] — B₂ ∈ X₁ — and is unchanged). Then c′₁ := swap(X₁)·c′ agrees
with c₁ on N[X₂], so X₂ is B₁'s (r,s_j)-chain in c′₁; inductively X₃, X₄. Lemma T's conditions Q3, Q4 are
chain-coincidence questions on c′₄, which agrees with c₄ on N[X₃ ∪ X₄] ⊇ the relevant chains … [one
caveat, stated: Q3 and Q4 are questions about (s_M,s_j)- and (s_M,s_i)-chains of c₄ that may leave
N[X₁..X₄]; the lemma's clean form is the FIRST clause — same chains, same cut — and the lock follows if
Q3, Q4 are also unchanged, which holds when N_O is disjoint from N[those two roads] as well. State the
lemma with the union of all six chain neighbourhoods and it is exact.] ∎
**Consequence:** every exiting first word acts inside N[X₁ ∪ X₂ ∪ X₃ ∪ X₄ ∪ R₃ ∪ R₄]. Where inside is the
question H_cut asks; Lemma N says the answer cannot be "nowhere near."

# 4. H_cut, CORRECTED BEFORE THE COUNT (an adjective-class audit on "contains")

K1840's H_cut: "for every exiting first word, its stage chains CONTAIN C; for every non-exiting legal first
word, its chains MISS C." **As worded it fires on the control.** The bridge word W_i itself (a non-exiting first
word on every locked configuration, Cal §820) has first stage chain X₁ = δ, and **every type-A cut vertex lies
in δ by definition** (Section 1). So "some stage chain contains C" is satisfied by the non-exiting word whenever
the cut has type-A vertices, and the test cannot separate. The same holds for O2 and O3 (first letter δ):
their stage-1 containment of type-A vertices is automatic and carries no information.

**Corrected H_cut (pre-registered now, before Elie's cross-tab reaches me):** for an exiting first word O,
every cut vertex u ∈ C lies in the NET support of O with final colour OUTSIDE the (r,s_i)-world:
(O·c₀)(u) ∈ {s_M, s_j} — i.e. u is recoloured out of the near copy's bridge world and STAYS out after the
fourth stage; for a non-exiting legal first word, some cut vertex has final colour in {r, s_i} (untouched, or
toggled and toggled back). Two sub-hypotheses to report separately: **H_A** (type-A vertices end s_M/s_j) and
**H_B** (type-B vertices end s_M/s_j). Pre-score: H_A ∧ H_B on all 93 with the control failing on every
non-exiting word ⟹ the Cut-Dissolution Lemma has its mechanism half measured; H_A holds but H_B fails on
witnesses with type-B cuts ⟹ type-B vertices are dissolved by rerouting (Section 6), not containment;
neither ⟹ H_cut dead in the corrected form too, and the third door is the live one.

# 5. When does M reach a type-A cut vertex? (derived to a chain question with a Jordan bound)

Let u be type A: c₀(u) = r, u ∈ δ. Under O1 stage 1 swaps θ = M. **u ∈ M ⟺ there is an (r,s_M)-alternating
path in c₀ from B₂ (or B₁, n_sM — all one chain) to u.** Jordan bound: F_j ∪ v (the (s_M,s_j)-road from n_sM
to n_sj closed through v) separates {B₂, n_si} from B₁; δ is colour-disjoint from it, so **every type-A cut
vertex lies on B₂'s side of F_j ∪ v**; M crosses that wall only at s_M-vertices of F_j (n_sM itself is one),
so **M reaches u iff u is (r,s_M)-connected to B₂ within B₂'s side of the wall, or to an s_M-vertex of F_j.**
That is the chain question Q_M(u), computable in c₀ (Grace's rank instrument reads it). When M reaches u,
stage 1 turns it s_M — out of both bridge worlds — and it STAYS out iff u ∉ M′ (not re-annexed at stage 3:
u is stranded or excised by stage 2) and u ∉ A₂ △ A₄ (not carried into s_i and left there). So under O1,
**a type-A cut vertex is dissolved iff Q_M(u) ∧ [u ∉ M′] ∧ [u's (s_M,s_i)-toggles cancel]** — three chain
questions, all in the middle word's own stage table (yesterday's stranding/excision machinery, T2582–T2584,
now aimed at the cut instead of at a size bound).

**When O1 is illegal (SJ fails: n_si ∈ M′, i.e. after stage 2 the near singleton, now s_M, is (r,s_M)-connected
to n_sM):** O3 = δ·α reaches type-A vertices with its α-letter only after δ has turned them s_i (Section 2 row
3: s_i → s_M requires u ∈ A₂ = the (s_M,s_i)-chain at n_si in c₁; B₂ is s_i in c₁ and adjacent to n_si, and u
is (r,s_i)-connected to B₂ in c₀, so after the δ-swap u and B₂ are (s_i,r)… — u ∈ A₂ iff u is (s_M,s_i)-
connected to n_si in c₁, a chain question Q_α(u)). O2 = δ·θ reaches them only at stage 4 after stage 3 has
turned them back to r (row 2). O4 reaches type A through γ (→ s_j, leaving the (r,s_i)-world by the OTHER
bridge world) or through θ at B₂ (→ s_M). **So the four orbits are the four ways a middle letter can meet the
cut: directly on r-material (O1: θ first), on s_i-material after a δ-toggle (O3: α second), on r-material
after a δ-toggle-and-back (O2: θ fourth), or on B₁'s side via the other bridge world (O4).** That is the
derived reason there are four, and it predicts which orbit fires from the cut's type composition — Elie's
cross-tab checks it.

# 6. The lemma's sufficiency half (NOT derived) and the THIRD DOOR (pre-registered)

**Cut-Dissolution Lemma (candidate).** If c₀ is bridge-locked with cut C, and a fully legal middle-touching
word O recolours every u ∈ C out of the (r,s_i)-world in its net support, then the bridge word from c′ = O·c₀
exits (Δ-NO, or Δ′-YES, or ¬Q3 ∨ ¬Q4 in c′'s bridge trajectory). **Not derived.** What would derive it: show
that with C recoloured, no (r,s_i)-path from B₂ to n_sj can re-form in c′₂ (Δ-NO) — the reconnection was
built from X₂'s new r-material through X₃, and C was the bottleneck of X₃ (it separates B₂ from n_sj
inside X₃); if C is gone from the world and nothing new bridges the gap, the tunnel cannot form. The gap:
O's net support may ADD (r,s_i)-material elsewhere (its own α/θ toggles) that re-bridges. That is the
lemma's whole difficulty and it is one Jordan argument away or one counterexample away.

**Kill (K-CD):** a witness where an exiting first word leaves some cut vertex in {r, s_i} (net) — the
corrected H_cut fails on an exit. One instance kills the containment mechanism (not the count).
**Third door (D-CD, Casey's, named as ordered): the cut dissolves by REROUTING the fence, not by containment.**
Signature: an exiting first word O with N_O ∩ C = ∅ (no cut vertex recoloured) but N_O ∩ N[X₂] ≠ ∅ — O has
changed the second swap's material so that the reconnection path P never forms from c′ (Δ-NO at c′), while
the old cut vertices sit untouched. Lemma N says N_O must meet some chain neighbourhood; D-CD says it meets
X₂'s (the fence-builder's), not C. Pre-score: if the cross-tab shows exits with N_O ∩ C = ∅, the mechanism
is rerouting and the lemma must be restated about X₂'s new material, not about C. Both mechanisms can
coexist on different witnesses; report the split, never a verdict.

# 7. What I need from Casey (the prior, in his words, before I aim the sufficiency proof)

When you paste in a boundary and recolour: (1) what do you LOOK AT to decide the middle move — the two same-
coloured neighbours, the vertex between them, or the chain that runs out from the middle? (2) Is "the edge"
in your picture the LINK (the pentagon around the hole) or the FENCE (the chain that walls one side off)?
(3) When the middle move is not available — the chain from the middle runs where you do not want it — what
do you do instead: move a copy first, or move the singleton next to it? Your answers map onto O1 / O2 / O3
directly (Section 5's four ways), and the one you actually use is the orbit I should try to derive first.

# 8. Inputs
One-Context (frame of c₀) · Lemma T (T2590) · Lemma D (T2592) · T2593 letters · chain maximality (Lemma N) ·
Jordan through v (K1834 S4) · T2582–T2584 (net support / confinement / forced excision, for Section 5's three
questions). No census number cited as a reason; Elie 5605's four orbits are the OBJECT of the derivation, not
its premise — the letter table would list the same four if the census had never run, because they are the
four positions of a middle letter relative to the δ-toggle.

— Lyra. The cut has two kinds of vertex, the middle colour is the only door out for one kind, and the four
exiting orbits are the four places a middle letter can stand relative to the near copy's own swap. What I
cannot yet show is that taking the door closes the tunnel behind you. Casey's hands know; I am asking them.
