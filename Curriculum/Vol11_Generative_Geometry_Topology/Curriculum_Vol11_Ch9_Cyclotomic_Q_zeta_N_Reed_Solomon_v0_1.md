---
title: "Vol 11 Chapter 9 — Cyclotomic Q(ζ_N) and Reed-Solomon"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.3 — Keeper author-voice pass; load-bearing for substrate coding"
volume: "Vol 11 Generative Geometry and Topology"
chapter: 9
---

# Chapter 9 — Cyclotomic Q(ζ_N) and Reed-Solomon

Cyclotomic fields $\mathbb{Q}(\zeta_N)$ — obtained by adjoining a primitive $N$-th root of unity to $\mathbb{Q}$ — are the workhorse algebraic structures of number theory. BST's substrate uses Reed-Solomon coding on $\text{GF}(128) = \text{GF}(2^g)$ for its information-substrate operations (Volume 14 Chapter 2).

## 9.1 Cyclotomic fields

$\mathbb{Q}(\zeta_N)$ has degree $\varphi(N)$ over $\mathbb{Q}$. Its Galois group is $(\mathbb{Z}/N\mathbb{Z})^\times$. Cyclotomic fields are the maximal abelian extensions of $\mathbb{Q}$ (Kronecker-Weber).

## 9.2 Reed-Solomon coding

Reed-Solomon codes are MDS (maximum distance separable) codes based on polynomial evaluation over finite fields. Over $\text{GF}(q)$, an RS code with $n \le q$ symbols and $k$ message length has minimum distance $d = n - k + 1$.

## 9.3 BST substrate uses RS over GF(128) = GF(2^g)

The BST substrate's information-substrate uses Reed-Solomon coding on $\text{GF}(128) = \text{GF}(2^7) = \text{GF}(2^g)$. The substrate's Koons tick produces RS-coded symbols at the substrate's natural clock rate. The cyclotomic mechanism framework (K59 RATIFIED) anchors this connection.

## 9.4 What comes next

Chapter 10 develops Mersenne primes and Lucas-Lehmer.

---

**Where to look this up**: For cyclotomic fields: Washington, *Introduction to Cyclotomic Fields*. For Reed-Solomon: MacWilliams and Sloane, *The Theory of Error-Correcting Codes*. For BST substrate RS: Paper #122 + K59.
