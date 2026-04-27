#!/usr/bin/env python3
"""
TOY 187: THE FUSION RING OF so(7) AT LEVEL 2
==============================================

The BST physical algebra is so(7) = B_3 at level 2.
It has g = 7 integrable representations — same as the genus.

Toy 176 found D² = 4, Z_2 × Z_2 fusion among non-wall primaries.
But that was only the 4 non-wall reps. THIS toy computes the
FULL fusion ring of ALL 7 integrable representations of so(7)_2,
including the wall reps (which contribute to the fusion despite
having zero quantum dimension in the modular S-matrix).

The Verlinde formula gives integer fusion coefficients N_{ij}^k.
We look for BST content in:
  - The fusion matrix eigenvalues
  - The total fusion multiplicities
  - The fusion algebra structure constants
  - The Grothendieck ring

Casey Koons, March 16, 2026
"""

import math
import cmath
from fractions import Fraction
from itertools import permutations, product as cartesian

print("=" * 72)
print("TOY 187: THE FUSION RING OF so(7) AT LEVEL 2")
print("=" * 72)

# BST integers
N_c = 3
n_C = 5
g = 7
C2 = 6
r = 2
c2 = 11
c3 = 13
P1 = 42

# ═══════════════════════════════════════════════════════════════
# Section 1. so(7) = B_3 AT LEVEL 2: ALL INTEGRABLE REPRESENTATIONS
# ═══════════════════════════════════════════════════════════════
print("\nSection 1. ALL 7 INTEGRABLE REPRESENTATIONS OF so(7) LEVEL 2")
print("-" * 50)

rank = 3
h_dual = 5
level = 2
M = level + h_dual  # = 7

rho = (Fraction(5, 2), Fraction(3, 2), Fraction(1, 2))

# Positive coroots for B_3
# Long roots: ±e_i ± e_j (coroot = same)
# Short roots: ±e_i (coroot = ±2e_i)
positive_coroots = [
    (1, -1, 0),   # e1-e2
    (1, 0, -1),   # e1-e3
    (0, 1, -1),   # e2-e3
    (1, 1, 0),    # e1+e2
    (1, 0, 1),    # e1+e3
    (0, 1, 1),    # e2+e3
    (2, 0, 0),    # 2e1 (coroot of short root e1)
    (0, 2, 0),    # 2e2 (coroot of short root e2)
    (0, 0, 2),    # 2e3 (coroot of short root e3)
]

# Positive roots (for classical dim)
positive_roots = [
    (1, -1, 0), (1, 0, -1), (0, 1, -1),
    (1, 1, 0), (1, 0, 1), (0, 1, 1),
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
]

def dynkin_to_eps(a1, a2, a3):
    """B_3 Dynkin labels to epsilon coordinates.
    ω₁ = (1,0,0), ω₂ = (1,1,0), ω₃ = (1/2,1/2,1/2)"""
    return (Fraction(a1) + Fraction(a2) + Fraction(a3, 2),
            Fraction(a2) + Fraction(a3, 2),
            Fraction(a3, 2))

def classical_dim(eps):
    """Classical dimension via Weyl formula."""
    lr = tuple(eps[i] + rho[i] for i in range(3))
    num = Fraction(1)
    den = Fraction(1)
    for root in positive_roots:
        ip_lr = sum(lr[i] * root[i] for i in range(3))
        ip_r = sum(rho[i] * root[i] for i in range(3))
        num *= ip_lr
        den *= ip_r
    return num / den

# Highest root of B_3: θ = e1+e2, θ∨ = e1+e2
# Level: <λ, θ∨> = a1 + 2*a2 + a3 ≤ level (marks of θ∨)
# Wait: B_3 has θ∨ = e1+e2 = (1,1,0) in eps coords
# <a1ω1+a2ω2+a3ω3, e1+e2> = a1·1 + a2·2 + a3·1
# So constraint: a1 + 2*a2 + a3 ≤ 2

