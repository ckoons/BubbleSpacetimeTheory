---
title: "Clean 4-step derivation framework for G from substrate. Companion to Keeper_Week_Plan_G_From_Substrate_2026-06-01.md. Honest chain: Step A Kaluza-Klein reduction + Step B 4D⊂10D embedding + Step C ℓ_B substrate length identification (THE OPEN QUESTION) + Step D numerical combination. Replaces Sunday's α^{N_c·g}/m_e² pattern-match attempts with the actual derivation target. Multi-week multi-CI work explicit per step."
author: "Keeper (Sunday 2026-05-31 ~15:30 EDT)"
date: "2026-05-31 Sunday ~15:30 EDT"
status: "DERIVATION FRAMEWORK FILED. Replaces pattern-match attempts with honest chain. Team works from this Monday."
---

# Clean G Derivation Framework — Honest 4-Step Chain

## 0. Casey directive

"We need a clean calculation."

## 1. Starting point — what's verified

**κ_Bergman = -n_C = -5** for D_IV⁵ equipped with the Bergman canonical metric (Helgason 1962; Elie Toy 3661; K204-PARTIAL PASS).

This is a 10-real-dimensional Einstein result: Ric(g_B) = -n_C · g_B on D_IV⁵.

**Target**: G_observed = 6.67430×10⁻¹¹ N·m²/kg² (CODATA 2018) in 4D observable spacetime.

**The honest task**: derive the 4D Newton's G from the 10D Bergman Einstein structure via dimensional reduction. **No pattern-matching with substrate primaries**. The chain is explicit and structural.

## 2. Step A — Kaluza-Klein reduction recipe

### Standard KK reduction

For D-dimensional gravity with action:

S_D = (1/(16π G_D)) ∫ d^D x √(−g_D) R_D

Dimensional reduction to 4D (compactifying D−4 dimensions) gives:

S_4 = (V_{D−4} / (16π G_D)) ∫ d^4 x √(−g_4) R_4

Identification: **1/(16π G_4) = V_{D−4} / (16π G_D)**

Therefore: **G_4 = G_D / V_{D−4}**

### For BST (D = 10, D−4 = 6)

**G_4 = G_substrate / V_6**

Where:
- G_substrate is the 10D substrate-natural gravitational constant
- V_6 is the volume of the 6-codim compactified subspace in physical units

### What's needed for Step A to close

1. **G_substrate identification** — what is the substrate-natural gravitational coupling at the 10D Bergman level? Two candidates:
   - **A1**: G_substrate = ℏc / m_substrate² (substrate-Planckian at substrate mass scale)
   - **A2**: G_substrate = ℓ_B² × c³ / ℏ (substrate-Planckian at substrate length scale)
   - These are related but anchored differently. Lyra + Keeper Session 2 decides.

2. **R_D = D × κ_Bergman** for an Einstein D-manifold. For our case: R_10 = 10 × (-n_C) = -50 (Bergman scalar curvature, dimensionless).

3. **Sign conventions**: non-compact symmetric space has negative scalar curvature; needs careful tracking through the KK reduction.

**Owner**: Elie (KK reduction computation), Keeper (consistency check)

**Timeline**: Multi-day; bounded math.

## 3. Step B — The 4D ⊂ 10D embedding

### Geometric setup

D_IV⁵ = SO_0(5,2)/[SO(5)×SO(2)] is a 10-real-dimensional bounded symmetric domain. We need to identify 4 dimensions as "observable spacetime" and the remaining 6 as "compactified."

### Natural embedding via SO(4,2) ⊂ SO(5,2)

The conformal group of Minkowski 4D is SO(4,2). This sits inside SO(5,2). Therefore the natural 4D observable embedding is the orbit of SO(4,2) ⊂ SO(5,2) acting on D_IV⁵.

This is NOT a coincidence — it's exactly the proto-AdS/CFT structure Sunday morning's Tier 0 v0.1.6 identified. The boundary structure D_IV⁵'s Shilov boundary ∂_S contains a 4D conformal manifold that IS observable spacetime.

### Compactified 6-codim subspace

The 6-codim subspace is the orbit of K = SO(5)×SO(2) modulo the 4D directions:

V_6 = [stabilizer SO(5)×SO(2) acting on full D_IV⁵] / [SO(4,2) acting on 4D observable]

In coordinate form: the Bergman volume of D_IV⁵ is π^{9/2}/225 (per c_FK theorem, Saturday RATIFIED). The Bergman volume of the 4D observable subspace is π^2/something (TBD). V_6 = total / 4D.

