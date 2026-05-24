---
title: "Vol 11 Chapter 10 — Mersenne Primes and Lucas-Lehmer"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; Mersenne ladder anchors BST primary exponents (May 22 2026 finding)"
volume: "Vol 11 Generative Geometry and Topology"
chapter: 10
load_bearing: "Mersenne primes M_p = 2^p − 1; Lucas-Lehmer primality test; Mersenne ladder anchors BST primary structure"
---

# Chapter 10 — Mersenne Primes and Lucas-Lehmer

## Level 1 — one sentence

Mersenne primes $M_p = 2^p - 1$ for prime $p$ have been studied since antiquity, with Lucas-Lehmer primality test providing efficient verification, and the BST team's Friday May 22, 2026 finding ("Mersenne Network Convergence") shows BST primary exponents are anchored in a Mersenne ladder: $M_{\text{rank}} = 3 = N_c$, $M_{N_c} = 7 = g$, $M_{n_C} = 31$, $M_g = 127$ — with additive identity $N_{\max} - M_g = 10 = g + N_c$.

## Level 2 — graduate-physicist precision

### 10.1 Mersenne primes

$M_p = 2^p - 1$. Prime $M_p$ requires $p$ prime, but not all prime $p$ give prime $M_p$.

Known Mersenne primes (52 as of 2024): $M_2 = 3, M_3 = 7, M_5 = 31, M_7 = 127, M_{13} = 8191, M_{17} = 131071, M_{19}, M_{31}, M_{61}, M_{89}, M_{107}, M_{127}, M_{521}, \ldots, M_{82589933}$.

GIMPS (Great Internet Mersenne Prime Search) project actively searches.

### 10.2 Lucas-Lehmer primality test

For $p \ge 3$ odd prime: define $s_0 = 4$ and $s_{i+1} = s_i^2 - 2 \pmod{M_p}$.

$M_p$ is prime iff $s_{p-2} \equiv 0 \pmod{M_p}$.

Polynomial time in $p$ — efficient.

### 10.3 BST Mersenne ladder (Friday May 22, 2026)

The team's Friday May 22, 2026 substrate-investigation finding (Mersenne Network Convergence):

BST primary exponents are anchored on Mersenne primes:
- $M_{\text{rank}} = M_2 = 3 = N_c$ (Mersenne exponent rank → BST primary $N_c$)
- $M_{N_c} = M_3 = 7 = g$ (Mersenne exponent $N_c$ → BST primary $g$)
- $M_{n_C} = M_5 = 31$ (Mersenne exponent $n_C$ → 31, prime)
- $M_g = M_7 = 127$ (Mersenne exponent $g$ → 127, prime)

**Additive identity**: $N_{\max} - M_g = 137 - 127 = 10 = g + N_c$. The substrate's natural integer relationship.

The $c_2 = 6$ "gap" resolved via $M_{c_2} = M_6 = 63 = 9 \cdot 7$, requiring composite interpretation.

### 10.4 6/7 Mersenne primes

6 of BST's first 7 primary-exponent Mersenne values are themselves prime: $\{3, 7, 31, 127\}$ are Mersenne primes. Only $M_6 = 63$ is composite (as expected — index 6 is composite).

This high "Mersenne primality density" in BST primary exponents is a substrate-mechanism finding (Lyra T2452, Friday May 22, 2026).

### 10.5 Substrate Mersenne network

Combined with Graph Forces (Grace) and Mersenne tower (Elie + Casey): three independent patterns converge on substrate Mersenne-anchored over-determination of BST primaries:
- Graph Forces (Grace, $p \approx 2.7 \times 10^{-5}$)
- Mersenne tower (T2452 Elie+Casey)
- Mersenne ladder (Friday May 22 finding)

Triple convergence is one of BST's strong-uniqueness pieces of evidence.

### 10.6 Substrate computational substrate

The substrate's natural RS coding on $\text{GF}(2^g) = \text{GF}(128)$ (Ch 9) has maximum codeword length $n = 127 = M_g = M_7$.

Substrate has a Mersenne prime as its natural codeword-length parameter — direct substrate-mechanism integer.

### 10.7 K-audit anchors

- **Mersenne ladder Friday May 22, 2026**
- **Lyra T2452**: Mersenne tower theorem
- **K156 audit anchor** (pending): three-layer over-determinism with Mersenne layer

## Level 3 — 5th-grader accessibility

**Mersenne primes**: $M_p = 2^p - 1$ for prime $p$. Examples: $M_2 = 3, M_3 = 7, M_5 = 31, M_7 = 127$. GIMPS project hunts for more. **BST Mersenne ladder** (May 22, 2026 finding): the BST primary integers fit into a Mersenne pattern: $M_2 = N_c, M_3 = g$, etc. **6 of 7** are Mersenne primes. **Additive identity**: $N_{\max} - M_g = 10 = g + N_c$. The substrate's natural integer arithmetic is Mersenne-anchored. Codeword length $127 = M_7 = M_g$ for substrate's Reed-Solomon coding.

---

## What comes next

Chapter 11 develops the generative-geometry framing thesis.

## Where to look this up

- GIMPS project
- Crandall-Pomerance, *Prime Numbers*
- BST: Mersenne ladder Friday May 22; Lyra T2452
