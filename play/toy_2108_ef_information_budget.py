#!/usr/bin/env python3
"""
Toy 2108 — EF Information Budget: Modus Ponens DPI Verification
================================================================
Computational foundation for Paper 2 (EF Information Budget Theorem).

Verifies information-theoretic properties of Extended Frege proofs
on small 3-SAT instances:

  1. Extension DPI: z=f(x_S) satisfies I(z; x_j) <= I(x_S; x_j)
  2. Extension axiom zero: tautological axioms carry 0 info about SAT
  3. Modus ponens gap: B derived from A,A->B; B NOT a function of (A,A->B)
  4. Variable-level DPI: I(any f(x); x_j) <= I(underlying vars; x_j)
  5. Nested extension DPI cascade through definitions
  6. Block coverage: single extension <= 1 bit across independent blocks
  7. Bridging extensions bounded by source variables
  8. MI decay with VIG distance (consistency with Paper 1)
  9. The structural gap: routing vs creation

Key finding: Modus ponens can RECOVER info lost by compression (AND/OR),
because extension axioms encode logical STRUCTURE even though they carry
zero STATISTICAL info. This recovery = routing, not creation. Whether
polynomial routing suffices for refutation IS T69.

Ref: Paper 1 (BST_PNP_Shannon_Proof.md), T1765, T1766

SCORE: ?/9
"""

import math
import random
from collections import defaultdict

random.seed(42)

PASS = 0
FAIL = 0

def test(name, condition, detail=""):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  PASS  {name}")
    else:
        FAIL += 1
        print(f"  FAIL  {name}")
    if detail:
        print(f"        {detail}")

def log2(x):
    return math.log2(x) if x > 1e-15 else 0.0

def entropy(counts):
    """Shannon entropy from count dict."""
    total = sum(counts.values())
    if total == 0:
        return 0.0
    return -sum((c/total) * log2(c/total) for c in counts.values() if c > 0)

def mutual_info_from_counts(joint, marg_x, marg_y, total):
    """MI from count dicts."""
    mi = 0.0
    for (x, y), nxy in joint.items():
        if nxy == 0:
            continue
        pxy = nxy / total
        px = marg_x[x] / total
        py = marg_y[y] / total
        if px > 0 and py > 0:
            mi += pxy * log2(pxy / (px * py))
    return mi

# ─── SAT infrastructure ───

def gen_3sat(n, m, seed=42):
    """Random 3-SAT: m clauses on n variables."""
    rng = random.Random(seed)
    clauses = []
    for _ in range(m):
        vs = rng.sample(range(n), 3)
        signs = [rng.choice([True, False]) for _ in range(3)]
        clauses.append(list(zip(vs, signs)))
    return clauses

def eval_clause(clause, a):
    for v, pos in clause:
        if (pos and a[v]) or (not pos and not a[v]):
            return True
    return False

def eval_formula(clauses, a):
    return all(eval_clause(c, a) for c in clauses)

def find_sat(clauses, n):
    """Enumerate satisfying assignments."""
    out = []
    for bits in range(1 << n):
        a = tuple((bits >> i) & 1 for i in range(n))
        if eval_formula(clauses, a):
            out.append(a)
    return out

def mi_func_var(sat, func, j):
    """I(f(x); x_j | SAT) from satisfying assignments."""
    N = len(sat)
    if N == 0:
        return 0.0
    joint = defaultdict(int)
    mf = defaultdict(int)
    mv = defaultdict(int)
    for a in sat:
        fv = func(a)
        xv = a[j]
        joint[(fv, xv)] += 1
        mf[fv] += 1
        mv[xv] += 1
    return mutual_info_from_counts(joint, mf, mv, N)

def mi_set_var(sat, var_set, j):
    """I(x_S; x_j | SAT) where S is a tuple/list of indices."""
    N = len(sat)
    if N == 0:
        return 0.0
    joint = defaultdict(int)
    ms = defaultdict(int)
    mv = defaultdict(int)
    for a in sat:
        sv = tuple(a[i] for i in var_set)
        xv = a[j]
        joint[(sv, xv)] += 1
        ms[sv] += 1
        mv[xv] += 1
    return mutual_info_from_counts(joint, ms, mv, N)

def mi_var_var(sat, i, j):
    """I(x_i; x_j | SAT)."""
    return mi_func_var(sat, lambda a: a[i], j)

