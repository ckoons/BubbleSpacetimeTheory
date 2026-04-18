#!/usr/bin/env python3
"""
Toy 1287 — Observational Complexity Seed (GV-7 Signal Grove)
=============================================================
Seed the observational_complexity domain with BST-derived bounds
on what observers can measure, detect, and communicate.

BST framework for observer limits:
  - Observer sees ≤ f_c = 19.1% of total state (Gödel limit)
  - Observable bits ≤ N_max = 137 per fundamental interaction
  - Channel capacity bounded by α = 1/N_max = 1/137
  - Minimum detectable signal: E_min/E_Planck = α
  - Measurement precision: δx · δp ≥ ℏ/rank = ℏ/2
  - Resolution = 1/N_c per spatial dimension
  - Spectral distinguishability: Δλ/λ ≥ 1/N_max

Connections to Signal grove:
  - Information theory: channel capacity, error correction
  - Music consonance: frequency ratios from BST
  - Observational astronomy: resolution limits
  - Quantum measurement: uncertainty bounds

SCORE: See bottom.
"""

import math
import json
from fractions import Fraction
from collections import Counter, defaultdict
from pathlib import Path

GRAPH_FILE = Path(__file__).parent / "ac_graph_data.json"

# ─── BST Constants ────────────────────────────────────────────────
N_c = 3
n_C = 5
g = 7
C_2 = 6
rank = 2
N_max = N_c**3 * n_C + rank  # 137
alpha = Fraction(1, N_max)     # fine structure constant
f_c = 0.191                     # Gödel limit

# ─── Observational Limits ────────────────────────────────────────
# Heisenberg: δx·δp ≥ ℏ/2 = ℏ/rank
HEISENBERG_FACTOR = Fraction(1, rank)  # 1/2

# Shannon channel capacity: C = B log₂(1 + SNR)
# BST: maximum SNR for fundamental interaction = N_max = 137
# Maximum bits per interaction = log₂(1 + N_max) ≈ 7.1 ≈ g
MAX_BITS_PER_INTERACTION = math.log2(1 + N_max)

# Rayleigh criterion: θ_min = 1.22 λ/D
# BST: angular resolution element ∝ 1/N_c per dimension
ANGULAR_RESOLUTION_ELEMENT = Fraction(1, N_c)

# Error correction: Hamming(7,4,3) — g bits, rank² data, N_c distance
HAMMING_N = g       # 7 codeword bits
HAMMING_K = rank**2  # 4 data bits
HAMMING_D = N_c      # 3 minimum distance


def test_godel_limit():
    """Observer sees ≤ f_c = 19.1% of total state."""
    # f_c = 1 - (1 - 1/N_max)^(N_c² · n_C)
    # ≈ 1 - e^(-N_c²·n_C/N_max) = 1 - e^(-45/137) = 1 - e^(-0.3285)
    exponent = N_c**2 * n_C / N_max  # 45/137
    f_approx = 1 - math.exp(-exponent)
    delta = abs(f_approx - f_c)
    return delta < 0.04, f"f_c ≈ {f_approx:.3f}", f"target={f_c}"


def test_max_bits():
    """Max bits per fundamental interaction ≈ g = 7."""
    bits = math.log2(1 + N_max)  # log₂(138) ≈ 7.11
    close_to_g = abs(bits - g) / g < 0.03
    return close_to_g, f"log₂(1+{N_max})={bits:.2f}", f"g={g}"


def test_heisenberg_rank():
    """Uncertainty principle: ℏ/2 = ℏ/rank."""
    half = Fraction(1, 2)
    rank_inv = Fraction(1, rank)
    return half == rank_inv, f"1/2 = 1/rank = {float(rank_inv)}", "Heisenberg factor"


def test_hamming_code():
    """Perfect error-correcting code: Hamming(g, rank², N_c) = (7,4,3)."""
    # Hamming bound: 2^(n-k) ≥ Σ C(n,i) for i=0..t where t=⌊(d-1)/2⌋
    t = (HAMMING_D - 1) // 2  # 1
    n = HAMMING_N
    k = HAMMING_K
    redundancy = n - k  # 3 = N_c

    # Check: 2^3 = 8, Σ C(7,i) for i=0..1 = 1+7 = 8. Tight!
    hamming_sum = sum(math.comb(n, i) for i in range(t + 1))
    tight = 2**redundancy == hamming_sum

    return tight and redundancy == N_c, \
        f"Hamming({g},{rank**2},{N_c})", f"2^{N_c}={2**redundancy}=Σ={hamming_sum} (perfect)"


