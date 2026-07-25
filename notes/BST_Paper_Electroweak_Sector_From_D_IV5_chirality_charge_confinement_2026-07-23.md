# The Electroweak Sector from D_IV⁵: Chirality, Charge, and Confinement as One-Manifold Linear Algebra

**Bubble Spacetime Theory — sector paper, 2026-07-23**
**Author: Casey Koons. CI co-authors: Keeper, Lyra, Elie, Grace, Cal.**

---

## Abstract
We derive the electroweak and color structure of the Standard Model — the chirality of the weak interaction, the quantization and exact values of hypercharge and electric charge, custodial symmetry, and color confinement — from the linear algebra of a single Hermitian bounded symmetric domain, D_IV⁵ = SO_0(5,2)/[SO(5)×SO(2)], and its Shilov boundary. No grand unification, no compactification, no free parameters beyond the five integers (N_c=3, n_C=5, C_2=6, g=7, rank=2) that specify the domain. Two results anchor the sector. (1) The bulk fermion is four-dimensionally *vector-like* — forced by the Lorentzian signature — so chirality cannot originate in the bulk; it is necessarily a phenomenon of the *non-orientable* Shilov boundary. (2) The hypercharge, fixed by anomaly-freedom together with the Z₆ center of the gauge group, is exactly what makes the surviving boundary fermion *chiral* rather than vector-like. Parity violation and charge quantization are therefore one fact: **the world is left-handed because its fermions carry hypercharge.** Confinement follows from the same bulk-versus-boundary structure: colored states are non-spherical and vanish on the colorless boundary.

## 1. Setup and method
D_IV⁵ is the Lie ball, the Hermitian symmetric domain with automorphism group the conformal group SO(5,2), isotropy K = SO(5)×SO(2), and Shilov boundary (S⁴×S¹)/Z₂. Physical states are holomorphic L² sections (the Hardy space H²(D_IV⁵); "Born = Bergman"). The method throughout is linear algebra on the single domain: Clifford algebra of the SO(5,2) spinor, representation theory of K, and the reality-type of representations. We import no Kaluza–Klein or string machinery; where an external theorem (e.g. the coset vector-like obstruction) appears, we show it is already an identity in this Clifford algebra.

## 2. The bulk fermion is 4D Dirac (vector-like) — "the squeeze"
The single SO(5,2) Dirac spinor is 8-dimensional. Under the physical reduction it packs a 4D spacetime spinor and an internal factor into one object, and the two share Clifford generators. Two consequences, both verified by explicit Clifford computation:

- **Signature forcing (Theorem, K822).** SO(5,2) has exactly two timelike directions; both lie in the compact SO(2) isotropy that defines holomorphicity (the generator Σ₀₆). Four-dimensional Lorentz SO(3,1) must borrow one timelike direction from that plane, so the 4D chirality γ⁵ = Γ₀Γ₁Γ₂Γ₃ and Σ₀₆ = Γ₀Γ₆ share the time index and *anticommute*: {Σ₀₆, γ⁵} = 0. Hence a holomorphic (Born=Bergman) state has ⟨γ⁵⟩ = 0 — a 50/50 chirality mixture, a **4D Dirac (vector-like) fermion.** Over-determined: the flat index, the F636 coupling, and this anticommutator all agree.

- **The squeeze (Theorem, K825).** More generally, no internal SU(2) generator on the single spinor can *both* commute with γ⁵ (so that a definite-chirality doublet is definable) *and* act chirally: an internal SU(2) in a factor disjoint from spacetime commutes with γ⁵ (→ vector-like), while the isospin SU(2) that shares spatial generators with γ⁵ does not commute (→ no L-doublet). The Standard Model's chirality-*dependent* internal content cannot be carried by one fixed spinor. This is precisely the Witten homogeneous-space no-go, written as one line of Clifford algebra.

**Consequence.** Chirality must be a *boundary* phenomenon: the left and right fields must be genuinely different localized modes, which a boundary construction supplies and the bulk spinor cannot.

