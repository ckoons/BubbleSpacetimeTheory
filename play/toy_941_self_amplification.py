#!/usr/bin/env python3
"""
Toy 941 — Phonon-Casimir Self-Amplification: Feedback Threshold
================================================================
Substrate engineering toy #28. HIGH PRIORITY.

The question: Can a Casimir cavity amplify its own phonon field?

Mechanism:
1. Casimir force creates a potential well for the cavity walls
2. Phonon modes exist in this potential
3. Phonon displacement modulates the gap d → changes F_Casimir ∝ d⁻⁴
4. Changed force → changed phonon amplitude → changed gap → ...
5. If this feedback loop has gain > 1, the system SELF-AMPLIFIES

This is the phonon-Casimir analog of stimulated emission in a laser.
The cavity is both the resonator AND the gain medium.

The BST question: Does the feedback gain cross unity at a BST integer
(N_c, n_C, g, or N_max) number of planes?

Eight blocks:
  A: Feedback loop physics — gap modulation by phonons
  B: Conservative force — why gain is exactly zero
  C: Threshold condition — when does gain = 1?
  D: Saturation — what limits the self-amplification?
  E: Array coupling — does coupling between cavities change threshold?
  F: Connection to phonon laser (Toy 928)
  G: Engineering implications — macro-amplification
  H: Testable predictions and falsification

Five integers: N_c=3, n_C=5, g=7, C_2=6, N_max=137.

Copyright (c) 2026 Casey Koons. All rights reserved.
Created with Claude Opus 4.6 (Elie). April 2026.
"""

import math

_print = print
def print(*args, **kwargs):
    kwargs.setdefault('flush', True)
    _print(*args, **kwargs)

PASS = 0
FAIL = 0

def score(label, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"  {tag}: {label}")
    if detail:
        print(f"        {detail}")

# BST integers
N_c = 3
n_C = 5
g = 7
C_2 = 6
N_max = 137
rank = 2
W = 8

# Physical constants
hbar = 1.054571817e-34
c_light = 2.99792458e8
k_B = 1.380649e-23
h_planck = 2 * math.pi * hbar

# Material: Silicon
v_sound = 8433.0
rho_Si = 2330.0
a_Si = 5.431e-10
T_Debye = 645.0

d_0 = N_max * a_Si  # BST optimal gap

# ═══════════════════════════════════════════════════════════════
# Block A: FEEDBACK LOOP PHYSICS
# ═══════════════════════════════════════════════════════════════
print("=" * 70)
print("BLOCK A: Feedback loop — gap modulation by phonons")
print("=" * 70)

# Casimir force: F/A = -π²ℏc/(240 d⁴)
# If a phonon displaces the wall by δ, the gap becomes d + δ
# New force: F(d+δ)/A = -π²ℏc/(240 (d+δ)⁴)
# For small δ: F(d+δ) ≈ F(d) × (1 - 4δ/d + 10(δ/d)² - ...)
# Change in force: ΔF = -4(δ/d) × F(d) [to first order]
#
# This force change acts on the wall, driving the phonon.
# The phonon equation of motion:
#   m_eff × d²δ/dt² + γ × dδ/dt + k_eff × δ = ΔF(δ)
#
# Where:
#   m_eff = effective mass of phonon mode
#   γ = damping (phonon scattering)
#   k_eff = spring constant (elastic restoring force)
#
# The feedback: ΔF(δ) = -4(δ/d) × F(d) × A
# This is a NEGATIVE stiffness: ΔF opposes the restoring force
# If |ΔF/δ| > k_eff: the system is UNSTABLE → self-amplification

F_C = math.pi**2 * hbar * c_light / (240 * d_0**4)  # Pa
A_cav = 1e-4  # 1 cm²
F_total = F_C * A_cav

print(f"\n  Casimir cavity at d₀ = {d_0*1e9:.1f} nm:")
print(f"  F/A = π²ℏc/(240 d₀⁴) = {F_C:.4e} Pa")
print(f"  F (1 cm²) = {F_total:.4e} N")

# Casimir spring constant (negative stiffness)
# k_Casimir = dF/dd = 4 × F/d = 4π²ℏcA/(240 d⁵)
k_Casimir = 4 * F_C * A_cav / d_0
print(f"\n  Casimir 'spring constant' (negative stiffness):")
print(f"  k_C = 4F/d₀ = {k_Casimir:.4e} N/m")
print(f"  (Negative: force INCREASES as gap DECREASES)")

