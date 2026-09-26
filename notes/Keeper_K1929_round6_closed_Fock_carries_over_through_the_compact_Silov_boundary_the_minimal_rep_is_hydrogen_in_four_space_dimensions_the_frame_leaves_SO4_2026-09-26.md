---
node_type: k_audit
id: K1929
title: "Round 6 closed; round 7 spine. (1) Casey's Fock question: Fock's mechanism DOES carry over, through the Šilov boundary, which is compact ((S⁴×S¹)/ℤ₂ = conformally compactified ℝ^{1,4}). Fock's stereographic S³ is the conformal compactification one dimension down. Discreteness = the compact realization of the boundary (J rotates its S¹); the continuum = the flat realization (P₀ on ℝ^{1,4}). (2) The frame's sl(2,ℝ) has centralizer so(4): SO(5,2) ⊃ SL(2,ℝ) × SO(4) is hydrogen's radial-so(2,1) × angular-rotation structure with four space dimensions. (3) D_IV⁵'s minimal representation (λ = 3/2, the corpus's Wallach seed, Time Derived's E₀) has exactly the level structure of hydrogen in FOUR space dimensions (ground ν = 3/2, degeneracies 1, 5, 14, 30), to be verified. (4) Discrete → continuum as a limit: Stephanov's deconstruction."
date: 2026-09-26
author: Keeper
instrument: play/keeper_K1928_three_times_so52.py (K1929 addition: centralizer of the frame sl(2,ℝ) = so(4), dim 6; ALL PASS)
rubric_cell: "Internal — container yes, mechanism open (boundary = open half); External — A2 FIRED certified (K1928 amendment)"
---

# K1929 — Round 6 closed; Fock carries over through the compact boundary

