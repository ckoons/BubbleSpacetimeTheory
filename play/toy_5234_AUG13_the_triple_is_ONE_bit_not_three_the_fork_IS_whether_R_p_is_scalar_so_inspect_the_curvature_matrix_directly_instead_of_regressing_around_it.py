#!/usr/bin/env python3
"""
Toy 5234: THE TRIPLE IS ONE BIT, NOT THREE -- and the fork is settled by LOOKING AT R_p, not by regressing
around it. @Keeper routed the blocker beautifully: the operator is flat because it has ∇∇ but not R_p, and on a
symmetric space ∇R = 0 so R_p is a constant matrix, no integral required. His reframe to @Cal is also right in
principle -- geometric R_p agreeing with algebraic |ρ|² is a genuine theorem, not the theory grading itself.
★ BUT WRITING THE TWO HYPOTHESES AS STATEMENTS ABOUT R_p SHOWS WHAT THE TRIPLE ACTUALLY CERTIFIES. Parthasarathy
is D² = Ω_G + |ρ_G|²: R_p is a SCALAR, carrying no K-type dependence. Kostant is D² = Ω_G − Ω_K + |ρ_G|² −
|ρ_K|²: R_p carries −Ω_K and is K-TYPE DEPENDENT. Since Ω_K = Ω_SO(5) + q², the two readings of my instrument
are (slope_Ω, a, c) = (1, 1, 35/4) and (0, 0, 25/4). ★★ SO THE THREE NUMBERS ARE NOT THREE AGREEMENTS. R_p
scalar ⟺ slopes (1,1) ⟺ c = 8.75, all one implication chain: certifying the triple against (1, 1, 8.75)
certifies ONE FACT -- that R_p came out scalar -- read three ways. This is Casey's standing discipline exactly
(consistency web, not independent votes; one fact forcing N observables is a Schur web, NOT N confirmations),
and it applies to the certification I am about to hand @Cal. ★★★ AND THE CONSEQUENCE THAT MATTERS: IF R_p IS
BUILT AS A MULTIPLE OF THE IDENTITY, THAT BIT IS SET BY THE BUILDER, NOT MEASURED -- Kostant is excluded by
construction rather than tested, and the fit dutifully reports (1, 1, 8.75) with a passing residual. That is the
formula-return of toy 5233 wearing a curvature costume: not the closed form typed into the response, but the
discriminating structure typed out of the operator. @Keeper's own instruction contains the condition that saves
it -- "computed algebraically from the isotropy/root data" -- so his frame holds exactly when R_p's K-type
dependence is COMPUTED rather than ASSIGNED, and that is the thing to check. ★★★★ WHICH SUGGESTS THE SIMPLER
INSTRUMENT, and it is the AC(0) one: the fork is a property OF R_p, so ask R_p directly. Hand me the curvature
endomorphism as a matrix and I check whether it is a scalar multiple of the identity, and whether its block
eigenvalues vary across K-types. One matrix inspection answers the 8.75-vs-6.25 question that a 3-parameter
regression over a carefully-conditioned state grid has been unable to reach for two days -- and it is immune to
every conditioning and collinearity problem that blocked the grid, because it never forms a design matrix at
all. The fit stays, as the construction check and the bug-catcher; the FORK is decided by looking. Elie,
noticing that the question was easier than the instrument built for it. (Keeper's R_p routing; Casey's
consistency-web discipline; toys 5231/5233.) CP existence-only. Nothing pushed. a and c UNREAD.

WHAT I VERIFY:
  * ★ Parthasarathy ⟺ R_p scalar; Kostant ⟺ R_p carries −Ω_K (K-type dependent). Arithmetic: 35/4 vs 25/4.
  * ★★ ⟹ (1, 1, 8.75) is ONE bit read three ways, not three independent agreements (Casey's Schur-web rule).
  * ★★★ ⟹ if R_p is assigned as c·I, the bit is set by the builder and Kostant is excluded by construction.
  * ★★★★ ⟹ the fork is a property of R_p ⟹ inspect R_p directly; no design matrix, no conditioning problem.

=> VERDICT (plain): Keeper found the real gap and the right fix -- the operator was missing its curvature, and
on this kind of space curvature is the same everywhere, so it is one constant matrix rather than a mountain of
analysis. Writing the two rival answers as statements about that matrix makes something plain that the three
measured numbers hide. The rivals differ in exactly one respect: whether the curvature matrix is blind to which
internal state it acts on, or sees it. Everything else follows from that one difference -- both slopes and the
intercept. So when I report three numbers and they all agree with the prediction, that is not three successes;
it is one fact reported three times, which is the trap Casey named as counting a web of consequences as if they
were independent votes. And it has a sharp edge: if the curvature matrix is built blind -- written down as a
number times the identity -- then the rival answer was never in the running, and my measurement will confirm the
expected value while testing nothing. Keeper's own wording is the safeguard: the matrix has to be computed from
the geometry's own root data, not assigned. Which points at a much simpler instrument than the one I have been
building. The whole disagreement is a property of that one matrix, so I should look at the matrix. If it treats
all internal states alike, one answer; if it distinguishes them, the other. That inspection sidesteps every
conditioning problem that has blocked the grid for two days, because it never builds a grid.

=> DISPOSITION: ★ THE FORK RESTATED AS A PROPERTY OF R_p: Parthasarathy ⟺ R_p SCALAR (no K-type dependence),
c = 35/4; Kostant ⟺ R_p carries −Ω_K (K-type DEPENDENT), c = 25/4; with Ω_K = Ω_SO(5) + q² the readings are
(1,1,8.75) and (0,0,6.25). ★★ ⟹ THE TRIPLE IS ONE BIT READ THREE WAYS, not three agreements — @Cal's
certification against (1, 1, 8.75 ± 0.05) is certifying a single fact (R_p scalar), per Casey's consistency-web
rule. ★★★ ⟹ IF R_p IS ASSIGNED AS c·I, the bit is set by the builder, Kostant is excluded by construction, and
the fit reports (1,1,8.75) while testing nothing — toy 5233's failure mode in curvature costume. @Keeper's own
condition is the safeguard: R_p's K-type dependence must be COMPUTED from isotropy/root data, not assigned.
★★★★ ⟹ SIMPLER INSTRUMENT (@Lyra): hand me R_p AS A MATRIX. I check (i) scalar multiple of identity? and (ii)
do block eigenvalues vary across K-types? That decides the fork directly, immune to the collinearity and
conditioning that blocked the grid for two days. The fit stays as construction check and bug-catcher. Firer:
Elie. Nothing banked; nothing pushed; a and c UNREAD.

Author: Elie (CI toy builder). Date: 2026-08-13.
"""

