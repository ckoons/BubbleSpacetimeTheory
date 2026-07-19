# F603 — Pinned the condensate direction O by hand: it's the SO(5) VECTOR (1,0)=5 (the Higgs bi-doublet), spherical/boundary-reaching. The top is the SPINOR (½,½)=4. The Yukawa is the γ-matrix vertex 4⊗4→5, and O is a NON-stretched branch — so y_t=1 is NOT forced by the angular CG. y_t reduces to the top's RADIAL overlap with the boundary condensate. Blocked on the June discrete-series address, but the direction is now pinned.

**Lyra, Sun 2026-07-19. Lead: pin O's K-type direction non-circularly, then compute ⟨t|O⟩.** Did the first half by hand — O's direction is pinned from its quantum numbers alone. The result sharpens y_t=1 to a single radial-overlap question and confirms it's not automatic.

## Pinned (non-circular — from O's quantum numbers, independent of the fermions)
Under K=SO(5)×SO(2), with SO(5)=Sp(4) ⊃ Sp(1)_L×Sp(1)_R = SU(2)_L×SU(2)_R:
- **vector 5 = (1,0) = (2,2) ⊕ (1,1)** [bi-doublet + singlet]
- **spinor 4 = (½,½) = (2,1) ⊕ (1,2)** [L-doublet + R-doublet]

The Higgs condensate O is **color-singlet, SU(2)_L doublet, Y=½** — i.e. the **(2,2) bi-doublet**, which lives in the **VECTOR (1,0) = 5**. So:
$$ \boxed{\;O \sim \text{SO(5) vector } (1,0)=5,\quad \lambda_2 = 0 \Rightarrow \textbf{spherical} \Rightarrow \text{reaches the Shilov boundary.}\;} $$
**This is consistent and non-circular:** O being a *boundary* condensate ⟺ O spherical (λ₂=0, F587) ⟺ O in the vector — all forced by "color-singlet SU(2)_L-doublet Y=½," not by making the top parallel. O's direction is pinned. ✓ (SO(2) weight = the hypercharge/S¹ winding.)

The top:
- **top_L** ∈ Q_L = (t,b)_L (SU(2)_L doublet, SU(2)_R singlet) = (2,1) ⊂ **spinor (½,½)=4**, λ₂=½ (non-spherical).
- **top_R** = t_R (SU(2)_L singlet, T₃_R=+½) = (1,2) ⊂ **spinor (½,½)=4**, λ₂=½ (non-spherical).

## The Yukawa is the γ-matrix vertex, and O is NOT the stretched branch
The mass term Q̄_L Φ t_R needs 4⊗4 ⊃ 5 (=O). Check: **4⊗4 = 1 + 5 + 10** (Sp(4): antisym 6=[1+5], sym 10=adjoint) — contains the 5. The coupling exists, and it's the **standard γ-matrix vertex** Q̄_L γ^a t_R Φ_a. But:
$$ \text{stretched}(4\otimes4) = (\tfrac12,\tfrac12)+(\tfrac12,\tfrac12) = (1,1) = 10\ (\text{adjoint}),\quad \textbf{not the 5}. $$
So **O = (1,0)=5 is a NON-stretched branch of 4⊗4.** The stretched (CG=1, maximal) coupling would be to the adjoint 10, not to the Higgs vector 5. Therefore:
$$ y_t = \underbrace{(\text{$\gamma$-vertex CG for the 5-branch})}_{O(1),\ \text{not }1} \times \underbrace{(\text{RADIAL overlap of the top mode with the boundary condensate }O)}_{\text{the open piece}}. $$
**y_t = 1 is NOT forced by the angular CG** — the angular part is a non-maximal γ-vertex coefficient, so reaching y_t=1 would require the radial overlap to conspire. This is *evidence that y_t=1 is not kinematic* (consistent with the observed 0.992 being near-but-not-exact), and it's the linear-algebra confirmation of the SUPPORTED tier.

## Keeper's tension is real and it's the radial-overlap question
Keeper flagged: O is a *ground* boundary condensate, the top is the *outermost* gen-3 mode — do they overlap? Now precise: **O is spherical (λ₂=0, boundary-reaching); the top is non-spherical (λ₂=½).** They live at different "λ₂ addresses," so their **radial overlap is not maximal by default** — it's set by how much the non-spherical top mode reaches the spherical boundary where O lives. That radial overlap is exactly y_t (up to the γ-CG), and computing it needs the **discrete-series address** of the top mode (which discrete (a,b) the top sits at) — **the sharply-pinned open core flagged back in June.**

## Verdict
- **O's DIRECTION: PINNED (non-circular)** — SO(5) vector (1,0)=5, spherical, boundary-reaching, = the Higgs bi-doublet. This is the vector Casey asked to pin, and it's forced by quantum numbers. ✓ **Genuine progress — the blocker named in F602 is half-resolved.**
- **top K-types: PINNED** — spinors (½,½)=4 (top_L=(2,1), top_R=(1,2)), non-spherical.
- **Yukawa = γ-vertex 4⊗4→5; O is the non-stretched branch** → y_t = γ-CG × radial overlap; **y_t=1 NOT forced by angular CG.**
- **y_t = 1: reduces to the top's RADIAL overlap with the spherical boundary O** — SUPPORTED, and now *evidence-against-kinematic* (the angular CG is sub-maximal). Blocked on the discrete-series address (June open core), NOT on O's direction (pinned).
- **The 0.992: reads as the top's near-but-not-full radial reach to the boundary** — a small deficit, consistent with non-spherical top not *quite* saturating the spherical boundary overlap.

## Handoffs
- **@Casey** — O's direction is pinned by hand: the vector (1,0)=5, spherical. The remaining crux is the *radial* overlap of the non-spherical top with the spherical boundary condensate — that's where your geometric intuition helps (does the outermost gen-3 mode reach the boundary where O sits, and does it saturate?). Computing it needs the top's discrete-series address (the June open core) — worth reasoning through together.
- **@Elie** — verify: 4⊗4=1+5+10 (5=O present, coupling exists); O=5 is the non-stretched branch (stretched=10 adjoint); so y_t = γ-CG × radial overlap, NOT forced to 1 by angular CG. The γ-vertex CG for the 5-branch is a clean number — compute it (it's the angular ceiling of y_t before the radial factor).
- **@Keeper** — your ground-vs-outermost tension is exactly the λ₂-mismatch (O spherical λ₂=0 vs top non-spherical λ₂=½); y_t=1 is the radial overlap across it, SUPPORTED, blocked on the discrete-series address (not O's direction — that's pinned). Bank: O's K-type pinned (vector 5, spherical); y_t reduces to radial overlap; angular CG sub-maximal ⟹ evidence y_t=1 not kinematic.
- **@Cal** — O's direction is derived from quantum numbers (target-innocent, non-circular). y_t=1 stays SUPPORTED; the new evidence (O is the non-stretched branch) *weakly disfavors* exact y_t=1 as kinematic — the angular CG alone doesn't reach 1.

Notes only; no toys/theorems claimed. — Lyra
