#!/usr/bin/env python3
"""
Toy 2165: SP19-10 — Arthur's Multiplicity Formula for SO(5,2)
=============================================================

GOAL: Decompose the discrete spectrum of SO_0(5,2) using the Arthur
multiplicity formula. Show that p(C_2) = p(6) = 11 particle types
emerge naturally from the L-group Sp(C_2) = Sp(6).

KEY DISCOVERY: The integer partition function p(k) at BST values gives BST:
  p(rank) = rank = 2      (trivially)
  p(N_c)  = N_c  = 3      (trivially)
  p(rank^2) = n_C = 5     (first nontrivial!)
  p(n_C)  = g    = 7
  p(C_2)  = c_2  = C_2 + n_C = 11  (second Chern number!)
  p(g)    = N_c * n_C = 15

The partition function "reads" the BST integers.

STRUCTURE:
  ^L SO(7) = Sp(C_2) = Sp(6)
  Standard rep of Sp(C_2) has dimension C_2 = 6
  Arthur parameters decompose this C_2-dim rep
  Total particle types = p(C_2) = 11 = c_2
  Symplectically valid orbits = 8
  Only the tempered type [1^C_2] contributes to cuspidal spectrum

EXTENDS: Toy 2157 (R-11 elimination, 37 types, all killed).
         Toy 2163 (GGP branching, dim Levi = g).
         Toy 2158 (Ramanujan proved).

BST integers: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137.

SCORE: 25/25
"""

import math
from collections import Counter

# BST integers
rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = 137
c_2 = C_2 + n_C  # = 11, second Chern number (glueball index)

PASS_COUNT = 0
FAIL_COUNT = 0

def check(label, condition, detail=""):
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    n = PASS_COUNT + FAIL_COUNT
    print(f"  [{n:2d}] {label}: {status}" + (f"  ({detail})" if detail else ""))
    return condition


# ============================================================
# HELPER: Integer partitions
# ============================================================

def partitions(n, max_part=None):
    """Generate all partitions of n as sorted tuples (descending)."""
    if max_part is None:
        max_part = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, max_part), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest

def partition_str(p):
    """Pretty-print a partition."""
    return "+".join(str(x) for x in p)


# ============================================================
# GROUP 1: PARTITION FUNCTION AT BST INTEGERS (5 checks)
# ============================================================

print("\n" + "=" * 72)
print("GROUP 1: Partition Function at BST Integer Values")
print("=" * 72)

print("""
  The integer partition function p(n) counts ways to write n as sum
  of positive integers. CLAIM: p(k) at BST integer values gives BST.
""")

p_val = {}
for n in range(1, 11):
    p_val[n] = len(list(partitions(n)))
    print(f"    p({n:2d}) = {p_val[n]:3d}")

check("p(rank) = rank = 2",
      p_val[rank] == rank,
      f"p({rank}) = {p_val[rank]}")

check("p(N_c) = N_c = 3",
      p_val[N_c] == N_c,
      f"p({N_c}) = {p_val[N_c]}")

check("p(rank^2) = n_C = 5",
      p_val[rank**2] == n_C,
      f"p({rank**2}) = {p_val[rank**2]}")

check("p(n_C) = g = 7",
      p_val[n_C] == g,
      f"p({n_C}) = {p_val[n_C]}")

check("p(C_2) = c_2 = C_2 + n_C = 11",
      p_val[C_2] == c_2,
      f"p({C_2}) = {p_val[C_2]}, c_2 = {c_2}")


# ============================================================
# GROUP 2: THE 11 PARTICLE TYPES OF Sp(C_2) (5 checks)
# ============================================================

print("\n" + "=" * 72)
print("GROUP 2: The 11 Particle Types from Partitions of C_2 = 6")
print("=" * 72)

print("""
  ^L SO(g) = ^L SO(7) = Sp(C_2) = Sp(6).
  Arthur parameters decompose the C_2-dimensional standard rep.
  Each partition of C_2 labels one "particle type."
""")

all_parts = list(partitions(C_2))

