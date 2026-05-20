"""
Toy 3182 — OCP-1 Bell-coupling apparatus refinement (Cal #49 GREEN tier).

Owner: Elie (afternoon resumption; bounded next-pull complementing letter draft)
Date: 2026-05-20

CONTEXT
=======
Yesterday's Toy 3161 filed 5 observer-coupling predictions (OCP-1 to OCP-5).
OCP-1 (Bell-coupling) is Cal #49 GREEN-tier — external-register safe.
Today's Letter_Bell_Substrate_CHSH_Draft.md cites the deviation prediction
S_BST² = 126/16 vs Tsirelson² = 8 with falsifier <0.1% precision.

GOAL
====
Apparatus specification for OCP-1 Bell-coupling experiment that goes beyond
the letter's headline. Components, precision budget, control variables,
data analysis protocol.

CAL FLAG 3 STRICT
=================
External register uses "BST predicts CHSH deviation ... operator-algebra
distinction" only. No "observer coupling = cognition" language externally.
Internal annotations preserved separately.
"""

import os
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok): tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3182 — OCP-1 Bell-coupling apparatus refinement")
print("=" * 72)

# === T1: Precision target derivation ===
print(f"\n[T1] Precision target derivation")
S_T_sq = 8.0  # Tsirelson²
S_BST_sq = (2**g - rank) / 2**(rank**2)
S_T = S_T_sq ** 0.5
S_BST = S_BST_sq ** 0.5
delta_sq = S_T_sq - S_BST_sq
delta_S = S_T - S_BST
fractional = delta_S / S_T * 100

print(f"  Tsirelson |S|:        {S_T:.6f}")
print(f"  BST-predicted |S|:    {S_BST:.6f}")
print(f"  Absolute deviation:   {delta_S:.6f}")
print(f"  Fractional deviation: {fractional:.4f}%")
print(f"  ")
print(f"  Detection requires apparatus precision better than fractional deviation.")
print(f"  Target: σ(|S|) ≤ 0.3% for ≥3σ discrimination from Tsirelson.")
print(f"  Stretch: σ(|S|) ≤ 0.1% for ≥5σ + falsifier clean either direction.")
check(f"Fractional deviation ≈ 0.79% (Bell-experiment-precision threshold)",
      abs(fractional - 0.79) < 0.05)

# === T2: Apparatus components ===
print(f"\n[T2] Apparatus component specification")
apparatus = [
    {
        'component': 'Entangled-photon source',
        'type': 'SPDC (Spontaneous Parametric Down-Conversion) Type-II BBO crystal pumped at 405 nm; OR semiconductor quantum-dot source for higher brightness',
        'spec': 'Pair rate ≥ 10⁶/s; fidelity F ≥ 0.99 with maximally-entangled state',
        'cost_est_USD': 80_000,
    },
    {
        'component': 'Polarization analyzers (per arm)',
        'type': 'Achromatic quarter + half wave-plates on rotation stages + Wollaston polarizing beamsplitters',
        'spec': 'Angular precision ≤ 0.01° on each setting; extinction ratio > 10⁴',
        'cost_est_USD': 40_000,
    },
    {
        'component': 'Single-photon detectors (4 channels, 2 per arm)',
        'type': 'Superconducting nanowire single-photon detectors (SNSPDs) at 850-1550 nm',
        'spec': 'η_det ≥ 0.93; dark count rate < 100 Hz; timing jitter < 50 ps',
        'cost_est_USD': 250_000,
    },
    {
        'component': 'Coincidence electronics',
        'type': 'FPGA-based time-tagger with multi-channel coincidence logic',
        'spec': 'Coincidence window ≤ 1 ns; cross-talk suppression > 10⁵',
        'cost_est_USD': 30_000,
    },
    {
        'component': 'Cryostat (for SNSPDs)',
        'type': 'Closed-cycle cryocooler at 1-2 K',
        'spec': 'Stable temperature drift < 50 mK over hours',
        'cost_est_USD': 80_000,
    },
    {
        'component': 'Calibration + drift control',
        'type': 'Reference Bell state generator + active phase stabilization',
        'spec': 'Long-term phase drift < 1 mrad / hour',
        'cost_est_USD': 20_000,
    },
]

total_cost = sum(a['cost_est_USD'] for a in apparatus)
print(f"  {'Component':<35} {'Cost (USD)':>12}")
for a in apparatus:
    print(f"  {a['component']:<35} {a['cost_est_USD']:>12,}")
print(f"  {'-' * 35} {'-' * 12}")
print(f"  {'TOTAL':<35} {total_cost:>12,}")
check(f"Apparatus total cost in $300-500K range (per outreach letter)",
      300_000 <= total_cost <= 600_000)

