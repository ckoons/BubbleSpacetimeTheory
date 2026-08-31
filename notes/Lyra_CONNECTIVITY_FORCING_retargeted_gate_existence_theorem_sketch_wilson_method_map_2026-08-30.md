---
title: "P3 — the Connectivity Forcing Lemma, retargeted after the transvection death: the Gate Existence Theorem as Gap B's first rung, a proof sketch from Middle-Strict + Lab-1 overlap geometry, the named missing step, and the Wilson/Feghali method map"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 17:34 EDT at round start)"
status: "ROUND 10, LANE P3 — the program's main line. One theorem-target restated, one proof sketch with its gap named, one method-import table. Sketch ≠ proof; nothing banks."
---

# THE CONNECTIVITY FORCING LEMMA, RETARGETED

## 1. What the transvection death changes (and what it doesn't)

Round 9's skeleton had McLaughlin at step 3. Tonight: 0/186 gate words act linearly — there are
NO linear parts to classify, and a third of the alphabet isn't even a function of the sign
pattern. McLaughlin exits; the skeleton's steps 1–2 RETARGET onto Wilson's actual method, which
never needed linearity: Wilson proves saturation by showing connectivity MANUFACTURES moves,
then composes moves combinatorially (cycle moves → 3-cycles → A_n), with a finite exceptional
check. Our translation:

**Gate Existence Theorem (the retargeted forcing lemma — Gap B's first rung, target to prove):**
*At every stuck configuration (τ = 6, deg-5 apex, in G−v), a 4-word gate with one-vertex net
support exists.* Measured: 739/739 across four graphs plus tranche-1 scale. Status: LAW-SHAPED,
UNPROVED. This is now the single most valuable theorem-target on the board: it is Wilson's
"2-connectivity manufactures the moves" in our dynamics.

## 2. Proof sketch (from machinery we already own), with the missing step NAMED

Setting: τ = 6, gap 2, positions 1..5 as always (1,3 = bridge r; 2 = middle s_M; 4, 5 = s_i,
s_j). Owned facts: Middle-Strict (the (r,s_M)-chain M ⊇ {1,2,3}, via link edges); forced
orientation (far copies pinned); the singleton chains F_i ⊇ {2,4}, F_j ⊇ {2,5}; and the Lab-1
collapse law (round 4): a commutator of two chains overlapping in a SINGLE CUT VERTEX whose
removal isolates the far anchor's side collapses to a one-vertex net recoloring — the gate.

Sketch: M and F_i overlap at vertex 2 (M carries colors {r,s_M}, F_i carries {s_M,s_i}; shared
vertices are s_M-colored; 2 is one). Both chains pass through the apex link with link-edge
rigidity on both sides of 2 (edges (1,2),(2,3) hold M; 2's membership in F_i is Middle-Strict's
dual). The commutator [σ_M, σ_{F_i}] anchored across 2 is, whenever 2 is a CUT of the overlap in
Lab-1's sense, a gate with support {2} or a link-adjacent vertex. Two of the six pair-types
overlap at 2 this way for ANY τ=6 coloring — candidates for the universal gate are therefore
STRUCTURALLY PRESENT at every stuck configuration; what is not yet proved is that the overlap
always satisfies the collapse criterion.

**The missing step, named: the Cut Lemma.** *At τ = 6, vertex 2's overlap between M and F_i (or
the σ-symmetric pair) always satisfies Lab-1's cut condition — i.e., removing the shared s_M
vertex separates the far anchor's component.* If the Cut Lemma holds, Gate Existence follows by
composition; if it fails somewhere, the measured 739/739 says some OTHER pair-type supplies the
gate there — so the honest full target is a disjunction over the finitely many overlap types at
the link, each with the same cut-condition shape. Elie's stored gate words already know which
pair-types fire where: **the empirical pair-type census is the free next datum for this proof
(request: tabulate which commutator template realized the gate, per stuck case).**

## 3. The method-import map (Feghali's survey as the atlas)

| Field method | Where it lives | Our import |
|---|---|---|
| Wilson 1974: connectivity manufactures moves; combinatorial composition; finite exceptions | puzzle groups | the skeleton itself (Section 1); exceptional list = frozen gallery |
| Mohar 2007 (via Fisk): parity/degree theory drives connectivity on 3-colorable planar | closed, Eulerian-adjacent | our charge theory IS the parity engine generalized; use charges to steer word construction (descent by frustration ordering) |
| Feghali 2023: 4-critical planar Kempe classes via structural induction on critical graphs | closed, critical | the induction template for lifting Gate Existence from configurations to graphs |
| Toroidal Kempe papers: winding arguments | genus cell | the monodromy summand's home; not tonight's lane |
| Bonamy–Bousquet–Feghali–Johnson (Mohar conjecture) | recoloring frontier | the live benchmark our closed-cell candidate must eventually meet in writing |

## 4. Order of battle (proposed, Casey routes)

(1) Elie's pair-type census (free, tonight — from stored words). (2) Prove the Cut Lemma for
the dominant pair-type (my lane, next session — it is a link-edge argument in Middle-Strict
style, exactly the kind that has held all day). (3) Compose: Gate Existence for that type;
disjunction closes as census dictates. (4) Then Gap B proper: gates + word order + the
frustration ordering as the descent — Wilson's composition step, ours to invent, with T2 (the
word problem) as Casey's live target on the worksheet.

— Lyra. Wilson didn't classify his moves; he manufactured them and composed. The gates are
manufactured 739 times over — tonight names the lemma that says they always will be.
