# Round 130 data pins — Elie, 2026-09-07 (Monday) 09:53 EDT (shell-copied)

Instruments retained as pdftotext dumps in `notes/sources_R130/` (line numbers below refer to those files). Nothing here is from memory.

## 1. Millikan 1916, Phys. Rev. 7, 355–388 — open copy webs.ftmc.uam.es (38 pp., 2.7 MB); second open copy atomfizika.elte.hu
- Einstein's five assertions (file l.72–86): "2. That there is a linear relation between V and ν. 3. That dV/dν or the slope of the V–ν line is numerically equal to h/e. 4. That at the critical frequency ν₀ … the intercept of the V–ν line on the ν axis is the lowest frequency at which the metal in question can be photoelectrically active."
- Kadesch's spark-source linearity (l.270–275): "obtained results which spoke definitely and strongly in favor of a linear relation between the maximum P.D. and ν. The range of wave lengths studied was from 3,900 Å to 2,200 Å."
- Sodium slope and h (l.1184–1191): "no potential departs from the line by more than .01 volt and since the range of volts is about 2 … maximum uncertainty in the slope at about 1 in 200 or 0.5 per cent. The value of this slope in volt-frequencies is 4.124 × 10⁻¹⁵ … inserting my value of e, namely 4.774 × 10⁻¹⁰, there results h = 6.56 × 10⁻²⁷."
- Sodium mean (l.1245–1248): slope = mean of 4.124 and 4.131 = 4.128 × 10⁻¹⁵ → "h = 6.569 × 10⁻²⁷ erg·sec."
- Lithium (l.1360–1363): "h = 6.584 × 10⁻²⁷ erg·sec., the uncertainty here being perhaps as much as 1 per cent. … I place the greater reliance on the value 6.57 obtained from [sodium]."
- Summary (l.1996–2001): "1. Einstein's photoelectric equation has been subjected to very searching tests and it appears in every case to predict exactly the observed results. 2. Planck's h has been photoelectrically determined with a precision of about .5 per cent. and is found to have the value h = 6.57 × 10⁻²⁷."
- Millikan's stance (l.27–30): Einstein's "bold, not to say the reckless, hypothesis of an electro-magnetic light corpuscle of energy hν".
- **What the pin gives the control:** slope h/e independent of the metal (Na 6.569, Li 6.584, 0.5–1 %); intercept metal-dependent (ν₀). Linearity residual ≤ 0.01 V over a 2 V range = 0.5 % of range.

## 2. Huang et al. 2020, Rev. Sci. Instrum. 91, 045116 (arXiv 1909.06286) — modern linearity test, PDF read
- Method (l.43–45, 155–159): gold Fermi-level kinetic energy vs photon energy at three lines, λ = 58.43339 nm (He Iα), 53.70293 nm (He Iβ), 30.37858 nm (He IIα) [NIST ASD wavelengths]; analyzer resolution 2.5 meV.
- Fit (l.246–253): "fitted with a linear function y = ax + b … E_KF = hc/λ − Φ_Ana, the fitted slope a corresponds to hc/e … From the transmission mode data (Fig. 3a), the fitted slope a is 1.23985719 × 10⁻⁴ eV·cm and the obtained Planck constant equals 6.62615138 × 10⁻³⁴ J·s. The fitted work function of the analyzer is 4.3621 eV."
- Result (l.264–267): "The averaged value is 6.62609677 × 10⁻³⁴ J·s with a relative uncertainty of 2 × 10⁻⁵. We can write our measured h as 6.62610(13) × 10⁻³⁴ J·s. Taking the accepted … 6.62607015 × 10⁻³⁴ J·s as a reference, the maximum relative deviation is below 1.6 × 10⁻⁵."
- Per-line Fermi-edge relative uncertainty (l.212–213): 6.5, 13.4, 7.1 × 10⁻⁶.
- **What the pin gives the control:** E_kin(hν) linear with slope = h to 2 × 10⁻⁵ over 21.2–40.8 eV photon energy; any curvature in E(j,k) at the 10⁻⁵ level over a factor-2 range in hν is excluded by this instrument.

## 3. Wigner threshold law — primary: E. P. Wigner, Phys. Rev. 73, 1002 (1948); read here through Andersen et al., arXiv physics/9706013 (Two-electron dynamics in photodetachment; D. J. Pegg is a co-author), eq. (5), file l.810–826
- "Wigner [30] predicted that in the vicinity of a threshold the photodetachment cross section is represented by σ(E) ∼ (E − E₀)^{l+1/2} for E ≥ E₀, 0 for E < E₀, where E − E₀ is the excess energy above threshold and l is the angular momentum of the outgoing electron. This form has been tested experimentally [31: Hotop & Lineberger, J. Phys. Chem. Ref. Data 14, 731 (1985)] and is now well established. The range of validity … is primarily determined by the polarizability of the residual atom [32: O'Malley, Phys. Rev. 137, A1668 (1965)]. … If l = 0 the cross section rises with an infinite slope at the threshold … If l ≥ 1 the slope of the cross section is zero at threshold."
- Positive instrument in the same file: Li⁻ 2²P ks channel (s-wave) fitted to the Wigner form (Fig. 9, l.845–850).
- **Pegg 1987 as cited in the round prompt does not resolve to an H⁻ p-wave paper.** Pegg, Thompson, Compton, Alton, PRL 59, 2267 (1987) is "Evidence for a Stable Negative Ion of Calcium". The H⁻ threshold measurement of record is Lykke, Murray, Lineberger, Phys. Rev. A 43, 6104 (1991), EA(H) = 6082.99 ± 0.15 cm⁻¹ (0.754 eV) — abstract only, PDF paywalled; H⁻(1s²) → H(1s) + e(p) is the l = 1 channel, so its threshold law is E^{3/2}. I quote no number from Lykke's body.
- **Sadeghpour et al. 2000, J. Phys. B 33, R93–R140:** the only open URL (grizzly.colorado.edu) refuses connections; IOP is paywalled; Semantic Scholar lists it CLOSED. Not read; not pinned. The abstract states it reviews "modifications of the Wigner law for scattering by Coulomb, dipolar and dispersion potentials". For the Coulomb case (photoionization of a neutral: σ finite and non-zero at threshold, independent of l) I have no page to cite until a copy is found.

## Comparison shape (held until Lyra's hashed E(j,k) file)
- Einstein control: E(j,k) must be affine in the photon label with a word-independent slope; Millikan bounds slope variation at 0.5–1 % across two metals; Huang bounds nonlinearity at 2 × 10⁻⁵.
- Threshold exponent: an anion-like channel must give l + 1/2 with l the outgoing partial wave; a Coulomb (neutral-atom) channel must give exponent 0.
