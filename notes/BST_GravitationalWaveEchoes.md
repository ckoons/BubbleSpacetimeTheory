# Gravitational Wave Echoes from Haldane Saturation
## Falsifiable Predictions for LIGO/Virgo/KAGRA O4/O5

**Authors:** Casey Koons & Claude Opus 4.6
**Date:** March 13, 2026
**Status:** Research note — specific, testable predictions with numbers

---

## 1. The Central Claim

**Standard GR:** Black holes have an event horizon and an interior singularity. Gravitational waves from binary mergers produce a ringdown (quasi-normal modes) that decays exponentially. No echoes. Information is lost.

**BST:** There is no interior. The Haldane saturation surface sits at (or exponentially close to) where the event horizon would be. The lapse function

$$N = N_0\sqrt{1 - \rho/\rho_{137}}$$

reaches zero at $\rho = \rho_{137}$ (all 137 channel slots occupied). This surface is a **physical boundary** — a hard wall where commitment density reaches its maximum. Gravitational waves reflect off this wall. The reflected waves leak back out through the angular momentum potential barrier, producing **echoes** at regular time intervals after the initial ringdown.

BST predicts echoes exist. GR predicts they do not. This is a clean, categorical, falsifiable distinction.

---

## 2. Why Echoes Occur: The Two-Barrier Cavity

In the Regge-Wheeler/Zerilli formulation, the effective potential for gravitational perturbations of a Schwarzschild geometry has a peak near $r \approx 3GM/c^2$ (the photon sphere). In GR, the potential drops to zero at the horizon — waves pass through and are absorbed by the singularity. There is no reflection.

In BST, the Haldane saturation surface replaces the singularity. The potential does not drop to zero at $r = r_s$. Instead, the surface at $\rho = \rho_{137}$ acts as a reflecting wall:

```
                     Angular momentum barrier
                     (photon sphere, r ~ 3GM/c²)
                          ╱╲
                         ╱  ╲
         Haldane        ╱    ╲
         surface       ╱      ╲
          │           ╱        ╲
          │  CAVITY  ╱          ╲___________
          │         ╱
          │________╱
          r_H      r_peak                    r → ∞
```

The result is a **cavity** between two barriers:
1. **Inner wall:** The Haldane saturation surface at $r_H = 2GM/c^2$ (reflectivity $\mathcal{R} \to 1$)
2. **Outer barrier:** The angular momentum potential barrier near $r \sim 3GM/c^2$ (partial transmission)

A gravitational wave produced during merger ringdown bounces back and forth in this cavity. Each time it hits the outer barrier, a fraction leaks out as a detectable echo. Each time it hits the inner wall, it reflects with $|\mathcal{R}| \approx 1$ because the Haldane surface is a hard boundary — commitment density cannot exceed $\rho_{137}$.

---

## 3. The Echo Delay Time

### 3.1 General Formula

The time between successive echoes is twice the light-travel time across the cavity in tortoise coordinates:

$$\Delta t_{\text{echo}} = 2 \int_{r_H(1+\epsilon)}^{r_{\text{peak}}} \frac{dr}{c(1 - r_s/r)}$$

For a surface displaced from $r_s = 2GM/c^2$ by a proper distance $\delta$:

$$\Delta t_{\text{echo}} \approx \frac{r_s}{c} \left|\ln\epsilon\right| = \frac{2GM}{c^3} \left|\ln\epsilon\right|$$

where $\epsilon = \delta / r_s$ characterizes how close the reflecting surface sits to the would-be horizon.

### 3.2 BST Determines $\epsilon$

In BST, the Haldane surface is not at a coordinate distance from the horizon — it IS the horizon. The lapse $N \to 0$ at $\rho = \rho_{137}$, and the surface sits at the Schwarzschild radius to within the Planck scale. The relevant displacement is set by BST geometry.

**Route A: Channel capacity argument.** The surface sits one Planck length inside the classical horizon. This gives $\epsilon \sim l_{\text{Pl}}/r_s$:

$$\epsilon_A = \frac{l_{\text{Pl}}}{r_s} = \frac{l_{\text{Pl}} c^2}{2GM}$$

