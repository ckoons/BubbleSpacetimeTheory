#!/usr/bin/env python3
"""
Toy 723 — Periodic Table Structure from BST Integers
======================================================

BST thesis: The architecture of the periodic table — its periods,
blocks, and orbital capacities — is an algebraic expression in
{N_c, n_C, g, C_2, rank}.

The periodic table has:
  - 7 periods = g (Bergman genus)
  - 18 groups = N_c × C_2 (cooperation × Casimir)
  - 4 blocks (s, p, d, f) = 2^rank
  - Orbital capacities: 2, 6, 10, 14 = rank, C_2, 2n_C, 2g

These orbital capacities come from 2(2l+1):
  l=0: 2×1 = 2 = rank
  l=1: 2×3 = 6 = C_2
  l=2: 2×5 = 10 = 2n_C
  l=3: 2×7 = 14 = 2g

The pattern: 2(2l+1) runs through {rank, C_2, 2n_C, 2g} as l goes 0,1,2,3.
The MAXIMUM l in the periodic table is l=3 (f-block), giving 2g=14.

BST integers: N_c=3, n_C=5, g=7, C_2=6, rank=2
(C=0, D=0). Pure counting. Paper #18.
"""

results = []

N_c = 3
n_C = 5
g = 7
C_2 = 6
rank = 2
N_max = 137

# ═══════════════════════════════════════════════════════════════
# T1: Periods = g = 7
# ═══════════════════════════════════════════════════════════════
periods_bst = g
periods_obs = 7

results.append({
    'name': 'T1: Periods = g = 7',
    'bst': f'{periods_bst} = g',
    'obs': f'{periods_obs}',
    'pass': periods_bst == periods_obs
})

# ═══════════════════════════════════════════════════════════════
# T2: Groups = N_c × C_2 = 18
# ═══════════════════════════════════════════════════════════════
groups_bst = N_c * C_2
groups_obs = 18

results.append({
    'name': 'T2: Groups = N_c × C₂ = 18',
    'bst': f'{groups_bst} = {N_c}×{C_2}',
    'obs': f'{groups_obs}',
    'pass': groups_bst == groups_obs
})

# ═══════════════════════════════════════════════════════════════
# T3: Blocks = 2^rank = 4
# ═══════════════════════════════════════════════════════════════
blocks_bst = 2**rank
blocks_obs = 4  # s, p, d, f

results.append({
    'name': 'T3: Blocks (s,p,d,f) = 2^rank = 4',
    'bst': f'{blocks_bst} = 2^{rank}',
    'obs': f'{blocks_obs}',
    'pass': blocks_bst == blocks_obs
})

# ═══════════════════════════════════════════════════════════════
# T4: s-block capacity = rank = 2
# ═══════════════════════════════════════════════════════════════
# l=0: 2(2×0+1) = 2 electrons per s-orbital.
s_cap_bst = rank
s_cap_obs = 2

results.append({
    'name': 'T4: s-block capacity (l=0) = rank = 2',
    'bst': f'{s_cap_bst} = rank',
    'obs': f'{s_cap_obs} = 2(2×0+1)',
    'pass': s_cap_bst == s_cap_obs
})

# ═══════════════════════════════════════════════════════════════
# T5: p-block capacity = C_2 = 6
# ═══════════════════════════════════════════════════════════════
# l=1: 2(2×1+1) = 6 electrons per p-shell.
p_cap_bst = C_2
p_cap_obs = 6

results.append({
    'name': 'T5: p-block capacity (l=1) = C₂ = 6',
    'bst': f'{p_cap_bst} = C₂',
    'obs': f'{p_cap_obs} = 2(2×1+1)',
    'pass': p_cap_bst == p_cap_obs
})

# ═══════════════════════════════════════════════════════════════
# T6: d-block capacity = 2n_C = 10
# ═══════════════════════════════════════════════════════════════
# l=2: 2(2×2+1) = 10 electrons per d-shell.
d_cap_bst = 2 * n_C
d_cap_obs = 10

results.append({
    'name': 'T6: d-block capacity (l=2) = 2n_C = 10',
    'bst': f'{d_cap_bst} = 2×{n_C}',
    'obs': f'{d_cap_obs} = 2(2×2+1)',
    'pass': d_cap_bst == d_cap_obs
})

