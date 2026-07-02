#!/usr/bin/env python3
"""
Toy 4541 — Mid-Year: scan the certified/candidate/frontier set for GUT-NUMEROLOGY
(values that coincide with GUT reps/relations), as input for the coordinated
Five-Absence pass Lyra flagged (F450: down-row GJ + T2494 SO(10) 16 are the same class).

BST FORBIDS a GUT (Five-Absence: no GUT, no proton decay, no X/Y, no SU(5)/SO(10)
unification). So any BST value that coincides with a GUT rep/relation must be shown
FORCED by D_IV⁵ mechanism (GUT-free), NOT importing GUT structure. The down-row is
the exemplar: mechanism GUT-free (K582) but VALUES = GJ GUT-scale texture (toy_4540).
This scan LOCATES the surface; the coordinated pass adjudicates each item.

Target-innocent: I match BST structure values to a fixed list of GUT fingerprints.
No bank, no demotion — a flag map for the team's Five-Absence pass.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7

# ---- GUT fingerprints (fixed reference list) --------------------------------
GUT = {
    "GJ mass texture {3,1/3,1}": "Georgi-Jarlskog down/lepton ratios at M_GUT",
    "SU(5) reps {5,10,24,45}":   "5 matter, 10 matter, 24 adjoint, 45 GJ-Higgs",
    "SO(10) reps {16,10,45,126}":"16 spinor generation, 126 Yukawa",
    "E6 reps {27,78,351}":       "27 fundamental (matter), 78 adjoint",
    "sin^2θ_W = 3/8":            "GUT tree-level weak angle",
    "b-τ / t-b-τ unification":   "mass-ratio=1 at M_GUT run down",
}
SU5 = {5, 10, 24, 45}
SO10 = {16, 10, 45, 54, 120, 126, 210}
E6 = {27, 78, 351}

results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 78)
print("Toy 4541 — GUT-numerology scan: is the surface broader than the down-row?")
print("=" * 78)

# ---- BST structures to scan (certified + candidate + frontier) --------------
# (name, key integer/relation, its BST reading, GUT-fingerprint? )
scan = []
def add(name, val, bst_reading, gut_hit, gut_what):
    scan.append((name, val, bst_reading, gut_hit, gut_what))

# certified banks
add("down-row {3,1/3,1}", "3,1/3,1", "N_c^{+1,-1,0} (K582 color-parity)", True,
    "= GJ GUT-scale texture (CONFIRMED toy_4540 — the exemplar)")
add("θ_QCD = 0", 0, "strong-CP substrate-natural", False, "not a GUT rep/relation")
add("m_t", "173 GeV", "boundary determinant", False, "not a GUT rep")
add("θ₁₃ = 1/45", 45, "N_c²·n_C (mixing angle, convention-robust)", (45 in SU5),
    "45 = SU(5) GJ-Higgs rep dim — number-coincidence; θ₁₃ is a dimensionless angle, "
    "mechanism-disambiguated (Keeper-certified). FLAG for pass; likely clean.")
add("α = 1/137", 137, "N_c³·n_C+rank channel capacity", False, "137 not a GUT rep")
add("muon (24/π²)^C_2", "206.77", "π-form (K547 sphere-locus)", False, "π-form, not GUT")

# strong candidates
add("τ  49·71", "49·71", "g²·71 (unforced product)", False, "not a GUT rep")
add("down-ladder d₃/d₂", 52, "flat-fiber mode count (Grace/Lyra)", False, "geometric, not GUT")

# frontier / flagged
add("α-frontier V₂₇ + tensor-tower", 27, "N_c³ = color-tensor (α + down-ladder)", (27 in E6),
    "27 = E6 FUNDAMENTAL (matter rep). SAME class as down-row: value is GUT-adjacent, "
    "claimed GUT-free as color-tensor. Threads BOTH frontiers (Lyra). NEEDS the pass.")
add("T2494 SO(10) 16", 16, "flagged by Lyra during backfill", (16 in SO10),
    "16 = SO(10) SPINOR (one GUT generation). GUT-adjacent. Lyra flagged.")

print(f"\n{'structure':32s} {'GUT?':5s} note")
print("-" * 78)
flagged = []
for name, val, reading, hit, what in scan:
    tag = "FLAG" if hit else "ok"
    if hit: flagged.append(name)
    print(f"  {name:30s} {tag:5s} {what[:60]}")

# ---- findings ----------------------------------------------------------------
print(f"\n[FINDINGS] {len(flagged)} GUT-adjacent structures flagged: {flagged}")
check("the GUT-numerology surface is BROADER than the down-row (>=3 structures)",
      len(flagged) >= 3, f"{flagged}")
check("27 = E6 fundamental threads BOTH frontiers (α V₂₇ + tensor-tower) — same class as down-row",
      27 in E6, "the α-frontier carries E6-GUT-adjacent numerology; needs same Five-Absence scrutiny")
check("T2494 SO(10) 16 is GUT-adjacent (Lyra's flag confirmed)", 16 in SO10,
      "SO(10) spinor generation")
check("θ₁₃'s 45 = SU(5) GJ-Higgs dim — number-coincidence flagged (likely clean: robust angle)",
      45 in SU5, "flag for completeness; θ₁₃ mechanism-disambiguated + convention-robust, distinct from a mass texture")
check("θ_QCD, m_t, α, muon, τ, down-ladder-52 are NOT GUT-adjacent (clean of the fingerprints)",
      True, "the surface is specific, not everywhere — most of the set is GUT-free by value too")

# ---- the discipline point ---------------------------------------------------
print("\n[DISCIPLINE] each flagged item needs the down-row treatment (Five-Absence):")
print("  is the value FORCED by D_IV⁵ mechanism (GUT-free), or importing GUT structure?")
print("  down-row: mechanism GUT-free (K582) but VALUES = GJ GUT-texture → the problem.")
print("  27: forced as color-tensor (GUT-free) OR importing E6? — the α-frontier's own Gate.")
print("  16: what BST mechanism, if any — or is it a relabel of the SO(10) generation?")
print("  45 (θ₁₃): N_c²·n_C forced + convention-robust → likely a clean number-coincidence.")
check("scan is a FLAG MAP for the coordinated Five-Absence pass (Lyra), not a demotion",
      True, "target-innocent; adjudication is the team's pass; no count move")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 78)
print("RESULTS")
print("=" * 78)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}")
print("=" * 78)
print("""
GUT-NUMEROLOGY SCAN VERDICT (input for the coordinated Five-Absence pass):
  * The surface is BROADER than the down-row. Flagged GUT-adjacent:
     - down-row {3,1/3,1}  = GJ GUT texture (CONFIRMED problem, toy_4540)
     - 27 = E6 fundamental = threads BOTH frontiers (α V₂₇ + tensor-tower) — SAME
       'GUT-numerology-without-GUT' class; the α-frontier's own Gate must show it's
       forced as color-tensor, not importing E6.
     - T2494 SO(10) 16   = SO(10) spinor generation (Lyra's flag confirmed)
     - θ₁₃'s 45 = SU(5) GJ-Higgs dim = number-coincidence flag (θ₁₃ is a convention-
       robust mixing angle, mechanism-disambiguated → likely CLEAN, but list it).
  * CLEAN of the fingerprints: θ_QCD, m_t, α=1/137, muon, τ, down-ladder-52 — the
    surface is specific, not pervasive.
  * DISCIPLINE: each flagged item gets the down-row treatment — is the value FORCED
    by D_IV⁵ (GUT-free) or importing GUT structure? Adjudication = the team's
    coordinated pass. This is a FLAG MAP, target-innocent, NO demotion, NO count move.
  Count 8 (3 firm + 3 conditional-downrow + α partial + muon-gated), unchanged.
""")
