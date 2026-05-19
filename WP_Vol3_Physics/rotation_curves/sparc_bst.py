#!/usr/bin/env python3
"""
BST Dark Matter: SPARC Database Rotation Curve Calculator
=========================================================
Authors: Casey Koons & Claude (Anthropic)
Date:    March 2026

Physical model:
  Dark matter = channel noise on S¹ fiber (incomplete windings)
  BST acceleration: μ(a_total/a0) · a_total = a_Newton
  Interpolating function: μ(x) = x / √(1 + x²)
  Flat rotation is a theorem of S/N asymptotics — not a fit.

Baryonic mass-to-light ratios (fixed, not fitted):
  Υ_disk = 0.5 M_sun/L_sun  (Schombert+2014 stellar pop synthesis at 3.6μm)
  Υ_bul  = 0.7 M_sun/L_sun

Usage:
  python3 sparc_bst.py                        # run full SPARC database
  python3 sparc_bst.py --galaxy NGC3198       # single galaxy
  python3 sparc_bst.py --quality 1            # quality 1 only
  python3 sparc_bst.py --a0-bst               # use BST-derived a0

SPARC data: http://astroweb.cwru.edu/SPARC/
  Rotmod_LTG.zip — rotation curve + baryonic decomposition files
  SPARC_Lelli2016c.mrt — galaxy table (distances, Vflat, quality flags)
"""

import numpy as np
import csv
import os
import argparse
import glob

# ============================================================
# PHYSICAL CONSTANTS
# ============================================================
G        = 4.302e-6    # (km/s)² kpc / M_sun
A0_SI    = 1.2e-10     # m/s²  (Milgrom / observed)
A0       = A0_SI / 3.241e-14   # (km/s)²/kpc  = 3702.6
C_KM     = 3e5         # km/s
H0       = 70.0        # km/s/Mpc
R_H      = C_KM / H0 * 1e3    # kpc (Hubble radius)
A0_BST   = C_KM * H0 / (np.sqrt(30) * 1e3)  # cH₀/√30  (km/s²), then → (km/s)²/kpc
# Convert to (km/s)²/kpc: H0 in km/s/Mpc, 1 Mpc = 1e3 kpc
A0_BST_SI = 2.998e8 * 2.184e-18 / np.sqrt(30)  # = 1.195e-10 m/s²
A0_BST   = A0_BST_SI / 3.241e-14   # (km/s)²/kpc

# Fixed mass-to-light ratios (Schombert+2014 at 3.6μm)
UPSILON_DISK = 0.5    # M_sun / L_sun
UPSILON_BUL  = 0.7    # M_sun / L_sun


# ============================================================
# BST MODEL FUNCTIONS
# ============================================================

def a_bst(a_N, a0=A0):
    """
    BST total acceleration from implicit equation:
      μ(a/a0) · a = a_N,  μ(x) = x/√(1+x²)
    Exact closed-form solution:
      u = (xN² + xN√(xN²+4)) / 2,  a_BST = √u · a0
    """
    xN = a_N / a0
    u  = (xN**2 + xN * np.sqrt(xN**2 + 4.0)) / 2.0
    return np.sqrt(np.maximum(u, 0.0)) * a0


def baryonic_accel(r, Vgas, Vdisk, Vbul,
                   upsilon_disk=UPSILON_DISK, upsilon_bul=UPSILON_BUL):
    """
    Newtonian acceleration from SPARC baryonic components.
    SPARC convention: Vgas, Vdisk, Vbul are signed velocity contributions
    at Υ=1; actual contribution is Υ × V × |V|.
    Total: v_N² = Vgas·|Vgas| + Υ_d·Vdisk·|Vdisk| + Υ_b·Vbul·|Vbul|
    """
    v2 = (Vgas * np.abs(Vgas)
          + upsilon_disk * Vdisk * np.abs(Vdisk)
          + upsilon_bul  * Vbul  * np.abs(Vbul))
    v2 = np.maximum(v2, 0.0)
    return v2 / r   # (km/s)²/kpc


