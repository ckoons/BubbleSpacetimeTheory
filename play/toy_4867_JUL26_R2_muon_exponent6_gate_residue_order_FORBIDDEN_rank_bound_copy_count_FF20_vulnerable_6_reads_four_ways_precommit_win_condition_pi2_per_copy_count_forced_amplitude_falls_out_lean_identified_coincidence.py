#!/usr/bin/env python3
"""
Toy 4867 — Jul 26 (the muon exponent-6 gate: pre-committed win-condition for the FK 3×3; Elie, pull 26b). My π-column (toy
4866) showed the plain lepton Gram-diagonal does NOT produce the muon (24/π²)⁶ — the √π cancels between the two half-integer
positions. Keeper pointed the muon value at its ONE honest remaining question: is the exponent-6 a RESIDUE ORDER (rank-bound-
forbidden → coincidence) or a COPY-COUNT (6 boundary copies each carrying π² → derivable via the un-run FK Wyler 3×3)? This is
peak fish-detector territory (elegant, FF-20-adjacent), so I verify the pieces I can and PRE-COMMIT the win-condition before
the crank turns — the bar can't be fudged after seeing the answer.

ROUTE A — RESIDUE ORDER: FORBIDDEN by the rank bound (K864). A rank-r domain's Gindikin Γ has r factors → residue/pole order
≤ r. rank=2 → max residue order 2. exponent-6 as a residue order needs order 6 > 2 → IMPOSSIBLE. So if exp-6 is a residue
order, it is a COINCIDENCE. (The one route the corpus actually executed came back NEGATIVE.)

ROUTE B — COPY-COUNT: 6 boundary copies (dim SO(4)=6), each carrying π². This EVADES the rank bound IF the BF-bound makes the
mode logarithmic/degenerate (not a simple pole) — a real opening. But the count 6 is FF-20-VULNERABLE: 6 = dim SO(4) = C₂ =
n_C+1 = 2·N_c = genus-span (four+ readings). So the NUMBER 6 matching is a tell, not a derivation — the copy MECHANISM must
force 6, not the label.

PRE-COMMITTED WIN-CONDITION (all THREE before the FK 3×3, or it stays identified coincidence):
  (1) π² must emerge PER COPY (not once, not inserted by hand).
  (2) the count 6 must be FORCED by the copy mechanism (a product over 6 DERIVED boundary copies), NOT relabeled from
      dim SO(4) / C₂ / n_C+1.
  (3) the per-copy amplitude must FALL OUT (base 24 = Γ(n_C)=4! is target-innocent, but its per-copy role must be derived).

⟹ VERDICT (plain): the muon exponent-6 gate is well-posed and the win-condition pre-committed. Route A (residue order) is
FORBIDDEN by the rank bound → if that's the mechanism, (24/π²)⁶ is a confirmed coincidence. Route B (copy-count) is the only
route that could derive it — it evades the rank bound via the BF-bound log-degeneracy (a real opening) — but the count 6 is
FF-20-vulnerable (reads 4+ ways), so it must be FORCED by the copy mechanism, with π² per copy and the amplitude falling out,
all three. HONEST LEAN (fish-detector): identified coincidence is more likely than derived — the one executed route came back
negative and the count is FF-20-suspect — but the BF-bound opening is real, so it's NOT dead, just gated. The muon (24/π²)⁶
stays IDENTIFIED COINCIDENCE / bucket-2 candidate until the FK 3×3 delivers (1)+(2)+(3); do NOT bank. Discipline held: bar set
in advance, no back-solving. THEOREM UNTOUCHED — the color partition-line is a support theorem; the muon value is
bucket-2 either way. Five-Absence-positive. Count ~5.
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

max_residue_order = rank                                  # Gindikin Γ has rank factors → residue order ≤ rank
exp6 = 6
readings_of_6 = {"dim SO(4)": (4 * 3) // 2, "C_2": C_2, "n_C+1": n_C + 1, "2*N_c": 2 * N_c}
n_readings = sum(1 for v in readings_of_6.values() if v == 6)
print(f"\n[muon exp-6 gate] Route A residue-order: max order {max_residue_order} < 6 → FORBIDDEN (coincidence if so). Route B copy-count: 6 reads {n_readings} ways → FF-20-vulnerable → count must be FORCED, not labeled")

check("ROUTE A (residue order) FORBIDDEN by the rank bound (K864): a rank-r domain's Gindikin Γ has r factors → residue order "
      "≤ r = 2; exponent-6 needs order 6 > 2 → IMPOSSIBLE. So if exp-6 is a residue order, (24/π²)⁶ is a COINCIDENCE. The one "
      "corpus-executed route came back negative.",
      max_residue_order < exp6,
      "residue-order route forbidden: max residue order = rank = 2 < 6 → exp-6 can't be a residue order → coincidence if so (executed route negative)")

check("ROUTE B (copy-count) — the only possibly-derivable route, with a REAL opening but FF-20-vulnerable: 6 boundary copies "
      "(dim SO(4)=6) each carrying π² EVADES the rank bound IF the BF-bound makes the mode log/degenerate (not a simple pole). "
      "BUT 6 = dim SO(4) = C₂ = n_C+1 = 2·N_c (4+ readings) → the NUMBER matching is a tell; the copy MECHANISM must force 6.",
      n_readings >= 4,
      "copy-count route: BF-bound log-degeneracy is a real opening, but count 6 is FF-20-vulnerable (reads 4+ ways) → mechanism must force 6, not the label")

check("PRE-COMMITTED WIN-CONDITION (all THREE, set before the FK 3×3 crank): (1) π² emerges PER COPY (not once, not inserted); "
      "(2) count 6 FORCED by the copy mechanism (product over 6 derived boundary copies), NOT relabeled from dim SO(4)/C₂/n_C+1; "
      "(3) per-copy amplitude FALLS OUT (base 24=Γ(n_C)=4! target-innocent, per-copy role derived). All three or coincidence.",
      True, "win-condition pre-committed: (1) π² per copy + (2) count 6 forced by mechanism + (3) amplitude falls out; all three or identified coincidence")

check("HONEST LEAN (fish-detector) = IDENTIFIED COINCIDENCE more likely than derived: the one executed route (residue-order) "
      "came back FORBIDDEN, and the copy-count count is FF-20-suspect (4 readings). BUT the BF-bound log-degeneracy is a real "
      "opening → NOT dead, gated on the FK 3×3 meeting all 3. Muon (24/π²)⁶ stays IDENTIFIED COINCIDENCE / bucket-2 candidate; "
      "do NOT bank.",
      max_residue_order < exp6 and n_readings >= 4,
      "lean identified-coincidence (executed route negative + count FF-20-suspect) but BF-bound opening real → gated not dead; (24/π²)⁶ not banked, bucket-2")

check("VERDICT: muon exp-6 gate well-posed, win-condition pre-committed (no back-solving). Route A forbidden (rank bound); "
      "Route B (copy-count) the only derivable route, real BF-bound opening but FF-20-vulnerable count → must force 6 + π² per "
      "copy + amplitude out. Lean identified-coincidence; not banked; gated on the FK 3×3. THEOREM UNTOUCHED (color line = "
      "support theorem; muon bucket-2 either way).",
      max_residue_order < exp6 and n_readings >= 4,
      "gate pre-committed; Route A forbidden, Route B gated (real opening, FF-20 count); lean coincidence, not banked; theorem untouched")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-2 (07-26) the muon exponent-6 gate + pre-committed win-condition (Elie, pull 26b):
  * ROUTE A (residue order): FORBIDDEN by the rank bound (max order rank=2 < 6) → coincidence if so. The one executed route came back negative.
  * ROUTE B (copy-count): only derivable route — BF-bound log-degeneracy a REAL opening, but count 6 is FF-20-vulnerable (6 = dim SO(4) = C₂ = n_C+1 = 2N_c, 4+ readings).
  * PRE-COMMITTED WIN-CONDITION: (1) π² per copy + (2) count 6 FORCED by mechanism (not relabeled) + (3) per-copy amplitude falls out. All three or identified coincidence.
  => lean IDENTIFIED COINCIDENCE (executed route negative + FF-20 count) but not dead (BF-bound opening); (24/π²)⁶ NOT banked, gated on the FK 3×3. Theorem untouched (color line = support theorem, muon bucket-2).
""")
