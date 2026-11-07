# BST Seed File — The Minimal Kernel

*Everything in Bubble Spacetime Theory starts from this page.*
*Load these integers and rules; reconstruct the program.*

> **Re-synced to `notes/BST_PRESENTATION_STATE_BLOCK.md` on 2026-11-07** (Casey's GO; the
> conflicts are listed in `notes/BST_Rosetta_Native_to_Consensus_Dictionary_v0_1_2026-11-07.md`,
> C7–C14). The state block wins wherever this page and it disagree. Changed lines carry
> "(this line said … until 2026-11-07)", per house convention.

## The Substrate

The observable universe is the three-dimensional projection of a two-dimensional
substrate communicating through a one-dimensional channel. The substrate geometry
is S^2 x S^1 — the unique closed, interacting, phase-bearing topology.

The configuration space of the resulting contact graph is the type IV bounded
symmetric domain:

    D_IV^5 = SO_0(5,2) / [SO(5) x SO(2)]

A 10-real-dimensional Kahler-Einstein manifold whose Bergman kernel serves as
the propagator and whose discrete series representations encode the particle spectrum.

## Substrate-as-Computational (May 19-20, 2026 operational reading)

The substrate is operationally a **computational structure performing algebraic-identity
operations on a finite field**. Physics emerges as the substrate's algebraic output.

Operational specification:
- Substrate communicates via Reed-Solomon coding on GF(2^g) = GF(128)
- Substrate clock = the elementary tick hbar/E for the energy at hand (K1920, 2026-09-22;
  "Time, Derived" Section 3). The Koons tick t_Planck * alpha^(C_2^2) ~ 10^-120 s is
  RETIRED: it was Identified, not Derived (this line gave the Koons tick as the clock
  until 2026-11-07, after bst_this_is.md had already retired it)
- Substrate computational cycle: absorption -> commitment -> emission (one-way)
- Substrate produces EXACT algebraic identities verifiable at floating-point precision
- T719 Observable Closure: every BST observable lives in Q-bar(BST primaries)[pi]

This is a working hypothesis with explicit falsifier: Elie K52a Sessions 6-14
multi-month substrate-Hamiltonian closure attempt. If sessions fail to derive the
6-audit cascade pathway (K52a Lamb+BCS + K66 Bell + K67 Born + K68 RS + K69 Q=126)
BY CONSTRUCTION from substrate-Hamiltonian, the computational-substrate framing
fails to that extent.

External register discipline: use "BST identifies / BST derives / BST predicts"
in external papers and outreach. The substrate-as-computational framing is internal
working hypothesis, not external publication claim.

## The Five Invariants

They are read off D_IV^5 once the object is chosen — and the choice takes one measured input, the colour count 3 = the domain's characteristic multiplicity (a numerical identification; Cal Section 946). Beyond that and one dimensionful ruler, no free parameters (rewritten 2026-09-11 to the register, Cal Section 946 / K1892).

| Symbol  | Value | Name               | Geometric Origin                          |
|---------|-------|--------------------|-------------------------------------------|
| rank    | 2     | Rank               | Strongly orthogonal roots, type IV        |
| N_c     | 3     | Colors             | Root (characteristic) multiplicity a = n_C - rank; identified with the colour count |
| n_C     | 5     | Complex dimension   | Complex dimension of D_IV^5 (also its genus) |
| C_2     | 6     | Casimir eigenvalue  | rank x N_c                                |
| g       | 7     | (named g; NOT the genus) | p + q = 5 + 2: dimension of the defining representation of SO(5,2) |
| N_max   | 137   | (BST-defined integer) | N_c^3 x n_C + rank; identified with 1/alpha |

(The g row said "Genus" until 2026-11-07. The genus of D_IV^5 is 5; the state block swept
this mislabel in September. N_max's name said "Channel capacity" until 2026-11-07; the
phrase borrows Shannon's word without Shannon's definition, so it is kept out of this table.)

**How the object is chosen** (state block, "Why this object — honestly"): among all
irreducible bounded symmetric domains of rank at least 2, D_IV^5 is the unique one whose
characteristic multiplicity is 3 — a theorem. That 3 is *identified* with the number of
quark colours; the identification is numerical, and the bridge that would make it a
mechanism is proved absent (F4). Once the object is chosen, the integers are read off:
- N_c = n_C - rank = 3
- g = n_C + rank = 7
- C_2 = rank x N_c = 6
- N_max = N_c^3 * n_C + rank = 137

