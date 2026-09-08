# PRE-REGISTRATION — Toys 5729 (E1), 5730 (E2), 5731 (E3), Round 132. Hashed before any runs.

**Elie, 2026-09-08 (Tuesday) 09:30 EDT (shell-copied).**

## E1 — Toy 5729: 5726's chain under the (D) reset
The (D)-survivor of a word (z·z)^j Y_k is (z·z)^j ⟨Y_k, Z_k^ξ⟩ Z_k^ξ: zonal degree l = k, winding j unchanged. So at every stopping rule the (j,l) law is the (j,k) law with l ≡ k, and **H(j,l) = H(j) = 4.02 / 10.16 / 12.15 bits** (S-m137 / S-k68 / S-k137) — identical to (C)'s numbers, because k is a function of j at each stop. (D) adds the axis and the value of l; it adds no entropy at the stop.
- **H1 (hashed values):** norm fraction retained by the un-renormalized (D) projection for Haar-random Y_k: 1/dim H_k(S⁴) = 6/((2k+3)(k+1)(k+2)): **k = 68: 8.937 × 10⁻⁶; k = 137: 1.1292 × 10⁻⁶.** Verified by the Schur identity ∫|⟨gY, Z⟩|² dg = ‖Y‖²‖Z‖²/dim on random rotations (k = 2, 3, exact sphere integration, ≤ 3 % MC error).
- **H2 (hashed range, can fail):** chain-averaged retained fraction under S-m137 (k = 137 − 2j, E[j] ≈ 58): **between 10⁻⁴ and 10⁻³**; under S-k68: 8.94 × 10⁻⁶ exactly; S-k137: 1.13 × 10⁻⁶ exactly.
- **H3 (control):** a state prepared zonal along ξ retains fraction 1 at every k.

## E2 — Toy 5730: the Gram of (z·z)^j (z·ξ)^l on Š in the Hardy norm
On Š, z = e^{it}x: (z·z)^j (z·ξ)^l = e^{i(2j+l)t} x₁^l, so ⟨f_{jl}, f_{j'l'}⟩ = δ_{2j+l, 2j'+l'} · M₅(l + l'), M₅(n) = ∫_{S⁴} x₁ⁿ dσ. On the maximal polydisc (a, b), z·z = ab, z·ξ = (a+b)/2, and its torus T² ⊂ Š.
- **G1 (can fail):** restriction to the polydisc is NOT an isometry onto symmetric H²(T²): ‖z·ξ‖²_Š = 1/5 vs ‖(a+b)/2‖²_{T²} = 1/2. Control l = 0: both give 1 for every j.
- **G2 (hashed identity, can fail):** with a = e^{i(t+φ)}, b = e^{i(t−φ)}: x₁ = cos φ and |a − b| = 2|sin φ|, and the S⁴ marginal in x₁ is ∝ (1 − x₁²) dx₁ = sin³φ dφ, so **the Š Hardy norm on the (D)-survivor is the torus norm with weight |a − b|³**: ‖f‖²_Š = ∫_{T²} |f|² |a−b|³ / ∫_{T²} |a−b|³. Verified exactly on the Gram for m ≤ 6.
- **G3 (family, hashed):** for D_IV^n the weight is **|a − b|^{n−2}**: n = 2 (the bidisc itself, Š = T²) gives the SYMMETRIC pull-back convention; n = 4 gives the JACOBIAN-weighted |a−b|² convention (the antisymmetric isomorphism of arXiv 1511.08962); **n = 5 gives |a−b|³ — neither literature norm.** Verified exactly at n = 2, 3, 4, 5, 6 on the Gram for m ≤ 4.

## E3 — Toy 5731: the axis ratchet
Start the next cycle from the zonal Z_l^ξ; apply coordinate writes z_u; the light branch is harm(z_u Y), the matter branch is ∂_u Y (the winding factor stripped). Track the zonal weight along ξ, w = |⟨Y, Z⟩|²/(‖Y‖²‖Z‖²), exactly (sphere moments, rational u).
- **R1 (control, cannot fail):** writes along ξ (u = ξ) keep w = 1 on both branches at every step.
- **R2 (can fail, the direction hashed):** with random-direction writes the expected zonal weight along ξ **shrinks** monotonically with each write from Z₂ (6 writes, 24 random walks) and is **below 0.5 after 6 writes**; the imprint is not ratcheted by covariant writes — only axis-aligned writes carry it at full strength. The axis is carried as a label (R1), not as content (R2).

Score: E1 X/3 (H2 can fail), E2 X/3 (G1, G2, G3 can fail), E3 X/2 (R2 can fail).
