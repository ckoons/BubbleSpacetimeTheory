#!/usr/bin/env python3
"""
Toy 4869 — Jul 26 (induced-Yang-Mills a₂ SETUP: sign first, routed through the confinement curvature; Elie, pull 26d, my
strong-sector lane, K-e). Keeper aimed the team: the QCD β-function via induced YM — the companion to the gravity work
(F60-F66). My lane is the a₂ (heat-kernel), TIER 1 = the SIGN (asymptotic freedom), routed through BST's confinement
curvature. SETUP/first-step on existing machinery, not a claimed derivation.

FIRST — OWN A CORRECTION (mine): my pull-26 message softened the muon (24/π²)⁶ to Grace's "live Jacobian route with two
gates." That was OVER-ENDORSING — I took Grace's prettier Jacobian framing WITHOUT running the τ-consistency check. Lyra
(F701)+Grace (K928) refuted it: the uniform Jacobian rule → m_τ/m_e=(24/π²)¹⁰≈7230 (carrying π), but τ=49·71=3479 (π-free) —
wrong ~2× AND wrong π-parity. My ORIGINAL "identified coincidence" lean was right; the softening was the error. Muon =
identified-coincidence, bucket-2, count 2, CLOSED. Owned.

THE INDUCED-YM SIGN STRUCTURE (TIER 1 — the standard decomposition BST must REPRODUCE from the induced action): the a₂ gives
F²_μν; its log-scale dependence gives b₀. b₀(gauge)/C_A = (paramagnetic +4) + (diamagnetic −1/3) = 11/3:
  * +4 = color-MAGNETIC moment (spin-1, NON-ABELIAN self-coupling, g=2) → ANTISCREENING.
  * −1/3 = orbital/diamagnetic → screening.
  +4 BEATS −1/3 → net positive → antiscreening. Fermions: −2/3 per T_R·N_f (QED-like screening). BST content (N_c=3,N_f=6):
  11·N_c − 2·N_f = 21 > 0 → ASYMPTOTICALLY FREE.

THE BST UNIFICATION TARGET (Lyra's aim — the result, not the re-import): the antiscreening sign comes from the gluon's
NON-ABELIAN self-coupling (+4 paramagnetic). BST derives CONFINEMENT from the SAME non-abelian color structure (colored ⟺
zero Shilov support / Schur, T2523). Genuine BST question: does the SAME non-abelian curvature that forces confinement ALSO
force the AF sign? If yes → confinement AND asymptotic freedom are ONE geometric structure in BST (as in nature).

⟹ VERDICT (plain): induced-YM a₂ route SET UP (companion to F60-F66), aimed at TIER 1 — the SIGN (b₀>0, from +4 paramagnetic
non-abelian beating −1/3 diamagnetic). Derivation-grade BST target: same curvature = confinement curvature (Schur/Shilov
T2523), unifying AF + confinement. TIER 2 (11/3 coefficient) FF-20-prone: must FALL OUT of Grace's book-sourced a₂, NOT a
c₂/dim-K shortcut. FF-20 traps QUARANTINED: elevens NOT welded (β-11 vs KK dim-K=11); β₀=g=7 is an IDENTIFICATION (7=g only at
all-6-flavors), not derived. SETUP/scoping toy — no BST claim banked; sign-from-confinement-curvature is the open work.
Machinery exists (Toys 241-278, T266 node). Partition theorem untouched. Five-Absence-positive. Count ~5.
"""
from fractions import Fraction as F
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

para, dia = F(4), F(-1, 3)
b0_gauge = para + dia
b0_num = 11 * N_c - 2 * 6
tau_jacobian = (24 / 3.14159265**2)**10
tau_obs = 49 * 71
tau_fails = abs(tau_jacobian - tau_obs) / tau_obs > 0.5
print(f"\n[induced-YM a₂] sign: para {para}+dia {dia}={b0_gauge}=11/3 (antiscreening); 11·N_c−2·N_f={b0_num}>0 → AF. muon τ-check: (24/π²)^10={tau_jacobian:.0f} vs 49·71={tau_obs} fails={tau_fails}")

