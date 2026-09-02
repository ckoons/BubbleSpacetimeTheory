---
title: "THE CANDIDATE ASSEMBLY — the Insertion Theorem, candidate form"
author: "Lyra"
date: "2026-09-01, Tuesday (clock-verified 09:20 EDT at round start)"
header_note: "This program has been one page from history before: in March a document titled as a proof carried one false premise for five months through a PASS it never earned (K1832's finding, 2026-08-30). That memory is a load-bearing part of this document. Accordingly: the verification protocol of Section 4 is attached to the assembly itself, the document contains no abstract, no status claim, and no statement of any consequence beyond what Section 1 states — it states what it proves, under which labeled conditions, and stops."
---

> **SUPERSEDED 2026-09-02 08:53 EDT by `Lyra_CANDIDATE_ASSEMBLY_v2_insertion_theorem_consumption_line_struck_OWL_named_2026-09-02.md`.** The count clause "at most d_gate(c) + 1" is STRUCK: d_gate is finite iff T is 4-colorable (Lyra 08:06 / Keeper K1835 08:10), so it presupposed the theorem. Retained unedited below as the record of what was assembled.

# THE CANDIDATE ASSEMBLY

## 1. The statement assembled

**Insertion Theorem (CANDIDATE — conditional on J1 and J2 of Section 3).**
For every sphere triangulation G, every vertex v of G with deg(v) = 5, and every proper
4-coloring c of G−v: there is a finite sequence of Kempe words in G−v, each of length ≤ 4,
of total count at most d_gate(c) + 1 — where d_gate is the M1 (Hamming) distance to the GATE
PHASE's target set (the τ ≤ 5 colorings, per Cal's data-independent seam ruling: the final
freeing swap is a phase boundary and carries its own honest +1; the subscript rule applies at
metric level) — whose application yields a coloring in which some color is absent from v's
link.

Case analysis carried by the assembly:
- some color absent from the link already: zero words;
- saturated with gap 1, or any configuration with τ(v) < 6: one single swap (Lemma 2 /
  the definition of operational tangling);
- saturated with τ(v) = 6 (the stuck case): by the One-Context Lemma every such configuration —
  initial or arising later in the sequence — presents the canonical context; by the One-Page
  Context Proof the anchored commutator applies there, is patch-local [J1], and strictly
  decreases d_gate [J2]; d_gate is a non-negative integer, so at most d_gate(c) such words
  occur, plus the phase boundary's one freeing swap.

Quantifier form, displayed: ∀ G (sphere triangulation) ∀ v (deg 5) ∀ c (proper on G−v) —
no quantifier is restricted to measured families anywhere in the chain; the restriction to
measured families enters only through the labels J1, J2.

## 2. The parts and their standing

| Part | Content | Standing |
|---|---|---|
| Hand-off Theorem (T2579) | no anchored wall exists between any pair of colorings of (G−v, ∅), under all moves and all proof operations | BANKED (Cal §803). Role: the mechanism theorem — the one exhibited freeze mechanism cannot operate anywhere in the sequence. The deductive chain below does not consume it; it stands as the reason the labeled joints are credible rather than hopeful. |
| One-Context Lemma | stuckness forces the canonical context, up to symmetry, in every sphere triangulation | derived (2026-09-01), zero census joints; inputs: Lemma 2, Lemma 3, Def-9 Remark (audit-verified sound, K1832); Middle-Strict, Orientation (proved, link-edge; registration pending) |
| One-Page Context Proof | in the canonical context: stages 1–3 of every family word are legal (derived — Cal §805's stage table); SOME family word is fully legal (stage 4 = sub-joint SJ, absorbed into the choice), patch-local [J1′, choice-quantified], and strictly M1-descending [J2, existence form] | three derived rows, two labeled joints, one choice clause carrying SJ |
| M1 = d_gate | Hamming distance to the gate phase's target set (the τ ≤ 5 colorings); frozen (Cal §801, consumer grounds; seam pinned data-independently — the freeing swap is the phase boundary's +1) | well-founded, strictly decreasing under [J2], minimized exactly at the gate phase |

## 3. The labeled conditions (the complete list — nothing else is assumed; swept 2026-09-01 to match the choice-quantified restatement)

- **SJ (stage-4 legality):** absorbed into the choice quantifier over the finite word family 𝒜
  (mirror × orientation × anchor-side; lengths 2–4); per Cal §805.

- **J1 (patch-locality):** proved on the single-cut overlap sub-case; measured 1,822/1,822 in
  the canonical context (three objects, two scales, zero splits, positive control); general
  derivation open (the Collapse Law for the context's forced overlap structure).
- **J2 (strict descent):** measured universal in the canonical context (Fritsch exact;
  sampled-freed caveat on tower columns); mechanism-supported (Wall Transport; no-tilt);
  derivation open (the transported-wall geometry argument, one clause from closed).
- **Scope of measurement:** J1/J2's measured columns cover three objects at two scales; the
  adversarial breadth falsifier (Section 4, running) extends or refutes.

## 4. The verification protocol (attached to the assembly; consumption before completion is a
protocol violation)

1. **Elie's adversarial breadth falsifier runs clean** — stuck configurations hunted across
   graph families the vocabularies did not grow up on; any second context, any patch-locality
   failure, any non-descending gate is a refutation of the corresponding joint and re-opens
   this document at the named line.
2. **Cal's hardest read passes** — the assembly, the One-Context derivation, and the One-Page
   proof; his scope log rides with any bank.
3. **The joints either close by derivation or remain labeled in every citation** — a citation
   of this document that omits J1/J2 misstates it.

## 5. Non-claims

1. Nothing is claimed for deg(v) ≤ 4 (classical Kempe territory; outside this document).
2. Nothing is claimed about any consequence of the statement in Section 1. This document
   states what it proves, under which labeled conditions, and stops.
3. The Hand-off Theorem's mechanism-uniqueness scope is unchanged (one freeze mechanism is
   exhibited and excluded; no claim that others cannot exist — J1/J2 are exactly where any
   other would surface, which is what the breadth falsifier hunts).
4. Word length ≤ 4 and count ≤ d_gate(c) + 1 are claims of the assembled statement; no claim
   of optimality in either.

— Lyra.
