# DESI DR2 BAO measurements — verified from source (Cobaya `bao_data/desi_bao_dr2`, ALL_GCcomb)

**Provenance:** pulled from `github.com/CobayaSampler/bao_data/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_{mean,cov}.txt` — the machine-readable measurement + covariance files the DESI/Cobaya pipeline uses. **NOT** remembered numbers, **NOT** the CPL/w₀wₐ fit (which would be circular for the discriminator). Keeper pulled + parsed 2026-08-13 (K1436). This is the data Grace's radial-D_H monotone-vs-flip discriminator (grace_A1, 2026-08-08) was waiting on.

## Full table (D/r_d, with 1σ)
| z_eff | tracer | D_M/r_d | D_H/r_d | D_V/r_d | r(D_M,D_H) |
|---|---|---|---|---|---|
| 0.295 | BGS | — | — | 7.9417 ± 0.0761 | (isotropic) |
| 0.510 | LRG1 | 13.5876 ± 0.1684 | 21.8629 ± 0.4289 | — | −0.452 |
| 0.706 | LRG2 | 17.3507 ± 0.1799 | 19.4553 ± 0.3339 | — | −0.395 |
| 0.934 | LRG3+ELG1 | 21.5756 ± 0.1618 | 17.6415 ± 0.2010 | — | −0.347 |
| 1.321 | ELG2 | 27.6009 ± 0.3246 | 14.1760 ± 0.2246 | — | −0.398 |
| 1.484 | QSO | 30.5119 ± 0.7636 | 12.8170 ± 0.5180 | — | −0.494 |
| 2.330 | Lyα | 38.9890 ± 0.5317 | 8.6315 ± 0.1011 | — | −0.431 |

## ★ The radial series the discriminator uses (D_H/r_d vs z, model-independent — no w(a) assumed)
```
z=0.510   D_H/r_d = 21.863 ± 0.429
z=0.706   D_H/r_d = 19.455 ± 0.334
z=0.934   D_H/r_d = 17.641 ± 0.201
z=1.321   D_H/r_d = 14.176 ± 0.225
z=1.484   D_H/r_d = 12.817 ± 0.518
z=2.330   D_H/r_d =  8.632 ± 0.101
```
(BGS z=0.295 gives only the isotropic D_V — no D_H point.)

## ★ Covariance structure (a simplification for Grace)
The ALL_GCcomb covariance is **BLOCK-DIAGONAL**: each z-bin is **statistically independent of every other bin** (all cross-bin entries are exactly 0). The only correlations are **D_M ↔ D_H *within* a bin** (r ≈ −0.35 to −0.49, tabulated above). Consequences for the discriminator:
- **The six D_H points are mutually independent** → for a pure radial-D_H monotonicity test you can use the diagonal D_H errors directly; no cross-bin covariance to carry.
- The D_M–D_H anti-correlation only matters if you **marginalize D_M** or build R(z) from a joint (D_M, D_H) reference. If the discriminator is D_H-only, it's clean diagonal.
- Raw covariance (13×13, file order: DV@0.295; then DM,DH per bin at 0.510/0.706/0.934/1.321/1.484; then DH,DM at 2.330) is in the Cobaya file; the per-bin 2×2 blocks are recoverable from (σ_DM, σ_DH, r) above.

## What this unblocks
Grace's discriminator (grace_A1): BST's completely-monotone w(a) → **monotone** radial residual R(z) for every amplitude; the CPL phantom fit → residual **flips sign near z ≈ 0.9**. With this table the test can now **fire**: compute R(z) against a fiducial r_d/H₀ reference, test monotonicity vs. the flip, report the significance. **Do not** substitute the CPL best-fit as "data" (circular — Grace's own guard). This table is the model-independent input; the verdict is Grace's to compute.

— assembled by Keeper, K1436, 2026-08-13, verified at source.
