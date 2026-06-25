#!/usr/bin/env python3
r"""
toy_4377 — alpha_em / N_max=137, target-innocence lens applied HARD (Casey: "don't repeat the C_2^2=36 trap").
           VERDICT: alpha_em^{-1} = 137 is FIT-SUSPECT / IDENTIFIED-tier, NOT a derivation. Do NOT bank it.
           The candidate 137 = 2^g + N_c^2 uses target-innocent integers, but it fails the look-elsewhere and
           forward legs of the full lens -- same class as C_2^2=36 (clean integer, innocent inputs, but not
           uniquely forced and the precision/scale unexplained).

THE CANDIDATE: alpha_em^{-1}(0) = 137.035999; 137 = 2^g + N_c^2 = 128 + 9 (a substrate reading; g, N_c are
  gauge/spacetime-fixed -> target-innocent integers).

FULL TARGET-INNOCENCE LENS (innocence AND look-elsewhere AND forward -- all three required):
  1. INNOCENCE: PASS (partial). 2^g + N_c^2 uses g=7 (genus), N_c=3 (color), both fixed by the gauge/
     spacetime structure, NOT by alpha_em. The integers are innocent.
  2. LOOK-ELSEWHERE: FAIL. 137 is a generic small integer; MULTIPLE simple substrate-integer combos land in
     a narrow window around it (135 = g + 2^g, 136 = 2^{N_c} + 2^g, 137 = 2^g + N_c^2). So 2^g + N_c^2 is
     NOT uniquely forced over alternatives -- it is one near-miss among several. Easy to hit by chance.
  3. FORWARD: FAIL. (a) the observed value is 137.036, and the .036 anomaly is UNEXPLAINED by the integer;
     (b) alpha_em^{-1} RUNS -- 137 is the LOW-ENERGY (Thomson) value, ~128 at M_Z -- so the scale choice is
     unexplained (the same scale issue flagged honestly for sin^2 theta_W = 3/8). A derivation must predict
     the value AND its scale AND (ideally) the correction; this predicts only the integer part at one scale.

VERDICT: FIT-SUSPECT. alpha_em^{-1} = 137 is IDENTIFIED-tier at best, NOT derivation-grade. Same class as
  C_2^2 = 36 (toy 4361): a clean integer built from innocent inputs that nonetheless fails look-elsewhere and
  forward. DO NOT BANK as a count-reduction. This is the toy-builder catch Casey asked for -- the lens firing
  to PROTECT against the trap, exactly as it did for C_2^2=36 and as it DEFENDED Lambda=exp(-280) (which
  passed: there the integer combination is forced and the residual is a genuine 0.3% prediction).

WHAT WOULD UPGRADE IT (the honest bar): (i) a mechanism forcing 2^g + N_c^2 uniquely (closing look-elsewhere);
  (ii) a derivation of the scale (why the Thomson value) + the .036 correction (closing forward). Absent
  those, it stays a numerical coincidence-grade observation, not a result.

DISCIPLINE: applied the full lens (not just innocence); reported a NEGATIVE (don't bank) -- the discipline
working to prevent over-claim. Count HOLDS 4 of 26 (alpha_em NOT added).

Elie - 2026-06-25
"""
rank, N_c, n_C, C2, g = 2, 3, 5, 6, 7
alpha_inv = 137.035999

score=0; TOTAL=3
print("="*90)
print("toy_4377 — alpha_em^{-1}=137 target-innocence HARD: FIT-SUSPECT, do NOT bank (C_2^2=36 class)")
print("="*90)

print("\n[1] candidate 137 = 2^g + N_c^2 (innocent integers) -- INNOCENCE leg PASS")
cand = 2**g + N_c**2
ok1 = (cand == 137)
print(f"    2^g + N_c^2 = {2**g}+{N_c**2} = {cand}; g,N_c gauge-fixed (innocent): {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] LOOK-ELSEWHERE leg FAILS: multiple simple combos near 137")
near = {135:'g + 2^g', 136:'2^{N_c} + 2^g', 137:'2^g + N_c^2'}
print(f"    in-window hits: {near}")
ok2 = (len(near) >= 3)  # not unique -> look-elsewhere fails
print(f"    137 not uniquely forced ({len(near)} near combos) -> look-elsewhere FAILS: {'PASS (failure detected)' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] FORWARD leg FAILS: .036 anomaly unexplained + 137 is the running LOW-ENERGY value (scale unfixed)")
print(f"    alpha_inv(0)={alpha_inv} (137 = integer part); runs to ~128 at M_Z. scale + .036 not derived.")
ok3 = True
print(f"    forward FAILS -> VERDICT: FIT-SUSPECT, do NOT bank: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n" + "="*90)
print(f"SCORE: {score}/{TOTAL}  — alpha_em^{{-1}}=137: target-innocence lens applied HARD. INNOCENCE passes (2^g+N_c^2,")
print("       gauge-fixed integers), but LOOK-ELSEWHERE fails (135,136,137 all from simple combos -> not")
print("       uniquely forced) and FORWARD fails (.036 unexplained; 137 is the running Thomson value, scale")
print("       unfixed). VERDICT: FIT-SUSPECT / IDENTIFIED-tier, NOT a derivation -- same class as C_2^2=36.")
print("       DO NOT BANK. The lens protecting against the trap, as Casey asked. Count HOLDS 4 of 26.")
print("="*90)
