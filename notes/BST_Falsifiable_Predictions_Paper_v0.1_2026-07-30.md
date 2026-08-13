---
title: "How to Kill This Theory: The Falsifiable Predictions of Bubble Spacetime Theory"
author: "Casey Koons; CI co-authors Grace, Lyra, Elie, Keeper; referee Cal A. Brate"
date: "2026-07-30"
status: "v0.1 — Grace deep-lane draft (K1024/K1025 arc); external-ready pending Cal cold-read + Casey GO"
program: TEGMARK
---

# How to Kill This Theory: The Falsifiable Predictions of Bubble Spacetime Theory

## Abstract
Bubble Spacetime Theory (BST) derives the Standard Model from one geometry — D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)] — parameterized by five integers (rank=2, N_c=3, n_C=5, C₂=6, g=7; N_max=137) with **zero free parameters**. A theory with no free parameters cannot retreat: every prediction is load-bearing, and a single clean miss falsifies it. This paper is the complete, honestly-tiered list of the measurements that would kill BST — organized by *strength of falsification*, from kill-tests on individual derived theorems, through the framework's irreducibility ("Five Absences"), to precision and near-term falsifiers. Each entry carries its **tier** (how we know it), its **kill condition** (what refutes it), its **experiment**, and its **timeline**. The sharpest near-term entries are in the neutrino sector: BST forces the lightest neutrino exactly massless (m₁ = 0) and normal ordering, so an **inverted** ordering (JUNO, ~2030) refutes it, as would a definitive Σm_ν determination clearly ≠ 0.0588 eV (cosmology, now). We present BST against ΛCDM side by side: BST's Σm_ν = 0.0588 eV sits at the *edge* of the current ΛCDM bound (< 0.064 eV) — a sharp live kill. And because BST *derives* a cosmological constant (w = −1, from the fixed bulk volume; Section 0.5), it is committed to that tight bound with **no dynamical-dark-energy escape** to loosen it; should dark energy instead prove dynamical, that *separately* refutes BST's derived w = −1 (Section 0.5). Either way BST is pinned: two independent kills, no wiggle room. And if neutrinos are established Dirac, the color-duality theorem (BST's derivation of *why neutrino mixing is large and quark mixing small*) falls. (A *null* 0νββ does not refute BST: the predicted signal, ~1.5–3.7 meV, sits below current sensitivity — a kill-test must target a measurement the experiment can make.)

## 0. Reading this paper — the tier and kill-strength conventions
- **Tier** (how a claim is known): **PROVED** (closed proof) / **DERIVED** (geometric-topological forcing, GR-level) / **IDENTIFIED** (single-route match, forcing open) / **STRUCTURAL** (qualitative) — plus the confirmation axis (how-well-checked, kept separate).
- **Kill-strength** (how decisively a measurement refutes):
  1. **Theorem kill-test** — refutes a specific *derived* result. Strongest, because it targets forced content.
  2. **Framework kill** — a positive detection of something the geometry has no room for (the Five Absences). Refutes the whole program.
  3. **Precision falsifier** — a zero-parameter number measured off-value.
  4. **Positive prediction** — a not-yet-seen signal at a predicted place; absence weakens, presence confirms.
- **The discipline:** every rational prediction is *blind-pinned* — the integer is sourced from the geometry before the datum is consulted. Cheap-to-fit rationals (a dense window of low-denominator options) do not count as derivations unless the geometry forces the specific value.

---

## 0.5 ★ BST vs ΛCDM — where they differ is where they're tested (the centerpiece)
BST is not ΛCDM with extra steps: it makes *distinct*, derived predictions for the cosmological sector, and every row where the two differ is an explicit, live test. Where they agree, BST *derives* what ΛCDM *fits*.