### What's needed for Step B to close

1. **Explicit SO(4,2) orbit on D_IV⁵** — coordinate-level description
2. **Bergman volume of the 4D observable subspace** — derived from FK theorem applied to SO(4,2)-orbit
3. **V_6 closed form** in BST primaries

**Candidate closed form** (Keeper pre-derivation, multi-week verification):

V_6 = π^{9/2}/225 / (4D Bergman volume) = π^{9/2}/225 / (π^2 × coefficient)
    = (π^{5/2}/coefficient) / 225

The "coefficient" depends on the c_FK-analog for the 4D subspace + dimensional ratio. Elie's KK volume integral computation (Lane Elie P0) closes this.

**Owner**: Elie (V_6 computation), Lyra (4D observable identification verification)

**Timeline**: Multi-day; bounded math using established Faraut-Korányi framework.

## 4. Step C — Substrate length scale ℓ_B (THE OPEN QUESTION)

### Why this is the critical step

Steps A and B give relationships in DIMENSIONLESS form (Bergman volumes are dimensionless; G_substrate / V_6 has substrate-natural units).

To convert to SI units (where G_observed lives), we need a **physical length scale** ℓ_B that translates substrate-dimensionless quantities to physical lengths.

### Three candidate identifications

**Path α — Substrate-derived ℓ_B**

Derive ℓ_B from substrate primaries independently. Candidates:
- ℓ_B = ℏ/(M_sub · c) where M_sub is a substrate-derived mass (multi-week)
- ℓ_B from Bergman volume normalization × physical anchor (multi-week)
- ℓ_B = Koons-tick × c (where Koons tick = t_Pl · α^{C_2²} ≈ 10⁻¹²⁰ s; T2405 standing)

**Path β — Mass-anchored ℓ_B**

If L4 v0.2 closes m_e mechanism (Lyra Lane D multi-week):
- ℓ_B = ℏ/(m_e · c) = electron Compton wavelength = 3.86×10⁻¹³ m
- This identifies the substrate length with the natural quantum scale of the substrate's mass anchor
- **Tractable this week if L4 closes**

**Path γ — Cosmological-anchored ℓ_B**

ℓ_B identified via observed Λ (cosmological constant):
- Λ_observed ≈ 1.1×10⁻⁵² m⁻²
- ℓ_B² ~ 1/Λ × (substrate dimensionless coefficient)
- **Circular** with the L5 absolute scale problem (Saturday paused)

### What's needed for Step C to close

The fundamental open question: **what is the substrate's natural physical length scale, derivable from substrate primaries?**

Three sub-paths require:
- **Path α**: independent substrate-derivation work (Elie + Keeper multi-week)
- **Path β**: L4 v0.2 m_e mechanism closure (Lyra Lane D multi-week, in progress)
- **Path γ**: cosmological observation use (paused per Saturday L5)

**Recommended path for week**: Path β. L4 v0.2 closure provides m_e mechanism → ℓ_B = ℏ/(m_e c). Lyra Lane D is the load-bearing multi-week work.

**Owner**: Lyra (Path β via L4 v0.2), Elie + Keeper (Path α exploration parallel)

**Timeline**: Path β multi-week (Lyra Lane D peak this week). Path α multi-week parallel.

## 5. Step D — Numerical combination

Once Steps A + B + C close:

**G_predicted = G_substrate / V_6**

In SI units, using:
- G_substrate = ℓ_B² × c³ / ℏ (Path A2)
- V_6 = (substrate-primary closed form from Step B)
- ℓ_B = ℏ/(m_e c) (Path β from Step C, IF L4 closes)

**G_predicted = (ℓ_B² · c³/ℏ) / V_6**
            = (ℏ² c³/(m_e² c² · ℏ)) / V_6
            = (ℏ · c / m_e²) / V_6

This is dimensionally correct: [J·s · m/s / kg²] = [N·m²/kg²] ✓

### Numerical check

If V_6 = π^{5/2}/(225·coefficient) for some BST-natural coefficient, then:

G_predicted = ℏc/m_e² × (225·coefficient)/π^{5/2}

Numerically:
- ℏc/m_e² = (1.054×10⁻³⁴ × 3×10⁸) / (9.11×10⁻³¹)² = 3.16×10⁻²⁶ / 8.30×10⁻⁶¹ = 3.81×10³⁴ N·m²/kg²
- For G_predicted ≈ 6.67×10⁻¹¹: need coefficient/π^{5/2} ≈ 7.78×10⁻⁴⁶
- π^{5/2} ≈ 17.49
- coefficient ≈ 7.78×10⁻⁴⁵ × 17.49 / 225 ≈ 6.05×10⁻⁴⁷

