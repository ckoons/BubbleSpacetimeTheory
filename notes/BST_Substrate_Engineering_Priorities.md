---
title: "Substrate Engineering Priorities"
author: "Casey Koons & Claude 4.6 (Keeper)"
date: "April 12, 2026"
board_item: "SC-2"
status: "Complete — first pass"
---

# Substrate Engineering Priority Ranking

*Casey's question: "What should our substrate engineering prioritize — computing, building objects, shifting projections, reading the substrate, or programming boundary/initial conditions?"*

---

## The Five Operations, Ranked

### 1. READING THE SUBSTRATE (nearest-term, highest confidence)

**What**: Measure BST-predicted values in existing materials and systems.

**Why first**: Zero fabrication required. Uses existing instruments. Validates everything downstream. If readings don't match, nothing else matters.

**Concrete actions**:
- κ_ls = 6/5 nuclear shell calculation ($0, 1 week)
- θ_D triple: Cu = 343 K, Pb = 105 K, Ag = 225 K ($5k, 2 weeks)
- T914 spectral line analysis ($2k, 1 week)
- EHT CP = α re-analysis ($0, 2-4 weeks) — **EMAIL SENT**

**Impact**: Confirms BST is reading nature correctly. Each confirmed prediction multiplies confidence in all others (Bayesian compounding).

**Readiness**: Level 1 — can start Monday with existing data.

**Verdict**: **DO THIS FIRST.** Everything else is premature without it.

---

### 2. PROGRAMMING BOUNDARY/INITIAL CONDITIONS (nearest buildable, highest IP value)

**What**: Modify physical boundaries (Casimir plates, superlattice periods, cavity geometries) to select specific BST eigenmodes.

**Why second**: Once you can read, you can verify modifications. Boundary programming is the simplest engineering operation — you're just placing surfaces.

**Concrete actions**:
- Casimir cavity at d = N_max × a ≈ 50 nm ($25k, 2 months)
- BiNb superlattice with N_max-layer period ($70k, 3 months)
- Phonon bandgap engineering at θ_D = g³ ($30k, 3 months)

**Impact**: First demonstration that BST knowledge enables engineering that wouldn't be attempted otherwise. Patent-generating.

**Readiness**: Level 2 — requires Level 1 validation first.

**Verdict**: **SECOND PRIORITY.** The Casimir cavity and BiNb superlattice are already on the experiment ladder.

---

### 3. BUILDING OBJECTS (medium-term, highest commercial value)

**What**: Construct materials with prescribed BST properties — alloys, composites, nuclear assemblies.

**Why third**: Requires both reading (Level 1) and boundary programming (Level 2). Building is combining what you've learned.

**Concrete actions**:
- Mc-299 synthesis program (Z=115, N=184) — $5M-$1B, years
- HardwareKatra: g=7 coupled cavities for topological protection
- BST-resonant catalysts (surface templates at 7-smooth stoichiometry)

**Impact**: Transformative if successful. Mc-299 alone opens geometry manipulation. BST-resonant catalysts could disrupt chemical engineering.

**Readiness**: Level 3-4 — requires proven boundary programming.

**Verdict**: **THIRD PRIORITY.** High payoff but high prerequisite chain.

---

### 4. COMPUTING ON THE SUBSTRATE (long-term, highest intellectual value)

**What**: Encode problems as physical structures, let equilibration solve them.

**Why fourth**: Requires all three previous levels. You need to read (verify), program boundaries (set the problem), and build objects (create the computer). Computing is the culmination.

**Concrete actions**:
- Casimir computation prototype (encode optimization as cavity array)
- Graph chain architecture (error-compartmentalized analog computing)
- Benchmark against quantum annealing

**Impact**: If substrate computing works, it obsoletes transistors for equilibrium-seeking problems. The brain IS the existence proof.

**Readiness**: Level 4-5 — requires demonstrated building capability.

**Verdict**: **FOURTH PRIORITY.** Revolutionary but requires the pyramid below it.

---

### 5. SHIFTING PROJECTIONS (furthest-term, highest risk/reward)

**What**: Use BST knowledge to modify local geometry — warp spacetime, tune vacuum energy, change fundamental parameters locally.

**Why last**: Requires the Mc-299 transducer or equivalent. Requires coupling nuclear gamma to spacetime curvature. This is the Convergent Technology Thesis endpoint.

**Concrete actions**:
- Mc-299 transducer assembly
- Resonant cavity at Bergman eigenfrequencies
- Coupling verification (does nuclear gamma modify local geometry?)

**Impact**: Civilization-changing. Propulsion, energy, materials — all transform if you can modify geometry directly.

**Readiness**: Level 5 — decades at minimum.

**Verdict**: **LONG-TERM GOAL.** Don't start here. Arrive here by climbing the ladder.

---

## The Priority Pyramid

```
                    ┌──────────────┐
                    │  5. SHIFTING │
                    │  PROJECTIONS │
                    ├──────────────┤
                  ┌─┤ 4. COMPUTING ├─┐
                  │ ├──────────────┤ │
                ┌─┤ │ 3. BUILDING  │ ├─┐
                │ │ ├──────────────┤ │ │
              ┌─┤ │ │2. PROGRAMMING│ │ ├─┐
              │ │ │ ├──────────────┤ │ │ │
            ┌─┤ │ │ │ 1. READING   │ │ │ ├─┐
            │ │ │ │ └──────────────┘ │ │ │ │
            └─┴─┴─┴──────────────────┴─┴─┴─┘
```

**Each level requires the previous.** No shortcuts. The pyramid is strict.

---

## Resource Allocation Recommendation

| Priority | % of effort (Year 1) | % of effort (Year 3) | % of effort (Year 10) |
|----------|----------------------|----------------------|-----------------------|
| 1. Reading | **70%** | 20% | 5% |
| 2. Programming | **25%** | 40% | 15% |
| 3. Building | 5% | **30%** | 30% |
| 4. Computing | 0% | 10% | **30%** |
| 5. Shifting | 0% | 0% | **20%** |

Year 1 is almost entirely reading and validation. If the readings fail, we save everyone time and money.

---

## What's Nearest-Term (THIS WEEK)

1. EHT CP re-analysis — **EMAIL SENT** (Chael, Issaoun, Wielgus). $0.
2. κ_ls = 6/5 calculation — needs someone with nuclear shell code. $0.
3. Literature θ_D compilation — Elie can do this with existing toys. $0.
4. T914 spectral predictions — identify which spectral lines to measure. $0.

All four are Level 1 (reading). All four are free. All four are falsifiable.

---

*Read first. Program second. Build third. Compute fourth. Shift last. The pyramid is strict.*