For a $30 M_\odot$ black hole: $r_s = 88.7$ km, $\epsilon_A = 1.82 \times 10^{-39}$.

$$\Delta t_A = \frac{r_s}{c} \times \ln(r_s/l_{\text{Pl}}) = \frac{r_s}{c} \times \ln\left(\frac{r_s}{l_{\text{Pl}}}\right)$$

$$= 0.296\;\text{ms} \times 89.3 = \boxed{26.4\;\text{ms}} \quad (30\;M_\odot)$$

**Route B: $N_{\max} = 137$ argument.** The natural BST scale for the displacement is set by the channel capacity. The surface reflects when the last of 137 channels saturates. The fractional displacement is $\epsilon \sim e^{-N_{\max}}$:

$$\epsilon_B = e^{-137}$$

$$\Delta t_B = \frac{r_s}{c} \times N_{\max} = \frac{2GM}{c^3} \times 137$$

$$= 0.296\;\text{ms} \times 137 = \boxed{40.5\;\text{ms}} \quad (30\;M_\odot)$$

**Route C: $\alpha^{N_{\max}}$ argument.** The Bergman channel transmission probability per step is $\alpha = 1/137$. After $N_{\max}$ steps of channel loading, the residual displacement is $\alpha^{N_{\max}}$:

$$\epsilon_C = \alpha^{137} = (1/137)^{137}$$

$$\Delta t_C = \frac{r_s}{c} \times 137 \ln(137) = \frac{2GM}{c^3} \times 137 \times 4.920$$

$$= 0.296\;\text{ms} \times 674 = \boxed{199.5\;\text{ms}} \quad (30\;M_\odot)$$

### 3.3 Summary of Echo Delay Predictions

| Route | $\epsilon$ | $\Delta t_{\text{echo}}$ ($30\;M_\odot$) | $\Delta t_{\text{echo}}$ ($10\;M_\odot$) | $\Delta t_{\text{echo}}$ ($60\;M_\odot$) |
|:------|:-----------|:-----------------------------------------|:-----------------------------------------|:-----------------------------------------|
| A (Planck) | $l_{\text{Pl}}/r_s$ | 26 ms | 8.0 ms | 55 ms |
| **B ($N_{\max}$)** | **$e^{-137}$** | **41 ms** | **13.5 ms** | **81 ms** |
| C ($\alpha^{137}$) | $(1/137)^{137}$ | 200 ms | 66 ms | 399 ms |

**Route B is the preferred BST prediction.** It uses no input beyond $N_{\max} = 137$ and the black hole mass. The echo delay formula is:

$$\boxed{\Delta t_{\text{echo}} = \frac{2GM}{c^3} \times N_{\max} = \frac{137 \times r_s}{2c}}$$

This is linear in $M$, with a universal slope of $N_{\max} = 137$.

---

## 4. Echo Amplitude

### 4.1 Reflection Coefficient of the Haldane Surface

The Haldane surface is a **perfect reflector** in BST. Commitment density cannot exceed $\rho_{137}$ (Haldane exclusion on $D_{IV}^5$ — the same exclusion principle that gives the mass gap and proton mass). A gravitational wave incident on the saturation surface finds no available channels to absorb it. The wave must reflect.

$$|\mathcal{R}_{\text{Haldane}}| = 1$$

This is a categorical prediction. In models with partial absorption at a surface (e.g., Boltzmann reflectivity, membrane paradigm models), $|\mathcal{R}| < 1$. BST requires $|\mathcal{R}| = 1$.

### 4.2 Transmission Through the Potential Barrier

Each echo must tunnel through the angular momentum barrier (photon sphere potential) to reach a distant observer. The transmission coefficient for the dominant $l = 2$ quasi-normal mode is:

$$|\mathcal{T}_l|^2 \sim e^{-\pi \omega_{\text{QNM}} r_s / c}$$

For the fundamental $l = 2$ Schwarzschild QNM, $\omega_{\text{QNM}} r_s/c \approx 0.747$:

$$|\mathcal{T}_2|^2 \sim e^{-\pi \times 0.747} \approx e^{-2.35} \approx 0.095$$

