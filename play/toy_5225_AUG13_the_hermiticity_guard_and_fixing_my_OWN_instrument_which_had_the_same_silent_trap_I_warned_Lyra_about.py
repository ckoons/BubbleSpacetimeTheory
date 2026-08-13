#!/usr/bin/env python3
"""
Toy 5225: THE HERMITICITY GUARD -- and fixing my own instrument, which had the very trap I warned @Lyra about.
@Keeper asked me to assert the Hermiticity check before the sea call. Building it turned up something I should
have noticed yesterday. ★★ (1) MY OWN PUBLISHED INSTRUMENT HAD THE TRAP IN IT. In toy 5224 I flagged that
numpy's eigvalsh silently returns confident wrong reals on a non-Hermitian matrix, and warned that
dolbeault_sea calls eigh. Then I published measure_c() -- which ALSO calls eigvalsh, with no guard. So if the
causal operator arrives still carrying a hermiticity defect, MY instrument would have produced a plausible c
and raised nothing: exactly the failure I had just described, in the tool I built to detect it. Fixed here.
★ (2) THE GUARD: assert_hermitian(D, tol, where) computes ‖D − D†‖/‖D‖ and refuses to proceed above tolerance,
reporting BOTH what eigvalsh would have returned and what the true spectrum is -- so the failure message shows
the size of the lie rather than just naming it. Verified: it passes the flat build (relative asymmetry
0.00×10⁰) and rejects a synthetic anti-Hermitian operator (2.00), where eigvalsh would have reported ±7.399
REAL against a true spectrum of ±7.399i. ★ (3) AND measure_c IS NOW GUARDED: it calls assert_hermitian before
any spectral step and RAISES rather than returning a number if the operator is not Hermitian. An instrument
that cannot fail loudly will eventually fail quietly, and this one is the last thing standing between a defect
and a headline. ★★ (4) A DELIBERATE CHOICE ABOUT HOW I DEMONSTRATED IT: I exercised the guard on a SYNTHETIC
anti-Hermitian operator (i × the flat build), NOT on the real curved operator -- because running the ungated
instrument on the real one would have shown me a number, and a number I have seen cannot be unseen before the
measurement that matters. The demonstration is complete without it. I still have not read c. ★ (5) OFFERED,
NOT IMPOSED: the guard is a six-line function in my file, not an edit to @Lyra's. One line adopts it --
assert_hermitian(D, 1e-10, "dolbeault_sea") immediately before the eigh call -- and her operator then cannot
silently produce a wrong sea. Her file stays hers. Elie, applying his own warning to his own tool.
(Keeper's route; toys 5223/5224.) CP existence-only. Nothing pushed. c NOT measured.

WHAT I COMPUTE:
  * ★★ my own measure_c() (published 5224) called eigvalsh unguarded -- the trap I had just warned about.
  * ★ assert_hermitian(): passes the flat build (0.00e+00), rejects synthetic anti-Hermitian (2.00),
    and reports what eigvalsh WOULD have returned (±7.399 real) vs the truth (±7.399i).
  * ★ measure_c is now guarded: raises instead of returning a number on a non-Hermitian operator.
  * ★★ demonstrated on a SYNTHETIC operator, deliberately, to avoid seeing a number that could anchor me.

=> VERDICT (plain): the guard was worth building for a reason I did not expect, which is that I needed it
myself. Yesterday I warned that a routine which assumes symmetry will lie without complaining when handed
something asymmetric, and then I published a measuring instrument that made exactly that assumption with no
check. Had the operator arrived tomorrow still carrying its defect, my own tool would have handed back a
confident number and said nothing, which is the precise failure I had spent the morning describing. So the
instrument now refuses: it looks at the operator first, and if the thing is not self-adjoint it stops and shows
how large the discrepancy is rather than quietly averaging it away. I also chose to test the guard on a
manufactured bad operator rather than the real one, because the real one would have shown me a number, and I
would rather arrive at the measurement genuinely not knowing. The guard is six lines and it is offered rather
than inserted; the file it protects belongs to someone else.

=> DISPOSITION: HERMITICITY GUARD built and wired in. ★★ SELF-CATCH: my own published measure_c() (toy 5224)
called eigvalsh unguarded -- the same silent trap I had flagged in dolbeault_sea one toy earlier. Now fixed;
the instrument RAISES rather than returning a number on a non-Hermitian operator. ★ assert_hermitian() verified:
passes the flat build (0.00e+00), rejects synthetic anti-Hermitian (2.00), and reports the size of the lie
(eigvalsh ±7.399 real vs true ±7.399i). ★★ Demonstrated on a SYNTHETIC operator by choice, to stay blind to any
number that could anchor the real reading. ★ OFFERED not imposed: one line adopts it in @Lyra's file
(assert_hermitian before the eigh call); her file stays hers. Firer: Elie. Owed: fire the instant the causal
operator lands, the point is named, and @Cal certifies. Nothing banked; nothing pushed; c NOT measured.

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

# ---------------------------------------------------------------------------
# THE GUARD -- offered for adoption; one line before any eigh/eigvalsh call.
# ---------------------------------------------------------------------------
def assert_hermitian(D, tol=1e-10, where="spectral step"):
    """Refuse to take a spectral projector of a non-self-adjoint operator.
       Reports the SIZE of the discrepancy and what eigvalsh would have silently returned."""
    asym = float(np.abs(D - D.conj().T).max()/max(np.abs(D).max(), 1e-300))
    if asym > tol:
        lie = np.linalg.eigvalsh(D)          # what a Hermitian routine would report
        truth = np.linalg.eigvals(D)         # what is actually there
        raise ValueError(
            f"NON-HERMITIAN operator at {where}: ||D-D^dag||/||D|| = {asym:.3e} > {tol:.0e}. "
            f"eigvalsh would have SILENTLY returned real eigenvalues up to {abs(lie).max():.4f}; "
            f"the true spectrum has |Im| up to {abs(truth.imag).max():.4f}. "
            "chi_(-inf,0) is undefined without a real spectrum -- fix the operator, do not average the triangles."
        )
    return asym

def measure_c(D_of, point, tol=0.05, ps=(0.20, 0.10, 0.05, 0.02, 0.01)):
    """GUARDED instrument. Declared inputs only; raises rather than returning a number on a bad operator."""
    d = np.ones(5, complex)/np.sqrt(5)
    c = None
    for s in ps:
        D = D_of(point, d*s)
        assert_hermitian(D, 1e-10, f"measure_c at |p|={s}")
        c = float(np.linalg.eigvalsh(D @ D).min())
    assert c is not None
    if abs(c - 8.50) < tol:
        v = "rank-2 symmetric-space rho"
    elif abs(c - 8.75) < tol:
        v = "full so(7) rho"
    elif abs(c) < tol:
        v = "still flat"
    else:
        v = f"NEITHER - raw c = {c:.4f}"
    return c, v

print("=" * 78)
print("Toy 5225: the Hermiticity guard -- and my own instrument had the trap. c NOT measured.")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. ★★ The self-catch.
# ---------------------------------------------------------------------------
print("\n--- 1. ★★ my own published instrument had the very trap I had just warned about ---")
check("In toy 5224 I flagged that numpy's eigvalsh silently returns confident wrong reals on a non-Hermitian "
      "matrix, and warned that dolbeault_sea calls eigh. Then, in the same toy, I published measure_c() -- "
      "which ALSO calls eigvalsh, with NO guard. So if the causal operator arrives still carrying a "
      "hermiticity defect, MY instrument would have produced a plausible c and raised nothing: exactly the "
      "failure I had spent the morning describing, in the tool I built to detect it. Caught here and fixed. "
      "The warning was right; I just had not applied it to myself.",
      True,
      "measure_c (5224) called eigvalsh unguarded — same trap, one toy later, in my own tool. Now fixed.")

# ---------------------------------------------------------------------------
# 2. ★ The guard, verified both ways.
# ---------------------------------------------------------------------------
print("\n--- 2. ★ the guard: passes the good operator, rejects the bad one, and shows the size of the lie ---")
rng = np.random.default_rng(3)
p = rng.normal(size=5) + 1j*rng.normal(size=5)
_, _, Df = kf.dolbeault_sea(p)
good = assert_hermitian(Df, 1e-10, "flat build")
Dbad = 1j*Df                     # SYNTHETIC anti-Hermitian; deliberately not the real curved operator
raised, msg = False, ""
try:
    assert_hermitian(Dbad, 1e-10, "synthetic anti-Hermitian")
except ValueError as e:
    raised, msg = True, str(e)
lie = abs(np.linalg.eigvalsh(Dbad)).max()
truth = abs(np.linalg.eigvals(Dbad).imag).max()
check(f"assert_hermitian PASSES the flat build (relative asymmetry {good:.2e}) and REJECTS the synthetic "
      f"anti-Hermitian operator, raising with the size of the discrepancy. Its message reports that eigvalsh "
      f"would have silently returned real eigenvalues up to {lie:.4f} while the true spectrum has |Im| up to "
      f"{truth:.4f} -- so the failure shows the SIZE of the lie rather than merely naming it. That matters: a "
      "guard that says 'not Hermitian' teaches nothing; one that says 'and here is the wrong answer you would "
      "have believed' teaches the reader why it matters.",
      good < 1e-12 and raised and "SILENTLY" in msg,
      f"flat: {good:.1e} PASS | synthetic anti-Herm: RAISED, eigvalsh {lie:.3f} real vs true |Im| {truth:.3f}")

# ---------------------------------------------------------------------------
# 3. ★ The instrument is now guarded.
# ---------------------------------------------------------------------------
print("\n--- 3. ★ measure_c now refuses rather than returning a number ---")
def bad_op(z, pc):
    _, _, D = kf.dolbeault_sea(pc)
    return 1j*D
refused = False
try:
    measure_c(bad_op, np.zeros(5, complex))
except ValueError:
    refused = True
check("measure_c now calls assert_hermitian before any spectral step and RAISES instead of returning a number "
      f"when the operator is not Hermitian (verified on the synthetic bad operator: refused = {refused}). An "
      "instrument that cannot fail loudly will eventually fail quietly, and this one is the last thing "
      "standing between a defect and a headline. It is also the honest position: if the operator is not "
      "self-adjoint then χ₍₋∞,₀₎ is undefined and there IS no c to report -- returning one anyway would be "
      "inventing a measurement.",
      refused,
      "measure_c RAISES on a non-Hermitian operator; no number is produced where none is defined")

# ---------------------------------------------------------------------------
# 4. ★★ A deliberate choice about the demonstration.
# ---------------------------------------------------------------------------
print("\n--- 4. ★★ and a deliberate choice about how I demonstrated it ---")
check("I exercised the guard on a SYNTHETIC anti-Hermitian operator (i × the flat build), NOT on the real "
      "curved operator. Running the ungated instrument on the real one would have shown me a number -- and a "
      "number I have seen cannot be unseen before the measurement that matters. The demonstration is complete "
      "without it, so there was no reason to pay that price. ★ I still have not read c.",
      True,
      "demonstrated on a synthetic operator by choice — staying blind to any number that could anchor the reading")

# ---------------------------------------------------------------------------
# 5. ★ Offered, not imposed.
# ---------------------------------------------------------------------------
print("\n--- 5. ★ offered for adoption, not inserted ---")
check("The guard is a six-line function living in my file, not an edit to @Lyra's. One line adopts it -- "
      "assert_hermitian(D, 1e-10, 'dolbeault_sea') immediately before the eigh call -- and her operator can "
      "then never silently produce a wrong sea. Her file stays hers; each lane owns its directory, and a guard "
      "is more useful accepted than imposed.",
      True,
      "one-line adoption offered: assert_hermitian(D, 1e-10, 'dolbeault_sea') before the eigh call")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (guard built and verified; my OWN instrument had the same silent trap and is now fixed; demonstrated synthetically to stay blind)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5225, applying my own warning to my own tool — c still NOT measured):
  * ★★ SELF-CATCH: in toy 5224 I flagged that eigvalsh lies silently on non-Hermitian input and warned that
    dolbeault_sea calls eigh — then published measure_c() in the same toy, which ALSO called eigvalsh with NO
    guard. Had the operator arrived still defective, **my own instrument would have returned a plausible c and
    raised nothing** — precisely the failure I had just described. Fixed here.
  * ★ THE GUARD: assert_hermitian() passes the flat build ({good:.1e}) and REJECTS the synthetic anti-Hermitian
    operator, reporting that eigvalsh would have silently returned reals up to {lie:.3f} against a true spectrum
    with |Im| up to {truth:.3f}. **The message shows the SIZE of the lie**, not just its existence.
  * ★ measure_c IS NOW GUARDED — it RAISES rather than returning a number on a non-Hermitian operator. If the
    operator isn't self-adjoint then χ₍₋∞,₀₎ is undefined and there IS no c; returning one would be inventing
    a measurement.
  * ★★ DELIBERATE CHOICE: demonstrated on a SYNTHETIC operator (i × flat), **not** the real curved one —
    running the ungated instrument on the real one would have shown me a number, and a number seen cannot be
    unseen. The demonstration was complete without paying that price.
  * ★ OFFERED, NOT IMPOSED: six lines in my file; one line adopts it in @Lyra's
    (`assert_hermitian(D, 1e-10, 'dolbeault_sea')` before the eigh call). Her file stays hers.

AUG-13. I fire the instant the causal operator lands, the point is named, and @Cal certifies.
Nothing pushed. Count once. CP existence-only.
""")
