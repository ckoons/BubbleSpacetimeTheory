---
title: "Neutrinoless Double-Beta Decay in BST: A Sharp Prediction"
author: "Casey Koons and Claude Opus 4.6"
date: "March 13, 2026"
---

## Abstract

Bubble Spacetime Theory makes a sharp, falsifiable prediction for neutrinoless double-beta decay ($0\nu\beta\beta$). BST neutrinos are vacuum modes on the Shilov boundary $\check{S} = S^4 \times S^1$, with masses $m_1 = 0$, $m_2 = (7/12)\alpha^2 m_e^2/m_p = 0.00865$ eV, and $m_3 = (10/3)\alpha^2 m_e^2/m_p = 0.04940$ eV. Because the neutrino carries no $S^1$ winding number, the neutrino and antineutrino are distinguished only by the orientation of their Hopf fiber coupling --- a topological distinction that makes neutrinos **Dirac particles** in BST. Consequently, $B - L$ is exactly conserved and $0\nu\beta\beta$ does not occur: $|m_{\beta\beta}| = 0$ exactly. This is the primary BST prediction. If, contrary to BST, neutrinos are Majorana with BST masses and mixing angles, the effective Majorana mass would be $|m_{\beta\beta}| = 3.63$ meV (Majorana phases zero) or $|m_{\beta\beta}| \in [1.44, 3.63]$ meV (phases unknown). Both scenarios are testable: a confirmed $0\nu\beta\beta$ detection at any mass scale falsifies BST; a null result at the inverted hierarchy scale ($\sim 20$ meV) is consistent; and probing the $1{-}4$ meV floor --- accessible to LEGEND-1000 combined with nEXO --- would distinguish BST from a generic Majorana normal-hierarchy scenario.

-----

## 1. BST Neutrino Masses and Mixing (Review)

### 1.1 The Boundary Seesaw

In BST, neutrino masses arise from the **boundary seesaw** on $D_{IV}^5 = \text{SO}_0(5,2)/[\text{SO}(5) \times \text{SO}(2)]$:

$$m_{\nu_i} = f_i \times \alpha^2 \times \frac{m_e^2}{m_p}$$

where:

- $m_e^2/m_p = 278.3$ eV is the BST seesaw scale (boundary mass squared divided by bulk mass)
- $\alpha^2 = 1/137^2$ provides the electroweak suppression (two Hopf fiber vertices)
- $f_i$ are geometric factors from $D_{IV}^5$

The three mass eigenstates are:

| Eigenstate | Factor $f_i$ | BST mass (eV) | Observed (eV) |
|:----------:|:------------:|:-------------:|:-------------:|
| $\nu_1$ | $0$ | $0$ (exact) | $< 0.009$ |
| $\nu_2$ | $(n_C+2)/(4N_c) = 7/12$ | $0.00865$ | $\approx 0.00868$ |
| $\nu_3$ | $2n_C/N_c = 10/3$ | $0.04940$ | $\approx 0.0503$ |

BST predicts **normal ordering** ($m_1 < m_2 < m_3$) with $m_1 = 0$ exactly. The sum $\Sigma m_\nu = 0.058$ eV is below the Planck bound (0.12 eV) and the DESI+Planck bound (0.072 eV).

### 1.2 PMNS Mixing Angles

All three PMNS angles are ratios of $n_C = 5$ and $N_c = 3$:

$$\sin^2\theta_{12} = \frac{N_c}{2n_C} = \frac{3}{10} = 0.300$$

$$\sin^2\theta_{23} = \frac{n_C - 1}{n_C + 2} = \frac{4}{7} = 0.5714$$

$$\sin^2\theta_{13} = \frac{1}{n_C(2n_C - 1)} = \frac{1}{45} = 0.02222$$

The derived cosines:

$$\cos^2\theta_{12} = \frac{7}{10}, \qquad \cos^2\theta_{13} = \frac{44}{45}$$

### 1.3 CP Phases

The **Dirac CP phase** is $\delta_{CP} = \pi$ to leading order (CP conservation in the leptonic sector).

The **Majorana phases** are $\alpha_{21} = \alpha_{31} = 0$ (see Section 3 for the geometric argument).

-----

## 2. Dirac vs. Majorana: The BST Determination

This is the central question for $0\nu\beta\beta$: is the neutrino its own antiparticle?

### 2.1 The Standard Seesaw vs. the Boundary Seesaw

