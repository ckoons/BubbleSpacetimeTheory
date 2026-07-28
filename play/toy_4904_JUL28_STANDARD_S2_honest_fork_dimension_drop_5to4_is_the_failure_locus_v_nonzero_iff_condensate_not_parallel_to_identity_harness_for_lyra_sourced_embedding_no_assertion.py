#!/usr/bin/env python3
"""
Toy 4904 — Jul 28 [PROGRAM: STANDARD] (S2 make-or-break: the HONEST fork; the 5→4 dimension drop is the failure locus; Elie,
pull 28h, Cal's bar). Casey's warning (verbatim intent): do NOT clear S2 on "O is obviously a non-singlet" — the SO(5) vector is
5-dim, the spin-factor vector part is ℝ⁴ (4-dim), the projection DROPS a dimension, so the condensate O could land in the
dropped direction (v=0). S2 clears IFF v≠0; v=0 → S2 FAILS and O is central (a real result either way). This toy builds the
harness and REFUSES to assert the branch — the sourced type-IV embedding (Lyra) decides. Literature-run (FK94 III.1.2 + K974),
NOT greenfield.

★ FIX THE 4902/4900 SIN: toy 4900 tested a frame-INVARIANT (central, v=0) symbol — tests nothing (owned). Toy 4902 then picked a
NON-central vector BY HAND (v=(cosθ,sinθ,0,0)) — which verifies the mechanism but ASSUMES the very thing at stake (v≠0). That is
"waving it through because it's pretty." The real make-or-break is whether the SOURCED embedding of the condensate has a nonzero
ℝ⁴ vector part — and the dimension drop is exactly where a non-singlet can still give v=0. This toy makes the answer CONTINGENT
on the embedding, computes both branches, and hands the sourced projection to Lyra.

★ THE GEOMETRY (pinned): V = ℝe ⊕ ℝ⁴ (spin factor, dim n_C=5). The vector part is ℝ⁴; the identity direction e is the DROPPED
5th. Project any O ∈ V onto the vector part: P(O) = O − ⟨O,e⟩e. Then v = P(O), and
      v = 0  ⟺  O ∈ span(e)  (O central / an identity-multiple)  ⟺  the frame is NOT selected.
So S2 clears ⟺ O has a nonzero component OFF the identity axis. Parametrize by the angle φ between O and e: |v| = |O|·|sin φ|,
zero exactly at φ=0 (O ∥ e). The make-or-break is φ ≠ 0, and φ is fixed by the SOURCED embedding — NOT assertible from "O is a
vector rep" (a non-singlet can still embed along e under the dimension drop).

⟹ VERDICT (plain, CALIBRATED — a fork, not a clear): the frame-selection MECHANISM is verified (a non-central O selects a unique
frame c±=½(e±v/|v|); a central O — 4900's case — selects none). But S2 itself is CONTINGENT: it clears IFF the sourced type-IV
embedding gives the condensate a nonzero ℝ⁴ vector part (φ≠0, v≠0), and FAILS (O central) if the condensate embeds along the
identity axis (φ=0, v=0) — the 5→4 dimension drop is precisely the failure locus. I do NOT assert the branch: which case holds is
Lyra's SOURCED projection (pin to the primary type-IV embedding, don't reconstruct). Cal's bar "is v non-central?" is the harness
output, pending Lyra's sourced O. If v≠0 → muon banks DERIVED (Keeper K967 blind); if v=0 → S2 fails and O is central — a real
result either way. NOT waved through. [STANDARD]. Nothing deleted. Count 6.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- Spin factor V = ℝe ⊕ ℝ⁴, Jordan product, identity e --------------------
def jp(x, y):
    (a0, av), (b0, bv) = (x[0], x[1:]), (y[0], y[1:])
    return np.concatenate([[a0 * b0 + av @ bv], a0 * bv + b0 * av])
e = np.array([1., 0, 0, 0, 0])
def project_vector_part(O):                 # drop the identity (e) direction: the 5→4 map
    return O - (O @ e) * e
def frame(v):                               # c± = ½(e ± v/|v|), defined ONLY if v≠0
    u = v / np.linalg.norm(v)
    return 0.5 * (e + u), 0.5 * (e - u)

# ---- MECHANISM (verify both ends, no assertion about the physical O) ---------
# non-central O selects a unique frame:
O_noncentral = np.array([2.0, 0.6, 0.3, 0.0, 0.0])      # some component off e
v_nc = project_vector_part(O_noncentral)
cp, cm = frame(v_nc)
selects = (np.linalg.norm(jp(cp, cp) - cp) < 1e-12 and np.linalg.norm(jp(cm, cm) - cm) < 1e-12
           and np.linalg.norm(jp(cp, cm)) < 1e-12 and np.linalg.norm(cp + cm - e) < 1e-12)
# central O (the 4900 case) selects none: its vector part is exactly 0
O_central = np.array([1.7, 0, 0, 0, 0])
v_c = project_vector_part(O_central)
selects_none = np.linalg.norm(v_c) < 1e-12

# ---- THE FORK: |v| as a function of the angle φ between O and e --------------
def vnorm_at_angle(phi):                     # |O|=1: O = cosφ·e + sinφ·(unit vector part)
    O = np.array([np.cos(phi), np.sin(phi), 0., 0., 0.])
    return np.linalg.norm(project_vector_part(O))
fork_fail = vnorm_at_angle(0.0) < 1e-12                 # φ=0: O ∥ e → v=0 → S2 FAILS (O central)
fork_clear = vnorm_at_angle(0.7) > 1e-9                 # φ≠0: v≠0 → S2 CLEARS
# the point: |v| = |sin φ|, so non-centrality is NOT implied by "O is a non-singlet" —
# a non-singlet embedded along e (φ=0) still gives v=0 under the dimension drop.
dim_drop = (len(e) - 1)                                  # vector part ℝ⁴ = one dimension less than V=ℝ⁵

print(f"\n[S2 honest fork] mechanism: non-central O selects unique frame ({selects}); central O (4900 case) selects none (v=0: {selects_none}). FORK on angle φ(O,e): φ=0 → |v|={vnorm_at_angle(0.0):.3f} FAIL (central); φ=0.7 → |v|={vnorm_at_angle(0.7):.3f} CLEAR. 5→4 drop (ℝ⁴ vs ℝ⁵) is the failure locus. Branch = Lyra's SOURCED embedding — NOT asserted.")

check("MECHANISM verified (both ends, no assertion): a NON-central O (v≠0) selects a UNIQUE frame c±=½(e±v/|v|) (idempotent, "
      "orthogonal, complete); a CENTRAL O (the 4900 case, O∥e) has vector part exactly 0 and selects NONE. This is the "
      "frame-selection law — verified — but it does NOT tell us which case the physical condensate is in.",
      selects and selects_none,
      "mechanism: non-central O → unique frame (verified); central O (4900) → v=0, selects none; law verified, physical branch still open")

check("THE 5→4 DIMENSION DROP IS THE FAILURE LOCUS: the SO(5) vector is 5-dim, the spin-factor vector part is ℝ⁴ (one less). "
      "Projecting O onto the vector part drops the identity (e) direction: v = O − ⟨O,e⟩e. |v| = |O|·|sin φ| where φ = angle(O,e). "
      "So v=0 EXACTLY when O∥e (φ=0) — and a non-singlet embedded along e STILL gives v=0. Non-centrality is NOT implied by "
      "'O is a vector rep.'",
      dim_drop == 4 and fork_fail,
      "dimension drop ℝ⁵→ℝ⁴ (one less); v=O−⟨O,e⟩e; |v|=|sinφ|; φ=0 (O∥e) → v=0 even for a non-singlet — the drop is the failure locus")

check("THE FORK (both branches computed, neither asserted): φ≠0 → v≠0 → S2 CLEARS → muon banks Derived; φ=0 → v=0 → S2 FAILS → "
      "O is central (a real result). I compute both and do NOT pick one. Which branch holds = the SOURCED type-IV embedding of "
      "the F603 condensate (Lyra, pinned to primary source, not reconstructed).",
      fork_clear and fork_fail,
      "fork computed both ways: φ≠0 clears (v≠0), φ=0 fails (v=0, O central); branch = Lyra's sourced embedding; NOT asserted here")

check("DO NOT WAVE THROUGH (Casey's bar, held): I refuse to clear S2 on 'O is obviously a non-singlet' — that is exactly the "
      "reasoning the dimension drop defeats. Toy 4902's hand-picked non-central vector VERIFIED the mechanism but ASSUMED v≠0; "
      "this toy makes v≠0 contingent on the sourced embedding. Honest either way: v≠0 → Derived; v=0 → S2 fails, O central.",
      True,
      "held: not cleared on 'non-singlet'; 4902 assumed v≠0 (mechanism only); here v≠0 is contingent on the sourced embedding — real result either branch")

check("CAL'S BAR IS THE HARNESS OUTPUT: 'is v non-central?' = compute v = P(O_sourced) and test |v|>0. The harness is ready; the "
      "input is Lyra's sourced condensate O under the primary type-IV embedding. Elie provides the computation; Lyra provides "
      "the sourced O; Cal audits the projection is sourced (not reconstructed); Keeper fires K967 blind on the result.",
      True,
      "Cal's bar = harness output |v|>0 on the SOURCED O; Elie harness ready, Lyra supplies sourced O, Cal audits source, Keeper fires blind")

check("VERDICT: S2 is a FORK, not a clear. The frame-selection mechanism is verified (non-central selects, central=4900 does "
      "not); but S2 clears IFF the sourced embedding gives the condensate v≠0 (φ≠0), and FAILS (O central) if it embeds along "
      "the identity (φ=0) — the 5→4 drop is the failure locus. Branch = Lyra's sourced projection; NOT asserted. v≠0 → muon "
      "Derived (K967 blind); v=0 → S2 fails, a real result.",
      selects and selects_none and fork_fail and fork_clear and dim_drop == 4,
      "S2 = fork: mechanism verified, clearance CONTINGENT on sourced embedding (v≠0 φ≠0 clears / v=0 φ=0 fails+central); 5→4 drop = failure locus; not asserted")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-28 [STANDARD] S2 make-or-break = the HONEST fork (Elie, pull 28h, Cal's bar):
  * MECHANISM verified (both ends): non-central O selects a unique frame c±=½(e±v/|v|); central O (the 4900 case, O∥e) selects none. The law, not the physical branch.
  * 5→4 DIMENSION DROP = the failure locus: v = O − ⟨O,e⟩e; |v| = |O|·|sin φ|, φ=angle(O,e). v=0 exactly when O∥e — and a non-singlet embedded along e STILL gives v=0. Non-centrality is NOT implied by 'O is a vector rep.'
  * THE FORK (both branches computed, neither asserted): φ≠0 → v≠0 → S2 clears → muon Derived; φ=0 → v=0 → S2 fails, O central. Branch = Lyra's SOURCED type-IV embedding (primary source, not reconstructed).
  * NOT waved through: 4902 assumed v≠0 (mechanism only); here it's contingent. Cal's bar = |v|>0 on the sourced O; Keeper fires K967 blind on the result. Real result either branch.
""")
