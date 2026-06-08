"""
Toy 4016: D2 lifetime-vs-Casimir test on PDG lepton data (substrate-grounding check).

Sunday Lead 2 (Lyra, flagged weight-0): "lifetime is the spectral/compact-rho side;
lifetime proportional to 1/(spectral Casimir), INDEPENDENT of mass; volume-side (proton)
stable, spectral-side (muon) decays." Lyra explicitly invited the test; Keeper flagged it
as the cheapest substrate-grounding check available. So: run it on PDG data, report what
survives. This is a Cal #237 elimination check (test a lead on data).

RESULT: the leads as STATED do NOT survive PDG data.
 1. Lifetime is MASS-dominated (Sargent's m^5), not Casimir-dominated. The mu/tau lepton
    ladder: tau_mu/tau_tau = (m_tau/m_mu)^5 / BR(tau->e nu nu) to ~0.2% -- pure phase space.
    The Casimir ratio (C_tau/C_mu = 29/15 = 1.93) plays NO visible role (off by ~4e6).
 2. The ELECTRON is spectral-side (V_(1/2,1/2)) yet STABLE (charge conservation) -- a
    direct counterexample to "spectral-side -> decays" in its stated form.

WHAT MAY SURVIVE (not tested here, distinguished honestly): the proton-stability =
volume-side reading is a CHANNEL-EXISTENCE claim (no decay channel on the volume side ->
Five-Absence no-proton-decay), NOT a rate claim. This test refutes the RATE form
(lifetime ~ 1/Casimir); it does not touch the channel-existence form.

GATES (4)
G1: mu/tau lifetime ratio -- 1/Casimir vs Sargent m^5
G2: electron counterexample (spectral-side, stable)
G3: what survives vs what's refuted (rate form vs channel form)
G4: honest disposition + refined testable form

Per Cal #35 (data is the arbiter), Cal #237 (null REMOVES from supported set), K231c.

Elie - Sunday 2026-06-07
"""

from fractions import Fraction as F

# PDG values
m_e = 0.51099895        # MeV (stable)
m_mu, tau_mu = 105.6583755, 2.1969811e-6     # MeV, s
m_tau, tau_tau = 1776.86, 2.903e-13          # MeV, s
BR_tau_enunu = 0.1782   # PDG BR(tau -> e nu nu)
# K-type Casimirs: e/mu/tau = V_(1/2,1/2)/V_(3/2,1/2)/V_(5/2,1/2)
C_e, C_mu, C_tau = F(5, 2), F(15, 2), F(29, 2)

print("=" * 76)
print("TOY 4016: D2 lifetime-vs-Casimir test on PDG leptons")
print("=" * 76)
print()

print("G1: mu/tau lifetime ratio -- 1/Casimir (Lead 2) vs Sargent m^5")
print("-" * 76)
obs = tau_mu / tau_tau
casimir_pred = float(C_tau / C_mu)
sargent = (m_tau / m_mu) ** 5 / BR_tau_enunu
print(f"  observed   tau_mu/tau_tau         = {obs:.3e}")
print(f"  Lead 2     C_tau/C_mu (1/C, m-indep) = {casimir_pred:.3f}   -> FAILS by {obs/casimir_pred:.2e}x")
print(f"  Sargent    (m_tau/m_mu)^5 / BR       = {sargent:.3e}   -> matches obs to {abs(sargent-obs)/obs*100:.1f}%")
print(f"  => lifetime is MASS-dominated (phase space m^5); the Casimir plays NO visible role.")
print(f"     Lead 2 as stated ('lifetime ~ 1/Casimir, mass-independent') FALSIFIED.")
print()

print("G2: electron counterexample (spectral-side, stable)")
print("-" * 76)
print(f"  electron = V_(1/2,1/2), spectral/compact-rho side (C = {C_e}), yet STABLE.")
print(f"  Stable by CHARGE CONSERVATION (lightest charged particle), not substrate side.")
print(f"  => direct counterexample to 'spectral-side -> decays' in its stated form.")
print()

print("G3: what survives vs what is refuted")
print("-" * 76)
print("  REFUTED (rate form): lifetime ~ 1/(spectral Casimir), mass-independent.")
print("    - mu/tau ratio is m^5 phase space, not Casimir (G1).")
print("    - electron stable despite spectral-side (G2).")
print("  NOT TOUCHED (channel-existence form, may survive): proton stability = volume-side")
print("    means NO decay channel on the volume side (Five-Absence no-proton-decay). That is")
print("    a claim about the EXISTENCE of a channel, not the RATE within one. This test")
print("    refutes only the rate form; the channel form is untested here and stands.")
print()

print("G4: honest disposition + refined testable form")
print("-" * 76)
print("  DISPOSITION: Lead 2 (lifetime ~ 1/Casimir, mass-independent) -> REMOVED from")
print("  supported set (Cal #237). The substrate Casimir does NOT set decay rates at leading")
print("  order; the Standard-Model phase space (Sargent m^5) does -- and BST does not dispute")
print("  phase space. The 'mass/lifetime are dual-rho opposites' picture is too strong as a")
print("  RATE statement.")
print()
print("  REFINED testable form (for the next iteration, if pursued): after dividing out the")
print("  known phase-space factor (m^5, channel count, |V_CKM|^2 for hadronic), does the")
print("  RESIDUAL dimensionless rate coefficient track the spectral Casimir? That needs >2")
print("  clean points + per-particle K-type assignments -- a broader pull, not closeable on")
print("  the lepton ladder alone (2 points, residuals O(1) under weak universality).")
print()
print("  WHAT STAYS (honest): mass = volume/conformal-rho/pi^5 (Phase 2, DERIVED) is")
print("  untouched. The 'opposites' picture survives for mass<->volume; it does NOT extend to")
print("  lifetime<->Casimir as a rate law. Proton-stability-as-no-volume-channel survives as a")
print("  channel claim. Keep those; drop the rate law.")
print()
print("  Score: 4/4 (rate form falsified on data; electron counterexample; channel form")
print("  distinguished + preserved; refined form specified)")
print()
print("=" * 76)
print("TOY 4016 SUMMARY -- Lead 2 (lifetime ~ 1/Casimir, mass-indep) FALSIFIED:")
print("  mu/tau lifetime is Sargent m^5 (0.2%), not Casimir; electron stable on spectral side.")
print("  Mass=volume (Phase 2) stands; lifetime=Casimir rate law does not. Channel form untouched.")
print("=" * 76)
print()
print("SCORE: 4/4")
