# Elie PREREG — Toy 5760, Round 148 E1 (the combined σ_β) + E2 (the flux-cut derivative, S6). Written 2026-09-14 11:24 EDT, before the run. Synthetic only; no catalogue until Cal's v1.2 hash.

## E1 — the joint fit
Data: the five count-channel dipoles D_i (observed-z bins of v1.1 §2.5, f_i = 2 + x_i(1+α) + B_i) and the redshift moment(s) R (variant F: the full sample, g = 1 + m; variant Q: five flux quantiles, g_k = 1 + m_k); model: D_i = f_i b + w_i a, −R_k = g_k b, ONE shared b = βû, the intrinsic vector a in the count channel only. Weighted linear LS (per-moment covariances; the count and redshift moments treated as independent — checked by the seed scatter). Quaia-like synthetic (4 M generated ≈ 1.3 M after cut, |b| > 30°, photo-z 0.01(1+z)), CMB β, 20 seeds.
- Expectation computed first: count alone 443 km/s (5758), full-sample redshift ≈ 170 ⟹ combined ≈ 1/√(1/443² + 1/170²) ≈ 160 km/s; five flux quantiles ≈ the same.
- P1 (can fail): the fit's quoted σ_β c (mean over seeds) lies in [120, 210] km/s for BOTH variants (the band is ±25 % around 160, wider than the seed-to-seed spread of the quoted σ, which is a few %).
- P2 (can fail): the quoted σ_β is CALIBRATED — the standard deviation of β̂ over the 20 seeds divided by the mean quoted σ_β lies in [0.7, 1.35] (the 2σ band for a variance ratio with 19 dof is ≈ [0.68, 1.32]).
- P3 (can fail): the mean of β̂/β_inj over the 20 seeds lies within ±2.5 σ_mean of 1, σ_mean = (σ_β/β_inj)/√20 ≈ 0.10 — i.e. in [0.75, 1.25].
- Reported: whether σ_β c < 185 km/s (Cal's 4.4 bar) — A/B-capable or C by construction.

## E2 — the flux-cut derivative, control S6
Synthetic counts with a BROKEN power law so that x changes with the cut (dN/dS ∝ S^{−(1+1.2)} above S_k = 1.3, S^{−(1+0.6)} below, in units where the deep cut is S = 1.0 ≙ G < 20.5 and the bright cut S = 1.585 ≙ G < 20.0). Boost (physical, incl. z′) AND an injected intrinsic dipole (A = 0.05 with Cal's per-bin w_i toward (90°, 20°), flux-independent by construction). Observable per bin and for the whole sample: ΔD = D(deep) − D(bright), predicted [Δ(x(1+α)) + ΔB] βû with x measured at each cut over [S_lim, 2 S_lim].
- P4 (can fail): at β = 0.01 on 13 M generated, whole-sample ΔD: direction within 3σ-cone of û (cone from the covariance of the difference, computed from the non-shared sources), amplitude ratio |ΔD|/([Δ(x(1+α)) + ΔB] β) within ±2.5σ of 1 (σ printed first), and the intrinsic direction ŵ contributes < 2σ to ΔD (the component of ΔD along ŵ⊥û consistent with zero).
- P5 (reported, not scored): the same at the CMB β and Quaia depth — the S/N of the whole-sample derivative (I expect < 1: signal ≈ 1.2 β ≈ 0.0015 against ≈ 0.0025 noise). The verdict for v1.3: a check IF P4 holds, with the power stated by P5.