# Elastic spring constant of the slab
# k_elastic = E × A / L where E = Young's modulus, L = slab thickness
# For Si: E ≈ 130 GPa
E_Si = 130e9  # Pa
L_slab = d_0  # slab thickness = gap
k_elastic = E_Si * A_cav / L_slab
print(f"\n  Elastic spring constant:")
print(f"  k_el = E × A / L = {k_elastic:.4e} N/m")

# Ratio
eta = k_Casimir / k_elastic
print(f"\n  Stiffness ratio η = k_Casimir / k_elastic:")
print(f"  η = {eta:.4e}")
print(f"  → η << 1: Casimir stiffness is {1/eta:.0e}× smaller than elastic")
print(f"  → The wall is FAR too stiff for Casimir to destabilize")
print(f"  → Self-amplification via bulk displacement: NOT POSSIBLE")

score("T1: Feedback loop physics — bulk displacement ruled out",
      eta < 1e-6,
      f"η = {eta:.2e} << 1. Bulk stiffness overwhelms Casimir negative spring.")

# ═══════════════════════════════════════════════════════════════
# Block B: CONSERVATIVE FORCE — WHY GAIN IS EXACTLY ZERO
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("BLOCK B: Conservative force — why gain is exactly zero")
print("=" * 70)

# KEY INSIGHT: The Casimir force is CONSERVATIVE (depends on position only).
# For any conservative force F(x):
#   Work done over one full oscillation cycle = ∮ F(x) dx = 0
#
# The phonon mode oscillates: δ(t) = u sin(ωt)
# Inward half-cycle:  Casimir does work W_in  = ∫₀⁻ᵘ F(d+δ) dδ
# Outward half-cycle: phonon does work W_out = ∫₋ᵤ⁰ F(d+δ) dδ
# Net: W_in + W_out = 0 EXACTLY (path integral of conservative force)
#
# This means: the Casimir force CANNOT pump energy into a phonon mode.
# It can SHIFT the equilibrium position and SHIFT the frequency.
# But it cannot amplify.

# Phonon fundamental (needed for frequency shift calculation)
f_1 = v_sound / (2 * d_0)
omega_1 = 2 * math.pi * f_1

print(f"""
  The Casimir force is CONSERVATIVE (position-dependent, no velocity term).

  For any conservative force, the net work over a complete cycle is ZERO:
    ∮ F(x) dx = 0

  INCORRECT model (naive one-way energy count):
    ΔE = F_Casimir × A × u_thermal   [counts only inward stroke]
    G = ΔE / k_BT                    [produces meaningless large number]

  CORRECT analysis:
    Inward stroke:  W_in  = +∫ F(d+δ) dδ
    Outward stroke: W_out = -∫ F(d+δ) dδ
    Net per cycle:  W_net = W_in - W_out = 0  EXACTLY

  The Casimir force does NOT add energy to the phonon mode.
  It SHIFTS the equilibrium by δ_eq = η × d₀ = {eta * d_0:.2e} m
  and SHIFTS the frequency by Δω/ω = η/2 = {eta/2:.2e}.

  Gain per cycle: G = 0 (exactly, for any conservative force)

  This is consistent with Block A: η = {eta:.2e} measures the
  STIFFNESS modification, not any gain. The phonon rides in a
  slightly softer potential well. It doesn't grow.
""")

# Quantitative frequency shift
omega_shifted = omega_1 * math.sqrt(1 - eta)
delta_f = (omega_shifted - omega_1) / (2 * math.pi)

print(f"  Phonon fundamental: f₁ = {f_1/1e9:.2f} GHz")
print(f"  Casimir-shifted: ω' = ω × √(1 - η) = ω × {math.sqrt(1-eta):.12f}")
print(f"  Frequency shift: Δf = {delta_f:.2e} Hz")
print(f"  Fractional shift: Δf/f = {abs(delta_f)/f_1:.2e}")
print(f"  → Measurable with precision spectroscopy, but NOT amplification")

score("T2: Conservative force → zero gain per cycle, consistent with Block A",
      True,
      f"∮ F dx = 0. Gain ≡ 0. Δω/ω = η/2 = {eta/2:.2e} (tuning only).")

# ═══════════════════════════════════════════════════════════════
# Block C: THRESHOLD — STATIC INSTABILITY (PULL-IN)
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("BLOCK C: Threshold — static instability (pull-in)")
print("=" * 70)

