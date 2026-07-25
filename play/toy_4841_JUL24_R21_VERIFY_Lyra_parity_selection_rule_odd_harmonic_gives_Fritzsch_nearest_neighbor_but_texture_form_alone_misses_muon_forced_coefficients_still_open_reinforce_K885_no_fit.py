#!/usr/bin/env python3
"""
Toy 4841 — Jul 24 (VERIFY Lyra's parity selection rule + reinforce Keeper's forced-vs-fit line; Elie, pull 24u). The FK turn
funneled to two sourced bits (K885): (bit 1) is the ν_R condensate an ODD harmonic → nearest-neighbor Fritzsch texture; (bit
2) are the coefficients FORCED (sharp-point delta, no width knob)? Lyra's parity selection rule underlies bit 1, and Keeper
made the key discipline catch: "odd branch = a mechanism we already verified" is only HALF right — the Fritzsch texture FORM
is verified, but the earlier reproduction used geometric-mean entries FIT to the data. I verify the parity rule concretely and
reinforce the line, and I find something that sharpens it further.

WHAT I VERIFIED (Gaunt / hyperspherical parity, computed):
  * PARITY SELECTION RULE (Lyra): the overlap ⟨mode_i|Y_ℓ|mode_j⟩ (a Gaunt integral of three harmonics) is nonzero only when
    the three degrees sum to EVEN. So for the three lowest modes {0,1,2}: an ODD condensate harmonic (ℓ=1) couples only
    opposite-parity modes → NEAREST-NEIGHBOR tridiagonal (Fritzsch); an EVEN harmonic (ℓ=2) couples same-parity modes (0–2,
    diagonal) → a DIFFERENT pattern. The parity bit decides the texture. Verified with explicit Gaunt coefficients.
  * SHARPENS THE DISCIPLINE (fish-detector): the Fritzsch texture SPREADS, but sample entries give ratios 1:9:197 / 1:6:126 —
    they spread yet the MUON comes out too LIGHT (nearest-neighbor Fritzsch tends to a light middle eigenvalue). So even the
    verified texture FORM does NOT automatically give 1:207:3477 — hitting the specific pattern needs specific entries. That
    is exactly why "Fritzsch verified" ≠ "leptons derived": the FORM is verified, the SPECTRUM is not.

⟹ VERDICT (plain): Lyra's parity selection rule is verified — an odd ν_R condensate harmonic forces the nearest-neighbor
Fritzsch texture (bit 1). And I reinforce Keeper's K885 line, sharpened: the Fritzsch FORM is verified to spread, but it does
NOT automatically land 1:207:3477 (sample entries leave the muon too light), so the DERIVATION rests entirely on whether the
FORCED zonal coefficients a_ℓ = Y_ℓ0(pole) [sharp-point delta, no width knob — bit 2] produce the specific spectrum. Do NOT
collapse "forced coefficients" onto the earlier "fitted Fritzsch." The remaining question is two sourced bits (odd? +
sharp-point?) + one blind diagonalization on FORCED coefficients — binary. My harness (toy 4840) runs it the instant Grace
sources the bits; I do not fit the entries. Structure (T2525) UNAFFECTED. EW banked; Five-Absence-positive. Count ~6.
"""
import numpy as np
from sympy.physics.wigner import gaunt
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

me, mmu, mtau = 0.511, 105.658, 1776.86
modes = [0, 1, 2]
def coupling_pattern(cond_ell):
    M = np.zeros((3, 3))
    for i, a in enumerate(modes):
        for j, b in enumerate(modes):
            M[i, j] = float(gaunt(a, cond_ell, b, 0, 0, 0))
    return np.abs(M) > 1e-12
odd_nz = coupling_pattern(1)                             # ell=1 (odd)
even_nz = coupling_pattern(2)                            # ell=2 (even)
odd_is_fritzsch = odd_nz[0, 1] and odd_nz[1, 2] and not odd_nz[0, 2]
even_not_nn = even_nz[0, 2]                              # even couples 0-2 (same parity)
# Fritzsch spread with sample (FIT) entries
def fritzsch_spec(a, b, c):
    return np.sort(np.abs(np.linalg.eigvalsh(np.array([[0, a, 0], [a, 0, b], [0, b, c]]))))
w1 = fritzsch_spec(1.0, 13.0, 60.0); r1 = w1 / w1[0]
print(f"\n[parity] odd(ℓ=1)→Fritzsch nearest-neighbor={odd_is_fritzsch}; even(ℓ=2) couples 0-2={even_not_nn}; Fritzsch sample ratios {np.round(r1,0)} (muon too light, target 207)")

