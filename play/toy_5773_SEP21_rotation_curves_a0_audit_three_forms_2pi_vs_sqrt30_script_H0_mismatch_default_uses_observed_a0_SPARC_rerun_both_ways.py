#!/usr/bin/env python3
"""Toy 5773 — Guide/Vol3_Physics/rotation_curves: the a₀ forms (K1912 "two inconsistent a₀ forms"; Keeper 09-19 @Grace @Elie).
Pins the forms from the files, flags the script's inconsistencies from its own text, and re-runs sparc_bst.py both ways in a scratch
copy (the committed March results file is not touched). Elie, 2026-09-21."""
import math, os, re, shutil, subprocess, tempfile, csv, statistics
here = os.path.dirname(os.path.abspath(__file__)); RC = os.path.join(here, "..", "Guide", "Vol3_Physics", "rotation_curves")
md = open(os.path.join(RC, "DarkMatterCalculation.md"), encoding="utf-8").read()
rd = open(os.path.join(RC, "README.md"), encoding="utf-8").read()
py = open(os.path.join(RC, "sparc_bst.py"), encoding="utf-8").read()
score, cf = [], []
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
c = 2.99792458e8; Mpc = 3.0856775814913673e22
H0_planck, sH0 = 67.36, 0.54          # Planck 2018, the md's own input (md §2)
H0s = H0_planck * 1e3 / Mpc
a_2pi = c * H0s / (2 * math.pi); a_s30 = c * H0s / math.sqrt(30); a_obs, sa_obs = 1.20e-10, 0.02e-10
print("=" * 100 + "\nTOY 5773 — rotation_curves a₀ audit\n" + "=" * 100)
print(f"  H₀ = {H0_planck} km/s/Mpc (Planck 2018, the note's own input) → cH₀ = {c*H0s:.4e} m/s²")
print(f"  form A  a₀ = cH₀/(2π)  = {a_2pi:.4e}   ({100*(a_2pi/a_obs-1):+.1f} % vs observed 1.20 ± 0.02 e-10)   [README:29,55 'c²/2πR_H = 1.08e-10'; md §2 prose: 'the 2π is the S¹ geometry', '10 % discrepancy']")
print(f"  form B  a₀ = cH₀/√30   = {a_s30:.4e}   ({100*(a_s30/a_obs-1):+.1f} % vs observed)   [md §2 formula; sparc_bst.py:44-47; registry T191]")
print(f"  ratio B/A = √30/(2π)... 2π/√30 = {2*math.pi/math.sqrt(30):.4f}")
sc("C1 README carries form A (2πR_H) while the md formula and the script carry form B (√30)", "2πR_H" in rd and "sqrt{30}" in md and "sqrt(30)" in py, False)
sc("C2 the md's prose under form B is form A's: '2π is the S¹ geometry' + '10% discrepancy' sit under the √30 formula", "2\\pi$ is the S" in md and "10% discrepancy" in md, False,
   f"form A misses observed by {100*(1-a_2pi/a_obs):.0f} %, form B by {100*(1-a_s30/a_obs):.1f} % — the prose describes A")
h70 = re.search(r"^H0\s*=\s*70\.0", py, re.M); h674 = "2.184e-18" in py
sc("C3 script carries two H₀: 70.0 km/s/Mpc (line 42, unused for a₀) and 2.184e-18 s⁻¹ = 67.4 (line 46, the one used)", bool(h70) and h674, False,
   f"2.184e-18 s⁻¹ = {2.184e-18*Mpc/1e3:.1f} km/s/Mpc")
sc("C4 script default uses the OBSERVED a₀ (A0_SI = 1.2e-10); the BST a₀ only with --a0-bst", "A0_SI    = 1.2e-10" in py and "a0_use = A0_BST if args.a0_bst else A0" in py, False)
# re-run both ways in a scratch copy
tmp = tempfile.mkdtemp(); shutil.copytree(RC, os.path.join(tmp, "rc"), ignore=shutil.ignore_patterns("*.pdf"))
def run(flag):
    subprocess.run(["python3", "sparc_bst.py"] + flag, cwd=os.path.join(tmp, "rc"), capture_output=True, text=True, timeout=600)
    rows = list(csv.DictReader(open(os.path.join(tmp, "rc", "SPARC_BST_Results.csv"))))
    rms = [float(r["rms_km_s"]) for r in rows]; pct = [float(r["rms_pct"]) for r in rows if r["rms_pct"] not in ("inf", "nan")]
    chi = [float(r["chi2_red"]) for r in rows if r["chi2_red"] not in ("inf", "nan")]
    q1 = [r for r in rows if r["quality"] == "1"]; ok15 = sum(1 for r in q1 if r["rms_pct"] not in ("inf", "nan") and float(r["rms_pct"]) <= 15)
    return dict(n=len(rows), med_rms=statistics.median(rms), med_pct=statistics.median(pct), med_chi=statistics.median(chi), q1=len(q1), q1_ok15=ok15)
obs, bst = run([]), run(["--a0-bst"])
print(f"\n  re-run (scratch copy), observed a₀: n = {obs['n']}, median RMS {obs['med_rms']:.1f} km/s, median RMS% {obs['med_pct']:.1f}, median χ²_red {obs['med_chi']:.2f}, Q=1 within 15 %: {obs['q1_ok15']}/{obs['q1']}")
print(f"  re-run (scratch copy), BST a₀ (√30):  n = {bst['n']}, median RMS {bst['med_rms']:.1f} km/s, median RMS% {bst['med_pct']:.1f}, median χ²_red {bst['med_chi']:.2f}, Q=1 within 15 %: {bst['q1_ok15']}/{bst['q1']}")
print("  md §6 table: 'Median RMS 12.4 km/s', 'Median RMS% 11.8', '59/87 = 68 % of high-quality galaxies within 15 % RMS'")
sc("C5 the committed 12.4 km/s median RMS reproduces from the retained script (observed a₀)", abs(obs["med_rms"] - 12.4) < 0.15, False, f"{obs['med_rms']:.2f}")
sc("P1 (can fail) swapping the BST a₀ for the observed one moves the median RMS by < 0.2 km/s (the two a₀ differ by 0.4 %)", abs(bst["med_rms"] - obs["med_rms"]) < 0.2, True, f"Δ = {bst['med_rms']-obs['med_rms']:+.2f}")
sc("P2 (can fail) the md's 'median RMS% 11.8' is NOT what the retained script prints", abs(obs["med_pct"] - 11.8) > 1.0, True, f"script: {obs['med_pct']:.1f}")
sc("P3 (can fail) the md's '59/87 within 15 %' is NOT reproduced by the retained script's Q=1 count", not (obs["q1"] == 87 and obs["q1_ok15"] == 59), True, f"script: {obs['q1_ok15']}/{obs['q1']}")
shutil.rmtree(tmp)
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s, c in zip(score, cf) if c and s)}/{sum(cf)} can-fail hit")
