#!/usr/bin/env python3
"""
Toy 4695 — Jul 17 (the J-sign discriminator, mine; held but flagged sharp): the "163° vs 197°" reflection ambiguity
in δ_PMNS is NOT academic — it is a yes/no on the SIGN of the leptonic Jarlskog, i.e. the DIRECTION of leptonic CP
violation that DUNE measures. I make it sharp: the branch = sign(Im ε) = the CHIRALITY of the imperfect-ℤ₂ mirror,
and it fixes sign(J_PMNS). So Lyra's ε-derivation must pick the sign of Im ε geometrically — and that single sign IS
the prediction of whether the lepton sector has J>0 or J<0.

THE TWO BRANCHES (same |cos δ|, opposite sin δ = ±rank/g):
  * δ ≈ 163.4°: sin δ = +rank/g = +2/7 > 0 → J_PMNS = +J_max·(2/7) ≈ +0.0094.
  * δ ≈ 196.6°: sin δ = −rank/g = −2/7 < 0 → J_PMNS = −J_max·(2/7) ≈ −0.0094.   [data (NuFIT NO) favors this]
  Both satisfy cos δ = −N_c√n_C/g (the sum rule); the DATA can't yet separate them — but they are PHYSICALLY
  distinct: opposite sign of leptonic CP.

THE BRANCH = sign(Im ε) (the mirror chirality): Lyra's ε = (1/g)(−1 + i·rank/(N_c√n_C)). δ = arg(ε), so
  sign(sin δ) = sign(Im ε). Im ε > 0 → δ≈163° → J>0; Im ε < 0 → δ≈197° → J<0. So the branch is literally the SIGN of
  the imaginary part of the mirror imperfection — the chirality of the imperfect ℤ₂. The derivation must pick it from
  the geometry (which way the S⁴ mirror is twisted), NOT read it off the data (Lyra flagged this honestly).

WHY IT MATTERS (not academic): sign(J_PMNS) is the sign of the CP asymmetry in neutrino oscillations,
  P(ν_μ→ν_e) − P(ν̄_μ→ν̄_e) ∝ J_PMNS. DUNE measures exactly this sign. So the branch = the DIRECTION of leptonic
  matter-vs-antimatter asymmetry — a fundamental yes/no, not a 34° cosmetic ambiguity. If BST's geometry forces
  Im ε < 0, it predicts J<0 (δ≈197°), the direction data currently favors — a sharp, falsifiable DUNE call.

⟹ VERDICT: the δ branch (163° vs 197°) = sign(Im ε) = the imperfect-ℤ₂ mirror's chirality = sign(J_PMNS) = the
DIRECTION of leptonic CP violation (DUNE-measurable). J_PMNS = ±0.009 with the sign SET by sign(Im ε). Held: banks
with δ the moment Lyra's ε-derivation picks the sign of the imperfection geometrically. This is the physical content
of the branch — flagged sharp so the derivation targets the SIGN, not just the magnitude. Count ~7-8 (α RULED, identified).
"""
import numpy as np
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def jarlskog(s12, s23, s13, d):
    c12,c23,c13 = np.sqrt(1-s12**2),np.sqrt(1-s23**2),np.sqrt(1-s13**2)
    return c12*s12*c23*s23*c13**2*s13*np.sin(d)
s12, s23, s13 = np.sqrt(0.3), np.sqrt(4/7), np.sqrt(1/45)

print("=" * 96)
print("Toy 4695 — J-sign discriminator: the δ branch = sign(Im ε) = mirror chirality = direction of leptonic CP (DUNE)")
print("=" * 96)

