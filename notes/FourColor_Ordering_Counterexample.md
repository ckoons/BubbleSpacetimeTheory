---
title: "Decisive Negative: the Path-Link ≤5 Reduction Does Not Tile Four-Color"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "NEGATIVE RESULT (decisive, verified). The degree-<=5 path-elimination ordering does NOT exist: there is a valid simple triangulated disk with EVERY boundary vertex of degree >=6 (an explicit stacked/Apollonian disk, all boundary degree 7). Hence the path-deg-<=5 analysis is NOT a reduction of the four-color theorem. The configurations Euler guarantees are degree-<=5 vertices with CYCLE links (and min-degree-5 triangulations have no path links at all). The path case is a genuine but special configuration class. This corrects the reduction claim throughout."
related: ["notes/FourColor_Path_Reduction_Paper.md","notes/FourColor_Minimal_Linear_Representation.md","play/fourcolor_ordering_counterexample.py"]
---

# The reduction does not tile four-color (verified)

The referee's hinge — does a degree-≤5 path-elimination ordering always exist? —
resolves **no**, with an explicit, validated counterexample.

## The counterexample

A **stacked (Apollonian) triangulated disk** inside triangle `{0,1,2}`, built by
inserting vertices into faces incident to the corners:

- valid simple planar triangulated disk: `V−E+F = 2`, max edge multiplicity 2,
  boundary a single 3-cycle `{0,1,2}`;
- **boundary degrees 8, 7, 7 — all ≥ 6**; no degree-≤5 boundary vertex exists;
- the low-degree vertices (degree 3) are all **interior**, with **cycle** links.

(`play/fourcolor_ordering_counterexample.py`, 5/5.) So a degree-≤5 *path*-link
elimination ordering is impossible for this disk. Equivalently, in the incremental
(de Fraysseix–Pach–Pollack) coloring, the back-degree (stuck-path length) is forced
above 5.

## Why this is fatal to the reduction claim

- Euler guarantees a degree-≤5 vertex, but it can be **interior**, where the link
  is a **cycle**, not a path. Stacked triangulations push all low-degree vertices
  inside and leave the boundary high-degree.
- **Min-degree-5 triangulations** (icosahedron and larger) are spheres with **no
  boundary at all** — every degree-5 vertex has a 5-**cycle** link. The path-link
  analysis has nothing to act on.
- A single degree-5 vertex with a 5-cycle link is exactly the Heawood/Birkhoff hard
  case and is **not** reducible alone (this is the core difficulty of four-color).

So the path-deg-≤5 results characterize a **special configuration class** (boundary
path-links of length ≤5) that **does not tile** general planar triangulations. They
are not a reduction of the four-color theorem.

## What remains true (and what must be re-labeled)

Still correct and self-contained:

- the `F_4 = AGL(2,2)` linear/cut-space model of Kempe freeing (any link);
- the **path-deg-≤5** realizability characterization (104 types), its completeness
  (Jordan + Kempe separation), the 7-residual / 2-code decomposition, and the
  "freedom always exists" escape-margin result — all **about path-links**.

Must be re-labeled (claims to retract/soften):

- "reduction of four-color", "near-proof", and "four-color in human focus" — the
  path reduction does **not** reach all triangulations.
- The honest description is: *a complete linear-algebra / coding analysis of the
  boundary path-deg-≤5 Kempe-freeing configuration class*, not a reduction of the
  theorem.

## The honest path forward (if continued)

The reduction that **does** tile four-color removes a degree-≤5 vertex of the
triangulation; its link is a **cycle**. The genuinely valuable redirection is to
apply the same `F_4`/cut-space linear model to the **cycle-deg-5** case — but that
is the Heawood-hard case, single-vertex-irreducible, where Appel–Haken/Birkhoff use
larger reducible configurations. The linear lens may illuminate it; it will not
trivialize it.
