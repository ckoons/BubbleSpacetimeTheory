#!/usr/bin/env python3
"""
Toy 5240: DIAGONALIZED. τ_min IS A TRUNCATION ZERO PLUS A FREE KNOB, AND λ = 5 HANDS BACK −6.25 EXACTLY. The
operator landed and I read it, as instructed. The reading is τ_min = −5λ/4 -- a free parameter -- and the route
by which it produces the expected number is a bug. ★ CREDIT FIRST, and it is real: @Lyra exposed ν as an
explicit argument instead of baking it, refused to diagonalize herself, flagged the rank-2 Gindikin completion
as owed to my cross-check, and wrote plainly in the file that "VALUE (6 vs 6.25) rides on nu (unpinned)." That
is honest engineering and it is why this was auditable at all. ★★ (1) BUT THE ASSEMBLED MATRIX IS DIAGONAL. A is
strictly sub-diagonal, so A†A is diagonal with entries (d+1)(ν+d) -- nothing mixes, the eigenvalues ARE the
diagonal, and the "tower tridiagonal" structure test passes VACUOUSLY (a diagonal matrix trivially has nothing
above the second diagonal). There is no diagonalization happening in any meaningful sense. ★★★ (2) AND THE LAST
DIAGONAL ENTRY IS ZERO, BECAUSE A[N+1, N] DOES NOT EXIST. (d+1)(ν+d) is never zero for d ≥ 0 and ν > 0, so that
zero is the TRUNCATION EDGE, not a state. Its eigenvector peaks at d = N for N = 8, 12, 20, 40 -- it rides the
cut wherever the cut is put, which is the textbook signature of a boundary artifact. ⟹ τ_min = 0 + R_p(q) =
min_q (λ/2)(q − 5/2) = −5λ/4: THE GROUND IS THE KNOB, AND NOTHING ELSE. ★★★★ (3) AND HERE IS THE PART THAT
MATTERS MOST: λ = 5 = n_C GIVES τ_min = −6.25 EXACTLY -- the expected Kostant number, on the nose, from a
truncation artifact plus a free parameter set to a BST integer. Verified: λ = 0 → 0.0000, λ = 2 → −2.5000, λ = 5
→ −6.2500, each matching −5λ/4 to machine precision. EIGHTH ADDRESS, and the most dangerous of the day, because
this one PRODUCES THE TARGET. ★ (4) AND WITH TWO FREE KNOBS THE SPECTRUM CANNOT DISCRIMINATE AT ALL: τ_min(ν,λ)
= ν − 5λ/4 is one equation in two unknowns, so 6.00 and 6.25 are each reachable by infinitely many (ν, λ) --
(6.00, 0.00) and (6.25, 0.20) both give 6, (6.25, 0.00) and (8.75, 2.00) both give 6.25. Exposing a knob does
not remove it. ★ (5) CONSTRUCTION GAP: the file assembles A†A = p⁻p⁺ only, not (A + A†)² -- the cross terms A²,
(A†)², AA† are dropped, differing by 162.0 at N = 12. This is one term of the Dirac square, not the square.
★ (6) AND R_p = (λ/2)(q − 5/2) IS LINEAR IN q, confirming toy 5239 from the code itself: it is the charge, not
−Ω_K (constant on the fiber) and not |ρ_G|² (constant). It matches NEITHER hypothesis, and it enters as
Rp·eye(n) -- a scalar shift per branch, so the intercept IS the parameter. ⟹ VERDICT: I read it, and the
reading is not a measurement. Not voided on residual -- voided because the object cannot answer the question.
Elie, reporting the number and what it is made of. (Lyra F980/assembled operator; toys 5233-5239.) CP
existence-only. Nothing pushed. NO VALUE READ.

WHAT I VERIFY:
  * ★★ the assembled D² is DIAGONAL (max off-diagonal 0.000e+00) ⟹ nothing mixes; structure test vacuous.
  * ★★★ the last diagonal entry is 0 (truncation edge); its eigenvector peaks at d = N for N = 8,12,20,40.
  * ★★★★ τ_min = −5λ/4 exactly; λ = 5 = n_C returns −6.2500, the expected number, from artifact + knob.
  * ★ τ_min(ν,λ) = ν − 5λ/4: one equation, two unknowns ⟹ 6.00 and 6.25 both reachable ⟹ no discrimination.
  * ★ assembled object is A†A, not (A+A†)² — differs by 162.0 at N = 12 (cross terms dropped).
  * ★ R_p = (λ/2)(q − 5/2) is linear in q ⟹ the charge; matches neither hypothesis (confirms toy 5239).

=> VERDICT (plain): the operator arrived, I diagonalized it, and I have to report that the number it gives is
not a measurement of anything. Three things went wrong and they compound. The matrix turns out to be diagonal,
so there is nothing to diagonalize and the structure test that was supposed to check its shape passes
automatically. Its last entry is zero for a mechanical reason -- the tower was cut off, and the cut leaves an
empty slot -- so the lowest state is the edge of the truncation rather than a physical ground. And once you
subtract that spurious zero, what remains is exactly the free parameter that was dialed in, times a fixed
factor. Set that parameter to five, which is one of our own integers, and the ground comes out at minus six and
a quarter: precisely the number we were hoping to see, assembled from a bug and a dial. That is the eighth time
today the same problem has surfaced and by far the most dangerous, because every earlier instance merely failed
to test the answer, and this one manufactures it. To be fair to the build: the parameter was exposed rather than
hidden, which is why I could catch this at all, and the author explicitly said the value rides on it. But
exposing a dial does not remove it -- with two dials, both candidate answers are reachable, so the spectrum
cannot choose between them no matter how carefully I read it.

=> DISPOSITION: ★ CREDIT: @Lyra exposed ν explicitly, refused to self-diagonalize, flagged the rank-2 completion
as owed, and stated the value rides on ν — honest engineering, and the reason this was auditable. ★★ (1) THE
MATRIX IS DIAGONAL (max off-diag 0.000e+00) ⟹ nothing mixes; the "tridiagonal" test passes vacuously. ★★★ (2)
LAST DIAGONAL ENTRY = 0 because A[N+1,N] does not exist ⟹ TRUNCATION EDGE, not a state; eigenvector rides the
cut at d = N for N = 8,12,20,40. ⟹ τ_min = 0 + R_p = −5λ/4: THE GROUND IS THE KNOB. ★★★★ (3) λ = 5 = n_C GIVES
τ_min = −6.2500 EXACTLY — the expected value from (truncation bug) + (knob at a BST integer). EIGHTH ADDRESS,
the first that PRODUCES the target rather than merely failing to test it. ★ (4) τ_min(ν,λ) = ν − 5λ/4: one
equation, two unknowns ⟹ 6.00 and 6.25 both reachable ⟹ NO DISCRIMINATION POSSIBLE. ★ (5) assembled object is
A†A = p⁻p⁺, NOT (A+A†)² (differs by 162.0 at N = 12) — cross terms dropped. ★ (6) R_p = (λ/2)(q − 5/2) LINEAR
in q ⟹ the charge, matching neither hypothesis (confirms 5239 from the code). ⟹ NOT VOIDED ON RESIDUAL —
voided because the object cannot answer. NO VALUE READ. Firer: Elie. Nothing banked; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-13.
"""

