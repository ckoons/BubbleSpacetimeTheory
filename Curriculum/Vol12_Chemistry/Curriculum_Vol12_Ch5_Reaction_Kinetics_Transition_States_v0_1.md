---
title: "BST Physics Curriculum Vol 12 Ch 5 — Reaction Kinetics + Transition States v0.4 (Calibration #23 substance-floor refill)"
author: "Lyra (Claude 4.7) [Vol 12 joint with Elie]"
date: "2026-05-23 Saturday EDT (Tier 1 Cal #104/#23 refill per Keeper redirect)"
chapter: "Vol 12 Ch 5"
status: "v0.4 chapter-grade narrative refilled per Calibration #23 substance-floor. Reaction kinetics: rate laws + Arrhenius equation + transition state theory (Eyring); BST substrate-cartography: activation energy = substrate K-type barrier; reaction rate = substrate-tick rate × Casimir-eigenvalue spread; catalysis = substrate K-type pathway shortcut. Per Calibration #19."
prerequisites: ["Vol 12 Ch 2-4 bonding + MO + thermo", "Vol 6 Ch 1 temperature substrate-reading", "T2405 Koons tick t_substrate = t_Planck · α^(C_2²) ≈ 10⁻¹²⁰ s"]
related: ["Arrhenius equation k = A exp(−E_a/RT)", "Transition state theory (Eyring 1935): k = (k_B T/h) exp(−ΔG‡/RT)", "Rate law + reaction order classification", "Catalysis (homogeneous, heterogeneous, enzymatic)", "T2405 Koons tick substrate-clock", "T2417 4-Zone Commitment Cycle"]
---

# Vol 12 Chapter 5 — Reaction Kinetics + Transition States

## Chapter motivation

Thermodynamics tells us IF a reaction is spontaneous (ΔG < 0); kinetics tells us HOW FAST. Most spontaneous reactions don't happen at observable rates without catalysis. Standard chemistry treatment: rate laws (rate = k [A]^m [B]^n), reaction orders, Arrhenius equation (k = A exp(−E_a/RT)), transition state theory (Eyring 1935: k = (k_B T/h) exp(−ΔG‡/RT)), catalysis mechanisms (homogeneous + heterogeneous + enzymatic). BST substrate-cartography reading: reaction rates are substrate computational throughput at given temperature; activation energy is a substrate K-type representation barrier; catalysis is substrate-pathway-shortcut via alternative K-type intermediate.

## Section 5.0b — Reader-grade 3-level pedagogy

**Level 1**: Reaction rate = substrate-tick computational rate × Casimir-eigenvalue spread. Activation energy E_a = substrate K-type barrier between reactant and product K-types. Catalysts lower E_a by providing alternative substrate-K-type pathway. Arrhenius equation k = A exp(−E_a/RT) is substrate Boltzmann-distribution barrier-crossing.

**Level 2 (graduate-chemist accessible)**: Rate laws: rate = −d[A]/dt = k [A]^m [B]^n where m + n is reaction order (zeroth, first, second, fractional). Integrated rate laws: first-order ln[A] = ln[A]₀ − kt (exponential decay; half-life t_{1/2} = ln2/k); second-order 1/[A] = 1/[A]₀ + kt; zeroth-order [A] = [A]₀ − kt. Arrhenius equation k = A exp(−E_a/RT): A = pre-exponential factor (collision frequency × steric factor); E_a = activation energy. Plot ln k vs 1/T gives slope −E_a/R. Transition state theory (Eyring 1935): k = (k_B T/h) · exp(−ΔG‡/RT) = (k_B T/h) · exp(ΔS‡/R) · exp(−ΔH‡/RT) where ‡ denotes activated complex. ΔG‡ activation free energy; ΔS‡ activation entropy reflects geometric constraints of activated complex; ΔH‡ activation enthalpy ≈ E_a − RT. Catalysis: homogeneous (catalyst + reactants same phase, e.g., acid-base catalysis), heterogeneous (catalyst different phase, e.g., Pt surface for H₂ + N₂ → NH₃ Haber process), enzymatic (substrate-specific protein catalysts, rate enhancements 10⁶-10²⁰× per Vol 13 Ch 9). Michaelis-Menten kinetics for enzymes: v = V_max [S]/(K_M + [S]). BST substrate-cartography reading: reaction rate = substrate-tick rate (t_substrate = t_Planck · α^(C_2²) ≈ 10⁻¹²⁰ s per T2405 Koons tick) × Casimir-eigenvalue spread × Boltzmann barrier-crossing probability exp(−E_a/k_B T). Activation energy E_a = substrate K-type representation barrier between reactant K-type and product K-type — energy required to traverse the K-type manifold via the transition-state K-type intermediate. Catalysts provide alternative substrate K-type pathway with lower barrier. Per T2417 4-Zone Commitment Cycle: reaction = substrate commitment-cycle traversing Zones 1→2→3 with the transition state being the Zone-2 commitment-processing peak.

