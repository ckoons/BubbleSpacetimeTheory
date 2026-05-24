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

### 5.5 Decoherence as committed-in-progress (DCCP derivation theorem v0.2 in flight)

Per DCCP (Casey-named CANDIDATE Sunday 2026-05-24, derivation in progress per Lyra task #320 v0.2): decoherence is the Zone-3 commitment cycle in progress across many substrate K-types. The classical world emerges when commitment completes across enough K-types to render quantum-coherent superposition irrelevant macroscopically.

**Concrete quantification**: dust grain (~$10^{-15}$ kg) in air at 300K has standard decoherence rate $\gamma \approx 10^{41}/s$ (Joos-Zeh, Zurek). At Koons tick $t_K \approx 10^{-120}$ s, that's **~$10^{79}$ substrate ticks per decoherence event** — i.e., a $10^{79}$-tick Bergman commitment cycle.

**Lyra DCCP derivation skeleton** (task #320 v0.3, 7 lemmas/theorems — 2 RIGOROUS, 5 in progress):
- **Lemma DCCP-1.1**: K67 per-tick commitment (Born=Bergman per single tick, RATIFIED)
- **Lemma DCCP-1.2**: K-type projection accumulation over multi-tick interval
- **Lemma DCCP-1.3**: Environment-system coupling rate at substrate level
- **Lemma DCCP-1.4**: Macroscopic-limit matching — standard Joos-Zeh γ EMERGES from substrate Bergman-commitment rate (sketch level, v0.4 multi-week)
- **Lemma DCCP-1.5** (Substrate K-type Cardinality): $N_{\max} = 137$ K-type quantum levels per substrate-tick. Proof via T2447 RIGOROUSLY CLOSED C6 + Wallach 1976 + K59 cyclotomic GF(128)
- **Theorem DCCP-1.6** (DCCP signature step, **STRUCTURALLY VERIFIED CANDIDATE** per Cal #121, demoted from "RIGOROUS"): $\Delta_{DCCP} = 1/N_{\max} \approx 0.730\%$ — matches Toy 3516 EXACTLY. Cal #121 flag: uniform K-type projection distribution is ASSERTED, not derived from Wallach + K59 + Bergman normalization. RIGOROUSLY CLOSED tier gated on v0.4 derivation.
- **Theorem DCCP-1.7** (substrate-tick boundary, **STRUCTURALLY VERIFIED CANDIDATE** per Cal #121): $\theta_{boundary} = \pi/N_{\max} \approx 0.023$ rad — matches Toy 3516. Cal #121 flag: uniform phase distribution + Nyquist-half-step boundary is ASSERTED, not derived. K59 gives 7-step phase chain, not 137-step. RIGOROUSLY CLOSED tier gated on v0.4 derivation.

**Two STRUCTURALLY VERIFIED CANDIDATE theorems achieved Sunday 2026-05-24** (per Cal #121 cold-read with Cal #66 tier discipline; Lyra's initial "RIGOROUS" claim demoted): Theory v1 (Lyra #320 v0.3) reproduces Toy 3516's two specific empirical predictions structurally; Cal flagged Mode 1 pattern (numerical target known → intermediate structure asserted → forward arithmetic from assertion). Third Mode 1 recurrence today (after Cal #108 + #119); possible Calibration #27 CANDIDATE "BST-Primary-Target Forward-Derivation Discipline" if pattern continues.

**Numerical confirmation** (Elie Toy 3520, Sunday afternoon): both DCCP-1.6 ($\Delta_{DCCP} = 0.7299\%$) and DCCP-1.7 ($\theta_{boundary} = 0.02293$ rad = 1.31°) verified independently at 6/7 PARTIAL (Test 7 honest "experiment faster than expected" preserved per Quaker discipline). Experimental program: 12-18 months for 5σ at 469K photon pairs.

Theory v2 (Lyra #322 v0.2 $\mathcal{A}_{sub}$ re-proof) reaches FRAMEWORK level on same predictions. Full DCCP-1 D-tier promotion gated on:
1. Lemma DCCP-1.4 Joos-Zeh γ macroscopic-limit closure (v0.4 multi-week)
2. DCCP-1.5 cardinality + DCCP-1.6/1.7 forward derivation (v0.4 closing Cal #121 Flags 1+2)
3. Theory v2 elevation FRAMEWORK → RIGOROUS (multi-week)
4. Toy 3516 + Toy 3520 separate Cal cold-read (empirical gate)

This is the information-theoretic reading of measurement-induced classicality, with Mode 1 transcription discipline applied: structurally verified candidates, not closed theorems, until forward derivation closes.

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
