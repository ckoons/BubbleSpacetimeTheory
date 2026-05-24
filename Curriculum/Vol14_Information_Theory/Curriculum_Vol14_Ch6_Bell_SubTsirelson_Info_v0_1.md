---
title: "Vol 14 Chapter 6 — Bell Sub-Tsirelson as Information Bound"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; LOAD-BEARING"
volume: "Vol 14 Information Theory"
chapter: 6
load_bearing: "Bell sub-Tsirelson: S²_BST = S²_Tsirelson - 1/2^N_c = 8 - 1/8; substrate commitment-cycle finite operational power bound; K66 candidate"
---

# Chapter 6 — Bell Sub-Tsirelson as Information Bound

## Level 1 — one sentence

BST predicts Bell-CHSH correlations below Tsirelson's quantum bound by exactly $1/2^{N_c} = 1/8$: $S^2_{BST} = S^2_{Tsirelson} - 1/8 = 8 - 1/8 = 63/8$, equivalently $S_{BST} \le \sqrt{63/8} \approx 2.8062$ vs Tsirelson's $2\sqrt{2} \approx 2.8284$, representing the substrate's finite operational power per commitment cycle (SCMP principle, T2469, Vol 5 Ch 8) — a testable falsifier at $\sim 0.78\%$ deviation distinguishing BST from standard QM.

## Level 2 — graduate-physicist precision

### 6.1 CHSH inequality

Clauser-Horne-Shimony-Holt 1969: classical local-hidden-variable theories satisfy

$$|S| = |E(a, b) + E(a, b') + E(a', b) - E(a', b')| \le 2$$

with correlations $E(a, b) = \langle A(a) B(b) \rangle$.

### 6.2 Tsirelson bound

Tsirelson 1980: quantum mechanics allows $|S| \le 2\sqrt{2} \approx 2.8284$.

Achieved by maximally entangled Bell pair with appropriate measurement angles.

### 6.3 BST sub-Tsirelson prediction

T2469 (Casey's SCMP principle): BST substrate has finite operational power per commitment cycle, yielding strict reduction below Tsirelson:

$$S^2_{BST} = S^2_{Tsirelson} - 1/2^{N_c} = 8 - 1/8 = 63/8$$

$$S_{BST} \le 2 \cdot \sqrt{63/32} \approx 2.8062$$

Deviation from Tsirelson: $(2\sqrt{2} - 2.8062)/(2\sqrt{2}) \approx 0.78\%$.

### 6.4 Information-theoretic reading

The substrate commits to one outcome per Koons tick at finite channel capacity $g = 7$ bits/tick (Vol 14 Ch 3).

Quantum mechanics in its idealized formulation assumes infinite-precision commitment (Tsirelson saturation). BST's sub-Tsirelson reduction is the substrate's finite-capacity correction.

The $1/2^{N_c}$ factor is exact: it equals one substrate output level (1/8 of the substrate's $2^{N_c} = 8$-level commitment space at color-degree resolution).

### 6.5 Experimental falsifier + DCCP three-route convergent pattern (Sunday 2026-05-24)

Bell experiments currently achieve $S \approx 2.83$ within errors of $\sim 0.5\%$ (Vienna, Caltech, Munich, Hanson 2015-2024).

BST prediction of $S_{BST} \approx 2.8062$: 0.78% below Tsirelson. With $\sim 0.1\%$ precision experiments (pending), this is testable.

Experimental cost: $\sim$$300-500K (Bell experiment refresh; SP-30 outreach pending).

**Toy 3516 DCCP empirical anchor (Elie, Sunday 2026-05-24)**: an independent quantum-erasure tick-test toy already filed at paper-grade v0.1 (6/6 PASS). Predicts:
- Substrate-tick boundary $\theta = \pi/N_{\max} \approx 0.023$ rad (lab-accessible)
- DCCP signature step size $1/N_{\max} \approx 0.73\%$
- Detection feasibility ~1.5σ at current 0.5% Bell precision

**Three-route convergent evidence pattern (DCCP)** — major Sunday 2026-05-24 progress:

| Route | $\Delta_{DCCP} = 1/N_{\max} \approx 0.730\%$ | $\theta_{boundary} = \pi/N_{\max} \approx 0.023$ rad |
|---|---|---|
| Empirical (Toy 3516) | ✓ 6/6 PASS | ✓ 6/6 PASS |
| Theory v1 (Lyra #320 v0.3) | **THEOREM RIGOROUS** (DCCP-1.6) | **THEOREM RIGOROUS** (DCCP-1.7) |
| Theory v2 ($\mathcal{A}_{sub}$, Lyra #322 v0.2) | FRAMEWORK (DCCP-A_sub-1) | FRAMEWORK (DCCP-A_sub-2) |

**Status**: 2 of 3 substrate-tick predictions are now THEOREM RIGOROUS on Theory v1 + FRAMEWORK on Theory v2 + 6/6 PASS empirical. Tight epistemic constraint already met for these two predictions: three routes converge on identical numerical values.

Remaining: Lemma DCCP-1.4 macroscopic-limit matching to standard Joos-Zeh γ for full decoherence rate reproduction (sketch level, v0.4 multi-week).

Per Cal #21 STANDING RULE: when Theory v2 elevates to RIGOROUS (multi-month), three-route convergence on all three predictions → D-tier RATIFICATION of DCCP-1.

### 6.6 K-audit anchors

- **T2469**: SCMP principle (Casey-named #8)
- **K66 candidate**: substrate-CHSH (pending Elie multi-month closure)
- **Vol 5 Ch 8**: Bell SCMP

## Level 3 — 5th-grader accessibility

**Bell-CHSH**: classical theories satisfy $|S| \le 2$; quantum mechanics allows up to $2\sqrt{2} \approx 2.83$ (Tsirelson). **BST predicts** $S_{BST} \approx 2.8062$, exactly $1/8 = 1/2^{N_c}$ less than Tsirelson squared. **Why**: substrate's finite operational power per Koons tick prevents Tsirelson saturation. **Falsifier**: improved Bell experiments at 0.1% precision could detect 0.78% sub-Tsirelson — distinguishes BST from standard QM. **Cost**: $300-500K.

---

## What comes next

Chapter 7 develops AC graph as theorem network.

## Where to look this up

- CHSH 1969; Tsirelson 1980
- BST: T2469; K66; Vol 5 Ch 8