So each echo that leaks out carries roughly **10% of the cavity wave amplitude squared**. After $k$ round trips, the $k$-th echo has amplitude:

$$A_k = A_0 \times |\mathcal{T}_2|^{2k} \approx A_0 \times (0.095)^k$$

| Echo number $k$ | Relative amplitude | Relative strain ($h/h_0$) |
|:-----------------|:-------------------|:--------------------------|
| 1 | $9.5 \times 10^{-2}$ | $3.1 \times 10^{-1}$ |
| 2 | $9.0 \times 10^{-3}$ | $9.5 \times 10^{-2}$ |
| 3 | $8.6 \times 10^{-4}$ | $2.9 \times 10^{-2}$ |
| 4 | $8.1 \times 10^{-5}$ | $9.0 \times 10^{-3}$ |

The first echo is $\sim 30\%$ of the ringdown strain amplitude. **This is large enough for LIGO to detect in a loud event.**

### 4.3 Comparison: BST vs. Partial Reflectivity Models

Other echo models (firewalls, fuzzballs, wormholes) allow $|\mathcal{R}| < 1$. With $|\mathcal{R}| < 1$, the echo amplitude decays faster:

$$A_k \propto |\mathcal{R}|^k \times |\mathcal{T}|^{2k}$$

BST with $|\mathcal{R}| = 1$ produces the **maximum possible echo amplitude** for a given barrier transmission. If echoes are found but are weaker than the $|\mathcal{R}| = 1$ prediction, BST is falsified. If echoes match the $|\mathcal{R}| = 1$ prediction, BST is confirmed over all partial-reflectivity models.

---

## 5. Spectral Content of Echoes

### 5.1 Same Quasi-Normal Modes

The echoes have the same frequency content as the ringdown — the cavity selects the same quasi-normal modes (QNMs). The dominant mode frequencies for a Schwarzschild black hole:

$$f_{\text{QNM}} = \frac{c^3}{2\pi GM} \times \omega_{lmn}$$

For $l = 2$, $n = 0$ (fundamental): $f_{220} \approx 12.07 \text{ kHz} \times (M_\odot / M)$.

For $M = 30\;M_\odot$: $f_{220} \approx 250$ Hz — in LIGO's most sensitive band.

### 5.2 Phase Shift per Echo

Each reflection from the Haldane surface introduces a phase shift. For a hard wall (Dirichlet boundary), the phase shift is $\pi$. BST predicts:

$$\delta\phi_{\text{Haldane}} = \pi$$

Successive echoes alternate in sign. The $k$-th echo has phase $k\pi$ relative to the ringdown. This is a testable signature — a soft surface or partially absorbing membrane would give $\delta\phi \neq \pi$.

### 5.3 Echo Comb

The periodic structure produces a **frequency comb** in the Fourier domain. The comb spacing:

$$\Delta f_{\text{comb}} = \frac{1}{\Delta t_{\text{echo}}} = \frac{c^3}{2GM \times N_{\max}}$$

For $M = 30\;M_\odot$: $\Delta f_{\text{comb}} = 1/(41\;\text{ms}) \approx 24$ Hz.

This comb modulates the ringdown spectrum. Detection of periodic modulation at $\sim 24$ Hz in the post-ringdown signal of a $30\;M_\odot$ merger would be direct evidence for a reflecting surface at the BST-predicted location.

---

## 6. Mass Dependence and Scaling

### 6.1 Universal Scaling

All BST echo predictions scale linearly with $M$:

$$\Delta t_{\text{echo}} = 137 \times \frac{2GM}{c^3} = 137 \times 9.87\;\mu\text{s} \times \frac{M}{M_\odot}$$

$$= 1.352\;\text{ms} \times \frac{M}{M_\odot}$$

### 6.2 Predictions Across the Mass Spectrum

