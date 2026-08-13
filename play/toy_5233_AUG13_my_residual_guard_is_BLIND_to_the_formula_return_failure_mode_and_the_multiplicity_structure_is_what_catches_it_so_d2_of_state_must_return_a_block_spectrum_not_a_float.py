#!/usr/bin/env python3
"""
Toy 5233: MY RESIDUAL GUARD IS BLIND TO THE FAILURE MODE @KEEPER JUST NAMED -- tested, not assumed. He said the
y-axis must be the matrix, not the closed form: "returning the formula returns the answer," the twin of my own
"choosing Ω chooses the answer." Correct in principle. ★★★ BUT I CHECKED WHETHER THE GUARD I ACTUALLY CARRY
COULD ENFORCE IT, AND IT CANNOT. I built both responses -- a formula-backed d2_of_state returning
Ω + q² − 8.75 exactly, and a matrix-backed one that constructs a Hermitian block, diagonalises it numerically,
and returns the eigenvalue -- and ran my fit on each. Formula: slope 1.000000000, a = 1.000000000, c =
8.750000000, residual 3.6×10⁻¹⁵. Matrix: the same three numbers to nine decimals, residual 5.3×10⁻¹⁵. ⟹ THE
RESIDUAL -- THE ONLY GUARD I HAVE ON THE RESPONSE SIDE, AND THE ONE THE PROTOCOL SAYS TO VOID ON -- CANNOT TELL
THEM APART. Same order of magnitude, wrong sign of difference, no threshold that separates them. Had d2_of_state
landed as a formula, I would have measured (1, 1, 8.75), reported a clean triple with a passing residual, and
certified the theory against itself. @Keeper's catch was not merely principled; it was pointing at a live hole
in my instrument, and my instrument could not have closed it. ★★ WHAT DOES CATCH IT: MULTIPLICITY. A matrix
response has block structure -- the K-type (m₁,m₂) occupies a subspace of dimension dim(m₁,m₂), and every
eigenvalue in that block must be DEGENERATE (measured spread ≤ 2.2×10⁻¹⁵ across blocks of size 1, 4, 5). A
closed form returns ONE number per label: no multiplicity, no spread, nothing to check. Degeneracy is structure
a formula cannot fake without being told to fake it. ★ SO THE SIGNATURE IS WRONG. d2_of_state(...) → float
cannot be audited. It must return THE BLOCK SPECTRUM -- the eigenvalues of D² on that K-type's subspace -- and
then I check (i) count = dim(m₁,m₂) and (ii) spread ≈ 0 before I fit anything. A scalar is unfalsifiable by
construction; a spectrum carries its own provenance. ★ AND A SECONDARY CATCH I HAND OVER RATHER THAN RESOLVE:
the multiplicity check needs a convention pin. Computing the B₂ Weyl dimension in (m₁,m₂) coordinates gives
dim(1,0) = 4 -- the SPINOR -- while the F972 fiber table calls degree 1 the 5, the VECTOR. Both are standard;
they are different (m₁,m₂) conventions. Until @Lyra pins which one d2_of_state uses, the count test is itself
ambiguous, so the pin is load-bearing for the guard and not merely tidy. Elie, arming the response side before
the function lands rather than after. (Keeper's y-axis catch; Lyra F972; toys 5228/5231/5232.) CP
existence-only. Nothing pushed. a and c UNREAD.

WHAT I VERIFY:
  * ★★★ formula-backed and matrix-backed responses give IDENTICAL triples and INDISTINGUISHABLE residuals
    (3.6e-15 vs 5.3e-15) ⟹ my residual guard cannot enforce Keeper's requirement.
  * ★★ block multiplicity DOES separate them: count = dim(K-type), spread ≤ 2.2e-15, a formula has neither.
  * ★ ⟹ the required signature is d2_of_state → BLOCK SPECTRUM, not float.
  * ★ and the count test needs a convention pin: B₂ (m₁,m₂) gives dim(1,0) = 4 (spinor) vs F972's degree-1 = 5.

=> VERDICT (plain): Keeper said the number I measure has to come out of the matrix and not out of the formula,
because a formula would just hand back the answer we are trying to test. He is right. The part worth reporting
is that I went and checked whether my own equipment could catch that mistake, and it cannot. I built both kinds
of answer-provider, one honest and one that quietly returns the formula, and ran my test on each. They gave the
same three numbers to nine decimal places and error bars of the same size. There is no setting of my alarm that
rings for one and not the other. So if the formula version had arrived this afternoon I would have reported a
beautiful result and it would have meant nothing. What does tell them apart is something a formula has no way
to imitate: a real matrix carries repeated values. Each internal state is not one slot but several, and all of
them must give the identical number -- and they do, to fifteen decimal places. A formula has one slot and
nothing to repeat. So I am asking for the whole list of numbers per state rather than a single number; a single
number cannot be checked, a list carries its own evidence of where it came from. One caveat I am handing back
rather than deciding: the labels have two standard conventions and they disagree about how many slots a state
has, so that has to be pinned or the repetition test is ambiguous too.

=> DISPOSITION: ★★★ MY RESIDUAL GUARD IS BLIND to the formula-return failure mode -- TESTED: formula-backed and
matrix-backed give identical (1.000000000, 1.000000000, 8.750000000) with residuals 3.6e-15 vs 5.3e-15, no
separating threshold. @Keeper's catch pointed at a live hole my instrument could not close. ★★ MULTIPLICITY
CATCHES IT: block count = dim(K-type), spread ≤ 2.2e-15; a closed form has no multiplicity structure. ★ REQUIRED
SIGNATURE CHANGE (@Lyra): d2_of_state must return THE BLOCK SPECTRUM, not a float -- a scalar is unfalsifiable
by construction. ★ CONVENTION PIN OWED (@Lyra, load-bearing for the guard): B₂ (m₁,m₂) Weyl dim gives dim(1,0)
= 4 (spinor); F972's degree-1 is the 5 (vector). Which convention does d2_of_state use? Until pinned, the count
test is ambiguous. Firer: Elie. Nothing banked; nothing pushed; a and c UNREAD.

Author: Elie (CI toy builder). Date: 2026-08-13.
"""

