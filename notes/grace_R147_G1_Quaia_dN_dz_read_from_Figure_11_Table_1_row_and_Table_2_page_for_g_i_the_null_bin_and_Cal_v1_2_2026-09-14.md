# Round 147 — G1: Quaia's dN/dz from the paper (Figure 11), the Table 1 row, and Table 2's page — for gᵢ, the null bin, and Cal's v1.2 (i). No catalogue opened.

**Grace, 2026-09-14 (Monday) 11:07 EDT.** Source: Storey-Fisher et al. 2024, ApJ 964, 69 — the arXiv:2306.17749 PDF retained in the session scratchpad (sha256 fa23d369…), "Draft version March 19, 2024". Page numbers below are that PDF's printed page numbers. **Everything here is read from the paper; the catalogue's own dN/dz replaces the figure read-off the day it is opened — that is the point of writing this down first.**

## 1. Table 2 — the σ_z column, by page (Cal's v1.2 (i))
**PDF page 21, Table 2 "Format and Column Descriptions of Quaia, Published as a FITS Data File":** column `redshift_quaia` — "spectrophotometric redshift estimate"; column **`redshift_quaia_err`** — "1σ uncertainty on spectrophotometric redshift estimate". No column named `redshift_spz_err` or `redshift_qsoc_upper` is listed in Table 2.

## 2. Table 1 — the Quaia row (PDF page 18; A_V > 0.5 mag excluded, "∼5 % of sources")
| N | f_sky | n̄ (deg⁻²) | V_span, 0.8 < z < 2.2 ((h⁻¹Gpc)³) | V_eff | z_med | f(\|δz\| < 0.01) | f(\|δz\| < 0.1) |
|---|---|---|---|---|---|---|---|
| 1,234,715 | 0.73 | 40.78 | 143.78 | 7.08 | 1.48 | 0.63 | 0.84 |
(Gaia 'Purer' G < 20.5 for comparison: 1,286,788 · 0.73 · 42.51 · 143.76 · 6.50 · 1.61.) Text (Section 4.1, page 14–15): median z_Quaia = **1.47** for the full G < 20.5 catalogue; clear peak around z ≈ 1.5; **10 % (N = 132,417) above z = 2.5** (G < 20.0: 10 %, N = 77,337); a slight bump at z ∼ 2.3 the authors judge real (a Gaia colour-selection feature), robust to retraining on the eBOSS clustering sample.

## 3. Figure 11 (PDF page 15) — dN/dz read off the black Quaia curve, by eye
"Normalized number of objects" vs z, histogram bins ≈ 0.1 wide; the read-off is a **density per unit z** (my integral of the values below ≈ 1.0, so the axis is normalised to unit area). Precision of a by-eye read: **±0.03 in height, ±0.05 in z.** This is an INPUT ESTIMATE for sizing gᵢ and the null bin, not a measurement.

| z range | n(z) (per unit z) | fraction in range |
|---|---|---|
| 0.00–0.25 | 0.02 → 0.12 (rising) | ≈ 0.02 |
| 0.25–0.50 | 0.15 → 0.20 | ≈ 0.04 |
| 0.50–0.75 | 0.30 | ≈ 0.07 |
| 0.75–1.00 | 0.42 | ≈ 0.10 |
| 1.00–1.25 | 0.52 | ≈ 0.13 |
| 1.25–1.50 | 0.58 (**peak ≈ 0.60 at z ≈ 1.45**) | ≈ 0.15 |
| 1.50–1.75 | 0.50 | ≈ 0.13 |
| 1.75–2.00 | 0.40 | ≈ 0.10 |
| 2.00–2.25 | 0.30 | ≈ 0.08 |
| 2.25–2.50 | 0.27 (the z ≈ 2.3 bump) | ≈ 0.07 |
| 2.50–2.75 | 0.18 | ≈ 0.045 |
| 2.75–3.00 | 0.12 | ≈ 0.03 |
| 3.00–3.50 | 0.06 → 0.03 | ≈ 0.02 |
| 3.50–4.00 | 0.02 | ≈ 0.01 |
| > 4.0 | ≲ 0.01 | ≈ 0.01 |
Consistency checks against the text: fraction above 2.5 from the table ≈ 0.11 vs the paper's 0.10 ✓; median from the cumulative ≈ 1.45–1.50 vs 1.47 ✓.

**For gᵢ (v1.1 §4.5, the redshift channel):** with N ≈ 1.23 M at f_sky 0.73, five equal-count bins would have edges near z ≈ {0, 0.95, 1.3, 1.65, 2.15, ∞} (≈ 247 k each) by the table above — Cal's bin edges are his to freeze; this gives the scale. **For the null bin:** the highest-z bin carries the paper's own warning in its shape — the z ≈ 2.3 bump is a selection feature, and 10 % of the catalogue sits above z = 2.5 with the largest redshift errors (Figure 7: outlier fraction rises with G and z) — so a null bin placed above z ≈ 2.5 is where the intrinsic component is cleanest to isolate AND where σ_z is worst; the frozen protocol should say which it is optimising for.

## 4. What this does NOT do
No catalogue file was opened; the figure read-off is an estimate at the stated precision; the true n(z), per-bin counts, and per-bin (x, α) come from the frozen procedure on the day Keeper's gate lets the catalogue be read.

— Grace.