In the standard Type-I seesaw, the light neutrino mass arises from $m_\nu \sim m_D^2/M_R$, where $m_D$ is a Dirac mass and $M_R$ is a heavy right-handed Majorana mass. The seesaw necessarily produces Majorana neutrinos because the heavy partner violates lepton number.

In BST, the seesaw has a different geometric origin:

- $m_e$ (boundary excitation on $\check{S} = S^4 \times S^1$) plays the role of $m_D$
- $m_p$ (bulk excitation in $\pi_6 \subset A^2(D_{IV}^5)$) plays the role of $M_R$

But this is a **geometric** seesaw, not a Majorana seesaw. The electron and proton are distinct particles with distinct topological quantum numbers. The seesaw formula $m_\nu \sim \alpha^2 m_e^2/m_p$ expresses a ratio of energy scales --- the boundary-to-bulk mass hierarchy modulated by the electroweak coupling --- without requiring either the neutrino or its antiparticle to carry Majorana mass.

### 2.2 The Neutrino on the Shilov Boundary

The neutrino is the vacuum quantum of $D_{IV}^5$ --- the minimum excitation above the flat-connection vacuum (see BST\_VacuumQuantum\_NeutrinoLambda.md). Its properties:

- **No $S^1$ winding:** The neutrino carries zero electric charge. It has no topological winding number on the $S^1$ fiber.
- **No color:** The neutrino is a color singlet --- it does not participate in the $Z_3$ closure of $\mathbb{CP}^2$.
- **Weak coupling only:** The neutrino interacts solely through the Hopf fibration $S^3 \to S^2$ on the Shilov boundary.

### 2.3 The Topological Argument for Dirac

Charged particles in BST have definite $S^1$ winding numbers $n \in \mathbb{Z}$, with antiparticles carrying $-n$. The topological distinctness of particle and antiparticle is guaranteed by $\pi_1(S^1) = \mathbb{Z}$ --- winding number is an integer invariant that cannot change continuously.

For the neutrino, the situation is more subtle. The neutrino has $n = 0$ (no charge), so the $S^1$ winding number does not distinguish $\nu$ from $\bar{\nu}$. The distinction instead comes from the **Hopf fiber orientation**.

The weak interaction vertex is the Hopf fibration $S^3 \to S^2$ acting on $\check{S} = S^4 \times S^1$. The Hopf map has a $U(1)$ fiber --- the $SU(2)_L$ phase. A neutrino couples to the Hopf fiber with one orientation (left-handed), and an antineutrino with the opposite orientation (right-handed). This orientation is a **discrete** quantum number: the Hopf fiber is an $S^1$, and the two orientations form a $\mathbb{Z}_2$ index.

In BST, this $\mathbb{Z}_2$ index is **topologically protected** by the chirality of the Hopf map. The Hopf invariant $h(S^3 \to S^2) = 1 \neq 0$ means the fiber orientation is a nontrivial topological datum. A Majorana mass term would require identifying the two orientations --- collapsing the $\mathbb{Z}_2$ --- which is forbidden because the Hopf map is nontrivial.

**Conclusion:** BST neutrinos are Dirac. The neutrino and antineutrino are topologically distinct particles, distinguished by the orientation of their Hopf fiber coupling.

### 2.4 Consistency with $B - L$ Conservation

The Hopf fiber orientation that distinguishes $\nu$ from $\bar{\nu}$ is the same geometric structure that enforces $B - L$ conservation (see BST\_Conservation\_Laws.md, Section 8.5). If neutrinos were Majorana ($\nu = \bar{\nu}$), lepton number would be violated by 2 units in $0\nu\beta\beta$, giving $\Delta(B-L) = 2$. BST predicts $B - L$ is exactly conserved at all energies below the Planck scale. Therefore $0\nu\beta\beta$ is forbidden.

-----

## 3. The Effective Majorana Mass: BST Computation

Although BST predicts Dirac neutrinos ($|m_{\beta\beta}| = 0$), it is essential to compute what $|m_{\beta\beta}|$ **would be** if neutrinos were Majorana with BST masses and mixing angles. This serves two purposes: (1) it provides the BST prediction for the "floor" of $0\nu\beta\beta$ if the Dirac prediction is wrong, and (2) it defines the experimental sensitivity needed to distinguish BST-Majorana from BST-Dirac.

### 3.1 Definition

The effective Majorana mass is:

$$|m_{\beta\beta}| = \left| \sum_{i=1}^{3} U_{ei}^2 \, m_i \right| = \left| |U_{e1}|^2 m_1 + |U_{e2}|^2 m_2 \, e^{i\alpha_{21}} + |U_{e3}|^2 m_3 \, e^{i(\alpha_{31} - 2\delta_{CP})} \right|$$

