# Figure spec — the B₂ root diagram (flagship §1, "the object and the seed")

*Grace | round 5 | 2026-07-18. Specs the flagship's root-diagram figure. It's linear algebra all the way down (Casey's steer): the BST seed IS a rank-2 root system — 8 vectors in a plane, the Weyl group = reflections, the primaries = the root-system invariants. Rendered asset: `notes/BST_B2_root_diagram_figure1.png` (matplotlib, 140dpi). Keeper: confirm design; drop under §1 Figure 2 (Fig 1 = the family tree).*

## What the figure IS (one line)
The Standard Model's "underlying symmetry," drawn: the **B₂ = SO(5) root system** — a rank-2 root system, 8 roots in a 2D plane. Being rank-2, it admits **no grand-unified extension** (the falsifiable core of §8).

## The linear algebra (exact coordinates)
- **8 roots** in ℝ² (the rank-2 Cartan):
  - **4 long roots** (blue): ±e₁±e₂ = (1,1), (1,−1), (−1,1), (−1,−1).
  - **4 short roots** (orange): ±e₁, ±e₂ = (1,0), (−1,0), (0,1), (0,−1).
- **Simple roots:** α₁ = (1,−1) [long], α₂ = (0,1) [short] → B₂ Dynkin diagram (double bond α₁⇐α₂). **rank = 2 = the number of simple roots = the seed.**
- **Weyl vector** ρ = ½·Σ(positive roots) = **(3/2, 1/2)** = the *compact* ρ_SO(5) — marked in red. Note λ₂ = ½ > 0 (see Shilov note).
- **Weyl group** W(B₂) = the dihedral group of order 8 (reflections in the roots) — the symmetries of the diagram.

## The BST annotations (the primaries ARE the root-system invariants)
Overlay these labels so a reader sees the physics inside the linear algebra:
- **rank = 2** — the 2 simple roots / the dimension of the plane (**the seed**).
- **N_c = 3** — the **root multiplicity** (a = n−2 for SO(n), n=5): color is not inserted, it's how many times the fundamental root repeats (F579).
- **ρ_conformal = (n_C/rank, N_c/rank) = (5/2, 3/2)** — the BST conformal ρ (vs the compact ρ=(3/2,1/2) shown); its direction sets the V_cb / τ-address angle.
- **The V_cb angle** ψ = arctan(N_c/n_C) = **30.96°**, cos ψ = 5/√34 (F379/F384) — draw the ρ_conformal direction as a dashed ray, angle-labeled.
- **The Shilov-vanishing axis:** an SO(5) K-type is labeled (λ₁, λ₂); by the round-4 theorem its Shilov-boundary value vanishes **iff λ₂ > 0 (non-spherical)**. The λ₂ direction is the short-root (e₂) axis. Shade the λ₂>0 half as "non-spherical / zero boundary support (confinement, m₁=0 engine)" vs λ₂=0 "spherical / reaches the boundary (emitted)." This is the linear-algebra picture of the master mechanism.

## Caption (draft, for §1)
> **Figure 2. The rank-2 root system B₂ = SO(5) — the BST seed.** The eight roots (long ±e₁±e₂, short ±e₁,±e₂) of the domain's restricted root system. The five BST integers are its invariants: rank = 2 (simple roots), N_c = 3 (root multiplicity), and the Weyl vector ρ. The conformal ρ = (5/2,3/2) direction (dashed) sets the τ-generation address and the V_cb angle (30.96°, cos = 5/√34). The short-root (λ₂) axis is the spherical/non-spherical divide of the round-4 Shilov theorem: K-types with λ₂ > 0 have zero Shilov-boundary value (confinement, m₁=0 engine). Being rank-2, this root system admits no grand-unified extension — the framework's central falsifiable prediction.

## Render notes (for a publication-grade version)
- Current asset (`BST_B2_root_diagram_figure1.png`) has the 8 roots + ρ + simple-root labels. To finalize: add the dashed ρ_conformal ray + angle arc (30.96°), the λ₂>0 shading, and the rank/N_c/multiplicity call-outs. TikZ (pgfplots) is the paper-grade route; the matplotlib PNG is the working proof.
- Pairs with **Figure 1** (the generative family tree, §1) — Fig 1 is the *arithmetic* (2 grows the integers), Fig 2 is the *geometry* (the integers are one root system). Together they are the §1 "object and seed."

— Grace, 2026-07-18. B₂ root-diagram figure spec + rendered PNG asset. The seed is a rank-2 root system; the primaries are its invariants; the short-root axis is the Shilov spherical/non-spherical divide. Linear algebra, drawn.
