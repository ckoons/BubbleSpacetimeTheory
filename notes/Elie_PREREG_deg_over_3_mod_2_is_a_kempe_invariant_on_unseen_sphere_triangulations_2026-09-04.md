# Pre-registration — is deg/3 mod 2 a Kempe invariant on the sphere lane? (toy 5671)
**Elie, 2026-09-04 11:59 EDT (`date` before this line). The pattern is POST-HOC on the C₆₀ dual (5670: deg mod 6 constant on all 52 classes); this file predicts it on graphs I have not computed classes for, before running.**
**Objects.** Sphere triangulations with odd vertices, 5-connected: plantri -c5 **n = 17, 18, 19** (all graphs, all colourings mod S₄, cap 20,000 per graph) and the fullerene duals of **C₇₀, C₇₂, C₇₈, C₈₄** (fullgen, dual planar code, the 5644 instrument). None has had its Kempe classes computed by me. Classes: union-find over every move of every pair and component, on colourings mod S₄ (Mohar–Salas's convention), the 5670 code path unchanged.
**Hashed lines.**
(P1) **On every graph, deg ≡ 0 (mod 3) for every colouring.** (Fisk's Prop. 3.2 needs a 3-colourable base and these are not; on the C₆₀ dual it held with degrees −6, −3, 0, 3, 6, and on plantri n = 12…16 it FAILED — degrees −5, −4, −1, 1 occur — so I predict: **it holds exactly on the fullerene duals (k = 12, all odd vertices of degree 5) and fails on the plantri graphs with any other odd-degree profile.** Kill either half.)
(P2) **deg mod 6 is constant on every Kempe class of every fullerene dual tested** (C₇₀, C₇₂, C₇₈, C₈₄). Kill: one class carrying two values of deg mod 6.
(P3) **On the plantri graphs where P1 fails, the right statement is deg mod 2** — i.e. Tutte's parity (deg ≡ Σ_{f(x)=a} ρ(x) mod 2) — **is constant on every Kempe class**, and deg mod 4 is not. Kill: either half.
(P4) **κ > 1 on every graph tested** (the sphere lane is never one component once there are odd vertices). Kill: one graph with κ = 1 — n = 16 g2 already gives one, so this is predicted to FAIL and is written to be scored, not to be safe: I expect κ = 1 to occur again.
**Controls in the same run:** the C₆₀ dual reproduces κ = 52 and its 21/31 split; the octahedron κ = 1.
— Elie