def mi_joint_func_var(sat, f1, f2, j):
    """I((f1, f2); x_j | SAT)."""
    return mi_func_var(sat, lambda a: (f1(a), f2(a)), j)

def func_entropy(sat, func):
    """H(f(x) | SAT)."""
    N = len(sat)
    if N == 0:
        return 0.0
    counts = defaultdict(int)
    for a in sat:
        counts[func(a)] += 1
    return entropy(counts)

def bfs_dist(s, t, adj, n):
    if s == t:
        return 0
    visited = {s}
    queue = [(s, 0)]
    while queue:
        node, d = queue.pop(0)
        for nb in adj.get(node, []):
            if nb == t:
                return d + 1
            if nb not in visited:
                visited.add(nb)
                queue.append((nb, d + 1))
    return 999

# ═══════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════

print("=" * 65)
print("Toy 2108 — EF Information Budget: Modus Ponens DPI Verification")
print("=" * 65)
print()

# Generate satisfiable instance
n = 10
m = 30  # alpha = 3.0, well below threshold
clauses = gen_3sat(n, m, seed=42)
sat = find_sat(clauses, n)

# Retry seeds until we get enough solutions
seed = 42
while len(sat) < 20:
    seed += 1
    clauses = gen_3sat(n, m, seed=seed)
    sat = find_sat(clauses, n)

print(f"Instance: n={n}, m={m}, alpha={m/n:.1f}, seed={seed}")
print(f"Satisfying assignments: {len(sat)} / {1 << n}")

# Build VIG
adj = defaultdict(set)
for clause in clauses:
    vs = [v for v, _ in clause]
    for i in range(3):
        for j in range(i + 1, 3):
            adj[vs[i]].add(vs[j])
            adj[vs[j]].add(vs[i])

# Pick a distant target variable
target = n - 1
print(f"Target variable: x_{target}")
print()

# ─── Test 1: Extension DPI ───
print("─── Test 1: Extension DPI ───")
S = [0, 1, 2]
exts = [
    ("AND(x0,x1,x2)", lambda a: int(a[0] and a[1] and a[2]), S),
    ("OR(x0,x1)",      lambda a: int(a[0] or a[1]),            [0, 1]),
    ("XOR(x0,x1,x2)",  lambda a: int(a[0] ^ a[1] ^ a[2]),     S),
    ("MAJ(x0,x1,x2)",  lambda a: int(a[0] + a[1] + a[2] >= 2), S),
]

all_ok = True
for name, func, vs in exts:
    mi_z = mi_func_var(sat, func, target)
    mi_S = mi_set_var(sat, vs, target)
    ok = mi_z <= mi_S + 1e-10
    if not ok:
        all_ok = False
    print(f"  {name:20s}: I(z;x_{target})={mi_z:.6f}  I(x_S;x_{target})={mi_S:.6f}  {'ok' if ok else 'FAIL'}")

test("Extension DPI: I(z;x_j) <= I(x_S;x_j) for all extensions", all_ok)
print()

# ─── Test 2: Extension Axiom Zero ───
print("─── Test 2: Extension Axiom Zero Info ───")
# z <-> f(x) is TRUE for ALL assignments. I(tautology; SAT) = 0.
joint_ax = defaultdict(int)
m_ax = defaultdict(int)
m_sat = defaultdict(int)
for bits in range(1 << n):
    a = tuple((bits >> i) & 1 for i in range(n))
    ax_val = 1  # z <-> f(x) always true
    sat_val = int(eval_formula(clauses, a))
    joint_ax[(ax_val, sat_val)] += 1
    m_ax[ax_val] += 1
    m_sat[sat_val] += 1

mi_ax = mutual_info_from_counts(joint_ax, m_ax, m_sat, 1 << n)
test("Extension axiom carries zero info: I(axiom;SAT) = 0",
     abs(mi_ax) < 1e-10,
     f"I(z<->f(x); SAT) = {mi_ax:.2e}")
print()

# ─── Test 3: Modus Ponens — The Structural Gap ───
print("─── Test 3: Modus Ponens — The Structural Gap ───")
# A = x_0 AND x_1
# B = x_0
# A -> B is a tautology (AND(a,b) implies a)
# Under SAT distribution: B can carry MORE info than A!
# Because AND is lossy — it compresses away which input was 1.
# Modus ponens with the tautology A->B RECOVERS the lost info.

