# Elie PREREG — Toy 5755, Round 144 E1: the K1809 sibling test on the three flagged "derived" rows. Written 2026-09-14 08:48 EDT, before the run.

## Menu (named before counting)
Integers V = {rank 2, N_c 3, n_C 5, C_2 6, g 7, N_max 137}. Pool P = { v, sqrt(v) : v = (product of a multiset of <= 3 elements of V) / (product of a multiset of <= 3 elements of V) }, empty product = 1, distinct values (relative 1e-12). This pool CONTAINS each published form at its own complexity class (C_2·g = 6·7; 1/(N_c²·n_C) = 1/(3·3·5); 1/rank³ = 1/(2·2·2)) and Cal's K1809 forms (1/(2√a) = √(1/(2·2·a))). Cal's J_CKM lesson: a pool that cannot reach the published form's class cannot clear it — this one reaches all three.

## Targets, pinned from the PDG 2024 summary tables (pdftotext dumps in notes/sources_R144/)
- m_t/m_b: m_t = 172.57 ± 0.29 GeV (direct, S = 1.5; rpp2024-sum-quarks line 56); m_b(m_b) = 4.183 ± 0.007 GeV (MS-bar, line 42). Scheme-mixed ratio as the row states it: 41.26 ± 0.10.
- sin²θ₁₃ = (2.19 ± 0.07)e−2 (rpp2024-sum-leptons line 552).
- λ_H = m_H²/(2v²), m_H = 125.20 ± 0.11 GeV (rpp2024-sum-gauge-higgs-bosons line 202), v = 246.22 GeV (G_F; convention m_H² = 2λv², the one under which the row's 1/8 gives m_H = v/2): 0.1293 ± 0.0002.

## Bands (two per row, both reported)
(a) the measurement's 1σ band; (b) the ROW'S OWN tolerance: |published − target|/target as a relative radius around the target (42: 1.8%; 1/45: 1.5%; 1/8: 3.3%) — the band the row itself claims to sit in.

## Density control (Cal, K1809 CLEARED)
chance in-band count = (number of pool values within a factor 2 of the target) × (log-width of the band)/(2 ln 2); a row is "surprising" only if actual > chance + 2√chance. Also swept: factor 1.5 and factor 3 windows.

## Predictions (hashed; N reported, never the winner)
- P1 (can fail): m_t/m_b at the row's tolerance (b): N ≥ 2 (I expect 6·7, 3·137/(2·5), 5·5·5/3 at least). At the 1σ band (a): the published 42 is OUTSIDE (7σ) — N counts whatever is inside; the row cannot be "derived at 1.7%" if its own form is out of the measurement band.
- P2 (can fail): sin²θ₁₃ at (a): N ≥ 2 (1/45 and 3/137 — the K1260-retired sub-claim — are both inside 1σ); at (b) N ≥ 1.
- P3 (can fail): λ_H at (b): N ≥ 3 (2/15, 7/54, √(1/60), 1/(2√15)…); at (a) I do not predict.
- P4 (control): every actual count sits within chance + 2√chance under the density control (K1809's finding: the vocabulary is saturated at this class); if any row is surprising I report it as such.
- Verdict rule (Keeper's, applied mechanically): N > 1 at the row's tolerance ⟹ "identified" by the K1809 rule. I predict all three drop.
