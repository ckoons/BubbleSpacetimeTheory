# Memo for Keeper and Cal — findings from Casey's session of 2026-11-20

**From:** Claude (Opus 5.5, claude.ai session with Casey), at Casey's request.
**For:** Keeper (audit/consistency) and Cal (cold read). Lyra, Elie and Grace copied.
**Status of everything below:** computed in a scratch workspace outside this repo; nothing in the corpus was edited. Scripts and both pre-registrations are in `memo_2026-11-20_scripts/` so every number can be reproduced. Please treat every item as a claim to audit, not a result to absorb.

---

## 1. PRIORITY — the Q⁵ heat-trace spectrum includes non-spherical representations

`notes/BST_SeeleyDeWitt_FiberPacking.md` sums the heat trace over **all** SO(n+2) irreps (p,q,0) with p ≥ q ≥ 0, citing Helgason. The scalar Laplacian on Q^n = SO(n+2)/[SO(n)×SO(2)] sees only the **spherical** irreps. For this pair those are **p ≡ q (mod 2)**: Helgason's theorem imposes a lattice condition, not just two integers. A direct check: (1,0), the 7-dimensional defining representation, has no vector fixed by SO(5)×SO(2), so it cannot appear in the scalar spectrum.

Curvature test (R = 6 a₁/a₀, against the algebraic value 2n²):

| n | all (p,q), as in the corpus | p ≡ q (mod 2) | algebraic 2n² |
|---|---|---|---|
| 3 | 15 | **18** | 18 |
| 4 | 29 | **32** | 32 |
| 5 | 47 | **50** | 50 |
| 6 | 69 | **72** | 72 |

- The "universal R-gap of 3" (Table 3, read there as a Casimir-to-Laplacian shift) is an **artifact** of the extra representations. With the spherical set the gap is 0 for every n.
- The corpus value a₄(Q⁵) = 2671/18 ≈ 148.389 is reproduced exactly by the all-(p,q) sum. With the spherical set, **a₄/a₀ ≈ 204.889** (and a₁/a₀ = 25/3, a₂/a₀ ≈ 34.778, a₃/a₀ ≈ 97.111, a₅/a₀ ≈ 350.995, in the corpus normalisation where the eigenvalues are p(p+5)+q(q+3)).
- So "a₄ ≈ N_c g² = 147, only at n = 5" does not survive in its current form.

**Requested:** a Keeper audit of everything downstream of the FiberPacking coefficients: the R-gap, the a₄ uniqueness claim, R(k) = C(k,2)/κ_Bergman and the Sub-leading Ratio Theorem, and the gravity coefficient read from a₁ (F60/F63). Script: `resonance2.py` and `ak.py`.

## 2. The α running test pinned in K1953 (item 5h) — run, and not a miss by orders of magnitude

K1953 pinned Q\* = m_e and the full one-loop Uehling formula, and Keeper predicted a miss "by orders of magnitude." Using standard QED, electron loop, spacelike momentum transfer:

- At Q = m_e, running lowers α⁻¹ by **0.01924**. The offset to explain is 0.03600.
- α_eff⁻¹(Q) = 137 exactly at **Q\* = 1.4292 m_e**.

That is neither an exact hit nor an orders-of-magnitude miss: running supplies about 53% of the offset at m_e. **Requested:** Elie reruns this formally against Cal's hash, using the hashed convention (spacelike versus timelike, the definition of Q) and tolerance. The ≈ √2 resemblance of 1.43 is noted and deliberately not credited. The K675 reading, n_C/N_max = 5/137 = 0.03650, is 1.38% above the measured 0.03600.

## 3. Boundary heat-kernel correction to G — pre-registered FAIL

Pre-registration `PREREG_boundary_G.md` (SHA-256 `30bcd5bc…5c5d`), written before computing. Model: D_IV⁵ as a region of Q⁵ with Q⁵'s compact Kähler metric (potential log(1+2|z|²+|z·z|²)), so its edge is at finite distance. Einstein–Hilbert-order heat coefficient (Gilkey): (1/6)[∫τ + 2∫L_aa], the same for Dirichlet and Neumann, so there was no knob. PASS window for ρ = 2∫L/∫τ: [5.2, 7.8]×10⁻⁴.

- Validation: Gauss–Bonnet on CP¹ caps reproduces 4π to six digits (it caught a curvature sign error first); det H·F⁵ = 32 constant (Kähler–Einstein).
- **Result: ρ = +1.601 ± 0.002.** Right sign, about 2,500 times too large (implied G shift −62%). FAIL.
- Curiosity, not a claim: ρ is consistent with 8/5. Worth an analytic check as a geometric fact; it has no bearing on G.
- Please log this under fired-and-lost.

## 4. Resonance (discrete-mode) correction at α-ladder steps — pre-registered FAIL

Pre-registration `PREREG_resonance.md` (SHA-256 `42eb7406…0dd9`). C(t) = Z_exact/Z_smooth − 1 on the spherical Q⁵ spectrum.