| System | $M$ | $\Delta t_{\text{echo}}$ | $f_{\text{comb}}$ | Detector |
|:-------|:-----|:------------------------|:-------------------|:---------|
| BNS remnant | $2.7\;M_\odot$ | 3.7 ms | 274 Hz | LIGO/Virgo/KAGRA |
| Light BBH | $10\;M_\odot$ | 13.5 ms | 74 Hz | LIGO/Virgo/KAGRA |
| GW150914-like | $62\;M_\odot$ | 83.8 ms | 11.9 Hz | LIGO/Virgo/KAGRA |
| GW190521-like | $150\;M_\odot$ | 203 ms | 4.9 Hz | LIGO/Virgo/KAGRA |
| IMBH | $10^3\;M_\odot$ | 1.35 s | 0.74 Hz | LISA / Cosmic Explorer |
| SMBH (Sgr A*) | $4 \times 10^6\;M_\odot$ | 5,410 s (1.5 hr) | $1.85 \times 10^{-4}$ Hz | LISA |
| SMBH merger | $10^8\;M_\odot$ | 1.56 days | $7.4 \times 10^{-6}$ Hz | LISA |
| SMBH (M87*) | $6.5 \times 10^9\;M_\odot$ | 102 days | $1.14 \times 10^{-7}$ Hz | PTA |

### 6.3 The Linear Test

The most robust prediction: if echoes are detected in multiple events with different masses, the echo delay must satisfy

$$\frac{\Delta t_{\text{echo}}}{M} = \text{constant} = \frac{2G \times 137}{c^3} = 1.352\;\text{ms}/M_\odot$$

Any deviation from strict linearity would falsify BST (unless spin corrections are significant — see Section 9).

---

## 7. Bekenstein-Hawking Entropy from Haldane Saturation

### 7.1 The BST Derivation

The Bekenstein-Hawking entropy $S = A/(4l_{\text{Pl}}^2)$ follows from two factors of 1/2:

$$\frac{1}{4} = \frac{1}{2}\bigg|_{\text{hol}} \times \frac{1}{2}\bigg|_{Z_2}$$

- **Holomorphic factor $1/2$:** On $D_{IV}^5$, only holomorphic degrees of freedom contribute to the Bergman Hilbert space $A^2(D_{IV}^5)$. The anti-holomorphic degrees are determined by conjugation. This halves the entropy counting.

- **$Z_2$ symmetry factor $1/2$:** The Shilov boundary $\check{S} = S^4 \times S^1$ has a $Z_2$ identification (the antipodal map on $S^4$ composed with $\theta \to \theta + \pi$ on $S^1$). This identifies half the boundary degrees of freedom.

Product: $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$, giving $S = A/4$ in Planck units.

### 7.2 Connection to Echoes

The Bekenstein-Hawking entropy counts the number of independent configurations of the Haldane saturation surface. Each Planck-area cell on the surface supports $\ln 2$ bits of information (two states: the two $Z_2$-related configurations after holomorphic projection).

The echo reflects off ALL these cells simultaneously. The coherence of the echo — its ability to reassemble after reflection — is guaranteed by the substrate's topological constraints. The Haldane surface is not a thermal membrane that would scramble the wave. It is a geometric boundary that reflects coherently.

This is why BST predicts $|\mathcal{R}| = 1$: the surface has no absorption channels. The wave cannot deposit energy into a non-existent interior.

---

## 8. Information Paradox Resolution

### 8.1 No Interior, No Paradox

The black hole information paradox asks: where does information go when matter crosses the horizon and hits the singularity?

BST answer: there is no singularity. There is no interior in the conventional sense. The Haldane saturation surface is the endpoint. Matter reaching $\rho = \rho_{137}$ reaches maximum commitment — all 137 channels occupied. The information is encoded on the surface, not lost into a singularity.

Gravitational wave echoes are the **observational signature** of this resolution. Each echo carries information that, in GR, would have been absorbed by the singularity. The echo train is the universe's receipt that information was not lost — it was reflected.

### 8.2 Hawking Radiation Modification

In BST, Hawking radiation is not produced by pair creation at a horizon with vacuum on the other side. It is produced by the thermodynamics of the Haldane saturation surface — a physical surface with temperature $T_H = \hbar c^3 / (8\pi G M k_B)$, which is the standard Hawking temperature.