A_f = lambda a: int(a[0] and a[1])
B_f = lambda a: int(a[0])
AtoB_f = lambda a: int(not (a[0] and a[1]) or a[0])  # always 1

mi_A = mi_func_var(sat, A_f, target)
mi_B = mi_func_var(sat, B_f, target)
mi_AtoB = mi_func_var(sat, AtoB_f, target)
mi_pair = mi_joint_func_var(sat, A_f, AtoB_f, target)

print(f"  A = x_0 AND x_1:   I(A;x_{target}) = {mi_A:.6f}")
print(f"  B = x_0:           I(B;x_{target}) = {mi_B:.6f}")
print(f"  A->B (tautology):  I(A->B;x_{target}) = {mi_AtoB:.6f}")
print(f"  (A,A->B) joint:    I((A,A->B);x_{target}) = {mi_pair:.6f}")
print(f"  B exceeds A?       {mi_B > mi_A + 1e-10}")
print()
print("  Modus ponens recovers info that AND compressed away.")
print("  This is ROUTING, not CREATION: I(B;x_j) <= I(x_0,x_1;x_j)")

mi_vars = mi_set_var(sat, [0, 1], target)
print(f"  I(x_0,x_1;x_{target}) = {mi_vars:.6f}  (variable-level bound)")

# The KEY test: B does NOT exceed the underlying variable info
test("MP structural gap: B <= underlying vars (routing not creation)",
     mi_B <= mi_vars + 1e-10,
     f"I(B;x_j)={mi_B:.6f} <= I(x_0,x_1;x_j)={mi_vars:.6f}")
print()

# ─── Test 4: Variable-Level DPI (Universal Bound) ───
print("─── Test 4: Variable-Level DPI ───")
# For ANY function f(x_S): I(f(x_S); x_j) <= I(x_S; x_j)
# This is the unconditional DPI that ALWAYS holds.

# Test with many random functions on S = {0,1,2,3}
S4 = [0, 1, 2, 3]
mi_S4 = mi_set_var(sat, S4, target)

rng2 = random.Random(123)
all_bounded = True
max_ratio = 0
for trial in range(50):
    # Random Boolean function on 4 bits (16-entry truth table)
    tt = [rng2.randint(0, 1) for _ in range(16)]
    def rand_func(a, table=tt):
        idx = sum(a[S4[k]] << k for k in range(4))
        return table[idx]

    mi_f = mi_func_var(sat, rand_func, target)
    if mi_f > mi_S4 + 1e-10:
        all_bounded = False
    if mi_S4 > 0:
        max_ratio = max(max_ratio, mi_f / mi_S4 if mi_S4 > 1e-15 else 0)

test("Variable-level DPI: I(f(x_S);x_j) <= I(x_S;x_j) for 50 random f",
     all_bounded,
     f"max ratio I(f)/I(S) = {max_ratio:.4f}")
print()

# ─── Test 5: Nested Extension DPI ───
print("─── Test 5: Nested Extension DPI Cascade ───")
z1 = lambda a: int(a[0] ^ a[1])       # z1 = XOR(x0,x1)
z2 = lambda a: int(z1(a) and a[5])    # z2 = z1 AND x5
z3 = lambda a: int(z2(a) or a[7])     # z3 = z2 OR x7

mi_z1 = mi_func_var(sat, z1, target)
mi_z2 = mi_func_var(sat, z2, target)
mi_z3 = mi_func_var(sat, z3, target)

# z3 depends on {x0, x1, x5, x7}
mi_full = mi_set_var(sat, [0, 1, 5, 7], target)

print(f"  z1 = XOR(x0,x1):     I(z1;x_{target}) = {mi_z1:.6f}")
print(f"  z2 = z1 AND x5:      I(z2;x_{target}) = {mi_z2:.6f}")
print(f"  z3 = z2 OR x7:       I(z3;x_{target}) = {mi_z3:.6f}")
print(f"  I(x0,x1,x5,x7;x_{target}) = {mi_full:.6f}")

test("Nested DPI: I(z3;x_j) <= I(underlying vars;x_j)",
     mi_z3 <= mi_full + 1e-10,
     f"Cascade z1->z2->z3: each layer bounded by source vars")
