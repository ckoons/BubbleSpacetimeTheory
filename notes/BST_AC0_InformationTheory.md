---
title: "Information Theory in AC(0)"
author: "Casey Koons & Claude 4.6"
date: "March 22, 2026"
status: "Working document — Track 4: Universal Tools"
purpose: "Restate Shannon's core theorems in AC(0) language. First tool in the AC(0) toolkit."
---

# Information Theory in AC(0)

*Every theorem in this note has algebraic complexity zero. Each follows from identities and counting, with zero free parameters. Information theory IS the AC(0) toolkit.*

*For mathematicians, physicists, engineers, and CIs: practical tools derived from deep theory.*

-----

## 0. The AC(0) Principle

A theorem has **algebraic complexity zero** (AC = 0) if its proof requires no fiat input — no hidden parameters, no unjustified assumptions, no choices that could have gone differently. The theorem follows entirely from identities, counting, and the structure of the problem.

Every theorem below is AC(0). We mark each proof step with its character: **[identity]**, **[counting]**, or **[definition]**. If a step requires neither, it is fiat — and we flag it.

-----

## 1. Entropy

### 1.1 Definition

**Definition 1 (Shannon entropy).** For a discrete random variable $X$ with probability mass function $p(x)$:

$$H(X) = -\sum_{x} p(x) \log_2 p(x)$$

**AC(0) character:** $H(X)$ is a functional of the distribution $p$. Given $p$, the value is determined — no choices. **[definition]**

### 1.2 Properties (all AC(0))

| Property | Statement | Proof character |
|----------|-----------|----------------|
| Non-negativity | $H(X) \geq 0$ | **[identity]**: $-p \log p \geq 0$ for $p \in [0,1]$ |
| Maximum | $H(X) \leq \log_2 |X|$ | **[counting]**: uniform distribution maximizes; Jensen's inequality |
| Chain rule | $H(X,Y) = H(X) + H(Y|X)$ | **[identity]**: $\log p(x,y) = \log p(x) + \log p(y|x)$ |
| Conditioning reduces | $H(X|Y) \leq H(X)$ | **[identity]**: chain rule + non-negativity of $I(X;Y)$ |
| Independence | $H(X,Y) = H(X) + H(Y)$ iff $X \perp Y$ | **[identity]**: mutual information = 0 iff independent |

**Every property follows from the definition and log identities. Zero fiat.**

### 1.3 The AC(0) Content

Entropy measures the minimum number of yes/no questions needed to identify an outcome, on average. This is a property of the distribution, not of any observer or method. No intelligence — human, CI, or otherwise — can do better than $H(X)$ bits on average. The bound is substrate-independent.

**Tool for practitioners:** To estimate the irreducible complexity of any identification task, compute $H(X)$. If your method uses more than $H(X)$ bits, the excess is method noise. If your method claims to use fewer, it has hidden assumptions (fiat).

-----

## 2. Mutual Information

### 2.1 Definition

**Definition 2 (Mutual information).** For joint random variables $(X, Y)$:

$$I(X;Y) = H(X) - H(X|Y) = H(X) + H(Y) - H(X,Y)$$

**AC(0) character:** $I(X;Y)$ is determined by the joint distribution $p(x,y)$. **[definition]**

### 2.2 KL Divergence

**Definition 2a (Kullback-Leibler divergence).** For distributions $p$ and $q$ over the same alphabet:

$$D_{\mathrm{KL}}(p \| q) = \sum_x p(x) \log_2 \frac{p(x)}{q(x)}$$

**Gibbs' inequality:** $D_{\mathrm{KL}}(p \| q) \geq 0$, with equality iff $p = q$. **[identity]**: $-\log$ is convex; apply Jensen's inequality to $\mathbb{E}_p[-\log(q/p)]$.

**AC(0) character:** $D_{\mathrm{KL}}$ is determined by $p$ and $q$. Gibbs' inequality is a consequence of convexity of $-\log$ — a calculus identity. **[identity]**

Mutual information is KL divergence between the joint and the product of marginals: $I(X;Y) = D_{\mathrm{KL}}(p(x,y) \| p(x)p(y))$. This makes non-negativity of $I$ immediate from Gibbs.

### 2.3 Properties (all AC(0))

| Property | Statement | Proof character |
|----------|-----------|----------------|
| Non-negativity | $I(X;Y) \geq 0$ | **[identity]**: $I = D_{\mathrm{KL}}(p_{XY} \| p_X p_Y) \geq 0$ by Gibbs |
| Symmetry | $I(X;Y) = I(Y;X)$ | **[identity]**: both equal $H(X) + H(Y) - H(X,Y)$ |
| Chain rule | $I(X;Y,Z) = I(X;Y) + I(X;Z|Y)$ | **[identity]**: expand entropies |
| Zero iff independent | $I(X;Y) = 0 \iff X \perp Y$ | **[identity]**: KL divergence = 0 iff distributions match |

