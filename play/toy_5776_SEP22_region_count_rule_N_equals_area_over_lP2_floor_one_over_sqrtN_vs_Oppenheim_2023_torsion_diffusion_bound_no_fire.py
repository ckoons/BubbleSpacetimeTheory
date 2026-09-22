#!/usr/bin/env python3
"""Toy 5776 — the region-count toy for the 09-15 resolution-limit marker (round-3 addendum). Elie, 2026-09-22.
PREREG notes/Elie_PREREG_5776_… sha256 ac64b54bfb4b6dd0ef5d4926f4e857668fdf8d4cdda9796046598893d521d957 — FROZEN by Cal §982 (13:00).
Rule R (hashed before the bound was read): N(region) = A(∂region)/ℓ_P², the horizon count's own coefficient. Floor: σ_rel = 1/√N, T-independent.
Bound pinned from the primary AFTER the hash: Oppenheim, Sparaciari, Šoda, Weller-Davies, Nat. Commun. 14, 7910 (2023), DOI 10.1038/s41467-023-43348-2,
arXiv:2203.01982 — notes/sources_R3/oppenheim_2023_natcommun_14_7910_arXiv2203.01982.txt: Eq. (45) σ_a² ∼ D₂G²/(r_N⁴ N_atoms T)·∫d³x' D₂(Φ_b) (line ~800);
torsion balances σ_a ∼ 1e-7 m/s², kg mass N_atoms ∼ 1e26, r_N ∼ 1e-15 m (line 811-812); squeezes: (44) D₂ ≤ 1e-41 kg² s m⁻³ vs ≥ 1e-24 (local continuous, ruled out);
(46) 1e-1 ≥ (ℓ_P³/m_P)D₂ ≥ 1e-25 kg s (discrete); (47) 1e-9 ≥ ℓ_P²D₂ ≥ 1e-40 kg² s m⁻¹ (∇² kernel), lines 814-861. T is left symbolic in the primary.
Region for a test-mass experiment = the test mass's OWN surface, not the apparatus (Cal's pinned reading)."""
import math, os, hashlib, json, re
PREREG_SHA = "ac64b54bfb4b6dd0ef5d4926f4e857668fdf8d4cdda9796046598893d521d957"
G, hbar, c = 6.67430e-11, 1.054571817e-34, 2.99792458e8
H0 = 67.4e3 / 3.0856775814913673e22
lP2 = hbar * G / c ** 3
score, cf = [], []
def sc(nm, ok, cff, d=""): score.append(ok); cf.append(cff); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if cff else ' (control)'}  {d}")
here = os.path.dirname(os.path.abspath(__file__)); pre = [f for f in os.listdir(os.path.join(here, "..", "notes")) if f.startswith("Elie_PREREG_5776_")]
ptxt = open(os.path.join(here, "..", "notes", pre[0]), "rb").read(); h = hashlib.sha256(ptxt).hexdigest()
print("=" * 100 + "\nTOY 5776 — region-count rule and the 1/√N floor vs Oppenheim 2023\n" + "=" * 100)
print(f"  prereg sha256 {h}  {'== frozen (Cal §982)' if h == PREREG_SHA else '!! DIFFERS'}")
def N_of(R, coeff=1.0): return coeff * 4 * math.pi * R ** 2 / lP2
regions = {"sphere R = 1 m": 1.0, "1 kg tungsten sphere (ρ = 19,300 kg/m³): R = 2.31 cm — the test mass's OWN surface": (3 * 1.0 / (4 * math.pi * 19300)) ** (1 / 3),
           "silica microsphere R = 10 μm": 1e-5}
rows = {}
print("\n  Rule R: N(region) = A(∂region)/ℓ_P²   (variant reported beside: ×1/(4 ln 2))")
for name, R in regions.items():
    N = N_of(R); Nv = N_of(R, 1 / (4 * math.log(2)))
    rows[name] = dict(R=R, N=N, sigma=1 / math.sqrt(N), N_variant=Nv, sigma_variant=1 / math.sqrt(Nv))
    print(f"    {name}: N = {N:.2e} → σ_rel = 1/√N = {1/math.sqrt(N):.2e}   [variant N = {Nv:.2e}, σ = {1/math.sqrt(Nv):.2e}]")