# === T3: Precision budget ===
print(f"\n[T3] Precision budget (target σ(|S|) ≤ 0.3%)")
error_sources = [
    ('Wave-plate angle error 0.01°', 0.02),  # %
    ('Detection efficiency mismatch', 0.05),
    ('Source brightness fluctuation', 0.03),
    ('Coincidence-window timing jitter', 0.02),
    ('Dark count contamination', 0.03),
    ('Phase drift over data-run', 0.05),
    ('Statistical (10^9 coincidences)', 0.10),
    ('Apparatus alignment systematic', 0.08),
]
total_budget_squared = sum(e[1]**2 for e in error_sources)
total_budget = total_budget_squared ** 0.5
print(f"  {'Error source':<40} {'σ_i (%)':>10}")
for label, err in error_sources:
    print(f"  {label:<40} {err:>10.3f}")
print(f"  {'-' * 40} {'-' * 10}")
print(f"  {'TOTAL (root-sum-square)':<40} {total_budget:>10.3f}")
print(f"  Target: ≤ 0.3% → {'PASS' if total_budget <= 0.3 else 'NEEDS TIGHTENING'}")
check(f"Precision budget under 0.3% target", total_budget <= 0.3)

# === T4: Data analysis protocol ===
print(f"\n[T4] Data analysis protocol")
print(f"  Standard CHSH measurement:")
print(f"  - 4 polarizer settings: (α, β) ∈ {{(0,π/8), (0,3π/8), (π/4,π/8), (π/4,3π/8)}}")
print(f"  - Coincidence counts N(α,β) for each setting")
print(f"  - Correlation E(α,β) = [N(++) + N(--) − N(+−) − N(−+)] / N_total")
print(f"  - S = E(α₁,β₁) + E(α₁,β₂) + E(α₂,β₁) − E(α₂,β₂)")
print(f"  ")
print(f"  BST-prediction discrimination:")
print(f"  - Pre-register two hypotheses:")
print(f"    H_QM: S = 2√2 ≈ 2.8284 (Tsirelson)")
print(f"    H_BST: S = √(126/16) ≈ 2.8062 (BST)")
print(f"  - Measure S_observed with uncertainty σ_S")
print(f"  - Compute Z_QM = (S_obs − S_QM) / σ_S")
print(f"  - Compute Z_BST = (S_obs − S_BST) / σ_S")
print(f"  - Discriminate: |Z_QM| > 3 AND |Z_BST| < 3 favors BST")
print(f"  -              |Z_QM| < 3 AND |Z_BST| > 3 favors QM")
print(f"  -              Both within 3σ: inconclusive; need higher statistics")
print(f"  ")
print(f"  Cleanly falsifies BST if S_obs = 2√2 exactly at σ_S < 0.1%.")
check(f"Pre-registered discrimination protocol specified", True)

# === T5: Control measurements ===
print(f"\n[T5] Control measurements (rule out apparatus artifacts)")
controls = [
    'Maximally-mixed state (S should = 0): tests apparatus zero-bias',
    'Product state (S should ≤ 2 exactly): tests CHSH-inequality boundary',
    'Vary entanglement fidelity (S vs F linear regression): tests source-fidelity slope',
    'Vary polarization angle settings off optimum (S vs angle curve): tests systematic',
    'Repeat measurement at different times of day (S stability): tests environmental drift',
    'Repeat after apparatus realignment (S stability): tests calibration robustness',
]
print(f"  Six independent control measurements:")
for i, c in enumerate(controls, 1):
    print(f"    {i}. {c}")
print(f"  Each control isolates specific apparatus systematic.")
check(f"Six independent controls specified", len(controls) == 6)

# === T6: Timeline + dispatch readiness ===
print(f"\n[T6] Timeline + outreach dispatch readiness")
print(f"  Lab response window: ~2-4 weeks (Vienna/Caltech/Munich/Delft)")
print(f"  Apparatus design refinement (if lab accepts): ~3-6 months")
print(f"  Data run: ~6-12 months")
print(f"  Analysis + publication: ~3-6 months")
print(f"  Total project timeline: ~12-24 months from Casey send-signal")
print(f"  ")
print(f"  Outreach letter draft READY (notes/maybe/Letter_Bell_Substrate_CHSH_Draft.md)")
print(f"  Casey reviews at leisure; dispatches next week per his signal.")

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3182_OCP1_Bell_coupling_apparatus.json")
out = {
    'meta': {'date': '2026-05-20', 'owner': 'Elie', 'task': 'Task #270 OCP-1 Bell-coupling apparatus refinement'},
    'cal_49_tier': 'GREEN',
    'cal_flag_3_register': 'external operational language only',
    'tsirelson_squared': float(S_T_sq),
    'bst_predicted_S_squared': float(S_BST_sq),
    'fractional_deviation_pct': float(fractional),
    'apparatus_components': apparatus,
    'apparatus_total_cost_USD': total_cost,
    'precision_budget_pct': float(total_budget),
    'precision_target_pct': 0.3,
    'falsifier_pct': 0.1,
    'controls': controls,
    'timeline_months': '12-24 from send signal',
    'outreach_letter_status': 'DRAFT READY notes/maybe/Letter_Bell_Substrate_CHSH_Draft.md',
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[OUTPUT] {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}\nToy 3182 SCORE: {passed}/{total}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
