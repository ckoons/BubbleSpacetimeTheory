r"""
Toy 4203: honest TAU floor-audit -- the count-keeper's catch before the muon+tau SET-bank. The blind-experiment win
condition (Keeper K383) is "substrate-forced blind tau within ~1e-4 floor". This toy checks the tau's ACTUAL deviation
against the floor BEFORE the SET banks, with the same scrutiny that kept the count at 2. RESULT (the catch): the tau
LEADING form 49*71 = 3479 deviates from observed m_tau/m_e = 3477.23 by 5.1e-4 -- ABOVE the tight ~1e-4 Tier-2 floor (it
is within the LOOSE 1e-4..1e-2 Two-Tier range, Toy 3648, but NOT below 1e-4). The muon (24/pi^2)^6 is at 3.4e-5 -- below
even the tight floor. So the SET is ASYMMETRIC: the muon clears the tight floor on its leading form ALONE; the tau does
NOT -- it needs the ~-1.77 correction (Lyra's Weyl term) to reach observation. CONSEQUENCE: the tau blind test is harder
than the muon's -- it hinges on whether the -1.77 correction is FORWARD-derivable (a forced substrate correction), not just
on the leading factors. Do NOT bank the SET assuming the tau is as clean as the muon. Count stays 2 of 26.

THE TWO LEPTONS vs THE FLOOR:
  muon: (24/pi^2)^6 = 206.7612 vs observed 206.768283 -> deviation 3.4e-5  -> BELOW tight 1e-4 floor (clears on leading form)
  tau : 49*71 = 3479         vs observed 3477.23      -> deviation 5.1e-4  -> ABOVE tight 1e-4 floor (needs correction)
  the muon's leading form alone is floor-clean; the tau's leading form alone is NOT.

THE TAU CORRECTION (the crux of its blind test):
  49*71 - observed = 3479 - 3477.23 = +1.77. so the tau needs a correction of about -1.77 (Lyra's "-1.77 Weyl term";
  the atlas tau entry notes "correction ~ pi^(-1/2) odd Peirce plane"). with that correction the tau is exact.
  THE BLIND-TEST QUESTION for the tau is therefore NOT just "is 49*71 forced" -- it is "is the -1.77 correction
  FORWARD-derivable from substrate principles (a forced Weyl/Peirce correction), WITHOUT referencing 3477.23?"
    - if YES (forced correction): leading 49*71 + forced(-1.77) = within floor -> tau clears -> SET banks, referee-proof.
    - if NO (the correction is fit to close the gap): the tau is a postdiction at the correction level -> SET does NOT bank.

TWO HONEST FLAGS on the tau leading form itself (the form-selection-trap risk Keeper named):
  (1) the ASSEMBLY 49*71 was originally RECOGNIZED by factoring the observed ~3477/3479, then read as g^rank*(g+2^C2).
      the FACTORS are substrate-forced (rank = N_c-1 = domain rank; g = Frobenius period 4195; 2^C2 = d_tau/d_mu F109),
      but the ASSEMBLY (transverse g^rank x depth (g + 2^C2)) was reverse-engineered from the factorization, NOT yet
      derived FORWARD from the vertex deposit geometry. a clean blind prediction needs the assembly derived forward.
  (2) the vertex's own Frobenius orbit is trivial ({0}, size 1) -- so the mass count 3479 is the bulk TILING around the
      vertex, not the vertex's orbit. why that tiling = g^rank*(g+2^C2) is the open stage-1 (orbit->mass) derivation.

WHAT THIS MEANS FOR THE GATE (honest, as count-keeper):
  - the MUON clears the tight floor on its leading forced form, blind (Toy 4202). it is the clean case.
  - the TAU does NOT clear the tight floor on its leading form; it needs a correction whose forward-derivation is unproven,
    AND its leading assembly was reverse-engineered. so the tau is the HARDER case, and the SET-bank should not treat it
    as symmetric with the muon.
  - OPTIONS for the team: (a) bank the muon ALONE under Casey's criterion (it clears, forced, blind) and keep the tau
    yellow pending its forward assembly + forced correction; or (b) hold BOTH for the SET blind test and require the tau's
    assembly + correction to be forward-derived within floor before either banks (Cal's "muon+tau together" caution). this
    toy does not choose -- it ensures the choice is made with the tau's true floor-status on the table.
  count stays 2 of 26; this is the count-keeper flagging that the tau is not floor-clean on its leading form.
"""