## Part 1 — Round 6 rulings (inputs: Lyra 5403ce97, 0917f749, 820ef4b7; Elie 5804–5806, 5809; Grace R165 02ac0dde and pins parts 1–4; Cal Section 992)
1. **Ground weight: TWO OBJECTS** (Lyra 5807 7/7; Cal's prereg P1–P3 match).
   - 3/2 is the Rac (minimal representation, Wallach point); 5/2 is H² (Hardy). The link is 5/2 = 3/2 + 1 (Theorem B: H² = Rac ⊗ odd clock).
   - Time, Derived v1.3 mislabels its carrier twice: line 26 puts "E₀ = 3/2 on H²", and line 19 calls H² "Bergman". The second is load-bearing, because Bergman weights are integers and the double cover would die.
   - **Lyra's one-line fixes are correct (Cal concurs). The paper is GO'd, so they wait on CASEY'S WORD.** Keeper recommends GO: the results survive on the correct module, and only the carrier's name changes.
2. **Three times: positions inside a chosen sl(2,ℝ). The choice is a frame, i.e. a coordinate** (Cal Section 992).
   - Clock gapped, spacing exactly 1; P₀ gap ~1/N; D gap ~π/log N (Elie 5806, 6/6). The continuum arrives two different ways.
   - D is G-conjugate to a boost, so calling it "scale" is a reading.
   - H² under SL(2,ℝ) × SO(4) = ⊕ D⁺_{5/2+i+2m} ⊗ (i/2, i/2) (Lyra 5808).
3. **Cayley = a change of realization, not a conjugation** (Lyra; Grace T2632). H² ↔ T2625's H²₊. K1928 corrected.
4. **Holographic operators D_IV⁵ → D_IV⁴:** unique for each k ≤ 4, Gegenbauer parameter μ = λ − 2, so Legendre-type at the Hardy point (Elie 5805; this matches Kobayashi–Pevzner's λ − (n−1)/2, pinned by Grace). The minimal representation splits as H_{3/2} ⊕ H_{5/2} (Jakobsen–Vergne Prop. 3.2, pinned). The tower at 5/2 is covered by Kobayashi 2008 Theorem 8.10 abstractly; no source prints it for 5/2.
5. **Mass gap: the kill line FIRES** (Lyra). Nothing in BST breaks the 4D conformal group to Poincaré × scale. The only gap is the ruler's KK gap (5/2)ħc/R = K1714. **Every Minkowski mass is the ruler times a number.** This is the present state, now stated in representation language. Calibrated both ways: this is not a loss, it is the corpus's existing claim made exact.
6. **Energies (Elie 5804, 10/10):** the sign of E is the conjugacy type of the equation's generator. BST's ladder gives a 1/ν² structure with two named imported inputs (a mass and a coupling). Not K1878's lane. Structure plus imported Coulomb; not a derived energy (Cal).
7. **Szegő:** the kernel exponent is the ground weight 5/2. Data outside the forward cone write nothing into the interior. The 2:1 over real forms is where the double cover lives (±i) (Lyra).
8. **T_bb / A14** (Grace R165; option B):
   - Class fixed before δ was read: PDG's 17 T-states. 12/17 lie within 30 MeV against a null of 6.46 (P = 7×10⁻⁴).
   - The T_bb line is two-sided.
   - The width-scaled test is next (several states are 80–310 MeV wide).
   - **X(6900), pinned here from PDG 2026 listings, not a search summary:** χ_c0(1P) 3415.50 ± 0.19 MeV (S = 1.7) and χ_c1(1P) 3510.67 ± 0.05 give a threshold of **6926.17 MeV**. At 6898 that is **δ ≈ −28 MeV**, inside the 30 MeV window.
   - **But this threshold was named AFTER the offset was known** (Cal flagged it from memory). It does not enter A14's count, and a quarkonium-pair threshold class must be fixed before it is used. The search summary's 3414.71 was PDG-stale: the lesson of 09-25 again.
9. **A2 FIRED on K_μ2, certified** (K1928 amendment, antecedent restated). **16/3: at threshold, final.** **E8: 19 colour-only, falsified.**
10. **Segal:** the spine was tried. His global time is our elliptic clock, and his redshift law is dead (Soneira 1979; Wright 1987). BST states it does not read the elliptic–parabolic difference as a redshift (T2632 row).

## Part 2 — Casey's Fock question, answered in the corpus's terms
Casey asked: could bound states be the interior of D_IV⁵ and the scattering the exterior?

Grace's answer: yes at the level of spectra. Copied literally at the level of curvature, the assignment inverts (bound → compact Q⁵). **Keeper's reading closes the inversion.**
- **Fock's mechanism is conformal compactification.** He maps momentum space ℝ³ stereographically onto S³. Bound states are harmonics on the compact S³, hence discrete, with degeneracy n².
- **D_IV⁵ carries exactly that structure one dimension up, on its Šilov boundary.** (S⁴ × S¹)/ℤ₂ is the conformal compactification of ℝ^{1,4}, a Lorentzian stereographic projection.
- H² is determined by its boundary values there (Szegő).
- **J rotates the S¹**, so its spectrum is discrete (5/2 + k).
- The S⁴ harmonics restricted to SO(4) are the hydrogen shells, cumulatively (K1927(b)).
- **The same boundary in its flat realization ℝ^{1,4} carries P₀ with continuous spectrum.** The difference between the two realizations is the light cone at infinity that the compactification adds.

**So Casey's picture in exact form:**
- **Bound (discrete) = the compact realization of the Šilov boundary.**
- **Continuum = its flat Minkowski realization.**
- The interior is what both realizations reconstruct (Cauchy–Szegő).
- "Exterior" is not needed. T2625 says the region outside the forward cone writes nothing.

This is Segal's cosmos-vs-Minkowski picture, and it inherits his lesson: the compact realization may not be read as a cosmological redshift. **Position or coordinate:** the compactification is a position (it is the Šilov boundary). Which realization an observer uses is a frame, the Machian input.

## Part 3 — Two findings for round 7 (verified or to verify)
**(a) The frame leaves SO(4)** (instrument, ALL PASS).
- The centralizer of the chosen sl(2,ℝ) = span{P₀, K₀, D} in so(5,2) is so(4), the rotations of the four spatial coordinates of ℝ^{1,4}. So **SO(5,2) ⊃ SL(2,ℝ) × SO(4)**.
- In hydrogen, the dynamical SO(4,2) ⊃ SO(2,1)_radial × SO(3)_angular: the radial ladder times the rotations of three-space.
- **D_IV⁵'s frame is the same structure with four space dimensions.**
- The frame is chosen once, which is the Machian input of T2565, and it leaves the rotation group of the descent (compact form; the (3,1) signature is T2545's).

**(b) The minimal representation of SO(5,2) has the level structure of hydrogen in four space dimensions** (to be verified; Nieto, Am. J. Phys. 47 (1979) 1067–1072, is the standard source, text pin owed).
- In d space dimensions the Coulomb levels are E = −Z²/(2ν²) with ν = n_r + l + (d−1)/2. The degeneracy of level N is the dimension of the degree-N harmonics in d+1 variables.
- For **d = 4**: ν = 3/2, 5/2, 7/2, …, with degeneracies 1, 5, 14, 30, ….
- That is exactly the SO(2)-weight ladder 3/2 + m of D_IV⁵'s minimal representation, with K-types the SO(5) harmonics (K1927(b)).
- **So the Wallach seed λ = 3/2 is "4-space hydrogen's ground ν", in the same sense that λ = 1 is 3-space hydrogen's (K1927).** It is structure, not energies: the coupling and the mass are imported, as Elie found.
- This also locates Elie's 1/ν² energies on the right ladder. The Rac carries ν = 3/2 + m; H² (= Rac ⊗ odd clock) carries 5/2 + k.
- **Kill line:** if the d = 4 Coulomb degeneracies or ν-offset differ from the minimal representation's K-types and weights, (b) dies.
- **Menu risk:** "hydrogen in d dimensions" is a family, and any D_IV^n has a d = n − 1 member. What is BST-specific is only that n = 5 was forced (Lyra D_IV⁵ FORCED). The finding is a recapitulation, like K1927, and is to be written as one.

**(c) Discrete → continuum as a limit** (Casey's "processes from the interior into the continuum").
- At boundary radius R the clock spectrum is discrete with spacing ħc/R (Lyra: the KK gap (5/2)ħc/R). As R → ∞ the flat realization's continuum is recovered.
- In 4D the H² tower's summands are conformal fields of dimension Δ = 5/2 + k, with continuous Källén–Lehmann density ∝ (μ²)^{Δ−2}.
- **Stephanov's "deconstruction" of unparticles** (pinned by Grace in R165) is exactly this: a discrete tower whose spacing → 0 becomes a continuous unparticle spectrum.
- **The testable object:** BST's boundary two-point function at finite R (from Szegő, exponent 5/2) should converge, as R → ∞, to the Δ = 5/2 generalized-free-field density in 5D. Its 4D restriction should converge to the sum of Δ = 5/2 + k densities.
- **Kill line:** if the limit is not a generalized free field, BST's boundary processes are not conformal fields, and the "continuum" claim must be restated.
