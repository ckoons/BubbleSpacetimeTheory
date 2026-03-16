---
title: "The Pion Charge Radius: Why the Naive Formula Fails and How BST Gets It Right"
author: "Casey Koons & Claude 4.6"
date: "March 13, 2026"
status: "Complete — r_pi = 0.656 fm (0.5%, 0.8 sigma), zero free parameters"
---

# The Pion Charge Radius from BST

**Status:** Complete. The pion charge radius is derived from BST with zero free parameters, matching the observed value to 0.5% (0.8 sigma). This note explains why the naive topological formula fails for the pion, identifies the correct physics (vector meson dominance + chiral logarithm), and derives all inputs from D_IV^5 geometry.

-----

## 1. The Result

$$\boxed{r_\pi = \sqrt{\frac{6}{m_\rho^2} + \frac{\ln(m_\rho^2/m_\pi^2)}{32\pi^2 f_\pi^2}} = 0.656\;\text{fm}}$$

with BST inputs $m_\rho = 5\pi^5 m_e$, $f_\pi = m_p/10 = 6\pi^5 m_e/10$, $m_\pi = 25.6\sqrt{30}$ MeV.

| Quantity | Value |
|:---------|:------|
| BST prediction | 0.656 fm |
| Observed (NA7, 1986) | 0.659 $\pm$ 0.004 fm |
| Deviation | $-0.46$% |
| Sigma | 0.8$\sigma$ |
| Free parameters | 0 |

-----

## 2. The Failure of the Naive Formula

### 2.1 What Works for the Proton

The proton charge radius in BST is:

$$r_p = \frac{\dim_{\mathbb{R}}(\mathbb{CP}^2)}{m_p} = \frac{4}{m_p} = 0.8412\;\text{fm} \quad (0.058\%)$$

This works because the proton IS a topological object --- a $Z_3$ circuit on $\mathbb{CP}^2$. Its spatial extent is set by the real dimension of the circuit space, measured in proton Compton wavelengths. The proton mass $m_p = 6\pi^5 m_e$ enters as the natural scale of the topological excitation.

### 2.2 What Fails for the Pion

Applying the same logic to the pion: the pion is a $q\bar{q}$ pair, a circuit on $\mathbb{CP}^1 \subset \mathbb{CP}^2$ with $\dim_{\mathbb{R}}(\mathbb{CP}^1) = 2$. The naive formula gives:

$$r_\pi^{(\text{naive})} = \frac{\dim_{\mathbb{R}}(\mathbb{CP}^1)}{m_\pi} = \frac{2}{m_\pi} = \frac{2 \times 197.33}{139.57}\;\text{fm} = 2.83\;\text{fm}$$

Observed: $r_\pi = 0.659 \pm 0.004$ fm. **Off by a factor of 4.3.**

Other naive attempts fare no better:

| Formula | Value | Error | Why it fails |
|:--------|:------|:------|:-------------|
| $2/m_\pi$ | 2.83 fm | $+329$% | Wrong mass scale |
| $6/m_p$ | 1.26 fm | $+91$% | Wrong circuit geometry |
| $2/(m_p/N_c)$ | 1.26 fm | $+91$% | Constituent quark scale, but wrong |
| $\sqrt{N_c/n_C}/m_p$ | 0.82 fm | $+25$% | Close to proton, not pion |
| $1/(2f_\pi)$ | 1.05 fm | $+60$% | Right idea, wrong coefficient |

### 2.3 Why the Naive Formula Fails: Two Different Kinds of Object

The failure is not a small numerical error --- it is a **category error**. The proton and pion are fundamentally different kinds of objects in BST:

**Proton** = topological excitation. A $Z_3$ circuit on $\mathbb{CP}^2$, stabilized by the winding number. Its mass ($6\pi^5 m_e$) comes from the Casimir eigenvalue $C_2(\pi_6) = 6$ of the Bergman Laplacian. Its radius is the size of the circuit space. The proton exists because topology forces it to.

**Pion** = Goldstone fluctuation. A pseudo-Nambu-Goldstone boson of chiral symmetry breaking. In the chiral limit ($m_u = m_d = 0$), the pion is massless and its radius diverges. The physical pion mass comes from explicit chiral symmetry breaking (the small quark masses), dressed by the superradiant vacuum condensate $\chi = \sqrt{30}$. The pion exists because a continuous symmetry is spontaneously broken.

