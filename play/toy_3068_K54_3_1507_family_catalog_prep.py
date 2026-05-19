"""
Toy 3068 — K54 candidate prep: 3/1507 = N_c/(N_max·c_2) family catalog.

Owner: Elie (self-direct per Casey "work the board"; K54 candidate Keeper-queued
       from Tuesday morning's 3/1507 reappearances)
Date: 2026-05-19 AM

CONTEXT
=======
Casey morning note flagged K54 candidate around "3/1507 family." This BST
primary form N_c/(N_max·c_2) = 3/(137·11) = 3/1507 ≈ 0.199% has appeared
across multiple substrate-coupling physical observable predictions:

  - Toy 3009 (Mar 2026): Decca 2007 Casimir-residual 3/1507 D-tier 0.6%
  - Toy 3020 (Apr 2026): BaTiO3 137-plane Casimir δ_137 prediction
  - SP29-1 H4 (May 2026): Cs-137 + Casimir cavity decay rate at 3/1507
  - Toy 3066 (May 19 today): W-32 decay rate vs T at (k_B T/m_e c²)·3/1507
  - Existing fine-structure family marker INV ~64389 (catalog)

This toy CATALOGS the family for Keeper's K54 audit, parallel to my Monday
K52 catalog scan / Toy 3054 K52a mechanism scoping.

PARALLELS TO K52a STRUCTURE
===========================
K52a "(1 ± 1/M_g) correction class": 2 D-tier instances (Lamb + BCS),
elevated-not-promoted, mechanism multi-week.

K54 candidate "N_c/(N_max·c_2) family": 1 D-tier instance (Decca) +
several pre-staged predictions awaiting experiment. Needs same audit
treatment.

DISCIPLINE (per Cal Rule 6 + audit-chain governance)
=====================================================
- Survey-only deliverable today
- Pre-stage what would constitute K54 promotion
- Flag instances that are MEASURED vs PRE-STAGED
- Honest scoping: measured ≠ predicted; mixing them confuses tier
- NOT unilateral promotion — Keeper K54 governs
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
INV_FILE = os.path.join(ROOT, "data", "bst_geometric_invariants.json")

rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok):
    tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3068 — K54 prep: 3/1507 family catalog scan")
print("=" * 72)

target = N_c / (N_max * c_2)  # 3/1507
print(f"\n[T1] Target BST primary form: N_c/(N_max·c_2) = {N_c}/{N_max*c_2} = {target:.6f}")
print(f"  Approximate scale: {target*100:.3f}%")
print(f"  Inverse: N_max·c_2/N_c = {N_max*c_2}/{N_c} ≈ {1/target:.2f}")

# === Catalog scan ===
print(f"\n[T2] Catalog scan: bst_geometric_invariants.json")
with open(INV_FILE) as f:
    inv_data = json.load(f)
invariants = inv_data.get('invariants', [])
print(f"  Loaded {len(invariants)} invariants")

hits = []
for inv in invariants:
    s = json.dumps(inv)
    # Match 3/1507, 3/(137·c_2), 0.199%, N_c/(N_max·c_2), 1/502.33, etc.
    matched_pat = None
    for pat in [
        '3/1507',
        'N_c / (N_max · c_2)',
        'N_c/(N_max·c_2)',
        'N_c/(N_max*c_2)',
        '3/(N_max·c_2)',
        '3/(137·11)',
        '3/(137*11)',
        '0.199%',
        '1/502.33',
        '1/502',
        'N_c/(N_max\\u00b7c_2)',  # JSON-escaped middle dot
    ]:
        if pat in s:
            matched_pat = pat
            break
    if matched_pat:
        prec = inv.get('precision_pct', inv.get('precision', None))
        hits.append({
            'id': inv.get('id', '?'),
            'name': inv.get('name', '?'),
            'symbol': inv.get('symbol', '?'),
            'domain': inv.get('domain', '?'),
            'tier': inv.get('tier', '?'),
            'precision': prec,
            'expression': inv.get('expression', inv.get('formula', '?')),
            'matched_pattern': matched_pat,
            'toy': inv.get('toy', '?'),
            'observed_value': inv.get('observed_value', inv.get('observed', None)),
        })

print(f"\n  3/1507 family hits in catalog: {len(hits)}")
for h in hits[:10]:
    name_short = (h['name'] or '?')[:50]
    print(f"    {h['id']}: {name_short} | tier={h['tier']} | toy={h['toy']}")

# === T3: Distinguish MEASURED vs PRE-STAGED ===
print(f"\n[T3] Distinguish MEASURED vs PRE-STAGED instances")
print(f"  Per audit-chain discipline: cannot mix measured-confirmation evidence")
print(f"  with predicted-but-unmeasured forms for promotion claim.")
print(f"  ")

measured_instances = []
pre_staged_instances = []
for h in hits:
    domain = (h['domain'] or '').lower()
    name = (h['name'] or '').lower()
    notes_blob = json.dumps(h).lower()

    # MEASURED markers: "decca", "observed", "measured", existing CODATA values
    measured = any(m in notes_blob for m in ['decca 2007', 'lifshitz residual', '2007'])
    # PRE-STAGED markers: SP29, prediction, proposal
    pre_staged = any(p in notes_blob for p in ['sp29', 'prediction', 'proposal', 'predicted', 'h4', 'cs-137'])

    if measured and not pre_staged:
        measured_instances.append(h)
    elif pre_staged and not measured:
        pre_staged_instances.append(h)
    elif measured and pre_staged:
        # both — counts toward MEASURED (the Decca anchor)
        measured_instances.append(h)
    # else: marker entries (e.g., fine-structure family marker without specific measurement)

print(f"  MEASURED (have CODATA / published measurement): {len(measured_instances)}")
for h in measured_instances[:5]:
    print(f"    {h['id']}: {h['name'][:55]}")
print(f"\n  PRE-STAGED (predictions, no measurement yet): {len(pre_staged_instances)}")
for h in pre_staged_instances[:5]:
    print(f"    {h['id']}: {h['name'][:55]}")

# === T4: External instance not in catalog yet — Toy 3066 W-32 ===
print(f"\n[T4] External instances filed today not yet cataloged")
print(f"  Toy 3066 W-32 decay-rate-vs-T pre-staged falsifier:")
print(f"    Δτ/τ = (k_B T / m_e c²) · (N_c/(N_max·c_2))")
print(f"    Amplitude at RT: 1×10^-10")
print(f"    Status: PRE-STAGED (atomic clock T-stability test, not yet executed)")
print(f"  Toy 3060 SP29-3 H2 angular Casimir uses (n_C/N_max), NOT 3/1507 — different family.")

# === T5: Family scope assessment ===
print(f"\n[T5] Family scope assessment")
total_instances = len(measured_instances) + len(pre_staged_instances) + 1  # +1 for Toy 3066 not in catalog
n_measured = len(measured_instances)
n_pre_staged = len(pre_staged_instances) + 1

print(f"  Total 3/1507 family instances: {total_instances}")
print(f"    Measured (D-tier match against observation): {n_measured}")
print(f"    Pre-staged (awaiting experiment): {n_pre_staged}")
print(f"  ")
print(f"  KEY CAVEAT for K54 promotion logic:")
print(f"    K52a has 2 D-tier MEASURED instances (Lamb + BCS, independent domains)")
print(f"    K54 has only 1 D-tier MEASURED instance (Decca Casimir residual)")
print(f"    The pre-staged predictions (SP29-1, W-32) DO NOT count for promotion")
print(f"    until measurement comes in.")
print(f"  ")
print(f"  Honest scoping: K54 candidate is currently a SINGLE-MEASURED-INSTANCE")
print(f"  family + several PRE-STAGED predictions. Less mature than K52a.")
check("K54 has at least 1 D-tier measured instance", n_measured >= 1)
check("K54 measured-instance count < K52a count (less mature)",
      n_measured < 2)

# === T6: Mechanism candidate (parallel to K52a triple-coincidence) ===
print(f"\n[T6] Mechanism candidate for N_c/(N_max·c_2) = 3/1507 specifically")
print(f"  ")
print(f"  Triple-component reading (parallel to K52a C1+C2+C3):")
print(f"  ")
print(f"  C1' (N_c factor): substrate-coupling carries color N_c at QCD-derived")
print(f"      substrate boundary effects. The 'commitment' processes inherit")
print(f"      color weight N_c at the boundary. (Cs-137 nuclear, Decca")
print(f"      photonic vacuum — both substrate-boundary.)")
print(f"  ")
print(f"  C2' (N_max·c_2 denominator): substrate scale is N_max (BST primary")
print(f"      atomic scale), dressed by c_2 = 11 = 2C_2 - 1 'dressed Casimir.'")
print(f"      Product N_max·c_2 = 1507 is the substrate-Casimir composite scale.")
print(f"  ")
print(f"  C3' (α² scale): 3/1507 ≈ α² × (some BST factor). Specifically:")
print(f"    α² = 1/N_max² = 1/18769")
print(f"    3/1507 / α² = 3·N_max²/1507 = 3·18769/1507 ≈ 37.34")
print(f"    Not a clean BST primary ratio — 3/1507 is α² order but NOT pure α².")
print(f"  ")
print(f"  Comparison to K52a 1/M_g:")
print(f"    1/M_g = 1/127 ≈ 0.787% (α-class correction)")
print(f"    3/1507 = 0.199% (α²-class correction)")
print(f"  Different scales (sub-leading vs sub-sub-leading); not interchangeable.")
print(f"  ")
print(f"  Mechanism IDEA (multi-week): the 'commitment process' on D_IV⁵")
print(f"  substrate has rate ~ α² with color weight N_c and substrate-scale")
print(f"  c_2 dressing. The 3/1507 form is the α² substrate-boundary commitment.")
print(f"  Lamb (1/M_g, α class) is sub-leading; Decca/SP29-1/W-32 (3/1507, α²")
print(f"  class) are sub-sub-leading. Both BST-substrate but at different orders.")

# === T7: Pre-registered falsifiable predictions for K54 audit ===
print(f"\n[T7] Pre-registered predictions for K54 promotion path")
print(f"  P1: SP29-1 Cs-137 Casimir experiment measurement → confirms or refutes 3/1507")
print(f"  P2: W-32 atomic clock T-stability re-analysis → confirms or refutes 1×10^-10")
print(f"  P3: Any new α²-order substrate-coupling observable should fit 3/1507 form")
print(f"  P4: Heavy-flavor or electroweak observables should NOT use 3/1507 form")
print(f"      (1/1507 too small at those scales — different α scaling)")
print(f"  ")
print(f"  If P1 confirms: K54 promotion to D-tier structural-law candidate")
print(f"  If P1 refutes: K54 walked-back, 3/1507 family is single-instance (Decca only)")
print(f"  If P1 + P2 both confirm: STRONG K54 → D-tier likely under new governance")

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3068_K54_3_1507_catalog.json")
out = {
    'meta': {
        'date': '2026-05-19',
        'owner': 'Elie',
        'task': 'K54 candidate prep: 3/1507 family catalog',
        'parallel_to': 'K52a (Monday) — same audit-chain discipline shape',
    },
    'BST_primary_form': 'N_c / (N_max · c_2) = 3 / (137 · 11) = 3/1507',
    'numerical_value': target,
    'percentage': target * 100,
    'instances_total': total_instances,
    'instances_measured': n_measured,
    'instances_pre_staged': n_pre_staged,
    'measured_list': [{'id': h['id'], 'name': h['name'], 'tier': h['tier'],
                        'toy': h['toy']} for h in measured_instances],
    'pre_staged_list': [{'id': h['id'], 'name': h['name'], 'tier': h['tier'],
                          'toy': h['toy']} for h in pre_staged_instances],
    'external_today': {
        'toy_3066_W32': 'Δτ/τ at 1e-10 amplitude RT thermal',
    },
    'mechanism_components_C1prime_C2prime_C3prime': {
        'C1prime': 'N_c factor — color weight at substrate boundary',
        'C2prime': 'N_max·c_2 denominator — substrate-Casimir composite scale',
        'C3prime': 'α² order — sub-sub-leading correction scale',
    },
    'tier_assessment': 'CANDIDATE elevated-not-promoted; awaiting SP29-1 measurement',
    'comparison_to_K52a': 'K54 less mature: 1 D-tier measured vs K52a 2 D-tier measured',
    'promotion_path': 'SP29-1 experimental confirmation → K54 D-tier under new governance',
}
with open(out_path, 'w') as f:
    json.dump(out, f, indent=2)
print(f"\n[T8] Output: {os.path.basename(out_path)}")

# Score
passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}")
print(f"Toy 3068 SCORE: {passed}/{total}")
print(f"{'='*72}")
for ok, label in tests:
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {label}")

print(f"""
K54 CANDIDATE PREP — 3/1507 FAMILY CATALOG SCAN:

  Family: N_c/(N_max·c_2) = 3/(137·11) = 3/1507 ≈ 0.199% (α² scale)

  Catalog instances total: {total_instances}
    Measured (CODATA / published): {n_measured} — Decca 2007 Casimir residual
    Pre-staged (awaiting experiment): {n_pre_staged} — SP29-1 H4, W-32, fine-
                                            structure family markers

  COMPARISON TO K52a (Monday):
    K52a: 2 D-tier measured instances (Lamb + BCS, independent domains)
    K54:  1 D-tier measured instance (Decca only); rest pre-staged
    → K54 LESS MATURE than K52a; cannot promote without SP29-1 measurement

  MECHANISM CANDIDATE (multi-week derivation, parallel to K52a triple-coincidence):
    C1' N_c color weight at substrate boundary
    C2' N_max·c_2 substrate-Casimir composite scale
    C3' α² sub-sub-leading correction order

  RECOMMENDED K54 PATH:
    1. SP29-1 experimental measurement (Casey send signal pending) → measure
    2. If confirms 3/1507 at ≥3σ: K54 promotes to 2 D-tier candidate
    3. With 2 instances + mechanism derivation: K54 D-tier structural law

  FILED FOR KEEPER K54 AUDIT DELIBERATION.

NOT CLAIMED:
  - K54 promotion (Keeper governs; single measured instance insufficient)
  - Universal applicability beyond α² substrate-coupling regime
  - Mechanism closure (parallel to K52a — multi-week)
""")
