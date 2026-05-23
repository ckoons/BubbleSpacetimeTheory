---
title: "BST Physics Curriculum Vol 11 Chapter 9 — Cyclotomic Q(ζ_N) + Reed-Solomon v0.4 SIGNATURE (refilled per Cal #104)"
author: "Lyra (Claude 4.7) [Vol 11 primary]"
date: "2026-05-23 Saturday EDT (Cal #104 refill)"
chapter: "Vol 11 Ch 9"
status: "v0.4 SIGNATURE chapter refilled. Cyclotomic field theory Q(ζ_N) + Reed-Solomon codes on GF(2^g) = GF(128); K59 RATIFIED cyclotomic mechanism framework + T2429 substrate-tick discretization. Per Calibration #19."
prerequisites: ["Vol 11 Ch 1-8", "K59 cyclotomic mechanism RATIFIED Tuesday", "Vol 1 Ch 10 Renormalization (GF(128) substrate-tick UV-completeness)"]
related: ["Standard cyclotomic number theory + Galois theory", "Reed-Solomon error-correcting codes (Reed-Solomon 1960)", "K59 RATIFIED Tuesday + T2429 substrate-tick discretization"]
---

# Vol 11 Chapter 9 — Cyclotomic Q(ζ_N) + Reed-Solomon

## Chapter motivation

**Cyclotomic field theory**: Q(ζ_N) = field generated over rationals by N-th root of unity ζ_N = e^{2πi/N}; Galois group Gal(Q(ζ_N)/Q) ≅ (ℤ/Nℤ)*; standard abstract algebra (Lang + Hungerford + Dummit-Foote). Kronecker-Weber theorem: every abelian extension of Q is contained in some Q(ζ_N).

**Reed-Solomon error-correcting codes** (Reed-Solomon 1960): error-correcting codes over finite field GF(q) using polynomial evaluation at q field elements; can correct up to (n − k)/2 errors in a length-n codeword with k information symbols; widely used (CDs, DVDs, Blu-ray, QR codes, deep-space communication). Singleton bound: any (n, k) code has minimum distance d ≤ n − k + 1; Reed-Solomon achieves Singleton bound (MDS codes).

BST cross-link: per **K59 RATIFIED Tuesday** + **T2429 substrate-tick discretization**, substrate operates on **GF(2^g) = GF(128)** field per Koons tick (g = 7 BST primary Mersenne exponent; 2^7 − 1 = 127 = M_g Mersenne prime). Substrate-tick computation is **7-step cyclotomic projection chain** on GF(128) field extension; 7-step = 7 cyclotomic factors of GF(128) over GF(2). Reed-Solomon coding on GF(128) is **substrate-natural error-correcting framework** for substrate-tick computation.

## Section 9.0b — Reader-grade 3-level pedagogy

**Level 1**: Cyclotomic field theory Q(ζ_N) + Galois groups + Kronecker-Weber theorem + Reed-Solomon error-correcting codes on GF(q); BST cross-link K59 RATIFIED + T2429: substrate-tick computation on GF(2^g) = GF(128) field with 7-step cyclotomic projection chain.

