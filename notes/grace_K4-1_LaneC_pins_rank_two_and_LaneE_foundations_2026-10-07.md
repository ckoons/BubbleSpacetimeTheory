# Grace — Round K4-1, Lane C: pins (rank two for Elie; Lane E foundations; Dirac 1962's body)

**Wednesday 2026-10-07.** Prompt: `notes/Keeper_prompts_team_roundK4-1_the_closed_sphere_record_the_one_circle_and_two_cleanups_2026-10-07.md`.
- **Status key:** PRIMARY (a standard monograph or the original paper, opened); SECONDARY (an arXiv paper or lecture notes by a named mathematician, opened); DERIVED (an argument, checked by instrument, not pinned); PIN-OWED.
- **Instrument:** toy 5861 (3/3).

## 1. The rank-two sub-geometry (for Elie's Lane B, item 1)

**No monograph was opened.** Wolf 1972, Korányi–Wolf 1965, Helgason Ch. VIII and Mok 1989 Ch. 5 are all PIN-OWED. Everything below is SECONDARY or DERIVED.

| Fact | Status | Source and verbatim |
|---|---|---|
| so(2,2) ≅ sl(2,ℝ) ⊕ sl(2,ℝ) | SECONDARY | Ólafsson–Quiroga-Barranco arXiv:1003.0704, Remark A.2: "The Lie algebra so(2, 2) ≃ sl(2, R) × sl(2, R) is not simple" |
| D_IV² ≅ bidisc Δ² | SECONDARY + instrument | Ghosh–Zwonek arXiv:2406.18396 eq. (2.1): "The Lie ball L2 is biholomorphic to D² by φ(z1, z2) = (z1 + iz2, −z1 + iz2)". **Toy 5861: 20,000/20,000 points agree, both directions.** |
| Q₂ ≅ ℙ¹ × ℙ¹ (≅ S² × S²) | SECONDARY (quadric) + DERIVED (ℂℙ¹ ≅ S²) | A. Kumar, MIT 18.727 Lecture 1 (2008): "The smooth quadric in P³ is the Segre embedding of P¹ × P¹ in P³" |
| Šilov(D_IV²) = T² | SECONDARY (bidisc) + DERIVED/instrument (Lie side) | Pal–Tomar arXiv:2304.05782: "The distinguished boundary of the polydisc D^m is the m-torus T^m". The Lie-sphere side (S¹ × S¹)/ℤ₂ is a torus: Chirvasitu's Lemma 1.2 at n even (his Section 1.1.4 is stated for n ≥ 5, so this use is DERIVED). **Toy 5861: φ maps the Šilov set onto T², with (ω, x) ≡ (−ω, −x).** |
| Polydisc theorem | SECONDARY | Viviani arXiv:1310.3665, Thm 2.31: "there exists a totally geodesic polydisk Δ^r ⊆ D … D = Stab(o) · Δ^r" (citing Mok 1989 Ch. 5) |
| Polysphere theorem (compact dual) | SECONDARY | Viviani, Thm 2.36: "there exists a totally geodesic polysphere (P¹)^r ⊆ X … X = Stab(o) · (P¹)^r"; Kim–Seo arXiv:2202.05471 Thm 2.1 (citing Wolf 72, Mok 86) |
| The polydisc in D_IV^n is the slice L_n ∩ (ℂ² × 0) = L_2 | DERIVED + instrument (n = 3..7) | It is the fixed set of z_j ↦ −z_j (j ≥ 3), an element of K, so it is totally geodesic. Pinned at n = 3 only, and only as a holomorphic retract (Ghosh–Zwonek: "any two dimensional retract M of L3 equals Φ(L2 × {0})"). |
| Its torus lies in Š(D_IV^n) | SECONDARY at n = 3 + DERIVED all n | Ghosh–Zwonek: "Clearly, ∂_S L2 × {0} ⊆ ∂_S L3." In general, 𝕋·S¹ ⊂ 𝕋·S^{n−1}. |