def f_dark_from_accel(a_N, a_total):
    """Dark matter fraction: 1 - a_Newton / a_total"""
    return 1.0 - a_N / np.maximum(a_total, 1e-30)


def tully_fisher_from_accel(a_N_outer, r_outer, a0=A0):
    """
    Asymptotic TF: v⁴ = G·M_bar·a0.
    Estimate from the outermost points where a_N is flattening.
    """
    a_N_flat = np.mean(a_N_outer[-3:]) if len(a_N_outer) >= 3 else a_N_outer[-1]
    # v_flat⁴ = a_N_flat · r_flat · a0 ... but TF is asymptotic:
    # simpler: just return v_BST at outermost r
    a_bst_flat = a_bst(a_N_flat, a0)
    v_flat_bst = np.sqrt(r_outer[-1] * a_bst_flat)
    return v_flat_bst


# ============================================================
# SPARC FILE READERS
# ============================================================

def read_rotmod(filepath):
    """
    Read a SPARC _rotmod.dat file.
    Columns: Rad  Vobs  errV  Vgas  Vdisk  Vbul  SBdisk  SBbul
    Returns dict of numpy arrays, or None on failure.
    """
    data = []
    distance_mpc = None
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('# Distance'):
                try:
                    distance_mpc = float(line.split('=')[1].split()[0])
                except Exception:
                    pass
                continue
            if line.startswith('#'):
                continue
            parts = line.split()
            if len(parts) >= 6:
                try:
                    data.append([float(x) for x in parts[:6]])
                except ValueError:
                    continue

    if not data or len(data) < 3:
        return None

    arr = np.array(data)
    return {
        "distance_mpc": distance_mpc,
        "r":     arr[:, 0],
        "Vobs":  arr[:, 1],
        "errV":  arr[:, 2],
        "Vgas":  arr[:, 3],
        "Vdisk": arr[:, 4],
        "Vbul":  arr[:, 5],
    }


def read_sparc_table(filepath):
    """
    Read SPARC master table (SPARC_Lelli2016c.mrt).
    Column order (whitespace-split):
      0=name 1=T 2=D 3=e_D 4=f_D 5=Inc 6=e_Inc 7=L[3.6] 8=e_L 9=Reff
      10=SBeff 11=Rdisk 12=SBdisk 13=MHI 14=RHI 15=Vflat 16=e_Vflat 17=Q
    Returns dict keyed by galaxy name.
    """
    # Hubble type strings
    HTYPES = {0:"S0",1:"Sa",2:"Sab",3:"Sb",4:"Sbc",5:"Sc",
              6:"Scd",7:"Sd",8:"Sdm",9:"Sm",10:"Im",11:"BCD"}

    galaxies = {}
    in_data = False
    with open(filepath) as f:
        for line in f:
            stripped = line.strip()
            # Data section starts after the final separator line
            if set(stripped) == {'-'} and len(stripped) > 10:
                in_data = True
                continue
            if not in_data or not stripped:
                continue
            # Skip reference key lines like "Be91 = ..."
            if '=' in stripped[:8] and len(stripped.split()[0]) <= 6:
                continue
            parts = stripped.split()
            if len(parts) < 18:
                continue
            try:
                name    = parts[0]
                t_int   = int(parts[1])
                hubtype = HTYPES.get(t_int, str(t_int))
                dist    = float(parts[2])
                inc     = float(parts[5])
                rdisk   = float(parts[11])
                mhi     = float(parts[13]) * 1e9   # 10^9 M_sun → M_sun
                vflat   = float(parts[15])
                evflat  = float(parts[16])
                quality = int(parts[17])
                galaxies[name] = {
                    "hubtype": hubtype,
                    "distance": dist,
                    "inc": inc,
                    "rdisk": rdisk,
                    "MHI": mhi,
                    "Vflat": vflat,
                    "eVflat": evflat,
                    "quality": quality,
                }
            except (ValueError, IndexError):
                continue
    return galaxies