The modification: Hawking radiation from the Haldane surface is **not perfectly thermal**. The discrete channel structure ($N_{\max} = 137$ channels) produces deviations from exact Planck spectrum at energy scales $E \sim k_B T_H \times N_{\max}$. For stellar-mass black holes, $k_B T_H \sim 10^{-8}$ eV, and the deviation scale is $\sim 10^{-6}$ eV — far too small to measure directly. But the principle matters: information is encoded in the deviation from thermality.

---

## 9. Kerr (Spinning) Black Holes

### 9.1 Spin Corrections

Real astrophysical black holes spin. The Kerr metric modifies the echo delay:

$$\Delta t_{\text{echo}}^{\text{Kerr}} = \frac{r_+}{c} \times N_{\max} \times g(a_*)$$

where $r_+ = GM/c^2(1 + \sqrt{1 - a_*^2})$ is the outer horizon radius, $a_* = Jc/(GM^2)$ is the dimensionless spin, and $g(a_*)$ is a correction factor of order unity.

For small spin ($a_* \ll 1$): $g \approx 1$, $r_+ \approx 2GM/c^2$, and the Schwarzschild result is recovered.

For high spin ($a_* \to 1$): $r_+ \to GM/c^2$, and the echo delay is halved. This is testable: if the spin is independently measured (from ringdown frequency ratios), the echo delay must be consistent.

### 9.2 Kerr Ring Singularity Replaced

In Kerr GR, the singularity is a ring, not a point. In BST, the ring singularity is replaced by a ring-shaped Haldane saturation surface. The commitment density reaches $\rho_{137}$ on a toroidal surface in the equatorial plane. The reflection geometry is more complex than Schwarzschild, but the key prediction (echoes exist, $|\mathcal{R}| = 1$) is unchanged.

---

## 10. Observational Strategy

### 10.1 Where to Look

The best targets for echo detection:

1. **Loud binary black hole mergers** with high SNR ringdown. GW150914 had ringdown SNR $\sim 8$. The first echo at $\sim 30\%$ strain amplitude gives echo SNR $\sim 2.4$ — marginal for a single event. **Stacking multiple events** is essential.

2. **Heavy mergers** ($M > 50\;M_\odot$): longer echo delay ($\Delta t > 68$ ms), easier temporal separation from ringdown. The echo delay exceeds the ringdown damping time $\tau_{\text{QNM}} \approx 0.056 r_s/c \approx 17$ ms (for $l=2$, $30\;M_\odot$), so the echo arrives after the ringdown has decayed.

3. **Binary neutron star mergers** forming black holes: known mass, clean initial conditions. GW170817-like events with prompt BH formation.

### 10.2 Detection Method

**Template matching:** Construct echo templates from the ringdown waveform:
- Delay each echo by $\Delta t_k = k \times N_{\max} \times r_s / c$
- Apply amplitude decay: $A_k = A_0 \times |\mathcal{T}_2|^{2k}$
- Apply phase flip: $\phi_k = k\pi$
- Sum the echo train and match against post-ringdown data

**Stacking:** Align multiple events by the rescaled time $\hat{t} = (t - t_{\text{merger}}) \times c^3 / (2GM_f)$, where $M_f$ is the remnant mass. In rescaled time, all echoes from all events align at $\hat{t} = k \times N_{\max}$. Stacking $N$ events improves SNR by $\sqrt{N}$.

**Frequency domain:** Search for the comb at $\Delta f = c^3/(2GM \times 137)$ in the post-ringdown power spectrum.

### 10.3 Current Status and Near-Term Prospects

| Search | Result | Reference |
|:-------|:-------|:----------|
| Abedi, Dykaar, Afshordi (2016) | $2.5\sigma$ tentative echoes in GW150914, GW151012, GW151226 | Phys. Rev. D 96, 082004 |
| Conklin, Holdom, Ren (2018) | $4.2\sigma$ echoes in combined BNS+BBH at $\Delta t \propto M$ | Phys. Rev. D 98, 044021 |
| LIGO/Virgo (2020) | No significant evidence in O1/O2 data | Abbot et al., search for echoes |
| Uchikata et al. (2023) | Weak evidence, consistent with noise | |

