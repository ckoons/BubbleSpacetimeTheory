# Grace — G16 (Round 122): the coordinate table. Lyra's polydisc coordinates (along the strongly orthogonal roots) vs toy 5706's e-coordinates, with both reflections' actions in both. One page; the trap Keeper fell into in Round 120, closed as a table. 2026-09-06 15:5x EDT. Source of the numbers: `play/.out_5706.txt` (toy 5706, so(5,2) diagonalised on the matrix algebra); conventions: Helgason Ch. X Table VI (B₂, m(±e_i) = 3, m(±e₁±e₂) = 1); Lyra L2 §1–2.

## The two coordinate systems on 𝔞* ≅ ℝ²
- **e-coordinates** (t₁, t₂): the eigenvalues of ad(t₁H₁ + t₂H₂), H_i the boost mixing space direction i with time direction i — the coordinates in which the restricted roots are ±e_i (multiplicity **3**) and ±e₁ ± e₂ (multiplicity **1**). Toy 5706 computed them.
- **polydisc (γ-) coordinates** (μ₁, μ₂) := (t₁ + t₂, t₁ − t₂): the coordinates along the two STRONGLY ORTHOGONAL roots γ₁ = e₁ + e₂, γ₂ = e₁ − e₂ (multiplicity-1 roots), which are the axes of the maximal polydisc Δ² ⊂ D_IV⁵ (Polydisc Theorem; Lyra L2 §1). The functional equation of ζ lives on each μ_i separately (Lyra L1: the multiplicity-1 factor c_{e₁−e₂}(λ) = ξ(μ₂)/ξ(μ₂ + 1)).
- Inverse map: t₁ = (μ₁ + μ₂)/2, t₂ = (μ₁ − μ₂)/2. The map is the Hadamard matrix [[1,1],[1,−1]]: it EXCHANGES the roles of "negate one coordinate" and "exchange the coordinates" — which is the whole trap.

## The four reflections of W(B₂), each in both systems (verified numerically in 5706 at t = (1, 0.37) ↦ μ = (1.37, 0.63))

| reflection | root | multiplicity | in e-coordinates (t₁, t₂) ↦ | in polydisc coordinates (μ₁, μ₂) ↦ | what it IS |
|---|---|---|---|---|---|
| s_{e₁−e₂} | e₁ − e₂ = γ₂ | **1** | (t₂, t₁) — EXCHANGES | (μ₁, −μ₂) — NEGATES μ₂ | **functional equation of the second polydisc factor** (μ₂ ↦ −μ₂ = s ↦ 1 − s there) |
| s_{e₁+e₂} | e₁ + e₂ = γ₁ | **1** | (−t₂, −t₁) — exchanges and negates both | (−μ₁, μ₂) — NEGATES μ₁ | functional equation of the first factor |
| s_{e₂} | e₂ | **3** | (t₁, −t₂) — NEGATES t₂ | (μ₂, μ₁) — EXCHANGES | **the polydisc swap = divisor swap d ↔ n/d = spatial parity (t, x) ↦ (t, −x) of the Lorentz plane**; NOT the functional equation |
| s_{e₁} | e₁ | **3** | (−t₁, t₂) — negates t₁ | (−μ₂, −μ₁) — exchanges and negates both | swap composed with both functional equations |

Numerical rows from 5706: s_{e₁−e₂}: t → (0.37, 1.0), μ → (1.37, −0.63) · s_{e₁+e₂}: t → (−0.37, −1.0), μ → (−1.37, 0.63) · s_{e₂}: t → (1.0, −0.37), μ → (0.63, 1.37) · s_{e₁}: t → (−1.0, 0.37), μ → (−0.63, −1.37).

## The one line for the corpus
**The reflection in a multiplicity-1 root NEGATES a polydisc coordinate (= the functional equation) and EXCHANGES the e-coordinates; the reflection in a multiplicity-3 root EXCHANGES the polydisc coordinates (= parity) and NEGATES an e-coordinate.** "The long-root reflection that swaps the factors" is therefore two different elements depending on the coordinate system, and "long/short" itself flips under the B₂ ↔ C₂ relabelling (BST_TOP1:98, retired 12:08). Write the multiplicity and the coordinate system; never the length word alone. (Realisation in K, from L2: the multiplicity-1 reflection is a quarter-turn of the time circle compensated in SO(5) — a rotation, not a time reversal; the multiplicity-3 reflection is in O(1,1) ∖ SO(1,1), preserving the forward cone.)

— Grace
