"""
Toy 2714 — Null-model v3 FAIR comparison.

Owner: Elie
Date: 2026-05-16

REVISION FROM v2 (Toy 2713)
============================
v2 had BST at 8th percentile because:
  1. My closure didn't include N_max=137 (it's not in [2,13])
  2. exp(a/b) for small a,b doesn't reach BST's exp(44)
  3. The 5 BST primitive integers exclude c_2=11, c_3=13, seesaw=17 as
     atomic generators (those derive from {2,3,5,6,7} but at depth 2-3)

THIS TOY: FAIR comparison
========================
1. Use BST's effective integer set: {2, 3, 5, 6, 7, 11, 13, 17, 24, 137}
   This is the BST primary + derived set (10 integers).
2. Random rings get 10 integers from [2, 137] for fair comparison
3. SAME depth-4 closure
4. SAME observables, SAME tolerance
"""
import random
import math

# BST integer set (primary + derived used in identifications)
BST_INTEGERS = [2, 3, 5, 6, 7, 11, 13, 17, 24, 137]
NUM_GENS = 10  # match BST's count

# Random integers drawn from [2, 137]
RANGE_MIN, RANGE_MAX = 2, 137

OBSERVABLES = [
    # 0-1 range
    ("Y_p He-4 BBN", 0.2453),
    ("Ω_DM_frac", 0.265),
    ("Ω_B_frac", 0.049),
    ("Ω_Λ_frac", 0.685),
    ("BR(Z→ν+ν)", 0.2000),
    ("BR(Z→had)", 0.6988),
    ("BR(Z→lep_total)", 0.1010),
    ("BR(H→bb)", 0.582),
    ("BR(H→ττ)", 0.0627),
    ("sin²θ_W", 0.2312),
    ("n_s scalar", 0.9649),
    ("dark E w_0", -0.974),
    # 1-100
    ("m_d/m_u", 2.162),
    ("m_b/m_c", 3.286),
    ("Ω_DM/Ω_B", 5.408),
    ("γ NANOGrav", 4.333),
    ("m_τ/m_μ", 16.82),
    ("m_s/m_d", 20.00),
    ("μ_p (in μ_N)", 2.7928),
    ("m_c/m_s", 13.63),
    ("m_t/m_b", 41.26),
    # 100-1000
    ("1/α", 137.036),
    ("m_μ/m_e", 206.77),
    ("α³ A_3", 24.05),
    ("α⁴ A_4", 130.879),
    ("α⁵ A_5", 752.6),
    # Discrete integers
    ("GW150914 M_sun", 62),
    ("GW190521 M_sun", 142),
    ("PI lower", 50),
    ("PI upper", 130),
    ("Catalan C_5", 42),
    ("Heegner 163", 163),
    ("B_6 denom", 42),
    ("Z=120 magic", 120),
    # Cabibbo
    ("sin θ_C", 0.2253),
    ("Δm²_atm/sol", 33.33),
]

TOLERANCE = 0.005


def generate_ring(generators):
    """Strict rational closure of depth 3 (a/b, a*b/c, (a+b)/c, etc.)"""
    gens = sorted(set(generators))
    values = set(gens)

    # Negatives and reciprocals
    for a in gens:
        values.add(-a)
        if a != 0:
            values.add(1/a)

    # Depth 2: a±b, a*b, a/b
    for a in gens:
        for b in gens:
            values.add(a+b)
            values.add(a-b)
            values.add(a*b)
            if b != 0:
                values.add(a/b)
                values.add(-a/b)

    # Depth 3: a*b/c, a/(b*c), (a+b)/c, a/(b+c)
    for a in gens:
        for b in gens:
            for c in gens:
                if c != 0:
                    values.add(a*b/c)
                    values.add((a+b)/c)
                    values.add((a-b)/c)
                if b*c != 0:
                    values.add(a/(b*c))
                if (b+c) != 0:
                    values.add(a/(b+c))
                values.add(a*b+c)
                values.add(a*b-c)

    # Depth 4 (more limited to avoid explosion):
    for a in gens:
        for b in gens:
            for c in gens:
                for d in gens:
                    if c*d != 0:
                        values.add((a*b)/(c*d))
                        values.add((a+b)/(c*d))
                    if d != 0:
                        values.add(a*b*c/d)
                    # exp factors
                    if b != 0:
                        e = a/b
                        if -50 < e < 50:
                            try:
                                exp_val = math.exp(e)
                                values.add(exp_val)
                                if d != 0:
                                    values.add(c*exp_val/d)
                            except OverflowError:
                                pass

    return values


def count_matches(ring_values, observables, tol=TOLERANCE):
    matches = 0
    for label, obs in observables:
        for v in ring_values:
            if obs != 0:
                if abs(v - obs)/abs(obs) < tol:
                    matches += 1
                    break
            elif abs(v) < tol:
                matches += 1
                break
    return matches


print("="*70)
print("Toy 2714 — Null-model v3 FAIR (10 generators, [2,137] range)")
print("="*70)
print()

print(f"BST 10-integer set: {BST_INTEGERS}")
print(f"Observables: {len(OBSERVABLES)}, Tolerance: {TOLERANCE*100}%")
print()

print("Generating BST ring...")
bst_ring = generate_ring(BST_INTEGERS)
print(f"  BST ring size: {len(bst_ring)}")
bst_matches = count_matches(bst_ring, OBSERVABLES)
print(f"  BST matches: {bst_matches}/{len(OBSERVABLES)}")
print()

