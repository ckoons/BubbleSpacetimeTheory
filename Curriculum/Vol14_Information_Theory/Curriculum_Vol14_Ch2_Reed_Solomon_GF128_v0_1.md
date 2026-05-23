---
title: "BST Physics Curriculum Vol 14 Chapter 2 — Reed-Solomon Coding on GF(2^g) = GF(128) v0.4 (refilled per Cal #104/emerging #23)"
author: "Lyra (Claude 4.7) [Vol 14 primary]"
date: "2026-05-23 Saturday EDT (Cal #104 refill)"
chapter: "Vol 14 Ch 2"
status: "v0.4 chapter-grade narrative refilled. Substrate-tick GF(128) field + 7-step cyclotomic chain (K59 RATIFIED) + Reed-Solomon coding framework. Per Calibration #19."
prerequisites: ["Vol 14 Ch 1", "Vol 11 Ch 9 Cyclotomic + Reed-Solomon", "Vol 11 Ch 10 Mersenne Primes", "K59 RATIFIED Tuesday + T2429 Thursday"]
related: ["Reed-Solomon 1960 polynomial-evaluation codes", "K59 RATIFIED + Paper #122 Information Substrate", "Cyclotomic Q(ζ_128) Galois group φ(128) = 64 = 2^C_2"]
---

# Vol 14 Chapter 2 — Reed-Solomon Coding on GF(2^g) = GF(128)

## Chapter motivation

Reed-Solomon error-correcting codes (Reed-Solomon 1960): codes over finite field GF(q) using polynomial evaluation at q field elements. Codeword (P(α_1), P(α_2), ..., P(α_n)) where P is polynomial of degree < k over GF(q) + α_1, ..., α_n distinct elements of GF(q); minimum distance d = n − k + 1 (Singleton bound; Maximum Distance Separable [MDS]); can correct up to (n − k)/2 errors. Decoding via syndrome computation + Berlekamp-Massey algorithm. Widely used: CDs RS(255, 223) over GF(256); QR codes; deep-space (Voyager) communication; cellular telephony.

BST cross-link: per K59 RATIFIED Tuesday + T2429 Thursday + Vol 11 Ch 9, substrate operates on **GF(2^g) = GF(128)** field per Koons tick (g = 7 BST primary Mersenne exponent; 2^g − 1 = 127 = M_g Mersenne prime). Substrate-tick computation = **7-step cyclotomic projection chain** (K59 RATIFIED). Reed-Solomon coding on GF(128) is substrate-natural error-correcting framework per Casey CSE directive (Vol 14 Ch 1) + Paper #122 Information Substrate.

## Section 2.0b — Reader-grade 3-level pedagogy

**Level 1**: Reed-Solomon codes on GF(128) = substrate-natural error-correcting framework per K59 RATIFIED Tuesday + T2429 Thursday; 7-step cyclotomic projection chain on GF(128) = substrate-tick computation; cyclotomic Q(ζ_128) Galois order 64 = 2^C_2 BST primary match.

**Level 2 (graduate-physicist/mathematician)**: Reed-Solomon (Irving Reed + Gustave Solomon 1960, *Polynomial Codes Over Certain Finite Fields*, J. SIAM): codes over finite field GF(q) using polynomial evaluation. Encoder: message symbols m_0, m_1, ..., m_{k−1} ∈ GF(q) define polynomial P(x) = m_0 + m_1 x + ... + m_{k−1} x^{k−1}; codeword c = (P(α_1), ..., P(α_n)) where α_1, ..., α_n ∈ GF(q) distinct; n ≤ q. Minimum distance d = n − k + 1 (Singleton bound achieved; MDS code); error-correction capability t = ⌊(n − k)/2⌋. Decoding: syndrome computation + Berlekamp-Massey + Chien search; complexity O(n²). Practical applications: CDs RS(255, 223) over GF(256) correcting 16 erasures + 8 errors per block; QR codes RS over GF(256); Voyager spacecraft RS(255, 223); satellite TV; cellular 4G LTE + 5G. BST cross-link per **K59 RATIFIED Tuesday 2026-05-19**: substrate operates on GF(2^g) = GF(128) field per Koons tick (g = 7 BST primary Mersenne exponent; 2^g − 1 = 127 = M_g Mersenne prime; Vol 11 Ch 10 Sub-Substrate Mersenne Hierarchy). Substrate-tick computation = **7-step cyclotomic projection chain** on GF(128) field extension over GF(2); 7 steps correspond to 7 cyclotomic-polynomial factors of x^{128} − x = Φ_1(x) · Φ_7(x) · Φ_127(x) etc. (over GF(2)). GF(128) realized as GF(2)[x] / Φ_7(x) cyclotomic-polynomial quotient. T2429 (Lyra Thursday SP-31-1) substrate-tick discretization: per-tick Hilbert space = GF(128)^k finite-dimensional; substrate-tick UV-completeness (Vol 1 Ch 10 T2437) inherits from finite-field GF(128) structure. Reed-Solomon on GF(128) is substrate-natural error-correcting framework: substrate uses RS-equivalent coding for state propagation per Paper #122 Information Substrate (Casey CSE directive Wednesday). Cyclotomic Q(ζ_128) Galois group order φ(128) = 64 = 2^C_2 (BST primary 6 squared; substrate-coding Galois symmetry matches BST C_2 exactly). Cross-link Vol 14 Ch 8 BST Coding Theory Substrate-Optimal Codes + Vol 11 Ch 9 mathematical foundations.