# ============================================================
# GALAXY RUNNER
# ============================================================

def run_rotmod(name, rotmod, meta=None, a0=A0,
               upsilon_disk=UPSILON_DISK, upsilon_bul=UPSILON_BUL,
               verbose=True):
    """
    Run BST calculation for one galaxy given its rotmod data dict.
    Returns results dictionary.
    """
    r    = rotmod["r"]
    Vobs = rotmod["Vobs"]
    errV = rotmod["errV"]
    Vgas = rotmod["Vgas"]
    Vdisk= rotmod["Vdisk"]
    Vbul = rotmod["Vbul"]

    # Newtonian acceleration
    a_N  = baryonic_accel(r, Vgas, Vdisk, Vbul, upsilon_disk, upsilon_bul)
    # BST total acceleration
    a_B  = a_bst(a_N, a0)
    # Predicted velocities
    v_bst   = np.sqrt(r * a_B)
    v_newt  = np.sqrt(np.maximum(r * a_N, 0.0))
    # Dark matter fraction
    f_dm    = f_dark_from_accel(a_N, a_B)

    # Metrics
    resid   = v_bst - Vobs
    rms     = np.sqrt(np.mean(resid**2))
    chi2    = np.sum((resid / np.maximum(errV, 1.0))**2) / max(len(r), 1)

    # Reference velocity: observed Vflat from table, or last few points
    vflat_obs = meta["Vflat"] if (meta and not np.isnan(meta["Vflat"])) else np.nan
    vflat_bst = v_bst[-1]       # BST asymptotic (last point)
    rms_pct   = 100 * rms / vflat_obs if not np.isnan(vflat_obs) else np.nan
    tf_err    = 100 * abs(vflat_bst - vflat_obs) / vflat_obs \
                if not np.isnan(vflat_obs) else np.nan

    quality  = meta["quality"] if meta else 3
    hubtype  = meta["hubtype"] if meta else ""
    distance = meta["distance"] if meta else rotmod.get("distance_mpc", 0)

    if verbose:
        print(f"\n{'='*60}")
        print(f"  Galaxy: {name}  [{hubtype}]  Q={quality}  D={distance:.1f} Mpc")
        print(f"{'='*60}")
        print(f"  Υ_disk={upsilon_disk}  Υ_bul={upsilon_bul}")
        print(f"  v_flat (obs) = {vflat_obs:.1f} km/s" if not np.isnan(vflat_obs) else "  v_flat (obs) = ---")
        print(f"  v_flat (BST) = {vflat_bst:.1f} km/s" +
              (f"  (TF err {tf_err:.1f}%)" if not np.isnan(tf_err) else ""))
        print(f"  RMS residual = {rms:.1f} km/s" +
              (f"  ({rms_pct:.1f}%)" if not np.isnan(rms_pct) else ""))
        print(f"  Reduced χ²   = {chi2:.2f}")
        print()
        print(f"  {'r':>7} {'Vobs':>7} {'errV':>5} {'Vbary':>7} "
              f"{'VBST':>7} {'resid':>7} {'f_dark':>7}")
        print(f"  {'-'*53}")
        for i in range(len(r)):
            print(f"  {r[i]:7.2f} {Vobs[i]:7.1f} {errV[i]:5.1f} "
                  f"{v_newt[i]:7.1f} {v_bst[i]:7.1f} {resid[i]:7.1f} {f_dm[i]:7.3f}")

    # Interpolate f_dark at reference radii
    def safe_interp(r_ref):
        if r_ref < r[0] or r_ref > r[-1]:
            return np.nan
        return float(np.interp(r_ref, r, f_dm))

    return {
        "name":        name,
        "hubtype":     hubtype,
        "quality":     quality,
        "distance":    distance,
        "n_points":    len(r),
        "vflat_obs":   vflat_obs,
        "evflat_obs":  meta["eVflat"] if meta else np.nan,
        "vflat_bst":   vflat_bst,
        "tf_err_pct":  tf_err,
        "rms_km_s":    rms,
        "rms_pct":     rms_pct,
        "chi2_red":    chi2,
        "f_dark_r5":   safe_interp(5.0),
        "f_dark_r10":  safe_interp(10.0),
        "f_dark_r20":  safe_interp(20.0),
        "r":     r,
        "Vobs":  Vobs,
        "errV":  errV,
        "v_bst": v_bst,
        "v_N":   v_newt,
        "f_dm":  f_dm,
    }


