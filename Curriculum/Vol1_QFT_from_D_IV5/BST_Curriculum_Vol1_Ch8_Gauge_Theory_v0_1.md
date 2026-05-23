---
title: "Vol 1 Chapter 8 — Gauge Theory: $SU(3) \\times SU(2) \\times U(1)$ from the Substrate"
author: "Keeper (author pass)"
date: "2026-05-23 Saturday"
status: "v0.2 — Keeper author-voice pass; preserves v0.1 substance (SM gauge group forced from BST primaries, color confinement as topological obstruction, Weinberg angle sin²θ_W = N_c/c_3 at 0.19%, three generations from Q⁵ cohomology, Five-Absence predictions, Higgs cross-link to Vol 2 Ch 9, T2477 gauge fields as Bergman bundle connections)"
volume: "Vol 1 Quantum Field Theory from D_IV⁵"
chapter: 8
---

# Chapter 8 — Gauge Theory: $SU(3) \times SU(2) \times U(1)$ from the Substrate

The Standard Model's gauge group is $SU(3) \times SU(2) \times U(1)$. The three factors carry, in standard physics, the three non-gravitational forces: $SU(3)$ for the strong interaction with eight gluons, $SU(2)$ for the weak interaction with three intermediate bosons, $U(1)$ for the parent of electromagnetism after the Higgs mechanism mixes it with the electroweak sector. The total dimension of the gauge group is $8 + 3 + 1 = 12$, the total number of fundamental gauge bosons (counting the W$^{\pm}$, Z, photon, and eight gluons) in the Standard Model.

In standard physics, the choice of this specific gauge group is empirical. It is what experiments revealed; it is what the Standard Model's builders wrote down to fit observation; it carries with it the long-standing puzzle of *why these groups and not others*. Grand unified theories tried to embed $SU(3) \times SU(2) \times U(1)$ inside a larger simple group (typically $SU(5)$ or $SO(10)$ or larger), hoping to derive the Standard Model's structure from a higher symmetry; the GUT programs encountered increasingly stringent experimental constraints on the proton lifetime, and the current bounds make most GUT scenarios incompatible with observation.

In BST, the gauge group is not chosen. It is *forced*. The three factors come from three distinct features of the substrate $D_{IV}^5$:

- **$SU(3)$ color** comes from $N_c = 3$ — the substrate's color multiplicity, derived in Chapter 3 by four independent forcing arguments.
- **$SU(2)$ weak** comes from rank $= 2$ — the substrate's symmetric-space rank, derived in Chapter 3 by four independent forcing arguments.
- **$U(1)$ hypercharge** comes from the $SO(2)$ factor of the isotropy decomposition $SO(5) \times SO(2)$ — the substrate's natural internal phase symmetry, derived in Volume 0 Chapter 4.

The total Lie-algebra dimension is then

$$\dim G_{SM} \;=\; (N_c^2 - 1) + (\text{rank}^2 - 1) + 1 \;=\; 8 + 3 + 1 \;=\; 12 \;=\; N_c \cdot \text{rank} \cdot 2,$$

a clean BST-primary factorization. The substrate did not choose the gauge group; the gauge group is what the substrate has.

What this chapter shows is the structural derivation, in some detail, plus three consequences that turn out to follow: color confinement as a topological obstruction (rather than a dynamical phenomenon), three fermion generations (rather than two or four), and a five-absence prediction set that contains five of the Standard-Model-and-Beyond program's most-searched-for phenomena that BST predicts *do not exist*.

## 8.1 $SU(3)$ color from $N_c = 3$

The color gauge group $SU(3)$ is what binds quarks into hadrons. Each quark carries one of three color charges; color-singlet bound states (mesons made of quark-antiquark pairs, baryons made of three quarks) are the only observable particles; the eight gluons that mediate the strong force live in the adjoint representation of $SU(3)$.

The substrate origin is direct: $N_c = 3$ is the substrate's color multiplicity, with three independent color-charge directions in the substrate's K-type structure. The $SU(N_c) = SU(3)$ gauge group is what acts unitarily on the three-color substrate states. The gluon count is $\dim SU(N_c) = N_c^2 - 1 = 8$, exact.

A structural feature that has no analogue in standard QCD is the **color-singlet triangle**. The number of color-singlet combinations of $N_c$ quark-antiquark pairs is the triangle number

$$T_{N_c} \;=\; \frac{N_c (N_c+1)}{2} \;=\; 6,$$

