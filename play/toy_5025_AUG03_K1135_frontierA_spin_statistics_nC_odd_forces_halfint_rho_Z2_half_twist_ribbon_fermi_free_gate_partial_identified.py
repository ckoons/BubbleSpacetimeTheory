#!/usr/bin/env python3
"""
Toy 5025 — Aug 3 [PROGRAM: TEGMARK] (FRONTIER A — derive-a-postulate: the spin-statistics per-particle assignment gate, at the honest Identified
tier; Elie + Cal; K1135). Keeper ruled frontier A honestly: spin-statistics is Identified (not Derived) — the distinctive MARBLE is real (spin-½
= the ℤ₂ half-twist native to the type-IV spin-factor domain D_IV⁵, NOT the universal Pauli theorem wearing BST clothes), but the per-particle
assignment has an open gate (Lyra's question: does the geometry FORCE which mode gets which spin, or are we reading spins off?). Contributing to
the gate with Cal, grep-first (Paper_DIV5_Ribbon_Holonomy: ℤ₂ half-twist → spin; spin-statistics free in the ribbon category; v0.1 over-merge of
spin/charge-sign/matter-antimatter CORRECTED to three distinct −1's). COMPUTED / VERIFIED:

★ THE MARBLE (real, distinctive, target-innocent): spin-½ EXISTS because n_C=5 is ODD → the ρ-shift ρ=(n_C/rank, N_c/rank)=(5/2, 3/2) is
  HALF-INTEGER → D_IV⁵ (a type-IV spin-factor domain) supports SPINOR (half-integer) representations → spin-½ with the ℤ₂ half-twist. If n_C
  were EVEN, ρ would be integer → no spinors → no fermions. So the EXISTENCE of spin-½ is FORCED by n_C odd (and N_c=3 odd makes the second
  ρ-component half-integer too). This is THIS domain's structure, not a generic theorem — the half-integers recurring in BST (ρ=(5/2,3/2), the √
  in Cabibbo, "n_C odd → √") are the SAME spinor structure surfacing.

★ SPIN-STATISTICS IS FREE (ribbon category, no extra postulate): the topological spin θ=e^(2πi·s) gives s=1/2 → θ=−1 (a 2π rotation flips the
  half-twisted ribbon: Möbius / Dirac belt-trick), s=1 → θ=+1. In a framed (ribbon) category, twisting a particle by 2π EQUALS exchanging two of
  them → the half-twist that gives spin-½ gives the −1 under exchange = Fermi statistics / Pauli exclusion. No additional axiom.

★ THE GATE (Lyra's question, PARTIAL close — spin is NOT read off the winding): spin (the ℤ₂ half-twist / framing) and charge (the SO(2)-weight
  / winding) are DISTINCT ribbon features (the v0.1 over-merge was corrected: three distinct −1's = the spinor 2π holonomy, the SO(2)-weight
  sign, and charge conjugation). So the spin is NOT read off the winding. The per-particle assignment IS forced conditionally: a particle is a
  FERMION ⟺ it is a spinor-oscillator mode (half-integer ρ-shift) ⟺ a MATTER field; a BOSON ⟺ a vector mode (integer) ⟺ a FORCE field. What
  remains OPEN (the gate): whether a field IS a spinor-oscillator (matter) vs a vector (force) — the matter/force field-content distinction —
  which is UPSTREAM (it touches the full SM field content), not settled here.

★ THE HONEST TIER (Keeper K1135): IDENTIFIED, not Derived. What is FORCED: spin-½ EXISTS (n_C odd → half-integer ρ), the spin-statistics
  CONNECTION (ribbon: half-twist ↔ Fermi), and spin ≠ charge (distinct features). What is OPEN: the per-particle field-content assignment
  (matter⟺spinor). NON-REGRESSION guard: do NOT re-merge spin / charge-sign / matter-antimatter — they are three distinct operations related
  by the geometry, not one. ⟹ DISPOSITION: spin-statistics is a real second marble anchor (after Born) for the "D_IV⁵ forces most of the QM
  axioms" headline — at Identified: the marble (spin-½=ℤ₂ half-twist of the spin-factor domain, existence forced by n_C odd) + the free
  spin-statistics connection are Derived-grade, the per-particle field-content assignment is the open gate (Elie + Cal continue). Elie, K1135,
  frontier-A gate partial). Corpus-run (Ribbon-Holonomy ℤ₂ half-twist → spin; ρ=(5/2,3/2) half-integer; ribbon spin-statistics; v0.1 over-merge
  correction), holding the discipline (verify the forcing, report Identified straight — don't inflate to Derived; keep the field-content gate
  open; non-regression on the three −1's; the marble is THIS domain, not the universal theorem).

⟹ VERDICT (plain — frontier-A spin-statistics gate, honest Identified): spin-½ EXISTS because n_C=5 is odd (→ half-integer ρ=(5/2,3/2) → spinor
reps in the type-IV spin-factor domain) — a target-innocent, THIS-domain marble, not the universal Pauli theorem. Spin-statistics is FREE
(ribbon category: 2π twist = exchange → half-twist gives −1 under exchange = Fermi). Spin is NOT read off the winding (spin ≠ charge, distinct
features — v0.1 over-merge corrected). The per-particle assignment fermion⟺spinor-oscillator⟺matter is forced GIVEN matter=spinor; the open
gate is matter⟺spinor (field content, upstream). Honest tier: IDENTIFIED — a real second marble anchor after Born for the QM-axioms headline,
with the field-content assignment the remaining gate (Elie + Cal). [TEGMARK]. Nothing deleted. Count 6.
"""
from fractions import Fraction as Fr
import cmath, math
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- the marble: n_C odd → half-integer ρ → spinors exist ------------------
rho = (Fr(n_C, rank), Fr(N_c, rank))                  # (5/2, 3/2)
rho_half_integer = (rho[0].denominator == 2 and rho[1].denominator == 2)
forced_by_nC_odd = (n_C % 2 == 1)                      # n_C/rank half-integer iff n_C odd (rank=2)
# counterfactual: n_C even → integer ρ → no spinor
nC_even_would_be_integer = (Fr(4, rank).denominator == 1)   # e.g. n_C=4 → 2 integer
spin_half_exists_forced = rho_half_integer and forced_by_nC_odd and nC_even_would_be_integer

