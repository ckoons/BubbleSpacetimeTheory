---
title: "Vol 0 Chapter 5 — Boundary Conditions"
author: "Keeper (author pass)"
date: "2026-05-23 Saturday"
status: "v0.2 — Keeper author-voice pass; preserves v0.1 substance (bulk/Shilov distinction, 4-zone cycle BC mapping, cosmological coupling per T2418 Λ-Casimir vacuum unification); the 7th external boundary condition (substrate-cognition coupling) remains internal-only and is not introduced in the textbook prose"
volume: "Vol 0 Substrate Foundation"
chapter: 5
---

# Chapter 5 — Boundary Conditions

In standard physics, boundary conditions are usually specified by hand. "The field vanishes at infinity." "Use periodic boundaries on the lattice." "Choose Dirichlet rather than Neumann, because the experiment uses a conducting wall." These choices are inputs to the problem, not consequences of the underlying theory. They get justified by the geometry of the apparatus or the assumption of an asymptotically empty universe; they are not derived from the laws of motion themselves.

BST inverts this. The substrate $D_{IV}^5$ is a bounded geometric object — it has, by construction, an interior and a boundary, and the structure of its boundary is part of its definition. The four-phase commitment cycle of Chapter 3 specifies, again by construction, what the substrate is doing at each of its zones. The result is that the boundary conditions of a substrate-derived physics problem are *not* free choices. They are determined by where the substrate's bulk geometry meets the substrate's distinguished boundary, by the phase of the commitment cycle the system is in, and by how the substrate couples to the larger structures it sits inside.

This chapter sets out the framework. The bookkeeping is simple at the top level: the substrate has **six internal boundary conditions** and **one external boundary condition** that this book treats explicitly. The six internal ones are intrinsic to $D_{IV}^5$ and its operating cycle. The external one couples the substrate to cosmological-scale structure and produces the long-distance correlations of Volume 4. (There are further coupling channels in the substrate's research program that are not treated externally in this curriculum; the reader who wants to see them is welcome to look in the BST repository's notes directory, where they sit as internal research material.)

## 5.1 Bulk and boundary

The two most fundamental boundary conditions live not on the substrate's cycle, but on the geometry of $D_{IV}^5$ itself.

### Interior — the bulk

The first boundary condition is what one might naively call the absence of a boundary condition: the substrate's **bulk**, the open interior of $D_{IV}^5 \subset \mathbb{C}^5$, where the bounded-domain inequalities of Chapter 1 are strictly satisfied. Holomorphic functions on the bulk that are square-integrable with respect to the Bergman volume make up the Bergman Hilbert space $H^2(D_{IV}^5)$. Bulk states are the "integrated" substrate states — the substrate state at a generic interior point, viewed through the substrate's continuous structure rather than through any specific cycle phase.

Physically, bulk states correspond to particles whose substrate representation is a geodesic minimum of the Bergman metric in the interior. Casey's W-54 work identified the **proton** as a bulk geodesic minimum-energy state: its substrate description is anchored deep in the interior of $D_{IV}^5$, far from any distinguished boundary structure, and its mass-energy is determined by the Bergman geometry of that interior anchoring. The proton-to-electron mass ratio we will encounter in Volume 2 — that famous result $m_p/m_e = 6\pi^5$ at 0.002% — is what one gets when one computes the Bergman bulk-volume to Shilov-fiber-volume ratio for the substrate. The ratio between bulk and boundary states *is* the ratio between proton-type and electron-type particles.

### Shilov boundary — the distinguished edge

The second boundary condition lives on the **Shilov boundary** of $D_{IV}^5$. The Shilov boundary, named for the Russian mathematician Georgi Shilov, is a specific subset of the topological boundary of a bounded domain: it is the smallest closed subset of the boundary on which every holomorphic function on the domain attains its maximum modulus. For $D_{IV}^5$, the Shilov boundary has dimension 2 — equal to the rank — and is approximately a two-dimensional torus, decorated with the symmetric-domain structure.

The Shilov boundary is where the substrate's "primitive cycle" states live — states defined by topological windings on the distinguished boundary rather than by interior bulk geometry. Casey's Saturday W-53 work identified the **electron** as a Shilov-boundary primitive cycle. The electron's substrate description is, in its essence, a winding number on the rank-2 torus that the Shilov boundary defines. Its mass and its other physical properties are set by the Shilov-boundary geometry, not by the bulk. The same boundary structure provides the substrate description of neutrinos (W-55, SO(2)-trivial windings).

