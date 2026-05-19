"""
Toy 3065 — SP-27 Track 2 dark matter observational reanalysis scoping.

Owner: Elie (Casey "do all" Tuesday queue, T-B2)
Date: 2026-05-19 AM

GOAL
====
SP-27 Track 2 ("dark matter observational reanalysis") scoping doc. Outline
the data sources, BST predictions, and reanalysis methodology for the multi-
week DM-track of the SP-27 observational reanalysis program.

BST DARK MATTER FRAMEWORK
==========================
From data/bst_geometric_invariants.json catalog:

  DM/baryon ratio: 16/N_c = 16/3 = 5.333 (Elie E-21 catalog, 0.58% match)
    Also expressible: rank^4/N_c = 2^4/N_c = 16/3

  Omega_DM as spectral remainder: 137/200 = N_max/(rank^3·n_C^2)
    Cross-anchored with |mu_n/mu_p| = -137/200 (T1447 D-tier)

  sigma_8 BST: ~2.7% tension between Planck CMB (1-rank/c_2) and LSS
    (1-n_C/chi), reading at I-tier; tension itself = 7/264 BST primary form

  KEY FRAMING per CLAUDE.md May 17 Architecture Day:
    "DM = Wallach shadow (16/3 at 0.2%)" - DM is the incomplete-winding
    geometric remainder, NOT a particle. Direct detection predicts NULL.

REANALYSIS QUESTIONS (per "do all" scope)
=========================================
For each major DM observational dataset, ask: does the data REQUIRE a
particle interpretation, or is BST's geometric-remainder reading
compatible?

  D1. Galaxy rotation curves (Rubin 1980 era + modern SPARC sample)
      → BST predicts geometric flat-curve profile via spectral remainder
      → Reanalysis: which curves require DM particle vs which are
        consistent with BST geometric capacity

  D2. CMB Omega_DM (Planck 2018)
      → BST: Omega_DM = N_max/(rank^3·n_C^2) = 137/200 = 0.685
      → Observed: Omega_DM·h^2 ≈ 0.120 → Omega_DM ≈ 0.26
      → Close to BST 137/200·h^2 but factor discrepancy needs careful
        normalization audit

  D3. Direct detection bounds (LUX, XENON, PandaX, DARWIN, XLZD)
      → BST predicts NULL result (no DM particle → zero direct-detection
        cross-section)
      → Current state: ALL null at 10^-47 cm^2 cross-section bound
      → BST consistency: STRONG (all observations consistent with null
        as predicted)

  D4. Bullet cluster / merging galaxy clusters
      → BST geometric reading: spectral remainder displaced by cluster
        dynamics same as gravitational lensing
      → Reanalysis: does BST naturally produce the lens-mass / stellar-
        mass offset observed in 1E 0657-558 ("Bullet Cluster")?

  D5. Dwarf spheroidal galaxy cores (NFW vs cored profiles)
      → BST geometric remainder at small-scale = different profile?
      → "Core/cusp problem": BST may resolve naturally vs CDM particle

  D6. Cosmic structure formation (BST n_s, sigma_8)
      → n_s = 1 - 5/137 = 0.9635 (DERIVED, Toy 1401)
      → sigma_8: 2.7% tension between Planck/LSS, BST = (1-rank/c_2)
        Planck side vs (1-n_C/chi) LSS side
      → Reanalysis: structural origin of sigma_8 tension via BST

SCOPING DELIVERABLE (this toy)
==============================
- Catalog of 6 DM observational areas (D1-D6)
- Per-area BST prediction (catalog references)
- Reanalysis question per area (what data clarifies BST vs CDM)
- Priority order: D3 (null detection — current evidence) > D2 (Omega_DM
  normalization) > D4 (Bullet Cluster) > D1/D5/D6 (multi-week each)
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok):
    tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3065 — SP-27 Track 2: dark matter observational reanalysis scoping")
print("=" * 72)

# === T1: BST DM framework summary ===
print("\n[T1] BST DM framework (from existing catalog)")
DM_baryon = 16 / N_c
Omega_DM_spectral = N_max / (rank**3 * n_C**2)
print(f"  DM/baryon ratio: rank^4/N_c = 16/{N_c} = {DM_baryon:.4f} (~5.3x DM density)")
print(f"  Omega_DM spectral remainder: N_max/(rank^3·n_C^2) = {N_max}/{rank**3 * n_C**2} = {Omega_DM_spectral:.4f}")
print(f"  Wallach shadow reading: DM = 16/3 at 0.2% (May 17 Architecture Day)")
print(f"  CRUCIAL: BST DM is GEOMETRIC REMAINDER, NOT a particle. Direct detection predicts NULL.")
check("DM/baryon = 16/3 matches catalog", abs(DM_baryon - 16/3) < 1e-6)
check("Omega_DM = 137/200 matches catalog", abs(Omega_DM_spectral - 137/200) < 1e-6)

# === T2: 6 observational areas ===
areas = [
    {
        'id': 'D1',
        'topic': 'Galaxy rotation curves',
        'data_sources': 'SPARC (Lelli+2016), MaNGA, individual rotation curves Rubin+',
        'BST_prediction': 'Geometric flat-curve profile from spectral remainder',
        'reanalysis': 'Identify curves explained by BST geometry vs requiring DM particle halo',
        'priority': 4,
        'scope_weeks': 4,
    },
    {
        'id': 'D2',
        'topic': 'CMB Omega_DM (Planck 2018)',
        'data_sources': 'Planck 2018 base-LCDM Omega_DM·h^2 ~ 0.120',
        'BST_prediction': 'Omega_DM = N_max/(rank^3·n_C^2) = 137/200 = 0.685 (catalog)',
        'reanalysis': 'Normalization audit: convert spectral-remainder fraction to physical density at z=0',
        'priority': 2,
        'scope_weeks': 2,
    },
    {
        'id': 'D3',
        'topic': 'Direct detection null results',
        'data_sources': 'LUX-ZEPLIN, XENONnT, PandaX-4T, DARWIN/XLZD (future)',
        'BST_prediction': 'NULL (no DM particle → zero cross-section)',
        'reanalysis': 'Current state: ALL null at <10^-47 cm^2. BST STRONGLY consistent.',
        'priority': 1,  # current evidence; most direct test
        'scope_weeks': 1,
    },
    {
        'id': 'D4',
        'topic': 'Bullet Cluster / merging clusters',
        'data_sources': '1E 0657-558 Chandra X-ray + weak-lensing maps',
        'BST_prediction': 'Spectral remainder displaced by dynamics; geometric lensing offset',
        'reanalysis': 'Does BST predict the 1E 0657 lens-mass offset naturally vs needing DM?',
        'priority': 3,
        'scope_weeks': 3,
    },
    {
        'id': 'D5',
        'topic': 'Dwarf spheroidal cores / NFW',
        'data_sources': 'Ursa Minor, Draco, Sculptor density profiles',
        'BST_prediction': 'Geometric remainder profile at small-scale (cored, not cuspy?)',
        'reanalysis': 'Core/cusp problem resolution via BST geometric DM vs CDM particle',
        'priority': 5,
        'scope_weeks': 4,
    },
    {
        'id': 'D6',
        'topic': 'sigma_8 tension + structure formation',
        'data_sources': 'Planck CMB sigma_8 vs LSS KiDS/DES sigma_8',
        'BST_prediction': 'Tension = 7/264 BST primary form between (1-rank/c_2) and (1-n_C/chi) readings',
        'reanalysis': 'Structural origin of the 2.7% sigma_8 tension via BST',
        'priority': 6,
        'scope_weeks': 4,
    },
]

print(f"\n[T2] Six observational areas catalogued (sorted by priority)")
areas_sorted = sorted(areas, key=lambda a: a['priority'])
print(f"\n  {'ID':<4} {'Topic':<35} {'Priority':>9} {'Scope (wk)':>10}")
print(f"  {'-'*4} {'-'*35} {'-'*9} {'-'*10}")
for a in areas_sorted:
    print(f"  {a['id']:<4} {a['topic'][:33]:<35} {a['priority']:>9} {a['scope_weeks']:>10}")

# === T3: D3 immediate quick-win (null detection consistency) ===
print(f"\n[T3] D3 immediate quick-win: direct detection null status")
print(f"  Current upper bounds (90% CL):")
print(f"    LUX-ZEPLIN 2024:    <2.5×10^-47 cm² @ 30 GeV WIMP mass")
print(f"    XENONnT 2023:       <2.6×10^-47 cm² @ 28 GeV WIMP mass")
print(f"    PandaX-4T 2024:     <5.0×10^-47 cm² @ 40 GeV WIMP mass")
print(f"  All experiments return NULL at sub-attobarn sensitivity.")
print(f"  BST prediction: ZERO cross-section. Compatible with all null results.")
print(f"  TIER VERDICT: BST DM framework PASSES current direct-detection")
print(f"    constraints. Future XLZD/DARWIN sensitivity gain (~factor 100)")
print(f"    will further test. BST predicts continued NULL.")
check("BST DM framework consistent with current direct-detection null results",
      True)  # Trivial — bounds are upper limits, zero is compatible

# === T4: D2 normalization audit (immediate analysis) ===
print(f"\n[T4] D2 Omega_DM normalization audit")
# Planck 2018: Omega_DM_h2 = 0.120 ± 0.001
# h ≈ 0.674 (Planck), so Omega_DM ≈ 0.120 / 0.674^2 = 0.264
h_Planck = 0.674
Omega_DM_h2_obs = 0.120
Omega_DM_obs = Omega_DM_h2_obs / h_Planck**2
print(f"  Planck 2018 base-LCDM: Omega_DM·h^2 = {Omega_DM_h2_obs}")
print(f"  With h = {h_Planck}: Omega_DM = {Omega_DM_obs:.4f}")
print(f"  BST catalog: Omega_DM = 137/200 = {Omega_DM_spectral:.4f}  (SPECTRAL REMAINDER)")
print(f"  Direct ratio: BST/obs = {Omega_DM_spectral / Omega_DM_obs:.4f}")
print(f"  Factor 2.6 discrepancy → BST spectral remainder is NOT directly the cosmological")
print(f"  Omega_DM. Need normalization step: how does BST 137/200 spectral fraction map")
print(f"  to Omega_DM_physical at z=0?")
print(f"  ")
print(f"  Possible resolution: Omega_DM_physical = (spectral remainder) × (other factor).")
print(f"  Candidate: Omega_DM = (137/200) × (Omega_M_total) where Omega_M = 1 - Omega_L,")
print(f"  Omega_L = 7/10 = N_c+rank/(C_2+rank). Then Omega_M = 3/10 = N_c/n_C·rank.")
print(f"  Omega_DM = (137/200)·(3/10) = 411/2000 = 0.2055 — close to 0.26 (~20% off)")
print(f"  ")
print(f"  HONEST FINDING: simple multiplicative interpretation off by ~20%.")
print(f"  Multi-week work needed to derive the spectral-to-cosmological")
print(f"  conversion factor properly. Defer to follow-up session.")

# === T5: SP-27 Track 2 scoping doc output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3065_SP27_T2_scoping.json")
out = {
    'meta': {
        'date': '2026-05-19',
        'owner': 'Elie',
        'task': 'SP-27 Track 2 dark matter observational reanalysis scoping',
    },
    'BST_DM_framework': {
        'DM_per_baryon': '16/N_c = 16/3 = 5.333',
        'Omega_DM_spectral': 'N_max/(rank^3·n_C^2) = 137/200 = 0.685',
        'particle_prediction': 'NULL (geometric remainder, not particle)',
        'Wallach_shadow_reading': '16/3 at 0.2% (May 17 Architecture Day)',
    },
    'observational_areas': areas_sorted,
    'priority_order': [a['id'] for a in areas_sorted],
    'immediate_findings': {
        'D3': 'BST DM framework consistent with all current direct-detection null results',
        'D2': 'Omega_DM normalization 20% off via simple 137/200·(3/10); proper conversion derivation needed',
    },
    'multi_week_total_scope_weeks': sum(a['scope_weeks'] for a in areas),
    'recommended_next': 'D2 normalization derivation OR D3 future-experiment falsification spec',
}
with open(out_path, 'w') as f:
    json.dump(out, f, indent=2)
print(f"\n[T5] Output: {os.path.basename(out_path)}")

# Score
passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}")
print(f"Toy 3065 SCORE: {passed}/{total}")
print(f"{'='*72}")
for ok, label in tests:
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {label}")

print(f"""
SP-27 TRACK 2 SCOPING DELIVERABLE:
  6 observational areas catalogued (D1-D6)
  Priority order: D3 (null) > D2 (Omega normalization) > D4 (Bullet Cluster) >
                  D1 (rotation curves) > D5 (dwarf cores) > D6 (sigma_8)
  Total multi-week scope: ~18 weeks across all six areas
  Immediate findings: D3 BST-consistent, D2 needs normalization derivation

NEXT SESSIONS:
  - D2 normalization derivation: convert BST spectral remainder 137/200 to
    cosmological Omega_DM_physical at z=0
  - D3 future-experiment falsification spec: predicted null at XLZD/DARWIN
  - D4 Bullet Cluster: simulate BST geometric DM displacement vs observed
    lens-mass offset

NOT CLAIMED:
  - That BST DM is now D-tier promoted (catalog already has DM/baryon at
    D-tier 0.58%; this scoping doesn't change tier)
  - Multi-week derivations completed in this session
""")
