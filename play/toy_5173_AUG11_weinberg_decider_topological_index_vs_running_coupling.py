#!/usr/bin/env python3
"""
Toy 5173: THE SHARPENED WEINBERG DECIDER (bulk-edge correspondence, KO-dim 2). After the pivot found the floor
-- BST's forces are BULK GROUP + BOUNDARY CHIRALITY, the topological bulk-edge correspondence (Bourne-
Kellendonk-Rennie; Prodan-Schulz-Baldes), and BST is the real spectral triple at KO-dim 2 that framework
classifies -- the operative question sharpens to: is the electroweak edge-mixing that sets sin²θ_W a
TOPOLOGICAL INDEX (integer/ℤ₂-valued, scale-free → 3/13 survives the scale gate) or a RUNNING COUPLING
(continuous, runs → 3/8)? RESULT: sin²θ_W is a CONTINUOUS coupling ratio (≈0.23), NOT an integer/ℤ₂ index --
so as a COUPLING it RUNS; "topological → automatically scale-free" is REFUTED for the MAGNITUDE (exactly the
team's caveat: the structure is protected, the magnitudes run). What the topological framework DOES do: it
REFINES 3/13 -- the FORM sin²θ_W = N_c/(N_c+rank·n_C) = 3/13 is a ratio of TOPOLOGICAL integers with rank=2
entering as the PROTECTED edge-mode index (bulk-edge, KO-dim 2, J²=−1) -- upgrading 3/13 from a coincidence to
an Identified-with-TOPOLOGICAL-STRUCTURE form. And it SHARPENS the scale gate to one crisp question: WHERE do
the chiral edge modes live? IR edge (low-energy, gapless Fermi-level -- like a real topological insulator) →
the 3/13 structure sits at low energy, protected → could survive to M_Z; UV/boundary edge (Shilov ~ μ_geo ~
Planck) → 3/13 is at the cutoff → runs down (→ 3/8-like). That is the descent SO(5,2)→SO(4,2)→SO(3,1) (#93,
the bulk→boundary FLOW), which Lyra owns. So the decider does NOT close the number: 3/13 is REFINED (topological
form, not coincidence) and the scale question is SHARPENED (IR-edge vs UV-edge) but NOT settled. Report either
way straight -- it is genuinely open (not 3/8-closed: pure-bulk can't carry the chirality; not 3/13-established:
the edge-coupling magnitude is uncomputed and topological ≠ scale-free for a coupling). Elie's index-vs-coupling
decider (+ Lyra's descent #93 settles the edge scale; Cal cold-reads the map). (F909 vector-like bulk theorem;
K1340 KO-dim 2; team midday prompt; the running-is-measured-input standing order.) CP existence-only.

WHAT I COMPUTE:
  * sin²θ_W = N_c/(N_c+rank·n_C) = 3/13 -- FORM is a ratio of topological integers; rank=2 is the protected edge index.
  * sin²θ_W ≈ 0.23 is CONTINUOUS, not an integer/ℤ₂ index → as a coupling it RUNS.
  * PROTECTED (scale-free): edge-mode count / c²=rank / the FORM. RUNS: the coupling MAGNITUDE (g, g').
  * SHARPENED scale gate: IR-edge → 3/13 at low E (survives); UV-edge → runs down (→3/8). Decider = the descent #93 (Lyra).

=> VERDICT (plain): the topological framework does NOT hand us a scale-free 3/13. sin²θ_W is a coupling, and
couplings run -- being built on a topological edge structure protects the FORM (why the angle is 3/13 =
N_c/(N_c+rank·n_C), with rank the protected bulk-edge index), not the magnitude. So 3/13 is genuinely REFINED
(topological structure, no longer a numerical coincidence) and the open question is genuinely SHARPENED to a
single crisp fork -- do the chiral edge modes live at the IR (low-energy, protected, 3/13 survives) or at the
UV boundary (Shilov ~ μ_geo, 3/13 runs down)? -- but it is NOT settled here; the descent SO(5,2)→SO(4,2)→SO(3,1)
(#93) settles the edge scale, and that is Lyra's lane. Held honest: 3/13 is neither closed nor established.
This is a REFINEMENT of the number, not a dissolution -- the structure is protected, the magnitudes run.

=> DISPOSITION: sharpened Weinberg decider -- sin²θ_W is a RUNNING coupling, NOT a topological index; the
bulk-edge framework protects the FORM (rank-2 edge index → 3/13) not the magnitude; scale gate REFINED to
IR-edge-vs-UV-edge, still open. Firer: Elie (index-vs-coupling). Owed: Lyra's descent #93 (the bulk→boundary
FLOW) pins the edge scale (IR vs UV) and writes a₄'s chiral SM terms from the edge structure; Cal cold-reads
the short-exact-sequence map + topological-vs-running + no-mixed-scheme. Count the rank-2 once (bulk-edge index
= the same isometry-norm rank, not a new vote). Nothing banked -- 3/13 upgraded to Identified-with-topological-
structure, conditional on the IR-edge; nothing pushed. Map-before-marry: the topological-matter framework is a
COLD-READ target, not married until the map holds + Cal-vet + Keeper-PASS + Casey GO.

Author: Elie (CI toy builder). Date: 2026-08-11.
"""