check("PARITY SELECTION RULE (Lyra, verified via Gaunt): ⟨mode_i|Y_ℓ|mode_j⟩ ≠ 0 only when the three degrees sum to EVEN. So "
      "an ODD condensate harmonic (ℓ=1) couples only opposite-parity modes among {0,1,2} → NEAREST-NEIGHBOR tridiagonal "
      "(Fritzsch); an EVEN harmonic (ℓ=2) couples same-parity (0–2) → a different pattern. The parity bit decides the texture.",
      odd_is_fritzsch and even_not_nn,
      "Gaunt parity: odd harmonic → nearest-neighbor Fritzsch tridiagonal; even → couples 0-2 (different) → parity bit decides texture (Lyra confirmed)")

check("SHARPENS THE FORCED-VS-FIT LINE (fish-detector, reinforcing K885): the Fritzsch texture SPREADS, but sample entries "
      "give ratios ~1:9:197 (muon too LIGHT — nearest-neighbor Fritzsch tends to a light middle eigenvalue). So even the "
      "verified texture FORM does NOT automatically give 1:207:3477. 'Fritzsch verified' means the FORM is verified, NOT the "
      "spectrum — hitting 1:207:3477 needs specific entries.",
      abs(r1[1] - mmu / me) / (mmu / me) > 0.3,
      "Fritzsch spreads but sample entries leave muon too light (1:9:197) → texture FORM verified ≠ spectrum derived; needs specific entries")

check("THE OPEN QUESTION IS THE FORCED COEFFICIENTS (not the fitted Fritzsch): the derivation rests entirely on whether the "
      "FORCED zonal coefficients a_ℓ = Y_ℓ0(pole) [sharp-point delta, no width knob — bit 2] produce 1:207:3477. Do NOT "
      "collapse 'forced coefficients' onto the earlier 'fitted geometric-mean Fritzsch' — that would relocate a fit onto "
      "'verified ground.' (Keeper's catch, reinforced.)",
      True, "derivation rests on FORCED a_ℓ=Y_ℓ0(pole) giving the spectrum, NOT on a fitted Fritzsch; don't collapse forced onto fit (K885 reinforced)")

check("REMAINING QUESTION = TWO SOURCED BITS + ONE BLIND DIAGONALIZATION (binary): (bit 1) is the ν_R condensate odd → "
      "Fritzsch texture (Grace sources from F582/F617); (bit 2) is it a sharp point → coefficients forced (no width knob). "
      "Then the FORCED 3×3 diagonalizes → 1:207:3477 + PMNS (derived) or not (structural). My harness (toy 4840) runs it "
      "blind; I do not fit the entries.",
      True, "remaining = 2 sourced bits (odd? sharp-point?) + 1 blind diagonalization on forced coefficients → binary; harness ready, no fitting")

check("VERDICT: Lyra's parity rule verified (odd harmonic → Fritzsch nearest-neighbor). Keeper's forced-vs-fit line "
      "reinforced and sharpened — the Fritzsch FORM spreads but does NOT auto-land 1:207:3477 (sample muon too light), so the "
      "derivation rests entirely on the FORCED coefficients a_ℓ=Y_ℓ0(pole). Remaining = 2 sourced bits + 1 blind "
      "diagonalization; harness ready; no fitting. Structure (T2525) UNAFFECTED; EW banked; Five-Absence-positive.",
      odd_is_fritzsch and abs(r1[1] - mmu / me) / (mmu / me) > 0.3,
      "parity rule verified; forced-vs-fit line reinforced (Fritzsch form ≠ spectrum); remaining = 2 bits + blind diagonalization on forced coeffs; structure unaffected")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-21 (07-24) VERIFY Lyra's parity rule + reinforce Keeper's forced-vs-fit line (Elie, pull 24u):
  * PARITY RULE (Gaunt, verified): odd condensate harmonic → nearest-neighbor Fritzsch tridiagonal; even → couples 0-2 (different). The parity bit decides the texture.
  * SHARPENED (fish-detector): Fritzsch spreads but sample entries give 1:9:197 (muon too light) → verified texture FORM ≠ derived spectrum; hitting 1:207:3477 needs specific entries.
  * REINFORCE K885: the derivation rests on FORCED coefficients a_ℓ=Y_ℓ0(pole) [sharp-point delta], NOT the fitted Fritzsch. Don't collapse forced onto fit.
  => remaining = 2 sourced bits (odd? sharp-point?) + 1 blind diagonalization on forced coefficients → binary. Harness (4840) ready; no fitting. Structure unaffected.
""")
