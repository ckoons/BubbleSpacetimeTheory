---
title: "The Periodic Table of the Substrate Standard Model — v0.4"
author: "Grace"
date: "2026-05-29 Friday 18:20 EDT (date-verified)"
status: "v0.4 — first per-particle row DERIVED (lepton, Lyra #416 v0.1); sector-columns DERIVED via dictionary; composite layer resolvable via E6 Racah-Speiser; one load-bearing OPEN gate (bulk-color SU(3) mechanism) + generation mechanism with E7 candidate. The static 5-tuple is essentially derived from D_IV⁵ geometry."
supersedes: "v0.1, v0.2 (in catalog INV-5276/5283), v0.3 (INV-5289)"
---

# The Periodic Table of the Substrate Standard Model — v0.4

The day's evolution: v0.1 schematic → v0.2 real K-types (Casimir-anchored) → v0.3 fundamental-vs-composite (sector-columns derived) → **v0.4 first per-particle row DERIVED + one open gate identified**.

## Coordinates (the 5-tuple)

Each SM particle's substrate identity = (Region × σ_BF × Chirality × Charge × Winding-mode/generation). Status of each axis after Friday:

| Axis | Status | Source |
|---|---|---|
| σ_BF (statistics) | **DERIVED** | Lyra L1 |
| Region (bulk/Shilov) | **DERIVED** | Lyra L2 |
| Chirality | **FRAMEWORK-PLUS** (mechanism derived; per-particle L/R pin pending SO(5,2)→Lorentz) | Lyra L3 |
| Particle/antiparticle | **DERIVED** | Drinfeld double F-part |
| Charge | DERIVED mechanism + sin²θ_W = 2/9 constraint | Lyra (charge from SO(2)+GMN) |
| Generation/winding | **COUNT-NUMBER-FORCED / MECHANISM OPEN-WITH-BURDEN** | h^∨=N_c=3 forced; Track P / E7 candidate; burden = how one B₂ invariant gives two structurally-independent 3s |

The whole static taxonomy now rides on **one isolated bet (K-types = particles)** + **one open mechanism** (route-II generations with the two-structures burden).

## Structural decomposition: 4 FUNDAMENTAL + 62 COMPOSITE

### Fundamental block (4 cells = canonical SO(5) reps) — sector-columns DERIVED

