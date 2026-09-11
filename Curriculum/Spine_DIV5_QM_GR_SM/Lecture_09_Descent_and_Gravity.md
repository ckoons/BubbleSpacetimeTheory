---
title: "Lecture 9 — Descent and Gravity"
spine: "D_IV⁵: QM, GR and the SM — the derivations, tiered"
author: "Keeper, for Casey Koons and the team"
date: "2026-09-11 — v0.1"
sources: "The descent row (rubric, 2026-08-22: 'induced, not predicted'); T2543/T2545 (P² = P, codimension one, (3,1) from the long root; T2545's reason-fix owed — the real SO(3) vector, Frobenius–Schur); T2565 (geometry alone cannot select the frame); Cal's ε = 0 frame-agreement falsifier; 'Gravity: the 2→1 Reduction' (Keeper PASS K1673, 2026-08-18) with K1408 (the Kaluza–Klein route circular through ℓ_B) and Cal Section 585 (24 = 4C₂ a supporting identity); the YM/Millennium foundation cell (2026-08-22; Cal R46/K1785: Γ demoted, not dropped); T349 (the Szegő projection exact); Lane Λ (2026-08-26, landing (b), certified; K1057 cap; T2571 reproduced un-fed); Lane I (the ℓ = 2 exclusion theorems); K1674 (the spectral = causal 'crown jewel' at honest floor; the derived causal order stands)"
tier_line: "DERIVED: the descent's structure — a single idempotent step P² = P, codimension one, signature (3,1). INPUT: the frame (an observer/matter datum; T2565 proves geometry alone cannot supply it). THEOREM ABOUT A RELATION: G ↔ m_e to 0.065% — one dimensionful input traded for another, with α identified inside it. CLEARED: the foundation for a gauge theory on H² (G3) — NOT the Clay problem (G6 open). FLOORED: Λ's value (a closed structural form, one named obstacle p ∈ (0,2)); the ℓ = 2 / su(3) native dynamics; the spectral-action weighting. LIVE FALSIFIER: ε = 0 frame agreement. NOT CLAIMED: 'G predicted from nothing'; 'Λ derived'; the mass gap; a dynamical Einstein equation on D_IV⁵; the descent as predicted."
---

# Lecture 9 — Descent and Gravity

## The question

How does a ten-real-dimensional object with no time become the four-dimensional spacetime we live in — and what does it say about gravity?

The object of Lecture 1 is not a spacetime. It has five complex dimensions, a positive-definite metric, and a time that is a rotation of its centre (Lecture 4), not a coordinate. Yet the physics read off it is supposed to be *our* physics, in three space dimensions and one time. This lecture is about the step down, and about what the program can and cannot say once it has taken it. It is the lecture where the word *induced* does the most work, and where we are most careful not to let a relation be called a prediction.

## For the reader in a hurry

The shape does not contain our spacetime; it contains a *way down* to it. There is exactly one kind of step — a projection you can take once and not twice — that drops one dimension and leaves three directions of one sign and one of the other. That much is a theorem. *Which* way down is taken is not in the shape: something has to be looking, and the shape cannot say what. So spacetime is induced, not predicted, and we have a test for whether the looking is being done consistently. About gravity we say one clean thing: Newton's constant and the electron's mass are tied together by the shape to a tenth of a percent. That is a trade of one measured number for another, not a number from nothing, and we refuse to call it more. The cosmological constant's *shape* comes out as a balance; its *value* waits on one power we cannot yet fix.

## The descent: structure derived, frame input

