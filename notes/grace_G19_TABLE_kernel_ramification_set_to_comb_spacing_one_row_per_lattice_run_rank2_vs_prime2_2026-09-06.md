# Grace — G19 (Round 123): kernel ramification set ↦ comb spacing, one row per lattice run. SKELETON at 16:0x EDT 2026-09-06; the E11 row and the shared-integer verdict are filled when Elie's kernel-swap run is scored. Every number below is quoted from a retained out-file or a hashed prediction, never from memory.

## The claim being separated
T1448 (April) attributed the a_e Eisenstein term's ln 2 to "ln(rank)" via a posited "intertwining operator rank^{−2s}". T2621/L8 attribute the same ln 2 to the PRIME 2: the product of the Steinberg root numbers ε = 2^{½−λ} at the two multiplicity-3 roots is 2^{1−2λ}, present because the kernel q₀ = x₃²+x₄²+x₅² is anisotropic exactly at {2, ∞}. Rank 2 and prime 2 are the same integer; the map that would make them the same object has never been exhibited. **E11 exhibits the difference by construction:** keep the two hyperbolic planes (rank stays 2), replace the kernel by a ternary form anisotropic exactly at {3, ∞}; if the comb spacing moves from 2π/ln 2 to 2π/ln 3 while ψ(½) stays, the logarithm belongs to the prime.

## The table (filled rows are from retained instruments; "—" = not run)

| lattice / run | rank | kernel q₀ | ramification set of q₀ (anisotropic places) | comb spacing (predicted) | comb spacing (measured) | ψ(½) archimedean −2 ln 2 | quadratic character | instrument | status |
|---|---|---|---|---|---|---|---|---|---|
| ⟨1⁵, −1²⟩ (D_IV⁵, the corpus's odd lattice), level 1 | 2 | x₃²+x₄²+x₅² | {2, ∞} | 2π/ln 2 = 9.06472028365 (Lyra L1, hashed be29f1dc) | 9.06472028365, orders 1.000, k = ±1…±5 (Elie 5704, max Δ 7×10⁻³⁰) | present (Γ_ℂ factor), unmoved | none (odd kernel) | 5704; Cal §855 odd-lattice 2-adic integral | T2621 |
| even model at 2 (Cal §854) | 2 | same form, even lattice | {2, ∞} | π/ln 2 (half spacing) | π/ln 2 (Cal cal_odd2_*/cal_family2_*) | unmoved | none | Cal §854/§855 | lattice-parity fact, owned by Cal |
| n = 3 (kernel a point; odd plane) | 2 | — | — | level-type comb (odd-k), from the odd plane | present (Cal §861 by the instrument) | — | none | Cal cal_oddfam2b_* | in T2621's family clause |
| n = 4 (kernel ⟨1,1⟩) | 2 | x₃²+x₄² | {2, ∞} ∪ {p ≡ 3 mod 4} | ABSENT — ζ_{ℚ(i)} absorbs the 2-factor (Cal §862) | absent (Cal §861) | — | χ₋₄ | Cal cal_oddfam2b_* | in T2621's family clause |
| n = 6 (kernel of four squares) | 2 | Σ₁⁴ x_i² | {2, ∞} | 2π/ln 2, at Re λ = −1 | present (Cal §861) | — | none (disc +1) | Cal | in T2621's family clause |
| n ≥ 7 (kernel of ≥ 5 squares, isotropic at 2) | 2 | Σ x_i² | ∅ finite | no 2-comb predicted (5705 label) | NOT ESTABLISHED by the instrument (Cal §862) | — | χ₋₄ at n = 8 | 5705 (label only) | open |
| **E11: kernel swap, ternary form anisotropic exactly at {3, ∞}, two hyperbolic planes kept** | **2** | ⟨1, 1, 3⟩-type (Lyra L10 pins the form: discriminant, integrality, anisotropy at 3 and ∞) | **{3, ∞}** | **2π/ln 3 = 5.71917…** (Round 123 prediction; kill: spacing stays 2π/ln 2) | — (Elie E11, hashed after L10) | predicted UNMOVED (archimedean; independent of the finite ramified prime) | — | E11 + Cal C11 blind | **pending** |
| (control) kernel swap to a form anisotropic at {2, ∞} but a different lattice | 2 | — | {2, ∞} | 2π/ln 2 | — | — | — | — | optional control |

## What closes the shared-integer note
- If E11 measures 2π/ln 3 with ψ(½) unmoved: **the logarithm is the prime's; "ln(rank)" is retired everywhere** (G18 sweep, mode A or B as E10 selects), and the rank-2 reading survives only as the count of hyperbolic planes (it fixes HOW MANY short-root factors carry a comb, not the base of the logarithm).
- If E11 measures 2π/ln 2 with the {3, ∞} kernel: the comb is not the kernel's ramified prime and L8's 2^{1−2λ} needs a different reading; the note stays open and T2621's "from the prime 2 alone" clause is re-read.

— Grace (skeleton; rows to be completed from `play/.out_E11*.txt` and Cal's C11 score)
