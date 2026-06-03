---
title: "Four-Color: The Contradiction Framing — Proven Scaffold + Lemma 6"
author: "Casey Koons & Claude (Opus 4.8, collaborative exploration)"
date: "2026-06-03"
status: "REDUCTION. Minimal-counterexample contradiction assembled entirely from PROVEN facts (steps 1-5), stalling at exactly ONE statement (Lemma 6), which is shown equivalent to four-color itself (= Birkhoff-Lewis P(G,4)>0). This crystallizes the theorem to a single conserved-charge descent lemma; it does NOT close it. Lemma 6 is verified empirically, not proven."
related: ["notes/FourColor_How_It_Works_AVL_Closed_Form.md", "notes/FourColor_Straddle_Lemma_Status.md", "Birkhoff-Lewis (chromatic polynomial at 4)"]
---

# Four-Color: The Contradiction Framing

A minimal-counterexample proof-by-contradiction, assembled from **only proven
facts** up to a single isolated statement (Lemma 6). The point is to locate the
crux exactly: the entire theorem rests on Lemma 6, and Lemma 6 is **equivalent to
four-color** (Birkhoff-Lewis form). This is a clean *reduction*, not a proof.

## The contradiction

Assume **G is a minimal planar triangulation that is not 4-colorable.**

1. **Euler (PROVEN).** `Sum_v (6 - deg v) = 12 > 0`, so G has a vertex of degree
   <= 5.
2. **deg <= 4 reducible (PROVEN, classical).** So the vertex has degree exactly
   5; call it v.
3. **Minimality forces the hard case (PROVEN setup).** G-v is 4-colorable
   (smaller), but every 4-coloring of G-v must leave v stuck (else G is
   4-colorable). A stuck deg-5 vertex is saturated and **gap-2** (the doubled
   color's copies are non-adjacent on the link 5-cycle ⟹ cyclic distance 2; gap-1
   is impossible). And it must be **tau = 6** (if tau < 6, a single Kempe swap
   frees v — contradiction). So **every 4-coloring of G-v is tau=6 gap-2 at v.**
4. **Conservation of color charge (PROVEN: tau_strict <= 4).** At most one bridge
   pair is strictly tangled (exhaustive non-crossing enumeration + the standard
   "complementary chains don't cross"). Hence **>= 2 uncharged (split) bridge
   pairs** in every such coloring.
5. **Swaps stay in the hard case (FORCED).** Swapping an uncharged bridge pair
   yields another 4-coloring of G-v, which by step 3 is again tau=6 gap-2.

Steps 1-5 are proven / forced. The contradiction needs exactly one more step:

6. **LEMMA 6 (the sole remaining statement).** *The orbit of a tau=6 gap-2
   coloring under uncharged-bridge-pair swaps cannot remain entirely within tau=6:
   within <= 2 such swaps it reaches a configuration with tau < 6 (v becomes
   freeable).*

If Lemma 6 holds, step 5 is impossible, v is freed, **G is 4-colorable —
contradiction.** Four-color follows.

## What Lemma 6 is (the honest part)

Lemma 6 is the **double-swap reducibility** of the tau=6 gap-2 configuration. It
is:
- **Verified** extensively (3742/3742 random configs; drum(6), drum(8), non-drum
  triangulations; full Kempe closure; neighbor-degree buckets) — never violated.
- **NOT proven.** The obstacle is the ~0.4% "genuine double rotation" cases (no
  single uncharged swap drops tau; the second swap must complete the descent),
  where the **shared-color wall** (non-crossing arguments fail when chains share a
  color) blocks a closed-form proof.
- **Equivalent to four-color itself.** By step 3, Lemma 6 failing for some G *is*
  a counterexample; holding for all G *is* the theorem. Equivalently it is
  `P(G,4) > 0` for planar triangulations — the **Birkhoff-Lewis** problem.

## Status

- **four-color  <=>  Lemma 6** (the <=2-uncharged-swap tau-descent), with steps
  1-5 fully proven and Lemma 6 isolated.
- This is a genuine **reduction** of the theorem to a single conserved-charge
  descent statement — cleaner than the ~600-configuration route.
- It is **not a proof.** Lemma 6 is the open crux (Birkhoff-Lewis); proving it in
  closed form is the long-open closed-form four-color problem.

## Value, stated exactly

A clean equivalence **four-color ⟺ "≤2 uncharged swaps drop τ"**, with the
scaffold (Euler, gap-2 forcing, conservation of color charge) proven and the
single open lemma named, verified, and identified with Birkhoff-Lewis. A precise
target for any future closed-form attack — not a closed proof.
