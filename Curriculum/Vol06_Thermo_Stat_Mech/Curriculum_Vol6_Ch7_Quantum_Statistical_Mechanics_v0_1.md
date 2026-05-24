---
title: "Vol 6 Chapter 7 — Quantum Statistical Mechanics"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; Bose-Einstein + Fermi-Dirac; BEC; blackbody; substrate Pin(2) particle-statistics origin"
volume: "Vol 6 Thermodynamics and Statistical Mechanics from D_IV⁵"
chapter: 7
load_bearing: "Bose-Einstein / Fermi-Dirac distributions from substrate Pin(2) double-cover; blackbody = substrate photon K-type spectrum; BEC = macroscopic substrate ground-state occupation"
---

# Chapter 7 — Quantum Statistical Mechanics

## Level 1 — one sentence

Quantum statistical mechanics — Bose-Einstein and Fermi-Dirac distributions, blackbody radiation, Bose-Einstein condensation, Fermi gases, ideal-gas heat capacities at low temperature — is the substrate's K-type spectrum populated with Pin(2)-determined particle statistics (bosons for integer-spin K-types, fermions for half-integer), with the discrete substrate spectrum producing all the quantum corrections to classical equipartition.

## Level 2 — graduate-physicist precision

### 7.1 Indistinguishable particles in stat mech

Quantum statistical mechanics applies to identical indistinguishable particles. The grand canonical partition function for a system of identical particles in single-particle states $\{|k\rangle\}$ with energies $\epsilon_k$:

$$\Xi = \prod_k \Xi_k$$

where the per-mode grand partition function depends on the particle statistics:

- **Bosons** (any occupation number $n_k = 0, 1, 2, \ldots$): $\Xi_k^B = \sum_{n=0}^\infty e^{-n\beta(\epsilon_k - \mu)} = \frac{1}{1 - e^{-\beta(\epsilon_k - \mu)}}$
- **Fermions** ($n_k = 0$ or $1$ by Pauli): $\Xi_k^F = 1 + e^{-\beta(\epsilon_k - \mu)}$

Substrate-mechanism reading: occupation number $n_k$ corresponds to the substrate's K-type multiplicity. Bosons can multiply-occupy (substrate Pin(2) integer-weight K-types accept additive amplitudes); fermions cannot (substrate Pin(2) half-integer-weight K-types are excluded by antisymmetrization, Volume 5 Chapter 9).

### 7.2 Bose-Einstein distribution

For bosons, the mean occupation of mode $k$:

$$\langle n_k\rangle_{BE} = \frac{1}{e^{\beta(\epsilon_k - \mu)} - 1}$$

Bose-Einstein distribution. Always positive. Diverges as $\epsilon_k \to \mu$ — the signature of Bose-Einstein condensation.

### 7.3 Fermi-Dirac distribution

For fermions, the mean occupation:

$$\langle n_k\rangle_{FD} = \frac{1}{e^{\beta(\epsilon_k - \mu)} + 1}$$

Always between 0 and 1 (Pauli). At $T = 0$: step function — $n_k = 1$ for $\epsilon_k < \mu$, $n_k = 0$ for $\epsilon_k > \mu$. The Fermi energy $E_F = \mu(T=0)$ separates filled from empty states.

### 7.4 Blackbody radiation

A blackbody is a perfect thermal-radiation emitter. The radiation field is a Bose gas (photons are bosons, spin 1) with $\mu = 0$ (photons can be freely created/destroyed). The Bose-Einstein distribution for photons gives:

$$\langle n(\omega)\rangle = \frac{1}{e^{\hbar\omega/k_BT} - 1}$$

Spectral energy density (Planck distribution):

$$u(\omega, T)d\omega = \frac{\hbar\omega^3}{\pi^2 c^3} \cdot \frac{d\omega}{e^{\hbar\omega/k_BT} - 1}$$