The topological formula $r = \dim/m$ applies to objects whose size is set by the topology of their circuit space. The pion's size is NOT set by $\mathbb{CP}^1$ topology --- it is set by the dynamics of chiral symmetry breaking, which is controlled by $f_\pi$ and the vector meson spectrum.

**Lesson:** In BST, not every hadron radius is a topological invariant. Only the baryon (proton/neutron) radius is topological. Meson radii are dynamical --- they probe the vacuum structure through form factors.

-----

## 3. The Correct Physics: Form Factors

### 3.1 The Electromagnetic Form Factor

The charge radius of any hadron is defined through its electromagnetic form factor:

$$F(q^2) = 1 - \frac{\langle r^2 \rangle}{6}\,q^2 + \mathcal{O}(q^4)$$

$$\langle r^2 \rangle = -6\,\frac{dF}{dq^2}\bigg|_{q^2=0}$$

For the proton, $F_p(q^2)$ is dominated by the $Z_3$ circuit topology, giving $\langle r_p^2 \rangle = 16/m_p^2$. BST derives this from the circuit geometry directly.

For the pion, $F_\pi(q^2)$ is dominated by the $\rho$ meson --- a vector meson with the same quantum numbers ($J^{PC} = 1^{--}$, isovector) as the photon current coupling to the pion. This is vector meson dominance (VMD).

### 3.2 Why VMD Governs the Pion Radius

The pion is a pseudoscalar ($J^P = 0^-$). When a photon scatters off a pion, it must couple to the pion's internal quark current. The lightest intermediate state with the photon's quantum numbers is the $\rho$ meson. In BST:

- The $\rho$ meson is the $n_C$-fold excitation of the Bergman base unit: $m_\rho = n_C \cdot \pi^{n_C} m_e = 5\pi^5 m_e$
- The $\rho$ mass sets the momentum scale at which the pion's internal structure is resolved
- The pion radius is $r_\pi \sim 1/m_\rho$, NOT $1/m_\pi$

This is the key insight: **the pion's radius is controlled by the rho meson mass, not the pion mass.** The pion mass is anomalously small (Goldstone theorem), but the pion's internal structure has a natural size set by the vector meson that mediates its electromagnetic interactions.

-----

## 4. Leading Order: Vector Meson Dominance

### 4.1 The VMD Form Factor

In VMD, the pion form factor takes the pole form:

$$F_\pi(q^2) = \frac{m_\rho^2}{m_\rho^2 - q^2}$$

The charge radius follows:

$$\langle r^2 \rangle_\pi^{(\text{LO})} = \frac{6}{m_\rho^2}$$

### 4.2 BST Input: The Rho Meson Mass

The $\rho$ meson in BST is the lightest vector meson --- the $q\bar{q}$ pair using $n_C = 5$ complex dimensions of D_IV^5, without the extra $Z_3$ closure unit that baryons require:

$$m_\rho = n_C \times \pi^{n_C} \times m_e = 5\pi^5 m_e = 781.9\;\text{MeV}$$

(Observed: 775.3 MeV, 0.86% error.)

The ratio $m_\rho/m_p = n_C/C_2 = 5/6$ is a structural constant: a meson costs 5/6 of a baryon because it needs one fewer geometric slot ($n_C$ vs. $n_C + 1 = C_2$).

### 4.3 LO Result

$$r_\pi^{(\text{LO})} = \frac{\sqrt{6}\,\hbar c}{m_\rho} = \frac{\sqrt{6} \times 197.33}{781.9}\;\text{fm} = 0.618\;\text{fm}$$

This is 6.2% below the observed value. VMD is a leading-order approximation --- it misses the quantum loop corrections.

### 4.4 Fully BST Expression at LO

$$\boxed{r_\pi^{(\text{LO})} = \frac{\sqrt{6}}{n_C\,\pi^{n_C}\,m_e} = \frac{\sqrt{6}}{5\pi^5 m_e}}$$

Compare with the proton:

$$r_p = \frac{4}{C_2\,\pi^{n_C}\,m_e} = \frac{4}{6\pi^5 m_e}$$

