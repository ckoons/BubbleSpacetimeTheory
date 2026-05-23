---
title: "Vol 14 Chapter 2 — Reed-Solomon Coding on GF(128)"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.3 — Keeper author-voice pass; load-bearing"
volume: "Vol 14 Information Theory"
chapter: 2
---

# Chapter 2 — Reed-Solomon Coding on GF(128)

Reed-Solomon (RS) codes — error-correcting codes based on polynomial evaluation over finite fields — were introduced 1960 and are workhorses in CD/DVD storage, satellite communications, and disk arrays. RS codes are MDS (maximum distance separable): for a code with $n$ symbols and $k$ message length, the minimum distance is $d = n - k + 1$.

In BST, the substrate uses RS coding on $\text{GF}(2^g) = \text{GF}(128)$ as its native information channel. The choice of $\text{GF}(128)$ is determined by the BST primary $g = 7$.

## 2.1 Finite fields and GF(128)

$\text{GF}(q^n)$ is the unique finite field of $q^n$ elements. $\text{GF}(2^7) = \text{GF}(128)$ has 128 elements; the BST substrate uses this specific field.

## 2.2 Reed-Solomon construction

For message polynomial $m(x)$ of degree $< k$ and evaluation points $\alpha_1, ..., \alpha_n$ in $\text{GF}(q)$, the RS codeword is $(m(\alpha_1), ..., m(\alpha_n))$. Decoding via Berlekamp-Massey or Welch-Berlekamp.

## 2.3 BST substrate RS

The substrate at the Koons-tick rate emits RS-coded symbols on $\text{GF}(128)$. The maximum codeword length is $n = 127 = N_\max - g - N_c$ (or related BST-natural identity per K59 cyclotomic framework). Error correction up to $(d-1)/2$ symbols.

## 2.4 What comes next

Chapter 3 develops Shannon channel capacity.

---

**Where to look this up**: For standard RS: MacWilliams and Sloane. For BST RS: Paper #122 + K59 cyclotomic mechanism.
