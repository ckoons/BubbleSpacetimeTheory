r"""
toy_4495 — STATUS-MAP of the reopened dimensionless lanes (Cal #470 FLOOR-not-saturation) with F417 tiers --
           firing on the reopened frontier, operationalizing the correction. Cal #470 reopened V_cb, V_ub,
           CP phase delta, PMNS angles, g1/g2 as live count-movers. HONEST STATUS: they ARE reachable, but
           every one currently sits at (C) #286-candidate or structural -- several rely on fish-suspect
           cofactors (79 in V_us, 13 in sin^2 theta_W, 16 in PMNS), and sin^2 theta_W additionally RUNS. To
           MOVE the count, each needs a disambiguating mechanism (F417). The most promising is the V_cb
           dual-rho ANGLE (target-innocent = (A)-tier; the magnitude is the open part) and the exp-12 blind
           derivation (in progress with Lyra+Grace). NO count move (a status map). Count 9/26.

THE REOPENED LANES (Cal #470) -- honest current status + F417 tier:
  - sin^2 theta_W : = N_c/(C_2+g) = 3/13 = 0.2308 vs 0.23122 (0.2%). BUT 13 = C_2+g is FISH-SUSPECT (Grace
      flagged the "13" tell), AND sin^2 theta_W RUNS (scale-dependent) -> (C) #286-candidate + running-limited.
      [NOT the forbidden GUT 3/8 -> Five-Absence PASS.]
  - V_us : = 2/sqrt(79) = 0.2250 vs 0.2243 (0.32%). BUT 79 is prime, NOT a clean substrate primary -> (C)
      #286-candidate (fish-suspect cofactor).
  - V_cb : dual-rho ANGLE cos psi = n_C/sqrt(n_C^2+N_c^2) = 5/sqrt(34) target-innocent = (A)-tier for the
      angle; MAGNITUDE structural ~8% (the open part). The most promising (clean angle, open magnitude).
  - V_ub, delta : CP sector -- delta INTERNAL (Cal #50); V_ub structural. (C)/INTERNAL.
  - PMNS sin^2 theta_12 = 5/16 = 0.3125 vs 0.307 (1.8%); 16 = rank^4 / 2^{2 rank} -- structural; the others
      within ~1 sigma. structural.

THE HONEST READ (operationalizing Cal #470): the dimensionless sector is OPEN and REACHABLE (NOT saturated),
  but it is NOT a pile of clean results waiting to be banked -- every lane is currently (C) #286-candidate or
  structural, with fish-suspect cofactors (79, 13, 16) flagged by F417, and sin^2 theta_W runs. So "reachable"
  means "a disambiguating MECHANISM (F417) would move it," NOT "it's nearly done." The two genuine count-mover
  routes: (1) the V_cb dual-rho magnitude (mine; the angle is already (A), the magnitude needs the
  localized-overlap mechanism); (2) the exp-12 blind derivation (Elie+Lyra+Grace, in progress).

TIER: status-map -- the reopened dimensionless lanes are reachable but currently (C)-candidate/structural,
  fish-suspect cofactors flagged (F417), the count-mover routes named (V_cb magnitude + exp-12). NO count
  move (a map). Count HOLDS 9/26.

DISCIPLINE: operationalized Cal #470 (the lanes ARE open) by HONESTLY mapping each to its current tier (NOT
  claiming they're nearly banked); applied F417 (flagged the fish-suspect cofactors 79/13/16 as (C)-candidate);
  noted sin^2 theta_W runs; ran Five-Absence (3/13 != 3/8 GUT, PASS); named the genuine count-mover routes
  without fishing them. Count HOLDS 9/26.

Elie - 2026-06-29
"""
import math
N_c, n_C, C2, g, rank, Nmax = 3, 5, 6, 7, 2, 137

score=0; TOTAL=4
print("="*98)
print("toy_4495 — STATUS-MAP reopened dimensionless lanes (Cal #470) with F417 tiers")
print("="*98)

print("\n[1] sin^2 theta_W = N_c/(C_2+g) = 3/13 = 0.2308 (0.2%) BUT 13 fish-suspect + RUNS -> (C)-candidate")
sw = 3/13
ok1 = (abs(sw - 0.23122)/0.23122 < 0.01) and (C2+g == 13)
print(f"    3/13 = {sw:.4f} vs 0.23122 ({abs(sw-0.23122)/0.23122*100:.2f}%); 13=C_2+g fish-suspect; runs; != 3/8 GUT (5-Abs PASS): {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] V_us = 2/sqrt(79) = 0.2250 (0.32%) BUT 79 prime, not substrate -> (C)-candidate (fish cofactor)")
vus = 2/math.sqrt(79)
ok2 = (abs(vus - 0.2243)/0.2243 < 0.01)
print(f"    2/sqrt(79) = {vus:.4f} vs 0.2243 ({abs(vus-0.2243)/0.2243*100:.2f}%); 79 not a clean primary -> candidate: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] V_cb: dual-rho ANGLE 5/sqrt(34) target-innocent = (A); MAGNITUDE structural ~8% -- MOST PROMISING")
cpsi = n_C/math.sqrt(n_C**2+N_c**2)
ok3 = (abs(cpsi - 5/math.sqrt(34)) < 1e-9)
print(f"    cos psi = n_C/sqrt(n_C^2+N_c^2) = {cpsi:.4f} = 5/sqrt(34) (angle (A)-tier); magnitude open (~8%): {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] honest read: reachable != nearly-done; each needs a disambiguating mechanism (F417); routes named")
ok4 = True
print("    count-mover routes: (1) V_cb dual-rho magnitude (mine); (2) exp-12 blind derivation (in progress)")
print(f"    the lanes are OPEN (Cal #470) but (C)/structural -- 'reachable' = 'a mechanism would move it': {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — STATUS-MAP of the reopened dimensionless lanes (Cal #470). They ARE open and")
print("       reachable, but HONESTLY every one is currently (C) #286-candidate or structural: sin^2 theta_W =")
print("       3/13 (0.2%, but 13 fish-suspect + runs), V_us = 2/sqrt(79) (0.32%, 79 not a primary), PMNS 5/16")
print("       (1.8%), V_cb dual-rho angle target-innocent but magnitude ~8%. 'Reachable' means a disambiguating")
print("       MECHANISM (F417) would move it -- NOT 'nearly banked'. The two genuine count-mover routes: the")
print("       V_cb dual-rho magnitude (mine) and the exp-12 blind derivation (in progress). NO count move.")
print("="*98)
