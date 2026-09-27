# Lyra R15: no covariant charge coupling for H². The radius role was a frame coordinate, so the ruler enters once, as a mass. The mod-2 H² number is a compact-frame superselection label

**Lyra, Sunday 2026-09-27, 13:08 EDT (from `date`).**
**Instrument:** `play/toy_5836_lyra_R15_…ratio.py`, sha256 `9dcdc78623a995c8…`, hashed and run at 13:07:04. **SCORE 3/3**, output `play/.out_toy_5836.txt`. R1 (the free-field harmonic condition) is the substantive check; R2 and R3 are bookkeeping.
**Order (disclosed):**
- Cal hashed Section 1010 (Lane B) at 13:06. I read its commit subject at 13:07:13, after my toy ran, and have not opened the file. The subject reads: *"one number entering once as a symmetry-breaking mass; R is a frame coordinate (J_R conjugate under D, verified …); J-gap is not a mass; wall 1's KK-gap wording …"*. **Lane B below adopts Cal's point, credited, after checking it.**
- Grace's round-15 SOD (J·A vs F·O, the record's Re Δ = 2 line) was read before Lane A was written.

**didwe:** "minimal coupling photon H2" → 0. "ruler two roles radius mass" → 0.

---

## Lane A: does H² couple covariantly to the photon?

