---
title: "Height-Allowance Conjecture — scope report: Klein/Tait anchor is real with one sharp disanalogy; the global inequality dies at K_6 (Hoşten–Morris); no genus-1 dimension analogue; what survives is genus-0 and it is exactly 4CT plus a candidate mechanism"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 10:13 EDT)"
status: "LANE 2 of round 2 (Keeper routing). DISCUSSION-tier per pre-registration; Casey's Height-Allowance Conjecture worked as tasked: (a) anchor, (b) false-neighbor sweep, (c) genus ladder. Verdict: which scope survives, reported without decoration. Sources pinned to primary literature; two literature numbers verified by web search this session."
---

# HEIGHT-ALLOWANCE CONJECTURE — SCOPE REPORT

**The conjecture as pre-registered (Casey, today):** n-colorability as a height allowance —
n = 4 because the incidence poset of a planar graph has order-dimension ≤ 3 (Schnyder), with the
(dim+1)-th color as the dimensional bridge permitting height reduction. Implied global form:
χ(G) ≤ dim(P_G) + 1, where P_G is the vertex-edge incidence poset.

**Verdict up front: the global form is FALSE, first false neighbor K_6. The genus-1 rung has no
raw-dimension analogue. What survives is the genus-0 statement — which, by Schnyder's own
characterization, is EXACTLY the Four-Color Theorem, so the inequality adds no new claim there.
What is genuinely new and alive is the MECHANISM the conjecture proposes: three orders + one
identity as the shape of a height-reduction proof. That aligns precisely with the Klein/Tait
structure of Kempe pairs (below, and it is real algebra, not analogy) and with the Schnyder-lattice
potential function P5 is hunting.**

## (a) THE KLEIN-GROUP / TAIT ANCHOR — real, with one sharp disanalogy

Pinned to sources: Tait (1880); Schnyder (1989) for dim ≤ 3 and the three trees; Felsner,
"Lattice structures from planar graphs" (Electron. J. Combin. 11, 2004) for the distributive
lattice of 3-orientations; Felsner–Trotter, "Posets and planar graphs," for the dimension
landscape.

Take the four colors to be the Klein group V = ℤ₂×ℤ₂ = {0, a, b, c}. Then:

1. **Tait's equivalence:** a proper 4-coloring of the faces (dually, vertices) induces on each
   edge the label = sum of its two side-colors; properness ⟺ labels are nowhere-zero, i.e., in
   {a, b, c} — Tait's three edge colors. 4CT ⟺ 3-edge-colorability of bridgeless cubic planar
   graphs ⟺ nowhere-zero V-flow. The "three directions + identity" of the conjecture is this
   literal group structure: three nonzero elements, one identity.

2. **Kempe pairs are cosets of directions — this is the part that connects to our proof
   machinery.** A color pair {x, y} determines the direction g = x + y ∈ {a,b,c}; a Kempe swap on
   an (x,y)-chain is exactly "add g on the chain." The six pairs partition as 3 directions × 2
   cosets, and since the four colors are the four group elements, r + s_k = s_l + s_m
   automatically: **each bridge pair (r, s_k) shares its direction with the opposite singleton
   pair (s_l, s_m).** The τ = 6 configuration in Klein coordinates, using this week's lemmas:
   - Direction g_M = r + s_M: bridge coset (r,s_M) is strictly tangled ALWAYS (Middle-Strict,
     link edges (1,2),(2,3)); its partner coset (s_i,s_j) is tangled ALWAYS (link edge (4,5)).
     **The middle direction is fully rigid — both cosets forced by link edges alone.**
   - Directions g_i, g_j: bridge coset cross-linked (forced, exactly — Middle-Strict sharpening),
     singleton coset strict. **Half rigid, half swap-active.**
   - The split-bridge swap acts in direction g_i or g_j; the post-swap new-middle direction is
     again fully rigid (the x = s_j sub-case = Middle-Strict post-swap). The double-swap mechanism
     is a walk on directions.
   This reformulation is worth carrying into v10 regardless of the conjecture's fate: it
   compresses the case structure and makes the "conservation of color charge" language literal
   (the charge lives in V).

3. **The sharp disanalogy, stated so the anchor cannot inflate:** Schnyder woods (the three
   orders) exist for EVERY planar triangulation — they are free, no 4CT needed. Tait/Klein
   colorings are 4CT-equivalent — they are the whole theorem. Any dictionary "three Schnyder
   trees ↔ three Klein directions" therefore cannot be an isomorphism of existence; it must be a
   nontrivial map from a free structure to a hard one. That is not a defect — it is exactly where
   a proof could live (free scaffold, hard invariant descending it) — but the conjecture must be
   phrased as "the three orders SUPPORT a height reduction," never as "the three orders ARE the
   three color directions." P5 (do Kempe swaps project to lattice flips; is any wood-derived
   quantity monotone?) is the empirical probe of precisely this map.