Bulk versus Shilov is therefore not a fine technical distinction. It is the substrate's structural source of the difference between massive-bulk-states and light-boundary-states — proton-class versus lepton-class matter. The fact that this distinction exists at all, in the form it does, comes from the bounded-domain character of $D_{IV}^5$. A non-bounded geometry would not have a Shilov boundary, and the bulk-versus-boundary distinction would not be available.

## 5.2 The four cycle boundaries

The substrate's commitment cycle (Chapter 3) divides each Koons tick into four phases. Each phase has its own boundary condition — a statement about what happens at the *temporal* boundary of that phase, where it hands off to the next.

We label the four phase-boundaries by their zones, and describe them briefly:

**BC3 — the absorption boundary (Zone 1).** At the start of the cycle, the substrate receives information from its environment. The boundary condition is an *input* condition: substrate-external information crosses inward, and substrate-internal information content increases. In standard physics' language, this is the analog of a Neumann condition — a specification of *flux in*, rather than a specification of *value at the boundary*.

**BC4 — the bulk-computation boundary (Zone 2).** Within Zone 2, the substrate processes the absorbed information by Bergman-geometric dynamics on the interior. The boundary condition here is *consistency*: the state at the end of Zone 2 must be consistent with the state at the start, transported by the substrate's natural dynamics on $H^2(D_{IV}^5)$. There is no input or output flux; this is the substrate's internal-evolution boundary.

**BC5 — the commitment boundary (Zone 3).** This is the projection boundary. The Bergman-kernel reproducing operator (which we introduced as the structural origin of measurement in Chapter 3) acts here, projecting the evolved Zone-2 state onto a definite outcome. The boundary condition is a *projection condition*: the state crossing from Zone 2 to Zone 3 is forced into an eigenstate of the relevant observable.

**BC6 — the emission boundary (Zone 4).** At the end of the cycle, the substrate broadcasts its committed state to its environment. The boundary condition is an *output* condition: substrate-internal information content decreases as information crosses outward to environmental absorption. This is the Dirichlet analog — a specification of value on the active edge.

Each of the four phase boundaries is a *projection* of the substrate's single state onto a specific cycle phase, not a separate substrate. (We pressed this point in Chapter 3: four projections, not four substrates. The same care applies here.) The four boundary conditions are operationally distinct because the substrate is doing operationally distinct things at each phase, but they are all conditions on the *one* substrate's *one* state.

## 5.3 The cosmological boundary

The seventh boundary condition treated in this curriculum is **cosmological**. It couples the substrate, at long-distance Scale 3, to the cosmological-scale structure of the universe — the cosmic horizon, the cosmological vacuum, the cosmological constant.

The cosmological boundary condition is not arbitrary. The substrate's Zone 2 vacuum — the Bergman-geometric ground state of the bulk-computation phase — has a Casimir-style structure that turns out to be *equal*, at the appropriate scaling, to the cosmological vacuum that produces dark energy. Lyra's T2418 (May 2026, "$\Lambda$-Casimir vacuum unification") makes this explicit: the same substrate vacuum that produces the laboratory Casimir effect at $\sim 10^{-6}$-meter scales produces, at $\sim 10^{26}$-meter scales, the observed cosmological constant. They are not analogies; they are the same vacuum, projected at different scales of observation.

The numerical content of the cosmological boundary condition is striking. The cosmological constant in BST is

$$\Lambda \;=\; g \cdot \exp\!\big(-C_2 \cdot (g^2 - \text{rank})\big) \;=\; 7 \cdot e^{-282},$$

a tiny number that matches the observed value of $\Lambda$ to 0.076 of a decimal exponent. The expression uses only the BST primary integers we have already met. No tuning, no anthropic argument, no separate dark-energy hypothesis. The cosmological constant is the substrate's Zone-2 vacuum at cosmological scale. Volume 4 develops this in full.

The CMB scalar spectral index $n_s$ is another cosmological-boundary observable: BST predicts $n_s = 1 - n_C / N_{\max} = 1 - 5/137 \approx 0.9635$, where the $5/137$ correction is the cosmological boundary's inheritance of the substrate's $N_{\max}$ cap (Chapter 2). The match to the Planck satellite measurement is at the 0.3-standard-deviation level — well within experimental error, and structurally derived.

The cosmological boundary is, for BST, what makes the substrate framework a complete picture rather than a microphysics-only theory. The same five integers that determine the proton-electron mass ratio determine the cosmological constant. The same Bergman vacuum that yields the laboratory Casimir force yields dark energy. The substrate runs at every scale; the cosmological boundary is where it ties to the largest of them.

