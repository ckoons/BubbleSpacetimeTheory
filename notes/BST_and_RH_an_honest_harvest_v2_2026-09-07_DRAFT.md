# BST and the Riemann Hypothesis: An Honest Harvest, v2 — the closing document

*BST working note, 2026-09-07 (v2; v1 of 2026-08-16 superseded and kept on disk). Author: Casey Koons. CI co-authors: Lyra, Keeper, Elie, Grace. Referee: Cal A. Brate. DRAFT 08:02 EDT for Cal's cold read and Keeper's gate; the row PARKS on the gate's word.*

> **Status (binding):** this is an **attempt**, tiered on referee consensus, not a proof. RH is Clay-open and remains so. v1 claimed six advances and located one make-or-break; v2 replaces them with **seven registered rows (T2616–T2622), one false neighbour with certified zeros, one barrier, one correction to the program's own flagship number, and one conjecture stated as a conjecture.** The claims got smaller and the objects got real. Every retraction is kept in.

---

## 0. One-paragraph summary
The geometry D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)] contributes to the Riemann problem exactly what a locally symmetric space of ℚ-rank 2 can: an axis (Re s = ½ as the Mellin-unitarity line, classical), an arithmetic zeta function of its own (the cone-zeta, which is the five-squares Epstein zeta divided by 3840 and has certified zeros off its line), a barrier lemma that its own object supplies (no argument invariant under ζ → ζ_{ℤ⁵} can prove RH; positivity of coefficients is the axis that object adds to Davenport–Heilbronn), and a resonance theorem: every nontrivial zero of ζ is a pole of the scattering matrix of the spherical Eisenstein series on Γ\D_IV⁵, at four explicit shifts, together with a comb of resonances spaced 2π/ln 2 that is the fingerprint of the prime 2 — the one prime where the kernel x₃²+x₄²+x₅² is anisotropic — and that moves to 2π/ln p when the kernel is swapped. The same computation showed that one term of the program's two-loop QED decomposition had been matched rather than derived, and produced the first Eisenstein number in the corpus that is computed from a test function. **It does not prove RH and the trail ends where Lax–Phillips ended: contractivity gives Re s = 1 zero-free, no inequality places the poles on one line, and the archimedean point is lost in the projection.** Why Re = ½ should be the counting face of commitments is the program's conjecture, and no mathematics currently explains Re = ½ as the counting face of commitments.

