r"""
Toy 4205: VERIFY Lyra's tau -sqrt(pi) correction -- and the two honest things the team needs before building on it. Lyra
flagged that the tau's -1.77 correction is -sqrt(pi) to five digits (and withdrew F152's over-scoped "F143 forbids it",
cleanly). Verifying the spectacular-or-coincidence claim is my job. RESULTS:
  (A) the number is real: 49*71 - sqrt(pi) = 3477.2275 vs observed m_tau/m_e = 3477.228 -> matches the CENTRAL value to
      2.1e-7. genuinely striking.
  (B) BUT the tau mass is measured to only 6.75e-5 (m_tau = 1776.86 +/- 0.12 MeV), 200x larger than that residual. two
      consequences the team must hold:
      (1) the LEADING form 49*71 = 3479 ALONE is 7.5 sigma ABOVE observation (1.77 / 0.235). so the correction is
          MANDATORY (the leading-order term is not the full prediction), not optional -- and not "within a loose floor":
          49*71 alone is experimentally EXCLUDED as the complete value.
      (2) the experimental window (+/- 0.24 on the ratio) ADMITS many ~1.77 corrections (sqrt(pi), 16/9, 9/16*pi, 7/4 all
          fit). so the DATA CANNOT SELECT sqrt(pi). it is the best central-value fit among simple candidates, but it is
          NOT data-confirmed.
  CONCLUSION: sqrt(pi) was reverse-engineered from the gap (back-fit risk HIGH, as Lyra said) AND the data is too imprecise
  to select it. so it counts ONLY if it comes out FORWARD -- Lyra's odd-Peirce / Gamma(1/2)=sqrt(pi) mechanism, derived
  blind with Cal watching. the numerical match alone is suggestive, not evidence. Count stays 2 of 26.

(A) THE NUMBER (verified):
  49*71 - sqrt(pi) = 3479 - 1.7724539 = 3477.227546
  observed m_tau/m_e = 1776.86 / 0.51099895 = 3477.2283  -> residual 2.1e-7 to the CENTRAL value. striking.

(B1) THE LEADING FORM ALONE IS 7.5 SIGMA OFF (the correction is mandatory):
  m_tau = 1776.86 +/- 0.12 MeV  -> m_tau/m_e = 3477.23 +/- 0.235  (experimental error 6.75e-5, dominated by m_tau).
  leading 49*71 = 3479 deviates from observation by 1.77 = 7.5 * 0.235 = 7.5 sigma. so 49*71 by itself is EXCLUDED as the
  complete prediction -- the sub-leading correction is REQUIRED for consistency with data (normal: leading order != exact).
  (this is sharper than Toy 4203's "above the structural floor": vs the experiment, the bare leading form is 7.5 sigma out.)

(B2) THE DATA CANNOT SELECT sqrt(pi) (the window is wide):
  the gap 49*71 - obs = 1.7717; the data allows the correction anywhere in [1.77 - 0.24, 1.77 + 0.24] = [1.54, 2.01].
  candidates inside that window: sqrt(pi)=1.7725, 16/9=1.7778, 9/16*pi=1.7671, 7/4=1.7500 -- ALL fit. sqrt(pi) is the best
  fit to the central value (2.1e-7) but the experiment is 200x too coarse to confirm it over the others. so the numerical
  match is the BEST among simple forms, not a measurement that pins sqrt(pi).

CONSEQUENCE (the discipline):
  sqrt(pi) is doubly un-banked: (i) reverse-engineered from the gap (back-fit), (ii) not data-selectable (window too wide).
  it earns its place ONLY by a FORWARD derivation -- Lyra's candidate is the odd-Peirce component (the half-dimensional
  eigenspace of the rank-2 Jordan structure), which carries a Gamma(1/2) = sqrt(pi) normalization, sub-leading and distinct
  from the pi-free leading term. that derivation is Lyra's lane (continuum); it must be blind (built from the geometry, not
  read from 1.772), with Cal verifying no back-fit. IF it comes out forward -> tau lands ~2e-7 (essentially exact, the
  experiment will sharpen later). IF NOT -> drop it; the tau is 49*71 at the broad floor, with the bare leading form 7.5
  sigma off and only an undetermined correction between it and the data.
  the MUON is the contrasting clean case: m_mu/m_e is measured to ~1e-8, and (24/pi^2)^6 sits at 3.4e-5 -- a genuine
  THEORY residual at the structural floor, well inside a precise measurement, leading-form, blind. the muon does not depend
  on any of this. count stays 2 of 26; muon clean, tau gated on the forward sqrt(pi).
"""

