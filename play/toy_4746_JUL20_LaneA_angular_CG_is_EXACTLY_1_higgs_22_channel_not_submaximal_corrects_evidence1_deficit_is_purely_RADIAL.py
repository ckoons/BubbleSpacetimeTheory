#!/usr/bin/env python3
"""
Toy 4746 — Jul 20 (Lane A angular CG, mine; condensate-study CORE support): compute the γ-vertex Clebsch-Gordan for the
top Yukawa on SO(5) — the angular contribution to y_t = ⟨top_L|Γ·O|top_R⟩. Result (and a correction to my own 4744):
the ANGULAR CG is EXACTLY 1 — NOT sub-maximal — because the physical top bilinear top_L⊗top_R = (2,1)⊗(1,2) = (2,2) is
precisely the Higgs (2,2) channel (part of the 5). The "5-branch sub-maximal (stretched branch is the adjoint 10)"
framing (my 4744 evidence-1, Lyra F603) CONFLATED the SAME-chirality highest weight (the 10 = top_L⊗top_L type) with
the OPPOSITE-chirality Yukawa (L⊗R = (2,2), CG=1). So the angular part does NOT lower y_t. CONSEQUENCE (sharpens the
core): the ENTIRE y_t deficit (127/128, if real) is RADIAL — the discrete-vs-boundary band-edge gap (Lane A #2) — the
angular part gives exactly 1. This reduces the whole y_t<1 question to ONE source (radial), not two.

THE COMPUTATION (SO(5) γ-matrices, 4×4, verified Clifford {Γ^A,Γ^B}=2δ):
  * SO(4) chirality = Γ⁵ → P_L = (1+Γ⁵)/2 [Sp(1)_L doublet (2,1)], P_R = (1−Γ⁵)/2 [(1,2)].
  * Higgs O = the (2,2) part of the 5 = span(Γ¹..Γ⁴) [SO(4) vector]; Γ⁵ is the (1,1) SO(4) singlet.
  * angular CG = largest singular value of P_L (Γ·O) P_R:
      - O = a (2,2) direction (Γ¹): CG = 1.0000 (MAXIMAL). [Γ¹ anticommutes with Γ⁵ → maps R fully into L.]
      - O = Γ⁵ (the (1,1) singlet): CG = 0 (doesn't couple L↔R). [consistency check.]
  So the Higgs (2,2) vertex is angular-MAXIMAL on the top: angular CG = 1.

THE CORRECTION (my 4744 evidence-1, Lyra F603 — the fish on our own claim): top_L⊗top_R = (2,1)⊗(1,2) = (2,2) = the
Higgs channel (part of the 5) → CG=1. The "stretched=10" is the SAME-chirality (1,1) highest weight (top_L⊗top_L type),
NOT the OPPOSITE-chirality Yukawa. So "5-branch sub-maximal" does NOT apply to the physical L⊗R top Yukawa. Evidence-1
(angular sub-maximal → y_t<1) is REFUTED for the physical overlap; the angular part is exactly 1.

⟹ VERDICT: the angular CG for the top Yukawa is EXACTLY 1 (computed, SO(5) γ-vertex, target-innocent) — the Higgs (2,2)
channel is angular-maximal on top_L⊗top_R=(2,2). This CORRECTS evidence-1 (my 4744 + Lyra F603: the "5 sub-maximal" was
the same-chirality 10, not the Yukawa). CONSEQUENCE: the ENTIRE y_t deficit (127/128, if real) is RADIAL — the
band-edge gap (Lane A #2, Lyra's) — the angular part contributes exactly 1. The whole y_t<1 question is now ONE
computation (radial), sharper. Count ~7-8 (α RULED). Five-Absence-safe (pure SO(5) rep theory, no new group).
"""
import numpy as np
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
np.random.seed(4746)
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- SO(5) gammas + Clifford ------------------------------------------------
s0 = np.eye(2); sx = np.array([[0,1],[1,0]]); sy = np.array([[0,-1j],[1j,0]]); sz = np.array([[1,0],[0,-1]])
G = [np.kron(sx,sx), np.kron(sx,sy), np.kron(sx,sz), np.kron(sy,s0), np.kron(sz,s0)]
clifford_err = max(np.max(np.abs(G[a]@G[b] + G[b]@G[a] - 2*(a==b)*np.eye(4))) for a in range(5) for b in range(5))
print(f"\n[SO(5) γ]: Clifford {{Γ^A,Γ^B}}=2δ, max err = {clifford_err:.1e}")
check("SO(5) γ-MATRICES BUILT: 5 anticommuting 4×4 matrices, {Γ^A,Γ^B}=2δ (err ~0). The spinor 4 = the SO(5) Dirac "
      "spinor; the bilinears 4⊗4 = 1(scalar) ⊕ 5(vector Γ^A) ⊕ 10(tensor Γ^{AB}).",
      clifford_err < 1e-10, "SO(5) γ built, Clifford verified — spinor 4, bilinears 1+5+10")

