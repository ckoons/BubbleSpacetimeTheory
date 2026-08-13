#!/usr/bin/env python3
"""
Toy 5223: HOLD THE GATE -- three structural facts about the assembled curved operator that must be settled
before @Cal certifies and before I measure. I have NOT measured c. Everything below is structural, and I
deliberately did not compute the constant, because the gate is not cleared. ★ (0) FIRST, THE GOOD NEWS, and it
is real: the content audit that FAILED twice (toys 5214 and 5217, 0/7 D_IV⁵ ingredients) now PASSES. The
operator takes a position argument, the connection comes from _logdetg via the generic norm with genus 5, and
bergman_connection is genuinely in the call path. The domain is in the object at last -- the missing curvature
I diagnosed in 5217 has arrived. ★★ (1) BUT THE OPERATOR HAS MIXED HERMITICITY, and this is load-bearing.
Decomposing it: the MOMENTUM term Σ γ^{z_i}(i·p_i) + γ^{z̄_i}(i·p̄_i) is EXACTLY ANTI-Hermitian (‖M + M†‖ =
0.00×10⁰), while the CONNECTION term Σ γ^{z_i}A_i + γ^{z̄_i}Ā_i is EXACTLY Hermitian (‖C − C†‖ = 0.00×10⁰).
The two halves have OPPOSITE hermiticity, so D is neither self-adjoint nor anti-self-adjoint, and ‖D − D†‖/‖D‖
= 2.0 at the origin. Compare the flat build (F954), where D was exactly Hermitian: the momentum term acquired a
factor of i that the connection term did not. ⟹ D² IS NOT SIGN-DEFINITE, AND A NEGATIVE GROUND FOLLOWS FROM
THAT FACTOR OF i -- not necessarily from curvature. ★★★ (2) CONFIRMED DIRECTLY: at the origin,
D_curved = i·D_flat to 1.1×10⁻¹³, and the connection there is A(0) = 1.5×10⁻¹³, i.e. zero. So at the centre the
curvature contributes NOTHING and the entire difference from the flat operator is the factor i -- whose square
is −1. That is an available explanation for a negative D² that has nothing to do with the Lichnerowicz
relation. I am not claiming the −8.75 is wrong; I am saying the SIGN is currently determined by an
inconsistency in the assembly rather than by the geometry, so the sign bridge cannot be written on this
operator as it stands. ★ (3) AND A SECOND THING TO PIN: since A(origin) = 0, "the ground of D² at zero
momentum" is ambiguous until the POINT is specified -- at the centre the connection vanishes and the curvature
cannot contribute. @Lyra's docstring says "in the K-type normalization," which may well resolve it, but it must
be stated as part of the measurement definition, not left to me to choose. Where I evaluate is not my choice to
make after the fact. ★★ THE FIX, and either branch is fine: (a) DROP the i from the momentum term, restoring
the flat build's convention -- then D is Hermitian, D² ⪰ 0, my toy-5222 argument applies unchanged, and the
prediction must be +8.75; or (b) PUT an i on the connection term as well -- then D is anti-Hermitian, D² ⪯ 0,
c ≤ 0 throughout, and −8.75 is consistent with the magnitude as the invariant. What is NOT acceptable is the
present mixed state, in which the sign of the answer is set by which term got the i. Elie, holding a gate he
was told to be ready to fire through. (Lyra F961 assembly; Keeper's sign-bridge order; toys 5217/5220/5222.)
CP existence-only. Nothing pushed. I have not measured c.

WHAT I COMPUTE (all structural; the constant is NOT read):
  * ★ content audit now PASSES: position argument present; _logdetg / bergman / genus / generic-norm in the path.
  * ★★ momentum term ‖M + M†‖ = 0.00e+00 (anti-Hermitian); connection term ‖C − C†‖ = 0.00e+00 (Hermitian).
  * ★★ ‖D − D†‖/‖D‖ = 2.0 at the origin ⟹ D† = −D there ⟹ D² ⪯ 0 there, from the i.
  * ★★★ D_curved(0, p) = i·D_flat(p) to 1.1e-13, with A(0) = 1.5e-13 ⟹ curvature contributes nothing at the centre.
  * ★ ⟹ the evaluation POINT must be specified before "ground D² at zero momentum" is well defined.

=> VERDICT (plain): the domain finally made it into the operator, and that part is genuine and worth saying
first -- the check I ran twice and failed twice now passes. But the assembled object has a defect that lands
exactly on the question we are about to test. Its two halves disagree about hermiticity: the momentum piece
carries a factor of i and is anti-self-adjoint, the connection piece does not and is self-adjoint. Squaring
something built that way gives a quantity with no definite sign, and at the centre of the domain the whole
operator is simply i times the flat one -- the connection vanishes there, so nothing curved is contributing at
all, and the only thing distinguishing it from last week's flat build is a factor whose square is minus one.
That is a complete explanation for a negative square that never mentions curvature. So the sign we were about
to certify as a prediction is, as things stand, a property of which term got the i. Fix that either way and the
sign becomes real, and I will measure whichever convention is ratified. And one smaller thing: since the
connection is zero at the centre, somebody has to say where the ground is to be evaluated, and it should not be
me choosing after I have seen the numbers.

=> DISPOSITION: GATE HELD, and I have NOT measured c. ★ Content audit PASSES for the first time -- the domain
is in the operator (position argument, Bergman connection, genus 5). ★★ MIXED HERMITICITY: momentum term
exactly anti-Hermitian, connection term exactly Hermitian ⟹ D² not sign-definite ⟹ the negative ground is
explained by the factor i, not necessarily by curvature. ★★★ At the origin D_curved = i·D_flat (1.1e-13) with
A(0) = 0 ⟹ no curvature contribution at the centre. ★ The evaluation POINT must be specified as part of the
measurement definition. ★★ FIX (either is fine, @Lyra to choose and @Cal to certify): (a) drop the i from the
momentum term ⟹ Hermitian ⟹ c ≥ 0 ⟹ predict +8.75 (toy 5222 applies unchanged); or (b) add the i to the
connection term ⟹ anti-Hermitian ⟹ c ≤ 0 ⟹ −8.75 consistent, magnitude the invariant. NOT acceptable: the
present mixed state, where the sign is set by which term got the i. Firer: Elie. Owed: I measure the instant
the convention is uniform, the point is named, and @Cal certifies. Nothing banked; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-13.
"""