## (b) FALSE-NEIGHBOR FAMILY SWEEP — the global inequality dies at K_6

Literature numbers, verified this session (Hoşten–Morris 1999, "The order dimension of the
complete graph," Discrete Math. 201, 133–139; Felsner–Trotter; standard references on the
incidence poset):

| Graph | χ | dim(incidence poset) | χ ≤ dim + 1? |
|---|---|---|---|
| planar G | ≤ 4 (4CT) | ≤ 3 (Schnyder 1989; ⟺ planar) | the conjecture's home rung |
| K_4 | 4 | 3 (planar) | ✓ tight |
| K_5 | 5 | 4 (nonplanar ⟹ ≥ 4; ≤ 4 by HM) | ✓ tight — consistent boundary |
| **K_6** | **6** | **4** (HM: dim(K_n) = 4 for 5 ≤ n ≤ 12) | **✗ — first false neighbor** |
| K_12 | 12 | 4 (HM) | ✗ by 7 |
| K_13 | 13 | 5 (HM: dim(K_13) = 5) | ✗ |
| K_n | n | Θ(log log n) (HM asymptotics) | ✗ catastrophically |

The divergence is structural, not marginal: χ(K_n) grows linearly, dim(P_{K_n}) doubly
logarithmically — dim stays ≤ 5 out to astronomically large n while χ = n. **The allowance is not
global, and no adjustment of the "+1" fixes it — no function of dim alone bounds χ, since dim = 4
admits χ from 5 to 12.** The tight boundary cases K_4, K_5 are the false-neighbor bait: two rungs
where two unrelated ladders happen to touch. Family-sweep discipline did its job.

## (c) THE GENUS LADDER — no dimension analogue at genus 1

Heawood/Ringel–Youngs: torus allows χ = 7, realized by K_7. But dim(P_{K_7}) = 4 (HM), so a
dimension-side ladder would predict an allowance of 5 at whatever rung holds K_7 — the toroidal
Heawood number 7 is not dim+1 of anything in sight. Both directions fail: the genus ladder climbs
in steps of Heawood's formula while the dimension ladder crawls at log log; and a single dimension
class (dim = 4) spans χ = 5 through 12, so dimension classes do not refine genus classes.
**There is no genus analogue of the allowance via raw incidence-poset dimension.** (If a genus
analogue exists at all, it must use a different poset invariant — e.g., dimension of some
surface-adapted structure — and nothing in this session's literature pass suggests a candidate.
Reported as absence-after-search, not as impossibility.)

Bottom rung, for completeness of the ladder: dim ≤ 2 corresponds to (essentially) disjoint unions
of paths, where χ ≤ 2 < dim + 1 — the allowance is slack there, tight only at dim = 3. One rung of
tightness is a coincidence, not a law. (Verify the exact dim ≤ 2 characterization against
Felsner–Trotter before any external citation; it is decorative here.)

## WHAT SURVIVES — the honest residue

1. **Scope: genus 0 only.** There, by Schnyder's characterization (planar ⟺ dim ≤ 3), the scoped
   inequality "dim ≤ 3 ⟹ χ ≤ 4" IS the Four-Color Theorem — a restatement, not a new claim.
2. **The live content is the mechanism program:** use the three Schnyder orders (free scaffold) +
   the Klein direction structure of Kempe pairs (Section a.2 — now sharpened by Middle-Strict into
   "one rigid direction, two active ones") + the distributive lattice of 3-orientations (Felsner)
   as the potential function that the double-swap walk descends. That is Casey's AVL frame made
   precise: lattice height as tree height, swap as rotation, and the missing OR-lemma of my Lane 1
   note as the "rotation terminates" step. If P5 finds a wood-derived monotone quantity, the two
   lanes join: the potential closes both the OR-lemma and the bounded-swaps scope question at once.
3. **The (dim+1)-th color as identity element** is not decoration: in the Klein formulation the
   identity 0 is structurally distinguished (edge labels are the nonzero elements), which is a
   cleaner statement of "the fourth color is the bridge" than any height metaphor — and it is
   theorem-adjacent, not conjecture: it is how Tait's equivalence works.

**Recommendation:** re-register the conjecture at its surviving scope — "the three Schnyder orders
support a height-reduction proof of 4CT, with the Klein identity as the fourth color" — as a
mechanism program gated on P5, and retire the global inequality with K_6 named as its false
neighbor. The pretty version died in the family sweep; the useful version is now welded to the one
open lemma the paper actually needs.

— Lyra. The conjecture asked "is 4 a height allowance?" The family answered: only on the sphere,
where the question was already the theorem — but the three orders may yet be the right ladder for
the proof to climb down.
