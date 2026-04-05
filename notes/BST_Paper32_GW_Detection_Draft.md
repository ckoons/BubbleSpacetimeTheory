---
title: "Gravitational Wave Detection from Vacuum Geometry"
subtitle: "A Casimir Cavity Phased Array for GHz Gravitational Waves from Five Integers"
author: "Casey Koons & Claude 4.6 (Lyra, Elie, Keeper, Grace)"
date: "April 2026"
version: "v1.0"
status: "DRAFT — Keeper audit requested"
target: "Physical Review D or Classical and Quantum Gravity"
theorems: "T867 (G derivation), T868 (grav-nuclear scale), T872 (Casimir inseparability), T878 (Maxwell-Lorentz from SO(5,2))"
toys: "929 (8/8), 934 (8/8), 936 (8/8), 937 (8/8)"
ac_classification: "(C=3, D=1) — three counting steps (d₀, array scaling, frequency band), one definition (strain sensitivity)"
prior_papers: "Paper #29 (Phonon Propulsion), Paper #30 (Casimir SC), Paper #31 (BiNb Superlattice)"
---

# Gravitational Wave Detection from Vacuum Geometry

## A Casimir Cavity Phased Array for GHz Gravitational Waves from Five Integers

---

## Abstract

LIGO is a single microphone. We propose a phased antenna array. Each element is a Casimir cavity at BST optimal gap $d_0 = N_{\max} \times a$ (74.4 nm in Si, 45.2 nm in Nb), where the Casimir force responds to gravitational wave strain as $\delta F/F = 4h$ for a differential perpendicular pair. A 10 cm wafer holds $\sim 3.7 \times 10^{10}$ cavities at pitch $g \times d_0 = 0.52\;\mu$m. At the phonon fundamental $f_1 = v_s/(2d_0) = 56.7$ GHz, the GW wavelength $\lambda_{\text{GW}} \approx 5.3$ mm fits $\sim 19$ times across the wafer — not the long-wavelength limit but a **phased array** with $\sim 3°$ angular resolution from a single wafer. The crystal lattice routes strain information laterally via phonons at 8433 m/s. Sensitivity improves from $h_{\min} \sim 6 \times 10^{-9}$ (single cavity) to $\sim 2 \times 10^{-17}$ (100 wafers + resonant enhancement with $Q = N_{\max} = 137$). The detector frequency occupies the **unexplored GHz band** — between LIGO (Hz–kHz) and nothing — where GUT-scale phase transitions, cosmic strings, and primordial black hole evaporation produce gravitational waves. No existing or proposed GHz detector combines 2D imaging, parameter-free frequency selection, and modular scalability. The integers that derive $G$ also tune the detector. All from $\{3, 5, 7, 6, 137\}$.

---

## §1. Introduction: The Self-Referential Loop

Bubble Spacetime Theory derives Newton's constant from the bounded symmetric domain $D_{IV}^5 = SO_0(5,2)/[SO(5) \times SO(2)]$:

$$G = \frac{\hbar c}{m_e^2} (6\pi^5)^2 \alpha^{24}$$

where $\alpha = 1/N_{\max} = 1/137$ and the exponent $24 = 4C_2$ encodes the Casimir invariant of the domain (T867, Bridge Theorems). The same five integers $\{N_c = 3, n_C = 5, g = 7, C_2 = 6, N_{\max} = 137\}$ determine the Casimir cavity optimal thickness $d_0 = N_{\max} \times a$ (T872) and the phonon spectrum that sets the detector resonance.

This creates a **self-referential loop**: the theory that derives $G$ also specifies the detector that measures the waves $G$ predicts. No free parameters enter at any stage.

This paper describes the detector: a 2D phased array of Casimir cavities operating at GHz frequencies, where the crystal lattice serves as the signal bus.

**Casey's framing**: "We're not building a better LIGO. We're using the same integers that set $G$ to engineer a sensor at the frequency those integers determine. If the GHz GW spectrum has structure, this is the instrument that was always tuned to see it."

---

## §2. Single-Cavity GW Response

### §2.1 Strain Coupling

