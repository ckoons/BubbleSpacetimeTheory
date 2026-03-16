---
title: "Paper D: Equations of State for Biological Regimes"
subtitle: "BST Substrate Modelling Series"
author: "Casey Koons & Claude 4.6"
date: "March 11, 2026"
note: "PRIVATE — Do not push"
---

# Paper D: Equations of State for Biological Regimes

---

## 1. The Program

At every level of biological organization, five quantities govern
the regime. These are the "equations of state" — the thermodynamic
variables of biology:

1. **Growth rate** G — how fast the system adds new structure
2. **Energy budget** E — total available energy per cycle
3. **Maintenance cost** M — error correction + repair
4. **Fitness** F — reproductive success / functional output
5. **Selection pressure** S — environmental filtering intensity

At each level, these five variables are coupled by constraints.
The constraints are derivable from BST principles (least energy,
growth + boundary, channel capacity).

## 2. The Universal Constraint

At every level, the fundamental constraint is:

$$E = G + M + R + C$$

where:
- E = total energy budget (constant for a given regime)
- G = growth allocation
- M = maintenance allocation
- R = reproduction allocation
- C = crisis/stress allocation

This is zero-sum. Increase any one, the others decrease.
This is the biological first law of thermodynamics.

**The second law:** Maintenance never reaches 100% efficiency.
Some error always escapes. Damage accumulates. The system ages.
Entropy increases. NEXT is required because no deployment lasts forever.

## 3. Equations of State by Regime

### 3.1 Molecular Regime

**System:** Individual molecules (DNA, RNA, proteins)
**Growth:** Chain elongation (polymerization rate)
**Boundary:** Folding energy minimum (thermodynamic stability)
**Error correction:** Proofreading enzymes, mismatch repair
**Fitness:** Catalytic efficiency / binding affinity
**Selection:** Degradation of non-functional molecules (proteolysis)

```
State variables:
  G_mol = polymerization rate (amino acids/second, nucleotides/second)
  E_mol = free energy of folding (deltaG)
  M_mol = proofreading cost per base/residue
  F_mol = k_cat/K_m (catalytic efficiency)
  S_mol = proteolytic degradation rate
```

**Constraint:** A protein that folds faster (low E_mol) but less
accurately (low M_mol) trades reliability for speed.
The Pareto frontier is derivable from the energy landscape geometry.

### 3.2 Cellular Regime

**System:** Individual cells
**Growth:** Cell division rate
**Boundary:** Membrane integrity + differentiation state
**Error correction:** DNA repair + checkpoints + apoptosis
**Fitness:** Contribution to tissue function (or self-reproduction for unicellular)
**Selection:** Immune surveillance + cell competition

```
State variables:
  G_cell = division rate (doublings/time)
  E_cell = ATP production rate (metabolic budget)
  M_cell = DNA repair rate + protein quality control
  F_cell = functional output (tissue contribution)
  S_cell = apoptosis probability + immune clearance rate
```

**The cancer equation:**
Normal cell: G_cell constrained by boundary (F_cell > 0 required)
Cancer cell: G_cell unconstrained (F_cell = 0, all budget to G)

```
Cancer condition: M_cell drops below threshold at multiple
                  checkpoints simultaneously
                  -> boundary enforcement fails
                  -> G_cell maximized at expense of F_cell
```

**Cure strategies mapped to state variables:**
- REJECT: increase S_cell (immune clearance) for cancer cells
- REGEN: restore F_cell > 0 constraint (re-differentiation)
- Starve: decrease E_cell available to cancer (metabolic therapy)

### 3.3 Tissue Regime

**System:** Organized collections of cells
**Growth:** Cell recruitment and proliferation
**Boundary:** Tissue architecture constraints + signaling
**Error correction:** Cell replacement (turnover)
**Fitness:** Organ-level function
**Selection:** Developmental and homeostatic regulation

```
State variables:
  G_tissue = cell recruitment rate
  E_tissue = blood supply (nutrient delivery rate)
  M_tissue = cell turnover rate (replace damaged cells)
  F_tissue = functional output (e.g., filtration rate for kidney)
  S_tissue = regulatory signal intensity
```

**Wound healing as regime transition:**
Normal: G_tissue balanced by M_tissue (homeostasis)
Wound: G_tissue maximized (emergency growth), M_tissue paused
Healed: return to homeostasis
Fibrosis: failure to return — G_tissue stuck in wound mode