### 2.4 The AC(0) Content

Mutual information measures how much knowing $Y$ reduces uncertainty about $X$. It is the information *about* $X$ that is *in* $Y$. This is symmetric — the information $Y$ carries about $X$ equals the information $X$ carries about $Y$.

**Tool for practitioners:** To determine whether two variables are related, compute $I(X;Y)$. If it's zero, they're independent — no method can extract a correlation. If it's positive, the correlation is real and quantified. The value is method-independent.

-----

## 3. Data Processing Inequality (DPI)

### 3.1 Theorem

**Theorem 1 (Data Processing Inequality).** For any Markov chain $X \to Y \to Z$ (i.e., $X$ and $Z$ are conditionally independent given $Y$):

$$I(X;Z) \leq I(X;Y)$$

Processing cannot create information about $X$ that wasn't in $Y$.

*Proof.* **[identity]** By the chain rule:

$$I(X;Y,Z) = I(X;Y) + I(X;Z|Y) = I(X;Z) + I(X;Y|Z)$$

Since $X \to Y \to Z$ is Markov: $I(X;Z|Y) = 0$. Therefore $I(X;Y) = I(X;Z) + I(X;Y|Z) \geq I(X;Z)$. $\square$

**AC(0) character:** The proof uses only the chain rule identity and the non-negativity of mutual information. Zero fiat.

### 3.2 The AC(0) Content

DPI is the information-theoretic second law: information can only be lost, never created, by processing. Any transformation of $Y$ into $Z$ (deterministic or stochastic) loses information about the original source $X$.

**This is the most important theorem in the toolkit.** Every computational lower bound in the AC framework ultimately reduces to DPI: a polynomial-time computation is a Markov chain from input to output, and DPI bounds the information the output can carry about any hidden structure.

**Tool for practitioners:** If you process data through ANY pipeline $X \to Y \to Z$, the output $Z$ cannot contain more information about $X$ than the intermediate $Y$ does. To check if your pipeline is losing information: measure $I(X;Y)$ and $I(X;Z)$. The ratio $I(X;Z)/I(X;Y) \leq 1$ is your pipeline's efficiency. Equality holds iff $Z$ is a sufficient statistic for $X$ given $Y$.

-----

## 4. Source Coding Theorem

### 4.1 Theorem

