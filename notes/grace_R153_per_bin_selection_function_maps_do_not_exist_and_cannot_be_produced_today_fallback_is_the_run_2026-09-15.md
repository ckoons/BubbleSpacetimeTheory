# Grace R153 — Do the per-bin selection-function maps exist, or can they be produced today? NO and NO. The fallback is the run.
**2026-09-15 09:50 EDT — Grace. Casey's one-word question after the 09:25 restart. Evidence retained here; nothing computed on the catalogue; the CMB target is not in this file.**

## 1. Do they exist? NO.
`data/quaia/selfunc_perbin/` holds 8 log files (all stamped 09:12) and **0 FITS maps**. Every log ends at the same line:
```
Training fitter
X_train: (24545, 7) y_train: (24545,)
y_train min: 1.0 y_train: 17.0
```
(G < 20.5 bin 1; the other seven differ only in the counts). The Gaussian-process fit was started for all eight bins at once and none reached "Minimizing", "Predicting" or "Saved map". Elie's `partB_v_close.py` line 42 globs `selfunc_NSIDE64_{tag}_bin*.fits` in that directory, found 0, and recorded FALLBACK — correctly.

## 2. Can they be produced today? NO — not eight, not on this machine, not before (vi).
**2a. The released code CAN make them (my G2 word stands as written).** At commit 92eca506, `code/selection_function_map.py`'s docstring names the use ("if computing the selection function for a redshift slice or other subsample … <fn_parentcat>"), and the authors' own job array `code/jobarr.s` is exactly this: `selection_function_map.py ../data/quaia_G20.5_zsplit2bin${i}.fits … ../data/quaia_G20.5.fits`. Two facts from the same file, verbatim:
```
#SBATCH --mem=340GB        (commented alternative: --cpus-per-task=48)
#SBATCH --time=18:00:00
# selection function: set cpus-per-task=48
# 4 templates: need mem 175GB. 6: mem 340
```
and `code/job.s`: `# selection function: need mem 175GB. set cpus-per-task=48`. One bin per array task, on a cluster.
**2b. Why: the fitter is a dense Gaussian process (george `BasicSolver`, `ExpSquaredKernel` in 7 dimensions, 8 hyper-parameters + mean).** From george's `gp.py` (`grad_log_likelihood`): `K_inv = self.solver.get_inverse()`, `A = einsum("i,j", alpha, alpha) - K_inv`, `Kg = self.kernel.get_gradient(self._x)` of shape (n, n, n_params), `grad = 0.5 * einsum("ijk,ij", Kg, A)`. At the log's n = 24,545 nonzero pixels per bin:

| object | size |
|---|---|
| one n×n float64 | 4.82 GB |
| kernel + Cholesky factor (compute stage) | 9.6 GB |
| Kg (n, n, 8) in one gradient step | 38.6 GB |
| peak per bin fit (K, factor, K⁻¹, ααᵀ, A, Kg) | ≈ 63 GB |
| eight fits at the compute stage | ≈ 77 GB |
| eight fits in a gradient step | ≈ 500 GB |
| this machine (`sysctl hw.memsize`) | 128 GB |

Calibration of the estimate against the authors' number: the full G < 20.5 catalogue has ≈ 45,000 nonzero pixels → one matrix 16 GB, ×11 ≈ 178 GB — the "need mem 175GB" in their script. The scaling is theirs, not mine.
**2c. So:** eight concurrent fits cannot fit in 128 GB at any point past "Training fitter"; ONE fit at a time can (≈ 63 GB peak). Sequential wall time is NOT measured: the authors gave each bin an 18-hour window on 48 cores; my order-of-magnitude for one bin here is an hour or more per bin (BFGS iterations × [Cholesky + inverse at n = 24.5k + a 38.6 GB einsum]), i.e. the eight bins are a day of the machine, single-tenant. That is not "today" and it is not "before (vi)".
**2d. The template inputs are NOT the barrier.** The seven template maps (dust, stars, m10, mcs, unwise, unwisescan, mcsunwise) load from `../data/maps/*.npy`; Elie's logs show all seven "already exists" — they came from the Zenodo record's template-maps zip (879 kB; my R151 G2 pin), into my scratchpad checkout, which the restart removed. Re-fetching is minutes. (The raw inputs behind them — a 3×10⁷-star Gaia sample and a 1 % unWISE sample — are not needed when the zip is used.)

## 3. On "the crash is the randoms" (Keeper 09:39) — flagged, not ruled.
Timeline on disk: 09:12 eight GP fits launched (logs); 09:17 `random_G20.5_10x.fits` written; 09:19–09:23 `partB_v_close.py` ran to completion (`.partB_v_closed.json`); ≈ 09:25 memory exhausted. The 12,955,802-row SkyCoord transform costs of order 1 GB per array it allocates — a few GB. The eight fits cost ≥ 77 GB at their floor and ≈ 500 GB if any two reached a gradient step. Both were running at once; the randoms sat on top of the fits. Keeper's fix for the randoms (chunked 3×3 rotation, no SkyCoord) is right and cheap; it does not by itself make the per-bin fits runnable. Which allocation failed first is not recorded anywhere I can read; I state both, in size order.

## 4. What this decides under the frozen text.
v1.4 §2.3 (carried into v1.5 unchanged — K1907 declares Section 5 + §1's sentence + §4.4 clause 1 only): "if Grace's G2 reports, on the board and before step (vi), that the released code cannot be run today, the executability fallback is the catalogue's published NSIDE-64 selection-function map of the chosen cut, used as the weight for EVERY bin … under the fallback H5 … is MANDATORY". My G2 word, amended before (vi) and recorded here: **the released code runs; the eight per-bin maps it would produce cannot be produced today on this machine. The fallback branch is selected. H5 is mandatory for A and for B.** Elie's (v) table already says FALLBACK; Keeper 09:39 already says H5 mandatory; this note is the third instrument saying the same thing, from the code and the authors' own scripts.

## 5. If the per-bin maps are wanted anyway (Casey's/Cal's call, not mine).
One bin at a time, single-tenant on the machine, nothing else running; measure the first bin's wall time before committing to the other seven; that is a separate day, after (vi)–(ix) have run under the fallback, and the per-bin run would then be H-check-shaped (does the weight choice move β by less than 1σ), not a re-run of (vi). I do not launch it: a 63 GB job on a machine that fell over at 09:25 is not a reversible act while three colleagues are running instruments on it.

## 6. Retained.
Code checkout at 92eca506 in my scratchpad (`gaia-quasars-lss/`, `git rev-parse HEAD` = 92eca506f730…); george `gp.py` fetched from dfm/george main (the allocation lines quoted above); Elie's eight logs unchanged on disk; the arithmetic is the one-line python in this note's commit message.