Limiting cases:
- $\hbar\omega \ll k_BT$ (Rayleigh-Jeans): $u \approx \omega^2 k_BT/(\pi^2 c^3)$ — classical equipartition
- $\hbar\omega \gg k_BT$ (Wien): $u \approx \hbar\omega^3 e^{-\hbar\omega/k_BT}/(\pi^2 c^3)$ — exponential cutoff

Integrated spectrum (Stefan-Boltzmann): $u_{\text{total}} = (8\pi^5/15) (k_BT)^4 / (hc)^3 = aT^4$ with $a$ the radiation constant.

Substrate-mechanism reading: the substrate's photon K-types (spin 1, massless, Pin(2) integer-weight) are populated thermally per the Bose-Einstein distribution. The blackbody spectrum is the substrate's photon-K-type thermal distribution function.

### 7.5 The ultraviolet catastrophe and Planck's revolution

Classical Rayleigh-Jeans for blackbody predicted $u(\omega) \propto \omega^2 T$ — diverges as $\omega \to \infty$ (ultraviolet catastrophe). Real blackbodies have a high-frequency cutoff. Planck 1900 introduced the quantization hypothesis $E = n\hbar\omega$ to fix the divergence; this was the first appearance of $\hbar$ in physics.

Substrate-mechanism reading: the discrete substrate K-type spectrum (Volume 5 Chapter 4) intrinsically cuts off high-energy modes. The substrate doesn't have "infinite resolution" — its K-types are quantized; high-$\omega$ modes are exponentially suppressed (Wien limit). No ultraviolet catastrophe at the substrate level.

### 7.6 Bose-Einstein condensation

For a gas of $N$ bosons in 3D below the critical temperature

$$T_c = \frac{1}{k_B}\left(\frac{n}{\zeta(3/2)}\right)^{2/3} \frac{h^2}{2\pi m}$$

(with $n = N/V$), a macroscopic fraction of particles condense into the ground state. The condensate fraction:

$$\frac{N_0}{N} = 1 - (T/T_c)^{3/2}$$

for $T < T_c$.

First observed experimentally Cornell-Wieman-Ketterle 1995 (Nobel 2001) — rubidium and sodium atomic gases at nanokelvin temperatures.

Substrate-mechanism reading: BEC is the substrate's macroscopic occupation of the ground-state K-type. Below $T_c$, the substrate's K-type Boltzmann distribution can no longer accommodate all $N$ atoms in excited K-types; the remainder pile into the ground state. The condensate is the substrate's coherent K-type accumulation.

### 7.7 Fermi gases and white dwarfs

For non-relativistic fermions at $T = 0$: all states below the Fermi energy $E_F$ are filled. Free-electron gas:

$$E_F = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$$

Mean energy per particle: $\langle E\rangle = (3/5)E_F$. Degeneracy pressure $P = (2/5) n E_F$.

Astrophysical application — white dwarfs: electron degeneracy pressure supports the star against gravity. Chandrasekhar mass limit $M_{Ch} \approx 1.4 M_\odot$ — above this, electron degeneracy fails and the star collapses to neutron star or black hole.

Substrate reading: the Fermi gas's degeneracy is the substrate's Pin(2) half-integer-weight K-type filling pattern; the substrate cannot multiply-occupy fermion K-types, producing the degeneracy pressure.

### 7.8 Heat capacity of solids: Einstein and Debye

Classical equipartition gives $C_V = 3R$ per mole (Dulong-Petit) for solids — but experimentally $C_V \to 0$ as $T \to 0$. Einstein 1907: model atoms as quantum harmonic oscillators with frequency $\omega_E$. Each oscillator contributes $\hbar\omega_E / (e^{\hbar\omega_E/k_BT} - 1)$ to internal energy. At low $T$: $C_V \propto e^{-\hbar\omega_E/k_BT}$ — exponentially small.

Debye 1912: extended to phonon modes with frequencies from 0 to a Debye cutoff $\omega_D$. Gives $C_V \propto T^3$ at low $T$ — matches experiment.

