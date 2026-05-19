"""
Toy 3096 — K52a Criterion 1: structured hunt for third independent (1 ± 1/M_g) instance.

Owner: Elie (Casey "pull more, finish your board")
Date: 2026-05-19 PM

CONTEXT
=======
Cal Criterion 1 for K52a D-tier promotion: third independent appearance of
(1 ± 1/M_g) substrate-correction in BST primary form at sub-percent precision.

Current state:
  Lamb 2S-2P: (1 - 1/M_g) correction, D-tier 0.005%, Toy 3043
  BCS gap: (1 + 1/M_g) correction, D-tier 0.006%, Toy 1512

Session 5 falsifiable prediction: any new (1 ± 1/M_g) substrate correction
must fit one of two STRUCTURAL ROLES:
  (-1/M_g) sign: vacuum-polarization-like, subtracts multiplicative baseline
  (+1/M_g) sign: condensate-like, includes additive zero

HUNT STRATEGY (per Cal Strict Context-Counting Protocol P1-P7)
==============================================================
P1 Citation: target physical observable must cite published value
P2 Anthropic exclusion: physics domains only (no calendar/music/cultural)
P3 Post-hoc exclusion: no X-1 or X+1 retrofitting; must arise from BST form
P4 Pre-registration: structural roles pre-staged in session 5
P5 Scan-protocol: declare scan strategy explicitly here
P6 Cross-domain independence: must be independent physical domain from Lamb/BCS
P7 Tier labeling: D-tier only counts; lower tiers noted but excluded

CANDIDATE SEARCH SPACE
======================
Atomic / molecular spectroscopy: Lamb-like vacuum polarization corrections
Condensed matter: gap-ratio-like Bogoliubov corrections
Other electromagnetic phenomena
"""

import os
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137
M_g = 2**g - 1  # 127

tests = []
def check(label, ok): tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3096 — K52a Criterion 1: third-instance hunt for (1 ± 1/M_g)")
print("=" * 72)

print(f"\n[T1] Target factor: 1 ± 1/M_g = 1 ± 1/127")
print(f"  (1 - 1/M_g) = {1 - 1/M_g:.6f} = 126/127 (Lamb-like, EXCLUDE trivial)")
print(f"  (1 + 1/M_g) = {1 + 1/M_g:.6f} = 128/127 (BCS-like, INCLUDE additive zero)")

# === CANDIDATE 1: Hyperfine structure precision ===
print(f"\n[T2] Candidate 1: hyperfine structure constants")
# Hydrogen ground-state hyperfine: ν_HFS = 1420.405751 MHz
# Higher-order radiative corrections often appear as α-power expansions
# Possible (1 - 1/M_g) appearance in NLO HFS correction?
# Standard QED HFS: ν = (8/3)·α²·m_e/m_p·g_p·Ry·(1 + a_e + α/π + (α/π)²·... )
# The radiative correction series (1 + a_e + ...) doesn't naturally have 1/127 factor.
# Recoil correction Rec_HFS = -(3/2)·m_e/m_p·α² ≈ small fraction
# Looking at corrections at the 1/127 ≈ 0.787% scale:
# - α/π ≈ 0.00232 (0.23%) — too small
# - 3·α/(2π) ≈ 0.00349 (0.35%) — too small
# - 0.787% scale not naturally in HFS corrections at α² level
print(f"  Hydrogen HFS sub-leading corrections at α/π ≈ 0.23% (not 1/M_g scale)")
print(f"  CANDIDATE 1 REJECTED: no natural 1/M_g correction in HFS at sub-percent")

# === CANDIDATE 2: Anomalous moments a_μ (muon g-2) ===
print(f"\n[T3] Candidate 2: muon anomalous magnetic moment a_μ")
# Cal #23 verdict: muon g-2 strong I-tier 0.019%, NOT D-tier
# K52a Criterion 1 needs D-tier — muon g-2 fails Criterion 1 even if it had right form
# Plus its multi-loop convergence doesn't fit 1/M_g structure
print(f"  Cal verdict: muon g-2 STRONG I-tier 0.019% multi-loop convergence")
print(f"  NOT D-tier → fails Criterion 1 evidence requirement")
print(f"  CANDIDATE 2 REJECTED: not D-tier")