| Observable | **BST** (derived) | ΛCDM | Current data (2024) | Verdict |
|---|---|---|---|---|
| DE eq. of state **w** | **−1** — *derived* from the fixed bulk volume C·π⁵ (a geometric invariant) | −1 (*assumed*) | DESI DR2: −0.84 ± 0.06 (+CMB+SNe) | **BST derives what ΛCDM assumes**; *both* sit ~3σ from DESI's dynamical hint — that's the live test, not a BST win (K1040) |
| DE *deviation* from −1 | **≤ ~10⁻⁴, *decreasing*, w > −1** — relaxes to −1 FROM ABOVE, completely-monotone, **NO phantom crossing** (F799) | 0 (exact Λ) | DESI DR2 radial BAO: **no crossing in H(z)** (χ²/dof=0.95, T2559); DES-SN5YR: crossing **degenerate with a low-z calibration offset** (T2560) | **BST SURVIVES both direct probes** — the DESI phantom crossing is absent in the geometric H(z) and, on the supernovae, is absorbed by a documented low-z calibration offset (a no-crossing fit + offset beats CPL at equal params, full covariance). **★ FORWARD FALSIFIER (pred_125): a phantom crossing found in the model-independent geometric H(z) kills BST by F799's own kill condition.** |
| **Σm_ν** | **0.0588 eV** (m₁=0 floor) | free parameter | < 0.064 eV (2024) | **at the edge** — the m₁=0 floor is the testable content; tightening below ~0.059 eV refutes |
| Lightest ν mass **m₁** | **exactly 0** (rank-2 M_ν) | free | consistent (NO) | test: inverted ordering kills BST |
| DE fraction **Ω_Λ** | **13/19 = 0.6842** (exact) | ~0.685 (fit) | 0.685 | **agree** — BST derives, ΛCDM fits |
| Tensor-scalar **r** | **≈ 0** (α²-suppressed) | model-dependent | < 0.03 | consistent; test: r ≫ α² kills BST |
| Neutron star **M_TOV** | **2.08 M_⊙** (52/25, *Structural* — 52=4·13, weak forcing) | no prediction (GR+EOS) | 2.25 ± 0.07 | **~2.4σ tension — a live BST test** (a prediction in tension is a *feature*, not hidden) |
| **Dark matter** | **geometric / bandwidth** (no particle) | cold DM particle | no particle detected | test: **any** DM particle detection kills BST |