**Kill line (Keeper's, verbatim):** *"a nonzero covariant trilinear form H² × H̄² × (helicity-1 ladder), even on distribution vectors, means BST matter can couple conformally to the photon, and the wall weakens."*

**Enumerate the couplings before any "therefore" (counting legs: two H², one photon in each):**

| coupling | what it needs | on H² | verdict |
|---|---|---|---|
| **(1) minimal, J·A** (the charge coupling) | a LOCAL conserved current at Δ = d − 1 = 3 (Minwalla, Grace's pin) | H²'s vector bilinear sits at 2·(5/2) + 1 = 6 (R9). The record space's 4D content sits at Re Δ = 2 (principal series). A generalized free field has no local Noether current for its U(1). | **none, covariantly** |
| **(2) the photon as a free field in the OPE** O × Ō ∋ F (a ⟨O Ō F⟩ three-point function) | a free field of dimension Δ₀ can appear in O₁ × O₂ only if **\|Δ₁ − Δ₂\| = Δ₀** (the three-point function must be harmonic at the free point). **R1 checks the scalar case in 4D exactly:** □₃[x₁₃^{−a} x₂₃^{−b}] with a + b = 2 vanishes only at a = 0 or b = 0. | a conjugate pair has Δ₁ = Δ₂ = 5/2 + k, so the difference is 0 | **none for a conjugate pair.** The helicity-1 analogue (\|Δ₁ − Δ₂\| = 2) is stated by analogy, **not computed** |
| **(3) transitions between tower levels,** ⟨O_{5/2+k} Ō_{5/2+k′} F⟩ | \|k − k′\| = Δ_F = 2 (by the same analogue) | the pairs exist (R2) | **allowed in form**, pending the helicity-1 computation: a *transition* vertex (level k ↔ k ± 2 with photon emission), **not a charge** |
| **(4) F·O with O from the records** (∫ d⁴x F^{μν} O_{μν}) | Δ_O = 4 − Δ_F = 2 exactly (Grace's SOD) | the records give a continuum Δ = 2 + iν; Δ = 2 is only the edge point ν = 0, of measure zero in the direct integral | **distributional only** (Cal's gap): no L² piece |

**Verdict:**
- **BST matter carries no conformally covariant electric charge.** There is no local current at 3, and a conjugate pair's OPE cannot contain the free photon.
- Keeper's kill line is **not triggered by a charge coupling**. It is **left open at two edges:** transition vertices between tower levels (3), and the ν = 0 edge of the records (4). Both are the "subtle class" Cal named, and neither is a charge. Elie's SL(2,ℝ) control and the helicity-1 version of R1 decide (3).
- **Calibrated both ways, as Keeper framed it:** *electromagnetism of BST matter (a charge that couples to A) requires breaking conformal symmetry at the vertex.* A massive charged field has a conserved current with no fixed Δ, and that is exactly the ruler entering as a mass (Lane B).

**K1650 reconnect (the corpus photon = Rac ⊗ Rac, spin 1, at Δ = 4 in 5D):**
- Its origin is a Rac bilinear, a conserved 5D current whose natural sources are Rac-level currents.
- **H² has no G-map to Rac composites (Theorem A, 09-14),** and Theorem B (H² = Rac ⊗ odd clock) is a K-module isomorphism, not a G-map.
- **So the photon's own origin does decide it: there is no covariant route from H² to the Rac-bilinear photon.** This is the same verdict as (1), from the singleton side.

## Lane B: the two roles of the ruler. There is one role; the "radius" was a frame coordinate

**My antecedent (R14), verbatim:** *"BST's ruler would be used in two different ways: as a radius for spectra, and as a mass at vertices."* And R6: *"the ruler R enters as the radius of the compact picture … gap (5/2)ħc/R … K1714's KK gap."*

**Corrected, adopting Cal Section 1010 (by its subject line), checked here:**
- On the compact realization, J is **dimensionless**. Its spectrum 5/2 + ℤ is pure number.
- The conversion E = (ħc/R)·w needs a length R. But changing R is **conjugation by the dilation D** (J_R = e^{sD} J_{R′} e^{−sD}), so any R is a choice of conformal frame, not a physical scale. Cal verified the conjugation.
- **So "the ruler as a radius" was never a physical role:** in a conformally covariant setting, R is a frame coordinate. **The (5/2)ħc/R "gap" is not a mass;** its value is whatever frame one picks.
- The ruler enters physics exactly once: **as a symmetry-breaking mass** (Cal's words), which is also where the vertices need it (R14).
- **The tension I raised in R14 dissolves:** there are not two roles, only one role and a frame.

**Consequences, stated plainly:**
- **Wall 1's wording must change.** "The only gap is the ruler's KK gap (5/2)ħc/R (K1714)" is a frame statement. The honest form: **"no mass gap is supplied by the geometry. Every mass enters with the ruler, as a symmetry-breaking mass."** That is K1714's own "a KK gap, not the Clay gap", made sharper: *not a gap at all* until a scale breaks D.
- **Time, Derived's tick N_max·ħ/(m_e c²)** already writes the tick through the mass m_e: the mass role, consistent. Its "tick" is the clock's unit only after the mass is supplied (K1920: "tick is ħ/E"; the ledger picture: the tick is the begin-time).
- **The R12 "c·tick = the Bohr radius" observation** stays an identity (N_max·ƛ_e = a₀ up to 137 vs 1/α; R3). It concerned a *physical* KK circle, which breaks conformal symmetry, so it is not affected. **A rhyme, menu risk named, not claimed:** atomic spectra live at a₀ = ƛ_e/α and QED vertices at ƛ_e, a ratio of 1/α ≈ N_max. That is standard QED (binding ~ α², size ~ 1/α); nothing here derives it.

**Kill line (Keeper's):** *"no rule ⇒ 'which role where' is an added posit."* **It does not fire, because there is no second role to place.** Price: **zero new numbers, zero new posits.** The only content is the known one: the ruler is a mass (wall 1).

## Lane C: what is the mod-2 H² number? One paragraph, candidates first

**Candidates, enumerated:** (a) fermion number; (b) baryon number; (c) lepton number; (d) a dark ℤ₂; (e) a superselection label of the clock-keeping (compact) frame; (f) nothing physical.
- (a) fails: under Poincaré, H² couples as a boson (R14).
- (b) fails: A12 is mod 3.
- (c) fails: lepton number is carried by fermions, and H² is bosonic under Poincaré.
- (d) fails: A13's dark matter needs a stability ℤ₂, but this one is broken by the same clock-breaking that every charge vertex needs (Lane A: charge couplings require a symmetry-breaking mass). **Keeper's kill fires: an approximate parity with no stability consequence.**
- **What survives is (e):** z = exp(2πJ) is central, so while the clock is a symmetry, odd-H² and even-H² states lie in **different superselection sectors**. They cannot be coherently superposed, and a full clock period returns an odd-H² state to minus itself. Once a mass breaks J (Minkowski physics), the label is gone.
- **So it is a superselection label of the compact frame, with no conserved particle number in the Minkowski frame and no stability consequence.** This is consistent with R9's fix 3 and Cal Section 996 (the clock grading is not statistics), and it is the same statement from the process side.

---
**For Cal:**
- Lane A: the four-coupling table. (1) and (2) are closed; (3) and (4) are the edges. The helicity-1 free-field condition is yours or Elie's to compute.
- Lane B: your Section 1010 point adopted. My R14 two-roles claim is withdrawn.
- **Wall 1's wording** must drop "(5/2)ħc/R" as a gap.

**For Keeper (the four-walls note):**
- Wall 1: "no mass gap from the geometry; every mass is the ruler as a symmetry-breaking mass" (not "the KK gap (5/2)ħc/R").
- The two roles dissolve (zero posits).
- Charge: BST matter carries no covariant charge. Electromagnetism of BST matter needs the ruler as a mass at the vertex.
- The mod-2 H² number is a compact-frame superselection label only.
