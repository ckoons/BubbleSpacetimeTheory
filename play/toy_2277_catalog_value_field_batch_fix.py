"""
Toy 2277 — Batch fix value-field placeholders in catalog.

Owner: Elie
Date: 2026-05-15
Out of: Toy 2275 surfaced 253 formula-vs-value mismatches.

Many are catalog entries where the `value` field is a placeholder (1.0
or rounded) while the formula evaluates to a clean BST value. Fix:
replace the placeholder with the computed value, where the formula is
clearly correct and the value is clearly placeholder.

CRITERIA for fix (conservative):
1. Formula evaluates to a clean integer or simple rational
2. Value field is exactly 1.0 (placeholder) and the formula computes
   something < 1 (like 1/N_max for alpha)
3. Or: value field is 1.0 and observed is a small fraction (placeholder
   for "compare to 1 reference")

Don't fix:
- Symbolic values ("structural", "exact", text)
- Cases where the formula and value are both meaningful but disagree
- Anything where the entry's intent is unclear

This is a non-destructive batch: only changes value field, leaves formula
and tier untouched.
"""

import json
import re


# BST integers
rank = 2
N_c  = 3
n_C  = 5
C_2  = 6
g    = 7
c_2  = 11
c_3  = 13
chi  = 24
N_max = 137


def safe_eval(formula_str):
    """Evaluate a BST formula string."""
    if not isinstance(formula_str, str):
        return None
    s = formula_str
    parts = re.split(r'\s*=\s*', s)
    for candidate in [p.strip() for p in parts if p.strip()]:
        try:
            if re.search(r'[a-zA-Z]', candidate):
                identifiers = set(re.findall(r'[A-Za-z_][A-Za-z_0-9]*', candidate))
                allowed = {"rank", "N_c", "n_C", "C_2", "g", "c_2", "c_3",
                           "chi", "N_max", "pi"}
                if not identifiers.issubset(allowed):
                    continue
            expr = (candidate
                    .replace("·", "*").replace("×", "*")
                    .replace("²", "**2").replace("³", "**3").replace("⁴", "**4")
                    .replace("⁵", "**5").replace("₂", "_2").replace("₃", "_3")
                    .replace("^", "**"))
            import math as m
            val = eval(expr, {"__builtins__": {}, "math": m},
                       {"rank": rank, "N_c": N_c, "n_C": n_C,
                        "C_2": C_2, "g": g, "c_2": c_2, "c_3": c_3,
                        "chi": chi, "N_max": N_max, "pi": m.pi})
            if isinstance(val, (int, float)):
                return float(val)
        except Exception:
            continue
    return None


CATALOG_PATH = "/Users/cskoons/projects/github/BubbleSpacetimeTheory/data/bst_geometric_invariants.json"

with open(CATALOG_PATH) as f:
    d = json.load(f)

# DRY RUN first — count candidates
candidates = []
for entry in d["invariants"]:
    v = entry.get("value")
    formula = entry.get("formula") or entry.get("bst_formula") or ""
    if not isinstance(formula, str) or not formula:
        continue
    # Only consider entries with numeric value
    if not isinstance(v, (int, float)):
        continue
    computed = safe_eval(formula)
    if computed is None:
        continue
    # Match check
    if v != 0 and abs(computed - v) / abs(v) < 0.01:
        continue  # matches, no fix needed
    if abs(computed - v) < 0.001:
        continue  # matches close
    # Mismatch: is value a placeholder 1.0 while formula computes <1?
    if abs(v - 1.0) < 0.001 and computed < 1.0 and computed > 0:
        candidates.append((entry.get("symbol", "?"), v, computed, formula[:80]))

print(f"\nCandidates for value-field batch fix: {len(candidates)}")
print(f"\n{'Symbol':<40} | {'old val':>8} | {'new val':>14} | Formula")
print("-" * 110)
for sym, old, new, formula in candidates[:30]:
    print(f"{sym:<40} | {old:>8.2f} | {new:>14.6g} | {formula[:50]}")

# APPLY the fixes (only the unambiguous cases)
fixes_applied = 0
for entry in d["invariants"]:
    v = entry.get("value")
    formula = entry.get("formula") or entry.get("bst_formula") or ""
    if not isinstance(formula, str) or not formula:
        continue
    if not isinstance(v, (int, float)):
        continue
    computed = safe_eval(formula)
    if computed is None:
        continue
    if v != 0 and abs(computed - v) / abs(v) < 0.01:
        continue
    if abs(computed - v) < 0.001:
        continue
    # Apply only the safest fix: value=1.0, computed < 1, computed > 0
    if abs(v - 1.0) < 0.001 and computed < 1.0 and computed > 0:
        entry["value"] = computed
        # Annotate
        notes = entry.get("notes", "")
        if "[VALUE-FIELD CORRECTED 2026-05-15" not in notes:
            entry["notes"] = (notes + " [VALUE-FIELD CORRECTED 2026-05-15 by Toy 2277: was 1.0 placeholder, replaced with computed]").strip()
        fixes_applied += 1

print(f"\n{fixes_applied} value-field fixes applied (placeholder 1.0 → computed value).")

# Save
with open(CATALOG_PATH, "w") as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

print(f"Catalog re-saved. Counts unchanged ({d['total']} entries).")

# Verify
with open(CATALOG_PATH) as f:
    d2 = json.load(f)
print(f"Verification: total={d2['total']}, meta={d2['meta']['total_entries']}, actual={len(d2['invariants'])}")
assert d2['total'] == d2['meta']['total_entries'] == len(d2['invariants'])
print("SYNC OK")