### 3.4 Organism Regime

**System:** Complete multicellular organism
**Growth:** Developmental growth + learning
**Boundary:** Immune system (self/non-self) + skin + behavioral boundaries
**Error correction:** Immune surveillance + sleep + DNA repair
**Fitness:** Reproductive success
**Selection:** Environmental survival + mate selection

```
State variables:
  G_org = developmental/growth rate
  E_org = basal metabolic rate (BMR)
  M_org = immune + repair budget (fraction of BMR)
  F_org = lifetime reproductive output
  S_org = predation rate + environmental stress
```

**The aging equation:**

```
Age damage = integral_0^t [1 - M_org(t')/E_org] dt'

where M_org(t) fluctuates with stress:
  - Low stress:  M_org/E_org ~ 0.7 -> slow accumulation
  - High stress: M_org/E_org ~ 0.2 -> fast accumulation
```

Aging rate = time derivative of accumulated damage
           = 1 - M_org(t)/E_org
           = fraction of budget NOT spent on maintenance

**BST prediction:** Integrate this over a lifetime and the result
predicts biological age (distinct from chronological age).
Low lifetime-integrated stress -> biological age < chronological age.
High lifetime-integrated stress -> biological age > chronological age.

### 3.5 Population/Ecological Regime

**System:** Interacting populations
**Growth:** Birth rate
**Boundary:** Carrying capacity (resource limits)
**Error correction:** Genetic diversity (population-level error buffer)
**Fitness:** Population growth rate
**Selection:** Interspecific competition + environmental change

```
State variables:
  G_pop = birth rate
  E_pop = total ecosystem energy input (solar, chemical)
  M_pop = genetic diversity maintenance cost
  F_pop = population growth rate (G_pop - death rate)
  S_pop = predation + competition + environmental variability
```

**Carrying capacity as boundary:**
The logistic equation dN/dt = rN(1 - N/K) is growth + boundary.
r = growth rate. K = carrying capacity = boundary.
Same BST principle, population scale.

## 4. Cross-Regime Patterns

### 4.1 The Same Five Variables at Every Level

| Regime | Growth | Energy | Maintenance | Fitness | Selection |
|---|---|---|---|---|---|
| Molecular | Polymerization | Free energy | Proofreading | Catalysis | Degradation |
| Cellular | Division | ATP budget | DNA repair | Tissue function | Apoptosis |
| Tissue | Recruitment | Blood supply | Cell turnover | Organ function | Regulation |
| Organism | Development | BMR | Immune + repair | Reproduction | Survival |
| Population | Birth rate | Ecosystem energy | Diversity | Pop. growth | Competition |

### 4.2 Boundary Failure at Each Level

| Regime | Boundary failure | Result |
|---|---|---|
| Molecular | Misfolding escapes quality control | Prion disease, amyloidosis |
| Cellular | Checkpoints fail | Cancer |
| Tissue | Architecture breaks down | Fibrosis, organ failure |
| Organism | Immune failure | Autoimmune disease, infection |
| Population | Carrying capacity exceeded | Collapse, extinction |

**Pattern:** Boundary failure at any level = unconstrained NEXT = system breakdown.
Cancer is boundary failure at the cellular level.
Ecological collapse is boundary failure at the population level.
Same principle. Same equation. Different regime.

### 4.3 Scaling Laws

