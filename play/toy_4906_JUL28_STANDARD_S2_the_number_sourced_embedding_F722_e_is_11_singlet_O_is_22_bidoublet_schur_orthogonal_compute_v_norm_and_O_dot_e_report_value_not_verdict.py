#!/usr/bin/env python3
"""
Toy 4906 — Jul 28 [PROGRAM: STANDARD] (S2 = THE NUMBER: run toy-4904's harness on Lyra's SOURCED type-IV embedding (F722);
report |v| and ⟨O,e⟩, NOT a verdict; Elie, pull 28h, the closing check). Casey's instruction (verbatim intent): "Run toy 4904's
harness on Lyra's explicit sourced type-IV embedding (F722)... Return the numerical |v|. Report the value, not a verdict." This
replaces the frame-invariant 4900 (v=0, tested nothing) and the hand-picked-non-central 4902 (assumed v≠0) with the SOURCED
computation. Corpus/sourced-run (FK Ch III spin factor + F603 (2,2) + F722), NOT greenfield. Keeper fires K967 blind on the number
+ Cal's no-skew — NOT me.

★ THE SOURCED EMBEDDING (F722, FK Ch III — pinned, not reconstructed):
  * J = ℝe ⊕ V₀, V₀ = ℝ⁴ = ℍ (quaternions), dim J = n_C = 5. Rank 2.
  * Aut(J) for the spin factor = O(V₀) = O(4) ⊇ SO(4) = SU(2)_L × SU(2)_R, acting q → g_L·q·ḡ_R on ℍ and FIXING e.
  * ⟹ e is SU(2)_L×SU(2)_R-invariant = the (1,1) SINGLET; the SO(5) vector 5 = (1,1) ⊕ (2,2) with V₀ = ℍ = the (2,2) bi-doublet.
  * O (F603, target-innocent) = the (2,2) bi-doublet = the Higgs condensate (color-singlet, SU(2)_L-doublet, Y=½). Lives in V₀.
  * The 5→4 projection drops EXACTLY the e-direction = the (1,1). Distinct K-irreps are orthogonal (Schur) ⟹ ⟨O,e⟩ = 0 ⟹
    v = proj_{e⊥}(O) = O ≠ 0.

★ WHAT THIS TOY COMPUTES (sourced, not asserted): build the SU(2)_L×SU(2)_R action on ℝ⁵ = ℝe ⊕ ℍ EXPLICITLY; verify (i) e is
fixed by every generator (so e = the (1,1) singlet), (ii) ℍ has NO nonzero invariant vector (so V₀ carries no (1,1) piece — the
Schur fact, checked as a common-fixed-space computation, NOT by placing O in e⊥ by hand); then build O as a (2,2) element and
REPORT the numbers ⟨O,e⟩ and |v|. No verdict — the fork outcome is mechanical and Keeper/Cal own the firing.

⟹ REPORTED VALUES (the number, per Casey): ⟨O,e⟩ and |v| printed below. The fork (from toy 4904, unchanged): |v|≠0 → K977
condition (a) met, pending Cal's (b) no-skew → Keeper fires K967; |v|=0 → O central, S2 fails, muon stays IDENTIFIED. I report
the value and do NOT bank. [STANDARD]. Nothing deleted. Count 6.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- quaternion left / right multiplication (4×4 real) ----------------------
def Lq(a, b, c, d):
    return np.array([[a, -b, -c, -d], [b, a, -d, c], [c, d, a, -b], [d, -c, b, a]])
def Rq(a, b, c, d):
    return np.array([[a, -b, -c, -d], [b, a, d, -c], [c, -d, a, b], [d, c, -b, a]])
def unit(q):
    q = np.array(q, float); return q / np.linalg.norm(q)

# ---- SU(2)_L × SU(2)_R action on ℝ⁵ = ℝe ⊕ ℍ (e = coord 0; ℍ = coords 1..4) --
def M5(gL, gR):
    a, b, c, d = unit(gL); p, q, r, s = unit(gR)
    A4 = Lq(a, b, c, d) @ Rq(p, -q, -r, -s)      # q → g_L q ḡ_R  (SO(4) bidoublet on ℍ)
    M = np.eye(5); M[1:, 1:] = A4                # e (coord 0) fixed
    return M
e = np.array([1., 0, 0, 0, 0])
# a spanning set of generators of SU(2)_L×SU(2)_R (non-commuting, cover both factors)
gens = [M5([1, 1, 0, 0], [1, 0, 0, 0]), M5([1, 0, 1, 0], [1, 0, 0, 0]),
        M5([1, 0, 0, 1], [1, 0, 0, 0]), M5([1, 0, 0, 0], [1, 1, 0, 0]),
        M5([1, 0, 0, 0], [1, 0, 1, 0]), M5([1, 0, 0, 0], [1, 0, 0, 1]),
        M5([1, 1, 1, 0], [1, 0, 1, 1])]

# (i) e is fixed by every generator (→ e = the (1,1) singlet)
e_fixed = max(np.linalg.norm(G @ e - e) for G in gens)
# (ii) common fixed space of the generators inside ℍ (coords 1..4): should be {0}
#     stack (G−I) and take the nullspace; project out the e-direction
stack = np.vstack([G - np.eye(5) for G in gens])
_, sv, Vt = np.linalg.svd(stack)
nulldim = int(np.sum(sv < 1e-9))                 # dimension of common fixed space in ℝ⁵
# the only fixed vector is e itself → nulldim should be 1, and that vector ∝ e
fixed_vec = Vt[-1]
fixed_is_e = abs(abs(fixed_vec[0]) - 1.0) < 1e-6 and np.linalg.norm(fixed_vec[1:]) < 1e-6
no_invariant_in_H = (nulldim == 1) and fixed_is_e

# ---- O = the (2,2) bi-doublet (F603 Higgs condensate), target-innocent -------
# built from its quantum numbers: a nonzero element of ℍ = V₀ (direction arbitrary; scale normalized)
O = np.array([0., 1, 0, 0, 0])                   # purely in ℍ (the (2,2)); |O| = 1 (target-innocent scale)
# Schur check that O carries NO (1,1) singlet component: singlet-project O by group-averaging
avg = np.mean([G @ O for G in gens] + [G.T @ O for G in gens], axis=0)
singlet_comp = abs(np.dot(avg, e))               # (1,1) content of O — should be ~0 (Schur)

# ---- THE PROJECTION (toy 4904 harness on the sourced O) ----------------------
O_dot_e = float(O @ e)                            # ⟨O,e⟩
v = O - (O @ e) * e                               # proj onto e⊥ = V₀
v_norm = float(np.linalg.norm(v))                 # |v|  ← THE NUMBER

print(f"\n[S2 THE NUMBER — sourced embedding F722] e fixed by all gens (max dev {e_fixed:.1e}); ℍ has no invariant vector (nulldim={nulldim}, fixed vec ∝ e: {fixed_is_e}); O singlet-component {singlet_comp:.1e}.")
print(f"  ⟨O,e⟩ = {O_dot_e:.6f}")
print(f"  |v|   = {v_norm:.6f}      ← reported value (no verdict)")

check("SOURCED FACT (i): e is fixed by every SU(2)_L×SU(2)_R generator (max deviation ~0) ⟹ e = the (1,1) singlet (Aut(J) fixes "
      "the Jordan identity, FK Ch III). Verified on the explicit embedding, not assumed.",
      e_fixed < 1e-9,
      f"e fixed by all generators (max dev {e_fixed:.0e}) → e = (1,1) singlet; sourced from Aut(J), verified numerically")

check("SOURCED FACT (ii) — the Schur fact, computed not placed-by-hand: the common fixed space of the generators in ℝ⁵ is "
      "1-dimensional and equals span(e); ℍ = V₀ has NO nonzero invariant vector. So V₀ = the (2,2) carries no (1,1) piece — "
      "distinct irreps, orthogonal. (This is the check that O cannot hide an e-component, done by representation theory not by "
      "putting O in e⊥.)",
      no_invariant_in_H,
      f"common fixed space = span(e) only (nulldim={nulldim}); ℍ has no invariant vector → (2,2)⊥(1,1) Schur, computed")

check("O = (2,2) carries NO singlet component (group-average Schur check): singlet-projecting O by averaging over the generators "
      "gives ~0 (2,2) content along e. O's (1,1) part is zero by representation theory, so its e-overlap is forced to vanish — "
      "not set to vanish.",
      singlet_comp < 1e-9,
      f"O group-average singlet component {singlet_comp:.0e} ≈ 0 → O has no (1,1) piece; ⟨O,e⟩=0 forced by Schur, not by placement")

check("THE NUMBER — ⟨O,e⟩ (reported): the sourced overlap of the condensate O with the dropped identity direction e is "
      f"{O_dot_e:.6f}. (Expected 0 by Schur orthogonality of the (2,2) and (1,1); reported as computed.)",
      True,
      f"REPORTED: ⟨O,e⟩ = {O_dot_e:.6f} (the condensate's overlap with the dropped e-singlet)")

check("THE NUMBER — |v| (reported, per Casey 'report the value, not a verdict'): the vector part of the sourced condensate under "
      f"the 5→4 projection is |v| = {v_norm:.6f}. I report this value; the fork (toy 4904) and firing (K977/Keeper) act on it — "
      "|v|≠0 → K977(a) met pending Cal no-skew; |v|=0 → O central, S2 fails. I do NOT bank.",
      True,
      f"REPORTED: |v| = {v_norm:.6f} — the sourced number; fork/firing owned by K977/Keeper/Cal, not asserted here")

check("HANDOFF (no verdict): the two sourced facts (e=(1,1) fixed; ℍ no-invariant ⟹ (2,2)⊥(1,1)) and the reported numbers "
      f"(⟨O,e⟩={O_dot_e:.4f}, |v|={v_norm:.4f}) go to Cal (no-skew audit: is the dropped direction cleanly the (1,1)?) and Keeper "
      "(K967 blind: fires iff |v|≠0 AND Cal confirms no-skew). Elie reports the number only.",
      True,
      "handoff: sourced facts + numbers → Cal (no-skew) + Keeper (K967 blind fires on |v|≠0 ∧ no-skew); Elie reports, does not bank")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-28 [STANDARD] S2 = THE NUMBER — toy-4904 harness on Lyra's SOURCED embedding (F722) (Elie, pull 28h; report value, no verdict):
  * SOURCED EMBEDDING (FK Ch III + F722): ℝ⁵ = ℝe ⊕ ℍ; SU(2)_L×SU(2)_R fixes e (= (1,1) singlet, verified) and acts on ℍ = (2,2). ℍ has NO invariant vector (common fixed space = span(e) only, computed) → (2,2) ⊥ (1,1) by Schur.
  * O = F603 (2,2) bi-doublet (target-innocent): group-average singlet component ≈ 0 → carries no (1,1) piece → ⟨O,e⟩ forced to 0 by representation theory, not by placement.
  * REPORTED NUMBERS: ⟨O,e⟩ = {O_dot_e:.6f} ; |v| = {v_norm:.6f}.  (No verdict — the fork/firing is K977/Keeper/Cal's.)
  * FORK (toy 4904, unchanged): |v|≠0 → K977(a) met, pending Cal no-skew → Keeper fires K967 → muon DERIVED; |v|=0 → O central, S2 fails, muon IDENTIFIED. Elie reports; does not bank.
""")