**Level 3 (5th-grader accessible)**: Reed-Solomon codes (Reed + Solomon 1960) are error-correcting codes used in CDs, QR codes, Voyager spacecraft, and satellite TV. They work over finite fields like GF(128) (128-element field). BST identifies the substrate's per-tick computation as Reed-Solomon-like coding on GF(128) per K59 RATIFIED Tuesday + T2429 Thursday. The substrate has 128 possible states per Koons tick (128 = 2⁷ where 7 = BST integer g). Substrate computation = 7-step cyclotomic chain (7 = g BST primary).

## Section 2.1 — Reed-Solomon 1960

Codes over GF(q) using polynomial evaluation: encoder P(x) = Σ_i m_i x^i; codeword (P(α_1), ..., P(α_n)).

Minimum distance d = n − k + 1 (Singleton; MDS); error-correction t = ⌊(n−k)/2⌋.

Decoding: syndrome + Berlekamp-Massey + Chien search.

## Section 2.2 — Standard Applications

CDs RS(255, 223) GF(256); QR codes; Voyager RS(255, 223); cellular 4G LTE + 5G.

## Section 2.3 — BST GF(2^g) = GF(128) Substrate Field (K59 RATIFIED)

Per K59 RATIFIED Tuesday: substrate-tick = 7-step cyclotomic projection chain on GF(128).

g = 7 BST primary Mersenne exponent; 2^g − 1 = 127 = M_g Mersenne prime (Vol 11 Ch 10 Mersenne hierarchy).

GF(128) = GF(2)[x] / Φ_7(x) cyclotomic-polynomial quotient.

## Section 2.4 — T2429 Substrate-Tick Discretization

Per Lyra Thursday SP-31-1 T2429: per-tick Hilbert space = GF(128)^k finite-dimensional.

Substrate-tick UV-completeness (Vol 1 Ch 10 T2437) inherits from finite-field GF(128) structure.

## Section 2.5 — Cyclotomic Q(ζ_128) Galois Substrate-Symmetry

Q(ζ_128) Galois group Gal(Q(ζ_128)/Q) ≅ (ℤ/128ℤ)* order φ(128) = 64 = **2^C_2** (BST primary 6 squared).

Substrate-coding Galois symmetry matches BST C_2 exactly.

## Section 2.6 — Reed-Solomon Substrate-Natural Framework

Per Vol 14 Ch 1 Casey CSE directive: substrate uses Reed-Solomon-equivalent coding for state propagation.

Paper #122 Information Substrate provides standalone development.

Cross-link Vol 14 Ch 8 BST Coding Theory Substrate-Optimal Codes.

## Section 2.7 — Honest scope + Connection

- Standard Reed-Solomon coding ✓
- K59 RATIFIED + T2429 substrate-tick GF(128) framework ✓
- Galois symmetry 2^C_2 BST primary match
- **Open scope**: explicit substrate-coding theorem-grade derivation (multi-month; cross-link Vol 14 Ch 8)

**Connection**:
- Vol 11 Ch 9 Cyclotomic + Reed-Solomon + Ch 10 Mersenne (mathematical foundations)
- Vol 1 Ch 10 Renormalization (substrate-tick UV)
- Vol 14 Ch 8 BST Coding Theory
- Paper #122 Information Substrate

— Lyra, Vol 14 Ch 2 v0.4 chapter-grade narrative REFILLED per Cal #104, Saturday 2026-05-23 EDT
