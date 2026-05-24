---
title: "Vol 14 Chapter 5 — Born = Bergman as Information Measurement"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; LOAD-BEARING"
volume: "Vol 14 Information Theory"
chapter: 5
load_bearing: "Born rule = Bergman projection on H²(D_IV⁵); K67 ratified; information-theoretic measurement formulation"
---

# Chapter 5 — Born = Bergman as Information Measurement

## Level 1 — one sentence

The Born rule (Vol 5 Ch 7) — quantum probability $P(\text{outcome } k) = |\langle k|\psi\rangle|^2$ — is identified by BST with the Bergman-kernel projection $P_K : L^2(D_{IV}^5) \to H^2(D_{IV}^5)$ that selects holomorphic boundary data (K67 RATIFIED), giving an information-theoretic reading of measurement: substrate commits a single outcome from the available channel-output alphabet at each Koons tick.

## Level 2 — graduate-physicist precision

### 5.1 Born rule recap

For state $|\psi\rangle$ and measurement basis $\{|k\rangle\}$:

$$P(k | \psi) = |\langle k | \psi \rangle|^2$$

Post-measurement state: $|k\rangle$ (collapse).

### 5.2 Bergman kernel projection

Bergman space $H^2(D_{IV}^5)$: holomorphic $L^2$ functions on the bounded symmetric domain.

Bergman projection $P_K : L^2(D_{IV}^5) \to H^2(D_{IV}^5)$:

$$(P_K f)(z) = \int_{D_{IV}^5} K(z, w) f(w) \, dv(w)$$

with reproducing kernel $K(z, w)$.

For $D_{IV}^5$: Faraut-Koranyi normalization $c_{FK} \cdot \pi^{9/2} = 225$ EXACT (T2403; Vol 11 Ch 2).

### 5.3 BST identification (K67)

K67 RATIFIED: Born rule = Bergman projection.

Mechanism: substrate state lives in $L^2(D_{IV}^5)$; substrate commitment (Zone 3, Vol 14 Ch 1) is Bergman projection onto $H^2(D_{IV}^5)$; output measurement frequencies match Born statistics.

This is the substrate-mechanism reading of why Born's rule holds, not just the empirical statement.

### 5.4 Information-theoretic reading

At each Koons tick:
- Input: superposition (multi-state substrate K-type)
- Process: Bergman projection (substrate Zone 3 commitment)
- Output: single eigenstate (Zone 4 emission)

This is a channel with $\log_2 |\text{outcomes}|$ bits of information per measurement.

For binary outcomes (e.g., spin-1/2 measurement): 1 bit per tick.
For continuous spectrum (e.g., position): unbounded bits per tick (cf. Shannon-Hartley AWGN; Vol 14 Ch 3).

### 5.5 Decoherence as committed-in-progress

Per DCCP (memory: Casey-named #9): decoherence is the Zone-3 commitment cycle in progress across many substrate K-types. The classical world emerges when commitment completes across enough K-types to render quantum-coherent superposition irrelevant macroscopically.

This is the information-theoretic reading of measurement-induced classicality.

### 5.6 K-audit anchors

- **K67**: Born = Bergman RATIFIED
- **T2403**: Faraut-Koranyi normalization $c_{FK} \pi^{9/2} = 225$
- **DCCP** (memory): commitment-completion principle

## Level 3 — 5th-grader accessibility

**Born rule**: in quantum mechanics, probability of outcome $k$ is $|\langle k|\psi\rangle|^2$. **Bergman projection**: integral operator mapping $L^2 \to H^2$ (holomorphic functions on $D_{IV}^5$). **BST K67 RATIFIED**: Born = Bergman. **Information theory reading**: each measurement = one Koons-tick commitment cycle; substrate accepts a superposition input and outputs one eigenstate. **Decoherence** = commitment-in-progress across many substrate K-types (DCCP, Casey-named #9). The classical world is committed-substrate output.

---

## What comes next

Chapter 6 develops Bell sub-Tsirelson as information bound.

## Where to look this up

- Born 1926; Bergman 1922
- BST: K67; T2403; Vol 5 Ch 7