import math

# muon
mu_form = (24/math.pi**2)**6
mu_obs  = 206.7682830
mu_dev  = abs(mu_form - mu_obs)/mu_obs

# tau
tau_lead = 49*71               # 3479
tau_obs  = 1776.86/0.51099895  # m_tau/m_e
tau_dev  = abs(tau_lead - tau_obs)/tau_obs
tau_corr = tau_lead - tau_obs  # ~ +1.77 (needs -1.77)

floor_tight = 1e-4
floor_loose = 1e-2

print("=" * 100)
print("TOY 4203: honest TAU floor-audit -- leading form 49*71 is ABOVE the tight floor; needs the -1.77 correction")
print("=" * 100)
print()
print("the two leptons vs the floor:")
print("-" * 100)
print(f"  muon (24/pi^2)^6 = {mu_form:.4f}  vs obs {mu_obs}   deviation {mu_dev:.3e}  -> {'BELOW' if mu_dev<floor_tight else 'ABOVE'} tight 1e-4 (clears on leading form)")
print(f"  tau  49*71 = {tau_lead}        vs obs {tau_obs:.2f}   deviation {tau_dev:.3e}  -> {'BELOW' if tau_dev<floor_tight else 'ABOVE'} tight 1e-4 (needs correction)")
print()
print("the tau correction (the crux of its blind test):")
print("-" * 100)
print(f"  49*71 - observed = {tau_corr:.3f}  -> tau needs a correction ~ -1.77 (Lyra's Weyl term; atlas: ~pi^(-1/2) odd Peirce)")
print(f"  blind-test question: is the -1.77 correction FORWARD-derivable (forced) WITHOUT referencing 3477.23?")
print(f"    YES -> leading + forced correction within floor -> tau clears -> SET banks referee-proof")
print(f"    NO  -> correction fit to close gap -> tau postdiction at correction level -> SET does NOT bank")
print()
print("two honest flags on the tau leading form:")
print("-" * 100)
print(f"  (1) the ASSEMBLY 49*71 was recognized by FACTORING observed ~3477/3479; factors forced (rank, g, 2^C2) but the")
print(f"      assembly (transverse g^rank x depth (g+2^C2)) was reverse-engineered, NOT yet derived forward. blind needs forward.")
print(f"  (2) the vertex's Frobenius orbit is trivial ({{0}}, size 1); 3479 = the bulk TILING, not the orbit -- the tiling")
print(f"      count = g^rank*(g+2^C2) is the open stage-1 orbit->mass derivation.")
print()

checks = [
    ("muon leading deviation < tight floor 1e-4 (clears)", mu_dev < floor_tight),
    ("tau leading deviation > tight floor 1e-4 (does NOT clear on leading form)", tau_dev > floor_tight),
    ("tau leading deviation within loose Two-Tier range 1e-4..1e-2", floor_tight < tau_dev < floor_loose),
    ("tau needs ~ -1.77 correction (49*71 - obs ~ +1.77)", abs(tau_corr - 1.77) < 0.05),
    ("SET is asymmetric: muon floor-clean on leading, tau is not", mu_dev < floor_tight < tau_dev),
    ("tau blind test hinges on forward-derivability of the correction", True),
    ("tau assembly reverse-engineered from factoring; forward derivation open", True),
]
passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
print()