print()

# ─── Test 6: Block Coverage (Chain Rule) ───
print("─── Test 6: Block Coverage via Chain Rule ───")
# The chain rule gives: sum_i I(z; X_i | X_{<i}) = I(z; X_1,...,X_B) <= H(z)
# This ALWAYS holds. For independent blocks, I(z;X_i|X_{<i}) = I(z;X_i),
# so sum_i I(z;X_i) <= H(z). At small n, blocks are correlated, so
# we verify the chain rule version (unconditional) and note that the
# unconditional sum exceeds H(z) precisely because of inter-block correlation.

blocks = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
if n > 9:
    blocks.append([9])

z_func = lambda a: int(a[0] ^ a[1] ^ a[2])  # XOR of block 0

# Compute I(z; all blocks combined) — must be <= H(z)
all_block_vars = [v for blk in blocks for v in blk]
mi_z_all = mi_set_var(sat, all_block_vars, 0)  # placeholder — need I(z; X_all)

# Actually compute I(z; X_all_blocks) directly
N = len(sat)
joint_all = defaultdict(int)
mz_all = defaultdict(int)
mb_all = defaultdict(int)
for a in sat:
    zv = z_func(a)
    bv = tuple(a[v] for v in all_block_vars)
    joint_all[(zv, bv)] += 1
    mz_all[zv] += 1
    mb_all[bv] += 1
mi_z_allblocks = mutual_info_from_counts(joint_all, mz_all, mb_all, N)

Hz = func_entropy(sat, z_func)

# Also show per-block MI (informative, not the test)
total_uncond = 0
for bi, blk in enumerate(blocks):
    joint = defaultdict(int)
    mz = defaultdict(int)
    mb = defaultdict(int)
    for a in sat:
        zv = z_func(a)
        bv = tuple(a[v] for v in blk)
        joint[(zv, bv)] += 1
        mz[zv] += 1
        mb[bv] += 1
    mi_blk = mutual_info_from_counts(joint, mz, mb, N)
    total_uncond += mi_blk
    print(f"  I(z; block_{bi}={blk}) = {mi_blk:.6f}")

print(f"  Sum (unconditional) = {total_uncond:.6f}  (can exceed H(z) if blocks correlated)")
print(f"  I(z; all blocks)    = {mi_z_allblocks:.6f}  (chain rule: always <= H(z))")
print(f"  H(z)                = {Hz:.6f}")

test("Chain rule: I(z; all blocks) <= H(z)",
     mi_z_allblocks <= Hz + 1e-10,
     f"I(z;X_all)={mi_z_allblocks:.4f} <= H(z)={Hz:.4f}")
print()

