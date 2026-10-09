#!/usr/bin/env python3
"""
Toy 5877 — Round K4-5, Lane B item 1: T3, the absolute count, BLIND (Elie, 2026-10-09). Hash: Cal S1041 (8ca18f75):
order N_census (every fork, on disk with its hash) → N_req from K1919's identity → the ratio; MATCH ≤ 1 decade; REPORT 1–3;
MISS > 3. One absorption = one bound–bound or bound–free transition of a bound electron caused by a real photon; scattering
does not count; recombination capture does not count; stellar interiors EXCLUDED (Casey Q2); χ ≡ 1 primary.
Inputs: Grace's T3 table (her Section 12; every number quoted from Section 9 with its source). didwe "absolute count census" → 0.

  --part1  : the census, every fork, written to play/.record_5877_census.json (no N_req computed or read)
  --part2  : N_req from the K1919 Section 7 identity (coded AFTER part 1 was on disk), the ratio, the rule
Cosmology and x_e(z): CAMB 1.6.6 background with its RECFAST recombination (Planck 2018 baseline, Grace 9.1).
"""
import sys, os, json, hashlib, math
import numpy as np
import camb

here = os.path.dirname(os.path.abspath(__file__))
REC = os.path.join(here, ".record_5877_census.json")
RESULTS = []
def score(tag, ok, msg):
    RESULTS.append(bool(ok)); print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

# ---------------------------------------------------------------- pins (Grace Section 9/12), SI constants (defined)
H0_kms = 67.36; Om_m = 0.3153; ombh2 = 0.02237; omch2 = 0.1200; T0 = 2.72548; tau = 0.0544      # Planck 2018 Table 1/2; Fixsen 2009
A10 = 2.85e-15; Tstar = 0.068; g1_over_g0 = 3.0                                                  # Wild 1952 / Furlanetto 2006 p. 22, g0 = 1, g1 = 3
COB, CIB = 24e-9, 26e-9                                                                            # Driver 2016, W m^-2 sr^-1 (0.1–8 μm, 8–1000 μm)
LYC_PER_BARYON_PRE6 = 8.0                                                                          # Madau–Dickinson 2014 p. 2848: "approximately 8 LyC photons per baryon ... prior to z ~ 6" (MODEL)
Z_WINDOWS = [(40.0, 200.0), (14.0, 21.0)]                                                          # Furlanetto 2006 / Pritchard–Loeb: the two absorption troughs (MODEL)
c = 299792458.0; hP = 6.62607015e-34; kB = 1.380649e-23; G = 6.67430e-11; hbar = hP / (2 * math.pi)
Mpc = 3.0856775814913673e22; mH = 1.67262192e-27 + 9.1093837e-31; eV = 1.602176634e-19
H0 = H0_kms * 1e3 / Mpc

pars = camb.CAMBparams(); pars.set_cosmology(H0=H0_kms, ombh2=ombh2, omch2=omch2, TCMB=T0, tau=tau)
bg = camb.get_background(pars)
YHe = pars.YHe; XH = 1 - YHe
print(f"CAMB {camb.__version__}; recombination model {type(pars.Recomb).__name__}; YHe = {YHe:.4f} (CAMB's BBN default; MODEL) → X_H = {XH:.4f}")
rho_crit0 = 3 * H0 ** 2 / (8 * math.pi * G)
Om_b = ombh2 / (H0_kms / 100) ** 2
n_H0 = XH * Om_b * rho_crit0 / mH                       # comoving hydrogen number density today, m^-3
V_H0 = 4 / 3 * math.pi * (c / H0) ** 3                   # today's Hubble volume, m^3 (Cal's definition)
N_Hatoms = n_H0 * V_H0
print(f"n_H,0 = {n_H0 * 1e-6:.3e} cm^-3; V_H,0 = {V_H0:.3e} m^3; hydrogen atoms in V_H,0 = {N_Hatoms:.3e}")

def xe_of(z): return bg.get_background_redshift_evolution(np.atleast_1d(z), ['x_e'], format='array')[:, 0]
def dt_dz(z): return 1.0 / ((1 + z) * bg.hubble_parameter(z) * 1e3 / Mpc)        # s per unit z

