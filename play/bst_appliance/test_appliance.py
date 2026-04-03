#!/usr/bin/env python3
"""BST Appliance v0.1 — Test Suite.

Verifies:
  1. All predictions evaluate without error
  2. Predicted values match measured values within stated precision
  3. Parser finds the right prediction for key queries
  4. Output formatting works for all three modes
"""
import sys
import os
import math

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bst_appliance.evaluator import evaluate, N_c, n_C, g, C_2, N_max, pi
from bst_appliance.knowledge_base import PREDICTIONS
from bst_appliance.parser import find_best, search
from bst_appliance.output import format_answer, format_gap, format_browse, format_integers

passed = 0
failed = 0
total = 0


def check(name, condition, detail=""):
    global passed, failed, total
    total += 1
    if condition:
        passed += 1
        print(f"  PASS  {name}")
    else:
        failed += 1
        print(f"  FAIL  {name}  {detail}")


def test_evaluator_basics():
    """Test that the evaluator namespace works."""
    print("\n=== Evaluator Basics ===")
    check("N_c", evaluate("N_c") == 3)
    check("n_C", evaluate("n_C") == 5)
    check("g", evaluate("g") == 7)
    check("C_2", evaluate("C_2") == 6)
    check("N_max", evaluate("N_max") == 137)
    check("rank", evaluate("rank") == 2)
    check("pi", abs(evaluate("pi") - math.pi) < 1e-15)
    check("6*pi^5", abs(evaluate("6 * pi**5") - 1836.118) < 0.001)
    check("integers sum", evaluate("N_c + n_C + g + C_2 + N_max") == 158)


def test_all_predictions_evaluate():
    """Test that every prediction's code evaluates without error."""
    print("\n=== All Predictions Evaluate ===")
    for p in PREDICTIONS:
        try:
            val = evaluate(p["code"])
            ok = val is not None
            check(f"{p['id']}: {p['name'][:35]}", ok)
        except Exception as e:
            check(f"{p['id']}: {p['name'][:35]}", False, str(e))


def test_key_accuracies():
    """Test that key predictions match measurements within 5%."""
    print("\n=== Key Prediction Accuracies ===")
    checks = [
        ("T187", "m_p/m_e", 1836.15267, 0.01),
        ("T190", "m_mu/m_e", 206.768, 0.01),
        ("T186", "proton mass", 938.272, 0.01),
        ("T280", "sin^2 theta_W", 0.23122, 1.0),
        ("T192", "Omega_Lambda", 0.685, 1.0),
        ("T193", "Omega_m", 0.315, 1.0),
        ("T196", "n_s", 0.9649, 1.0),
        ("T333", "amino acids", 20, 0.01),
        ("T731", "phyla", 35, 0.01),
        ("T320", "Cabibbo", 0.2250, 1.0),
        ("T330", "theta_12", 0.307, 5.0),
        ("T331", "theta_23", 0.572, 5.0),
        ("T332", "theta_13", 0.0222, 5.0),
        ("T310", "mu_p", 2.7928, 1.0),
        ("T311", "mu_n", -1.9130, 1.0),
        ("T245", "(m_n-m_p)/m_e", 2.5310, 1.0),
        ("T240", "m_s/m_d", 20, 0.01),
        ("T241", "m_t/m_c", 136, 1.0),
        ("T200", "N_gen", 3, 0.01),
        ("T729", "D_2 diagrams", 7, 0.01),
        ("T729b", "D_3 diagrams", 72, 0.01),
        ("T729c", "D_4 diagrams", 891, 0.01),
        ("T729d", "D_5 diagrams", 12672, 0.01),
    ]

    for tid, name, measured, tol_pct in checks:
        try:
            pred = None
            for p in PREDICTIONS:
                if p["id"] == tid:
                    pred = p
                    break
            if pred is None:
                check(f"{tid} {name}", False, "not found")
                continue
            val = evaluate(pred["code"])
            if measured == 0:
                dev = abs(val)
            else:
                dev = abs(val - measured) / abs(measured) * 100
            check(f"{tid} {name}: {val:.6g} vs {measured} ({dev:.3f}%)",
                  dev < tol_pct,
                  f"deviation {dev:.3f}% > {tol_pct}%")
        except Exception as e:
            check(f"{tid} {name}", False, str(e))


def test_parser():
    """Test that the parser finds the right predictions."""
    print("\n=== Parser Tests ===")
    queries = [
        ("proton mass", "T187"),
        ("dark energy", "T192"),
        ("amino acids", "T333"),
        ("higgs", "T230"),
        ("cabibbo", "T320"),
        ("muon mass", "T190"),
        ("spectral index", "T196"),
        ("weak mixing", "T280"),
        ("proton moment", "T310"),
        ("neutrino theta 23", "T331"),
        ("feynman diagrams", "T729"),
        ("phyla", "T731"),
        ("fine structure", "T198"),
        ("eta prime", "T265"),
        ("pion", "T250"),
        ("godel limit", "T199b"),
    ]

    for query, expected_id in queries:
        result = find_best(query)
        if result is None:
            check(f"'{query}' -> {expected_id}", False, "no match")
        else:
            check(f"'{query}' -> {expected_id}",
                  result["id"] == expected_id,
                  f"got {result['id']} ({result['name']})")


def test_output_formatting():
    """Test that output formatting works."""
    print("\n=== Output Formatting ===")

    # Mode 1: ANSWER
    pred = find_best("proton mass")
    output = format_answer(pred, "proton mass")
    check("ANSWER mode has box", "═" in output)
    check("ANSWER has formula", "6pi^5" in output or "6*pi^5" in output or "pi" in output)
    check("ANSWER has theorem", "T187" in output)

    # Mode 2: GAP
    output = format_gap("unicorn mass")
    check("GAP mode has box", "═" in output)
    check("GAP has message", "No BST prediction" in output)

    # Mode 3: BROWSE
    output = format_browse()
    check("BROWSE has categories", "predictions" in output.lower())

    output = format_browse("cosmology")
    check("BROWSE category works", "cosmology" in output.lower())

    # Integers
    output = format_integers()
    check("INTEGERS display", "137" in output and "N_c" in output)


def test_coverage():
    """Verify we have enough predictions."""
    print("\n=== Coverage ===")
    check(f"Total predictions: {len(PREDICTIONS)} >= 50",
          len(PREDICTIONS) >= 50,
          f"only {len(PREDICTIONS)}")

    from bst_appliance.knowledge_base import get_categories
    cats = get_categories()
    check(f"Categories: {len(cats)} >= 5", len(cats) >= 5)

    # Check each category has predictions
    for cat in cats:
        from bst_appliance.knowledge_base import get_by_category
        n = len(get_by_category(cat))
        check(f"  {cat}: {n} predictions", n > 0)


if __name__ == "__main__":
    print("=" * 60)
    print("  BST Appliance v0.1 — Test Suite")
    print("  Five integers. Zero free parameters.")
    print("=" * 60)

    test_evaluator_basics()
    test_all_predictions_evaluate()
    test_key_accuracies()
    test_parser()
    test_output_formatting()
    test_coverage()

    print("\n" + "=" * 60)
    print(f"  Results: {passed}/{total} PASS, {failed}/{total} FAIL")
    if failed == 0:
        print("  ALL TESTS PASSED")
    print("=" * 60)

    sys.exit(0 if failed == 0 else 1)