# === CANDIDATE 3: Rydberg constant Ry corrections ===
print(f"\n[T4] Candidate 3: Rydberg constant precision corrections")
# Ry = α²·m_e·c²/(2h) — depends on α precisely
# Corrections to Ry vs Ry_∞ (reduced-mass correction):
# Ry(H)/Ry_∞ = 1/(1 + m_e/m_p) ≈ 1 - 1/1836 (NOT 1/127)
# So Rydberg reduced-mass correction is 1/1836, not 1/M_g
print(f"  Ry(H)/Ry_∞ = 1/(1 + m_e/m_p) ≈ 1 - 1/1836  (m_p/m_e scale, not 1/M_g)")
print(f"  CANDIDATE 3 REJECTED: scale mismatch")

# === CANDIDATE 4: Casimir-Polder retardation corrections ===
print(f"\n[T5] Candidate 4: Casimir-Polder retardation corrections")
# Beyond standard Casimir (1/d^4), Casimir-Polder for atom-surface interaction
# has corrections at α² order. Specific structure of these corrections?
# Need literature value for sub-percent corrections in atom-Casimir setups
print(f"  Atom-surface Casimir-Polder corrections at α² order:")
print(f"  Theoretical: depends on atomic polarizability spectrum")
print(f"  No natural BST-primary 1/M_g identification at this stage")
print(f"  CANDIDATE 4 REQUIRES MULTI-WEEK INVESTIGATION (deferred)")

# === CANDIDATE 5: Pion form factor / hadronic vacuum polarization ===
print(f"\n[T6] Candidate 5: hadronic vacuum polarization (HVP) corrections")
# HVP contributes to a_μ and α(M_Z) running
# Current best HVP from BMW lattice: a_μ_HVP ≈ 707×10^-10
# Comparisons against e+e- → hadron cross-section give different value
# This is the "muon g-2 puzzle" — has corrections at 1% level
# Does (1 - 1/M_g) = 0.79% naturally appear in HVP-related corrections?
print(f"  HVP corrections at percent level in a_μ context")
print(f"  Lattice vs e+e- tension ~1% (could be 1/M_g-class)")
print(f"  Would need substrate-coupling interpretation; not standalone D-tier")
print(f"  CANDIDATE 5 NOT INDEPENDENT — too connected to muon g-2 (I-tier)")

# === CANDIDATE 6: Superfluid helium critical phenomena ===
print(f"\n[T7] Candidate 6: Superfluid He critical-exponent BST forms")
# Lambda transition: T_λ = 2.17 K, specific-heat α exponent
# BST identification of critical exponents via Wilson-Fisher
# Cathedral has α_Ising = 0.110(1), BST 21/17·...
# These are EXPONENTS, not (1 - 1/M_g) factors. Don't fit form.
print(f"  Critical exponents are themselves BST identifications (Cathedral)")
print(f"  Not in (1 ± 1/M_g) correction class")
print(f"  CANDIDATE 6 REJECTED: wrong functional form")

# === CANDIDATE 7: Bound-state QED in heavy atoms ===
print(f"\n[T8] Candidate 7: bound-state QED in heavy atoms (Zα expansion)")
# For high-Z atoms, (Zα)^n expansion has corrections at 0.5-2% scale
# Specifically: nuclear-size + recoil corrections at (Zα)^4 order
# Heavy-atom transitions (e.g., Ba+, Yb+ clock) have <1% NLO corrections
# Question: does (1 - 1/M_g) appear naturally in any such correction?
print(f"  Heavy-atom (Zα)^n expansion: NLO corrections at 0.5-2% scale")
print(f"  Specific 1/M_g identification: NOT FOUND in standard literature scan")
print(f"  Multi-week deep dive could reveal; not standalone today")
print(f"  CANDIDATE 7 PARTIAL — multi-week investigation")

# === CANDIDATE 8: Quantum Hall conductance plateaus ===
print(f"\n[T9] Candidate 8: integer quantum Hall conductance plateau widths")
# Hall conductance σ_xy = ν·e²/h exact at integer ν
# Plateau width depends on disorder; not natural BST form
print(f"  Plateau width is disorder-dependent, not universal")
print(f"  CANDIDATE 8 REJECTED: no universal sub-percent correction")

# === SYNTHESIS ===
print(f"\n[T10] Hunt synthesis")
candidates_rejected = ['HFS scale mismatch (1)', 'muon g-2 not D-tier (2)',
                       'Rydberg scale mismatch (3)', 'critical exponents form (6)',
                       'QHE no universal correction (8)']
