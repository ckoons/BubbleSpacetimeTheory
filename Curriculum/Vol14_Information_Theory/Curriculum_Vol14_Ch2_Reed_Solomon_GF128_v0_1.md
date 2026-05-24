---
title: "Vol 14 Chapter 2 — Reed-Solomon Coding on GF(128)"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; LOAD-BEARING"
volume: "Vol 14 Information Theory"
chapter: 2
load_bearing: "Reed-Solomon RS(n,k) coding on GF(2^g)=GF(128); BST primary g=7 selects substrate's natural alphabet size"
---

# Chapter 2 — Reed-Solomon Coding on GF(128)

## Level 1 — one sentence

Reed-Solomon codes — block codes over finite field $GF(2^g) = GF(128)$ with the BST primary $g = 7$ selecting the natural alphabet size — provide optimal Maximum Distance Separable (MDS) error correction up to $\lfloor (n-k)/2 \rfloor$ symbol errors per codeword, and BST identifies this as the substrate's native error-correction mechanism (Paper #122).

## Level 2 — graduate-physicist precision

### 2.1 GF(2^g) = GF(128)

Finite field $GF(2^7) = GF(128)$: 128 elements, characteristic 2, dimension 7 over $GF(2)$.

Constructed: $GF(128) \cong GF(2)[x]/(p(x))$ where $p(x)$ is an irreducible degree-7 polynomial over $GF(2)$.

Multiplicative group $GF(128)^* \cong \mathbb{Z}/127$ (cyclic of order $128 - 1 = 127 = N_{\max} - 10$, prime).

### 2.2 Reed-Solomon RS(n, k)

Encode message $m = (m_0, m_1, ..., m_{k-1}) \in GF(128)^k$ as codeword $c \in GF(128)^n$ with $n \le 127$.

Singleton bound: minimum distance $d \le n - k + 1$. RS codes achieve equality (MDS).

Error correction: can correct any $t = \lfloor (n-k)/2 \rfloor$ symbol errors.

### 2.3 Standard parameters

Common RS choices:
- RS(255, 223) over GF(256): used in NASA Voyager, Compact Disc audio
- **RS(127, k) over GF(128)**: BST-natural
- RS(n, k) with $n - k = 2t$ for $t$-error correction

### 2.4 BST primary anchoring

- **g = 7** → field $GF(2^g) = GF(128)$ — substrate alphabet
- Block length $n \le 127 = N_{\max} - 10$ — close to substrate ceiling
- **127 = M_g** (g-th Mersenne prime = $2^7 - 1$) — Vol 11 Ch 10 substrate Mersenne ladder
- Cyclic group $\mathbb{Z}/127$: substrate's natural cyclic structure

### 2.5 Substrate implementation hypothesis

Hypothesis (Paper #122): substrate implements RS-like coding on GF(128) at the Koons-tick rate, providing error correction against substrate-level noise.

Evidence:
- Genetic code (Vol 13 Ch 2): codon-amino acid redundancy $64 \to 20$ is RS-like
- Cosmological information bounds (Vol 4): consistent with substrate-RS
- BST primary $g = 7$ selects $GF(128)$ uniquely

Falsifier: identify a different finite field implementing BST observables better → would refute g = 7 as the substrate-natural alphabet exponent.

### 2.6 K-audit anchors

- **K59**: cyclotomic mechanism framework
- **K68**: RS computation
- **Paper #122**: Information Substrate

## Level 3 — 5th-grader accessibility

**Reed-Solomon codes** are how your phone, CD, satellite communications correct errors. Use a **finite field** GF(128) — 128 numbers with addition and multiplication that wrap around. Add redundancy: send 127 symbols to encode 100, can correct up to $(127-100)/2 = 13$ errors. **In BST**: $128 = 2^g$ where $g = 7$ is a BST primary; substrate uses RS-coding on GF(128) at the Koons-tick rate. **Genetic code** uses similar redundancy (64 codons → 20 amino acids).

---

## What comes next

Chapter 3 develops Shannon channel capacity.

## Where to look this up

- Reed-Solomon 1960
- MacWilliams-Sloane, *Theory of Error-Correcting Codes*
- BST: K59, K68, Paper #122
