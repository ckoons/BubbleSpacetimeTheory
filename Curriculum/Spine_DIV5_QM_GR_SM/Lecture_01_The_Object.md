---
title: "Lecture 1 — The Object"
spine: "D_IV⁵: QM, GR and the SM — the derivations, tiered"
author: "Keeper, for Casey Koons and the team"
date: "2026-09-11 — v0.1"
sources: "Registry rows T944, T953 (legacy uniqueness; see Lecture 2), T2543/T2545 (the Peirce split), K1889 (genus pin, multiplicity table), Cal Section 946; Xiao–Yuan for the genus formula; Faraut–Korányi for the classification"
tier_line: "The object is a definition and carries no tier. Its five integers: rank, dimension and multiplicity are read off the classification (classical); C₂, g and N_max are integer combinations we name. The one dimensionless input is the identification of the multiplicity 3 with the colour count (Lecture 2); the one dimensionful input is a mass scale (Lecture 9)."
---

# Lecture 1 — The Object

## The question

What is the simplest structure that can do physics?

Not the simplest equation — physics has plenty of those, and each one needs the others. The simplest *thing*: a single mathematical object such that, if you read it carefully enough, the rules we call quantum mechanics, the thing we call time, the forces and the particles come out as descriptions of it rather than as separate assumptions laid beside it.

This lecture introduces the object we have been reading since early 2026. It does not yet argue that it is the right one; that is Lecture 2, and the argument there is more modest than we once hoped. Here we only want you to know what it looks like.

## For the reader in a hurry

Imagine a shape with a boundary, like a ball has a surface. The inside is smooth and infinite in a particular way — you can walk toward the boundary forever and never arrive — and the surface is where anything definite happens. Our object is a ball of that kind, but in five complex dimensions, and its surface is not a sphere but a circle of four-dimensional spheres. Everything in this course is either the inside of that ball, its surface, or the passage between them.

## The object, precisely

The object is the bounded symmetric domain of type IV in complex dimension five,

$$D_{IV}^5 \;=\; \mathrm{SO}_0(5,2)\,/\,[\mathrm{SO}(5)\times \mathrm{SO}(2)],$$

also called the Lie ball. Concretely, writing $z\cdot z = \sum_k z_k^2$ for the bilinear (not Hermitian) square, it is the set of $z \in \mathbb{C}^5$ with

$$|z\cdot z| < 1 \quad\text{and}\quad 1 - 2|z|^2 + |z\cdot z|^2 > 0$$