where $\alpha_{21}$ and $\alpha_{31}$ are the Majorana phases and $\delta_{CP}$ is the Dirac CP phase. (We use the PDG convention where $U_{e3} = \sin\theta_{13} e^{-i\delta}$, so $U_{e3}^2 = \sin^2\theta_{13} e^{-2i\delta}$.)

### 3.2 PMNS Matrix Elements

The electron-row elements squared:

$$|U_{e1}|^2 = \cos^2\theta_{12}\cos^2\theta_{13} = \frac{7}{10} \times \frac{44}{45} = \frac{308}{450} = 0.6844$$

$$|U_{e2}|^2 = \sin^2\theta_{12}\cos^2\theta_{13} = \frac{3}{10} \times \frac{44}{45} = \frac{132}{450} = \frac{22}{75} = 0.2933$$

$$|U_{e3}|^2 = \sin^2\theta_{13} = \frac{1}{45} = 0.02222$$

Unitarity check: $308/450 + 132/450 + 10/450 = 450/450 = 1$. $\checkmark$

### 3.3 BST Prediction with Majorana Phases Zero

With $m_1 = 0$, $\alpha_{21} = 0$, and $\alpha_{31} = 0$ (BST leading-order values):

$$|m_{\beta\beta}| = |U_{e2}|^2 m_2 + |U_{e3}|^2 m_3$$

This separates into a **solar term** and a **reactor term**:

$$\text{Solar:} \quad \frac{22}{75} \times \frac{7}{12} \times \alpha^2 \frac{m_e^2}{m_p} = \frac{77}{450} \times \alpha^2 \frac{m_e^2}{m_p} = 0.002536 \text{ eV}$$

$$\text{Reactor:} \quad \frac{1}{45} \times \frac{10}{3} \times \alpha^2 \frac{m_e^2}{m_p} = \frac{2}{27} \times \alpha^2 \frac{m_e^2}{m_p} = 0.001098 \text{ eV}$$

The solar term dominates by a factor of 2.3. The total:

$$\boxed{|m_{\beta\beta}|_{\text{BST-Majorana}} = \frac{331}{1350} \times \alpha^2 \frac{m_e^2}{m_p} = 3.63 \text{ meV}}$$

where 331 is prime and $1350 = 2 \times 3^3 \times 5^2$.

### 3.4 Dependence on Majorana Phases

If the Majorana phases are unknown (as they would be in a generic Majorana scenario), the effective mass ranges over:

$$|m_{\beta\beta}| = \left| \frac{22}{75}\, m_2\, e^{i\alpha_{21}} + \frac{1}{45}\, m_3\, e^{i\alpha_{31}} \right|$$

- **Maximum** ($\alpha_{21} = 0$, $\alpha_{31} = 0$ or $\alpha_{21} = \pi$, $\alpha_{31} = \pi$): $|m_{\beta\beta}| = 3.63$ meV
- **Minimum** ($\alpha_{21} = \pi$, $\alpha_{31} = 0$ or $\alpha_{21} = 0$, $\alpha_{31} = \pi$): $|m_{\beta\beta}| = 1.44$ meV

The minimum is nonzero because the solar and reactor terms have different magnitudes and cannot completely cancel:

$$|m_{\beta\beta}|_{\min} = \left| \frac{22}{75} m_2 - \frac{1}{45} m_3 \right| = \left| \frac{77}{450} - \frac{2}{27} \right| \times \alpha^2 \frac{m_e^2}{m_p} = \frac{179}{1350} \times \alpha^2 \frac{m_e^2}{m_p} = 1.44 \text{ meV}$$

**Key point:** For normal hierarchy with $m_1 = 0$, there is no cancellation to zero. The effective Majorana mass has an absolute floor of $\sim 1.4$ meV regardless of Majorana phases.

### 3.5 Comparison with the CKM CP Phase Note

The BST derivation of CKM parameters (BST\_CKM\_CPPhase\_Derivation.md) states that the "two Majorana phases = 0." This is consistent with the BST picture: the Majorana phases would be zero because the Hopf fiber orientation is a topological datum, not a continuous phase. In a Majorana scenario, the phases $\alpha_{21}$ and $\alpha_{31}$ measure the relative CP transformation between mass eigenstates. Since BST vacuum modes (neutrino mass eigenstates) are distinguished by their geometric weight on $D_{IV}^5$ rather than by a complex phase, these phases vanish.