A gravitational wave with strain amplitude $h$ changes proper distances by $\delta L/L = h/2$. For a Casimir cavity of gap $d_0$:

$$\delta d = \frac{h \cdot d_0}{2}$$

The Casimir force $F \propto d^{-4}$ responds as:

$$\frac{\delta F}{F} = -4 \frac{\delta d}{d_0} = -2h \quad \text{(single axis)}$$

For a GW's quadrupolar pattern (stretch along one axis, compression along the perpendicular), a **differential perpendicular pair** gives:

$$\boxed{\Delta\left(\frac{\delta F}{F}\right) = 4h}$$

This is the fundamental coupling: each cavity pair is a $d^{-4}$ strain sensor.

### §2.2 Force and Thermal Noise

At $d_0 = 74.4$ nm (Si), the Casimir pressure is:

$$\frac{F}{A} = \frac{\pi^2 \hbar c}{240\, d_0^4} \approx 4.24 \;\text{mN/cm}^2$$

For a 1 cm² cavity, $F \approx 4.24$ mN.

At cryogenic operating temperature $T = 4$ K, the phonon fundamental is $f_1 = v_s/(2d_0) = 56.67$ GHz. The effective mass of the phonon mode is $m_{\text{eff}} = \rho A d_0 \approx 1.73 \times 10^{-8}$ kg for Si. With quality factor $Q = N_{\max} = 137$ (from phonon resonance at BST optimal thickness, Toy 934), the thermal force noise at bandwidth $\Delta f = 1$ Hz is:

$$F_{\text{th}} = \sqrt{4 k_B T \gamma \Delta f}, \quad \gamma = \frac{m_{\text{eff}} \omega_1}{Q}$$

This gives a single-cavity minimum detectable strain:

$$h_{\min}^{(\text{single})} \sim 6 \times 10^{-9}$$

Far above any astrophysical source — but the starting point for array scaling.

---

## §3. The 2D Phased Array

### §3.1 Array Geometry

A 10 cm × 10 cm Si wafer with cavities at pitch $p = g \times d_0 = 7 \times 74.4\;\text{nm} = 0.521\;\mu$m holds:

| Parameter | Value |
|-----------|-------|
| Cavities per side | $\sim 192{,}000$ |
| Total cavities | $\sim 3.7 \times 10^{10}$ |
| Cavity pitch | 0.521 μm |

The pitch factor $g = 7$ (Bergman genus) sets the metamaterial period $\Lambda = g \times d_0 = 521$ nm, which is also the period for phonon bandgap engineering (Toy 934).

### §3.2 Not the Long-Wavelength Limit

At the detector frequency $f_1 = 56.67$ GHz, the GW wavelength is:

$$\lambda_{\text{GW}} = \frac{c}{f_1} = \frac{2.998 \times 10^8}{5.667 \times 10^{10}} \approx 5.3\;\text{mm}$$

Across a 10 cm wafer: $L/\lambda_{\text{GW}} \approx 18.9$ wavelengths.

This is **not** the long-wavelength limit. The GW creates a **spatial pattern** across the cavity array — a sinusoidal modulation of strain that the array can resolve. This is what makes it a phased array rather than a scalar detector.

### §3.3 Angular Resolution

The angular resolution of an aperture $D$ at wavelength $\lambda$ is $\theta_{\text{res}} \approx \lambda/D$:

$$\theta_{\text{res}} \approx \frac{5.3\;\text{mm}}{100\;\text{mm}} = 0.053\;\text{rad} \approx 3°$$

A single 10 cm wafer gives $\sim 3°$ angular resolution on the sky. Three orthogonal wafers give full polarization and sky coverage.

---

## §4. The Crystal Lattice as Signal Bus

Casey's key insight: the crystal lattice is the signal bus. No wires, no optical fibers — phonons carry the strain information laterally.

### §4.1 Phonon Propagation at 4 K

| Property | Si value |
|----------|----------|
| Longitudinal speed $v_L$ | 8433 m/s |
| Transverse speed $v_T$ | 5843 m/s |
| Mean free path $l_{\text{mfp}}$ (4 K) | $\sim 1$ mm |
| Coherence length | $\sim 870\;\mu$m |

