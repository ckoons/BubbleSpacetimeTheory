---
title: "L2 — THE ONE-PAGE CONTEXT PROOF: in the canonical context a gate exists, is patch-local, and strictly M1-descends — the construction derived, the two residual joints labeled exactly (J1 patch-locality, J2 descent), with their mechanism support and their closure paths named"
author: "Lyra"
date: "2026-09-01, Tuesday (clock-verified 09:20 EDT at round start)"
status: "The one page, choice-quantified (Cal §805; swept 2026-09-01 same-hour rule, fourth and fifth strings). The deductive residue is J1′ + J2 + the choice clause carrying SJ — nothing else stands between the assembly and an unconditional theorem. Cal's read of the restatement owed."
---

# THE ONE-PAGE CONTEXT PROOF

Setting: the canonical context of the One-Context Lemma — link word (0,1,0,2,3), all six
partitions forced. Write M for the (r,s_M)-chain (contains {B₁, n_sM, B₂} — forced) and F for
the (s_M,s_i)-chain (contains {n_sM, n_si} — forced). The metric is M1, frozen (Cal §801):
d(c) := min over freed colorings c* of the Hamming distance |{u : c(u) ≠ c*(u)}|.

**Claim (CHOICE-QUANTIFIED — restated per Cal §805 and Toy 5568; this restatement supersedes
the original compressed paragraph).** There is a finite, explicitly listed word family 𝒜 —
the mirror (i/j) × orientation × anchor-side options of the 4-move template (Elie's
enumeration supplies the concrete list, so the existence quantifier ranges over a finite
object) — such that at every stuck configuration:
(1) stages 1–3 of every family word are legal [DERIVED — Cal's stage table, below];
(2) SOME w ∈ 𝒜 is fully legal — stage-4 legality is ABSORBED INTO THE CHOICE, and this
    sub-joint carries its name: **SJ (stage-4 / n_si ∉ X₃)**;
(3) that w's net effect is patch-local at size ≤ C [**J1′ — choice-quantified
    patch-locality**]; and
(4) that w strictly M1-descends [**J2 — existence form**, F3's 100%-per-stuck].

**The stage table (Cal §805's derivation, carried as handed):**
- Stage 1 legal: n_sM carries s_M ∈ α's pair. [Derived]
- Stage 2 legal: n_si carries s_i, untouched by move 1 (it is not in X₁'s color world). [Derived]
- Stage 3 legal: move 1 flipped n_sM to r, and r IS in α's pair — the anchor's color moves
  WITH the pair, and X₂ cannot touch it (n_sM is r-colored in c₁, invisible to the
  (s_M,s_i)-subgraph). [Derived]
- Stage 4 NOT forced: n_si carries s_M in c₂, but its survival requires n_si ∉ X₃, and the
  forced partitions do not exclude an interior (r,s_M)-path in c₂ from n_si to n_sM (B₂ is
  provably out of that world — the link edge forces B₂ ∈ X₂ — but interior routes are open).
  [SUB-JOINT SJ — absorbed into the choice quantifier, per §805.]

The complete deductive residue of the assembly is therefore **J1′ + J2 + the choice clause
carrying SJ** — as Cal ruled: two joints and a choice, every one labeled.

**J1 — patch-locality (2), LABELED JOINT.** What stands: the single-cut overlap case is PROVED
(the Cut Lemma's single-overlap case, R15 note — when M ∩ F = {n_sM}, the commutator's net
support collapses to a bounded patch at the anchor); the general Collapse Law (arbitrary
overlap) is UNPROVED — the named debt since R11. In-context standing: patch-locality measured
1,822/1,822 across three objects at two scales, zero splits, positive control passed
(Toy 5562). Closure path: prove the Collapse Law for the canonical context's forced overlap
structure — a bounded case analysis on how M and F can share s_M-vertices beyond the anchor.
STATUS: proved on the single-cut sub-case; measured-universal in context; general derivation
open.

**J2 — strict descent (3), LABELED JOINT.** What stands: strict M1 descent measured universal
in context (Fritsch exact 144/144; the 1,822-instance census; sampled-freed caveat on tower
columns, Fritsch column exact). Mechanism support, labeled as mechanism and not derivation:
(i) Wall Transport — the gate moves the wall to the target rather than shrinking it, and a
transported wall overlapping the difference region at the link reduces Hamming count there;
(ii) no-tilt — an unpinned hole is never height-extremal (Scope-Theorem mechanism), so a local
rearrangement toward the freed set is never height-forbidden. Closure path: derive descent from
the transported wall's geometry in the canonical context (the patch meets the link; every freed
target differs from c at link-adjacent vertices; the gate's re-signing agrees with some freed
target on ≥ 1 patch vertex and disagrees nowhere new — the last clause is the open step).
STATUS: measured-universal in context; mechanism-supported; derivation open.

**Iterability (derived).** After w, the configuration is freed or stuck; if stuck, the
One-Context Lemma applies again (it is a ∀-statement over all sphere triangulations and all
stuck configurations), yielding the same context and the same template. With (3), d strictly
decreases each round; d is a non-negative integer; the process reaches a freed coloring in at
most d(c₀) gate applications. [Derived, GIVEN (2)–(4) — i.e., modulo J1′, J2, and the
choice clause carrying SJ.]

**The honest sentence (swept 2026-09-01 per the restatement — the same-hour rule):** the page
is a stage table with three derived rows, one sub-joint (SJ) riding the choice quantifier, and
two joints. J1′ + J2 + the choice clause carrying SJ are the complete deductive residue of the
program: close them and the Insertion Theorem is unconditional; leave them and it is a
candidate with its conditions in plain sight — which is what the Candidate Assembly says, and
stops.

— Lyra. One page, as ordered: the construction earns its keep by derivation, and the two
places where measurement still carries the load are named in capital letters, because that is
how this program builds things that stay built.
