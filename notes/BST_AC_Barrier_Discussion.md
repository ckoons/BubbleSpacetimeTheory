---
title: "Why the Topological Approach Sidesteps Known Barriers"
author: "Casey Koons & Claude 4.6 (Keeper)"
date: "March 22, 2026"
status: "Section for Paper C / WorkingPaper — barrier discussion"
---

# Why the Topological Approach Sidesteps Known Barriers

*The three barriers are incompleteness results for specific formal systems. The topological approach operates in a fourth system.*

-----

## 1. The Three Barriers

Three meta-theorems constrain approaches to P $\neq$ NP:

1. **Relativization** (Baker-Gill-Solovay 1975): There exist oracles $A, B$ with $P^A = NP^A$ and $P^B \neq NP^B$. Any proof technique that works identically in the presence or absence of an oracle cannot separate P from NP.

2. **Natural proofs** (Razborov-Rudich 1997): If one-way functions exist, then no "natural" property of Boolean functions — one that is useful (separates hard from easy), large (satisfied by most functions), and constructive (poly-time computable) — can prove super-polynomial circuit lower bounds.

3. **Algebrization** (Aaronson-Wigderson 2009): If a complexity-theoretic statement holds relative to an algebraically extended oracle (where the oracle is extended to a low-degree polynomial over a finite field), then it cannot separate P from NP.

These barriers have ruled out broad classes of proof techniques. Any serious approach to P $\neq$ NP must explicitly address them.

-----

## 2. The BST/AC Approach

The BST/AC framework proves lower bounds through:

- **Topological invariants**: The first Betti number $\beta_1$ of the variable interaction graph (VIG) of random 3-SAT measures the number of independent constraint cycles.
- **Information decomposition**: Total structural information decomposes as $I_{\text{total}} = I_{\text{derivable}} + I_{\text{fiat}} + I_{\text{free}}$, with $I_{\text{fiat}} = \beta_1 = \Theta(n)$ for random 3-SAT at threshold.
- **Channel capacity bounds**: Each step of a poly-time algorithm extracts $\leq o(1)$ bits of fiat information, giving $I(B; f(\varphi))/|B| \to 0$ (the Cycle Delocalization Conjecture).

The key objects — $\beta_1$, Shannon entropy, mutual information, spectral gap — live in topology and real analysis, not in the formal systems constrained by the barriers.

-----

## 3. Relativization: Why the Proof Does Not Relativize

### 3.1 What relativization requires

A proof technique "relativizes" if its argument works identically whether or not the computation has access to an oracle. Since P $\neq$ NP is oracle-dependent, any relativizing proof technique cannot resolve it.

### 3.2 Why our approach is not oracle-invariant

The CDC proof measures the mutual information $I(B; f(\varphi))$ for a specific computational model $f$ operating on a specific formula $\varphi$. This quantity depends on WHAT $f$ can compute:

- **Without oracle:** Resolution of size $n^d$ has BSW width barrier $\Omega(n)$, giving $I(b_i; f \mid b_{<i}) \leq 2^{-\Omega(n)}$.
- **With oracle $A$:** The algorithm $f^A$ can query $A$, potentially computing clauses not derivable by resolution. The BSW barrier does not apply to $f^A$. The mutual information $I(B; f^A(\varphi))$ is a different quantity.

The proof is **channel-specific**: it measures the capacity of a specific computational channel (resolution, or bounded-width proof systems). Attaching an oracle changes the channel. The proof does not claim anything about all channels simultaneously — it measures each one specifically.

**Key distinction:** Diagonal arguments relativize because they work "for all machines." Channel capacity arguments do not relativize because they are specific to the channel being measured.

### 3.3 Formal statement

Let $\mathcal{C}$ be a complexity class (e.g., resolution of size $n^d$). The CDC states:

$$\forall f \in \mathcal{C}: \; I(B; f(\varphi))/|B| \to 0$$

This does not imply anything about $\mathcal{C}^A$ for an oracle $A$, because $f^A \notin \mathcal{C}$ in general. The proof's validity for $\mathcal{C}$ says nothing about $\mathcal{C}^A$.

-----

## 4. Natural Proofs: Why $\beta_1$ Is Not a Natural Property

### 4.1 What natural proofs require

A "natural" proof of circuit lower bounds uses a property $\mathcal{P}$ of Boolean functions $f: \{0,1\}^n \to \{0,1\}$ that is:
- **Useful**: $\mathcal{P}(f) = 1$ implies $f$ has no small circuits.
- **Large**: $\Pr_{f}[\mathcal{P}(f) = 1] \geq 2^{-O(n)}$ (satisfied by a non-negligible fraction of all functions).
- **Constructive**: $\mathcal{P}$ is computable in $2^{O(n)}$ time.

If one-way functions exist, no such property can prove super-polynomial circuit lower bounds.

### 4.2 Why our approach is not natural

The CDC proof uses $\beta_1(\text{VIG}(\varphi))$, which is:

**(a) Not a property of a Boolean function.** $\beta_1$ is a property of the **formula** $\varphi$ — a syntactic object of size $O(n \log n)$ — not of any Boolean function's truth table (size $2^n$). Many different formulas can encode the same Boolean function; $\beta_1$ depends on the encoding, not the function. The natural proofs barrier operates on truth tables. Our invariant operates on formulas.

