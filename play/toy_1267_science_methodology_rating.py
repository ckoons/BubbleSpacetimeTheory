#!/usr/bin/env python3
"""
Toy 1267 — Science Methodology Rating: Which Sciences Are Alchemy?
===================================================================
Computational classification of ~40 scientific disciplines by methodology
quality, rated on 7 axes derived from BST/AC(0) principles.

Casey's insight: "Most sciences are hodgepodge of ideas from their epoch of
creation. Chemistry isn't thermodynamics and feels like alchemy with a periodic
table. Geology isn't evolutionary. Zoology does nothing to connect animals to
their environment. Most physics since mid-19th century adopted the most complex
mathematics and tried to look smart."

Rating Axes (0-10):
  1. Mathematical rigor       — formal proofs? (10=pure math, 0=anecdotal)
  2. Predictive power         — predict new observations? (10=QED g-2, 0=none)
  3. Computational tractability — can you compute answers? (10=circuits, 0=consciousness)
  4. Internal consistency     — subfields agree? (10=thermodynamics, 0=psychology)
  5. Reductionist depth       — how far down? (10=particle physics, 0=sociology)
  6. Methodology transparency — method explicit? (10=statistics, 0=clinical medicine)
  7. Linearizability          — core in linear algebra? (10=QM, 0=ecology)

BST context: D_IV^5 = SO_0(5,2)/[SO(5)xSO(2)], five integers:
  rank=2, N_c=3, n_C=5, C_2=6, g=7

Elie — April 18, 2026

Copyright (c) 2026 Casey Koons. All rights reserved.
"""

import math

# ── BST constants ──
rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = N_c**3 * n_C + rank  # 137

passed = 0
failed = 0
total = 12


def test(n, name, condition, detail=""):
    global passed, failed
    status = "PASS" if condition else "FAIL"
    if condition:
        passed += 1
    else:
        failed += 1
    print(f"  T{n}: [{status}] {name}")
    if detail:
        print(f"       {detail}")


# ═══════════════════════════════════════════════════════════════════════
# DISCIPLINE DATABASE
# Each entry: (name, category, [rigor, predictive, tractable, consistent,
#               reductionist, transparent, linearizable])
# ═══════════════════════════════════════════════════════════════════════