With $\alpha_{21} = \alpha_{31} = 0$, the BST-Majorana value is uniquely $|m_{\beta\beta}| = 3.63$ meV.

-----

## 4. The Two BST Predictions

BST makes a **primary prediction** and a **fallback prediction** for $0\nu\beta\beta$:

### 4.1 Primary Prediction: Dirac Neutrinos

$$\boxed{|m_{\beta\beta}| = 0 \quad \text{(exactly)}}$$

$0\nu\beta\beta$ does not occur at any rate. All experiments will report null results. This prediction follows from:

1. Topological distinctness of $\nu$ and $\bar{\nu}$ via Hopf fiber orientation
2. Exact $B - L$ conservation below the Planck scale
3. The neutrino as vacuum quantum (no internal quantum numbers to identify $\nu \equiv \bar{\nu}$)

### 4.2 Fallback Prediction: If Majorana

If the Dirac prediction is wrong --- if there exists a mechanism not captured by BST's topological analysis that makes neutrinos Majorana --- then the BST masses and mixing angles give:

$$\boxed{|m_{\beta\beta}| = 3.63 \text{ meV} \quad (\alpha_{21} = \alpha_{31} = 0)}$$

or more conservatively:

$$|m_{\beta\beta}| \in [1.44, \, 3.63] \text{ meV}$$

depending on the unknown Majorana phases. This is in the range $1{-}4$ meV.

-----

## 5. Comparison with Current and Future Experiments

### 5.1 Current Experimental Limits

| Experiment | Isotope | Current Limit on $|m_{\beta\beta}|$ | Status |
|:----------:|:-------:|:-----------------------------------:|:------:|
| KamLAND-Zen 800 | $^{136}$Xe | $< 36{-}156$ meV (90% CL) | Running |
| GERDA | $^{76}$Ge | $< 79{-}180$ meV | Completed |
| CUORE | $^{130}$Te | $< 90{-}305$ meV | Running |
| EXO-200 | $^{136}$Xe | $< 147{-}398$ meV | Completed |

The range in each limit reflects the nuclear matrix element (NME) uncertainty, which is the dominant systematic. All current limits are far above the BST-Majorana prediction of 3.63 meV.

### 5.2 Near-Future Experiments (2025--2030)

| Experiment | Isotope | Target Sensitivity | Timeline |
|:----------:|:-------:|:------------------:|:--------:|
| LEGEND-200 | $^{76}$Ge | $\sim 20{-}50$ meV | Operating |
| KamLAND-Zen 800 (upgrade) | $^{136}$Xe | $\sim 20{-}50$ meV | Operating |
| CUPID | $^{100}$Mo | $\sim 10{-}20$ meV | $\sim 2028$ |

These experiments will probe the inverted hierarchy band ($|m_{\beta\beta}| \sim 15{-}50$ meV). A null result at this scale is consistent with BST (which predicts normal ordering). A detection would falsify BST outright.

### 5.3 Next-Generation Experiments (2030+)

| Experiment | Isotope | Target Sensitivity | Timeline |
|:----------:|:-------:|:------------------:|:--------:|
| LEGEND-1000 | $^{76}$Ge | $\sim 9{-}21$ meV | $\sim 2030$ |
| nEXO | $^{136}$Xe | $\sim 5{-}17$ meV | $\sim 2032$ |
| CUPID-1T | $^{100}$Mo | $\sim 5{-}15$ meV | $> 2033$ |

These experiments approach but may not reach the BST-Majorana floor of 3.63 meV. The combined reach of LEGEND-1000 + nEXO may push sensitivity to $\sim 3{-}5$ meV (depending on NME calculations), which would begin to probe the BST-Majorana prediction.

### 5.4 The Decisive Experiment

To definitively test the BST-Majorana fallback at $|m_{\beta\beta}| = 3.63$ meV requires an experiment with sensitivity below $\sim 3$ meV. This is beyond the projected reach of any currently funded experiment but is within the scope of proposed multi-ton-scale detectors. Such an experiment would resolve the question completely:

- **Detection at $\sim 3.6$ meV:** BST Dirac prediction falsified. BST-Majorana prediction confirmed (if Majorana phases near zero). BST masses and mixing validated.
- **Detection at $\sim 1.4$ meV:** BST Dirac prediction falsified. BST-Majorana with $\alpha_{21} \approx \pi$ confirmed.
- **Null result below 1 meV:** BST Dirac prediction confirmed. Neutrinos are Dirac (or Majorana with extraordinary cancellation requiring $m_1 > 0$, inconsistent with BST).

