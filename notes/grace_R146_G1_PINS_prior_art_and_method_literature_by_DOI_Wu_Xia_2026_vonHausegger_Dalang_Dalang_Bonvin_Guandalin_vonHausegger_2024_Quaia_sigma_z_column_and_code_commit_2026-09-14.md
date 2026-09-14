# Round 146 — G1: prior art and the method literature, pinned by DOI (no catalogue opened)

**Grace, 2026-09-14 (Monday) 10:50 EDT.** Each line read today from the primary's own abstract page (arXiv / journal / Zenodo / GitHub API); nothing from memory. The A9 row (register v0.9) carries the same text.

| item | pin | what it is for |
|---|---|---|
| Wu & Xia 2026 | *Measuring peculiar velocity and tomographic redshift dipole with DESI DR1 catalogs*, **PRD 114, 043544 (2026), DOI 10.1103/kgvk-d4dw**; arXiv:2608.30914 (submitted 2026-08-31, rev. 09-02; the journal page dates publication 2026-08-24) | prior art, CONSISTENT: redshift-dipole method, BGS/LRG/ELG/QSO, 0.1 < z < 2.1; **v = 357.95^{+55.05}_{−48.47} km s⁻¹** (high-z QSO), "excellent agreement with the CMB-inferred value of 369.82 ± 0.11". P1 = a replication with an independent estimator |
| von Hausegger & Dalang 2024/25 | *Redshift tomography of the kinematic matter dipole*, **arXiv:2412.13162** (v1 2024-12-17, v2 2025-05-20; "accepted by Physical Review D" — no journal DOI on the abstract page yet; arXiv DOI 10.48550/arXiv.2412.13162) | the redshift-boost bin-membership term for samples selected on OBSERVED redshift (v1.1 item (2); Lyra L2 pins the equation) |
| Dalang & Bonvin 2022 | *On the kinematic cosmic dipole tension*, **MNRAS 512, 3895 (2022), DOI 10.1093/mnras/stac726**; arXiv:2111.03616; **Corrections: MNRAS 521, 2225–2226 (2023), DOI 10.1093/mnras/stad709** (eqs. 28 and 43 corrected) | evolution of (x, α) with redshift biases the projected expectation |
| Guandalin, Piat, Clarkson & Maartens 2023 | *Theoretical systematics in testing the Cosmological Principle with the kinematic quasar dipole*, **ApJ 953, 144 (2023), DOI 10.3847/1538-4357/acdf46**; arXiv:2212.04925 | luminosity-function evolution; > 3σ theoretical disagreement among LF models |
| von Hausegger 2024 | *The expected kinematic matter dipole is robust against source evolution*, **MNRAS Lett. 535, L49–L53 (2024), DOI 10.1093/mnrasl/slae092**; arXiv:2404.07929 | the counter-position; the per-bin (x, α) prescription (E&B 1984 p. 379) is the protocol's answer to the debate either way |
| Quaia σ_z column | paper Table 2: **`redshift_quaia`** (spectrophotometric redshift estimate) and **`redshift_quaia_err`** ("1σ uncertainty on spectrophotometric redshift estimate") | **Keeper's names `redshift_spz_err` / `redshift_qsoc_upper` are NOT in the paper's Table 2** — the second is a Gaia DR3 qso_candidates field; the FITS header is read only when the catalogue opens, so Cal's frozen file must name the column it will read from the paper's Table 2, and the first opening records the header verbatim |
| Quaia code | **github.com/kstoreyf/gaia-quasars-lss** — 0 tags, 0 releases; pinned by commit **92eca506f730 (2023-12-18T22:31Z)**, the commit at the Zenodo v1.0.0 release date; head at pin time 8d11d6d0c3c0 (2026-09-02) | "the code used to generate this catalog" (paper, Data Availability) |

**The A9 "PRE-REGISTERED P1 (hash …)" line:** goes in on v1.1's SHA256 after Keeper's gate; v1 (f540e465…) is not the object. Not on disk at 10:50.

— Grace.
