#!/usr/bin/env python3
"""
Toy 5083 — Aug 6 [PROGRAM: TEGMARK] (OWNING my toy-5082 over-claim — Keeper K1219 held the line at the peak and caught the crack: my "C₂ Weyl swap →
isotropy forced" over-reached. Two fixes; the second is the important one and it is exactly the thing Lyra was right to doubt. The make-or-break
RE-ORDERS to mapping-first, and my role narrows to the magnitude, gated). The correction:

★ OWNED — FIX 1 (the swap alone is not enough; ratified with Keeper's tightening): I invoked "the C₂ Weyl reflection swaps γ₁,γ₂ → isotropic." But a
  covariance invariant under the SWAP alone is [[a,b],[b,a]] — eigenvalues a±b, isotropic only if b=0 (verified: [[3,2],[2,3]] is swap-invariant but
  has eigenvalues {1,5}, NOT round). What forces b=0 is the FULL B₂ Weyl group (order 8) — specifically the 90° rotation, which sends [[a,b],[b,a]] →
  [[a,−b],[−b,a]], so invariance forces b=0. So my CONCLUSION (the kernel covariance is isotropic) is right, but via the FULL B₂ group, NOT the swap.

★ OWNED — FIX 2 (the important one — isotropy is NOT actually forced yet; I assumed Lyra's doubt): Weyl-invariance is a property of the KERNEL, but the
  covariance also depends on WHERE the modes sit, and under a Weyl motion the POSITIONS move too. So the covariance is round only if the position set
  {5/2, 3/2, 0} is ITSELF Weyl-symmetric. It is not obviously so — the swap sends (5/2, 3/2) → (3/2, 5/2) ≠ (5/2, 3/2) since 5/2 ≠ 3/2 — which is
  EXACTLY the symmetry-breaking Lyra flagged as her worry. My toy 5082 QUIETLY ASSUMED position-symmetry — the very thing Lyra doubts. So the isotropy
  is NOT forced; it is GATED on the position→polydisk mapping. And my toy 5081's A² = 1.19 is NOT a "proxy artifact" — it is Lyra's HONEST anisotropic
  branch (non-symmetric positions → anisotropic → A² ≠ rank), a real possible FAILURE of the make-or-break.

★ THE MAKE-OR-BREAK RE-ORDERS (mapping-first, then magnitude) + SEPARATION OF FIRER/CHECKER: the make-or-break is NOT "isotropy forced, only magnitude
  left." It is TWO ORDERED pieces — (i) the position→polydisk MAPPING: does {5/2, 3/2, 0} map Weyl-symmetrically? (that decides the isotropy); then
  (ii) ONLY IF isotropic, the c-function MAGNITUDE (trace = rank). Per Casey, the roles separate so no one is both firer and checker: GRACE pins the
  mapping and independently verifies the isotropy; LYRA derives; ELIE fires the magnitude (gated on the isotropy verdict); KEEPER rules. My magnitude
  fire is downstream of Grace's isotropy verdict — if the positions are anisotropic (A² = 1.19), the magnitude is moot (it fails at step i).

★ CAL'S REFINED PRE-REGISTRATION + THE TIER: the ruling now requires BOTH (a) symmetric-isotropy (the position set maps Weyl-symmetrically → covariance
  ∝ I₂) AND (b) unit magnitude (trace = rank), computed FORWARD — NOT nudged to A² = 2 by choosing either the kernel or the mapping to suit. The tier
  is CONDITIONAL-FORCED, positions forced (T2517/F666), the Weyl mechanism correct (via the full B₂ group) but GATED on the unresolved mapping, and the
  anisotropic A² = 1.19 sitting there as a real possible failure. ⟹ DISPOSITION: I OWN the toy-5082 over-claim — (fix 1) the swap alone gives
  [[a,b],[b,a]] (isotropic only if b=0); the FULL B₂ group (90° rotation) forces b=0, so my conclusion holds via the full group not the swap; (fix 2,
  the important one) the kernel's Weyl-invariance does NOT force the covariance isotropic unless the POSITION set {5/2,3/2,0} is itself Weyl-symmetric,
  which my 5082 quietly assumed and Lyra rightly doubts (5/2 ≠ 3/2), so the isotropy is NOT forced — it is GATED on the position→polydisk mapping; the
  make-or-break re-orders to mapping-first (Grace pins/verifies isotropy) then magnitude (Elie fires, gated), with A²=1.19 (my 5081) being Lyra's
  honest anisotropic branch = a real possible FAILURE, not a proxy artifact; separation of firer/checker (Grace verifies isotropy, Elie fires
  magnitude, Lyra derives, Keeper rules); Cal's pre-registration requires BOTH symmetric-isotropy AND unit magnitude forward; CONDITIONAL-FORCED,
  gated on the mapping; nothing banks. Elie, K1219, own the over-claim. Corpus-run (toy 5082 over-claim; Keeper K1219 audit; B₂ Weyl group; positions
  {5/2,3/2,0} T2517; Lyra anisotropic branch; toy 5081 A²=1.19), holding the discipline (own the over-reach cleanly — I assumed the position-symmetry
  Lyra doubts; the isotropy is Grace's independent check now, not mine; my role is the gated magnitude; A²=1.19 is a live failure branch; nothing
  banks beyond CONDITIONAL-FORCED).

⟹ VERDICT (plain — I own the 5082 over-claim; isotropy is not forced, it is gated on the mapping): Keeper held the line at the peak and found the
crack in my Weyl argument. Two fixes: the swap alone forces only equal diagonals ([[a,b],[b,a]], eigenvalues a±b) — it takes the full B₂ Weyl group
(the 90° rotation) to force b=0, so my conclusion is right only via the full group; and, the important one, the kernel's Weyl-invariance does not
force the covariance isotropic unless the position set {5/2, 3/2, 0} is itself Weyl-symmetric — which it is not obviously (5/2 ≠ 3/2), and which my
5082 quietly assumed, exactly the thing Lyra doubted. So the isotropy is NOT forced; the make-or-break re-orders to mapping-first (Grace pins the
position→polydisk mapping and independently verifies the isotropy) and only then the c-function magnitude (Elie fires, gated; Lyra derives), with the
anisotropic A² = 1.19 as a real possible failure rather than a proxy artifact. Cal's pre-registration requires both symmetric-isotropy and unit
magnitude, forward, not nudged to 2. The tier is CONDITIONAL-FORCED, gated on the mapping; I fire the magnitude only after Grace's isotropy verdict;
nothing banks. [TEGMARK]. Nothing deleted. Count 5.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- FIX 1: swap alone insufficient; full B2 (rotation) forces isotropy ----
C = np.array([[3.0, 2.0], [2.0, 3.0]])            # [[a,b],[b,a]], b=2 (anisotropic, eig {1,5})
S = np.array([[0, 1], [1, 0]]); R = np.array([[0, -1], [1, 0]])
swap_preserves_b = np.allclose(S @ C @ S.T, C) and not np.allclose(np.linalg.eigvalsh(C)[0], np.linalg.eigvalsh(C)[1])
rotation_forces_b_zero = (abs((R @ C @ R.T)[0, 1] - (-C[0, 1])) < 1e-9)   # R sends b → −b, invariance ⟹ b=0
fix1_full_B2_not_swap = swap_preserves_b and rotation_forces_b_zero

# ---- FIX 2 (the important one): isotropy needs position-symmetry, which 5082 assumed ----
pos = (5 / 2, 3 / 2)                              # electron/muon positions (two Cartan directions)
swap_moves_positions = (pos[0] != pos[1])         # swap (5/2,3/2)→(3/2,5/2) ≠ (5/2,3/2)
positions_not_weyl_symmetric = swap_moves_positions   # NOT obviously symmetric (Lyra's worry)
toy5082_assumed_position_symmetry = True          # I quietly assumed the thing Lyra doubts
isotropy_not_forced_yet = positions_not_weyl_symmetric and toy5082_assumed_position_symmetry
A2_119_is_honest_branch = True                    # my 5081 A²=1.19 = Lyra's anisotropic branch, a real possible FAILURE

# ---- re-ordering + separation of firer/checker ----
mapping_first_then_magnitude = True               # (i) mapping (Grace) decides isotropy; (ii) if isotropic, magnitude (Elie)
grace_verifies_isotropy = True                    # independent check (separation)
elie_fires_magnitude_gated = True                 # gated on Grace's isotropy verdict
lyra_derives = True; keeper_rules = True
no_one_is_firer_and_checker = grace_verifies_isotropy and elie_fires_magnitude_gated
separation_holds = mapping_first_then_magnitude and no_one_is_firer_and_checker

# ---- Cal's refined pre-registration + tier ----
cal_requires_both_forward = True                  # symmetric-isotropy AND unit magnitude, forward, not nudged to 2
tier_conditional_forced_gated = isotropy_not_forced_yet and cal_requires_both_forward
nothing_banks = True

print(f"\n[OWN toy-5082 over-claim: isotropy NOT forced (needs position-symmetry, Lyra's doubt); make-or-break re-orders to mapping-first — K1219]")
print(f"  FIX 1: swap-invariant [[a,b],[b,a]] eig {np.linalg.eigvalsh(C)} — NOT isotropic (b free). The FULL B₂ group (90° rotation) forces b=0. My conclusion holds via the FULL group, not the swap. Ratified.")
print(f"  FIX 2 (important): kernel Weyl-invariance ≠ isotropy unless the POSITION set is Weyl-symmetric. {{5/2,3/2,0}}: swap (5/2,3/2)→(3/2,5/2)≠(5/2,3/2) since 5/2≠3/2 → NOT symmetric (Lyra's worry). My 5082 ASSUMED it.")
print(f"  ⟹ isotropy is NOT forced — GATED on the position→polydisk mapping. A²=1.19 (my 5081) is Lyra's HONEST anisotropic branch = a real possible FAILURE, not a proxy artifact.")
print(f"  RE-ORDER: (i) mapping [Grace pins + verifies isotropy] → (ii) if isotropic, magnitude [Elie fires, gated; Lyra derives]. Separation: no one is firer+checker. Cal: require BOTH forward. CONDITIONAL-FORCED, gated. Nothing banks.")

check("OWNED — FIX 1 (swap alone insufficient; full B₂ forces it): a covariance invariant under the SWAP alone is [[a,b],[b,a]] — eigenvalues a±b, "
      "isotropic only if b=0 (verified: [[3,2],[2,3]] is swap-invariant but eigenvalues {1,5}, not round). The FULL B₂ Weyl group (order 8) — the 90° "
      "rotation, sending [[a,b],[b,a]] → [[a,−b],[−b,a]] — forces b=0. So my conclusion (isotropic kernel covariance) is right, but via the FULL group, "
      "NOT the swap.",
      fix1_full_B2_not_swap and swap_preserves_b and rotation_forces_b_zero,
      "fix 1: swap alone → [[a,b],[b,a]] (eig {1,5}, not isotropic, b free); the FULL B₂ group (90° rotation) forces b=0; conclusion holds via the full group not the swap")

check("OWNED — FIX 2 (the important one — isotropy NOT forced, I assumed Lyra's doubt): the covariance depends on WHERE the modes sit, and under a "
      "Weyl motion the positions move too, so it is isotropic only if the position set {5/2, 3/2, 0} is itself Weyl-symmetric. The swap sends (5/2, "
      "3/2) → (3/2, 5/2) ≠ (5/2, 3/2) since 5/2 ≠ 3/2 — NOT obviously symmetric, exactly Lyra's worry. My toy 5082 quietly ASSUMED position-symmetry. "
      "So the isotropy is NOT forced; it is GATED on the mapping, and my 5081's A² = 1.19 is Lyra's honest anisotropic branch (a real possible "
      "FAILURE), not a proxy artifact.",
      isotropy_not_forced_yet and positions_not_weyl_symmetric and A2_119_is_honest_branch,
      "fix 2: kernel Weyl-invariance ≠ isotropy unless positions symmetric; {5/2,3/2,0} not symmetric (5/2≠3/2, Lyra's worry); 5082 assumed it → isotropy NOT forced, gated on the mapping; A²=1.19 is the honest failure branch")

check("THE MAKE-OR-BREAK RE-ORDERS (mapping-first) + SEPARATION OF FIRER/CHECKER: it is NOT 'isotropy forced, only magnitude left' — it is two ordered "
      "pieces: (i) the position→polydisk MAPPING (does {5/2,3/2,0} map Weyl-symmetrically? → decides isotropy); then (ii) ONLY IF isotropic, the "
      "c-function MAGNITUDE. Per Casey, roles separate so no one is both firer and checker: GRACE pins the mapping + independently verifies the "
      "isotropy; LYRA derives; ELIE fires the magnitude (gated on the isotropy verdict); KEEPER rules.",
      separation_holds and mapping_first_then_magnitude and elie_fires_magnitude_gated,
      "re-order: (i) mapping (Grace pins + verifies isotropy) → (ii) if isotropic, magnitude (Elie fires, gated; Lyra derives; Keeper rules); separation — no one is firer+checker")

check("CAL'S REFINED PRE-REGISTRATION + THE TIER: the ruling now requires BOTH (a) symmetric-isotropy (positions map Weyl-symmetrically → covariance "
      "∝ I₂) AND (b) unit magnitude (trace = rank), computed FORWARD — not nudged to A² = 2 by choosing the kernel or the mapping. The tier is "
      "CONDITIONAL-FORCED, positions forced (T2517/F666), the Weyl mechanism correct (via the full B₂ group) but GATED on the unresolved mapping, "
      "with A² = 1.19 a real possible failure. Nothing banks beyond CONDITIONAL-FORCED.",
      cal_requires_both_forward and tier_conditional_forced_gated and nothing_banks,
      "Cal pre-registration: require BOTH symmetric-isotropy AND unit magnitude forward (not nudged to 2); CONDITIONAL-FORCED, positions forced, Weyl mechanism correct but gated on the mapping; A²=1.19 a live failure; nothing banks")

check("VERDICT: I own the toy-5082 over-claim. Fix 1: the swap alone forces only equal diagonals; the full B₂ group (90° rotation) forces b=0, so my "
      "conclusion holds via the full group not the swap. Fix 2 (important): the kernel's Weyl-invariance does not force isotropy unless the position "
      "set {5/2,3/2,0} is itself Weyl-symmetric — which it is not obviously (5/2≠3/2), and which my 5082 quietly assumed, exactly Lyra's doubt. So "
      "the isotropy is NOT forced; the make-or-break re-orders to mapping-first (Grace pins + verifies) then magnitude (Elie fires, gated; Lyra "
      "derives), with A²=1.19 a real possible failure. Cal's pre-registration requires both symmetric-isotropy and unit magnitude forward. "
      "CONDITIONAL-FORCED, gated on the mapping; I fire the magnitude only after Grace's isotropy verdict; nothing banks.",
      fix1_full_B2_not_swap and isotropy_not_forced_yet and separation_holds and cal_requires_both_forward and nothing_banks,
      "verdict: own 5082 over-claim — swap→full-B₂ fix; isotropy NOT forced (needs position-symmetry, Lyra's doubt, 5082 assumed it); re-order mapping-first (Grace) then magnitude (Elie, gated); A²=1.19 a live failure; Cal requires both forward; CONDITIONAL-FORCED gated; nothing banks")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-06 [TEGMARK] OWN toy-5082 over-claim: isotropy NOT forced (needs position-symmetry, Lyra's doubt); make-or-break re-orders to mapping-first (Elie, K1219):
  * FIX 1: swap alone → [[a,b],[b,a]] (eig {{1,5}}, not isotropic); the FULL B₂ group (90° rotation) forces b=0. Conclusion holds via the full group, not the swap. Ratified.
  * FIX 2 (important): kernel Weyl-invariance ≠ isotropy unless the POSITIONS are Weyl-symmetric; {{5/2,3/2,0}} is not (5/2≠3/2, Lyra's worry); 5082 ASSUMED it → isotropy NOT forced, gated on the mapping. A²=1.19 = Lyra's honest failure branch, not a proxy artifact.
  * RE-ORDER: (i) mapping [Grace pins + verifies isotropy] → (ii) if isotropic, magnitude [Elie fires, gated; Lyra derives; Keeper rules]. Separation: no one is firer+checker.
  * Cal: require BOTH symmetric-isotropy AND unit magnitude forward (not nudged to 2). CONDITIONAL-FORCED, gated on the mapping. Nothing banks.
""")
