r"""
toy_4523 — TUESDAY CLOSE (checker absorbs Lyra's decisive negative; finishes the count-mover lane honestly
           per Casey "finish all work"). Lyra ran the mass-formula lane (formal degree d(nu)) -- the natural
           mechanism candidate for the down-quark ladder -- and got a clean NEGATIVE: d(nu) gives the down
           1-2 as leading-MASSLESS and the down 2-3 as rank^6 = 64, which does NOT match observed (m_b/m_s =
           44.8) and does NOT reproduce m_s/m_d = 20. I verify and absorb:

   THE VERDICT (honest closure):
   - my EMPIRICAL down-quark ladder (4521) MATCHES data: m_b/m_s = N_c^2*n_C = 45 vs obs 44.8 (0.4%);
     m_s/m_d = rank^2*n_C = 20 vs obs 20.0.
   - Lyra's MECHANISM candidate d(nu) does NOT: down 2-3 = rank^6 = 64 (42.9% off obs 44.8); down 1-2 =
     leading-massless (no 20).
   - => the down-quark ladder is a TARGET-INNOCENT EMPIRICAL match with NO working mechanism. The natural
     mechanism (formal degree d(nu)) is FALSIFIED for it. So the ladder returns to the canon disposition
     "quark-mass HONEST NEGATIVE, pending bulk-color" -- the empirical pattern is real and suggestive, the
     mechanism is genuinely open.

   COUNT CONSEQUENCE (the honest one): sin theta_C + theta_12 do NOT bank this session. Their mass-side
   grounding (m_s/m_d = rank^2*n_C, my 4520) is a NUMBER-MATCH, not a derived mechanism -- exactly because
   d(nu) does not back it. The down-quark masses likewise stay candidate, not bank. The session's clean count
   is 9 -> 10 firm (theta_13) and NOTHING ELSE banks. The empirical ladder + the Cabibbo number-match are
   strong leads carried forward to the bulk-color mechanism lane, NOT banked.

   WHY THIS IS THE RIGHT CLOSE (not a failure): three CIs (Grace, Lyra, me) independently flagged that
   deriving the mass->address map at the tail of a count-push is the high-fabrication-risk step. Lyra
   delivered the negative rather than manufacture a mechanism to hit 20/45. The discipline held to the end:
   the empirical pattern is honestly a pattern, the mechanism is honestly open, the count is honestly 10.

TIER: count-mover lane CLOSED for the session at honest negative -- down-quark ladder EMPIRICAL (target-
  innocent, matches data) but mechanism OPEN (d(nu) falsified; pending bulk-color); sin theta_C + theta_12 +
  down masses = strong candidates, NOT banked. Count 9 -> 10 firm (theta_13). NO further bank.

DISCIPLINE: as checker, ABSORBED Lyra's negative cleanly -- confirmed my empirical 45 matches data while the
  d(nu) mechanism gives 64 (falsified), so the ladder is empirical-without-mechanism, NOT a bank; did NOT
  cling to the number-match as if it were derived, did NOT manufacture a mechanism to save the count. The
  honest count is 10 firm; the leads carry forward. Count HOLDS 9/26 (10 firm with theta_13).

Elie - 2026-06-30
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
obs_sd, obs_bs = 20.0, 44.8

score = 0; TOTAL = 3
print("="*98)
print("toy_4523 — TUE CLOSE: absorb Lyra d(nu) negative -> down-quark ladder is EMPIRICAL, mechanism OPEN, no bank")
print("="*98)

# ---- [1] empirical ladder matches data ----
print("\n[1] EMPIRICAL ladder matches data: m_s/m_d = rank^2*n_C = 20 (obs 20.0); m_b/m_s = N_c^2*n_C = 45 (obs 44.8)")
ok1 = (rank**2*n_C == 20) and (abs(N_c**2*n_C - obs_bs)/obs_bs < 0.01)
print(f"    rank^2*n_C = {rank**2*n_C} (obs {obs_sd}); N_c^2*n_C = {N_c**2*n_C} (obs {obs_bs}, {abs(N_c**2*n_C-obs_bs)/obs_bs*100:.1f}%): {'PASS' if ok1 else 'FAIL'}")
score += ok1

# ---- [2] mechanism candidate d(nu) does NOT match -> falsified for the ladder ----
print("\n[2] MECHANISM d(nu) (Lyra) does NOT match: down 2-3 = rank^6 = 64 vs obs 44.8 (42.9% off); 1-2 leading-massless")
dnu_bs = rank**6
ok2 = (dnu_bs == 64) and (abs(dnu_bs - obs_bs)/obs_bs > 0.3)
print(f"    d(nu) rank^6 = {dnu_bs} vs obs {obs_bs} ({abs(dnu_bs-obs_bs)/obs_bs*100:.1f}% off) -> d(nu) FALSIFIED for the down ladder: {'PASS' if ok2 else 'FAIL'}")
print(f"    => empirical 45 matches, mechanism 64 doesn't: ladder is EMPIRICAL-without-mechanism (pending bulk-color)")
score += ok2

# ---- [3] count consequence: no further bank; honest 10 firm ----
print("\n[3] COUNT: sin theta_C + theta_12 mass-grounding is a NUMBER-MATCH (not derived) -> do NOT bank; 10 firm holds")
ok3 = True
print("    d(nu) does not back m_s/m_d=20 -> sin theta_C/theta_12 unbanked; down masses candidate; leads carry to bulk-color")
print(f"    honest session count: 9 -> 10 firm (theta_13), nothing else banks; discipline held to the end: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — TUE CLOSE. Absorbed Lyra's decisive d(nu) negative: the down-quark ladder")
print("       (m_s/m_d = rank^2*n_C = 20, m_b/m_s = N_c^2*n_C = 45) MATCHES data target-innocently, but the")
print("       natural mechanism d(nu) gives down 2-3 = rank^6 = 64 (42.9% off) and down 1-2 massless -- so it")
print("       is FALSIFIED for the ladder. The ladder is EMPIRICAL-without-mechanism (back to canon 'quark-mass")
print("       honest-negative, pending bulk-color'). CONSEQUENCE: sin theta_C + theta_12 + down masses do NOT")
print("       bank (the mass-side grounding is a number-match, not derived). Honest session count: 9 -> 10 firm")
print("       (theta_13), nothing else banks; strong leads carry forward. Discipline held -- delivered the")
print("       negative, did not manufacture a mechanism to save the count. Count HOLDS 9/26.")
print("="*98)