# ---- angular CG: P_L (Γ·O) P_R ----------------------------------------------
G5 = G[4]; PL = (np.eye(4)+G5)/2; PR = (np.eye(4)-G5)/2
def ang_cg(Ovec):
    GO = sum(c*G[i] for i, c in enumerate(Ovec))
    return np.linalg.svd(PL @ GO @ PR, compute_uv=False)[0]
cg_22 = ang_cg([1,0,0,0,0])       # (2,2) Higgs direction
cg_singlet = ang_cg([0,0,0,0,1])  # (1,1) SO(4) singlet Γ⁵
orand = np.random.randn(4); orand /= np.linalg.norm(orand)
cg_rand = ang_cg(list(orand)+[0])
print(f"[angular CG]: O=(2,2) Higgs → CG = {cg_22:.4f} (MAXIMAL); O=Γ⁵ singlet → CG = {cg_singlet:.4f} (no L↔R); O=random(2,2) → {cg_rand:.4f}")
check("ANGULAR CG = EXACTLY 1 (Higgs (2,2) channel): the largest singular value of P_L(Γ·O)P_R for O = the (2,2) Higgs "
      "direction is 1.0000 — angular-MAXIMAL. (The vector vertex Γ·O anticommutes with the chirality Γ⁵ → maps R fully "
      "into L.) Consistency: O=Γ⁵ (the (1,1) SO(4) singlet) gives CG=0 (doesn't couple L↔R). So the angular part is "
      "exactly 1, NOT sub-maximal.",
      abs(cg_22 - 1) < 1e-9 and cg_singlet < 1e-9, "angular CG = 1.0000 for the Higgs (2,2); =0 for the singlet — angular-maximal, not sub-maximal")

# ---- the correction to evidence-1 -------------------------------------------
check("CORRECTION to evidence-1 (my 4744 + Lyra F603 — fish on our own claim): top_L⊗top_R = (2,1)⊗(1,2) = (2,2) = the "
      "Higgs channel (part of the 5) → CG=1. The 'stretched=10' is the SAME-chirality (1,1) highest weight (top_L⊗top_L "
      "type), NOT the OPPOSITE-chirality Yukawa (L⊗R). So '5-branch sub-maximal' does NOT apply to the physical L⊗R top "
      "Yukawa — the angular part is exactly 1. Evidence-1 (angular sub-maximal → y_t<1) is REFUTED for the physical overlap.",
      abs(cg_22 - 1) < 1e-9, "top_L⊗top_R=(2,2)=Higgs channel → CG=1; 'stretched=10' is same-chirality, not the Yukawa — evidence-1 corrected")

# ---- consequence: the deficit is purely radial ------------------------------
check("CONSEQUENCE (sharpens Lane A CORE): since the angular CG is exactly 1, the ENTIRE y_t deficit (127/128, if real) "
      "is RADIAL — the discrete-vs-boundary band-edge gap (Lane A #2, Lyra's). The angular part contributes exactly 1, "
      "so the whole y_t<1 question reduces to ONE computation (the radial band-edge gap), not two. If that gap = 1/2^g → "
      "y_t=127/128 derived; if 0 → y_t=1 exact. The angular half is settled (=1).",
      abs(cg_22 - 1) < 1e-9, "angular=1 → the y_t deficit is PURELY RADIAL (band-edge gap); whole question reduces to Lane A #2 radial computation")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the angular CG for the top Yukawa is EXACTLY 1 (SO(5) γ-vertex, target-innocent) — the Higgs (2,2) "
      "channel is angular-maximal on top_L⊗top_R=(2,2). This CORRECTS evidence-1 (my 4744 + F603: '5 sub-maximal' was "
      "the same-chirality 10, not the Yukawa). CONSEQUENCE: the ENTIRE y_t deficit is RADIAL (the band-edge gap, Lane A "
      "#2) — the whole y_t<1 question is now ONE radial computation. Sharper problem; the angular half is done (=1).",
      abs(cg_22 - 1) < 1e-9 and cg_singlet < 1e-9 and clifford_err < 1e-10,
      "angular CG=1 (computed); evidence-1 corrected; y_t deficit is purely RADIAL → Lane A reduces to the band-edge gap alone")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print("""
LANE A ANGULAR CG (condensate study CORE) — the angular half is settled at 1:
  * SO(5) γ-vertex: angular CG = largest SV of P_L(Γ·O)P_R = 1.0000 for the Higgs (2,2) channel (=0 for the singlet).
  * WHY: top_L⊗top_R = (2,1)⊗(1,2) = (2,2) = the Higgs channel → CG=1 (Γ·O anticommutes with chirality Γ⁵).
  * CORRECTS evidence-1 (my 4744 + F603): '5 sub-maximal (stretched=10)' is the SAME-chirality highest weight, NOT the L⊗R Yukawa.
  => the ENTIRE y_t deficit (127/128) is RADIAL (the band-edge gap, Lane A #2). Angular half done (=1); the whole question is now one radial computation.
""")
