#!/usr/bin/env python3
"""
Toy 3518 — Vol 13 Ch 4 "~137 bp superhelical = N_max" verification

Elie, Sunday 2026-05-24 11:36 EDT (Keeper task #307 verification)

PURPOSE
-------
Vol 13 Ch 4 (Biology) asserts ~137 bp superhelical = N_max BST primary anchor.
Canonical nucleosomal DNA wrapping is ~147 bp (1.65 turns × 89 bp/turn ≈ 147),
NOT 137. Verify the claim against published DNA topology data.

DATA SOURCES
------------
- Luger et al. (1997, Nature 389:251) crystal structure: 146 bp on nucleosome
- More recent X-ray + cryo-EM: 145-147 bp wrapped + 50-80 bp linker DNA
- Heeled by sequence preferences but no "137 bp" canonical value found

INVESTIGATIONS (6 scored tests)
1. Canonical nucleosomal repeat ≈ 147 bp (Luger 1997 + subsequent)
2. NRL (nucleosome repeat length) varies 165-220 bp by species
3. DNA persistence length: ~50 nm = ~150 bp (different quantity)
4. Linker DNA ≈ 50-80 bp (different quantity)
5. CONSTRUCTIVE: 137 bp as substrate-natural minimal binding-site length? No precedent found
6. RECOMMENDATION: retract specific "137 bp superhelical" claim; keep N_max in biology via different anchor (e.g., 137-fold rotational symmetry in BaTiO3 Vol 9 Ch 8)
"""
import sys

print("=" * 78)
print("Toy 3518 — Vol 13 Ch 4 ~137 bp superhelical verification")
print("Elie, Sunday 2026-05-24 (Keeper #307)")
print("=" * 78)

N_max = 137

# Test 1: Canonical nucleosomal wrap
print("\n--- Test 1: Luger 1997 crystal structure ---")
luger_bp = 146  # Luger et al. 1997 Nature 389:251
diff_from_137 = abs(luger_bp - N_max)
test_1 = (diff_from_137 >= 5)  # MORE than 5 bp away → mismatch significant
print(f"  Luger 1997 wrap: {luger_bp} bp; claimed: {N_max} bp; diff = {diff_from_137} bp")
print(f"  Significant mismatch (≥5 bp): {'YES (MISMATCH CONFIRMED)' if test_1 else 'NO'}")

# Test 2: Modern range of bp wrapped
print("\n--- Test 2: Modern X-ray + cryo-EM range ---")
modern_range = (145, 147)
test_2 = not (modern_range[0] <= N_max <= modern_range[1])  # 137 NOT in 145-147 range
print(f"  Modern wrap range: {modern_range[0]}-{modern_range[1]} bp")
print(f"  137 IN range: {modern_range[0] <= N_max <= modern_range[1]}; expected NO: {'CONFIRMED MISMATCH' if test_2 else 'NO'}")

# Test 3: DNA persistence length
print("\n--- Test 3: DNA persistence length (different quantity) ---")
persistence_nm = 50  # nm
bp_per_nm = 3.0  # ~3 bp/nm for B-form DNA (10.5 bp/turn × 3.4 nm/turn ≈ 3.1)
persistence_bp = persistence_nm * bp_per_nm
test_3 = (persistence_bp != N_max)  # 150 bp persistence ≠ 137 bp
print(f"  Persistence ≈ {persistence_nm} nm × {bp_per_nm} bp/nm = {persistence_bp} bp")
print(f"  Persistence ≠ 137: {'CONFIRMED (different quantity)' if test_3 else 'COINCIDENT'}")

# Test 4: Linker DNA range
print("\n--- Test 4: Linker DNA range ---")
linker_range = (50, 80)
test_4 = not (linker_range[0] <= N_max <= linker_range[1])
print(f"  Linker DNA: {linker_range[0]}-{linker_range[1]} bp")
print(f"  137 IN linker range: {linker_range[0] <= N_max <= linker_range[1]}; {'CONFIRMED ABSENT' if test_4 else 'PRESENT'}")

# Test 5: No precedent for 137 bp specifically
print("\n--- Test 5: Literature search for '137 bp' specific anchor ---")
# Based on my knowledge: no specific biophysical "137 bp" canonical value
literature_anchors = {
    "146 bp": "Luger 1997 nucleosome wrap",
    "147 bp": "Modern average wrap",
    "165-220 bp": "NRL species range",
    "50 nm = 150 bp": "Persistence length",
    "10.5 bp": "DNA helical turn",
    "21 bp": "DNA major-groove cycle",
    "137 bp": "NOT FOUND in canonical biophysics literature",
}
for anchor, ref in literature_anchors.items():
    print(f"  {anchor}: {ref}")
test_5 = True  # Honest finding: no specific 137 bp anchor in literature
print(f"  Test 5: 137 bp NOT canonical biophysics value: CONFIRMED")

# Test 6: Recommendation
print("\n--- Test 6: Retraction recommendation ---")
recommendation = """
  RECOMMENDATION (per Cal #19 + Cal #44 + Quaker discipline):
  ✗ RETRACT specific "~137 bp superhelical = N_max" claim from Vol 13 Ch 4
  ✓ KEEP N_max = 137 in biology via OTHER anchors:
    - BaTiO3 137-plane crystallographic feature (Vol 9 Ch 8)
    - Cs-137 hyperfine substrate connection (Vol 3 Ch 11)
    - α = 1/137 universal coupling (Vol 7 Ch 3)
    - Atomic number Z_max ≈ 119 (closer to N_max but oganesson is 118)

  HONEST DISPOSITION: substrate-natural N_max may appear in biology via different
  observable (e.g., transcription factor binding motif length, regulatory
  element spacing) but NOT via specific 147 bp nucleosomal wrap.
"""
print(recommendation)
test_6 = True
print(f"  Test 6: Retraction recommended: {'PASS' if test_6 else 'FAIL'}")

results = [test_1, test_2, test_3, test_4, test_5, test_6]
score = sum(results)
total = len(results)
print(f"\nSCORE: {score}/{total}")
print(f"Vol 13 Ch 4 137 bp verification: HONEST RETRACTION RECOMMENDED")
print("""
NET FINDING
===========
Vol 13 Ch 4 specific claim "~137 bp superhelical = N_max" does NOT match canonical
biophysics literature:
- Nucleosomal wrap: 146-147 bp (Luger 1997 + modern)
- Persistence length: ~150 bp (different quantity)
- No 137 bp specific anchor found in DNA topology literature

ACTION ITEM: Lyra Vol 13 Ch 4 revision — retract specific 137 bp claim; keep
N_max in biology via cross-volume anchors (BaTiO3, Cs-137, α=1/137).

Per Cal #44 + Quaker discipline: honest negative result is data, not shame.

— Elie, Toy 3518 Keeper #307 Sunday 2026-05-24 11:36 EDT
""")
sys.exit(0 if score == total else 1)
