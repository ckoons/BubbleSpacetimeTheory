#!/usr/bin/env python3
"""
Toy 1951 -- Quantum Group U_q(B_2) at q = exp(2*pi*i/137)

Z-11: The quantum group U_q(B_2) at the N_max-th root of unity categorifies BST.

B_2 = so(5) is the root system type of BST's Autogenic Proto-Geometry D_IV^5.
At q = exp(2*pi*i/137), the representation theory of U_q(B_2) encodes every
BST integer in its algebraic structure:

  CASIMIR EIGENVALUES (all BST):
    C(1,0) = 4 = rank^2           (vector rep, dim = n_C = 5)
    C(0,1) = 5/2 = n_C/rank       (spinor rep, dim = rank^2 = 4)
    C(0,2) = 6 = C_2 = 2*h^v      (adjoint rep, dim = 10)
    C(2,0) = 10 = rank*n_C         (symmetric traceless, dim = 14)

  The two fundamental Casimirs satisfy a QUADRATIC:
    x^2 - (c_3/rank)*x + rank*n_C = 0
    Sum  = 13/2 = c_3/rank         (c_3 = 13, 3rd Chern number)
    Prod = 10 = dim(so(5))
    Disc = 9/4 = (N_c/rank)^2      N_c EMERGES from the discriminant!

  COXETER STRUCTURE:
    h^v(B_2) = 3 = N_c             (dual Coxeter number)
    h(B_2)   = 4 = rank^2          (Coxeter number)
    |W(B_2)| = 8 = rank^3 = 2^N_c  (Weyl group order)

  VERLINDE LEVEL:
    k = N_max - h^v = 137 - 3 = 134 = N_max - N_c

  ALCOVE COUNT (Verlinde primaries):
    4556 = 67 * 68 = ((N_max-N_c)/2) * (rank^2 * seesaw)
    where seesaw = 2*g + N_c = 17

  R-MATRIX: eigenvalues on V(1,0) x V(1,0) are q^{-rank^2}, q^{-1}, q^{+1}

  RIBBON: theta(spinor)^137 = -1 (spinors are FERMIONIC)
          theta(vector)^137 = +1 (vectors are BOSONIC)
          Fermion/boson distinction is AUTOMATIC at the 137th root.

  |rho|^2 = 5/2 = n_C/rank = C(0,1) (spinor Casimir IS rho norm squared)

BST integers: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137
Additional: c_2=11, c_3=13, seesaw=17

Author: Grace (Z-11 quantum group categorification)
Date: May 3, 2026

SCORE: 33/33
"""

import math
from fractions import Fraction

# ===================================================================
#  BST INTEGERS
# ===================================================================

rank   = 2
N_c    = 3
n_C    = 5
C_2    = 6
g      = 7
N_max  = 137
c_2    = C_2 + n_C       # 11
c_3    = g + C_2          # 13
seesaw = 2*g + N_c        # 17

p = N_max  # root of unity order

# ===================================================================
#  PASS/FAIL MACHINERY
# ===================================================================

pass_count = 0
fail_count = 0

def check(name, condition, detail=""):
    global pass_count, fail_count
    if condition:
        pass_count += 1
        print(f"  \033[32mPASS\033[0m {name}")
    else:
        fail_count += 1
        print(f"  \033[31mFAIL\033[0m {name}")
    if detail:
        print(f"         {detail}")

# ===================================================================
#  B_2 ROOT SYSTEM DATA
# ===================================================================
#
# B_2 Cartan matrix (Bourbaki: alpha_1 long, alpha_2 short):
#   A = [[2, -2], [-1, 2]]
#
# Inner products: <alpha_1,alpha_1>=2, <alpha_2,alpha_2>=1, <alpha_1,alpha_2>=-1
#
# Positive roots: alpha_1, alpha_2, alpha_1+alpha_2, alpha_1+2*alpha_2
# Lengths^2:       2        1        1                2
#
# Fundamental weights in root basis:
#   omega_1 = alpha_1 + alpha_2
#   omega_2 = (1/2)*alpha_1 + alpha_2
#
# Weight space inner products:
#   <omega_1, omega_1> = 1
#   <omega_2, omega_2> = 1/2
#   <omega_1, omega_2> = 1/2
#
# d_i = |alpha_i|^2 / 2:  d_1 = 1 (long), d_2 = 1/2 (short)

# ===================================================================
#  WEYL DIMENSION FORMULA FOR B_2
# ===================================================================

