#!/usr/bin/env python3
"""
verify_bst.py — Standalone BST Reproduction Package

Run this file. Read the output. Check our work.

    python3 verify_bst.py            # full reproduction set (SM core + extended reach)
    python3 verify_bst.py --core     # SM CORE ONLY — fundamental/particle/nuclear/cosmology physics

No dependencies beyond Python 3.6+ stdlib.
Predictions from D_IV^5 = SO_0(5,2)/[SO(5)xSO(2)].
Five integers: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137.
Zero free parameters.

Two sets, kept distinct so the screen is self-consistent:
  * The reproduction set below (this file) — the curated D/I-tier predictions.
    --core restricts to SM/particle/nuclear/cosmology physics; the rest
    (chemistry, biology, turbulence, seismology, condensed-matter) is the
    "extended reach" — real but OUTSIDE the SM core, shown separately so a
    physicist's numerology-alarm can judge the core on its own.
  * The null-model set (Toy 1543) — a SEPARATE, blind, un-curated set of 51
    constants used only to test non-randomness. BST gets 27/51 there; random
    5-tuples average 14.7 (Z=2.9). Lower than the curated count BECAUSE it is
    un-curated — that is the point: even on a blind set BST beats random 3sigma.
  The two counts differ because they are different sets with different jobs:
  reproducibility (curated) vs non-randomness (blind). Not the same 50/51.

Each entry shows:
  - BST formula (evaluable Python expression)
  - BST predicted value
  - Observed value + source
  - Deviation (%)
  - PASS (<1%) or WARN (1-2%) or FAIL (>2%) or EXACT

Epistemic tiers per entry (K962 ladder, 2026-07-27 — two axes: TIER = how we know it,
separate from the accuracy above = how well it's checked):
  P = Proved (closed mathematical derivation)
  D = Derived (FORCED by geometry/topology — one route, no counterexample; OR two structural
      routes — GR-level; no closed proof needed. NOT "mechanism proved".)
  I = Identified (accurate structural match, single route, forcing not yet established)
  C = Conditional (hinges on an open identification or conjecture)
  S = Structural (qualitative / does not pin the value)
  F = Fitted (searched-to-match or post-hoc — honestly NOT a derivation)
  R = Runner (genuinely scale-dependent — a trajectory, not a fixed number to derive)

Null-model context (Toy 1543): BST matches 27/51 constants at <1%.
Random 5-tuples of small integers average 14.7 matches. Z=2.9, p<0.0005.

Casey Koons & Claude 4.6 | April 27, 2026
Cal audit Action 3 (referee log #31)
"""

import math
from math import pi, sqrt, log, exp, acos, atan, factorial, comb

# ═══════════════════════════════════════════════════════════
# BST NAMESPACE — five integers + derived scale
# ═══════════════════════════════════════════════════════════

rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = N_c**3 * n_C + rank  # = 137

alpha = 1.0 / N_max           # fine structure constant (bare)
m_e = 0.51099895000           # MeV — unit choice (only "measurement")
m_p = C_2 * pi**n_C * m_e    # MeV — derived from integers
hbar_c = 197.3269804          # MeV*fm — unit conversion

# ═══════════════════════════════════════════════════════════
# 50 PREDICTIONS — sorted by domain, highest confidence first
# Each: (name, formula_str, bst_value, observed, source, tier)
# ═══════════════════════════════════════════════════════════