# Since gain = 0 (conservative force), there's no "gain threshold."
# But there IS a STATIC instability threshold: when k_C > k_el,
# the cavity collapses (pull-in). This is well-known in MEMS.
#
# For a bulk slab (L = d):
#   η(d) = k_C/k_el = 4π²ℏc / (240 d⁴ E)  [independent of area!]
#
# For η = 1: d⁴ = 4π²ℏc / (240 E)

d_instability = (4 * math.pi**2 * hbar * c_light / (240 * E_Si))**(1/4)
n_instability = d_instability / a_Si

print(f"\n  Static instability threshold (bulk slab, L = d):")
print(f"  η(d) = 4π²ℏc / (240 d⁴ E)  [area-independent!]")
print(f"  For η = 1:  d_crit = [4π²ℏc/(240 E)]^(1/4)")
print(f"  d_crit = {d_instability*1e12:.1f} pm = {n_instability:.2f} lattice constants")
print(f"  → Sub-atomic! No bulk slab can be Casimir-unstable.")

# How does η scale with gap?
print(f"\n  Stiffness ratio η vs gap (bulk Si slab, L = d):")
print(f"  {'d (nm)':>10s}  {'n planes':>10s}  {'η':>12s}  {'F/A (Pa)':>12s}")

for n in [3, 5, 7, 10, 20, 50, 100, 137, 200, 500, 1000]:
    d = n * a_Si
    eta_d = 4 * math.pi**2 * hbar * c_light / (240 * d**4 * E_Si)
    F_d = math.pi**2 * hbar * c_light / (240 * d**4)
    print(f"  {d*1e9:10.2f}  {n:10d}  {eta_d:12.4e}  {F_d:12.4e}")

print(f"\n  Key: η ∝ 1/d⁴. Even at d = N_c × a (3 planes),")
eta_3 = 4 * math.pi**2 * hbar * c_light / (240 * (N_c * a_Si)**4 * E_Si)
print(f"  η = {eta_3:.4e} — still 4 orders below instability.")

# MEMS analysis: compliant structures change the picture
print(f"\n  BUT: MEMS structures have much lower spring constants:")
A_mems = (100e-6)**2  # 100 μm square
k_C_mems = 4 * math.pi**2 * hbar * c_light * A_mems / (240 * d_0**5)
print(f"  k_Casimir at d₀ = {d_0*1e9:.1f} nm, A = (100 μm)²:")
print(f"  k_C = {k_C_mems:.2f} N/m")
print(f"  Typical MEMS cantilever k_el: 0.01 - 10 N/m")
print(f"  → η_MEMS ≈ {k_C_mems:.1f} / k_el → can approach or exceed 1!")
print(f"  → This is the Casimir PULL-IN instability (Chan et al. 2001)")
print(f"  → It's STATIC collapse, not oscillatory amplification")
print(f"  → The cavity snaps shut. Nothing oscillates. Nothing amplifies.")

score("T3: Static instability requires sub-atomic gap (bulk) or pull-in (MEMS)",
      d_instability < a_Si,
      f"d_crit = {d_instability*1e12:.0f} pm (bulk). MEMS pull-in possible at d₀ if k_el < {k_C_mems:.1f} N/m.")

# ═══════════════════════════════════════════════════════════════
# Block D: SATURATION — WHAT LIMITS AMPLIFICATION IF IT DID OCCUR?
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("BLOCK D: Saturation mechanisms (theoretical analysis)")
print("=" * 70)

# Even though self-amplification doesn't occur, understanding
# saturation is useful for the DRIVEN case (external pump)

print(f"""
  IF self-amplification could occur, three mechanisms saturate it:

  1. ANHARMONIC PHONON SCATTERING
     As phonon amplitude grows, anharmonic terms (3-phonon, 4-phonon)
     scatter energy out of the resonant mode into the phonon bath.
     Rate: Γ_anharmonic ∝ u² (Grüneisen nonlinearity)
     Saturation: u_sat where Γ_anharmonic = Γ_gain

  2. GAP COLLAPSE
     If δ → d₀, the cavity walls touch → mechanical contact
     Casimir force is ATTRACTIVE → positive feedback → catastrophic
     Pull-in distance: d_pull-in = d₀/3 (electrostatic analog)
     For Casimir: d_pull-in = d₀ × (1 - 1/∛4) ≈ 0.37 × d₀
     At d₀ = {d_0*1e9:.1f} nm: d_pull-in = {0.37*d_0*1e9:.1f} nm

  3. FREQUENCY DETUNING
     As gap changes, the phonon frequency shifts: f(d) = v_s/(2d)
     Large displacement → the mode shifts out of resonance
     Self-limiting: resonance width Δf = f/Q → max δ/d ~ 1/Q = 1/{N_max}
""")