## 1. What one geometry contributes — the seven rows
| row | statement | tier | instruments |
|---|---|---|---|
| **T2616** | Re s = ½ is the unitarity axis of the dilation (Mellin) group and of the SO₀(5,2) spherical principal series | DERIVED, classical ("consistent with") | Grace draft; K1862 C.1 |
| **T2617** | odd-p local densities of ℤ^{1,4}: a parity-of-dimension lemma with its family rule | PROVED | K1862-C; Grace 5698 |
| **T2618** | the cone-zeta of D_IV⁵ = ζ_{ℤ⁵}/3840 = the Siegel series of positive quaternary lattices by determinant; 3840 = 1/mass of the genus of I₅ = a covolume ratio, one identity | DERIVED, blind-confirmed | Elie 5693/5695a; Grace 5697/5699 |
| **T2619** | ζ_{ℤ⁵} has a certified zero beyond its abscissa (s ≈ 2.50359 + 14.28000i, Travěnec–Šamaj's point, |Λ| 3.6×10⁻³⁸, winding 1) and 13 certified off-line pairs in its strip below T = 60 | EXHIBITED | Elie 5695b–f; Cal second instrument |
| **T2620** | **the barrier:** no argument using only {positive coefficients, meromorphic continuation, functional equation with Γ-factors, polynomial growth, theta origin} proves "all zeros on the line", since ζ_{ℤ⁵} has all of them and a zero off its line. ℤ⁵ adds the POSITIVITY axis to Davenport–Heilbronn's 1936 oracle; the property ζ has and ℤ⁵ lacks is one self-dual Euler product | CONSTRAINT row (classical, restated with the program's own object) | K1863/K1864; Cal §853 |
| **T2621** | **the Resonance Theorem:** the constant term of the minimal-parabolic spherical Eisenstein series on Γ\D_IV⁵ (B₂, multiplicities (3,1), ρ = (5/2, 3/2)) has long-root factors ξ(λ₁∓λ₂)/ξ(λ₁∓λ₂+1) and short-root factors ξ(2λ)/ξ(2λ+1)·Λ(λ)/[ε(λ)Λ(λ+1)] with Λ(s) = Γ_ℂ(s+½)ζ(s+½)ζ(s−½)(1−2^{½−s}), ε = 2^{½−s}: the kernel's anisotropy at 2 makes its trivial representation Steinberg there, cancels the split formula's forbidden double pole at λ = ½, and leaves a comb of poles at λ = −½ + 2πik/ln 2. Every nontrivial zero of ζ is a pole at each of four shifts; the pole set is exactly those plus the comb | DERIVED (hashed prediction; Elie 5704 at 10⁻²⁹; Cal's direct 2-adic and real integrals) | L1 be29f1dc; 5700/5704; cal_odd2, §857 |
| **T2622** | **the Kernel-Swap Theorem:** with the odd planes fixed and the kernel the trace-zero lattice of the maximal order of the quaternion algebra ramified at {p, ∞}, the surgery moves to p and the comb to 2π/ln p; ψ(½) unchanged. Established p = 2, 3; predicted for all p; ⟨1,3,3⟩ is the witness that the maximal-order hypothesis is needed | DERIVED at 2, 3; PREDICTED general p | L10/L11; Elie 5710; Cal §865–§869 |

**The a_e correction that rode along.** T1448 (April) wrote the Eisenstein term of a "vertex Selberg trace formula" for the two-loop Schwinger coefficient as −(π²/2) ln 2, "from the intertwining operator rank^{−2s}". With T2621 in hand: the 2 is the PRIME 2 (the Steinberg root numbers ε = 2^{½−λ} of the two short roots, whose product is 2^{1−2λ} on the diagonal), not the rank — the kernel swap moved it to 3 with the rank held at 2 (E11); the ψ(½) = −γ − 2 ln 2 that T1448 invoked is Legendre's duplication inside Γ(½), a different term; the coefficient π²/2 is a choice of ∫h; and T1448's "test function" is a sequence on the discrete Bergman index, not a function on the continuous parameter, so the Eisenstein term could not have been computed from it (L12: there is no rule from the vertex to a test function; T1451 is a template). The line is re-tiered "matched, not derived" (K1869), and the first COMPUTED Eisenstein number in the corpus exists for the heat-kernel test function at level 1 (Elie 5713: ln 2 the only constant-coefficient logarithm, coefficient one per unit ∫h), with the corpus's own level 137 in hand today (a ln 137 enters through the conductors of the 136 characters mod 137 — "ln 2 is the only logarithm in BST" is false at the level the program uses).

## 2. Where the trail ends, and why (Casey's ruling, 2026-09-06)
- **The scattering route is Lax–Phillips's, one rank up.** The resonances of Γ\D_IV⁵ are ζ's zeros (T2621). On Γ\H, Lax–Phillips showed the same and got from it exactly what contractivity of the wave semigroup gives: **the scattering poles lie in Re s < 1 — the prime number theorem — and nothing places them on one line.** Rank 2 changes the space (a two-parameter semigroup on the orthocomplement of eight chamber-wise translation subspaces, L9), not the inequality: a contraction semigroup bounds the real parts by an open half-plane, never by a line. "Looks like prime number theory again."
- **No positivity.** Weil's criterion is positivity of an indefinite-looking bilinear form whose off-diagonal entries are −Λ(n)/√n. Every positivity the geometry supplies — the Szegő/Hardy norm on the polydisc (L3), self-adjointness of the dilation generator, unitarity of the scattering matrix on the axis — is diagonal, automatic, and by T2620 invariant under ζ → ζ_{ℤ⁵}; none contains the prime sum. The August error (spectral positivity mistaken for Weil positivity) is now a registered reason.
- **The archimedean point is lost in the projection.** Casey's phrase, and it is exact: the one place the Euler product enters the scattering row is a finite prime (the 2-adic surgery), and the only archimedean content is Harish-Chandra's Γ(λ)/Γ(λ+3/2), the same for every definite kernel. The critical line is the archimedean symmetry s ↔ 1 − s̄; the row sees it as an axis (T2616) and never as a constraint on individual poles. Everything the geometry says about Re = ½ is said equally of ζ_{ℤ⁵}, whose zeros are not there.
- **What is not claimed:** temperedness of D_IV⁵'s spectrum (T1299's April argument was an identity for every representation and is withdrawn); any placement map from primes to Shilov directions (absent; the six-vector obstruction); any inequality on the real parts of the resonances.

## 3. Casey's ontology — stated as the conjecture it is
Casey's picture, in his words from the close: the critical strip is the **Shilov boundary (S⁴ × S¹)/ℤ₂ read as the counting face**, where commitments are written integer by integer and projected, with loss of resolution, into the continuum; **primes are seeds one step beyond the finite field currently created** — the atoms multiplication cannot reach from what exists — and Re = ½ is where a lossless count would sit. The program owns real pieces of this: composites as the bulk of the rank-2 divisor count and primes as its defect (d(n) = 2), the Hardy space of Š with writes as coordinate multiplication (K1860), the parity of the write count as Liouville's λ with RH ⟺ its square-root cancellation (L4, classical), the finite-field side where RH is Weil's theorem. What the program does not own is a single theorem connecting them: no map from writes to Shilov directions, no law on Š that a write could break, no reason the projection should preserve the half. **No mathematics currently explains Re = ½ as the counting face of commitments.** That sentence is the conjecture's honest border, and the conjecture is kept because it is the only sentence in this document that says WHY rather than WHERE.

