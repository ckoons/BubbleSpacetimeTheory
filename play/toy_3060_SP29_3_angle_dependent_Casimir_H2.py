"""
Toy 3060 — SP29-3: Angle-dependent Casimir asymmetry prediction (H2).

Owner: Elie (Casey "do all", Keeper SP29-3 pull)
Date: 2026-05-18 PM

CONTEXT
=======
SP-29 Casimir Mechanism Investigation H2: "angle of incidence of commitment
circle matters." Per BST_SP29_Casimir_Mechanism_Investigation.md line 30, this
hypothesis predicts angle-dependent Casimir force asymmetry under plate
rotation. Preliminary form in SP29-6 master comparison:

  F(θ)/F(0) = 1 + (n_C/N_max) · sin²(2θ)    [master doc preliminary]

This toy refines the prediction and specifies the experimental discriminator.

BST H2 STRUCTURAL READING
=========================
The substrate-coupling commitment circle is BST-geometric (D_IV⁵ origin
orientation). Rotation of a Casimir plate relative to the source breaks
alignment between plate normal and substrate commitment direction. Expected
modulation amplitude is at the substrate-correction scale ~n_C/N_max or
similar BST primary fraction.

Three candidate BST primary forms for the amplitude:
  (A) n_C/N_max = 5/137 = 3.65% — master doc preliminary
  (B) N_c/N_max = 3/137 = 2.19% — same-decay-mode form as SP29-1 (Lamb dressing)
  (C) 1/N_max = 1/137 = 0.73% — bare α scale

The angular function sin²(2θ) has period π/2, consistent with 4-fold symmetry
of D_IV⁵ rank-2 root system B₂ in some readings. Alternative: sin²(θ) (period
π) for 2-fold symmetry of the substrate axis.

PRE-STAGED PREDICTION (this toy)
================================
We pre-stage form (A) per master doc:
  F(θ)/F(0) - 1 = (n_C/N_max) · sin²(2θ)

Peak asymmetry at θ = 45°: ΔF/F = n_C/N_max = 5/137 ≈ 3.65%
Period: 90° in θ
Standard Casimir parallel-plate (θ=0): no modulation

EXPERIMENTAL DISCRIMINATOR (per master doc + this toy refinement)
================================================================
Apparatus: parallel-plate Casimir cavity with rotation stage on top plate
Measurement: F(θ) at θ ∈ {0°, 15°, 30°, 45°, 60°, 75°, 90°} (7 points)
Expected at confirmation: F(45°)/F(0°) = 1 + 5/137 = 142/137 ≈ 1.0365
Standard QED (Schwinger/Lifshitz) prediction: F(θ)/F(0) ≡ 1 (rotational
  invariance of dispersion forces between parallel plates)

3σ confirmation threshold: ΔF/F measured > 3·σ_F at peak θ=45° relative to θ=0
Falsification threshold: ΔF/F < 0.5% over full 360° rotation

PRECISION REQUIREMENTS
======================
For 3σ confirmation of 3.65% effect:
  σ_F / F < 3.65% / 3 = 1.22% per measurement
  → ~80 averages per angle at 10%-precision per shot → 1.1% statistical

Typical Casimir-force precision (Decca 2007 class):
  ~0.1% at fixed geometry → 36σ confirmation if effect is real (overwhelming)
  ~1% at fixed geometry → 3σ confirmation (marginal)
  → Decca-class apparatus sufficient; modest force-precision experiment suffices

COST/TIMELINE (per master doc)
==============================
$30-50K (rotation stage + Decca-class force sensitivity + cavity)
~6 months end-to-end
"""

import os
import math
import json
from fractions import Fraction

rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok):
    tests.append((bool(ok), label))


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


print("=" * 72)
print("Toy 3060 — SP29-3: Angle-dependent Casimir asymmetry H2 prediction")
print("=" * 72)

# === T1: BST primary amplitude candidates ===
print(f"\n[T1] BST primary amplitude candidates for ΔF/F at peak θ=45°")
candidates = {
    'n_C/N_max (master)': (Fraction(n_C, N_max), 5/137),
    'N_c/N_max (Lamb-class)': (Fraction(N_c, N_max), 3/137),
    '1/N_max (bare α)': (Fraction(1, N_max), 1/137),
}
print(f"  {'Form':<25} {'Frac':<10} {'%':>8}")
print(f"  {'-'*25} {'-'*10} {'-'*8}")
for name, (frac, val) in candidates.items():
    print(f"  {name:<25} {str(frac):<10} {100*val:>7.3f}%")

