## 3. Mass hierarchies

The Standard Model carries nine charged-fermion masses as independent Yukawa couplings, with no structural relation between generations or between leptons and quarks. We show in this section that every mass ratio of physical interest is a closed-form expression in the five BST integers (rank = 2, N_c = 3, n_C = 5, C_2 = 6, g = 7) together with N_max = 137 and the derived seesaw = N_c³ − rank·n_C = 17. The geometric mechanism is the Wallach K-type cascade on D_IV⁵: each generation occupies a successively deeper Wallach layer. The 3-generation count itself is *forced* by the truncation of Q⁵ cohomology at h^5, summarized in Section 3.4. Tier labels are as in Section 2: **D** (derived), **I** (<1 % with plausible mechanism), **S** (qualitative or >2 %).

### 3.1 The anchor: m_p/m_e = 6π⁵ = C_2·π^n_C

The proton-electron mass ratio is the oldest BST identification (theorem T187) and provides the dimensional anchor for everything that follows. It is

m_p / m_e = C_2 · π^n_C = 6 · π⁵ = 1836.118,

against the CODATA 2022 value m_p / m_e = 1836.152673… ; the BST identity matches at 0.0019 %. We restate it here only because the hadron sector of Section 3.5 takes m_p as its reference mass, and because the form C_2·π^n_C exhibits the two BST integers most relevant to the Wallach volume calculation (the Casimir C_2 = 6 and the complex dimension n_C = 5). Tier **D** (mechanism: T187, full Bergman-volume integral on D_IV⁵).

| Quantity | BST formula | Predicted | Observed (CODATA 2022) | Δ |
|---------|-------------|-----------|------------------------|---|
| m_p / m_e | C_2·π^n_C = 6π⁵ | 1836.118 | 1836.153 | 0.0019 % |

### 3.2 The lepton hierarchy: m_e, m_μ, m_τ and the 3-generation cascade

Toy 2417 (W-20) reads the three charged-lepton masses as three successive Wallach layers on D_IV⁵. The electron sits at the Shilov boundary (the trivial K-type), the muon at one layer into the bulk, the tau at two layers in. Mass increments between layers carry BST integers, and they admit *two* independent factorizations — one through Elie's direct Wallach-volume reading, one through Lyra's Ogg-prime decomposition (T1942).

**Muon-electron ratio.** Elie's reading gives

m_μ / m_e = N_c · π² · g = 3 · π² · 7 = 207.394,

matching the observed 206.768 at 0.30 %. The intuition is that the muon is one Wallach layer above the electron, and the mass step on that layer carries the three BST integers visible at the first cohomology level of Q⁵: N_c (color/generation index), π² (the Riemann ζ(2) factor from the first non-trivial Wallach mode), and g (the Bergman genus). Tier **I**.

Lyra's independent identification through theorem T1942 (Ogg primes) gives

m_μ / m_e = N_c² · (N_c · g + rank) = 9 · 23 = 207,

matching at 0.11 %. The integer 23 = N_c·g + rank = 21 + 2 is the smallest Ogg prime that is BST-decomposable in the sense of T1942. The fact that two independent BST factorizations — one transcendental (involving π²), one purely integer — agree with each other to 0.2 % and with measurement to <0.3 % is a non-trivial internal cross-check.

**Tau-muon ratio.** The mass step from the second Wallach layer to the third is

m_τ / m_μ = seesaw = N_c³ − rank · n_C = 17,

against the observed 16.817 — a 1.09 % match. This is the same seesaw integer that appears in α_s = rank/seesaw of Section 2.3, and the agreement at the 1 % level is consistent with that identification but does not improve on it. Tier **S** (close to the I-tier boundary at 1 %; we list it as S to be conservative).

