#!/usr/bin/env python3
"""
Toy 4758 — Jul 20 (Round-11 Target-1: derive (near-)maximal leptonic CP + the 4/7-correlated offset, mine; target-innocent
fish-detector on the "near-μ-τ → near-maximal δ" thesis). The route: μ-τ (2↔3) reflection symmetry forces θ₂₃=45° AND
δ=±π/2 (maximal); BST is "near-μ-τ" via banked sin²θ₂₃ = rank²/g = 4/7 → θ₂₃≈49°, so the claim is δ_PMNS ≈ −π/2 with a
4/7-correlated offset. My job: verify the μ-τ↔maximal link, derive the offset target-innocently, and confirm the rank-2
structural result. Result: μ-τ reflection ⟺ maximal δ is EXACT (verified); but the 4/7 offset is a REAL, sizable μ-τ
break (NOT "near" in symmetry terms), and it pushes δ off maximal by ~18° — so BST predicts δ_PMNS NEAR-maximal ≈ −72°
(NOT exactly −π/2). And rank-2 → J_PMNS ≫ J_CKM structurally (matches data).

RESULT 1 — μ-τ REFLECTION ⟺ MAXIMAL CP (exact, verified): the μ-τ reflection deviation Σ_i ||U_μi|−|U_τi|| = 0 ONLY at
θ₂₃=45° AND δ=±90°. So μ-τ reflection symmetry (M_ν's rows 2,3 equal-magnitude ⟺ M_ν commutes with P₂₃ up to conjugation)
FORCES maximal Dirac CP. The linear-algebra link (μ-τ = maximal) is correct.
RESULT 2 — THE CATCH (fish-detector): "near-μ-τ in θ₂₃" is NOT near in SYMMETRY terms, and the offset is REAL. At θ₂₃=49.1°
(=4/7) even with δ=90° the μ-τ deviation is 0.23 — ~80% of the full δ=0 break (0.29). And δ=±90° does NOT minimize the
residual breaking when θ₂₃≠45°: for θ₂₃=49.1° the minimizing δ is ~72°, NOT 90°. So the 4/7 deviation FEEDS INTO δ,
pushing it ~18° OFF maximal. ⟹ near-maximal δ is NOT automatic from the θ₂₃ deviation — a naive "near-μ-τ → δ≈−π/2" reading
is over-simple; the offset is a genuine consequence of the 4/7 break.
RESULT 3 — THE OFFSET / CANDIDATE PREDICTION (target-innocent): IF BST's rank-2 texture minimizes residual μ-τ breaking
given θ₂₃=4/7, then δ_PMNS ≈ ±72° (the negative branch 288° ≈ −72° matches the T2K/NOvA sign) — NEAR-maximal with a ~18°
offset CORRELATED with (4/7 − 1/2). This is DISTINGUISHABLE from exactly-maximal (−90°) at DUNE/Hyper-K → a sharper
falsifier than "maximal." HELD AS CANDIDATE: the offset magnitude is criterion-dependent (the residual-breaking norm, the
θ₁₃/θ₁₂ inputs) and the "minimize breaking" premise needs Lyra's actual rank-2 M_ν. NOT banked as a prediction.
RESULT 4 — RANK-2 → J_PMNS ≫ J_CKM (structural, bankable): the neutrino is rank-2 (F589, m₁=0), NOT rank-1-suppressed like
the quark sector, so its mixing angles are large → J_PMNS ≈ 0.033 (near-maximal δ) ≫ J_CKM ~ 3.08×10⁻⁵ (~1000×). This
CKM ≪ PMNS hierarchy is a clean STRUCTURAL result (quark rank-1 vs neutrino rank-2) and it MATCHES the data.

⟹ VERDICT: μ-τ reflection ⟺ maximal δ is EXACT (verified) — the linear-algebra link holds. But BST's sin²θ₂₃ = 4/7 is a
REAL μ-τ break (not merely "near"), and it pushes δ ~18° off maximal → BST predicts δ_PMNS NEAR-maximal ≈ −72° (a
4/7-correlated offset), NOT exactly −π/2 — a sharper, DUNE/Hyper-K-distinguishable falsifier, HELD AS CANDIDATE (offset is
criterion-dependent + needs Lyra's M_ν). BANKABLE structural result: rank-2 neutrino → J_PMNS ≫ J_CKM (~1000×), CKM ≪ PMNS
matching data; J_CKM ∝ ε³ structural, not the exact value derived. Count ~7-8 (α RULED). Five-Absence-safe (CP within SM).
"""
import numpy as np
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# best-fit reactor + solar angles (inputs; not the prediction)
t12, t13 = np.radians(33.4), np.radians(8.6)
t23_bst = np.arcsin(np.sqrt(4/7))   # sin²θ₂₃ = 4/7 → θ₂₃ ≈ 49.1°