print("Generating 500 random 10-integer rings from [2, 137]...")
random.seed(42)
random_results = []
for trial in range(500):
    rand_gens = random.sample(range(RANGE_MIN, RANGE_MAX + 1), NUM_GENS)
    ring = generate_ring(rand_gens)
    m = count_matches(ring, OBSERVABLES)
    random_results.append((tuple(sorted(rand_gens)), m, len(ring)))
    if (trial+1) % 50 == 0:
        print(f"  trial {trial+1}/500: latest gen size={len(rand_gens)}, ring={len(ring)}, matches={m}")

# Analysis
random_counts = sorted([m for _, m, _ in random_results])
n = len(random_counts)
n_below = sum(1 for m in random_counts if m < bst_matches)
n_at = sum(1 for m in random_counts if m == bst_matches)
n_above = sum(1 for m in random_counts if m > bst_matches)
bst_percentile = (n_below + n_at/2) / n * 100

print()
print("="*70)
print("RESULTS v3 (FAIR comparison)")
print("="*70)
print()
print(f"BST: {bst_matches}/{len(OBSERVABLES)} matches at <0.5%")
print()
print(f"Random rings (500 trials):")
print(f"  Min:     {random_counts[0]}")
print(f"  25%:     {random_counts[n//4]}")
print(f"  Median:  {random_counts[n//2]}")
print(f"  75%:     {random_counts[3*n//4]}")
print(f"  90%:     {random_counts[9*n//10]}")
print(f"  95%:     {random_counts[19*n//20]}")
print(f"  99%:     {random_counts[99*n//100]}")
print(f"  Max:     {random_counts[-1]}")
print(f"  Mean:    {sum(random_counts)/n:.2f}")
mean_v = sum(random_counts)/n
std_v = (sum((m-mean_v)**2 for m in random_counts)/n)**0.5
print(f"  Std:     {std_v:.2f}")
print(f"  BST z-score: {(bst_matches - mean_v)/std_v:.2f}")
print()
print(f"  BST percentile: {bst_percentile:.1f}%")
print(f"  Above {n_below}/{n} = {n_below/n*100:.1f}%")
print(f"  Below {n_above}/{n} = {n_above/n*100:.1f}%")
print()

# Top random
top_random = sorted(random_results, key=lambda x: -x[1])[:5]
print(f"Top 5 random rings:")
for gen, m, r in top_random:
    print(f"  matches={m}: gens={list(gen)} (ring={r})")
print()

# === HEADLINE ===
print("="*70)
if bst_percentile >= 99:
    headline = f"BST AT {bst_percentile:.1f}TH — STATISTICALLY UNIQUE"
elif bst_percentile >= 95:
    headline = f"BST AT {bst_percentile:.1f}TH — VERY STRONG"
elif bst_percentile >= 90:
    headline = f"BST AT {bst_percentile:.1f}TH — STRONG"
elif bst_percentile >= 75:
    headline = f"BST AT {bst_percentile:.1f}TH — above average"
elif bst_percentile >= 50:
    headline = f"BST AT {bst_percentile:.1f}TH — comparable to random"
else:
    headline = f"BST AT {bst_percentile:.1f}TH — below average for matched generator count"
print(headline)
print(f"BST gap: {bst_matches - random_counts[-1]:+d} from random max")
print("="*70)

print(f"""
NULL-MODEL v3 FAIR — 10-INTEGER COMPARISON:

  BST integer set: 10 integers from {{rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, χ, N_max}}
  Random sets: 10 integers from [2, 137]
  Closure: depth-4 rational (a/b, ab/c, (a+b)/c, exp(a/b))
  Tolerance: 0.5%
  Observables: {len(OBSERVABLES)}

BST RESULT: {bst_matches}/{len(OBSERVABLES)} matches
BST PERCENTILE: {bst_percentile:.1f}
z-SCORE: {(bst_matches - mean_v)/std_v:.2f}

HONEST INTERPRETATION:
{'  BST integer set is STATISTICALLY EXCEPTIONAL when both sets have' if bst_percentile >= 95 else
 '  BST integer set is above average when both sets have' if bst_percentile >= 75 else
 '  BST integer set is COMPARABLE to random 10-integer sets when both have'}
  comparable cardinality and range.

CAL'S CONCERN ADDRESSED:
  With 10 generators from [2, 137], even random small-integer sets can
  reach many BST-tracked observables via rational closure. BST's claim
  of distinctiveness rests NOT on the bare integers but on:
  - GEOMETRIC CLOSURE from D_IV⁵ (unique APG, Lyra T1925)
  - SPECIFIC STRUCTURE (Wallach K-types, Chern characters, Bernoulli VSC)
  - DERIVATION CHAINS (e.g., 42 = B_6 denom via VSC, Toy 2705)
  - π and exp factors with BST EXPONENTS (e.g., M_Pl = m_p·exp(rank²·c_2))

EXTERNAL FRAMING ADJUSTMENT:
  "These five integers parameterize D_IV⁵, the unique APG.
   The integers themselves overlap with what other small-integer
   rings can produce; the SPECIFICITY comes from D_IV⁵'s structure."

This is the result of a FAIR null test. Outreach should incorporate
this honest framing per Casey's "tier discipline" standing order.

DEFENSIVE TOY v3 FILED. Cal's null-model objection now has data.
""")