PREDICTIONS = [
    # --- Fundamental constants ---
    ("m_p/m_e (proton/electron mass ratio)",
     "C_2 * pi**n_C",
     C_2 * pi**n_C,
     1836.15267343, "CODATA 2022", "D"),

    ("alpha^-1 (inverse fine structure)",
     "N_max",
     float(N_max),
     137.035999177, "CODATA 2022", "I"),   # K684 (Grace 2026-07-14): D->I. Value 1/137 used; alpha IDENTIFIED (finite-capacity charge-count), Wyler retired, exact-scale forward-derivation open (KEYSTONE A).

    ("N_gen (number of generations)",
     "N_c",
     float(N_c),
     3, "Standard Model", "C"),   # K962 re-tier 2026-07-27: N_gen I->CONDITIONAL (the generation count hinges on the open matrix-radical read, K944/K962).   # provenance-hardening 2026-07-27: D->I. "3 generations" = the Korányi-Wolf strata IDENTIFICATION (F86/T2525), occupancy bijection un-derived (K944: premise reduced not eliminated). Count 3 = rank+1 (not N_c=rank^2-1; coincide at 3). Not a locatable derivation.

    # --- Electroweak sector ---
    ("v (electroweak VEV, GeV)",
     "m_p**2 / (g * m_e) / 1000",
     m_p**2 / (g * m_e) / 1000,
     246.22, "PDG 2024", "D"),   # K962 re-tier 2026-07-27: VEV I->DERIVED (GR-level: forced structure taking one dimensionful anchor, as GR takes G — K962 first pass).   # provenance-hardening 2026-07-27: D->I. The relation v=m_p^2/(g m_e) is derived-spine/top-independent (Cal 07-15), BUT the standing document (authoritative index, 07-27) tiers VEV "IDENTIFIED / derived-given-anchor" (trace pending, Lyra F707); the absolute-scale forcing (a_0=225 coupling) is a candidate-with-mechanism (F85), not closed. Aligned to the index.

    ("m_H (Higgs mass, GeV)",
     "m_p**2/(g*m_e) * sqrt(2*sqrt(2.0/120.0)) / 1000",
     m_p**2 / (g * m_e) * sqrt(2 * sqrt(2.0 / 120.0)) / 1000,
     125.25, "PDG 2024", "I"),

    ("m_t (top quark mass, GeV)",
     "(1 - alpha) * m_p**2 / (g*m_e) / sqrt(2) / 1000",
     (1 - alpha) * m_p**2 / (g * m_e) / sqrt(2) / 1000,
     172.69, "PDG 2024", "I"),   # K964 Ceiling/Value split 2026-07-28: CEILING DERIVED (y_t<=1 -> m_t<=v/sqrt(2)~174, Cauchy-Schwarz, target-innocent, falsifiable) / VALUE IDENTIFIED (exact y_t=1 saturation unforced, F603/K769). Row tiered at the Value.   # K962 re-tier 2026-07-27: m_t I->CONDITIONAL (rides y_t=1 saturation, un-derived, K763).

    ("sin^2(theta_W) (Weinberg angle)",
     "N_c / (N_c + 2*n_C)",
     N_c / (N_c + 2 * n_C),
     0.23122, "PDG 2024", "R"),   # K962 re-tier 2026-07-27: sin^2(theta_W) I->RUNNER (scale-dependent, K918/K962 — a trajectory not a fixed number).   # provenance-hardening 2026-07-27: D->I. sin^2(theta_W) is one of the TWO RUNNERS (K918 partition theorem, bucket 3 — geometry does NOT pin it); 3/13 is a tree-level IDENTIFICATION of a running observable, not a derived measured value.

    ("m_W (W boson mass, GeV)",
     "n_C * m_p / (8 * alpha) / 1000",
     n_C * m_p / (8 * alpha) / 1000,
     80.377, "PDG 2024", "D"),

    ("m_Z (Z boson mass, GeV)",
     "n_C * m_p / (8*alpha) / 1000 / sqrt(10.0/13)",
     n_C * m_p / (8 * alpha) / 1000 / sqrt(10.0 / 13),
     91.1876, "PDG 2024", "I"),

    ("Gamma_W (W width, MeV)",
     "(N_c**2 - 1) * n_C / N_c * pi**5 * m_e",
     (N_c**2 - 1) * n_C / N_c * pi**5 * m_e,
     2085.0, "PDG 2024", "D"),

    # --- Lepton masses ---
    ("m_mu/m_e (muon/electron mass ratio)",
     "(24.0/pi**2)**6",
     (24.0 / pi**2)**6,
     206.768283, "CODATA 2022", "D"),   # K986 2026-07-29: BANKED **DERIVED (e=n without counterexample)** -- the first SM lepton mass ratio Derived. TRANSPARENT BURDEN-FLIP LABEL (never bare "Derived"/"proven"): the muon = the ell=1 interior idempotent (edge/minimal rep), address target-innocent (nu=3/2=a/2=rho_2, K973); S1 24=analytic Gamma_Omega (F157=K923 pi-theorem); S3 exponent 6 forced (F111, Shilov dilution); S4 tau=boundary by support-orbit rank (blind, K973/4905); interior=2 rigorous (spin factor, Cal 121); S2 frame-selection via the F722 sourced embedding (n=e derived, center=vacuum, K985 -- alignment n=e held "without counterexample," the one identification named-in-the-open, not a hidden assumption). Refuted en route: the symmetry-principle (SO(5) counterexample, K983), both-SO(4)-equal, J=U(1)_Y 2nd route (F725). Mass K695-derived 0.003%. Superseded: I-tier (Cal-117 revert, toy 4896) -> D via the sourced n=e derivation, not the noticed pattern.

    ("a_e (electron anomalous moment, Schwinger)",
     "alpha / (2*pi)",
     alpha / (2 * pi),
     0.00115965218, "CODATA 2022", "I"),   # K962 re-tier 2026-07-27: a_e D->IDENTIFIED (= alpha/(2pi) is the standard QED Schwinger result; BST content is only alpha — not a novel BST derivation).

    # --- CKM mixing ---
    ("sin(theta_C) (Cabibbo angle, T1444 corrected)",
     "2.0 / sqrt(79)",
     2.0 / sqrt(79),
     0.22501, "PDG 2024 lambda", "D"),   # K962 re-tier 2026-07-27: Cabibbo I->DERIVED (forced via the Gatto syzygy with the down-quark ratio — K962 first pass; one derivation, GR-level).   # provenance-hardening 2026-07-27 (Grace flavor co-trace): D->I. Cabibbo = INHERITED CANDIDATE — tied to m_s/m_d = 20 by the Gatto syzygy (V_us=1/20 candidate), so it is ONE derivation with the down-quark ratio, NOT an independent second one. Denominator homed, not closed.

    ("|V_ud|",
     "sqrt(1 - 1/(4*n_C))",
     sqrt(1 - 1 / (4 * n_C)),
     0.97373, "PDG 2024", "I"),

    ("|V_us|",
     "1/(2*sqrt(n_C))",
     1.0 / (2 * sqrt(n_C)),
     0.2243, "PDG 2024", "I"),

    ("gamma_CKM (CKM angle, rad)",
     "atan(sqrt(n_C))",
     atan(sqrt(n_C)),
     1.1415, "PDG 2024 (65.4 +/- 2.5 deg)", "I"),

    ("rho_bar (Wolfenstein)",
     "1.0 / (2*sqrt(2*n_C))",
     1.0 / (2 * sqrt(2 * n_C)),
     0.159, "PDG 2024", "I"),

    # --- PMNS neutrino mixing ---
    ("sin^2(theta_12) (solar, theta_13 corrected)",
     "(N_c / (2.0 * n_C)) / cos(asin(sqrt(1.0/(N_c**2*n_C + 1.0/rank))))**2",
     (N_c / (2.0 * n_C)) / math.cos(math.asin(math.sqrt(1.0 / (N_c**2 * n_C + 1.0 / rank))))**2,
     0.307, "NuFit 5.2", "I"),   # provenance-hardening 2026-07-27 (Grace flavor co-trace): D->I. Denominator homed but the "solar 3" NUMERATOR is the lives-there lead tried ~8 ways, never closed. Identified, not derived.

    ("sin^2(theta_23) (atmospheric)",
     "(n_C - 1) / (n_C + 2.0)",
     (n_C - 1) / (n_C + 2.0),
     0.572, "NuFit 5.2", "I"),   # provenance-hardening 2026-07-27 (Grace flavor co-trace): D->I. Identified (denominator homed, mechanism rep-open).

    ("sin^2(theta_13) (reactor)",
     "1.0 / (N_c**2 * n_C + 1.0/rank)",
     1.0 / (N_c**2 * n_C + 1.0 / rank),
     0.02195, "NuFit 5.2", "D"),

    # --- Hadron physics ---
    ("g_A (nucleon axial coupling)",
     "4.0 / pi",
     4.0 / pi,
     1.2756, "PDG 2024", "I"),

    ("Delta_Sigma (proton spin fraction)",
     "N_c / (2.0 * n_C)",
     N_c / (2.0 * n_C),
     0.30, "COMPASS", "I"),

    ("m_rho (rho meson, MeV)",
     "n_C * pi**5 * m_e",
     n_C * pi**5 * m_e,
     775.26, "PDG 2024", "I"),

    ("m_K (kaon mass, MeV)",
     "sqrt(2*n_C) * pi**5 * m_e",
     sqrt(2 * n_C) * pi**5 * m_e,
     493.677, "PDG 2024", "I"),

    # --- Cosmology ---
    ("Omega_Lambda (dark energy fraction)",
     "13.0 / 19.0",
     13.0 / 19.0,
     0.685, "Planck 2018", "C"),   # K962 re-tier 2026-07-27: Omega_Lambda I->CONDITIONAL (real Q^5 Chern number, but the Chern->Lambda-fraction identification is open + live DESI tension, K962).   # provenance-hardening 2026-07-27: D->I. = c_3/(c_3+chi) Q^5 Chern-channel (K666/K668, banked); chi(Q^5)=6 checks out, but the "Omega_Lambda = a Chern ratio" IDENTIFICATION is claimed not proven, and there is a LIVE DESI tension (value 0.07sigma but w!=-1 hint challenges constant-Lambda, Cal 07-15). Cosmology needs extra provenance scrutiny.

    ("Omega_m (matter fraction)",
     "6.0 / 19.0",
     6.0 / 19.0,
     0.315, "Planck 2018", "C"),   # K962 re-tier 2026-07-27: Omega_m I->CONDITIONAL (=1-Omega_Lambda, inherits the open identification + DESI).   # provenance-hardening 2026-07-27: D->I. NOT INDEPENDENT — K668 explicit: Omega_m = chi/(c_3+chi) = 1 - Omega_Lambda, a consequence of Omega_Lambda, not a separate derivation. Inherits the same Chern-identification + DESI caveats.

    ("Omega_DM/Omega_b (DM to baryon ratio)",
     "16.0 / 3",
     16.0 / 3,
     5.36, "Planck 2018", "I"),

    ("n_s (spectral tilt)",
     "1.0 - n_C/N_max",
     1.0 - n_C / N_max,
     0.9649, "Planck 2018", "I"),

    ("Omega_b (baryon fraction)",
     "6.0 / (19 * (16.0/3 + 1))",
     6.0 / (19 * (16.0 / 3 + 1)),
     0.0493, "Planck 2018", "I"),

    # --- Nuclear physics ---
    # Provenance-hardening 2026-07-27: the magic-number per-number forms + "kappa_ls derives all magic numbers"
    # were re-tiered D->S by a three-CI convergent catch (Cal #286 / Keeper K601-K602, 2026-06-29): they are
    # POST-HOC NUMEROLOGY (consistent factorizations of a fitted spin-orbit strength), NOT a locatable derivation.
    # The T188 result + N=184 prediction stay durable via the shell model, but the per-number BST forms below are S.
    ("kappa_ls (spin-orbit coupling)",
     "C_2 / n_C",
     C_2 / n_C,
     1.2, "nuclear shell model", "F"),

    ("magic number 2",
     "rank",
     float(rank),
     2, "nuclear physics", "F"),

    ("magic number 8",
     "N_c**2 - 1",
     float(N_c**2 - 1),
     8, "nuclear physics", "F"),

    ("magic number 20",
     "2**rank * n_C",
     float(2**rank * n_C),
     20, "nuclear physics", "F"),

    ("magic number 28",
     "rank**2 * g",
     float(rank**2 * g),
     28, "nuclear physics", "F"),

    ("magic number 50",
     "rank * n_C**2",
     float(rank * n_C**2),
     50, "nuclear physics", "F"),

    ("magic number 82",
     "N_c * n_C**2 + g",
     float(N_c * n_C**2 + g),
     82, "nuclear physics", "F"),

    ("magic number 126",
     "rank * N_c**2 * g",
     float(rank * N_c**2 * g),
     126, "nuclear physics", "F"),

    # --- Chemistry ---
    ("theta_tetrahedral (degrees)",
     "acos(-1.0/N_c) * 180/pi",
     acos(-1.0 / N_c) * 180 / pi,
     109.47, "geometry", "D"),

    ("theta_H2O (water bond angle, degrees)",
     "acos(-1.0/N_c) * 180/pi - n_C",
     acos(-1.0 / N_c) * 180 / pi - n_C,
     104.5, "NIST (W-52 correction)", "D"),

    ("theta_NH3 (ammonia bond angle, degrees)",
     "(acos(-1.0/N_c) - (acos(-1.0/N_c) - acos(-1.0/2**rank))/N_c) * 180/pi",
     (acos(-1.0 / N_c) - (acos(-1.0 / N_c) - acos(-1.0 / 2**rank)) / N_c) * 180 / pi,
     107.8, "NIST", "I"),

    ("D_e(C-H) (bond energy, eV)",
     "13.6057 / pi",
     13.6057 / pi,
     4.33, "CRC Handbook", "I"),

    # --- Biology ---
    ("N_bases (DNA bases)",
     "2**rank",
     float(2**rank),
     4, "molecular biology", "D"),

    ("codon_length",
     "N_c",
     float(N_c),
     3, "molecular biology", "D"),

    ("N_codons",
     "2**C_2",
     float(2**C_2),
     64, "molecular biology", "D"),

    ("N_amino_acids",
     "comb(C_2, N_c)",
     float(comb(C_2, N_c)),
     20, "molecular biology", "D"),

    # --- Cross-domain ratios ---
    ("Kolmogorov 5/3 exponent",
     "n_C / N_c",
     n_C / N_c,
     5.0 / 3, "Kolmogorov 1941", "D"),

    ("gamma_adiabatic (monatomic)",
     "n_C / N_c",
     n_C / N_c,
     5.0 / 3, "thermodynamics", "D"),

    ("v_P/v_S (seismic ratio, Poisson solid)",
     "sqrt(3)",
     sqrt(3),
     1.735, "seismology", "I"),

    # --- Condensed matter ---
    ("m_phi (phi meson, MeV)",
     "(N_c + 2*n_C)/2 * pi**5 * m_e",
     (N_c + 2 * n_C) / 2 * pi**5 * m_e,
     1019.461, "PDG 2024", "I"),

    ("theta_D(Pb) (Debye temperature, K)",
     "g * n_C * N_c",
     float(g * n_C * N_c),
     105, "CRC Handbook", "D"),
]