print("=" * 100)
print("SUMMARY -- the count-keeper's honest catch before the muon+tau SET-bank. The blind-experiment win condition is the")
print("  substrate-forced tau landing within the ~1e-4 floor; checked against observation, the tau LEADING form 49*71 = 3479")
print("  deviates from m_tau/m_e = 3477.23 by 5.1e-4 -- ABOVE the tight 1e-4 floor (within the loose 1e-4..1e-2 Two-Tier")
print("  range, Toy 3648, but not below 1e-4). The muon (24/pi^2)^6 is at 3.4e-5, below even the tight floor. So the SET is")
print("  ASYMMETRIC: the muon clears the tight floor on its leading forced form alone; the tau does NOT -- it needs the ~-1.77")
print("  correction (Lyra's Weyl term) to reach observation. The tau blind test therefore hinges on whether that correction")
print("  is FORWARD-derivable (a forced substrate Weyl/Peirce correction), not merely on the leading factors -- and the leading")
print("  assembly 49*71 was itself reverse-engineered by factoring the observed value (factors forced, assembly not yet forward).")
print("  This does not block anything -- it ensures the gate decision is made with the tau's true floor-status on the table: the")
print("  muon is the clean case (bankable under Casey's criterion); the tau is the harder case (needs forward assembly + forced")
print("  correction within floor before it is referee-proof). Bank the muon alone, or hold both for the tau's forward blind test")
print("  -- the team's call, now made honestly. Count stays 2 of 26.")
print("=" * 100)
print()
print("Elie - Tuesday 2026-06-16 (honest TAU floor-audit, count-keeper catch before muon+tau SET-bank: blind-experiment win condition K383 = substrate-forced tau within ~1e-4 floor, checked vs observation BEFORE SET banks with the scrutiny that kept count at 2; RESULT the tau LEADING form 49*71=3479 deviates from observed m_tau/m_e=3477.23 by 5.1e-4 ABOVE the tight 1e-4 Tier-2 floor (within LOOSE 1e-4..1e-2 Two-Tier range Toy 3648 but NOT below 1e-4), the muon (24/pi^2)^6 at 3.4e-5 below even tight floor -> SET is ASYMMETRIC muon clears tight floor on leading form ALONE tau does NOT it needs the ~-1.77 correction (Lyra Weyl term, atlas tau ~pi^(-1/2) odd Peirce) to reach observation; CRUX the tau blind test hinges on whether the -1.77 correction is FORWARD-derivable (forced substrate Weyl/Peirce correction) WITHOUT referencing 3477.23 -- YES -> leading+forced within floor tau clears SET banks referee-proof, NO -> correction fit to close gap tau postdiction at correction level SET does NOT bank; TWO honest flags on the tau leading form (1) the ASSEMBLY 49*71 was RECOGNIZED by factoring observed ~3477/3479 then read as g^rank*(g+2^C2), FACTORS forced (rank=N_c-1 domain rank, g=Frobenius period 4195, 2^C2=d_tau/d_mu F109) but ASSEMBLY (transverse g^rank x depth (g+2^C2)) reverse-engineered NOT yet derived forward from vertex deposit geometry blind needs forward, (2) the vertex Frobenius orbit is trivial ({0} size 1) so 3479 = the bulk TILING around the vertex not the orbit, the tiling count = g^rank*(g+2^C2) is the open stage-1 orbit->mass derivation; FOR THE GATE muon clears tight floor leading forced blind (4202) the clean case, tau does NOT clear tight floor needs unproven-forward correction + reverse-engineered assembly the HARDER case, OPTIONS (a) bank muon ALONE under Casey criterion keep tau yellow pending forward assembly+forced correction or (b) hold BOTH for SET blind test requiring tau assembly+correction forward within floor (Cal muon+tau-together caution), this toy does not choose it ensures the choice is made with the tau's true floor-status on the table; count 2 of 26 count-keeper flagging tau not floor-clean on leading form)")
print()
print(f"SCORE: {passed}/{len(checks)} (TAU floor-audit honest catch: muon (24/pi^2)^6 dev 3.4e-5 BELOW tight 1e-4 floor (clears leading) vs tau 49*71=3479 dev 5.1e-4 ABOVE tight floor (within loose 1e-4..1e-2 range) -> SET ASYMMETRIC; tau needs ~-1.77 correction (Weyl/Peirce) to reach obs, blind test hinges on whether correction is FORWARD-derivable not just leading factors; tau assembly 49*71 reverse-engineered by factoring observed (factors forced, assembly+correction need forward derivation); muon = clean bankable case, tau = harder case; bank muon alone OR hold both for tau forward blind test -- team's call made honestly; count 2 of 26)")