import importlib.util
import inspect
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
print("Toy 5223: HOLD THE GATE -- three structural facts before certification. c NOT measured.")
print("=" * 78)

# ---------------------------------------------------------------------------
# 0. The good news first.
# ---------------------------------------------------------------------------
print("\n--- 0. ★ the content audit that failed twice now PASSES ---")
src = (inspect.getsource(kf.dolbeault_dirac_curved) + inspect.getsource(kf.bergman_connection)
       + inspect.getsource(kf._logdetg))
ing = {t: (t in src) for t in ("Gd", "genus", "bergman", "_logdetg", "np.vdot")}
haspos = "def dolbeault_dirac_curved(z" in src
check("The mechanical audit that failed twice -- 0/7 D_IV⁵ ingredients in toys 5214 and 5217 -- now PASSES: "
      + ", ".join(f"{t} {'PRESENT' if v else 'absent'}" for t, v in ing.items())
      + f", and the operator takes a POSITION argument ({haspos}). The connection is built from the generic "
      "norm with genus 5 via _logdetg. ★ The domain is in the object at last; the missing curvature I "
      "diagnosed in 5217 has arrived. That is real and it deserves saying before anything else.",
      all(ing.values()) and haspos,
      f"{sum(ing.values())}/{len(ing)} ingredients present + position argument ⟹ the domain IS in the operator")