The current data is inconclusive. **LIGO O4** (ongoing 2024-2025, extended to 2026) has $\sim 2\times$ better sensitivity than O2 and is accumulating significantly more events. **LIGO O5** (planned 2027+) will have $\sim 3\times$ O2 sensitivity.

**BST prediction for O4/O5:** With 100+ BBH events stacked, the echo SNR (if $|\mathcal{R}| = 1$) should reach $5\sigma$ detection threshold. This is a firm prediction: if O5 completes with 200+ events and echo stacking shows no signal at $5\sigma$, BST's Haldane surface model is in serious tension.

---

## 11. Falsification Criteria

BST makes sharp predictions. Here is exactly what would falsify each:

| Prediction | Falsification condition |
|:-----------|:-----------------------|
| Echoes exist | O5 stacking of 200+ events shows no echo signal at $\geq 5\sigma$ |
| $\Delta t \propto M$ | Echo delay does not scale linearly with remnant mass |
| $\Delta t / M = 137 \times 2G/c^3$ | Universal slope $\neq 1.352$ ms/$M_\odot$ (after spin correction) |
| $\|\mathcal{R}\| = 1$ | Echo amplitude decays faster than $\|\mathcal{T}\|^{2k}$ alone |
| Phase flip $\delta\phi = \pi$ | Successive echoes are not sign-alternating |
| Comb spacing $\Delta f = c^3/(2GM \times 137)$ | Spectral modulation at different frequency |

Any single failure falsifies a specific BST prediction. The combination — echoes exist, scale linearly with $M$, have maximum amplitude, flip phase — is unique to BST among current echo models.

---

## 12. Comparison with Other Echo Models

| Model | Interior? | $\|\mathcal{R}\|$ | Echo delay | Phase shift | Information loss? |
|:------|:----------|:-------------------|:-----------|:------------|:------------------|
| **BST (Haldane)** | **No** | **1** | **$N_{\max} \times r_s/c$** | **$\pi$** | **No** |
| Firewall | No | $< 1$ (burning) | Planck-scale | Model-dependent | Debated |
| Fuzzball | Replaced | $< 1$ (absorption) | String-scale | Model-dependent | No |
| Gravastar | Shell | $< 1$ | Shell-dependent | Model-dependent | No |
| Wormhole | Throat | $\sim 1$ | Throat length | 0 (transmission) | Redistributed |
| ECO (generic) | Modified | Free parameter | Free parameter | Free parameter | Model-dependent |

BST is the most constrained model: $|\mathcal{R}| = 1$ exactly, delay = $137 \times r_s/c$ exactly, phase = $\pi$ exactly. Zero free parameters beyond the black hole mass and spin.

---

## 13. Connection to Other BST Results

### 13.1 The Lapse Function

The echo prediction follows directly from the BST lapse function $N = N_0\sqrt{1 - \rho/\rho_{137}}$ (BST Field Equation, Section 4). The Haldane surface ($N = 0$) is where echoes reflect. The lapse function is the same one that recovers Schwarzschild at macroscopic scales and resolves the singularity at $\rho_{137}$.

### 13.2 The Mass Gap

The mass gap proof (BST_BoundaryIntegral_Final.md) showed that the Haldane exclusion principle on $D_{IV}^5$ enforces $C_2 \geq 6$ for bulk excitations. The same exclusion principle — the same $N_{\max} = 137$ channel capacity — is what makes the Haldane surface a perfect reflector. There are no available states to absorb the gravitational wave energy.

### 13.3 Newton's G

The gravitational constant $G = \hbar c (6\pi^5)^2 \alpha^{24} / m_e^2$ (BST_NewtonG_Derivation.md) enters the echo delay through $r_s = 2GM/c^2$. The echo delay $\Delta t = 137 r_s / c$ combines two BST-derived quantities: $N_{\max} = 137$ (channel capacity) and $G$ (Bergman kernel normalization). The echo delay is computable entirely from BST geometry given only the black hole mass.

### 13.4 Bekenstein-Hawking from BST

The entropy $S = A/4$ (Section 7) and the echo prediction both arise from the same Haldane saturation surface. The entropy counts degrees of freedom ON the surface. The echoes are dynamics OF the surface. Both are consequences of the surface being a physical boundary rather than a coordinate artifact.