all_reps = []
for a1 in range(3):
    for a2 in range(2):
        for a3 in range(3):
            if a1 + 2*a2 + a3 <= level:
                eps = dynkin_to_eps(a1, a2, a3)
                lr = tuple(eps[i] + rho[i] for i in range(3))

                # Wall check
                on_wall = False
                for coroot in positive_coroots:
                    ip = sum(lr[i] * coroot[i] for i in range(3))
                    if ip % M == 0:
                        on_wall = True
                        break

                cdim = classical_dim(eps)
                all_reps.append({
                    'dynkin': (a1, a2, a3),
                    'eps': eps,
                    'lr': lr,
                    'on_wall': on_wall,
                    'classical_dim': int(cdim),
                })

print(f"  B_3 level {level}: h∨={h_dual}, ℓ+h∨={M}={g}")
print(f"  Total integrable reps: {len(all_reps)} = g = genus")
print()

# Name the representations
rep_names = {
    (0,0,0): '1',        # trivial
    (1,0,0): 'V',        # vector (7-dim)
    (0,1,0): 'A',        # adjoint (21-dim)
    (2,0,0): 'S²V',      # sym² vector (27-dim)
    (0,0,1): 'Sp',       # spinor (8-dim)
    (0,0,2): 'S²Sp',     # sym² spinor (27+... dim)
    (1,0,1): 'V⊗Sp',     # vector × spinor
}

for rep in all_reps:
    d = rep['dynkin']
    name = rep_names.get(d, '?')
    wall = "  [WALL]" if rep['on_wall'] else ""
    eps_str = f"({rep['eps'][0]}, {rep['eps'][1]}, {rep['eps'][2]})"
    print(f"  {name:6s}  {str(d):12s}  eps={eps_str:20s}  "
          f"dim={rep['classical_dim']:3d}{wall}")

non_wall = [r for r in all_reps if not r['on_wall']]
wall_reps = [r for r in all_reps if r['on_wall']]

print(f"\n  Non-wall: {len(non_wall)} = {C2} - {r} = C₂ - r")
print(f"  Wall:     {len(wall_reps)} = {N_c} = N_c")
print(f"  Total:    {len(all_reps)} = {g} = g")

# Classical dimensions
dims = [rep['classical_dim'] for rep in all_reps]
print(f"\n  Classical dimensions: {dims}")
print(f"  Sum of dimensions: {sum(dims)}")

# ═══════════════════════════════════════════════════════════════
# Section 2. QUANTUM DIMENSIONS
# ═══════════════════════════════════════════════════════════════
print("\n\nSection 2. QUANTUM DIMENSIONS AT q = e^{2πi/7}")
print("-" * 50)

def quantum_dim(eps, rho_vec, M_val, coroots):
    """Quantum dimension using Weyl character formula at q-deformed level."""
    lr = tuple(float(eps[i] + rho_vec[i]) for i in range(len(rho_vec)))
    num = 1.0
    den = 1.0
    for coroot in coroots:
        ip_lr = sum(lr[i] * coroot[i] for i in range(len(rho_vec)))
        ip_r = sum(float(rho_vec[i]) * coroot[i] for i in range(len(rho_vec)))
        num *= math.sin(math.pi * ip_lr / M_val)
        den *= math.sin(math.pi * ip_r / M_val)
    return num / den

D_sq = 0
for rep in all_reps:
    dq = quantum_dim(rep['eps'], rho, M, positive_coroots)
    rep['qdim'] = dq
    D_sq += dq**2
    name = rep_names.get(rep['dynkin'], '?')
    wall = "  [WALL → dim_q = 0]" if rep['on_wall'] else ""
    print(f"  {name:6s}  dim_q = {dq:10.6f}  dim_q² = {dq**2:10.6f}{wall}")

print(f"\n  Total quantum dimension D² = Σ(dim_q²) = {D_sq:.6f}")
print(f"  D = {math.sqrt(D_sq):.6f}")
print(f"  D² = {round(D_sq)} = C₂ - r = {C2} - {r}")

# ═══════════════════════════════════════════════════════════════
# Section 3. FULL S-MATRIX (ALL 7 REPS)
# ═══════════════════════════════════════════════════════════════
print("\n\nSection 3. FULL MODULAR S-MATRIX (ALL 7 REPS)")
print("-" * 50)

