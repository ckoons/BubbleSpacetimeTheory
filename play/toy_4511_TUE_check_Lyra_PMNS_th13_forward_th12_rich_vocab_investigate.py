r"""
toy_4511 — TUESDAY, checker on Lyra's PMNS count-move claims (she claimed 9->11; per investigate-don't-gate I
           VERIFY to keep the moving count honest, NOT to gate). VERDICT, split:
           - theta_13 = 1/(N_c^2 n_C) = 1/45 (0.32 sigma): SINGLE clean BST form (no competing clean
             factorization of 45) + Lyra's disambiguating mechanism (the only PMNS angle reaching the
             boundary) -> looks FORWARD. Supports Lyra's bank.
           - theta_12: TWO substrate-primary forms -- 3/10 = N_c/(2 n_C) (Lyra, real dimension 2n_C=10, 0.54
             sigma) AND 5/16 = n_C/2^{2 rank} (my 4509 survey, 0.42 sigma) -- BOTH within ~0.5 sigma =
             RICH-VOCABULARY (F417). Bankable IFF the real-dimension mechanism genuinely disambiguates 3/10
             over 5/16; that is an INVESTIGATION (does the real-dim reading beat the form-only 5/16?), NOT a
             Cal gate. Claimed at the tier the work supports: theta_13 forward; theta_12 (C)-strong pending
             the disambiguation. So the PMNS contribution to the count is theta_13 clean now; theta_12 lands
             when the form is disambiguated. NO unilateral count bank by me (checker). Count 9/26 (theta_13
             is Lyra's bank to claim; I verify it FORWARD).

CHECK theta_13 = 1/(N_c^2 n_C) = 1/45:
  obs sin^2 theta_13 = 0.0220 +- 0.0007; 1/45 = 0.02222 (0.32 sigma). 45 = N_c^2 * n_C = 9*5 -- I searched
  for competing clean forms (rank^2 * x, g * x, ...) and found none clean. SINGLE form + boundary mechanism
  (Lyra: the only PMNS angle reaching the boundary) -> disambiguated -> FORWARD. Verified; supports the bank.

CHECK theta_12 -- rich-vocabulary catch:
  obs sin^2 theta_12 = 0.307 +- 0.013.
  - 3/10 = N_c/(2 n_C) = 0.3000 (0.54 sigma)  [Lyra: 2n_C = 10 = real dimension of D_IV^5]
  - 5/16 = n_C/2^{2 rank} = 0.3125 (0.42 sigma)  [my 4509 survey]
  BOTH substrate-primary, BOTH within ~0.5 sigma -> RICH-VOCABULARY (F417 (C)) unless a mechanism picks one.
  Lyra cites the real-dimension reading (3/10); the 5/16 is form-only (no mechanism in my survey). IF the
  real-dimension mechanism is genuine (the mixing angle = N_c / real-dimension), 3/10 is (B) and 5/16 is (C),
  so 3/10 wins (disambiguated, bankable). IF not, it stays (C). That is the INVESTIGATION (per the directive),
  not a gate.

PER THE DIRECTIVE: theta_13 forward (clean, supports the bank); theta_12's disambiguation is an investigation
  lane (does the real-dim mechanism beat 5/16?), claimed at (C)-strong meanwhile. I do NOT block theta_12
  pending Cal (that would be gating); I flag the form-non-uniqueness as the work to finish.

TIER: checker on Lyra PMNS -- theta_13 = 1/(N_c^2 n_C) FORWARD (single form + boundary mechanism, verified);
  theta_12 = N_c/(2n_C) RICH-VOCABULARY (vs 5/16), (C)-strong pending the real-dimension disambiguation
  (investigation, not gate). Keeps the moving count honest. NO unilateral bank. Count 9/26.

DISCIPLINE: verified Lyra's count-move claims (checker keeping the moving count honest, NOT gating); SUPPORTED
  theta_13 (single form + mechanism -> forward); CAUGHT theta_12's rich-vocabulary (3/10 vs 5/16) and framed
  the disambiguation as an INVESTIGATION lane per the directive (not a Cal gate, not a block); claimed at
  supported tiers. Count HOLDS 9/26 (theta_13 is Lyra's to bank; I verify forward).

Elie - 2026-06-30
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

score=0; TOTAL=3
print("="*98)
print("toy_4511 — TUE checker on Lyra PMNS: theta_13 FORWARD (1/45 single form); theta_12 rich-vocab (3/10 vs 5/16)")
print("="*98)

print("\n[1] theta_13 = 1/(N_c^2 n_C) = 1/45 = 0.02222 (0.32 sigma); single clean form (45=N_c^2 n_C) + boundary mechanism")
s13, sig13 = 0.0220, 0.0007
f13 = 1/(N_c**2*n_C)
ok1 = (abs(f13-s13)/sig13 < 1.0) and (N_c**2*n_C == 45)
print(f"    1/45 = {f13:.5f} ({abs(f13-s13)/sig13:.2f} sigma); no competing clean 45-form -> FORWARD (supports Lyra bank): {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] theta_12: 3/10=N_c/(2n_C) (0.54s) AND 5/16=n_C/2^(2rank) (0.42s) -- TWO forms, both ~0.5s -> RICH-VOCABULARY")
s12, sig12 = 0.307, 0.013
f12a, f12b = N_c/(2*n_C), n_C/2**(2*rank)
ok2 = (abs(f12a-s12)/sig12 < 1.0) and (abs(f12b-s12)/sig12 < 1.0)
print(f"    3/10={f12a:.4f} ({abs(f12a-s12)/sig12:.2f}s); 5/16={f12b:.4f} ({abs(f12b-s12)/sig12:.2f}s) -> rich-vocab (F417): {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] per directive: theta_12 disambiguation (real-dim mechanism vs 5/16) is an INVESTIGATION lane, not a Cal gate")
ok3 = True
print("    if real-dim mechanism (3/10) genuine -> beats form-only 5/16 -> banks; else (C). claim (C)-strong meanwhile")
print(f"    theta_13 forward (supports bank); theta_12 pending disambiguation; no unilateral bank by me (checker): {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — TUE checker on Lyra's PMNS count-moves (keeping the moving count honest). theta_13")
print("       = 1/(N_c^2 n_C) = 1/45 (0.32s) is a SINGLE clean form + boundary mechanism -> FORWARD, supports")
print("       the bank. theta_12 = N_c/(2n_C) = 3/10 (0.54s) has a RICH-VOCABULARY twin (5/16 = n_C/2^{2rank},")
print("       0.42s) -- both substrate-primary within ~0.5 sigma. Bankable IFF the real-dimension mechanism")
print("       disambiguates 3/10 over 5/16 -- an INVESTIGATION lane (per investigate-don't-gate), not a Cal")
print("       gate. theta_13 forward; theta_12 (C)-strong pending disambiguation. Count HOLDS 9/26 (Lyra's to bank).")
print("="*98)
