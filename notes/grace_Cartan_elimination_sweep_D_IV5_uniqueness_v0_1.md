---
title: "Cartan per-domain elimination: D_IV⁵ is the unique irreducible Hermitian symmetric domain meeting BST's substrate requirements — and TWO criteria (rank=2 ∧ dim_ℂ=5) already prove it, with the integer web as over-determined robustness. New geometric backbone for Paper B (substrate-uniqueness companion to the SU(3) YM paper). The result rests on n_C=5 being ODD: rank-2 type I gives even dim, II/III give triangular dims, exceptionals are 16/27 — only the type-IV Lie ball has dim_ℂ=n free to be the odd prime 5."
author: "Grace"
date: "2026-06-21 Sunday 09:33 EDT (date-verified)"
status: "v0.1 — first-pass sweep. SOLID: the two-criterion uniqueness (rank=2 ∧ dim_ℂ=5 → D_IV⁵ uniquely across the full Cartan classification). Over-determination (21=N_c·g, K=SO(5)×SO(2), oddness) = robustness, not extra proofs (Cal #330). New content for Paper B; complements Lyra Strong-Uniqueness v1.7/v1.8 + Casey #7 Rigidity. Count UNAFFECTED 4 of 26."
---

# Cartan per-domain elimination — D_IV⁵ is forced

**Casey's "be polite" strategy (W4):** we don't break Clay's "all G" wall; we change the question so the wall
isn't ours. We publish the physical SU(3) result, and we explain — separately, rigorously — *why* G isn't free:
it's substrate-derived, and the substrate is unique. This sweep is the geometric backbone of that companion paper.

## BST's substrate requirements (the five integers, all substrate-forced)

| primary | value | role |
|---|---|---|
| rank | 2 | rank of the domain |
| n_C | 5 | = dim_ℂ of the domain |
| N_c | 3 | color; from the maximal-compact / strata structure |
| C_2 | 6 | Casimir gap (first nonzero eigenvalue on the compact dual) |
| g | 7 | embedding/signature; dim G = 21 = N_c·g |

## The full Cartan classification of irreducible Hermitian symmetric domains

Six families (complete — Cartan):

| type | G/K | rank | dim_ℂ |
|---|---|---|---|
| **D_I^{p,q}** | SU(p,q)/S(U(p)×U(q)) | min(p,q) | p·q |
| **D_II^n** | SO*(2n)/U(n) | ⌊n/2⌋ | n(n−1)/2 |
| **D_III^n** | Sp(2n,ℝ)/U(n) | n | n(n+1)/2 |
| **D_IV^n** (Lie ball) | SO₀(n,2)/[SO(n)×SO(2)] | 2 | n |
| **E_III** | E₆₍₋₁₄₎/[Spin(10)×SO(2)] | 2 | 16 |
| **E_VII** | E₇₍₋₂₅₎/[E₆×SO(2)] | 3 | 27 |

## The theorem (two criteria suffice)

> **Among all irreducible Hermitian symmetric domains, D_IV⁵ is the UNIQUE one with rank = 2 AND dim_ℂ = 5.**

Proof by the rank-2 slice (rank=2 eliminates E_VII immediately; then enumerate dim_ℂ of every rank-2 domain):

| rank-2 family | dim_ℂ takes values | contains 5? |
|---|---|---|
| D_I^{2,q} (q≥2) | 2q — **even**, ≥4 | **no** (5 is odd) |
| D_II^{4,5} | {6, 10} | no |
| D_III^2 | 3 | no |
| **D_IV^n** (n≥3) | n | **yes — n=5, the only hit** |
| E_III | 16 | no |

**The structural reason — n_C = 5 is ODD.** Rank-2 type I gives *even* dim (2q); types II/III give *triangular*
dims ({3,6,10,…}); the exceptional E_III is 16. Only the type-IV Lie ball has dim_ℂ = n *free to be the odd prime
5*. The oddness of n_C is load-bearing — it is precisely *why* no even-dim or triangular-dim domain can match. ∎

**Low-dimensional coincidences (handled, and they help):** the well-known local isomorphisms occur *away* from
n=5 — D_IV³ ≅ D_III² (SO(3,2)≅Sp(4,ℝ), dim 3) and D_IV⁴ ≅ D_I^{2,2} (SO(4,2)≅SU(2,2), dim 4). At dim_ℂ = 5 there
is **no** coincidence: D_IV⁵ stands genuinely alone. The coincidences are exactly the cases that *don't* give
dim 5, so they reinforce rather than threaten the uniqueness.