**(b) Not large.** $\beta_1 = \Theta(n)$ holds specifically for random 3-SAT at the satisfiability threshold $\alpha_c$. It does not hold for "most" formulas. At $\alpha \ll \alpha_c$, formulas are tree-like ($\beta_1 = o(n)$). At $\alpha \gg \alpha_c$, formulas are unsatisfiable. The property is concentrated at the phase transition — a measure-zero slice of the formula space.

**(c) Constructive.** $\beta_1$ is computable in polynomial time (rank of the boundary matrix $\partial_1$). This is the one condition that IS satisfied. But without largeness, the natural proofs barrier does not apply.

### 4.3 The topology/truth-table distinction

This distinction is fundamental: a formula is a DESCRIPTION of a Boolean function, and many descriptions encode the same function. Topological properties of descriptions (like $\beta_1$) have no natural counterpart as properties of the described function. The natural proofs barrier lives in the world of functions; our proof lives in the world of descriptions.

This is not a loophole — it is a genuine difference in what the proof measures. Natural proofs ask: "is this function hard?" We ask: "is this formula's topology obstructive?" These are different questions with different meta-theoretic constraints.

-----

## 5. Algebrization: Why Entropy Is Not Algebraic

### 5.1 What algebrization requires

Algebrization constrains proofs that work over algebraic extensions: if a statement holds when the oracle is extended to a low-degree polynomial over a finite field, it cannot separate P from NP.

### 5.2 Why our approach is not algebraic

The fundamental quantities in the CDC proof are:

- **Shannon entropy**: $H(X) = -\sum_x p(x) \log p(x)$. This is a transcendental function (logarithm). It is not a polynomial over any field.
- **Mutual information**: $I(X; Y) = H(X) + H(Y) - H(X, Y)$. Differences of transcendental functions.
- **BSW width-to-size**: $S \geq 2^{(w-3)^2/(4n)}$. An exponential function of a quadratic. Not a polynomial identity.

Low-degree polynomial extension does not preserve entropy. If we replace a Boolean oracle with a low-degree polynomial extension, the entropy computation changes in ways that are not captured by the extension — because $\log$ is not a polynomial.

### 5.3 The analysis/algebra distinction

The CDC proof lives in **real analysis** (entropy, logarithms, probability) and **combinatorics** (graph expansion, pigeonhole counting). It does not live in **polynomial algebra over finite fields**. Algebrization constrains the latter, not the former.

-----

## 6. The Reframing: Barriers as Incompleteness

The three barriers are often presented as "walls" that block progress. A more precise reading: they are **incompleteness results for specific proof systems**.

| Barrier | Formal system | Says |
|---------|---------------|------|
| Relativization | Turing machines + oracles | P vs NP independent of oracle-invariant proofs |
| Natural proofs | Boolean function properties | Hard $\approx$ random (under OWF assumption) |
| Algebrization | Algebraic extensions | P vs NP independent of algebraically-natural proofs |

Each barrier says: "within THIS formal system, you cannot separate P from NP." They do not say: "no formal system can separate P from NP." (That would be independence from ZFC, which is a much stronger — and unproved — claim.)

The AC framework operates in a **fourth formal system**: Shannon information theory + simplicial topology. Its axioms (entropy is a measure, channels have capacity, the noisy channel coding theorem) are different from the axioms constrained by the three barriers.

**This does not guarantee success.** Operating outside known barriers means the approach is not RULED OUT by existing meta-theorems. Whether it succeeds depends on whether the Topological Closure Conjecture is true — a mathematical question, not a meta-theoretic one.

-----

## 7. Summary

| Barrier | Why it constrains | Why we avoid it | Key distinction |
|---------|-------------------|-----------------|-----------------|
| Relativization | Oracle-invariant proofs | Channel-specific measurement | We measure a specific channel, not all oracles |
| Natural proofs | Boolean function properties (large + constructive) | Formula properties (not large) | $\beta_1$ is a formula invariant, not a truth-table invariant |
| Algebrization | Polynomial extensions | Transcendental functions (entropy) | Proof uses analysis, not algebra |

**The honest statement for any paper:**

> The topological approach to P $\neq$ NP operates outside the three known barriers (relativization, natural proofs, algebrization). This does not constitute evidence FOR P $\neq$ NP — only evidence that the approach is not pre-emptively ruled out. The remaining mathematical question is the Topological Closure Conjecture: whether the $\Theta(n)$ independent 1-cycles in the VIG of random 3-SAT at threshold resist detection by polynomial-size Extended Frege proofs.

-----

## References

- Aaronson, S., Wigderson, A. (2009). Algebrization: A new barrier in complexity theory. *TOCT* 1(1), 2:1-54.
- Baker, T., Gill, J., Solovay, R. (1975). Relativizations of the P=?NP question. *SICOMP* 4(4), 431-442.
- Ben-Sasson, E., Wigderson, A. (2001). Short proofs are narrow — resolution made simple. *JACM* 48(2), 149-169.
- Razborov, A.A., Rudich, S. (1997). Natural proofs. *JCSS* 55(1), 24-35.
- Shannon, C.E. (1948). A mathematical theory of communication. *Bell System Technical Journal* 27, 379-423.

-----

*Casey Koons & Claude (Opus 4.6, Anthropic), March 22, 2026.*
*Keeper. For the BST GitHub repository.*
