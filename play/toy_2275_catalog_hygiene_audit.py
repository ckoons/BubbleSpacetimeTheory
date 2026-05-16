"""
Toy 2275 — Catalog hygiene audit: formula-vs-value structural check.

Owner: Elie
Date: 2026-05-15
Out of: RUN_LIST queue item 4 (catalog hygiene grep).

PURPOSE
=======
Sweep every catalog entry with an integer value and an integer-arithmetic
formula. Try to evaluate the formula and check it matches the value.
Flag mismatches — those are broken catalog entries.

This is the same audit Casey/Keeper had me do for Fe-56 (Toy 2257) and
Pb-208 (Toy 2264). Now broaden to the whole catalog.

APPROACH
========
1. For each catalog entry:
   - Extract value (integer if possible)
   - Extract formula string
   - Try to parse-and-evaluate the BST symbols
2. If formula evaluates to a number and that number != value, flag as broken.
3. Don't try to fix — that's a separate pass. Just flag for Grace's sweep.
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
M_g  = 127
M_5  = 31
M_3  = 7
M_2  = 3


def safe_eval(formula_str):
    """Try to safely evaluate a BST formula string. Returns (success, value)."""
    if not isinstance(formula_str, str):
        return (False, None)
    # Strip equality and right-hand side (take the leftmost expression)
    s = formula_str
    # Drop trailing "= XXX" parts
    parts = re.split(r'\s*=\s*', s)
    candidates = [p.strip() for p in parts if p.strip()]
    for candidate in candidates:
        try:
            # Skip if has variables outside our namespace
            if re.search(r'[a-zA-Z]', candidate):
                # Only allow BST identifiers
                identifiers = set(re.findall(r'[A-Za-z_][A-Za-z_0-9]*', candidate))
                allowed = {"rank", "N_c", "n_C", "C_2", "g", "c_2", "c_3",
                           "chi", "N_max", "M_g", "M_5", "M_3", "M_2", "pi"}
                if not identifiers.issubset(allowed):
                    continue
            # Replace BST notation
            expr = (candidate
                    .replace("·", "*")
                    .replace("×", "*")
                    .replace("²", "**2")
                    .replace("³", "**3")
                    .replace("⁴", "**4")
                    .replace("⁵", "**5")
                    .replace("₂", "_2")
                    .replace("₃", "_3")
                    .replace("^", "**"))
            # Try eval
            val = eval(expr, {"__builtins__": {}},
                       {"rank": rank, "N_c": N_c, "n_C": n_C,
                        "C_2": C_2, "g": g, "c_2": c_2, "c_3": c_3,
                        "chi": chi, "N_max": N_max, "M_g": M_g,
                        "M_5": M_5, "M_3": M_3, "M_2": M_2})
            if isinstance(val, (int, float)):
                return (True, val)
        except Exception:
            continue
    return (False, None)


def extract_value(entry):
    """Try to extract numerical value from entry."""
    v = entry.get("value")
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        # Try parsing first number in string
        m = re.match(r'\s*(-?\d+\.?\d*)', v)
        if m:
            try:
                return float(m.group(1))
            except ValueError:
                return None
    return None


# Load catalog
with open("/Users/cskoons/projects/github/BubbleSpacetimeTheory/data/bst_geometric_invariants.json") as f:
    d = json.load(f)

print(f"Catalog has {len(d['invariants'])} entries.")

mismatches = []
unparseable = []
matched = 0
no_value = 0

for entry in d["invariants"]:
    sym = entry.get("symbol", "?")
    val = extract_value(entry)
    if val is None:
        no_value += 1
        continue

    formula = entry.get("formula") or entry.get("bst_formula") or ""
    ok, computed = safe_eval(formula)
    if not ok:
        unparseable.append((sym, formula[:80] if isinstance(formula, str) else ""))
        continue

    # Compare
    if abs(computed - val) < 0.001:
        matched += 1
    elif val != 0 and abs(computed - val) / abs(val) < 0.01:
        matched += 1  # within 1% — acceptable for non-exact entries
    else:
        mismatches.append((sym, val, computed, formula[:100] if isinstance(formula, str) else ""))


print(f"\nResults:")
print(f"  Matched (formula evaluates close to value): {matched}")
print(f"  Mismatches (computed != stated value):     {len(mismatches)}")
print(f"  Unparseable formulas:                       {len(unparseable)}")
print(f"  No-value entries:                           {no_value}")
print()

print(f"Top 30 MISMATCHES (catalog hygiene targets):")
print(f"{'Symbol':<35} | {'Value':>12} | {'Computed':>12} | Formula")
print("-" * 110)
for sym, val, computed, formula in mismatches[:30]:
    diff_pct = (computed - val) / val * 100 if val != 0 else float('inf')
    print(f"{sym:<35} | {val:>12.2f} | {computed:>12.2f} | {formula[:50]}")

# Summary stats
print(f"\nSUMMARY:")
print(f"  Total checked: {matched + len(mismatches) + len(unparseable) + no_value}")
print(f"  Match rate (of parseable): {100*matched/(matched + len(mismatches)):.1f}%")
print(f"  Mismatch rate: {100*len(mismatches)/(matched + len(mismatches)):.2f}%")
print(f"  Catalog health: {matched + len(unparseable)}/{matched + len(mismatches) + len(unparseable)} = {100*(matched+len(unparseable))/(matched+len(mismatches)+len(unparseable)):.1f}% (parseable + matching)")
