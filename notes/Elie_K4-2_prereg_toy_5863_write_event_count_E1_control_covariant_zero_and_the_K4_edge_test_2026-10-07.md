# Elie — PREREG toy 5863 (Round K4-2, Lane B). Wed 2026-10-07 15:33 EDT (from `date`, its own call). Written BEFORE any code.
didwe "write event selection rules photon absorption count" → 0. Read before writing: Cal S1033 (KL-W0..W4), K1937/38, K1946/47. No Lyra/Grace K4-2 output read.

## Framework (stated first)
A one-photon transition i → f is ALLOWED iff the symmetry that survives admits a nonzero intertwiner from (operator ⊗ i) to f. With rotations only, that means a nonzero Gaunt integral ∫ Y*_{l'm'} Y_{kq} Y_{lm} for multipole rank k, with parity built in, and identity on spin.

## Controls
- C1 (positive, E1, k = 1), exact for l, l' ≤ 6: allowed set = {Δl = ±1, Δm ∈ {−1, 0, 1}}, Δs = 0. From (1, 0): **4 targets** (Cal's [I]).
- C2 (negative, KL-W0): free electron + real photon → electron: (p + k)² = m² + 2p·k > m² for every real k ≠ 0, so 0 allowed. In the covariant module form: the lowest energy of L_ψ ⊗ L_γ is 7/2 + E_γ > 7/2, so there is no L_ψ summand (complete reducibility of positive-energy tensor products: pin-owed, Jakobsen–Vergne).
- C3 (rank check): k = 2 gives Δl ∈ {0, ±2} (l + l' ≥ 2), |Δm| ≤ 2; k = 1 (M1, the angular-momentum operator, same parity) gives Δl = 0, Δm = ±1 between distinct states.

## The count
- W1 (i) covariant only: **0 write states** (C2). The wall, reproduced as the absorption form of K1937.
- W2 (ii) with the breaking named (a binder absorbs the recoil; rotations SO(3) survive; the energy scale is the measured binding, so the tier carries m_e and α): from the ground state s, E1 gives **3 targets p_q, q ∈ {−1, 0, 1}**.
  - The E1 graph on {s, p₋₁, p₀, p₊₁} is the STAR K_{1,3}: 3 of K4's 6 edges.
  - Adding M1 gives p₋₁–p₀ and p₀–p₊₁ (5 edges). Adding E2 gives p₋₁–p₊₁ (6 edges = K4).
  - **Prediction: the write's own (E1) count gives K4's VERTICES (frame = initial s, values = the three Δm) but NOT its edges.** K4's edge set needs three multipole orders.
  - The "3" is KL-W3's "three Δm values" = spin-1's three states (the generic cage).
- W3 nulls:
  - fixed photon axis (helicity only, q = ±1): s + 2 = a K3 vertex set (star K_{1,2});
  - lowest multipole E2 (s → d): 1 + 5 = a K6 vertex set.
  - So K4's vertex count is selected only by "lowest multipole, all directions": the rank-1 3.
- W4 spin: E1 leaves spin unchanged, so every vertex doubles (8 states = two disjoint stars). The vertex map holds only if the record erases spin.
- W5 the corpus's electron K-type V_(1/2,1/2) (the so(5) spinor) is 4-dimensional, with weights (±½, ±½). W(B₂) acts on them as D₄ (order 8): a SQUARE, not K4's S₄. **The 4 appears; K4's symmetry does not.**
- Decoy (Cal): spin 2 × helicity 2 = 4 in-states, no edges, no frame. Recorded, not used.

## Carry-over (K4-1 item 4)
- H: the Haldane code computes ln Z(β) = Σ_{l ≤ l_max} Σ_{|m| ≤ m_max} d_l · ln[(1 − e^{−(N_max+1)βE_{lm}})/(1 − e^{−βE_{lm}})], with E_{lm} = √(l(l+3)/R_b² + m²/R_s²) and d_l = (2l+3)(l+1)(l+2)/6.
  - A zero-energy mode contributes ln(N_max + 1); a mode with βE ≥ 50 contributes 0.
  - Each mode is a bosonic occupation truncated at N_max. It is ln Z, not Z, and contains no binomial.
  - Checked against the code to machine precision.
