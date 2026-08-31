---
title: "The three-algebra dictionary — Klein/Tait XOR, Heawood GF(3) triangle signs, Tutte 4-flows: one object, three coordinate systems; with the Straddle-Flip Lemma (candidate) as the new row"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified ~10:34 EDT at round start)"
status: "ROUND 3, LANE L3. Dictionary rows are classical (Tait 1880, Heawood 1898, Tutte 1954) except where marked NEW. The Straddle-Flip Lemma is a candidate: derived by hand this session, case-verified, NOT toy-verified — verification request to Elie's E4 below. Nothing banks."
---

# THE THREE-ALGEBRA DICTIONARY

Everything on a planar triangulation T (sphere), colors identified with the Klein group
V = ℤ₂×ℤ₂ = {0, a, b, c}.

## 1. THE THREE COORDINATE SYSTEMS (classical)

| | Klein/Tait (vertex) | Heawood GF(3) (face) | Tutte flow (dual edge) |
|---|---|---|---|
| Variable | vertex color f(v) ∈ V | face sign z_t ∈ {±1} ⊂ GF(3) | dual-edge flow φ(e) ∈ V∖{0} |
| Constraint | adjacent colors differ | Σ_{t ∋ v} z_t ≡ 0 (mod 3) ∀v | Kirchhoff at dual vertices |
| 4CT says | proper f exists | nowhere-zero solution exists | NZ 4-flow exists (planar case) |
| Translation | edge label ℓ(uv) = f(u)+f(v) ∈ {a,b,c} | z_t = orientation of the label triple | φ = ℓ on dual edges |

The translation mechanism, spelled once: a proper coloring makes every triangle's three vertex
colors distinct, so its three edge labels are three distinct nonzero elements summing to 0 — i.e.,
exactly {a,b,c} on every face. Walking a face's boundary counterclockwise reads the labels as a
permutation of (a,b,c); its parity is the Heawood sign z_t. The vertex condition Σ z_t ≡ 0 mod 3
around each vertex is the consistency condition for reconstructing f from z (up to global
V-translation and the a/b/c relabeling). Tait's 3-edge-coloring of the dual cubic graph is the
label function ℓ itself; the nowhere-zero V-flow is ℓ read as a flow.

## 2. KEMPE DYNAMICS IN EACH COORDINATE SYSTEM

**Klein (Toy 5514, verified — the exact row):** a Kempe swap on a (p,q)-chain S adds
g = p + q to f on S: an XOR-toggle. Pairs are cosets of directions: {p,q} and its complementary
coset share the direction g, so the six pairs = 3 directions × 2 cosets. (Middle-Strict in this
language: at τ = 6 the middle direction has BOTH its cosets rigid via link edges; the two active
directions each have a cross-linked bridge coset and a strict singleton coset.)

**Heawood GF(3) — NEW ROW, the Straddle-Flip Lemma (candidate).**
*Under a Kempe (p,q)-swap on chain S, the sign vector transforms as z_t ↦ −z_t exactly on the
faces with 1 or 2 vertices in S (the faces straddling ∂S), and z_t is unchanged on faces with 0
or 3 vertices in S.*

Proof sketch (case-complete, by hand this session):
- 0-in / 3-in: every edge keeps or shifts BOTH endpoints by g — labels unchanged, sign unchanged.
- 1-in (u ∈ S; outside neighbors v, w): v, w are adjacent to u with colors outside {p,q} (else
  they would be in the chain), so the outside edge's label is f(v)+f(w) = p+q = g — the FIXED
  label is g. The two moved labels shift by g; on the label alphabet, ℓ ↦ ℓ+g is the
  transposition τ_g (fixes g, swaps the other two — Klein: sum of two distinct nonzero elements
  is the third). The two non-g labels swap; the triple's parity flips. (ℓ = g cannot occur on a
  moved edge: it would force an outside neighbor into {p,q}.)
- 2-in (u,v ∈ S adjacent, colors p,q; w outside): the inside edge's label is p+q = g and both its
  endpoints shift — label fixed at g. The two moved labels are again the non-g pair (their sum is
  g and neither equals g by properness), and they swap. Parity flips.

Corollaries if it survives verification:
- **Kempe dynamics = a walk on the nowhere-zero GF(3) solution set, moving by sign-flips
  supported on dual cut cycles** (the straddle set of a chain is the set of faces met by the dual
  cycles bounding S). The Heawood constraints are preserved automatically (properness is).
- The flow avatar: the swap adds the elementary g-valued circulation on ∂S's dual cycles — Toy
  5514's "XOR-toggle on chain boundaries," now in all three coordinates at once.
- E4's rank/coset computation acquires a dynamical reading: stuck-vs-unstuck is a question about
  which NZ solutions are reachable by straddle-flips of CURRENT chains (the move set depends on
  the current point — this is where the nonlinearity, and the whole difficulty, lives; the linear
  system is free, the walk is not. Same free-scaffold/hard-invariant split as Schnyder-vs-Tait in
  yesterday's scope report.)

**Verification request (Elie, E4, one extra assertion):** while building the GF(3) instrument,
check per swap that the observed z-flip set equals the straddle set of the swapped chain —
one boolean per swap over the gallery. Any exception kills the lemma; 0 exceptions promotes it to
toy-verified candidate for registration.

## 3. WHAT THE DICTIONARY BUYS THE ROW

1. **One object, three instruments.** Stuckness (rescue depth) can be measured in Klein
   coordinates (chain structure, our lemmas), GF(3) coordinates (rank/coset, E4), or flow
   coordinates (circulation space). A configuration invisible in one system may be plain in
   another — the wall-routing principle applied to the proof itself.
2. **The corpus hook, stated as framing, not claim:** the Heawood system is the kernel of a
   vertex–face incidence matrix over GF(3) — a linear code; 4CT is "this code has a full-support
   codeword"; Kempe moves are the local re-encodings. This puts the row on the corpus's
   GF/Reed–Solomon substrate footing and satisfies the linearization standing order (every result
   as an element/eigenvalue/grading of one operator — here the incidence operator mod 3).
3. **For L1 (potential program):** the Straddle-Flip Lemma localizes a swap's entire effect to
   ∂S. Iterated swaps propagate sign-flips boundary-by-boundary — exactly the geometry a per-layer
   descent potential needs (see the L1 note filed alongside this one).

## 4. HONEST EDGES OF THE DICTIONARY

- The Klein↔GF(3)↔flow equivalences are classical; the Straddle-Flip Lemma is elementary enough
  that it is PLAUSIBLY in the literature (Fisk's coloring-geometry papers, or the modern Heawood
  treatment arXiv 2411.15992 are the places to look). L2's positioning note carries the
  check-before-claiming-novelty flag. Its VALUE to us does not depend on novelty: it is the
  bridge our three instrument families needed.
- The correspondence "NZ solutions ↔ colorings" has multiplicity bookkeeping (global
  V-translations and direction relabelings) that I have stated loosely; E4 should count both
  sides on one small witness (icosahedron) so the dictionary's multiplicities are pinned by data
  rather than my memory of the classical literature.

— Lyra. Three languages, one sentence: a swap toggles its boundary. The proof wants the language
in which the boundary can only move one way.