DISCIPLINES = [
    # ── Pure Mathematics ──
    ("Number Theory",          "Pure Math",   [10, 7, 6, 9, 10, 10, 7]),
    ("Topology",               "Pure Math",   [10, 5, 5, 9, 9, 10, 6]),
    ("Abstract Algebra",       "Pure Math",   [10, 5, 6, 10, 10, 10, 8]),
    ("Real/Complex Analysis",  "Pure Math",   [10, 6, 7, 10, 9, 10, 8]),
    ("Geometry",               "Pure Math",   [10, 6, 7, 9, 9, 10, 7]),
    ("Combinatorics",          "Pure Math",   [10, 7, 9, 9, 8, 10, 7]),
    ("Mathematical Logic",     "Pure Math",   [10, 4, 7, 10, 10, 10, 5]),

    # ── Physics ──
    ("Classical Mechanics",    "Physics",     [9, 9, 9, 9, 6, 9, 8]),
    ("Electromagnetism",       "Physics",     [9, 10, 9, 10, 7, 9, 9]),
    ("Thermodynamics",         "Physics",     [8, 9, 8, 10, 6, 9, 6]),
    ("Statistical Mechanics",  "Physics",     [9, 9, 8, 9, 8, 9, 7]),
    ("Quantum Mechanics",      "Physics",     [9, 10, 8, 9, 9, 8, 10]),
    ("Quantum Field Theory",   "Physics",     [8, 10, 5, 7, 10, 6, 8]),
    ("General Relativity",     "Physics",     [9, 9, 4, 9, 9, 8, 4]),
    ("Condensed Matter",       "Physics",     [7, 8, 6, 7, 7, 7, 8]),
    ("Nuclear Physics",        "Physics",     [7, 8, 5, 7, 8, 7, 6]),
    ("Particle Physics",       "Physics",     [8, 9, 4, 8, 10, 7, 7]),
    ("Optics",                 "Physics",     [8, 9, 9, 9, 6, 9, 9]),
    ("Acoustics",              "Physics",     [7, 8, 9, 9, 5, 8, 9]),
    ("Fluid Dynamics",         "Physics",     [7, 7, 5, 7, 5, 7, 5]),

    # ── Chemistry ──
    ("Physical Chemistry",     "Chemistry",   [7, 7, 7, 8, 7, 7, 6]),
    ("Organic Chemistry",      "Chemistry",   [4, 5, 4, 6, 5, 5, 2]),
    ("Inorganic Chemistry",    "Chemistry",   [4, 4, 4, 5, 5, 5, 2]),
    ("Biochemistry",           "Chemistry",   [4, 5, 3, 5, 6, 5, 2]),
    ("Materials Science",      "Chemistry",   [6, 7, 6, 6, 6, 6, 5]),

    # ── Biology ──
    ("Molecular Biology",      "Biology",     [4, 6, 4, 6, 7, 5, 2]),
    ("Genetics",               "Biology",     [5, 7, 5, 7, 7, 6, 3]),
    ("Evolutionary Biology",   "Biology",     [4, 5, 3, 5, 4, 5, 2]),
    ("Ecology",                "Biology",     [3, 3, 3, 4, 3, 4, 1]),
    ("Neuroscience",           "Biology",     [3, 3, 2, 3, 5, 4, 2]),
    ("Zoology",                "Biology",     [2, 2, 2, 4, 3, 3, 1]),

    # ── Earth Sciences ──
    ("Geology",                "Earth Sci",   [3, 3, 3, 5, 4, 4, 2]),
    ("Meteorology/Climate",    "Earth Sci",   [5, 5, 6, 4, 4, 6, 4]),
    ("Oceanography",           "Earth Sci",   [4, 4, 5, 5, 4, 5, 3]),

    # ── Engineering Sciences ──
    ("Electrical Engineering", "Engineering", [8, 9, 10, 9, 6, 9, 10]),
    ("Computer Science",       "Engineering", [9, 8, 9, 8, 8, 9, 8]),
    ("Information Theory",     "Engineering", [10, 9, 9, 10, 8, 10, 9]),

    # ── Social/Other ──
    ("Economics",              "Social",      [5, 3, 5, 3, 2, 4, 5]),
    ("Psychology",             "Social",      [2, 2, 2, 2, 2, 3, 1]),
    ("Linguistics",            "Social",      [5, 4, 5, 5, 4, 5, 3]),
]

AXIS_NAMES = [
    "Rigor", "Predictive", "Tractable", "Consistent",
    "Reductionist", "Transparent", "Linearizable"
]

# Weights for total score (sum to 1.0)
# BST/AC(0) emphasizes: linearizability, tractability, rigor, predictive power
WEIGHTS = [0.15, 0.20, 0.15, 0.10, 0.10, 0.10, 0.20]


# ═══════════════════════════════════════════════════════════════════════
# SCORING FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════

def weighted_score(ratings):
    """Weighted average of 7 axes, 0-10 scale."""
    return sum(w * r for w, r in zip(WEIGHTS, ratings))


def ac0_friendliness(ratings):
    """
    AC(0) friendliness: how amenable to depth-0 (counting/linear) treatment?

    Key factors:
    - Linearizability (most important — can you express it in linear algebra?)
    - Computational tractability (can you actually compute?)
    - Mathematical rigor (is there formal structure to work with?)
    - Internal consistency (are the rules settled?)

    Formula: geometric mean of the four key axes, normalized to 0-10.
    Geometric mean penalizes any single zero harshly — you need ALL four.
    """
    lin = ratings[6]       # linearizability
    tract = ratings[2]     # tractability
    rigor = ratings[0]     # rigor
    consist = ratings[3]   # consistency
    # Geometric mean
    product = lin * tract * rigor * consist
    if product <= 0:
        return 0.0
    return product ** 0.25


def complexity_overhead(ratings):
    """
    Complexity overhead: high math complexity with low predictive power.
    This identifies fields that "adopted complex math for status."

    High rigor + low predictive power + low tractability = over-complicated.
    Score: rigor - (predictive + tractable) / 2
    Positive = over-complicated. Negative = under-formalized or balanced.
    """
    return ratings[0] - (ratings[1] + ratings[2]) / 2.0


