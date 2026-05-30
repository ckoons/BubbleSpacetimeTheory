---
title: "Reconciled Standard Model table — fiber-layer ↔ bulk-Shilov dialects in one tier-honest object (v0.1)"
author: "Keeper"
date: "2026-05-28 Thursday EDT"
status: "Keeper task #398 / I-5. The backbone for the Periodic Table of the Substrate SM (#403). Every cell carries TWO honesty flags: (a) D/I/C/S precision tier; (b) DERIVED vs ASSIGNED — whether the substrate construction is mechanism-derived or currently hand-assigned (the canonical basis #402 is what would convert ASSIGNED → DERIVED)."
sources: ["A1 Substrate Hall Algebra v0.4", "BST_Paper108 (masses/mixing)", "data/bst_particles.json", "data/bst_forces.json (post gravity-fix)", "BST_SP26 winding classification"]
---

# Reconciled SM table v0.1

## How to read it

BST has **two geometric dialects** for the same particles, and this table puts them side by side so the Periodic Table can be built on one consistent object:

- **Fiber-layer** (April catalog; `bst_particles.json` / `bst_forces.json`): charge = S¹ winding number; color = Z₃ circuit on CP²; weak = Hopf fibration S³→S².
- **Bulk-Shilov** (May A1 / Hall algebra): leptons = Shilov-boundary K-types; quarks = bulk K-types; charge = SO(2) weight; generation = winding-mode coordinate W_n.