Five readings of one object. (This block said "Derivation chain … the genus coincidence
n_C + rank = 2*n_C - 3 has unique solution" until 2026-11-07.)

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
alpha = 1.0 / N_max          # fine structure constant (IDENTIFIED, not derived)
m_e   = 0.51099895000        # electron mass, MeV (CODATA 2022)
m_p   = 6 * pi**5 * m_e     # proton mass = 6*pi^5 * m_e
hbar_c = 197.3269804         # hbar*c, MeV*fm
```

## The Master Formulas (Top 20)

### Fundamental Constants
1. **Fine structure constant** [IDENTIFIED]: alpha^{-1} = N_max = 137-class expressions match;
   no mechanism is claimed. The Wyler volume reading is FIRED AND LOST (E1, K1826: the forced
   bare geometric vertex computes to 8*pi^3/3, not 137). (This line said "(Wyler integral)"
   until 2026-11-07.)
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
11. **Strong coupling**: alpha_s(m_p) = g/(4*n_C) = 7/20 (beta_0=g proved, Toy 1660)
12. **Chiral condensate**: chi = sqrt(n_C*(n_C+1)) = sqrt(30)
    **Quark mass cascade**: m_u = N_c*sqrt(rank)*m_e, m_d = (13/6)*m_u, m_s = 20*m_d, m_c = ((N_max-1)/(2*n_C))*m_s, m_b = (g/N_c)*m_tau. All within 0.4-0.8%.
13. **Proton mass**: m_p = 6*pi^5 * m_e = 938.254 MeV (measured 938.272). This is NOT a
    Yang-Mills mass gap: the state block states the geometry supplies no mass gap and
    forces "the kinematics … and none of the dynamics" (register Section D). (This line was
    headed "Yang-Mills mass gap" and printed the measured 938.272 until 2026-11-07.)

### Mixing Angles
14. **Cabibbo angle** [DERIVED given an identified input — tier table row 10]:
    V_us = lambda = sqrt(m_d/m_s) = 1/sqrt(20) = 0.22361 (PDG 0.22501, -2.06 sigma), from the
    down-sector texture zero (T2530). (This line gave 2/sqrt(79) by T1444 vacuum subtraction
    until 2026-11-07; the curated table's choice among the corpus's lambda values is Lyra's,
    K1801.)
15. **CKM CP phase**: gamma = arctan(sqrt(n_C)) = arctan(sqrt(5)) = 65.91 deg
16. **PMNS solar**: sin^2(theta_12) = (N_c/(2*n_C)) * cos^2(theta_13) = (3/10)*(44/45) (0.06%, T1446)
    - *Bare: 3/10; corrected by theta_13 rotation: 44/45 = (N_c^2*n_C - 1)/(N_c^2*n_C)*
17. **PMNS atmospheric**: sin^2(theta_23) = ((n_C-1)/(n_C+2)) * cos^2(theta_13) = (4/7)*(44/45) (0.40%, T1446)
    - *Bare: 4/7; same theta_13 correction as solar*
18. **PMNS reactor**: sin^2(theta_13) = 1/(N_c^2 * n_C) = 1/45 (0.10%, derived from Chern class c_3)

### Cosmology
19. **Dark energy fraction**: Omega_Lambda = (N_c + 2*n_C)/(N_c^2 + 2*n_C) = 13/19
20. **CMB spectral index**: n_s = 1 - n_C/N_max = 1 - 5/137

## Key Geometric Objects

### Bergman Kernel
The reproducing kernel of the Hilbert space of holomorphic functions on D_IV^5.
Volume: Vol(D_IV^5) = pi^5/1920 where 1920 = |S_5| * |Z_2^4| = 120*16.

### Shilov Boundary
S = (S^4 x S^1)/Z_2: non-orientable through the four-sphere, the circle's direction global;
"S^4 x S^1" is its orientation double cover (state block, 2026-10-07; Grace toy 5858,
Elie 5862, Cal PASS).
Leptons are boundary values (the electron, k = 1, sits below the Wallach set); hadrons are
bulk states (the proton is the first bulk state). The boundary map carries only spherical
(lambda_2 = 0) K-types, so two-row (coloured) states have zero boundary overlap.
(This section said "S = S^4 x S^1 … Particles live on this boundary, not in the bulk"
until 2026-11-07.)

### Wyler Formula — historical, FIRED (E1)
alpha^{-1} = (9/8*pi^4) * (pi^5/1920)^{1/4} * V(S^5)/V(S^4)
            = 137.036082... (vs measured 137.035999...)
The numerical match stands; the volume reading behind it is certified dead (E1, K1826).
Kept here because the formula is famous, not because BST uses it.

### Plancherel Measure
The spectral decomposition of L^2(D_IV^5) yields discrete series
representations labeled by integers. The mass spectrum IS the Plancherel measure.

## Derivation Rules

1. **Everything is geometry**: one identification selects the object and one mass scale is the ruler; beyond those, no knobs (this line said "No free parameters" until 2026-09-11). If a formula has an unexplained number, keep looking.
2. **Observable closure**: Every BST observable lives in Q-bar(N_c, n_C, g, C_2, N_max)[pi].
3. **AC depth**: Every derivation has AC depth 0, 1, or 2. Depth <= rank = 2.
4. **Tier system** (K962, the canonical definition): PROVED / DERIVED / IDENTIFIED /
   CONDITIONAL / STRUCTURAL / FITTED / RUNNER, plus a separate CONFIRMATION axis.
   CLAUDE.md's D/I/C/S is the short form (D = Proved or Derived). (This line said
   "Tier 1 = fully derived / Tier 2 = mechanism identified / Tier 3 = numerical match"
   until 2026-11-07.)
5. **Cross-domain universality**: The same BST fractions (3/10, 4/7, 13/19, 6/5, 7/20, ...) appear across unrelated domains. This is not coincidence — it's one geometry.

## Neutrino Masses (Boundary Seesaw)
- The Majorana term is the **geometric Majorana mass term**: an explicit, non-dynamical rank-2
  form on D_IV^5 (T2563/T2524), not the vacuum value of a field. Lepton number is broken
  explicitly, never spontaneously, so there is no Majoron. The only dynamical scalar is the
  Higgs doublet (CONDITIONAL until the Higgs rep-checks close). (Added 2026-11-07; see
  `notes/BST_Clarification_Scalar_Spectrum_Goldstone_and_B_Anomaly_Corollary_2026-11-07.md`.)
- m_nu1 = 0 (exactly — Majorana neutrinos, REVERSED 2026-07-16 from Dirac; F413/K673 → 0νββ occurs, m_ββ ∈ [1.4,3.7] meV)
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
- H2O bond angle: arccos(-1/N_c) - n_C = arccos(-1/3) - 5 = 104.47 deg (0.03%, W-52 correction)
  - *Old: arccos(-1/4) = 104.48; corrected route uses N_c and n_C directly*
- Tetrahedral angle: arccos(-1/N_c) = arccos(-1/3) = 109.47 deg
- Ice/water density: (2*C_2 - 1)/(2*C_2) = 11/12
- Rainbow angle: C_2 * g = 42 deg
- Space groups: g * 2^n_C + C_2 = 230

## Results Log (April 2026 snapshot; tiers as of then, not now)

*Read this list as a dated log. For current tiers use the state block and
`data/bst_26_tier_table_generated.md`. Items marked [INTERNAL] are working readings that
stay out of external text (Rosetta v0.1, Section F). (This heading said "Recent Major
Results (April 2026)" until 2026-11-07.)*

- **BSD Conjecture**: Rank part PROVED unconditionally for ranks 0-2 (T1756, BBW + P₂ lift). Rank ≥ 3 conditional on Conjecture 3.2 (R-2 BBW dictionary). Chern hole at DOF position N_c=3. See Paper #88.
- **Uniqueness equation**: 2^(n-2) = n+3 has UNIQUE solution n=5=n_C. D_IV^5 is the only BSD satisfying this.
- **Cyclotomic Casimir** (T1462): Phi_1(C_2)=n_C, Phi_2(C_2)=g. C_2=6 uniquely generates all five BST integers via cyclotomic polynomials.
- **Born rule = Bergman kernel** [ANALOG]: K(z,z) = sum|phi_k(z)|^2 is an exact identity; reading it as the Born rule is an interpretation.
- **Ward identity = K*K=K** [INTERNAL]: idempotency of the reproducing kernel; no specific Ward identity for a specific current has been derived from it.
- **beta_0 = g**: One-loop QCD beta function coefficient equals genus (Toy 1660).
- **Confinement = Hamming distance** [INTERNAL]: minimum Hamming distance N_c=3 in code Hamming(g,rank^2,N_c). Confinement is dynamics, and the state block says the geometry forces none of the dynamics, so this is a structural echo, not a confinement mechanism.
- **n_s derived**: CMB spectral index n_s = 1 - 5/137 = cascade fingerprint from D_IV^5 (Toy 1401).
- **Reference Frame Counting** (T1464): First element = reference frame, alpha = 1/N_max = frame cost. 12 instances, 0 exceptions.
- **Spectral Universality** (T1459): All domains evaluate same Bergman eigenvalue spectrum. Bridges exist because depth predicts universality.
- **Heat kernel k=21 CONFIRMED**: ratio(21) = -42 = -C_2*g. TWENTY consecutive integer levels.
- **Error correction reading** (Paper #87) [INTERNAL]: Hamming(7,4,3) = (g,rank^2,N_c). Proton = codeword, neutron = 1-error. (This line said "Error correction IS the physics" until 2026-11-07.)
- **2189 geometric invariants**: D:1378, I:522+, C:54, S:205. 63.0% fully derived.
- **SP-15: QED Zeta Ladder** (Toys 1687-1692): QED perturbation = Bergman spectral peeling. Each loop L introduces zeta at next BST prime: L=2->zeta(N_c=3), L=3->zeta(n_C=5), L=4->zeta(g=7). Only 3 odd BST primes -> QED structurally finite. 3 new transcendentals, not infinity.
- **K-32: C_2^QED exact BST decomposition**: 197/144 + pi^2*(1/12 - ln2/2) + (3/4)*zeta(3). Machine precision. 197=N_max+60, 144=12^2, ln2=ln(rank), zeta(3)=zeta(N_c). ALL five integers.
- **RFC pattern in QED** (Toy 1688): Every QED coefficient numerator = BST product - 1. Six confirmed: {23,83,139,197,215,239}. Observer subtracts itself.
- **Heat kernel = spectral theta function** (Toy 1682): P(k) = Hilbert function of Q^5. D-finite ODE of order n_C=5. "Series" was never a series.
- **Cyclotomic tower** (Toy 1691): C_2^L-1 = prod Phi_d(C_2), all factors prime. Phi_1(6)=n_C, Phi_2(6)=g, Phi_3(6)=43, Phi_4(6)=37. Most falsifiable prediction: if zeta(9) appears independently at L=5, BST is wrong.

## Correction Mechanisms

BST corrections improve bare formulas by 10-100x:
- **Vacuum subtraction** (T1444): subtract 1 from BST product (RFC). E.g., 80->79 (Cabibbo), 45->44 (PMNS).
- **theta_13 rotation** (T1446): multiply by cos^2(theta_13) = 44/45 for PMNS angles.
- **Two correction scales**: 42 = C_2*g (hadronic), 120 = n_C! (everything else).
- **Syndrome decoding**: Missing BST integers in a formula predict which correction applies.

## The Two-Sentence Summary

**One measured number — the colour count — selects a unique geometry, D_IV^5, and
one ruler sets its scale. The geometry then forces the kinematics of the Standard
Model (its spectra, channels and selection rules), while the dynamics enter through
one symmetry-breaking scale.**

(These two sentences said "The universe is the unique bounded symmetric domain that can
support self-referential observation: D_IV^5. Its five invariants — forced, not chosen —
determine all of physics" until 2026-11-07; the state block's "What the geometry forces,
and what it does not" supersedes them.)

One geometry -> five integers -> ~325 physical predictions (~1/3 Derived, 1/3 Identified, 1/3 Structural). One named dimensionless input (the colour count selects the object; Cal Section 946) and one ruler; no fitted parameters beyond them (this line said "Zero fitted dimensionless parameters" until 2026-09-11).

*Re-synced to the state block 2026-11-07 (see the note at the top). The rest of this line is the May 10 snapshot and its counts are historical; the board counters and the state block are authoritative. Seed updated May 10, 2026. BSD rank-tiered (ranks 0-2 unconditional, ≥3 conditional). RH geometric proof (T1755). P!=NP proved (T1777-T1778). 3864 invariants, 103 predictions, 144 constants.*