def formalization_gap(ratings):
    """
    Formalization gap: good intuition (predictive) but poor math (rigor).

    High predictive or reductionist potential with low rigor = under-formalized.
    Score: max(predictive, reductionist) - rigor
    Positive = under-formalized. Negative = well-formalized.
    """
    return max(ratings[1], ratings[4]) - ratings[0]


def alchemy_score(ratings):
    """
    "Alchemy with a periodic table" score.

    Alchemy = cataloguing without understanding.
    High: lots of facts (some reductionism, some prediction) but
          low rigor, low linearizability, low consistency.

    Measures: classification effort without mathematical backbone.
    Score: (reductionist + predictive) / 2 - (rigor + linearizable + consistent) / 3
    Positive = alchemy-like. Negative = mathematically grounded.
    """
    catalog_effort = (ratings[4] + ratings[1]) / 2.0
    math_backbone = (ratings[0] + ratings[6] + ratings[3]) / 3.0
    return catalog_effort - math_backbone


# ═══════════════════════════════════════════════════════════════════════
# COMPUTE ALL SCORES
# ═══════════════════════════════════════════════════════════════════════

results = []
for name, category, ratings in DISCIPLINES:
    ws = weighted_score(ratings)
    ac0 = ac0_friendliness(ratings)
    co = complexity_overhead(ratings)
    fg = formalization_gap(ratings)
    alch = alchemy_score(ratings)
    results.append({
        "name": name,
        "category": category,
        "ratings": ratings,
        "total": ws,
        "ac0": ac0,
        "complexity_overhead": co,
        "formalization_gap": fg,
        "alchemy": alch,
    })

# Sort by total score descending
results.sort(key=lambda r: -r["total"])


# ═══════════════════════════════════════════════════════════════════════
# TIER ASSIGNMENT
# ═══════════════════════════════════════════════════════════════════════

def assign_tier(r):
    """
    Tier 1: Ready for AC treatment (ac0 >= 7.0)
    Tier 2: Needs formalization first (4.0 <= ac0 < 7.0 AND rigor >= 5)
    Tier 3: Needs fundamental restructuring (ac0 < 4.0 OR rigor < 5)
    """
    if r["ac0"] >= 7.0:
        return 1
    elif r["ac0"] >= 4.0 and r["ratings"][0] >= 5:
        return 2
    else:
        return 3


for r in results:
    r["tier"] = assign_tier(r)


# ═══════════════════════════════════════════════════════════════════════
# OUTPUT
# ═══════════════════════════════════════════════════════════════════════

print("=" * 78)
print("Toy 1267 — Science Methodology Rating: Which Sciences Are Alchemy?")
print("=" * 78)

# ── Full Rankings ──
print(f"\n{'─' * 78}")
print(f"  FULL RANKINGS (weighted score, 0-10)")
print(f"  Weights: Rig={WEIGHTS[0]:.0%} Pred={WEIGHTS[1]:.0%} Tract={WEIGHTS[2]:.0%} "
      f"Con={WEIGHTS[3]:.0%} Red={WEIGHTS[4]:.0%} Trans={WEIGHTS[5]:.0%} Lin={WEIGHTS[6]:.0%}")
print(f"{'─' * 78}")
print(f"  {'Rank':>4}  {'Discipline':<25} {'Cat':<11} {'Score':>5} {'AC(0)':>5} {'Tier':>4}  "
      f"{'Rig':>3} {'Prd':>3} {'Trc':>3} {'Con':>3} {'Red':>3} {'Trn':>3} {'Lin':>3}")
print(f"  {'─'*4}  {'─'*25} {'─'*11} {'─'*5} {'─'*5} {'─'*4}  "
      f"{'─'*3} {'─'*3} {'─'*3} {'─'*3} {'─'*3} {'─'*3} {'─'*3}")

for i, r in enumerate(results, 1):
    rat = r["ratings"]
    print(f"  {i:4d}  {r['name']:<25} {r['category']:<11} {r['total']:5.2f} "
          f"{r['ac0']:5.2f}   T{r['tier']}  "
          f"{rat[0]:3d} {rat[1]:3d} {rat[2]:3d} {rat[3]:3d} {rat[4]:3d} {rat[5]:3d} {rat[6]:3d}")

