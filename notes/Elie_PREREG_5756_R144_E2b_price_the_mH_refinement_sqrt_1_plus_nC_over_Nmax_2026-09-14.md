# Elie PREREG — Toy 5756, Round 144 E2b: price the m_H refinement √(1 + n_C/N_max). Written 2026-09-14 09:14 EDT, before the run.

Object: the correction factor c = m_H/(v/2), published form √(1 + n_C/N_max) = √(142/137) = 1.018085. Target from PDG 2024 (notes/sources_R144/): m_H = 125.20 ± 0.11 GeV; v = (√2 G_F)^(−1/2) with G_F = 1.1663788e−5 GeV⁻² (CODATA 2022) = 246.2196 GeV ⟹ c = 1.01698 ± 0.00089.

Menu (named before counting): the published form's own class — (1 + s·p/q)^e with s ∈ {+1, −1}, p and q products of ≤ 2 elements of {2,3,5,6,7,137} (empty product 1), e ∈ {1, 1/2, −1, −1/2}; distinct values. Plus, as a second instrument, the 5755 degree-3 ±√ pool applied to c itself. Bands: (a) PDG 1σ; (b) the form's own miss |published − c|/c as radius. Density control as in 5755.

Predictions (hashed):
- P1 (can fail): the published form sits OUTSIDE the 1σ band (I compute +1.2σ, 0.11 %); the row's "0.02 %" is not reproducible from the PDG 2024 primaries — I will print which (m_H, v) pair would give 0.02 %.
- P2 (can fail): N ≥ 2 competitors of the published form's class inside the 1σ band (I expect 1/30 under √, 7/(3·137) linear, at least).
- P3 (can fail): N ≥ 3 at the form's own miss tolerance.
- P4 (control): counts at chance under the density control.
Verdict rule: N > 1 ⟹ identified; a form outside 1σ at the primary is reported as such, not as "0.02 %".