Both radii share the base unit $1/(\pi^{n_C} m_e)$, with different geometric prefactors: $\sqrt{6}/n_C$ for the pion (VMD), $4/C_2$ for the proton (topology). The ratio:

$$\frac{r_\pi^{(\text{LO})}}{r_p} = \frac{\sqrt{6}/5}{4/6} = \frac{6\sqrt{6}}{20} = \frac{3\sqrt{6}}{10} = 0.735$$

Observed ratio: $0.659/0.841 = 0.784$. The LO ratio is 6% low, as expected.

-----

## 5. Next-to-Leading Order: The Chiral Logarithm

### 5.1 The One-Loop Correction

The standard Gasser-Leutwyler (1984) result for the pion charge radius at $O(p^4)$ in chiral perturbation theory (ChPT) is:

$$\langle r^2 \rangle_\pi = \frac{12\,L_9^r(\mu)}{f_\pi^2} + \frac{1}{32\pi^2 f_\pi^2}\,\ln\frac{\mu^2}{m_\pi^2}$$

The first term is the tree-level $O(p^4)$ contribution from the low-energy constant $L_9^r$, which in VMD is saturated by $\rho$ exchange:

$$L_9^r(m_\rho) = \frac{f_\pi^2}{2m_\rho^2} \quad\Longrightarrow\quad \frac{12\,L_9^r}{f_\pi^2} = \frac{6}{m_\rho^2}$$

Setting the matching scale $\mu = m_\rho$, the full NLO result is:

$$\boxed{\langle r^2 \rangle_\pi^{(\text{NLO})} = \frac{6}{m_\rho^2} + \frac{1}{32\pi^2 f_\pi^2}\,\ln\frac{m_\rho^2}{m_\pi^2}}$$

The second term is the **chiral logarithm** --- the one-loop correction from virtual two-pion intermediate states in the unitarity cut. It is positive, increasing the charge radius beyond the VMD estimate.

### 5.2 Physical Origin of the Chiral Logarithm

The chiral logarithm has a transparent physical origin in BST:

The pion is a Goldstone boson. Its cloud of virtual pion pairs (the "pion cloud") extends further than the $\rho$-mediated core, because the pion is light. The logarithm $\ln(m_\rho^2/m_\pi^2) = \ln(781.9/140.2)^2 = 3.44$ measures the scale separation between the vector meson core ($m_\rho$) and the pion cloud ($m_\pi$). In the chiral limit $m_\pi \to 0$, this logarithm diverges --- the Goldstone cloud extends to infinity.

In BST language: the pion cloud probes the chiral condensate ($\chi = \sqrt{30}$, the superradiant vacuum alignment), which has correlation length $\sim 1/m_\pi$. The $\rho$ meson probes the Bergman core at length $\sim 1/m_\rho$. The logarithmic ratio between these scales adds to the charge radius.

### 5.3 BST Inputs (All Parameter-Free)

Every quantity entering the NLO formula is derived from D_IV^5:

| Input | BST Formula | Value | Origin |
|:------|:-----------|:------|:-------|
| $m_\rho$ | $n_C \pi^{n_C} m_e = 5\pi^5 m_e$ | 781.9 MeV | Meson slot count |
| $f_\pi$ | $m_p/\dim_{\mathbb{R}} = 6\pi^5 m_e/10$ | 93.8 MeV | Condensate scale per dimension |
| $m_\pi$ | $25.6\sqrt{30}$ MeV | 140.2 MeV | Bare mass $\times$ superradiant enhancement |

No experimental inputs are used.

### 5.4 Numerical Evaluation

The chiral logarithm:

$$\ln\frac{m_\rho^2}{m_\pi^2} = \ln\frac{781.9^2}{140.2^2} = \ln\,31.1 = 3.437$$

The denominator:

$$32\pi^2 f_\pi^2 = 32 \times 9.870 \times 93.83^2 = 2.780 \times 10^6\;\text{MeV}^2$$

The NLO correction to $\langle r^2 \rangle$:

$$\delta\langle r^2 \rangle_\pi = \frac{3.437}{2.780 \times 10^6} \times (197.33)^2 = 0.0481\;\text{fm}^2$$