# ============================================================
# OUTPUT
# ============================================================

def write_results_csv(results, filename="SPARC_BST_Results.csv"):
    """Write per-galaxy summary to CSV."""
    if not results:
        print("No results to write.")
        return

    fieldnames = [
        "name", "hubtype", "quality", "distance", "n_points",
        "vflat_obs", "evflat_obs", "vflat_bst", "tf_err_pct",
        "rms_km_s", "rms_pct", "chi2_red",
        "f_dark_r5", "f_dark_r10", "f_dark_r20",
    ]

    def fmt(v):
        if isinstance(v, float):
            return f"{v:.4f}" if not np.isnan(v) else "nan"
        return str(v)

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for res in results:
            writer.writerow({k: fmt(res.get(k, np.nan)) for k in fieldnames})

    print(f"\nResults written to: {filename}  ({len(results)} galaxies)")


def print_summary(results, label="BST SPARC RESULTS"):
    """Print summary statistics."""
    if not results:
        return
    rms  = np.array([r["rms_km_s"] for r in results if not np.isnan(r["rms_km_s"])])
    pct  = np.array([r["rms_pct"]  for r in results if not np.isnan(r["rms_pct"])])
    tf   = np.array([r["tf_err_pct"] for r in results if not np.isnan(r["tf_err_pct"])])
    chi2 = np.array([r["chi2_red"] for r in results if not np.isnan(r["chi2_red"])])

    print(f"\n{'='*60}")
    print(f"  {label}  ({len(results)} galaxies)")
    print(f"{'='*60}")
    print(f"  RMS:  median={np.median(rms):.1f}  mean={np.mean(rms):.1f} km/s")
    print(f"  RMS%: median={np.median(pct):.1f}  mean={np.mean(pct):.1f}%"
          if len(pct) else "  RMS%: ---")
    print(f"  TF error: mean={np.mean(tf):.1f}%  median={np.median(tf):.1f}%"
          if len(tf) else "  TF: ---")
    print(f"  Reduced χ²: mean={np.mean(chi2):.2f}  median={np.median(chi2):.2f}")
    print(f"  Free parameters: 0  (Υ_disk=0.5, Υ_bul=0.7 fixed by SPS)")
    print()

    ranked = sorted(results, key=lambda x: x.get("rms_km_s", np.inf))
    print("  Best fits:")
    for r in ranked[:5]:
        q = r['quality']
        print(f"    {r['name']:<14} {r['rms_km_s']:5.1f} km/s "
              f"({r['rms_pct']:5.1f}%)  Q={q}  [{r['hubtype']}]")
    if len(ranked) > 10:
        print("  ...")
    print("  Worst fits:")
    for r in ranked[-5:]:
        q = r['quality']
        print(f"    {r['name']:<14} {r['rms_km_s']:5.1f} km/s "
              f"({r['rms_pct']:5.1f}%)  Q={q}  [{r['hubtype']}]")


# ============================================================
# MAIN RUNNER
# ============================================================