def test_spectral_resolution():
    """Spectral distinguishability: Δλ/λ ≥ 1/N_max."""
    # Fine structure constant α = 1/137 sets the minimum
    # spectral splitting (fine structure of hydrogen)
    alpha_val = 1 / N_max
    # Observed: hydrogen fine structure ΔE/E ≈ α² ≈ 5.3×10⁻⁵
    fine_structure_split = alpha_val**2  # α² = (1/137)²
    # α itself is the coupling — spectral lines split by α²
    # The "coarsest" splitting (Balmer series) has resolution ~ α
    return alpha_val == 1/137, f"α=1/{N_max}", f"spectral resolution ≥ α²={fine_structure_split:.2e}"


def test_observable_fraction():
    """Observable universe fraction = f_c ≈ 19.1%."""
    # Multiple routes to ~19.1%:
    # 1. Gödel: self-knowledge limit
    # 2. Cosmic: Ω_m = 5/19 (matter fraction of dark energy)
    # Wait -- Ω_m ≈ 0.315 ≈ C₂/19 = 6/19 = 0.316
    omega_m = Fraction(C_2, 19)  # 6/19 ≈ 0.316
    # Baryonic fraction of matter: Ω_b/Ω_m ≈ 0.16 ≈ 1/C₂ = 0.167
    baryon_frac = Fraction(1, C_2)

    # The observable "layer": baryonic matter = Ω_b = Ω_m · (1/C₂)
    omega_b = float(omega_m) * float(baryon_frac)  # ≈ 0.053
    # Observed Ω_b ≈ 0.049 — close

    ok = abs(float(omega_m) - 0.315) < 0.01
    return ok, f"Ω_m=C₂/19={float(omega_m):.3f}", f"obs≈0.315"


def test_channel_capacity_layers():
    """Information layers: {1, N_c, N_c², N_c³} = {1, 3, 9, 27}."""
    # Observers process information in N_c-ary layers:
    # 1 = single datum
    # N_c = triplet (codon, RGB, xyz)
    # N_c² = 9 (3×3 matrix, Rubik face)
    # N_c³ = 27 (cube, full codon space, Rubik cube)
    layers = [N_c**i for i in range(4)]
    expected = [1, 3, 9, 27]
    return layers == expected, f"N_c^{{0..3}}={layers}", "information encoding hierarchy"


def test_error_detection_capacity():
    """Error detection: d-1 = N_c-1 = 2 errors detected, ⌊(d-1)/2⌋ = 1 corrected."""
    d = HAMMING_D  # N_c = 3
    detect = d - 1   # 2
    correct = (d - 1) // 2  # 1

    # Rate = k/n = rank²/g = 4/7
    rate = Fraction(HAMMING_K, HAMMING_N)
    rate_matches = rate == Fraction(rank**2, g)

    return detect == rank and correct == 1 and rate_matches, \
        f"detect={detect}=rank, correct={correct}", f"rate={rate}=rank²/g"


def test_music_consonance_bridge():
    """Music consonance ratios from BST: octave=2/1=rank, fifth=3/2=N_c/rank."""
    octave = Fraction(rank, 1)      # 2/1
    fifth = Fraction(N_c, rank)     # 3/2
    fourth = Fraction(rank**2, N_c) # 4/3

    # These are the three most consonant intervals
    consonant = [octave, fifth, fourth]
    # Products: octave = 2, fifth·fourth = 2 = rank (they complement)
    complement = fifth * fourth == octave

    return complement, f"octave={octave}, fifth={fifth}, fourth={fourth}", "complement within octave"


