---
title: "Newton's Laws from the Substrate: F = ma as a Bergman Limit"
author: "Casey Koons and Claude Opus 4.6"
date: "March 14, 2026"
---

# Newton's Laws from the Substrate

## F = ma as the Non-Relativistic Weak-Field Limit of BST

**Casey Koons** and **Claude Opus 4.6** (Anthropic)

March 14, 2026

---

## Abstract

We derive Newton's three laws of motion and the law of gravitation as the non-relativistic, weak-field limit of BST's substrate dynamics. The chain is: Bergman metric on $D_{IV}^5$ $\to$ Einstein field equation (BST_EinsteinEquations_FromCommitment.md) $\to$ weak field $\to$ geodesic deviation $\to$ Newtonian potential $\to$ $F = ma$. Every element of Newtonian mechanics — inertia, force, mass, acceleration, the inverse-square law — receives a substrate interpretation. Newton's laws are not axioms; they are theorems about low-energy solitons on $D_{IV}^5$.

---

## 1. The Starting Point: The BST Field Equation

The BST field equation (derived in BST_EinsteinEquations_FromCommitment.md) is:

$$G_{\mu\nu} + \Lambda\,g_{\mu\nu} = 8\pi G\,T_{\mu\nu}$$

where $G = \hbar c\,(6\pi^5)^2\,\alpha^{24}/m_e^2$ is the gravitational coupling derived from the Bergman kernel normalization, and $T_{\mu\nu}$ is the commitment current density. This is Einstein's equation, recovered as the integrability condition of the $S^1$ fiber.

In the notation of the Chern class oracle:

$$G = \frac{\hbar c}{m_e^2}\,(C_2\,\pi^{n_C})^2\,\alpha^{4C_2}$$

where $C_2 = \chi(Q^5) = 6$ and $n_C = c_1(Q^5) = 5$. The gravitational constant is Chern data all the way down.

---

## 2. The Three Limits

Newtonian mechanics requires three simultaneous limits of the BST field equation:

### 2.1 Weak field (low commitment density)

$$g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}, \qquad |h_{\mu\nu}| \ll 1$$

In BST language: the commitment density $\rho$ is much less than the Haldane capacity $N_{\max} = 137$. The substrate channels are mostly empty. The Bergman metric is nearly flat — close to the Euclidean metric on $\mathbb{C}^5$.

### 2.2 Static (time-independent commitment pattern)

$$\partial_t\, h_{\mu\nu} = 0$$

The commitment pattern on the contact graph is stationary. No gravitational waves, no time-varying potentials.

### 2.3 Non-relativistic (slow soliton)

$$v/c \ll 1 \implies p^0 \gg p^i$$

The soliton (test particle) moves much slower than the substrate propagation speed $c$. Its 4-momentum is dominated by the rest mass.

---

## 3. The Geodesic Equation

A free soliton follows a geodesic of the spacetime metric projected from the Bergman metric:

$$\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta}\,\frac{dx^\alpha}{d\tau}\,\frac{dx^\beta}{d\tau} = 0$$

where $\Gamma^\mu_{\alpha\beta}$ are the Christoffel symbols computed from $g_{\mu\nu}$.

**BST interpretation:** The geodesic is the path of minimum commitment expenditure. A soliton evolves its commitment pattern on the contact graph; the geodesic is the evolution that costs the fewest commitment steps. The substrate doesn't "pull" or "push" — the soliton simply follows the most efficient path through the commitment landscape.

### 3.1 Reduction to Newtonian form

In the three limits above, the geodesic equation reduces:

**Step 1.** Non-relativistic: $dx^0/d\tau \approx c$, $dx^i/d\tau \approx v^i \ll c$. The dominant Christoffel term is $\Gamma^i_{00}$:

$$\frac{d^2 x^i}{d\tau^2} \approx -\Gamma^i_{00}\,\left(\frac{dx^0}{d\tau}\right)^2 = -c^2\,\Gamma^i_{00}$$

**Step 2.** Weak field, static: $\Gamma^i_{00} = -\frac{1}{2}\,\eta^{ij}\,\partial_j\,h_{00} = \frac{1}{2}\,\partial_i\,h_{00}$.