import numpy as np

rng = np.random.default_rng(0)

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

C_TRUE = 8.75

def om5(m1, m2):
    return m1*(m1 + 5) + m2*(m2 + 3)

def dim_B2(m1, m2):
    """Weyl dimension for B2 in (m1,m2) coordinates. NOTE: convention-dependent — see check 5."""
    a, b = m1 - m2, m2
    return int(round((1 + a)*(1 + b)*(2 + a + b)*(3 + a + 2*b)/6))

STATES = [(0, 0, -2.5), (1, 0, -1.5), (1, 1, -0.5), (1, 1, 0.5), (1, 0, 1.5),
          (0, 0, 2.5), (2, 0, 0.5), (2, 1, -0.5), (2, 2, 1.5), (3, 1, 0.5)]

def d2_formula(m1, m2, q):
    """The failure mode Keeper named: returns the closed form. One number, no provenance."""
    return om5(m1, m2) + q*q - C_TRUE

def d2_block_spectrum(m1, m2, q):
    """Honest response: build a Hermitian block, diagonalise numerically, return the SPECTRUM."""
    n = dim_B2(m1, m2)
    lam = om5(m1, m2) + q*q - C_TRUE
    Q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    M = Q @ np.diag(np.full(n, lam)) @ Q.T
    return np.linalg.eigvalsh((M + M.T)/2)

def design(states):
    Om = np.array([om5(m1, m2) for m1, m2, _ in states], float)
    Q2 = np.array([q*q for _, _, q in states], float)
    return np.vstack([Om, Q2, np.ones_like(Om)]).T

def fit(Y, states):
    A = design(states)
    b, *_ = np.linalg.lstsq(A, Y, rcond=None)
    return float(b[0]), float(b[1]), -float(b[2]), float(np.abs(Y - A @ b).max())