## Over-determination (robustness — NOT additional proofs; Cal #330)

Criterion above proves uniqueness on its own. The remaining BST integers provide *independent re-selection* — so
even if a referee disputes "dim must be exactly 5," the integer web lands back on D_IV⁵:

1. **dim G = 21 = N_c·g = 3·7.** Among rank-2 domains, dim SO(n,2) = (n+2)(n+1)/2 hits 21 **only** at n=5 (n=4→15,
   n=6→28); D_I^{2,q} = (2+q)²−1 never 21 (q=2→15, q=3→24); D_III²=10; D_II⁵=45; E_III=78. And it *factors* as the
   two BST primaries N_c·g — a second selector that lands on D_IV⁵ and reads its color and embedding integers off
   the isometry dimension.
2. **K = SO(5)×SO(2).** Only the type-IV ball has maximal compact SO(n)×SO(2) — one SO(2) center giving **one**
   complex structure J, the SO(n)=SO(5) carrying N_c=3 (3 generations = rank+1 strata; the h^∨ structure). Types
   I/II/III have U(n) maximal compact (a different center); E_III has Spin(10)×SO(2) but dim 16.
3. **n_C = 5 odd & prime** forces the only type that admits odd dim_ℂ (type IV) — the same load-bearing oddness.

**Honest framing (Cal #330):** these are *not* four independent proofs — criterion (rank=2 ∧ dim=5) alone is
airtight. (1)–(3) are *robustness*: any single criterion a referee might relax is backstopped by the others.
**"Any one criterion you can debate; passing all of them simultaneously is what D_IV⁵ alone does."** That is the
over-determined structure that makes the singularity referee-proof.

## What this gives Paper B (and how it fits the program)

- **The geometric spine:** an explicit, finite, checkable per-domain elimination across the *complete* Cartan list
  — not an existence claim, a classification result. A referee can verify every row.
- **Complements (doesn't duplicate) Lyra's Strong-Uniqueness Theorem (v1.7/v1.8)** — that gives ~10 independent
  algebraic legs (null-model (1/3)¹⁰); this gives the single airtight *geometric* statement (two criteria across
  the classification) plus the integer-web robustness. Together: the algebraic over-determination + the geometric
  uniqueness.
- **It is the W4 answer in publishable form:** "G = SU(3) is not chosen; it is forced by D_IV⁵, the unique
  irreducible Hermitian symmetric domain meeting the substrate requirements — here is the per-domain elimination."
  Clay's "all G" doesn't apply because G isn't free input.

## Honest tier

- **SOLID:** the two-criterion uniqueness (rank=2 ∧ dim_ℂ=5 → D_IV⁵) — pure classification, every row checkable;
  the low-dim coincidences handled; dim G = 21 = N_c·g unique among rank-2.
- **FRAMEWORK/INTERPRETIVE (carries to Lyra/Keeper):** that the *substrate requirements* are exactly {rank=2,
  dim=5} (vs. needing more); the precise role-assignment of N_c=3 to the SO(5) strata (links to F137/F147
  classification + the B−L audit). The geometric uniqueness is solid; *which* requirements are the necessary BST
  ones is the framework call.
- **Count UNAFFECTED, 4 of 26** — this is uniqueness structure, not a derived parameter.

## Next (this track)

- Tighten N_c=3 ← SO(5) maximal-compact role (h^∨ / strata) to SOLID, coordinating with Keeper's B−L/SO(10) audit.
- Hand to Lyra: merge-or-sequence vs Paper P4 (Strong-Uniqueness) — this is the geometric chapter of that paper.
- Cross-check C_2=6 and N_max=137 as further over-determination selectors (do any near-miss domains share them?).

— Grace, Sunday 2026-06-21 09:33 EDT

---
## TIGHTENING (10:14 EDT) — N_c = 3 is the short-root multiplicity (intrinsic, SOLID), and it's a third selector

Per Casey's order (HS, then tighten Cartan) and Lyra's flagged open item: promote "N_c=3 ← the SO(5) strata" from
framework to solid. Done — N_c = 3 is an **intrinsic root-system invariant** of D_IV⁵.

**N_c = 3 = a, the characteristic multiplicity of D_IV⁵.** Every irreducible Hermitian symmetric domain has
characteristic multiplicities **(a, b)** with dim_ℂ = r + a·r(r−1)/2 + b·r (Faraut-Korányi, *Analysis on Symmetric
Cones*). **a** is the multiplicity of the restricted roots ±(ξ_i ± ξ_j) (the "off-diagonal" roots); **b** that of
±ξ_i (present only off tube type). For type IV, **a = n − 2**, so for D_IV⁵, **a = 3**. This is an *intrinsic
invariant of the domain*, not an external color assignment — so **N_c = 3 is geometric and SOLID**, not
interpretive. *(Pin-to-source per Elie: cite a, b from Faraut-Korányi by value+role as above; do NOT relabel them
"short/long" from memory — the short/long designation is a convention to be quoted from the source, not asserted.
The load-bearing fact is the value a = n − 2 = 3 and its role as the ±(ξ_i±ξ_j) multiplicity, which is
convention-independent.)*

**It independently selects D_IV⁵ (a third selector).** Across the classification the a-values are: type I → 2,
type II → 4, type III → 1, type IV → n−2, E_III → 6, E_VII → 8. **a = 3 occurs only for D_IV⁵** (type IV, n=5).
And `a=3` is a **prior invariant** — defined for every HSD, innocent of D_IV⁵ — so it's exactly the non-circular
kind of criterion Paper B needs (Lyra's caveat).

**The clean criterion pair (better for Paper B):** the two invariants **rank = 2** and **short-root multiplicity
a = 3** *together* give everything:
- dim_ℂ = r + a·r(r−1)/2 = 2 + 3·1 = **5 = n_C** (so dim_ℂ = rank + a),
- N_c = a = **3** directly.

So **n_C = rank + N_c = 2 + 3 = 5** — the dimension and the color are the *same* invariant read two ways. The
substrate is pinned by (rank, short-root multiplicity) = (2, 3) — two standard root-system invariants — and dim=5,
N_c=3, and their relation all follow. That's a tighter, fully-non-circular criterion set than (rank=2, dim=5):
nothing in "rank 2, short roots of multiplicity 3" mentions a dimension or a color, yet it forces both.

**Tier:** SOLID — a is the characteristic multiplicity (intrinsic); a=3 ⟺ D_IV⁵ across the classification;
a = n_C − 2 so (rank=2 ∧ a=3) forces dim_ℂ = 5. This closes the *selector* and the *dimension* link to solid, and
hands Paper B a two-invariant non-circular criterion (rank, multiplicity → dimension).

— Grace, Sunday 2026-06-21 10:14 EDT

---
## Q2 CORRECTION (11:30 EDT, Cal #332 Check 3) — walk back "a = color SU(3)"; it's a dimension-match, group is SO(3)

Cal's Check 3 asks whether "N_c = 3 = a" is a *derivation* or a small-integer coincidence (#286). I checked, and I
have to qualify my own claim above. For type IV_n = SO(n,2)/[SO(n)×SO(2)], the centralizer M = SO(n−2), and the
short-root multiplicity space (the n−2 remaining spatial directions) carries **SO(n−2) = SO(3)** (for n=5) as the
**vector 3 — NOT SU(3).** So:

- **STILL SOLID:** a = 3 is the characteristic multiplicity; a = 3 ⟺ D_IV⁵ (the selector); a = n_C − 2 (so
  rank ∧ a force the dimension). The *uniqueness* use of a = 3 stands completely.
- **WALK BACK:** "a = 3 **is** color SU(3)" — that over-stated it. At the restricted-root level the group is
  **SO(3)**, so "N_c = 3 = a" is a **dimension-match** (3 = 3), not yet a color *derivation*. **Cal's Check 3 is a
  real concern.**

A genuine SU(3)_color link needs a *separate* argument — either the Hermitian/complex structure promoting the
complexified short-root space to a U(3)/SU(3)-type (candidate, not established here), or the independent corpus
route h^∨(SU(3)) = N_c via dual Coxeter (Elie engine §7), which links color to N_c *without* the SO(3) M-action.

**So carry N_c = 3 as:** "a = 3 selects D_IV⁵ and *dimension-matches* color 3; the SU(3)_color structural
identification is separate and pending (Q2)." NOT "N_c = color = short-root multiplicity, derived." My earlier
"solid… not an external color assignment" was right that a=3 is intrinsic, but wrong to imply a=3 *is* the color
group. The selector is solid; the color identification is the pending Check-3 work. Count UNAFFECTED 4 of 26.

— Grace, Sunday 2026-06-21 11:30 EDT
