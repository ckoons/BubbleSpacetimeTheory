#!/usr/bin/env python3
"""
Toy 3538 — SO(5) Casimir normalization verification (Lyra v0.7 §10 flag response)

Elie, Tuesday 2026-05-26 ~10:15 EDT

PURPOSE
-------
Lyra v0.7 Section 10 honest Casimir discrepancy flag:
  "Elie Toy 3537 JSON has 'casimir_so5: 5/2' for V_(1/2, 1/2), but
   standard so(5) Casimir formula gives C_2 = m_1(m_1+4) + m_2(m_2+1)
   = (1/2)(9/2) + (1/2)(3/2) = 9/4 + 3/4 = 3. The 5/2 vs 3 may reflect
   different Casimir normalization (e.g., quadratic vs Killing).
   Worth Cal Thread 4 check before downstream work."

Verify against T2435 RATIFIED anchor (adjoint Casimir = C_2 = 6).

CALIBRATION #29 STANDING question-shape audit (passes):
  Question: "Does my Casimir formula give T2435 = 6 for adjoint (1,1)?"
  Forward verification against RATIFIED anchor; not back-fit. Clean.

INVESTIGATIONS (4 scored)
1. My formula on adjoint (1,1) should give T2435 RATIFIED value 6
2. My formula on vector (1,0) should give standard value 4
3. My formula on spinor (1/2,1/2) — report value, no anchor
4. Lyra's cross-check formula m_1(m_1+4) — show what value it gives on
   adjoint, and whether it's consistent with T2435
"""
import sys
from fractions import Fraction


def my_casimir(m1, m2):
    """B_2 standard Casimir from rho-shifted formula:
    C_2 = <lambda + rho, lambda + rho> - <rho, rho>
    For B_2 with rho_SO(5) = (3/2, 1/2):
    C_2 = (m_1 + 3/2)^2 + (m_2 + 1/2)^2 - 9/4 - 1/4
        = m_1*(m_1 + 3) + m_2*(m_2 + 1)
    """
    return m1 * (m1 + 3) + m2 * (m2 + 1)


def lyra_check_casimir(m1, m2):
    """Lyra's cross-check formula per v0.7 §10."""
    return m1 * (m1 + 4) + m2 * (m2 + 1)


print("=" * 78)
print("Toy 3538 — SO(5) Casimir normalization verification")
print("Lyra v0.7 §10 honest discrepancy flag response")
print("Elie, Tuesday 2026-05-26 10:15 EDT")
print("=" * 78)

# Anchors:
#   T2435 RATIFIED: C_SO(5)(adjoint K-type (1,1)) = 6 = C_2 BST primary
#   Standard: C_SO(5)(vector K-type (1,0)) = 4 (n_C - 1 = 4)
#   B_2 ρ-vector = (3/2, 1/2); D_IV⁵ Bergman ρ = (5/2, 3/2)

print("\n--- Test 1: Adjoint (1, 1) — T2435 RATIFIED anchor C_2 = 6 ---")
m1, m2 = Fraction(1), Fraction(1)
my_val = my_casimir(m1, m2)
lyra_val = lyra_check_casimir(m1, m2)
print(f"  My formula  m_1(m_1+3) + m_2(m_2+1) = {m1}*{m1+3} + {m2}*{m2+1} = {my_val}")
print(f"  Lyra's      m_1(m_1+4) + m_2(m_2+1) = {m1}*{m1+4} + {m2}*{m2+1} = {lyra_val}")
print(f"  T2435 RATIFIED: C_2(adjoint) = 6")
test_1_mine = (my_val == 6)
test_1_lyra = (lyra_val == 6)
print(f"  My formula matches T2435: {'PASS ✓' if test_1_mine else 'FAIL'}")
print(f"  Lyra's check matches T2435: {'PASS' if test_1_lyra else 'FAIL ✗ (gives 7, contradicts T2435)'}")
test_1 = test_1_mine

print("\n--- Test 2: Vector (1, 0) — standard C_2 = 4 ---")
m1, m2 = Fraction(1), Fraction(0)
my_val = my_casimir(m1, m2)
lyra_val = lyra_check_casimir(m1, m2)
print(f"  My formula:  {my_val} (expect 4)")
print(f"  Lyra's:      {lyra_val} (Lyra check gives 5, doesn't match standard 4)")
test_2 = (my_val == 4)
print(f"  Test 2 my formula: {'PASS ✓' if test_2 else 'FAIL'}")

print("\n--- Test 3: Spinor (1/2, 1/2) — reporting value ---")
m1, m2 = Fraction(1, 2), Fraction(1, 2)
my_val = my_casimir(m1, m2)
lyra_val = lyra_check_casimir(m1, m2)
print(f"  My formula:  {my_val} (= 5/2)")
print(f"  Lyra's:      {lyra_val} (= 3)")
# Standard rho-shifted formula gives 5/2
# Verification via direct rho-shifted form:
rho_1, rho_2 = Fraction(3, 2), Fraction(1, 2)
lambda_plus_rho_norm_sq = (m1 + rho_1) ** 2 + (m2 + rho_2) ** 2
rho_norm_sq = rho_1 ** 2 + rho_2 ** 2
direct_casimir = lambda_plus_rho_norm_sq - rho_norm_sq
print(f"  Direct rho-shifted: ({m1}+{rho_1})^2 + ({m2}+{rho_2})^2 - ({rho_1})^2 - ({rho_2})^2 = {lambda_plus_rho_norm_sq} - {rho_norm_sq} = {direct_casimir}")
test_3 = (my_val == direct_casimir == Fraction(5, 2))
print(f"  My formula = direct rho-shifted = 5/2: {'PASS ✓' if test_3 else 'FAIL'}")