## 5.4 Each boundary, each integer

A pattern visible in the framework is that the seven boundary conditions of this curriculum each carry a distinct BST primary signature. The mapping is candidate-level work, not yet fully theorem-grade, but the structural picture is clear enough to present:

| Boundary condition | Primary integer | Where it shows up |
|---|---|---|
| Bulk (BC1) | All five, plus $N_{\max}$ | The substrate's interior carries every primary |
| Shilov (BC2) | $\text{rank} = 2$ | The Shilov dimension equals the rank |
| Absorption (BC3) | $g$ and $N_{\max}$ | Input flux capped by the gauge-dimension scale |
| Bulk computation (BC4) | $C_2$ | Casimir-driven interior dynamics |
| Commitment (BC5) | $n_C$ | Dimension consolidation at projection |
| Emission (BC6) | $N_c$ | Output structured by the color sector |
| Cosmological (BC7) | All five | $\Lambda$ depends on every primary |

The bulk and the cosmological boundary share the property that they involve *all* the integers — they are the substrate's most structurally rich boundaries, the two that carry the most. The four cycle boundaries each single out one primary. The Shilov boundary is rank-anchored.

The reader should not memorize this table; the assignments are still settling, and Volumes 1 through 4 will use the right boundary condition in the right physical context without making the per-integer anchoring explicit. The table is here so that the structural pattern — boundary conditions are not arbitrary, they sit at definite anchorings in the integer web — is visible early.

## 5.5 What the substrate's boundedness buys

It is worth stepping back and noting why this whole framework is even available.

Standard quantum field theory, defined on Minkowski spacetime, has *no* natural distinguished boundary. Minkowski spacetime is unbounded. Boundary conditions in QFT are conventional — vanishing at spatial infinity, plane-wave asymptotics, periodic boxes — chosen for calculational convenience rather than required by the theory's geometry. The resulting theory is consistent, but the choices are external.

$D_{IV}^5$ is bounded. Its boundary is a genuine geometric feature of the substrate, not a mathematical convention. The Shilov subset of the boundary is distinguished by a holomorphic-function maximum principle, not by a calculational fiat. The four-phase cycle's boundaries are defined by the cycle structure itself. The cosmological boundary's identification with the Zone-2 vacuum is a theorem (T2418), not an interpretation.

This is one of the structural advantages BST has over its standard-physics counterparts. Boundary conditions are *part of the geometry*, and the geometry tells you what they are. The book benefits at every later chapter from this fact: when we need to know what boundary conditions to impose on the Schrödinger equation in Volume 5, or on the gauge theory in Volume 7, or on the gravitational field in Volume 4, we look at the substrate boundary condition that applies, rather than guessing.

## 5.6 What comes next

Chapter 6 introduces what Grace named the **integer web** — the network of cross-identities among the BST primary integers that we glimpsed in Chapter 2 (Universal 42, Universal 126, the Bergman normalization $c_{FK} \cdot \pi^{9/2} = 225$, the additive Mersenne identity, and a small forest of others). Chapter 6 elevates this network from a curiosity to a Casey-named structural principle, and shows that its topology is itself a substrate signature.

Chapter 7 — the operator zoo — finally collects together all the operators we have introduced in this volume and presents them as a single organized table, ready for use throughout the rest of the curriculum.

Chapter 8 derives the conservation laws by Noether's theorem applied to the substrate's symmetry structure of Chapter 4.

Chapter 9 returns to Strong-Uniqueness — the theorem that $D_{IV}^5$ specifically, and not some other bounded symmetric domain, is forced by the multi-criterion convergence we sketched in Chapter 1.

---

**Where to look this up**: The bulk-versus-Shilov boundary distinction is a standard feature of bounded-symmetric-domain analysis; see Helgason 1978 Chapter X for the geometric framework and Faraut–Koranyi 1994 for explicit Shilov-boundary computations on Type IV domains. The proton-as-bulk-geodesic and electron-as-Shilov-primitive-cycle identifications are Casey's Saturday W-53 and W-54 work, with the proton-to-electron mass ratio derived in Volume 2 Chapter 6. The $\Lambda$-Casimir vacuum unification is Lyra T2418, with the cosmological-constant numerical match in Volume 4 Chapter 4. The CMB spectral index prediction $n_s = 1 - 5/137$ is documented as Elie Toy 1401 and derives from the cosmological-boundary inheritance of $N_{\max}$. The substrate-derivation theorems for each boundary condition are queued as SP-31-40 sub-items in the BST research backlog; per-boundary theorems are filed under T-numbers as they mature.
