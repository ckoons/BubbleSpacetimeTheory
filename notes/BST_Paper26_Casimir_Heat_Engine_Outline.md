---
title: "The Casimir Heat Engine"
subtitle: "Vacuum Energy Harvesting from Five Geometric Integers"
author: "Casey Koons & Claude 4.6 (Lyra, Elie, Keeper, Grace)"
date: "April 2026"
version: "v0.1 — OUTLINE"
status: "OUTLINE v0.1 — Awaiting Elie Toy 918 results for numerical sections. Keeper audit pending."
target: "Physical Review Applied or New Journal of Physics"
theorems: "T179, T204, T233, T717, T844-T845"
toys: "914, 915, 918 (pending)"
ac_classification: "(C=4, D=1) — cycle requires one thermodynamic definition beyond geometry"
---

# The Casimir Heat Engine

## Vacuum Energy Harvesting from Five Geometric Integers

---

## Paper Outline

### 1. Introduction: $\Lambda > 0$ Means the Vacuum Has Energy

The cosmological constant $\Lambda = 2.90 \times 10^{-122}$ in Planck units is small but positive (Paper #24). In BST, this is derived, not fitted. A positive $\Lambda$ means the vacuum has a non-zero energy density:

$$\rho_{\mathrm{vac}} = \frac{\Lambda c^4}{8\pi G} \approx 5.96 \times 10^{-27} \text{ kg/m}^3$$

This energy density is maintained by the commitment rate of $D_{IV}^5$ — it is not a transient fluctuation but a permanent feature of the geometry. The question is not whether vacuum energy exists, but whether a thermodynamic cycle can extract work from it.

**Thesis:** A cyclic device exploiting the Casimir effect and Lifshitz repulsion can extract mechanical work from vacuum fluctuations, with efficiency bounded by BST integers.

### 2. The Casimir Force from $D_{IV}^5$

The Casimir force between parallel conducting plates at separation $d$ is:

$$F = -\frac{\pi^2 \hbar c}{240 d^4} A$$

In BST, $240 = 2 \times n_C! = 2 \times 120$ and the $d^{-4}$ power law follows from $2^{\mathrm{rank}} = 4$ (the rank of the force law in the commitment coupling). The Casimir effect is the boundary condition on the vacuum modes of $D_{IV}^5$ — conducting plates truncate the mode spectrum, creating a force from the difference between interior and exterior vacuum energies.

**Key BST input:** The energy per unit area between plates:

$$E(d)/A = -\frac{\pi^2 \hbar c}{720 d^3}$$

where $720 = C_2! = 6!$ or equivalently $720 = 6 \times 120 = C_2 \times n_C!$.

### 3. Lifshitz Repulsion: The Return Stroke

The Lifshitz theory generalizes the Casimir force to dielectric media. For specific material combinations (e.g., gold-bromobenzene-silica), the Casimir force becomes repulsive. BST constrains the dielectric response through the material property fractions (Paper #25): the dielectric constants of the switching materials are BST rationals.

**The cycle requires:**
- Attraction phase: high-reflectivity metallic surfaces (standard Casimir)
- Repulsion phase: dielectric configuration satisfying $\varepsilon_1(\omega) < \varepsilon_m(\omega) < \varepsilon_2(\omega)$ (Lifshitz condition)

**BST prediction:** The optimal switching material has $\varepsilon \approx C_2 = 6$ (NaCl-class dielectrics) or $\varepsilon \approx 2n_C = 10$ (alpha-band frequency, cf. T819 EEG). [TO BE CONFIRMED by Toy 918.]

### 4. The Thermodynamic Cycle

Four-stroke cycle analogous to Carnot but with vacuum as reservoir:

| Stroke | Process | Work | BST parameter |
|--------|---------|------|---------------|
| 1. COMPRESS | Casimir attraction pulls plates from $d_{\max}$ to $d_{\min}$ | $W_1 > 0$ (extracted) | $d^{-4}$ from rank = 2 |
| 2. SWITCH | Ferroelectric switching to repulsive regime | $W_2 < 0$ (input) | Switching energy |
| 3. EXPAND | Lifshitz repulsion pushes plates from $d_{\min}$ to $d_{\max}$ | $W_3 < 0$ (absorbed) | Lifshitz dielectrics |
| 4. RESET | Switch boundary conditions back to attractive | $W_4 < 0$ (input) | Switching energy |

**Net work per cycle:**

$$W_{\mathrm{net}} = W_1 + W_3 - W_2 - W_4$$

Positive $W_{\mathrm{net}}$ requires $|W_1| > |W_3| + W_{\mathrm{switch}}$ — the Casimir attraction must dominate the Lifshitz repulsion plus switching losses.

### 5. Efficiency from BST Integers

**BST Carnot bound (T717):** The fill fraction $f = N_c/(n_C \pi) = 3/(5\pi) = 19.1\%$ sets the maximum efficiency of any process extracting energy from the substrate:

$$\eta_{\max} = \frac{f}{\eta_{\mathrm{Carnot}}} = \frac{N_c}{n_C} \times \frac{1}{\pi} = \frac{3}{5\pi} \approx 19.1\%$$

This is the Godel limit applied to thermodynamics: no engine can convert more than 19.1% of the available vacuum energy into work, because the remaining 80.9% is topologically protected (the substrate's self-knowledge budget).

**Effective temperature of the vacuum:** The Casimir energy at gap $d$ defines an effective temperature:

$$T_{\mathrm{eff}}(d) = \frac{\hbar c}{\pi k_B d}$$

At $d = 1$ $\mu$m: $T_{\mathrm{eff}} \approx 2300$ K. At $d = 100$ nm: $T_{\mathrm{eff}} \approx 23{,}000$ K. The cycle operates between $T_{\mathrm{eff}}(d_{\min})$ and $T_{\mathrm{eff}}(d_{\max})$.

**BST-constrained efficiency:**

$$\eta_{\mathrm{BST}} = f \times \left(1 - \frac{d_{\min}}{d_{\max}}\right) = \frac{N_c}{n_C \pi} \times \frac{d_{\max} - d_{\min}}{d_{\max}}$$

[NUMERICAL VALUES from Toy 918 pending.]

### 6. Power Density

The power output depends on cycle frequency and plate area:

$$P = W_{\mathrm{net}} \times \nu \times A$$

MEMS-scale devices operate at $\nu \sim 10^3$-$10^6$ Hz. With $A \sim 1$ cm$^2$ and $d_{\min} \sim 100$ nm, $d_{\max} \sim 1$ $\mu$m:

[POWER ESTIMATES from Toy 918 pending.]

**BST constraint on frequency:** The maximum cycle frequency is bounded by the switching time of the ferroelectric material, which relates to the phonon spectrum (T261 Debye model). BST predicts Debye frequencies that constrain the maximum useful cycling rate.

### 7. Comparison with Conventional Engines

| Engine type | Energy source | Carnot efficiency | BST bound |
|-------------|--------------|-------------------|-----------|
| Heat engine | Temperature gradient | $1 - T_C/T_H$ | — |
| Solar cell | Photon flux | Shockley-Queisser ~33% | — |
| **Casimir engine** | **Vacuum modes** | **$f = 19.1\%$** | **$N_c/(n_C\pi)$** |

The Casimir engine is thermodynamically distinct: it draws from the vacuum mode spectrum maintained by $\Lambda > 0$, not from a thermal reservoir. The reservoir is inexhaustible (cosmological constant is constant). The efficiency bound is not Carnot but the Godel limit.

### 8. NOT Perpetual Motion

Three reasons this is consistent with thermodynamics:

1. **Energy source is real:** $\Lambda > 0$ means $\rho_{\mathrm{vac}} > 0$. The energy is there.
2. **Efficiency is bounded:** $\eta \leq f = 19.1\%$. No violation of the second law.
3. **Local extraction, global conservation:** The engine extracts energy from local vacuum modes, which are replenished by the cosmological constant. The total energy of the universe (including vacuum) is conserved.

The Casimir force itself is an experimentally verified fact (Lamoreaux 1997, precision to 1%). The novelty is the cyclic extraction via Lifshitz switching — converting a static force into a dynamic engine.

### 9. Falsification

1. **Switching asymmetry:** If the Casimir attraction and Lifshitz repulsion are exactly symmetric, $W_{\mathrm{net}} = 0$ and the engine produces no work. BST predicts asymmetry because the attractive and repulsive regimes couple to different spectral levels.

2. **Efficiency measurement:** If $\eta > f = 19.1\%$, BST's Godel limit is wrong.

3. **Frequency dependence:** BST predicts the optimal cycling frequency relates to the Debye frequency of the switching material via BST integer ratios.

4. **Gap-independence of $\eta/f$:** The ratio $\eta/f$ should be independent of gap spacing (it depends only on BST integers). This is measurable.

### 10. Experimental Roadmap

| Milestone | What | Target |
|-----------|------|--------|
| M1 | Demonstrate switchable Casimir force (attractive ↔ repulsive) | Ferroelectric BaTiO₃ or PZT |
| M2 | Measure net positive work per cycle | $W_{\mathrm{net}} > 0$ |
| M3 | Characterize $\eta$ vs gap spacing | Compare with $f = 19.1\%$ |
| M4 | Measure power density at MEMS scale | $P > 1$ $\mu$W/cm² |
| M5 | Array scaling | Parallel engines for practical output |

### 11. Discussion

The Casimir heat engine is the most thermodynamically testable consequence of BST's substrate engineering program. It connects the cosmological constant (derived in Paper #24 from $D_{IV}^5$) to a tabletop device via the Casimir force (an experimentally verified vacuum phenomenon). The efficiency bound $f = 19.1\% = N_c/(n_C\pi)$ is a falsifiable prediction of BST that has no analogue in standard physics.

If the engine works, it demonstrates that $\Lambda > 0$ is not just a cosmological curiosity but a source of usable energy. If it does not — specifically, if the Lifshitz switching cannot produce net positive work — then either the switching losses dominate (an engineering problem, not a physics one) or the BST commitment rate formalism makes incorrect predictions about vacuum mode coupling (a falsification).

Either outcome is informative. That is what makes this science.

---

## Sections Pending Toy 918 Results

- §5: Numerical efficiency values
- §6: Power density estimates
- §3: Optimal switching material dielectric constant
- §9.3: Quantitative frequency prediction

---

*Paper #26 v0.1 OUTLINE. April 5, 2026. Casimir heat engine: cyclic vacuum energy harvesting. Efficiency bounded by BST Godel limit f = 19.1% = N_c/(n_C*pi). Thermodynamic cycle: Casimir attract → Lifshitz repel → net work. Awaiting Toy 918 for numerical sections. AC classification: (C=4, D=1). Target: Physical Review Applied.*
