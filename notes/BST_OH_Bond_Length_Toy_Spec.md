---
title: "O-H Bond Length from D_IV^5 — Toy Spec"
author: "Keeper (for Elie)"
date: "April 2, 2026"
toy: "next available"
paper: "#18 (Molecular Geometry)"
priority: "Track A, Item 3"
---

# O-H Bond Length from Five Integers — Toy Spec

## Goal

Derive the O-H bond length in water from BST integers. Second chemistry prediction after bond angles (Toy 680).

## Known values

- **NIST O-H bond length**: 0.9572 Å (gas phase H₂O)
- **BST bond angle**: arccos(-1/4) = 104.478° (T700, 0.028° from measured)
- **Bohr radius**: a₀ = ℏ/(m_e c α) = 0.52918 Å

## Candidate routes

### Route A: Bohr radius × integer formula
The simplest BST approach — bond length as a rational multiple of a₀.

- a₀ × 2^rank = 0.52918 × 4 = 2.117 Å (too long)
- a₀ × (N_c + 2)/n_C = 0.52918 × 1 = 0.529 Å (too short)
- a₀ × C₂/n_C × rank/N_c = 0.52918 × 6/5 × 2/3 = 0.52918 × 0.8 = 0.423 Å (too short)
- **a₀ × (2N_c - 1)/N_c = a₀ × 5/3 = 0.8820 Å** (7.9% short)
- **a₀ × (n_C + rank × N_c)/(2n_C) = a₀ × 11/10 = 0.5821 Å** (too short)

Try: a₀ × f(Z_O) where Z_O = 8 = 2^N_c = |W(B₂)|.

### Route B: Bond angle + molecular geometry
Given θ = arccos(-1/4) and the O-H distance, the H-H distance follows. Or reverse: derive H-H from BST, get O-H.

- H-H in H₂: 0.7414 Å. Ratio O-H/H-H(H₂) = 1.291. Is 1.291 a BST number?
- In H₂O: H-H distance = 2 × r_OH × sin(θ/2) = 2 × 0.9572 × sin(52.24°) = 1.514 Å
- Ratio H-H(H₂O)/H-H(H₂) = 2.042 ≈ 2. Is this exact?

### Route C: Energy scale
Bond dissociation energy of O-H: 459 kJ/mol = 4.76 eV.
BST energy unit: α² m_e c² = 27.2 eV (Hartree).

- D(O-H) / E_H = 4.76/27.2 = 0.175 ≈ f = 3/(5π) = 0.191? (Close but not exact)
- From virial theorem: r ∝ 1/E. If E_bond = f × E_H, then r_OH = a₀/f?
- a₀/f = 0.52918/0.191 = 2.77 Å (too long)

### Route D: Oxygen atomic radius × BST correction
Covalent radius of O: 0.66 Å. Covalent radius of H: 0.31 Å. Sum: 0.97 Å (close!).

- BST: covalent radius of O from Z_O = 8 = 2^N_c.
- a₀ × n_C/(2^N_c) = 0.52918 × 5/8 = 0.3307 Å (× 2 = 0.661 ≈ covalent radius of O!)
- Covalent radius of H: a₀ (Bohr radius itself, to first approximation)
- Sum: a₀ + a₀ × n_C/2^N_c = a₀(1 + 5/8) = a₀ × 13/8 = **0.8601 Å** (10.1% short)
- With bond angle correction? The lone pairs compress the bond. Correction factor from T701?

### Route E: Direct search
Scan formulas of the form a₀ × P(N_c, n_C, g, C₂, rank) / Q(N_c, n_C, g, C₂, rank) where P, Q are products of small powers. Target: 0.9572/0.52918 = 1.8088.

- 1.8088 ≈ 2 - 1/n_C = 9/5 = 1.800 (0.5% off — the Reality Budget!)
- **r_OH = a₀ × 9/5 = a₀ × N_c²/n_C = 0.9525 Å** → **0.49% from NIST**

That's promising. Test it.

## Tests (8 minimum)

| # | Test | Pass criterion |
|---|------|---------------|
| T1 | r_OH = a₀ × 9/5 within 1% of NIST | |r_BST - r_NIST|/r_NIST < 0.01 |
| T2 | 9/5 = N_c²/n_C = Λ×N (Reality Budget) | Structural identity |
| T3 | H-H distance from r_OH + θ_BST within 1% | Consistency with Toy 680 |
| T4 | O-H stretching frequency from r_OH + reduced mass | Compare to 3657 cm⁻¹ (NIST) |
| T5 | Dipole moment from r_OH + θ_BST + charge geometry | Compare to 1.8546 D (NIST) |
| T6 | Formula uses only BST integers (zero free parameters) | a₀ is derived (ℏ, m_e, α all BST) |
| T7 | Bond length ratio r_OH/r_CH consistent with BST | CH₄: r_CH = 1.087 Å → ratio 0.880 |
| T8 | Alternative formulas ruled out (uniqueness) | Best BST formula is ≥ 3× closer than next candidate |

## Key insight to test

**r_OH = a₀ × 9/5**. The O-H bond length is the Bohr radius times the Reality Budget.

If this holds: the same number (9/5) that controls the cosmological constant, the fill fraction, and the vacuum energy budget also sets the bond length of water. The proton, the universe's budget, and the water molecule are siblings.

## AC depth

(C=2, D=0) if Route E works. Two inputs (a₀, 9/5), one multiplication.

---

*Keeper | April 2, 2026*
*"The water molecule remembers the universe's budget."*