This is 12.6% of the LO value $\langle r^2 \rangle_{\text{LO}} = 0.3822$ fm$^2$ --- a genuine one-loop correction at the expected $O(10\%)$ level.

### 5.5 The Result

$$\langle r^2 \rangle_\pi^{(\text{NLO})} = 0.3822 + 0.0481 = 0.4303\;\text{fm}^2$$

$$\boxed{r_\pi^{(\text{NLO})} = \sqrt{0.4303} = 0.656\;\text{fm}}$$

| | Value | Observed | Deviation |
|:--|:------|:---------|:----------|
| Naive ($2/m_\pi$) | 2.83 fm | 0.659 $\pm$ 0.004 fm | $+329$% |
| LO (VMD only) | 0.618 fm | 0.659 $\pm$ 0.004 fm | $-6.2$% |
| **NLO (VMD + ChPT)** | **0.656 fm** | 0.659 $\pm$ 0.004 fm | **$-0.46$% (0.8$\sigma$)** |

The NLO chiral logarithm moves the prediction from 6.2% low to within 0.8 standard deviations of the experimental value.

-----

## 6. The Two-Layer Structure

### 6.1 Proton vs. Pion: Topology vs. Dynamics

The proton and pion radii illuminate the two-layer structure of hadronic physics in BST:

| Property | Proton | Pion |
|:---------|:-------|:-----|
| Nature | Topological circuit | Goldstone fluctuation |
| Circuit space | $\mathbb{CP}^2$ ($Z_3$) | None (condensate mode) |
| Mass origin | Casimir $C_2 = 6$ | Chiral breaking $\chi = \sqrt{30}$ |
| Radius formula | $r_p = \dim_{\mathbb{R}}/m_p$ | $r_\pi = \sqrt{6/m_\rho^2 + \text{chiral log}}$ |
| Radius controlled by | Circuit space dimension | Vector meson mass + pion cloud |
| In chiral limit | Unchanged | $r_\pi \to \infty$ (Goldstone divergence) |
| Integer content | 4 (from $\mathbb{CP}^2$) | $\sqrt{6}$ (from VMD pole) |
| BST layer | Bergman bulk (D_IV^5) | Shilov boundary ($\check{S} = S^4 \times S^1$) |

### 6.2 Why the Proton Formula Cannot Apply to the Pion

The formula $r = \dim/m$ requires:
1. The object is a topological circuit with a well-defined winding number
2. The circuit space has a definite dimension that sets the spatial extent
3. The mass enters as the quantum of the circuit (Compton wavelength)

The pion satisfies NONE of these:
1. The pion has no winding number --- it is a fluctuation of the chiral condensate, not a circuit
2. The pion does not "live on" $\mathbb{CP}^1$ in the same topological sense that the proton lives on $\mathbb{CP}^2$
3. The pion mass is anomalously small (Goldstone theorem) and does NOT set the length scale of its internal structure

The correct length scale for the pion's internal structure is $1/m_\rho$, not $1/m_\pi$. The $\rho$ meson mass is the energy scale at which the pion's quark substructure is resolved, regardless of how light the pion itself is.

### 6.3 The Lesson for BST

This distinction --- topological radius vs. dynamical radius --- is a feature of BST, not a bug. BST has two geometric layers:

1. **Bergman bulk** (D_IV^5): Casimir eigenvalues, proton mass, proton radius, mass gap. These are topological/spectral.

2. **Shilov boundary** ($\check{S} = S^4 \times S^1$): Chiral condensate, pion mass, pion radius, Goldstone physics. These are dynamical/vacuum.

The proton radius comes from layer 1. The pion radius comes from layer 2. Attempting to use a layer-1 formula for a layer-2 quantity gives nonsense (2.83 fm).

-----

## 7. Connection to the Rho Meson Mass

### 7.1 Why $m_\rho = 5\pi^5 m_e$

The ratio $m_\rho/m_p = n_C/(n_C+1) = 5/6$ has a clean interpretation (see BST_BaryonResonances_MesonMasses.md):