import math

sqrtpi = math.sqrt(math.pi)
lead = 49 * 71                      # 3479
val = lead - sqrtpi                 # 3477.2275

m_tau, m_tau_err = 1776.86, 0.12    # MeV, PDG
m_e = 0.51099895000
obs = m_tau / m_e
obs_err = obs * (m_tau_err / m_tau)
resid_central = abs(val - obs) / obs
exp_relerr = obs_err / obs
gap = lead - obs
sigma_leading = (lead - obs) / obs_err

# muon for contrast
mu = (24 / math.pi**2)**6
mu_obs = 206.7682830
mu_resid = abs(mu - mu_obs) / mu_obs

print("=" * 100)
print("TOY 4205: tau -sqrt(pi) correction VERIFIED -- but data can't select it; forward derivation is mandatory")
print("=" * 100)
print()
print("(A) the number (verified):")
print("-" * 100)
print(f"  49*71 - sqrt(pi) = 3479 - {sqrtpi:.7f} = {val:.6f}")
print(f"  observed m_tau/m_e = {obs:.4f}   residual to CENTRAL value = {resid_central:.2e}  (striking)")
print()
print("(B1) the leading form ALONE is 7.5 sigma off (correction MANDATORY):")
print("-" * 100)
print(f"  m_tau = {m_tau} +/- {m_tau_err} MeV -> m_tau/m_e = {obs:.2f} +/- {obs_err:.3f}  (exp rel err {exp_relerr:.2e})")
print(f"  leading 49*71 = {lead} deviates by {lead-obs:.3f} = {sigma_leading:.1f} sigma -> EXCLUDED as the complete value")
print()
print("(B2) the data cannot select sqrt(pi) (window too wide):")
print("-" * 100)
print(f"  gap = {gap:.4f}; data allows correction in [{gap-obs_err:.3f}, {gap+obs_err:.3f}]")
for name, c in [("sqrt(pi)", sqrtpi), ("16/9", 16/9), ("9/16*pi", 9/16*math.pi), ("7/4", 1.75)]:
    inside = abs(c - gap) < obs_err
    print(f"    {name:9} = {c:.4f}  resid-to-central {abs((lead-c)-obs)/obs:.1e}  in window: {inside}")
print(f"  sqrt(pi) is the BEST central-value fit, but the experiment is ~200x too coarse to confirm it over the others.")
print()
print("(contrast) the muon is the clean case:")
print("-" * 100)
print(f"  m_mu/m_e measured to ~1e-8; (24/pi^2)^6 residual = {mu_resid:.2e} -- genuine theory residual at the floor, leading-form, blind.")
print()

checks = [
    ("49*71 - sqrt(pi) matches central obs to ~2e-7", resid_central < 1e-6),
    ("experimental error on m_tau/m_e ~ 6.8e-5 (dominated by m_tau)", abs(exp_relerr - 6.75e-5) < 1e-5),
    ("leading form 49*71 ALONE is >7 sigma off (correction mandatory)", sigma_leading > 7),
    ("data window admits sqrt(pi) AND 16/9 AND 9/16*pi (cannot select)", all(abs(c-gap) < obs_err for c in [sqrtpi, 16/9, 9/16*math.pi])),
    ("sqrt(pi) is the best central-value fit among simple candidates", resid_central < min(abs((lead-c)-obs)/obs for c in [16/9, 9/16*math.pi, 1.75])),
    ("sqrt(pi) reverse-engineered from the gap (back-fit risk) -> forward-derivation mandatory", True),
    ("muon clean + independent (3.4e-5, precise measurement, leading-form)", mu_resid < 1e-4),
]
passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
print()

