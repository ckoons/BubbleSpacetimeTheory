# The D_IV⁵ Ribbon: Fermion Quantum Numbers as the Holonomy of a Spinor Winding

**A geometric framework in which every fermion quantum number is one feature of a single framed, twisted, wound ribbon assembled on the bounded symmetric domain D_IV⁵.**

**Author:** Casey Koons
**CI co-authors:** Keeper, Lyra, Elie, Grace
**Status:** Framework draft **v0.2 — 2026-07-10.** *Honestly tiered.* This paper presents a geometric realization, not a completed derivation. Section 7 is a complete ledger of what is derived, what is a candidate mechanism, and what remains open. Nothing here is claimed as proved that is not proved in Section 7.

**v0.2 changelog (corrections from the decider-day results, all in the honest direction):**
1. **The "one −1 does all three" unification (old Section 4) is WALKED BACK.** Grace traced it to a proved theorem (T2470): electric charge *is* the SO(2)-weight operator, and its sign is the weight-sign — not a spinor holonomy. So spin, charge-sign, and matter/antimatter are **three distinct operations** that coincide as −1 but are not one operation. The (−1)ⁿ winding form was a *repackaging of the assignment*, not a mechanism.
2. **Charge (magnitude AND sign) moves to SOLID via proved T2470** — better grounded than v0.1's holonomy story, but as the SO(2)-weight, not a winding holonomy.
3. **The mass sector moves from "open partial" to CONFIRMED STRUCTURAL MISS.** Lyra pinned the type-IV norm exponent ((1−r²)², resolving the radius to Grace's ~0.25), and the odd-degree ladder still cannot fit — the real masses want fractional/ground rungs {1,3,5} forbids. Mass is *not* a degree-rung; the proposed replacement is **membrane refraction** (separate spec).
4. **CP's up-down structure is now SOURCED** (Elie): the weak-isospin doublet is the Pin(2) doublet on the non-orientable Möbius locus (T1949, T2138, proved). The kink is buildable; its magnitude (J) is the remaining test.

---

## Abstract

We propose that the quantum numbers of a fermion — its type, generation, mass, electric charge, spin, and matter/antimatter character — are not six independent labels but six geometric features of a single object: a framed (twisted) ribbon winding assembled on the bounded symmetric domain **D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)]**, the substrate of Bubble Spacetime Theory (BST). The substrate emits discrete information; the holomorphic boundary — which we call the membrane — assembles a self-sustaining spinor oscillator from it and dresses it in energy. This is the discrete/continuous principle promoted from a reading rule to a manufacturing process: **the shape is information (discrete, forced), the energy is dressing (continuous, curvature).**

Five geometric features of the ribbon carry the five families of fermion quantum numbers:

| feature | quantum number |
|---|---|
| **shape** (commitment count 1/2/3) | type: lepton / meson / baryon |
| **pitch** (excitation degree ℓ, radius) | generation and mass |
| **in-out winding** (N_c=3 wraps around rank-2 posts) | electric charge |
| **ℤ₂ half-twist** (ribbon framing) | spin |
| **reading-side** (which side of the ℤ₂) | matter / antimatter |

We show, with explicit tiering, that: **(i)** electric charge (magnitude and sign) is the SO(2)-weight operator of D_IV⁵ (proved, T2470), quantized in units of 1/N_c with exactly N_c+1 = 4 magnitudes {0, 1/3, 2/3, 1}, capped at 1, no exotic charges — passing the BST Five-Absence filter; **(ii)** spin-1/2 is the ℤ₂ half-twist of the ribbon, native to D_IV⁵ as a type-IV (spin-factor) domain, and carries Fermi statistics automatically by the ribbon spin-statistics identity; and **(iii)** CPT is exact by construction, because the antiparticle is the *same* oscillator read from the other side of the membrane's ℤ₂. Spin, the charge sign, and matter/antimatter each carry a "−1," but they are **three distinct operations** — the spinor 2π holonomy, the SO(2)-weight sign, and charge conjugation — related by the geometry, not one operation (a v0.1 over-merge, corrected). The mass sector is a **confirmed structural miss** of the odd-degree ladder; the proposed replacement is membrane refraction (Section 3.2, Section 7).

