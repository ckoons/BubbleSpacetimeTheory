"""
Toy 2712 — Null-model test for BST integer ring (Keeper Idea 1, Cal-flagged).

Owner: Elie (compute), Grace (analysis when she's free)
Date: 2026-05-16

PURPOSE
=======
Cal has flagged this defensive concern multiple times. The structural question:

  "Are BST's integers SPECIAL, or would any 5-generator ring of small integers
   produce comparable match-counts against SM observables?"

PROTOCOL
========
1. Define ~50 SM/cosmology observables (dimensionless values)
2. For BST ring with generators {2, 3, 5, 6, 7}:
   - Enumerate all rationals a/b · c^d / e where each from generator set + small
     numerator/denominator factors
   - Count matches at <2% for each observable
3. For 1000 RANDOM rings with 5 generators from [2, 13]:
   - Same enumeration and count
4. Report BST's percentile in distribution

EXPECTATIONS
============
BST should sit at 99th+ percentile if claim "BST integers are special" is right.
If in the bulk, framing must adjust to "BST integers are sufficient."

Either result closes the longest-standing referee objection.
"""
import random
import itertools

BST_GEN = [2, 3, 5, 6, 7]  # BST 5 integers
RANGE_MIN, RANGE_MAX = 2, 13  # random ring generator range

# OBSERVABLES (dimensionless, sub-2% precision known)
# Format: (label, observed_value, BST-known-match optional)
OBSERVABLES = [
    # Particle physics
    ("sin²θ_W", 0.2312),
    ("cos²θ_W", 0.7688),
    ("m_d/m_u", 2.162),
    ("m_s/m_d", 20.00),
    ("m_s/m_u", 43.24),
    ("m_c/m_s", 13.63),
    ("m_b/m_c", 3.286),
    ("m_t/m_b", 41.26),
    ("m_τ/m_μ", 16.82),
    ("m_μ/m_e", 206.77),
    ("m_p/m_e", 1836.15),
    ("m_W/m_Z (1-sin²θ_W)", 0.7688),
    # Cosmology
    ("Y_p (BBN He-4)", 0.2453),
    ("n_s scalar tilt", 0.9649),
    ("Ω_DM/Ω_B", 5.408),
    ("Ω_Λ", 0.685),
    ("Ω_m/Ω_Λ", 0.460),
    ("eta_B exp", -21.21),  # log_e(eta_B/baseline)
    ("N_eff (neutrinos)", 3.046),
    ("Δm²_atm/sol", 33.33),
    # QED
    ("1/α", 137.036),
    ("α³ A_3", 24.05),
    ("α⁴ A_4", 130.879),
    ("α⁵ A_5", 752.6),
    # Z partial widths
    ("BR(Z→νν)", 0.2000),
    ("BR(Z→had)", 0.6988),
    ("BR(Z→lep)", 0.1010),
    # Higgs
    ("BR(H→bb)", 0.582),
    ("BR(H→ττ)", 0.0627),
    ("BR(H→γγ)", 0.00227),
    ("Γ_H/m_H", 3.25e-5),
    # Nuclear / atomic
    ("μ_p (Bohr units)", 2.7928),
    ("μ_n (Bohr units)", -1.9130),
    ("Li-11/Li-9 radius", 1.417),
    ("Z=120 magic", 120.0),
    ("Z_max stable ~92", 92.0),
    # Gravity / GW
    ("GW150914 mass", 62.0),
    ("GW190521 mass", 142.0),
    ("PI lower edge", 50.0),
    ("PI upper edge", 130.0),
    # CMB
    ("CMB acoustic l1", 220.0),
    ("CMB acoustic l2", 540.0),
    # Atomic
    ("Ionization H (eV)", 13.606),
    ("Rydberg/Hartree", 0.5),
    # Math
    ("Catalan C_5", 42.0),
    ("Heegner 163", 163.0),
    ("Bernoulli B_6 denom", 42.0),
    ("π(180)", 42.0),
    ("Pell P_8", 408.0),
    ("Twin prime C2", 0.66),
    # Decay
    ("τ_μ/τ_τ ratio", 7.57e6),
    ("Cabibbo sin θ_C", 0.2253),
]

# === RING CONSTRUCTION ===
def generate_ring_values(generators, max_depth=4):
    """Generate all rational values reachable from generators with limited depth.

    Depth-4 means up to 4 generator-tokens combined via +, *, /, with small integer
    coefficients (1-3). Values returned as floats."""
    gens = list(generators)
    values = set(gens)

    # Depth 1: just generators
    # Depth 2: a±b, a*b, a/b
    # Depth 3: combine depth-1 and depth-2 results
    # Depth 4: a*b*c*d, a/(b·c·d), a/b + c/d, etc.

    # Enumerate all "monomial" forms a^p * b^q / (c^r * d^s) with small exponents
    # Plus sums/differences of these
    current = set(gens)
    for depth in range(1, max_depth):
        new_vals = set(current)
        for a in current:
            for b in gens:
                if b != 0:
                    new_vals.add(a + b)
                    new_vals.add(a - b)
                    new_vals.add(a * b)
                    if a != 0:
                        new_vals.add(b / a)
                    new_vals.add(a / b)
        # Add small-integer coefficients (1, 2, 3) for compositional richness
        for a in list(new_vals):
            for k in [1, 2, 3]:
                new_vals.add(a * k)
                new_vals.add(a / k)
        current = new_vals
        # Trim to avoid explosion
        if len(current) > 50000:
            current = set(list(current)[:50000])

    return current