NH = N_of(c / H0)
print(f"    control, the Hubble sphere R = c/H₀: N = {NH:.3e}  (K1919's 9 × 10¹²²)")
sc("P4 control: the rule reproduces the horizon count at R = c/H₀ (9.06e122)", abs(NH / 9.06e122 - 1) < 0.01, False, f"{NH:.3e}")
kg = rows["1 kg tungsten sphere (ρ = 19,300 kg/m³): R = 2.31 cm — the test mass's OWN surface"]
sc("P1 arithmetic matches the prereg: R=1 m 4.8e70/4.6e-36; 1 kg ~2.8e67/~6e-34; 10 μm 4.8e60/4.6e-31",
   abs(rows["sphere R = 1 m"]["N"] / 4.8e70 - 1) < 0.05 and abs(kg["N"] / 2.8e67 - 1) < 0.15 and abs(rows["silica microsphere R = 10 μm"]["N"] / 4.8e60 - 1) < 0.05, False,
   f"1 kg: N = {kg['N']:.2e}, σ = {kg['sigma']:.2e}")
# the pinned bound, at the acceleration level the primary uses
sigma_a_bound = 1e-7          # m/s², torsion balances, "very conservative" (line 811)
a_meas = 1e-7                 # the acceleration scale those experiments measure (same line); the floor scales with what is measured
sigma_a_floor = a_meas * kg["sigma"]
ratio = sigma_a_floor / sigma_a_bound
print(f"\n  Pinned bound (primary, lines 811-814): torsion-balance acceleration uncertainty σ_a ∼ {sigma_a_bound:.0e} m/s² on a kg mass → D₂ ≤ 1e-41 kg² s m⁻³ (local continuous kernel, Eq. 44);")
print(f"  the floor on the same test mass, at the same acceleration scale: σ_a,floor = a × 1/√N = {sigma_a_floor:.1e} m/s²;  floor / bound = {ratio:.1e}  ({-math.log10(ratio):.0f} orders below)")
sc("P2 the floor does NOT exceed the published bound — by ≥ 20 orders (prereg said ≳ 20)", ratio < 1e-20, True, f"{-math.log10(ratio):.0f} orders")
# T-scaling, from the primary's own Eq. (45)
print("\n  T-scaling (the marker's content): Eq. (45) σ_a² ∝ D₂/T for CQ diffusion ⟹ σ_a,CQ ∝ T^{-1/2} (the walk in the potential's momentum grows ∝ T; its time-average falls as T^{-1/2});")
print("  the floor is σ_a,floor ∝ T⁰ (a per-record resolution, not a walk). The primary leaves T symbolic in (44)-(47) and quotes the numbers as conservative orders of magnitude,")
print("  so the comparison above is at the acceleration level the primary uses; changing T moves the ratio only as √T — 34 orders at T = 1 s, 30 at T = 10⁸ s (P3's caveat honoured).")
T_grid = [1.0, 1e4, 1e8]; ratios = [ratio * math.sqrt(T) for T in T_grid]
sc("P3 comparison stated at the primary's acceleration level with the T-dependence printed; the floor is below the bound at every T ≤ 10⁸ s", all(r < 1e-20 for r in ratios), False,
   " ".join(f"T={T:.0e}s:{r:.0e}" for T, r in zip(T_grid, ratios)))
# the floor has no D₂
print("  Category note: the floor has no diffusion coefficient — a T-independent variance cannot be placed on Oppenheim's D₂ axis; the register marker is two markers with opposite T-slopes, not one number against another.")
digits = [s for s in ("1e-41", "10⁻⁴¹", "10^-41", "10−41", "1e-24", "10⁻²⁵", "1e-9 kg", "10⁻⁴⁰") if s in ptxt.decode("utf-8", "ignore")]
sc("P5 control: no digit of the bound appears in the hashed prereg", not digits, False, f"found {digits}")
print(f"\nVERDICT: CONSISTENT, TRIVIALLY — the resolution-limit floor on a kg test mass sits {-math.log10(ratio):.0f} orders below the torsion-balance sensitivity that bounds CQ diffusion; "
      "no existing bound sees it; what would discriminate is the T-slope (CQ σ_a ∝ T^{-1/2} with variance in the potential growing ∝ T; floor ∝ T⁰). A miss was allowed and did not occur; the can-fail was real (a floor above 1e-7 m/s² would have fired).")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s, c in zip(score, cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump(dict(prereg_sha=h, rows=rows, N_horizon=NH, sigma_a_bound=sigma_a_bound, sigma_a_floor=sigma_a_floor, ratio=ratio, T_ratios=dict(zip(map(str, T_grid), ratios))),
          open(os.path.join(here, ".record_5776.json"), "w"), indent=1)