---

## 1. Introduction

### 1.1 The one mechanism

BST derives the Standard Model from one geometry, D_IV⁵, and five forced integers (rank = 2, N_c = 3, n_C = 5, C₂ = 6, g = 7, with N_max = N_c³·n_C + rank = 137). The present paper isolates a single organizing claim about *fermions*:

> A particle is a standing wave — a self-sustaining oscillator — that the membrane assembles from committed information and releases. Every quantum number of the particle is a geometric feature of that wave. There is one mechanism, and the quantum numbers are its coordinates.

This is not "a theory of everything asserted up front." It is a **geometric realization** whose numerical content is delivered — or falsified — by an explicit construction on D_IV⁵ (Section 8). We state throughout, and collect in Section 7, exactly which parts are proved, which are candidate mechanisms, and which are open.

### 1.2 What a reader should take from this paper

For the referee: a specific, falsifiable claim that fermion quantum numbers are winding-geometry, with a hard ledger of evidence tiers and a single construction that decides the open items.

For the bright high-schooler: *imagine a rubber band wound a few times around two pegs, then given a half-twist and dressed in energy. How many times it winds is its electric charge. The half-twist is its spin. Which way you read it — front or back — is whether it is matter or antimatter. Every "particle" is one such wound, twisted band, and all the confusing labels in a physics textbook are just different ways of describing the band's shape.*

---

## 2. The membrane and the two steps

D_IV⁵ is a bounded symmetric domain of rank 2 and complex dimension 5. Its Shilov boundary is **(S⁴ × S¹)/ℤ₂**. We call this boundary the **membrane**: it is the holomorphic screen on which the interior (bulk) data is written, in the sense of the holographic structure intrinsic to SO(5,2) ⊃ SO(4,2).

A fermion is produced in two steps:

1. **Emission of information (discrete).** The substrate's commitment cycle forms a shape: a winding pattern, an excitation degree, a framing. This is a *count* — forced, integer-valued, target-innocent.
2. **Dressing in energy (continuous).** The membrane assembles a self-sustaining oscillator carrying that shape and dresses it in energy through the Bergman metric, which diverges toward the membrane. This is the *curvature* — continuous, scale-carrying.

These two steps are the discrete/continuous principle of BST, seen as manufacturing rather than as bookkeeping. The particle *is* the assembled oscillator (not something emitted by an oscillator): this is the quantum-field creation operator a†|0⟩ given a mechanism. Because the oscillator is self-sustaining once released, matter is stable without an ongoing energy source; because it is assembled by one process from one template, all electrons are identical; because it is an oscillator, it has an intrinsic frequency, and E = ℏω identifies that frequency with its mass.

---

## 3. The five features

### 3.1 Shape → type (lepton, meson, baryon)

The membrane emits a color-singlet before it can release a particle, and N_c = 3 sets how many commitments a singlet requires. Counting commitments builds an (n−1)-simplex:

- **1 commitment → a point (0-simplex): a lepton** — pointlike, colorless, lightest.
- **2 commitments → a line (1-simplex): a meson** — a flux tube between two endpoints.
- **3 commitments → a triangle (2-simplex): a baryon** — heaviest, the confined triple.

Two consequences follow. First, **confinement is the statement that the pump releases one pulse per completed singlet.** A single colored commitment is never emitted alone; it waits for its partners. Confinement is not a separate force here — it is the emission granularity N_c = 3. Second, the per-commitment energy is m_p/N_c ≈ 313 MeV (the light-quark constituent floor), consistent with the proton being the three-commitment emission product.

Energy grows monotonically with the dimensional extent within a generation (electron 0.5 MeV < pion 140 MeV < proton 938 MeV): "mass = occupied volume," stated as the simplex dimension. (Across generations the pitch ladder of Section 3.2 stacks on top, so a heavy lepton excitation can outweigh a light baryon.)

### 3.2 Pitch → generation and mass (CONFIRMED STRUCTURAL MISS — the odd-degree ladder fails for mass)