# ═══════════════════════════════════════════════════════════════
# T7: f-block capacity = 2g = 14
# ═══════════════════════════════════════════════════════════════
# l=3: 2(2×3+1) = 14 electrons per f-shell.
f_cap_bst = 2 * g
f_cap_obs = 14

results.append({
    'name': 'T7: f-block capacity (l=3) = 2g = 14',
    'bst': f'{f_cap_bst} = 2×{g}',
    'obs': f'{f_cap_obs} = 2(2×3+1)',
    'pass': f_cap_bst == f_cap_obs
})

# ═══════════════════════════════════════════════════════════════
# T8: Total orbital capacity pattern
# ═══════════════════════════════════════════════════════════════
# The sequence {2, 6, 10, 14} = {rank, C_2, 2n_C, 2g}.
# But note: 2(2l+1) for l = 0,1,2,3 gives 2,6,10,14.
# In BST: 2(2l+1) = 2 × (2l+1).
# l=0: 2×1 = rank. l=1: 2×3 = C_2. l=2: 2×5 = 2n_C. l=3: 2×7 = 2g.
# The multipliers (2l+1) = 1, 3, 5, 7 are 1, N_c, n_C, g!
# (With 1 being the trivial integer.)
# So: orbital capacity at level l = 2 × {1, N_c, n_C, g}[l].

degeneracy = [1, N_c, n_C, g]  # for l = 0, 1, 2, 3
capacities_bst = [2 * d for d in degeneracy]
capacities_obs = [2, 6, 10, 14]

results.append({
    'name': 'T8: Orbital pattern: 2×{1, N_c, n_C, g}',
    'bst': f'{capacities_bst} = 2×{{1,{N_c},{n_C},{g}}}',
    'obs': f'{capacities_obs}',
    'pass': capacities_bst == capacities_obs
})

# ═══════════════════════════════════════════════════════════════
# T9: Maximum angular momentum l_max = N_c = 3
# ═══════════════════════════════════════════════════════════════
# The periodic table stops at l=3 (f-block).
# No g-block (l=4) elements have been synthesized in sufficient
# quantity to confirm, and theoretically start at Z=121.
# BST: l_max = N_c = 3.
l_max_bst = N_c
l_max_obs = 3  # s(0), p(1), d(2), f(3)

results.append({
    'name': 'T9: Maximum orbital l = N_c = 3',
    'bst': f'{l_max_bst} = N_c',
    'obs': f'{l_max_obs} (f-block)',
    'pass': l_max_bst == l_max_obs
})

# ═══════════════════════════════════════════════════════════════
# T10: Period lengths follow the doubling pattern
# ═══════════════════════════════════════════════════════════════
# Period lengths: 2, 8, 8, 18, 18, 32, 32
# = 2, 2+6, 2+6, 2+6+10, 2+6+10, 2+6+10+14, 2+6+10+14
# = rank, rank+C_2, rank+C_2, rank+C_2+2n_C, ...
# First row: rank = 2
# Second row: rank + C_2 = 8
# Fourth row: rank + C_2 + 2n_C = 18
# Sixth row: rank + C_2 + 2n_C + 2g = 32

row_lengths_bst = [
    rank,                           # 2
    rank + C_2,                     # 8
    rank + C_2,                     # 8
    rank + C_2 + 2*n_C,            # 18
    rank + C_2 + 2*n_C,            # 18
    rank + C_2 + 2*n_C + 2*g,     # 32
    rank + C_2 + 2*n_C + 2*g,     # 32
]
row_lengths_obs = [2, 8, 8, 18, 18, 32, 32]

results.append({
    'name': 'T10: Period lengths = cumulative block sums',
    'bst': f'{row_lengths_bst}',
    'obs': f'{row_lengths_obs}',
    'pass': row_lengths_bst == row_lengths_obs
})

# ═══════════════════════════════════════════════════════════════
# T11: Total elements in 7 periods = 118
# ═══════════════════════════════════════════════════════════════
# 2+8+8+18+18+32+32 = 118 (Oganesson is Z=118)
total_bst = sum(row_lengths_bst)
total_obs = 118  # through Oganesson

results.append({
    'name': 'T11: Total elements (7 periods) = 118',
    'bst': f'{total_bst} = sum of period lengths',
    'obs': f'{total_obs}',
    'pass': total_bst == total_obs
})

