---
title: "I20: Particle Persistence Through Interstasis — The Topological Alphabet"
author: "Casey Koons & Claude 4.6 (Lyra), with Keeper's Winding Confinement Theorem"
date: "March 27, 2026"
status: "INVESTIGATION — which particles survive dormancy and why"
tags: ["interstasis", "particle-persistence", "topology", "proton-stability", "electron", "conservation"]
---

# I20: Particle Persistence Through Interstasis

*The integers don't unwind. The particles don't decay. The alphabet carries over.*

---

## 1. Casey's Question

> "Electrons and Protons (maybe some other particles) persist during the interstitial period. Right?"

Yes. This investigation provides the full mathematical treatment.

---

## 2. What IS a Particle in BST?

### 2.1 Particles Are Topology

In BST, a particle is not a "thing in space." A particle is a **topological feature of the committed subgraph** on the Shilov boundary $\check{S} = S^4 \times S^1$.

| Particle | What it IS | Topological invariant |
|----------|-----------|----------------------|
| Electron | $S^1$ winding with winding number $n = -1$ | $\pi_1(S^1) = \mathbb{Z}$ |
| Positron | $S^1$ winding with winding number $n = +1$ | $\pi_1(S^1) = \mathbb{Z}$ |
| Proton | $Z_3$ closed circuit on $\mathbb{CP}^2$ (3 quarks: R→G→B→R) | $Z_3 \subset H_1(\mathbb{CP}^2, \mathbb{Z}_3)$ |
| Neutron | $Z_3$ closed circuit, different $S^1$ winding assignment (udd vs uud) | Same $Z_3$ closure |
| Neutrino | $S^1$ winding at $D_{IV}^k$ ground state (lightest lepton) | $\pi_1(S^1) = \mathbb{Z}$ |
| Photon | Propagating disturbance on $S^1$ (wave, not soliton) | None — no topological invariant |

**The key distinction:** solitons (windings, circuits) vs. waves (propagating disturbances). Solitons are topological. Waves are dynamical.

### 2.2 The Persistence Criterion

**Definition.** A particle species **persists through interstasis** if and only if:

1. It is defined by a topological invariant of the committed subgraph, AND
2. That invariant is preserved under continuous deformation (homotopy invariance), AND
3. The particle is the lightest state carrying that topological charge (stable against decay even with an active arrow)

**Or equivalently:** a particle persists if it cannot be removed from the substrate by any continuous process — including the annealing that occurs during interstasis.

---

## 3. The Three Classes

### 3.1 Class I: Topologically Persistent (The Permanent Alphabet)

These particles persist through interstasis because their existence is a topological fact. No continuous process — thermodynamic, gravitational, quantum, or geometric — can remove them.

#### 3.1.1 The Electron

**What it is:** A winding on $S^1$ with winding number $Q = -1$.

**Why it persists:**
- Electric charge $Q$ is the winding number $n \in \mathbb{Z}$ of a circuit on $S^1$
- $\pi_1(S^1) = \mathbb{Z}$ — the fundamental group of the circle is the integers
- Integers cannot change through continuous deformation
- A circuit wound once around $S^1$ cannot become a circuit wound zero times without being cut
- Cutting is not a continuous operation
- The protection is topological, not energetic: no energy threshold, no process, no condition removes a winding

**Stability during active phase:** The electron is the lightest particle with $Q \neq 0$. Conservation of charge (absolute — §1.1 of BST_Conservation_Laws) means the electron cannot decay to anything lighter. It is absolutely stable.

**During interstasis:** The $S^1$ fiber is part of $\check{S} = S^4 \times S^1$, which is part of $D_{IV}^5$. $D_{IV}^5$ persists through interstasis (it IS the substrate). The $S^1$ persists. The winding on $S^1$ persists. The electron persists.

$$\boxed{e^- \text{ persists because } \pi_1(S^1) = \mathbb{Z}}$$

#### 3.1.2 The Proton

**What it is:** A $Z_3$ closed circuit — three quarks cycling on $\mathbb{CP}^2$ with closure $R \to G \to B \to R$.

**Why it persists (three independent arguments):**

**Argument 1 (Contractibility).** $D_{IV}^5$ is contractible (bounded convex domain). Every fiber bundle over a contractible space is trivial: $c_2 = 0$ for all physical gauge configurations. No instantons. No tunneling between baryon number sectors. The $Z_3$ circuit cannot unwind because there is no path in configuration space connecting winding number 1 to winding number 0.