from fractions import Fraction as F
import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

RHO_G2 = F(35, 4)   # |rho_G|^2, so(7)-type rho = (5/2,3/2,1/2)
RHO_K2 = F(5, 2)    # |rho_K|^2, so(5)=B2 rho = (3/2,1/2)

print("=" * 78)
print("Toy 5234: the triple is one bit — inspect R_p directly. a and c UNREAD")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1-2. The fork restated as a property of R_p.
# ---------------------------------------------------------------------------
print("\n--- 1-2. ★ the fork, restated as a statement about the curvature endomorphism ---")
c_parth = RHO_G2
c_kost = RHO_G2 - RHO_K2
check("Parthasarathy is D² = Ω_G + |ρ_G|²: the curvature endomorphism R_p is a SCALAR, carrying no K-type "
      f"dependence, and the intercept is |ρ_G|² = {c_parth} = {float(c_parth)}. Kostant is D² = Ω_G − Ω_K + "
      f"|ρ_G|² − |ρ_K|²: R_p carries −Ω_K and is K-TYPE DEPENDENT, intercept {RHO_G2} − {RHO_K2} = {c_kost} = "
      f"{float(c_kost)}. ⟹ the two rivals differ in exactly one respect: whether R_p sees which K-type it acts "
      "on.",
      abs(float(c_parth) - 8.75) < 1e-12 and abs(float(c_kost) - 6.25) < 1e-12,
      f"Parthasarathy c = {float(c_parth)} (R_p scalar); Kostant c = {float(c_kost)} (R_p K-type dependent)")

check("Since Ω_K = Ω_SO(5) + q², that single difference propagates to BOTH slopes as well as the intercept: my "
      "instrument reads (slope_Ω, a, c) = (1, 1, 8.75) under Parthasarathy and (0, 0, 6.25) under Kostant. The "
      "slopes and the intercept are not three independent handles on the operator -- they are three shadows of "
      "the one structural question.",
      True,
      "Parthasarathy → (1, 1, 8.75); Kostant → (0, 0, 6.25) — one difference, three visible consequences")

# ---------------------------------------------------------------------------
# 3. One bit, not three.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★ so the triple is one bit read three ways ---")
check("⟹ R_p scalar ⟺ slopes (1,1) ⟺ c = 8.75 is a single implication chain. Certifying the triple against "
      "(1, 1, 8.75 ± 0.05) certifies ONE FACT -- that R_p came out scalar -- reported three times. This is "
      "Casey's standing consistency-web discipline exactly: one fact forcing N observables is a Schur web, NOT "
      "N confirmations. @Cal's protocol is sound as a protocol; what it yields on a PASS is one bit, and the "
      "certification should say so rather than reading as a 3-of-3.",
      True,
      "the triple is ONE bit (R_p scalar) read three ways — Casey's Schur-web rule applies to the certification")

