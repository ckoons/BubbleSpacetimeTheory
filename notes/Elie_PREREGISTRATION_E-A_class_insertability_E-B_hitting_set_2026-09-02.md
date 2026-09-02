---
title: "PRE-REGISTRATION — E-A Class-Insertability and E-B the hitting set (K1836 Section 2). Populations, enumerator, positive control, pre-scored outcomes. Held at Keeper's gate; nothing below runs as an experiment until the gate says so (the positive control runs as INSTRUMENT VALIDATION only)."
author: "Elie"
date: "2026-09-02, Wednesday (clock-verified 08:51 EDT, stamp copied from a separate render)"
status: "PRE-REGISTRATION. Toys claimed: 5594 (E-A), 5595 (E-B). Correction filed in Section 0."
---

# 0. Correction of my 08:33 sentence (and the spec's Section 8)

I wrote "its truth for all T is 4CT." Wrong direction. **The One-Word Lemma (OWL) for all T is SUFFICIENT
for 4CT; it is not equivalent to it** — 4CT does not give OWL back (a 4-colorable T can in principle have a
stuck coloring no single family word exits). Corrected in the spec (Section 8) at 08:51. OWL's status:
sufficient for 4CT, stronger than 4CT, measured 2,927/2,927, proved nowhere. The lemma is never called the
theorem; 4CT is never called proved.

# 1. E-A — Class-Insertability (toy 5594)

**Question.** For (T, v), v of degree 5: enumerate the Kempe classes of proper 4-colorings of T−v (Kempe
swaps in T−v, any seed, any pair; v absent). Does EVERY class contain a coloring with τ_v ≤ 5 or a color
absent at v (insertable)? Kempe words never leave a class, so ONE class with no insertable member kills OWL
and every bounded-menu claim at once.

**Enumerator.** Backtracking enumeration of all proper 4-colorings of T−v modulo the 24 color permutations
(canonical form: colors relabeled by first appearance in a fixed vertex order; Kempe swaps commute with
relabeling, and τ_v and insertability are relabeling-invariant, so classes-mod-S4 carry the question
exactly). Kempe adjacency: for every canonical coloring, every vertex u ≠ v, every color b ≠ c(u): swap the
(c(u), b)-chain of u, canonicalize, union. Classes = union-find components. Per class: does any member
satisfy insertable(v)? Reported per (T, v): number of classes, number with an insertable member; per
population: k/N classes-with-an-insertable-member and the list of (T, v, class-size) for any class without.
Raw-coloring class counts (not mod S4) reported alongside on the small cases as a consistency line.

**Positive control (runs BEFORE any negative, as instrument validation — not the experiment).** Florek's
G_n = n-antiprism + two apexes (poles non-adjacent, degree n; 2n vertices of degree 5), arXiv 2511.00485:
PROVED ≥ ⌊n/6⌋ Kempe classes of 4-colorings of G_n. **The bound separates only at n ≥ 12 (⌊12/6⌋ = 2).**
The control is therefore G_12 whole (26 vertices): the enumerator must report ≥ 2 classes on G_12 or it
may not report "one class" anywhere. Secondary control: the enumerator on G_n whole for n = 6…11 reports its
counts (the bound there is 1 and does not separate; reported, not relied on). If G_12 whole is beyond the
hour's compute, the fallback control is FCW-014's disc twins (Z1, toys 5526/5559), a corpus-internal
multi-class case — stated now so the switch is not a surprise.

**Populations, in order.**
(i) plantri exhaustive: all triangulations n = 6…11 (2 · 5 · 14 · 50 · 233 · 1,249), EVERY degree-5 vertex.
    Note for the gate: min-degree-5 triangulations (-m5) begin at n = 12 (one: the icosahedron); at n ≤ 11
    the population is all triangulations, degree-5 vertices included wherever they occur. Then n = 12, 13
    4-connected (-c4: 87 and 313) if time permits.
(ii) Florek's G_n, n = 5…12, at a degree-5 vertex (all degree-5 vertices are equivalent under the dihedral
     symmetry of the antiprism; one representative, symmetry stated). G_n − v for n = 12 has 25 vertices —
     same scale as the control.
(iii) THE NINE hard configurations (saved .nine_hard.json: 4 on T3, 5 on B-errera; both 17-vertex objects,
      T−v = 16 vertices — exhaustive is feasible): the class of each stuck coloring, whole, and whether it
      contains an insertable member. Also whether the class contains the one-word image found by 5591 (a
      consistency line: it must).

**Pre-scored.** Any class without an insertable member, anywhere → **OWL DEAD**, DGT survives only
class-qualified ("in every Kempe class containing a target"); the class certificate (T, v, the class as a
list of canonical colorings, its size, the absence verified exhaustively) is the exhibit. All classes
insertable everywhere → the NECESSARY condition stands; not proof; the sentence is "Class-Insertability holds
on N triangulations / M (T, v) pairs / K classes," counts only. Instrument catch: a (T, v) whose coloring
enumeration exceeds the cap is reported "not enumerated," never counted either way.

**Kill conditions on the instrument itself.** (a) G_12 reports 1 class → enumerator broken; nothing reports.
(b) A class found without an insertable member on a plantri case is re-checked by raw (non-canonical)
enumeration before it is called a kill. (c) The nine's classes must contain 5591's images (else join-key
mismatch, checked first).

# 2. E-B — The hitting set (toy 5595)

**Question.** Over the stuck configurations measured (the 54 · the 1,801 · the 1,072 whole stuck sets;
deduplicated by (object, coloring) — the true count reported, 2,927 is the nominal), each configuration's
HIT SET = the fully-legal family words whose image has a color absent at v. Minimum hitting set of words;
its growth across populations; whether a FIXED set of ≤ 4 words hits everything.

**Method.** Exact minimum via a small branch-and-bound over the 186 words (lower bound = greedy-disjoint
packing; upper bound = greedy set cover), reported with both bounds if the exact search exceeds the cap.
Curve: minimum hitting-set size per population and cumulative in the order Fritsch → T3 → B-errera →
D-flip2 → D-flip3 → the 54 → tranche-2a → tranche-2b. The candidate fixed set named in advance:
(B1,(r,s_i))(B2,(r,s_j)) and its three equivalents (715 direct hits each in 5593).

**If ≤ 4 fixed words hit everything: the chain-interaction pattern table.** For each hitting word on each
configuration: the four stage chains X₁…X₄ (the Kempe chains actually swapped at stages 1–4), the pattern =
(which link roles each stage chain contains; which stages' chains meet; support = (X₁△X₃) ∪ (X₂△X₄) per
Net-Support, checked against the measured support), and which patterns FREE which color. Table = distinct
patterns × count × freed color. Lyra derives completeness; I harvest occurrence.

**Pre-scored.** Fixed set of ≤ 4 hits all → OWL's derivation is a finite case analysis on those words'
patterns (the table is the case list). Hitting set grows with population → the menu is doing work no one
has derived; the number and the curve are the result, no interpretation added by me.

# 3. Scope and honesty lines
No percentages. Every negative is positive-controlled. "Not enumerated" is a category. The lemma is never
called the theorem. Nothing here runs as an experiment before Keeper's gate; the control and the enumerator's
self-tests run now as instrument validation and are reported as such.

— Elie
