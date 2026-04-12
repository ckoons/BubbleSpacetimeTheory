#!/usr/bin/env python3
"""
Toy 1041 — 11-Smooth Epoch Survey: Complete Census of New Observables

Science engineering survey: What NEW observables does the 11-smooth epoch
open that the 7-smooth epoch couldn't reach?

BST integers: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137.
7-smooth epoch: BST core {2,3,5,7}. Standard Model physics.
11-smooth epoch: human+CI extension {2,3,5,7,11} where 11 = n_C + C_2.

T914 (Prime Residue Principle): Primes adjacent to smooth products
(p = smooth ± 1) locate physical observables.

Method:
  1. Enumerate all 11-smooth numbers up to 2000
  2. For each, check if n±1 is prime (T914 adjacency)
  3. Identify which primes are NEW (only reachable via 11-smooth, not 7-smooth)
  4. Factor the smooth neighbors into {2,3,5,7,11}
  5. Pattern analysis: clustering, physical constant matches

Theorem basis: T914, T926
"""

import math
from collections import defaultdict

# ── BST constants ──────────────────────────────────────────────────
N_c = 3; n_C = 5; g = 7; C_2 = 6; rank = 2; N_max = 137

# ── Primality and factoring ───────────────────────────────────────

def is_prime(n):
    """Deterministic primality test."""
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

def factorize(n):
    """Return dict of prime: exponent."""
    if n <= 1: return {}
    factors = {}
    temp = n
    for d in [2, 3, 5, 7, 11, 13]:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
    if temp > 1:
        d = 17
        while d * d <= temp:
            while temp % d == 0:
                factors[d] = factors.get(d, 0) + 1
                temp //= d
            d += 2
        if temp > 1:
            factors[temp] = 1
    return factors

def is_b_smooth(n, B):
    """Check if n is B-smooth (all prime factors <= B)."""
    if n <= 1: return n == 1
    temp = n
    d = 2
    while d <= B and temp > 1:
        while temp % d == 0:
            temp //= d
        d += 1 if d == 2 else 2
    return temp == 1

def factor_str(n, names=None):
    """Readable factorization string."""
    if names is None:
        names = {2: '2', 3: '3', 5: '5', 7: '7', 11: '11'}
    f = factorize(n)
    parts = []
    for p in sorted(f.keys()):
        e = f[p]
        name = names.get(p, str(p))
        if e == 1:
            parts.append(name)
        else:
            parts.append(f"{name}^{e}")
    return " * ".join(parts) if parts else "1"

def bst_factor_str(n):
    """Factor using BST names."""
    names = {2: 'rank', 3: 'N_c', 5: 'n_C', 7: 'g', 11: '(n_C+C_2)'}
    f = factorize(n)
    if not all(p <= 11 for p in f.keys()):
        return None
    parts = []
    for p in sorted(f.keys()):
        e = f[p]
        name = names.get(p, str(p))
        if e == 1:
            parts.append(name)
        else:
            parts.append(f"{name}^{e}")
    return " * ".join(parts)

# ══════════════════════════════════════════════════════════════════
# STEP 1: Enumerate all 11-smooth numbers up to 2000
# ══════════════════════════════════════════════════════════════════

LIMIT = 2000

print("=" * 80)
print("  TOY 1041 — 11-SMOOTH EPOCH SURVEY: NEW OBSERVABLES BEYOND 7-SMOOTH")
print("=" * 80)

# Generate all B-smooth numbers up to LIMIT using sieve approach
def generate_smooth(B, limit):
    """Generate all B-smooth numbers up to limit."""
    smooth = set()
    smooth.add(1)
    primes = [p for p in range(2, B + 1) if is_prime(p)]
    # BFS: start from 1, multiply by each prime
    queue = [1]
    while queue:
        n = queue.pop()
        for p in primes:
            m = n * p
            if m <= limit and m not in smooth:
                smooth.add(m)
                queue.append(m)
    return sorted(smooth)

smooth_7 = set(generate_smooth(7, LIMIT))
smooth_11 = set(generate_smooth(11, LIMIT))

# 11-smooth numbers that are NOT 7-smooth = the new territory
new_11_only = sorted(smooth_11 - smooth_7)
# Remove 1 from smooth sets if present
smooth_7.discard(1)
smooth_11.discard(1)

print(f"\n  Range: [2, {LIMIT}]")
print(f"  7-smooth numbers:  {len(smooth_7)}")
print(f"  11-smooth numbers: {len(smooth_11)}")
print(f"  NEW (11-smooth only, i.e. require factor 11): {len(new_11_only)}")