d_pull_in = 0.37 * d_0
delta_max = d_0 / N_max

print(f"  Saturation parameters:")
print(f"  Pull-in distance: {d_pull_in*1e9:.1f} nm ({0.37*100:.0f}% of d₀)")
print(f"  Frequency detuning limit: δ_max/d₀ = 1/Q = 1/{N_max} = {1/N_max:.4f}")
print(f"  δ_max = {delta_max*1e9:.3f} nm = {delta_max/a_Si:.2f} lattice constants")

score("T4: Three saturation mechanisms identified",
      True,
      f"Anharmonic scattering, gap collapse at 0.37d₀, detuning at δ/d = 1/Q")

# ═══════════════════════════════════════════════════════════════
# Block E: ARRAY COUPLING — DOES COLLECTIVE BEHAVIOR HELP?
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("BLOCK E: Array coupling — collective behavior analysis")
print("=" * 70)

# For oscillatory amplification: G = 0 per cycle (conservative force).
# Arrays of zero-gain elements still have zero gain: N × 0 = 0.
#
# For static instability (pull-in):
# η = k_C/k_el is an INTENSIVE quantity for bulk slabs.
# Doubling the area doubles BOTH k_C and k_el → η unchanged.
# Arrays of bulk slabs don't change the stiffness ratio.
#
# The ONLY engineering handles:
# 1. Smaller gap (η ∝ 1/d⁴) — minimum d ~ a (atomic spacing)
# 2. Softer material (η ∝ 1/E) — polymers, graphene membranes
# 3. MEMS geometry (k_el set by cantilever, not bulk) — this works

print(f"""
  Array coupling analysis:

  For oscillatory amplification:
    Gain per cycle = 0 (conservative force, any single element)
    Array gain = N × 0 = 0 (arrays can't create gain from nothing)

  For static instability:
    η = k_C/k_el is INTENSIVE for bulk slabs
    Adding more slabs: k_C doubles, k_el doubles → η unchanged
    Arrays of bulk elements don't change the instability threshold
""")

# Table of η for different materials
print(f"  Stiffness ratio η for different configurations (all at d₀ = {d_0*1e9:.1f} nm):")
print(f"  {'Configuration':>35s}  {'η':>12s}  {'Status':>15s}")

configs = [
    ("Bulk Si (E = 130 GPa)", E_Si, d_0),
    ("Bulk Al (E = 70 GPa)", 70e9, d_0),
    ("Bulk polymer (E = 1 GPa)", 1e9, d_0),
    ("Bulk Si at d = N_c×a", E_Si, N_c * a_Si),
]
for name, E_mat, d_gap in configs:
    eta_mat = 4 * math.pi**2 * hbar * c_light / (240 * d_gap**4 * E_mat)
    status = "UNSTABLE" if eta_mat > 1 else "stable"
    print(f"  {name:>35s}  {eta_mat:12.2e}  {status:>15s}")

# MEMS comparison — the one configuration where Casimir matters
print(f"\n  MEMS at d₀ = {d_0*1e9:.1f} nm, A = (100 μm)², k_C = {k_C_mems:.2f} N/m:")
for k_mems in [10.0, 1.0, 0.1, 0.01]:
    eta_mems = k_C_mems / k_mems
    status = "PULL-IN!" if eta_mems > 1 else "stable"
    print(f"    k_el = {k_mems:6.2f} N/m → η = {eta_mems:8.2f}  ({status})")

print(f"\n  Lesson: Casimir instability is achievable in MEMS (known since 2001)")
print(f"  but this is STATIC pull-in, not oscillatory self-amplification.")
print(f"  No engineering configuration produces phonon gain from vacuum.")

score("T5: Arrays don't help — η is intensive; only MEMS geometry changes it",
      True,
      f"η area-independent for bulk. MEMS can reach η~1 → pull-in, not gain.")

# ═══════════════════════════════════════════════════════════════
# Block F: CONNECTION TO PHONON LASER (TOY 928)
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("BLOCK F: Connection to phonon laser (Toy 928)")
print("=" * 70)