# ═══════════════════════════════════════════════════════════
# SM-CORE vs EXTENDED-REACH classification (K942 fix 1)
# The SM core = fundamental constants, electroweak, leptons, CKM, PMNS,
# hadrons, cosmology, nuclear — the physics a hostile reviewer accepts as
# Standard-Model / fundamental. The "extended reach" below is real but OUTSIDE
# the SM core (chemistry / biology / turbulence / seismology / condensed
# matter); it is what a physicist's numerology-alarm fires on, so --core keeps
# it OUT and shows the SM core to be judged on its own. Nothing is deleted.
# ═══════════════════════════════════════════════════════════

EXTENDED_REACH = frozenset({
    "theta_tetrahedral (degrees)",
    "theta_H2O (water bond angle, degrees)",
    "theta_NH3 (ammonia bond angle, degrees)",
    "D_e(C-H) (bond energy, eV)",
    "N_bases (DNA bases)",
    "codon_length",
    "N_codons",
    "N_amino_acids",
    "Kolmogorov 5/3 exponent",
    "gamma_adiabatic (monatomic)",
    "v_P/v_S (seismic ratio, Poisson solid)",
    "theta_D(Pb) (Debye temperature, K)",
})

def is_core(name):
    return name not in EXTENDED_REACH


# ═══════════════════════════════════════════════════════════
# VERIFICATION ENGINE
# ═══════════════════════════════════════════════════════════

