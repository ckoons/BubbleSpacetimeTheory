---
title: "Lecture 4 — Time"
spine: "D_IV⁵: QM, GR and the SM — the derivations, tiered"
author: "Keeper, for Casey Koons and the team"
date: "2026-09-11 — v0.1"
sources: "'Time, Derived' v1.0 (Lyra, 2026-08-17; FULL Keeper pass K1670, 2026-08-18; ships on Casey's word) — Sections 1–8 and 12; Fernando–Günaydin arXiv:1409.2185 for the singleton weights (scalar E = 3/2, Section 7 eq 7.1; spinor E = 2, Section 9 Table 2); T1136 (the Koons tick; 2π ruling and wording fix of 09-07, K1877); K1687 (charge in the SO(5) Cartan; the K-centre is time's rotation); the positive-time ontology note (CPT-mirror impossible; the arrow is dynamical, not geometric); K1880–K1884 (the nucleation lane); K1884 (the α-drift withdrawal)"
tier_line: "DERIVED: time as the flow parameter of the commitment semigroup exp(−τJ); STRUCTURE-DERIVED (the paper's own word): the generator J = the SO(2)-centre weight (the linear conformal Hamiltonian), not the Casimir; POSIT (T2625 clause (i), named as an input in Lecture 2): the positive-time sector; the arrow = spectrum positivity; the two Wick faces (a standard theorem, cited). DERIVED on H² (Cal §954): the degree-2 cover of the imaginary circle is forced by odd n_C; NOTE, not a claim: on the two-singleton composites the cover is fermion parity. IDENTIFIED: the value of the elementary tick ℏ/E. DEFINITION: the Koons tick τ₀ = N_max·ℏ/(m_e c²) = a₀/c ≈ 0.1765 as — the program's clock unit, in T1136's own convention. FLOORED: the nucleation survivor. NOT CLAIMED: a preferred frame; periodic physical time; an observable 4π; α drift."
---

# Lecture 4 — Time

## The question

What is time, in a geometry that has none built in — and why does it run one way?

The object of Lecture 1 has ten real dimensions and a positive-definite metric. Nothing in it moves. There is no axis labelled $t$, and if there were, the symmetry group would move it somewhere else. Yet the physics we read off the object has a time — the Schrödinger evolution of Lecture 3 needs a parameter, and measurement in Lecture 3 was a *commit*, something that happens and cannot un-happen. This lecture says where that parameter comes from and why it has a direction. It is, in our own accounting, the place where the program's derivation is most nearly complete: the arrow and the two faces of time are readings of one operator the geometry hands us — *given one posit*, which we name below rather than hide.

## For the reader in a hurry

Our shape has a circle at its centre — one of the two pieces of the group that leaves a point fixed. Nothing turns that circle by itself. But the *records* on the shape's edge (Lecture 3) can only be made in one order, and "how far the record-making has run" turns out to be exactly "how far around that circle we have gone." That is time: not a stage the play is performed on, but a count of what has been committed. It runs one way because the operator that turns the circle has a lowest energy and no highest — you can always run it forward and never backward. And it has a smallest step, about a sixth of a billionth of a billionth of a second, which is the time light takes to cross the radius of the hydrogen atom's smallest orbit.

## The generator is forced, and it is not the obvious one

Recall $K = \mathrm{SO}(5) \times \mathrm{SO}(2)$, the stabiliser of a point. The $\mathrm{SO}(2)$ factor is a circle; its Lie algebra is one-dimensional; call its generator $J$. On the Hardy space $H^2(D_{IV}^5)$ — the physical space of Lecture 3 — $J$ acts with a discrete spectrum, and the eigenvalue of $J$ on a state is that state's **conformal weight** $E$. This is the **linear conformal Hamiltonian**: the $U(1)$ energy of the representation.

Two things about it are derived and were not obvious to us.