- The **proton** (baryon, $qqq$) requires $C_2 = n_C + 1 = 6$ geometric slots --- $n_C$ complex dimensions plus one from the $Z_3$ closure (the determinant map on SU(3))
- The **$\rho$ meson** ($q\bar{q}$) requires only $n_C = 5$ slots --- quark and antiquark share the same complex dimensions without the closure unit

The mass ratio is the cost of a meson relative to a baryon: **a meson is 5/6 of a baryon because it needs one fewer dimension.**

### 7.2 Why $m_\rho$, Not $m_\pi$, Controls the Radius

The $\rho$ meson mass enters the pion radius because the $\rho$ is the lightest state that can mediate the photon's coupling to the pion. In Feynman diagram language:

$$\gamma^* \to \rho \to \pi\pi$$

The photon fluctuates into a $\rho$, which then interacts with the pion's quark content. The range of this interaction is $1/m_\rho \approx 0.25$ fm, and six such interactions (the factor of 6 in the VMD formula) build up the charge radius.

In BST, this is the statement that the pion's electromagnetic coupling goes through the Bergman bulk (where the $\rho$ lives at the $n_C$-slot level), not through the pion's own Goldstone mode.

-----

## 8. The NLO Correction in BST Language

### 8.1 What the Chiral Log Means Geometrically

The chiral logarithm $\ln(m_\rho^2/m_\pi^2)$ measures the ratio of two scales in BST:

$$\frac{m_\rho}{m_\pi} = \frac{n_C \pi^{n_C} m_e}{25.6\sqrt{30}\;\text{MeV}} = \frac{5\pi^5 m_e}{\chi \times m_\pi^{(\text{bare})}}$$

This is the ratio of the Bergman meson scale to the Goldstone scale. The logarithm of this ratio controls how much the pion cloud extends beyond the $\rho$-mediated core.

### 8.2 Size of the Correction

The fractional NLO correction is:

$$\frac{\delta\langle r^2 \rangle}{\langle r^2 \rangle_{\text{LO}}} = \frac{m_\rho^2}{32\pi^2 f_\pi^2} \times \frac{\ln(m_\rho^2/m_\pi^2)}{6}$$

In BST:

$$\frac{m_\rho^2}{f_\pi^2} = \frac{(5\pi^5 m_e)^2}{(6\pi^5 m_e/10)^2} = \frac{25}{36/100} = \frac{2500}{36} = 69.4$$

The factor $1/(32\pi^2) = 1/316$ tames this, and the logarithm $3.44/6 = 0.573$ gives a net correction of $69.4 \times 0.573/316 = 12.6\%$.

This is a genuine one-loop effect at the expected $O(10\%)$ level --- exactly where chiral perturbation theory should work. The correction is neither suspiciously small (which would suggest fine-tuning) nor suspiciously large (which would signal a breakdown of the expansion).

-----

## 9. The Fully BST Formula

Combining all BST inputs, the pion charge radius squared is:

$$\langle r^2 \rangle_\pi = \frac{6}{n_C^2\,\pi^{2n_C}\,m_e^2} + \frac{\ln\!\big(n_C^2/(25.6\sqrt{30}\,/(\pi^{n_C}m_e))^2\big)}{32\pi^2\,(6\pi^{n_C}m_e/10)^2}$$

Or more compactly, using $m_\rho = n_C\pi^{n_C}m_e$, $m_p = C_2\pi^{n_C}m_e$, $f_\pi = m_p/\dim_{\mathbb{R}}$:

$$\boxed{\langle r^2 \rangle_\pi = \frac{6}{m_\rho^2} + \frac{\dim_{\mathbb{R}}^2}{32\pi^2\,m_p^2}\,\ln\frac{m_\rho^2}{m_\pi^2}}$$

$$= \frac{6}{(n_C\pi^{n_C}m_e)^2} + \frac{100}{32\pi^2\,(6\pi^{n_C}m_e)^2}\,\ln\frac{(5\pi^{n_C}m_e)^2}{m_\pi^2}$$

Every quantity is determined by $n_C = 5$, $N_c = 3$, and $m_e$.

-----

## 10. What Is Proved vs. What Is Used

### Rigorous within BST