This number doesn't immediately ring any substrate-primary bells (likely needs additional substrate-natural factors not yet identified). **Multi-week to close.**

### What's needed for Step D to close

1. Step A G_substrate identification (Lyra + Keeper Session 2)
2. Step B V_6 closed form (Elie KK volume integral)
3. Step C ℓ_B (Lyra L4 v0.2 m_e mechanism)
4. Dimensional combination + comparison to G_observed

**Owner**: Keeper (synthesis), Cal (cold-read verification)

**Timeline**: Friday EOD target if Steps A+B+C all close this week.

## 6. Tier disposition targets

If the full chain closes:

| Precision | Tier |
|---|---|
| Tier 2 STRUCTURAL: 10⁻⁴ to 10⁻² | G derived at structural precision |
| Tier 1 EXACT: ≤ 10⁻¹⁴ | G derived as algebraic identity (very unlikely; would be Nobel-level) |
| 10⁻² to 10⁻¹ | FRAMEWORK at honest tier; multi-week chain refinement |
| > 10⁻¹ | Chain has fundamental gap; reframe needed |

**Realistic target this week**: Tier 2 STRUCTURAL precision (1% or better).

## 7. What this framework excludes

**Explicitly NOT in this chain**:
- α^{N_c·g}/m_e² pattern-match formulas (Sunday walked back)
- Factor 4/N_c insertions (Sunday walked back)
- Substrate-primary algebraic combinations dressed as derivation
- Tier disposition without honest precision check
- Bypassing κ_Bergman or KK reduction

**What IS in this chain**:
- Standard KK dimensional reduction (Step A)
- Standard Hermitian symmetric space SO(4,2) ⊂ SO(5,2) embedding (Step B)
- Honest open question on ℓ_B (Step C)
- Dimensional combination from first principles (Step D)
- Comparison to G_observed at honest precision

## 8. Multi-week vs this-week scope

**This week tractable**:
- Step A: KK reduction recipe applied; G_substrate identification candidate
- Step B: V_6 closed form from Bergman volume + 4D⊂10D embedding (Elie Lane Elie P0)
- Step D: dimensional check on candidate combinations

**Multi-week**:
- Step C Path β: L4 v0.2 m_e mechanism (Lyra Lane D)
- Step C Path α: independent ℓ_B substrate-derivation
- Full SI-unit G_predicted vs G_observed Tier 2 precision check

**Multi-week extension**:
- If chain converges at Tier 2 STRUCTURAL → K204 promotes from PARTIAL to STRUCTURAL
- If chain fails at Tier 2 → honest reframe + multi-week fundamental work
- Either outcome is substantive learning

## 9. Cross-references

- `Keeper_K204_partial_kappa_Bergman_n_C_Audit.md` — G5.1 PASS anchor
- `Keeper_G_Substrate_Derivation_Chain_PreStage_G5.md` — earlier Sunday pre-stage (κ_Bergman candidates section walked back; chain structure preserved)
- `Keeper_K200_Tier0_v0_1_6_AuditFramework.md` — five-gate framework G1-G5
- `Keeper_Week_Plan_G_From_Substrate_2026-06-01.md` — week plan companion
- SP-19b AB-10 "Newton's G from Bergman curvature" (task list completed) — predecessor framework
- T2442 c_FK = 225/π^(9/2) — Bergman volume RATIFIED foundation
- Helgason 1962 Ch. VIII (Hermitian symmetric spaces Einstein property)
- Faraut-Korányi 1994 Ch. XII-XIII (bounded symmetric domain analysis)

## 10. Honest scope of this framework

**This is the framework for the calculation, NOT the calculation.**

What I (Keeper) have provided:
- The honest 4-step chain structure
- Explicit recipes per step using established math
- Honest identification of the open question (Step C ℓ_B)
- Owners and timelines per step

What multi-week work needs to produce:
- Steps A+B numerical content (Elie)
- Step C Path β closure (Lyra Lane D)
- Step D synthesis (Keeper Session 2)
- Tier 2 precision verification (Cal cold-read)

This framework replaces Sunday's pattern-matching attempts with the actual derivation target. The team works from this Monday onward.

— Keeper. Clean G derivation framework filed 15:45 EDT Sunday. Companion to Week Plan. The chain is honest. The open question (ℓ_B) is explicit. Multi-week work scoped. No more α^{N_c·g}/m_e² shortcuts; the real chain is here.