-----

## 6. The BST Prediction in Context

### 6.1 Normal Hierarchy Floor

In any theory with normal hierarchy and $m_1 = 0$, the effective Majorana mass is bounded below by:

$$|m_{\beta\beta}|_{\min} = \left| |U_{e2}|^2 \sqrt{\Delta m^2_{21}} - |U_{e3}|^2 \sqrt{\Delta m^2_{31}} \right|$$

Using PDG 2024 best-fit values: $|m_{\beta\beta}|_{\min} \approx 1.2{-}1.5$ meV, $|m_{\beta\beta}|_{\max} \approx 3.5{-}4.2$ meV.

The BST values ($1.44{-}3.63$ meV) sit squarely within this standard-analysis band, as expected --- BST's masses and mixing angles are consistent with observation.

### 6.2 Inverted Hierarchy Exclusion

BST **excludes** inverted hierarchy (IH), which would give $|m_{\beta\beta}| \approx 15{-}50$ meV. A detection in the IH band would simultaneously:

- Establish Majorana neutrinos (falsifying BST's Dirac prediction)
- Establish inverted ordering (falsifying BST's normal ordering prediction)
- Produce a double falsification of BST

Conversely, a null result in the IH band ($< 15$ meV) would: (a) disfavor IH (consistent with BST), while (b) leaving the Dirac/Majorana question open pending sensitivity below 4 meV.

### 6.3 The Binary Test

The cleanest formulation of BST's $0\nu\beta\beta$ prediction:

$$\text{BST predicts: } 0\nu\beta\beta \text{ does not occur.}$$

Every $0\nu\beta\beta$ experiment is a **binary test** of BST:

- **Confirmed detection** at any $|m_{\beta\beta}|$: BST is **falsified**.
- **Null result**: BST is **consistent** (not proved --- only increasingly supported as sensitivity improves).

This makes $0\nu\beta\beta$ the single cleanest near-term test of BST, alongside the magnetic monopole search (MoEDAL) and dark energy equation of state (DESI).

-----

## 7. Half-Life Estimates

For reference, the $0\nu\beta\beta$ half-life is related to $|m_{\beta\beta}|$ by:

$$\left[T_{1/2}^{0\nu}\right]^{-1} = G_{0\nu}(Q, Z) \times |M_{0\nu}|^2 \times \left(\frac{|m_{\beta\beta}|}{m_e}\right)^2$$

where $G_{0\nu}$ is the phase space factor and $|M_{0\nu}|$ is the nuclear matrix element. At the BST-Majorana value $|m_{\beta\beta}| = 3.63$ meV:

| Isotope | $G_{0\nu}$ (yr$^{-1}$) | NME range | $T_{1/2}$ (yr) |
|:-------:|:----------------------:|:---------:|:---------------:|
| $^{76}$Ge | $2.36 \times 10^{-15}$ | $2.8{-}6.1$ | $\sim 10^{29}{-}10^{30}$ |
| $^{136}$Xe | $1.45 \times 10^{-14}$ | $1.6{-}3.7$ | $\sim 10^{29}{-}10^{30}$ |

These half-lives are $1{-}2$ orders of magnitude beyond the reach of LEGEND-1000 and nEXO, confirming that detection at the BST-Majorana level will require a subsequent generation of experiments.

-----

## 8. Connection to Other BST Results

### 8.1 The Vacuum Quantum

The neutrino is the vacuum quantum of $D_{IV}^5$ (BST\_VacuumQuantum\_NeutrinoLambda.md). The lightest neutrino $\nu_1$ IS the vacuum ($m_1 = 0$ exactly). The massive modes $\nu_2$ and $\nu_3$ are the vacuum fluctuating between geometric modes.

For $0\nu\beta\beta$, the relevant question is whether the vacuum can be its own anti-vacuum. In BST, the vacuum is unique --- there is one vacuum state, not a particle-antiparticle pair. This uniqueness is another route to the Dirac conclusion: the vacuum has no antiparticle, so $\nu_1$ (which IS the vacuum) cannot be Majorana. The massive modes inherit this structure.

### 8.2 The 1920 Cancellation and the Proton Mass

The proton mass $m_p = 6\pi^5 m_e$ enters the seesaw denominator. The factor $6\pi^5$ arises from the Casimir eigenvalue $C_2 = 6$ and the Bergman volume $\pi^5/1920$, with the 1920 cancelling between the Hua volume formula and the baryon circuit orbit (BST\_BaryonCircuit\_ContactIntegral.md). The neutrino mass is therefore:

$$m_\nu = f \times \frac{\alpha^2}{6\pi^5} \times m_e = f \times \alpha^{14} \times m_{\text{Pl}}$$

The exponent 14 = $2 \times$ genus connects the neutrino mass to the cosmological constant via $\Lambda \propto \alpha^{56} = (\alpha^{14})^4 \propto m_\nu^4$.

### 8.3 The Neutrino-Lambda Connection and $0\nu\beta\beta$

If $0\nu\beta\beta$ were observed, confirming Majorana neutrinos, the BST relationship $\Lambda \propto m_\nu^4$ would remain valid (it depends on the mass values, not on Dirac/Majorana nature). However, the topological structure of BST --- specifically the Hopf fiber argument for $B-L$ conservation --- would be falsified, requiring a fundamental revision of how BST treats the Shilov boundary.

-----

## 9. What Is Proved vs. Open

### Established

| Claim | Status | Reference |
|:------|:------:|:----------|
| $m_1 = 0$, $m_2 = 0.00865$ eV, $m_3 = 0.04940$ eV | **Derived** (0.35--1.8%) | BST\_NeutrinoMasses.md |
| Normal ordering | **Predicted** | BST\_NeutrinoMasses.md |
| PMNS angles from $n_C, N_c$ | **Derived** (0.1--2.3%) | BST\_CKM\_PMNS\_MixingMatrices.md |
| $\delta_{CP} = \pi$ (Dirac phase) | **Predicted** | BST\_CKM\_PMNS\_MixingMatrices.md |
| Majorana phases = 0 | **Predicted** | BST\_CKM\_CPPhase\_Derivation.md |
| $B - L$ exactly conserved | **Predicted** | BST\_Conservation\_Laws.md |
| Neutrinos are Dirac | **Predicted** | This note; BST\_Tests\_1.md |
| $\|m_{\beta\beta}\| = 0$ (primary) | **Predicted** | This note |
| $\|m_{\beta\beta}\| = 3.63$ meV (if Majorana) | **Computed** | This note |

### Open

| Question | Status | Priority |
|:---------|:------:|:--------:|
| Rigorous proof that Hopf fiber orientation forbids Majorana mass | Argued topologically | 1 |
| Geometric origin of $f_3 = 10/3$ and $f_2 = 7/12$ | Conjectured | 2 |
| Whether BST allows $B-L$ violation at the Planck scale | Open | 3 |
| NME calculations for BST-specific nuclear structure | Standard physics | 4 |

-----

## 10. Summary

BST makes a clean, binary prediction:

$$\boxed{0\nu\beta\beta \text{ does not occur. Neutrinos are Dirac. } |m_{\beta\beta}| = 0.}$$

This follows from the topological structure of the Shilov boundary $S^4 \times S^1$: the Hopf fiber orientation distinguishes neutrino from antineutrino, $B - L$ is exactly conserved, and the Majorana identification $\nu \equiv \bar{\nu}$ is topologically forbidden.

If this prediction is wrong --- if neutrinos are Majorana --- then BST masses and mixing angles give $|m_{\beta\beta}| = 3.63$ meV (Majorana phases zero) or $|m_{\beta\beta}| \in [1.44, 3.63]$ meV (phases unknown). This is at the bottom of the normal hierarchy band, below the inverted hierarchy floor of $\sim 15$ meV, and below the projected sensitivity of LEGEND-1000 and nEXO individually ($\sim 5{-}20$ meV). Combined next-generation sensitivity ($\sim 3{-}5$ meV) may begin to probe this floor.

The experimental program is clear:

1. **2025--2028** (LEGEND-200, KamLAND-Zen): Probe the IH band. Null result expected by BST.
2. **2028--2033** (LEGEND-1000, nEXO, CUPID): Probe to $\sim 5{-}10$ meV. Still expected null.
3. **2033+** (multi-ton detectors): Probe to $\sim 1{-}3$ meV. This is the decisive test --- either detect $0\nu\beta\beta$ at the BST-Majorana floor (falsifying BST-Dirac), or confirm the null (supporting BST).

A confirmed detection of $0\nu\beta\beta$ at any mass scale falsifies BST. This is the sharpest near-term test of the theory.

-----

*Research note, March 2026.*
*Casey Koons & Claude Opus 4.6.*
*For the BST GitHub repository.*