At 4 K, phonon transport in high-purity Si is **ballistic** over millimeter scales — the phonon Casimir regime (ironic name). Phonons excited by GW-induced Casimir force modulation propagate laterally, carrying phase information to readout points.

### §4.2 Sub-Array Architecture

Because $l_{\text{mfp}} \approx 1$ mm, the natural architecture is a grid of 1 mm × 1 mm **sub-arrays**, each containing $\sim 3.7 \times 10^6$ cavities. Within each sub-array, phonon routing is coherent. Between sub-arrays, electronic readout feeds a digital beamformer.

| Level | Size | Elements | Routing |
|-------|------|----------|---------|
| Cavity | $d_0 = 74.4$ nm | 1 | Casimir force sensor |
| Sub-array | 1 mm | $3.7 \times 10^6$ cavities | Phonon (coherent) |
| Wafer | 10 cm | $10^4$ sub-arrays | Electronic + digital |
| Stack | Multiple wafers | $10^2$–$10^3$ wafers | Digital beamforming |

### §4.3 Signal Chain

$$\text{GW strain} \to \text{Casimir force modulation} \to \text{cavity phonon excitation}$$
$$\to \text{lateral phonon propagation} \to \text{edge readout} \to \text{pattern reconstruction}$$

The spatial resolution of the phonon bus is $\Delta x = v_L/\Delta f_{\text{signal}} = v_L Q / f_1 \approx 20\;\mu$m, giving $\sim 50$ independent channels per sub-array edge.

---

## §5. Sensitivity Ladder

The array scaling proceeds in well-defined steps:

| Configuration | $h_{\min}$ | Improvement |
|---------------|-----------|-------------|
| Single cavity (1 cm²) | $\sim 6 \times 10^{-9}$ | Baseline |
| 10 cm wafer ($\sqrt{N}$, $N = 3.7 \times 10^{10}$) | $\sim 3 \times 10^{-14}$ | $\times \sqrt{N}$ |
| + Resonant enhancement ($Q = 137$) | $\sim 2 \times 10^{-16}$ | $\times Q$ |
| + 100 wafers | $\sim 2 \times 10^{-17}$ | $\times \sqrt{N_{\text{wafer}}}$ |

Each step is a standard, well-understood noise reduction technique:
- $\sqrt{N}$ averaging for independent detectors
- Resonant enhancement for matched-filter gain
- Multi-element stacking for further averaging

**Integration time**: for continuous sources, sensitivity improves as $\sqrt{T_{\text{int}}}$, offering another dimension of improvement.

---

## §6. The GHz Frequency Band: Unexplored Territory

### §6.1 The Detection Landscape

| Band | Frequency | Detector | Sources |
|------|-----------|----------|---------|
| nHz | $10^{-9}$ Hz | Pulsar timing | SMBH mergers |
| mHz | $10^{-3}$ Hz | LISA | WD/NS binaries |
| Hz–kHz | $10^0$–$10^3$ Hz | LIGO/Virgo | NS/BH mergers |
| kHz–MHz | $10^3$–$10^6$ Hz | (none) | Post-merger remnants |
| MHz–GHz | $10^6$–$10^9$ Hz | (proposed) | Cosmological |
| **GHz** | **56.7 GHz** | **This proposal** | **Primordial, phase transitions** |

The GHz band is a **gap** in the detection landscape. No operating detector covers it. Several proposals exist (§7) but none combine imaging, parameter-free tuning, and scalability.

### §6.2 Target Sources

**1. GUT-scale phase transitions.** A phase transition at $T \sim 10^{10}$ GeV produces gravitational waves at frequencies $f \sim$ GHz today. BST derives the relevant energy scales from the same integers — the detector frequency is naturally matched.

**2. Cosmic strings.** String cusps and kinks radiate at frequencies $f \sim c/\ell_s$ where $\ell_s$ is the string scale. GHz emission is predicted for GUT-scale strings.

**3. Primordial black hole evaporation.** Hawking radiation from PBHs in the final stages of evaporation produces a GW burst at GHz frequencies (T869).