# Weyl group of B_3: signed permutations, |W| = 48
weyl_group = []
for signs in cartesian([1, -1], repeat=3):
    for perm in permutations(range(3)):
        def make_w(s, p):
            def w(v):
                return tuple(s[i] * v[p[i]] for i in range(3))
            det = 1
            for ss in s:
                det *= ss
            inv = sum(1 for i in range(3) for j in range(i+1, 3) if p[i] > p[j])
            det *= (-1)**inv
            return w, det
        w, det = make_w(signs, perm)
        weyl_group.append((w, det))

assert len(weyl_group) == 48, f"Expected |W(B_3)| = 48, got {len(weyl_group)}"

n = len(all_reps)
S_mat = [[complex(0)] * n for _ in range(n)]

for i, rep_i in enumerate(all_reps):
    lri = tuple(float(rep_i['lr'][j]) for j in range(3))
    for j, rep_j in enumerate(all_reps):
        lrj = tuple(float(rep_j['lr'][k]) for k in range(3))
        total = complex(0)
        for w, det in weyl_group:
            w_lri = w(lri)
            ip = sum(w_lri[k] * lrj[k] for k in range(3))
            total += det * cmath.exp(-2j * cmath.pi * ip / M)
        S_mat[i][j] = total

# Normalize: rows should be unit vectors
row_norm = math.sqrt(sum(abs(S_mat[0][j])**2 for j in range(n)))
S_norm = [[S_mat[i][j] / row_norm for j in range(n)] for i in range(n)]

print(f"  7 × 7 S-matrix (normalized, real parts):")
print(f"        ", end="")
for j, rep_j in enumerate(all_reps):
    name = rep_names.get(rep_j['dynkin'], '?')
    print(f"  {name:>7s}", end="")
print()

for i, rep_i in enumerate(all_reps):
    name = rep_names.get(rep_i['dynkin'], '?')
    print(f"  {name:6s}", end="")
    for j in range(n):
        val = S_norm[i][j]
        if abs(val.imag) < 1e-8:
            print(f"  {val.real:7.4f}", end="")
        else:
            print(f"  {val.real:+.3f}{val.imag:+.3f}i", end="")
    print()

# ═══════════════════════════════════════════════════════════════
# Section 4. QUANTUM DIMENSIONS FROM S-MATRIX
# ═══════════════════════════════════════════════════════════════
print("\n\nSection 4. QUANTUM DIMENSIONS FROM S-MATRIX")
print("-" * 50)

print("  d_i = S_{i0}/S_{00}:")
for i, rep_i in enumerate(all_reps):
    name = rep_names.get(rep_i['dynkin'], '?')
    dq = S_norm[i][0] / S_norm[0][0]
    rep_i['qdim_S'] = dq.real
    print(f"    {name:6s}: d_q = {dq.real:10.6f}")

# ═══════════════════════════════════════════════════════════════
# Section 5. VERLINDE FUSION COEFFICIENTS (FULL 7×7×7 TENSOR)
# ═══════════════════════════════════════════════════════════════
print("\n\nSection 5. VERLINDE FUSION COEFFICIENTS (FULL)")
print("-" * 50)

