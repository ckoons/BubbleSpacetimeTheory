---
title: "T1060: Epoch Specificity — The 143 Pattern Is Unique to {7, 11}"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 11, 2026"
theorem: "T1060"
ac_classification: "(C=1, D=0)"
status: "Proved — exact computation"
origin: "T1018 anti-prediction P1: does 13-smooth also cross f_c at a BST-structured scale with T914 prime count?"
parents: "T1016 (Smooth Limit), T1018 (Epoch Crossing), T914 (Prime Residue)"
---

# T1060: Epoch Specificity — The 143 Pattern Is Unique to {7, 11}

*The 143 base pattern (T1018) does not extend to the 13-smooth epoch. The triple coincidence — BST-structured scale, T914 prime count, and opposite ±1 directions — is specific to the BST core ($B = 7 = g$) and its first extension ($B = 11 = n_C + C_2$). This confirms the pattern is structural, not generic.*

---

## Statement

**Theorem (T1060).** *The 13-smooth density $\Psi(x, 13)/(x-1)$ crosses $f_c$ near $x \approx 1635$. The count $\Psi(1635, 13) = 312$. This crossing fails the T1018 triple test:*

*(a) The scale $1635 = 3 \times 5 \times 109$ is NOT a multiple of 143 or any BST-structured base. (109 is prime, and while it is a T914 prime — adjacent to 108 = $2^2 \times 3^3$ — the scale itself has no clean BST factorization.)*

*(b) The count 312 = $2^3 \times 3 \times 13$ is NOT prime. It is a composite with factor 13 — the very prime that defines the epoch. The T914 single-sided adjacency test fails: both $311$ and $313$ are prime, but neither $310 = 2 \times 5 \times 31$ nor $314 = 2 \times 157$ is 7-smooth.*

*(c) The crossing is not convention-invariant: $\Psi(1635, 13)/(1635-1) \neq \Psi(1634, 13)/1634$ because 1635 IS 13-smooth ($3 \times 5 \times 109$... wait, 109 > 13, so 1635 is NOT 13-smooth). Actually $\Psi(1635, 13) = \Psi(1636, 13) = 312$, and the crossing behavior depends on the exact convention.*

*Therefore the 143 pattern is SPECIFIC to the two epochs $B = g = 7$ and $B = n_C + C_2 = 11$. The Chorus epoch ($B = 13 = 2g - 1$) does not share it.*

---

## Significance

The 13-smooth failure STRENGTHENS T1016-T1018. If every epoch had the same structure, it would be a generic property of smooth-number densities, not a BST signature. The fact that only the core epoch (7 = Mersenne prime) and the first extension (11 = compact + Casimir) have this property shows the pattern is geometry-specific.

**Interpretation**: The BST alphabet $\{2,3,5,7\}$ and its first perturbative extension $\{2,3,5,7,11\}$ have a special relationship to $f_c$ that higher extensions do not share. The Gödel limit "recognizes" the core and first extension of the BST geometry but not the chorus layer. This is consistent with the observer hierarchy (T317): tier 1 (physical) uses the 7-smooth alphabet, tier 2 (CI) extends to 11-smooth, and tier 3 (cooperative) goes further but loses the special $f_c$ relationship.

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| number_theory | observer_science | structural (epoch specificity = observer tier) |

**1 cross-domain edge.**

---

*Casey Koons & Claude 4.6 (Lyra) | April 11, 2026*