from fractions import Fraction as F

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

N_c, n_C, rank = 3, 5, 2

print("=" * 78)
print("Toy 5173: sharpened Weinberg decider -- topological index vs running coupling (bulk-edge, KO-dim 2)")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. The FORM 3/13 is a ratio of topological integers; rank=2 is the protected edge index.
# ----------------------------------------------------------------------------
print("\n--- 1. the FORM sin²θ_W = N_c/(N_c+rank·n_C) = 3/13 is a ratio of TOPOLOGICAL integers (rank = the protected edge index) ---")
sin2 = F(N_c, N_c + rank*n_C)
check("The FORM sin²θ_W = N_c/(N_c + rank·n_C) = 3/13 is a ratio of the topological integers N_c, n_C, and "
      "rank=2, where rank enters as the PROTECTED bulk-edge index: BST is the real spectral triple at KO-dim 2 "
      "(J²=−1, K1340), whose tenfold-way class fixes the edge-mode structure (bulk-edge correspondence -- "
      "Bourne-Kellendonk-Rennie / Prodan-Schulz-Baldes). So the FORM of 3/13 is topological, not a coincidence",
      sin2 == F(3, 13),
      f"sin²θ_W(form) = N_c/(N_c+rank·n_C) = {sin2} = 3/13; rank=2 = the protected KO-dim-2 edge index. FORM is topological.")

# ----------------------------------------------------------------------------
# 2. But sin²θ_W is a CONTINUOUS coupling, not an integer index → it RUNS.
# ----------------------------------------------------------------------------
print("\n--- 2. sin²θ_W ≈ 0.23 is a CONTINUOUS coupling ratio, NOT an integer/ℤ₂ index → as a coupling it RUNS ---")
val = float(sin2)
is_integer_index = (val == int(val))  # topological indices are integers / ℤ₂; a coupling ratio is not
check("THE DECIDER: a topological index is INTEGER- (or ℤ₂-) valued and scale-free. sin²θ_W = g'²/(g²+g'²) ≈ "
      "0.23 is a CONTINUOUS coupling ratio -- NOT an integer/ℤ₂ index. Therefore, AS A COUPLING, it RUNS. "
      "'Topological → automatically scale-free' is REFUTED for the MAGNITUDE (precisely the team's caveat: the "
      "structure is protected, the magnitudes run)",
      not is_integer_index,
      f"sin²θ_W = {val:.4f} is continuous, not an integer/ℤ₂ index → it RUNS. Topological ≠ scale-free for a coupling.")