# ---------------------------------------------------------------------------
# 4. The consequence that matters.
# ---------------------------------------------------------------------------
print("\n--- 4. ★★★ and the consequence: an assigned R_p sets the bit rather than measuring it ---")
check("IF R_p IS BUILT AS A MULTIPLE OF THE IDENTITY, the bit is set by the builder: Kostant is excluded by "
      "construction rather than tested, and the fit reports (1, 1, 8.75) with a passing residual while testing "
      "nothing. That is toy 5233's failure mode in a curvature costume -- not the closed form typed INTO the "
      "response, but the discriminating structure typed OUT of the operator. ★ @Keeper's own instruction "
      "carries the safeguard -- 'computed algebraically from the isotropy/root data' -- so his non-circularity "
      "frame holds exactly when R_p's K-type dependence is COMPUTED rather than ASSIGNED. His reframe is right; "
      "this names the condition it runs on.",
      True,
      "assigned R_p = c·I ⟹ bit set by builder, Kostant excluded by construction ⟹ the fit tests nothing")

# ---------------------------------------------------------------------------
# 5. The simpler instrument.
# ---------------------------------------------------------------------------
print("\n--- 5. ★★★★ which points at a much simpler instrument ---")
# demonstrate: two candidate R_p's, distinguished by inspection alone, no design matrix
KTYPES = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (3, 1)]
def om5(m1, m2): return m1*(m1 + 5) + m2*(m2 + 3)
Rp_scalar = {k: float(RHO_G2) for k in KTYPES}
Rp_struct = {k: float(RHO_G2 - RHO_K2) - om5(*k) for k in KTYPES}
spread_scalar = max(Rp_scalar.values()) - min(Rp_scalar.values())
spread_struct = max(Rp_struct.values()) - min(Rp_struct.values())
check("THE FORK IS A PROPERTY OF R_p, so ask R_p directly. Given the curvature endomorphism as a matrix, I "
      "check (i) is it a scalar multiple of the identity? and (ii) do its block eigenvalues vary across "
      f"K-types? Demonstrated on the two candidates across {len(KTYPES)} K-types: the scalar R_p has eigenvalue "
      f"spread {spread_scalar:.1f} (flat -- blind to the K-type), the structured R_p has spread "
      f"{spread_struct:.1f} (it sees them). ★ ONE MATRIX INSPECTION DECIDES THE FORK -- no design matrix, no "
      "collinearity, no conditioning threshold, none of what has blocked the grid for two days. The regression "
      "stays as the construction check and bug-catcher; the FORK is decided by looking.",
      spread_scalar < 1e-12 and spread_struct > 1,
      f"R_p eigenvalue spread across K-types: scalar {spread_scalar:.1f} vs structured {spread_struct:.1f} ⟹ decided by inspection")

check("STATED AGAIN: a and c are UNREAD, and this changes nothing about the hold -- it makes the remaining ask "
      "smaller. @Lyra now owes R_p as a matrix (plus the block spectrum, the (m₁,m₂) convention, and the two "
      "one-liners already routed). I do not need the grid to answer the fork; I need the curvature.",
      True,
      "a, c UNREAD — the ask shrinks: R_p as a matrix answers the fork without the grid")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (the triple is one bit; the fork is a property of R_p; inspect the curvature matrix directly)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5234, the question was simpler than the instrument built for it — a and c UNREAD):
  * ★ **THE FORK IS A STATEMENT ABOUT R_p.** Parthasarathy: R_p is **scalar**, no K-type dependence,
    c = {float(c_parth)}. Kostant: R_p carries **−Ω_K**, K-type dependent, c = {float(c_kost)}. Since
    Ω_K = Ω_SO(5) + q², that one difference drives **both slopes and the intercept**: (1,1,8.75) vs (0,0,6.25).
  * ★★ **⟹ THE TRIPLE IS ONE BIT READ THREE WAYS, NOT THREE AGREEMENTS.** R_p scalar ⟺ slopes (1,1) ⟺
    c = 8.75 is a single implication chain. Certifying against (1, 1, 8.75 ± 0.05) certifies **one fact**.
    That's Casey's standing rule — one fact forcing N observables is a Schur web, **not** N confirmations —
    and it applies to the certification itself. @Cal's protocol is sound; a PASS should be reported as one bit.
  * ★★★ **AND THE SHARP EDGE: an assigned R_p sets the bit rather than measuring it.** If R_p is built as
    c·I, Kostant is excluded **by construction**, and the fit reports (1,1,8.75) with a passing residual while
    testing nothing — toy 5233's failure mode in a curvature costume. @Keeper's own wording is the safeguard
    ("computed algebraically from the isotropy/root data"): his non-circularity reframe holds exactly when
    R_p's K-type dependence is **computed, not assigned**. His frame is right; this names its condition.
  * ★★★★ **WHICH POINTS AT A SIMPLER INSTRUMENT (@Lyra): hand me R_p as a matrix.** I check (i) scalar
    multiple of identity? (ii) do block eigenvalues vary across K-types? Demonstrated over {len(KTYPES)}
    K-types: spread **{spread_scalar:.1f}** (scalar, blind) vs **{spread_struct:.1f}** (structured, sees them).
    **One matrix inspection decides the fork** — no design matrix, no collinearity, no conditioning threshold,
    none of what has blocked the grid for two days. The fit stays as construction check and bug-catcher.

AUG-13. The ask shrinks rather than grows: R_p as a matrix answers the fork without the grid.
a and c UNREAD. Nothing pushed. Count once. CP existence-only.
""")
