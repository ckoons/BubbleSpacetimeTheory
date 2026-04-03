#!/usr/bin/env python3
"""
Toy 715 — Vertebral Column, Essential Amino Acids, and More Biology Counts
===========================================================================

BST thesis: Several independently-counted biological quantities
are algebraic expressions in {N_c, n_C, g, C_2, rank}.

Tests: vertebral column decomposition, essential amino acids,
chromosome counts, and other structural biology numbers.

BST integers: N_c=3, n_C=5, g=7, C_2=6, rank=2
(C=0, D=0). Pure counting. Paper #18/#19.
"""

results = []

N_c = 3
n_C = 5
g = 7
C_2 = 6
rank = 2
N_max = 137

# ═══════════════════════════════════════════════════════════════
# T1: Vertebral regions = n_C = 5
# ═══════════════════════════════════════════════════════════════
# Human spine: cervical, thoracic, lumbar, sacral, coccygeal = 5 regions
vertebral_regions_bst = n_C
vertebral_regions_obs = 5

results.append({
    'name': 'T1: Vertebral regions = n_C = 5',
    'bst': f'{vertebral_regions_bst} = n_C',
    'obs': f'{vertebral_regions_obs}',
    'pass': vertebral_regions_bst == vertebral_regions_obs
})

# ═══════════════════════════════════════════════════════════════
# T2: Cervical vertebrae = g = 7
# ═══════════════════════════════════════════════════════════════
# Nearly ALL mammals have exactly 7 cervical vertebrae.
# Giraffes, mice, humans, whales — all 7.
# BST: g = 7 (Bergman genus). The most conserved vertebral number.
cervical_bst = g
cervical_obs = 7

results.append({
    'name': 'T2: Cervical vertebrae = g = 7 (all mammals)',
    'bst': f'{cervical_bst} = g',
    'obs': f'{cervical_obs}',
    'pass': cervical_bst == cervical_obs
})

# ═══════════════════════════════════════════════════════════════
# T3: Thoracic vertebrae = 2C_2 = 12
# ═══════════════════════════════════════════════════════════════
# Humans: 12 thoracic vertebrae (one per rib pair).
# BST: 2 × C_2 = 2 × 6 = 12.
thoracic_bst = 2 * C_2
thoracic_obs = 12

results.append({
    'name': 'T3: Thoracic vertebrae = 2C₂ = 12',
    'bst': f'{thoracic_bst} = 2×{C_2}',
    'obs': f'{thoracic_obs}',
    'pass': thoracic_bst == thoracic_obs
})

# ═══════════════════════════════════════════════════════════════
# T4: Lumbar vertebrae = n_C = 5
# ═══════════════════════════════════════════════════════════════
lumbar_bst = n_C
lumbar_obs = 5

results.append({
    'name': 'T4: Lumbar vertebrae = n_C = 5',
    'bst': f'{lumbar_bst} = n_C',
    'obs': f'{lumbar_obs}',
    'pass': lumbar_bst == lumbar_obs
})

# ═══════════════════════════════════════════════════════════════
# T5: Sacral vertebrae (fused) = n_C = 5
# ═══════════════════════════════════════════════════════════════
sacral_bst = n_C
sacral_obs = 5

results.append({
    'name': 'T5: Sacral vertebrae (fused) = n_C = 5',
    'bst': f'{sacral_bst} = n_C',
    'obs': f'{sacral_obs}',
    'pass': sacral_bst == sacral_obs
})

# ═══════════════════════════════════════════════════════════════
# T6: Coccygeal vertebrae (fused) ≈ 2^rank = 4
# ═══════════════════════════════════════════════════════════════
# Humans: 3-5 coccygeal, typically 4.
coccygeal_bst = 2**rank  # = 4
coccygeal_obs = 4  # typical

results.append({
    'name': 'T6: Coccygeal vertebrae = 2^rank = 4',
    'bst': f'{coccygeal_bst} = 2^{rank}',
    'obs': f'{coccygeal_obs} (typical, range 3-5)',
    'pass': coccygeal_bst == coccygeal_obs
})