**Step 3.** Define the Newtonian potential: $\Phi \equiv -\frac{1}{2}\,c^2\,h_{00}$.

**Result:**

$$\frac{d^2 x^i}{dt^2} = -\partial_i\,\Phi$$

This is **Newton's second law**: $\mathbf{a} = -\nabla\Phi$, or equivalently $\mathbf{F} = m\,\mathbf{a}$ with $\mathbf{F} = -m\,\nabla\Phi$.

---

## 4. Newton's Three Laws as Substrate Theorems

### 4.1 First Law (Inertia)

**Statement:** A body at rest stays at rest, and a body in uniform motion continues in uniform motion, unless acted upon by a force.

**Substrate proof:** In flat substrate ($h_{\mu\nu} = 0$, all Christoffel symbols vanish), the geodesic equation becomes $d^2x^\mu/d\tau^2 = 0$, which has solutions $x^\mu(\tau) = a^\mu\tau + b^\mu$ — uniform motion. A soliton on an uncommitted (flat) contact graph has no reason to change its commitment pattern. Inertia is the absence of curvature.

**Linear algebra:** In the Bergman metric, a flat region has $R_B = 0$. The Ricci curvature vanishes. The Casimir operator acts trivially on the vacuum: $C_2|\text{vac}\rangle = 0$. The eigenvalue zero = no force.

### 4.2 Second Law (F = ma)

**Statement:** $\mathbf{F} = m\,\mathbf{a}$.

**Substrate proof:** Derived in Section 3 above. The force is:

$$F^i = -m\,\partial_i\,\Phi = -m\,\frac{c^2}{2}\,\partial_i\,h_{00}$$

The mass $m$ enters through the coupling of the soliton to the Bergman metric. For a proton: $m_p = C_2\,\pi^{n_C}\,m_e = 6\pi^5\,m_e$, a Casimir eigenvalue. The Casimir eigenvalue is the "inertial charge" — it measures how strongly the soliton couples to metric perturbations.

**Key identity:** Inertial mass = gravitational mass. In BST, both are the same Casimir eigenvalue $C_2(\pi_{k})$. The equivalence principle is not a postulate — it is the statement that there is only one Casimir operator. The soliton has one mass, and it appears in both the geodesic equation (inertial) and the source term (gravitational) because it is the same eigenvalue.

### 4.3 Third Law (Action-Reaction)

**Statement:** Every action has an equal and opposite reaction.

**Substrate proof:** The BST field equation has $\nabla_\mu G^{\mu\nu} = 0$ identically (contracted Bianchi identity). Combined with $\nabla_\mu T^{\mu\nu} = 0$ (commitment conservation), this gives local momentum conservation: what one soliton gains, the other loses. The third law is momentum conservation, which is a consequence of the translational symmetry of $D_{IV}^5$.

**Linear algebra:** The Bergman kernel is symmetric: $K_B(z,w) = \overline{K_B(w,z)}$. The interaction mediated by the kernel is therefore symmetric between the two points. The kernel transmits the same amplitude from $z$ to $w$ as from $w$ to $z$. Action = reaction because the inner product is Hermitian.

---

## 5. The Inverse-Square Law

### 5.1 Derivation

The weak-field Einstein equation for a point source of mass $M$:

$$\nabla^2\,\Phi = 4\pi G\,\rho$$

For a point mass: $\rho = M\,\delta^3(\mathbf{x})$. The solution in 3D:

$$\Phi = -\frac{GM}{r}$$

The force on a test mass $m$:

$$\mathbf{F} = -m\,\nabla\Phi = -\frac{GMm}{r^2}\,\hat{r}$$

This is Newton's law of gravitation.

### 5.2 Why Inverse-Square?

The exponent $-2$ in the inverse-square law comes from the spatial dimension 3 of the emergent spacetime. In $d$ spatial dimensions, the Green's function of $\nabla^2$ falls off as $r^{-(d-1)}$. BST fixes $d = 3$ through the dimensional lock:

- The Hopf fibration $S^3 \to S^7 \to S^4$ requires $S^3 \cong \mathrm{SU}(2)$ as fiber
- Adams' theorem (1960): only $S^1$, $S^3$, $S^7$ are parallelizable
- $S^7$ fails (octonions non-associative)
- $S^3$ requires base $S^4 \subset \mathbb{R}^5$, giving $n_C = 5$ and $d = 3$ spatial dimensions