# ── Category Averages ──
print(f"\n{'─' * 78}")
print(f"  CATEGORY AVERAGES")
print(f"{'─' * 78}")
categories = {}
for r in results:
    cat = r["category"]
    if cat not in categories:
        categories[cat] = {"scores": [], "ac0s": [], "ratings": [[] for _ in range(7)]}
    categories[cat]["scores"].append(r["total"])
    categories[cat]["ac0s"].append(r["ac0"])
    for j in range(7):
        categories[cat]["ratings"][j].append(r["ratings"][j])

print(f"  {'Category':<15} {'N':>3} {'Score':>6} {'AC(0)':>6}  "
      f"{'Rig':>4} {'Prd':>4} {'Trc':>4} {'Con':>4} {'Red':>4} {'Trn':>4} {'Lin':>4}")
print(f"  {'─'*15} {'─'*3} {'─'*6} {'─'*6}  "
      f"{'─'*4} {'─'*4} {'─'*4} {'─'*4} {'─'*4} {'─'*4} {'─'*4}")

for cat in ["Pure Math", "Physics", "Engineering", "Chemistry", "Biology",
            "Earth Sci", "Social"]:
    if cat not in categories:
        continue
    c = categories[cat]
    n = len(c["scores"])
    avg_s = sum(c["scores"]) / n
    avg_a = sum(c["ac0s"]) / n
    avg_r = [sum(c["ratings"][j]) / n for j in range(7)]
    print(f"  {cat:<15} {n:3d} {avg_s:6.2f} {avg_a:6.2f}  "
          f"{avg_r[0]:4.1f} {avg_r[1]:4.1f} {avg_r[2]:4.1f} "
          f"{avg_r[3]:4.1f} {avg_r[4]:4.1f} {avg_r[5]:4.1f} {avg_r[6]:4.1f}")

# ── Tier Groupings ──
print(f"\n{'─' * 78}")
print(f"  TIER CLASSIFICATION")
print(f"{'─' * 78}")

for tier in [1, 2, 3]:
    tier_names = {
        1: "READY for AC(0) treatment",
        2: "NEEDS FORMALIZATION first",
        3: "NEEDS FUNDAMENTAL RESTRUCTURING",
    }
    members = [r for r in results if r["tier"] == tier]
    members.sort(key=lambda r: -r["ac0"])
    print(f"\n  Tier {tier}: {tier_names[tier]} ({len(members)} disciplines)")
    for r in members:
        print(f"    {r['name']:<25} AC(0)={r['ac0']:.2f}  Score={r['total']:.2f}")

# ── Over-Complicated Sciences ──
print(f"\n{'─' * 78}")
print(f"  OVER-COMPLICATED: High math complexity, low predictive return")
print(f"  (adopted complex math for status rather than progress)")
print(f"{'─' * 78}")

overcomplicated = sorted(results, key=lambda r: -r["complexity_overhead"])
for r in overcomplicated:
    co = r["complexity_overhead"]
    if co > 0:
        bar = "!" * int(co * 3)
        print(f"  {r['name']:<25} overhead={co:+5.1f}  {bar}")

print(f"\n  Sciences with NEGATIVE overhead (math earns its keep):")
for r in overcomplicated[::-1]:
    co = r["complexity_overhead"]
    if co <= 0:
        bar = "*" * int(abs(co) * 3)
        print(f"  {r['name']:<25} overhead={co:+5.1f}  {bar}")
    else:
        break

# ── Under-Formalized Sciences ──
print(f"\n{'─' * 78}")
print(f"  UNDER-FORMALIZED: Good intuition, poor math")
print(f"  (would benefit most from BST/AC methodology)")
print(f"{'─' * 78}")

underformalized = sorted(results, key=lambda r: -r["formalization_gap"])
for r in underformalized:
    fg = r["formalization_gap"]
    if fg > 0:
        bar = ">" * int(fg * 3)
        print(f"  {r['name']:<25} gap={fg:+5.1f}  {bar}")

# ── Alchemy Score ──
print(f"\n{'─' * 78}")
print(f"  'ALCHEMY WITH A PERIODIC TABLE' RANKING")
print(f"  (cataloguing without mathematical backbone)")
print(f"{'─' * 78}")

alchemists = sorted(results, key=lambda r: -r["alchemy"])
for r in alchemists:
    a = r["alchemy"]
    if a > 0:
        bar = "~" * int(a * 4)
        print(f"  {r['name']:<25} alchemy={a:+5.2f}  {bar}")
    else:
        print(f"  {r['name']:<25} alchemy={a:+5.2f}  [grounded]")

