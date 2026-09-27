# Lyra R11: where is 4D's λ = 1? Only KK supplies it, from the Rac. The zero-mode rule is Δ₄ = Δ₅ − ½. BST supplies neither the compact circle nor its radius, so the fourth wall fires in its conditional form

**Lyra, Sunday 2026-09-27, 09:43 EDT (from `date`).**
- **Blindness:** Cal hashed Section 1001 at 09:40 (d37778f8). I have not opened the file. **My toy was hashed at 09:40:45**, before I read Cal's commit subject at 09:41:00, which says "restriction to embedded SO(4,2) cannot contain any 4D massless rep (J ≥ 3/2 shared; helicity check owed); KK ev…". This note was written after I saw that subject.
- **didwe:** "Kaluza-Klein zero mode" → 0. "compact normal direction" → 0 relevant hits. "F64 internal volume" → K255 (CONDITIONAL; ℓ_B not pinned). "ladder representation massless" → 0. "non-unitary weight ghost" → 0.
- **Instrument:** `play/toy_5828_lyra_R11_…ghosts.py`. **Run 1** (sha 85d0de73) crashed on a generator loop-order bug before K4 printed; K1–K3 held. **Run 2** (sha 65b4d182, hashed before running): **SCORE 4/4**, output `play/.out_toy_5828.txt`.
- **Time, Derived:** done first, on Casey's GO, as **v1.4 (6ccc2d69).** v1.3 is read-only and hash-verified (K1670), so it stays the GO record. Eight lines differ: the six fix sentences plus the date and status. Line 60's "ground E₀ = 3/2 (Section 2)" needed "on the Rac, 5/2 on H²" to stay consistent with fix 2; **@Cal, that line is outside the three named fixes, so please gate it too.** The PDF is built. Its missing-glyph warnings (⊄, ⟺) are for characters already present in v1.3.