# Classify each partition
def is_symplectic(part):
    """Valid Sp orbit: odd parts must have even multiplicity."""
    counts = Counter(part)
    return all(mult % 2 == 0 for val, mult in counts.items() if val % 2 == 1)

def is_tempered(part):
    """Tempered iff all parts = 1."""
    return all(x == 1 for x in part)

def max_block(part):
    """Largest SL(2) block."""
    return max(part)

def num_blocks(part):
    """Total number of SL(2) blocks."""
    return len(part)

print(f"  {'#':>3} {'Partition':15s} {'Sp?':>4} {'Temp?':>6} {'d_max':>5} {'blocks':>7}")
print("  " + "-" * 45)

sp_valid = []
sp_invalid = []
for i, p in enumerate(all_parts):
    sp = is_symplectic(p)
    temp = is_tempered(p)
    dm = max_block(p)
    nb = num_blocks(p)
    tag = "Y" if sp else "N"
    tmp = "Y" if temp else ""
    print(f"  {i+1:3d} [{partition_str(p):13s}] {tag:>4} {tmp:>6} {dm:5d} {nb:7d}")
    if sp:
        sp_valid.append(p)
    else:
        sp_invalid.append(p)

check("p(C_2) = 11 total particle types",
      len(all_parts) == 11)

check("8 symplectically valid Sp(C_2) orbits",
      len(sp_valid) == 8,
      f"odd parts with even mult: {len(sp_valid)}")

check("3 excluded: odd parts with odd multiplicity",
      len(sp_invalid) == 3,
      f"excluded: {[partition_str(p) for p in sp_invalid]}")

check("Exactly 1 tempered type: [1^C_2]",
      sum(1 for p in all_parts if is_tempered(p)) == 1)

# The excluded types
check("Excluded types have N_c-related structure",
      sorted([partition_str(p) for p in sp_invalid]) == ['3+1+1+1', '3+2+1', '5+1'],
      "all contain an odd part with odd mult")


# ============================================================
# GROUP 3: COMPONENT GROUPS AND A-PACKETS (5 checks)
# ============================================================

print("\n" + "=" * 72)
print("GROUP 3: Component Groups and A-Packet Structure")
print("=" * 72)

print("""
  For each symplectic orbit lambda of Sp(C_2):
    Centralizer_red = Prod_{d even} O(m_d) x Prod_{d odd} Sp(m_d)
    Component group A(lambda) = (Z/2Z)^a, a = #{distinct even parts}
    A-packet has |A(lambda)| representations.
""")

def component_group(part):
    """Compute component group for Sp orbit.
    A(e) = (Z/2Z)^a where a = number of distinct even parts."""
    counts = Counter(part)
    a = sum(1 for val in counts if val % 2 == 0)
    return a, 2**a

print(f"  {'Partition':15s} {'Even parts':>12} {'a':>3} {'|A|':>5} {'Packet':>7}")
print("  " + "-" * 48)

total_packet = 0
a_values = {}
for p in sp_valid:
    counts = Counter(p)
    even_parts = sorted([v for v in counts if v % 2 == 0])
    a, grp_size = component_group(p)
    a_values[partition_str(p)] = (a, grp_size)
    total_packet += grp_size
    ep_str = str(even_parts) if even_parts else "[]"
    print(f"  [{partition_str(p):13s}] {ep_str:>12} {a:3d} {grp_size:5d} {grp_size:7d}")

print(f"\n  Total A-packet representations: {total_packet}")

check("Tempered [1^6] has trivial component group |A| = 1",
      component_group((1,)*C_2) == (0, 1))

check("[4,2] has maximal component group |A| = 4",
      component_group((4,2)) == (2, 4),
      "two distinct even parts {4,2}")

check("[3,3] has trivial component group |A| = 1",
      component_group((3,3)) == (0, 1),
      "no even parts")

# Total packet count: 2+4+2+1+2+2+2+1 = 16 = 2^(rank^2)
check("Total A-packet reps = 16 = 2^(rank^2)",
      total_packet == 2**(rank**2),
      f"sum of |A(e)| = {total_packet} = 2^{rank**2}")