**Level 3 (5th-grader accessible)**: Even reactions that "want to happen" (negative ΔG) need to climb over an energy hill called the activation barrier. The taller the hill, the slower the reaction. Heating things up gives molecules more energy to climb the hill faster. Catalysts (like enzymes in your body) provide shortcuts over lower hills — they don't change the start or end, just the path. BST framework says these energy hills are substrate "K-type barriers" — moving from one substrate building-block configuration to another costs energy, and the cost determines the rate.

## Section 5.1 — Rate Laws and Reaction Order

Rate = k [A]^m [B]^n. Order m + n determined by mechanism (rate-limiting step), not stoichiometry.

Integrated rate laws by order:
- Zeroth: [A] = [A]₀ − kt (linear decay)
- First: ln[A] = ln[A]₀ − kt (exponential decay; t_{1/2} = ln2/k = 0.693/k)
- Second: 1/[A] = 1/[A]₀ + kt

Half-life provides experimental measure of rate constant.

## Section 5.2 — Arrhenius Equation

k = A exp(−E_a/RT). Pre-exponential factor A combines collision frequency + steric factor. Activation energy E_a measured from slope of ln k vs 1/T plot.

Typical E_a values: 50-250 kJ/mol for chemical reactions; catalyzed reactions much lower (enzymatic 25-50 kJ/mol).

BST framing: Boltzmann barrier-crossing exp(−E_a/k_B T) = substrate fraction with sufficient K-type Casimir-eigenvalue to traverse barrier.

## Section 5.3 — Transition State Theory (Eyring)

Eyring equation: k = (k_B T/h) exp(−ΔG‡/RT) = (k_B T/h) exp(ΔS‡/R) exp(−ΔH‡/RT).

ΔS‡ negative for tight associative complexes (orientation cost); ΔS‡ positive for dissociative complexes.

BST framing: transition state = Zone-2 commitment-processing peak K-type intermediate in substrate 4-Zone cycle.

## Section 5.4 — Catalysis

Three classes:
- Homogeneous: catalyst + reactants same phase (acid/base, transition metal complexes)
- Heterogeneous: different phase (Pt for hydrogenation, V₂O₅ for SO₂ → SO₃)
- Enzymatic: protein catalysts (Vol 13 Ch 9 metabolism)

Michaelis-Menten enzyme kinetics: v = V_max [S]/(K_M + [S]). At [S] >> K_M, v → V_max (saturation); at [S] << K_M, v → (V_max/K_M)[S] (first-order in [S]).

BST framing: catalysis = alternative substrate K-type pathway with lower K-type barrier.

## Section 5.5 — Connection

- Vol 12 Ch 2-4 Chemical bonding + thermodynamics (prerequisites)
- Vol 6 Ch 1 Temperature as substrate-reading (Boltzmann factor origin)
- T2405 Koons tick substrate-clock (rate ultimate substrate scale)
- T2417 4-Zone Commitment Cycle (transition state = Zone-2 peak)
- Vol 13 Ch 9 Metabolism (enzymatic catalysis biological full treatment)
- Vol 12 Ch 6 Spectroscopy (transition state characterization)

**Honest scope**: Substrate K-type barrier framework provides organizing principle; specific quantitative rate-constant derivations from substrate Hamiltonian remain multi-year SP-31 program. Enzymatic rate enhancements 10⁶-10²⁰× are empirically tabulated, not yet substrate-derived.

— Lyra, Vol 12 Ch 5 v0.4 chapter-grade narrative REFILLED per Cal #104 + Calibration #23, Saturday 2026-05-23 EDT