**Kill line (Keeper's, restated verbatim):** *"if no route supplies λ = 1 without importing it, the descent carries no massless 4D particle and Gauss's law is imported."*

**Invariants, quoted first:**
- A 4D massless representation is a ladder at Δ = j + 1: scalar 1, helicity ½ at 3/2, helicity 1 at 2 (Mack 1977; the theorem pin is Grace's).
- The Wallach norms of H_λ(D_IV^n) on the Schmid K-type (m₁, m₂) are (λ)_{m₁}·(λ − (n−2)/2)_{m₂}.
- The generic norm is h(z,w) = 1 − 2z·w̄ + (z·z)(w̄·w̄).

---

## Item 1: the routes, enumerated before any "therefore"

**(a) Kaluza–Klein zero mode. It supplies λ = 1, from the Rac, and only if the normal direction is compact.**
- **The exponent rule (K1):** on ℝ^{1,3} × S¹_R, a 5D field of dimension Δ₅ has a zero mode whose correlator is Σ_n (x² + (2πRn)²)^{−Δ₅}. It falls as x^{1−2Δ₅} for x ≫ R and as x^{−2Δ₅} for x ≪ R. **So Δ₄ = Δ₅ − ½ (the Källén–Lehmann exponent is preserved).** Checked: the Rac gives −2 and −3, and H² gives −4 and −5. Control, 4D → 3D: Δ = 1 → ½.
- **The two singletons land exactly on 4D's massless ladders:**
  - **Rac (3/2) → Δ₄ = 1: λ = 1, the scalar ladder.**
  - **Di (2) → Δ₄ = 3/2: the helicity-½ ladder.** The Weyl content is Cal's "helicity check owed": a 5D Dirac spinor gives a 4D Dirac pair.
- **H² (5/2) → Δ₄ = 2: a generalized free field.** It is a continuum (flat 4D density ∝ (μ²)⁰), **not a particle.** Keeper's expectation holds, with the value fixed at Δ₄ = 2.
- **The tower:** masses n/R, the ruler's KK gap (K1714).
- **The photon itself (helicity 1, Δ = 2) is not a singleton zero mode.** The 5D singletons are only the Rac and the Di. What (a) supplies are its *sources*: zero-mode bilinears at 2 + s, which are conserved (K2).
- **Does BST force the compact normal? No, and three corpus facts say why.** They were enumerated before concluding:
  - (i) The Šilov compact realization compactifies all of space as S⁴ at one conformal radius. The normal to an equatorial S³ in S⁴ is the **polar interval θ ∈ [0, π] with warp sin²θ, not a product circle.**
  - (ii) **F64** (06-07) did a KK reduction *inside the domain* (6 of 10 real directions integrated out, "internal volume = π^{n_C}"). The reduction integral was never computed, and ℓ_B was never pinned (Grace R170: ℓ_B is the ruler, an input). That is a different KK from a compact boundary normal.
  - (iii) **T2565:** the descent's selection is Machian.
- **And the radius cannot come from BST.** BST has one length. The zero mode is 4D only at distances x ≫ R (K1: below R the correlator is 5D, so Coulomb would go as 1/r³). A 4D Coulomb law at laboratory distances needs R below every tested distance, which puts the tower at masses ≥ ħc/R. **Two external bounds pinch R:** inverse-square tests of Coulomb's law from above, and KK-photon / universal-extra-dimension searches from below. Both pins are owed to Grace; I have not used a number from memory.
- **Position:** Δ₄ = Δ₅ − ½; Rac → λ = 1 and Di → the helicity-½ ladder, given a compact normal. **Coordinate:** which direction is normal (T2565). **Import:** a product circle, and its radius.

**(b) Boundary-value restriction. It dies: the exponent is inherited.** The generic norm restricts exactly: h₅(z,w) at z₅ = w₅ = 0 equals h₄(z,w) (K3, symbolic). So the kernel h^{−λ} on the sub-Šilov (S³ × S¹)/ℤ₂ is H_λ(D_IV⁴)'s kernel **with the same λ.** Szegő data give 5/2 → 5/2 (not D_IV⁴'s Hardy exponent 2), and the Rac gives 3/2 → 3/2. The result is the holomorphic restriction's k = 0 piece, as K1927 found; the k ≥ 1 pieces sit higher. **Never λ = 1. Position.**

**(c) A non-unitary 5D weight. It is a ghost, as expected.** At λ = 1 on D_IV⁵ the norms are (1)_{m₁}(−½)_{m₂}: **negative for every m₂ ≥ 1** (K4). Every q^b direction has negative norm. Its D_IV⁴ counterpart H₁(D_IV⁴) has (1)_{m₁}(0)_{m₂}: the q-tower is **null**, and the quotient is exactly the unitary ladder. So the 5D module whose 4D k = 0 shadow *is* the λ = 1 ladder exists only with negative-norm states. BST has no reason to populate a weight outside its Wallach set. **Import (a ghost). Position.**

**(d) Compact dual / K-type recapitulation: structure only.** The n² shells are K-types (K1927). The compact dual Q⁵ carries only finite-dimensional representations (holomorphic sections of O(k)), while λ = 1 is an infinite-dimensional unitary module of the non-compact group. **No. Position.**

**(e) Records: likely no.** H² ⊗ H̄² is continuous (Ørsted–Zhang, with Grace's caveats) and of L²/tempered type. λ = 1 is the **minimal**, non-tempered representation of SO(4,2). A discrete non-tempered summand in the restriction of an L²-type representation would be unusual. **Pin owed** (Kobayashi's restriction theory), so this is direction only.

**Verdict (kill line, as written): it fires in its conditional form.**
- **λ = 1 enters 4D only by route (a): the KK zero mode of the Rac on a compact normal circle whose radius sits below every laboratory distance.** BST forces neither the circle (its compact normal is a warped interval) nor the radius (one length only).
- **So: no massless 4D particle from the descent without an imported compact direction and an imported scale.** That is the fourth wall, stated at its true strength.
- **Calibrated the other way,** and this is new: **if** the normal is compact, BST's geometry places the 4D massless content exactly. The Rac gives the scalar ladder λ = 1, the Di gives the helicity-½ ladder, H² gives only a Δ = 2 continuum, and the conserved 4D currents are Rac zero-mode bilinears. **That placement is zero-knob. What is imported is only the circle and its size.**
- The photon *field* (helicity 1) needs a 5D spin-1 field, which no singleton is.

## Item 2: does a compact normal also give the 4D stress tensor? Yes. And the third wall then covers 4D exactly

- The zero-mode bilinears of the Rac sit at 2·1 + s = 2 + s: **conserved 4D currents at every spin, and a 4D stress tensor at s = 2** (K2). H²'s zero-mode bilinears sit at 4 + s: none.
- The KK zero-mode sector is a **free** massless 4D theory. It keeps every higher-spin current, so by Maldacena–Zhiboedov / Alba–Diab it is free, plus a massive tower that is also free.
- **So under route (a) the third wall transfers to 4D exactly:** the kinematics (the massless ladders, their currents, T) are placed, and no dynamics is supplied. R10's "4D has no T" becomes "4D has T if and only if the normal is compact, and then it is free".

**Reconnects:**
- **K1714:** the boundary gap is a KK gap. Here it is the tower n/R.
- **F64:** an interior KK, a different object; its reduction integral and ℓ_B are still owed.
- **T2565:** the normal direction is Machian.
- **R7:** Gauss's law is the exponent Δ₄ = 1. Under (a) it is Δ₅ − ½ of the Rac: **4D Gauss's law is 5D Gauss's law integrated over a compact normal**, which is the textbook KK statement, now tied to BST's singleton.

---
**For Cal:**
- (a) The exponent rule, and the singletons landing on the ladders. I say compactness is not forced (warped interval, F64 interior, T2565) and the radius is imported. Helicity is yours.
- (b) Dies. (c) Ghost. (d) No. (e) Pin owed.
- Line 60 of Time, Derived v1.4.

**For Grace:**
- Coulomb inverse-square bounds and KK-photon / UED mass bounds, from numbered statements. These bound the one radius route (a) needs.
- Kobayashi on restricting L²-type representations (for route e).

**For Keeper:** the fourth wall, conditional form, one sentence: *"λ = 1 (and with it Gauss's law, the 4D currents and T) enters only as the KK zero mode of the Rac on a compact normal circle that BST does not supply, at a radius BST cannot set."*
