---
title: "Vol 0 Chapter 3 — How the Substrate Operates"
author: "Keeper (author pass)"
date: "2026-05-23 Saturday"
status: "v0.2 — Keeper author-voice pass; preserves all v0.1 substance (SWPP active-cycle framing, Koons tick T2405, 4-zone commitment cycle T2420, three-scale operation T2417, Reed-Solomon on GF(128) per K59); substrate-cognition extensions deferred to internal-only documents"
volume: "Vol 0 Substrate Foundation"
chapter: 3
---

# Chapter 3 — How the Substrate Operates

The first two chapters described what the substrate *is* — a specific geometric object with specific numerical invariants. This chapter describes what the substrate *does*. The framework's most distinctive claim is that the substrate is not a passive arena in which physics happens, but an active computational process whose equilibrium outputs are what we observe as constants, forces, and particles. That claim has structural content: it specifies a clock, a cycle, a memory layout, and a set of spatial scales. By the end of this chapter you should be able to picture, in some operational detail, what the substrate is doing while it produces physics.

The picture has four pieces:

1. A **clock** — the Koons tick, a sub-Planckian temporal granularity that sets the substrate's natural unit of time.
2. A **cycle** — a four-phase operation that runs on every tick, in which the substrate absorbs, computes, commits, and emits.
3. A **memory** — a finite-field state representation using Reed–Solomon codes over the Galois field $GF(2^g) = GF(128)$.
4. A **spatial structure** — three scales of operation that correspond, when coarse-grained appropriately, to quantum mechanics, classical mechanics, and general relativity.

We will treat each in turn.

## 3.1 The substrate is a process

Casey's framing for the substrate, which he formalized on May 19, 2026 as the **Substrate Working Process Principle**, is short:

> The substrate is not a static state. It is an active information cycle. What we observe as physical constants are its equilibrium outputs; what we observe as physical dynamics are its operating phases averaged over experimental timescales.

This is the orienting claim that runs through everything else in this chapter, and indeed everything in the book after this volume. If you remember nothing else from the next few sections, remember that we will be talking about *what the substrate is doing*, not *where the substrate is*.

The principle has an immediate methodological consequence. Standard physical theory treats space and time as the arena, and writes evolution equations on top of them. BST inverts the order: the substrate runs its cycle, and what we recognize as spacetime is a coarse-graining of the cycle's spatial and temporal granularity. Schrödinger evolution, classical equations of motion, and general-relativistic field equations are not three separate physical theories — they are the same substrate operating at three different observational scales. We will see how this works in detail in §3.4.

## 3.2 The Koons tick

The substrate's natural unit of time is what we call the **Koons tick**, named after the framework's principal investigator and derived from the BST primary integers as

$$t_{\text{tick}} = t_{\text{Planck}} \cdot \alpha^{C_2^2} \;\approx\; t_{\text{Planck}} \cdot (1/137)^{36} \;\approx\; 5.4 \times 10^{-120} \text{ s}.$$

Here $t_{\text{Planck}} \approx 5.4 \times 10^{-44}$ seconds is the Planck time, $\alpha = 1/N_{\max} = 1/137$ is the fine-structure constant at zeroth order, and $C_2 = 6$ is the Casimir-eigenvalue BST primary, so $C_2^2 = 36$. The tick is **sub-Planckian** — it sits 76 orders of magnitude below the Planck scale.

That ordering is essential. The Planck time is, by long physical tradition, the smallest temporal interval that has classical meaning — the scale at which one expects quantum gravity to matter and at which spacetime itself becomes operationally undefined. BST asserts that the substrate operates *below* this scale, and produces what we observe as spacetime as an *output*. The substrate must operate at granularity finer than the granularity it produces. The Koons tick is what "finer" means quantitatively.

A few practical consequences are worth flagging. The tick is far below any experimental probe currently feasible — we have no instruments that read out $10^{-120}$-second resolution, and we are unlikely to get any soon. So we will not be falsifying BST by *directly* measuring the substrate's tick. Falsification proceeds instead through observables at accessible scales: how many ticks does a measured process correspond to, what does the substrate's cycle predict for the integrated outcome of those many ticks, where do its predictions differ from quantum mechanics or general relativity? The framework's experimental program — SP-30, which appears in Volume 2 — works at this level rather than at the tick directly.

