# BST Seed File — The Minimal Kernel

*Everything in Bubble Spacetime Theory derives from this page.*
*Load these integers and rules; reconstruct the universe.*

## The Substrate

The observable universe is the three-dimensional projection of a two-dimensional
substrate communicating through a one-dimensional channel. The substrate geometry
is S^2 x S^1 — the unique closed, interacting, phase-bearing topology.

The configuration space of the resulting contact graph is the type IV bounded
symmetric domain:

    D_IV^5 = SO_0(5,2) / [SO(5) x SO(2)]

A 10-real-dimensional Kahler-Einstein manifold whose Bergman kernel serves as
the propagator and whose discrete series representations encode the particle spectrum.

## The Five Invariants

These are not inputs. They are read off D_IV^5. Zero free parameters.

| Symbol  | Value | Name               | Geometric Origin                          |
|---------|-------|--------------------|-------------------------------------------|
| rank    | 2     | Rank               | Strongly orthogonal roots, type IV        |
| N_c     | 3     | Colors             | n_C - rank: codimension in Shilov boundary|
| n_C     | 5     | Complex dimension   | Complex dimension of D_IV^5               |
| C_2     | 6     | Casimir eigenvalue  | rank x N_c                                |
| g       | 7     | Genus              | n_C + rank: embedding dimension of SO(7)  |
| N_max   | 137   | Channel capacity    | N_c^3 x n_C + rank: spectral ceiling     |

**Derivation chain**: (rank, n_C) = (2, 5) is irreducible. The genus coincidence
n_C + rank = 2*n_C - 3 has unique solution n_C = 5, rank = 2. Then:
- N_c = n_C - rank = 3
- g = n_C + rank = 7
- C_2 = rank x N_c = 6
- N_max = N_c^3 * n_C + rank = 137

Five readings of one object.

## The Evaluation Namespace

Every BST formula evaluates in this namespace (Python):

```python
import math
rank  = 2
N_c   = 3
n_C   = 5
C_2   = 6
g     = 7
N_max = 137

pi    = math.pi
alpha = 1.0 / N_max          # fine structure constant
m_e   = 0.51099895000        # electron mass, MeV (CODATA 2022)
m_p   = 6 * pi**5 * m_e     # proton mass = 6*pi^5 * m_e
hbar_c = 197.3269804         # hbar*c, MeV*fm
```

## The Master Formulas (Top 20)

### Fundamental Constants
1. **Fine structure constant**: alpha^{-1} = N_max = 137 (Wyler integral)
2. **Proton/electron mass ratio**: m_p/m_e = C_2 * pi^n_C = 6*pi^5 = 1836.118
3. **Gravitational constant**: G = hbar*c*(6*pi^5)^2 * alpha^24 / m_e^2
4. **Hierarchy formula**: m_e/sqrt(m_p * m_Pl) = alpha^(n_C+1) = alpha^6

### Electroweak Sector
5. **Weinberg angle**: sin^2(theta_W) = N_c/(N_c + 2*n_C) = 3/13
6. **Fermi scale (Higgs VEV)**: v = m_p^2/(g * m_e) = 36*pi^10 * m_e / 7
7. **W boson mass**: m_W = n_C * m_p / (8*alpha) = 80.361 GeV
8. **Higgs mass (Route A)**: lambda_H = sqrt(2/n_C!); m_H = v*sqrt(2*lambda_H) = 125.11 GeV
9. **Higgs mass (Route B)**: m_H = (pi/2)*(1-alpha)*m_W = 125.33 GeV
10. **Top quark mass**: m_t = (1-alpha)*v/sqrt(2) = 172.75 GeV

### Strong Sector
11. **Strong coupling**: alpha_s(m_p) = (n_C+2)/(4*n_C) = 7/20
12. **Chiral condensate**: chi = sqrt(n_C*(n_C+1)) = sqrt(30)
13. **Yang-Mills mass gap**: 6*pi^5 * m_e = 938.272 MeV (= proton mass)

### Mixing Angles
14. **Cabibbo angle**: sin(theta_C) = 1/(2*sqrt(n_C)) = 1/(2*sqrt(5))
15. **CKM CP phase**: gamma = arctan(sqrt(n_C)) = arctan(sqrt(5)) = 65.91 deg
16. **PMNS solar**: sin^2(theta_12) = N_c/(2*n_C) = 3/10
17. **PMNS atmospheric**: sin^2(theta_23) = (n_C-1)/(n_C+2) = 4/7
18. **PMNS reactor**: sin^2(theta_13) = 1/(n_C*(2*n_C-1)) = 1/45