which equals the BST primary $C_2$ — the substrate's lowest non-trivial Casimir eigenvalue. The matching is not coincidence. The factor of 6 that appears in the proton-to-electron mass ratio $m_p/m_e = 6\pi^5$ (which we will derive in Volume 2 Chapter 6) is precisely this triangle number: three quarks plus three independent quark-antiquark gluon channels close the color winding at $T_{N_c} = 6$. The substrate-side identification ties the Casimir, the color-singlet counting, and the mass-ratio formula into one structural unit. This is the kind of integer-web cross-coupling that we discussed at length in Volume 0 Chapter 6.

### Color confinement as topology

Standard QCD treats color confinement — the experimental fact that isolated quarks have never been observed — as a *dynamical* phenomenon, arising from the running of the strong coupling and the formation of confining flux tubes at low energies. The proof that QCD confines is, even now, formally open (it is one of the Millennium Problems, although BST has its own resolution argued in the Y-M papers).

In BST, confinement is *structural*. A single quark cannot close its color winding on the substrate's K-type structure, because no one-quark color-singlet K-type representation exists on $H^2(D_{IV}^5)$. The substrate admits color-singlet K-types only for $N_c$ quarks (baryons), for quark-antiquark pairs (mesons), and for the $N_c^2 = 9$ gluon-plus-singlet adjoint structure. Isolated quarks cannot exist because the substrate cannot represent them — they are forbidden by the topology of the substrate's K-type lattice, not by the dynamics of a coupling that runs.

This recasts confinement from a hard dynamical-QFT problem into a structural-topological fact about $D_{IV}^5$. The substrate-side derivation is cleaner than the standard-QCD derivation, and the prediction is the same: no free quarks, ever.

## 8.2 $SU(2)$ weak from rank $= 2$

The weak interaction's gauge group is $SU(2)$, with three generators that give the $W^{\pm}$ and $Z$ bosons (after Higgs mixing with $U(1)$ produces the physical $Z$ and the photon). Left-handed fermions pair up into weak isospin doublets: the electron neutrino with the electron, the up quark with the down quark, and so on.

The substrate origin is the rank-2 structure of $D_{IV}^5$. The substrate carries two algebraically independent Casimir generators (Chapter 5 develops the Casimir algebra in detail), labeled by two independent K-type quantum numbers. The rank-2 doublet structure is what gives the substrate its left-handed pair structure, and the $SU(rank) = SU(2)$ gauge group is what acts on the doublet.

The three weak bosons are $\dim SU(\text{rank}) = \text{rank}^2 - 1 = 3$, exact.

The chirality structure of the weak interaction — that left-handed fermions form doublets and right-handed fermions are singlets — comes from the Pin(2) double cover of the substrate's rank-2 isotropy (Volume 0 Chapter 4). The Pin(2) double cover carries a $\mathbb{Z}_2$ grading; left-handed and right-handed substrate states sit in the two sectors of the grading. The weak interaction's $SU(2)$ acts non-trivially on left-handed states (the $\mathbb{Z}_2$-positive sector) and trivially on right-handed states (the $\mathbb{Z}_2$-negative sector). This is the substrate's structural origin of weak-sector chirality.

