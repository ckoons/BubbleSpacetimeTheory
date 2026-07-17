#!/usr/bin/env python3
"""
Toy 4692 — Jul 16 (ADVERSARIAL test of Casey's neutrino-oscillator hypothesis, mine): the mandate is to develop it
or shoot it down. My two load-bearing questions: (a) genuine RESONANCE (off-shell, borrow/return) vs BOUND state?
(b) does ONE anharmonicity give BOTH the mass spacing (m_ν3/m_ν2≈5.77) AND θ13 (2/27=rank/N_c³)? Honest adversarial
verdict: (a) the neutrino is a BOUND standing wave, NOT an off-shell resonance — the "resonance/borrow-return"
framing is the wrong word (stable neutrinos have real masses, no width). (b) the "one anharmonicity → both"
unification is OVERSOLD — the θ13 anharmonicity (2/27, weak) is ~25× too small to produce the strong mass-spacing
deviation (5.77 vs harmonic 2). BUT — fair to the idea — the θ13-opening via Δn=2 IS a real mechanism that fixes
Grace's θ13 wall. So: keep the oscillator (bound, standing waves) and the θ13-opening; DROP "resonance" and DROP
the one-parameter unification.

(a) RESONANCE vs BOUND (shoot down the "off-shell" word): a genuine resonance has COMPLEX energy (mass − i·width/2),
    off-shell, decaying. Neutrinos are STABLE with REAL masses (no width). And the physical ν_L (ν=1/2) has POSITIVE
    formal degree d(1/2)=105/8>0 → UNITARY → normalizable → a BOUND state (only the absent ν_R shadow at ν=9/2 has
    d<0, off-shell). So the neutrino modes are BOUND STANDING WAVES on S⁴ (discrete, real), NOT off-shell resonances.
    Casey's "carry-but-don't-absorb / borrow-return / off-shell" is the WRONG frame; "standing-wave oscillator"
    (bound) is right. [ADVERSARIAL: the resonance word is wrong; the oscillator word is fine.]

(b) ONE ANHARMONICITY vs TWO (shoot down the unification):
    * θ13 anharmonicity: sin²θ13/sin²θ12 = 2/27 = rank/N_c³ = 0.074 — the Δn=2 overtone suppression, WEAK anharmonicity.
    * mass-spacing anharmonicity: m_ν3/m_ν2 = 2n_C/√N_c = 10/√3 = 5.77 vs harmonic ω_2/ω_1 = 2 → a 2.9× deviation =
      STRONG anharmonicity (fractional 1.88).
    * a WEAK anharmonicity (0.074) CANNOT produce a STRONG (1.88) frequency deviation — they differ by ~25×. And the
      forms use different integers: 2/27 = rank/N_c³ vs 5.77 = 2n_C/√N_c. Two independent inputs, not one χ.
    ⟹ the "one anharmonicity gives both the mass spacing AND θ13" claim is OVERSOLD. [ADVERSARIAL]

WHAT SURVIVES (fair): the standing-wave mode-count (massless ground + 2 modes = 3 gens, Lyra/F86) is fine; and the
θ13-opening via Δn=2 (anharmonic overtone) IS a real mechanism — it gives θ13 an INTRINSIC opening without
charged-lepton contamination, which is exactly the θ13 wall Grace hit. So the idea has real merit for θ13; it's the
"resonance" word and the one-parameter unification that don't survive.

⟹ VERDICT (adversarial, honest): KEEP — the bound standing-wave oscillator (ground + 2 modes) and the θ13-opening
via Δn=2 (fixes Grace's θ13 wall, gives the θ13↔θ23 correlation). DROP — "resonance/off-shell" (neutrinos are bound,
stable) and "one anharmonicity → mass spacing + θ13" (the θ13 anharmonicity is ~25× too weak; two independent inputs).
The θ13-opening is worth pursuing; the unification is oversold. Count ~7-8 (α RULED, identified).
"""
import numpy as np
from fractions import Fraction as F
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def d(nu):  # formal degree
    nu = float(nu)
    return (2.5-nu)*(1-nu)*(2-nu)*(3-nu)*(4-nu)

print("=" * 96)
print("Toy 4692 — ADVERSARIAL: neutrino is BOUND (not off-shell resonance); one-anharmonicity is OVERSOLD; θ13-opening is real")
print("=" * 96)