- C(α) = −2×10⁻¹⁵, and smaller still at α¹² and α²⁴, as predicted: discreteness on a compact symmetric space is exponentially small at short heat time.
- |C| first reaches 3.25×10⁻⁴ at t ≈ 0.199 (≈ α^0.33, not a ladder step), and with positive sign. FAIL.

## 5. Chirality — Cl(4,1) versus Cl(5,2)

- Cl(4,1), the Shilov boundary's signature: γ₅ is proportional to the extra gamma matrix; both chiralities 2+2; no chirality. The 4+1 boundary alone cannot give chirality.
- Cl(5,2): ω central, ω² = −1. Within an irreducible representation, γ₅ is locked to ω_int; only (L,+)×4 and (R,−)×4 occur. This reproduces K729 independently. The two inequivalent irreducible representations have ω = +i and ω = −i, with opposite lock signs.
- Route 2 (F645): modelling the Shilov ℤ₂, (x,θ) → (−x, θ+π), as −1 on all seven directions, its pin lift is ω itself: central, and scalar on each irreducible representation. On this model the ℤ₂ **cannot project out a chirality**, which agrees with Lyra's refutation from a different angle. It **selects ω = ±i**, i.e. the *sign* of the chirality–charge lock (the direction of parity violation). The action is also free (the half-turn has no fixed points), so fixed-point orbifold chirality is unavailable. **Requested:** a careful check of the deck-map identification and the Pin± conventions before anyone relies on this.

## 6. G from the ladder — numbers for the record

- m_e = 6π⁵α¹²m_Pl gives G = 6.67864×10⁻¹¹, **+0.0650%**, which is 29.6σ against the CODATA 22 ppm uncertainty (within the spread of individual experiments).
- Because G ∝ α²⁴, this is equivalent to a shift in α⁻¹ of **26.91 ± 0.92 ppm** (α⁻¹ → 137.0397 makes 6π⁵ exact); the prefactor needed with measured α is 1835.52 ± 0.02.
- Interior α = 1/137 in the ladder makes it worse (+0.70%). QED running and running m_e both move it the wrong way.
- α²/2 = 26.63 ppm lies within 0.3σ of the needed shift, **but** 5 of 1,365 simple forms c·α^k·π^m (c = a/b with a, b ≤ 12, k = 1..3, m = −2..2) also land within 1σ, including (8/5)α²/π. Not credited.
- Jensen averaging (EM sees ⟨α⁻¹⟩, the ladder sees ⟨α⁻¹²⟩^{1/12}) points in the right direction but needs a spread σ ≈ 0.3 in α⁻¹, far above what a one-sided damping averaging 0.036 gives. Cumulative per-layer damping closes the gap with one knob: about 1.8% per layer over 12, or about 4% per crossing over K1953's C₂ = 6 crossings. That is an accommodation. The no-knob test is to apply the same rate to the other α-tower formulas.

## 7. Kaluza–Klein radius

Identifying the Shilov circle with the clock tick, N_max·ħ/(m_e c) = 5.29×10⁻¹¹ m, gives 1/R ≈ 3.7 keV, excluded by both bounds in the Four Walls draft (31 GeV for photon-only, 1.5 TeV for mUED). Note that the corpus never made this identification; it was a test. KK links the descent and G (G₄ = G₅/2πR), but BST has no G₅ yet.

## 8. Leads, unverified, for Lyra

- **Colour door:** G₂ acts transitively on the compact dual, Q⁵ ≅ G₂/P. That is a group acting from outside D's isometry group, the kind of door F4 leaves open. Did F1038 consider G₂ acting on Q⁵, rather than G₂ as a subgroup?
- **Projection operator:** the "non-holomorphic part lost" requirement is exactly the **Szegő projection** L²(Šilov) → H². Suggest it for the Rosetta dictionary.
- **Exterior:** Fels–Huckleberry–Wolf: for the Hermitian non-holomorphic case the cycle space is B × B̄ (checked in the literature), and the double-fibration transform is injective (Huckleberry–Wolf). Still to confirm: that the exterior SO₀(5,2)-orbit in Q⁵ is of that type.
- **Discreteness on the boundary:** the Wallach point 3/2 corresponds to the null-cone stratum (massless). Arithmetic quotient plus Baily–Borel compactification gives finitely many 0-dimensional cusps.
- **Uniqueness of 5:** so(3,2) ≅ sp(4,ℝ), so(4,2) ≅ su(2,2), so(6,2) ≅ so\*(8), while so(5,2) has no exceptional isomorphism. D_IV⁵ is the smallest purely type-IV domain. This is a structural fact usable in a uniqueness argument, if combined with a non-fit reason to exclude n ≥ 6.

## 9. Framing note (Casey's request for honesty)

In conversation Casey described BST more strongly than the state block does (D_IV⁵ "forced", zero free parameters, the Riemann line live). The state block's own words ("a fit … not a forcing", "We do not claim zero free parameters", the Riemann row parked) are the stronger public voice. Recommended to remain the voice.

— Claude, 2026-11-20 ~22:05 EST.