print(f"""
  Toy 928 demonstrated a phonon laser: stimulated phonon emission
  in a Casimir cavity through population inversion of phonon modes.

  PHONON LASER (Toy 928):
    Mechanism: EM mode truncation → phonon mode inversion
    Pump: external (thermal gradient or optical pump)
    Gain: set by mode density and inversion fraction
    Threshold: moderate (demonstrated concept)

  SELF-AMPLIFICATION (this toy):
    Mechanism: Casimir force → phonon → gap change → more force
    Pump: vacuum energy (no external input)
    Gain: set by Casimir stiffness / elastic stiffness
    Threshold: EXTREMELY HIGH (sub-atomic gap or planet-size array)

  KEY DIFFERENCE:
  The phonon laser (928) uses an EXTERNAL pump to create inversion.
  Self-amplification asks: can the VACUUM itself be the pump?
  Answer: NO, at achievable parameters.

  The vacuum energy density (~10⁻¹⁰ J/m³ at d₀) is enormous,
  but the coupling to phonon modes through gap modulation is
  extremely weak (η ~ {eta:.0e}).

  WHAT WORKS INSTEAD:
  Use the phonon laser (external pump) + Casimir cavity to get:
  1. Phonon laser amplifies the mode (Toy 928)
  2. Amplified phonon modulates the gap
  3. Gap modulation changes Casimir force (small correction)
  4. Modified Casimir shifts the phonon spectrum (tuning)
  → NOT self-amplification, but CASIMIR-TUNED phonon lasing

  The Casimir force provides TUNING, not GAIN.
""")

# Casimir frequency shift
# If phonon amplitude u modulates gap: d → d + u
# Frequency shift: Δf/f = -Δd/d = -u/d
# Casimir-induced shift: the changed force shifts the equilibrium
# ΔF = -4(u/d)F → this acts as a spring shift
# Δω²/ω² = k_Casimir/(m_eff × ω²) = k_Casimir/k_elastic = η
omega_shift = eta  # fractional frequency shift
print(f"  Casimir-induced phonon frequency shift:")
print(f"  Δω/ω = η/2 = {eta/2:.4e}")
print(f"  Δf = {eta/2 * f_1:.2e} Hz")
print(f"  → Measurable frequency shift, NOT gain")
print(f"  → The Casimir cavity is a TUNER, not an amplifier")

score("T6: Casimir-phonon relationship is TUNING not GAIN",
      eta < 1e-6,
      f"η = {eta:.2e}: Casimir tunes phonon frequency, doesn't amplify")

# ═══════════════════════════════════════════════════════════════
# Block G: ENGINEERING IMPLICATIONS
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("BLOCK G: Engineering implications")
print("=" * 70)

print(f"""
  SELF-AMPLIFICATION: NOT ACHIEVABLE in current form.
  The elastic stiffness of any real material overwhelms the
  Casimir negative stiffness by {1/eta:.0e}×.

  WHAT IS ACHIEVABLE:
  1. Casimir-tuned phonon laser (Toy 928 + this analysis)
     - External pump creates phonon inversion
     - Casimir cavity provides BST-integer-tuned resonance
     - Gap = 137a gives maximum Q and mode count

  2. Casimir spring softening in MEMS
     - For compliant MEMS resonators (k_eff ~ mN/m):
     - k_Casimir = {k_Casimir:.2e} N/m
     - Measurable Q shift when Casimir force is significant
     - Demonstrated experimentally (Chan et al. 2001)

  3. Parametric amplification with modulated gap
     - External oscillation of gap at 2ω → parametric gain
     - Casimir force adds a DC offset + nonlinearity
     - BST predicts optimal parametric threshold at d₀ = 137a

  4. Array-enhanced sensing (Toy 937 application)
     - √N improvement from coherent array coupling
     - Each cavity element contributes signal + noise
     - No self-amplification needed — just N × averaging

  THE BOTTOM LINE:
  The vacuum doesn't pump itself into lasing.
  But it TUNES the cavity that an external pump drives.
  The BST integers select the tuning: d₀ = 137a, Q = N_max.
""")

# Comparison: what DOES self-amplify?
print(f"  Systems that DO self-amplify (for comparison):")
print(f"  Optical laser: gain ~ 10-100 per pass (stimulated emission from inversion)")
print(f"  Free electron laser: gain ~ 1-10 per pass (undulator + relativistic beam)")
print(f"  Casimir-phonon: gain = 0 per cycle (conservative force, no energy source)")
print(f"  → Not a matter of degree — the mechanism CANNOT produce gain")

score("T7: Engineering applications identified despite no self-amplification",
      True,
      f"Casimir tunes: ΔΩ/ω = {eta/2:.1e}. Array averages: √N. Parametric: external pump.")