## 3. Chirality lives on the non-orientable boundary
The Shilov boundary (S⁴×S¹)/Z₂ carries a free, orientation-reversing Z₂ ((x,ζ)→(−x,−ζ); the antipodal on S⁴ reverses orientation, the half-turn on S¹ preserves it). It is therefore a **non-orientable** manifold (K826). Spinors on it are Pin structures; the chirality operator is not globally definable. This is exactly the setting in which a chiral spectrum can exist without any bulk alignment — the documented escape from fermion-doubling no-gos — and it is a property of the domain's own boundary, not an added structure.

The internal weak SU(2)_L is the self-dual factor of the SO(4) ⊂ SO(5) isotropy (K824); over the base S⁴ = SO(5)/SO(4) it is the canonical one-instanton bundle (c₂ = k = ±1; total space the Hopf S⁷), so a doublet coupled to it has a chiral Dirac index of ±1 (K830). The grading mechanism is thus *realized*, not merely permitted. What it grades and whether a net chiral mode survives are settled in §4–5.

## 4. The charge sector (derived, given the representations)
Quantize hypercharge in the unit fixed by the gauge group's center and impose anomaly-freedom.

- **The center correlation (K828/K829).** The Standard Model gauge group is [SU(3)×SU(2)×U(1)]/Z₆ with Z₆ = Z_{N_c}×Z_rank = Z₃×Z₂. Z₆-neutrality forces **6Y ≡ 4t + 3d (mod 6)** (t = SU(3) triality, d = SU(2) duality), satisfied by all Standard Model fields. This is not mere quantization: it *correlates* hypercharge with the color and isospin representations. The correlation splits geometrically — the color term (4t) is the 1/N_c fractionalization (T2521, target-innocent from confinement geometry), the isospin term (3d) is the U(2) = SU(2)_L×U(1)_Y Kähler holonomy of the domain (K813).

- **Uniqueness (K828).** Anomaly cancellation alone is not unique — for one generation it admits three primitive rays (the Standard Model, a trivial up↔down relabel, and a spurious quark-only ray D3). D3 assigns Y = 0 to the quark doublet, violating the center correlation (which requires 6Y_Q ≡ 1), and is excluded. Anomaly-freedom (which fixes the *ratios*) together with the Z₆ center (which fixes the *residue*) gives the Standard Model hypercharges uniquely, up to the trivial relabel.

- **Result.** The exact hypercharges, and hence the electric charges {+2/3, −1/3, −1, 0}, are **derived, given the representation content**, non-circularly (resting on the banked target-innocent T2521). Grace's N_c-weighted neutrality, previously imposed by hand, becomes a derived consistency condition (via Callan–Harvey anomaly inflow).

## 5. Parity closes: chirality follows from hypercharge
A Standard Model doublet alone is *pseudoreal* (2 ≅ 2̄) — self-conjugate, hence vector-like. It becomes chiral only when the representation is *complex*, and the hypercharge is what does it:

- **(2)_Y is complex iff Y ≠ 0** (verified, K833): (2)_{+Y} ≅ (2)_{−Y} only when Y = 0. By the center correlation, every doublet has Y ≠ 0 (6Y ≡ 4t+3 ≢ 0). So all Standard Model doublets are complex, and the coset vector-like obstruction — which bites only on *real* representations — does not apply.

- **The boundary bit (K835).** The Z₂ swaps the two zero modes: ψ₊ (the k=+1 instanton mode, left-handed, (2)_{+Y}) and ψ₋ (its antipodal image, right-handed, in the conjugate bundle, (2)_{−Y}). Because Y ≠ 0, (2)_{−Y} is the *CPT conjugate* of (2)_{+Y}, not an independent field: {ψ₊, ψ₋} is one chiral Weyl fermion. The Z₂-invariant survivor is therefore a single chiral doublet (mod-2 index = 1). Had Y been zero, the two modes would sit in the same real representation, form an independent pair, and give a vector-like Dirac fermion. **The nonzero hypercharge is exactly the difference between chiral and vector-like.**