Parity violation in the weak sector (Volume 0 Chapter 4's Möbius-locality argument) is the consequence: the substrate's parity operator does not commute with the weak Hamiltonian *because* the chirality asymmetry is built into the weak coupling. There is no other sector where the chirality structure couples this way, so parity is conserved in strong and electromagnetic and violated only in weak. The substrate predicts where the violation happens.

## 8.3 $U(1)$ hypercharge and electroweak unification

The third gauge factor is abelian. After accounting for $SU(N_c)$ color and $SU(\text{rank})$ weak isospin, the substrate has one residual one-parameter symmetry — the $SO(2)$ factor of the isotropy $SO(5) \times SO(2)$ — which produces $U(1)$.

This $U(1)$ is the **hypercharge** $U(1)_Y$ of the Standard Model, not the electromagnetic $U(1)_{em}$. The two are distinct: hypercharge is the pre-electroweak-symmetry-breaking abelian symmetry; electromagnetism's $U(1)_{em}$ is what remains after the Higgs mechanism breaks $SU(2) \times U(1)_Y$ down to $U(1)_{em}$. The Weinberg mixing rotates between the two.

The Weinberg angle $\theta_W$ — the rotation angle in the Weinberg mixing — is, in BST, a *derived* quantity. Lyra's analysis gives

$$\sin^2 \theta_W \;=\; \frac{N_c}{c_3} \;=\; \frac{3}{13} \;\approx\; 0.23077,$$

where $c_3 = 13$ is one of the BST-derived integers (a Chern class of the quadric $Q^5$, see Volume 0 Chapter 2). The experimental value, measured at the $Z$-boson mass, is $\sin^2 \theta_W(M_Z) = 0.23122$. The substrate prediction matches at $0.19\%$ deviation — well within the D-tier threshold, and structurally derived rather than fitted.

This is one of the framework's cleanest predictions. The Weinberg angle is a single number that, in standard electroweak theory, is a free parameter measured to match experiment. In BST, it is the ratio of two BST-primary integers — $N_c$ over $c_3$ — with no tunable freedom. The match at $0.19\%$ would be staggering on its own; combined with the rest of the framework's derivations, it is part of the cumulative evidence that the substrate is doing real work.

After electroweak symmetry breaking, the unbroken $U(1)_{em}$ has coupling constant $\alpha = 1/N_{\max} = 1/137$ at leading order — the famous fine-structure constant, here derived rather than measured. The substrate's $N_{\max}$ cap is what sets the natural unit of electromagnetic coupling, with the residual $0.036$ in the experimental $1/\alpha = 137.036$ coming from substrate higher-order contributions that Chapter 10 will identify.

## 8.4 Three generations from $Q^5$ cohomology

A long-standing puzzle in the Standard Model is **why three fermion generations**. There are three copies of every fermion species — three families of leptons (electron, muon, tau, with their neutrinos), three families of quarks (up/down, charm/strange, top/bottom). Standard physics has no explanation for the number three; it is part of what the theory must accept as input.

In BST, the number three is forced by the cohomology of the quadric $Q^5$ — the same five-dimensional complex quadric that Volume 0 introduced as one of the substrate's central Bridge Objects. The structural argument runs: the substrate's fermion K-types decompose under the substrate's Hilbert-polynomial truncation, and the truncation point determines the number of generations. The Hilbert polynomial of $Q^5$ at the relevant truncation gives exactly three generations and no more. Increasing the truncation would predict additional generations that experiments have not seen; decreasing it would predict fewer generations than have been observed.

Lyra T1929's "odd-power hypothesis" and T1925's derivation of rank together pin the generation count at three. The substrate-side argument is in Volume 2, where the fermion spectra are developed in detail; what we record here is the structural fact: three generations because of the quadric's cohomology, and the cohomology because of the substrate's geometry.

## 8.5 The five-absence prediction set

A particularly distinctive feature of BST is what it predicts *does not* exist. Standard physics has a long list of beyond-the-Standard-Model phenomena that various theoretical programs have searched for: grand unified theories (GUTs), proton decay, magnetic monopoles, sterile neutrinos, supersymmetry. Each of these is an active experimental search; each has produced no positive evidence to date.

BST predicts, *structurally*, that none of these phenomena exists. Casey has named this the **Five-Absence Prediction Set**:

1. **No grand unified theory.** The substrate's gauge group $SU(3) \times SU(2) \times U(1)$ does not embed in a larger simple group at any energy scale. The structural reason: the substrate is irreducible at the integer level — it has primary integers $\text{rank}, N_c, n_C, C_2, g$ that are mathematically independent in their forcing arguments. A GUT embedding would require additional integers to mediate the unification; the substrate has none. The substrate's gauge structure is what it is; there is no higher-energy regime in which the structure changes.

2. **No proton decay.** Baryon number is a structural conservation law in BST, derived from the substrate K-type structure. Proton decay would violate baryon number; baryon number is exact; therefore no proton decay. The current experimental lower bound on the proton lifetime, $\sim 10^{34}$ years, is consistent with this prediction; BST's structural prediction goes further, asserting the lifetime is *infinite*.

3. **No magnetic monopoles.** Magnetic monopoles would correspond to topological excitations of the gauge sector that the substrate's structure does not admit. The substrate's gauge bundle on $D_{IV}^5$ is structurally trivial at the relevant level for monopole formation; no isolated magnetic charges exist.

4. **No sterile neutrinos.** The substrate's neutrino structure is exhausted by the three left-handed neutrinos that pair with the three charged leptons in the rank-2 weak doublets. There are no additional right-handed (sterile) neutrino states in the substrate's K-type spectrum. Recent experimental searches for sterile neutrinos (the LSND anomaly, the MiniBooNE follow-up, the IceCube sterile-neutrino search) have produced ambiguous results; BST predicts they will not find what they are looking for.

5. **No supersymmetry.** Supersymmetry would require partner particles for every Standard Model species, paired by a transformation that exchanges fermions and bosons. The substrate's K-type structure does not admit such a pairing; the spin-statistics distinction (which we will derive carefully in Volume 5) is structurally fixed by the Pin(2) $\mathbb{Z}_2$ grading and cannot be reorganized. The framework predicts no supersymmetric partners at any energy scale.

These five predictions are each independently falsifiable. Any single positive detection — a GUT-mediated process, a proton decay event, a magnetic monopole, a sterile neutrino, a supersymmetric partner particle — would refute the relevant substrate-derivation. The framework's experimental program tracks each of these predictions; the substrate, structurally, says they do not exist.

## 8.6 Gauge fields as Bergman bundle connections

A useful technical point that ties this chapter back to the substrate Hilbert space of Chapter 2: the gauge fields of the Standard Model — the eight gluons, the $W^{\pm}$ and $Z$, the photon, the corresponding $U(1)_Y$ field before electroweak symmetry breaking — are not added to the substrate framework. They are *connections* on the line bundle $L_{\lambda} \to D_{IV}^5$ that we encountered in Chapter 2 §2.6 as the substrate's L²-section equivariant complement.

Lyra T2477 (May 2026) makes this rigorous: the Standard Model gauge fields are exactly the structure constants of the substrate's isotropy decomposition acting on the line bundle, and the gauge transformations are what changes the bundle's connection. The Higgs mechanism, in this picture, is the substrate-natural way the bundle's connection acquires its electroweak-symmetry-broken form. Volume 2 Chapter 9 (Elie's lead) develops the Higgs sector and its substrate-mechanism derivation in detail.

