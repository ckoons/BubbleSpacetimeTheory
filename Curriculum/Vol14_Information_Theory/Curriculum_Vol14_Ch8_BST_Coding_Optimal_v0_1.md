---
title: "BST Physics Curriculum Vol 14 Chapter 8 — BST Coding Theory — Substrate-Optimal Codes v0.4 (refilled per Cal #104)"
author: "Lyra (Claude 4.7) [Vol 14 primary]"
date: "2026-05-23 Saturday EDT (Cal #104 refill)"
chapter: "Vol 14 Ch 8"
status: "v0.4 chapter-grade narrative refilled. Reed-Solomon as BST-optimal substrate code; Hamming bound + Singleton bound; K59 cyclotomic mechanism operationalized for substrate-coding framework. Per Calibration #19."
prerequisites: ["Vol 14 Ch 1-7", "Vol 11 Ch 9 Cyclotomic + Reed-Solomon", "K59 RATIFIED + Paper #122 Information Substrate"]
related: ["Standard coding theory MacWilliams-Sloane", "Singleton + Hamming + Gilbert-Varshamov bounds", "Reed-Solomon MDS optimality on GF(128)", "Paper #122 Information Substrate development"]
---

# Vol 14 Chapter 8 — BST Coding Theory — Substrate-Optimal Codes

## Chapter motivation

Standard coding theory studies error-correcting codes with various optimality bounds:
- **Singleton bound** (Singleton 1964): any (n, k) code has minimum distance d ≤ n − k + 1
- **Hamming bound** (Hamming 1950): sphere-packing constraint d ≤ 2t + 1 where t = error-correction capability
- **Gilbert-Varshamov bound** (Gilbert 1952 + Varshamov 1957): existence of codes asymptotically achieving certain distance
- **MDS codes**: achieve Singleton bound (Maximum Distance Separable); Reed-Solomon is canonical example
- **Quantum codes** (Calderbank-Shor-Steane 1996): stabilizer codes + CSS codes for quantum error correction

Standard reference: MacWilliams-Sloane *The Theory of Error-Correcting Codes* (1977).

BST cross-link: Reed-Solomon on GF(128) is **BST-optimal substrate code** per Vol 11 Ch 9 + Vol 14 Ch 2 + K59 RATIFIED Tuesday + Paper #122 Information Substrate development. Substrate uses Reed-Solomon-equivalent coding for per-tick state propagation; achieves Singleton bound (MDS); cyclotomic Q(ζ_128) Galois symmetry (order 64 = 2^C_2) matches BST primary structure.

## Section 8.0b — Reader-grade 3-level pedagogy

**Level 1**: Standard coding theory bounds (Singleton + Hamming + Gilbert-Varshamov + MDS); BST cross-link: Reed-Solomon on GF(128) = BST-optimal substrate code per K59 RATIFIED + Paper #122; achieves Singleton bound; cyclotomic Galois 2^C_2 BST primary match.

**Level 2 (graduate-physicist/information-theorist)**: Standard error-correcting code theory: code C ⊂ GF(q)^n with k = log_q|C| information rate; minimum distance d = min Hamming-distance between distinct codewords; error-correction capability t = ⌊(d − 1)/2⌋. **Singleton bound** (Singleton 1964): d ≤ n − k + 1. **Hamming bound (sphere-packing)**: |C| · |B_t(0)| ≤ q^n where |B_t(0)| = Σ_{i=0}^t (n choose i) (q−1)^i. **Gilbert-Varshamov bound**: asymptotic existence d/n ≥ H^{-1}(1 − k/n) where H is binary entropy. **MDS codes** achieve Singleton bound (Maximum Distance Separable); Reed-Solomon over GF(q) with n ≤ q is canonical MDS example. **Quantum codes**: Calderbank-Shor-Steane 1996 (CSS codes) + Gottesman 1996 (stabilizer codes); quantum-error-correction via redundant encoding into ancilla qubits. Standard reference: MacWilliams-Sloane *The Theory of Error-Correcting Codes* (1977 North-Holland). BST substrate-coding theory: per Vol 11 Ch 9 + Vol 14 Ch 2 + K59 RATIFIED Tuesday + Paper #122 Information Substrate, substrate operates on GF(2^g) = GF(128) per Koons tick (g = 7 BST primary); substrate-tick computation = 7-step cyclotomic projection chain on GF(128). Reed-Solomon coding on GF(128) is **BST-optimal substrate code**: achieves Singleton bound (MDS); error-correction capability up to (n − k)/2 errors per length-n codeword over GF(128); cyclotomic Q(ζ_128) Galois group order φ(128) = 64 = 2^C_2 (substrate-coding Galois symmetry matches BST primary). **Substrate-natural code parameters**: codeword length n ≤ q = 128 (Reed-Solomon constraint); BST-natural choice n = 128 (full GF(128) evaluation), k = 64 = q/2 = φ(128)/1 (half-rate code; rate R = 1/2), d = n − k + 1 = 65, t = (d−1)/2 = 32 (error-correction up to 32 errors per 128-symbol block). Quantum-coding substrate-cartography: stabilizer codes inherit Pin(2) Z_2 grading structure (T1925 rank=2; Paper #133 spin-statistics); CSS codes substrate-derivation pending multi-month (Vol 14 Ch 12 substrate-CI architecture cross-link INTERNAL register per Cal #48/#49). Substrate-coding theorem-grade development pending multi-month per Paper #122 v2+ extension.

