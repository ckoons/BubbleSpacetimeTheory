# Grace — Round K4-2, Lane C: pins (E1 rules for Elie's control; the photon's degrees of freedom; prior art on the absorber as a writer; Sargent's rule for Lyra)

**Wednesday 2026-10-07.** Prompt: `notes/Keeper_prompts_team_roundK4-2_the_write_event_electron_circle_to_sphere_record_2026-10-07.md`.
- One researcher did the searching. Grace re-grepped every starred quote in the downloaded texts.
- **Status key:** PRIMARY (the original or a standard reference, opened); SECONDARY (named lecture notes or a data sheet, opened); DERIVED; PIN-OWED.

## 1. E1 selection rules (Elie's control)
- **★ PRIMARY: Martin & Wiese, NIST *Atomic Spectroscopy*, Section 17, "Selection rules for discrete transitions"**, E1 column (physics.nist.gov/Pubs/AtSpec/node17.html).
  - Rigorous rules:
    1. "ΔJ = 0, ±1 (except 0 ↔ 0)"
    2. "ΔM = 0, ±1 (except 0 ↔ 0 when ΔJ = 0)"
    3. "Parity change"
  - With negligible configuration interaction: "4. One electron jumping, with Δl = ±1, Δn arbitrary".
  - LS coupling only: "5. ΔS = 0"; "6. ΔL = 0, ±1 (except 0 ↔ 0)".
  - **Note for the control:** Δl = ±1 is NOT a rigorous rule. It sits under the configuration-interaction heading. The rigorous content is ΔJ, ΔM and parity. A counting framework should reproduce rules 1–3 exactly, and rule 4 only in the one-electron limit.
- **Polarisation ↔ ΔM (SECONDARY):** Steck, "Rubidium 87 D Line Data" rev. 2.3.4: "σ+-polarized light couples mF → m′F = mF + 1, π-polarized light couples mF → m′F = mF, and σ−-polarized light couples mF → m′F = mF − 1".
- Condon & Shortley (1935): PIN-OWED (the archive scan is access-restricted). Bethe–Salpeter, Sakurai and Griffiths: not opened.

## 2. The photon's physical degrees of freedom
- **★ PRIMARY: Wigner, Ann. Math. 40 (1939) 149**, Section 7 (massless case 0₊) and Section 8.
  - "The 'little group' is, in this case, the group of rotations in a plane … These are all one dimensional (e^{isθ})".
  - "for s = ±1 Maxwell's electromagnetic equations".
  - Reflection "'doubles' the number of dimensions of the irreducible representations in which the little group was the two dimensional rotation group", so the representation contains "both s and −s".
- **DERIVED, not quoted:** "no helicity-0 (longitudinal) photon". Each massless irrep is one-dimensional with a fixed s, and Maxwell is s = ±1. Wigner does not say "no longitudinal mode" in those words.
- Weinberg QTF Vol. 1, Sec. 2.5: PIN-OWED.
- **For Keeper's candidate:**
  - The photon's physical data are 3 real (momentum) plus 1 sign (helicity), with the sign ±1 only.
  - Under parity the two helicities are ONE representation, per Wigner Section 8. So the "parity bit" of the candidate is exactly Wigner's doubling. That is a pinned fact for Lyra to use or kill.

## 3. Sargent's rule (for Lyra's K-T3)
- **Original: Sargent, Proc. R. Soc. A 139 (1933) 659, doi:10.1098/rspa.1933.0045. PIN-OWED** (the publisher returned 403).
- **SECONDARY:** Bravar, Geneva lecture "Weak Decays" (PPA2 L8).
  - "Note the E0^5 dependence of the decay width – Sargent's law"
  - Γ ≈ G_F²E₀⁵/(30π³).
  - Muon: "Γ = G_F² m_μ⁵/(192π³) (Sargent's law)".
- Krane, *Introductory Nuclear Physics* (1988), Sec. 9.3: the E₀ dependence sits in the Fermi integral f(Z′, E₀). The fifth power is not written there explicitly.
- Free-neutron Q (CODATA 2022, allascii): (m_n − m_p)c² = 1.293 332 51(38) MeV, minus m_e c² = 0.510 998 950 69(16) MeV, gives **Q = 0.782 333 MeV** (arithmetic; neutrino mass neglected). This matches the K4-0 pin's 0.7823 MeV.

## 4. Prior art: the absorber as the writer of a record

| Source | Status | Verbatim | Closeness |
|---|---|---|---|
| ★ Wheeler & Feynman, RMP 17 (1945) 157 | PRIMARY | "interpret it as a consequence of an interaction between a source and an absorber" (p. 159, on Tetrode) | adjacent: the absorber is necessary, but there is no record language |
| ★ Cramer, RMP 58 (1986) 647, Sec. 3.2 | PRIMARY (author HTML) | "The transaction is a 'handshake' between the emitter and the absorber participants of a quantum event"; the exchange "cyclically repeats until the net exchange of energy and other conserved quantities satisfies the quantum boundary conditions" | **adjacent, the closest structurally:** absorption completes a discrete event fixed by boundary conditions |
| ★ Kastner, arXiv:1204.5227 | PRIMARY | "it is actualized transactions which establish empirical spatiotemporal events"; "spacetime emerges only at the level of actualized transactions" | **adjacent to same:** absorption actualizes; spacetime is built from actualized events. Compare with "D_IV⁵ is the shared ledger" before claiming novelty |
| Zurek, arXiv:0903.5082 | PRIMARY | "the proliferation, in the environment, of multiple records of selected states" | different direction: photons carry records of the system; the absorber is not the writer |
| ★ Wheeler, "Law Without Law" (in Wheeler & Zurek 1983, I.13) | PRIMARY | "No elementary phenomenon is a phenomenon until it is a registered (observed) phenomenon"; "an indelible record, an act of registration" | adjacent: registration happens at a MACROSCOPIC amplifier |
| Bohr, *Atomic Physics and Human Knowledge* (1958), p. 51, p. 88 | PRIMARY | "practically irreversible amplification effects" | adjacent, macroscopic. "Irreversible act of amplification" is Wheeler's wording, not Bohr's |
| ★ Specht et al. (Rempe), Nature 473 (2011) 190, arXiv:1103.1528 | PRIMARY | "mapping arbitrary polarization states of light into and out of a single atom"; "the phase relation between the σ± input polarization modes is mapped to a relative phase between the populations of the aforementioned Zeeman substates"; storage heralded "by means of state detection" | **SAME, experimentally:** one atom's electron writes the photon's polarization into discrete m-substates as a retrievable record. Raman/STIRAP, not plain E1, and no ontology claimed |

**What this means for the write-event claim (C3):**
- "An electron captures a photon's information into discrete states and stores it" is a 2011 laboratory fact (Specht et al.), done by exactly the E1/σ± rules of Section 1.
- The candidate novelty is NOT the capture. It is (i) that the record is written to the BOUNDARY as a K4 word, and (ii) that this is ontology rather than engineering.
- **Specht's line that the σ± phase relation is mapped "to a relative phase between the populations" is direct support for Lyra's Lane E rewrite:** "instruction content = RELATIVE phases between records" is what the experiment stores.
- Still PIN-OWED: Wheeler–Feynman 1949; Wheeler 1978 and 1989/90 ("it from bit"); Han–Kim arXiv:1907.03073 (not opened); Condon–Shortley; Weinberg Sec. 2.5; Sargent 1933.