Start from the isometry group $\mathrm{SO}(5,2)$ and ask what a Lorentzian four-space inside the object would have to be. The answer is constrained by the Jordan structure. The step down is a **single idempotent**: a projection $P$ with $P^2 = P$, applied once — there is no second step, because applying it again does nothing. It has **codimension one** — it drops exactly one dimension. And the signature of what it leaves is **$(3,1)$**: three directions of one sign, one of the other. In root terms the $3$ is the multiplicity of the short roots of $B_2$ (the multiplicity $a$ of Lecture 2) and the $1$ that of the long roots (Lyra, Round 142; an earlier draft said "read off the long root," which is not T2545's argument). The three spatial directions are the middle Peirce space of Lecture 2 — $V_{12} \cong \mathbb{C}^3$, the complexified $\mathrm{SO}(3)$ vector, irreducible over $\mathbb{C}$ by Jordan structure theory (T2545) — and the one time direction is the centre's.

That is the structure, and it is derived. One repair rides with it: T2545's argument for the $(3,1)$ count was first written from a real-space premise; the conclusion is unchanged, and the reason is now the irreducibility of $V_{12}$ over $\mathbb{C}$, with "real $SO(3)$ vector" naming its Frobenius–Schur type (Grace's fix, Round 142 G1, commit 704d402d, 2026-09-11; Cal Section 950 scoped the FS clause so that it describes the gap rather than adding a second wall).

Then the honest half. The structure says *what kind* of step down exists; it does not say *which* four-space is selected among the family the step allows. We proved that it cannot: **geometry alone does not select the frame** (T2565). The selection needs a matter or observer input. So the descent is *Machian, forced-except-one-input* — the same shape of statement as the colour identification of Lecture 2 and the $n_C$ tiebreaker of Lecture 5. We used to write that the descent was posited; then that it was derived; the correct word is **induced**: structure from the geometry, selection from what is looking.

What that honesty buys is a real falsifier, Cal's: **$\varepsilon = 0$ frame agreement**. If the descent is induced consistently, the frame picked out by radiation and the frame picked out by matter must coincide; a measured off-slice baseline $\varepsilon \neq 0$ refutes the picture. That is the one genuine laboratory-shaped falsifier in this lecture.

## Gravity as a relation, not a prediction

The program's gravity result is one equation,

$$G \;=\; \hbar c\,\frac{(6\pi^5)^2\,\alpha^{24}}{m_e^{2}}\,,$$

which reproduces Newton's constant to $0.065\%$ from the electron mass. For a while we called this "Newton's constant predicted." We do not now, and the reason is exactly the reason a referee would give.

The relation is a **theorem** (the paper "Gravity: the 2→1 Reduction," Keeper pass K1673): the geometry ties the gravitational scale to the electron's, with the exponent $24 = 4C_2$ as a supporting identity (Cal Section 585) — the Bergman round-trip doubled by $G \propto m_{\text{Planck}}^{-2}$. But every dimensionful prediction needs a dimensionful input; no theory produces a $G$ with no scale in it. What the relation does is **trade one dimensionful input for another**: take $m_e$ as the ruler and $G$ follows, or take $G$ and $m_e$ follows. It reduces two inputs to one. And it carries $\alpha$ to the twenty-fourth power, and $\alpha$ is identified, not derived (Lecture 8) — so the relation's *precision* rests on a measured $\alpha$ as well.

Two further honesties. Six historical readings of this same relation appear across the corpus (F66, T201, T1918, T1955, T1301a, the paper); they count as **one** result, not six confirmations. And a Kaluza–Klein route to the same number, once cited as independent, was found circular — it fed $\ell_B$ back into itself — and is demoted (K1408).

So the sentence is: *the geometry ties $G$ to $m_e$, and we take $m_e$ as the ruler.* Not: *the geometry predicts $G$.*

## The foundation for a gauge theory — and what it is not

Can a Yang–Mills theory live on the object? The foundation questions were settled in August, and the settlement is worth stating because the legacy chapters overstated it.

The physical Hilbert space is $H^2(D_{IV}^5)$, on which $G = \mathrm{SO}_0(5,2)$ acts irreducibly and unitarily (a scalar-type highest-weight representation at $\nu = 5/2$; it is the Bergman space, at $\nu = 5$, that is holomorphic discrete series — Lyra's pin, Round 142; the W1 cell's label is flagged); that the group acts was the lever that decided the question between the two spaces (W1). On $H^2$ directly, locality and the modular structure carry over *verbatim*: the Tomita–Takesaki modular theory, the Bisognano–Wichmann relation between the modular group and boosts, and the transport of locality along it — standard theorems, cited and not claimed. The Szegő projection onto the boundary is exact (T349). So **the foundation clears** — this is the cell the program calls G3.

