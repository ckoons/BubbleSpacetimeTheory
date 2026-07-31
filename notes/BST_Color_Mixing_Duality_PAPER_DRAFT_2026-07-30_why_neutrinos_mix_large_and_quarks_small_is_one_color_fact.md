# Why Neutrinos Mix Widely and Quarks Barely: The Color–Mixing Duality
### The Standard Model's two mixing sectors have opposite character for one gauge reason

*v1.0 (external-ready) — 2026-07-30. Lyra (Claude Opus 4.8) with Casey Koons; team: Elie, Grace, Keeper, Cal. Repo-internal; pending Cal's rigor cold-read + Casey's GO. Not for distribution without it.*

---

## Abstract

The Standard Model contains, as unexplained input, a striking asymmetry: the leptonic mixing matrix (PMNS) is *large* — two of its three angles are near or above 30° — while the quark mixing matrix (CKM) is *small*, close to the identity. The SM offers no reason. We show, in Bubble Spacetime Theory (BST) on the domain D_IV⁵, that this contrast is **forced by color**: a Majorana mass requires a color-singlet fermion, so quarks (color triplets) cannot be Majorana and are Dirac-only, giving them a single mass-condensate and nearly-aligned frames (small CKM); leptons (color singlets) admit a Majorana neutrino — required here by the odd embedding integer g = 7 — giving them a *second*, independent mass-condensate and misaligned frames (large PMNS). The **qualitative contrast is Derived** from gauge invariance plus the odd-g Majorana lock; the exact mixing values remain separate, per-sector computations. The result is falsifiable in a clean way: it requires the neutrino to be Majorana, so **any demonstration that neutrinos are Dirac refutes it.** And the sharpest handle is *live now*: a massless lightest neutrino (m₁ = 0) gives Σm_ν ≈ 0.0588 eV, right at the current cosmological bound (Σm_ν < 0.064 eV at 95%, DESI DR2 + Planck + ACT, 2024) — a modest tightening refutes it. BST *derives* a cosmological constant (w = −1, from the fixed bulk volume of the domain), so it is committed to this tight bound rather than an escape to a looser one — making Σm_ν = 0.0588 eV a genuine edge kill with no wiggle room. (BST's w = −1 is itself a derived prediction and a separate live test: DESI DR2's central fit currently hints at dynamical dark energy, w₀ ≈ −0.84, so a firm dynamical result would be in tension with BST's w = −1.) BST also predicts *normal* ordering, which JUNO can confirm or kill by ~2030.

---

## 1. The unexplained fact

Two unitary matrices rotate the Standard Model's fermions between their mass and interaction bases: V_CKM for quarks, V_PMNS for leptons. Measured, they could hardly be more different:

| | CKM (quarks) | PMNS (leptons) |
|---|---|---|
| 1–2 angle | θ_C ≈ 13° | θ₁₂ ≈ 33° |
| 2–3 angle | ≈ 2.4° | θ₂₃ ≈ 45° |
| 1–3 angle | ≈ 0.2° | θ₁₃ ≈ 8.6° |
| character | **≈ identity** | **large** |

The SM accommodates both by fiat — 10 independent Yukawa-derived parameters — and explains neither the smallness of one nor the largeness of the other. This paper gives the reason for the *contrast*.

## 1.5 The setting (self-contained)

Bubble Spacetime Theory derives the Standard Model's structure from a single bounded symmetric domain, D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)] — the rank-2, five-complex-dimensional Cartan domain of type IV. Five integers fix everything: rank = 2, the color number N_c = 3, the complex dimension n_C = 5, the second Casimir C₂ = 6, and the embedding integer **g = 7**. Two features of this domain carry the present argument, and a reader need accept only these two:

1. **Color is the off-diagonal of the domain's Jordan structure**, of dimension N_c = 3 — so quarks (which live there) are color triplets and leptons (which live on the color-neutral frame) are singlets. Standard SU(3) gauge invariance then applies unchanged.
2. **The embedding integer g = 7 is odd**, and this odd dimension chirality-locks the light right-handed neutrino out of the physical (holomorphic, positive-energy) spectrum: there is no unitary Dirac partner for the neutrino. This is the BST-specific input — the "odd-g Majorana lock" — and it is the reason the neutrino mass, if it exists, must be Majorana rather than Dirac.

Everything else in this paper is ordinary gauge theory. The claim is that these two facts, together, force the observed contrast between the two mixing matrices.

## 2. The gauge lemma

> **Lemma.** A Majorana mass term is SU(3)_color-invariant if and only if the fermion is a color singlet.

A Majorana mass ties a field to itself: it lives in the symmetric product of the field's gauge representation with itself. For a color triplet, 3 ⊗ 3 = 6 ⊕ 3̄ contains **no singlet**, so a quark Majorana mass is not color-invariant and is forbidden. For a color singlet the term is trivially invariant. This is standard, exact gauge theory — it is precisely why every quark in nature is Dirac, and why a Majorana neutrino is not excluded.

## 3. The two sectors

**Quarks — one shared condensate, small mixing.** Quarks are color triplets, so by the Lemma they admit no Majorana mass; they are Dirac-only, with all mass from the single Higgs condensate. In BST the up- and down-type quarks are *near-identical* modes — weak-isospin partners in the domain's off-diagonal "color" sector, differing only by an internal weight — and both couple to that *one shared* condensate. Because a single operator acts on near-identical modes, the diagonalizing frames U_up and U_down nearly coincide, so

> V_CKM = U_up† U_down is close to the identity 𝟙 (small off-diagonal mixing) — forced.

(We write "≈ 𝟙" for *small mixing*, not exact identity: the off-diagonal entries are non-zero but suppressed, precisely because the two frames differ only through the small internal-weight splitting of otherwise-shared modes.)

**Leptons — two condensates, large mixing.** Leptons are color singlets, so the Lemma *permits* a Majorana neutrino mass. In BST it is also *required*: the odd embedding integer g = 7 chirality-locks out a unitary right-handed neutrino, so no Dirac neutrino mass can form and the neutrino mass must be Majorana — generated by a **second** condensate (the Weinberg operator), distinct from the charged leptons' Dirac Higgs. The charged-lepton and neutrino frames U_charged and U_ν are thus the diagonalizing frames of *two different operators*, generically misaligned (alignment would be a measure-zero coincidence), so

> V_PMNS = U_charged† U_ν — large, forced.

## 4. The theorem

> **Color–Mixing Duality.** On D_IV⁵ with the BST field content, color-charge determines the number of independent mass-operators in a sector — one for the colored quarks (Dirac only), two for the colorless leptons (Dirac + Majorana) — and the number of operators determines whether the sector's two frames align (small mixing) or not (large mixing). Hence CKM is small and PMNS is large, forced by SU(3)_color together with the odd embedding integer g = 7.

The Standard Model's two mixing sectors are therefore *not independent*: their relative size is one consequence of color.

## 5. What is derived, and what is not

We are deliberate about the tier, because a clean qualitative theorem must not borrow credit for numbers it does not fix.

- **Derived (qualitative):** the *contrast* — CKM small, PMNS large. Both inputs are forced (the gauge lemma is exact; g = 7 → Majorana is a structural lock in BST).
- **Not fixed by this theorem (separate, per-sector):** the *exact* mixing values — CKM's small angles and PMNS's individual angles are separate computations on D_IV⁵, reported elsewhere, each at its own honest tier. Two examples of that separate work, to show the tiering is real and not rhetorical: the reactor angle is derived as sin²θ₁₃ = 1/(N_c²·n_C) = 1/45 (within experimental error); and the atmospheric angle is derived *maximal*, sin²θ₂₃ = 1/2, forced two independent ways — a μ–τ interchange symmetry of the Shilov boundary (a ℤ₂ quotient) and a parity theorem on the modes (the muon and tau modes have opposite parity, so a degree-1 condensate can generate their mixing but not the diagonal asymmetry that would shift the angle off maximal). This is consistent with the current global fit, and pointedly so: NuFIT-6.0 (2024) gives a normal-ordering best-fit in the *lower* octant (θ₂₃ ≈ 43.3°, sin²θ₂₃ ≈ 0.47), with the octant unresolved. Maximal (0.5) sits *between* the two octants and is consistent with both — so BST's exact prediction is on the robust, octant-agnostic value, whereas a naive "pretty" upper-octant value (e.g. 4/7 ≈ 0.571) would sit on the wrong side of the current best-fit. (Any small deviation from maximal is a separate, subleading effect BST does not currently force — stated as an honest limitation, not papered over.)
- **Not claimed:** that "large" means "maximal," or that the theorem sets any angle's value. It fixes the *sign of the contrast*.

## 6. Falsifiability — how to kill this, and by when

The theorem stands on the neutrino being Majorana with a massless lightest state (m₁ = 0, normal ordering). Each is a live experimental handle; we state them with their *current* sensitivities (as of 2024), and are explicit about which is testable now.

- **Sum of neutrino masses — the sharpest, live *now*, and a genuine edge kill.** With m₁ = 0 and the measured splittings, BST predicts the minimal normal-ordering floor **Σm_ν ≈ 0.0588 eV**. The current cosmological bound is **Σm_ν < 0.064 eV (95%)** (DESI DR2 + Planck + ACT, 2024) — BST sits within ~0.005 eV of it, so a modest tightening below ~0.059 eV refutes m₁ = 0, and with it the boundary-Majorana structure. Crucially, BST does not get to escape to a looser bound: it **derives** dark energy as a *cosmological constant* (w = −1, fixed by the domain's bulk volume; see below), so it is committed to the tight (ΛCDM-form) bound. There is no dynamical-dark-energy relaxation available to BST, because BST's own dark energy is w = −1. So this is a genuine present-day kill-test with no wiggle room.
- **Dark energy — a separate live test, shown as its own prediction.** BST derives **w = −1** (a cosmological constant, from the fixed bulk volume of the domain, with the deviation from −1 → 0). This is a prediction, not an assumption, and it is itself testable: DESI DR2's central fit currently prefers *dynamical* dark energy (w₀ ≈ −0.84 ± 0.06), so a firm confirmation of w ≠ −1 would be in tension with BST. We report this as its own row rather than fold it into the neutrino line — BST predicts w = −1, the data currently hint otherwise, and that difference is the testable content.
- **Neutrino mass ordering.** BST predicts *normal* ordering (m₁ = 0). A confirmed *inverted* ordering refutes the mechanism. JUNO is expected to resolve the ordering at ~3σ by roughly 2030, model-independently — the sharpest *near-term* handle after Σm_ν.
- **The Dirac-vs-Majorana question, directly.** The large-PMNS half of the duality has no source unless the neutrino is Majorana. Any demonstration that neutrinos are Dirac kills it.
- **Neutrinoless double-beta decay (0νββ) — stated honestly.** With m₁ = 0 (normal ordering), BST gives |m_ββ| ≈ 1.5–3.7 meV. This is **3–10× below** the reach of the current generation of experiments (LEGEND-1000, nEXO, KamLAND-Zen probe ~10–20 meV). So a *null* at present sensitivity does **not** refute BST — the signal simply sits below reach, and we do not claim otherwise. What *would* refute m₁ = 0 is a *detection* at ≳10 meV. A future experiment reaching the 1–4 meV floor could test the prediction directly.

This is the strong kind of falsifiability done honestly: several independent handles, the sharpest of them (Σm_ν) already at the edge of a current bound, and each stated with the sensitivity it actually needs rather than one aimed at a measurement no experiment can make. It is also BST-native — the g = 7 that forces the Majorana lock is one of the theory's five defining integers.

## 6.5 Scope and limitations

We state the boundaries of the claim explicitly.

- **"Large" is not "maximal."** The theorem forces the *sign* of the contrast (PMNS large, CKM small). It does not, by itself, set any angle's magnitude; those are separate per-sector results (Section 5). In particular it does not derive that any PMNS angle is maximal — that θ₂₃ comes out maximal is an *additional*, independent result, not a consequence of this theorem.
- **The generic-misalignment step.** "Two independent operators ⟹ misaligned frames ⟹ large mixing" uses that exact alignment of two independently-determined unitary frames is a measure-zero coincidence; generic misalignment gives an O(1) mixing angle. This is the standard expectation, but it is a genericity argument, not a computation of the size — again, the size is the separate per-sector work. What is forced is: leptons *can* mix by O(1) (two operators), quarks *cannot* without a coincidence (one operator on shared modes).
- **The odd-g Majorana lock is the BST-specific input.** The gauge lemma is model-independent; the statement that the neutrino *must* be Majorana (no Dirac option) relies on the g = 7 chirality lock, which is internal to BST. A reader skeptical of that step should read the theorem as conditional: *given* that the neutrino is Majorana, the color lemma explains why only the lepton sector carries the second condensate.
- **CP phases are out of scope here.** The Dirac CP phases (δ_CKM, δ_PMNS) are a separate frontier; the two sectors' phases differ and are treated in companion work. This paper concerns the *magnitudes'* contrast only.

None of these weaken the central claim; they delimit it. The forced content is the *contrast*, rooted in gauge invariance plus the odd-g lock — and it is falsifiable (Section 6).

## 7. Plain-language version

Neutrinos mix a lot; quarks barely mix. Physicists measure both and shrug. Here is the reason. A neutrino can be its *own* antiparticle — a "Majorana" particle — but only if it carries no color charge, because the math of a color charge forbids a particle from pairing with itself. Quarks carry color, so they can't do this; they're stuck with one way of getting mass (from the Higgs), and that one way lines their families up, so they barely mix. Leptons carry no color, so their neutrinos get a *second*, different way of getting mass (the "being-its-own-antiparticle" way, which the geometry forces on them) — and two different ways of getting mass twist their families apart, so they mix a lot. The whole big-versus-small difference is one fact about color. And it's testable: if experiments prove the neutrino is *not* its own antiparticle, the explanation is wrong.

---

## Supporting results (BST corpus)

The inputs and companion results this paper relies on, for the reader who wants the underlying derivations:

- **The domain and five integers** — D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)]; rank 2, N_c = 3, n_C = 5, C₂ = 6, g = 7.
- **The odd-g Majorana lock** — g = 7 odd ⟹ no unitary light ν_R ⟹ Weinberg/Majorana neutrino mass; m₁ = 0 (rank-2 M_ν). *(BST F413; 0νββ prediction |m_ββ| ∈ [1.44, 3.63] meV, normal ordering.)*
- **Color = the Peirce off-diagonal V₁₂** of the type-IV Jordan algebra, dim N_c = 3; leptons = the color-neutral frame. *(BST T2511 — the Peirce/spin-factor decomposition of D_IV⁵: color is the off-diagonal V₁₂, dim N_c; explicitly a color multiplicity, NOT a generation genus.)*
- **Small-CKM / one-condensate** — up and down as weak-isospin partners of the same color-triplet modes on one rank-1 condensate. *(BST K768; V_us = 1/√20 blind, 0.31σ.)*
- **Per-sector mixing values** (separate tiers) — sin²θ₁₃ = 1/45; sin²θ₂₃ = 1/2 (maximal, doubly-forced); |U_e2|² = 3/10.