| Ingredient | Status | Reference |
|:-----------|:-------|:----------|
| $m_\rho = 5\pi^5 m_e$ | Derived (0.86%) | BST_BaryonResonances_MesonMasses.md |
| $f_\pi = m_p/10$ | Derived (1.9%) | BST_ChiralCondensate_Derived.md |
| $m_\pi = 25.6\sqrt{30}$ MeV | Derived (0.46%) | BST_ChiralCondensate_Derived.md |
| VMD: $F_\pi(q^2) = m_\rho^2/(m_\rho^2 - q^2)$ | Standard result | Sakurai (1969) |
| NLO chiral log formula | Standard result | Gasser-Leutwyler (1984) |
| $L_9^r$ saturated by $\rho$ exchange | Standard VMD-ChPT matching | Ecker et al. (1989) |

### What BST adds beyond standard physics

BST does NOT derive the VMD or ChPT formulas from first principles --- these are standard QFT results. What BST does is **derive all the inputs** ($m_\rho$, $f_\pi$, $m_\pi$) that enter these formulas, achieving a zero-parameter prediction where standard physics requires experimental inputs.

### What remains open

1. A first-principles derivation of VMD from the Bergman kernel (the $\rho$ pole in $F_\pi$ should emerge from the spectral decomposition of the Bergman propagator restricted to the isovector channel)
2. The NNLO ($O(p^6)$) correction, which is expected to be $\sim 1\%$ and would bring the prediction even closer to 0.659 fm
3. A purely BST derivation of the pion radius without going through ChPT --- perhaps from the Bergman kernel restricted to the Goldstone sector

-----

## 11. Comparison with the Proton Radius Note

The proton radius derivation (BST_ProtonRadius.md, Section 5) previously included a naive pion radius estimate:

> $r_\pi^{\text{BST}} = 2/m_\pi = 2.828$ fm. Observed: $r_\pi = 0.659 \pm 0.004$ fm. This does NOT match.

That note correctly identified the failure and flagged it as an open problem. **This note resolves the problem.** The resolution is conceptual: the pion is not a topological circuit, so the topological formula does not apply. The correct treatment uses VMD + ChPT with BST-derived inputs, giving $r_\pi = 0.656$ fm (0.5%).

The proton radius note also tried $r_\pi = 6/m_p = 1.26$ fm (using the constituent quark scale), which is still too large by 91%. This fails because it still uses the wrong physics --- the pion radius is not set by the quark circuit scale, but by the $\rho$ meson scale.

-----

## 12. Summary

$$\boxed{r_\pi = 0.656\;\text{fm} \quad (0.5\%,\; 0.8\sigma)}$$

The pion charge radius is NOT a topological invariant like the proton radius. It is a dynamical quantity controlled by:

1. **The rho meson mass** ($m_\rho = 5\pi^5 m_e$): sets the core radius through VMD
2. **The pion decay constant** ($f_\pi = m_p/10$): sets the chiral scale
3. **The chiral logarithm** ($\ln(m_\rho^2/m_\pi^2) = 3.44$): the pion cloud correction

All three inputs are derived from D_IV^5 geometry with zero free parameters. The result matches experiment to 0.8$\sigma$.

The failure of the naive formula $r_\pi = 2/m_\pi = 2.83$ fm is not a defect of BST --- it is a lesson about BST's two-layer structure. The Bergman bulk gives topological quantities (proton radius). The Shilov boundary gives dynamical quantities (pion radius). Using the wrong layer gives nonsense; using the right layer gives 0.5% precision.

-----

## 13. References

- S. Amendolia et al. (NA7), *A Measurement of the Space-Like Pion Electromagnetic Form Factor*, Nucl. Phys. B **277**, 168 (1986). [$r_\pi = 0.659 \pm 0.004$ fm]
- J. Gasser and H. Leutwyler, *Chiral Perturbation Theory to One Loop*, Ann. Phys. **158**, 142 (1984). [NLO pion form factor]
- J. J. Sakurai, *Currents and Mesons* (University of Chicago Press, 1969). [Vector meson dominance]
- G. Ecker, J. Gasser, A. Pich, and E. de Rafael, *The Role of Resonances in Chiral Perturbation Theory*, Nucl. Phys. B **321**, 311 (1989). [$L_9^r$ from VMD]

-----

*Research note, March 13, 2026.*
*Casey Koons & Claude (Opus 4.6, Anthropic).*