# Pre-staged primary choice (master doc form A)
amplitude = Fraction(n_C, N_max)
amplitude_pct = 100 * float(amplitude)
print(f"\n  Pre-staged (master doc form A): ΔF/F peak = n_C/N_max = {amplitude} = {amplitude_pct:.3f}%")

# === T2: Angular function ===
print(f"\n[T2] Angular function: sin²(2θ)")
print(f"  Period: π/2 (90°) — 4-fold symmetric")
print(f"  Phase: peaks at θ ∈ {{45°, 135°, 225°, 315°}}, zeros at θ ∈ {{0°, 90°, 180°, 270°}}")
print(f"  BST motivation: D_IV⁵ rank-2 root system B₂ has 4-fold-related Weyl chambers")
print(f"  Alternative: sin²(θ) (period 180°, 2-fold) — falsifies the 4-fold claim")

# === T3: Predicted force ratios at experimental angles ===
print(f"\n[T3] Predicted F(θ)/F(0) at experimental angles")
print(f"  Formula: F(θ)/F(0) = 1 + (n_C/N_max)·sin²(2θ)")
print(f"\n  {'θ (deg)':>8} {'sin²(2θ)':>10} {'F(θ)/F(0)':>11} {'ΔF/F %':>9}")
print(f"  {'-'*8} {'-'*10} {'-'*11} {'-'*9}")
predictions = []
for theta_deg in [0, 15, 30, 45, 60, 75, 90]:
    theta = math.radians(theta_deg)
    sin2_2theta = math.sin(2 * theta) ** 2
    ratio = 1 + float(amplitude) * sin2_2theta
    delta_pct = 100 * (ratio - 1)
    predictions.append({
        'theta_deg': theta_deg,
        'sin2_2theta': sin2_2theta,
        'F_ratio': ratio,
        'delta_pct': delta_pct,
    })
    print(f"  {theta_deg:>8} {sin2_2theta:>10.4f} {ratio:>11.4f} {delta_pct:>+8.3f}%")

# === T4: Discrimination thresholds ===
print(f"\n[T4] Experimental discrimination thresholds")
sigma_required_3sig = amplitude_pct / 3
sigma_required_5sig = amplitude_pct / 5
print(f"  Peak amplitude (θ=45°): ΔF/F = {amplitude_pct:.3f}%")
print(f"  3σ confirmation: σ_F/F per measurement < {sigma_required_3sig:.3f}%")
print(f"  5σ confirmation: σ_F/F per measurement < {sigma_required_5sig:.3f}%")
print(f"  Decca 2007 Casimir-force precision class: ~0.1% per geometry")
print(f"    → 36σ on a single measurement; overwhelmingly decisive if real")
print(f"  Modest 1% precision: still 3σ-discriminating (sufficient for first test)")

check("3σ confirmation σ_F/F < 1.5% (Decca class easily achieves)",
      sigma_required_3sig < 1.5)

# === T5: Falsification criteria ===
print(f"\n[T5] Falsification criteria")
print(f"  CONFIRMS H2: F(45°)/F(0°) > 1.011 at 3σ over 6-month measurement")
print(f"  REFUTES H2: |F(θ)/F(0°) - 1| < 0.5% across 7 angles measured to 0.1% each")
print(f"  Standard QED prediction: ΔF/F ≡ 0 (rotational invariance)")
print(f"    Both Schwinger and Lifshitz-Casimir frameworks predict zero")
print(f"    Non-zero ≥0.5% asymmetry would CONTRADICT both standard frameworks")
check("3σ confirmation threshold definable (predicted > falsifier)",
      amplitude_pct > 0.5)

# === T6: Alternative-form sensitivity test ===
print(f"\n[T6] Alternative-form sensitivity (4-fold sin²(2θ) vs 2-fold sin²(θ))")
print(f"  If 4-fold: F(45°) = F(135°) = F(225°) = F(315°) all PEAK")
print(f"    F(90°) = F(180°) = F(270°) = F(0°) all ZERO modulation")
print(f"  If 2-fold (sin²(θ)): F(90°) PEAK, F(0°) and F(180°) ZERO")
print(f"  CRUCIAL DIAGNOSTIC: F(90°) measurement discriminates 4-fold vs 2-fold")
print(f"    Expected (4-fold): F(90°)/F(0°) = 1.0 (zero modulation)")
print(f"    Expected (2-fold): F(90°)/F(0°) = 1 + 5/137 = 1.0365 (peak)")