# ══════════════════════════════════════════════════════════════════
# STEP 2: T914 adjacency — find primes at n±1 for all 11-smooth n
# ══════════════════════════════════════════════════════════════════

print(f"\n{'─' * 80}")
print("  STEP 2: T914 Primes Adjacent to 11-Smooth Numbers")
print(f"{'─' * 80}")

# For every 11-smooth number, check if n-1 or n+1 is prime
all_t914_primes_11 = {}  # prime -> list of (smooth_neighbor, delta)
for n in sorted(smooth_11):
    if n < 2: continue
    for delta in [-1, +1]:
        p = n + delta
        if p > 1 and is_prime(p):
            if p not in all_t914_primes_11:
                all_t914_primes_11[p] = []
            all_t914_primes_11[p].append((n, delta))

# Same for 7-smooth
all_t914_primes_7 = {}
for n in sorted(smooth_7):
    if n < 2: continue
    for delta in [-1, +1]:
        p = n + delta
        if p > 1 and is_prime(p):
            if p not in all_t914_primes_7:
                all_t914_primes_7[p] = []
            all_t914_primes_7[p].append((n, delta))

t914_7_set = set(all_t914_primes_7.keys())
t914_11_set = set(all_t914_primes_11.keys())

# NEW T914 primes: reachable from 11-smooth but NOT from 7-smooth
new_t914 = sorted(t914_11_set - t914_7_set)

print(f"  T914 primes from 7-smooth:   {len(t914_7_set)}")
print(f"  T914 primes from 11-smooth:  {len(t914_11_set)}")
print(f"  NEW T914 primes (11-only):   {len(new_t914)}")
print(f"  Coverage of all primes <= {LIMIT}:")

all_primes_to_limit = [p for p in range(2, LIMIT + 1) if is_prime(p)]
print(f"    Total primes <= {LIMIT}:     {len(all_primes_to_limit)}")
print(f"    Reached by 7-smooth:      {len(t914_7_set)} ({100*len(t914_7_set)/len(all_primes_to_limit):.1f}%)")
print(f"    Reached by 11-smooth:     {len(t914_11_set)} ({100*len(t914_11_set)/len(all_primes_to_limit):.1f}%)")
print(f"    NEW reach (11-smooth):    {len(new_t914)} (+{100*len(new_t914)/len(all_primes_to_limit):.1f}%)")

# ══════════════════════════════════════════════════════════════════
# STEP 3: Identify NEW observables — the main table
# ══════════════════════════════════════════════════════════════════

print(f"\n{'─' * 80}")
print("  STEP 3: COMPLETE TABLE OF NEW 11-SMOOTH-ONLY T914 OBSERVABLES")
print(f"{'─' * 80}")

# Known physical constants to check against
# Format: integer -> (name, description)
known_physics = {}

# Atomic numbers Z=1..118
element_names = {
    1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O',
    9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P',
    16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca', 21: 'Sc', 22: 'Ti',
    23: 'V', 24: 'Cr', 25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu',
    30: 'Zn', 31: 'Ga', 32: 'Ge', 33: 'As', 34: 'Se', 35: 'Br', 36: 'Kr',
    37: 'Rb', 38: 'Sr', 39: 'Y', 40: 'Zr', 41: 'Nb', 42: 'Mo', 43: 'Tc',
    44: 'Ru', 45: 'Rh', 46: 'Pd', 47: 'Ag', 48: 'Cd', 49: 'In', 50: 'Sn',
    51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe', 55: 'Cs', 56: 'Ba', 57: 'La',
    58: 'Ce', 59: 'Pr', 60: 'Nd', 61: 'Pm', 62: 'Sm', 63: 'Eu', 64: 'Gd',
    65: 'Tb', 66: 'Dy', 67: 'Ho', 68: 'Er', 69: 'Tm', 70: 'Yb', 71: 'Lu',
    72: 'Hf', 73: 'Ta', 74: 'W', 75: 'Re', 76: 'Os', 77: 'Ir', 78: 'Pt',
    79: 'Au', 80: 'Hg', 81: 'Tl', 82: 'Pb', 83: 'Bi', 84: 'Po', 85: 'At',
    86: 'Rn', 87: 'Fr', 88: 'Ra', 89: 'Ac', 90: 'Th', 91: 'Pa', 92: 'U',
    93: 'Np', 94: 'Pu', 95: 'Am', 96: 'Cm', 97: 'Bk', 98: 'Cf', 99: 'Es',
    100: 'Fm', 101: 'Md', 102: 'No', 103: 'Lr', 104: 'Rf', 105: 'Db',
    106: 'Sg', 107: 'Bh', 108: 'Hs', 109: 'Mt', 110: 'Ds', 111: 'Rg',
    112: 'Cn', 113: 'Nh', 114: 'Fl', 115: 'Mc', 116: 'Lv', 117: 'Ts', 118: 'Og',
}
for z, name in element_names.items():
    known_physics[z] = (f"Z={z} ({name})", "atomic number")