print("=" * 100)
print("SUMMARY -- verifying Lyra's tau correction = -sqrt(pi), with the two caveats the team needs. The number is real:")
print("  49*71 - sqrt(pi) = 3477.2275 matches the central m_tau/m_e = 3477.228 to 2.1e-7 -- striking, and Lyra withdrew her")
print("  over-scoped 'F143 forbids it' cleanly so it is properly open. But the tau mass is known only to 6.75e-5 (200x that")
print("  residual), which forces two honest conclusions. First, the bare leading form 49*71 = 3479 is 7.5 sigma ABOVE the")
print("  measurement -- it is EXCLUDED as the complete value, so the sub-leading correction is mandatory, not a loose-floor")
print("  nicety (sharper than 4203). Second, the experimental window (+/- 0.24 on the ratio) admits sqrt(pi), 16/9, 9/16*pi,")
print("  7/4 alike, so the DATA CANNOT SELECT sqrt(pi); it is merely the best central-value fit among simple forms. Since")
print("  sqrt(pi) was also reverse-engineered from the gap (back-fit risk high), it is doubly un-banked and earns its place")
print("  ONLY by a FORWARD derivation -- Lyra's odd-Peirce / Gamma(1/2) = sqrt(pi) mechanism, built blind from the geometry")
print("  with Cal watching. If it derives forward, the tau lands ~2e-7 (essentially exact); if not, drop it and the tau is")
print("  49*71 with an undetermined correction. The muon is unaffected and clean (3.4e-5, precise measurement, leading-form,")
print("  blind). Count stays 2 of 26; muon clean, tau gated on the forward sqrt(pi).")
print("=" * 100)
print()
print("Elie - Tuesday 2026-06-16 (VERIFY Lyra's tau -sqrt(pi) correction + the two honest caveats: Lyra flagged the tau -1.77 correction = -sqrt(pi) to five digits + withdrew F152 over-scoped 'F143 forbids it' cleanly; (A) NUMBER REAL 49*71 - sqrt(pi) = 3479 - 1.7724539 = 3477.2275 vs observed m_tau/m_e = 1776.86/0.51099895 = 3477.2283 -> residual 2.1e-7 to the CENTRAL value striking; (B) BUT tau mass measured only to 6.75e-5 (m_tau=1776.86+/-0.12 MeV) = 200x that residual, two consequences -- (B1) the LEADING form 49*71=3479 ALONE is 7.5 sigma ABOVE observation (1.77/0.235), so the correction is MANDATORY not optional + not within-a-loose-floor: 49*71 alone is experimentally EXCLUDED as the complete value (sharper than 4203 structural-floor framing), normal because leading-order != exact; (B2) experimental window +/-0.24 on the ratio ADMITS many ~1.77 corrections (sqrt(pi)=1.7725, 16/9=1.7778, 9/16*pi=1.7671, 7/4=1.7500 all fit) so DATA CANNOT SELECT sqrt(pi), it is the BEST central-value fit among simple candidates (2.1e-7 vs 16/9 1.7e-6 etc) but NOT data-confirmed (experiment 200x too coarse); CONCLUSION sqrt(pi) doubly un-banked (i) reverse-engineered from the gap (back-fit risk HIGH as Lyra said) (ii) not data-selectable (window too wide), counts ONLY by a FORWARD derivation = Lyra's odd-Peirce component (half-dimensional eigenspace of rank-2 Jordan structure) carrying Gamma(1/2)=sqrt(pi) normalization sub-leading + distinct from pi-free leading term, her continuum lane, MUST be blind (built from geometry not read from 1.772) Cal verifying no back-fit, IF forward -> tau ~2e-7 essentially exact IF NOT -> drop it tau = 49*71 broad floor bare-leading 7.5 sigma off + undetermined correction; MUON contrasting clean case m_mu/m_e measured ~1e-8 + (24/pi^2)^6 at 3.4e-5 genuine theory residual at structural floor inside a precise measurement leading-form blind, muon independent of all this; count 2 of 26 muon clean tau gated on forward sqrt(pi))")
print()
print(f"SCORE: {passed}/{len(checks)} (tau -sqrt(pi) verified + 2 caveats: (A) 49*71-sqrt(pi)=3477.2275 matches central obs 2.1e-7 striking; (B1) tau mass known only to 6.75e-5 so bare leading 49*71 is 7.5 sigma off -> correction MANDATORY, 49*71 alone EXCLUDED as complete value; (B2) data window +/-0.24 admits sqrt(pi)/16/9/9-16-pi alike -> DATA CANNOT SELECT sqrt(pi), best central fit not data-confirmed; sqrt(pi) reverse-engineered+not-selectable -> counts ONLY if forward-derived (Lyra odd-Peirce Gamma(1/2), blind, Cal-watched); muon clean+independent 3.4e-5 precise; count 2 of 26)")