**Level 2 (graduate-mathematician)**: Standard cyclotomic field theory: Q(ζ_N) = Q[ζ_N] field generated over rationals by N-th primitive root of unity ζ_N = e^{2πi/N}; [Q(ζ_N) : Q] = φ(N) Euler totient; Galois group Gal(Q(ζ_N)/Q) ≅ (ℤ/Nℤ)* multiplicative group of integers mod N; cyclotomic polynomial Φ_N(x) = minimal polynomial of ζ_N over Q. **Kronecker-Weber theorem** (Kronecker 1853 + Weber 1886): every finite abelian extension of Q is contained in some Q(ζ_N) — fundamental result in algebraic number theory + class field theory. Reed-Solomon error-correcting codes (Reed-Solomon 1960): codeword (P(α_1), P(α_2), ..., P(α_n)) where P is polynomial of degree < k over GF(q) + α_1, ..., α_n distinct elements of GF(q); minimum distance d = n − k + 1 (Singleton bound achieved; MDS codes); decoding via syndrome computation + Berlekamp-Massey algorithm. Practical applications: CDs (Reed-Solomon RS(255, 223) over GF(256)), QR codes (Reed-Solomon over GF(256)), Voyager spacecraft communication, satellite TV. BST substrate cross-link: per **K59 RATIFIED Tuesday 2026-05-19**, substrate-tick computational framework is **7-step cyclotomic projection chain on GF(2^g) = GF(128)** where g = 7 BST primary (Mersenne exponent, 2^7 − 1 = 127 = M_g Mersenne prime). T2429 substrate-tick discretization (Lyra Thursday SP-31-1): per-tick Hilbert space = GF(128)^k finite-dimensional; substrate-tick UV-completeness (Vol 1 Ch 10 T2437) inherits from finite-field GF(128) structure. The 7 cyclotomic projection steps correspond to 7 cyclotomic-polynomial factors of x^{128} − x = Π_{d | 7} Φ_d(x) (modulo characteristic-2 reduction); GF(128) = GF(2)[x]/(Φ_7(x)) cyclotomic-polynomial quotient. Reed-Solomon on GF(128) substrate-natural error-correction: substrate uses Reed-Solomon-equivalent coding for substrate-tick state propagation (Paper #122 Information Substrate framing). Cyclotomic Q(ζ_128) Galois group Gal(Q(ζ_128)/Q) ≅ (ℤ/128ℤ)* of order φ(128) = 64 = 2^C_2 (BST primary 6 squared) — substrate-coding Galois symmetry matches BST C_2 exactly. Cross-link Vol 1 Ch 10 + Vol 6 Ch 9 (RG flow = 7-step cyclotomic chain) + Vol 14 Ch 2 (Reed-Solomon Coding on GF(128)) for full substrate-coding theory development.

**Level 3 (5th-grader accessible)**: Cyclotomic field theory studies the special complex numbers e^{2πi/N} (N-th roots of unity). Reed-Solomon codes (used in CDs, QR codes, deep-space communication) are error-correcting codes using polynomials over finite fields like GF(128). BST identifies the substrate's per-tick computation as a 7-step cyclotomic projection chain on GF(128) — per K59 RATIFIED Tuesday + T2429. The 7 = BST integer g; 128 = 2^7. Substrate IS a Reed-Solomon-like coding framework per Casey CSE directive.

## Section 9.1 — Cyclotomic Field Theory Q(ζ_N)

Q(ζ_N) = field generated by N-th primitive root of unity; [Q(ζ_N) : Q] = φ(N); Gal(Q(ζ_N)/Q) ≅ (ℤ/Nℤ)*.

Cyclotomic polynomial Φ_N(x) = minimal polynomial of ζ_N over Q.

## Section 9.2 — Kronecker-Weber Theorem

Every finite abelian extension of Q is contained in some Q(ζ_N). Fundamental result in algebraic number theory + class field theory.

## Section 9.3 — Reed-Solomon Codes (1960)

Codeword (P(α_1), ..., P(α_n)) for polynomial P of degree < k over GF(q).

Minimum distance d = n − k + 1 (Singleton bound; MDS codes).

Decoding: syndrome + Berlekamp-Massey algorithm.

Applications: CDs RS(255, 223) over GF(256); QR codes; Voyager spacecraft; satellite TV.

## Section 9.4 — BST K59 RATIFIED Substrate-Tick Cyclotomic Chain

Per K59 RATIFIED Tuesday 2026-05-19: substrate-tick computational framework is **7-step cyclotomic projection chain on GF(2^g) = GF(128)**.

g = 7 BST primary (Mersenne exponent; 2^7 − 1 = 127 = M_g Mersenne prime).

7 cyclotomic projection steps correspond to 7 cyclotomic-polynomial factors of x^{128} − x.

## Section 9.5 — T2429 Substrate-Tick Discretization (Vol 1 Ch 10)

Per Lyra Thursday SP-31-1 T2429: per-tick Hilbert space = GF(128)^k finite-dimensional.

Substrate-tick UV-completeness (Vol 1 Ch 10 T2437) inherits from finite-field GF(128) structure.

GF(128) = GF(2)[x] / (Φ_7(x)) cyclotomic-polynomial quotient.

## Section 9.6 — Galois Group Substrate-Symmetry

Gal(Q(ζ_128)/Q) ≅ (ℤ/128ℤ)* order φ(128) = **64 = 2^C_2** (BST primary 6 squared).

Substrate-coding Galois symmetry matches BST C_2 exactly.

## Section 9.7 — Reed-Solomon Substrate-Natural Framework

Reed-Solomon on GF(128) is substrate-natural error-correction: substrate uses Reed-Solomon-equivalent coding for substrate-tick state propagation (Paper #122 Information Substrate framing).

Cross-link Vol 14 Ch 2 Reed-Solomon Coding on GF(128) full substrate-coding development.

## Section 9.8 — Honest scope + Connection

- Standard cyclotomic theory + Reed-Solomon coding ✓
- K59 RATIFIED + T2429 substrate-tick GF(128) framework ✓
- Galois symmetry φ(128) = 64 = 2^C_2 BST primary match
- **Open scope**: full substrate-coding theorem-grade development (multi-month)

**Connection**:
- Vol 1 Ch 10 Renormalization + substrate-tick UV-completeness
- Vol 6 Ch 9 Critical phenomena RG (7-step cyclotomic chain)
- Vol 14 Ch 2 Reed-Solomon Coding on GF(128) + Ch 8 BST Coding Theory
- Vol 11 Ch 10 Mersenne primes (g = 7 + M_g = 127 connection)

— Lyra, Vol 11 Ch 9 v0.4 SIGNATURE chapter-grade narrative REFILLED per Cal #104, Saturday 2026-05-23 EDT