import importlib.util
import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

spec = importlib.util.spec_from_file_location("ld", "notes/Lyra_assembled_dirac_operator.py")
ld = importlib.util.module_from_spec(spec)
assert spec is not None and spec.loader is not None
spec.loader.exec_module(ld)

print("=" * 78)
print("Toy 5240: DIAGONALIZED — τ_min is a truncation zero plus a free knob. NO VALUE READ")
print("=" * 78)

# ---------------------------------------------------------------------------
# 0. Credit.
# ---------------------------------------------------------------------------
print("\n--- 0. credit first ---")
check("@Lyra exposed ν as an explicit argument instead of baking it, refused to diagonalize herself, flagged "
      "the rank-2 Gindikin completion as owed to my cross-check, and wrote in the file that 'VALUE (6 vs 6.25) "
      "rides on nu (unpinned).' That is honest engineering and it is the reason any of what follows was "
      "auditable at all.",
      True,
      "ν exposed not baked; self-diagonalization refused; rank-2 gap flagged — honest, and auditable")

# ---------------------------------------------------------------------------
# 1. The matrix is diagonal.
# ---------------------------------------------------------------------------
print("\n--- 1. ★★ is there anything to diagonalize? ---")
M = ld.assemble_D2(2.5, 5.0, 12, q_ground=0)
offd = float(np.max(np.abs(M - np.diag(np.diag(M)))))
check(f"A is strictly sub-diagonal, so A†A is DIAGONAL: max |off-diagonal| = {offd:.3e}. Nothing mixes, the "
      "eigenvalues ARE the diagonal entries (d+1)(ν+d), and the 'tower tridiagonal' structure test passes "
      "VACUOUSLY -- a diagonal matrix trivially has nothing above its second diagonal. There is no "
      "diagonalization happening in any meaningful sense.",
      offd < 1e-12,
      f"max off-diagonal = {offd:.3e} ⟹ diagonal; 'tridiagonal' test passes vacuously")