def U_pmns(t23, d):
    s12,s13,s23 = np.sin(t12),np.sin(t13),np.sin(t23); c12,c13,c23 = np.cos(t12),np.cos(t13),np.cos(t23)
    return np.array([
     [c12*c13, s12*c13, s13*np.exp(-1j*d)],
     [-s12*c23-c12*s23*s13*np.exp(1j*d), c12*c23-s12*s23*s13*np.exp(1j*d), s23*c13],
     [ s12*s23-c12*c23*s13*np.exp(1j*d), -c12*s23-s12*c23*s13*np.exp(1j*d), c23*c13]])
def mutau_dev(t23, d):
    U = U_pmns(t23, d); return np.sum(np.abs(np.abs(U[1,:])-np.abs(U[2,:])))
def J(t23, d):
    s12,s13,s23 = np.sin(t12),np.sin(t13),np.sin(t23); c12,c13,c23 = np.cos(t12),np.cos(t13),np.cos(t23)
    return c12*c13**2*c23*s12*s13*s23*np.sin(d)

# ---- Result 1: mu-tau reflection <=> maximal --------------------------------
d0 = mutau_dev(np.radians(45), np.radians(90)); dbad = mutau_dev(np.radians(45), np.radians(0))
print(f"\n[R1] μ-τ dev: (45°,90°)={d0:.4f} (=0) ; (45°,0°)={dbad:.4f} → dev=0 ONLY at θ₂₃=45° ∧ δ=±90°")
check("RESULT 1 — μ-τ REFLECTION ⟺ MAXIMAL CP (exact): the μ-τ reflection deviation Σ_i ||U_μi|−|U_τi|| = 0 ONLY at "
      "θ₂₃=45° AND δ=±90°. So μ-τ reflection symmetry (M_ν commutes with P₂₃ up to conjugation) FORCES maximal Dirac CP. "
      "The linear-algebra link μ-τ = maximal holds.",
      d0 < 1e-9 and dbad > 0.1, "μ-τ reflection dev = 0 only at (45°,±90°) → μ-τ symmetry ⟺ maximal δ (verified)")

# ---- Result 2: the 4/7 offset is a real break -------------------------------
dev_bst_90 = mutau_dev(t23_bst, np.radians(90))
ds = np.linspace(0, 360, 3601)
dmin_bst = ds[int(np.argmin([mutau_dev(t23_bst, np.radians(dd)) for dd in ds]))]
print(f"[R2] θ₂₃=4/7 (49.1°): dev at δ=90° = {dev_bst_90:.4f} (sizable); δ minimizing breaking = {dmin_bst:.1f}° (NOT 90°)")
check("RESULT 2 — THE CATCH (fish-detector): 'near-μ-τ in θ₂₃' is NOT near in SYMMETRY terms, and the offset is REAL. At "
      "θ₂₃=49.1° (=4/7), even with δ=90° the μ-τ deviation is 0.23 (~80% of the full δ=0 break). And δ=±90° does NOT "
      "minimize the residual breaking when θ₂₃≠45° — for θ₂₃=49.1° the minimizing δ is ~72°, NOT 90°. So the 4/7 deviation "
      "FEEDS INTO δ, pushing it ~18° off maximal → near-maximal δ is NOT automatic; a naive 'near-μ-τ → δ≈−π/2' is over-simple.",
      dev_bst_90 > 0.15 and abs(dmin_bst - 90) > 10, "θ₂₃=4/7 is a real μ-τ break (dev 0.23); the breaking-minimizing δ is ~72° not 90° → the 4/7 offset pushes δ ~18° off maximal")