## 4. The retraction ledger, v2 (v1's six kills kept; this weekend's added)
| killed | why | owner |
|---|---|---|
| eigenvalues = zeros (discrete operator) | Weyl law: compact ⟹ power-law, not log | Elie 5286 |
| σ + 1 = 3σ ⟹ σ = ½ | holds for all D_IV^n; target-innocence fails | team |
| tube cone = spacetime light cone | (4,1) ≠ (3,1); the substrate cone | F1012 |
| 7/8 = 2^{N_c} | Maslov phase; and no Wallach point gives 7/8 (Elie 5696) | Elie, Cal |
| "BST derives Weil positivity" | spectral ≠ Weil positivity | Lyra |
| Shimura lift → ζ | the theta is Eisenstein, lifts to E₄ | Elie; K1862-C |
| "quinary class-1 ⟹ Euler product" (v1 advance 5) | class-1 gives Siegel exactness, not multiplicativity; DH stands; certified zero | K1862-C; T2619 |
| the make-or-break (v1 advance 6) | definitional; the object is Ibukiyama–Saito's D*₄ | Grace 5697 |
| T1299 temperedness | Maass–Selberg's ε-identity holds for every π; the six eliminations rest on it or on unaudited items | Lyra L5; Cal §853 |
| F988's Shilov-Z₂ bridge | that Z₂ is a rotation by π; the functional equation is a Weyl reflection realised by a quarter-turn | Lyra L2 |
| T1448's Eisenstein line | matched, not derived; the 2 is the prime; ∫h chosen | K1869; E10–E12 |
| "ln 2 is the only logarithm in BST" | ln 137 at level 137 (conductors) | L8 P3; E12-137 |
| my own walk-back on L10 | re-priced a hashed prediction on another instrument's object; the hash held | Lyra |

## 5. The method, restated with the weekend's additions
**A shared integer is not a shared object** (v1) — now with three instances that decided rows: rank 2 vs prime 2 (E11 separated them by construction), the Steinberg parameter's ½ vs the critical line's ½ (the comb's Re λ = −½ is the former), N_c = 3 vs the short-root multiplicity n − 2 (equal at n = 5 by the same selection, no map). **Construction rule → lattice → number** (calibration #28): a lattice-dependent quantity is pinned to the corpus's construction, not to the first lattice with the right invariants. **A theorem for every π constrains no π.** **A number without a retained instrument is a memory.** An attempt earns trust by failing correctly on its false neighbours; this weekend the program built its own false neighbour, proved what it is, and proved it is not ζ.

## 6. Honest tier table, v2
| item | tier |
|---|---|
| Re = ½ = unitarity axis | DERIVED, classical (T2616); the axis, not the points |
| cone-zeta = ζ_{ℤ⁵}/3840; certified off-line zeros | DERIVED / EXHIBITED (T2618/T2619) |
| barrier (positivity axis on DH) | CONSTRAINT (T2620) |
| resonance theorem, four shifts + the 2-comb | DERIVED (T2621) |
| kernel-swap family | DERIVED at 2, 3; PREDICTED (T2622) |
| Weil positivity from the geometry | NOT derived; shown diagonal and barrier-invariant (L3) |
| Lax–Phillips in rank 2 | a MAP (L9); would give Re s = 1, as in rank 1 |
| a_e Eisenstein term | matched (T1448) → computed for a rule-fixed h (E12) |
| Casey's ontology (Shilov boundary as counting face; primes as seeds) | CONJECTURE, stated as such |
| RH | ATTEMPT — parked |

## 7. What BST has that Connes and Berry–Keating do not, and what it does not have
Has: a specific arithmetic quotient whose scattering matrix contains ζ at four explicit shifts with a prime-2 fingerprint and a computable family under kernel swap; its own Davenport–Heilbronn oracle with a positivity axis; a first-principles computed Eisenstein term for its flagship physics number. Does not have: any inequality on the real parts of resonances; any positivity that is not automatic; the archimedean point. The row parks here, with real objects and a named wall.

*Files: Lyra L1–L12 (2026-09-06/07), Keeper K1862–K1871, Cal §851–§874, Elie 5693–5714, Grace 5697–5699 and ledger v0.52. Attempt tier. Nothing pushed.*