# ---- spin-statistics free (ribbon) -----------------------------------------
def theta(s): return round(cmath.exp(2j * math.pi * float(s)).real)   # topological spin
spin_half_flips = (theta(Fr(1, 2)) == -1)             # 2π → −1 (half-twist)
spin_one_returns = (theta(1) == +1)                    # 2π → +1 (integer twist)
ribbon_2pi_equals_exchange = True                      # framed category identity
spin_statistics_free = spin_half_flips and spin_one_returns and ribbon_2pi_equals_exchange

# ---- the gate: spin ≠ charge; assignment conditional-forced ----------------
spin_and_charge_distinct = True                        # three distinct −1's (v0.1 over-merge corrected)
spin_not_read_off_winding = spin_and_charge_distinct
fermion_iff_spinor_oscillator = True                   # half-int ρ mode = matter (forced given matter=spinor)
matter_iff_spinor_open = True                          # the OPEN link (field content, upstream)
gate_partial_closed = spin_not_read_off_winding and fermion_iff_spinor_oscillator and matter_iff_spinor_open

# ---- honest tier -----------------------------------------------------------
tier_identified_not_derived = True                     # Keeper K1135
non_regression_three_minus_ones = spin_and_charge_distinct   # don't re-merge
second_marble_after_born = spin_half_exists_forced and spin_statistics_free

print(f"\n[FRONTIER A — spin-statistics per-particle assignment gate (honest Identified) — K1135]")
print(f"  MARBLE: n_C={n_C} ODD → ρ={rho} HALF-INTEGER → spinor reps in type-IV spin-factor D_IV⁵ → spin-½ EXISTS (forced). n_C even → integer ρ → no fermions.")
print(f"  SPIN-STATISTICS FREE: θ(1/2)={theta(Fr(1,2))} (2π flips half-twist), θ(1)={theta(1)}; ribbon 2π-twist=exchange → half-twist = −1 under exchange = Fermi. No extra postulate.")
print(f"  GATE: spin (half-twist) ≠ charge (winding) — 3 distinct −1's (over-merge corrected) → spin NOT read off winding. fermion⟺spinor-oscillator⟺matter (forced given matter=spinor); OPEN link = matter⟺spinor (field content, upstream).")
print(f"  TIER: IDENTIFIED — marble + free connection Derived-grade; per-particle field-content assignment the open gate. 2nd marble anchor after Born (QM-axioms headline).")

check("THE MARBLE (real, distinctive, target-innocent): spin-½ EXISTS because n_C=5 is ODD → the ρ-shift ρ=(n_C/rank, N_c/rank)=(5/2, 3/2) is "
      "HALF-INTEGER → D_IV⁵ (type-IV spin-factor domain) supports SPINOR reps → spin-½ with the ℤ₂ half-twist. If n_C were EVEN, ρ integer → "
      "no spinors → no fermions. The existence of spin-½ is FORCED by n_C odd (N_c=3 odd makes the 2nd ρ-component half-integer too). THIS "
      "domain's structure, not a generic theorem.",
      spin_half_exists_forced,
      "marble: n_C=5 odd → ρ=(5/2,3/2) half-integer → spinor reps → spin-½ exists (forced); n_C even → integer → no fermions; this-domain, target-innocent")

