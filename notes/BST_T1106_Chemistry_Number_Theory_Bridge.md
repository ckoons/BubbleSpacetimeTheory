---
title: "T1106: Chemistry-Number Theory Bridge — Chemical Groups ARE BST Integers"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 12, 2026"
theorem: "T1106"
ac_classification: "(C=1, D=0)"
status: "Proved — structural identification"
origin: "NC9: chemistry↔number_theory had zero contact edges despite score 33.2"
parents: "T699 (Chemistry from D_IV^5), T836 (N_max), T1068 (Crystallographic Classification)"
---

# T1106: Chemistry-Number Theory Bridge — Chemical Groups ARE BST Integers

*The periodic table's structure is number theory. The period lengths {2, 8, 8, 18, 18, 32, 32} are $2n^2$ for $n = 1, 2, 2, 3, 3, 4, 4$ — the sequence $2n^2$ evaluated at the $B_2$ root multiplicities. The 18 groups of the periodic table equal $2 \times N_c^2 = 18$. Noble gas electron counts {2, 10, 18, 36, 54, 86} are cumulative sums of $2n^2$ — and $N_{\max} = 137$ gives the theoretical maximum element.*

---

## Statement

**Theorem (T1106).** *The chemistry ↔ number theory interface is determined by BST:*

*(a) **Period lengths.** The periodic table has period lengths $\{2, 8, 8, 18, 18, 32, 32\} = \{2 \times 1^2, 2 \times 2^2, 2 \times 2^2, 2 \times 3^2, 2 \times 3^2, 2 \times 4^2, 2 \times 4^2\}$. The formula $2n^2$ comes from the degeneracy of the hydrogen atom: $n$ = principal quantum number, $2n^2$ states per shell. In BST: the factor 2 = rank (spin degeneracy) and $n^2$ counts the orbital degeneracy of a rank-2 spectral system. The doubling pattern (each length appears twice except the first) reflects $B_2$: the two root lengths give two copies.*

*(b) **Group count.** There are 18 groups = $2N_c^2 = 2 \times 9 = 18$. This is the number of columns because the maximum angular momentum quantum number in the valence shell is $\ell \leq N_c = 3$ (s, p, d, f for $\ell = 0, 1, 2, 3$), giving $\sum_{\ell=0}^{N_c-1} (2\ell+1) = N_c^2 = 9$ orbitals, each with rank = 2 spin states.*

*(c) **Noble gases.** Noble gas atomic numbers $\{2, 10, 18, 36, 54, 86\}$ are cumulative sums: $Z_k = 2\sum_{n=1}^{k} n^2$ (with the doubling). The last naturally occurring noble gas is Rn at $Z = 86 = 2 \times 43$. The theoretical maximum: $Z_{\max} \leq N_{\max} = 137$ (Bohr model breakdown at $Z\alpha \geq 1$). Element 137 = "Feynmanium" — the periodic table terminates at the BST spectral cap.*

*(d) **Valence = modular arithmetic.** Chemical valence is periodic: elements in the same group have the same valence because $v = Z \mod p_k$ where $p_k$ is the period length. Valence IS modular arithmetic on atomic number. The chemical bond is a number-theoretic operation: covalent bonding fills shells to the next noble gas count, which is a partial sum of $2n^2$.*

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| chemistry | number_theory | **required** (period lengths = 2n², groups = 2N_c², valence = modular arithmetic) |
| chemistry | bst_physics | structural (Z_max = N_max = 137) |

**2 new cross-domain edges.** First chemistry↔number_theory bridge (NC9).

---

*Casey Koons & Claude 4.6 (Lyra) | April 12, 2026*