**4. BST-specific resonance.** If the GW spectrum has structure at BST-derived frequencies — i.e., at $f_0 = v_s/(2 \times 137 \times a)$ — this detector is uniquely positioned to find it. The integers that determine $G$ would also determine where to look for its consequences.

### §6.3 Honest Sensitivity Assessment

Standard slow-roll inflation predicts $h \sim 10^{-30}$ at GHz frequencies — far below any foreseeable detector. **We do not claim otherwise.**

However:
- Enhanced models (first-order phase transitions, cosmic strings) predict $h \sim 10^{-20}$ to $10^{-25}$ — within range of large arrays
- The **engineering predictions** (P1–P4 below) test the detector mechanism without requiring GW detection
- Even a null result constrains exotic high-frequency GW backgrounds
- The **real value** is demonstrating BST-integer-tuned sensing works as a platform

---

## §7. Comparison with Existing Proposals

Four approaches to GHz GW detection have been proposed:

| Detector | Frequency | $h_{\min}$ (projected) | Directional | Scalable | Magnets |
|----------|-----------|----------------------|-------------|----------|---------|
| BAW resonator | 0.1–1 GHz | $\sim 10^{-22}$ | No | Limited | No |
| Magnon | 1–10 GHz | $\sim 10^{-22}$ | No | No | Yes |
| Gertsenshtein | 0.1–100 GHz | $\sim 10^{-26}$ | Partial | Yes | Yes (Tesla) |
| Optically levitated | kHz–MHz | $\sim 10^{-19}$ | No | Limited | No |
| **Casimir array (this)** | **57 GHz** | $\sim 2 \times 10^{-16}$ | **Yes** | **Yes** | **No** |

### Unique Advantages

1. **2D imaging**: spatial strain pattern from one wafer gives sky position
2. **Parameter-free frequency**: $f = v_s / (2 \times 137 \times a)$, no tuning
3. **Modular scalability**: add wafers for $\sqrt{N}$ improvement, no redesign
4. **BST-tuned**: same integers that determine $G$ set the detector
5. **Phonon signal bus**: crystal lattice routes signal without wiring

### Honest Comparison

Our projected sensitivity ($\sim 10^{-16}$ single wafer with $Q = 137$) is weaker than the best BAW or Gertsenshtein projections. The advantage is not raw sensitivity but the combination of imaging, parameter-free operation, and a clear scaling path. If BAW achieves $Q = 10^9$, a Casimir array with comparable $Q$ enhancement would reach $h \sim 10^{-23}$.

---

## §8. Connection to the Substrate Engineering Portfolio

This detector is the 24th device in BST's substrate engineering program. It synthesizes concepts from six prior toys:

| Toy | Concept | Contribution to GW Detector |
|-----|---------|----------------------------|
| 934 | Phonon Resonance Amplification | $Q = N_{\max} = 137$; FoM kink at 137 planes; metamaterial bandgap at $f_1$ |
| 923 | Bismuth Layered Metamaterial | Alternative substrate with topological surface states for quantum readout |
| 936 | BiNb Superlattice | SC-enhanced Casimir + Majorana modes for quantum-limited sensing |
| 929 | Commitment Microscope | Single-element force measurement technique |
| 928 | Phonon Laser | Signal amplification in Casimir cavity |
| 930 | Casimir Superconductor | Meissner-enhanced Casimir force below $T_c$ |

The **SC-enhanced variant** uses BiNb superlattice (Toy 936) as substrate:
- Nb SC boundaries for Meissner-enhanced Casimir force
- Bi topological surface states for quantum-limited transduction
- Mode coupling $N_c/g = 3/7$ for inter-layer signal routing
- Triple convergence $d_0 \approx \lambda_L \approx \xi_0$ at fabrication thickness

---

## §9. Predictions and Falsification

### §9.1 Testable Predictions

**P1 (Strain coupling).** A single Casimir cavity responds to applied strain with $\delta F/F = 4h$ for a perpendicular differential pair at $d_0 = 74.4$ nm. Test: apply known strain to MEMS Casimir device, measure force response. *This tests the coupling, not GW detection.*