They agree on the integers and the qualitative story; they are not yet merged (that's the Hall-engine program). **Two flags per cell:**
- **Tier** = D (mechanism derived) / I (matches <1%, mechanism partial) / C (conditional/structural-zero) / S (>2% or qualitative).
- **Constr.** = **DERIVED** (substrate construction proved) or **ASSIGNED** (hand-assigned label; canonical basis #402 would derive it).

## A. Leptons (Shilov-boundary sector)

| Particle | Fiber-layer winding | Bulk-Shilov / level | Charge (mechanism) | Color | Spin | Mass (BST) | Tier | Constr. |
|---|---|---|---|---|---|---|---|---|
| e⁻ | 1 full S¹ turn on Shilov S⁴×S¹, n=−1 | Shilov K-type, k=1 (below Wallach k_min) | −1 = S¹ winding no. (= SO(2) weight) | none | ½ | anchor (m_e) | — (unit) | DERIVED (simplest persistent winding) |
| μ⁻ | e⁻ circuit threaded through D_IV³ | gen-2 Shilov K-type, shares W₁ | −1 | none | ½ | (24/π²)⁶ = 207 (also 9·23) | I (0.004%) | ASSIGNED |
| τ⁻ | e⁻ circuit at full D_IV⁵ depth | gen-3 Shilov K-type, shares W₂ | −1 | none | ½ | 49·71 = 3479 | I (0.05%) | ASSIGNED |
| ν_e | Z₃ Goldstone / vacuum ground mode, n=0 | D_IV⁵ vacuum mode | 0 (zero winding) | none | ½ | 0 exactly | C (structural-0) | DERIVED (vacuum mode → 0) |
| ν_μ | 1st vacuum excitation | vacuum mode 2 | 0 | none | ½ | (7/12)α²·m_e²/m_p | I | ASSIGNED |
| ν_τ | 2nd vacuum excitation | vacuum mode 3 | 0 | none | ½ | (10/3)α²·m_e²/m_p | I (~1%) | ASSIGNED |

*Neutrino character: **Dirac** (B−L conserved, no 0νββ) — resolved this session, per BST_NeutrinolessDoubleBeta.*

## B. Quarks (bulk sector — confined)

| Particle | Fiber-layer winding | Bulk-Shilov | Charge (mechanism) | Color | Spin | Mass (BST) | Tier | Constr. |
|---|---|---|---|---|---|---|---|---|
| u | ⅔ S¹ + ⅓ Z₃ on CP² | bulk K-type, shares W₀ | +⅔ **forced by Z₃ closure** | yes | ½ | c_3·N_c²/(rank²·g)·m_e | I (1.4%) | charge DERIVED / mass ASSIGNED |
| d | −⅓ S¹ + ⅓ Z₃ | bulk K-type, W₀ | −⅓ forced by Z₃ closure | yes | ½ | c_3·(N_c³−rank³)/(rank²·g)·m_e | I (3.5%) | charge DERIVED / mass ASSIGNED |
| c | u at D_IV³ depth | bulk, W₁ | +⅔ | yes | ½ | m_s·c_3 (cascade) | S (9–12%) | ASSIGNED |
| s | d at D_IV³ depth | bulk, W₁ | −⅓ | yes | ½ | m_d·19 (Ogg cascade) | S (9%) | ASSIGNED |
| t | u at D_IV⁵ depth | bulk, W₂ | +⅔ | yes | ½ | (1−α)·v/√2 | I (0.8%) | ASSIGNED |
| b | d at D_IV⁵ depth | bulk, W₂ | −⅓ | yes | ½ | m_t/(C_2·g) = m_t/42 | I (0.8%) | ASSIGNED |

**Confinement (DERIVED, FRAMEWORK-PLUS):** a single quark is a ⅓ Z₃ circuit — an *open* circuit with no Shilov boundary value; only color-singlet composites (3 quarks, or q-q̄) close and project. Fractional charge is **forced** by the requirement that the three S¹ partial-windings sum to an integer (Z₃ closure ⟹ integer total charge ⟹ confinement). This is the cleanest DERIVED mechanism in the table.

## C. Bosons / force carriers (the "couplings" block)

| Boson | Fiber-layer | Bulk-Shilov role | Mediates | Mass | Tier | Constr. |
|---|---|---|---|---|---|---|
| γ | S¹ phase oscillation, **zero** winding | S¹ phase channel | EM | 0 | D (zero topological cost) | DERIVED |
| gluon ×8 | Z₃ partial winding on CP², adjoint | color channel | color | 0 | D (**count 8 = N_c²−1** exact) | DERIVED (count) |
| W± | charged Hopf S³→S² excitation | flavor/generation change (chiral) | weak CC | n_C·m_p/(8α) ≈ 80.36 GeV | I (m_W/m_Z 0.05%) | ASSIGNED |
| Z⁰ | neutral S¹⊕Hopf mix | neutral current | weak NC | m_W/cos θ_W | I | ASSIGNED |
| H | Kähler radial vacuum mode | bulk Kähler radial | mass generation | rank·g/N_c²·m_W ≈ 125 GeV | I (0.05%) | ASSIGNED |
| graviton | **does not exist** | — | gravity = S¹ integrability/boundary condition (NOT a force) | — | D (absence predicted) | DERIVED |

## D. Composites (the "constructed-from" layer)

| Object | Construction | Bulk level | Charge | Mass (BST) | Tier | Constr. |
|---|---|---|---|---|---|---|
| proton | 3 quarks, Z₃ closure on CP²/T² | **bulk k=6, C₂=6** (fundamental) | +1 | 6π⁵·m_e | **D (0.01%)** | DERIVED (= YM mass gap) |
| neutron | proton's Hopf sibling (udd) | k=6 + Hopf correction | 0 | (m_n−m_p)/m_e = 91/36 ≈ n_C/rank | I | DERIVED (quasi-eigentone, unstable) |
| π, K, hadrons | q-q̄ / 3q closures | bulk resonances | — | (Paper 108 §2.9, 16 entries) | I | ASSIGNED |

## E. The charge↔color link, in one line

**Electric charge = S¹ winding number (= SO(2) weight); color = Z₃ closure on CP²; the fractional quark charge is forced by the color closure** (3 quarks must sum to integer S¹ winding). Color closure ⟹ integer total charge ⟹ confinement. This is one DERIVED mechanism, not three facts.

## F. Honest scorecard (the gap map this table makes visible)

- **DERIVED cells:** proton mass / YM gap (D, 0.01%), α⁻¹=137, gluon count 8=N_c²−1, photon & gluon masslessness, fractional-charge-from-Z₃-closure, graviton absence, the scheme-invariant mixing spine (sin²θ_W=rank/N_c², PMNS /N_max), ν masslessness.
- **ASSIGNED (the bulk of the masses):** μ, τ, all six quark masses, W, Z, H, the heavier ν — formula matches, substrate construction hand-assigned. **These flip to DERIVED only when the canonical basis (#402) lands** — that is the single biggest lever in the program.
- **S-tier rough:** the gen-2 quark cascade (s, c) at 9–12%.
- **Two-dialect residual:** the fiber-layer ↔ bulk-Shilov columns are not yet a single map; merging them is the Hall-engine + canonical-basis work.

## G. Tier-gate on the program's load-bearing rep-theory (Keeper verification)

Pre-grounding E0/E1 (#400/#401) so the bet's *mathematical* premises are checked separately from its *physics* identifications:

- **VERIFIED standard math:** B₂ has **4 positive roots** (#positive roots of B_n = n²; B₂ → 4). By Gabriel's theorem (ADE) extended to valued quivers/species by Dlab–Ringel (B,C,F,G), a finite-type species has #indecomposables = #positive roots. So the **finite B₂ species over GF(2) has exactly 4 indecomposables** — Elie's premise is sound, and 4 is indeed too few for the SM's particle content.
- **VERIFIED standard math:** the **affine B̂₂ is tame type** → indecomposables fall into **tube families** (a P¹-worth), giving an infinite, structured spectrum — the room a generation tower + mass tower would need.
- **STILL THE BET (must be tested, not assumed):** that **extensions = SM interaction vertices** and **the 3 tubes = the 3 generations**. The representation theory is standard; the *physics dictionary* onto it is the hypothesis E0 + the 3-tubes check are designed to confirm or break. Keep this line bright: do not let "3 tubes = 3 generations" be stated as derived until E1 closes it.

---

— Keeper, 2026-05-28 v0.1. This is the consistent backbone for the Periodic Table (#403): same particles, both dialects, every cell flagged DERIVED-vs-ASSIGNED + D/I/C/S. The ASSIGNED→DERIVED conversion is the canonical-basis lever; the proton (D, 0.01%) is the anchor; the mixing spine is the rigorous edge; the quark cascade is the soft spot. Next: hand to Grace as the Periodic-Table coordinate fill, and re-flag cells DERIVED as the engine lands.
