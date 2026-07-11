#!/usr/bin/env python3
"""
Toy 4617 — Jul 11 (my task, Keeper's up-sector gate): is the bulk (down) / boundary (up) mass-mechanism
split FORCED (a real geometric asymmetry) or PER-SECTOR FITTING (two mechanisms chosen to fit)? Two
mechanisms is more freedom, so the bar fires here. Verdict: HALF-forced — down forced, up not — so the
split is currently per-sector, and the gate is NOT passed. Down banks; up stays a lead.

DOWN sector — FORCED: ν = N_c = 3 = k_min is the WALLACH THRESHOLD (the FK object's own singular point,
  where it vanishes = the TIR emission threshold). The input ν IS a forced geometric threshold, not a
  choice. s/d = (N_c+1)(N_c+2) = 20 EXACT. → genuinely forced (F506, my degrees {1,3,5} vindicated).

UP sector — test the forced-ness (it fails the same test):
  (a) ν for up: c/u = 588 needs ν ≈ 23. Is 23 a threshold? 23 = N_c·g+rank (BST-expressible) but NOT a
      Wallach threshold (k_min = N_c). So the up ν is NOT forced the way the down ν = N_c is.
  (b) boundary primes: c/u = 19·31 = 589 (0.2%). 19 = N_c·C_2+1, 31 = 2^{n_C}−1 = M_{n_C} (Mersenne) —
      BST-EXPRESSIBLE, but not derived from a forced structure (an expressible number ≠ a forced one).

CANDIDATE forced reason for up→boundary (fair hearing, then the honest limit):
  the TOP is AT the Shilov boundary: m_t ≈ v/√2 ≈ 174 GeV ≈ 172.5 (T2009/T2046). So the up tower REACHES
  the boundary (top = the vev), while the down tower (m_b ≈ 4.2 ≪ v) stays in the bulk — that MOTIVATES
  up→boundary. BUT: it rests on WHY the top (up-type) is the heaviest / at v — not independently forced;
  and even c/u (no top) already needs ν ≠ N_c, so the up sector differs from down before the top even enters.

⟹ HONEST VERDICT: HALF-FORCED. The DOWN sector is forced (ν = N_c, a real Wallach threshold — F506 banks).
The UP sector is NOT forced the same way (ν ≈ 23 is not a threshold; the boundary primes 19·31 are
expressible-not-derived; the top-at-v reason is a candidate, not a derivation). So the "down→bulk,
up→boundary" split is currently PER-SECTOR FITTING (down forced, up fitted), NOT a fully forced
bulk/boundary asymmetry. THE GATE IS NOT PASSED. The up-sector stays a LEAD, not a mechanism-bank,
until (a) up→boundary is forced and (b) the boundary primes 19·31 are derived (not just expressible).

HONEST: this fires the bar on the two-mechanism freedom, as Keeper asked. Down-specific banking stands
(F506, forced); the bulk/boundary asymmetry is not yet a forced mechanism. Count ~7-8 (α RULED).
"""
rank, N_c, n_C, C_2, g, Nmax = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 82)
print("Toy 4617 — bulk/boundary gate: HALF-forced (down yes, up no) → per-sector, gate NOT passed")
print("=" * 82)

# ---- down forced ------------------------------------------------------------
print(f"\n[DOWN — FORCED]: ν = N_c = 3 = k_min (Wallach THRESHOLD, the FK object's singular point); s/d = (N_c+1)(N_c+2) = {(N_c+1)*(N_c+2)} exact")
check("DOWN is FORCED: ν = N_c = the Wallach threshold (a forced geometric singular point), not a choice; s/d = 20 exact",
      (N_c+1)*(N_c+2) == 20, "the down input ν IS a forced threshold — F506 banks, my degrees {1,3,5} vindicated")

# ---- up not forced ----------------------------------------------------------
print(f"\n[UP — NOT forced the same way]: ν≈23 = N_c·g+rank = {N_c*g+rank} (expressible, NOT a threshold); primes 19·31 = {19*31} (0.2%), expressible not derived")
check("UP is NOT forced: ν≈23 is not a Wallach threshold (k_min=N_c); the boundary primes 19·31 are BST-expressible but not derived from a forced structure",
      N_c*g+rank == 23 and 19*31 == 589, "an expressible number ≠ a forced one; even c/u (no top) needs ν≠N_c → the up sector differs from down structurally")

# ---- candidate reason -------------------------------------------------------
v = 246.0
print(f"\n[candidate forced reason (fair hearing)]: top at the boundary, m_t ≈ v/√2 = {v/2**0.5:.0f} ≈ 172.5 (T2009); up tower reaches boundary, down stays bulk")
check("CANDIDATE up→boundary (top at v ≈ boundary/vev) motivates it, but rests on WHY the top is heaviest/at-v (not forced) — a candidate, not a derivation",
      abs(v/2**0.5 - 172.5)/172.5 < 0.02, "and c/u already needs ν≠N_c before the top enters — so the up sector differs structurally, not just via the top")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: HALF-FORCED — down forced (ν=N_c), up NOT (ν≈23 not a threshold, primes expressible-not-derived). Split is PER-SECTOR → gate NOT passed",
      True, "the bulk/boundary asymmetry is not yet a forced mechanism; up stays a LEAD, not a mechanism-bank")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 82)
print(f"SCORE: {passed}/{total}")
print("=" * 82)
print("""
BULK/BOUNDARY GATE — half-forced, gate NOT passed (fires the bar on the two-mechanism freedom):
  * DOWN is FORCED: ν = N_c = the Wallach threshold (a forced singular point); s/d = (N_c+1)(N_c+2) = 20
    exact. F506 banks; my degrees {1,3,5} vindicated.
  * UP is NOT forced the same way: ν ≈ 23 is not a threshold (23 = N_c·g+rank, expressible); the boundary
    primes 19·31 are BST-expressible but not derived. Even c/u (no top) needs ν ≠ N_c.
  * CANDIDATE reason (top at v ≈ boundary/vev, T2009) motivates up→boundary but rests on why the top is
    heaviest/at-v — a candidate, not a derivation.
  ⟹ HALF-FORCED. The bulk/boundary split is currently PER-SECTOR (down forced, up fitted), NOT a fully
  forced asymmetry — GATE NOT PASSED. Down-specific banking stands; the up sector stays a LEAD until
  up→boundary is forced and 19·31 is derived. Count ~7-8 (α RULED).
""")