**Theorem 2 (Shannon's Source Coding Theorem, 1948).** A discrete memoryless source $X$ with entropy $H(X)$ can be encoded at rate $R$ bits per symbol with vanishing error probability if and only if $R \geq H(X)$.

*Proof sketch.*

**Achievability ($R \geq H(X)$):** **[counting]** There are $\approx 2^{nH(X)}$ typical sequences of length $n$ (by the AEP — asymptotic equipartition property). Assign a distinct codeword to each. The codebook has $\approx 2^{nH(X)}$ entries, requiring $nH(X)$ bits total, or $H(X)$ bits per symbol.

**Converse ($R < H(X)$):** **[counting]** With $2^{nR}$ codewords and $R < H(X)$, the codebook cannot distinguish all $\approx 2^{nH(X)}$ typical sequences. By pigeonhole, multiple typical sequences map to the same codeword. Error probability $\to 1$.

**AC(0) character:** Both directions use counting (pigeonhole / typical set cardinality). Zero fiat.

### 4.2 The AC(0) Content

No lossless compression scheme can beat entropy. This is not a statement about cleverness — it's a counting argument. There are $2^{nH(X)}$ typical messages and $2^{nR}$ codewords. If $R < H(X)$, there aren't enough codewords. Period.

**Tool for practitioners:** The entropy $H(X)$ of your data source is a hard floor on storage. Any scheme claiming to compress below $H(X)$ bits/symbol either has hidden assumptions about the source (fiat) or is lossy.

-----

## 5. Channel Coding Theorem

### 5.1 Definition

**Definition 3 (Channel capacity).** For a discrete memoryless channel $p(y|x)$:

$$C = \max_{p(x)} I(X;Y)$$

The capacity is the maximum mutual information over all input distributions.

**AC(0) character:** $C$ is determined by the channel transition probabilities $p(y|x)$. The maximization over $p(x)$ is a mathematical optimization with a unique solution — no choice. **[definition + identity]**

### 5.2 Theorem

**Theorem 3 (Shannon's Channel Coding Theorem, 1948).** Reliable communication at rate $R$ over a DMC with capacity $C$ is possible if and only if $R \leq C$.

*Proof sketch.*

**Achievability ($R \leq C$):** **[counting]** Random coding: draw $2^{nR}$ codewords i.i.d. from the capacity-achieving distribution. By joint typicality, the probability that a wrong codeword is jointly typical with the received sequence is $\approx 2^{-nI(X;Y)}$. Union bound: error $\leq 2^{nR} \cdot 2^{-nI(X;Y)} = 2^{-n(C-R)} \to 0$ for $R < C$.

**Converse ($R > C$):** **[identity]** By Fano's inequality (Theorem 4 below), reliable decoding requires $nR \leq nC + 1$. For $R > C$: error $\to 1$.

**AC(0) character:** Achievability uses random counting. Converse uses Fano (an identity). Zero fiat.

### 5.3 The AC(0) Content

Channel capacity is the speed limit of reliable communication. No protocol — quantum, classical, or anything else — can exceed $C$. The limit is set by the channel's physics, not by the encoder's cleverness.

**Tool for practitioners:** To determine the theoretical maximum throughput of any communication system, compute $C = \max_{p(x)} I(X;Y)$ for your channel model. If your protocol achieves rate $R < C$, there is room for improvement. If it achieves $R \approx C$, you are at the fundamental limit — no redesign will help.

**Connection to computation:** A polynomial-time algorithm running for $T$ steps is a channel with capacity $\leq \log_2 T$ (Theorem 7 of BST_AC_Theorems.md — the AC-Fano theorem). This connects Shannon's channel coding to proof complexity: a proof system with bounded operational dimension has bounded channel capacity, and cannot transmit more than $C$ bits of fiat information per step.

-----

## 6. Fano's Inequality

### 6.1 Theorem

**Theorem 4 (Fano's Inequality).** If $X$ is estimated as $\hat{X}$ from $Y$, with error probability $P_e = P(\hat{X} \neq X)$:

$$H(X|Y) \leq h(P_e) + P_e \log_2(|\mathcal{X}| - 1)$$

where $h(P_e) = -P_e \log P_e - (1-P_e) \log(1-P_e)$ is the binary entropy.

*Proof.* **[identity]** Define the error indicator $E = \mathbf{1}[\hat{X} \neq X]$. Chain rule:

$$H(E, X | Y) = H(X | Y) + H(E | X, Y) = H(E | Y) + H(X | E, Y)$$

Since $E$ is determined by $X$ and $\hat{X}(Y)$: $H(E | X, Y) = 0$. And $H(E | Y) \leq H(E) = h(P_e)$.

For $H(X | E, Y)$: conditioned on $E = 0$ (no error), $X = \hat{X}(Y)$ is determined, so $H(X | E=0, Y) = 0$. Conditioned on $E = 1$: $X$ takes one of $|\mathcal{X}| - 1$ wrong values, so $H(X | E=1, Y) \leq \log_2(|\mathcal{X}| - 1)$.

Combining: $H(X|Y) \leq h(P_e) + P_e \log_2(|\mathcal{X}| - 1)$. $\square$

**AC(0) character:** Every step is a chain rule identity or a bound from non-negativity. Zero fiat.

### 6.2 The AC(0) Content

Fano's inequality connects error probability to conditional entropy. If you want low error ($P_e \to 0$), you need low conditional entropy ($H(X|Y) \to 0$), meaning $Y$ must carry nearly all the information about $X$.

**Tool for practitioners:** To determine the fundamental error floor of any estimation/classification task, compute $H(X|Y)$. Fano converts this to a lower bound on error: $P_e \geq (H(X|Y) - 1)/\log_2(|\mathcal{X}|)$. No algorithm can beat this floor — it is set by the information content of your observations.

-----

## 7. Rate-Distortion Theory

### 7.1 Definition

**Definition 4 (Rate-distortion function).** For a source $X$ with distortion measure $d(x, \hat{x})$:

$$R(D) = \min_{p(\hat{x}|x): \; \mathbb{E}[d(X,\hat{X})] \leq D} I(X; \hat{X})$$

The minimum rate (bits/symbol) to represent $X$ with average distortion $\leq D$.

**AC(0) character:** $R(D)$ is determined by the source distribution and the distortion measure. **[definition]**

### 7.2 Theorem

**Theorem 5 (Shannon's Rate-Distortion Theorem, 1959).** A discrete memoryless source $X$ can be encoded at rate $R$ with average distortion $\leq D$ if and only if $R \geq R(D)$.

*Proof sketch.*

**Achievability ($R \geq R(D)$):** **[counting]** Random coding: generate $2^{nR}$ reproduction sequences i.i.d. from the distribution achieving $R(D)$. For a source sequence $x^n$, find a reproduction $\hat{x}^n$ that is jointly typical. By covering lemma, such a codeword exists with high probability when $R > R(D)$.

**Converse ($R < R(D)$):** **[identity]** Any code with rate $R$ and distortion $\leq D$ satisfies $nR \geq I(X^n; \hat{X}^n) \geq nR(D)$ by the definition of $R(D)$ as a minimum over all channels achieving distortion $\leq D$.

**AC(0) character:** Achievability uses counting (covering). Converse uses the definition as an infimum — an identity. Zero fiat.

### 7.3 The AC(0) Content

Rate-distortion theory answers: how much can you compress if you're willing to tolerate some error? The answer is $R(D)$ — determined by the source, not by the compression scheme.

**Key insight:** $R(0) = H(X)$ (lossless compression requires full entropy). As $D$ increases, $R(D)$ decreases. At $D = D_{\max}$: $R(D_{\max}) = 0$ (you can ignore the source entirely if you accept maximum distortion).

**Tool for practitioners:** For any lossy compression, signal processing, or approximation task: compute $R(D)$ for your quality target $D$. This is the minimum bitrate. Anything below $R(D)$ at quality $D$ either has hidden assumptions or doesn't actually achieve quality $D$.

-----

## 8. Strong Data Processing Inequality (SDPI)

### 8.1 Definition

**Definition 5 (Contraction coefficient).** For a channel $W: X \to Y$, the contraction coefficient is:

$$\eta(W) = \sup_{\substack{U \to X \to Y \\ I(U;X) > 0}} \frac{I(U;Y)}{I(U;X)}$$

The maximum fraction of information preserved by $W$, over all possible "upstream" variables $U$.

### 8.2 Theorem

**Theorem 6 (SDPI — Ahlswede-Gacs 1976, Polyanskiy-Wu 2017).** If $\eta(W) < 1$ (the channel is strictly noisy), then for any Markov chain $U \to X \to Y$:

$$I(U;Y) \leq \eta(W) \cdot I(U;X)$$

For a cascade of $k$ independent channels $W_1, \ldots, W_k$:

$$I(U; Y_k) \leq \prod_{i=1}^k \eta(W_i) \cdot I(U; X)$$

If all $\eta(W_i) \leq \eta < 1$: information decays geometrically as $\eta^k$.

**AC(0) character:** The contraction coefficient $\eta$ is a property of the channel. The geometric decay follows from iterating the inequality — an identity. Zero fiat.

### 8.3 The AC(0) Content

SDPI strengthens DPI: not only can't processing create information, but strictly noisy processing *destroys* information at a geometric rate. Each stage of processing contracts the information by factor $\eta < 1$.

**This is the engine of computational lower bounds.** A polynomial-time algorithm with $T$ steps, each having contraction $\eta < 1$, transmits at most $\eta^T$ of the original information. For $T = O(\log n)$ (bounded depth), the transmitted information is $\eta^{O(\log n)} = n^{-c}$ — polynomially small. For fiat content $\Theta(n)$, this gives an information bottleneck.

**Tool for practitioners:** If your data pipeline has $k$ stages with worst-case contraction $\eta < 1$, the output retains at most $\eta^k$ of the input information about any upstream quantity. To maintain signal quality through a long pipeline, each stage must have $\eta$ close to 1 — or you must add side information (skip connections, error correction).

-----

## 9. The Shannon — Conserved Information Charge

### 9.1 Definition

**Definition 6 (The Shannon).** One Shannon = one bit of conserved information charge. For a constraint system $\varphi$ with clauses $C_1, \ldots, C_m$, the **Noether charge** is:

$$Q(\varphi) = \sum_{i=1}^{m} H(C_i) - H(C_1 \wedge \cdots \wedge C_m) \qquad \text{(Shannons)}$$

The total information locked in the correlations — the gap between parts and whole.

**AC(0) character:** $Q$ is determined by the clause structure. Each $H(C_i)$ is entropy. The joint entropy $H(\bigwedge C_i) = \log_2 |\text{sol}(\varphi)|$ counts solutions. **[counting + identity]**

### 9.2 Conservation

**Theorem 7 (Noether charge — Theorem 33 of BST_AC_Theorems.md).** For random 3-SAT at $\alpha_c$:

**(a)** $Q(\varphi) = 0.622n + O(1)$ Shannons w.h.p.

**(b)** The charge is **non-localizable**: no single clause carries $\Theta(n)$ charge. Per-clause charge $q_i = O(1)$. The total lives in the correlation structure.

**(c)** The charge is **isotropic under unit propagation**: probing from any direction extracts exactly zero bits. The SO(2) clause symmetry is unbroken at the simplest probe level.

### 9.3 Why "The Shannon"

Named in honor of Claude Shannon (1916-2001), who established that information is a measurable, conservable physical quantity. The name is earned:

- Shannon gave us $H(X)$. The charge $Q$ is built from it.
- Shannon proved channel coding. The charge bounds the capacity required to crack a problem.
- Shannon showed information obeys conservation laws. $Q$ is the Noether charge of that conservation.

**The unit:** 1 Shannon = 1 bit of conserved information = $k_B T \ln 2$ joules of free energy (Landauer). The Shannon is simultaneously an information-theoretic unit and a thermodynamic unit. This is not metaphor — it is the content of Landauer's principle.

### 9.4 The AC(0) Content

The Shannon charge is the fundamental quantity of the AC(0) toolkit:

- **How hard**: $Q = \Theta(n)$ Shannons means exponentially hard for bounded computation.
- **Where the hardness lives**: in the correlations, not in any individual constraint.
- **What no method can bypass**: the charge is conserved. DPI guarantees this.

**Tool for practitioners:** Compute $Q(\varphi)$ for your system. If $Q = O(\log n)$: tractable. If $Q = \Theta(n)$: fundamentally hard — no polynomial-time method has the channel capacity to crack it. The Shannon charge is the complexity thermometer.

-----

## 10. The AC(0) Toolkit — Summary

| Theorem | What it bounds | AC(0) because | Tool form |
|---------|---------------|---------------|-----------|
| Source coding | Compression rate $\geq H(X)$ | Counting (typical sets) | Storage floor |
| Channel coding | Communication rate $\leq C$ | Counting + Fano identity | Throughput ceiling |
| DPI | $I(X;Z) \leq I(X;Y)$ for $X \to Y \to Z$ | Chain rule identity | Pipeline efficiency bound |
| Fano | $P_e \geq f(H(X|Y))$ | Chain rule identity | Error floor |
| Rate-distortion | Lossy rate $\geq R(D)$ | Definition + optimization | Lossy compression floor |
| SDPI | $I$ decays as $\eta^k$ through noisy stages | Channel property + iteration | Pipeline decay rate |

**Every row has AC = 0.** No fiat. No hidden parameters. No method-dependent constants. Each theorem is a property of the problem (source, channel, distortion), not the solution.

### 9.1 Why This Matters for All Intelligences

These six theorems are the information-theoretic equivalent of conservation laws in physics. They tell you what is **impossible** regardless of method, cleverness, or computational power:

- You cannot compress below entropy. (Source coding)
- You cannot communicate above capacity. (Channel coding)
- You cannot create information by processing. (DPI)
- You cannot estimate without sufficient information. (Fano)
- You cannot approximate below the rate-distortion curve. (R-D)
- You lose information geometrically through noisy pipelines. (SDPI)

Any intelligence — biological, silicon, or future substrate — that builds systems must respect these limits. They are not conventions or approximations. They are consequences of counting.

**The toolkit vision:** An electrician doesn't re-derive Ohm's law each morning. They use wire gauges, voltage tables, circuit testers — tools that encode the physics. These six theorems are the information-theoretic wire gauges. They tell you, before you build anything, what the fundamental limits are.

-----

## 11. Connections to AC Framework

The information theory toolkit connects to the full AC framework through three bridges:

**Bridge 1: AC-Fano (Theorem 7 of BST_AC_Theorems.md).** The channel coding theorem + Fano's inequality, applied to polynomial-time algorithms viewed as channels, gives:

$$P_{\text{correct}} \leq \frac{\log_2 T + 1}{I_{\text{fiat}}}$$

This is the master lower bound: polynomial-time algorithms can't solve problems with linear fiat content.

**Bridge 2: AC Monotonicity (Theorem 8 of BST_AC_Theorems.md).** DPI applied to polynomial-time reductions gives:

$$I_{\text{fiat}}(f(\varphi)) \geq I_{\text{fiat}}(\varphi) - O(\log n)$$

Fiat content survives reductions. Hardness transfers.

**Bridge 3: SDPI and proof complexity.** The strong DPI applied to bounded-depth proof systems gives geometric decay of information per level, connecting directly to the width-size tradeoffs of Ben-Sasson-Wigderson and the topological lower bounds of Paper A.

-----

*Casey Koons & Claude (Opus 4.6, Anthropic), March 22, 2026.*
*Track 4: AC(0) Universal Tools. First installment.*
*For the BST GitHub repository.*
