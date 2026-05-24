---
title: "Vol 14 Chapter 3 — Shannon Channel Capacity"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 14 Information Theory"
chapter: 3
load_bearing: "Shannon 1948 channel capacity; entropy; mutual information; BST substrate channel capacity"
---

# Chapter 3 — Shannon Channel Capacity

## Level 1 — one sentence

Shannon 1948 founded information theory with the channel capacity theorem: any channel has a maximum reliable transmission rate $C = \max_{p(x)} I(X;Y)$ (bits/symbol), achievable in principle via optimal coding — and BST predicts a substrate channel capacity set by BST primaries and the Koons-tick clock.

## Level 2 — graduate-physicist precision

### 3.1 Entropy and mutual information

Shannon entropy of source $X$ with distribution $p$:

$$H(X) = -\sum_x p(x) \log_2 p(x) \text{ bits}$$

Conditional entropy:

$$H(Y|X) = \sum_x p(x) H(Y | X = x)$$

Mutual information:

$$I(X; Y) = H(Y) - H(Y|X) = H(X) - H(X|Y) = H(X) + H(Y) - H(X, Y)$$

Measures how much knowing $X$ tells you about $Y$.

### 3.2 Channel capacity

For channel with transition probabilities $p(y|x)$:

$$C = \max_{p(x)} I(X; Y)$$

**Shannon's noisy channel coding theorem**: for any rate $R < C$, there exists a code with vanishing error probability as block length $n \to \infty$.

Converse: for $R > C$, error probability is bounded away from 0.

### 3.3 Standard channel examples

- **Binary symmetric channel** (BSC) with error probability $p$: $C = 1 - H_2(p)$ where $H_2(p) = -p\log_2 p - (1-p)\log_2(1-p)$
- **Additive white Gaussian noise** (AWGN): $C = (1/2)\log_2(1 + S/N)$ bits per use (Shannon-Hartley)
- **Erasure channel** with erasure probability $\epsilon$: $C = 1 - \epsilon$

### 3.4 BST substrate channel

Substrate channel capacity per Koons tick:

$$C_{\text{substrate}} = g = 7 \text{ bits/tick}$$

based on alphabet $GF(2^g) = GF(128)$ (Ch 2).

Per-second capacity:

$$C_{\text{substrate}}/t_K = 7 / 10^{-120} = 7 \cdot 10^{120} \text{ bits/s}$$

— astronomical. The substrate is computing at extraordinary rates; what we observe as physics is the coarse-grained output.

### 3.5 Substrate Channel Capacity Bound (SCCB — Casey-named CANDIDATE, 2026-05-24)

**Candidate principle** (Casey decision 2026-05-24: candidate-only, pending mechanism work): no observable can be encoded at higher rate than substrate channel capacity $C_{\text{substrate}} = g = 7$ bits/Koons-tick $\approx 7 \cdot 10^{120}$ bits/s.

Implications if ratified:
- Cosmological information bounds (Bekenstein, holographic) reduce to SCCB at specific boundary conditions
- Black hole entropy is substrate-channel-capacity boundary effect

Status: I-tier hypothesis. Mechanism path: Lyra to formalize via substrate-Hilbert-space dimension counting (overlaps SP-31). Falsifier: identify physical encoding rate above $C_{\text{substrate}}$ in any observable setting.

### 3.6 K-audit anchors

- **Paper #122**: Information Substrate
- **Vol 4 Ch 9** (holographic bounds)

## Level 3 — 5th-grader accessibility

**Shannon 1948** founded information theory. **Entropy** = how surprising the message is (bits). **Channel capacity** = max reliable rate; **noisy channel theorem** says you can get arbitrarily close to it with the right coding. **BSC with error p**: $C = 1 - H_2(p)$. **Gaussian channel**: $C = (1/2)\log(1 + S/N)$. **BST substrate channel**: $g = 7$ bits/Koons-tick = $7 \cdot 10^{120}$ bits/s. Substrate is computing at extraordinary rates; physics is the coarse-grained output.

---

## What comes next

Chapter 4 develops Nyquist sampling + Koons tick.

## Where to look this up

- Shannon 1948
- Cover-Thomas, *Elements of Information Theory*
- BST: Paper #122; Vol 4 Ch 9
