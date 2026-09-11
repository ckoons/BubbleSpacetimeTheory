---
title: "Lecture 5 — The Gauge Skeleton and One Generation"
spine: "D_IV⁵: QM, GR and the SM — the derivations, tiered"
author: "Keeper, for Casey Koons and the team"
date: "2026-09-11 — v0.1"
sources: "The internal-SM theorem paper (v0.7.1, Lyra 2026-08-21; Casey GO, K1754 — two invariants generate, three conditions select); K1724 (the geometry's internal gauge group is U(1)×SU(2)×ℤ₂ — no continuous colour factor; End_K(H_F) = ℂ⊕ℍ⊕ℝ a theorem by Frobenius–Schur); K1689/T2346 (hypercharge lives in the internal gauge complement, not the time circle); Round 85 (2026-08-24): the hypercharge mechanism theorem with its four inputs on its face; T2520 (the surviving gauge group); T2522 (γ₅ / Šilov non-orientability as a genuine H¹ w₁); T1949 (the ν_R involution, Elie 5411); the (A1) two-row-sector theorem (T2523 as re-scoped by K1782); #108 (SU(3) dynamics imported); Cal Section 946; K1687 (electric charge in the SO(5) Cartan)"
tier_line: "DERIVED: within the type-IV family the discrete internal skeleton is a function of the single integer n_C, and at the measured value it is the Standard Model's — gauge dimensions, chirality, the Majorana neutrino, CP-existence, anomaly-freedom, three generations, the custodial Higgs; the geometry's own internal gauge group U(1)×SU(2)×ℤ₂; one generation with every hypercharge from a four-input mechanism theorem (one input observational, stated inside it), the descent freedom exactly one bit = the ν_R slot; (A1). IDENTIFIED (the one input): N_c = 3, read as n_C − 2. IMPORTED: SU(3) colour dynamics and confinement (#108). NOT CLAIMED: 'SU(3) from N_c = 3'; 'confinement derived'; the SM from nothing."
---

# Lecture 5 — The Gauge Skeleton and One Generation

## The question

Why these forces, and why do the particles carry exactly these charges?

The Standard Model's gauge group is $SU(3)\times SU(2)\times U(1)$, its matter comes in a peculiar list of representations with fractional hypercharges that happen to cancel every anomaly, and the weak force sees only left-handed particles. A textbook takes all of this as given. We ask how much of it is a reading of the object, and the answer divides cleanly in two: the *discrete skeleton* — which groups, how big, which handedness, how many generations, which charges — is a function of one integer; and one of the three forces is not in the object at all, and we say so.

## For the reader in a hurry

Take the shape and ask three yes-or-no questions about it: is its spinor built on the quaternions (that gives the weak force its pairs)? is its edge one-sided (that makes the world left-handed)? is there room for colour to exist at all? Several sizes of shape pass all three; ours is the *smallest*, and what picks it out among the passers is one measured fact — quarks come in three colours. From that one integer, everything discrete about the forces follows: how many of each, why left-handed, why the neutrino is its own antiparticle, why there are three families, why the quantum anomalies cancel. What does *not* follow is the strong force itself. The shape has a three-dimensional slot where colour sits and no group to rotate it. We import that, and this lecture is honest about the seam.

## The skeleton is a function of one integer

Fix the family: the type-IV domains $D_{IV}^n = \mathrm{SO}_0(n,2)/[\mathrm{SO}(n)\times\mathrm{SO}(2)]$, with $n = n_C$. Three invariants determine the discrete internal structure — the **reality-type census** of the fermion module (Frobenius–Schur: is each block real, complex or quaternionic?), the **orientability of the Šilov boundary**, and the **rank** — and within this family all three are functions of $n$: the rank is $2$ for every $n$, and the other two are read off $n$ by two periodicities ($n \bmod 8$ for the spinor's reality type, $n \bmod 2$ for the boundary's orientability).