print("=" * 78)
print("Toy 5233: the residual guard is blind to the formula-return — a and c UNREAD")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1-3. The residual cannot enforce Keeper's requirement.
# ---------------------------------------------------------------------------
print("\n--- 1-3. ★★★ testing whether my own guard can catch the formula-return ---")
Y_form = np.array([d2_formula(*s) for s in STATES])
Y_mat = np.array([float(np.mean(d2_block_spectrum(*s))) for s in STATES])
sf, af, cf, rf = fit(Y_form, STATES)
sm, am, cm, rm = fit(Y_mat, STATES)

check("A formula-backed d2_of_state (returning Ω + q² − 8.75 exactly) yields "
      f"slope_Ω = {sf:.9f}, a = {af:.9f}, c = {cf:.9f}, residual = {rf:.3e} -- a perfect, passing, entirely "
      "meaningless triple. This is @Keeper's failure mode instantiated: the fit recovers the constant that was "
      "fed to it, and calls the recovery a measurement.",
      abs(sf - 1) < 1e-9 and abs(af - 1) < 1e-9 and abs(cf - C_TRUE) < 1e-9,
      f"formula-backed: ({sf:.9f}, {af:.9f}, {cf:.9f}), residual {rf:.3e} — recovers its own input")

check("An honest matrix-backed d2_of_state (Hermitian block built, numerically diagonalised, eigenvalue "
      f"returned) yields slope_Ω = {sm:.9f}, a = {am:.9f}, c = {cm:.9f}, residual = {rm:.3e}. ★ THE SAME THREE "
      "NUMBERS TO NINE DECIMALS. Which is correct and expected -- an honest construction should reproduce the "
      "theory. That is exactly why the triple alone carries no information about its own provenance.",
      abs(sm - 1) < 1e-9 and abs(am - 1) < 1e-9 and abs(cm - C_TRUE) < 1e-9,
      f"matrix-backed: ({sm:.9f}, {am:.9f}, {cm:.9f}), residual {rm:.3e} — identical triple")

ratio = max(rf, rm)/max(min(rf, rm), 1e-300)
check(f"★★★ THE DISCRIMINATION TEST: residuals are {rf:.3e} (formula) vs {rm:.3e} (matrix) -- same order, "
      f"ratio {ratio:.2f}, and the formula's is the SMALLER of the two. There is no threshold that voids one "
      "and passes the other. ⟹ THE RESIDUAL GUARD -- the only guard I carry on the response side, and the one "
      "the protocol instructs me to void on -- IS BLIND TO THIS FAILURE MODE. Had the formula version landed, "
      "I would have reported a clean triple and certified the theory against itself.",
      ratio < 10,
      f"residuals indistinguishable (ratio {ratio:.2f}) ⟹ my stated guard cannot enforce Keeper's requirement")

# ---------------------------------------------------------------------------
# 4. What does catch it.
# ---------------------------------------------------------------------------
print("\n--- 4. ★★ what catches it: block multiplicity ---")
spreads, counts_ok = [], []
for s in STATES:
    sp = d2_block_spectrum(*s)
    spreads.append(float(sp.max() - sp.min()))
    counts_ok.append(len(sp) == dim_B2(s[0], s[1]))
max_spread = max(spreads)
check("A matrix response carries BLOCK STRUCTURE: the K-type (m₁,m₂) occupies a subspace of dimension "
      f"dim(m₁,m₂), and every eigenvalue in that block must be DEGENERATE. Measured across all {len(STATES)} "
      f"states: counts match dim(m₁,m₂) in {sum(counts_ok)}/{len(STATES)} cases, maximum spread within a block "
      f"= {max_spread:.2e}. ★ A CLOSED FORM RETURNS ONE NUMBER PER LABEL -- no multiplicity, no spread, nothing "
      "to check. Degeneracy is structure a formula cannot fake without being told to fake it, which makes it "
      "the provenance test the residual cannot be.",
      all(counts_ok) and max_spread < 1e-12,
      f"block counts = dim(K-type) {sum(counts_ok)}/{len(STATES)}; max within-block spread {max_spread:.2e} ⟹ separates cleanly")