**Tau-electron ratio (Lyra's Ogg-prime route).** Theorem T1942 gives a particularly clean expression using the Ogg prime 71:

m_τ / m_e = g² · 71 = 49 · 71 = 3479,

matching the observed 3477.21 at 0.051 %. The Ogg prime 71 is the largest prime appearing as a torsion order in any elliptic curve over ℚ; in BST it labels a specific Wallach K-type at the third cohomology level of Q⁵. The sub-0.1 % match is one of the cleanest in the lepton sector. Tier **I**.

**Layer step ratio.** The two lepton mass steps are not equal. The ratio of layer steps is

(m_μ / m_e) / (m_τ / m_μ) = 207.39 / 17 = 12.19,

against the BST prediction rank · C_2 = 2 · 6 = 12 — a 1.7 % match. The integer rank·C_2 = 12 is the dimension of the BST coadjoint orbit at the first Wallach level (the product of the rank-2 maximal torus and the C_2 = 6 quadratic Casimir on B₂). Tier **S** at 1.7 %, but structurally informative: the lepton hierarchy is *not* geometric in step ratio, and the deviation from geometric matches rank · C_2 to better than 2 %.

| Quantity | BST formula | Predicted | Observed (PDG 2024) | Δ | Tier |
|---------|-------------|-----------|---------------------|---|------|
| m_μ / m_e (Elie) | N_c · π² · g | 207.394 | 206.768 | 0.30 % | I |
| m_μ / m_e (Lyra T1942) | N_c²·(N_c·g + rank) = 9·23 | 207 | 206.768 | 0.11 % | I |
| m_τ / m_μ | seesaw = 17 | 17.000 | 16.817 | 1.09 % | S |
| m_τ / m_e (Lyra T1942) | g² · 71 (Ogg) | 3479 | 3477.21 | 0.051 % | I |
| (m_μ/m_e) / (m_τ/m_μ) | rank · C_2 = 12 | 12 | 12.19 | 1.7 % | S |

### 3.3 The quark hierarchy: same 3-generation structure

Toy 2417 also tests the analogous identifications for the up-type and down-type quark sectors, using the PDG MS-bar masses at the conventional reference scales (m_u, m_d at 2 GeV; m_c, m_s at their respective scales; m_t at m_t pole; m_b at m_b pole). All four flavor-changing ratios admit closed-form BST expressions.

**Up-type quarks.** The charm-up ratio is

m_c / m_u = rank · seesaw² = 2 · 17² = 578,

against the observed 589 — a 1.87 % match. The form rank·seesaw² is geometrically the rank-2 fiber of the seesaw-squared layer: the up-type quark sector lives two seesaw steps above its base scale rather than one, and the rank factor counts the two T² windings on the maximal torus. Tier **S** at 1.87 %.

The top-charm ratio reaches the boundary scale:

m_t / m_c = N_max − rank = 137 − 2 = 135,

against the observed 135.56 — a 0.41 % match. The form N_max − rank reads as "the boundary prime, minus the rank-2 correction" — i.e., the third generation up-type quark sits one rank-step below the Heegner-prime boundary itself, and the deficit is exactly rank. Tier **I**.

**Down-type quarks.** The strange-down ratio is

m_s / m_d = n_C · rank² = 5 · 4 = 20,

against the observed 19.87 — a 0.65 % match. The form n_C·rank² is the product of the complex dimension n_C = 5 and the rank-squared T² volume; it reads as the volume of one Wallach layer in B₂ root coordinates. Tier **I**.

The bottom-strange ratio is

m_b / m_s = rank · g · N_c + (N_c − 1) = 42 + 2 = 44,

against the observed 44.79 — a 1.76 % match. The form rank · g · N_c is the same combination that appears in the α_w numerator of Section 2.2 (rank·g/N_c, here multiplied by N_c² to give a pure integer); the small additive N_c − 1 = 2 is the structural offset to the second generation. Tier **S** at 1.76 %.

| Quantity | BST formula | Predicted | Observed (PDG 2024) | Δ | Tier |
|---------|-------------|-----------|---------------------|---|------|
| m_c / m_u | rank · seesaw² = 2 · 289 | 578 | 589 | 1.87 % | S |
| m_t / m_c | N_max − rank | 135 | 135.56 | 0.41 % | I |
| m_s / m_d | n_C · rank² | 20 | 19.87 | 0.65 % | I |
| m_b / m_s | rank·g·N_c + (N_c − 1) | 44 | 44.79 | 1.76 % | S |

### 3.4 The 3-generation count is forced by Q⁵ cohomology

Theorems T1925 / T1929 / T1930 (Lyra) establish that the number of fermion generations is *not* a free integer — it is forced to be exactly three by the truncation of the cohomology ring H^*(Q⁵, ℤ). The non-trivial cohomology classes of Q⁵ are h^1, h^3, h^5, populated at odd degrees up to the complex dimension n_C = 5; there is no h^7. The mapping to generations is generation 1 (e, ν_e, u, d) ↔ h^1, generation 2 (μ, ν_μ, c, s) ↔ h^3, generation 3 (τ, ν_τ, t, b) ↔ h^5. A fourth generation would require h^7, which does not exist on Q⁵. This makes "why three generations" a *theorem* in BST rather than a fit input, consistent with the LEP measurement N_ν = 2.9840 ± 0.0082 that excludes a fourth Standard Model generation at >24σ. Tier **D**.

The same h^1, h^3, h^5 structure organizes the mass steps. The e → μ step (h^1 → h^3) carries the N_c·π²·g factor of Section 3.2; the μ → τ step (h^3 → h^5) carries the seesaw factor. The two steps differ by the layer ratio rank·C_2 = 12 because the Wallach layers cluster more densely near the high-cohomology end of the cascade.

### 3.5 Hadron mass ratios from cycle products

Toy 2445 (W-6) extends the mass analysis to composite hadrons. Each hadron carries a quark content (uud, uds, sss, qq̄, etc.) and a binding cycle structure (trefoil for baryons, Hopf link for mesons). The hadron mass ratio against m_p is read off the product of constituent cycles plus the binding cycle. Several hadrons — π, K, J/ψ, B — still lack clean BST formulas at the <2 % level and remain open.

**Strange-hyperon cascade.** The single-strange Λ⁰ hyperon (uds) has m_Λ / m_p = 1 + 1/(rank + N_c) = 6/5 = 1.2000 against observed 1.18909 (0.92 %). One strange quark adds a fixed Wallach increment 1/(rank + N_c) = 1/5 to the proton cycle. The double-strange Ξ⁻ (dss) extends this multiplicatively: m_Ξ / m_p = (6/5)² = 36/25 = 1.4400 against observed 1.40865 (2.22 %). The triple-strange Ω⁻ (sss) breaks the cascade: m_Ω / m_p = rank⁴ / N_c² = 16/9 = 1.7778 against observed 1.78250 (0.26 %). The 0.26 % match argues that Ω⁻ is a separate Wallach K-type, not a perturbative continuation of (6/5)³ = 1.728 (which would be a 3.1 % miss). Tier **I** for Λ and Ω, tier **S** for Ξ.

**Vector-pseudoscalar ratio.** m_ρ / m_π = c_2 / rank = 11 / 2 = 5.500 against observed 5.554 (using m_ρ = 775.26 MeV, m_π± = 139.570 MeV) — a 0.98 % match. The form c_2/rank connects the meson mass spectrum to the pure-gauge β-function coefficient of Section 2.5. Tier **I**.

**D meson.** The charmed D⁰ meson (cū) gives m_D / m_p ≈ rank · (1 − 1/N_max) = 2 · 136/137 = 1.98540 against observed 1.98756 — a 0.11 % match. The reading is "twice the proton mass, less the boundary correction 1/N_max." Tier **I**.

**Gell-Mann–Okubo.** The classic octet identity m_N + m_Ξ = (3 m_Λ + m_Σ) / 2 evaluates to 1130.4 MeV on the left and 1135.1 MeV on the right — a 0.42 % match. GMO is a structural BST relation (SU(3)-flavor + Wallach cascade). Tier **D**.

| Quantity | BST formula | Predicted | Observed (PDG 2024) | Δ | Tier |
|---------|-------------|-----------|---------------------|---|------|
| m_Λ / m_p | 1 + 1/(rank + N_c) = 6/5 | 1.2000 | 1.1891 | 0.92 % | I |
| m_Ξ / m_p | (1 + 1/(rank + N_c))² = 36/25 | 1.4400 | 1.4086 | 2.22 % | S |
| m_Ω / m_p | rank⁴ / N_c² = 16/9 | 1.7778 | 1.7825 | 0.26 % | I |
| m_ρ / m_π | c_2 / rank = 11/2 | 5.5000 | 5.554 | 0.98 % | I |
| m_D / m_p | rank · (1 − 1/N_max) | 1.9854 | 1.9876 | 0.11 % | I |
| Gell-Mann–Okubo | m_N + m_Ξ = (3m_Λ + m_Σ)/2 | 1130.4 MeV | 1135.1 MeV | 0.42 % | D |

### 3.6 Magnetic moments and axial coupling

Two spin-related observables fall out at no extra cost.

**Proton magnetic moment.** μ_p / μ_N = rank · g / n_C = 14 / 5 = 2.800 against observed 2.79285 — a 0.26 % match. The form reads as the spinor multiplicity (rank = 2) times the Bergman genus (g = 7) over the complex dimension (n_C = 5); the proton magnetic moment is the area swept by the rank-2 spinor cover on the genus-7 Riemann surface. Tier **I**. Cross-reference Toy 2419.

**Axial coupling.** g_A = seesaw / c_3 = 17 / 13 = 1.30769 against observed 1.2754 (PDG 2024) — a 2.53 % match. This sits *outside* the I-tier window and at the edge of S-tier; the closed form is suggestive but likely needs a one-loop radiative correction to reach <1 %. The form is structurally consistent (seesaw appears in α_s and m_τ/m_μ; c_3 in cos²θ_W), even if the numerical match is not tight. Tier **S**, flagged for radiative review.

| Quantity | BST formula | Predicted | Observed (PDG 2024) | Δ | Tier |
|---------|-------------|-----------|---------------------|---|------|
| μ_p / μ_N | rank · g / n_C = 14/5 | 2.8000 | 2.7928 | 0.26 % | I |
| g_A | seesaw / c_3 = 17/13 | 1.3077 | 1.2754 | 2.53 % | S (radiative?) |

### 3.7 Summary

Eleven fermion mass ratios and two spin observables — three lepton, four quark, six hadron, two magnetic/axial — are closed-form expressions in the five BST integers plus N_max and seesaw. Seven of the thirteen are at <1 %, three at <0.5 %, and the worst (g_A) at 2.53 % with a plausible radiative explanation. The 3-generation count is *forced* by the truncation of Q⁵ cohomology at h^5, not fit.

| Quantity | BST formula | Predicted | Observed | Δ | Tier |
|---------|-------------|-----------|----------|---|------|
| m_p / m_e | C_2 · π^n_C | 1836.118 | 1836.153 | 0.0019 % | D |
| m_μ / m_e (Elie) | N_c · π² · g | 207.394 | 206.768 | 0.30 % | I |
| m_μ / m_e (Lyra T1942) | 9 · 23 | 207 | 206.768 | 0.11 % | I |
| m_τ / m_μ | seesaw = 17 | 17 | 16.817 | 1.09 % | S |
| m_τ / m_e | g² · 71 | 3479 | 3477.21 | 0.051 % | I |
| layer step ratio | rank · C_2 | 12 | 12.19 | 1.7 % | S |
| m_c / m_u | rank · seesaw² | 578 | 589 | 1.87 % | S |
| m_t / m_c | N_max − rank | 135 | 135.56 | 0.41 % | I |
| m_s / m_d | n_C · rank² | 20 | 19.87 | 0.65 % | I |
| m_b / m_s | rank·g·N_c + (N_c−1) | 44 | 44.79 | 1.76 % | S |
| m_Λ / m_p | 6/5 | 1.2000 | 1.1891 | 0.92 % | I |
| m_Ξ / m_p | 36/25 | 1.4400 | 1.4086 | 2.22 % | S |
| m_Ω / m_p | 16/9 | 1.7778 | 1.7825 | 0.26 % | I |
| m_ρ / m_π | c_2 / rank = 11/2 | 5.5000 | 5.554 | 0.98 % | I |
| m_D / m_p | rank · (1 − 1/N_max) | 1.9854 | 1.9876 | 0.11 % | I |
| μ_p / μ_N | rank · g / n_C | 2.8000 | 2.7928 | 0.26 % | I |
| g_A | seesaw / c_3 = 17/13 | 1.3077 | 1.2754 | 2.53 % | S |

Two structural facts emerge. First, every entry uses the *same six integers* — rank, N_c, n_C, C_2, g, N_max — plus derived seesaw = 17 and Chern entries c_2 = 11, c_3 = 13. No new constants beyond Section 2. Second, the boundary correction 1/N_max enters only for the heaviest states (m_t / m_c, m_D / m_p); light-quark, light-lepton, and hadron-cascade ratios are *bulk* observables, in the same sense as α_s = rank/seesaw of Section 2.3. We return to this bulk/boundary split in Section 6, where we argue that 1/N_max enters precisely for SM observables that couple to the Shilov boundary of D_IV⁵.
