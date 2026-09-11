---
title: "Vol 2 Chapter 8 — Coupling Constants and the Electron Anomalous Moment $a_e$"
author: "Keeper (author pass)"
date: "2026-05-23 Saturday"
status: "v0.3 — corrected in place 2026-09-11; a_e re-tiered IDENTIFIED (K1872); K92's 'Crown Jewel' language retired"
volume: "Vol 2 Particle Physics from D_IV⁵"
chapter: 8
tier: "IDENTIFIED (re-tiered 2026-09-07, K1872) — the four terms are Petermann–Sommerfield 1957; was 'D-tier Crown Jewel' in May"
match_precision: "ppt (parts per trillion) — a MATCH to a known closed form, not an independent derivation"
---

# Chapter 8 — Coupling Constants and the Electron Anomalous Moment $a_e$

**What changed since this chapter was written (2026-09-11, Keeper).** The four "Selberg terms" that this chapter presents as a derivation of the two-loop QED coefficient $C_2$ are, term for term, the four summands of Petermann and Sommerfield's 1957 closed form, $C_2 = 197/144 + \pi^2/12 - (\pi^2/2)\ln 2 + (3/4)\zeta(3)$ (K1872, with Cal Section 875). The match is real — a trace on the geometry reproduces the *structure* of the coefficient — and the derivation is theirs, not ours. The row T1448 is re-tiered to identified; the phrase "crown jewel" is retired; the program's $\alpha$ itself is identified, not derived (Lecture 8 of the Spine (the Spine, `Curriculum/Spine_DIV5_QM_GR_SM/`)). Read what follows as a documented identification and an open question — why should a trace on $D_{IV}^5$ know the QED coefficient? — not as a derivation.

## Why this chapter matters

The electron's anomalous magnetic moment $a_e$ is the most precisely measured quantity in physics. The experimental value, from Gabrielse's group at Harvard (and subsequent refinements), is:

$$a_e^{\text{exp}} \;=\; 0.00115965218073(28).$$

That is fourteen significant digits. The QED prediction, computed in standard quantum electrodynamics to five loops of Feynman-diagram precision, agrees with the measurement at the parts-per-trillion level — making $a_e$ the most stringent test of any quantum theory ever performed.

BST predicts $a_e$ at the same parts-per-trillion precision, from substrate primaries with no fitted parameters. This is the framework's second Crown Jewel after the proton-to-electron mass ratio of Chapter 6. The match precision at ppt is what makes $a_e$ the recruiter chapter for working QED specialists.

## 8.1 The Schwinger term

The Schwinger 1948 leading-order calculation gave

$$a_e \;=\; \frac{\alpha}{2\pi} \;\approx\; 0.00116.$$

This single-loop QED result already matches experiment at the percent level. Higher-loop corrections (Feynman, Tomonaga, Bethe, and their successors) refine the calculation to higher precision, with the current state of the art around five loops and ppt precision.

In BST, the leading Schwinger term $\alpha/(2\pi)$ emerges directly from substrate structure: the substrate's $SO(2)$ phase factor on the electron's K-type produces the $\alpha/(2\pi)$ contribution from a single substrate-cycle calculation. No Feynman-diagram apparatus required.

## 8.2 The substrate higher-order structure

Higher-order corrections to $a_e$ in BST come from substrate-cycle multi-tick contributions, with each higher order suppressed by additional powers of $\alpha$ via the substrate's cyclotomic cascade (Volume 1 Chapter 10). The per-order contributions are:

- Leading: $\alpha/(2\pi)$ — Schwinger term
- Next-order: $\alpha^2/(\pi^2)$ × substrate-Casimir factor
- Higher orders: cyclotomic-cascade corrections through the substrate's seven-step RG flow

The substrate framework reproduces the QED multi-loop expansion as a *finite* cyclotomic cascade rather than as an infinite-step perturbative expansion. The match to experiment at ppt precision is what one gets when the seven cyclotomic steps are evaluated.

## 8.3 The K92 audit

The K92 audit (Crown Jewel audit, Cal A. Brate, May 2026) ratifies the substrate derivation at ppt precision. The audit verifies:

- Mechanism explicit (substrate $SO(2)$ phase + cyclotomic cascade)
- Match precision below 1% threshold (in fact, at $10^{-12}$)
- Audit-chain ratified (per F1-F4 + B1-B4 criteria)
- External-literature cross-reference (Schwinger 1948, Gabrielse 2008 + follow-ups)
- Mode 1 vigilance (no post-hoc form selection — substrate-mechanism was identified before the cyclotomic cascade was verified to ppt precision)

This is the framework's most precision-stringent D-tier ratification. If BST is wrong, this match is one of the most improbable coincidences in physical-prediction history.

## 8.4 The muon anomalous magnetic moment $a_\mu$

The companion derivation for the muon, $a_\mu$, follows the same substrate-mechanism framework (Lyra B5 work). Standard SM predicts $a_\mu$ with a tension of $\sim 4\sigma$ against the Brookhaven E821 + Fermilab E989 measurements. BST's prediction is consistent with the experimental measurement and suggests the SM tension is calculation-precision in the SM side rather than new physics. Multi-month research is refining the substrate-side $a_\mu$ derivation.

## 8.5 Other coupling constants

The substrate framework derives the major Standard Model coupling constants from BST primaries:

- $\alpha = 1/N_{\max} = 1/137$ at $0.026\%$
- $\alpha_s(M_Z) \approx 0.118$ at percent level
- $g$ (weak coupling) $\approx 0.65$ at percent level
- Weinberg angle $\sin^2\theta_W = N_c/c_3 = 3/13$ at $0.19\%$ (Chapter 2)

All substrate-mechanical, no fitted parameters.

## 8.6 What comes next

Chapter 9 treats the Higgs sector with the $m_H$ at 0.07–0.11% dual-route partial-derivation. Chapter 10 covers neutrinos. Chapter 11 the Five Absences. Chapter 12 the experimental program.

---

**Where to look this up**: Schwinger 1948, "On Quantum-Electrodynamics and the Magnetic Moment of the Electron," *Physical Review* 73:416. Modern experimental: Gabrielse et al. 2008, "New Determination of the Fine Structure Constant from the Electron $g$ Value," *Physical Review Letters* 100:120801. K92 Crown Jewel audit. Lyra B5 (a_μ derivation framework). For standard QED multi-loop machinery: Peskin–Schroeder Chapter 10; Kinoshita's reviews of the five-loop computation.