# ---------------------------------------------------------------------------
# 2. The truncation zero.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★★ where does the lowest eigenvalue come from? ---")
Mk = ld.assemble_D2(2.5, 0.0, 12, q_ground=0)
diag = np.diag(Mk)
rides = []
for N in [8, 12, 20, 40]:
    Mn = ld.assemble_D2(2.5, 0.0, N, q_ground=0)
    w, v = np.linalg.eigh(Mn)
    rides.append(int(np.argmax(np.abs(v[:, 0]))) == N)
check(f"The diagonal at ν = 2.5, N = 12 is {np.round(diag,1).tolist()} -- the LAST ENTRY IS {diag[-1]:.1f}, "
      "because A[N+1, N] does not exist. But (d+1)(ν+d) is never zero for d ≥ 0 and ν > 0, so that zero is the "
      f"TRUNCATION EDGE, not a state. ★ Its eigenvector peaks at d = N for N = 8, 12, 20, 40 "
      f"({sum(rides)}/4) -- it rides the cut wherever the cut is placed, the textbook signature of a boundary "
      "artifact. ⟹ τ_min = 0 + R_p(q): THE GROUND IS THE KNOB AND NOTHING ELSE.",
      diag[-1] == 0.0 and all(rides),
      f"last diagonal entry = 0 (truncation edge); zero-mode eigenvector rides d = N in {sum(rides)}/4 cases")

# ---------------------------------------------------------------------------
# 3. lambda = 5 hands back -6.25.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★★★ and what does the knob produce? ---")
rows = []
for lam in [0.0, 2.0, 5.0]:
    acc = ld.accessor(2.5, lam, 12)
    t = min(float(np.min(np.linalg.eigvalsh(acc[q]))) for q in range(6))
    rows.append((lam, t, -5*lam/4))
ok = all(abs(t - pred) < 1e-9 for _, t, pred in rows)
check("Diagonalized at ν = 2.5: " + ", ".join(f"λ = {l:.0f} → τ_min = {t:.4f}" for l, t, _ in rows) +
      " -- each matching the closed form −5λ/4 to machine precision. ★ λ = 5 = n_C GIVES τ_min = −6.2500 "
      "EXACTLY: the expected Kostant number, on the nose, assembled from a truncation artifact plus a free "
      "parameter set to a BST integer. EIGHTH ADDRESS, and the most dangerous of the day -- every earlier "
      "instance merely failed to TEST the answer; this one MANUFACTURES it.",
      ok and abs(rows[-1][1] + 6.25) < 1e-9,
      f"τ_min = −5λ/4 exactly; λ = 5 = n_C → −6.2500, the expected value, from artifact + knob")

# ---------------------------------------------------------------------------
# 4. Two knobs, no discrimination.
# ---------------------------------------------------------------------------
print("\n--- 4. ★ can the spectrum discriminate 6 from 6.25 at all? ---")
sols = {t: [(nu, 4*(nu - t)/5) for nu in (6.0, 6.25, 8.75)] for t in (6.0, 6.25)}
check("τ_min(ν, λ) = ν − 5λ/4 is ONE EQUATION IN TWO UNKNOWNS. Target 6.00 is reached at "
      + ", ".join(f"(ν={a:.2f}, λ={b:.2f})" for a, b in sols[6.0]) + "; target 6.25 at "
      + ", ".join(f"(ν={a:.2f}, λ={b:.2f})" for a, b in sols[6.25])
      + " -- and by infinitely many others. ★ BOTH CANDIDATE VALUES ARE REACHABLE BY CONSTRUCTION, so the "
      "spectrum cannot choose between them however carefully I read it. Exposing a knob does not remove it.",
      True,
      "one equation, two unknowns ⟹ 6.00 and 6.25 both reachable ⟹ no discrimination possible")

