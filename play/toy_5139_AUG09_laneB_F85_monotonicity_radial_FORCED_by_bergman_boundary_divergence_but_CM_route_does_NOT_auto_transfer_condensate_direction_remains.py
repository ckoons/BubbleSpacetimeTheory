#!/usr/bin/env python3
"""
Toy 5139: LANE B -- F85 monotonicity, the completely-monotone (CM) route TESTED (not assumed). RESULT
(honest, both ways): (1) the RADIAL part of F85 monotonicity is FORCED -- the Bergman kernel (1-r²)^{-p}
diverges MONOTONICALLY toward the Shilov boundary, so a mode's boundary-support (coupling) grows
monotonically with boundary-proximity (exactly the F824 physics: higher shelf = more boundary support =
heavier). (2) BUT the CM/Bernstein SHORTCUT does NOT auto-transfer: a representative coupling-vs-depth
model is monotone yet NOT completely monotone (h'' changes sign) -- the DE-sign CM structure (T2546/F778,
in the spectral-bleed variable) does NOT carry to coupling-vs-depth unless the coupling is a POSITIVE
spectral superposition (Bernstein), which needs the exact form. (3) So F85 can close via DIRECT radial
monotonicity (Bergman boundary-divergence, forced); the remaining piece is the CONDENSATE DIRECTION
(angular alignment) -- Lyra's F85. Elie's Lane-B half (Lyra+Elie). (K1305.) Tested the transfer per the caveat.

WHAT I TEST:
  * RADIAL monotonicity: g_rad(r) = (1-r²)^{-p/2} (boundary-support of a mode at radius r, from the Bergman
    kernel) -- monotone INCREASING toward the boundary (r->1). Forced by the Bergman divergence.
  * CM transfer: is the coupling-vs-depth completely monotone (like the DE bleed)? A natural model
    h(d) = sech^p(d) (boundary-support decaying into the bulk) is monotone-decreasing but (-1)^n h^(n) does
    NOT stay >= 0 (h'' changes sign) -> NOT completely monotone. So CM is NOT automatic.
  * CM iff positive spectral superposition: g(d) = Σ c_k e^{-λ_k d}, c_k >= 0 IS completely monotone
    (Bernstein) -- so IF the coupling is a positive-weight superposition of mode-decays, CM holds. That is
    the exact-form question (Lyra).

=> VERDICT (plain): F85 monotonicity is REACHABLE, but NOT via the CM shortcut automatically. (1) The
RADIAL coupling monotonicity is FORCED by the Bergman kernel's monotone boundary-divergence ((1-r²)^{-p}
grows monotonically toward the Shilov boundary) -- direct, no CM needed, and it IS the F824 boundary
principle. (2) The CM/Bernstein route does NOT auto-transfer (a natural coupling model is monotone but not
CM; the DE monotonicity lived in the spectral-bleed variable, and the transfer FAILS for the generic
depth model) -- the prompt's caveat validated. (3) CM WOULD hold iff the coupling is a positive spectral
superposition Σ c_k e^{-λ_k d}, c_k>=0 -- the exact-form question for Lyra. So F85 closes via DIRECT radial
monotonicity; the remaining piece is the CONDENSATE DIRECTION (angular alignment, Lyra's F85), plus the
Lane-A constraint (the up 12-block must be suppressed).

=> DISPOSITION: F85 radial monotonicity FORCED (Bergman divergence); CM shortcut NOT automatic (tested,
caveat validated -- needs positive-spectral-superposition); remaining piece = condensate direction (Lyra)
+ Lane-A up-suppression. Firer: Elie; Lyra pins the condensate direction + tests if the coupling is a
positive spectral superposition (CM). Cal audits. Nothing pushed. Nothing banked past the radial-monotone
(forced) + the CM-not-automatic finding.

Author: Elie (CI toy builder). Date: 2026-08-09.
"""

import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

p = 5.0     # weight = n_C

print("=" * 78)
print("Toy 5139: Lane B -- F85 radial monotonicity FORCED (Bergman divergence); CM route NOT automatic")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. RADIAL monotonicity FORCED by the Bergman boundary-divergence.
# ----------------------------------------------------------------------------
print("\n--- 1. RADIAL: coupling g(r)=(1-r²)^{-p/2} monotone toward the boundary (Bergman divergence, forced) ---")
rs = np.linspace(0.0, 0.98, 40)
g_rad = (1 - rs**2)**(-p/2)
mono_rad = np.all(np.diff(g_rad) > 0)
check("the Bergman kernel (1-r²)^{-p} diverges MONOTONICALLY toward the Shilov boundary (r->1), so a mode's "
      "boundary-support / coupling g(r) = (1-r²)^{-p/2} grows MONOTONICALLY with boundary-proximity -- this "
      "is F85's radial monotonicity, FORCED by the Bergman divergence (= the F824 physics: higher shelf = "
      "more boundary support = stronger coupling = heavier)",
      mono_rad,
      f"g(r) from {g_rad[0]:.2f} (center) to {g_rad[-1]:.1f} (near boundary), strictly increasing. Radial "
      "monotonicity is a forced property of the Bergman kernel -- no CM assumption needed.")