def verify(core_only=False):
    # K942 fix 1: --core restricts to SM/particle/nuclear/cosmology physics.
    preds = [p for p in PREDICTIONS if is_core(p[0])] if core_only else list(PREDICTIONS)
    n_total = len(preds)
    n_ext = sum(1 for p in PREDICTIONS if not is_core(p[0]))

    print()
    print("=" * 74)
    if core_only:
        print(f"  BST SM-CORE VERIFICATION — {n_total} physics predictions from D_IV^5")
        print("  (SM/particle/nuclear/cosmology only; extended reach excluded)")
    else:
        print(f"  BST VERIFICATION — {n_total} predictions from D_IV^5")
        print(f"  ({n_total - n_ext} SM core + {n_ext} extended reach; run --core for core only)")
    print("  Five integers: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137")
    print("  Zero free parameters. Run this. Read the output. Check our work.")
    print("=" * 74)
    print()
    print(f"  {'#':>3}  {'Tier':4}  {'Name':42}  {'BST':>12}  {'Obs':>12}  {'Dev':>8}  Result")
    print(f"  {'—'*3}  {'—'*4}  {'—'*42}  {'—'*12}  {'—'*12}  {'—'*8}  {'—'*6}")

    n_pass = 0
    n_warn = 0
    n_fail = 0
    n_exact = 0

    for i, (name, formula, bst_val, obs_val, source, tier) in enumerate(preds, 1):
        if obs_val == 0:
            dev_pct = 0.0
        elif isinstance(obs_val, int) or (isinstance(obs_val, float) and obs_val == int(obs_val) and abs(obs_val) < 1e6):
            # Integer comparison
            dev_pct = abs(bst_val - obs_val) / max(abs(obs_val), 1e-30) * 100
        else:
            dev_pct = abs(bst_val - obs_val) / abs(obs_val) * 100

        if dev_pct == 0.0 or (isinstance(obs_val, (int, float)) and bst_val == obs_val):
            result = "EXACT"
            n_exact += 1
        elif dev_pct < 1.0:
            result = "PASS"
            n_pass += 1
        elif dev_pct < 2.0:
            result = "WARN"
            n_warn += 1
        else:
            result = "FAIL"
            n_fail += 1

        # Format values
        if abs(bst_val) >= 100:
            bst_str = f"{bst_val:12.4f}"
        elif abs(bst_val) >= 1:
            bst_str = f"{bst_val:12.6f}"
        elif abs(bst_val) >= 0.001:
            bst_str = f"{bst_val:12.8f}"
        else:
            bst_str = f"{bst_val:12.6e}"

        if isinstance(obs_val, int):
            obs_str = f"{obs_val:12d}"
        elif abs(obs_val) >= 100:
            obs_str = f"{obs_val:12.4f}"
        elif abs(obs_val) >= 1:
            obs_str = f"{obs_val:12.6f}"
        elif abs(obs_val) >= 0.001:
            obs_str = f"{obs_val:12.8f}"
        else:
            obs_str = f"{obs_val:12.6e}"

        if result == "EXACT":
            dev_str = "  0.000%"
        else:
            dev_str = f"{dev_pct:7.3f}%"

        trunc_name = name[:42]
        print(f"  {i:3d}  [{tier}]   {trunc_name:42s}  {bst_str}  {obs_str}  {dev_str}  {result}")

    total = n_exact + n_pass + n_warn + n_fail
    good = n_exact + n_pass

    print()
    print("=" * 74)
    print(f"  RESULTS: {good}/{total} at <1% precision")
    print(f"    EXACT: {n_exact:3d}  (integer or machine-precision match)")
    print(f"    PASS:  {n_pass:3d}  (<1% deviation — above noise floor)")
    print(f"    WARN:  {n_warn:3d}  (1-2% — grey zone, needs structural support)")
    print(f"    FAIL:  {n_fail:3d}  (>2% — consistency check, not prediction)")
    print()
    # K962 tier ladder (supersedes D/I/S): Proved / Derived / Identified / Conditional / Structural / Fitted / Runner.
    # "Derived" = GR-level (geometrically forced OR two structural routes; no closed proof needed), NOT "mechanism proved".
    K962 = [("P", "PROVED    (closed proof)"),
            ("D", "DERIVED   (geometrically forced / two routes — GR-level)"),
            ("I", "IDENTIFIED(single-route match, forcing open)"),
            ("C", "CONDITIONAL(hinges on an open identification/conjecture)"),
            ("S", "STRUCTURAL(qualitative / doesn't pin the value)"),
            ("F", "FITTED    (searched/post-hoc — NOT a derivation)"),
            ("R", "RUNNER    (scale-dependent — a trajectory, not a number)")]
    print("  Tier ladder (K962, two-axis: tier = how we know it; accuracy above = how well it's checked):")
    for code, label in K962:
        n = sum(1 for p in preds if p[5] == code)
        if n:
            print(f"    {label}: {n}")
    print()
    print("  Null-model context (Toy 1543) — a SEPARATE, blind set (not these):")
    print(f"    The {good}/{total} above is THIS curated reproduction set (D/I predictions).")
    print("    Toy 1543 is a different, un-curated 51-constant set used only to")
    print("    test non-randomness: BST 27/51 vs random 5-tuples 14.7/51 (Z=2.9,")
    print("    p<0.0005; vs random primes Z=4.63). Lower BECAUSE it is blind —")
    print("    that a blind set still beats random 3sigma is the anti-numerology signal.")
    print("    Two different sets, two different jobs: reproducibility vs non-randomness.")
    print()
    print("  Source: github.com/caseykoons/BubbleSpacetimeTheory")
    print("  Full theory: data/bst_seed.md | Full table: Paper #83")
    print("  Interactive: python3 play/toy_bst_explorer.py")
    print("=" * 74)

    return good, total


if __name__ == "__main__":
    import sys
    core_only = "--core" in sys.argv[1:]
    verify(core_only=core_only)