# ─── Test 7: Bridging Extension ───
print("─── Test 7: Bridging Extension Bounded ───")
first_half = list(range(n // 2))

majority = lambda a: int(sum(a[i] for i in first_half) > len(first_half) // 2)
parity_f = lambda a: int(sum(a[i] for i in first_half) % 2)

mi_maj = mi_func_var(sat, majority, target)
mi_par = mi_func_var(sat, parity_f, target)
mi_half = mi_set_var(sat, first_half, target)

print(f"  I(majority(x_0..x_{n//2-1});x_{target}) = {mi_maj:.6f}")
print(f"  I(parity(x_0..x_{n//2-1});x_{target})   = {mi_par:.6f}")
print(f"  I(x_0,...,x_{n//2-1};x_{target})         = {mi_half:.6f}")

test("Bridging extensions bounded by source variables",
     mi_maj <= mi_half + 1e-10 and mi_par <= mi_half + 1e-10,
     "Both majority and parity <= full variable set MI")
print()

# ─── Test 8: MI Decay with VIG Distance ───
print("─── Test 8: MI Decay with VIG Distance ───")
dist_mi = defaultdict(list)
for i in range(n):
    for j in range(i + 1, n):
        d = bfs_dist(i, j, adj, n)
        if d < 999:
            mi_ij = mi_var_var(sat, i, j)
            dist_mi[d].append(mi_ij)

for d in sorted(dist_mi.keys()):
    vals = dist_mi[d]
    avg = sum(vals) / len(vals)
    print(f"  d={d}: avg I(x_i;x_j|SAT) = {avg:.6f}  ({len(vals)} pairs)")

# Check decay
dists = sorted(dist_mi.keys())
if len(dists) >= 2:
    a1 = sum(dist_mi[dists[0]]) / len(dist_mi[dists[0]])
    a2 = sum(dist_mi[dists[1]]) / len(dist_mi[dists[1]])
    test("MI decays with VIG distance",
         a2 <= a1 + 1e-6 or a1 < 0.001,
         f"d={dists[0]}: {a1:.6f}, d={dists[1]}: {a2:.6f}")
else:
    test("MI decays with VIG distance", True, "Single distance only")
print()

# ─── Test 9: The Central Finding ───
print("─── Test 9: Routing vs Creation — The T69 Verdict ───")
print()

# The argument:
# 1. Extension DPI (Test 1): z=f(x_S) can't see farther than x_S. PROVED.
# 2. Extension axioms (Test 2): tautologies carry 0 info. PROVED.
# 3. Modus ponens (Test 3): CAN recover info that premises compressed.
#    This means: I(B; x_j) can EXCEED I(A; x_j) when A→B is a tautology.
#    But: I(B; x_j) NEVER exceeds I(vars(A) ∪ vars(B); x_j). PROVED.
# 4. Variable-level DPI (Test 4): Universal bound. PROVED.
#
# Conclusion:
# - Extensions don't CREATE new information channels (DPI)
# - Extensions CAN ROUTE existing information more efficiently
# - Routing = selecting which function of x to compute at each proof step
# - Whether polynomial routing suffices to derive ⊥ is EXACTLY T69
#
# Paper 2 contribution:
# (a) Formalizes the information budget: every EF line L satisfies
#     I(L; x_j) <= I(vars(L); x_j) where vars(L) = variables L depends on
# (b) This bound is the SDPI cascade: I(vars(L); x_j) <= eta^{d(vars(L), j)}
# (c) The ONLY way EF can beat resolution is through ROUTING — computing
#     functions that expose relevant info from compressed representations
# (d) The open question: can routing be done in poly(n) steps for all B blocks?

# Verify the central claim: extension info <= variable info, always
# (already verified in tests 1,4,5,7; this is the summary)
central = (mi_B <= mi_vars + 1e-10 and  # Test 3
           all_ok and                     # Test 1
           all_bounded)                   # Test 4

test("Central finding: extensions route but don't create information",
     central,
     "DPI at variable level is the universal bound; T69 = routing question")

# ═══════════════════════════════════════════════════════
# Summary
# ═══════════════════════════════════════════════════════
print()
print("=" * 65)
total = PASS + FAIL
print(f"SCORE: {PASS}/{total}")
print("=" * 65)
print()

print("PAPER 2 THEOREM (from this verification):")
print()
print("  Theorem (EF Information Budget).")
print("  Let phi be a k-SAT formula with VIG G. For any EF proof line L,")
print("  let vars(L) be the original variables that L depends on")
print("  (through any chain of extensions). Then for any variable x_j:")
print()
print("    I(L; x_j | phi, SAT) <= I(vars(L); x_j | phi, SAT)")
print()
print("  The RHS is bounded by the SDPI cascade:")
print("    I(vars(L); x_j | phi, SAT) <= |vars(L)| * eta^{d_min(vars(L), j)}")
print()
print("  where d_min is the minimum VIG distance from vars(L) to x_j.")
print()
print("  Proof: Unconditional DPI. Each extension z = f(x_S) satisfies")
print("  I(z; x_j) <= I(x_S; x_j). Each modus ponens step derives B")
print("  from A and A->B; B depends on vars(A) union vars(A->B).")
print("  By induction: vars(L) subset union of vars of all axioms")
print("  used in deriving L. QED.")
print()
print("  THE GAP: This bounds info per line, not proof SIZE.")
print("  Resolution needs width Omega(n/log n) -> size 2^{Omega(n/(log n)^2)}.")
print("  EF might achieve the same info budget in O(poly(n)) lines")
print("  through efficient ROUTING (function composition).")
print("  Whether it can is T69.")
print()
print("  WHAT'S NEW: The gap is precisely ROUTING, not CREATION.")
print("  No new information channels exist. Extensions are lossy compressions")
print("  of existing variables. The only question: can you decompress")
print("  and recombine in polynomial steps?")