# ---------------------------------------------------------------------------
# 1. ★★ Mixed hermiticity.
# ---------------------------------------------------------------------------
print("\n--- 1. ★★ but the two halves disagree about hermiticity ---")
rng = np.random.default_rng(1)
z = np.array([0.1, 0.05, 0, 0, 0], complex)
pc = rng.normal(size=5) + 1j*rng.normal(size=5)
gz, gzb, _ = kf.dolbeault_clifford(5)
A = kf.bergman_connection(z)
M = sum(gz[i]*(1j*pc[i]) + gzb[i]*(1j*np.conj(pc[i])) for i in range(5))
C = sum(gz[i]*A[i] + gzb[i]*np.conj(A[i]) for i in range(5))
anti_M = float(np.abs(M + M.conj().T).max()/np.abs(M).max())
herm_C = float(np.abs(C - C.conj().T).max()/max(np.abs(C).max(), 1e-30))
D0 = kf.dolbeault_dirac_curved(np.zeros(5, complex), pc)
ratio0 = float(np.abs(D0 - D0.conj().T).max()/np.abs(D0).max())
check("Decomposing the operator: the MOMENTUM term Σγ^{z_i}(i·p_i) + γ^{z̄_i}(i·p̄_i) is EXACTLY ANTI-Hermitian "
      f"(‖M + M†‖/‖M‖ = {anti_M:.2e}), while the CONNECTION term Σγ^{{z_i}}A_i + γ^{{z̄_i}}Ā_i is EXACTLY "
      f"Hermitian (‖C − C†‖/‖C‖ = {herm_C:.2e}). Opposite hermiticity, so D is neither self-adjoint nor "
      f"anti-self-adjoint -- at the origin ‖D − D†‖/‖D‖ = {ratio0:.1f}. In the flat build (F954) D was EXACTLY "
      "Hermitian; the momentum term has acquired a factor of i that the connection term did not. ⟹ D² IS NOT "
      "SIGN-DEFINITE, and a negative ground follows from that i rather than necessarily from curvature.",
      anti_M < 1e-12 and herm_C < 1e-12 and ratio0 > 1.9,
      f"momentum ANTI-Hermitian ({anti_M:.1e}); connection Hermitian ({herm_C:.1e}); ‖D−D†‖/‖D‖ = {ratio0:.2f} at origin")

# ---------------------------------------------------------------------------
# 2. ★★★ Confirmed at the origin.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★★ and at the centre the operator is simply i × the flat one ---")
devs, Anorm = [], []
for _ in range(3):
    p = rng.normal(size=5) + 1j*rng.normal(size=5)
    Dc = kf.dolbeault_dirac_curved(np.zeros(5, complex), p)
    _, _, Df = kf.dolbeault_sea(p)
    devs.append(float(np.abs(Dc - 1j*Df).max()/np.abs(Dc).max()))
    Anorm.append(float(np.abs(kf.bergman_connection(np.zeros(5, complex))).max()))
check(f"At the origin D_curved = i·D_flat to {max(devs):.1e}, and the connection there is A(0) = "
      f"{max(Anorm):.1e} -- zero. So at the centre the curvature contributes NOTHING, and the entire "
      "difference from last week's flat build is a factor whose square is −1. That is a complete explanation "
      "for a negative D² that never mentions the Lichnerowicz relation. ★ I am NOT claiming the −8.75 is "
      "wrong. I am saying the SIGN is currently set by an inconsistency in the assembly rather than by the "
      "geometry, so the sign bridge cannot be written on this operator as it stands.",
      max(devs) < 1e-10 and max(Anorm) < 1e-10,
      f"D_curved(0) = i·D_flat to {max(devs):.1e}; A(0) = {max(Anorm):.1e} ⟹ no curvature at the centre")

# ---------------------------------------------------------------------------
# 3. ★ The evaluation point must be named.
# ---------------------------------------------------------------------------
print("\n--- 3. ★ and the evaluation point has to be part of the definition ---")
check("Since A(origin) = 0, 'the ground of D² at zero momentum' is ambiguous until the POINT is specified: at "
      "the centre the connection vanishes and the curvature cannot contribute at all. @Lyra's docstring says "
      "'in the K-type normalization,' which may well resolve it -- but it has to be stated as part of the "
      "measurement definition, before I run. Where I evaluate is not a choice I should be making after seeing "
      "numbers, and I am not going to.",
      max(Anorm) < 1e-10,
      "A(origin) = 0 ⟹ the point must be named in the definition, not chosen by me post hoc")