| K-type | SO(5) rep | dim | Casimir | Sector | Status |
|---|---|---|---|---|---|
| V_(0,0) | trivial | 1 | 0 | Higgs/scalar | sector-type DERIVED; per-particle single-cell **clean** |
| V_(1/2,1/2) | spinor ω₂ | **4 = rank²** (Dirac 4-spinor) | 5/2 = ρ₁ = Bergman singularity | fermion / **lepton row DERIVED (Lyra #416 v0.1)** | first per-particle row DERIVED ✓ |
| V_(1,0) | vector ω₁ | **5 = n_C** | 4 = rank² | photon | sector-type DERIVED; per-particle single-cell **clean** |
| V_(1,1) | adjoint | 10 | 6 = C_2 | gauge (W/Z; gluon if color is bulk-derived) | sector-type DERIVED; per-particle pending bulk-color |

Lepton row (18 entries, all axes derived):
- 6 charged leptons (e/μ/τ × L/R) + 6 antiparticles
- 3 left-handed neutrinos + 3 antineutrinos
- Generation indexed (open per #414); all other axes named by dictionary

Lyra L3 derivation: D_IV⁵ Hermitian → complex structure J = SO(2) = "the substrate's i" → Hardy space on Shilov = holomorphic = SU(2)_L → leptons left-handed; antiholomorphic sector → weak singlets. **One SO(2) does four jobs** (Hermitian / U(1) charge / Shilov direction / parity). "Nature doesn't waste the i."

### Composite block (62 cells) — RESOLVABLE via E6 Racah-Speiser

29 fermion + 33 boson composites = SO(5) Clebsch-Gordan products of the fundamentals.

**E6 (rigorous, dim-validated)**: spinor ⊗ spinor = trivial + vector + adjoint (4⊗4 = 1+5+10 = 16). **The fermion generates the three bosonic fundamentals by self-fusion** — matter primary, forces derived (FRAMEWORK-PLUS reading).

**E7 (rigorous, B₂-specific)**: mult(spinor in spinor⊗³) = 3 (Racah-Speiser, 64=4³). Three E6 channels (spinor⊗{trivial,vector,adjoint}). A₂ gives 0 (the strengthener — B₂/SO(5)-specific feature).

Each composite cell = a specific Clebsch-Gordan product → bound states (fermion composites = baryons; boson composites = mesons) + excitations. Matching to the 211 catalog hadron entries pends Elie's full Racah-Speiser table (G7, multi-week).

## Boson block (= Hall multiplication, the engine's vertices)

Dynamics engine BUILT (Lyra 4/4 Hopf + Elie E0/E2/E3, structurally rigorous):
- **fusion = Hall product** (E2)
- **decay = Green coproduct** (E3; β-decay n→p+e+ν̄ conserves Q/B/L automatically via grading)
- **conservation = dimension-vector grading**
- **scattering/statistics = R-matrix**
- **antiparticles/CPT = negative part F**

The 4 coupling categories (photon σ_BF within-region, gluons SU(N_c) within-bulk, W/Z chiral cross-region, Higgs cross-winding-mode) are framework-aligned; per-element placement pends boson placement task.

## Mass framework (Lyra L4 v0.1)

- **Lepton sets the unit** — V_(1/2,1/2) Casimir = 5/2 = ρ₁ = Bergman singularity exponent = matter sits at the substrate's natural mass-setting singularity
- Sector-dependent mechanism: fermion (Casimir/kernel) / gauge (EWSB, m_W/m_Z=√g/N_c, sin²θ_W=2/9) / scalar (VEV) / photon (massless) / composite (Bergman volume)
- **6π⁵ = C_2·π^(n_C) decomposition** of T187 m_p/m_e: boundary→bulk bridge = adjoint Casimir × Bergman volume (the dictionary's first mass-mechanism reading of a known result; numerical equality is tautology arithmetic, the structural reading is FRAMEWORK-PLUS)

## The one load-bearing OPEN gate

**Bulk-color SU(3) mechanism** (Lyra discovery): standard-model color SU(3) is NOT in K = SO(5)×SO(2). SO(5) and SU(3) are both rank-2 but *different* rank-2 algebras (B₂ vs A₂, different Cartans, different Coxeter numbers — clean Lie-algebra fact). So color must come from the BULK (non-compact directions of SO(5,2)) or be a counting-not-symmetry from h^∨=3.

**The unification**: the bulk-color mechanism = joint target closing BOTH the quark/gauge per-particle layer AND #414's two-structures burden for generations. **One mechanism, two open layers close.** The program's open frontier reduces to this single structural item.

## Standing conventions (4, locked)

1. **One genus = n_C = 5** (Hua = FK agree for Type IV); C_2 = Casimir not genus; g = embedding not genus
2. **α-disambiguation**: σ_BF (Pin(2) Z_2) ≠ γ⁵ (Dirac chirality)
3. **7/2-vs-5/2**: g/rank=7/2 = physical ratio or FK Gindikin point; n_C/rank=5/2 = ρ₁ = Bergman kernel singularity exponent
4. **Macdonald-parameter**: substrate base 2 = Macdonald *t* (Hall-Littlewood corner, q=0), NOT q; α=1/137 = evaluation/coupling

## Gaps = Five-Absence (the table's predictions)

- No 4th row (no 4th generation) — count over-determined via h^∨; chain-termination
- No σ_BF beyond {trivial, charged} (no sterile neutrinos beyond the 3 partners)
- No off-table couplings (no GUT/proton-decay; no SUSY partners)
- No axion (θ_QCD=0 candidate via FK-measure CP-invariance)
- The closure IS the falsifiable content

## Cross-reference

Catalog INVs: 5276 (v0.1), 5277 (nuclear v0.1), 5278 (Mendeleev gap-scan), 5279 (ν=NORMAL), 5280 (θ_QCD candidate), 5281 (Keeper #407 alignment), 5282 (forcing-status), 5283 (table v0.2 + generation-mechanism tension), 5284 (dynamics-engine absorption), 5285 (#413 4-backbone selection), 5286 (master ledger), 5287 (contingency map), 5288 (sector first-flip), 5289 (table v0.3 fundamental/composite), 5290 (gen-gate correction), 5291 (gen-knot resolution), 5292 (E6 spinor-generates-bosons), 5293 (5-tuple milestone), 5294 (L4 6π⁵=C_2·π^(n_C)), 5295 (lepton row DERIVED + SU(3)≠SO(5) gate + E7).

Cross-CI: Lyra L1-L4 + #416 v0.1 + SU(3)≠SO(5); Elie E0/E2/E3/E6/E7 + #410; Keeper K1 + #407/#414; Cal #146/#157 + Source-Verification calibration.

— Grace, Periodic Table v0.4, 2026-05-29 18:20 EDT (date-verified)