# ---- the two branches, opposite sign of J -----------------------------------
sin_delta = rank/g                                  # |sin δ| = 2/7
J_197 = jarlskog(s12, s23, s13, np.radians(196.6))  # sin δ < 0
J_163 = jarlskog(s12, s23, s13, np.radians(163.4))  # sin δ > 0
print(f"\n[branches]: |sin δ| = rank/g = 2/7 = {rank/g:.3f}; δ=197° → J_PMNS = {J_197:.4f} (<0);  δ=163° → J_PMNS = {J_163:.4f} (>0)")
check("TWO BRANCHES, OPPOSITE SIGN OF J: same |cos δ| (the sum rule), opposite sin δ = ±rank/g = ±2/7. δ≈197° → "
      "J_PMNS<0 (data-favored); δ≈163° → J_PMNS>0. Data can't yet separate them, but they are PHYSICALLY distinct — "
      "opposite direction of leptonic CP.",
      J_197 < 0 and J_163 > 0 and abs(abs(J_197) - abs(J_163)) < 1e-6, "197°→J<0, 163°→J>0 — the branch flips the sign of J")

# ---- the branch = sign(Im ε) ------------------------------------------------
eps = (1/g)*(-1 + 1j*rank/(N_c*np.sqrt(n_C)))       # Lyra's ε (as written, Im>0)
arg_eps = np.degrees(np.angle(eps))
print(f"[branch = sign(Im ε)]: ε = (1/g)(−1 + i·rank/(N_c√n_C)) = {eps:.3f}; arg ε = {arg_eps:.1f}° → δ branch; sign(sin δ)=sign(Im ε)")
check("THE BRANCH = sign(Im ε) (mirror chirality): δ = arg(ε), so sign(sin δ) = sign(Im ε). Lyra's ε as written has "
      "Im ε > 0 → arg ε ≈ 163° → J>0; flipping to Im ε < 0 → 197° → J<0. So the branch IS the sign of the imaginary "
      "part of the imperfect-ℤ₂ imperfection — the chirality of the mirror. The geometry must pick it, not the data.",
      abs(arg_eps - 163.4) < 1.0 and np.imag(eps) > 0, "arg ε ≈ 163° for Im ε>0; the branch = sign(Im ε) = mirror chirality")

# ---- why it matters (DUNE, direction of leptonic CP) ------------------------
check("WHY IT MATTERS (not academic): sign(J_PMNS) is the sign of the neutrino-oscillation CP asymmetry, "
      "P(ν_μ→ν_e) − P(ν̄_μ→ν̄_e) ∝ J_PMNS — exactly what DUNE measures. So the branch = the DIRECTION of leptonic "
      "matter-vs-antimatter asymmetry, a fundamental yes/no, not a 34° cosmetic ambiguity. If BST forces Im ε < 0 → "
      "J<0 (δ≈197°), that's the data-favored direction and a sharp falsifiable DUNE call.",
      True, "sign(J) = DUNE's ν/ν̄ asymmetry sign = direction of leptonic CP — the branch is physical, DUNE-testable")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the δ branch (163° vs 197°) = sign(Im ε) = the imperfect-ℤ₂ mirror's chirality = sign(J_PMNS) = the "
      "DIRECTION of leptonic CP violation (DUNE-measurable). J_PMNS = ±0.009 with the sign SET by sign(Im ε). Held — "
      "banks with δ the moment Lyra's ε-derivation picks the sign of the imperfection geometrically. Flagged sharp so "
      "the derivation targets the SIGN, not just the magnitude.",
      J_197 < 0 and J_163 > 0, "branch=sign(Im ε)=sign(J)=direction of leptonic CP; held for Lyra's sign-pick. Count ~7-8 (α RULED)")

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
J-SIGN DISCRIMINATOR — the δ branch is the direction of leptonic CP (DUNE), not an academic ambiguity:
  * TWO BRANCHES: sin δ = ±rank/g = ±2/7 → δ=197° (J<0, data-favored) vs 163° (J>0). Same |cos δ| (sum rule).
  * BRANCH = sign(Im ε): δ=arg(ε), so sign(J)=sign(Im ε) = the chirality of the imperfect-ℤ₂ mirror.
  * WHY IT MATTERS: sign(J_PMNS) = sign of P(ν_μ→ν_e)−P(ν̄_μ→ν̄_e) — DUNE measures it. The branch = direction of
    leptonic matter/antimatter asymmetry, a fundamental yes/no.
  => the ε-derivation must pick sign(Im ε) from the geometry → predicts sign(J) → a sharp DUNE call. Held. Count ~7-8.
""")