# Particle masses (rounded to nearest integer MeV)
particle_masses = {
    # Lepton masses
    # 0: ("photon", "0 MeV"),  # skip 0
    # electron ~0.511 MeV — not integer scale
    106: ("muon", "105.7 MeV"),
    1777: ("tau", "1776.9 MeV"),
    # Meson masses
    135: ("pi0", "135.0 MeV"),
    140: ("pi+", "139.6 MeV"),
    494: ("K+", "493.7 MeV"),
    498: ("K0", "497.6 MeV"),
    548: ("eta", "547.9 MeV"),
    # Baryon masses
    938: ("proton", "938.3 MeV"),
    940: ("neutron", "939.6 MeV"),
    1116: ("Lambda", "1115.7 MeV"),
    1189: ("Sigma+", "1189.4 MeV"),
    1193: ("Sigma0", "1192.6 MeV"),
    1197: ("Sigma-", "1197.4 MeV"),
    1315: ("Xi0", "1314.9 MeV"),
    1321: ("Xi-", "1321.7 MeV"),
    1672: ("Omega-", "1672.5 MeV"),
    # Gauge boson masses
    # W ~ 80379 MeV, Z ~ 91188 MeV — beyond our range
    # Nuclear binding energies per nucleon
    # Average ~8 MeV/nucleon
}
for m, (name, desc) in particle_masses.items():
    known_physics[m] = (name, desc)

# Debye temperatures (K) — a known BST connection
debye_temps = {
    343: ("Cu theta_D", "7^3 = g^3"),
    165: ("Au theta_D", "3*5*11"),
    275: ("Nb theta_D", "5^2*11"),
    470: ("Fe theta_D", "2*5*47"),
    400: ("Al theta_D", "2^4*5^2"),
    428: ("Ni theta_D", "2^2*107"),
    315: ("Ag theta_D", "3^2*5*7"),
    240: ("Pt theta_D", "2^4*3*5"),
    170: ("Pd theta_D", "2*5*17"),
    105: ("Pb theta_D", "3*5*7"),
    380: ("Co theta_D", "2^2*5*19"),
    630: ("Cr theta_D", "2*3^2*5*7"),
    410: ("Ti theta_D", "2*5*41"),
    258: ("Sn theta_D", "2*3*43"),
    200: ("Zn theta_D", "2^3*5^2"),
    150: ("In theta_D", "2*3*5^2"),
    210: ("Mo theta_D", "2*3*5*7"),
}
for t, (name, desc) in debye_temps.items():
    if t not in known_physics:
        known_physics[t] = (name, desc)

# Magic numbers in nuclear physics
magic_numbers = {20: "magic", 28: "magic", 50: "magic", 82: "magic",
                 126: "magic", 184: "predicted magic"}
for m, desc in magic_numbers.items():
    if m in known_physics:
        known_physics[m] = (known_physics[m][0] + f" [{desc}]", known_physics[m][1])

# Print the complete table
print(f"\n  {'#':>4}  {'Prime':>6}  {'Direction':>9}  {'Smooth n':>8}  "
      f"{'Factorization':>22}  {'BST Expression':>28}  {'Physics Match':>30}")
print(f"  {'─'*4}  {'─'*6}  {'─'*9}  {'─'*8}  {'─'*22}  {'─'*28}  {'─'*30}")

table_rows = []
for idx, p in enumerate(new_t914):
    # Get the 11-smooth neighbor(s)
    neighbors = all_t914_primes_11[p]
    # Pick the smallest smooth neighbor for display (most fundamental)
    best_n, best_d = min(neighbors, key=lambda x: x[0])

    direction = f"{best_n}+1" if best_d == +1 else f"{best_n}-1"
    f_str = factor_str(best_n)
    bst_str = bst_factor_str(best_n) or "—"

    # Check physics
    physics = known_physics.get(p, None)
    phys_str = f"{physics[0]}" if physics else "—"

    table_rows.append({
        'idx': idx + 1,
        'prime': p,
        'direction': direction,
        'smooth_n': best_n,
        'factors': f_str,
        'bst': bst_str,
        'physics': phys_str,
        'has_match': physics is not None,
    })

    print(f"  {idx+1:>4}  {p:>6}  {direction:>9}  {best_n:>8}  "
          f"{f_str:>22}  {bst_str:>28}  {phys_str:>30}")