**What this gives Lane B (positions):**
- The compact-dual side carries a totally geodesic (S²)², the polysphere.
- The boundary side carries a T² (the polydisc's torus) inside the non-orientable Š.
- **Both are present in EVERY rank-two domain** (Viviani's polydisc and polysphere theorems hold for every rank). The slice argument is the same for every n.
- **The null therefore comes back POSITIVE on all of D_IV³…D_IV⁷: the sphere and the torus are "allowed, generic", not special to n = 5.**
- What could still be specific to n = 5 is how the torus sits inside Š: Š is non-orientable for odd n, while the polydisc torus is orientable. That is Elie's to compute, not a pin.

## 2. Lane E foundations (researcher; ★ = Grace re-grepped the downloaded text)

- **★ PBR, Nat. Phys. 8 (2012) 475; arXiv:1111.3328v3** (PRIMARY, arXiv version).
  - Abstract: "any model in which a quantum state represents mere information about an underlying physical state of the system, and in which systems that are prepared independently have independent physical states, must make predictions which contradict those of quantum theory."
  - **Preparation independence, Eq. (4):** n independently prepared systems have physical states "distributed according to the product distribution µx1(λ1)µx2(λ2)···µxn(λn)".
  - PBR's own concession: "models where the quantum state is not a physical property can be constructed by dropping our assumption of preparation independence[16]."
  - PBR do not use the words ψ-ontic or ψ-epistemic. They use "physical property" vs "mere information" (after Harrigan–Spekkens): the distributions µ₀ and µ₁ "do not overlap".
- **Emerson–Serbin–Sutherland–Veitch, arXiv:1312.1345** (PRIMARY).
  - "Local Independence": ∫µψ,φ(λ1,λ2,λs)dλs = µψ(λ1)µφ(λ2).
  - "PBR's assumption of independence encodes an assumption of local causality… Under this weaker principle we are able to construct an explicit hidden variable model that is purely statistical and also reproduces the quantum predictions."
- **Leifer, Quanta 3 (2014) 67; arXiv:1409.1570** (PRIMARY).
  - Def. 4.11: "An ontological model is ψ-ontic if all pairs of pure quantum states ψ ≠ φ … are ontologically distinct. Otherwise the model is ψ-epistemic."
  - Warning: "a ψ-ontic model is not necessarily ψ-complete".
  - Defs. 7.3–7.4 split preparation independence into a Cartesian Product Assumption (Λ_AB = Λ_A × Λ_B; no "genuinely nonlocal properties") and a No-Correlation Assumption.
- **★ Bell, Physics 1 (1964) 195** (PRIMARY, scan of the journal pages).
  - "The vital assumption [2] is that the result B for particle 2 does not depend on the setting a of the magnet for particle 1, nor A on b."
  - Inequality, Eq. (15): 1 + P(b,c) ≥ |P(a,b) − P(a,c)|. The OCR is garbled; the form was rebuilt from the derivation.
  - The independence of ρ(λ) from the settings is implicit in Eq. (2), not stated.
- **★ Bohm & Hiley, *The Undivided Universe* (1993)** (PRIMARY, archive.org OCR).
  - Section 3.2, p. 35: "a concept that we shall call active information. The basic idea of active information is that a form having very little energy enters into and directs a much greater energy."
  - Section 3.3, p. 39: "the phase, δS, clearly depends only on the form of the field and not on the amplitude… it is this form which 'in-forms' the energy".
  - The 1984 and 1987 papers are PIN-OWED.
- **★ 't Hooft, arXiv:1405.1548** (PRIMARY).
  - p. 45: "An ontological basis is a basis in terms of which the Schrödinger equation sends basis elements into other basis elements".
  - p. 33: "In the ontological basis, this phase ϕ has no physical meaning at all, but as soon as one considers operators… these phases have to be chosen."
  - p. 10, superdeterminism "may not quite be as absurd as it seems".
- **★ Spekkens, PRA 75 (2007) 032110; quant-ph/0401052** (PRIMARY).
  - Knowledge-balance principle: "the amount of knowledge one possesses about the ontic state … must equal the amount of knowledge one lacks."
  - Reproduces: interference, no-cloning, teleportation, and more.
  - Does NOT reproduce: "Contextuality", "Nonlocality (i.e. the existence of a Bell theorem)", "The continuum of quantum states", exponential speed-up.

**Positions for Lane E's definition (ψ = record content vv† + instruction content, the phases vv† forgets):**
- (a) **The closest precedent is Bohm–Hiley's "active information".** It is carried by the phase, depends "only on the form … not on the amplitude", and is "not essentially related to our own knowledge". Our "instruction content" must be compared with it before any novelty claim.
- (b) **'t Hooft takes the opposite position:** phases have "no physical meaning" in the ontic basis. Our definition must say which side it is on.
- (c) **A ψ-ontic claim must name which form of preparation independence it adopts.** The options are PBR's product form, or Leifer's Cartesian-product and no-correlation parts. A boundary ledger shared by all systems ("D_IV⁵ is the shared ledger") is exactly the kind of common, non-factorizing variable that Emerson et al. use to evade PBR. So the shared-ledger picture may **not** automatically be ψ-ontic.
- (d) **Spekkens marks the line our discriminator must cross.** An epistemic toy gets interference but not Bell violations or the continuum. A record-plus-instruction model that only reproduces interference has not separated itself from an epistemic toy.

## 3. Dirac 1962's body: PIN-OWED (closed access)

Tried and failed: royalsocietypublishing PDF and ePDF, Semantic Scholar, OpenAlex, archive.org. The abstract stays pinned (K4-0 note). Everything below is SECONDARY.
- **Trzetrzelewski, arXiv:1103.1674:** "the electron could be modeled by a conducting, elastic membrane of spherical topology".
  - **Whether Dirac ASSUMED or DERIVED the spherical topology is not settled by any source opened.** The secondary sources impose spherical symmetry by hand (x1 = r − ρ). For Lyra's P-closed and P-minimal: closedness enters in Dirac's setup as "splitting R³ into interior and exterior", which is a modelling choice.
  - Hamiltonian, Eq. (1): H = √(−ħ²∂ρ² + ω²ρ⁴) + e²/2ρ.
- **Davidson–Rubin, arXiv:0907.1189, Eqs. 3–4:** E(R) = e²/2R + σR², so R_e = (e²/4σ)^{1/3} and m_e = 3e²/4R_e.
- **Gnädig, Kunszt, Hasenfratz & Kuti, Annals Phys. 116 (1978) 380** (abstract via INSPIRE): "Dirac's extended electron is unstable against quadrupole deformations." No mass value is in the abstract; their excited-state mass is PIN-OWED.
  - Trzetrzelewski's own spectrum is m/m_e ≈ 43.6, 76.3, 103.0, 126.5, "consistent with" GKHK's results (a different technique, his numbers).
  - So the first excitation is ≈ 44–53 m_e on every quantization, against a measured 206.768.
- **New fact for the lane: Dirac's sphere is UNSTABLE against quadrupole deformations** (GKHK). A closed-sphere record built on Dirac inherits that instability unless something else stabilizes it.