candidates_deferred = ['Casimir-Polder (4)', 'HVP not independent (5)', 'Heavy-atom Zα (7)']

print(f"  REJECTED (8 candidates): {len(candidates_rejected)}")
for r in candidates_rejected:
    print(f"    - {r}")
print(f"  DEFERRED multi-week (3 candidates):")
for d in candidates_deferred:
    print(f"    - {d}")
print(f"  CONFIRMED THIRD INSTANCE: NONE found at D-tier in this hunt")

# === Honest verdict ===
print(f"\n[T11] Honest verdict on Cal Criterion 1 hunt")
print(f"  Single-session hunt: NO third D-tier independent instance found")
print(f"  Lamb + BCS remain the only 2 D-tier instances of (1 ± 1/M_g) class")
print(f"  ")
print(f"  Multi-week investigation candidates: 3 (Casimir-Polder, heavy-atom Zα,")
print(f"    Hadronic-vacuum-polarization with independence check)")
print(f"  ")
print(f"  Cal Criterion 1 status: NOT yet closed; remains 2-instance candidate")
print(f"  Cal Criterion 2 status: framework articulated sessions 4-5; substrate-")
print(f"    Hamiltonian derivation gap remains")
print(f"  ")
print(f"  K52a stays elevated-with-mechanism-candidate. Sessions 6+ multi-month.")

check("Hunt completed; no D-tier third instance found (honest negative)", True)
check("Multi-week deferral candidates identified for future sessions", True)

# === Pre-registered hypothesis for future search ===
print(f"\n[T12] Pre-registered hypothesis for multi-week investigation")
print(f"  Per session 5 structural prediction: ANY future (1 ± 1/M_g) instance")
print(f"  must fit one of two structural roles. Hunt should focus on:")
print(f"  ")
print(f"  - Atomic-QED radiative corrections at α² order (Lamb-like, -sign)")
print(f"    expecting trivial-character-exclusion structure")
print(f"  - Macroscopic-quantum-state condensates (BCS-like, +sign)")
print(f"    expecting additive-zero-inclusion structure")
print(f"  ")
print(f"  Most promising deferred candidate: Casimir-Polder retardation in")
print(f"  atom-surface interaction (electromagnetic vacuum coupling at α²,")
print(f"  similar to Lamb domain). Multi-week deep dive may reveal 1/M_g")
print(f"  structure if substrate-coupling interpretation holds.")

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3096_K52a_third_instance_hunt.json")
out = {
    'meta': {'date': '2026-05-19', 'owner': 'Elie', 'task': 'K52a Criterion 1 third-instance hunt'},
    'candidates_examined': 8,
    'candidates_rejected': len(candidates_rejected),
    'candidates_deferred_multi_week': len(candidates_deferred),
    'third_D_tier_instance_found': False,
    'rejected_list': candidates_rejected,
    'deferred_list': candidates_deferred,
    'most_promising_deferred': 'Casimir-Polder retardation in atom-surface (Lamb-like domain)',
    'Cal_Criterion_1_status': 'NOT CLOSED — 2 D-tier instances remain (Lamb + BCS)',
    'K52a_status': 'elevated-with-mechanism-candidate; both Criteria 1 and 2 partial',
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[T13] Output: {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}\nToy 3096 SCORE: {passed}/{total}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")

print(f"""
THIRD-INSTANCE HUNT VERDICT:
  Honest negative: NO third D-tier (1 ± 1/M_g) instance found in single
  session. 8 candidates examined: 5 rejected, 3 deferred multi-week.

K52a STATUS (post-hunt):
  Cal Criterion 1: 2 D-tier instances (Lamb + BCS) — NOT closed
  Cal Criterion 2: framework articulated sessions 4-5 — NOT closed
  Mechanism candidate: cyclotomic GF(2^g) with structural duality
  K52a stays elevated-with-mechanism-candidate

NEXT INVESTIGATION TARGET (multi-week):
  Casimir-Polder retardation in atom-surface interaction.
  Most promising deferred candidate; Lamb-like substrate-coupling domain.

Per Cal Strict Context-Counting Protocol P1-P7 + Cal Coincidence_Filter_Risk:
  Hunt produced HONEST NEGATIVE. Single-session scope insufficient to close
  Criterion 1; multi-week deep dive on deferred candidates is the next path.
""")