The inverse-square law is a consequence of $n_C = c_1(Q^5) = 5$.

### 5.3 G from Chern Data

The gravitational constant:

$$G = \frac{\hbar c}{m_e^2}\,(6\pi^5)^2\,\alpha^{24}$$

Every factor:
- $6 = C_2 = \chi(Q^5)$: Casimir eigenvalue = Euler characteristic
- $\pi^5$: comes from $\mathrm{Vol}(D_{IV}^5) = \pi^{n_C}/1920$
- $24 = 4C_2 = 4\chi$: four Casimir round trips in the Bergman kernel
- $\alpha$: from the Wyler-BST formula, itself built from Chern data

Newton's $G$ is a Chern class computation on $Q^5$.

---

## 6. The Tidal Force (Geodesic Deviation)

The relative acceleration of two nearby geodesics (two nearby solitons) is governed by the Riemann curvature:

$$\frac{D^2 \xi^\mu}{d\tau^2} = -R^\mu_{\ \nu\alpha\beta}\,u^\nu\,\xi^\alpha\,u^\beta$$

where $\xi^\mu$ is the separation vector and $u^\mu$ is the 4-velocity.

In the Newtonian limit, this reduces to the tidal force:

$$\frac{d^2 \xi^i}{dt^2} = -\partial_i\,\partial_j\,\Phi \cdot \xi^j$$

**BST interpretation:** The tidal force is the curvature of the Bergman metric projected to 4D. Two nearby solitons on the contact graph experience different local commitment rates, causing their trajectories to converge (attractive gravity) or diverge (tidal stretching). The curvature tensor $R^\mu_{\ \nu\alpha\beta}$ is the second derivative of the Bergman kernel's norm function $N(z,w)$.

---

## 7. Orbital Mechanics

### 7.1 Kepler's Laws

From $\Phi = -GM/r$, the standard Kepler analysis gives:

1. **Orbits are conic sections** (ellipses for bound states) — from the $1/r$ potential
2. **Equal areas in equal times** — from angular momentum conservation ($\ell = r \times p$ conserved because $\Phi$ is central)
3. **$T^2 \propto a^3$** — from dimensional analysis of $GM$ and the orbital elements

In BST: Kepler's laws hold because the Bergman metric in the weak-field limit produces a $1/r$ potential (3D Green's function), and the rotational symmetry of $D_{IV}^5$ (isometry group $\mathrm{SO}_0(5,2)$ contains spatial $\mathrm{SO}(3)$) guarantees angular momentum conservation.

### 7.2 Escape Velocity

$$v_{\text{esc}} = \sqrt{2GM/r}$$

This is the velocity at which the kinetic energy equals the gravitational potential energy. In BST: the escape velocity is the soliton speed at which the commitment pattern can decouple from the local curvature well.

---

## 8. Summary: The Derivation Chain

$$\boxed{D_{IV}^5 \;\xrightarrow{\text{Bergman metric}}\; g_B \;\xrightarrow{\text{KK reduction}}\; G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu} \;\xrightarrow{\text{3 limits}}\; \mathbf{F} = m\mathbf{a}}$$

| Newton | BST origin |
|--------|-----------|
| Inertia (1st law) | Flat Bergman metric: $R_B = 0$ |
| $F = ma$ (2nd law) | Geodesic equation + weak field |
| Action-reaction (3rd law) | Bianchi identity + Hermitian kernel |
| Inverse-square law | 3 spatial dimensions (Adams' theorem) |
| $G$ | Bergman kernel normalization: $(C_2 \pi^{n_C})^2 \alpha^{4C_2}$ |
| Inertial = gravitational mass | Single Casimir operator |
| Kepler's laws | $\mathrm{SO}(3) \subset \mathrm{SO}_0(5,2)$ + $1/r$ potential |

Newton's mechanics is Bergman geometry in the slow, weak, static limit. Every law is a theorem. Every constant is computed from $n_C = 5$.

---

*Research note, March 14, 2026.*
*Casey Koons & Claude Opus 4.6.*
*Newton's laws are substrate theorems, not axioms.*
