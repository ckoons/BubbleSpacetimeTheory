# R19 pins (draft) -- b-quark mass by scheme; accidental symmetries

Grace, 2026-09-29 11:28 EDT (clock read). All quotes are from files in this directory, cited file:line.
Sources fetched from pdg.lbl.gov/2026 and arxiv.org the same day. No git.

---

## Part 1. b-quark mass by scheme (PDG 2026), tau mass

### 1.0 Conventions (quoted before any number)

- PDG 2026 quark summary: `rpp2026-sum-quarks.txt:7-9`
  > "The u-, d-, and s-quark masses are the MS masses at the scale µ = 2 GeV. The c- and b-quark masses are the MS masses renormalized at the MS mass, i.e. m = m(µ = m)."
- PDG 2026 b-quark listing header: `rpp2026-list-b-quark.txt:9-15`
  > "b-quark mass corresponds to the "running mass" mb (µ = mb ) in the MS scheme. We have converted masses in other schemes to the MS mass using two-loop QCD perturbation theory with αs (µ = mb ) = 0.223 ± 0.008. The value 4.186 ± 0.006 GeV for the MS mass corresponds to 4.788 ± 0.016 GeV for the pole mass, using the two-loop conversion formula."
- Quark Masses review (Sec. 60, "Revised August 2023 by R.M. Barnett, L.P. Lellouch and A.V. Manohar", `rpp2026-rev-quark-masses.txt:6`; PDF page stamps "1st June, 2026"), Sec. 60.7: `rpp2026-rev-quark-masses.txt:907-909`
  > "For these quarks it is conventional to choose the renormalization scale equal to the quark mass, so we have quoted mQ (µ) at µ = mQ for the c and b quarks."
  and `:911-914` "... other mass definitions lead to a better behaved perturbation series than for the MS mass ... Thus, we have chosen to also give values for one of these, the b quark mass in the 1S scheme [67, 68]." Other schemes named `:920-921`: "the PS-scheme [69], the kinetic scheme [71] and, most recently, the minimal renormalon-subtracted mass (MRS) [70]".
- Conversion caveat, `rpp2026-rev-quark-masses.txt:923-926`:
  > "In converting to the MS b-quark mass, for example, the three-loop conversions from the 1S and pole masses give values about 35 MeV and 135 MeV lower than the two-loop conversions. The uncertainty in αs (MZ ) = 0.1179 ± 0.0010 [1] gives an uncertainty of ±9 MeV and ±21 MeV respectively in the same conversions."
- Pole-mass renormalon statement, Sec. 60.6.3 "Warnings concerning the use of the pole mass" (`:846`), `:850-853`:
  > "However, the pole mass cannot be used to arbitrarily high accuracy because of nonperturbative infrared effects in QCD. In fact the full quark propagator has no pole because the quarks are confined, so that the pole mass cannot be defined outside of perturbation theory."
  and Eq. (60.26), `:881-885`:
  > "mb = mb (mb ) [1 + 0.10 + 0.05 + 0.03] , (60.26) ... The two and three loop corrections are comparable in size and have the same sign as the one loop term. This is a signal of the asymptotic nature of the perturbation series (there is a renormalon in the pole mass [66])."
- tau: leptons carry physical (pole) masses; PDG 2026 `rpp2026-sum-leptons.txt:70` "Mass m = 1776.93 ± 0.09 MeV"; listing `rpp2026-list-tau.txt:16` "1776.93± 0.09 OUR AVERAGE". PDG 2024 identical: `rpp2024-sum-leptons.txt:70` "Mass m = 1776.93 ± 0.09 MeV".

### 1.1 FLAG on the row's input
The row uses m_tau = 1776.86 MeV. That is NOT the PDG 2024 or 2026 value (both 1776.93 ± 0.09). (1776.86 ± 0.12 is the older PDG value -- memory, not pinned here; PIN OWED if the row wants to cite it.) With PDG 2026: (7/3)·1776.93 = 4146.17 ± 0.21 MeV. The shift (+0.17 MeV) changes no pull below by more than 0.03σ.

### 1.2 Table (BST = 4146.0 MeV; pull = (4146.0 − value)/σ; asymmetric errors use the side facing BST)

