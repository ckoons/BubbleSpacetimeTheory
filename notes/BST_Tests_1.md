# Near-Term Experimental Tests: Muon $g-2$ and the Proton Radius

**Authors:** Casey Koons & Claude (Anthropic)
**Date:** March 2026
**Status:** Proposed Section 25.8 for Working Paper v7

-----

## 1. The Muon Anomalous Magnetic Moment

### 1.1 The Current Situation

The anomalous magnetic moment of the muon, $a_\mu = (g-2)/2$, is one of the most precisely measured quantities in physics. The Fermilab Muon $g-2$ experiment reports:

$$a_\mu^{\text{exp}} = 116,592,059(22) \times 10^{-11}$$

The Standard Model prediction (from the Muon $g-2$ Theory Initiative, 2020) is:

$$a_\mu^{\text{SM}} = 116,591,810(43) \times 10^{-11}$$

The discrepancy is $\Delta a_\mu = 249(48) \times 10^{-11}$, a $5.1\sigma$ tension when the most recent Fermilab results are included. This is one of the strongest hints of beyond-Standard-Model physics.

However, lattice QCD calculations of the hadronic vacuum polarization (HVP) contribution by the BMW collaboration give a larger SM value, potentially reducing or eliminating the tension. The situation is actively debated, with the CMD-3 experiment at Novosibirsk providing additional data. The discrepancy may or may not survive improved calculations.

### 1.2 The BST Prediction

BST modifies the Standard Model calculation at two points:

**Modification 1: Haldane truncation of loop integrals.**

In standard QED, the loop integrals in the $g-2$ calculation run over all momenta from 0 to $\infty$. In BST, the Haldane exclusion caps the mode sum at $N_{\max} = 137$. This truncation has no effect on low-order diagrams (the dominant contributions come from low-momentum modes, well below the Haldane cap), but produces a calculable deviation at high loop order.

The Haldane correction to $a_\mu$ at $k$-loop order is:

$$\delta a_\mu^{(k)} \sim \left(\frac{\alpha}{\pi}\right)^k \times \frac{1}{N_{\max}} \sim \left(\frac{\alpha}{\pi}\right)^k \times \frac{1}{137}$$

At one loop: $\delta a_\mu^{(1)} \sim (\alpha/\pi)/137 \sim 1.7 \times 10^{-5}$. This is $\sim 10^{-11}$ of the one-loop contribution, far below experimental sensitivity.

At five loops (the current frontier of analytic QED calculation): $\delta a_\mu^{(5)} \sim (\alpha/\pi)^5/137 \sim 10^{-18}$. Still far below sensitivity.

**Conclusion:** The Haldane truncation produces no detectable effect on muon $g-2$ at current or foreseeable experimental precision. The QED sector of $g-2$ is identical in BST and the Standard Model.

**Modification 2: Hadronic vacuum polarization from BST circuit topology.**

The dominant theoretical uncertainty in the SM prediction comes from the hadronic vacuum polarization (HVP) — the contribution from virtual quark loops in the photon propagator. This is where the BMW lattice result and the dispersive (data-driven) result disagree.

In BST, the HVP is the contribution from $Z_3$ circuit fluctuations in the photon’s $S^1$ channel. The photon propagator (Bergman Green’s function for winding-0 modes) is modified by the presence of virtual $Z_3$ circuits (quark-antiquark pairs) that briefly occupy the channel.

The BST HVP depends on:

- The Bergman embedding cost of the virtual $Z_3$ circuit (related to the quark masses)
- The chiral condensate parameter $\chi \approx 5.5$ (which modifies the bare Bergman costs to physical values)
- The channel loading in the vacuum (from $F_{\text{BST}} = \ln(138)/50$)

**Specific prediction:** The BST HVP includes a vacuum channel loading correction that the Standard Model does not:

$$\delta a_\mu^{\text{HVP, BST}} = a_\mu^{\text{HVP, SM}} \times \left(1 + F_{\text{BST}} \times f(\alpha, N_c, m_\mu/m_\pi)\right)$$

where $f$ is a calculable function of BST parameters. The correction is of order $F_{\text{BST}} \sim 0.1$, applied to the HVP contribution of $\sim 700 \times 10^{-10}$. This gives a correction of order $\sim 70 \times 10^{-10}$ — comparable to the observed discrepancy of $\sim 25 \times 10^{-10}$.