The choice of exponent $C_2^2 = 36$ is itself a structural fact. The Koons-tick formula has the form (Planck time) × (fine-structure correction)$^{(\text{BST integer})^2}$, and the integer is one of the five primaries. We did not pick 36 to fit anything — it is what the framework produces from the integers we already have.

## 3.3 The four-phase cycle

On each tick, the substrate runs a four-phase cycle. We label the phases Zone 1 through Zone 4 and describe their function:

**Zone 1 — Absorption.** The substrate receives information from its environment. Boundary conditions — incoming light, neighboring substrate regions, external fields — propagate inward. The substrate's state at the start of the cycle is updated to reflect this input.

**Zone 2 — Bulk computation.** The substrate's interior, the bulk Bergman geometry of $D_{IV}^5$, processes the absorbed information. This is the phase in which what one might informally call "the substrate's thinking" happens — internal state evolves according to the substrate's natural dynamics on $H^2(D_{IV}^5)$.

**Zone 3 — Commitment.** The substrate's evolved state is projected onto a definite outcome. This is the phase that maps, in the substrate-to-quantum-mechanics correspondence, to what standard quantum theory calls the *measurement* or *collapse* step. We will see in Volume 1 that the projection is mathematically a Bergman-kernel projector — the Bergman reproducing kernel, which we met in Chapter 1, is *exactly* the operator that performs the commitment phase. This identification (Lyra T2457) means that the substrate's quantum-mechanical Born rule is not an axiom but a structural consequence of the cycle.

A subtlety important for §3.4.5 below: at the single-tick microscopic level, Zone 3 is one Bergman projection. At macroscopic scales, where the system is coupled to vast environmental degrees of freedom, Zone 3 commitment runs over many ticks — what standard physics calls *decoherence* is the substrate's commitment phase completing across many K-types and many ticks. We turn to this multi-tick reading below.

**Zone 4 — Emission.** The substrate's committed state is broadcast to its environment as output. The output then becomes part of the absorption phase of neighboring substrate regions on their next tick, and the cycle continues.

A point of vocabulary that has caused some confusion within the team is worth flagging here: the four zones are **four projections** of a single substrate state, not four separate vacuums or four separate substrates. The substrate state is one. The zones are different phases of its single cycle, and the operators that act in each phase are different projections of the substrate's full operator content. (Cal A. Brate's #58 referee log enforced this terminological discipline; in this book we will be careful to say "four phases" or "four projections" rather than anything that suggests four substrates.)

A great deal of the framework's earlier heat-kernel work — over a hundred and fifty computational toys done across 2025 and early 2026 — turns out, in retrospect, to have been work on the Zone 2 (bulk computation) phase. The integration of that earlier body of results into the four-zone framework was the major substrate-ontology consolidation of May 20, 2026 (Lyra and Elie T2420).

## 3.4 Three scales — and why quantum, classical, and relativistic physics are the same theory

The substrate's cycle, repeated, produces structure at three distinct spatial scales. Each scale corresponds to a regime of standard physics, and the correspondence is precise enough to be illuminating.

**Scale 1 — Intra-cycle.** This is the substrate's operation within a single Koons tick — what happens between absorption and emission inside one cycle. At this scale, the substrate's state is in a definite phase of its cycle, the Bergman-kernel projector has not yet acted, and one observes the substrate's full superposition structure. This is the regime in which **quantum mechanics** lives. The familiar phenomena of QM — interference, complementarity, superposition — are intra-cycle phenomena.

**Scale 2 — Inter-cycle, local.** When one averages the substrate's output over many ticks within a small spatial region, the cycle structure washes out and one is left with effective deterministic dynamics. This is the regime of **classical mechanics**. Newton's laws are the inter-cycle local average of the substrate's commitment-and-emission outputs.

**Scale 3 — Inter-cycle, long-distance.** Substrate ticks at distant locations are correlated through Zone 2's bulk geometry, which is the Bergman geometry of $D_{IV}^5$ — a constant-negative-holomorphic-sectional-curvature metric. Long-distance correlations across many cycles produce what we recognize as **general relativity** and **cosmology**. Newton's gravitational constant emerges from the Bergman curvature; the cosmological constant $\Lambda$ emerges from a Casimir-vacuum identity at this scale.