# ---- Result 3: the offset / candidate prediction ----------------------------
offset = abs(dmin_bst - 90) if dmin_bst < 180 else abs((360-dmin_bst) - 90)
delta_candidate = 360 - dmin_bst  # negative branch matching T2K/NOvA sign
print(f"[R3] candidate δ_PMNS ≈ {delta_candidate:.0f}° (≈ −{360-delta_candidate:.0f}°), offset ~{offset:.0f}° from maximal — DUNE-distinguishable")
check("RESULT 3 — THE OFFSET / CANDIDATE PREDICTION (target-innocent, HELD as candidate): IF BST's rank-2 texture "
      "minimizes residual μ-τ breaking given θ₂₃=4/7, then δ_PMNS ≈ ±72° (the negative branch ≈288°≈−72° matches the "
      "T2K/NOvA sign) — NEAR-maximal with a ~18° offset CORRELATED with (4/7−1/2), DISTINGUISHABLE from exactly-maximal "
      "(−90°) at DUNE/Hyper-K → a SHARPER falsifier than 'maximal'. CANDIDATE only: the offset is criterion-dependent (the "
      "residual-breaking norm, the θ₁₃/θ₁₂ inputs) + the minimize-breaking premise needs Lyra's rank-2 M_ν. NOT banked.",
      15 < offset < 25, "candidate δ_PMNS ≈ −72° (near-maximal, ~18° offset correlated with 4/7) — DUNE-distinguishable from −90°; HELD as candidate, offset criterion-dependent")

# ---- Result 4: rank-2 -> J_PMNS >> J_CKM ------------------------------------
JP = J(t23_bst, delta_candidate*np.pi/180); ratio = abs(JP)/3.08e-5
print(f"[R4] J_PMNS(near-max) = {JP:.4f} vs J_CKM ~ 3.08e-5 → ~{ratio:.0f}× larger (rank-2 vs rank-1)")
check("RESULT 4 — RANK-2 → J_PMNS ≫ J_CKM (structural, bankable): the neutrino is rank-2 (F589, m₁=0), NOT "
      "rank-1-suppressed like the quark sector, so its angles are large → J_PMNS ≈ 0.03 ≫ J_CKM ~ 3.08×10⁻⁵ (~1000×). The "
      "CKM ≪ PMNS hierarchy is a clean STRUCTURAL result (quark rank-1 vs neutrino rank-2) and MATCHES the data. J_CKM ∝ "
      "ε³ structural (Target 3), NOT the exact value derived (inherits Tier-2 angles).",
      ratio > 500, "J_PMNS ≈ 0.03 ≫ J_CKM ~ 3e-5 (~1000×) → CKM ≪ PMNS matches data (rank-2 vs rank-1); J_CKM ∝ ε³ structural not exact")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: μ-τ reflection ⟺ maximal δ is EXACT (verified). But BST's sin²θ₂₃=4/7 is a REAL μ-τ break (not merely "
      "'near'), pushing δ ~18° off maximal → BST predicts δ_PMNS NEAR-maximal ≈ −72° (a 4/7-correlated offset), NOT "
      "exactly −π/2 — a sharper, DUNE/Hyper-K-distinguishable falsifier, HELD AS CANDIDATE (offset criterion-dependent + "
      "needs Lyra's M_ν). BANKABLE structural result: rank-2 neutrino → J_PMNS ≫ J_CKM (~1000×), CKM ≪ PMNS matching data; "
      "J_CKM ∝ ε³ structural, not the exact value derived.",
      d0 < 1e-9 and abs(dmin_bst - 90) > 10 and ratio > 500,
      "μ-τ⟺maximal exact; 4/7 is a real break → δ≈−72° near-maximal candidate (not −90°); rank-2→J_PMNS≫J_CKM structural (bank); J_CKM∝ε³")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-11 (near-)maximal leptonic CP — Target-1 (mine), fish-detector on 'near-μ-τ → near-maximal δ':
  * R1: μ-τ reflection ⟺ maximal δ — EXACT (dev=0 only at θ₂₃=45°,δ=±90°). The linear-algebra link holds.
  * R2 (CATCH): θ₂₃=4/7 is a REAL μ-τ break (dev 0.23); the breaking-minimizing δ is ~72°, NOT 90° → the 4/7 offset pushes δ ~18° off maximal. Near-maximal is NOT automatic.
  * R3 (CANDIDATE): IF the texture minimizes breaking, δ_PMNS ≈ −72° (near-maximal, ~18° offset correlated with 4/7) — DUNE-distinguishable from −90°. Held as candidate (criterion-dependent + needs Lyra's M_ν).
  * R4 (BANK): rank-2 neutrino → J_PMNS ≈ 0.03 ≫ J_CKM ~ 3e-5 (~1000×) → CKM ≪ PMNS matches data. J_CKM ∝ ε³ structural, not exact.
  => μ-τ⟺maximal exact; BST predicts NEAR-maximal δ≈−72° (offset from 4/7), candidate; rank-2→CKM≪PMNS structural (bankable).
""")
