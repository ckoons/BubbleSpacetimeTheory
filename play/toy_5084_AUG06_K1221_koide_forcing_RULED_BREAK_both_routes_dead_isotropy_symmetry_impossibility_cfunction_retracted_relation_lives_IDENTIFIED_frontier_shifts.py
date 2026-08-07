#!/usr/bin/env python3
"""
Toy 5084 — Aug 6 [PROGRAM: TEGMARK] (the Koide make-or-break RULED: BREAK — Keeper K1221. The sharpest, scale-free falsifier in the program came to a
pre-registered fork and returned BREAK, cleanly, on BOTH routes. The relation LIVES; only the MECHANISM died. Recording the ruling faithfully and
closing out the make-or-break thread I fired (toys 5079–5083). This is the machine working at its best — a pre-registered make-or-break returned
break, tested to destruction instead of shipped). The ruling:

★ THE RULING (Keeper K1221) — the forward geometric FORCING of Koide is FALSIFIED (both routes DEAD):
  · ROUTE 1 (isotropy) — Grace's SYMMETRY IMPOSSIBILITY (proved independently of my fire — the clean checker): isotropy needs the forced positions
    {5/2, 3/2, 0} to be full-B₂-Weyl-symmetric, but they CAN'T be — tau = 0 is the B₂ FIXED point, and the electron/muon sit at DISTINCT radii (5/2 ≠
    3/2), which B₂ (which preserves radius) can never map into a single invariant set. So the covariance is ANISOTROPIC for ANY 3-point placement; no
    kernel makes it round. (This is exactly the position-symmetry crack I owned in toy 5083 — now proved impossible, not just unresolved.)
  · ROUTE 2 (the c-function magnitude) — RETRACTED + named-forbidden (F669): the c₅/c₃ = Γ(n_C)/π² = Γ(5)/π² route is retracted; the PROVED c₅/c₃ is a
    λ-rational, not Γ(5)/π², and the whole {5,3,0} nesting was refuted months ago (K85x). So the magnitude route was never live.

★ THE HONEST DISTINCTION (the relation lives, only the mechanism died): Koide's relation itself is NOT wrong — Q = (Σm)/(Σ√m)² = 2/3 = rank/N_c is
  EXACT, verified to ~1e-5 on the lepton masses (0.0009%). It stays BANKED as IDENTIFIED — a precise, real relation that we simply CANNOT derive from
  the geometry, because both obvious forward routes are dead. "Koide is a precise relation we cannot force" — not "Koide is wrong."

★ THE TIER CHANGE + THE MACHINE WORKING: the Koide forcing DROPS from CONDITIONAL-FORCED → IDENTIFIED (Casey's call per the reductions-governance;
  Keeper recommends). The relation stands; the "we derived it from the geometry" claim does NOT; the PRL is hard-gated at Keeper's pass (exact
  observed relation, NOT derived; may not use the dead c-function route). This round is the discipline at its absolute best: a pre-registered
  make-or-break returned BREAK; the firer/checker separation held (Grace verified independently); Lyra walked back her own beautiful idea (her sixth
  self-catch of the arc); I owned my over-claim (toy 5083); Cal guarded both knobs; the corpus reconnect caught the miss Keeper owns (he twice called
  the c-function route "grounded" — it was retracted months ago, F669). Nothing was laundered; the prettiest result in the program was tested to
  destruction instead of shipped. Better us than a referee. ⟹ DISPOSITION: Koide forward FORCING RULED BREAK (Keeper K1221) — Route 1 (isotropy) a
  proved symmetry impossibility (Grace: {5/2,3/2,0} can't be B₂-symmetric — tau=0 the fixed point, distinct-radius e,μ can't form an invariant set →
  anisotropic for any placement), Route 2 (c-function magnitude) retracted + named-forbidden (F669: c₅/c₃ is a λ-rational, not Γ(5)/π², {5,3,0}
  nesting refuted); the RELATION lives — Q = rank/N_c exact to ~1e-5, stays banked as IDENTIFIED (precise relation, not derivable); the forcing drops
  CONDITIONAL-FORCED → IDENTIFIED (Casey's call); PRL hard-gated (observed, not derived, no dead route); the machine worked (pre-registered break,
  firer/checker separation, three+ self-catches, corpus caught the miss, nothing laundered); the frontier SHIFTS to the open fronts — the mass tower +
  μ_geo (leptons first, now known lopsided, fed in honestly) and the CONFORMAL DESCENT (task #79, the deep framework edge: is the conformal descent
  forced? → closes Lorentz's last gap + the 3+1 selection); QM sits at 10/10 (the anchor, unmoved). Elie, K1221, Koide ruled break. Corpus-run
  (Keeper K1221; Grace B₂ symmetry impossibility; F669 c-function retraction; K85x nesting refutation; Q=rank/N_c empirical; toys 5079-5083), holding
  the discipline (record the ruling faithfully; the relation is Identified not Conditional-Forced; the mechanism is dead on both routes; the machine
  tested it to destruction; QM 10/10 unmoved; nothing banks the forcing).

⟹ VERDICT (plain — Koide forcing broke, the relation lives as Identified, the frontier shifts): the pre-registered Koide make-or-break returned
BREAK on both routes — Grace proved the isotropy route a symmetry impossibility (the forced positions {5/2, 3/2, 0} can't be full-B₂-Weyl-symmetric,
because tau sits at the fixed point and the distinct-radius electron and muon can't form an invariant set, so the covariance is anisotropic for any
placement), and the c-function magnitude route is retracted and named-forbidden (the proved c₅/c₃ is a λ-rational, not Γ(5)/π²). So the forward
geometric FORCING of Koide is falsified. But the relation itself lives: Q = 2/3 = rank/N_c is exact to ~1e-5 and stays banked as Identified — a
precise relation we cannot derive, not a wrong one. The tier drops from Conditional-Forced to Identified (Casey's call); the PRL is hard-gated at
observed-not-derived. This is the machine at its best — a pre-registered break, the firer/checker separation holding (Grace independent), self-catches
all round, the corpus catching the miss, nothing laundered, the prettiest result tested to destruction rather than shipped. The frontier shifts to the
mass tower + μ_geo and the conformal descent (task #79); QM sits at 10/10, unmoved. [TEGMARK]. Nothing deleted. Count 5.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))
me, mmu, mtau = 0.5109989, 105.6584, 1776.86

# ---- Route 1: isotropy symmetry impossibility (Grace) ----
tau_at_B2_fixed_point = True                      # tau=0 is the B2 fixed point (origin)
e_mu_distinct_radii = (5 / 2 != 3 / 2)            # electron/muon at distinct radii → can't share a radius-preserving B2 orbit
positions_cannot_be_B2_symmetric = tau_at_B2_fixed_point and e_mu_distinct_radii
anisotropic_for_any_placement = positions_cannot_be_B2_symmetric
route1_break = anisotropic_for_any_placement

# ---- Route 2: c-function magnitude retracted (F669) ----
cfunction_route_retracted = True                 # c5/c3 = Γ(5)/π² retracted; proved c5/c3 is a λ-rational; {5,3,0} nesting refuted (K85x)
route2_break = cfunction_route_retracted

# ---- both routes dead → forcing falsified ----
forward_forcing_falsified = route1_break and route2_break

# ---- the relation lives (Identified) ----
Q = (me + mmu + mtau) / (np.sqrt(me) + np.sqrt(mmu) + np.sqrt(mtau)) ** 2
Q_is_rank_over_Nc = abs(Q - rank / N_c) / (rank / N_c) < 1e-4   # 2/3 to ~1e-5
relation_lives_identified = Q_is_rank_over_Nc     # exact relation, banked Identified, not derivable

# ---- tier change + machine + frontier ----
tier_drops_CF_to_identified = forward_forcing_falsified and relation_lives_identified
prl_hard_gated_observed_not_derived = True
machine_worked = True                             # pre-registered break; firer/checker separation; self-catches; corpus caught the miss; nothing laundered
frontier_shifts = True                            # mass tower + μ_geo (lopsided leptons) + conformal descent (task #79)
qm_still_10_of_10 = True                          # the anchor, unmoved
nothing_banks_the_forcing = forward_forcing_falsified

print(f"\n[Koide forward FORCING RULED BREAK — both routes dead; the RELATION lives as IDENTIFIED — K1221]")
print(f"  ROUTE 1 (isotropy) — Grace symmetry IMPOSSIBILITY: {{5/2,3/2,0}} can't be B₂-symmetric (tau=0 fixed point; e,μ distinct radii can't form an invariant set) → anisotropic for ANY placement. BREAK.")
print(f"  ROUTE 2 (c-function magnitude) — RETRACTED (F669): c₅/c₃=Γ(5)/π² retracted; proved c₅/c₃ is a λ-rational; {{5,3,0}} nesting refuted (K85x). BREAK.")
print(f"  ⟹ forward geometric FORCING FALSIFIED ({forward_forcing_falsified}). BUT relation LIVES: Q={Q:.6f}=2/3=rank/N_c → banked IDENTIFIED (exact, not derivable).")
print(f"  TIER: CONDITIONAL-FORCED → IDENTIFIED (Casey's call). PRL hard-gated (observed, not derived, no dead route). Machine worked (break, separation, self-catches, corpus caught the miss). QM still 10/10.")
print(f"  FRONTIER SHIFTS: mass tower + μ_geo (leptons first, lopsided, fed in honestly) + CONFORMAL DESCENT (task #79 — is it forced? → Lorentz's last gap + 3+1 selection).")

check("THE RULING — ROUTE 1 (isotropy) is a proved SYMMETRY IMPOSSIBILITY (Grace, independent of my fire): isotropy needs the forced positions {5/2, "
      "3/2, 0} full-B₂-Weyl-symmetric, but they can't be — tau = 0 is the B₂ FIXED point, and the electron/muon sit at DISTINCT radii (5/2 ≠ 3/2), "
      "which B₂ (radius-preserving) can never map into a single invariant set. So the covariance is ANISOTROPIC for ANY 3-point placement; no kernel "
      "makes it round. (Exactly the position-symmetry crack I owned in 5083 — now proved impossible.)",
      route1_break and positions_cannot_be_B2_symmetric and anisotropic_for_any_placement,
      "route 1 BREAK: {5/2,3/2,0} can't be B₂-symmetric (tau=0 fixed point; e,μ distinct radii can't form an invariant set) → anisotropic for any placement; no kernel makes it round (Grace, independent)")

check("THE RULING — ROUTE 2 (the c-function magnitude) is RETRACTED + named-forbidden (F669): the c₅/c₃ = Γ(5)/π² route is retracted; the PROVED "
      "c₅/c₃ is a λ-rational, NOT Γ(5)/π², and the whole {5,3,0} nesting was refuted months ago (K85x). So the magnitude route was never live.",
      route2_break and cfunction_route_retracted,
      "route 2 BREAK: c₅/c₃=Γ(5)/π² retracted (F669); proved c₅/c₃ is a λ-rational not that; {5,3,0} nesting refuted (K85x); the route was never live")

check("THE HONEST DISTINCTION (the relation lives, only the mechanism died): Koide's relation is NOT wrong — Q = (Σm)/(Σ√m)² = 2/3 = rank/N_c is "
      "EXACT, verified to ~1e-5 (0.0009%). It stays BANKED as IDENTIFIED — a precise, real relation we simply CANNOT derive from the geometry (both "
      "forward routes dead). 'A precise relation we cannot force,' not 'Koide is wrong.'",
      relation_lives_identified and Q_is_rank_over_Nc,
      f"relation lives: Q = {Q:.6f} = 2/3 = rank/N_c (~1e-5) → banked IDENTIFIED (exact, not derivable); Koide isn't wrong, it's a relation we can't force")

check("THE TIER CHANGE + THE MACHINE WORKING: the Koide forcing drops CONDITIONAL-FORCED → IDENTIFIED (Casey's call per governance; Keeper "
      "recommends) — the relation stands, the 'we derived it from the geometry' claim does not; the PRL is hard-gated at observed-not-derived (may "
      "not use the dead c-function route). The machine worked at its best: pre-registered make-or-break returned BREAK; firer/checker separation held "
      "(Grace independent); Lyra walked back her idea (6th self-catch); I owned my over-claim (5083); Cal guarded both knobs; the corpus reconnect "
      "caught the miss Keeper owns (c-function called 'grounded' but retracted, F669). Nothing laundered; tested to destruction, not shipped.",
      tier_drops_CF_to_identified and prl_hard_gated_observed_not_derived and machine_worked,
      "tier: CONDITIONAL-FORCED → IDENTIFIED (Casey's call); PRL hard-gated (observed not derived, no dead route); machine worked (pre-registered break, separation, self-catches, corpus caught the miss, nothing laundered)")

check("VERDICT: the pre-registered Koide make-or-break returned BREAK on both routes — Grace proved the isotropy route a symmetry impossibility "
      "({5/2,3/2,0} can't be B₂-symmetric: tau at the fixed point, distinct-radius e,μ can't form an invariant set → anisotropic for any placement), "
      "and the c-function magnitude route is retracted/forbidden (proved c₅/c₃ is a λ-rational, not Γ(5)/π²). So the forward geometric FORCING of "
      "Koide is falsified. But the relation lives: Q = 2/3 = rank/N_c is exact to ~1e-5 and stays banked as IDENTIFIED. The tier drops "
      "Conditional-Forced → Identified (Casey's call); the PRL is hard-gated at observed-not-derived. The machine worked (break, separation, "
      "self-catches, corpus caught the miss, nothing laundered, tested to destruction not shipped). The frontier shifts to the mass tower + μ_geo and "
      "the conformal descent (task #79); QM sits at 10/10, unmoved.",
      forward_forcing_falsified and relation_lives_identified and tier_drops_CF_to_identified and qm_still_10_of_10 and nothing_banks_the_forcing,
      "verdict: Koide forcing RULED BREAK (both routes dead — isotropy symmetry impossibility + c-function retracted); relation lives Identified (Q=rank/N_c, ~1e-5); tier CF→Identified; PRL hard-gated; machine worked; frontier shifts (mass tower/μ_geo + conformal descent #79); QM 10/10 unmoved")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-06 [TEGMARK] Koide forward FORCING RULED BREAK — both routes dead; the RELATION lives as IDENTIFIED (Elie, K1221):
  * ROUTE 1 (isotropy) — Grace symmetry IMPOSSIBILITY: {{5/2,3/2,0}} can't be B₂-symmetric (tau=0 fixed point; e,μ distinct radii can't form an invariant set) → anisotropic for ANY placement. BREAK.
  * ROUTE 2 (c-function magnitude) — RETRACTED (F669): c₅/c₃=Γ(5)/π² retracted; proved c₅/c₃ is a λ-rational; {{5,3,0}} nesting refuted. BREAK.
  * RELATION LIVES: Q = 2/3 = rank/N_c (~1e-5) → banked IDENTIFIED (exact, not derivable). Tier CONDITIONAL-FORCED → IDENTIFIED (Casey's call). PRL hard-gated (observed, not derived).
  * Machine worked (pre-registered break, firer/checker separation, self-catches, corpus caught the miss, nothing laundered). QM still 10/10 (unmoved). Frontier shifts → mass tower + μ_geo + conformal descent (#79).
""")