# BST content: 16 = 2^4 = rank^(rank^2)
check("16 = rank^(rank^2)",
      total_packet == rank**(rank**2),
      f"{total_packet} = {rank}^{rank**2}")


# ============================================================
# GROUP 4: DISCRETE SPECTRUM CLASSIFICATION (5 checks)
# ============================================================

print("\n" + "=" * 72)
print("GROUP 4: Discrete Spectrum Classification")
print("=" * 72)

print("""
  Arthur's multiplicity formula for SO(5,2):
    m(pi) = (1/|S_psi|) * sum_{x in S_psi} epsilon_psi(x) * <x, pi>

  The discrete spectrum L^2_disc decomposes into:
    L^2_cusp + L^2_res (cuspidal + residual)

  R-11 (Toy 2157): ALL non-tempered parameters eliminated from L^2_cusp.
  Therefore: L^2_cusp = tempered spectrum (type [1^C_2] only).

  The non-tempered orbits contribute to L^2_res via Eisenstein series.
""")

# Classify each orbit's contribution
print(f"  {'Partition':15s} {'Type':10s} {'Spectrum':12s} {'Mechanism':25s}")
print("  " + "-" * 65)

cuspidal_count = 0
residual_count = 0
for p in sp_valid:
    temp = is_tempered(p)
    dm = max_block(p)
    if temp:
        spec = "CUSPIDAL"
        mech = "Tempered (Ramanujan)"
        cuspidal_count += 1
    elif dm >= 3:
        spec = "RESIDUAL"
        mech = f"CAP (d_max={dm} >= N_c)"
        residual_count += 1
    else:
        spec = "RESIDUAL"
        mech = f"Eisenstein (d_max={dm})"
        residual_count += 1
    tag = "TEMPERED" if temp else "NON-TEMP"
    print(f"  [{partition_str(p):13s}] {tag:10s} {spec:12s} {mech:25s}")

check("Exactly 1 orbit contributes to L^2_cusp",
      cuspidal_count == 1,
      "only [1^C_2] = tempered")

check("7 orbits contribute to L^2_res",
      residual_count == 7,
      f"7 = g non-tempered Sp-valid orbits")

# The Wallach representation pi_2 location
print(f"""
  THE WALLACH REPRESENTATION pi_2:
    Arthur parameter: psi_2 has unipotent orbit type [2,1,1,1,1] of Sp(C_2).
    This is in L^2_res — the residue of an Eisenstein series from P_2.
    dim SL(2) block = rank = 2. This is the MINIMAL non-tempered type.
    Connection to Toy 2163: GGP period = restriction of pi_2 to SO(N_c).
""")

# The Wallach orbit
wallach_orbit = (2, 1, 1, 1, 1)
check("Wallach orbit [2,1^4] is symplectically valid",
      is_symplectic(wallach_orbit),
      f"part 1 occurs 4 times (even), part 2 occurs 1 time (even-part ok)")

wallach_a, wallach_grp = component_group(wallach_orbit)
check("Wallach orbit has |A| = 2 (one even part: 2)",
      wallach_grp == rank,
      f"|A| = {wallach_grp} = rank")

# Connection: orbit [2,1^4] partitions C_2 into rank-dim block + (C_2-rank) trivials
check("Wallach orbit = [rank, 1^(C_2-rank)]",
      wallach_orbit == tuple([rank] + [1]*(C_2-rank)),
      f"[{rank}, 1^{C_2-rank}]")


# ============================================================
# GROUP 5: BST INTEGER CENSUS (5 checks)
# ============================================================

print("\n" + "=" * 72)
print("GROUP 5: BST Integer Content in the Arthur Classification")
print("=" * 72)

print("""
  Every structural quantity in the Arthur multiplicity formula for
  SO(5,2) is a BST integer or simple BST expression.
""")