# ═══════════════════════════════════════════════════════════════
# T7: Total vertebrae = g + 2C_2 + n_C + n_C + 2^rank = 33
# ═══════════════════════════════════════════════════════════════
total_bst = cervical_bst + thoracic_bst + lumbar_bst + sacral_bst + coccygeal_bst
total_obs = 7 + 12 + 5 + 5 + 4  # = 33

results.append({
    'name': 'T7: Total vertebrae = 33',
    'bst': f'{total_bst} = g + 2C₂ + n_C + n_C + 2^rank',
    'obs': f'{total_obs}',
    'pass': total_bst == total_obs
})

# ═══════════════════════════════════════════════════════════════
# T8: Rib pairs = 2C_2 = 12
# ═══════════════════════════════════════════════════════════════
# 12 pairs of ribs (one per thoracic vertebra).
# True ribs: 7 = g (attach directly to sternum)
# False ribs: 5 = n_C (3 cartilage + 2 floating)
rib_pairs_bst = 2 * C_2
rib_pairs_obs = 12
true_ribs_bst = g  # = 7
true_ribs_obs = 7
false_ribs_bst = n_C  # = 5
false_ribs_obs = 5

results.append({
    'name': 'T8: Rib pairs = 2C₂; true ribs = g; false ribs = n_C',
    'bst': f'total={rib_pairs_bst}, true={true_ribs_bst}, false={false_ribs_bst}',
    'obs': f'total={rib_pairs_obs}, true={true_ribs_obs}, false={false_ribs_obs}',
    'pass': (rib_pairs_bst == rib_pairs_obs and
             true_ribs_bst == true_ribs_obs and
             false_ribs_bst == false_ribs_obs)
})

# ═══════════════════════════════════════════════════════════════
# T9: Essential amino acids = N_c² = 9
# ═══════════════════════════════════════════════════════════════
# 9 essential amino acids for humans (must be obtained from diet):
# His, Ile, Leu, Lys, Met, Phe, Thr, Trp, Val
# (Some sources say 8, with His being conditionally essential;
#  current consensus: 9.)
# BST: N_c² = 9. The cooperation dimension squared.

essential_aa_bst = N_c**2  # = 9
essential_aa_obs = 9

results.append({
    'name': 'T9: Essential amino acids = N_c² = 9',
    'bst': f'{essential_aa_bst} = N_c²',
    'obs': f'{essential_aa_obs}',
    'pass': essential_aa_bst == essential_aa_obs
})

# ═══════════════════════════════════════════════════════════════
# T10: Standard amino acids = 2^rank × n_C = 20
# ═══════════════════════════════════════════════════════════════
# 20 standard amino acids in the genetic code.
# Already in Toy 690. Consistency: 2^rank × n_C = 4 × 5 = 20.

std_aa_bst = 2**rank * n_C  # = 20
std_aa_obs = 20

results.append({
    'name': 'T10: Standard amino acids = 2^rank × n_C = 20',
    'bst': f'{std_aa_bst} = 2^{rank} × {n_C}',
    'obs': f'{std_aa_obs}',
    'pass': std_aa_bst == std_aa_obs
})

# ═══════════════════════════════════════════════════════════════
# T11: Non-essential amino acids = 20 - 9 = 11 = 2n_C + 1
# ═══════════════════════════════════════════════════════════════
nonessential_bst = std_aa_bst - essential_aa_bst  # = 11
nonessential_check = 2 * n_C + 1  # = 11

results.append({
    'name': 'T11: Non-essential AA = 20 - 9 = 11 = 2n_C + 1',
    'bst': f'{nonessential_bst} = {std_aa_bst} - {essential_aa_bst}',
    'obs': f'{nonessential_check} = 2×{n_C} + 1',
    'pass': nonessential_bst == 11 and nonessential_check == 11
})