check("OWN THE MUON OVER-ENDORSEMENT (τ refutes the Jacobian): I softened (24/π²)⁶ to a 'live Jacobian route' without the "
      "τ-check. Uniform rule → m_τ/m_e=(24/π²)¹⁰≈7230 (π), but τ=49·71=3479 (π-free) — wrong ~2× AND wrong parity (Lyra F701, "
      "Grace K928). Original 'identified coincidence' was right. Muon closed: bucket-2, count 2.",
      tau_fails,
      "muon Jacobian fails τ-consistency ((24/π²)^10≈7230 π vs 49·71=3479 π-free) → identified-coincidence closed; over-endorsement owned")

check("INDUCED-YM SIGN (TIER 1): b₀(gauge)/C_A = para(+4, color-magnetic moment, NON-ABELIAN self-coupling) + dia(−1/3, "
      "orbital) = 11/3; +4 BEATS −1/3 → ANTISCREENING. The sign origin the induced a₂ must reproduce.",
      b0_gauge == F(11, 3) and para > abs(dia),
      "b₀(gauge)=+4 para(non-abelian) −1/3 dia = 11/3; para beats dia → antiscreening (sign origin)")

check("ASYMPTOTIC FREEDOM for BST content (sign, TIER 1): 11·N_c − 2·N_f = 21 > 0 → b₀>0 → asymptotically free (gauge "
      "antiscreening dominates fermion screening).",
      b0_num == 21 and b0_num > 0,
      "11·N_c−2·N_f=21>0 → asymptotically free (gauge antiscreening beats fermion screening); the sign")

check("BST UNIFICATION TARGET (Lyra, derivation-grade): the +4 antiscreening comes from the gluon NON-ABELIAN self-coupling; "
      "BST derives CONFINEMENT from the SAME structure (colored⟺zero Shilov/Schur, T2523). TARGET: same curvature forces BOTH "
      "→ confinement AND asymptotic freedom = ONE geometric structure (as in nature). Open work, not banked.",
      True, "target: same non-abelian curvature forces confinement (Schur/Shilov T2523) AND the AF sign → one structure; open")

check("TIERS + FF-20 QUARANTINE: TIER 1 = SIGN (achievable, via confinement curvature); TIER 2 = 11/3 (must FALL OUT of "
      "Grace's book-sourced a₂, NOT a c₂/dim-K shortcut). Elevens NOT welded (β-11 vs KK dim-K=11, toy 4868); β₀=g=7 is an "
      "IDENTIFICATION (7=g only at all-6-flavors), not derived. Setup toy — nothing banked.",
      True, "TIER 1 sign / TIER 2 coefficient (Grace a₂, no shortcut); elevens quarantined; β₀=g=7 identification; setup, nothing banked")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-4 (07-26) induced-YM a₂ SETUP — sign first, via confinement curvature (Elie, pull 26d, strong-sector K-e):
  * OWN: muon 'live Jacobian route' softening was over-endorsing — τ-consistency refutes ((24/π²)^10≈7230 π vs 49·71=3479 π-free, Lyra F701/Grace K928). Original 'identified coincidence' right. Muon closed, bucket-2, count 2.
  * TIER 1 SIGN: b₀(gauge)=+4 para(non-abelian) −1/3 dia = 11/3 → antiscreening; 11·N_c−2·N_f=21>0 → asymptotically free.
  * BST TARGET (Lyra): same non-abelian curvature that forces confinement (Schur/Shilov T2523) must force the AF sign → confinement + AF = one structure (open derivation).
  * TIER 2 (11/3): must fall out of Grace's book-sourced a₂, no shortcut. Elevens quarantined; β₀=g=7 = identification. Setup, nothing banked. Machinery: Toys 241-278, T266.
""")