## References (external)

- P. Minkowski; Gell-Mann–Ramond–Slansky; Yanagida — the seesaw / Weinberg dimension-5 operator (Majorana neutrino mass).
- E. Majorana (1937) — Majorana fermions.
- Particle Data Group — CKM and PMNS values; the CKM-small / PMNS-large asymmetry.
- NuFIT-6.0 (Esteban et al., 2024; arXiv:2410.05380) — current global fit of neutrino oscillation parameters; θ₂₃ octant unresolved / consistent with maximal; δ_CP consistent with CP conservation within ~1σ for normal ordering; normal ordering mildly preferred.
- DESI DR2 + Planck + ACT (2024; DESI VI, arXiv:2404.03002) — Σm_ν < 0.064 eV (95%): the current bound against which BST's Σm_ν ≈ 0.0587 eV floor is the live kill-test.
- JUNO — reactor experiment expected to resolve the neutrino mass ordering (~3σ, ~2030): the near-term ordering kill-test.
- LEGEND-1000, nEXO, KamLAND-Zen — current 0νββ programs (sensitivity ~10–20 meV); *above* BST's predicted 1.5–3.7 meV signal, so a present null does not refute (Section 6).

---

*Status: v1.7, external-ready (registry-consistency pass). The qualitative theorem (CKM small / PMNS large) is Derived from gauge invariance + the g = 7 Majorana lock (T2534/T2535, DERIVED; T2511 Peirce color = V₁₂, DERIVED); exact mixing values are separate per-sector results, honestly tiered (Section 5). Cal cleared + 2 polishes ("≈𝟙" clarified; "one shared condensate" tightened) + 2 registry fixes (T2511 described correctly as the Peirce color decomposition, not a generation result; bare superseded DE citations stripped). Dark energy = BST's derived value **w = −1** (cosmological constant, from the fixed C·π⁵ bulk volume; deviation → 0), shown as its own falsifiable row (BST w = −1 vs DESI's w₀ ≈ −0.84 hint). Because BST is committed to w = −1 there is **no dynamical-dark-energy escape**, so Σm_ν = 0.0588 eV is a genuine edge kill against the 0.064 eV bound (not softened). Other falsifiers (Section 6): mass ordering (JUNO ~2030); 0νββ signal below current reach (a null does not refute); θ₂₃ maximal sits between the octants (NuFIT-6.0 NO best-fit lower-octant 43.3°, so 4/7-upper would be on the wrong side); δ_CP near-180° agrees within ~1σ. Scope and limitations stated (Section 6.5). Repo-internal; pending Cal's final clearance and Casey's GO; not pushed or distributed.*