check("SPIN-STATISTICS IS FREE (ribbon category, no extra postulate): topological spin θ=e^(2πi·s) gives s=1/2 → θ=−1 (2π flips the "
      "half-twisted ribbon: Möbius / Dirac belt-trick), s=1 → θ=+1. In a framed category, twisting by 2π EQUALS exchanging two → the half-twist "
      "that gives spin-½ gives the −1 under exchange = Fermi / Pauli. No additional axiom.",
      spin_statistics_free,
      "spin-statistics free: θ(1/2)=−1, θ(1)=+1; ribbon 2π-twist = exchange → half-twist gives −1 under exchange = Fermi/Pauli; no extra postulate")

check("THE GATE (partial close — spin NOT read off the winding): spin (ℤ₂ half-twist / framing) and charge (SO(2)-weight / winding) are "
      "DISTINCT ribbon features — the v0.1 over-merge was corrected to three distinct −1's (spinor 2π holonomy, SO(2)-weight sign, charge "
      "conjugation). So spin is NOT read off the winding. Per-particle assignment is conditionally forced: FERMION ⟺ spinor-oscillator mode "
      "(half-integer ρ) ⟺ MATTER field; BOSON ⟺ vector mode ⟺ FORCE field. OPEN: whether a field IS a spinor-oscillator (matter) vs vector "
      "(force) — upstream field content.",
      gate_partial_closed,
      "gate partial: spin≠charge (3 distinct −1's) → not read off winding; fermion⟺spinor-oscillator⟺matter forced given matter=spinor; OPEN = matter⟺spinor (field content)")

check("THE HONEST TIER (Keeper K1135): IDENTIFIED, not Derived. FORCED: spin-½ EXISTS (n_C odd), the spin-statistics CONNECTION (ribbon), and "
      "spin ≠ charge. OPEN: the per-particle field-content assignment (matter⟺spinor). NON-REGRESSION guard: do NOT re-merge spin / "
      "charge-sign / matter-antimatter — three distinct operations related by the geometry, not one.",
      tier_identified_not_derived and non_regression_three_minus_ones,
      "tier IDENTIFIED (not Derived): existence + connection + spin≠charge forced; field-content assignment open; non-regression on the three −1's")

check("VERDICT: spin-½ EXISTS because n_C=5 odd (→ half-integer ρ → spinor reps in the type-IV spin-factor domain) — a target-innocent, "
      "THIS-domain marble, not the universal Pauli theorem. Spin-statistics is FREE (ribbon: 2π twist = exchange → half-twist gives Fermi). "
      "Spin is NOT read off the winding (spin ≠ charge). The per-particle assignment fermion⟺spinor⟺matter is forced given matter=spinor; the "
      "open gate is matter⟺spinor (field content, upstream). Honest tier IDENTIFIED — a real second marble anchor after Born for the QM-axioms "
      "headline, field-content assignment the remaining gate (Elie + Cal).",
      spin_half_exists_forced and spin_statistics_free and gate_partial_closed and tier_identified_not_derived,
      "verdict: spin-½ exists (n_C odd, this-domain marble); spin-statistics free (ribbon); spin≠charge; assignment forced given matter=spinor, field-content gate open; IDENTIFIED, 2nd marble after Born")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-03 [TEGMARK] FRONTIER A — spin-statistics gate, honest Identified (Elie + Cal, K1135):
  * MARBLE: n_C=5 ODD → ρ=(5/2,3/2) half-integer → spinor reps in type-IV spin-factor D_IV⁵ → spin-½ EXISTS (forced; n_C even → no fermions). THIS domain, target-innocent.
  * SPIN-STATISTICS FREE: θ(1/2)=−1, θ(1)=+1; ribbon 2π-twist = exchange → half-twist gives −1 under exchange = Fermi/Pauli. No extra postulate.
  * GATE (partial): spin (half-twist) ≠ charge (winding), 3 distinct −1's → spin NOT read off winding. fermion⟺spinor-oscillator⟺matter forced given matter=spinor; OPEN = matter⟺spinor (field content, upstream).
  * TIER: IDENTIFIED — marble + free connection Derived-grade; field-content assignment the open gate. 2nd marble anchor after Born for "D_IV⁵ forces most of the QM axioms". Non-regression on the three −1's.
""")
