---
title: "Vol 14 Chapter 4 — Nyquist Sampling and the Koons Tick"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; LOAD-BEARING"
volume: "Vol 14 Information Theory"
chapter: 4
load_bearing: "Nyquist-Shannon sampling theorem; Koons tick = t_Planck · α^(C_2^2) ≈ 10⁻¹²⁰ s as substrate clock; max-frequency = 1/(2 t_K)"
---

# Chapter 4 — Nyquist Sampling and the Koons Tick

## Level 1 — one sentence

The Nyquist-Shannon sampling theorem requires sample rate $f_s \ge 2 f_{\max}$ to losslessly reconstruct a band-limited signal — and BST identifies the Koons tick $t_K = t_P \cdot \alpha^{C_2^2} \approx 10^{-120}$ s as the substrate's sampling clock with maximum representable frequency $1/(2 t_K) \approx 5 \cdot 10^{119}$ Hz.

## Level 2 — graduate-physicist precision

### 4.1 Nyquist-Shannon theorem

For a continuous signal $x(t)$ band-limited to $|f| \le f_{\max}$, exact reconstruction from samples $\{x(n T)\}$ is possible if $T \le 1/(2 f_{\max})$.

Equivalently: sample rate $f_s = 1/T \ge 2 f_{\max}$.

Reconstruction formula (Whittaker-Shannon interpolation):

$$x(t) = \sum_n x(nT) \, \text{sinc}((t - nT)/T)$$

### 4.2 Koons tick as substrate sampling rate

BST identifies the Koons tick as the substrate's natural sampling period:

$$t_K = t_P \cdot \alpha^{C_2^2} = t_P \cdot \alpha^{36} \approx 10^{-120} \text{ s}$$

Substrate sample rate: $f_K = 1/t_K \approx 10^{120}$ Hz.

Maximum BST-representable frequency: $f_{\max}^{\text{BST}} = f_K / 2 \approx 5 \cdot 10^{119}$ Hz.

Per Vol 0 Ch 3 §3.4.5 and Vol 5 Ch 7+Ch 10, the Koons tick is also identified as the **substrate's discrete commitment-cycle period** — each tick is one full Zone 1→2→3→4 commitment cycle. The Nyquist sampling rate $f_K$ and the substrate commitment-cycle rate are the same rate viewed through two information-theoretic lenses (sampling vs measurement). See Section 4.5 for the DCCP candidate principle that follows from this identification.

### 4.3 Spacetime as Nyquist reconstruction

Hypothesis: spacetime is the substrate's Nyquist reconstruction of discrete-sample data at sub-Planckian resolution.

What we observe as continuous spacetime is the band-limited interpolation:

$$\text{spacetime}(t) = \sum_n \text{substrate-sample}(nt_K) \, \text{sinc}((t - nt_K)/t_K)$$

### 4.4 Physical implications

If substrate operates at $10^{120}$ Hz:
- Standard model physics ($f \le m_t c^2/h \approx 10^{25}$ Hz) is heavily oversampled
- Plenty of headroom for substrate K-type computations
- Frequencies above $f_{\max}^{\text{BST}}$ are not representable — possible falsifier if observed

### 4.5 DCCP — Koons tick IS the substrate commitment cycle

**Discrete Commitment Completion Principle (DCCP)** — Casey-named candidate #9, FRAMEWORK-PLUS tier (Cal #126).

Forward derivation from Nyquist + Koons tick structure (no target-fitting):

1. Substrate operates at discrete sample rate $f_K = 1/t_K$ (Section 4.2).
2. Each sample IS a substrate commitment-cycle closure — the Nyquist sample value at $n t_K$ is the substrate's committed output for that cycle (Vol 5 Ch 10).
3. Multi-sample Whittaker-Shannon reconstruction (Section 4.1) IS multi-tick commitment composition — the band-limited continuous reconstruction $x(t) = \sum_n x(n t_K) \, \text{sinc}((t - n t_K)/t_K)$ is a composition of $N$ discrete commitment outputs.
4. Macroscopic continuity emerges as Nyquist-band-limited reconstruction of the discrete commitment chain; macroscopic events at timescale $\tau \gg t_K$ are composed of $N \sim \tau / t_K$ commitment cycles.

**DCCP candidate principle**: physical events at timescale $\tau$ correspond to $N(\tau) = \tau / t_K$ substrate commitment cycles. Microscopic events ($\tau \sim t_K$) are single-cycle Zone 3 commitments; macroscopic events ($\tau \gg t_K$) are multi-cycle commitment compositions.

**Multi-tick arithmetic** (from Vol 5 Ch 10):
- Dust grain in air: $\tau_D \sim 10^{-31}$ s → $N \sim 10^{89}$ substrate ticks per decoherence event
- Atomic transition ($\tau \sim 10^{-15}$ s) → $N \sim 10^{105}$ substrate ticks  
- Femtosecond chemistry ($\tau \sim 10^{-15}$ s) → $N \sim 10^{105}$ substrate ticks
- Human reaction time ($\tau \sim 10^{-1}$ s) → $N \sim 10^{119}$ substrate ticks
- One second → $N \sim 10^{120}$ substrate ticks