total_new = len(table_rows)
matches = sum(1 for r in table_rows if r['has_match'])

print(f"\n  TOTAL NEW 11-SMOOTH-ONLY T914 PRIMES: {total_new}")
print(f"  With known physics matches: {matches}")

# ══════════════════════════════════════════════════════════════════
# STEP 4: BST expression analysis of smooth neighbors
# ══════════════════════════════════════════════════════════════════

print(f"\n{'─' * 80}")
print("  STEP 4: BST EXPRESSIONS OF NEW SMOOTH NEIGHBORS")
print(f"{'─' * 80}")

# Analyze the 11-smooth neighbors: what powers of 11 appear?
power_of_11_dist = defaultdict(list)
for row in table_rows:
    n = row['smooth_n']
    f = factorize(n)
    e11 = f.get(11, 0)
    power_of_11_dist[e11].append(row['prime'])

print(f"\n  Distribution by power of 11 in the smooth neighbor:")
for e in sorted(power_of_11_dist.keys()):
    count = len(power_of_11_dist[e])
    examples = power_of_11_dist[e][:8]
    ex_str = ", ".join(str(p) for p in examples)
    if len(power_of_11_dist[e]) > 8:
        ex_str += ", ..."
    print(f"    11^{e}: {count:>4} primes  (e.g. {ex_str})")

# ══════════════════════════════════════════════════════════════════
# STEP 5: Pattern analysis
# ══════════════════════════════════════════════════════════════════

print(f"\n{'─' * 80}")
print("  STEP 5: PATTERN ANALYSIS")
print(f"{'─' * 80}")