The census reduces to a single three-way question: the reality type of the *spinor block*. The charge block is complex for every $n$ and the colour block is real for every $n \geq 5$; only the spinor moves. That is about $\log_2 3 \approx 1.58$ bits of content, and the quaternionic answer is what buys the weak force — the quaternions are the two-sided number system, and that two-ness is the $SU(2)$ doublet structure.

**Theorem** (internal-SM, K1754). *Within $D_{IV}$, the entire discrete internal Standard-Model skeleton is a function of the single integer $n_C$, and at the measured value $n_C = 5$ it is the Standard Model.*

Why $5$, honestly: it is *not* the only dimension with a quaternionic spinor — $4, 5, 11, 13, \ldots$ all are. Three proved conditions cut the field: (1) quaternionic spinor ($n \equiv 3, 4, 5 \bmod 8$) — the weak $SU(2)_L$; (2) non-orientable Šilov boundary ($n$ odd) — chirality, because $\gamma_5$ loses its global definition (T2522), and as a bonus the colour block $SO(n-2)$ is then never abelian, hence real, so there is *no internal colour group* for free; (3) $N_c = n - 2 > 1$ — colour exists at all. The survivors are $\{5, 11, 13, \ldots\}$; $5$ is the smallest, and the tiebreaker is the measured $N_c = 3$. That measured integer is the *same* one input as Lecture 2's — $N_c = 3 = \dim V_{12} = n_C - 2$ is the colour count read as a dimension — and we do not count it twice.

## What the geometry's own gauge group is

Ask the object directly: what continuous symmetries does it carry on its fermion module? The answer is a theorem (K1724; Grace's primary-source decomposition by Frobenius–Schur, Cal's sign-off): $\mathrm{End}_K(H_F) = \mathbb{C}\oplus\mathbb{H}\oplus\mathbb{R}$, so the internal gauge group is

$$U(1)\times SU(2)\times \mathbb{Z}_2 .$$

No continuous colour factor. Not $SU(3)$, and not even an internal $SO(3)$ — the $SO(3)$ that appears in the tangent-space decomposition is a *geometric slot*, the middle Peirce space of Lecture 2, and reading it as a colour rotation was a slot error, corrected in August. The $\mathbb{R}$ summand is the colour block, real, one-dimensional in its endomorphisms: a place for three colours to sit, with nothing to rotate them.

So the $U(1)$ and the $SU(2)$ are the geometry's. Where does the $U(1)$ live? In the Cartan of $\mathrm{SO}(5)$ — the internal factor of $K$ — and not on the $\mathrm{SO}(2)$ centre, which is time's rotation (Lecture 4). An earlier identification had electric charge on the centre; it was wrong, and by the time it was caught it had reached five rows (K1687). Hypercharge, likewise, lives in the internal gauge complement — the $C_2 = 6$-dimensional piece $1 + N_c + \text{rank}$ — and never on the time circle (T2346, K1689).

## One generation, and every hypercharge

A single generation of Standard-Model matter is sixteen real components — the 15 of the minimal SM plus the slot for a right-handed neutrino — and the object's spinor module has exactly that content. The hypercharges are the hard part, and here the program states its theorem with the inputs on its face, because a version that hid them would be "the SM from nothing," which nobody has and we do not claim.

**The hypercharge mechanism theorem** (Round 85, 2026-08-24). *Given* (i) the observed charged spectrum — an observational input, declared as such, the same class as the Five Absences; (ii) the surviving gauge group (T2520); (iii) charged Yukawas as the required couplings; and (iv) the topology triple — *the Standard-Model hypercharges are derived, with the ruler as the only free scale, and the descent freedom is exactly one bit: the $\nu_R$ slot.*