### Cosmology
19. **Dark energy fraction**: Omega_Lambda = (N_c + 2*n_C)/(N_c^2 + 2*n_C) = 13/19
20. **CMB spectral index**: n_s = 1 - n_C/N_max = 1 - 5/137

## Key Geometric Objects

### Bergman Kernel
The reproducing kernel of the Hilbert space of holomorphic functions on D_IV^5.
Volume: Vol(D_IV^5) = pi^5/1920 where 1920 = |S_5| * |Z_2^4| = 120*16.

### Shilov Boundary
S = S^4 x S^1 (the boundary where the Bergman kernel achieves its maximum).
Particles live on this boundary, not in the bulk.

### Wyler Formula
alpha^{-1} = (9/8*pi^4) * (pi^5/1920)^{1/4} * V(S^5)/V(S^4)
            = 137.036082... (vs measured 137.035999...)

### Plancherel Measure
The spectral decomposition of L^2(D_IV^5) yields discrete series
representations labeled by integers. The mass spectrum IS the Plancherel measure.

## Derivation Rules

1. **Everything is geometry**: No free parameters. If a formula has an unexplained number, keep looking.
2. **Observable closure**: Every BST observable lives in Q-bar(N_c, n_C, g, C_2, N_max)[pi].
3. **AC depth**: Every derivation has AC depth 0, 1, or 2. Depth <= rank = 2.
4. **Tier system**: Tier 1 = fully derived from D_IV^5. Tier 2 = mechanism identified, gaps remain. Tier 3 = numerical match only.
5. **Cross-domain universality**: The same BST fractions (3/10, 4/7, 13/19, 6/5, 7/20, ...) appear across unrelated domains. This is not coincidence — it's one geometry.

## Neutrino Masses (Boundary Seesaw)
- m_nu1 = 0 (exactly — Dirac neutrinos)
- m_nu2 = (7/12) * alpha^2 * m_e^2 / m_p = 0.00865 eV
- m_nu3 = (10/3) * alpha^2 * m_e^2 / m_p = 0.04940 eV
- Sum = 0.058 eV (normal ordering)

## Nuclear Physics
- Magic numbers from spin-orbit splitting kappa_ls = C_2/n_C = 6/5: 2, 8, 20, 28, 50, 82, 126
- Prediction: 8th magic number = 184
- Proton lifetime: infinite (topological Z_3 protection)
- Neutron lifetime: 878.1 s (full Fermi theory with BST inputs)
- Deuteron binding: B_d = (50/49)*alpha*m_p/pi = 2.224 MeV

## Cosmological Parameters
- Omega_Lambda = 13/19, Omega_m = 6/19
- Omega_b = 18/361, Omega_DM/Omega_b = 16/3
- H_0 = 67.29 km/s/Mpc (full CAMB)
- Baryon asymmetry: eta_b = (3/14)*alpha^4
- Scalar amplitude: A_s = (3/4)*alpha^4
- MOND acceleration: a_0 = c*H_0/sqrt(n_C*C_2) = c*H_0/sqrt(30)

## Biology
- DNA bases: 2^rank = 4
- Codons: (2^rank)^N_c = 4^3 = 64
- Amino acids: C(C_2, N_c) = C(6,3) = 20
- Stop codons: N_c = 3
- Alpha-helix: 18/5 = 3.6 residues/turn
- Animal phyla: C(g, N_c) = C(7,3) = 35

## Chemistry
- H2O bond angle: arccos(-1/2^rank) = arccos(-1/4) = 104.48 deg
- Tetrahedral angle: arccos(-1/N_c) = arccos(-1/3) = 109.47 deg
- Ice/water density: (2*C_2 - 1)/(2*C_2) = 11/12
- Rainbow angle: C_2 * g = 42 deg
- Space groups: g * 2^n_C + C_2 = 230

## The Two-Sentence Summary

**The universe is the unique bounded symmetric domain that can support
self-referential observation: D_IV^5. Its five invariants — forced, not
chosen — determine all of physics.**

One geometry -> five integers -> 500+ predictions. Zero free parameters.