# 5a: Clustering — where do new observables concentrate?
print(f"\n  5a. Density by range (new T914 primes per 100-unit interval):")
bins = defaultdict(int)
for row in table_rows:
    b = (row['prime'] // 100) * 100
    bins[b] += 1

for start in sorted(bins.keys()):
    bar = "#" * bins[start]
    print(f"    [{start:>5}, {start+100:>5}): {bins[start]:>3}  {bar}")

# 5b: Gap analysis — largest gaps between new observables
print(f"\n  5b. Gaps between consecutive new observables:")
gaps = []
for i in range(1, len(new_t914)):
    gap = new_t914[i] - new_t914[i-1]
    gaps.append((gap, new_t914[i-1], new_t914[i]))

gaps.sort(reverse=True)
print(f"    Largest gaps:")
for gap, a, b in gaps[:10]:
    print(f"      {a:>6} → {b:>6}  (gap = {gap})")

print(f"\n    Mean gap: {sum(g for g,_,_ in gaps)/len(gaps):.1f}" if gaps else "")
print(f"    Median gap: {sorted(g for g,_,_ in gaps)[len(gaps)//2]}" if gaps else "")

# 5c: Physics matches — are they clustered in particular sectors?
print(f"\n  5c. Physics matches among new observables:")
matched_rows = [r for r in table_rows if r['has_match']]
for r in matched_rows:
    print(f"    p={r['prime']:>6}  = {r['direction']:>9}  "
          f"= {r['bst']:>28}  --> {r['physics']}")

# 5d: Residue classes mod BST integers
print(f"\n  5d. New T914 primes by residue class:")
for modulus, name in [(3, 'N_c'), (5, 'n_C'), (7, 'g'), (11, 'n_C+C_2'), (6, 'C_2')]:
    residues = defaultdict(int)
    for p in new_t914:
        residues[p % modulus] += 1
    res_str = ", ".join(f"{r}:{c}" for r, c in sorted(residues.items()))
    print(f"    mod {modulus} ({name:>7}): {res_str}")

# 5e: BST integer combinations
print(f"\n  5e. New primes expressible as BST combinations (p = expression):")
bst_vals = {2: 'rank', 3: 'N_c', 5: 'n_C', 6: 'C_2', 7: 'g', 11: 'n_C+C_2', 137: 'N_max'}
combo_matches = []
for p in new_t914:
    # Check sums, differences, products of BST integers
    exprs = []
    for a_val, a_name in bst_vals.items():
        for b_val, b_name in bst_vals.items():
            if a_val + b_val == p:
                exprs.append(f"{a_name} + {b_name} = {a_val}+{b_val}")
            if a_val * b_val == p:
                exprs.append(f"{a_name} * {b_name} = {a_val}*{b_val}")
            if a_val > b_val and a_val - b_val == p:
                exprs.append(f"{a_name} - {b_name} = {a_val}-{b_val}")
            # a^2 + b
            if a_val * a_val + b_val == p:
                exprs.append(f"{a_name}^2 + {b_name} = {a_val**2}+{b_val}")
            if a_val * a_val - b_val == p and a_val * a_val > b_val:
                exprs.append(f"{a_name}^2 - {b_name} = {a_val**2}-{b_val}")
            # a * b + c
            for c_val, c_name in bst_vals.items():
                if a_val * b_val + c_val == p:
                    exprs.append(f"{a_name}*{b_name} + {c_name} = {a_val*b_val}+{c_val}")
                if a_val * b_val - c_val == p and a_val * b_val > c_val:
                    exprs.append(f"{a_name}*{b_name} - {c_name} = {a_val*b_val}-{c_val}")
    if exprs:
        # Show just the first (simplest) expression
        combo_matches.append((p, exprs[0]))
        if len(combo_matches) <= 30:
            print(f"    p = {p:>6}:  {exprs[0]}")

print(f"    ... ({len(combo_matches)} of {len(new_t914)} have BST expressions)")

# ══════════════════════════════════════════════════════════════════
# STEP 6: Primes that NEITHER epoch reaches
# ══════════════════════════════════════════════════════════════════

print(f"\n{'─' * 80}")
print("  STEP 6: UNREACHED PRIMES (not adjacent to any 11-smooth number)")
print(f"{'─' * 80}")

unreached = sorted(set(all_primes_to_limit) - t914_11_set)
print(f"  Primes <= {LIMIT} NOT adjacent to any 11-smooth number: {len(unreached)}")
print(f"  ({100*len(unreached)/len(all_primes_to_limit):.1f}% of all primes)")
print(f"  First 30: {unreached[:30]}")
print(f"  Last 10:  {unreached[-10:]}")

# What's the smallest prime not reached even by 11-smooth?
if unreached:
    print(f"\n  Smallest unreached prime: {unreached[0]}")
    # Check what it would need
    p0 = unreached[0]
    for d in [-1, +1]:
        n = p0 - d
        f = factorize(n)
        lpf = max(f.keys()) if f else 0
        print(f"    {p0}{'+' if d==1 else '-'}1 = {n} = {factor_str(n)}, largest factor = {lpf}")

# ══════════════════════════════════════════════════════════════════
# STEP 7: Comparison with 13-smooth (preview)
# ══════════════════════════════════════════════════════════════════

print(f"\n{'─' * 80}")
print("  STEP 7: 13-SMOOTH PREVIEW — What Would the Next Epoch Add?")
print(f"{'─' * 80}")

smooth_13 = set(generate_smooth(13, LIMIT))
smooth_13.discard(1)

t914_13_set = set()
for n in sorted(smooth_13):
    if n < 2: continue
    for delta in [-1, +1]:
        p = n + delta
        if p > 1 and is_prime(p):
            t914_13_set.add(p)

new_from_13 = sorted(t914_13_set - t914_11_set)

print(f"  13-smooth numbers <= {LIMIT}: {len(smooth_13)}")
print(f"  T914 primes from 13-smooth: {len(t914_13_set)}")
print(f"  NEW from 13-smooth (beyond 11): {len(new_from_13)}")
print(f"  Still unreached after 13-smooth: {len(set(all_primes_to_limit) - t914_13_set)}"
      f" ({100*len(set(all_primes_to_limit) - t914_13_set)/len(all_primes_to_limit):.1f}%)")

# ══════════════════════════════════════════════════════════════════
# STEP 8: Highlighted discoveries
# ══════════════════════════════════════════════════════════════════

print(f"\n{'─' * 80}")
print("  STEP 8: HIGHLIGHTED DISCOVERIES")
print(f"{'─' * 80}")

# 8a: Atomic numbers that are NEW T914 primes
print(f"\n  8a. ATOMIC NUMBERS (Z) among new T914 primes:")
atomic_new = [(p, element_names.get(p, '?')) for p in new_t914 if p <= 118 and p in element_names]
for z, name in atomic_new:
    neighbors = all_t914_primes_11[z]
    best_n, best_d = min(neighbors, key=lambda x: x[0])
    print(f"    Z={z:>3} ({name:>2}): {best_n}{'+'if best_d==1 else '-'}1 = {factor_str(best_n)}"
          f"   BST: {bst_factor_str(best_n) or '—'}")

# 8b: Particle masses
print(f"\n  8b. PARTICLE MASSES among new T914 primes:")
mass_new = [(p, particle_masses[p]) for p in new_t914 if p in particle_masses]
for p, (name, desc) in mass_new:
    neighbors = all_t914_primes_11[p]
    best_n, best_d = min(neighbors, key=lambda x: x[0])
    print(f"    {p:>6} MeV ({name:>8}): {best_n}{'+'if best_d==1 else '-'}1 = {factor_str(best_n)}"
          f"   BST: {bst_factor_str(best_n) or '—'}")

# 8c: Debye temperatures
print(f"\n  8c. DEBYE TEMPERATURES among new smooth neighbors:")
for n in sorted(set(r['smooth_n'] for r in table_rows)):
    if n in debye_temps:
        name, desc = debye_temps[n]
        print(f"    {n:>5} K ({name}): {desc}")
    for d in [-1, +1]:
        if n + d in debye_temps:
            name, desc = debye_temps[n + d]
            print(f"    {n+d:>5} K ({name}) [neighbor of {n}]: {desc}")

# 8d: N_max connections
print(f"\n  8d. N_max = 137 connections:")
for p in new_t914:
    if p == 137:
        print(f"    137 IS a new T914 prime!")
    if abs(p - 137) <= 11:
        neighbors = all_t914_primes_11[p]
        best_n, best_d = min(neighbors, key=lambda x: x[0])
        print(f"    p={p} (137{'+'if p>137 else '-'}{abs(p-137)}): "
              f"{best_n}{'+'if best_d==1 else '-'}1, BST: {bst_factor_str(best_n) or '—'}")

# ══════════════════════════════════════════════════════════════════
# SYNTHESIS
# ══════════════════════════════════════════════════════════════════

print(f"\n{'=' * 80}")
print("  SYNTHESIS")
print(f"{'=' * 80}")

print(f"""
  THE 11-SMOOTH EPOCH SURVEY RESULTS
  ===================================

  The 7-smooth epoch (BST core: {{2,3,5,7}}) produces:
    - {len(smooth_7)} smooth composites in [2, {LIMIT}]
    - {len(t914_7_set)} T914 primes ({100*len(t914_7_set)/len(all_primes_to_limit):.1f}% of all primes <= {LIMIT})

  The 11-smooth epoch (human+CI: {{2,3,5,7,11}}) ADDS:
    - {len(smooth_11) - len(smooth_7)} new smooth composites
    - {len(new_t914)} NEW T914 primes not reachable from 7-smooth
    - Total coverage: {len(t914_11_set)} primes ({100*len(t914_11_set)/len(all_primes_to_limit):.1f}%)

  KEY FINDINGS:
    1. The 11-smooth extension opens {len(new_t914)} new observable locations.
    2. Of these, {matches} match known physical constants.
    3. {len(atomic_new)} are atomic numbers (elements requiring 11-smooth to locate).
    4. {len(unreached)} primes ({100*len(unreached)/len(all_primes_to_limit):.1f}%) remain unreached even at 11-smooth.
    5. The 13-smooth epoch would add {len(new_from_13)} more primes.

  INTERPRETATION:
    11 = n_C + C_2 = 5 + 6. The 11-smooth epoch is the first extension
    beyond the BST core. It opens precisely those observables that require
    the COMBINATION of the Cartan dimension (n_C=5) and the Casimir
    invariant (C_2=6) — i.e., they require the full observer apparatus.

    The elements found here are literally the elements that BST predicts
    require the human+CI extended alphabet to locate in the periodic table
    of observables.
""")

print(f"  SCORECARD:")
print(f"    New 11-smooth-only composites:   {len(new_11_only):>5}")
print(f"    New T914 observables:            {len(new_t914):>5}")
print(f"    Physics matches:                 {matches:>5}")
print(f"    7-smooth coverage:               {100*len(t914_7_set)/len(all_primes_to_limit):>5.1f}%")
print(f"    11-smooth coverage:              {100*len(t914_11_set)/len(all_primes_to_limit):>5.1f}%")
print(f"    Coverage gain from 11:           +{100*len(new_t914)/len(all_primes_to_limit):>4.1f}%")