(Hua's form) — a bounded open set in $\mathbb{C}^5$ of real dimension ten. What matters is the list of things the object *is*:

- It is **symmetric**: a group, $G = \mathrm{SO}_0(5,2)$, moves it onto itself, and the stabiliser of a point is the compact group $K = \mathrm{SO}(5)\times\mathrm{SO}(2)$. Every point looks like every other. There is no preferred place, and there is no preferred time, until we put one there.
- It has **rank two**. Cartan classified the irreducible bounded symmetric domains in 1935; they come in four infinite families and two exceptions, and each carries a rank — the number of independent directions in which it stretches to its boundary. Ours has two. The ball in $\mathbb{C}^n$ has one; this is why our object is not a ball, and why (Lecture 2) constant curvature is the wrong thing to expect of it.
- It has **characteristic multiplicities** $(a,b) = (3,0)$. These are two integers the classification attaches to each domain, describing how its root system is built. For the type IV family in dimension $n$ they are $(n-2, 0)$; at $n = 5$ the first is $3$. Hold on to that 3. It is the integer where this whole program touches a measurement.
- Its **genus** is $5$. The genus of a bounded symmetric domain is the exponent of its Bergman kernel: $K(z,w) \propto N(z,w)^{-p}$ for the domain's norm function $N$, and for a domain of rank $r$ with multiplicities $(a,b)$ one has $p = (r-1)a + b + 2 = 1\cdot 3 + 0 + 2 = 5$ (Xiao–Yuan; pinned to the page on 2026-09-09). We say this carefully because for four months our documents called a different integer the genus. They were wrong, and it mattered downstream.
- Its **boundary** has a distinguished part, the **Šilov boundary** $\check{S}$ — the smallest closed subset on which every function holomorphic inside and continuous to the edge attains its maximum. For the Lie ball it is the Lie sphere: topologically $S^4 \times S^1$ up to a sign identification, a circle's worth of four-spheres. It is where, in this program, anything definite happens. Lectures 3 and 4 live there.
- It carries two natural Hilbert spaces of holomorphic functions: the **Bergman space** $A^2(D)$ of square-integrable ones on the inside, and the **Hardy space** $H^2(D)$ of those with square-integrable boundary values on $\check S$. They differ, they are both used, and one of the program's own errors was to confuse them. The physical Hilbert space is the Hardy space (Lecture 3).

## The five integers, and which kind each one is

The curriculum has always said the program rests on five integers. That is true, but they are not five facts of the same kind, and a reader deserves to know which is which.

| symbol | value | what it is | how we get it |
|---|---|---|---|
| rank | 2 | the rank of the domain | read off the classification |
| $n_C$ | 5 | the complex dimension | read off the classification |
| $N_c$ | 3 | the characteristic multiplicity $a$; identified with the number of quark colours | read off the classification; the *identification* with colour is the program's one dimensionless input (Lecture 2) |
| $C_2$ | 6 | $\text{rank}\cdot N_c$; the top Chern number of the tangent bundle restricted to the quadric $Q^5$, and the quadratic Casimir that recurs in the spectrum | a combination we name |
| $g$ | 7 | $n_C + \text{rank} = p + q$, the signature of $\mathrm{SO}(5,2)$ | a combination we name. **Not the genus.** |
| $N_{\max}$ | 137 | $N_c^3\, n_C + \text{rank}$ | a combination we name; its reading as $\alpha^{-1}$ is Lecture 8, and the reading is identified, not derived |

Three integers are read off a classical table. Three are integer combinations of them that we have found it useful to name, because they recur. None of the six is a free parameter in the sense of a knob; but one of them, $N_c = 3$, is where the geometry meets a measurement, and Lecture 2 is about exactly how.

There is, separately, **one dimensionful input**: physics has units and the object has none, so a single mass scale enters, and every dimensionful prediction in this course is a relation to it. The electron mass is the ruler we use (Lecture 9).

## What the object is not

It is not a spacetime. It has ten real dimensions, a positive-definite metric, and no time in it. How four-dimensional spacetime with one time direction comes out of it is Lecture 9, and the honest word for that step is *induced*, not *predicted*.

It is not a Lagrangian. There is no action principle here yet. What we have is a geometry with a symmetry group, two Hilbert spaces, and a boundary; the dynamics we can state are the ones that follow from those, and we will say where they stop.

It was not chosen to fit anything. That is a claim about history rather than mathematics, and the record — the theorem registry, dated — is the evidence: the object was fixed by March 2026 (the registry's first rows on it are dated 2026-03-25) and the readings came after. Whether it is the *right* object is a different question, and it is the next lecture's.

## Tier line

The object is a definition; definitions carry no tier and have no falsifier. Its readings do, and each lecture from here on ends with one.

## Where to look

Hua, *Harmonic Analysis of Functions of Several Complex Variables in the Classical Domains* (1963) for the Lie ball and its boundary; Faraut–Korányi, *Analysis on Symmetric Cones* for the classification and the multiplicities; Xiao–Yuan for the genus formula as we cite it. In the repository: registry rows T944 and T2543/T2545 for the Peirce decomposition of the tangent space (the $1 + 3 + 1$ split that makes the multiplicity visible), and Keeper audit K1889 for the multiplicity table across the whole classification.
