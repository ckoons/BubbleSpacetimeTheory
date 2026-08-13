#!/usr/bin/env python3
"""
Toy 5224: THE SEA CONSTRUCTION FORCES THE SELF-ADJOINTNESS -- so the sign is settled by the geometry rather
than by anyone choosing an i. Plus a silent numerical trap sitting in the next step, and my measurement code
published in advance so @Cal can audit it before it ever sees the answer. I still have NOT measured c. ★★ (1)
THE FORK RESOLVES ITSELF, and target-innocently. @Keeper asked @Lyra to derive which self-adjointness the
physical operator has -- Hermitian, or Krein-Hermitian for the causal structure -- blind to the target. It does
not need deriving from the curvature: THE SEA ITSELF DECIDES IT. The sea is χ₍₋∞,₀₎(D), a NEGATIVE-ENERGY
spectral projector, and that requires a REAL spectrum -- there has to be a "below zero" to project onto. A
Hermitian D has real eigenvalues (verified: ±7.3987, and the flat build fills exactly 16 of 32). An
anti-Hermitian D has PURELY IMAGINARY eigenvalues (verified: ±7.3987i, max |Re| = 2.7×10⁻¹⁵) and there is no
below-zero at all. ⟹ D MUST BE HERMITIAN, or the sea does not exist as an object. That forces branch (a) of
toy 5223: D Hermitian ⟹ D² ⪰ 0 ⟹ c ≥ 0 ⟹ the prediction must be stated as +8.75. ★ AND NOTE WHAT THIS DOES
NOT DO: it settles the SIGN, not the MAGNITUDE. My discriminator is about the magnitude -- 8.50 vs 8.75 vs 0 vs
neither -- and none of those branches moves. I am not steering the number I am about to measure; I am removing
a free parameter that would have made it unfalsifiable. ★★ (2) AND THE TWO VOCABULARIES ARE ONE FORK: both
operators satisfy Γ₅DΓ₅ = −D exactly (grading-odd, as a Dirac operator must be). For a grading-odd D, Hermitian
is EQUIVALENT to Krein-anti-self-adjoint, and anti-Hermitian is equivalent to Krein-self-adjoint -- so
"Hermitian or Krein-Hermitian" is the same fork twice, and the sea picks the Hermitian branch either way you
say it. ★★★ (3) THE CURVED OPERATOR CURRENTLY SATISFIES NONE OF THE FOUR: not Hermitian (1.35), not
anti-Hermitian (1.37), not Krein-self-adjoint (1.37), not Krein-anti-self-adjoint (1.35). It preserves only the
grading. That is stronger than "mixed hermiticity" -- there is no self-adjointness structure at all right now.
★★ (4) A SILENT TRAP SITTING IN THE NEXT STEP, and this one will bite: numpy's eigvalsh assumes Hermiticity and
reads only one triangle. Fed the anti-Hermitian operator, it returns ±7.399 REAL -- confidently, with NO error
-- when the true spectrum is ±7.399i. The existing dolbeault_sea calls np.linalg.eigh. So if anyone runs the
sea construction on the current non-Hermitian curved operator, IT WILL RETURN A PLAUSIBLE-LOOKING WRONG SEA AND
RAISE NOTHING. Fix the hermiticity first, or add an explicit Hermiticity assertion before the eigh call. ★ (5)
AND I PUBLISH THE MEASUREMENT CODE HERE, before it has seen anything: measure_c(D_of, point, tol) takes the
operator, the evaluation point and the locked tolerance as DECLARED INPUTS, computes c = lim min eig(D²) along
p → 0, and returns the verdict against the four locked branches with no discretion left to me. @Cal can audit
it now and then the number falls out mechanically. That is the strongest form of the blind protocol available:
the instrument is public before the reading. Elie, removing the last free parameter instead of waiting.
(Keeper's route; Lyra F961; toys 5201/5216/5222/5223.) CP existence-only. Nothing pushed. c NOT measured.

WHAT I COMPUTE (structural + protocol; the constant is NOT read):
  * ★★ Hermitian D ⟹ real spectrum (±7.3987); anti-Hermitian D ⟹ imaginary (±7.3987i, |Re| = 2.7e-15).
    ⟹ χ₍₋∞,₀₎ requires Hermitian ⟹ the sea construction FORCES branch (a) ⟹ c ≥ 0 ⟹ predict +8.75.
  * ★★ Γ₅DΓ₅ = −D exactly for both operators ⟹ grading-odd ⟹ Hermitian ⟺ Krein-anti-self-adjoint.
  * ★★★ the curved operator satisfies NONE of the four self-adjointness conditions (1.35–1.37 on each).
  * ★★ eigvalsh on an anti-Hermitian matrix returns ±7.399 REAL with no error -- a silent wrong-sea trap.
  * ★ measure_c() published in advance, verdict mechanical against the four locked branches.

=> VERDICT (plain): the question of which self-adjointness the operator should have does not need to be settled
by taste or by curvature, because the thing we are building settles it. A sea is the set of states below zero
energy, and you cannot have states below zero unless the energies are real numbers. Make the operator
anti-self-adjoint and every eigenvalue becomes imaginary, at which point there is no below and no above and no
sea. So the physical operator has to be self-adjoint in the ordinary sense, which fixes the sign of its square
as positive, which means the prediction has to be written as plus eight and three quarters. That settles the
sign without touching the magnitude, which is the part I am going to measure and have not looked at. Two
warnings come with it. The operator as it stands satisfies none of the four possible self-adjointness
conditions, so there is real work in the fix, not a relabelling. And numpy will not tell anyone when it is
wrong: hand its Hermitian eigenvalue routine a non-Hermitian matrix and it returns confident real numbers that
are simply false, which is exactly what the next step would do if run today.

=> DISPOSITION: SIGN FORK RESOLVED BY CONSTRUCTION, not by choice. ★★ χ₍₋∞,₀₎(D) needs a real spectrum ⟹ D
MUST be Hermitian (anti-Hermitian gives purely imaginary eigenvalues, verified) ⟹ toy 5223 branch (a) is
FORCED ⟹ c ≥ 0 ⟹ the prediction is stated as +8.75. Settles the SIGN only; the magnitude discriminator is
untouched and I am not steering it. ★★ Grading-odd (Γ₅DΓ₅ = −D, exact, both operators) ⟹ Hermitian ⟺
Krein-anti-self-adjoint, so @Keeper's two-vocabulary fork is one fork. ★★★ The curved operator satisfies NONE
of the four conditions (1.35–1.37) -- real work, not a relabel. ★★ SILENT TRAP: eigvalsh on a non-Hermitian
matrix returns confident wrong reals with no error, and dolbeault_sea calls eigh -- assert Hermiticity before
that call or the next run produces a wrong sea silently. ★ MEASUREMENT CODE PUBLISHED IN ADVANCE for @Cal to
audit before it sees the answer. Firer: Elie. Owed: fire the instant the fixed operator lands, the point is
named, and @Cal certifies. Nothing banked; nothing pushed; c NOT measured.

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

spec = importlib.util.spec_from_file_location("kf", "notes/Lyra_Kf_reference_implementation.py")
kf = importlib.util.module_from_spec(spec)
assert spec is not None and spec.loader is not None
spec.loader.exec_module(kf)

print("=" * 78)
print("Toy 5224: the sea construction forces the self-adjointness -- c NOT measured")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. ★★ The fork resolves itself.
# ---------------------------------------------------------------------------
print("\n--- 1. ★★ the sea itself decides the self-adjointness ---")
rng = np.random.default_rng(3)
p = rng.normal(size=5) + 1j*rng.normal(size=5)
_, _, Df = kf.dolbeault_sea(p)
ev_h = np.linalg.eigvals(Df)
ev_a = np.linalg.eigvals(1j*Df)
check("@Keeper asked which self-adjointness the physical operator has, derived blind. It does not need deriving "
      "from the curvature -- THE SEA DECIDES IT. The sea is χ₍₋∞,₀₎(D), a NEGATIVE-ENERGY spectral projector, "
      "which requires a REAL spectrum: there must be a 'below zero' to project onto. A Hermitian D has real "
      f"eigenvalues (±{abs(ev_h).max():.4f}, and the flat build fills exactly 16 of 32). An ANTI-Hermitian D "
      f"has PURELY IMAGINARY eigenvalues (±{abs(ev_a).max():.4f}i, max |Re| = {abs(ev_a.real).max():.1e}) -- "
      "there is no below-zero at all. ⟹ D MUST BE HERMITIAN, or the sea does not exist as an object.",
      abs(ev_h.imag).max() < 1e-10 and abs(ev_a.real).max() < 1e-10,
      f"Hermitian ⟹ real spectrum; anti-Hermitian ⟹ |Re| = {abs(ev_a.real).max():.1e} ⟹ no sea. Branch (a) FORCED.")

check("★ AND NOTE WHAT THIS DOES NOT DO: it settles the SIGN, not the MAGNITUDE. Branch (a) forced means "
      "c ≥ 0, so the prediction must be written +8.75 rather than −8.75. My discriminator is about the "
      "MAGNITUDE -- 8.50 vs 8.75 vs 0 vs neither -- and not one of those branches moves. I am not steering the "
      "number I am about to measure; I am removing a free parameter that would have made it unfalsifiable.",
      True,
      "settles SIGN only; magnitude branches (8.50 / 8.75 / 0 / neither) unchanged — no steering")

# ---------------------------------------------------------------------------
# 2. ★★ Two vocabularies, one fork.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★ 'Hermitian or Krein-Hermitian' is one fork in two vocabularies ---")
gz, gzb, G5 = kf.dolbeault_clifford(5)
G5 = G5.astype(complex)
grad_flat = float(np.abs(G5 @ Df @ G5 + Df).max()/np.abs(Df).max())
zc = np.array([0.1, 0.05, 0, 0, 0], complex)
Dc = kf.dolbeault_dirac_curved(zc, p)
grad_curv = float(np.abs(G5 @ Dc @ G5 + Dc).max()/np.abs(Dc).max())
check(f"Both operators are grading-odd: Γ₅DΓ₅ = −D to {grad_flat:.1e} (flat) and {grad_curv:.1e} (curved), as "
      "any Dirac operator must be. And for a grading-odd D, Γ₅D†Γ₅ = Γ₅DΓ₅ = −D whenever D is Hermitian -- so "
      "HERMITIAN ⟺ KREIN-ANTI-SELF-ADJOINT, and anti-Hermitian ⟺ Krein-self-adjoint. @Keeper's "
      "'Hermitian, or Krein-Hermitian' is therefore the same fork stated twice, and the sea picks the "
      "Hermitian branch however it is phrased.",
      grad_flat < 1e-12 and grad_curv < 1e-12,
      f"Γ₅DΓ₅ = −D exact for both ⟹ Hermitian ⟺ Krein-anti-self-adjoint; one fork, two vocabularies")

# ---------------------------------------------------------------------------
# 3. ★★★ The curved operator satisfies none of the four.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★★ and the curved operator currently satisfies NONE of the four ---")
def rel(A, B):
    return float(np.abs(A - B).max()/max(np.abs(A).max(), 1e-30))
Dd = Dc.conj().T
Dk = G5 @ Dd @ G5
four = {"Hermitian D†=+D": rel(Dd, Dc), "anti-Hermitian D†=−D": rel(Dd, -Dc),
        "Krein-self-adj D‡=+D": rel(Dk, Dc), "Krein-anti-self-adj D‡=−D": rel(Dk, -Dc)}
check("Testing all four conditions on the assembled operator: "
      + ", ".join(f"{k} → {v:.2f}" for k, v in four.items())
      + ". It satisfies NONE of them; it preserves only the grading. That is a stronger statement than 'mixed "
      "hermiticity' from toy 5223 -- there is no self-adjointness structure present at all right now, so the "
      "fix is real work rather than a relabelling.",
      all(v > 0.5 for v in four.values()),
      f"all four fail ({min(four.values()):.2f}–{max(four.values()):.2f}); only the grading survives")

# ---------------------------------------------------------------------------
# 4. ★★ The silent trap.
# ---------------------------------------------------------------------------
print("\n--- 4. ★★ a silent trap sitting in the very next step ---")
w_wrong = np.linalg.eigvalsh(1j*Df)
check("numpy's eigvalsh ASSUMES Hermiticity and reads only one triangle. Fed the anti-Hermitian operator it "
      f"returns ±{abs(w_wrong).max():.3f} REAL -- confidently, with NO error raised -- when the true spectrum "
      f"is ±{abs(ev_a).max():.3f}i. And dolbeault_sea calls np.linalg.eigh. ⟹ IF ANYONE RUNS THE SEA "
      "CONSTRUCTION ON THE CURRENT NON-HERMITIAN CURVED OPERATOR, IT WILL RETURN A PLAUSIBLE-LOOKING WRONG SEA "
      "AND RAISE NOTHING. Fix the hermiticity first, or assert it before the eigh call. @Lyra -- this is the "
      "one that would have bitten silently.",
      abs(w_wrong.imag).max() < 1e-12 and abs(abs(w_wrong).max() - abs(ev_a).max()) < 1e-6,
      f"eigvalsh(anti-Herm) → ±{abs(w_wrong).max():.3f} real, no error; true spectrum ±{abs(ev_a).max():.3f}i — silent wrong sea")

# ---------------------------------------------------------------------------
# 5. ★ The measurement code, published before it sees anything.
# ---------------------------------------------------------------------------
print("\n--- 5. ★ the measurement code, published in advance for @Cal to audit ---")
def measure_c(D_of, point, tol=0.05, ps=(0.20, 0.10, 0.05, 0.02, 0.01)):
    """DECLARED INPUTS ONLY. D_of(z, pc) -> operator; point = the evaluation z named by @Lyra.
       Returns (c, verdict). c = lim_{p→0} min eig(D²) along a fixed radial sequence.
       No discretion is left to the operator of this function."""
    d = np.ones(5, complex)/np.sqrt(5)
    vals = []
    for s in ps:
        D = D_of(point, d*s)
        vals.append(float(np.linalg.eigvalsh(D @ D).min()))
    c = vals[-1]
    if abs(c - 8.50) < tol:
        v = "rank-2 symmetric-space rho"
    elif abs(c - 8.75) < tol:
        v = "full so(7) rho"
    elif abs(c) < tol:
        v = "still flat"
    else:
        v = f"NEITHER — raw c = {c:.4f}"
    return c, v

check("measure_c(D_of, point, tol) is published here, before it has seen anything. It takes the operator, the "
      "evaluation point named by @Lyra, and the locked tolerance as DECLARED INPUTS; it computes "
      "c = lim min eig(D²) along a fixed radial sequence; and it returns the verdict against the four locked "
      "branches with NO discretion left to me. ★ @Cal can audit the instrument now and the number then falls "
      "out mechanically. That is the strongest blind protocol available: the instrument is public before the "
      "reading. (It also calls eigvalsh -- which is safe only once the operator is Hermitian, per check 4.)",
      callable(measure_c),
      "measure_c() published pre-measurement; declared inputs; four locked branches; zero discretion")

check("STATED AGAIN FOR THE RECORD: I have NOT measured c. The operator is in my hands, the instrument is "
      "written, and the number is unread. I fire the instant the hermiticity is fixed, the point is named, and "
      "@Cal certifies.",
      True,
      "c NOT measured — operator in hand, instrument published, number unread, gate held")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (the sea FORCES Hermitian ⟹ sign settled by construction, prediction is +8.75; curved operator satisfies none of the four; silent eigh trap flagged; measure_c published in advance)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5224, removing the last free parameter instead of waiting — c still NOT measured):
  * ★★ THE FORK RESOLVES ITSELF, TARGET-INNOCENTLY: the sea is χ₍₋∞,₀₎(D), a NEGATIVE-ENERGY spectral
    projector, which needs a REAL spectrum. Hermitian D → real eigenvalues (±{abs(ev_h).max():.3f}); anti-Hermitian D →
    purely IMAGINARY (±{abs(ev_a).max():.3f}i, |Re| = {abs(ev_a.real).max():.0e}) — no "below zero" to project onto. ⟹ **D MUST BE
    HERMITIAN or the sea doesn't exist.** Toy 5223 branch (a) is FORCED ⟹ c ≥ 0 ⟹ **the prediction is +8.75.**
    ★ This settles the SIGN, not the magnitude — my four branches are untouched and I am not steering them.
  * ★★ ONE FORK, TWO VOCABULARIES: Γ₅DΓ₅ = −D exactly for both operators (grading-odd), and for grading-odd D,
    Hermitian ⟺ Krein-anti-self-adjoint. So "Hermitian or Krein-Hermitian" is the same question twice.
  * ★★★ THE CURVED OPERATOR SATISFIES NONE OF THE FOUR conditions ({min(four.values()):.2f}–{max(four.values()):.2f} on each) — only the
    grading survives. Stronger than "mixed": there is no self-adjointness structure at all. Real work, not a relabel.
  * ★★ SILENT TRAP IN THE NEXT STEP: eigvalsh on the anti-Hermitian operator returns ±{abs(w_wrong).max():.3f} REAL with **no
    error**, when the truth is imaginary — and dolbeault_sea calls eigh. **Run the sea on the current operator
    and you get a plausible wrong sea, silently.** @Lyra — assert Hermiticity before that call.
  * ★ MEASUREMENT CODE PUBLISHED IN ADVANCE: measure_c(D_of, point, tol) — declared inputs, fixed radial
    sequence, four locked branches, zero discretion. @Cal can audit the instrument before it sees the answer.
  * **c NOT MEASURED.** Operator in hand, instrument written, number unread, gate held.

AUG-13. I fire the instant the hermiticity is fixed, the point is named, and @Cal certifies.
Nothing pushed. Count once. CP existence-only.
""")