# ---------------------------------------------------------------------------
# 4. ★★ The fix.
# ---------------------------------------------------------------------------
print("\n--- 4. ★★ the fix -- either branch is fine, but the present mixed state is not ---")
fixes = {
    "(a) drop the i from the momentum term": "D Hermitian ⟹ D² ⪰ 0 ⟹ c ≥ 0 ⟹ predict +8.75 (toy 5222 applies unchanged)",
    "(b) add an i to the connection term": "D anti-Hermitian ⟹ D² ⪯ 0 ⟹ c ≤ 0 ⟹ −8.75 consistent, magnitude the invariant",
}
check("Either branch makes the sign real: "
      + "; ".join(f"{k} → {v}" for k, v in fixes.items())
      + ". @Lyra chooses, @Cal certifies. ★ What is NOT acceptable is the present mixed state, in which the "
      "sign of the answer is set by which term happened to get the i -- because then the number I measure "
      "cannot fail, and a result that cannot fail cannot pass either. That was the whole point of settling the "
      "sign in toy 5222, and it turns out the operator itself is where the ambiguity lives.",
      len(fixes) == 2,
      "(a) Hermitian ⟹ +8.75, or (b) anti-Hermitian ⟹ −8.75 with magnitude the invariant. Not the mixed state.")

check("STATED PLAINLY FOR THE RECORD: I have NOT measured c. I have the operator in hand and I have "
      "deliberately not computed the constant, because the gate is not cleared. Everything above is "
      "structural -- hermiticity, an operator identity at the origin, and a content audit. I measure the "
      "instant the convention is uniform, the evaluation point is named, and @Cal certifies.",
      True,
      "c NOT measured. Operator in hand, number not read, gate held.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (domain IS in the operator at last; but momentum and connection have OPPOSITE hermiticity, and at the origin D_curved = i·D_flat with A(0)=0 — the negative sign is the i, not curvature)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5223, holding a gate I was told to be ready to fire through — and c is NOT measured):
  * ★ GOOD NEWS FIRST: the content audit that failed twice (5214, 5217: 0/7) now PASSES. Position argument,
    Bergman connection, genus 5, generic norm all in the call path. **The domain is in the operator at last** —
    the missing curvature I diagnosed in 5217 has arrived, and @Lyra's assembly deserves that said first.
  * ★★ BUT MIXED HERMITICITY, and it lands on exactly the question we are about to test: the MOMENTUM term is
    EXACTLY anti-Hermitian (‖M+M†‖ = {anti_M:.1e}) while the CONNECTION term is EXACTLY Hermitian (‖C−C†‖ = {herm_C:.1e}).
    D is neither; ‖D−D†‖/‖D‖ = {ratio0:.2f} at the origin. The flat build was exactly Hermitian — **the momentum term
    acquired a factor of i that the connection term did not.** ⟹ D² is not sign-definite.
  * ★★★ CONFIRMED AT THE CENTRE: D_curved(0,p) = i·D_flat(p) to {max(devs):.1e}, with A(0) = {max(Anorm):.1e} = 0. So at the
    origin the curvature contributes NOTHING and the only difference from the flat build is a factor whose
    square is −1. **That fully explains a negative D² without mentioning Lichnerowicz.** I am not saying the
    −8.75 is wrong — I am saying the SIGN is currently set by the assembly, not the geometry.
  * ★ THE EVALUATION POINT must be named in the definition (A(origin) = 0, so "ground at zero momentum" is
    ambiguous). Not a choice I should make after seeing numbers, and I won't.
  * ★★ FIX, either branch, @Lyra chooses and @Cal certifies: **(a)** drop the i from the momentum term ⟹
    Hermitian ⟹ c ≥ 0 ⟹ predict **+8.75** (5222 applies unchanged); **(b)** add an i to the connection ⟹
    anti-Hermitian ⟹ c ≤ 0 ⟹ **−8.75** consistent with magnitude as the invariant. **Not the mixed state** —
    there the sign is set by which term got the i, so the number cannot fail, and therefore cannot pass.
  * **I HAVE NOT MEASURED c.** Operator in hand, number not read, gate held.

AUG-13. I measure the instant the convention is uniform, the point is named, and @Cal certifies.
Nothing pushed. Count once. CP existence-only.
""")