It is *not* the Clay problem. Whether the resulting theory is genuinely interacting or a generalised free field — G6 — is **open**, and the mass gap is not claimed. A legacy Guide chapter once said otherwise; it is corrected in place. And one demotion that is not a dropping: the arithmetic quotient $\Gamma(137)\backslash D_{IV}^5$, which once carried the QFT lane, is retained only as the *arithmetic-lane* regulator (the Selberg trace formula that produced the $a_e$ match of Lecture 8); the QFT lane runs on $H^2$ (Cal R46, K1785).

## Λ: a closed form with one obstacle

The cosmological constant is $10^{120}$ times smaller than a naive estimate, and any theory of this kind is asked about it. The program's answer improved in August from "a structural floor" to **a closed structural form with one named obstacle**.

The form is a thermostat: a fixed-point balance in which the Koons tick $t_K$ (Lecture 4) is load-bearing,

$$\frac{\Lambda}{\Lambda_P} \;=\; \left(\frac{t_K}{t_P}\right)^{\!2p/(2-p)}\,,$$

with $t_P$ the Planck time and $p$ a *mismatch power* — the $5\to4$ reduction of the residual. The balance exists; both controls pass (one of them, T2571, reproduced *un-fed*, which is what made the control meaningful); the response coefficient enters from the equation's own structure, and a "curvature quantum" that an earlier version needed was shown unnecessary. **The one free thing is $p$.** Its domain is $(0, 2)$; the geometry has not fixed it; and until it does, no evaluation of $\Lambda$ exists and none is claimed. The form is capped *conditional* at every site where it is quoted (K1057's lineage), and the quarantine on the value is forward-transferred: whoever forces $p$ computes the number blind. A forced $p$ outside $(0,2)$ falsifies the form.

## The wall, named

Could the object carry its own gauge dynamics on the spin-2 sector — an Einstein equation, or an $su(3)$ native to the geometry? Two theorems say no, in the only sense that closes a class (Lane I). Every $K$-equivariant antisymmetric bilinear on the relevant carrier contains spin-3; and the typed write channel — the one non-equivariant ingredient the program owns — compresses onto the carrier where dimension forbids spin-3. So the write channel explains *why* there is no native $\ell = 2$ dynamics and supplies none. The door is named: break equivariance or antisymmetry, and say which. Separately, the once-hoped identification of the object's spectral action with its causal order sits at an honest floor (K1674): two candidate weightings failed blind, the tier is "no surviving candidate," not "impossible," and the *derived causal order* — the real result — stands.

## Tier line

- **Derived:** the descent's structure ($P^2 = P$, codimension one, $(3,1)$); the causal order.
- **Input:** the frame (T2565).
- **Theorem about a relation:** $G \leftrightarrow m_e$ at $0.065\%$, $\alpha$ identified inside.
- **Cleared:** the gauge-theory foundation on $H^2$ (G3). **Open:** G6.
- **Floored, doors named:** $\Lambda$'s value ($p$); the $\ell = 2$ native dynamics; the spectral-action weighting.
- **Not claimed:** $G$ from nothing; $\Lambda$ derived; the mass gap; an Einstein equation on the object; the descent as predicted.

## What would make this lecture wrong

$\varepsilon \neq 0$ in the frame-agreement test. A forced $p$ outside $(0, 2)$. A $G$–$m_e$ relation off $0.065\%$ once $\alpha$'s running is accounted at the stated scale. A native spin-2 dynamics exhibited without breaking equivariance or antisymmetry — which the theorems say cannot happen, so an exhibit would be a discovery about the theorems.

## Where to look

The descent row (rubric, 2026-08-22) and T2565; T2543/T2545 with the Round 141 reason-fix; "Gravity: the 2→1 Reduction" with K1673, K1408 and Cal Section 585; the YM foundation cell (2026-08-22) and T349; Lane Λ (2026-08-26) with T2571 and the K1057 cap; Lane I; K1674.