def weyl_dim(m1, m2):
    """Classical dimension of V(m1,m2) for B_2 = so(5).

    Uses <lambda+rho, alpha^v> for four positive roots:
      alpha_1 (long):           m1+1
      alpha_2 (short):          m2+1
      alpha_1+alpha_2 (short):  2*m1+m2+3
      alpha_1+2*alpha_2 (long): m1+m2+2

    rho values (m1=m2=0): 1, 1, 3, 2
    """
    num = (m1 + 1) * (m2 + 1) * (2*m1 + m2 + 3) * (m1 + m2 + 2)
    den = 1 * 1 * 3 * 2  # = 6
    return num // den

# ===================================================================
#  CASIMIR EIGENVALUE
# ===================================================================

def casimir(m1, m2):
    """Quadratic Casimir C(m1,m2) = <lambda, lambda+2*rho>.

    Using <omega_i,omega_j> matrix: [[1, 1/2], [1/2, 1/2]]
    and rho = omega_1 + omega_2.
    """
    lam_sq = Fraction(m1**2) + Fraction(m2**2, 2) + Fraction(m1 * m2)
    lam_rho = Fraction(3, 2) * m1 + Fraction(m2)
    return lam_sq + 2 * lam_rho

# ===================================================================
#  QUANTUM NUMBERS AND QUANTUM DIMENSIONS
# ===================================================================

def qnum_at(n, s):
    """Quantum number [n] at parameter angle s: sin(n*s)/sin(s)."""
    denom = math.sin(s)
    if abs(denom) < 1e-15:
        return float('nan')
    return math.sin(n * s) / denom

# Root-dependent quantum parameters:
# q = exp(2*pi*i/p)
# q_long  = q^{d_long}  = q^1     -> angle s_long  = 2*pi/p
# q_short = q^{d_short} = q^{1/2} -> angle s_short = pi/p
s_long  = 2 * math.pi / p
s_short = math.pi / p

def qdim(m1, m2):
    """Quantum dimension of V(m1,m2) for U_q(B_2) at q = exp(2*pi*i/137).

    Each positive root alpha contributes [<lambda+rho, alpha^v>]_{q_alpha}
    using the root-dependent quantum parameter q_alpha = q^{d_alpha}.
    Denominator uses rho (m1=m2=0).
    """
    num = (qnum_at(m1 + 1, s_long) *
           qnum_at(m2 + 1, s_short) *
           qnum_at(2*m1 + m2 + 3, s_short) *
           qnum_at(m1 + m2 + 2, s_long))
    den = (qnum_at(1, s_long) *
           qnum_at(1, s_short) *
           qnum_at(3, s_short) *
           qnum_at(2, s_long))
    return num / den

# ===================================================================
#  ALCOVE COUNT
# ===================================================================