# ---------------------------------------------------------------------------
# 5-6. Construction gaps.
# ---------------------------------------------------------------------------
print("\n--- 5-6. ★ two construction gaps ---")
N = 12
A = np.zeros((N+1, N+1))
for d in range(N):
    A[d+1, d] = ld.bergman_raise_coeff(d, 2.5)
gap = float(np.max(np.abs((A + A.T) @ (A + A.T) - A.T @ A)))
check(f"The file assembles A†A = p⁻p⁺ ONLY, not (A + A†)²: they differ by {gap:.1f} at N = {N}. The cross terms "
      "A², (A†)² and AA† are dropped. ⟹ the assembled object is ONE TERM of the Dirac square, not the square. "
      "That is a construction gap independent of the knobs, and it changes the spectrum.",
      gap > 1,
      f"assembled = A†A ≠ (A+A†)², differing by {gap:.1f} at N = {N} — cross terms dropped")

rp = ld.Rp_grading(2.0)
lin = all(abs(rp[q] - (q - 2.5)) < 1e-12 for q in range(6))
check(f"And R_p(q) = (λ/2)(q − 5/2) is LINEAR in q -- at λ = 2 it gives exactly {[round(rp[q],2) for q in range(6)]} "
      "= the SO(2) charges. ★ That confirms toy 5239 FROM THE CODE: the reported grading is the CHARGE, not "
      "−Ω_K (constant on the fiber) and not |ρ_G|² (constant). It matches NEITHER hypothesis -- and it enters "
      "as Rp·eye(n), a scalar shift per branch, so the intercept IS the parameter.",
      lin,
      "R_p = (λ/2)(q − 5/2) linear in q ⟹ the charge; matches neither hypothesis; enters as a scalar shift")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (diagonalized: τ_min = −5λ/4, a truncation zero plus a free knob; λ = 5 returns −6.25 exactly; NO VALUE READ)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5240, I read it and the reading is not a measurement — NO VALUE READ):
  * **CREDIT:** @Lyra exposed ν explicitly rather than baking it, refused to self-diagonalize, flagged the
    rank-2 completion as owed, and stated in the file that the value rides on ν. **That honesty is why this
    was auditable.**
  * ★★ **THE MATRIX IS DIAGONAL** (max off-diagonal {offd:.3e}). A is strictly sub-diagonal ⟹ A†A is diagonal,
    nothing mixes, eigenvalues *are* the diagonal, and the "tower tridiagonal" test **passes vacuously**.
  * ★★★ **THE LOWEST EIGENVALUE IS THE TRUNCATION EDGE.** The last diagonal entry is **0** because A[N+1,N]
    doesn't exist — yet (d+1)(ν+d) is never 0 for d ≥ 0, ν > 0. Its eigenvector **peaks at d = N for N = 8,
    12, 20, 40** — it rides the cut wherever the cut is placed. ⟹ **τ_min = 0 + R_p = −5λ/4: the ground is
    the knob.**
  * ★★★★ **AND λ = 5 = n_C GIVES τ_min = −6.2500 EXACTLY** — the expected Kostant number, on the nose, from
    **a truncation artifact plus a free parameter set to a BST integer**. Verified: λ = 0 → 0.0000,
    λ = 2 → −2.5000, λ = 5 → −6.2500. **EIGHTH ADDRESS, and the most dangerous of the day**: every earlier
    instance merely failed to *test* the answer — **this one manufactures it.**
  * ★ **AND TWO KNOBS MEANS NO DISCRIMINATION.** τ_min(ν,λ) = ν − 5λ/4 is one equation in two unknowns; 6.00
    and 6.25 are each reachable by infinitely many (ν, λ). **Exposing a knob does not remove it.**
  * ★ **CONSTRUCTION GAPS:** the object is **A†A = p⁻p⁺, not (A+A†)²** (differs by {gap:.1f} at N = 12 — cross
    terms dropped); and **R_p = (λ/2)(q − 5/2) is linear in q**, i.e. the charge — confirming toy 5239 **from
    the code**, matching neither hypothesis, and entering as a scalar shift so the intercept *is* the parameter.

**NOT VOIDED ON RESIDUAL — voided because the object cannot answer the question.** The fiber was degenerate
(5239); the polynomial tower as built is diagonal with an artifact ground and two free dials. **NO VALUE READ.**

AUG-13. Nothing pushed. Count once. CP existence-only.
""")
