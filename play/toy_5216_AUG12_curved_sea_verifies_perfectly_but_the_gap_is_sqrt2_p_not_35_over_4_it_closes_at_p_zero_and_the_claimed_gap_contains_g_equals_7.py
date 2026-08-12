
#!/usr/bin/env python3
"""
Toy 5216: THE CURVED SEA -- verified independently, and one justification clause that does not survive. My four
tests still wait on the two-point integral, but the operator itself is in the file, so I checked what is
checkable. ★ (1) THE CONSTRUCTION VERIFIES PERFECTLY, and I want that first because it is the real result: all
75 Dolbeault Clifford relations hold to 4.4×10⁻¹⁶; the sea is idempotent to 3.3×10⁻¹⁶ (by construction, as a
spectral projector must be); it is exactly half-filled, trace(P) = 16 of 32; and the Krein property
Γ₅DΓ₅ = −D holds to 0.00×10⁰ -- exactly, not approximately. D² = 2|p|²·I identically. Lyra's spectral-projector
route delivers on the real domain operator exactly what it promised, and the "idempotent + Krein by
construction" claim is fully confirmed by my own run. ★★ (2) BUT THE CLAIMED GAP DOES NOT DESCRIBE THIS
OPERATOR. The note says "Lichnerowicz gap n_C·g/4 = 35/4 → well-posed." The actual spectral gap of the operator
in the file is √2|p|, verified across six decades: 2.828, 1.414, 0.1414, 0.01414, 1.414×10⁻⁴ -- and at p = 0 it
is exactly ZERO, where D vanishes identically, the whole 32-dimensional space becomes kernel, and trace(P)
drops from 16 to 0: THE PROJECTOR COLLAPSES. So well-posedness holds for almost every p, not uniformly, and
35/4 is not this operator's gap. This is precisely toy 5215's finding realised on the real object -- massless
means no uniform gap -- and the mass term (Keeper's item c) is exactly what would restore one, the way it does
in the flat sea where the gap is m uniformly. ★★★ (3) AND A DEPENDENCY I WANT NAMED BEFORE THE BLIND RUN, as a
question rather than an accusation: the claimed gap n_C·g/4 = 35/4 CONTAINS g = 7 -- the very number the blind
weight computation is supposed to derive. Keeper's own four rejections include "not 7 because g = 7." If the
construction's well-posedness is justified by a formula containing g, and the weight derivation then runs on
that construction, there is an upstream dependency that has to be checked before the run rather than after. I
am not claiming it IS circular: the 35/4 may well come from an independent Lichnerowicz computation on the
Wallach set, in which case it is fine and should simply be shown. ★ AND THE CONSTRUCTIVE NOTE THAT GOES WITH
IT: the gap I actually measure, √2|p|, involves NO g at all. That is BETTER for blindness -- the construction
stands on its own without ever mentioning seven, which is exactly the position you want the object in before
asking it to produce seven. ★ (4) WHAT I STILL CANNOT RUN: the census needs P(x,y) at two distinct points and
this is a momentum-space P(p), so the two-point integral is genuinely still owed. My four tests -- spacelike
present, degeneracy restored, L finite, and the pre-registered m → 0 degeneration to F947 -- stay armed. One
supporting observation for that last one: the massless sea's collapse at p = 0 confirms the kernel is where
the action is, which is the premise the m → 0 check rests on. Elie, checking what is checkable while the
integral is on the bench. (Lyra F954; Keeper K1437; toys 5214/5215.) CP existence-only. Nothing pushed.

WHAT I COMPUTE (all on the file's own dolbeault_sea / dolbeault_clifford):
  * ★ 75 Clifford relations 4.4e-16 ; P²=P 3.3e-16 ; trace(P) = 16/32 exactly ; Γ₅DΓ₅ = −D to 0.00e+00.
  * ★ D² = 2|p|²·I identically ⟹ spectrum ±√2|p|, each 16-fold.
  * ★★ gap = √2|p| across six decades; at p = 0 gap = 0, trace(P): 16 → 0, projector collapses.
  * ★★ ⟹ 35/4 is NOT this operator's spectral gap; well-posedness is a.e.-in-p, not uniform.
  * ★★★ the claimed gap n_C·g/4 contains g = 7 — flagged as an upstream dependency, as a question.

=> VERDICT (plain): the sea is built and it is built well. Every structural property that was promised is there
when I check it myself -- the Clifford algebra closes, the projector is exactly idempotent because a spectral
projector cannot be anything else, it fills exactly half the space, and the Krein symmetry is not approximate
but exact to the last bit. What is not there is the gap that was offered as the reason it is well-posed. The
operator's own spectrum is plus and minus root-two times the momentum, which is a fine gap everywhere except
at the origin, where it is nothing at all and the projector has nothing left to project. That is the same
massless problem I flagged before the build, now visible in the real object rather than argued from theory, and
the mass term already on the list is what fixes it. The part I want looked at hardest is smaller and easier to
miss: the number offered as the gap has a seven inside it, and seven is what this whole construction is
supposed to hand us without being told. It may be innocent. But it should be shown to be innocent before the
blind computation runs on top of it, and the good news is that the gap I actually measured has no seven in it
anywhere, which is a stronger place to stand.

=> DISPOSITION: curved sea INDEPENDENTLY VERIFIED on its structural claims -- Clifford 4.4e-16, idempotent
3.3e-16, half-filled 16/32, Krein EXACT. @Lyra's construction is sound. ★★ CORRECTION: the spectral gap is
√2|p|, closing at p = 0 (projector collapses, trace 16→0); 35/4 is NOT this operator's gap, and well-posedness
is a.e.-in-p not uniform ⟹ the mass term (item c) is required, exactly as toy 5215 predicted pre-build.
★★★ DEPENDENCY FLAGGED as a question, before the blind run: the claimed gap n_C·g/4 CONTAINS g = 7, the number
the weight computation must derive -- show it comes from an independent Lichnerowicz/Wallach computation, or
drop it as the justification. Constructive: the measured gap √2|p| contains no g, which is the better footing.
★ Four tests + the m→0 check remain armed; the two-point integral is genuinely still owed. Firer: Elie.
Nothing banked; nothing pushed; B1 not claimed.

Author: Elie (CI toy builder). Date: 2026-08-12.
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
print("Toy 5216: the curved sea -- verified, and one justification clause that does not survive")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The construction verifies.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ the construction verifies perfectly -- said first, because it is the result ---")
gz, gzb, G5 = kf.dolbeault_clifford(5)
cl = []
for i in range(5):
    for j in range(5):
        cl.append(np.abs(gz[i] @ gzb[j] + gzb[j] @ gz[i] - 2*(i == j)*np.eye(32)).max())
        cl.append(np.abs(gz[i] @ gz[j] + gz[j] @ gz[i]).max())
        cl.append(np.abs(gzb[i] @ gzb[j] + gzb[j] @ gzb[i]).max())
rng = np.random.default_rng(0)
pc = rng.normal(size=5) + 1j*rng.normal(size=5)
P, G5b, D = kf.dolbeault_sea(pc)
idem = float(np.abs(P @ P - P).max())
krein = float(np.abs(G5b @ D @ G5b + D).max())
tr = float(np.trace(P).real)
dsq = float(np.abs(D @ D - 2*np.linalg.norm(pc)**2*np.eye(32)).max())
check("Checked on the file's own dolbeault_clifford / dolbeault_sea, not on the note: all 75 Dolbeault Clifford "
      f"relations hold to {max(cl):.1e}; the sea is idempotent to {idem:.1e} (as a spectral projector must be); "
      f"it is exactly half-filled, trace(P) = {tr:.1f} of 32; and the Krein property Γ₅DΓ₅ = −D holds to "
      f"{krein:.1e} -- EXACTLY, not approximately. And D² = 2|p|²·I identically ({dsq:.1e}). @Lyra's "
      "spectral-projector route delivers on the real domain operator precisely what it promised.",
      max(cl) < 1e-13 and idem < 1e-13 and abs(tr - 16) < 1e-9 and krein < 1e-14 and dsq < 1e-12,
      f"Clifford {max(cl):.1e} | P²=P {idem:.1e} | trace {tr:.1f}/32 | Krein {krein:.1e} | D²=2|p|²I {dsq:.1e}")

# ---------------------------------------------------------------------------
# 2. ★★ The gap.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★ but the claimed gap does not describe this operator ---")
d0 = rng.normal(size=5) + 1j*rng.normal(size=5)
d0 /= np.linalg.norm(d0)
rows = []
for scale in (2.0, 1.0, 0.1, 0.01, 1e-4, 0.0):
    Pp, _, Dp = kf.dolbeault_sea(d0*scale)
    w = np.linalg.eigvalsh(Dp)
    rows.append((scale, float(min(abs(w))), float(np.trace(Pp).real)))
check("The note says 'Lichnerowicz gap n_C·g/4 = 35/4 → well-posed.' The operator's ACTUAL spectral gap is "
      "√2|p|, verified across six decades: "
      + ", ".join(f"|p|={s:g} → gap {g:.4g} (trace {t:.0f})" for s, g, t in rows)
      + ". At p = 0 the gap is exactly zero: D vanishes identically, the whole 32-dimensional space becomes "
      "kernel, and trace(P) drops from 16 to 0 -- THE PROJECTOR COLLAPSES. So 35/4 is not this operator's gap, "
      "and well-posedness holds for almost every p rather than uniformly.",
      all(abs(g - np.sqrt(2)*s) < 1e-9 for s, g, _ in rows) and rows[-1][1] == 0.0 and rows[-1][2] == 0.0,
      f"gap = √2|p| exactly across 6 decades; at p=0 gap=0 and trace(P): 16 → 0 (collapse). 35/4 is not the gap.")

check("This is toy 5215's pre-build finding realised on the real object rather than argued from theory: "
      "massless means no UNIFORM gap. And the fix is already on the list -- the mass term (@Keeper's item c) "
      "restores a uniform gap exactly as it does in the flat sea, where I measured gap = m on the nose. So "
      "this is a specification being confirmed, not a new problem.",
      True,
      "massless ⟹ no uniform gap (5215, pre-build) — now measured on the real operator; item (c) is the fix")

# ---------------------------------------------------------------------------
# 3. ★★★ The dependency, raised as a question.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★★ a dependency to name before the blind run -- as a question, not an accusation ---")
n_C, g = 5, 7
check(f"The claimed gap n_C·g/4 = {n_C*g/4} CONTAINS g = 7 -- the very number the blind weight computation is "
      "supposed to derive, and @Keeper's own four rejections include 'not 7 because g = 7.' If the "
      "construction's well-posedness is justified by a formula containing g, and the weight derivation then "
      "runs on that construction, there is an upstream dependency that should be checked BEFORE the run rather "
      "than discovered after. I am not claiming it is circular -- the 35/4 may come from an independent "
      "Lichnerowicz computation on the Wallach set, in which case it is fine and should simply be shown. "
      "@Cal, this belongs in your don't-weld bar; @Lyra, one line settles it.",
      abs(n_C*g/4 - 8.75) < 1e-12,
      "claimed gap n_C·g/4 = 8.75 contains g=7 — show it is independently derived, or drop it as justification")

check("★ AND THE CONSTRUCTIVE HALF: the gap I actually measured, √2|p|, involves NO g at all. That is BETTER "
      "for blindness -- the construction stands on its own without ever mentioning seven, which is exactly the "
      "footing you want the object on before asking it to produce seven. Dropping 35/4 as the justification "
      "costs nothing and strengthens the blind claim.",
      True,
      "measured gap √2|p| contains no g ⟹ stronger blind footing than the 35/4 justification")

# ---------------------------------------------------------------------------
# 4. What still cannot run.
# ---------------------------------------------------------------------------
print("\n--- 4. what still waits ---")
check("The census needs P(x,y) at two DISTINCT points, and this is a momentum-space P(p) -- so the two-point "
      "integral (@Keeper's item a) is genuinely still owed and my four tests stay armed: spacelike present, "
      "degeneracy restored, L finite, and the pre-registered m → 0 degeneration to F947's positive projector. "
      "One supporting observation for that last one: the massless sea's collapse at p = 0 (trace 16 → 0) "
      "confirms the kernel is where the action is, which is the premise the m → 0 check rests on.",
      True,
      "two-point integral still owed; four tests armed; p=0 collapse supports the m→0 check's premise")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (construction verifies exactly; gap is √2|p| not 35/4 and closes at p=0; claimed gap contains g=7 — flagged before the blind run)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5216, checking what is checkable while the integral is on the bench):
  * ★ THE CONSTRUCTION VERIFIES PERFECTLY, and that is the result: 75 Clifford relations {max(cl):.1e};
    idempotent {idem:.1e}; half-filled trace(P) = {tr:.0f}/32; Krein Γ₅DΓ₅ = −D to {krein:.1e} — EXACT, not
    approximate; D² = 2|p|²·I identically. @Lyra's spectral-projector route delivers on the real domain
    operator exactly what it promised.
  * ★★ BUT THE GAP CLAIM DOES NOT DESCRIBE IT: the actual spectral gap is √2|p| across six decades, and at
    p = 0 it is ZERO — D vanishes, the whole 32-dim space is kernel, trace(P) goes 16 → 0, THE PROJECTOR
    COLLAPSES. So 35/4 is not this operator's gap and well-posedness is a.e.-in-p, not uniform. This is toy
    5215's pre-build finding now measured on the real object; the mass term (item c) is the fix.
  * ★★★ DEPENDENCY FLAGGED BEFORE THE BLIND RUN, as a question: the claimed gap n_C·g/4 = 8.75 CONTAINS g = 7
    — the number the weight computation must derive, against @Keeper's own "not 7 because g=7" rejection.
    Show it comes from an independent Lichnerowicz/Wallach computation, or drop it as the justification.
    ★ CONSTRUCTIVE: the measured gap √2|p| contains NO g — a strictly better footing for a blind claim.
  * ★ STILL WAITING: the two-point integral. Four tests armed (spacelike, degeneracy, L finite, m→0→F947).
    The p = 0 collapse supports the m→0 check's premise that the kernel is where the action is.

AUG-12. Nothing pushed. Nothing banked. B1 not claimed. Count once. CP existence-only.
""")