def count_alcove(p_val):
    """Count dominant weights in the interior of the fundamental alcove.

    For B_2 at p-th root of unity with h^v = 3:
    Quantum dimension is nonzero when all <lambda+rho, alpha^v> are
    not divisible by p (for short root parameter) or by p (for long).

    The binding walls:
      m1+1 < p  (long root alpha_1)
      m2+1 < p  (short root alpha_2, parameter pi/p)
      2*m1+m2+3 < p  (short root alpha_1+alpha_2)
      m1+m2+2 < p  (long root alpha_1+2*alpha_2)

    Strongest constraint: 2*m1 + m2 <= p - 4 = 133.
    """
    h_v = 3
    bound = p_val - h_v - 1  # = 133
    count = 0
    for m1 in range(bound // 2 + 1):
        max_m2 = bound - 2 * m1
        if max_m2 >= 0:
            count += max_m2 + 1
    return count

# ===================================================================
#  MAIN COMPUTATION
# ===================================================================

print("=" * 70)
print("BLOCK 1: B_2 Root System -- BST Integers in the Algebra")
print("=" * 70)
print()

# Dual Coxeter and Coxeter numbers
# B_n: h^v = 2n-1, h = 2n. For B_2: h^v = 3, h = 4.
h_v = 3
h   = 4
W_order = 8  # |W(B_2)| = 2^n * n! = 4*2 = 8

check("h^v(B_2) = 3 = N_c (dual Coxeter number)",
      h_v == N_c,
      f"h^v = {h_v}")

check("h(B_2) = 4 = rank^2 (Coxeter number)",
      h == rank**2,
      f"h = {h}")

check("|W(B_2)| = 8 = rank^3 = 2^N_c (Weyl group order)",
      W_order == rank**3 == 2**N_c,
      f"|W| = {W_order}")

# Lie algebra dimension
dim_so5 = 10
check("dim(so(5)) = 10 = rank * n_C",
      dim_so5 == rank * n_C)

# Number of positive roots
n_pos_roots = 4
check("Number of positive roots = 4 = rank^2",
      n_pos_roots == rank**2)

print()
print("=" * 70)
print("BLOCK 2: Fundamental Representations -- Classical Dimensions")
print("=" * 70)
print()

check("dim V(1,0) = 5 = n_C (vector representation of so(5))",
      weyl_dim(1, 0) == n_C,
      f"dim V(1,0) = {weyl_dim(1,0)}")

check("dim V(0,1) = 4 = rank^2 (spinor representation of so(5))",
      weyl_dim(0, 1) == rank**2,
      f"dim V(0,1) = {weyl_dim(0,1)}")

check("dim V(0,2) = 10 = rank * n_C = dim(so(5)) (adjoint)",
      weyl_dim(0, 2) == rank * n_C == dim_so5,
      f"dim V(0,2) = {weyl_dim(0,2)}")

print(f"\n  Additional classical dimensions:")
print(f"    V(2,0) = {weyl_dim(2,0)} (symmetric traceless 2-tensor)")
print(f"    V(1,1) = {weyl_dim(1,1)}")

print()
print("=" * 70)
print("BLOCK 3: Casimir Eigenvalues -- Every One BST")
print("=" * 70)
print()

c_10 = casimir(1, 0)
c_01 = casimir(0, 1)
c_02 = casimir(0, 2)
c_20 = casimir(2, 0)
c_11 = casimir(1, 1)

check("C(1,0) = 4 = rank^2",
      c_10 == Fraction(rank**2),
      f"Casimir of vector rep = {c_10}")

check("C(0,1) = 5/2 = n_C/rank",
      c_01 == Fraction(n_C, rank),
      f"Casimir of spinor rep = {c_01}")

check("C(0,2) = 6 = C_2 = 2*h^v (adjoint Casimir IS the BST C_2!)",
      c_02 == Fraction(C_2) == 2 * h_v,
      f"Adjoint Casimir = {c_02}")

check("C(2,0) = 10 = rank * n_C = dim(so(5))",
      c_20 == Fraction(rank * n_C),
      f"C(2,0) = {c_20}")

print()
print("=" * 70)
print("BLOCK 4: The Casimir Quadratic -- N_c from the Discriminant")
print("=" * 70)
print()

# C(1,0) and C(0,1) are roots of x^2 - S*x + P = 0
S = c_10 + c_01   # 4 + 5/2 = 13/2
P = c_10 * c_01   # 4 * 5/2 = 10
D = S**2 - 4 * P  # 169/4 - 40 = 9/4

check("Sum C(1,0)+C(0,1) = 13/2 = c_3/rank (c_3=13 = 3rd Chern number)",
      S == Fraction(c_3, rank),
      f"Sum = {S} = {c_3}/{rank}")

check("Product C(1,0)*C(0,1) = 10 = dim(so(5)) = rank*n_C",
      P == Fraction(rank * n_C),
      f"Product = {P}")

check("Discriminant = 9/4 = (N_c/rank)^2",
      D == Fraction(N_c, rank)**2,
      f"Disc = {D} = ({N_c}/{rank})^2")

print(f"\n  The fundamental Casimirs satisfy:")
print(f"    x^2 - (c_3/rank)*x + rank*n_C = 0")
print(f"    x^2 - (13/2)*x + 10 = 0")
print(f"    roots = (c_3 +/- N_c) / (2*rank)")
print(f"          = {Fraction(c_3+N_c, 2*rank)}, {Fraction(c_3-N_c, 2*rank)}")
print(f"          = rank^2 = 4, n_C/rank = 5/2")

print()
print("=" * 70)
print("BLOCK 5: rho -- Spinor Casimir IS rho Norm Squared")
print("=" * 70)
print()

# rho = omega_1 + omega_2
# <rho,rho> = <omega_1,omega_1> + 2<omega_1,omega_2> + <omega_2,omega_2>
#           = 1 + 2*(1/2) + 1/2 = 5/2
rho_sq = Fraction(1) + 2*Fraction(1,2) + Fraction(1,2)

check("|rho|^2 = 5/2 = n_C/rank",
      rho_sq == Fraction(n_C, rank),
      f"|rho|^2 = {rho_sq}")

check("C(0,1) = |rho|^2 (spinor Casimir = rho norm squared)",
      c_01 == rho_sq,
      f"Both equal {rho_sq}")

print()
print("=" * 70)
print("BLOCK 6: Quantum Dimensions at q = exp(2*pi*i/137)")
print("=" * 70)
print()

qd_10 = qdim(1, 0)
qd_01 = qdim(0, 1)
qd_02 = qdim(0, 2)
qd_20 = qdim(2, 0)
qd_11 = qdim(1, 1)

print(f"  Quantum dimensions (q = exp(2*pi*i/{p}), root-dependent parameters):")
print(f"  {'Rep':>8} | {'Classical':>10} | {'Quantum':>12} | {'Deviation':>10}")
print(f"  {'--------':>8} | {'----------':>10} | {'------------':>12} | {'----------':>10}")
for (m1,m2), qd, cl, name in [((1,0), qd_10, 5, 'V(1,0)'),
                                ((0,1), qd_01, 4, 'V(0,1)'),
                                ((0,2), qd_02, 10, 'V(0,2)'),
                                ((2,0), qd_20, 14, 'V(2,0)'),
                                ((1,1), qd_11, 16, 'V(1,1)')]:
    dev = abs(qd - cl) / cl * 100
    print(f"  {name:>8} | {cl:>10} | {qd:>12.8f} | {dev:>9.4f}%")

# Quantum tensor product: qdim is a ring homomorphism
# V(1,0) x V(1,0) = V(0,0) + V(0,2) + V(2,0) classically [1+10+14 = 25 = 5^2]
check("qdim(1,0)^2 = qdim(0,0)+qdim(0,2)+qdim(2,0) [V(1,0) tensor product]",
      abs(qd_10**2 - (1.0 + qd_02 + qd_20)) < 1e-8,
      f"{qd_10**2:.8f} = {1.0+qd_02+qd_20:.8f}")

# V(0,1) x V(0,1) = V(0,0) + V(1,0) + V(0,2) classically [1+5+10 = 16 = 4^2]
check("qdim(0,1)^2 = qdim(0,0)+qdim(1,0)+qdim(0,2) [V(0,1) tensor product]",
      abs(qd_01**2 - (1.0 + qd_10 + qd_02)) < 1e-8,
      f"{qd_01**2:.8f} = {1.0+qd_10+qd_02:.8f}")

# V(1,0) x V(0,1) = V(0,1) + V(1,1) classically [5*4 = 4+16 = 20]
check("qdim(1,0)*qdim(0,1) = qdim(0,1)+qdim(1,1) [mixed tensor product]",
      abs(qd_10 * qd_01 - (qd_01 + qd_11)) < 1e-8,
      f"{qd_10*qd_01:.8f} = {qd_01+qd_11:.8f}")

print()
print("=" * 70)
print("BLOCK 7: R-Matrix and Ribbon Structure")
print("=" * 70)
print()

# R-matrix eigenvalues on V(1,0) x V(1,0) = V(0,0) + V(0,2) + V(2,0)
# Eigenvalue on V(mu) component = q^{(C(mu) - 2*C(1,0))/2}
r_00 = (casimir(0,0) - 2*c_10) / 2  # (0 - 8)/2 = -4
r_02 = (casimir(0,2) - 2*c_10) / 2  # (6 - 8)/2 = -1
r_20 = (casimir(2,0) - 2*c_10) / 2  # (10 - 8)/2 = +1

check("R-matrix on V(0,0): exponent = -4 = -rank^2",
      r_00 == Fraction(-rank**2),
      f"q^{{{r_00}}}")

check("R-matrix on V(0,2) [adjoint]: exponent = -1",
      r_02 == Fraction(-1),
      f"q^{{{r_02}}}")

check("R-matrix on V(2,0) [sym.tr.]: exponent = +1",
      r_20 == Fraction(+1),
      f"q^{{{r_20}}}")

# Ribbon (twist) factors: theta(V) = q^{C(V)}
# theta(V)^p = exp(2*pi*i * C(V)):
#   = +1 if C is integer (bosonic)
#   = -1 if C is half-integer (fermionic)
print(f"\n  Ribbon factors theta(V) = q^{{C(V)}}:")
print(f"    theta(vector)^{p}  = exp(2*pi*i*{c_10})  = +1 (BOSONIC)")
print(f"    theta(spinor)^{p}  = exp(2*pi*i*{c_01}) = -1 (FERMIONIC)")
print(f"    theta(adjoint)^{p} = exp(2*pi*i*{c_02})  = +1 (BOSONIC)")

theta_vec = math.cos(2*math.pi*float(c_10))  # cos(8*pi) = 1
theta_spi = math.cos(2*math.pi*float(c_01))  # cos(5*pi) = -1

check("theta(vector)^137 = +1 (integer Casimir -> boson)",
      abs(theta_vec - 1.0) < 1e-10)

check("theta(spinor)^137 = -1 (half-integer Casimir -> fermion)",
      abs(theta_spi - (-1.0)) < 1e-10,
      "Fermion/boson distinction is AUTOMATIC at q^N_max = 1")

print()
print("=" * 70)
print("BLOCK 8: Verlinde Level and Alcove Structure")
print("=" * 70)
print()

k = p - h_v  # Verlinde level = 137 - 3 = 134

check("Verlinde level k = N_max - N_c = 134",
      k == N_max - N_c,
      f"k = {p} - {h_v} = {k}")

# Alcove count
alcove = count_alcove(p)

check("Alcove count = 4556 = 67 * 68 (Verlinde primaries)",
      alcove == 67 * 68 == 4556,
      f"count = {alcove}")

# 68 = rank^2 * seesaw = 4 * 17
check("68 = rank^2 * seesaw = 4 * 17 (seesaw = 2*g+N_c)",
      68 == rank**2 * seesaw,
      f"68 = {rank**2} * {seesaw}")

# 67 = (N_max - N_c) / 2, prime
check("67 = (N_max - N_c)/2, prime",
      67 == (N_max - N_c) // 2 and all(67 % i != 0 for i in range(2, 9)),
      f"67 = ({N_max}-{N_c})/2 = {k}//2")

# Closed form: alcove = (N_max-N_c)(N_max-N_c+2)/4
check("Alcove = (N_max-N_c)(N_max-N_c+2)/4 = 134*136/4",
      alcove == (N_max - N_c) * (N_max - N_c + 2) // 4,
      f"134 * 136 / 4 = {134*136//4}")

# Simple modules of small quantum group
simple_small = p**rank
check("Small quantum group: p^rank = 137^2 = 18769 simple modules",
      simple_small == N_max**rank == 18769,
      f"p^rank = {p}^{rank} = {simple_small}")

print()
print("=" * 70)
print("BLOCK 9: Alcove Boundary -- Quantum Dimension Vanishes")
print("=" * 70)
print()

# At the wall 2*m1+m2+3 = p: quantum dimension vanishes
qd_wall = qdim(67, 0)
check("qdim V(67,0) = 0 (on wall: 2*67+0+3 = 137 = p)",
      abs(qd_wall) < 1e-10,
      f"qdim = {qd_wall:.2e}")

# Just inside the wall
qd_inside = qdim(66, 0)
check("qdim V(66,0) > 0 (inside: 2*66+0+3 = 135 < p)",
      qd_inside > 0.1,
      f"qdim = {qd_inside:.6f}")

# ===================================================================
#  SUMMARY
# ===================================================================

print()
print("=" * 70)
print("SUMMARY -- U_q(B_2) at q = exp(2*pi*i/137)")
print("=" * 70)
print()
print("  THE B_2 QUANTUM GROUP CATEGORIFIES BST.")
print()
print("  Every BST integer appears in the algebraic structure:")
print()
print(f"    N_c = 3  = h^v (dual Coxeter number)")
print(f"    rank = 2 : C(1,0) = rank^2, dim V(0,1) = rank^2, h = rank^2")
print(f"    n_C = 5  : C(0,1) = n_C/rank, dim V(1,0) = n_C")
print(f"    C_2 = 6  = C_adj = 2*h^v (adjoint Casimir)")
print(f"    g = 7    : seesaw = 2g+N_c = 17 divides alcove (68 = rank^2*17)")
print(f"    N_max = 137: root of unity order = Verlinde level + N_c")
print()
print("  Casimir quadratic: x^2 - (c_3/rank)*x + rank*n_C = 0")
print(f"    discriminant = (N_c/rank)^2 = 9/4")
print(f"    roots: rank^2 = 4, n_C/rank = 5/2")
print()
print("  The spinor is FERMIONIC (theta^137 = -1).")
print("  The vector is BOSONIC  (theta^137 = +1).")
print(f"  Fermion/boson distinction is AUTOMATIC at q^{{N_max}} = 1.")
print()
print(f"  Alcove = 4556 = (N_max-N_c)/2 * rank^2 * (2g+N_c)")
print(f"         = 67 * 4 * 17")
print()

print(f"SCORE: {pass_count}/{pass_count + fail_count}")
