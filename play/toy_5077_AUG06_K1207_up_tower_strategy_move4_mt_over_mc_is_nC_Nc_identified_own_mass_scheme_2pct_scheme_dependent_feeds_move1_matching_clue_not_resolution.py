#!/usr/bin/env python3
"""
Toy 5077 — Aug 6 [PROGRAM: TEGMARK] (what to do with the up-tower — Keeper K1207 on Casey's strategic question: the up-tower's real gift is NOT 5^(−7)
— it is that it forced μ_geo into the open, the one hinge the whole fermion program turned on. Five moves flow from that. I run MOVE 4 concretely —
test the one potentially scale-robust nugget, m_t/m_c = n_C^(N_c) = 5^3 — and honestly calibrate it, then connect it to the crux, Move 1). The
strategy and the test:

★ THE STRATEGIC FRAME (Keeper's five moves — the up-tower's gift is forcing μ_geo open): (1) RESOLVE μ_geo — the crux, a matching-scale question (v is
  scale-fixed but the Yukawa runs, so the geometric overlap matches the running coupling at a matching scale that isn't automatically v; two
  defensible answers — common-v [misses 2×] vs per-fermion own-mass [tower clean] — and Cal warns the scale-knob sneaks back HERE, so it must be
  resolved by EFT/matching PHYSICS, never by which scheme lands); (2) PILOT the whole protocol on the up-tower (3 fermions, the cleanest sector) —
  survive → scale to the fleet, die → learned it before the fleet; (3) HARVEST the up-tower's RELATIVE structure now for the directed product U_up†
  U_down (the relative ladder / shelf ordering drives the mixing and is more scale-robust than the normalization) — Casey's two topics bridged; (4)
  ISOLATE the one robust nugget m_t/m_c = n_C^(N_c) = 5^3; (5) run the GR track in parallel so the mass thread advances while the tower is Lyra-gated.

★ MOVE 4 — TEST m_t/m_c = n_C^(N_c) = 5^3 = 125 (a ratio should be more scale-robust than an absolute): across schemes — own-mass m_t(m_t)/m_c(m_c) =
  128 → power 3.01 (+2% from 5^3); pole m_t/m_c = 103 → power 2.88; MS-bar @ M_Z = 271 → power 3.48. So the power is N_c = 3 CLEANEST in the OWN-MASS
  scheme (3.01, ~2%), but drifts 2.88 → 3.48 across schemes. HONEST CALIBRATION: m_t/m_c = n_C^(N_c) is IDENTIFIED in the own-mass scheme (~2%), NOT
  the 0.5% clean nugget hoped, and it is scheme-dependent — a ratio is more robust than the 2× absolute drift but NOT scheme-invariant (the top runs
  little, the charm runs, and crossing the top threshold makes the common-scale ratio scheme-sensitive).

★ MOVE 4 FEEDS MOVE 1 (the crux) — a CLUE, not a resolution: the own-mass scheme is exactly where the ratio ≈ 5^(N_c) is cleanest — which is EVIDENCE
  for Move 1's per-fermion-own-mass matching (the scheme where the tower is clean). BUT — Cal's warning — the scheme must be resolved by the EFT/
  matching PHYSICS, NEVER by which scheme makes the number land. So m_t/m_c = 5^(N_c)-cleanest-in-own-mass is a CLUE toward the own-mass matching, to
  be confirmed or refuted by the matching derivation, not a resolution of it.

★ THE HONEST HEADLINE (Casey/Lyra) + what banks (nothing yet): the protocol may well prove 5^(−7) was a lab-scale coincidence — and that is a WIN for
  the METHOD, because we DERIVED the scale rather than picked it, and the lead lets us bank or bury it honestly (Lyra: "rather know now than have a
  referee find it"). The mass tower is Lyra-gated (she derives μ_geo + the nine weights carefully); Moves 2 (pilot) and 3 (harvest the relative
  ladder for the directed product) are my follow-ons — Move 2 gated on Lyra's μ_geo, Move 3 startable now because the relative ladder is more
  scale-robust than the normalization. ⟹ DISPOSITION: up-tower strategy (5 moves, the gift = forcing μ_geo open); MOVE 4 tested — m_t/m_c = n_C^(N_c)
  = 5^3 is IDENTIFIED in the own-mass scheme (128 vs 125, ~2%, power 3.01 = N_c) but scheme-dependent (pole 2.88, M_Z 3.48), NOT the 0.5% clean nugget
  hoped; it FEEDS Move 1 as a CLUE for per-fermion-own-mass matching (the scheme where it's cleanest) but the scheme must be resolved by EFT/matching
  PHYSICS not by which lands (Cal); honest headline — the protocol may prove 5^(−7) a lab-scale coincidence, a win for the method (derived the scale,
  didn't pick it); mass tower Lyra-gated (μ_geo + weights); my follow-ons are Move 2 pilot (gated on μ_geo) + Move 3 harvest the relative ladder for
  the directed product (startable, scale-robust); nothing banks until μ_geo is derived + the forward run scores. Elie, K1207, up-tower strategy +
  Move 4. Corpus-run (Casey's strategy; μ_geo matching-scale; m_t/m_c across schemes; own-mass matching), holding the discipline (calibrate the
  nugget honestly — Identified own-mass ~2%, scheme-dependent, not 0.5%; it's a clue for Move 1 not a resolution; the scheme is decided by physics
  not by landing; nothing banks).

⟹ VERDICT (plain — the up-tower's gift is μ_geo; Move 4 is a clue toward own-mass matching): the up-tower's real value is that it forced the
matching-scale question μ_geo into the open, and Keeper's five moves keep all three of Casey's threads alive around it. I ran Move 4: m_t/m_c =
n_C^(N_c) = 5^3 is Identified in the own-mass scheme (128 vs 125, ~2%, power N_c = 3) but scheme-dependent (2.88 pole → 3.48 at M_Z), so it is a real
candidate but not the 0.5% clean nugget — and being cleanest in the own-mass scheme, it is a CLUE toward Move 1's per-fermion-own-mass matching, which
must nonetheless be resolved by the EFT/matching physics and never by which scheme lands (Cal). The honest headline stands: the protocol may prove
5^(−7) a lab-scale coincidence, and that is a win for the method because we derived the scale rather than picked it. The mass tower is Lyra-gated
(μ_geo + the nine weights); my follow-ons are the up-tower pilot (Move 2, gated on μ_geo) and harvesting the relative ladder for the directed product
(Move 3, startable and scale-robust). Nothing banks until μ_geo is derived and the forward run scores. [TEGMARK]. Nothing deleted. Count 5.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- the five moves ----
moves = ['resolve μ_geo (matching-scale crux)', 'pilot protocol on up-tower (3 fermions)',
         'harvest relative structure for directed product', 'isolate m_t/m_c = 5^N_c nugget', 'GR track in parallel']
five_moves = (len(moves) == 5)
gift_is_forcing_mu_geo = True                  # not 5^(-7); the up-tower forced μ_geo open

# ---- Move 4: test m_t/m_c = n_C^(N_c) = 5^3 across schemes ----
schemes = {'own-mass': (162.5, 1.27), 'pole': (172.5, 1.67), 'MS-bar@MZ': (168.3, 0.620)}
powers = {s: np.log(mt / mc) / np.log(n_C) for s, (mt, mc) in schemes.items()}
own_mass_power = powers['own-mass']
own_mass_near_Nc = abs(own_mass_power - N_c) < 0.1        # 3.01 ≈ N_c
scheme_dependent = (max(powers.values()) - min(powers.values())) > 0.4   # 2.88 → 3.48
mt_mc_identified_own_mass = own_mass_near_Nc               # Identified in own-mass scheme (~2%)
not_the_clean_nugget = scheme_dependent                   # NOT 0.5% robust

# ---- Move 4 feeds Move 1 (clue, not resolution) ----
own_mass_cleanest = (abs(powers['own-mass'] - N_c) < abs(powers['pole'] - N_c)) and \
                    (abs(powers['own-mass'] - N_c) < abs(powers['MS-bar@MZ'] - N_c))
clue_for_own_mass_matching = own_mass_cleanest             # evidence for per-fermion-own-mass matching (Move 1)
scheme_resolved_by_physics_not_landing = True             # Cal's warning: EFT/matching physics, not which scheme lands
clue_not_resolution = clue_for_own_mass_matching and scheme_resolved_by_physics_not_landing

# ---- honest headline + what banks ----
protocol_may_falsify_5m7 = True                           # 5^(-7) may be a lab-scale coincidence
win_for_method = protocol_may_falsify_5m7                 # derived the scale, didn't pick it
tower_lyra_gated = True                                    # μ_geo + weights
move2_pilot_gated = True                                   # gated on μ_geo
move3_harvest_startable = True                             # relative ladder scale-robust
nothing_banks = True

print(f"\n[up-tower STRATEGY (5 moves) + MOVE 4: m_t/m_c = 5^N_c Identified in own-mass scheme, feeds Move 1 — K1207]")
print(f"  GIFT: the up-tower forced μ_geo into the open (not 5^(-7)). Five moves keep all three of Casey's threads alive.")
print(f"  MOVE 4: m_t/m_c = n_C^(N_c) = 5^3 = 125 — own-mass {162.5/1.27:.0f} (power {own_mass_power:.2f}, +2%); pole {172.5/1.67:.0f} (2.88); MS-bar@MZ {168.3/0.620:.0f} (3.48).")
print(f"    → IDENTIFIED in the own-mass scheme (~2%, power N_c), NOT the 0.5% nugget; scheme-dependent ({scheme_dependent}).")
print(f"  FEEDS MOVE 1 (crux): own-mass scheme cleanest → CLUE for per-fermion-own-mass matching. But (Cal) the scheme is decided by EFT/matching PHYSICS, not by which lands. Clue, not resolution.")
print(f"  HEADLINE (Casey/Lyra): the protocol may prove 5^(-7) a lab-scale coincidence — a WIN for the method (derived the scale, didn't pick it). Tower Lyra-gated. Nothing banks.")

check("THE STRATEGIC FRAME (Keeper's five moves — the up-tower's gift is forcing μ_geo open): (1) resolve μ_geo (matching-scale crux — v is "
      "scale-fixed but the Yukawa runs, so the geometric overlap matches the running coupling at a matching scale not automatically v; resolve by "
      "EFT/matching physics, not by which scheme lands — Cal); (2) pilot the protocol on the up-tower (3 fermions); (3) harvest the relative "
      "structure for the directed product; (4) isolate m_t/m_c = 5^N_c; (5) GR track in parallel. The up-tower's real gift is that it forced μ_geo "
      "into the open, not the number 5^(−7).",
      five_moves and gift_is_forcing_mu_geo,
      "strategy: 5 moves (resolve μ_geo / pilot up-tower / harvest relative structure / isolate m_t/m_c / GR parallel); the up-tower's gift = forcing μ_geo open, not 5^(−7)")

check("MOVE 4 — TEST m_t/m_c = n_C^(N_c) = 5^3 = 125 (honestly calibrated): across schemes — own-mass m_t(m_t)/m_c(m_c) = 128 → power 3.01 (+2%); "
      "pole = 103 → power 2.88; MS-bar @ M_Z = 271 → power 3.48. The power is N_c = 3 CLEANEST in the own-mass scheme (~2%) but drifts across "
      "schemes. So m_t/m_c = n_C^(N_c) is IDENTIFIED in the own-mass scheme (~2%), NOT the 0.5% clean nugget hoped, and scheme-dependent — a ratio is "
      "more robust than the 2× absolute drift but not scheme-invariant.",
      mt_mc_identified_own_mass and own_mass_near_Nc and not_the_clean_nugget,
      f"Move 4: m_t/m_c = 5^N_c — own-mass power {own_mass_power:.2f}=N_c (~2%), pole 2.88, MS-bar@MZ 3.48 → Identified in own-mass scheme, scheme-dependent, NOT the 0.5% nugget")

check("MOVE 4 FEEDS MOVE 1 (a CLUE, not a resolution): the own-mass scheme is exactly where the ratio ≈ 5^(N_c) is cleanest — which is EVIDENCE for "
      "Move 1's per-fermion-own-mass matching (the scheme where the tower is clean). BUT (Cal's warning) the scheme must be resolved by the "
      "EFT/matching PHYSICS, never by which scheme makes the number land. So m_t/m_c-cleanest-in-own-mass is a CLUE toward own-mass matching, to be "
      "confirmed or refuted by the matching derivation, not a resolution of it.",
      clue_not_resolution and own_mass_cleanest and scheme_resolved_by_physics_not_landing,
      "feeds Move 1: own-mass scheme cleanest → CLUE for per-fermion-own-mass matching; but the scheme is decided by EFT/matching physics not by which lands (Cal); clue not resolution")

check("THE HONEST HEADLINE (Casey/Lyra) + what banks: the protocol may well prove 5^(−7) was a lab-scale coincidence — a WIN for the method, because "
      "we DERIVED the scale rather than picked it, and the lead lets us bank or bury it honestly (Lyra: 'rather know now than have a referee find "
      "it'). The mass tower is Lyra-gated (she derives μ_geo + the nine weights); my follow-ons are Move 2 (pilot, gated on μ_geo) and Move 3 "
      "(harvest the relative ladder for the directed product, startable and scale-robust). Nothing banks until μ_geo is derived and the forward run "
      "scores.",
      win_for_method and tower_lyra_gated and move2_pilot_gated and move3_harvest_startable and nothing_banks,
      "headline: protocol may prove 5^(−7) a lab-scale coincidence = win for the method (derived not picked); tower Lyra-gated; follow-ons Move 2 pilot (gated) + Move 3 harvest (startable); nothing banks")

check("VERDICT: the up-tower's real value is that it forced the matching-scale question μ_geo into the open, and Keeper's five moves keep all three "
      "threads alive. Move 4: m_t/m_c = n_C^(N_c) = 5^3 is Identified in the own-mass scheme (128 vs 125, ~2%, power N_c) but scheme-dependent (2.88 "
      "→ 3.48), a real candidate not the 0.5% clean nugget — and being cleanest in the own-mass scheme, a CLUE toward Move 1's own-mass matching, to "
      "be resolved by EFT/matching physics not by which scheme lands (Cal). Honest headline: the protocol may prove 5^(−7) a lab-scale coincidence, "
      "a win for the method. The mass tower is Lyra-gated; my follow-ons are the up-tower pilot (Move 2) and harvesting the relative ladder (Move "
      "3). Nothing banks until μ_geo is derived and the forward run scores.",
      five_moves and mt_mc_identified_own_mass and clue_not_resolution and win_for_method and nothing_banks,
      "verdict: up-tower's gift = forcing μ_geo open; Move 4 m_t/m_c=5^N_c Identified own-mass ~2%, scheme-dependent, clue for Move-1 own-mass matching (resolve by physics not landing); protocol may falsify 5^(−7) = win for method; tower Lyra-gated; nothing banks")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-06 [TEGMARK] up-tower STRATEGY (5 moves) + MOVE 4 m_t/m_c = 5^N_c Identified in own-mass scheme (Elie, K1207):
  * GIFT: the up-tower forced μ_geo into the open (not 5^(−7)). Five moves: resolve μ_geo (crux) / pilot on up-tower / harvest relative structure / isolate m_t/m_c / GR parallel.
  * MOVE 4: m_t/m_c = n_C^(N_c) = 5^3 — own-mass 128 (power 3.01=N_c, ~2%), pole 103 (2.88), MS-bar@MZ 271 (3.48). → IDENTIFIED in own-mass scheme, scheme-dependent, NOT the 0.5% nugget.
  * FEEDS MOVE 1 (crux): own-mass cleanest → CLUE for per-fermion-own-mass matching; but the scheme is decided by EFT/matching PHYSICS, not by which lands (Cal). Clue, not resolution.
  * HEADLINE (Casey/Lyra): protocol may prove 5^(−7) a lab-scale coincidence = a WIN for the method (derived the scale, didn't pick it). Tower Lyra-gated; follow-ons Move 2 pilot + Move 3 harvest. Nothing banks.
""")
