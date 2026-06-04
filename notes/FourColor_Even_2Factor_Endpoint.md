---
title: "The Irreducible Endpoint: Four-Color = Even 2-Factor Existence"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "ENDPOINT (characterization verified). The flow/Penrose track terminates at: a cubic graph is 3-edge-colorable <=> it has a 2-factor of all even cycles. So four-color (flow form) <=> every bridgeless planar cubic graph has an even 2-factor. The provable sufficient conditions (Hamiltonian, bipartite, scaling-reducible, and their move-closure) are exactly the easy ways to produce an even 2-factor; beyond them, finding one IS colorability -- the irreducible, four-color-equivalent core where the Appel-Haken reducible-configuration machinery is needed. This is where it becomes irreducible."
related: ["notes/FourColor_NonVanishing_Class.md","notes/FourColor_Move_Calculus.md","notes/FourColor_Narrowed_Core.md","play/fourcolor_even_2factor.py"]
---

# Where it goes: the irreducible endpoint

Pushing the provably-non-vanishing class to its limit lands on one clean
characterization, and that is the natural terminus of the whole flow/Penrose track.

## The characterization (verified)

> **A cubic graph is 3-edge-colorable ⇔ it has a 2-factor of all even cycles.**

Equivalently: a perfect matching whose complement (a 2-regular spanning subgraph)
has only even cycles — the matching is color 3, the even 2-factor is 2-colored.
(Verified colorable ⇔ even-2-factor on K4, prism, cube; `play/fourcolor_even_2factor.py`.)

Hence the flow form of four-color is:

> **Four-color ⇔ every bridgeless planar cubic graph has an even 2-factor.**

This is the cleanest combinatorial statement the track produces: pure
matching/2-factor parity, no signs, no embeddings.

## The provable class is "easy even 2-factors"

Every sufficient condition we proved is just an easy way to exhibit an even 2-factor:

- **(H) Hamiltonian** — a Hamilton cycle (even, since cubic ⇒ even order) is itself an
  even 2-factor.
- **(B) bipartite** — every cycle is even, so *any* 2-factor is even; a perfect
  matching exists, so an even 2-factor does.
- **(S) scaling-reducible** — `R1–R4` reduce `G` to a Hamiltonian/bipartite graph.
- **Move-closure** — any `G` that reduces by `R1–R4` to an (H)/(B) graph.

This class is large; by four-color it is *everything* (planar) — but the easy
witnesses run out exactly when no Hamilton cycle, no bipartiteness, and no scaling
reduction is available.

## Where the easy witnesses stop (the irreducible core)

Beyond the provable class, exhibiting an even 2-factor **is** deciding
colorability. For planar cubic graphs the first cases with no easy witness are the
**non-Hamiltonian** ones (Tutte's 46-vertex 3-connected planar cubic graph is the
classical small example) and the high-girth, cyclically-5-connected graphs
(dodecahedron and up). On these:

- no scaling move fires (they are core graphs);
- there is no Hamilton cycle and no bipartiteness to hand you the 2-factor;
- so an even 2-factor must be *found*, which is the four-color-equivalent core —
  precisely the territory of the **Appel–Haken reducible-configuration +
  unavoidability** machinery.

## The honest terminus

The track has done exactly what it set out to: it carried four-color, in three
faithful languages (flows / `SO(3)` / matchings), down to **one irreducible,
four-color-equivalent statement — every bridgeless planar cubic graph has an even
2-factor** — with everything around it proven:

- the reset and equivalences (verified),
- the narrowing `R0–R4` (proven),
- the scaling vs binor move calculus (computed; scaling = non-vanishing-preserving
  and exhaustive-to-core),
- the provable non-vanishing class (H/B/S, proven),
- and the honest negative (no single-binor-step positivity; the minus is real).

What remains is **irreducible**: the even-2-factor existence on rigid core graphs,
equivalent to four-color, where no further honest reduction is available and the
computer-assisted reducibility method is the known route. This is the wall, named
precisely — and the map to it is complete.