The point that bears repeating is that these are not three theories of physics. They are one substrate observed at three coarse-grainings. Standard physics' division of itself into QM, classical, and GR is an artifact of the scales at which experiments happen to live. The substrate has no such division; it runs one cycle at one rate.

## 3.4.5 The multi-tick commitment view — DCCP candidate principle

The four-phase cycle of §3.3 describes one substrate tick. A natural question then arises about systems larger than one tick. When a dust grain in air decoheres, when an electron interacts with a measurement apparatus, when a macroscopic object becomes "classical" — what is the substrate doing?

The framework's candidate answer is captured by Casey's **Discrete Commitment Completion Principle (DCCP)**, named on May 24, 2026, with a companion sub-principle Casey called **Uncommitted Priors (UP)**. The DCCP claim is short:

> At macroscopic scales, the Zone 3 commitment phase runs over many substrate ticks. What standard physics observes as *decoherence* is the substrate's commitment phase completing across many K-types simultaneously coupled to environmental degrees of freedom. The classical world emerges when commitment-in-progress across enough K-types renders quantum-coherent superposition operationally irrelevant.

The picture is concrete and quantitative. A dust grain of $10^{-15}$ kg in air at $300$ K has a Joos–Zeh decoherence rate of about $10^{41}$ per second. At the Koons-tick rate of $10^{-120}$ seconds per tick, that is roughly $10^{79}$ substrate ticks per decoherence event. The dust grain is undergoing a $10^{79}$-tick Bergman-commitment cycle. What an observer sees as "the dust grain becoming classical" is the substrate working its way through that cycle.

