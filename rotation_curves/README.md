# BST Rotation Curves: SPARC Calculation

**Authors:** Casey Koons & Claude (Anthropic)
**Date:** March 2026

Reproducible code and results for the BST channel noise rotation curve calculation against the full SPARC database (175 galaxies, zero free parameters).

The theoretical basis is documented in the BST Working Paper (root directory). The complete derivation and analysis are in `DarkMatterCalculation.md` (available on request; PDF forthcoming).

---

## Quick Start

```bash
# Run all 175 SPARC galaxies
python3 sparc_bst.py

# Single galaxy
python3 sparc_bst.py --galaxy NGC3198

# Quality-1 galaxies only
python3 sparc_bst.py --quality 1

# Use BST-derived a0 = c²/2πR_H instead of observed
python3 sparc_bst.py --a0-bst
```

Requires Python 3, numpy, scipy.

---

## Files

| File | Description |
|---|---|
| `sparc_bst.py` | Main calculator — reads SPARC rotmod files, applies BST acceleration formula, outputs per-galaxy metrics |
| `SPARC_BST_Results.csv` | Full results: RMS, TF error, dark non-matter fractions, reduced χ² for all 175 SPARC galaxies |
| `SPARC_data/` | SPARC rotation curve files (Lelli, McGaugh & Schombert 2016) — see attribution below |

---

## The BST Formula

Dark non-matter = incomplete windings on the S¹ channel (channel noise). The total acceleration satisfies:

```
μ(a_total / a0) · a_total = a_Newton

μ(x) = x / √(1 + x²)          ← derived from Shannon S/N of Haldane channel
a0 = c² / 2πR_H = 1.08×10⁻¹⁰ m/s²   ← derived from S¹ fiber geometry
```

Closed-form solution:

```python
def a_bst(a_N, a0=3702.6):   # a0 in (km/s)²/kpc
    xN = a_N / a0
    u  = (xN**2 + xN * np.sqrt(xN**2 + 4)) / 2
    return np.sqrt(u) * a0
```

Mass-to-light ratios fixed by stellar population synthesis (not fitted):
- Υ_disk = 0.5 M☉/L☉
- Υ_bul  = 0.7 M☉/L☉

**Free parameters: 0**

---

## Results Summary

| Metric | Value |
|---|---|
| Galaxies | 175 (full SPARC sample) |
| Median RMS | 12.4 km/s |
| Median RMS% | 11.8% |
| Free parameters | 0 |
| Dark non-matter particles required | None |

68% of high-quality galaxies (Q=1) fit within 15% RMS with zero free parameters — comparable to MOND with the same fixed mass-to-light priors, while BST derives the interpolating function and a₀ from first principles.

---

## SPARC Data Attribution

Rotation curve data from:

> Lelli, F., McGaugh, S. S., & Schombert, J. M. (2016). SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves. *The Astronomical Journal*, 152, 157.

Data available at: http://astroweb.cwru.edu/SPARC/