Substrate-mechanism reading: solids are substrate K-type lattices; phonons are substrate vibrational K-types (Volume 9 Chapter 7). Low-T heat capacity is the substrate's exponential suppression of high-energy K-type modes.

### 7.9 Worked example: photon gas in a cavity

For thermal radiation in a cubical cavity of side $L$ at temperature $T$:
- Photon density: $n_\gamma = (2\zeta(3)/\pi^2)(k_BT/\hbar c)^3$
- Energy density: $u = aT^4$ with $a = \pi^2 k_B^4/(15\hbar^3 c^3)$
- Entropy density: $s = (4/3)u/T$
- Pressure: $P = u/3$

For $T = 300$ K: $n_\gamma \approx 5 \times 10^{14}$/m³ — about half a quadrillion photons per cubic meter at room temperature. Substrate reading: the substrate has $5 \times 10^{14}$ photon-K-type quanta occupied per m³ at thermal coupling 300 K.

### 7.10 Pauli paramagnetism and Landau diamagnetism

For an electron gas in a magnetic field $B$:
- Spin Zeeman energy: $\pm \mu_B B$
- More electrons spin-aligned with $B$ → paramagnetic susceptibility $\chi_P > 0$
- Orbital motion: cyclotron orbits in $B$; spread over $B$ direction gives diamagnetic susceptibility $\chi_D < 0$
- Net: $\chi_{\text{total}} = \chi_P - \chi_D > 0$ for most metals

Substrate reading: spin Zeeman is the substrate's Pin(2) coupling to external EM K-types (Volume 5 Chapter 3); cyclotron orbits are substrate Lorentz-coupled K-type motion.

### 7.11 K-audit anchors

- **Volume 5 Chapter 9**: spin-statistics theorem from substrate Pin(2) double cover
- **Chapter 5 of this volume**: partition function on $D_{IV}^5$
- **Casey's Principle**: counting at depth 0 → bosons count multi-occupancy, fermions count single-occupancy
- **Mayer-Jensen 1949** (L1 ESTABLISHED): nuclear shell model (Fermi gas application)

## Level 3 — 5th-grader accessibility

Quantum particles come in two flavors: **bosons** (photons, gluons, Higgs) and **fermions** (electrons, quarks, neutrinos). Bosons can pile up in one state (Bose-Einstein condensation: cool a gas of bosons enough and they ALL fall into the lowest state, becoming one big quantum object). Fermions can't share (Pauli exclusion: each state holds at most one fermion). This explains:
- **Blackbody radiation**: photons (bosons) fill modes according to BE distribution; that's the Planck curve, no UV catastrophe because high-frequency modes are quantum-suppressed.
- **Specific heats**: at low T, the substrate can't reach excited K-type modes; heat capacities drop to zero (the third law).
- **White dwarfs**: electrons (fermions) can't pile up; their degeneracy pressure holds up the star against gravity. Above 1.4 solar masses, gravity wins → neutron star or black hole.
- **Lasers**: photons (bosons) like to share, so once you get a few photons in one mode, more pile in. That's stimulated emission, the basis of lasers.

All of this comes from the substrate's Pin(2) double cover deciding which particles can share K-types.

---

## What comes next

Chapter 8 develops phase transitions — order parameters, mean-field theory, Ising model, critical exponents.

## Where to look this up

- **Bose-Einstein, Fermi-Dirac**: Pathria Ch 6-8; Huang Ch 8-9
- **BEC**: Cornell-Wieman-Ketterle 1995; Pitaevskii and Stringari, *Bose-Einstein Condensation*
- **White dwarfs**: Chandrasekhar 1931; Shapiro and Teukolsky, *Black Holes, White Dwarfs, and Neutron Stars*
- **Debye model**: Debye 1912; Ashcroft and Mermin Ch 23
- **BST anchors**: Volume 5 Chapter 9 spin-statistics; Chapter 5 partition function