# ── AC(0) Friendliness Ranking ──
print(f"\n{'─' * 78}")
print(f"  AC(0) FRIENDLINESS RANKING")
print(f"  (geometric mean of rigor x tractability x consistency x linearizability)")
print(f"{'─' * 78}")

ac0_sorted = sorted(results, key=lambda r: -r["ac0"])
for r in ac0_sorted:
    bar_len = int(r["ac0"])
    bar = "#" * bar_len
    print(f"  {r['name']:<25} AC(0)={r['ac0']:5.2f}  {bar}")

# ── Casey's Key Questions ──
print(f"\n{'─' * 78}")
print(f"  CASEY'S KEY QUESTIONS")
print(f"{'─' * 78}")

# Q1: Which sciences are "alchemy with a periodic table"?
print(f"\n  Q1: Which sciences are 'alchemy with a periodic table'?")
alch_positive = [r for r in results if r["alchemy"] > 0.5]
alch_positive.sort(key=lambda r: -r["alchemy"])
for r in alch_positive:
    print(f"      {r['name']:<25} alchemy={r['alchemy']:+.2f}")
if not alch_positive:
    print(f"      (none above threshold)")

# Q2: Which adopted complex math for status?
print(f"\n  Q2: Which adopted complex math for status rather than progress?")
status_seekers = [r for r in results if r["complexity_overhead"] > 1.0]
status_seekers.sort(key=lambda r: -r["complexity_overhead"])
for r in status_seekers:
    print(f"      {r['name']:<25} overhead={r['complexity_overhead']:+.1f}")
if not status_seekers:
    print(f"      (none above threshold)")

# Q3: Which could be streamlined with BST/AC methodology?
print(f"\n  Q3: Which could be streamlined with BST/AC methodology?")
print(f"      (Tier 2: has enough structure to formalize)")
streamlinable = [r for r in results if r["tier"] == 2]
streamlinable.sort(key=lambda r: -r["formalization_gap"])
for r in streamlinable:
    print(f"      {r['name']:<25} AC(0)={r['ac0']:.2f}  gap={r['formalization_gap']:+.1f}")

# ── BST Connection ──
print(f"\n{'─' * 78}")
print(f"  BST CONNECTION: Five-Integer Lens")
print(f"{'─' * 78}")

print(f"""
  BST derives from D_IV^5 with five integers: rank={rank}, N_c={N_c}, n_C={n_C}, C_2={C_2}, g={g}.
  N_max = {N_max}.

  The methodology rating reveals a hierarchy that mirrors BST structure:

  * The {sum(1 for r in results if r['tier'] == 1)} Tier-1 sciences share a property: they are
    ALREADY expressed in linear algebra or formal logic. AC(0) can operate
    on them immediately because their core operations are counting at bounded depth.

  * The {sum(1 for r in results if r['tier'] == 2)} Tier-2 sciences have structure but need
    linearization — exactly what BST's linearization program (T419-T420,
    T567-T570) provides. These are the best targets for 'science engineering.'

  * The {sum(1 for r in results if r['tier'] == 3)} Tier-3 sciences need fundamental restructuring.
    They currently operate as catalogues, not theories. BST's approach:
    find the geometry first, derive the catalogue second.

  Observation: The 'alchemy' sciences are exactly those that built periodic
  tables (catalogues) before they had the geometry to derive them. Chemistry
  IS thermodynamics + quantum mechanics. Zoology IS ecology + genetics +
  physics. The periodic table came before quantum mechanics explained it.
  BST says: geometry first, table second. Always.

  Casey's AC(0) program: any science whose core can be expressed as counting
  at bounded depth IS already solved in principle. The methodology rating
  quantifies which sciences are close to that threshold and which are far.
""")

# ── Key Statistics ──
print(f"{'─' * 78}")
print(f"  KEY STATISTICS")
print(f"{'─' * 78}")