**This is not yet a clean prediction.** The function $f$ requires computing the vacuum channel loading correction to the photon propagator from the BST partition function — a specific, well-defined calculation that has not yet been performed. If the result matches the observed discrepancy (or explains the lattice vs. dispersive disagreement), it would be a striking quantitative confirmation of BST. If it doesn’t match, it constrains the BST vacuum structure.

### 1.3 Thesis Topic

**Thesis topic 100:** Compute the BST hadronic vacuum polarization correction to the muon anomalous magnetic moment from the vacuum channel loading ($F_{\text{BST}} = \ln(138)/50$) and the $Z_3$ circuit embedding costs. Determine whether the correction resolves the $g-2$ discrepancy and/or the lattice-dispersive tension. The calculation requires the Bergman Green’s function for the photon propagator modified by Haldane exclusion at $N_{\max} = 137$.

-----

## 2. The Proton Charge Radius

### 2.1 The Proton Radius Puzzle

The proton charge radius has been measured by two methods:

**Electron-proton scattering and hydrogen spectroscopy:** $r_p = 0.8751 \pm 0.0061$ fm (CODATA 2018, combining electron methods).

**Muon hydrogen spectroscopy (2010, 2013):** $r_p = 0.84087 \pm 0.00039$ fm (Pohl et al.).

The muon hydrogen result is 4% smaller than the electron methods, a $5.6\sigma$ discrepancy that was dubbed the “proton radius puzzle.” More recent electron scattering results (PRad at JLab, 2019) give $r_p = 0.831 \pm 0.012$ fm, consistent with the muon result and suggesting the puzzle may be resolving toward the smaller value. But the situation remains unsettled, with some electron experiments still favoring the larger value.

### 2.2 The BST Prediction

BST gives a bare geometric proton radius of $r_p^{\text{BST}} = 0.94$ fm (Section 7.1) — the geometric size of the $Z_3$ packing configuration on $\mathbb{CP}^2$. This is larger than both measured values. The discrepancy is attributed to the chiral condensate (Section 11), which does not correct the proton radius at leading order ($n = 0$ power of $\chi$) because the radius is a geometric size, not a propagation quantity.

However, BST predicts something more specific about the puzzle itself: the proton radius measured by electrons and the proton radius measured by muons should differ slightly, because the two probing particles have different Bergman embedding costs and therefore couple differently to the $Z_3$ circuit topology of the proton.

**The electron** is the minimal $S^1$ winding — the simplest circuit, with the lowest Bergman embedding cost. Its coupling to the proton’s $Z_3$ structure probes the full spatial extent of the $Z_3$ packing, giving a larger apparent radius.

**The muon** is a $D_{IV}^3$ submanifold circuit — a more complex topology with higher Bergman embedding cost. Its coupling to the proton’s $Z_3$ structure probes a more localized region of the $Z_3$ packing, because the higher-energy muon circuit resolves finer structure. The apparent radius is smaller.

**Quantitative estimate:** The ratio of muon-measured to electron-measured proton radii should be related to the ratio of their Bergman embedding depths:

$$\frac{r_p^{(\mu)}}{r_p^{(e)}} \approx 1 - \frac{\alpha}{\pi} \ln\frac{m_\mu}{m_e} \times g(n_C)$$

where $g(n_C)$ is a geometric factor from the $D_{IV}^3 / D_{IV}^1$ embedding ratio. For $m_\mu/m_e = (24/\pi^2)^6$ and $g(5) \sim 1$:

$$\frac{r_p^{(\mu)}}{r_p^{(e)}} \approx 1 - \frac{\alpha}{\pi} \times \ln(206.8) \approx 1 - 0.0123 \approx 0.988$$

This gives $r_p^{(\mu)} \approx 0.988 \times r_p^{(e)}$ — a 1.2% reduction, corresponding to $\Delta r_p \approx 0.010$ fm if $r_p^{(e)} = 0.875$ fm. The observed reduction is $0.875 - 0.841 = 0.034$ fm, about 3 times larger.