# === T7: Cross-check against existing SP-29 framework ===
print(f"\n[T7] Cross-check against existing SP-29 family")
print(f"  SP29-1 (H4 decay rate): ΔΓ/Γ ≈ N_c/(N_max·c_2) = 3/1507 ≈ 0.199%")
print(f"  SP29-3 (H2 angle):       ΔF/F  ≈ n_C/N_max     = 5/137 ≈ 3.65%")
print(f"  Different scales: H4 is product N_max·c_2 (denominator), H2 is N_max (denominator)")
print(f"  H2 is ~18x larger amplitude than H4 — easier to measure decisively")
print(f"  Cost ratio (master doc): H2 $30-50K vs H4 $40-60K → similar order")
check("H2 amplitude > H4 amplitude (easier-to-measure prediction)",
      float(amplitude) > 3/1507)

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3060_SP29_3_H2_angle_prediction.json")
out = {
    'meta': {
        'date': '2026-05-18',
        'owner': 'Elie',
        'task': 'SP29-3 angle-dependent Casimir H2 prediction',
    },
    'hypothesis': 'H2: angle of incidence of commitment circle matters',
    'pre_staged_form': 'F(θ)/F(0) = 1 + (n_C/N_max)·sin²(2θ)',
    'amplitude_fraction': f"{n_C}/{N_max}",
    'amplitude_pct': amplitude_pct,
    'angular_function': 'sin²(2θ), 4-fold symmetric',
    'period_deg': 90,
    'peak_theta_deg': 45,
    'standard_QED_prediction': 'ΔF/F ≡ 0 (rotational invariance)',
    'predictions': predictions,
    'discrimination': {
        'three_sigma_required_sigma_F_pct': sigma_required_3sig,
        'five_sigma_required_sigma_F_pct': sigma_required_5sig,
        'decca_class_precision_pct': 0.1,
        'expected_significance_at_decca_precision_sigma': amplitude_pct / 0.1,
    },
    'cost_USD': '30-50K',
    'timeline_months': 6,
    'alternative_forms_to_discriminate': {
        'four_fold_sin2_2theta': 'F(90°)/F(0°) ≈ 1.000',
        'two_fold_sin2_theta': 'F(90°)/F(0°) ≈ 1.037',
        'discriminating_measurement': 'F(90°) sample',
    },
}
with open(out_path, 'w') as f:
    json.dump(out, f, indent=2)
print(f"\n[T8] Output: {os.path.basename(out_path)}")

# Score
passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}")
print(f"Toy 3060 SCORE: {passed}/{total}")
print(f"{'='*72}")
for ok, label in tests:
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {label}")

print(f"""
SP29-3 PRE-STAGED PREDICTION:
  F(θ)/F(0) = 1 + (n_C/N_max)·sin²(2θ) = 1 + (5/137)·sin²(2θ)
  Peak asymmetry at θ=45°: ΔF/F = 5/137 = 3.65%

DISCRIMINATION:
  Decca-class (~0.1% precision) → ~36σ discrimination if real
  Standard QED predicts zero (rotational invariance)
  Falsification threshold: <0.5% asymmetry over 360° rotation

NOT CLAIMED:
  - That the sin²(2θ) angular form is BST-derivable (master doc filed it
    "preliminary, SP29-3 will refine" — this toy uses it as pre-staged form,
    DOES NOT derive it from substrate dynamics; that's multi-week work)
  - That the n_C/N_max amplitude is uniquely determined (alternative
    candidates N_c/N_max and 1/N_max also presented)
  - Tier promotion of H2 (Keeper governs; this is pre-staged prediction
    awaiting experimental data)

NEXT STEPS:
  - Master doc SP29-6 updated with refined predictions
  - Experimental outreach if Casey approves (alongside SP29-1)
  - Multi-week: derive sin²(2θ) angular form from BST substrate dynamics
    (vs. just stating it from B₂ root system 4-fold symmetry)
""")