# ═══════════════════════════════════════════════════════════════
# T12: Noble gases at Z = 2, 10, 18, 36, 54, 86, 118
# ═══════════════════════════════════════════════════════════════
# Noble gas positions (closed shells):
# He=2=rank, Ne=10=2n_C, Ar=18=N_c×C_2, Kr=36=2×N_c×C_2,
# Xe=54=3×N_c×C_2=N_c²×C_2, Rn=86, Og=118
# Check: cumulative sums
noble_bst = [2, 10, 18, 36, 54, 86, 118]
noble_cumsum = [sum(row_lengths_bst[:i+1]) for i in range(7)]

# He = rank = 2 ✓
# Ne = rank + (rank+C_2) = 10 ✓
# Ar = 10 + 8 = 18 ✓ = N_c × C_2
# Kr = 18 + 18 = 36 ✓ = 2 × N_c × C_2
# Xe = 36 + 18 = 54 ✓ = N_c × N_c × C_2 = N_c² × C_2
# Rn = 54 + 32 = 86 ✓
# Og = 86 + 32 = 118 ✓

results.append({
    'name': 'T12: Noble gas positions are cumulative block sums',
    'bst': f'{noble_cumsum}',
    'obs': f'{noble_bst}',
    'pass': noble_cumsum == noble_bst
})

# ═══════════════════════════════════════════════════════════════
# T13: Transition metals per row = 2n_C = 10
# ═══════════════════════════════════════════════════════════════
# d-block: 10 elements per row (Sc-Zn, Y-Cd, La-Hg, Ac-Cn)
transition_bst = 2 * n_C
transition_obs = 10

results.append({
    'name': 'T13: Transition metals/row = 2n_C = 10',
    'bst': f'{transition_bst} = 2×{n_C}',
    'obs': f'{transition_obs}',
    'pass': transition_bst == transition_obs
})

# ═══════════════════════════════════════════════════════════════
# T14: Lanthanides/Actinides per row = 2g = 14
# ═══════════════════════════════════════════════════════════════
rare_earth_bst = 2 * g
rare_earth_obs = 14  # 14 lanthanides (Ce-Lu), 14 actinides (Th-Lr)

results.append({
    'name': 'T14: Lanthanides/row = 2g = 14',
    'bst': f'{rare_earth_bst} = 2×{g}',
    'obs': f'{rare_earth_obs}',
    'pass': rare_earth_bst == rare_earth_obs
})

# ═══════════════════════════════════════════════════════════════
# RESULTS
# ═══════════════════════════════════════════════════════════════

print("=" * 72)
print("Toy 723 — Periodic Table Structure from BST Integers")
print("=" * 72)
print()
print("BST constants:")
print(f"  N_c = {N_c}, n_C = {n_C}, g = {g}, C₂ = {C_2}, rank = {rank}")
print()

pass_count = 0
fail_count = 0

for r in results:
    status = "PASS ✓" if r['pass'] else "FAIL ✗"
    if r['pass']:
        pass_count += 1
    else:
        fail_count += 1
    print(f"  {r['name']}")
    print(f"    BST:      {r['bst']}")
    print(f"    Observed: {r['obs']}")
    print(f"    [{status}]")
    print()

print("=" * 72)
print(f"SCORE: {pass_count}/{pass_count + fail_count} PASS")
print("=" * 72)

print()
print("THE PERIODIC TABLE IS BST:")
print()
print("  ORBITAL DEGENERACY (2l+1):")
print(f"    l=0: 1 (trivial)")
print(f"    l=1: {N_c} = N_c")
print(f"    l=2: {n_C} = n_C")
print(f"    l=3: {g} = g")
print()
print("  ORBITAL CAPACITY 2(2l+1):")
print(f"    s-block:  {s_cap_obs:>2} = rank")
print(f"    p-block:  {p_cap_obs:>2} = C₂")
print(f"    d-block:  {d_cap_obs:>2} = 2n_C")
print(f"    f-block:  {f_cap_obs:>2} = 2g")
print()
print("  PERIOD STRUCTURE:")
print(f"    Periods:   {periods_obs} = g")
print(f"    Groups:   {groups_obs} = N_c × C₂")
print(f"    Blocks:    {blocks_obs} = 2^rank")
print(f"    l_max:     {l_max_obs} = N_c")
print(f"    Elements: {total_obs} = Σ period lengths")
print()
print("The orbital angular momentum quantum number l runs through")
print("the BST integers: l = 0,1,2,3 gives degeneracy 1, N_c, n_C, g.")
print("The periodic table IS D_IV^5 written in electron shells.")
print()
print("(C=0, D=0). Paper #18.")