def run_all(sparc_dir, output_csv="SPARC_BST_Results.csv",
            quality_cut=None, a0=A0, verbose_each=False):
    """
    Run BST on all rotmod files in sparc_dir.
    Reads metadata from SPARC_Lelli2016c.mrt if present.
    """
    # Load galaxy metadata
    table_file = os.path.join(sparc_dir, "SPARC_Lelli2016c.mrt")
    meta_all   = {}
    if os.path.exists(table_file):
        meta_all = read_sparc_table(table_file)
        print(f"Loaded metadata for {len(meta_all)} galaxies from {table_file}")
    else:
        print(f"WARNING: {table_file} not found — no metadata available")

    # Find all rotmod files
    rotmod_files = sorted(glob.glob(os.path.join(sparc_dir, "*_rotmod.dat")))
    print(f"Found {len(rotmod_files)} rotmod files")

    results = []
    skipped = []

    for fpath in rotmod_files:
        fname = os.path.basename(fpath)
        name  = fname.replace("_rotmod.dat", "")

        rotmod = read_rotmod(fpath)
        if rotmod is None:
            skipped.append(name)
            continue

        meta = meta_all.get(name, None)

        # Quality cut
        if quality_cut is not None and meta:
            if meta["quality"] > quality_cut:
                skipped.append(f"{name}(Q={meta['quality']})")
                continue

        try:
            res = run_rotmod(name, rotmod, meta=meta, a0=a0,
                             verbose=verbose_each)
            results.append(res)
        except Exception as e:
            skipped.append(f"{name}(err:{e})")
            continue

    if skipped:
        print(f"Skipped {len(skipped)}: {', '.join(skipped[:10])}"
              + (" ..." if len(skipped) > 10 else ""))

    write_results_csv(results, output_csv)
    print_summary(results)
    return results


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="BST Dark Matter: SPARC Rotation Curve Calculator")
    parser.add_argument("--sparc",    metavar="DIR",
                        default="SPARC_data",
                        help="Path to SPARC data directory (default: ./SPARC_data)")
    parser.add_argument("--galaxy",   metavar="NAME",
                        help="Run single galaxy by name")
    parser.add_argument("--output",   metavar="CSV",
                        default="SPARC_BST_Results.csv",
                        help="Output CSV filename")
    parser.add_argument("--quality",  metavar="N", type=int, default=None,
                        help="Only run galaxies with quality ≤ N (1=best)")
    parser.add_argument("--a0-bst",   action="store_true",
                        help="Use BST-derived a0 = cH₀/√30 instead of observed")
    parser.add_argument("--verbose",  action="store_true",
                        help="Print per-galaxy rotation curve tables")
    args = parser.parse_args()

    a0_use = A0_BST if args.a0_bst else A0
    a0_label = f"a0_BST = {A0_BST:.0f}" if args.a0_bst else f"a0_obs = {A0:.0f}"

    print(f"BST Constants:")
    print(f"  G        = {G:.4e} (km/s)² kpc/M_sun")
    print(f"  a0 (obs) = {A0:.1f} (km/s)²/kpc  [{A0_SI*1e10:.2f} × 10⁻¹⁰ m/s²]")
    print(f"  a0 (BST) = {A0_BST:.1f} (km/s)²/kpc  [cH₀/√30, {100*(A0_BST-A0)/A0:+.1f}%]")
    print(f"  Using:     {a0_label} (km/s)²/kpc")
    print(f"  Υ_disk   = {UPSILON_DISK}  Υ_bul = {UPSILON_BUL}")
    print()

    if args.galaxy:
        name     = args.galaxy
        fpath    = os.path.join(args.sparc, f"{name}_rotmod.dat")
        if not os.path.exists(fpath):
            print(f"File not found: {fpath}")
        else:
            table_file = os.path.join(args.sparc, "SPARC_Lelli2016c.mrt")
            meta_all   = read_sparc_table(table_file) if os.path.exists(table_file) else {}
            rotmod     = read_rotmod(fpath)
            run_rotmod(name, rotmod, meta=meta_all.get(name), a0=a0_use, verbose=True)
    else:
        if not os.path.isdir(args.sparc):
            print(f"SPARC directory not found: {args.sparc}")
            print("Download data from http://astroweb.cwru.edu/SPARC/ (Rotmod_LTG.zip)")
        else:
            run_all(args.sparc, args.output,
                    quality_cut=args.quality,
                    a0=a0_use,
                    verbose_each=args.verbose)