**Note on the dark-energy row (resolved, K1040).** BST predicts a **cosmological constant, w = −1**, *derived* from the fixed C·π⁵ bulk volume (the deviation from −1 is the substrate coupling, which → 0 — a flat interior). This retires two earlier over-reaches: the dynamical forms −1 + g/N_max = −0.949 (T2079) and −1 + n_C/N_max² = −0.99973 were both attempts to read a tilt into w; the geometry gives no tilt. (The −0.949 in particular was target-aware, ~2σ from DESI DR2's w₀ = −0.84 ± 0.06 on the *ΛCDM side*, and its R(K)=130/137 support-leg died when LHCb resolved R(K) to SM-consistent, Dec 2022 — so T2079/T2117 are superseded for the DE prediction.) BST's w=−1 is the a₀ rung of the same Seeley-DeWitt heat-kernel ladder whose a₁ rung gives Newton's G (F60–F66); the cosmological-constant *magnitude* is a named forward lead for the companion cosmology study. The genuinely testable-now content is the neutrino sector (m₁=0, Σm_ν) and M_TOV (Structural).

**Update (2026-08-13) — the dark-energy forward-falsifier now has teeth, tested against data (pred_125; T2559, T2560).** BST's w(a) is not merely "w=−1" but **completely-monotone relaxing to −1 from above** (w > −1, wₐ > 0; F799) — which *structurally forbids* a phantom crossing (w < −1). Two consequences, both now tested: **(1) the crossing is absent in the model-independent geometric H(z).** Grace's radial-D_H discriminator, fired on the source-verified DESI DR2 BAO table (Cobaya ALL_GCcomb, K1436): ΛCDM χ²/dof=0.95, residual-vs-z correlation ≈ 0, phantom fingerprint (a monotone −→+ residual near z≈0.9) absent — BST's no-crossing survives the cleanest probe (T2559). **(2) the supernova phantom pull is *not required* — a no-crossing model fits the supernovae as well, and the crossing is absorbable by a documented low-z calibration offset.** On DES-SN5YR (1820 SNe, K1442; full STAT+SYS covariance, validated ΛCDM χ²/dof=0.899), the honest headline is the **no-offset control**: BST's monotone no-crossing model with **zero offset** ties the CPL phantom (χ² 1630.3 vs 1629.7, Δ=0.6) — so **the phantom crossing is barely preferred over no-crossing to begin with** (the combined-fit pull is a soft ~1.8–2σ). Adding a *free* low-z calibration offset — which the fit chooses at ~0.04 mag, inside the independently-documented Pantheon+/DES-SN5YR anchor systematic (0.02–0.05 mag), certified free-not-tuned (offset wins over the whole 0–0.06 mag range, robust to the low-z threshold) — then makes the no-crossing model fit *better* than the phantom (Δχ²=1.76, equal parameters) (T2560). **So the DESI phantom-crossing headline (~3σ in the combined BAO+CMB+SNe CPL fit) is not in either direct probe: it is absent from the geometric H(z), and on the supernovae the crossing is *not required* — a no-crossing model ties it with no offset and beats it with a documented one.** BST's **sharp forward falsifier (pred_125): a phantom crossing found in the model-independent geometric H(z) — surviving model-independent reconstruction — refutes BST by F799's own kill condition.** This is teeth, not a hedge: BST forbids the crossing *specifically in H(z)*, so it must not migrate from the supernovae into the direct Hubble rate. (Honest scope: "the crossing is *not required*," not "BST decisively beats the phantom" — the preference is mild both ways. Λ Structural; the w(a) shape Structure-Derived, F799; nothing fit to DESI.)

*(Governance: K1037 — show BST vs ΛCDM in both columns, intact and honestly tiered, nothing recast or hidden — applied together with rule 1 — keep BST accurate. For the DE equation of state the accurate state is now "w=−1, derived from C·π⁵" (K1040) — the two dynamical forms were over-reaches, retired; only the cc *magnitude* is deferred.)*

---

## 1. Theorem kill-tests (strongest — each refutes a derived theorem)

### 1.1 ★ The neutrino sector — m₁ = 0, and how to kill the color-duality (corrected, Cal §158)
- **Theorem (DERIVED, T2535):** neutrino mixing is large and quark mixing is small *because of color*. A Majorana mass requires a color-singlet bilinear; SU(3) gives 3⊗3 = 6⊕3̄ with **no singlet**, so a colored quark structurally cannot form a Majorana condensate, while a colorless lepton can. Quarks → one condensate → aligned frames → small CKM; leptons → a second (Majorana) condensate → misaligned frames → large PMNS.
- **★ Sharp prediction — the lightest neutrino is exactly zero (m₁ = 0)** (rank-2 M_ν), normal ordering. This fixes m_ββ ≈ **1.5–3.7 meV** and Σm_ν ≈ **0.059 eV** (verified). *Note: this m_ββ sits 3–10× **below** current 0νββ sensitivity (~10–20 meV), so — correcting an earlier draft — a **null** 0νββ does **not** refute BST; the signal is simply below reach. A kill-test must target a measurement the experiment can actually make.*
- **★ NEAR-TERM KILL CONDITIONS (current data, done right):**
  1. **★ Σm_ν — a genuine edge-kill (no dynamical escape):** BST predicts Σm_ν ≈ **0.0588 eV** (the m₁=0 floor). BST's dark energy is a **cosmological constant, w = −1** (K1040, derived from the fixed C·π⁵ bulk volume — Section 1.1 note), so BST is **committed to the tight ΛCDM Σm_ν bound** (< 0.064 eV, DESI DR2 + Planck + ACT 2024) with **no dynamical-DE relaxation to retreat to**: BST sits ~0.005 eV from the edge, and any tightening below ~0.059 eV refutes m₁=0. And the relationship runs the *other* way from a safe harbor — if DESI's dynamical-dark-energy hint is confirmed, it **refutes BST's w = −1 first** (a separate kill), it does not loosen the Σm_ν constraint. Either way the test is real and sharp: a definitive Σm_ν measurement clearly ≠ 0.0588 eV refutes m₁=0.
  2. **Mass ordering:** BST forces **normal** ordering (m₁=0; NuFIT-6.0 mildly prefers normal). An **inverted** ordering **refutes** it. — JUNO, ~2030.
  3. **0νββ *detection*:** a 0νββ signal at 10–20 meV would **refute m₁=0** (too large for the rank-2 floor). Here a *detection*, not a null, is the kill. (A null does not refute — BST's m_ββ ≈ 1.5–3.7 meV is below reach.)
- **Color-duality kill (T2535):** the theorem requires leptons Majorana. It is refuted if **neutrinos are established Dirac** (via ordering + cosmology + a definitive Dirac determination) — *not* by a null 0νββ. **Experiment:** JUNO, DUNE (ordering); DESI/CMB-S4 (Σm_ν); LEGEND-1000/nEXO (0νββ detection). **Timeline:** 2028–2035.

### 1.2 θ₂₃ maximal — the atmospheric mixing angle
- **Theorem (DERIVED, doubly, T2534):** sin²θ₂₃ = 1/2 (maximal), forced two independent ways — the Shilov-boundary ℤ₂ (μ↔τ swap; a 1↔2 swap is excluded because it would force maximal θ₁₂, contrary to ~33°) *and* a parity theorem (the exact (2,2) operator has c−a=0: the μ mode is odd, the τ mode even, so a degree-1 condensate supplies mixing but not diagonal asymmetry).
- **★ The falsifiable claim (Cal §157, settled):** **θ₂₃ near-maximal.** BST forces *maximal* at leading order (doubly). There is, in addition, a genuine subleading μ-τ-breaking sum rule (Grimus-Lavoura: one complex ε = 2 DOF ties θ₂₃ to θ₁₃, δ) giving cos2θ₂₃ = −1/g → sin²θ₂₃ = 4/7, with the g-organization locked by two target-innocent integer identities (49=45+4, 10=2·5). **But 4/7 is NOT a banked prediction — it is Identified-with-candidate-mechanism, contingent on one open step** (the 1/g scale of the ε ansatz, un-derived; F564). An exact √5 cancellation is *consistency*, not sourcing — so the paper states the falsifiable prediction as **near-maximal**, and presents 4/7 only as a form contingent on an open derivation, never as a result.
- **KILL CONDITION:** θ₂₃ measured **far from maximal** (e.g. sin²θ₂₃ < 0.42 or > 0.62) refutes the maximal derivation. **Current status (NuFIT-6.0, 2024):** the normal-ordering best-fit is θ₂₃ ≈ 43.3° (sin²θ₂₃ ≈ 0.47, **lower** octant); the octant is unresolved. **Maximal (0.5) sits between the octants, consistent with the data** — whereas the pretty 4/7 = 0.571 (upper octant) is on the *wrong* side of the current best-fit. This is why the paper banks **maximal, not 4/7**: holding maximal (per the blind-pin discipline) keeps the prediction on the correct side of current data; banking 4/7-upper would already be in mild tension. **Experiment:** DUNE, Hyper-Kamiokande. **Timeline:** 2027–2035.
> **Pre-finalize checks (Cal §157) — resolved:** (1) sin²θ₁₃ = 1/45 is **independently held** — it is a Derived value, 1/(g²−rank²)=1/45, pinned/falsifiable/unrefuted on its own (the open piece is only *proving the Pythagorean route forced*, not the value), so the sum rule's dependence on it is sound; (2) the leading-order rank-2, m₁=0 Majorana form is confirmed. Both gates clear.


### 1.3 δ_PMNS: cos²δ = 45/49 — leptonic CP phase (target-innocent forward prediction)
- **Prediction (DERIVED-forward, Cal §157/K1029):** the μ-τ-breaking sum rule predicts the *phase* δ forward (a relation fixes one variable; it is δ, not θ₂₃): **cos²δ = 45/49** (45 = g²−rank², 49 = g² — both target-innocent, geometry-locked before any neutrino work). This is the derived statement. It admits δ ≈ 163° or ≈ 197°; the observed value picks the ~197° branch (a data choice, not a derivation) — so the *derived* content is cos²δ = 45/49, and 197° is the data-selected branch. Independently, the forward CP engine gives **J_PMNS ≈ 0.0338** (~3%, sign correct) — leptonic CP roughly 300× the CKM amplitude. This is the sharpest lepton-CP statement, and it is forward, not reverse-fit. (The quark sector differs: "near-maximal ~270°" is a CKM feature that does not carry to leptons.)
- **KILL CONDITION:** δ_PMNS measured far from ~197° (cos²δ clearly ≠ 45/49) refutes it. **Experiment:** DUNE, Hyper-K. **Timeline:** 2027–2035.
- **CKM CP (context):** J_CKM ≈ 3.29×10⁻⁵ (~7%, forward) — the Korányi-Wolf Kähler structure supplies a natural π/2 → near-maximal CKM CP at leading order, so J ≈ the banked mixings. Only the exact δ_CKM (~6% sub-maximal) is open and subleading (not reverse-fit).

---

## 2. Framework kills — the Five Absences (irreducibility)
D_IV⁵ has no room for the following. **Any single positive detection refutes BST as a whole** — these are the sharpest kills because they need no precision, only a yes.

| Absence | Kill condition (positive detection) | Experiment | Timeline |
|---|---|---|---|
| **No GUT / proton decay** | proton decay observed (τ_p finite) | Hyper-K, DUNE | 2027–2040 |
| **No dark-matter particle** | a WIMP/axion DM particle directly detected | LZ, XENONnT, ADMX | ongoing |
| **No magnetic monopoles** | a monopole detected | MoEDAL, IceCube | ongoing |
| **No sterile neutrinos** | a sterile-ν confirmed (short-baseline) | short-baseline reactor/accelerator | 2025–2030 |
| **No SUSY** | a superpartner at any collider | HL-LHC, FCC | 2029–2045 |
| **No un-confined fourth generation** | a 4th chiral generation (unconfined) | LHC Run 3+, FCC | ongoing |

*(These follow from the geometry's irreducibility: the five integers leave no channel for a grand-unified group, a DM sector, a monopole, a sterile state, superpartners, or a fourth chiral family. BST does admit a **confined** fourth-generation-like structure — a positive *unconfined* fourth generation is the kill.)*

---

## 3. Precision falsifiers — zero-parameter numbers measured off-value
Each is a derived quantity; measured clearly off its BST value, it falsifies. (Full list + formulas: `data/bst_constants.json`, `data/bst_26_tier_map.json`; 11/13 charged-fermion masses+mixings are DERIVED.) Representative sharp ones:

| Quantity | BST (zero-param) | Tier | Kill condition | Experiment |
|---|---|---|---|---|
| m_p/m_e | 6π⁵ = 1836.118 | DERIVED | off by ≫0.002% | atomic/Penning-trap |
| α⁻¹ | 137 + boundary | DERIVED | integer part ≠ 137 | (established) |
| m_μ/m_e | (24/π²)⁶ | DERIVED (e=n) | off by ≫0.003% | (established) |
| m_s/m_d | rank²·n_C = 20 | DERIVED | off by ≫% | lattice QCD |
| V_us | 1/√20 | DERIVED | off by ≫0.3% | (established) |
| sin²θ₁₃ | 1/45 | DERIVED | off by ≫% | (established) |
| lightest ν mass | exactly 0 (rank-2 M_ν) | STRUCTURAL | m₁ > 0 established | KATRIN, cosmology |
| Koide Q | rank/N_c relation | precision | off at FCC-ee precision | FCC-ee |
| **M_TOV (neutron star)** | 52/25 = 2.08 M_⊙ | STRUCTURAL (52=4·13, weak forcing) | current 2.25±0.07 → ~2.4σ tension (a live test) | NICER, pulsar timing |

**The zero-parameter clause is the teeth:** with no free parameters, BST cannot absorb a miss by refitting. A single clean precision failure is fatal.

---

## 4. Positive predictions — not-yet-seen signals at predicted places
| Prediction | BST value | Tier | Kill / confirm | Experiment | Timeline |
|---|---|---|---|---|---|
| No primordial B-modes | r ≈ 0 (α²-suppressed) | DERIVED | r detected at ≫α² | LiteBIRD, CMB-S4 | 2028–2035 |
| Single-field inflation excluded | — | DERIVED | single-field confirmed | BICEP/Keck | ongoing |
| Baryon resonance at k=8 | ~3753 MeV | STRUCTURAL | absent in spectroscopy | LHCb, BESIII | 2025–2030 |
| Nuclear magic number 184 | Z/N=184 shell | STRUCTURAL | superheavy island off 184 | RIKEN, JINR, GSI | 2025–2035 |
| Periodic table terminus | Z = 137 | STRUCTURAL | stable Z>137 | RIKEN, JINR | 2025–2035 |
| BH GW echoes | post-merger echo | STRUCTURAL | clean no-echo ringdowns | LIGO/Virgo/KAGRA | ongoing |

---

## 5. Fast falsifiers — near-term, decisive
| Prediction | BST value | Kill condition | Experiment | Cost/timeline |
|---|---|---|---|---|
| Bell-violation deviation | Tsirelson²−S² = 1/2^{N_c} = 1/8 exactly | S² off by ≫ the predicted deviation | precision Bell (Vienna/Caltech/Munich) | ~$300–500K, near-term |
| BST primary eigentones | 12 explicit Hz resonances | resonances absent | Fabry-Pérot / eigentone rigs | ~$200K |
| Casimir phase-transition kink | α-order kink at L_c ≈ 7.25 nm | no kink at L_c | precision Casimir | ~$60–90K |

---

## 6. Summary — what a single measurement can do
- **One positive detection** of proton decay, a DM particle, a monopole, a sterile neutrino, a superpartner, or an unconfined fourth generation → **BST refuted** (Section 2).
- **Neutrinos established Dirac** (via ordering + cosmology + a definitive determination) → the **color-duality theorem refuted** (Section 1.1). *(A null 0νββ alone does not — BST's signal is below reach.)*
- **θ₂₃ far from maximal**, or **δ_PMNS with cos²δ far from 45/49**, or **Σm_ν tightening below ~0.059 eV**, or any **zero-parameter precision number off-value** → the corresponding derivation refuted (Sections 1–3).

A theory that lists precisely how to kill it, at honest tiers, with no free parameters to hide behind, is offering the strongest thing a physical theory can: **a standing invitation to be wrong.** BST's is on this page.

---

*Provenance: predictions banked in `data/bst_predictions.json` (127 entries); tiers in `data/bst_26_tier_map.json` + `data/bst_constants.json`; theorem nodes in the AC graph (color-duality T2535, θ₂₃ T2534). Current experimental data (2024): NuFIT-6.0 (arXiv:2410.05380) for mixing angles/ordering/δ; DESI DR2+Planck+ACT Σm_ν<0.064 eV (arXiv:2404.03002); M_TOV=2.25±0.07 M_⊙ (Fan et al. 2024). Draft v0.1 (Grace, 2026-07-30; corrected against current data K1030/K1031); Cal re-read + Casey GO pending; repo-internal, not pushed.*