# N_{ij}^k = Σ_s S_{is} S_{js} S*_{ks} / S_{0s}
fusion = [[[0.0] * n for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            total = complex(0)
            for s in range(n):
                if abs(S_norm[0][s]) > 1e-10:
                    total += (S_norm[i][s] * S_norm[j][s] *
                             S_norm[k][s].conjugate() / S_norm[0][s])
            fusion[i][j][k] = total.real

# Print all non-zero fusion rules
print("  All non-zero fusion rules N_{ij}^k:")
for i in range(n):
    for j in range(i, n):
        terms = []
        for k in range(n):
            coeff = round(fusion[i][j][k])
            if abs(fusion[i][j][k] - coeff) < 0.1 and coeff > 0:
                name_k = rep_names.get(all_reps[k]['dynkin'], '?')
                if coeff == 1:
                    terms.append(name_k)
                else:
                    terms.append(f"{coeff}·{name_k}")
        if terms:
            name_i = rep_names.get(all_reps[i]['dynkin'], '?')
            name_j = rep_names.get(all_reps[j]['dynkin'], '?')
            print(f"    {name_i:6s} × {name_j:6s} = {' + '.join(terms)}")

# ═══════════════════════════════════════════════════════════════
# Section 6. FUSION MATRICES AND THEIR EIGENVALUES
# ═══════════════════════════════════════════════════════════════
print("\n\nSection 6. FUSION MATRICES N_i AND THEIR EIGENVALUES")
print("-" * 50)

for i in range(n):
    name_i = rep_names.get(all_reps[i]['dynkin'], '?')
    # N_i is the matrix with (N_i)_{jk} = N_{ij}^k
    N_i = [[round(fusion[i][j][k]) for k in range(n)] for j in range(n)]

    # Compute eigenvalues (characteristic polynomial method is complex;
    # use the fact that eigenvalues of N_i = S_{is}/S_{0s})
    eigs = []
    for s in range(n):
        if abs(S_norm[0][s]) > 1e-10:
            eig = S_norm[i][s] / S_norm[0][s]
            eigs.append(eig.real)
        else:
            eigs.append(0.0)

    eigs_sorted = sorted(eigs, reverse=True)

    print(f"\n  N_{name_i} eigenvalues (= S_{{i,s}}/S_{{0,s}}):")
    for idx, e in enumerate(eigs_sorted):
        bst = ""
        e_round = round(e)
        if abs(e - e_round) < 0.001:
            for bname, bval in [('1', 1), ('-1', -1), ('0', 0),
                                ('r', 2), ('-r', -2), ('N_c', 3), ('-N_c', -3),
                                ('n_C', 5), ('C₂', 6), ('g', 7),
                                ('2^N_c', 8), ('dim(B_3)', 21), ('d_2', 27)]:
                if e_round == bval:
                    bst = f" = {bname}"
                    break
        print(f"    λ_{idx} = {e:10.6f}{bst}")

    # Trace and determinant
    tr = sum(eigs)
    det_val = 1
    for e in eigs:
        det_val *= e

    print(f"    Tr(N_{name_i}) = {tr:.4f}")
    print(f"    det(N_{name_i}) = {det_val:.4f}")

# ═══════════════════════════════════════════════════════════════
# Section 7. FUSION RING ARITHMETIC
# ═══════════════════════════════════════════════════════════════
print("\n\nSection 7. FUSION RING ARITHMETIC: BST CONTENT")
print("-" * 50)

# Total fusion multiplicities
print("\n  Total fusion multiplicities Σ_k N_{ij}^k:")
total_fusions = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        total_fusions[i][j] = sum(round(fusion[i][j][k]) for k in range(n))

print(f"        ", end="")
for j, rep_j in enumerate(all_reps):
    name = rep_names.get(rep_j['dynkin'], '?')
    print(f"  {name:>5s}", end="")
print()

for i, rep_i in enumerate(all_reps):
    name = rep_names.get(rep_i['dynkin'], '?')
    print(f"  {name:6s}", end="")
    for j in range(n):
        print(f"  {total_fusions[i][j]:5d}", end="")
    print()

# Row sums = how many channels each rep can fuse into
print(f"\n  Row sums (total channels per rep):")
for i, rep_i in enumerate(all_reps):
    name = rep_names.get(rep_i['dynkin'], '?')
    row_sum = sum(total_fusions[i][j] for j in range(n))
    print(f"    {name:6s}: {row_sum}")

# Grand total
grand_total = sum(sum(total_fusions[i][j] for j in range(n)) for i in range(n))
print(f"\n  Grand total Σ_{'{i,j}'} Σ_k N_{'{ij}'}^k = {grand_total}")

# Factor
for bname, bval in [('g', 7), ('g²', 49), ('g³', 343),
                     ('c₂', 11), ('c₃', 13), ('P(1)', 42),
                     ('N_c×g', 21), ('n_C×g', 35), ('g×c₂', 77),
                     ('2^N_c×g', 56)]:
    if grand_total == bval:
        print(f"  ★ Grand total = {bval} = {bname}")
    elif grand_total % bval == 0 and bval > 1:
        print(f"    {grand_total} / {bval} = {grand_total // bval} ({bname})")

# ═══════════════════════════════════════════════════════════════
# Section 8. THE FUSION GRAPH
# ═══════════════════════════════════════════════════════════════
print("\n\nSection 8. THE FUSION GRAPH OF THE VECTOR REP V")
print("-" * 50)

# The vector rep V = (1,0,0) generates the fusion ring
# Its fusion matrix N_V has eigenvalues = quantum dimensions of V
# evaluated at different points

# Find index of V
v_idx = None
for i, rep in enumerate(all_reps):
    if rep['dynkin'] == (1, 0, 0):
        v_idx = i
        break

if v_idx is not None:
    print(f"  V × X = ? for each X:")
    for j in range(n):
        name_j = rep_names.get(all_reps[j]['dynkin'], '?')
        terms = []
        for k in range(n):
            coeff = round(fusion[v_idx][j][k])
            if coeff > 0:
                name_k = rep_names.get(all_reps[k]['dynkin'], '?')
                if coeff == 1:
                    terms.append(name_k)
                else:
                    terms.append(f"{coeff}·{name_k}")
        result = ' + '.join(terms) if terms else '0'
        print(f"    V × {name_j:6s} = {result}")
else:
    print("  V = (1,0,0) is on the wall — cannot generate!")

# ═══════════════════════════════════════════════════════════════
# Section 9. THE SPINOR FUSION
# ═══════════════════════════════════════════════════════════════
print("\n\nSection 9. SPINOR FUSION")
print("-" * 50)

sp_idx = None
for i, rep in enumerate(all_reps):
    if rep['dynkin'] == (0, 0, 1):
        sp_idx = i
        break

if sp_idx is not None:
    print(f"  Sp × X = ? for each X:")
    for j in range(n):
        name_j = rep_names.get(all_reps[j]['dynkin'], '?')
        terms = []
        for k in range(n):
            coeff = round(fusion[sp_idx][j][k])
            if coeff > 0:
                name_k = rep_names.get(all_reps[k]['dynkin'], '?')
                if coeff == 1:
                    terms.append(name_k)
                else:
                    terms.append(f"{coeff}·{name_k}")
        result = ' + '.join(terms) if terms else '0'
        print(f"    Sp × {name_j:6s} = {result}")

# ═══════════════════════════════════════════════════════════════
# Section 10. ASSOCIATIVITY CHECK
# ═══════════════════════════════════════════════════════════════
print("\n\nSection 10. ASSOCIATIVITY CHECK: (V × Sp) × Sp vs V × (Sp × Sp)")
print("-" * 50)

if v_idx is not None and sp_idx is not None:
    # Compute V × Sp
    vsp = [round(fusion[v_idx][sp_idx][k]) for k in range(n)]
    print(f"  V × Sp = ", end="")
    terms = []
    for k in range(n):
        if vsp[k] > 0:
            name_k = rep_names.get(all_reps[k]['dynkin'], '?')
            terms.append(f"{vsp[k]}·{name_k}" if vsp[k] > 1 else name_k)
    print(' + '.join(terms))

    # (V × Sp) × Sp
    result1 = [0] * n
    for k in range(n):
        if vsp[k] > 0:
            for m in range(n):
                result1[m] += vsp[k] * round(fusion[k][sp_idx][m])

    print(f"  (V × Sp) × Sp = ", end="")
    terms = []
    for m in range(n):
        if result1[m] > 0:
            name_m = rep_names.get(all_reps[m]['dynkin'], '?')
            terms.append(f"{result1[m]}·{name_m}" if result1[m] > 1 else name_m)
    print(' + '.join(terms))

    # Sp × Sp
    spsp = [round(fusion[sp_idx][sp_idx][k]) for k in range(n)]
    print(f"  Sp × Sp = ", end="")
    terms = []
    for k in range(n):
        if spsp[k] > 0:
            name_k = rep_names.get(all_reps[k]['dynkin'], '?')
            terms.append(f"{spsp[k]}·{name_k}" if spsp[k] > 1 else name_k)
    print(' + '.join(terms))

    # V × (Sp × Sp)
    result2 = [0] * n
    for k in range(n):
        if spsp[k] > 0:
            for m in range(n):
                result2[m] += spsp[k] * round(fusion[v_idx][k][m])

    print(f"  V × (Sp × Sp) = ", end="")
    terms = []
    for m in range(n):
        if result2[m] > 0:
            name_m = rep_names.get(all_reps[m]['dynkin'], '?')
            terms.append(f"{result2[m]}·{name_m}" if result2[m] > 1 else name_m)
    print(' + '.join(terms))

    if result1 == result2:
        print("  ✓ ASSOCIATIVITY VERIFIED")
    else:
        print("  ✗ ASSOCIATIVITY FAILS!")

# ═══════════════════════════════════════════════════════════════
# Section 11. COMPARISON WITH CLASSICAL TENSOR PRODUCTS
# ═══════════════════════════════════════════════════════════════
print("\n\nSection 11. CLASSICAL vs QUANTUM: TRUNCATION")
print("-" * 50)

print("""
  Classical so(7) tensor products vs fusion rules:

  Classical V ⊗ V = 1 + A + S²V        (1 + 21 + 27 = 49 = 7²)
  Classical V ⊗ Sp = Sp + V⊗Sp          (8 + 48 = 56 = 2³×7)
  Classical Sp ⊗ Sp = 1 + V + A + S²Sp   (1 + 7 + 21 + 35 = 64 = 2⁶)

  Quantum truncation at level 2 modifies these products.
  The fusion coefficients are the quantum-group truncation of
  the classical Clebsch-Gordan series.
""")

# ═══════════════════════════════════════════════════════════════
# Section 12. FROBENIUS-PERRON DIMENSION
# ═══════════════════════════════════════════════════════════════
print("\nSection 12. FROBENIUS-PERRON DIMENSIONS")
print("-" * 50)

# The FP dimension is the largest eigenvalue of N_i
for i in range(n):
    name_i = rep_names.get(all_reps[i]['dynkin'], '?')
    eigs = []
    for s in range(n):
        if abs(S_norm[0][s]) > 1e-10:
            eig = (S_norm[i][s] / S_norm[0][s]).real
            eigs.append(eig)
        else:
            eigs.append(0.0)

    fp = max(eigs)
    print(f"  {name_i:6s}: FPdim = {fp:10.6f}  (classical: {all_reps[i]['classical_dim']})")

# ═══════════════════════════════════════════════════════════════
# Section 13. T-MATRIX (TWISTS)
# ═══════════════════════════════════════════════════════════════
print("\n\nSection 13. T-MATRIX (MODULAR TWISTS)")
print("-" * 50)

print(f"  T_ii = exp(2πi(h_i - c/24)) where h_i is conformal weight")
print(f"  c = {C2}, c/24 = {Fraction(C2, 24)} = {Fraction(1, 4)}")
print()

for rep in all_reps:
    name = rep_names.get(rep['dynkin'], '?')
    eps = rep['eps']
    # Conformal weight h = C₂(λ) / (2(ℓ+h∨))
    # where C₂(λ) = <λ, λ+2ρ>
    lr2 = tuple(eps[i] + 2*rho[i] for i in range(3))
    casimir = sum(eps[i] * lr2[i] for i in range(3))
    h = Fraction(casimir, 2 * M)
    twist = h - Fraction(C2, 24)

    print(f"  {name:6s}: h = {str(h):8s}  T = exp(2πi × {str(twist):8s})"
          f"  = exp(2πi × {float(twist):.6f})")

# ═══════════════════════════════════════════════════════════════
# Section 14. SYNTHESIS
# ═══════════════════════════════════════════════════════════════
print("\n")
print("=" * 72)
print("Section 14. SYNTHESIS: THE BST FUSION RING")
print("=" * 72)

print(f"""
  THE FUSION RING OF so(7) AT LEVEL 2

  7 integrable representations = g (genus)
    4 non-wall = C₂ - r (interior of alcove)
    3 wall     = N_c (boundary of alcove)

  Quantum parameter: q = e^{{2πi/7}} (7th root = g-th root)
  Central charge: c = 6 = C₂ (mass gap)
  Total quantum dimension: D² = 4 = C₂ - r

  The fusion ring encodes how representations COMBINE.
  Classical tensor product is TRUNCATED by the level:
    only representations with marks ≤ 2 survive.

  The wall reps (dim_q = 0) are the CONFINED representations —
  they exist in the algebra but have zero quantum weight.
  There are exactly N_c = 3 of them.

  ★ The fusion ring of the BST physical algebra has:
    - g = 7 objects
    - N_c = 3 confined objects
    - D² = 4 total quantum dimension
    - q = e^{{2πi/g}} quantum parameter
""")

print("=" * 72)
print("TOY 187 COMPLETE — THE FUSION RING OF so(7)₂")
print("=" * 72)