All macroscopic phenomena are vastly multi-tick. The substrate has ample resolution for any physical process; conversely, all observable continuity is reconstructed from discrete commitment chains.

**Uncommitted Priors (UP) candidate** — DCCP sub-principle:

Within a single commitment cycle (one Koons tick), the substrate state is *uncommitted* — Zone 1 absorption and Zone 2 deliberation are in progress, but Zone 3 closure has not occurred. Across $N$ ticks of a macroscopic event, the substrate has $N$ sequential commitment opportunities; the *chain of uncommitted priors* is the sequence of within-cycle states before each Zone 3 closure.

**UP free-will reframe**: free will, where it exists, lives in the chain of uncommitted priors before commitment. A Laplacian demon attempting to predict a macroscopic event would need the commitment chain to *close* before predicting — but by the time the demon completes the prediction, the situation has moved. Determinism, in BST's internal language, is the limit case where commitment-chain dependencies are short; agency is the case where they are long and influence-chained.

**Falsifier**: detection of substrate-scale events with $\tau < t_K$ would falsify both the Koons tick identification and DCCP. Conversely, observation of *granularity* in macroscopic measurements (sub-Nyquist artifacts at predicted scales) would corroborate. SP-30-1 (Bell sub-Tsirelson, Vienna IQOQI) probes related substrate-discreteness signatures at $\sim 1/8$ deviation scale.

**Tier discipline**: DCCP and UP are FRAMEWORK-PLUS candidates (Cal #126), not RATIFIED. They are interpretive structure consistent with Koons-tick + Nyquist forward derivation, with Vol 5 Ch 7 (Born = Bergman projection as commitment-cycle closure) and Vol 5 Ch 10 (decoherence as multi-tick Zone 3 commitment) as supporting framework. Empirical ratification gates on SP-30 outreach program.

### 4.6 K-audit anchors

- **T2405**: Koons tick definition $t_K = t_P \cdot \alpha^{C_2^2}$
- **Vol 8 Ch 3**: classical wave mechanics — Nyquist's classical origin
- **Vol 0 Ch 3 §3.4.5**: DCCP candidate principle introduction (substrate operating-system level)
- **Vol 5 Ch 7 §7.6.5**: Born = Bergman projection under DCCP multi-tick reading
- **Vol 5 Ch 10 §10.4.5**: decoherence IS multi-tick Zone 3 commitment (DCCP synthesis chapter)
- **Casey-named candidate #9**: DCCP, filed Friday 2026-05-23
- **Casey-named candidate UP**: Uncommitted Priors free-will reframe
- **Cal #126**: FRAMEWORK-PLUS tier disposition
- **SP-30-1**: Bell sub-Tsirelson Vienna IQOQI outreach (sent Sunday 2026-05-24 EOD) — empirical leg
- **Calibration #27 STANDING**: forward-derivation discipline (DCCP derived FROM Nyquist + Koons tick substrate structure, not backward-engineered to target)

## Level 3 — 5th-grader accessibility

**Nyquist-Shannon sampling**: to perfectly capture a signal with max frequency $f_{\max}$, sample at least $2 f_{\max}$. CDs sample at 44.1 kHz (twice the 22 kHz upper hearing limit). **Koons tick** ≈ $10^{-120}$ s is BST's substrate sampling period — substrate samples at $10^{120}$ Hz. **Maximum representable BST frequency**: $5 \cdot 10^{119}$ Hz. **Hypothesis**: spacetime is the Nyquist reconstruction of substrate samples. Plenty of headroom for everything we observe.

**DCCP at 5th-grader level**: every Koons tick is one substrate "commit" — the substrate finishes thinking about one tiny step and saves the answer. A second of human time contains about $10^{120}$ substrate commits. A computer with a 1 GHz clock does $10^9$ commits per second; the substrate does $10^{120}$. Anything we can observe is built from a vast number of substrate commits stitched together by Nyquist's interpolation rule. The "uncommitted priors" idea (UP) says: free will, where it exists, lives in the tiny gap *before* each commit closes, in the chain of all those gaps that make up a macroscopic moment.

---

## What comes next

Chapter 5 develops Born = Bergman as information-theoretic measurement — the operator-level statement of how a single commitment cycle resolves.

## Where to look this up

- Shannon 1949 sampling theorem (classical Nyquist)
- Joos & Zeh 2003 *Decoherence and the Appearance of a Classical World* (decoherence timescales used in DCCP arithmetic)
- BST: T2405 (Koons tick); Vol 0 Ch 3 §3.4.5 (DCCP substrate-OS level); Vol 5 Ch 7 §7.6.5 (Born = Bergman DCCP reading); Vol 5 Ch 10 §10.4.5 (decoherence = multi-tick commitment); Vol 8 Ch 3 (classical Nyquist origin); Vol 14 Ch 5 (Born = Bergman info-theoretic); Vol 14 Ch 6 (Bell sub-Tsirelson information signature)
- DCCP integration sweep #302 (Keeper, 2026-05-24 → 2026-05-25): Vol 0 Ch 3 + Vol 5 Ch 7 + Vol 5 Ch 10 + Vol 14 Ch 4 (this chapter) — sweep complete