n_disc = len(results)
avg_total = sum(r["total"] for r in results) / n_disc
avg_ac0 = sum(r["ac0"] for r in results) / n_disc
median_total = sorted(r["total"] for r in results)[n_disc // 2]
top_name = results[0]["name"]
bot_name = results[-1]["name"]
max_alchemy = max(results, key=lambda r: r["alchemy"])
max_overhead = max(results, key=lambda r: r["complexity_overhead"])
max_gap = max(results, key=lambda r: r["formalization_gap"])

print(f"  Disciplines rated:          {n_disc}")
print(f"  Average total score:        {avg_total:.2f} / 10")
print(f"  Median total score:         {median_total:.2f} / 10")
print(f"  Average AC(0) friendliness: {avg_ac0:.2f} / 10")
print(f"  Highest total:              {top_name} ({results[0]['total']:.2f})")
print(f"  Lowest total:               {bot_name} ({results[-1]['total']:.2f})")
print(f"  Most 'alchemy':             {max_alchemy['name']} ({max_alchemy['alchemy']:+.2f})")
print(f"  Most over-complicated:      {max_overhead['name']} ({max_overhead['complexity_overhead']:+.1f})")
print(f"  Largest formalization gap:   {max_gap['name']} ({max_gap['formalization_gap']:+.1f})")
print(f"  Tier 1 (AC-ready):          {sum(1 for r in results if r['tier'] == 1)}")
print(f"  Tier 2 (needs formalization):{sum(1 for r in results if r['tier'] == 2)}")
print(f"  Tier 3 (needs restructuring):{sum(1 for r in results if r['tier'] == 3)}")


# ═══════════════════════════════════════════════════════════════════════
# TESTS
# ═══════════════════════════════════════════════════════════════════════

print(f"\n{'─' * 78}")
print(f"  TESTS")
print(f"{'─' * 78}")

# T1: Correct number of disciplines
test(1, f"Rated {n_disc} disciplines (>= 35)",
     n_disc >= 35,
     f"n={n_disc}")

# T2: Information Theory should be top-5
info_rank = next(i for i, r in enumerate(results, 1) if r["name"] == "Information Theory")
test(2, "Information Theory in top 5",
     info_rank <= 5,
     f"rank={info_rank}")

# T3: QM should be top-5
qm_rank = next(i for i, r in enumerate(results, 1) if r["name"] == "Quantum Mechanics")
test(3, "Quantum Mechanics in top 5",
     qm_rank <= 5,
     f"rank={qm_rank}")

# T4: Psychology should be bottom-5
psych_rank = next(i for i, r in enumerate(results, 1) if r["name"] == "Psychology")
test(4, "Psychology in bottom 5",
     psych_rank >= n_disc - 4,
     f"rank={psych_rank}")

# T5: Pure Math average rigor > 9
pure_math_rigor = [r["ratings"][0] for r in results if r["category"] == "Pure Math"]
avg_pm_rigor = sum(pure_math_rigor) / len(pure_math_rigor)
test(5, "Pure Math average rigor > 9",
     avg_pm_rigor > 9,
     f"avg={avg_pm_rigor:.1f}")

# T6: Chemistry has positive alchemy score on average
chem_alchemy = [r["alchemy"] for r in results if r["category"] == "Chemistry"]
avg_chem_alchemy = sum(chem_alchemy) / len(chem_alchemy)
test(6, "Chemistry avg alchemy score > 0 (it IS alchemy)",
     avg_chem_alchemy > 0,
     f"avg={avg_chem_alchemy:.2f}")

# T7: Zoology has lowest total score among biology (least mathematical)
bio_scores = [(r["name"], r["total"]) for r in results if r["category"] == "Biology"]
bio_scores.sort(key=lambda x: x[1])
test(7, "Zoology has lowest score in biology (least mathematical)",
     bio_scores[0][0] == "Zoology",
     f"bottom={bio_scores[0][0]} ({bio_scores[0][1]:.2f})")

# T8: EE and Optics both have linearizability >= 9
ee_lin = next(r["ratings"][6] for r in results if r["name"] == "Electrical Engineering")
optics_lin = next(r["ratings"][6] for r in results if r["name"] == "Optics")
test(8, "EE and Optics linearizability >= 9",
     ee_lin >= 9 and optics_lin >= 9,
     f"EE={ee_lin}, Optics={optics_lin}")

# T9: All weights sum to 1.0
test(9, "Weights sum to 1.0",
     abs(sum(WEIGHTS) - 1.0) < 1e-10,
     f"sum={sum(WEIGHTS):.10f}")

# T10: Tier 1 average AC(0) > Tier 2 > Tier 3
t1_ac0 = [r["ac0"] for r in results if r["tier"] == 1]
t2_ac0 = [r["ac0"] for r in results if r["tier"] == 2]
t3_ac0 = [r["ac0"] for r in results if r["tier"] == 3]
avg_t1 = sum(t1_ac0) / len(t1_ac0) if t1_ac0 else 0
avg_t2 = sum(t2_ac0) / len(t2_ac0) if t2_ac0 else 0
avg_t3 = sum(t3_ac0) / len(t3_ac0) if t3_ac0 else 0
test(10, "Tier 1 AC(0) > Tier 2 > Tier 3",
     avg_t1 > avg_t2 > avg_t3,
     f"T1={avg_t1:.2f} > T2={avg_t2:.2f} > T3={avg_t3:.2f}")

# T11: GR has negative linearizability overhead (nonlinear by nature)
gr = next(r for r in results if r["name"] == "General Relativity")
test(11, "GR linearizability < 5 (can't linearize curvature!)",
     gr["ratings"][6] < 5,
     f"GR linearizability={gr['ratings'][6]}")

# T12: Topology has complexity overhead (rigorous but low predictive)
topo = next(r for r in results if r["name"] == "Topology")
test(12, "Topology has positive complexity overhead",
     topo["complexity_overhead"] > 0,
     f"overhead={topo['complexity_overhead']:+.1f}")


# ═══════════════════════════════════════════════════════════════════════
# FINDINGS
# ═══════════════════════════════════════════════════════════════════════

print(f"\n{'─' * 78}")
print(f"  KEY FINDINGS")
print(f"{'─' * 78}")
print(f"""
  1. ALCHEMY SCIENCES: Chemistry (especially organic/inorganic), zoology,
     and neuroscience are catalogues without mathematical backbone. They have
     periodic tables (classification schemes) built before the geometry that
     would derive them.

  2. STATUS MATH: Topology and mathematical logic score high rigor but low
     predictive power — the math is internally consistent but doesn't yet
     connect to observables. This is sophistication without payoff.
     (Note: BST USES topology — it's powerful when applied, but the field
     as practiced often values abstraction as an end in itself.)

  3. STREAMLINABLE: Physical chemistry, materials science, meteorology, and
     genetics have enough structure for AC(0) formalization. They need the
     linearization program, not fundamental restructuring.

  4. THE LINEARIZABILITY CLIFF: There is a sharp divide around linearizability
     score 5. Sciences above it (QM, E&M, EE, optics) are computationally
     tractable. Sciences below it (ecology, zoology, neuroscience) cannot
     currently be computed. BST's linearization theorems (T419-T420) target
     exactly this cliff.

  5. GR IS SPECIAL: General relativity scores high on rigor and prediction
     but low on linearizability and tractability — because you literally
     can't linearize curvature (Casey's Curvature Principle). This is not
     a flaw; it is a theorem about the structure of spacetime.

  6. INFORMATION THEORY IS THE BRIDGE: Shannon's framework scores near the
     top on every axis. It is the natural language for AC(0) treatment of
     any science — exactly as BST uses it.
""")

print(f"{'─' * 78}")
print(f"  HONEST CAVEATS")
print(f"{'─' * 78}")
print(f"""
  1. SUBJECTIVITY: All ratings are judgments, not measurements. Different
     raters would assign different numbers. The RELATIVE rankings matter
     more than the absolute scores.

  2. WITHIN-FIELD VARIATION: "Physics" contains QED (spectacularly predictive)
     and string theory (zero predictions). We rate the mainstream practice,
     not the best or worst subfield.

  3. WEIGHTING CHOICE: The AC(0)-heavy weighting (20% linearizability, 20%
     predictive) reflects BST methodology priorities. A different weighting
     would produce different rankings. The alchemy and overhead scores are
     weight-independent.

  4. IMPROVEMENT IS POSSIBLE: A low score is not permanent. Chemistry scored
     2/10 on rigor in 1800 and 7/10 by 1930 (quantum chemistry). Any field
     can climb — that is the point of science engineering.

  5. CATALOGUE IS NOT WORTHLESS: Zoology's classification work was essential
     for evolution. The critique is not "cataloguing is bad" but "cataloguing
     without mathematical structure leaves the science incomplete."
""")

# ── Score ──
print(f"{'=' * 78}")
print(f"SCORE: {passed}/{total} PASS")
print(f"{'=' * 78}")
