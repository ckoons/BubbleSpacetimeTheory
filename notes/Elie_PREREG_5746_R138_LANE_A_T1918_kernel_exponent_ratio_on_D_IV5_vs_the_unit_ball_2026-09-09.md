# PRE-REGISTRATION — Toy 5746, Round 138 LANE A (CRITICAL): T1918's "Bergman/Szegő kernel exponent ratio"

**Elie, 2026-09-09 (Wednesday) 11:21 EDT (shell-copied). Hashed before the run.**

**The row (found by grep, registry line 2653, tier Proved, gravity-cluster, CANONICAL=T201):** *"Gravitational Coupling α_G from D_IV⁵ Bergman + Shilov Boundary Winding: α_G = (C_2²/n_C)·exp(−C_2·N_c·n_C) = (36/5)·exp(−90) at 0.11% match. **Shilov winding = (n+1)/n is Bergman/Szegő kernel exponent ratio.** Same factor refines T1485 Λ (Toy 2350) closing H_0 to 0.12%."*

## The instrument (two definition-level probes, no kernel exponent assumed)
- **Probe H (which weight is the Hardy/Szegő one):** the Shilov boundary is where |z|² = 1, so the Szegő weight is the unique ν at which ⟨|z|²⟩_ν ≡ 1 for **every** word. Run the sweep and read ν off.
- **Probe B (which weight is the Bergman one):** the Bergman weight is the one whose norm is Lebesgue integration over the domain. Run a fresh uniform Monte Carlo on each domain and read which ν it matches.
Both probes are applied to the unit ball FIRST as a positive control, then to D_IV⁵.

## Hashed lines
- **P1 (positive control, can fail):** on B⁵, ⟨|z|²⟩_ν for z₁^m is (m+5)/(ν+m). Probe H returns **ν_Hardy(B⁵) = 5**; Probe B (uniform Monte Carlo in B⁵) matches **ν_Bergman(B⁵) = 6**, i.e. 1 − ⟨|z|²⟩ = 1/(m+6), my 5721 P3 number. **Ratio = 6/5 — the row's number reproduced from my instrument.** General d: ν_H = d, ν_B = d+1, ratio (d+1)/d.
- **P2 (can fail):** on D_IV⁵, Probe H returns **ν_Hardy = 5/2** (5744 A1: ⟨|z|²⟩ ≡ 1 identically there and at no other weight) and Probe B (uniform Monte Carlo on the Lie ball) matches **ν_Bergman = 5** (5721: 0.5012 measured vs 1/2 exact at the vacuum, 0.5248 vs 11/21 at (0,1)). **Ratio = 5/(5/2) = 2.**
- **P3 (family, can fail):** for D_IV^n the ratio is **2 at every n** (ν_B = n, ν_H = n/2), while for B^d it is (d+1)/d. **So (n+1)/n is the unit ball's formula, and it equals 6/5 = C_2/n_C only at n = 5, by coincidence of two unrelated objects.** Ratio of the two answers: 2 ÷ 6/5 = **5/3**.
- **P4 (the propagation, both branches priced, no ruling — Cal's C1):**
  - **If the sentence is LOAD-BEARING** (the 6/5 in the prefactor is derived from the kernel ratio, so the prefactor is C_2 × ratio): the prefactor becomes 6 × 2 = 12 and α_G = 12·e^{−90} = **9.83 × 10⁻³⁹** against the observed Gm_p²/(ħc) = **5.906 × 10⁻³⁹** — a **66 % miss** where the row claims 0.11 %.
  - **If the sentence is DECORATIVE** (the prefactor is C_2²/n_C = 36/5 as a BST integer ratio and the kernel sentence is a bolted-on justification): the number is untouched and only the justification is struck. **This is my memory's own lesson — a false reason bolted to a correct number survives every correction — so I price both and rule neither.**
  - Downstream named for the hold: T1485 (Λ), Toy 2350, the H_0 closure at 0.12 %, and T1924's joint anchor if it inherits.

Score X/4; P1, P2, P3 can fail.