**It is $J$, not the Casimir.** The Axioms paper (Lecture 3's source) took the quadratic Casimir $C_2(K)$ as the time generator; "Time, Derived" corrected it, and the two vetted papers still disagree on the row — a collision ruled here for $J$; T2631's items 2–3 were registered from Cal's pre-amendment text and still name the $K$-Casimir — the annotation recording the collision is owed to Grace (Cal, third pass). The reason is structural, and it is *not* the one the paper gave: $J$ is exactly as central in $K$ as the Casimir is (Cal, second pass). Nor is it that the Casimir is scalar: $C_2(K)$ is the Casimir of $K$, not of $G$, and on $H^2$ both it and $J$ are scalar on every $K$-type and non-scalar overall — both generate diagonal flows that re-weight $K$-types and move nothing inside one (Cal, second pass; an earlier draft of this paragraph gave the scalar-on-irreps reason, which is right for the $G$-Casimir and wrong for this one). The discriminator is the dictionary: energy *is* conformal weight — the standard conformal Hamiltonian, linear in the weight — and a damping quadratic in the weight is not a Schrödinger evolution. That assignment is the paper's, and it is what makes $J$ the generator. The paper's own tier for this is Structure-Derived, and that is the word we keep; an earlier draft of this lecture promoted it to "forced," which Cal caught.

**Which space — ruled.** Lyra's fact read caught that "Time, Derived" was written five days before the W1 resolution and computes on the *singleton* spaces — the scalar singleton (Rac) at $E = 3/2$ and the spinor singleton (Di) at $E = 2$, weights read from Fernando–Günaydin — and on their composites, where every weight is $E = \tfrac32\,\#\mathrm{Rac} + 2\,\#\mathrm{Di} + n$. The Hardy space $H^2$ of Lecture 3 is a different representation: its lowest weight is $5/2$, and its weights are $n_C/2 + k$. **Cal ruled (Round 143, Section 954): this lecture is about $H^2$.** The register's state space is $H^2$ (T2625 (i), T2626, T2630, T2631), and the flow of this lecture is Lecture 3's semigroup, which acts there. What that ruling does to each sentence below is stated where it applies.

## Time is the flow, and the arrow is positivity

The commitment dynamics of Lecture 3 — the contractive face — is the one-parameter semigroup

$$\rho_{\text{commit}}(\tau) \;=\; \exp(-\tau J/\hbar).$$

**Time is $\tau$.** Not an external axis against which the semigroup is plotted; the semigroup's own parameter, read as "how far the commitment has run." *When* is a measure of accumulated commitment. There is no clock behind this clock.

**The arrow is that $J$ is bounded below.** $\operatorname{spec} J \geq E_0 = 5/2 > 0$ on $H^2$ (the arrow needs only positivity, and has it on every space in play), so $e^{-\tau J}$ is a contraction, defined for $\tau \geq 0$ and not for $\tau < 0$; the flow has no inverse. That is the arrow of time — not an added postulate, but the statement that the energy operator has a ground state and no ceiling. Energy generates, time counts.

We are careful about what kind of arrow this is. It is the *geometric* arrow — the absolute irreversibility of the contractive face. The *thermodynamic* irreversibility of unwriting an amplified record — its cost — is a separate theorem in the companion paper, and we do not merge the two. And it is **dynamical, not geometric in the other sense**: the shape has no arrow; the dynamics on it does. A CPT-mirror of the substrate — a copy running the other way — is not a second solution that happens not to be realised; it is not a solution at all (the positive-time ontology note). So the program's ontology is pure positive time. One honesty rides with that sentence: *which* of the two holomorphic extensions is the physical one — the forward sector — is a **posit** (T2625, clause (i), registered 2026-09-08), and Lecture 2's account of the program's inputs names it. Given the sector, the arrow is derived; the sector itself is chosen, and we say so. (An earlier draft of this paragraph said "not a boundary condition somebody chose"; Cal caught the contradiction with T2625.)

## Charge is not time

Could electric charge be a reading of the *same* circle — charge as where a state sits, time as the circle turning? For a while we thought so. It is excluded, decisively, by degeneracy: the muon and the neutrino are both Rac$\,\otimes\,$Di composites at the same conformal weight $\Delta = 7/2$, and carry $Q = -1$ and $Q = 0$. So $Q$ is not a function of $J$ at all. Electric charge lives in the Cartan of $\mathrm{SO}(5)$ — internal — and the $\mathrm{SO}(2)$ centre is time's, and only time's (K1687; this was the fifth row that one mislabel had reached). We keep the two words strictly apart: where this lecture says "weight" it means the eigenvalue of $J$; where it says "charge" it means $Q$ on $\mathrm{SO}(5)$.

## The two faces

Because $J$ is self-adjoint and bounded below, $\exp(-zJ)$ is a holomorphic semigroup on the right half-plane $\operatorname{Re} z \geq 0$ (Hille–Yosida; a standard theorem, cited and not claimed). Its two boundary faces are

- the **real-time face** $e^{-\tau J}$, $z = \tau$: the irreversible tick, a half-line;
- the **imaginary-time face** $e^{i\theta J}$, $z = i\theta$: the reversible circle — the unitary evolution of Lecture 3, rule 3.

Euclidean and Lorentzian time are the two edges of one complex parameter, tied by $\tau \leftrightarrow i\theta$. What is specific to this program is not that time has two faces — every bounded-below generator has them — but that the generator is *forced by the geometry*.

**Physical time is not periodic.** Say this plainly, because the word "circle" invites the misreading. The physical flow is the real face: a one-way half-line with no recurrence. The circle is the Wick face, and its role is a *selection rule* on which states are admissible (next section). We never claim time comes back around.

## The circle closes twice — and that is spin-statistics, not a prediction

The imaginary circle's minimal period is fixed by the spectrum of $J$: within a superselection sector, $T = 2\pi / \gcd\{\text{weights}\}$, and $T = 4\pi$ exactly when the gcd is $\tfrac12$. The Rac's $3/2$ supplies the half-integer, so the circle is represented faithfully only on its **degree-2 cover**: $e^{2\pi i J} = -1$ on half-odd-weight states.

Here is the honest content of that fact, on $H^2$ — the ruled space. The weights are $n_C/2 + k$, so one turn acts as $e^{2\pi i J} = e^{i\pi n_C} = -1$ on *every* state exactly when $n_C$ is odd: **the double cover is forced because $n_C = 5$ is odd** — a one-line theorem on $H^2$. That is the sentence the paper retracted; on the space the paper computed on it was false, and on the space this lecture is about it is true (Cal, Section 954). What does *not* live on $H^2$ is the fermion-parity reading: $e^{2\pi iJ} = (-1)^{\#\mathrm{Rac}} = (-1)^F$ holds on the two-singleton *composites* — a different representation, at $\nu = 3/2$, reached only through the identification particles $=$ composites — where fermions ride the cover (720°) and bosons do not, the geometric restatement of spin-statistics. On $H^2$ every state rides it, so the cover carries no parity grading there. We keep the composite reading as a *note*, not a claim, and we keep the retraction in print for what it was: a true statement about a space the lecture turned out not to be about. And the $4\pi$ is not observable by interferometry on either space: an interferometer measures phase *differences*, period $2\pi$; its content is a selection rule, and we say so rather than promise a fringe.

## Two ticks, and which is which

Two quantities in this program are called "the tick," and one of the lessons of September was to stop letting one word carry two objects.

**The elementary tick** of the paper is $\hbar/E$ for the relevant energy: the smallest step of the commitment flow. Its *value* is identified, not derived (the paper's own Section 8 says so), and we do not lean on it.

**The Koons tick** (T1136) is the program's clock *unit* for writes:

$$\tau_0 \;=\; N_{\max}\,\frac{\hbar}{m_e c^2} \;=\; \frac{a_0}{c} \;\approx\; 0.1765 \text{ attoseconds},$$

$137$ reduced Compton times of the electron — equivalently the Bohr radius over the speed of light. It is a *definition*, and its convention matters: $\tau_0$ is $137$ **radians** of the central circle — about $21.8$ turns — a duration, not $137$ turns; and not a count of writes per push either, because push and write are one event (T2630/K1888; an earlier draft of this sentence still counted them separately). One of us wrote "137 turns $= 1.1$ as" in September; it was a convention slip, caught within the day, and the standing rule that came out of it is to quote the invariant, not the coordinate. The row's own text also once wrote $\nu_C = m_e c^2/\hbar$ for what is an angular frequency; it now reads $\omega_C$.

Because $\alpha$ enters T1136 as a ratio fixed *through the success of a write*, the program's $\alpha$ is constant by definition, and no laboratory drift bound reaches it. We withdrew a claim to the contrary the day it was made (Lecture 8).

## What survives a reset

If time is commitment and the universe has cycles, what does the clock carry across a reset? Casey asked this in September and the answer is a floor (K1880–K1884): there is **no lawful initialisation vector**. A reset that is a law of the substrate is $\mathrm{SO}(5)$-equivariant, and the equivariant survivors of the record space are the constants; the direction average on every saturated state is zero. What survives is a *distribution on the winding count* — four to twelve bits — and nothing lawful consults it. Re-entry fails (the environment is legible, not remembered). We had hoped for a richer starting point and did not find one; the floor has three witnesses and stands.

## Tier line

- **Derived:** time as the flow parameter; the arrow as positivity (given the sector); the two Wick faces; charge internal.
- **Structure-derived:** $J$ as the generator (the paper's own tier).
- **Posit, named:** the positive-time sector (T2625 (i)).
- **Derived on $H^2$ (the ruled space):** the degree-2 cover is forced by odd $n_C$. **Note, not a claim:** on the composite representation the same cover is fermion parity — a consistency with spin-statistics, carried as a note.
- **Identified:** the value of the elementary tick.
- **Definition:** the Koons tick $\tau_0 = a_0/c$.
- **Floored:** the nucleation survivor.
- **Ruled (Cal, Section 954):** this lecture is about $H^2$; the double cover is forced by odd $n_C$ there; the fermion-parity reading is a note on the composite representation.
- **Open:** no row relates the record space $H^2$ to the particle space of two-singleton composites — the referee's first question about this lecture, and the row is owed.
- **Not claimed:** a preferred frame (the corpus derives frame-independence from the group's transitivity on the domain, and the honest form is "the program cannot derive a preferred frame," not "none exists"); periodic physical time; an observable $4\pi$; $\alpha$ drift; "nothing imported."

## What would make this lecture wrong

A physical process that reverses a committed record at zero cost — an inverse to the contractive face — would falsify the arrow as derived. A boson found to ride the double cover, or a fermion the single one, would break the parity identity, which is protected for free-field singleton weights and *not* protected against anomalous dimensions (the paper says so). Neither is a near-term laboratory test, and we do not dress them as one. The honest exposure is the identified tick value and the open question of what, if anything, the clock's rate has to do with $\alpha$.

## Where to look

"Time, Derived" v1.0 (2026-08-17), Sections 1–8 and its Section 12 — the list of what it does not claim is the paper's strength; K1670 for the pass; Fernando–Günaydin for the weights; T1136 with its 09-07 annotations; K1687; K1880–K1884 for the reset floor. One alias to carry: the paper's abstract writes "$H^2(D_{IV}^5)$, the Bergman space" — read *Hardy* (the W1 resolution came five days after the paper).