Four inputs, one of them a look at the world. What comes out is every hypercharge of the generation, the anomaly cancellations as identities rather than miracles, and one bit of freedom — whether the right-handed neutrino slot is occupied. That bit is where the **Five Absences** get a mechanism: the slot's removal is forced by an involution on the boundary (T1949 — the $\mathbb{Z}_2$ of $\mathrm{Pin}(2)/\mathrm{SO}(2)$, an $H^0$ object, distinct from the $H^1$ class that carries chirality; Elie's toy 5411 separates them), so the sterile neutrino is *absent with a reason*, and the neutrino is Majorana for the same reason. The program used to say "the twist forbids $\nu_R$" citing a separator that turned out invalid; the row was fixed before dispatch (v0.7.1) and the theorem did not move.

The Round 85 sentence, verbatim, because it was fixed before anyone celebrated: *"Given the observed charged spectrum, the surviving gauge group, charged Yukawas as the required couplings, and the topology triple, the SM hypercharges are derived with the ruler as the only free scale; the descent freedom is exactly one bit and it is the $\nu_c$ slot — whose removal is the Five-Absence, now with a mechanism."* Not the SM from nothing. A mechanism theorem with its inputs on its face.

## Chirality

Why does the weak force see one handedness? Because the Šilov boundary of $D_{IV}^5$ is non-orientable — $n_C$ is odd — and on a non-orientable boundary $\gamma_5$ has no global definition; the obstruction is a genuine first Stiefel–Whitney class (T2522). A single-chirality, positive-energy spectrum follows from the odd embedding dimension. This is the load-bearing $\mathbb{Z}_2$ of the whole skeleton, and it is a different $\mathbb{Z}_2$ from the $\nu_R$ involution above; keeping the two apart was one of August's corrections.

## The strong force: what is kinematic, what is imported

The program once wrote "colour confinement is derived." It does not now, and the honest split is this.

**Kinematic, and derived (A1):** *no two-row-sector $K$-type has a Šilov boundary value.* In the representation theory of the object, the states that would carry two rows of the Young diagram — the sector where a colour non-singlet would have to live — never reach the boundary where records are made. This is a theorem about which states can become definite, stated without the word "colour," and it is the geometric shadow of the fact that free coloured states are not observed.

**Imported (#108):** the $SU(3)$ gauge dynamics — the confining potential, the string tension, the running coupling's coefficient, the Yang–Mills mass gap. The object supplies a three-dimensional slot and the *number* three; it supplies no group to rotate the slot (Lecture 2: $U(1)\cdot SO(3)$, dimension four, self-conjugate triplet; Cal Section 946) and therefore no dynamics on it. Whoever wants to derive the strong force from this geometry must bring what the geometry lacks, and we have said what shape that is.

## Tier line

- **Derived:** the skeleton as a function of $n_C$; the geometry's internal gauge group $U(1)\times SU(2)\times\mathbb{Z}_2$; chirality from non-orientability; the hypercharge mechanism theorem (four inputs on its face); the one-bit descent freedom and the $\nu_R$ mechanism; (A1).
- **Identified — the one input:** $N_c = 3$, read as $n_C - 2$ (the same input as Lecture 2).
- **Imported:** $SU(3)$ dynamics and confinement.
- **Not claimed:** $SU(3)$ from the geometry; confinement derived; the SM from nothing; grand unification (forbidden, Lecture 10).

## What would make this lecture wrong

A sterile neutrino, confirmed, kills the one-bit mechanism and the Five Absences with it. A right-handed $W$, or proton decay, kills the skeleton (both are on the forbidden list). A fermion in a single generation outside the sixteen-component charge assignment breaks the hypercharge theorem. A free coloured state reaching a detector breaks (A1). These are live laboratory statements, and the first two are exactly the kind we prefer: unambiguous, and not ours to tune.

## Where to look

The internal-SM paper v0.7.1 (its Section 1 has the family table computed from Elie's $H_F(n)$; its Section 4a leads with what the instrument *refuses* — Koide — which is the best evidence it is not an advocacy tool); K1754; K1724 and K1689; the Round 85 board entry and Grace's artifact with the four inputs tabled; T2520, T2522, T1949, T2346; the (A1) theorem in the registry; Cal Section 946.