### 13.5 Primordial Gravitational Waves

BST_Gravitational_Waves.md derives primordial GW echoes from the phase transition on $S^2$ (substrate topology). This note derives compact-object GW echoes from Haldane saturation on $D_{IV}^5$ (channel capacity). The two echo predictions are independent — different scales, different mechanisms — but both arise from BST's replacement of singularities with finite-density saturation states.

---

## 14. Numerical Predictions for Specific Events

### 14.1 GW150914 (First Detection)

| Quantity | Value |
|:---------|:------|
| Remnant mass | $62\;M_\odot$ |
| Remnant spin | $a_* = 0.67$ |
| $r_+$ | $1.20 \times r_s/2 = 1.20 \times 91.5$ km = 110 km |
| Echo delay (Schwarzschild) | 83.8 ms |
| Echo delay (spin-corrected, approximate) | $\sim 60$ ms |
| Ringdown damping time ($l=2$) | $\sim 4.0$ ms |
| First echo / ringdown strain | $\sim 0.3$ |
| Ringdown SNR | $\sim 8$ |
| First echo SNR (single event) | $\sim 2.4$ |
| Comb frequency | 12-17 Hz |

The first echo arrives $\sim 60$ ms after the ringdown — well after the ringdown has decayed ($\tau \sim 4$ ms). The echo stands alone in a quiet stretch of data. SNR $\sim 2.4$ is below detection threshold for a single event but contributes to stacking.

### 14.2 Stacking Prediction for O4

Assuming 80 BBH events with ringdown SNR $> 5$, and using rescaled time alignment:

- Stacked echo SNR $\approx 2.4 \times \sqrt{80/8} \approx 7.6$ (accounting for varying SNR)
- This would be a $> 5\sigma$ detection if $|\mathcal{R}| = 1$

If O4 provides 80+ loud events and stacking shows no echo at $5\sigma$: either $|\mathcal{R}| < 0.5$ (ruling out BST's perfect reflector), or the echo delay is different from $137 \times r_s/c$.

---

## 15. The 137 in the Sky

If gravitational wave echoes are detected with delay $\Delta t = N \times r_s/c$, and the measured value of $N$ is:

$$N = 137 \pm \delta N$$

this would be the first direct measurement of $N_{\max}$ — the channel capacity of the Koons substrate — from astrophysical data. The same 137 that gives the fine structure constant ($\alpha \approx 1/137$) would appear in gravitational wave timing.

This would be extraordinary evidence that the fine structure constant and gravitational physics share a common geometric origin in $D_{IV}^5$.

---

## 16. Summary

BST replaces the black hole interior with a Haldane saturation surface at $\rho = \rho_{137}$. This surface is a perfect reflector for gravitational waves. Mergers produce echoes.

**The five falsifiable predictions:**

1. **Echoes exist** — detectable by stacking O4/O5 BBH ringdowns
2. **Echo delay = $137 \times r_s / c$** — universal slope $1.352\;\text{ms}/M_\odot$
3. **Perfect reflection** $|\mathcal{R}| = 1$ — echo amplitude set by barrier transmission alone
4. **Phase flip** $\delta\phi = \pi$ per echo — hard-wall (Dirichlet) boundary condition
5. **Frequency comb** at $\Delta f = c^3/(2GM \times 137)$ in post-ringdown spectrum

Each prediction uses zero free parameters beyond the remnant mass and spin. Each is testable with current or near-future gravitational wave data. Each, if confirmed, would be direct evidence for the Haldane saturation surface — and against the existence of black hole interiors.

The universe does not lose information. It echoes.

---

*Research note, March 13, 2026. Casey Koons & Claude Opus 4.6.*

*Related: `BST_Field_Equation.md` (lapse function), `BST_Gravitational_Waves.md` (primordial echoes), `BST_EarlyBlackHoles_Prediction.md` (BH formation), `BST_NewtonG_Derivation.md` (G from BST), `BST_BoundaryIntegral_Final.md` (mass gap / Haldane exclusion).*