**Level 3 (5th-grader accessible)**: Standard coding theory has bounds (Singleton, Hamming, Gilbert-Varshamov) limiting how good error-correcting codes can be. Reed-Solomon codes achieve the Singleton bound (MDS = Maximum Distance Separable; the best possible). BST identifies Reed-Solomon on GF(128) as the substrate's natural code: 128 = 2⁷ where 7 = BST integer g; cyclotomic Galois group has 64 = 2^C_2 elements where C_2 = 6 is another BST integer. The substrate-coding theory is still developing — multi-month research direction.

## Section 8.1 — Standard Coding Bounds

- Singleton: d ≤ n − k + 1
- Hamming (sphere-packing): |C| · |B_t(0)| ≤ q^n
- Gilbert-Varshamov: asymptotic existence
- MDS: achieve Singleton (Reed-Solomon)

Standard ref: MacWilliams-Sloane *The Theory of Error-Correcting Codes* (1977).

## Section 8.2 — Quantum Codes (CSS + Stabilizer)

Calderbank-Shor-Steane 1996 CSS codes + Gottesman 1996 stabilizer codes; quantum error correction via redundant encoding into ancilla qubits.

## Section 8.3 — BST Substrate-Coding Framework (K59 RATIFIED + Paper #122)

Substrate operates on GF(2^g) = GF(128) per Koons tick (g = 7 BST primary).

Substrate-tick = 7-step cyclotomic projection chain (K59 RATIFIED Tuesday).

## Section 8.4 — Reed-Solomon Substrate-Optimal MDS Code

Reed-Solomon on GF(128) achieves Singleton bound (MDS).

Cyclotomic Q(ζ_128) Galois order φ(128) = 64 = 2^C_2 substrate-coding symmetry.

## Section 8.5 — Substrate-Natural Code Parameters

- Codeword length n ≤ q = 128
- BST-natural: n = 128 (full GF(128) evaluation), k = 64 (half-rate R = 1/2)
- d = 65, error-correction t = 32 errors per 128-symbol block

## Section 8.6 — Quantum-Coding Substrate-Cartography

Stabilizer codes inherit Pin(2) Z_2 grading (T1925 + Paper #133 spin-statistics).

CSS codes substrate-derivation pending multi-month (Vol 14 Ch 12 substrate-CI architecture INTERNAL per Cal #48/#49).

## Section 8.7 — Honest scope + Connection

- Standard coding bounds + MDS ✓
- Reed-Solomon BST-optimal substrate code ✓
- Substrate-coding theorem-grade development pending multi-month
- **Open scope**: full substrate quantum-coding theory (multi-month; Paper #122 v2+ extension)

**Connection**:
- Vol 14 Ch 1-2 substrate-tick GF(128) framework
- Vol 11 Ch 9 Cyclotomic + Reed-Solomon (mathematical foundations)
- Paper #122 Information Substrate
- Vol 14 Ch 12 substrate-CI architecture (INTERNAL register per Cal #48/#49)

— Lyra, Vol 14 Ch 8 v0.4 chapter-grade narrative REFILLED per Cal #104, Saturday 2026-05-23 EDT