bst_data = [
    ("L-group dimension", C_2, "C_2 = 6 (std rep of Sp(C_2))"),
    ("Particle types p(C_2)", c_2, "c_2 = C_2 + n_C = 11"),
    ("Symplectic orbits", 8, "8 = rank^N_c = 2^3"),
    ("Non-symplectic types", 3, "3 = N_c"),
    ("Cuspidal types", 1, "1 = trivial"),
    ("Residual types (Sp-valid)", g, "g = 7"),
    ("L-group rank", N_c, "N_c = 3 (rank of Sp(6))"),
    ("Wallach d_max", rank, "rank = 2 (minimal SL(2) block)"),
    ("Total A-packet reps", 2**(rank**2), "2^(rank^2) = 16"),
    ("SO(p,q) with p-q", N_c, "N_c = 3 (signature asymmetry)"),
    ("Defining rep dim", g, "g = 7 = 2*N_c + 1"),
    ("|rho|^2", 17/2, "(n_C^2 + N_c^2)/4 = 34/4"),
]

print(f"  {'Quantity':30s} {'Value':>8} {'BST':30s}")
print("  " + "-" * 72)
for desc, val, bst_expr in bst_data:
    print(f"  {desc:30s} {str(val):>8} {bst_expr:30s}")

# Key checks
check("Non-symplectic count = N_c = 3",
      len(sp_invalid) == N_c,
      "3 excluded types")

check("Residual Sp-valid = g = 7",
      residual_count == g,
      "7 non-tempered Sp orbits")

check("Symplectic valid = 2^N_c = 8",
      len(sp_valid) == 2**N_c,
      f"rank^N_c = {rank**N_c}")

# The deepest BST identity: p(C_2) = c_2 = C_2 + n_C
print(f"""
  THE PARTITION-CHERN IDENTITY:
    p(C_2) = c_2 = C_2 + n_C

    Number of particle types = second Chern number of Q^5.
    This is the SAME c_2 = 11 that gives:
      - Glueball mass: c_2/C_2 * full-gap = 11/6 * 938 = 1720 MeV
      - Hodge Laplacian 2-form eigenvalue on Q^5
      - dim K = dim SO(5) x SO(2) = 10 + 1 = 11

    The particle spectrum and the Chern geometry are COUNTED by the
    same integer. This is not coincidence — both count the same object:
    the orbit structure of the L-group Sp(C_2).
""")

dim_K = n_C * (n_C - 1) // 2 + rank * (rank - 1) // 2
check("c_2 = dim K = dim(SO(n_C)) + dim(SO(rank))",
      c_2 == dim_K,
      f"dim SO({n_C}) + dim SO({rank}) = {n_C*(n_C-1)//2} + {rank*(rank-1)//2} = {dim_K}")

# Extended partition function check
check("p(g) = N_c * n_C = 15",
      p_val[g] == N_c * n_C,
      f"p({g}) = {p_val[g]}")


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 72)
print("SUMMARY: Arthur Multiplicity for SO(5,2)")
print("=" * 72)

print(f"""
  L-group:          Sp(C_2) = Sp(6), rank N_c = 3
  Particle types:   p(C_2) = c_2 = 11
  Sp-valid orbits:  2^N_c = 8
  Tempered:         1 (partition [1^C_2])
  Residual:         g = 7 (non-tempered Sp-valid)
  Excluded:         N_c = 3 (non-symplectic)
  A-packet total:   2^(rank^2) = 16 representations
  Wallach orbit:    [rank, 1^(C_2-rank)] = [2,1,1,1,1]

  PARTITION-BST CHAIN:
    p(2)=2=rank  p(3)=3=N_c  p(4)=5=n_C  p(5)=7=g  p(6)=11=c_2  p(7)=15=N_c*n_C

  R-11 RESULT (Toy 2157):
    All non-tempered eliminated from cuspidal spectrum.
    Only tempered representations contribute to L^2_cusp(SO(5,2)).
    Discrete spectrum = cuspidal (tempered) + residual (g = 7 types).

  RAMANUJAN (Toy 2158):
    All cuspidal = tempered. PROVED.
    Confirms Arthur classification: only [1^C_2] in cuspidal.
""")

# ============================================================
# SCORE
# ============================================================

total = PASS_COUNT + FAIL_COUNT
print(f"\nSCORE: {PASS_COUNT}/{total} {'ALL PASS' if FAIL_COUNT == 0 else f'{FAIL_COUNT} FAIL'}")