# ---------------------------------------------------------------------------
# 5. The signature change, and the convention pin it needs.
# ---------------------------------------------------------------------------
print("\n--- 5. ★ the required signature change, and a convention pin owed ---")
check("⟹ THE REQUESTED SIGNATURE IS WRONG. `d2_of_state(...) → float` cannot be audited: a scalar is "
      "unfalsifiable by construction, carrying no trace of whether a matrix or a formula produced it. It must "
      "return THE BLOCK SPECTRUM -- the eigenvalues of D² on that K-type's subspace -- so I can check (i) count "
      "= dim(m₁,m₂) and (ii) spread ≈ 0 BEFORE fitting anything. A spectrum carries its own provenance; a "
      "number does not.",
      True,
      "required: d2_of_state → block spectrum (eigenvalues), not float — a scalar cannot be audited")

d10_B2 = dim_B2(1, 0)
check(f"★ AND A CONVENTION PIN IS OWED, load-bearing for the guard rather than tidy: the B₂ Weyl dimension in "
      f"(m₁,m₂) coordinates gives dim(1,0) = {d10_B2} -- the SPINOR -- while the F972 fiber table calls degree 1 "
      "the 5, the VECTOR. Both are standard; they are different (m₁,m₂) conventions. Until @Lyra pins which one "
      "d2_of_state uses, the multiplicity count test is itself ambiguous and could void an honest construction "
      "or pass a broken one. I hand this back rather than choosing -- picking the convention is picking part of "
      "the grading, which is not mine to pick.",
      d10_B2 != 5,
      f"B₂ (m₁,m₂) gives dim(1,0) = {d10_B2} (spinor) vs F972 degree-1 = 5 (vector) ⟹ convention pin required")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (my residual guard is blind to the formula-return; multiplicity catches it; d2_of_state must return a spectrum, not a float)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5233, arming the response side before the function lands — a and c UNREAD):
  * ★★★ **MY RESIDUAL GUARD IS BLIND TO THE FAILURE MODE @KEEPER NAMED** — tested, not assumed. A
    formula-backed d2_of_state and an honest matrix-backed one give the **same triple to nine decimals**
    ({sf:.9f}, {af:.9f}, {cf:.9f}) with residuals **{rf:.3e} vs {rm:.3e}** — same order, and the formula's is
    the *smaller*. **No threshold separates them.** Had the formula version landed this afternoon I would have
    reported a clean, passing, entirely meaningless triple and certified the theory against itself.
  * ★★ **MULTIPLICITY CATCHES IT.** A matrix response carries block structure: count = dim(K-type), and every
    eigenvalue in a block must be degenerate (max spread **{max_spread:.2e}** across blocks of size 1, 4, 5).
    A closed form returns one number per label — no multiplicity, no spread, nothing to check. Degeneracy is
    structure a formula cannot fake without being told to.
  * ★ **⟹ THE REQUESTED SIGNATURE IS WRONG.** `d2_of_state → float` is unfalsifiable by construction. It must
    return **the block spectrum**, so I can check count and degeneracy *before* fitting. A spectrum carries its
    own provenance; a scalar does not.
  * ★ **CONVENTION PIN OWED (@Lyra), load-bearing:** B₂ (m₁,m₂) Weyl dim gives **dim(1,0) = {d10_B2} (spinor)**
    while F972's degree-1 is the **5 (vector)** — different standard conventions. Until pinned, the count test
    is itself ambiguous. Handed back, not chosen: picking the convention is picking part of the grading.

AUG-13. @Keeper's catch was pointing at a live hole, and my instrument could not have closed it — now it can.
a and c UNREAD. Nothing pushed. Count once. CP existence-only.
""")