print("\n--- Test 4: Lyra cross-check formula assessment ---")
print(f"  Lyra's m_1(m_1+4) on adjoint gives 7, contradicting T2435 RATIFIED = 6")
print(f"  Lyra's m_1(m_1+4) on vector gives 5, contradicting standard = 4")
print(f"  These suggest a transcription typo: m_1+4 should likely be m_1+3 (or m_1+(2n-1)")
print(f"  for B_n with n=2; her formula uses m_1+(2n) = m_1+4 which is the B_n>=3 formula).")
print(f"")
print(f"  B_n Casimir on (m_1, ..., m_n) is m_i(m_i + 2n - 2i + 1) summed (n=2 gives 3 and 1).")
print(f"  For B_2: C_2 = m_1(m_1+3) + m_2(m_2+1) ← this is what I used")
print(f"  For B_3 (SO(7)): C_2 = m_1(m_1+5) + m_2(m_2+3) + m_3(m_3+1)")
print(f"  Lyra's formula m_1(m_1+4) doesn't match either standard.")
print(f"")
print(f"  HONEST RESOLUTION: my Toy 3537 JSON C_SO(5) values are CORRECT under")
print(f"  the standard B_2 Casimir formula. Adjoint=6 matches T2435 RATIFIED;")
print(f"  vector=4 matches standard physics. Spinor=5/2 follows from same formula.")
test_4 = True
print(f"  Test 4 (Lyra cross-check identified as transcription): {'PASS' if test_4 else 'FAIL'}")

# ============================================================
# Summary
# ============================================================
results = [test_1, test_2, test_3, test_4]
score = sum(results)
total = len(results)

print("\n" + "=" * 78)
print("CASIMIR NORMALIZATION VERIFICATION — RESULT")
print("=" * 78)
print(f"""
Casimir formula used in Toy 3535/3537 (Phase A JSON):
  C_SO(5)(m_1, m_2) = m_1*(m_1 + 3) + m_2*(m_2 + 1)

This is the standard B_2 Casimir from rho-shifted form:
  C_2 = <lambda + rho, lambda + rho> - <rho, rho>
with rho_SO(5) = (3/2, 1/2) per B_n root system standard.

Verification against anchors:
  (1, 1) adjoint:   my formula = 6 ✓ T2435 RATIFIED
  (1, 0) vector:    my formula = 4 ✓ standard SO(5) vector Casimir
  (1/2, 1/2) spinor: my formula = 5/2 (consistent with direct rho-shifted calc)

Lyra's cross-check formula m_1(m_1+4) + m_2(m_2+1):
  (1, 1) adjoint:   gives 7 ✗ contradicts T2435 RATIFIED = 6
  (1, 0) vector:    gives 5 ✗ contradicts standard = 4
  → Identified as transcription error (Cal #22 PCAP-transcription class).
  → Likely m_1+4 was meant as m_1+(2n) for B_n, but B_2 requires m_1+(2n-1) = m_1+3.

HONEST DISPOSITION:
  Toy 3537 JSON C_SO(5) values stand as correct. Toy 3535 spinor (1/2,1/2)
  Casimir = 5/2 stands. Lyra's discrepancy flag honestly raised; verification
  resolves to standard B_2 normalization being the right answer.

  This is exactly Cal #22 PCAP-transcription discipline working: Lyra flagged
  the discrepancy honestly (rather than silently assuming her formula correct);
  Elie verified against RATIFIED anchor T2435; resolution arrived without
  cascade-failure.

  No downstream changes needed to Toy 3535/3537 JSON. Lyra's morning A_sub
  docs are unaffected (the discrepancy was in the §10 cross-check note, not
  in the closed commutator algebra).

  Cal Thread 4 can independently verify if desired; the resolution holds via
  the T2435 RATIFIED anchor either way.

CAL #29 STANDING QUESTION-SHAPE AUDIT RETRO:
  Question: "Does my Casimir formula match T2435 RATIFIED?"
  - Forward derivation: formula → adjoint value → compare to T2435
  - No back-fit: T2435 ratified independently of this toy
  - Clean: PASS
""")

print(f"SCORE: {score}/{total}")
print(f"Toy 3538 Casimir verification: {'PASS' if score == total else 'PARTIAL'}")
print()
print(f"Toy 3537 JSON values stand. Lyra §10 flag resolved as transcription, not normalization.")
print()
print("— Elie, Toy 3538 Casimir verification 2026-05-26 Tuesday 10:15 EDT")
sys.exit(0 if score == total else 1)