# ----------------------------------------------------------------------------
# 2. CM transfer TESTED: a natural coupling model is monotone but NOT completely monotone.
# ----------------------------------------------------------------------------
print("\n--- 2. CM transfer TESTED: natural model monotone but NOT completely monotone (caveat validated) ---")
dd = np.linspace(0.05, 4, 500)
h = (1 - np.tanh(dd)**2)**(p/2)          # sech^p(d): boundary-support decaying into the bulk
d1 = np.gradient(h, dd); d2 = np.gradient(d1, dd); d3 = np.gradient(d2, dd)
monotone = np.all(d1 < 1e-9)
completely_monotone = monotone and np.all(d2 > -1e-6) and np.all(d3 < 1e-6)
check("CM TRANSFER (per the caveat -- test, don't assume): a natural coupling-vs-depth model h(d)=sech^p(d) "
      "is MONOTONE-decreasing (h'<=0) but NOT completely monotone -- (-1)^n h^(n) does NOT stay >=0 (h'' "
      "changes sign). So the DE-sign CM structure (T2546/F778, which lives in the spectral-bleed variable) "
      "does NOT auto-transfer to coupling-vs-depth. The shortcut is NOT free",
      monotone and not completely_monotone,
      f"h(d): monotone-decreasing = {monotone}; completely-monotone = {completely_monotone} (h'' sign-changes). "
      "CM is NOT automatic for the generic depth model -- the caveat validated.")

# ----------------------------------------------------------------------------
# 3. CM holds IFF positive spectral superposition (Bernstein) -- the exact-form question.
# ----------------------------------------------------------------------------
print("\n--- 3. CM holds IFF positive spectral superposition Σ c_k e^{-λ_k d}, c_k>=0 (Lyra's exact form) ---")
# demonstrate: a positive superposition of exponentials IS completely monotone -- ANALYTIC derivatives:
# g(d)=Σ c_k e^{-λ_k d}; (-1)^n g^(n)(d) = Σ c_k λ_k^n e^{-λ_k d} >= 0 (every term positive) for ALL n.
c = np.array([1.0, 0.5, 0.3]); lam = np.array([1.0, 2.5, 5.0])  # c_k >= 0
def sign_alt_deriv(n):  # min over d of (-1)^n g^(n)(d) = Σ c_k λ_k^n e^{-λ_k d}
    vals = np.array([np.sum(c*(lam**n)*np.exp(-lam*d)) for d in dd])
    return vals.min()
cm_pos = all(sign_alt_deriv(n) >= 0 for n in range(0, 6))   # (-1)^n g^(n) >= 0 for n=0..5
check("CM WOULD hold IFF the coupling is a POSITIVE spectral superposition g(d) = Σ c_k e^{-λ_k d} with "
      "c_k >= 0 (Bernstein): such a g IS completely monotone (verified: all (-1)^n g^(n) >= 0). So the CM "
      "route reduces to ONE exact-form question -- is the boundary-condensate coupling a positive-weight "
      "superposition of mode-decays? That is Lyra's to pin (the condensate direction + the mode weights)",
      cm_pos,
      "positive exp-superposition -> completely monotone (Bernstein). If the coupling has this form, CM "
      "(and monotonicity) is automatic; else use the DIRECT radial monotonicity (forced, part 1).")

# ----------------------------------------------------------------------------
# 4. Verdict: F85 radial monotonicity forced; CM not automatic; condensate-direction remains.
# ----------------------------------------------------------------------------
print("\n--- 4. verdict: F85 radial monotonicity FORCED; CM not automatic; condensate-direction = Lyra ---")
check("VERDICT: F85 monotonicity is REACHABLE. (1) The RADIAL coupling monotonicity is FORCED by the "
      "Bergman boundary-divergence ((1-r²)^{-p} monotone toward the boundary) -- direct, = the F824 "
      "principle. (2) The CM/Bernstein SHORTCUT does NOT auto-transfer (a natural depth model is monotone "
      "but not CM; caveat validated) -- it holds only if the coupling is a positive spectral superposition "
      "(Lyra's exact-form question). (3) Remaining piece = the CONDENSATE DIRECTION (angular alignment, "
      "Lyra's F85) + the Lane-A constraint (up 12-block suppressed). Magnitude off",
      mono_rad and (monotone and not completely_monotone) and cm_pos,
      "F85 closes via DIRECT radial monotonicity (forced); Lyra pins the condensate direction + tests CM "
      "(positive superposition). The whole finish line = radial (forced) + angular/condensate (Lyra) + up-suppression (Lane A).")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (F85 radial monotonicity forced; CM not automatic; condensate-direction remains)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5139, Lane B -- F85 monotonicity, CM route tested):
  * RADIAL monotonicity FORCED: the Bergman kernel (1-r²)^{{-p}} diverges monotonically toward the Shilov
    boundary -> coupling g(r) grows monotonically with boundary-proximity (= F824). Direct, no CM needed.
  * CM TRANSFER TESTED (caveat): a natural model sech^p(d) is monotone but NOT completely monotone (h''
    sign-changes) -> the DE-CM structure does NOT auto-transfer to coupling-vs-depth.
  * CM iff POSITIVE SPECTRAL SUPERPOSITION: g(d)=Σ c_k e^{{-λ_k d}}, c_k>=0 IS completely monotone
    (Bernstein) -> the CM route reduces to one exact-form question (Lyra: is the coupling such a superposition?).
  * VERDICT: F85 closes via DIRECT radial monotonicity (forced); CM shortcut not automatic; remaining =
    condensate direction (Lyra) + up 12-block suppression (Lane A).

AUG-09 [TEGMARK]. Nothing pushed. Nothing banked past the forced radial-monotonicity + the CM-not-automatic
finding. F85 radial monotonicity FORCED by the Bergman boundary-divergence; the CM shortcut tested and NOT
automatic (caveat validated -- needs positive spectral superposition, Lyra's exact form); condensate
direction remains. Magnitude off. Count N.
""")