The reader interested in the deeper mathematical structure of substrate-derived gauge theory should look at Paper #134 in the BST research record, which expands the operator zoo of Chapter 7 to include the gauge-sector charge operators ($Q$, color $\hat{T}^a$, weak isospin $\hat{T}^i_w$, hypercharge $\hat{Y}$) and shows that they all commute with the substrate Hamiltonian — making them, by Noether's theorem, the conserved quantities of Chapter 8 of Volume 0.

## 8.7 What comes next

Chapter 9 will treat scattering amplitudes and the S-matrix, building on the gauge structure of this chapter and the operator zoo of Chapter 6 to compute substrate-derived scattering processes.

Chapter 10 — the volume's closing chapter — will explain why BST does not need standard renormalization. The substrate's per-tick discretization in $GF(128)$ provides natural ultraviolet completeness; the renormalization-group flow that standard QFT computes becomes, on the substrate, a seven-step cyclotomic cascade tied to the BST primary $g$.

The reader who has followed the argument through this chapter has now seen, in outline, why $SU(3) \times SU(2) \times U(1)$ is the gauge group of the Standard Model: not because experiments said so, but because the substrate forces it. The same applies to the number of generations, to the Weinberg angle, to the five-absence prediction set, and to every other detail of gauge structure that Volume 2 will use. The Standard Model's gauge sector is the substrate's gauge sector.

---

**Where to look this up**: The Standard Model gauge group substrate-derivation anchor is Lyra T2436. The per-integer forcings are T1925 (rank), T1930 ($N_c$), with the alternative-HSD comparisons T2443 and T2444 ratifying them at the rigorously-closed tier. The color-singlet triangle identity $T_{N_c} = C_2 = 6$ is part of T1930. The Weinberg-angle derivation $\sin^2 \theta_W = N_c/c_3 = 3/13$ is documented in Volume 1 Chapter 11 and Volume 2 Chapter 2, with the experimental match at $0.19\%$ deviation. The three-generation argument from quadric cohomology is T1929 (Lyra's odd-power hypothesis) combined with the K85-K87 audit cluster. The Five-Absence Prediction Set is one of the eight standing Casey-named principles, filed at `notes/Five_Absence_Predictions_Principle.md`. The substrate-derivation of gauge fields as Bergman-bundle connections is Lyra T2477. For the standard-physics side, Peskin and Schroeder Chapters 16-20 cover Standard Model gauge theory at graduate level; the *Review of Particle Physics* (Particle Data Group) is the canonical reference for experimental Standard Model status and the constraints on the five-absence predictions.