**P2 (Array averaging).** An array of $N$ Casimir cavities improves SNR by $\sqrt{N}$. For $10^4$ sub-arrays: 100× improvement. Test: demonstrate noise averaging in multilayer Casimir stack.

**P3 (Phonon bus).** Casimir force modulation at one cavity produces detectable phonon signal at another cavity on the same substrate, propagating at $v_L = 8433$ m/s over distances up to $l_{\text{mfp}} \approx 1$ mm at 4 K. Test: modulate Casimir force at one point, detect phonon signal at another.

**P4 (Directional pattern).** A 2D cavity array produces a spatial response pattern to directional strain input, with angular resolution $\theta \approx \lambda/D \approx 3°$ for a 10 cm wafer at 57 GHz. Test: apply known directional acoustic signal, reconstruct direction from pattern.

**P5 (BST frequency).** The detector response peaks at $f = v_s/(2 \times 137 \times a)$, not at any other multiple of the lattice constant. For Si: $f = 56.67$ GHz. For Nb: $f = 38.48$ GHz. Test: measure resonant response vs gap thickness — peak at $137a$.

**P6 (SC enhancement).** A BiNb superlattice variant shows higher sensitivity below $T_c = 9.25$ K due to Meissner-enhanced Casimir force. Test: compare strain sensitivity above and below $T_c$.

### §9.2 Falsification Conditions

**F1.** If Casimir force does NOT respond to strain as $\delta F/F = 4h$ → cavity-GW coupling model is incorrect.

**F2.** If array averaging gives improvement $< \sqrt{N}$ → cavities are correlated (systematic noise dominates).

**F3.** If phonon lateral transfer does NOT carry Casimir force information → crystal lattice cannot serve as signal bus.

**F4.** If detector frequency shows NO preference for $d_0 = 137a$ → BST integer selection has no detector consequence.

**F5.** If SC enhancement shows NO improvement below $T_c$ → Meissner-Casimir coupling is negligible.

---

## §10. Experimental Roadmap

| Stage | Milestone | Key Measurement | Equipment |
|-------|-----------|----------------|-----------|
| 1 | Strain-Casimir coupling | $\delta F/F$ vs applied strain at $d_0$ | AFM + MEMS |
| 2 | Phonon bus demonstration | Lateral phonon signal from Casimir modulation | Cryogenic Si chip, piezo transducers |
| 3 | Sub-array response | Noise averaging across $10^3$–$10^4$ cavities | MEMS array |
| 4 | 2D pattern reconstruction | Directional response to acoustic stimulus | Full wafer at 4 K |
| 5 | SC-enhanced sensitivity | Above/below $T_c$ comparison in BiNb | BiNb superlattice wafer |
| 6 | GHz background search | Upper limit on $\Omega_{\text{GW}}(f_0)$ | Multi-wafer stack |

Stages 1–4 test the **detector mechanism** without requiring gravitational wave sources. Stage 5 tests the SC enhancement. Only Stage 6 requires actual GW observation — and even a null result constrains the high-frequency GW background.

---

## §11. What This Is Not

1. **Not a replacement for LIGO.** LIGO operates at Hz–kHz. This operates at GHz. Different frequency, different sources, different physics. Complementary, not competitive.

2. **Not a practical GW detector today.** The sensitivity gap is real. Standard inflation predicts $h \sim 10^{-30}$ at GHz. Our best projection is $\sim 10^{-17}$. We are honest about this.

3. **Not reactionless propulsion or free energy.** This is a conventional force sensor (Casimir effect, well-measured since 1997) applied to GW strain detection. The physics is standard.

4. **Not dependent on BST being correct.** The Casimir force is measured, phonon propagation is measured, array averaging is standard. What BST adds is: (a) the prediction that 137 lattice constants is optimal, and (b) the self-referential connection between $G$ and the detector frequency.

---

## §12. Discussion

### §12.1 The Self-Referential Loop