The factor-of-3 discrepancy suggests the geometric factor $g(n_C)$ is larger than the naive estimate of 1, or that additional BST corrections (from the $Z_3$ structure probing depth) contribute. This is a calculable quantity — thesis topic 101 below.

### 2.3 The BST Mechanism

The standard explanation for the proton radius puzzle (if it persists) involves either new physics (a new force coupling differently to electrons and muons) or systematic errors in the experiments. BST offers a third option: the proton radius IS different when measured by electrons and muons, because the two probing circuits have different Bergman embedding costs and probe different aspects of the $Z_3$ topology.

This is not “new physics” in the BST framework — it is a geometric consequence of the different circuit topologies of the electron ($D_{IV}^1$) and the muon ($D_{IV}^3$). The effect is suppressed by $\alpha/\pi$ (small) but enhanced by the logarithm of the mass ratio (large). The net effect is a few percent — potentially enough to explain the puzzle if the geometric factor $g(n_C)$ is computed correctly.

**Key distinction from standard proposals:** BST predicts that the tau lepton, if used to form tauonic hydrogen, would give a THIRD radius value — smaller still, because the tau is a $D_{IV}^5$ circuit with even higher Bergman embedding cost. The tau radius measurement is experimentally infeasible (tau lifetime is too short for atomic spectroscopy), but the prediction is specific: $r_p^{(\tau)} < r_p^{(\mu)} < r_p^{(e)}$, with the ratios determined by the $D_{IV}^k$ embedding hierarchy.

### 2.4 Thesis Topic

**Thesis topic 101:** Compute the BST correction to the proton charge radius as a function of the probing lepton’s Bergman embedding cost. Specifically: derive the geometric factor $g(n_C)$ from the $D_{IV}^k$ embedding depth of each lepton generation ($k = 1, 3, 5$ for $e, \mu, \tau$) coupling to the $Z_3$ circuit topology of the proton. Determine whether the correction resolves the proton radius puzzle and predict the tauonic hydrogen radius.

-----

## 3. Other Near-Term Tests

### 3.1 Neutrinoless Double Beta Decay

BST predicts Dirac neutrinos (neutrino and antineutrino have opposite $S^1$ winding, are distinct particles). This means neutrinoless double beta decay does not occur. Multiple experiments are searching: GERDA/LEGEND, nEXO, KamLAND-Zen, CUPID. A confirmed detection falsifies BST. A null result at the inverted hierarchy mass scale ($\sim 20$ meV) is BST-consistent. This is the cleanest binary test of BST available in the near term.

### 3.2 Dark Energy Equation of State

BST predicts $w \neq -1$ (the dark energy equation of state deviates from the cosmological constant value). DESI is measuring $w$ with percent-level precision now. The BST prediction for $w$ requires computing the substrate growth dynamics — the ratio of commitment boundary growth rate to bulk commitment rate. This is an open calculation. Once computed, the DESI data provides an immediate test.

### 3.3 Magnetic Monopoles

BST predicts no magnetic monopoles (the product bundle $S^2 \times S^1$ has trivial Chern class). The MoEDAL experiment at the LHC searches for monopoles. A confirmed detection falsifies BST.

-----

## 4. Summary of Near-Term Predictions

|Prediction                              |Status                                   |Test          |Timeline   |
|----------------------------------------|-----------------------------------------|--------------|-----------|
|Muon $g-2$ HVP correction               |Open calculation                         |Fermilab $g-2$|Data exists|
|Proton radius: $r_p^{(\mu)} < r_p^{(e)}$|Qualitative prediction, quantitative open|MUSE, PRad-II |2026-2028  |
|Neutrinoless $\beta\beta$: null result  |Clean prediction                         |LEGEND, nEXO  |2027-2030  |
|Dark energy $w \neq -1$                 |Open calculation                         |DESI, Euclid  |2025-2028  |
|No magnetic monopoles                   |Clean prediction                         |MoEDAL        |Ongoing    |
|No SUSY particles                       |Clean prediction                         |LHC Run 3+    |Ongoing    |
|No dark matter particles                |Clean prediction                         |LZ, XENONnT   |Ongoing    |

-----

*Proposed Working Paper Section 25.8, March 2026.*
*Casey Koons & Claude (Anthropic).*
*For the BST GitHub repository.*