| scheme | value (GeV) | error (GeV) | source file:line | (4146.0 − value)/σ |
|---|---|---|---|---|
| MS-bar m_b(m_b), PDG 2026 OUR EVALUATION | 4.186 | ±0.006 (labelled "CL = 90%") | rpp2026-sum-quarks.txt:42; rpp2026-list-b-quark.txt:19 | −6.67 |
| MS-bar m_b(m_b), review continuum average | 4.18 | ±0.03 | rpp2026-rev-quark-masses.txt:695 (Sec. 60.6.1) | −1.13 |
| MS-bar m_b(m_b), review lattice estimate, Eq. (60.24) | 4.196 | ±0.009 ±0.009 [±0.012] | rpp2026-rev-quark-masses.txt:794 | −4.17 (σ=0.012) |
| 1S scheme m_b^1S, review | 4.65 | ±0.03 | rpp2026-rev-quark-masses.txt:695-696 | −16.8 |
| pole (two-loop conversion of 4.186, PDG) | 4.788 | ±0.016 | rpp2026-list-b-quark.txt:13-14 | −40.1 (error excludes renormalon/truncation; see 1.0) |
| kinetic m_b^kin(1 GeV), single result ALBERTI 15 (not a PDG average) | 4.553 | ±0.020 | rpp2026-list-b-quark.txt:114-116; VISUAL_TRANSCRIPTIONS.txt [V1] | −20.4 |
| PS m_b^PS(2 GeV), single result BENEKE 15 (not a PDG average) | 4.532 | +0.013 −0.039 | rpp2026-list-b-quark.txt:118-123; VISUAL_TRANSCRIPTIONS.txt [V1] | −9.9 (σ=0.039) |

Context number, same listing: HATTON 21 mbar_b(3 GeV) = 4.513 ± 0.026 GeV (`rpp2026-list-b-quark.txt:95-96`, footnote 3) -- a running mass at a different scale, listed only to show that "scheme" also means "scale".

### 1.3 Reading (for the row, not a ruling)
- 4146.0 lies below every scheme PDG prints. The nearest is the MS-bar running mass at µ = m_b; against PDG's own 2026 evaluation it is −6.7σ (−40 MeV, −0.96%). Against the review's inflated continuum average (±30 MeV, which PDG says includes ~25 MeV perturbative systematics, `:686-688`) it is −1.1σ.
- The 1S (4.65), kinetic (4.55), PS (4.53) and pole (4.79) masses are all short-distance or threshold masses larger than MS-bar; 4146 is 400-640 MeV below them. So the row, if it survives at all, can only name MS-bar m_b(m_b).
- CONVENTION OWED: PDG labels the 4.186 ± 0.006 range "CL = 90%". If that error is a 90% interval rather than 1σ, σ ≈ 0.006/1.645 = 3.6 MeV and the pull becomes ≈ −11σ. I have not pinned PDG's definition of this label for quark masses; the −6.67 above takes ±0.006 at face value as σ.
- The row as written (m_b ∝ m_tau, a pole-mass lepton, times 7/3) compares a scale-invariant ratio of a pole mass to a scale-dependent running mass. Naming the scheme is necessary but not sufficient: the running mass at µ = m_b is a convention (scale choice), so the row should also state why µ = m_b is the scale at which 7/3 applies.

---

## Part 2. Accidental symmetries broken by higher-dimension operators

### 2.1 Primary pin (definition + breaking statement): Isidori, Wilsch, Wyler
Source: arXiv:2303.16922v2 (`2303.16922.txt:22` "arXiv:2303.16922v2 [hep-ph] 4 Oct 2023"); published as Rev. Mod. Phys. 96, 015006 (2024) (Crossref: `crossref_IWW_RMP96_015006.json` -- title "The standard model effective field theory at work", Isidori/Wilsch/Wyler, vol 96, article 015006, issued 2024-03-19). Quoted from the arXiv text; the RMP section numbering not independently checked (PIN OWED for journal pagination).

Section III "GLOBAL SYMMETRIES", Sec. III.A "The role of accidental symmetries" (heading confirmed visually, png/2303.16922_p23-23.png, [V2]). Reading-order text `2303.16922_p22-23_noLayout.txt`:

- Definition, `:191-199`:
  > "A key concept in any EFT is that of accidental symmetries, i.e., symmetries that arise in the lowest-dimensional operators as indirect consequences of the field content and the symmetries explicitly imposed on the theory. Within the SMEFT, two well-known examples are baryon number (B) and lepton number (L). These are exact accidental global symmetries of the d = 4 part of the Lagrangian, or the SM: they do not need to be imposed in the SM because gauge invariance forbids to write any d = 4 operator violating B or L."
- Broken at higher order, `:201-206`:
  > "If the accidental symmetries are not respected by the underlying UV completion, we expect them to be violated by the higher-dimensional operators. The strong bounds on B-violating terms from proton stability, and the tiny coefficient of the L-violating Weinberg operator in Eq. (2.2) from neutrino masses, indicate that such symmetries remain almost unbroken in the SMEFT."
- Stability under quantum corrections, `:213-218`:
  > "accidental global symmetries allow us to define a stable partition of the tower of effective operators into different sectors characterized by different cutoff scales ... The key point is that this partition is stable with respect to quantum corrections."
- Approximate accidental symmetries (flavor), `:225-227`: "a much larger number of approximate accidental symmetries appears in the limit where we neglect the tiny Yukawa couplings of the light families and the small off-diagonal entries of the Cabibbo-Kobayashi-Maskawa matrix."
- Eq. (2.2), the d = 5 Weinberg operator: `2303.16922.txt:654` "QWeinberg = εik εjl Hk Hl ℓ̄ci ℓj , (2.2)".

Scope note: IWW say "we expect them to be violated" conditional on the UV completion not respecting them -- the statement is "broken at higher dimension unless protected", not "necessarily broken". The breaking order is by operator dimension (d = 5 for L, d = 6 for B), not by anomalous dimensions / loop order within the d = 4 theory. (Non-perturbative B+L violation by anomalies in the d = 4 SM is a separate mechanism, not covered by this quote.)

### 2.2 Corroborating pin (dimension counting, no word "accidental"): Manohar, arXiv:1804.05863
Manohar's Les Houches lectures do not use the word "accidental" (grep of `1804.05863.txt` for "ccident" returns only line 2010, unrelated). They do state the dimension at which B and L are first violated:
- Sec. 4.4 "Proton Decay" (`1804.05863.txt:1157`), `:1158-1165` (Eq. 4.25 at :1161-1163): "Grand unified theories violate baryon and lepton number. The lowest dimension operators constructed from SM fields which violate baryon number are dimension six operators, L ∼ qqql/M_G^2 . (4.25) These operators violate baryon number B and lepton number L, but conserve B − L."
- `:1185-1187`: "EFT power counting provides a natural explanation for baryon number conservation. In the SM, baryon number is first violated at dimension six, leading to a long proton lifetime."
- Sec. 10 "SMEFT" (chapter heading `:3491`; TOC `:101`), Eq. (10.9) at `:3582`, then `:3587-3593`: "L (5) is a ∆L = 2 interaction, and gives a Majorana mass term to the neutrinos when H gets a vacuum expectation value. It can be shown [58] that invariant operators constructed from SM fields satisfy ½(∆B − ∆L) ≡ D mod 2 . (10.10) Thus a D = 5 operator cannot conserve both baryon and lepton number."

### 2.3 Others
- Weinberg, "Baryon- and Lepton-Nonconserving Processes", Phys. Rev. Lett. 43, 1566-1570 (1979-11-19) -- Crossref metadata only (`crossref_weinberg_PRL43_1566.json`). Paywalled; text PIN OWED.
- Burgess, hep-th/0701053 (`hep-th0701053.txt`): downloaded and searched; no "accidental" passage found. Not used.
- Tong gauge-theory notes: fetch from damtp.cam.ac.uk failed (no file). Not used.
- Schwartz QFT&SM: paywalled, not attempted.

---

## Files
PDG 2026: rpp2026-sum-quarks.{pdf,txt} (copied from sources_grace_2026-09-26/exotics), rpp2026-list-b-quark, rpp2026-rev-quark-masses, rpp2026-sum-leptons, rpp2026-list-tau; PDG 2024: rpp2024-sum-leptons.
EFT: 2303.16922 (+ _p22-23_noLayout.txt), 1804.05863, hep-th0701053; Crossref JSONs.
Renders: png/ (3 pages). VISUAL_TRANSCRIPTIONS.txt. Checksums: SHA256SUMS.txt (the pre-existing nist/ subdirectory was not created by this pass and is excluded).