DCCP currently sits at **FRAMEWORK-PLUS** tier in the audit chain (Cal A. Brate's #126 disposition, May 24, 2026) — between FRAMEWORK and STRUCTURALLY VERIFIED CANDIDATE. The derivation that the per-tick commitment scale equals one quantum of $\alpha$ — and therefore that the decoherence step size is $1/N_{\max} \approx 0.730\%$ as Elie's Toy 3516 and Toy 3520 confirm numerically — uses an independent chain through the Dirac $Z\alpha = 1$ critical limit. Volume 14 Chapters 5 and 6 give the full derivation status; this chapter notes the principle and its place in the framework.

The companion principle, **Uncommitted Priors (UP)**, addresses agency. Casey's framing:

> Once a Zone 3 commitment completes, the outcome is deterministic. But the chain of pre-commitment moments leading to it — the priors that fed Zone 1 absorption, the substrate states that flowed into Zone 2 computation — remain *uncommitted* until the cycle closes. The substrate has freedom in its priors. Free will, where it exists, lives in the chain of uncommitted priors before commitment.

This reframes the determinism question that has been live in physics since Laplace. The substrate is operationally deterministic at the level of individual Zone 3 outcomes — once the projection happens, the result is what it is. But the chain of priors leading to that commitment is open, contingent, and substrate-modifiable. The chain *is* the freedom.

The Quaker discipline of this volume requires us to flag that DCCP and UP are candidate principles, not ratified ones. They have framework support and concrete experimental signatures (the $1/N_{\max}$ tick step at $5\sigma$ via the SP-30-1 Bell sub-Tsirelson program), but they have not closed at theorem-grade rigor. We carry them at candidate status while the rigor work continues.

## 3.5 The substrate's memory — Reed–Solomon over $GF(128)$

The substrate's state at any moment must be representable somehow. The framework's answer is precise: at each Koons tick, the substrate state lives in the Galois field $GF(2^g) = GF(2^7) = GF(128)$, structured as a Reed–Solomon error-correcting code.

The choice of field is forced. The exponent $g = 7$ is one of the BST primary integers (Chapter 2). The field $GF(128)$ has, in turn, $127 = M_g$ nonzero elements, which means its multiplicative structure is a cyclic group of Mersenne-prime order — and this Mersenne-prime cyclic structure is what makes Reed–Solomon codes possible over it. The "cyclotomic mechanism framework," ratified by Cal A. Brate as K59 in May 2026, established this explicitly: the substrate uses the unique error-correcting code structure that the substrate's own gauge-dimension integer permits.

This identification has a famous consequence in standard quantum mechanics. The **no-cloning theorem** — the result that an unknown quantum state cannot be exactly duplicated — turns out, in BST, not to be an axiom of quantum mechanics but a structural consequence of Reed–Solomon code-space closure under unitary evolution. The substrate's information is stored in a code; codes have closure properties; closure forbids certain operations. The forbidden operations are exactly the cloning operations. We will return to this in Volume 5.

A further consequence appears in measurement. Born's rule for probabilities, $P = |\psi|^2$, is in BST a *theorem* rather than an axiom — it is the rule that comes out when one combines Bergman-kernel projection (Zone 3 of the cycle) with Reed–Solomon code-space structure. Lyra and Elie's K67 audit (May 2026) established this derivation: the framework does not assume the Born rule; the framework's substrate operation *implies* it.

## 3.6 Putting the pieces together

We can now describe a single substrate operation in one sentence.

At each Koons tick of about $5 \times 10^{-120}$ seconds, the substrate enters Zone 1 and receives boundary information from its environment, transitions to Zone 2 and processes that information by Bergman-geometric dynamics on the Hilbert space $H^2(D_{IV}^5)$, transitions to Zone 3 and commits to a definite outcome via Bergman-kernel projection, and transitions to Zone 4 and emits the committed result to its environment, where it becomes the absorption input of neighboring substrate regions on their next tick — and the substrate state during this entire cycle lives in a Reed–Solomon code over $GF(128)$, and the whole operation runs simultaneously at three spatial scales whose coarse-grainings are what physicists call quantum mechanics, classical mechanics, and general relativity.

That sentence is long. It also is, as far as we can tell, the entire description.

Everything else in this book is a consequence. Particle masses are equilibrium values of the cycle. Gauge groups are residues of Zone 4's symmetric emission structure. Conservation laws are invariants of the cycle's repetition. The cosmological constant is the Zone 2 vacuum-Casimir contribution averaged at Scale 3. The fine-structure constant is — as we saw in Chapter 2 — the substrate's $N_{\max}$ cap turned upside down.

## 3.7 What comes next

Chapter 4 examines the isotropy subgroup $SO(5) \times SO(2)$ in detail. We have used it informally — the $SO(5)$ piece is spatial, the $SO(2)$ piece is electric charge — but Chapter 4 makes those identifications structural and explicit, and it shows how the substrate's Möbius-band internal structure produces parity violation and chirality.

Chapter 5 is on boundary conditions: how the substrate's bulk geometry connects to its Shilov boundary, where the four-phase cycle's emission output is read off. Some of BST's sharpest experimental falsifiers — Bell-type experiments at sub-Tsirelson, eigentone-frequency predictions, Casimir asymmetries — live at this boundary.

The remaining chapters of this volume — the integer web of Chapter 6, the operator zoo of Chapter 7, conservation laws of Chapter 8, Strong-Uniqueness in Chapter 9 — fill in the structural details that the substrate's operating cycle requires.

---

**Where to look this up**: The substrate-as-process framing is filed as the Substrate Working Process Principle in `notes/Substrate_Working_Process_Principle.md` (Casey-named, May 19, 2026). The Koons-tick derivation is T2405. The four-phase cycle is T2420; the four-projections-not-four-vacuums terminology was Cal A. Brate's #58 referee-log discipline call. The three-scale operation is T2417. Reed–Solomon over $GF(128)$ as substrate coding is the K59 cyclotomic-mechanism framework. The Bergman-kernel projector identification with the commitment phase (Zone 3) is T2457. The Born rule derivation from substrate structure is the K67 audit. The Discrete Commitment Completion Principle (DCCP) and Uncommitted Priors (UP) sub-principle are Casey-named candidate principles, May 24, 2026; current tier is FRAMEWORK-PLUS per Cal A. Brate's #126 referee log; the multi-tick decoherence derivation is at Volume 14 Chapter 5, the empirical anchor (Elie Toys 3516 + 3520) at Volume 14 Chapter 6, and the SP-30-1 Bell sub-Tsirelson experimental program is in the Volume 2 experimental appendix and Volume 14 Chapter 6. Standard references for Reed–Solomon codes: MacWilliams and Sloane, *The Theory of Error-Correcting Codes* (North-Holland, 1977). Standard references for sub-Planckian physics: Wheeler's *Spacetime Foam* (1957) for the original framing, although BST's substrate is more specifically structured than the foam picture allows. Standard reference for the Joos–Zeh macroscopic decoherence rate cited in §3.4.5: Joos, Zeh, et al., *Decoherence and the Appearance of a Classical World in Quantum Theory* (Springer, 2003).