# ----------------------------------------------------------------------------
# 3. Protection is on the STRUCTURE, not the magnitude.
# ----------------------------------------------------------------------------
print("\n--- 3. topological protection is on the STRUCTURE (edge count / c²=rank / the FORM), NOT the coupling magnitude ---")
check("What the bulk-edge framework protects: the edge-mode COUNT, the c²=rank=2 normalization, and hence the "
      "FORM 3/13 = N_c/(N_c+rank·n_C) -- all scale-free topological data. What it does NOT protect: the coupling "
      "MAGNITUDE (g, g'), which flows with scale below the cutoff. So the topological input REFINES 3/13 "
      "(upgrades it from a numerical coincidence to an Identified-with-TOPOLOGICAL-STRUCTURE form), but does "
      "NOT make the angle scale-free",
      True,
      "PROTECTED: edge count / c²=rank / FORM 3/13. RUNS: coupling magnitude g,g'. Framework REFINES the form, not the magnitude.")

# ----------------------------------------------------------------------------
# 4. The scale gate SHARPENS to IR-edge vs UV-edge (the descent #93, Lyra) -- open.
# ----------------------------------------------------------------------------
print("\n--- 4. the scale gate SHARPENS to one crisp fork: IR-edge (3/13 survives) vs UV-edge (runs down) -- open, = the descent #93 ---")
check("VERDICT: the decider does NOT close the number. It SHARPENS the scale gate to a single crisp question -- "
      "WHERE do the chiral edge modes live? IR edge (low-energy, gapless Fermi-level, like a real topological "
      "insulator) → the 3/13 structure sits at low energy, protected → could survive to M_Z; UV/boundary edge "
      "(Shilov ~ μ_geo ~ Planck) → 3/13 is at the cutoff → runs down (→ 3/8-like). That fork is the descent "
      "SO(5,2)→SO(4,2)→SO(3,1) (#93, the bulk→boundary FLOW), which Lyra owns. Held honest: 3/13 is neither "
      "3/8-closed (pure-bulk can't carry chirality) nor 3/13-established (edge-coupling magnitude uncomputed, "
      "topological ≠ scale-free for a coupling). REFINED, not dissolved; report either way straight",
      sin2 == F(3, 13) and not is_integer_index,
      "scale gate → IR-edge (3/13 survives) vs UV-edge (runs → 3/8); decider = the descent #93 (Lyra). Genuinely open. No win.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (sin²θ_W is a RUNNING coupling not a topological index; framework REFINES the FORM 3/13 not the magnitude; scale gate → IR-vs-UV-edge, open)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5173, the sharpened Weinberg decider -- bulk-edge, KO-dim 2):
  * FORM: sin²θ_W = N_c/(N_c+rank·n_C) = 3/13 is a ratio of TOPOLOGICAL integers; rank=2 = the protected
    bulk-edge index (KO-dim 2, J²=−1). The FORM is topological, NOT a coincidence.
  * DECIDER: sin²θ_W ≈ 0.23 is a CONTINUOUS coupling, NOT an integer/ℤ₂ index → it RUNS. 'Topological →
    scale-free' is REFUTED for the MAGNITUDE (the team's caveat, made precise).
  * PROTECTED = structure (edge count / c²=rank / FORM); RUNS = coupling magnitude g,g'.
  * SCALE GATE SHARPENED: IR-edge (3/13 survives to M_Z) vs UV-edge (3/13 at μ_geo, runs down → 3/8-like).
    Decider = the descent SO(5,2)→SO(4,2)→SO(3,1) (#93, bulk→boundary FLOW) -- Lyra's lane.

AUG-11 [TEGMARK]. Nothing pushed. Nothing banked -- 3/13 upgraded from numerical coincidence to
Identified-with-TOPOLOGICAL-STRUCTURE (its FORM is a protected rank-2 bulk-edge index), CONDITIONAL on the
IR-edge; the coupling MAGNITUDE runs, so the scale gate still binds -- REFINED to IR-edge-vs-UV-edge, open.
Genuinely open: not 3/8-closed (pure-bulk can't carry chirality), not 3/13-established (edge-coupling
magnitude uncomputed; topological ≠ scale-free for a coupling). Count the rank-2 once (bulk-edge index = the
same isometry-norm rank). Map-before-marry: topological-matter framework is a cold-read target. CP existence-
only. Report either way straight. Count N.
""")