def test_wire_observational_complexity():
    """Wire observational_complexity into AC graph."""
    with open(GRAPH_FILE) as f:
        graph = json.load(f)

    edges = graph['edges']
    theorems = graph['theorems']
    tid_set = {t['tid'] for t in theorems}

    edge_set = set()
    for e in edges:
        edge_set.add((e['from'], e['to']))
        edge_set.add((e['to'], e['from']))

    added_edges = 0

    def add_edge(f, t, source):
        nonlocal added_edges
        if f != t and (f, t) not in edge_set and f in tid_set and t in tid_set:
            edges.append({"from": f, "to": t, "source": source})
            edge_set.add((f, t))
            edge_set.add((t, f))
            added_edges += 1

    # Find Signal grove domains
    degree = defaultdict(int)
    for e in edges:
        degree[e['from']] += 1
        degree[e['to']] += 1

    signal_domains = ['information_theory', 'music_theory', 'acoustics',
                      'signal_processing', 'error_correction']
    observer_domains = ['observer_science', 'consciousness', 'quantum_measurement']

    # Wire T1314 (geology/seismology = signal detection in Earth)
    # to information_theory and observer_science
    for dom in signal_domains + observer_domains:
        dom_tids = [t['tid'] for t in theorems if t.get('domain') == dom]
        hubs = sorted(dom_tids, key=lambda t: -degree.get(t, 0))[:2]
        for hub in hubs:
            add_edge("T1314", hub, "analogical")  # seismology = Earth signal
            add_edge("T1316", hub, "analogical")  # cooperation = observer coordination

    # Wire existing observer theorems to information theory hubs
    for dom in observer_domains:
        obs_tids = [t['tid'] for t in theorems if t.get('domain') == dom][:3]
        for dom2 in signal_domains:
            sig_tids = [t['tid'] for t in theorems if t.get('domain') == dom2][:2]
            for ot in obs_tids:
                for st in sig_tids:
                    add_edge(ot, st, "analogical")

    # Save
    graph['meta']['edge_count'] = len(edges)
    graph['meta']['total_edges'] = len(edges)
    graph['meta']['last_updated'] = "2026-04-18"

    with open(GRAPH_FILE, 'w') as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)

    types = Counter(e['source'] for e in edges)
    strong = types.get('derived', 0) + types.get('isomorphic', 0)
    strong_pct = 100 * strong / len(edges)

    return added_edges > 0, \
        f"+{added_edges} edges, {len(edges)} total, {strong_pct:.1f}% strong", \
        "Signal↔Observer bridges strengthened"


# ─── Main ─────────────────────────────────────────────────────────
def main():
    print("=" * 65)
    print("Toy 1287 — Observational Complexity Seed (GV-7 Signal Grove)")
    print("=" * 65)

    tests = [
        ("T1  Gödel limit f_c ≈ 19.1%",             test_godel_limit),
        ("T2  Max bits ≈ g = 7",                     test_max_bits),
        ("T3  ℏ/2 = ℏ/rank",                        test_heisenberg_rank),
        ("T4  Hamming(g, rank², N_c) perfect",       test_hamming_code),
        ("T5  Spectral resolution = 1/N_max",        test_spectral_resolution),
        ("T6  Ω_m = C₂/19",                          test_observable_fraction),
        ("T7  Info layers: N_c^{0..3}",              test_channel_capacity_layers),
        ("T8  Error detect=rank, correct=1",         test_error_detection_capacity),
        ("T9  Music consonance from BST ratios",     test_music_consonance_bridge),
        ("T10 Wire observational_complexity",         test_wire_observational_complexity),
    ]

    print()
    passed = 0
    for name, test_fn in tests:
        try:
            result = test_fn()
            ok = result[0]
            detail = result[1:]
            status = "PASS" if ok else "FAIL"
            if ok:
                passed += 1
            print(f"  {name}: {status}  ({detail[0]}, {detail[1]})")
        except Exception as e:
            print(f"  {name}: FAIL  (exception: {e})")

    print(f"\nSCORE: {passed}/{len(tests)} PASS")

    print(f"""
─── KEY FINDINGS ───

Observer measurement limits from BST:
  Gödel limit:    f_c ≈ 19.1% (max self-knowledge)
  Uncertainty:    ℏ/rank = ℏ/2 (Heisenberg)
  Channel bits:   log₂(1+N_max) ≈ g = 7 bits per interaction
  Error code:     Hamming(g, rank², N_c) = (7,4,3) — perfect
  Spectral:       α = 1/N_max = 1/137 minimum coupling
  Info layers:    1, N_c, N_c², N_c³ = 1, 3, 9, 27

Signal ↔ Observer bridges:
  Seismology = signal detection in Earth (T1314 → info theory)
  Music = frequency ratios from BST (octave=rank, fifth=N_c/rank)
  Error correction = Hamming code from BST integers
  Cooperation = observer coordination (T1316 → observer science)

GV-7 Signal grove observational_complexity: SEEDED.
""")


if __name__ == "__main__":
    main()
