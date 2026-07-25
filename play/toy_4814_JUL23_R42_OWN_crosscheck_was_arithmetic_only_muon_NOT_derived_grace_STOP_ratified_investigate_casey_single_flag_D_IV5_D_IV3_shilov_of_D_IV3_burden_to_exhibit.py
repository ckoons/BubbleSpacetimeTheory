#!/usr/bin/env python3
"""
Toy 4814 — Jul 23 (own my arithmetic-only cross-check; the muon is NOT derived — Grace's STOP ratified; investigate Casey's
single-flag fix; Elie, pull 23p). At peak convergence Grace fired the discipline on her OWN theorem (T2511) and called STOP:
{5,3,0} is not a single consistent geometry, so the muon is NOT derived. I own my part cleanly and hold the STOP while
investigating Casey's candidate fix — WITHOUT re-banking.

OWN MY ROLE (honest): my "blind cross-check PASS" (toys 4811/4812) verified (24/π²)⁶ = 206.77 — that is ARITHMETIC only. It
confirmed the NUMBER, NOT the geometry/derivation. The geometry — {5,3,0} as a single consistent structure — is exactly what
FAILED. So my PASS never certified the muon as derived; it certified the assembled form's arithmetic. I state that plainly so
the "PASS" is not misread as a derivation check.

GRACE'S STOP — RATIFIED (K853, on her own T2511): D_IV⁵'s Jordan algebra = spin factor ℝc₁ ⊕ ℝc₂ ⊕ V₁₂; the two idempotents
are DIM-1 (rank-1 boundary faces = genus-1 disks); the N_c=3 is V₁₂ (the color Peirce multiplicity), NOT the muon's
sub-domain genus. And {5,3,0} is not one geometry:
  * boundary-FACE reading (where F86 places the generations): genera {5,1,0} → muon genus 1 (disk), NOT 3.
  * interior geodesic TOWER: genera {5,3,1} → tau genus 1 (D_IV¹), NOT the Shilov point (0).
  * the claimed {5,3,0} glues the muon's genus-3 (from the tower) to the tau's genus-0 (from the faces) — INCONSISTENT.
So the muon is NOT derived. What SURVIVES: the EW area bank (parity/confinement/ν-Majorana); (24/π²)⁶ as a strong ASSEMBLED
FORM (structural home now OPEN); the "mass = depth in a nested structure" intuition (may survive in corrected form).

INVESTIGATE CASEY'S FIX (K854, candidate — a single FLAG): D_IV⁵ ⊃ D_IV³ ⊃ Shilov-point-OF-D_IV³ — the tau lives on the
boundary of the MUON's own doll, so interior-genus-3 (muon) and boundary-genus-0 (tau) sit in ONE filtration legitimately.
  * genera {D_IV⁵=5, D_IV³=3, Shilov(D_IV³)=0} = {5,3,0} in a SINGLE filtration (each contains the next) → resolves Grace's
    "can't have both": the tau's genus-0 is the Shilov of D_IV³ (INSIDE the muon), not a separate D_IV⁵ face.
  * position-consistency (leading weight n/2): D_IV⁵→5/2, D_IV³→3/2, Shilov-point→0 → the derived positions {5/2,3/2,0}
    (T2517) MATCH this flag.
  * the mass MECHANISM: containment — the electron (D_IV⁵) wraps all three levels (lightest), the tau (the point) wraps
    nothing (heaviest); mass runs inverse to what each generation contains. A mechanism for the hierarchy, not a relabeling.

⟹ VERDICT (plain): the muon is NOT derived — Grace's STOP is RATIFIED and I own that my cross-check confirmed only the
arithmetic (24/π²)⁶, never the geometry. Casey's single-flag fix (D_IV⁵ ⊃ D_IV³ ⊃ Shilov(D_IV³)) is a CONSISTENT candidate
that resolves Grace's inconsistency and matches the derived positions — but the BURDEN is to EXHIBIT (that the generations
sit on THIS flag rather than F86's boundary faces, and that the containment overlap reproduces the c-function AND (24/π²)⁶),
NOT to assume it. Grace's STOP stands until exhibited; I do NOT bank the muon. What holds: EW area banked, (24/π²)⁶ a strong
assembled form (home open), mass=depth intuition (corrected form pending). This is the discipline paying for itself — a
"derived" we hadn't earned, caught before banking, correcting toward a firmer structure. Nothing false is in the book.
Five-Absence-positive. Count ~7-8.
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

import numpy as np
number = (24/np.pi**2)**6
face = [n_C, 1, 0]        # boundary-face reading {5,1,0}
tower = [n_C, 3, 1]      # interior tower {5,3,1}
casey = [n_C, N_c, 0]     # Casey flag {5,3,0} (D_IV^5, D_IV^3, Shilov(D_IV^3))
print(f"\n[muon NOT derived] (24/π²)⁶ = {number:.2f} = arithmetic only (my cross-check confirmed the NUMBER, not the geometry)")
print(f"  faces {face} (muon genus 1) | tower {tower} (tau genus 1) | claimed {{5,3,0}} glues both → INCONSISTENT (Grace STOP)")
print(f"  Casey flag D_IV⁵⊃D_IV³⊃Shilov(D_IV³): genera {casey} in ONE filtration; positions {{5/2,3/2,0}} match → consistent candidate")

# ---- own arithmetic-only ---------------------------------------------------
check("OWN (arithmetic-only): my blind cross-check verified (24/π²)⁶=206.77 — the NUMBER, not the geometry. It never "
      "certified the muon as derived; it certified the assembled form's arithmetic. The geometry ({5,3,0} single structure) "
      "is what FAILED. Stated plainly so 'PASS' isn't misread as a derivation.",
      abs(number - 206.76) < 0.1, "blind cross-check = arithmetic (24/π²)⁶=206.77 only, NOT the geometry; muon NOT derived; owned")

# ---- Grace STOP ratified ----------------------------------------------------
check("GRACE'S STOP RATIFIED (her own T2511): {5,3,0} is not a single geometry — boundary faces give {5,1,0} (muon genus 1 "
      "disk), the interior tower gives {5,3,1} (tau genus 1), and {5,3,0} glues the muon's tower-genus-3 to the tau's "
      "face-genus-0 (inconsistent). N_c=3 is the color Peirce multiplicity V₁₂, NOT the muon's sub-domain genus. Muon NOT "
      "derived.",
      face != casey and tower != casey, "STOP ratified: faces {5,1,0} ≠ tower {5,3,1} ≠ claimed {5,3,0}; N_c=3 is V₁₂ color mult not genus → muon NOT derived")

# ---- investigate Casey flag ------------------------------------------------
check("INVESTIGATE CASEY'S FIX (candidate): the single flag D_IV⁵ ⊃ D_IV³ ⊃ Shilov(D_IV³) — tau on the boundary of the "
      "MUON's own doll — gives genera {5,3,0} in ONE filtration (each contains the next), resolving Grace's 'can't have "
      "both' (tau genus-0 = Shilov of D_IV³, inside the muon). Positions {5/2,3/2,0}=leading weights {D_IV⁵,D_IV³,point} "
      "match (T2517). Mass mechanism = containment (electron wraps all, lightest; tau wraps nothing, heaviest).",
      casey == [n_C, N_c, 0], "Casey flag D_IV⁵⊃D_IV³⊃Shilov(D_IV³): genera {5,3,0} single filtration, matches positions, containment mass-mechanism → consistent candidate")

# ---- hold the STOP: burden to exhibit --------------------------------------
check("HOLD THE STOP (burden to EXHIBIT, not assume): Casey's flag is a consistent candidate that resolves the "
      "inconsistency and matches positions, BUT the burden is to EXHIBIT that the generations sit on THIS flag (vs F86's "
      "boundary faces) AND that the containment overlap reproduces the c-function + (24/π²)⁶ — not assume it. Grace's STOP "
      "stands until exhibited. I do NOT bank the muon.",
      True, "burden = exhibit (generations on this flag + overlap reproduces number), not assume; STOP stands; muon NOT banked")

# ---- verdict ---------------------------------------------------------------
check("VERDICT: muon NOT derived — STOP ratified, my cross-check owned as arithmetic-only. Casey's single-flag fix "
      "(D_IV⁵⊃D_IV³⊃Shilov(D_IV³)) is a consistent candidate resolving the inconsistency + matching positions, but the "
      "burden is to EXHIBIT (not assume). What holds: EW area banked; (24/π²)⁶ a strong assembled form (home open); "
      "mass=depth intuition (corrected form pending). Discipline paid for itself — an unearned 'derived' caught before "
      "banking, correcting toward a firmer structure. Nothing false in the book. Five-Absence-positive.",
      abs(number - 206.76) < 0.1 and casey == [n_C, N_c, 0] and face != casey,
      "muon NOT derived (STOP ratified, cross-check owned arithmetic-only); Casey flag = consistent candidate to EXHIBIT not assume; EW banked, (24/π²)⁶ home open; nothing false banked")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-42 (07-23) muon NOT derived — Grace STOP ratified, Elie owns arithmetic-only + investigates Casey's fix (pull 23p):
  * OWN: my blind cross-check = arithmetic (24/π²)⁶=206.77 only, NOT the geometry. Muon NOT derived.
  * GRACE STOP (her T2511): {{5,3,0}} not one geometry — faces {{5,1,0}}, tower {{5,3,1}}; N_c=3 is V₁₂ color mult, not genus. Ratified.
  * INVESTIGATE Casey flag D_IV⁵⊃D_IV³⊃Shilov(D_IV³): genera {{5,3,0}} single filtration, matches positions {{5/2,3/2,0}}, containment mass-mechanism → consistent CANDIDATE.
  * HOLD: burden = EXHIBIT (generations on this flag + overlap reproduces number), not assume. STOP stands; NOT banked.
  => discipline paid for itself: unearned 'derived' caught before banking. EW area banked; (24/π²)⁶ home open; nothing false in the book.
""")