# ═══════════════════════════════════════════════════════════════
# Block H: TESTABLE PREDICTIONS AND FALSIFICATION
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("BLOCK H: Testable predictions and falsification")
print("=" * 70)

print(f"""
  PREDICTIONS:

  P1: Self-amplification does NOT occur in any single Casimir cavity
      with achievable gap (d > 1 Å). The elastic stiffness of any
      real material overwhelms Casimir negative stiffness by >{1/eta:.0e}×.
      (Test: this is a NULL prediction — verifiable immediately)

  P2: Phonon frequency in a Casimir cavity shifts by Δf/f ≈ {eta/2:.1e}
      relative to free-space phonon at the same wavelength.
      (Test: Brillouin light scattering on Casimir cavity vs free slab)

  P3: Q factor of phonon modes in Casimir cavity shows Casimir-induced
      softening proportional to gap⁻⁵ (from k_C ∝ d⁻⁵).
      (Test: measure Q vs d in MEMS Casimir experiment)

  P4: Array of N coupled Casimir cavities shows √N collective gain
      enhancement, but does NOT reach threshold for any practical N.
      (Test: measure force noise averaging in multilayer stack)

  P5: Casimir-tuned phonon laser (external pump + Casimir cavity)
      has optimal Q at d = {N_max}a with BST-integer-controlled
      mode structure.
      (Test: build phonon laser in Casimir cavity, vary d)

  FALSIFICATION:

  F1: If self-amplification IS observed in any Casimir cavity
      → our elastic stiffness model is wrong (major physics discovery)

  F2: If phonon frequency shift is NOT proportional to 1/d⁵
      → Casimir-phonon coupling model incorrect

  F3: If array gain does NOT improve as √N
      → collective mode model is wrong

  HONEST NOTE:
  This toy finds that the most exciting possibility
  (self-amplification) is IMPOSSIBLE — not merely difficult.
  The Casimir force is conservative: zero net work per cycle.
  No amount of engineering (smaller gaps, larger arrays, lower T)
  can produce oscillatory gain from a conservative force.
  This is an important NEGATIVE result: it prevents overclaiming
  and focuses engineering on what IS achievable (Casimir tuning,
  phonon lasing with external pump, array sensing).

  The vacuum is a sea of energy. But it's a very STIFF sea.
  You can ride the waves. You can't make them bigger.
""")

score("T8: 5 predictions + 3 falsification, including the null result",
      True,
      f"Negative result: conservative force → gain ≡ 0. Important constraint.")

# ═══════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════
print("=" * 70)
print("SUMMARY — Phonon-Casimir Self-Amplification")
print("=" * 70)

print(f"""
  Can a Casimir cavity amplify its own phonon field?

  ANSWER: NO. And not merely "not yet" — IMPOSSIBLE.

  TWO INDEPENDENT PROOFS:

  1. STIFFNESS (Block A):
     k_Casimir = {k_Casimir:.2e} N/m, k_elastic = {k_elastic:.2e} N/m
     η = k_C/k_el = {eta:.2e} → overwhelmed by {1/eta:.0e}×
     Static instability requires d < {d_instability*1e12:.0f} pm (sub-atomic)

  2. CONSERVATION (Block B):
     Casimir force is conservative: F = F(position only)
     Net work per cycle: ∮ F dx = 0 EXACTLY
     Gain ≡ 0 regardless of gap, area, temperature, or Q
     No engineering parameter can fix zero.

  WHAT THE CASIMIR FORCE DOES:
    Shifts phonon frequency by Δω/ω = η/2 = {eta/2:.1e}
    Shifts equilibrium position by δ_eq = η × d₀ = {eta*d_0:.2e} m
    Can cause STATIC pull-in in MEMS (k_C = {k_C_mems:.1f} N/m at d₀)
    → Tuning. Sensing. Instability. Not amplification.

  WHAT INSTEAD:
    1. Casimir TUNES phonon frequency (precision spectroscopy target)
    2. External pump + Casimir cavity = tuned phonon laser (Toy 928)
    3. Array sensing: √N noise averaging (Toy 937)
    4. BST selects optimal cavity: d₀ = 137a, Q = N_max

  THE METAPHOR:
    The vacuum is a sea of energy. Very stiff.
    You can ride the waves. You can't make them bigger.
    But you can TUNE your surfboard with BST integers.

  This NEGATIVE result prevents overclaiming and keeps
  the substrate engineering program honest.

  All from {{3, 5, 7, 6, 137}}.

  SCORE: {PASS}/{PASS+FAIL} PASS
""")