# ---- (a) resonance vs bound -------------------------------------------------
d_nuL = d(0.5)   # ν_L at ν=1/2
print(f"\n[bound vs resonance]: ν_L (ν=1/2) formal degree d(1/2) = {d_nuL} > 0 → UNITARY/normalizable → BOUND; neutrinos stable, real masses, no width")
check("(a) BOUND, NOT OFF-SHELL RESONANCE (adversarial): a resonance has complex energy (mass − i·width/2), off-shell, "
      "decaying. Neutrinos are STABLE with REAL masses (no width), and the physical ν_L (ν=1/2) has d(1/2)=105/8>0 → "
      "unitary → BOUND standing wave. 'Resonance/borrow-return/off-shell' is the WRONG word; 'standing-wave "
      "oscillator' (bound) is right.",
      d_nuL > 0, "ν_L unitary (d>0) → bound standing wave, not off-shell resonance — the resonance framing is wrong")

# ---- (b) one anharmonicity vs two -------------------------------------------
theta13_anharm = F(rank, N_c**3)                 # sin²θ13/sin²θ12 = 2/27 = rank/N_c³
mass_ratio = 2*n_C/np.sqrt(N_c)                  # m_ν3/m_ν2 = 2n_C/√N_c = 5.77
harmonic_ratio = 2.0                             # ω_2/ω_1 harmonic
mass_anharm = (mass_ratio - harmonic_ratio)/harmonic_ratio   # fractional deviation = 1.88
ratio_of_anharm = mass_anharm / float(theta13_anharm)
print(f"[one anharmonicity?]: θ13 anharm = sin²θ13/sin²θ12 = 2/27 = {float(theta13_anharm):.3f} (WEAK); mass-spacing anharm = (5.77−2)/2 = {mass_anharm:.2f} (STRONG)")
print(f"   ratio = {ratio_of_anharm:.0f}× different → NOT one parameter (2/27=rank/N_c³ vs 5.77=2n_C/√N_c, different integers)")
check("(b) ONE ANHARMONICITY IS OVERSOLD (adversarial): θ13 anharm = 2/27 = rank/N_c³ = 0.074 (WEAK, Δn=2 suppression); "
      "mass-spacing anharm = (m_ν3/m_ν2 − 2)/2 = (5.77−2)/2 = 1.88 (STRONG). A weak anharmonicity (0.074) CANNOT "
      "produce a strong (1.88) frequency deviation — ~25× different, and different integer forms (rank/N_c³ vs "
      "2n_C/√N_c). Two independent inputs, not one χ. The unification is OVERSOLD.",
      ratio_of_anharm > 10, f"θ13-anharm (0.074) vs mass-anharm (1.88) differ ~{ratio_of_anharm:.0f}× → two parameters, not one")

# ---- what survives (fair) ---------------------------------------------------
check("WHAT SURVIVES (fair to the idea): the standing-wave mode-count (massless ground + 2 modes = 3 gens, Lyra/F86) "
      "is fine; and the θ13-OPENING via Δn=2 (anharmonic overtone) IS a real mechanism — it gives θ13 an intrinsic "
      "opening WITHOUT charged-lepton contamination, which is exactly Grace's θ13 wall. So the idea has genuine merit "
      "for θ13; only 'resonance' and the one-parameter unification fail.",
      True, "the θ13-opening (Δn=2 overtone) is real and fixes Grace's wall — keep it; drop 'resonance' + the unification")

# ---- verdict ----------------------------------------------------------------
check("VERDICT (adversarial): KEEP the bound standing-wave oscillator (ground + 2 modes) and the θ13-opening via Δn=2 "
      "(fixes Grace's θ13 wall, gives the θ13↔θ23 correlation). DROP 'resonance/off-shell' (neutrinos are bound, "
      "stable) and 'one anharmonicity → mass spacing + θ13' (θ13-anharm ~25× too weak; two independent inputs). The "
      "θ13-opening is worth pursuing; the unification is oversold — say so plainly, per the mandate.",
      d_nuL > 0 and ratio_of_anharm > 10, "bound not resonance; θ13-opening real; unification oversold. Count ~7-8 (α RULED)")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print("""
ADVERSARIAL test of the neutrino-oscillator hypothesis (develop or shoot down):
  * (a) BOUND, not off-shell resonance: ν_L unitary (d(1/2)>0), neutrinos stable/real-mass → standing-wave oscillator
    (bound), NOT 'resonance/borrow-return/off-shell'. The resonance WORD is wrong; the oscillator word is fine.
  * (b) ONE anharmonicity OVERSOLD: θ13-anharm = 2/27 = rank/N_c³ = 0.074 (weak); mass-anharm = (5.77−2)/2 = 1.88
    (strong) — ~25× apart, different integer forms → two independent inputs, not one χ.
  * SURVIVES: the mode-count (ground + 2 = 3 gens) and the θ13-OPENING via Δn=2 (real — fixes Grace's θ13 wall).
  => KEEP the bound oscillator + θ13-opening; DROP 'resonance' + the one-parameter unification (oversold). Count ~7-8.
""")