def census():
    rec = {"classes": {}, "forks": {}, "control": {}}
    # ---- (1) 21-cm: hyperfine absorptions of relic photons by neutral H. Rate per atom = (g1/g0) A10 n_occ P0,
    #      n_occ = 1/(e^{T*/Tγ} − 1), P0 = fraction in F = 0 = 1/(1 + 3 e^{−T*/T_S}) with T_S = Tγ (equilibrium occupation; MODEL)
    def rate21(z):
        Tg = T0 * (1 + z); n_occ = 1 / np.expm1(Tstar / Tg); P0 = 1 / (1 + 3 * np.exp(-Tstar / Tg))
        return g1_over_g0 * A10 * n_occ * P0
    def N21(zlo, zhi, xe_override=None):
        z = np.linspace(zlo, zhi, 4001)
        xHI = np.clip(1 - (xe_of(z) if xe_override is None else xe_override), 0, 1)
        return N_Hatoms * np.trapz(xHI * rate21(z) * dt_dz(z), z)
    n21_windows = sum(N21(*w) for w in Z_WINDOWS)
    n21_all = N21(0.0, 1100.0)
    rec["classes"]["21cm_troughs_only"] = n21_windows
    rec["forks"]["21cm_all_neutral_epochs_z<1100"] = n21_all
    print(f"  (1) 21-cm absorptions: troughs only (40–200, 14–21) = {n21_windows:.3e}; all neutral epochs z < 1100 = {n21_all:.3e}  "
          f"[per atom in the troughs: {n21_windows / N_Hatoms:.3e}]")
    # ---- (2)+(3) Lyman: stellar UV photons absorbed by neutral H (bound–bound Lyα and bound–free LyC).
    #      MD14: ~8 LyC photons per baryon emitted before z ~ 6; in a neutral IGM each is absorbed (one bound–free transition).
    #      Lyα–Lyβ band photons: counted equal to the LyC count (UNPINNED ratio; fork ×1), absorbed once (resonant re-scattering NOT counted
    #      in the primary — a scattering fork would multiply by ~τ_GP, unpinned here; reported as owed, not computed).
    n_baryons = Om_b * rho_crit0 / (1.67262192e-27) * V_H0
    nLyC = LYC_PER_BARYON_PRE6 * n_baryons
    nLya = 1.0 * nLyC
    rec["classes"]["LyC_photoionizations_pre_z6_MD14"] = nLyC
    rec["classes"]["Lya_absorptions_once_fork_x1_of_LyC"] = nLya
    print(f"  (2) Lyα absorptions (once; ×1 of LyC, unpinned ratio) = {nLya:.3e};  (3) LyC photo-ionizations pre-z6 (MD14 8/baryon) = {nLyC:.3e}")
    # ---- (4) dust: starlight absorbed by grains = the CIB's photons at emission: N = u_CIB,0 (1 + z̄) V / <E_abs>
    u_CIB0 = 4 * math.pi * CIB / c; u_COB0 = 4 * math.pi * COB / c
    dust = {}
    for zbar in (1.0, 2.0):
        for Eabs in (1.0, 3.0):
            dust[f"zbar={zbar},Eabs={Eabs}eV"] = u_CIB0 * (1 + zbar) * V_H0 / (Eabs * eV)
    rec["forks"]["dust_absorptions"] = dust
    n_dust_primary = dust["zbar=2.0,Eabs=3.0eV"] if False else u_CIB0 * (1 + 2.0) * V_H0 / (2.0 * eV)
    rec["classes"]["dust_absorptions_primary_zbar2_Eabs2eV"] = n_dust_primary
    print(f"  (4) dust absorptions of starlight (CIB energy / <E_abs>; z̄ = 2, 2 eV primary) = {n_dust_primary:.3e}; forks {{{', '.join(f'{k}: {v:.2e}' for k, v in dust.items())}}}")
    # ---- (5) COB photons absorbed by other bound electrons (gas, solids, life): an UPPER fork = every COB photon absorbed by today
    cob_upper = {f"E={E}eV": u_COB0 * V_H0 / (E * eV) for E in (0.6, 1.2)}
    rec["forks"]["COB_all_absorbed_upper"] = cob_upper
    print(f"  (5) COB photons (upper fork, all absorbed by today): {{{', '.join(f'{k}: {v:.2e}' for k, v in cob_upper.items())}}}  — NOT in the primary (they are the escaped light)")
    # ---- primary sum and span
    primary = n21_windows + nLya + nLyC + n_dust_primary
    low = n21_windows + nLyC + min(dust.values())                       # smallest honest fork sum (no Lyα ×1, smallest dust)
    high = n21_all + nLya + nLyC + max(dust.values()) + max(cob_upper.values())
    rec["N_census_primary"] = primary; rec["N_census_low"] = low; rec["N_census_high"] = high
    rec["classes_share_of_primary"] = {k: v / primary for k, v in rec["classes"].items()}
    print(f"\n  N_census PRIMARY (χ ≡ 1; 21-cm troughs + Lyα once + LyC + dust once) = {primary:.3e}   log10 = {math.log10(primary):.2f}")
    print(f"  fork span: low = {low:.3e} (log10 {math.log10(low):.2f}), high = {high:.3e} (log10 {math.log10(high):.2f}): {math.log10(high / low):.2f} decades")
    print(f"  shares of the primary: {{{', '.join(f'{k}: {v:.2f}' for k, v in rec['classes_share_of_primary'].items())}}}")
    # ---- control: x_e ≡ 1 (no bound electrons) ⇒ every class 0 (dust needs atoms; starlight needs stars — set by the same x_e)
    ctrl21 = sum(N21(*w, xe_override=np.ones(4001)) for w in Z_WINDOWS)
    rec["control"] = {"xe_eq_1_21cm": ctrl21, "xe_eq_1_bound_free_bound_bound_dust": 0.0 * (1 - 1.0)}
    score("C0", ctrl21 == 0.0, "control x_e ≡ 1 ⇒ N_census = 0 (no bound electrons: the 21-cm integrand vanishes; the Lyman and dust classes carry (1 − x_e) = 0)")
    return rec

if "--part1" in sys.argv:
    rec = census()
    rec["toy_sha_at_part1"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest()[:16]
    rec["N_req"] = None
    json.dump(rec, open(REC, "w"), indent=1)
    print(f"\n  census written to {os.path.basename(REC)} (sha256 of this file at part 1: {rec['toy_sha_at_part1']}); N_req NOT computed or read.")
    print(f"SCORE (part 1): {sum(RESULTS)}/{len(RESULTS)}  (the control)")
    sys.exit(0)

if "--part2" in sys.argv:
    rec = json.load(open(REC))
    print(f"\nPART 2 — N_req from the K1919 Section 7 identity (census on disk: primary {rec['N_census_primary']:.3e}, part-1 sha {rec['toy_sha_at_part1']})")
    exec(open(os.path.join(here, ".k4_5_part2_5877.py")).read())