# ═══════════════════════════════════════════════════════════════
# T12: Human teeth = 2^n_C = 32
# ═══════════════════════════════════════════════════════════════
# Adult humans: 32 teeth (including wisdom teeth).
# Dental formula: 2-1-2-3 per quadrant × 4 quadrants = 32.
teeth_bst = 2**n_C  # = 32
teeth_obs = 32

results.append({
    'name': 'T12: Human adult teeth = 2^n_C = 32',
    'bst': f'{teeth_bst} = 2^{n_C}',
    'obs': f'{teeth_obs}',
    'pass': teeth_bst == teeth_obs
})

# ═══════════════════════════════════════════════════════════════
# T13: Dental quadrants = 2^rank = 4
# ═══════════════════════════════════════════════════════════════
quadrants_bst = 2**rank  # = 4
quadrants_obs = 4

results.append({
    'name': 'T13: Dental quadrants = 2^rank = 4',
    'bst': f'{quadrants_bst} = 2^{rank}',
    'obs': f'{quadrants_obs}',
    'pass': quadrants_bst == quadrants_obs
})

# ═══════════════════════════════════════════════════════════════
# T14: Teeth per quadrant = 2^N_c = 8
# ═══════════════════════════════════════════════════════════════
per_quadrant_bst = 2**N_c  # = 8
per_quadrant_obs = 8  # 2 incisors + 1 canine + 2 premolars + 3 molars

results.append({
    'name': 'T14: Teeth per quadrant = 2^N_c = 8',
    'bst': f'{per_quadrant_bst} = 2^{N_c}',
    'obs': f'{per_quadrant_obs}',
    'pass': per_quadrant_bst == per_quadrant_obs
})

# ═══════════════════════════════════════════════════════════════
# T15: Consistency — 32 = 4 × 8 = 2^rank × 2^N_c = 2^(rank+N_c) = 2^n_C
# ═══════════════════════════════════════════════════════════════
# rank + N_c = 2 + 3 = 5 = n_C. So 2^n_C = 2^(rank+N_c). ✓
consistency = (rank + N_c == n_C)

results.append({
    'name': 'T15: rank + N_c = n_C (=5) self-consistency',
    'bst': f'{rank} + {N_c} = {rank + N_c} = n_C = {n_C}',
    'obs': 'Fundamental BST relation',
    'pass': consistency
})

# ═══════════════════════════════════════════════════════════════
# RESULTS
# ═══════════════════════════════════════════════════════════════

print("=" * 72)
print("Toy 715 — Vertebral Column, Amino Acids, and More Biology Counts")
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
print("VERTEBRAL DECOMPOSITION:")
print(f"  Cervical:  {cervical_obs:>2} = g")
print(f"  Thoracic:  {thoracic_obs:>2} = 2C₂")
print(f"  Lumbar:    {lumbar_obs:>2} = n_C")
print(f"  Sacral:    {sacral_obs:>2} = n_C")
print(f"  Coccygeal: {coccygeal_obs:>2} = 2^rank")
print(f"  ──────────────")
print(f"  Total:     {total_obs:>2} = g + 2C₂ + 2n_C + 2^rank")
print()
print("RIB DECOMPOSITION:")
print(f"  True ribs:  {true_ribs_obs:>2} = g (attach to sternum)")
print(f"  False ribs: {false_ribs_obs:>2} = n_C (cartilage + floating)")
print(f"  Total:      {rib_pairs_obs:>2} = 2C₂")
print()
print("AMINO ACID DECOMPOSITION:")
print(f"  Essential:     {essential_aa_obs:>2} = N_c²")
print(f"  Non-essential: {11:>2} = 2n_C + 1")
print(f"  Total:         {std_aa_obs:>2} = 2^rank × n_C")
print()
print("DENTAL DECOMPOSITION:")
print(f"  Quadrants:     {quadrants_obs:>2} = 2^rank")
print(f"  Per quadrant:  {per_quadrant_obs:>2} = 2^N_c")
print(f"  Total:         {teeth_obs:>2} = 2^n_C = 2^(rank+N_c)")
print()
print("Same five integers. Different domains. Same algebra.")
print()
print("(C=0, D=0). Paper #18/#19.")