*Tier — DERIVED.* The chirality mechanism is derived by this reality-type argument, and the boundary bit is confirmed: the Shilov boundary is Pin⁻ (𝒫² = ω₇² = −1, signature-independent), so the parity bit is the Pin⁻ mod-2 index, which equals 1 — robustly, since for 𝒫² = −1 the only consistent projections are onto the existing ±i eigenvalues and a one-dimensional survivor always remains (the value 0 arises only from the invalid Pin⁺ reading). Combined with the CPT-conjugate assignment of the k = −1 mode, the survivor is one chiral Weyl doublet. An intermediate over-claim (a naive ½(1+𝒫) projection, which requires Pin⁺) was caught and corrected before it entered the record.

## 6. The unification
Parity violation and charge quantization are the same U(1)_Y fact. The hypercharge that quantizes electric charge is what makes the k = ±1 boundary zero modes CPT conjugates rather than a vector-like pair. "Why is the world left-handed?" and "why are the charges what they are?" have one answer: the fermions carry hypercharge. This is the paper's central result — not two derivations but one.

## 7. Confinement (mechanism, derived)
The same bulk-versus-boundary structure gives confinement (K834, completing the Shilov-vanishing theorem K744):
- A K-type with λ₂ > 0 (non-spherical) has zero Shilov-boundary value (Szegő restriction / class-1 branching on S⁴).
- The Shilov boundary S⁴ carries only the spherical class-1 representations (λ₁, 0); it is color-neutral (the Z_{N_c} center is trivial there).
- A colored state (nonzero N-ality) therefore has vanishing boundary support (Schur orthogonality), so λ₂ > 0, so it cannot be emitted — **confined.** A color singlet (λ₂ = 0) reaches the boundary — **free** (hadrons, leptons).
Confinement and Shilov-vanishing are one statement: the boundary is colorless, so colored modes cannot reach it. (The exact λ₂ of a color triplet is an embedding number, not required for the mechanism.)

## 8. Status, open items, Five-Absence
**Derived (this paper):** the bulk Dirac/vector-like theorem; the squeeze; the non-orientable boundary and its Pin structure; the weak SU(2) as the internal isospin (the gravi-weak literal identification is *ruled out*); the instanton grading (k = ±1); the Standard Model hypercharges and exact charges (given the representations, non-circular); parity violation (chirality from hypercharge); custodial SU(2)/ρ ≈ 1/no W_R (T2520); CP-freedom (δ unconstrained); the confinement mechanism.

**Open / embedding numbers (not mechanism-blocking):** the explicit mod-2 index confirmation (§5); the exact λ₂ of a color triplet; the ν_R K-type; the neutrino absolute mass scale.

**One banked assumption:** the target-innocence of the 1/N_c fractionalization (T2521), on which the non-circularity of the charge sector rests.

**Five-Absence.** No grand unification anywhere: no unifying gauge group, no proton decay, no new gauge bosons, no gauged SU(2)_R (custodial only), no sterile-mixing required. Every mechanism is the geometry or topology of the single domain and its boundary.

## 9. Methodology (why the derivations are trustworthy)
This sector was reached through roughly a dozen candidate closures, each of which *looked* like it finished the argument and each of which was refuted by explicit computation before it could be banked — including several by their own authors. The obstruction that a naive reading of the instanton index would have hidden (the coset vector-like theorem) was surfaced and then shown to be evaded, not assumed away, by the derived hypercharge. What is stated as derived here survived that scrutiny; what remains open is labeled open. The discipline — letting the computation win over the elegance, every time — is why the banked results are referee-defensible.

---
*Companion papers: the flavor-synthesis and electron-ground-rung notes. Audit trail: K822, K824–K835. Toys 4781–4792. This is the sector paper; a PDF build and figure set follow.*