def count_matches(ring_values, observables, tol=0.02):
    """Count how many observables have at least one ring value within tol."""
    matches = 0
    for label, obs in observables:
        for v in ring_values:
            if v != 0 and obs != 0:
                if abs(v - obs)/abs(obs) < tol:
                    matches += 1
                    break
            elif obs == 0 and abs(v) < tol:
                matches += 1
                break
    return matches


# === BST RING ===
print("="*70)
print("Toy 2712 — Null-model test for BST integer ring")
print("="*70)
print()

print(f"BST GENERATORS: {BST_GEN}")
print(f"Observables to test: {len(OBSERVABLES)}")
print()

print(f"Generating BST ring (depth 4)...")
bst_ring = generate_ring_values(BST_GEN, max_depth=4)
print(f"  Ring size: {len(bst_ring)} distinct values")
bst_matches = count_matches(bst_ring, OBSERVABLES, tol=0.02)
print(f"  BST matches: {bst_matches}/{len(OBSERVABLES)}")
print()

# === RANDOM RINGS ===
print(f"Generating 1000 random rings (5 generators each, range [2,13])...")
random.seed(42)
random_match_counts = []
for trial in range(1000):
    rand_gens = random.sample(range(RANGE_MIN, RANGE_MAX + 1), 5)
    ring = generate_ring_values(rand_gens, max_depth=4)
    m = count_matches(ring, OBSERVABLES, tol=0.02)
    random_match_counts.append((tuple(sorted(rand_gens)), m))
    if (trial+1) % 100 == 0:
        print(f"  trial {trial+1}/1000: latest gen={sorted(rand_gens)}, matches={m}")

# === ANALYSIS ===
random_matches = sorted([m for _, m in random_match_counts])
n = len(random_matches)
n_below = sum(1 for m in random_matches if m < bst_matches)
n_at = sum(1 for m in random_matches if m == bst_matches)
n_above = sum(1 for m in random_matches if m > bst_matches)
bst_percentile = (n_below + n_at/2) / n * 100

print()
print("="*70)
print("RESULTS")
print("="*70)
print()
print(f"BST match count: {bst_matches}/{len(OBSERVABLES)}")
print()
print(f"RANDOM RING DISTRIBUTION (1000 trials):")
print(f"  Min:    {random_matches[0]}")
print(f"  25%:    {random_matches[n//4]}")
print(f"  Median: {random_matches[n//2]}")
print(f"  75%:    {random_matches[3*n//4]}")
print(f"  90%:    {random_matches[9*n//10]}")
print(f"  95%:    {random_matches[19*n//20]}")
print(f"  99%:    {random_matches[99*n//100]}")
print(f"  Max:    {random_matches[-1]}")
print(f"  Mean:   {sum(random_matches)/n:.2f}")
print()
print(f"  BST percentile: {bst_percentile:.2f}%")
print(f"  BST sits above {n_below} / {n} = {n_below/n*100:.1f}% of random rings")
print(f"  BST ties with {n_at} random rings")
print(f"  BST below {n_above} / {n} = {n_above/n*100:.1f}% of random rings")
print()

# === TOP-MATCHING RANDOM RINGS ===
top_rings = sorted(random_match_counts, key=lambda x: -x[1])[:10]
print("TOP 10 RANDOM RINGS:")
for gen, m in top_rings:
    print(f"  matches={m}: generators={list(gen)}")
print()

# === BST GENERATORS IN TOP RINGS ===
overlap_count = 0
for gen, m in top_rings:
    if set(gen) == set(BST_GEN):
        overlap_count += 1
print(f"BST set {{2,3,5,6,7}} in top 10: {overlap_count}")
print()

# === HEADLINE ===
print("="*70)
if bst_percentile >= 99:
    headline = "BST IS AT 99th+ PERCENTILE — INTEGERS ARE SPECIAL"
elif bst_percentile >= 90:
    headline = "BST IS AT 90th+ PERCENTILE — strong but not unique"
elif bst_percentile >= 75:
    headline = "BST IS AT 75th+ PERCENTILE — above average, room to improve framing"
else:
    headline = "BST IN THE BULK — framing must shift to 'sufficient' not 'special'"
print(f"HEADLINE: {headline}")
print(f"Specifically: {bst_percentile:.2f}th percentile")
print("="*70)

print(f"""
NULL-MODEL ANALYSIS (Keeper Idea 1, Cal-flagged):

PROTOCOL: 1000 random 5-generator rings in [2,13], depth-4 closure,
~50 SM/cosmology/math observables, ≤2% tolerance.

BST MATCH COUNT: {bst_matches}/{len(OBSERVABLES)}
BST PERCENTILE: {bst_percentile:.2f}

INTERPRETATION:
{'  BST integers ARE SPECIAL — claim survives external null model.' if bst_percentile >= 99 else
 '  BST integers are above-average but not statistically unique in this framework.' if bst_percentile >= 75 else
 '  BST integers are at the median — framing should adjust to "sufficient."'}

CAVEAT:
  This is a SIMPLE depth-4 closure. Real BST observables use:
  - Specific BST integer combinations (rank²·c_2, c_2·g, etc.)
  - π factors (from Bergman kernel)
  - exp() factors (heat kernel coefficients)
  - α (Heegner cap normalization)
  Pure integer ring closure misses these structural elements.

EXTERNAL DEFENSE:
  Whatever the percentile, this null model is now FILED.
  Cal's repeated concern is now addressed empirically, not theoretically.
""")