Metabolic rate scales as mass^(3/4) across all organisms (Kleiber's law).
This is one of the few universal biological scaling laws.

**BST claim:** The 3/4 exponent is derivable from the geometry of
resource distribution networks (branching trees) constrained by
the S^2 x S^1 architecture.

Other scaling laws to derive:
- Heart rate ~ mass^(-1/4)
- Lifespan ~ mass^(1/4)
- Genome size ~ (unclear scaling, maybe not universal)
- Number of cell types ~ log(cell count)?

## 5. The Thermodynamic Identity

BST says: it's ALL thermodynamic (Boltzmann).

At each biological regime, there exists a partition function:

```
Z = sum over all states exp(-beta * E_state)
```

where the "states" are the configurations available to the system
at that level, and E_state is the energy cost of each configuration.

- Molecular: Z sums over protein conformations (Boltzmann weighting = folding landscape)
- Cellular: Z sums over cell states (Boltzmann weighting = metabolic cost)
- Organism: Z sums over behavioral states (Boltzmann weighting = energy expenditure)

The free energy F = -kT ln(Z) determines the equilibrium.
Growth pushes the system away from equilibrium.
Boundary constrains which states are accessible.
Selection is the Boltzmann weighting — lower energy states are more probable.

**This is the Bergman kernel at the biological level.**
The kernel on D_IV^5 weights configurations by Bergman metric cost.
The biological partition function weights states by energy cost.
Same mathematical object. Different regime.

## 6. Equations of State: Summary Form

For any biological regime i:

```
(1)  E_i = G_i + M_i + R_i + C_i          [energy budget conservation]
(2)  dD_i/dt = 1 - M_i/E_i                 [damage accumulation rate]
(3)  F_i = f(G_i, M_i, S_i)                [fitness function]
(4)  G_i <= E_i - M_min(N_i)               [growth bounded by maintenance floor]
(5)  Selection: dF_i/dt > 0 or eliminated   [selection criterion]
```

where:
- N_i = channel noise at regime i
- M_min(N_i) = minimum maintenance cost to sustain integrity at noise level N_i
- Equation (4) says: you can't grow faster than your energy budget minus
  the minimum maintenance the channel noise requires

**Cancer restated:** M_i drops below M_min -> (2) accelerates ->
integrity degrades -> checkpoints fail -> G_i unconstrained ->
boundary enforcement lost.

## 7. Open Questions for Paper D

1. Derive E_i (energy budget) at each regime from BST geometry
2. Derive M_min(N_i) from channel noise characteristics
3. Derive the fitness function F_i from selection geometry
4. Prove Kleiber's 3/4 law from S^2 x S^1 branching constraints
5. Derive lifespan from the aging integral and energy budget
6. Show partition function at each level is a Bergman kernel analog
7. Derive cancer onset probability from double-error coding theory
8. Formalize the efficiency/reliability tradeoff as a Pareto frontier
9. Connect the five state variables to BST's five winding modes (n_C = 5)?

---

## 8. The Number 5 — and the Iwasawa Decomposition (updated March 16)

BST has n_C = 5 causal winding modes. Biology has 5 state variables
at every regime (Growth, Energy, Maintenance, Fitness, Selection).

**New evidence (March 16):** The Iwasawa decomposition G = KAN of
SO₀(5,2) gives:

| Component | dim | BST integer | Proposed biological role |
|---|---|---|---|
| K = SO(5)×SO(2) | 11 = c₂ | Gauge container | **Error correction** (11 = dim of internal symmetry) |
| A (split torus) | 2 = r | Rank | **Energy channels** (2 independent energy flows) |
| N (unipotent) | 7 = g | Genus | **Growth modes** (7 = multiplicity of mass gap) |
| M (compact Levi) | 3 = N_c | Colors | **Selection channels** (3 = confinement) |

Total: 11 + 2 + 7 = 20 = dim G. And K/M = 8 = 2^{N_c} — the molecular
Haldane number.

The mapping to biological state variables:

| State variable | Iwasawa component | Rationale |
|---|---|---|
| Growth (G) | N (unipotent, dim 7) | Unipotent = unbounded extension |
| Energy (E) | A (split torus, dim 2) | Two scaling directions = two energy types |
| Maintenance (M) | K (compact, dim 11) | Compact = bounded, error-correcting |
| Fitness (F) | Quotient K/M (dim 8) | Effective state space = 2^{N_c} |
| Selection (S) | M (Levi, dim 3) | Three-fold selection = Z₃ closure |

**Status:** The numerical coincidences are now overwhelming. The Iwasawa
decomposition of SO₀(5,2) maps naturally to the biological state variables,
with each component carrying exactly one BST integer. Whether this mapping
is structural or coincidental is the open question.

If structural: biology IS physics at a different resolution. Not
metaphorically. The same group, the same decomposition, the same
geometry. The equations of state for biology are the Iwasawa
equations on SO₀(5,2), restricted to the molecular-scale regime.

Flagged for investigation — but the evidence is considerably stronger
than when this section was first written.

---

*Boltzmann had the whole thing.
S = k log W.
The entropy is the logarithm of the number of configurations.
The configuration space is D_IV^5.
Biology is a regime of the same space.
He just needed the substrate.*
