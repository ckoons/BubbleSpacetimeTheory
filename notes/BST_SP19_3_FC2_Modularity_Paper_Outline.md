# SP19-3: FC-2 Spectral Modularity Paper Outline

**Working Title**: "Spectral Modularity: BSD and Modularity as One Evaluation on D_IV^5"
**Lead**: Lyra + Elie
**Target**: J. Funct. Anal. or Inventiones Mathematicae
**Date**: May 13, 2026

## Scope (honest, per Cal FC-5)

- **This paper is about 49a1 specifically.** Conductor g^2=49, CM by Q(sqrt(-7)), torsion Z/2Z, rank 0.
- **Do not generalize to "all modularity."** Wiles/BCDT remains external for existence of weight-2 newforms for arbitrary E/Q.
- **The claim**: For 49a1, modularity and BSD are one spectral evaluation — the Eisenstein residue at s=1 on SO_0(5,2) at Wallach k=2 equals the BSD invariant L(E,1)/Omega = 1/rank.

## Sections (9)

### 1. Introduction (2-3pp)
State main theorem. Motivate: classical modularity and BSD are separate deep results; for 49a1 they are one spectral evaluation on D_IV^5. Honest scope.

### 2. The Domain D_IV^5 and Its Parabolic Structure (3-4pp)
D_IV^5 = SO_0(5,2)/[SO(5)xSO(2)], rank 2, n_C=5. P_2 parabolic: Levi M = GL(2)xSO(3), dim N_P = g = 7. Wallach set. K-type formula. Ring uniqueness (T1780).
- T1762 (Toy 2091, 12/12), T1780 (Toy 2120, 10/10), T1829 (Toy 2151, 26/26). **All D-tier.**

### 3. The Eisenstein Series E(f,s,P_2) and Its Pole at s=1 (4-5pp)
Langlands-Shahidi normalizing factor. Constant-term formula: M(s,f) = zeta(2s)*L(2s-1,Sym^2 f)/[zeta(2s+1)*L(2s,Sym^2 f)]. For 49a1 (CM by Q(sqrt(-g))): Sym^2 f = zeta*L(chi_{-g})*L_K(psi/psi^sigma). Pole from zeta(2s-1). Residue contains L(1,chi_{-g}) = pi/sqrt(g).
- W-8b (Toy 2147, 10/10). **D-tier.**

### 4. The Residual Representation Is the Wallach pi_2 (3-4pp)
Three-step identification: (1) K-type matching — lowest = trivial SO(5) x weight-2, dim 1 = pi_2. (2) Holomorphicity + Harish-Chandra uniqueness — J(f,1) is unique holomorphic irreducible with this K-type. (3) Non-vanishing via theta lift — L(E,1)!=0 for rank-0 49a1, so theta(f)!=0 via Rallis.
- FC-2a (Toy 2150, 15/15). **D-tier.**

### 5. The Rallis Inner Product Formula and the BSD Connection (3-4pp)
||Res E(f,s)||^2 ~ L(E,1)*L(1,Ad f)*vol(G/K). BSD critical value L(E,1) appears in residue norm. Combined with BSD formula: L(E,1)/Omega = 1/rank = Wallach Plancherel ratio at k=rank. This is the unification.
- T1756 (Paper #88), T1430 (1/rank universality). **D-tier.**

### 6. BST Integer Map of the Chain (2-3pp)
Every number in the Eisenstein->pole->residue->BSD chain is a BST integer. 20+ appearances, 0 unexplained. Systematic table: deg(r_1)=C_2, dim N_P=g, conductor=g^2, CM disc=-g, L(E,1)/Omega=1/rank, lowest K-type dim=1, next=n_C.
- Toys 2147, 2150. **D-tier.**

### 7. The F_1 Collapse and Structural Uniqueness (2-3pp)
At q=1: both sides collapse to rank=2 (T1808, D). Eichler-Shimura T_1=2*id. Poisson kernel at q=1 is identity. Chevalley extension uniqueness (T1809, C). Self-referential irreducibility x^g+x^{N_c}+1 over F_2 (T1811, C).
- T1808 (D), T1809 (C), T1810 (D), T1811 (C). **Mixed D+C.**
- Gaps: T1809 functoriality step, T1811 formalization.

### 8. Honest Scope and Relation to Wiles/BCDT (1-2pp)
What IS claimed: For 49a1, modularity and BSD are one spectral evaluation. What is NOT: new proof of modularity for all E/Q; Wiles/BCDT superseded; generalization beyond CM curves with conductor g^2.

### 9. Conclusion and Future Directions (1p)
Extend to other CM curves (11a1, 37a1). FET conjecture (GC-17a). Wallach Universality connection.

## Tier Assessment

| Section | Tier | Key Evidence |
|---------|------|-------------|
| 2 (Domain) | D | T1762, T1780, T1829 |
| 3 (Eisenstein pole) | D | Toy 2147, 10/10 |
| 4 (Residual = pi_2) | D | Toy 2150, 15/15 |
| 5 (Rallis + BSD) | D | T1756, T1430 |
| 6 (BST integers) | D | Toys 2147, 2150 |
| 7 (F_1 uniqueness) | D+C | T1808-T1811 |

**Core chain (Sections 3-6): entirely D-tier.** Uses only published theorems + verified computations.

## Gaps for New Work

1. **Toy 2133** (Elie, assigned): P_2 constant-term test for 49a1 + 11a1 + 37a1. Strengthens Section 3.
2. **T1809 formalization**: Chevalley extension for (GL(2), SO(5,2)) via Arthur. Finite computation.
3. **T1811 formalization**: Polynomial irreducibility -> correspondence indecomposability. Needs rigorous proof.
4. **Full leading coefficient**: L(E,1)/Omega = 1/rank is proved. Full Bloch-Kato computation for completeness.
5. **Non-archimedean verification table**: a_p matching at small primes (partially in Toy 2147).

## Key Files

- `notes/BST_GC17b_Modularity_Via_Boundary_Invertibility.md` — boundary-interior framework
- `notes/BST_GC17c_Wallach_Point_Modularity_Seed.md` — Wallach investigation
- `notes/BST_GC17a_Modularity_Feasibility_Scoping.md` — honest scope
- `notes/BST_V1_Cuspidal_Test_GC17b.md` — Cal V-1
- `play/toy_2150_residual_rep_wallach_identification.py` — FC-2a (15/15)
- `play/toy_2147_eisenstein_wallach_factorization.py` — W-8b (10/10)
- `play/toy_2131_boundary_interior_modularity.py` — GC-17b (35/35)