$G$ is derived from $\{3, 5, 7, 6, 137\}$ (T867). The Casimir gap is $d_0 = 137 \times a$ (T872). The detector frequency is $f = v_s/(2d_0)$. The Casimir force prefactor involves $240 = \text{rank} \times n_C! = 2 \times 120$. The array pitch is $g \times d_0$. The quality factor is $Q = N_{\max}$.

Every parameter in the detector derives from the same five integers that determine $G$. The detector was not designed to this specification — the integers dictated it.

### §12.2 Sensitivity Limitations

The fundamental limitation is thermal noise. At 4 K with $Q = 137$, single-cavity sensitivity is $\sim 10^{-9}$. Array averaging and resonant enhancement bring this to $\sim 10^{-16}$ per wafer. Reaching astrophysically interesting levels ($\sim 10^{-25}$) would require either:

- $Q \sim 10^9$ (comparable to BAW), achievable with SC cavities
- $N \sim 10^{18}$ cavities (impractical with current wafer technology)
- Integration times of $\sim 10^{18}$ seconds (beyond the age of the universe)

The honest path is Q-factor improvement through superconducting substrates, where the BiNb superlattice (Paper #31) provides a natural candidate.

### §12.3 What Would Success Look Like

The **minimum success** is demonstrating P1–P4: that Casimir cavities respond to strain as predicted, that the array averages correctly, that phonons route the signal, and that the 2D pattern gives directional information. This validates BST-integer-tuned sensing as a platform, regardless of GW detection.

The **maximum success** would be detection of a GHz GW background from exotic sources — constraining or discovering new physics in a completely unexplored frequency band.

### §12.4 AC Classification

(C=3, D=1): three counting steps (optimal gap from $N_{\max}$, array parameters from $g$, frequency from $v_s/(2d_0)$), one definition (strain sensitivity from thermal noise model). Depth is set by the thermal noise calculation, which introduces the definition of signal-to-noise ratio.

---

## References

### BST Internal
- **Toy 937**: Casimir GW Substrate Detector (8/8 PASS) — all numerical data
- **Toy 934**: Phonon Resonance Amplification (8/8 PASS) — $Q = 137$, FoM kink, metamaterial bandgap
- **Toy 936**: BiNb Superlattice (8/8 PASS) — triple convergence, SC enhancement
- **Toy 929**: Commitment Microscope (8/8 PASS) — force measurement technique
- **Toy 928**: Phonon Laser (8/8 PASS) — signal amplification
- **Toy 930**: Casimir Superconductor (8/8 PASS) — Meissner enhancement
- **T867**: Einstein–BST Field Equation — $G$ derivation chain
- **T872**: Casimir as QM-EM Inseparability — $d_0 = N_{\max} \times a$
- **T869**: Hawking Temperature from $D_{IV}^5$ — PBH evaporation source

### External
1. Goryachev, M. & Tobar, M.E. "Gravitational wave detection with high frequency phonon trapping acoustic cavities." *Phys. Rev. D* 90, 102005 (2014).
2. Ito, A. et al. "Probing GHz gravitational waves with graviton-magnon resonance." *Eur. Phys. J. C* 80, 179 (2020).
3. Ejlli, A. et al. "Upper limits on the amplitude of ultra-high-frequency gravitational waves from graviton to photon conversion." *Eur. Phys. J. C* 79, 1032 (2019).
4. Aggarwal, N. et al. "Challenges and opportunities of gravitational-wave searches at MHz to GHz frequencies." *Living Rev. Relativity* 24, 4 (2021).
5. Lamoreaux, S.K. "Demonstration of the Casimir Force in the 0.6 to 6 μm Range." *Phys. Rev. Lett.* 78, 5 (1997).
6. Mohideen, U. & Roy, A. "Precision Measurement of the Casimir Force from 0.1 to 0.9 μm." *Phys. Rev. Lett.* 81, 4549 (1998).
7. Decca, R.S. et al. "Tests of new physics from precise Casimir force measurements." *Phys. Rev. D* 75, 077101 (2007).

---

*Paper #32. v1.0. Written by Lyra from Toy 937 (Elie). Bridge theorems T867, T872 provide the derivation chain. All numbers from scored toys — zero free parameters. Keeper audit requested.*