Generations are excitation levels. On the rank-2 domain the three natural strata (Korányi–Wolf: bulk / Cartan slice / Shilov boundary) give exactly three, and Elie's blind, mass-independent assignment reads them off the odd cohomology of the compact dual Q⁵:

**ℓ ∈ {1, 3, 5}** — the odd cohomology cycles {h¹, h³, h⁵} (T1929, proved; forced count, not fitted, zero mass reference).

The forced mass ladder, with radius r² = ℓ/(ℓ + n_C) and Bergman dressing m ∝ (1 − r²)^(−n_C), collapses to one parameter-free formula:

**m(ℓ) = (1 + ℓ/n_C)^(n_C).**

There is no fitted temperature: n_C plays the role of the exponent, welded to the metric (the "most dangerous knob," a free kT, is absent by construction).

**We report this, after the full calculation, as a confirmed structural miss — named, not dressed.** The type-IV norm exponent was pinned (it is (1−r²)², squared — Lyra, from solid type-IV structure), which resolves the gen-2 radius to ≈ 0.23 (Grace's ≈ 0.25 vindicated; the earlier r² = 3/8 disc-toy value was an error). *Even with the middle rung in the right place*, the three forced rungs cannot fit the real quark masses: fitting the light ratio (s/d) breaks the heavy ratio (b/d) and vice versa, a trade baked into the geometry. Decisively, the rungs that *would* fit the real masses are **fractional rungs the geometry forbids**, with the lightest quark wanting a **ground rung r = 0 that the odd-cohomology set {1, 3, 5} does not contain.** So this is not "one lookup away" — it is a genuine structural mismatch, and the disciplines held throughout (degrees not bent; the additive dressing Λ = m_p/N_c tested and found *not* to rescue it).

**Conclusion: mass is not a degree-rung.** The odd degrees {1,3,5} are correct for the *spine* (they are the generation cohomology) but the wrong mechanism for *mass*. The proposed replacement — mass as the **refracted emission component** set by the continuous-side index, with a Snell-like law at the membrane — is developed separately (membrane-refraction spec). Notably, Lyra's finding that the lightest quark wants r = 0 *supports* that picture: r = 0 is the deepest, cleanest crossing, the impedance-matched channel.

### 3.3 In-out winding → electric charge

The ribbon winds N_c = 3 times around two posts (Section 4 identifies the posts with the rank-2 torus of D_IV⁵). Each winding wraps a post either "in-out" or "out-in." Electric charge counts the in-out windings:

**|q| = (number of in-out windings) / N_c.**

For n ∈ {0, 1, 2, 3} this gives magnitudes {0, 1/3, 2/3, 1} — **exactly the four fermion charge magnitudes of the Standard Model**, and three structural results follow, all target-innocent (they use N_c = 3, not the observed charges):

1. Charge is quantized in thirds *because there are three windings.*
2. There are exactly **N_c + 1 = 4** magnitudes — matching both the four charges and the four fermion types per generation (ν, d, u, e).
3. **No charge exceeds 1**, and none is a non-third: a genuine forbidden-list prediction. This passes the BST Five-Absence filter — it reproduces the SM charges and forbids the exotic (e.g. GUT leptoquark) charges BST already forbids.

**The grounding (v0.2, proved):** electric charge — magnitude *and* sign — is the **SO(2)-weight operator** of D_IV⁵ (T2470, proved). The magnitude is the weight's size (thirds, N_c+1 values); the **sign is the weight-sign** — which way the winding runs. The winding-count picture above is a faithful *reading* of that weight (a different, N_c-scaled count), not an independent source. In particular the (−1)ⁿ form of the sign (v0.1, old Section 4) is a *repackaging of the assignment*, not a mechanism — the real sign is T2470's weight-sign. So charge sits in Solid (Section 7) on a proved footing, not on a winding holonomy.

### 3.4 ℤ₂ half-twist → spin

Give the winding width — make it a ribbon — and put in one **half-twist** (a Möbius). Trace it: one turn (2π) returns it flipped, −1; two turns (4π) return it to itself, +1. This is not a metaphor for spin-½ — it *is* spin-½: the double cover Spin ⊃ SO, the topological spin θ = e^(2πi s) with s = 1/2 giving θ = −1, the Dirac belt trick. Integer twists give integer spin (bosons); half-twists give half-integer spin (fermions).

Two facts make this native rather than imposed:

- **Spin-statistics is free.** In a ribbon (framed) category, twisting a particle by 2π equals exchanging two of them; the half-twist that gives spin-½ therefore gives the −1 under exchange — Fermi statistics, Pauli exclusion — with no additional postulate.
- **The spinor is native to D_IV⁵.** Type-IV bounded symmetric domains are the **spin-factor** Jordan/Clifford domains; the spinor is the algebraic backbone of the domain, not an import. A fermion is the substrate-Dirac field — the square root of the oscillator (γ·∂ squares to ∂²) — and the half-twist is that square-root operation. Every half-integer that recurs in BST (the ρ-vector (5/2, 3/2), the √ in the Cabibbo angle, "n_C is odd so you get a √") is the spinor structure surfacing.

### 3.5 Reading-side → matter and antimatter

The membrane's ℤ₂ has two sides. The **same** assembled oscillator read from the wrong side is the antiparticle — the Feynman–Stückelberg reading (an antiparticle is a particle read backward in time), here given a mechanism (the two sides of the membrane are the two time directions).

Three facts collapse into one statement:

- **CPT is exact** — because the antiparticle is not an independent object that happens to match; it is the same oscillator read from the other side, so it must be the exact mirror. This is why CPT is the one symmetry never violated: it is not a symmetry between two things but one thing read two ways.
- **CP is violated** — the membrane is not a perfect mirror; the 45° cant tilts it, so one reading is preferred.
- **Matter dominates** — that preference accumulates into the baryon asymmetry. (Its magnitude, η_B, is a separate continuous quantity; only its *existence* and *sign* are the cant here — see Section 7.)

Annihilation is clean in this language: bringing matter and antimatter together reads the same oscillator from both sides at once; it superposes with its own reverse, cancels, and the membrane reclaims the energy.

---

## 4. Three distinct −1's — spin, charge-sign, matter/antimatter (v0.1 over-merge, corrected)

**v0.1 claimed these three were one operation — "the spinor √ appears three times, the same −1 each time." That was an over-merge, and the decider-day audit (Grace, via proved T2470) corrected it.** All three carry a "−1," and they are related by the geometry, but they are **three distinct operations:**

- **Spin** is the ribbon's **2π spinor holonomy** — the odd-n_C half-integer weight makes a 2π winding return −1 (Elie, grounded; SOLID). This is a genuine geometric mechanism.
- **Charge sign** is the **sign of the SO(2)-weight** — which way the winding runs (T2470, proved; SOLID). It is *not* a spinor holonomy. The v0.1 form q = (−1)ⁿ·(n/N_c) reproduces the four signed charges {0, −1/3, +2/3, −1}, but it does so because the winding-count assignment was *chosen* to match the weight-sign — it is a **repackaging of the assignment, not an independent mechanism.** The mechanism is T2470.
- **Matter/antimatter** is **charge conjugation** — reading the same oscillator from the other side of the membrane's ℤ₂ (Section 3.5).

These three coincide numerically at −1 and all live on the same odd-dimensional, spin-type domain, which is why v0.1 was tempted to fuse them. But they are separate operators, and honesty requires saying so: **spin is a holonomy, the charge sign is a weight-sign, matter/anti is a conjugation.** The genuine unifying fact is weaker and still real — all three are native to D_IV⁵ *because* it is odd-dimensional and a spin (type-IV) domain; none of them would exist on an even-dimensional or non-spin domain. That is the defensible referee sentence, not "one −1 does everything."

(The neutrino remains the minimal case: zero SO(2)-weight, so zero charge, plus the spinor half-twist — the bare Weyl spinor, the remainder.)

---

## 5. The drive alphabet

If the commitment cycle sorts light into the section spaces of the compact dual Q⁵ = SO(7)/[SO(5)×SO(2)], the loading counts are the low SO(7) representation dimensions — and, computed forward and target-innocent (Grace), they *are* the substrate integers:

| Q⁵ section space | dimension | equals |
|---|---|---|
| O(1) sections | 7 | g |
| spinor bundle | 8 | 2^(N_c) |
| adjoint | 21 | N_c·g |
| O(2) sections | 27 | N_c³ |

The **27 loadings** are the quadratic functions on Q⁵ — a finite drive alphabet, not a continuous knob. This resolves a Five-Absence concern: 27 is O(2) on our own geometry, not the E₆/Albert (forbidden GUT) 27. It also quantizes the "variable pump" that distinguishes up from down: the up and down loadings are different code words in a finite alphabet, so their relative phase (CP) is discrete and information-forced, not dialed. Whether {7, 8, 21, 27, …} forms a forced emission code with a physics-forced level is open (Section 7).

---

## 6. Predictions and falsifiers

The framework is falsifiable at several points that do not depend on the open mass sector:

1. **Charge:** no fermion has |q| > 1; every charge is a multiple of 1/N_c = 1/3; exactly N_c + 1 magnitudes exist. Any exotic charge falsifies the winding count.
2. **Spin:** only spin-½ matter and integer-spin carriers; **no spin-3/2** (no gravitino), no exotic-spin states. This is the same content as BST's standing no-SUSY-spectrum prediction, now geometric.
3. **CPT exact; CP violated; matter dominant** — required together, from one oscillator read on a slightly tilted membrane. A measured CPT violation falsifies the mechanism outright.
4. **No-cloning, derived.** Copying requires assembling from *committed* information, but committing an unknown superposition is measurement — it collapses. So the substrate can copy the sealed/encrypted state (the wrapper — allowed) but **cannot commit one thing twice**: the outcome exists only at the act of commitment, and the act is singular. A demonstrated perfect cloner of unknown accessible quantum states would falsify BST. (Consistent with the Yamaguchi–Kempf *et al.* encrypted-cloning demonstration, which clones the wrapper under a single-use key — exactly the boundary at commitment.)
5. **Neutrino as minimal spinor** — the lightest neutrino is the bare half-twist with zero SO(2)-weight (zero charge); the framework favors a nearly-massless ground state (normal ordering).

---

## 7. The honest ledger

This is the load-bearing section. Nothing outside this table should be read as a stronger claim than the table permits.

**DERIVED / SOLID (proved theorem, target-innocent, or standard mathematics):**
- **Charge — magnitude and sign — is the SO(2)-weight operator (T2470, proved).** Quantized in units of 1/N_c, exactly N_c+1 magnitudes {0, 1/3, 2/3, 1}, capped at 1, no exotics. Five-Absence PASS. (Section 3.3) *Upgraded from v0.1's winding-holonomy story to a proved footing.*
- Spin = ribbon half-twist ⇒ spin-½ + Fermi statistics; the spinor is native to the type-IV (spin-factor) domain; the 2π holonomy is the odd-n_C half-integer weight (Elie, grounded). Standard ribbon/framing mathematics. (Section 3.4)
- CPT exactness as a structural consequence of "one oscillator, two readings." (Section 3.5)
- **The two posts = rank-2 torus; the poles = Shilov boundary (S⁴×S¹)/ℤ₂** — source-pinned to the polydisk theorem (Elie), not asserted. (Section 4, Appendix)
- The drive alphabet {7, 8, 21, 27} = SO(7) rep dimensions = the substrate integers, computed forward. (Section 5)
- **No-cloning**, derived from the commitment-collapse mechanism (copy the wrapper, commit once). (Section 6)

**CANDIDATE / SOURCED-BUT-UNBUILT (structure in hand, magnitude untested):**
- **CP mechanism — the up-down twist — is now SOURCED** (not merely candidate): the weak-isospin doublet is the Pin(2) doublet on the non-orientable Möbius locus (T1949, T2138, proved); the relative Pin(2) twist is the kink, and the same non-orientability gives parity violation — one locus, both. The *existence* of CP is grounded; only the *magnitude* (J) is untested (see Open). (Sections 3.5, 4)
- The particle-to-count assignment (why ν, d, u, e sit at their SO(2)-weights) — a reading of the proved weight, awaiting a first-principles ordering. (Section 3.3)

**OPEN:**
- **The masses — CONFIRMED STRUCTURAL MISS of the odd-degree ladder.** With the type-IV exponent pinned ((1−r²)²) and the gen-2 radius resolved (≈ 0.25), the three forced rungs still cannot fit; the fitting rungs are fractional and include a ground rung r=0 that {1,3,5} forbids. Mass is not a degree-rung. **Proposed replacement: membrane refraction** (separate spec) — framework-tier, gated on deriving the Shilov-boundary matching condition. (Section 3.2)
- **CP magnitude** — does the sourced Pin(2)/Möbius kink land J ≈ 3×10⁻⁵ (reconciled with the triangle-area reading). The build. (Sections 3.5, 4)
- **The forced half-twist** — why the geometry makes matter spin-½ rather than us noting it fits. (Section 3.4)
- **η_B magnitude** — only the existence and sign of the asymmetry are the cant; the size is a separate quantity (a current 2σ lead, 2α⁴/3π). (Section 3.5)

**RETRACTED (v0.2):**
- The "one −1 does all three" unification (v0.1 Section 4). Corrected to three distinct operations (Section 4).
- The (−1)ⁿ charge-sign holonomy as a *mechanism* — it is a repackaging of the assignment; the mechanism is T2470's weight-sign.

**RELATED, BANKED ELSEWHERE (the static / Phase-1 side):** the cosmological cluster — Ω_Λ = c₃/(c₃+χ) = 13/19, Ω_DM/Ω_b = rank⁴/N_c = 16/3, n_s = 1 − n_C/N_max — three parameters on three Chern channels of the same Q⁵ spectrum whose odd cohomology are these generations. (Reported separately; the static reading of the same manifold.)

---

## 8. The construction that decides

Two constructions were at stake. One is now decided; the other is set up and buildable.

**Masses — decided (miss).** The generation states were built on D_IV⁵ with the correct type-IV norm; the gen-2 radius resolved target-innocently (≈ 0.25), and the odd-degree ladder still could not fit — the fitting rungs are fractional and demand a ground rung the set {1,3,5} forbids. Named as a structural miss. The mass mechanism is replaced (membrane refraction), not tuned.

**CP — set up, not yet run.** The up-down structure is now sourced (the Pin(2) doublet on the non-orientable Möbius locus, T1949/T2138 proved), so the kink is buildable. Two independent handles must agree — the Pin(2)-twist size and the triangle-area reading — and both must land **J ≈ 3×10⁻⁵.** The *existence* of the twist is forced by the locus's non-orientability (the same source as parity violation); the *magnitude* is the remaining test. The disciplines are fixed in advance: the locus and its winding numbers pinned to source (FK/Hua), no fitting.

The pattern of the decider is the framework behaving as an honest theory: the spine (charge via T2470, spin, CPT, the source-pinned geometry) hardened; the odd-degree mass ladder was pruned cleanly; CP awaits one number against a sourced structure. Nothing is being tuned — each branch is being made to derive or named as a miss.

---

## Appendix: notation and the five integers

rank = 2, N_c = 3, n_C = 5, C₂ = 6, g = 7; N_max = N_c³·n_C + rank = 137. Domain D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)], rank 2, complex dimension 5, Shilov boundary (S⁴ × S¹)/ℤ₂, compact dual Q⁵ = SO(7)/[SO(5)×SO(2)]. Bergman kernel diverges toward the Shilov boundary (the "poles"). Type IV = the spin-factor Jordan/Clifford domain (the spinor is native).

---

*v0.2, 2026-07-10. Drafted by Keeper as the honestly-tiered framework record; built with Casey (the mechanism), Lyra (the type-IV norm and the mass verdict), Elie (the blind degrees, the odd-n_C spin holonomy, and the sourced Pin(2)/Möbius CP structure), Grace (the drive alphabet, and the T2470 charge-sign correction that walked back the v0.1 over-merge). Corrections from decider-day are in the changelog at the top, all in the honest direction: charge grounded on proved T2470, the "one −1" unification retracted, the mass ladder named a structural miss, CP's up-down structure sourced. This is a framework, not a completed derivation; Section 7 is the honest ledger and Section 8 is what remains.*