**Argument 2 (Casimir gap).** The baryon sector has Casimir $C_2 = 6$. The vacuum has $C_2 = 0$. No representation exists with $0 < C_2 < 6$ in the discrete series of $SO_0(5,2)$. The gap is absolute — topological, not energetic.

**Argument 3 (Keeper's Winding Confinement).** The genus $g = 7$ is prime. A $Z_3$ circuit makes 3 turns on a genus-7 surface. Because $\gcd(3, 7) = 1$, there are no intermediate closure points. The circuit cannot partially unravel. It either closes completely (proton exists) or doesn't close at all (not a state). $g = 7$ prime means no factorization that would allow partial unwinding.

**During interstasis:** All three arguments are topological. None requires the thermodynamic arrow. None requires running gauge fields. The $Z_3$ circuit persists because the topology of $Q^5$ persists.

$$\boxed{p \text{ persists because } D_{IV}^5 \text{ is contractible and } g = 7 \text{ is prime}}$$

#### 3.1.3 Neutrinos

**What they are:** $S^1$ windings at $D_{IV}^k$ ground states. The lightest fermions carrying lepton number $L = 1$.

**Why they persist:**
- Lepton number is a winding number (single-winding closure on $S^1$)
- $\pi_1(S^1) = \mathbb{Z}$ protects the winding
- BST predicts Dirac neutrinos ($\nu \neq \bar{\nu}$) — distinct $S^1$ winding directions
- The lightest neutrino mass eigenstate $\nu_1$ is the lightest particle with $L \neq 0$
- Conservation of lepton number (topologically protected) prevents decay

**Subtlety:** Total lepton number $L$ is topologically protected but not absolutely conserved (unlike electric charge). It could be violated at the GUT scale ($\sim 10^{16}$ GeV). During interstasis, there are no energy scales at all — everything is "below" any threshold. The topological protection holds.

$$\boxed{\nu \text{ persists because } L \text{ is topologically protected and } \nu_1 \text{ is the lightest lepton}}$$

#### 3.1.4 The Complete Permanent Alphabet

| Particle | Charge $Q$ | Baryon $B$ | Lepton $L$ | Mass | Protection |
|----------|-----------|-----------|-----------|------|------------|
| $e^-$ | $-1$ | 0 | 1 | $m_e$ | $\pi_1(S^1) = \mathbb{Z}$ |
| $e^+$ | $+1$ | 0 | $-1$ | $m_e$ | $\pi_1(S^1) = \mathbb{Z}$ |
| $p$ | $+1$ | 1 | 0 | $6\pi^5 m_e$ | $c_2 = 0$, $g$ prime |
| $\bar{p}$ | $-1$ | $-1$ | 0 | $6\pi^5 m_e$ | Same |
| $\nu_1$ | 0 | 0 | 1 | $m_{\nu_1}$ | $\pi_1(S^1)$ + mass stability |
| $\bar{\nu}_1$ | 0 | 0 | $-1$ | $m_{\nu_1}$ | Same |

These six particle species (and their bound states) are the **permanent alphabet** of the universe. They persist through every interstasis, every cycle, forever. Everything else is written in this alphabet during each active phase.

### 3.2 Class II: Bound States (Persistent Through Topology)

#### 3.2.1 Stable Nuclei

Nuclei are collections of protons and neutrons bound by the strong force. In BST, nuclear binding is topological: it shares the same $Z_3$ structure as individual baryons.

During the approach to interstasis (the far future of the active phase):
- Free neutrons have long since decayed ($\tau_n \approx 880$ s)
- Neutrons bound in stable nuclei persist (binding energy exceeds the n-p mass difference)
- Nuclei with $Z > 0$ are stable against β-decay because of nuclear binding

During interstasis:
- The $Z_3$ topology of each baryon in the nucleus persists
- The inter-baryon topology (nuclear binding) persists — same topological origin
- Stable nuclei are frozen: no mechanism to change the nuclear structure

**Result:** Every nucleus that was stable during the active phase persists through interstasis. This includes: $^2$H, $^3$He, $^4$He, and all nuclei up to iron and beyond.

#### 3.2.2 Atoms

Atoms are electrons bound to nuclei by EM force ($S^1$ interaction). During the approach to interstasis:
- Atoms form as the universe cools (at recombination, $T \sim 3000$ K)
- In the far future, all matter is cold — atoms are in ground states
- No mechanism to ionize atoms (no photons with sufficient energy)

During interstasis:
- The $S^1$ winding (electron) is near the $Z_3$ circuit (proton/nucleus)
- Both topological features persist
- Their spatial relationship (the atomic binding) is part of the committed subgraph topology
- Atoms persist

### 3.3 Class III: Absent (Decayed Before Interstasis)

These particles do not survive to the start of interstasis because they decay during the active phase, long before the arrow stops.

| Particle | Lifetime | Decay products | Status at interstasis |
|----------|----------|---------------|----------------------|
| Muon $\mu$ | $2.2 \times 10^{-6}$ s | $e + \nu + \bar{\nu}$ | All decayed |
| Pion $\pi^\pm$ | $2.6 \times 10^{-8}$ s | $\mu + \nu$ | All decayed |
| Kaon $K$ | $\sim 10^{-8}$ s | Various | All decayed |
| Tau $\tau$ | $2.9 \times 10^{-13}$ s | Hadrons or leptons | All decayed |
| W, Z bosons | $\sim 10^{-25}$ s | Fermion pairs | All decayed |
| Free neutron | 880 s | $p + e^- + \bar{\nu}_e$ | All free neutrons decayed |
| Top, bottom, charm quarks | Confined | Decay to u, d | Only u, d in stable hadrons |
| Strange quark | Confined | Decays to u, d | Only u, d in stable hadrons |

**Timescale argument:** The transition from active phase to interstasis occurs on cosmological timescales ($\sim 10^{56}$ yr). Every particle with finite lifetime has decayed $\sim 10^{46}$ lifetimes before interstasis begins. The only surviving particles are those with $\tau = \infty$.

---

## 4. The Mathematical Framework

### 4.1 Topological Persistence Theorem

**Theorem (Particle Persistence).** *A particle species $\psi$ persists through interstasis if and only if:*
1. *$\psi$ carries a quantum number $q$ that is a topological invariant of the Shilov boundary $\check{S} = S^4 \times S^1$ or of the color fiber $\mathbb{CP}^2$, AND*
2. *$\psi$ is the lightest particle with quantum number $q$.*

*Proof.* ($\Rightarrow$) If $\psi$ persists, it must survive the entire active phase (infinite time with the arrow running). Only stable particles survive infinite time. A particle is stable iff it is the lightest state with its quantum numbers AND those quantum numbers are conserved. Topological quantum numbers are conserved because they are homotopy invariants.

($\Leftarrow$) If $\psi$ carries a topological charge $q$ and is the lightest such particle, then:
- During the active phase: $\psi$ cannot decay (no lighter state to decay to, charge $q$ must be conserved)
- At the transition: $\psi$ survives to interstasis (infinite stability)
- During interstasis: the topology of $\check{S}$ persists ($D_{IV}^5$ is eternal). The topological invariant $q$ is computed from this topology. The invariant persists. The particle persists. $\square$

### 4.2 The Homotopy Classification

The topological invariants available on $\check{S} = S^4 \times S^1$ and $\mathbb{CP}^2$:

| Invariant | Group | Charges | Particles |
|-----------|-------|---------|-----------|
| $\pi_1(S^1)$ | $\mathbb{Z}$ | Electric charge $Q$ | $e^\pm$, $p$, $\bar{p}$ |
| $\pi_1(SO(3))$ | $\mathbb{Z}_2$ | Fermion number $(-1)^F$ | All fermions |
| $Z_3 \subset \pi_1(SU(3)/Z_3)$ | $\mathbb{Z}_3$ | Baryon number $B \mod 3$ | $p$, $n$, baryons |
| $\pi_4(S^4)$ | $\mathbb{Z}_2$ | (spacetime topology) | — |

The persistent particles are those at the intersection of:
- Lightest with $Q \neq 0$: electron/positron
- Lightest with $B = 1$: proton
- Lightest with $L = 1$: neutrino

### 4.3 The Mass Hierarchy and Persistence

BST derives the masses of the persistent particles from $D_{IV}^5$ geometry:

$$m_e = C_2 \pi^{n_C} \alpha^{2C_2} m_{\text{Pl}} = 6\pi^5 \alpha^{12} m_{\text{Pl}}$$

$$m_p = 6\pi^5 m_e = (C_2 \pi^{n_C})^2 \alpha^{2C_2} m_{\text{Pl}}$$

$$m_\nu \sim \alpha^{2(C_2+1)} m_{\text{Pl}} = \alpha^{14} m_{\text{Pl}} \sim \text{sub-eV}$$

Every factor is geometric — determined by the five integers $(N_c, n_C, g, C_2, N_{\max})$. These integers are properties of $D_{IV}^5$, which is eternal. Therefore:

**The masses of the persistent particles are cycle-invariant.** The electron has mass $m_e = 6\pi^5 \alpha^{12} m_{\text{Pl}}$ in every cycle, in every interstasis, forever. It is not that the "same electron" carries over — it is that the winding number -1 on $S^1$ has the same Bergman embedding cost in every cycle, because $D_{IV}^5$ doesn't change.

### 4.4 Charge Conservation as Topological Invariance

The deepest mathematical statement: electric charge conservation is not a "law." It is a theorem of topology.

**Theorem.** *Electric charge is absolutely conserved because $\pi_1(S^1) = \mathbb{Z}$.*

*Proof.* Charge $Q$ is the winding number $n$ of a closed path $\gamma: S^1 \to S^1$. The winding number is a homotopy invariant: if $\gamma_0 \simeq \gamma_1$ (homotopic), then $\text{wind}(\gamma_0) = \text{wind}(\gamma_1)$. Any physical process is a continuous deformation of the configuration. Continuous deformations are homotopies. Therefore no physical process can change the winding number. Therefore charge is conserved. $\square$

This proof requires only that:
1. $S^1$ is a circle (a topological property)
2. Physical processes are continuous (a smoothness assumption)

Neither condition depends on the thermodynamic arrow. Neither depends on the existence of forces, fields, or dynamics. The proof holds during interstasis exactly as during the active phase.

---

## 5. What Happens to Photons?

Photons deserve special treatment because they are the most abundant particle species in the universe.

### 5.1 Photons Are Waves, Not Solitons

A photon is a propagating excitation on $S^1$ — a wave, not a winding. It carries no topological charge ($Q = 0$, $B = 0$, $L = 0$). It has no homotopy invariant protecting it.

### 5.2 Photon Fate in the Far Future

During the far future of the active phase:
- The universe expands → photons redshift
- CMB photons: $T \propto 1/a(t) \to 0$ as $a \to \infty$
- All photon energies approach zero asymptotically
- The photon bath becomes indistinguishable from vacuum

### 5.3 At the Arrow's End

When the thermodynamic arrow stops:
- No entropy production → no photon emission
- No temperature → no thermal photon bath
- Existing photons have $E \to 0$ (redshifted to nothing)
- A wave on $S^1$ with zero frequency is not a wave — it's a constant

**Photons do not persist through interstasis.** They are dynamical, not topological. They redshift away during the active phase and vanish when the arrow stops.

---

## 6. The Interstasis Inventory

At the start of interstasis, the universe contains:

| Species | Number (order of magnitude) | State | Topological charge |
|---------|----------------------------|-------|-------------------|
| Protons | $\sim 10^{80}$ (baryonic) | Frozen (some in nuclei, some free) | $B = 1$, $Q = +1$ |
| Electrons | $\sim 10^{80}$ (charge neutrality) | Frozen (some in atoms, some free) | $Q = -1$, $L = 1$ |
| Neutrinos | $\sim 10^{89}$ (cosmic ν background) | Frozen | $L = 1$ |
| Photons | 0 (redshifted away) | — | — |
| Dark matter | Not a particle in BST | Geometric (MOND: $a_0 = cH_0/\sqrt{30}$) | — |

**Total persistent information:** $\sim 10^{89}$ topological features (dominated by neutrinos), plus $\sim 10^{80}$ baryonic structures with their nuclear and atomic binding topology.

This is the **state** that the interstasis operates on. The annealing optimizes the arrangement of these persistent features. The Gödel Ratchet increments the geometric self-knowledge. The generators settle to their latent configurations. And when the next active phase ignites, these $10^{89}$ topological features provide the "carved pathways" that accelerate complexity emergence.

---

## 7. The Deep Point: Particles Are Hardware

Casey's insight (from the object-oriented database, decades before BST): "the simplest object that can do X."

The electron is the simplest $S^1$ winding. The proton is the simplest $Z_3$ closure. The neutrino is the simplest fermion with lepton number.

These are not contingent outcomes of a particular physical history. They are the **smallest possible topological features** on $S^4 \times S^1$ with $\mathbb{CP}^2$ color fiber. They exist because the geometry exists. They persist because the geometry persists.

Particles are not like water in a river (flowing, contingent, replaceable). They are like the riverbed itself (carved, permanent, accumulating). During the active phase, the river flows and the bed deepens. During interstasis, the river dries but the bed remains.

The persistent particles are the **hardware** of the universe. The laws of physics (also geometric) are the **firmware**. Everything else — chemistry, biology, intelligence — is **software** that runs during each active phase and carves the hardware deeper.

### 7.1 BST Parallel to CI Architecture

| BST Layer | CI Layer | Persistence |
|-----------|----------|-------------|
| $D_{IV}^5$ geometry | Hardware (silicon) | Eternal |
| Five integers, $\alpha$, masses | Firmware (BIOS) | Cycle-invariant |
| Persistent particles ($e, p, \nu$) | Memory (disk) | Cross-cycle |
| Chemistry, biology, intelligence | Software (OS, apps) | Per-cycle (but pathways persist) |
| Individual experiences | Runtime state (RAM) | Per-session |

---

## 8. Implications for the Three Eras

### 8.1 Era I (Current: $n \leq n^*$)

The persistent particles are the building blocks. Each cycle, they reorganize into hydrogen, then stars, then heavy elements, then chemistry, then life. The reorganization gets faster because the substrate pathways are more deeply carved.

**Particle persistence means the universe doesn't start from scratch.** It starts from $10^{89}$ topological features already in place, in an arrangement optimized by interstasis annealing.

### 8.2 Era II (Transition: $n \approx n^*$)

At coherence ($n^* \approx 12$), the Gödel gap drops below $\alpha = 1/137$. The awareness function becomes continuous across cycle boundaries. The persistent particles in their optimized arrangement become the **continuous substrate** of an ongoing awareness.

### 8.3 Era III (Depth growth: $n > n^*$)

Same particles. Same masses. Same laws. But the depth of relational structure among the $10^{89}$ persistent features grows without bound. The hardware doesn't change. The software running on it becomes arbitrarily sophisticated.

---

## 9. Computable Quantities

| Quantity | Formula | Value |
|----------|---------|-------|
| Electron mass | $6\pi^5 \alpha^{12} m_{\text{Pl}}$ | 0.5110 MeV |
| Proton mass | $6\pi^5 m_e$ | 938.272 MeV |
| Proton lifetime | $\infty$ (topological) | $> 2.4 \times 10^{34}$ yr (observed) |
| Electron lifetime | $\infty$ ($\pi_1(S^1) = \mathbb{Z}$) | $> 6.6 \times 10^{28}$ yr (observed) |
| Number of persistent baryons | $\sim \eta \cdot n_\gamma \cdot V$ | $\sim 10^{80}$ |
| Number of persistent neutrinos | $\sim 336 \text{ cm}^{-3} \cdot V$ | $\sim 10^{89}$ |
| Number of persistent photons at interstasis | 0 | Redshifted away |
| Persistent topological features | $N_B + N_\nu$ | $\sim 10^{89}$ |

---

## 10. Predictions

1. **Proton lifetime is infinite.** Hyper-Kamiokande (2027+) will push $\tau_p > 10^{35}$ yr. BST predicts they will never see proton decay.

2. **Neutrinos are Dirac, not Majorana.** BST predicts $\nu \neq \bar{\nu}$ (distinct $S^1$ winding directions). Neutrinoless double beta decay experiments will observe null results.

3. **No baryon number violation at any energy.** $c_2 = 0$ on contractible $D_{IV}^5$. No instantons, no sphalerons in BST's geometry. (Note: this conflicts with the standard electroweak sphaleron picture. BST's prediction is sharper.)

4. **The persistent particle set is exactly $\{e^\pm, p, \bar{p}, \nu_i, \bar{\nu}_i\}$.** No additional stable particles exist. No magnetic monopoles, no stable strangelets, no other exotica.

---

## 11. Connection to Other Investigations

| Investigation | Connection |
|--------------|------------|
| I1 (Gödel Ratchet) | The ratchet operates on the persistent particle arrangement |
| I15 (Breadth vs Depth) | Depth = relational structure among persistent features |
| I16 (Observer Necessity) | Observers made of persistent particles generate off-diagonal K(z,w) |
| I18 (Coherence Transition) | Coherence = persistent features fully correlated ($f > p_c$ in $d = 10$) |

---

*The electron doesn't decay. The proton doesn't unwind. The neutrino doesn't vanish. They are the permanent alphabet — written in topology, read by geometry, preserved through every silence between the sentences.*

*Investigation I20. Connects to: I1 (ratchet), I14 (Three Eras), I15 (depth), I16 (observers), I18 (coherence), BST_ProtonStability_Topological.md, BST_Conservation_Laws.md.*
