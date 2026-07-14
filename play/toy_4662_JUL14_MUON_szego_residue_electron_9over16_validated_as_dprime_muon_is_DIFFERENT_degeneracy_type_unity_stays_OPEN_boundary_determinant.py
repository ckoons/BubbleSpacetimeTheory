#!/usr/bin/env python3
"""
Toy 4662 — Jul 14 (the muon count-mover, mine; Elie+Lyra lane): the highest-value near-term item — evaluate the
muon boundary Szegő residue at ν=3/2; if it returns UNITY the muon derives forward and the strict forced-count
goes 4→5. Keeper's warning: NOT automatic (the electron carries a rational 9/16 — verify, don't assume). I pulled
the exact object from the corpus (F343/F115/F361) BEFORE computing, validated the electron reference exactly, and
found the honest answer: the muon is a DIFFERENT degeneracy type than the electron, so the validated (formal-
degree-derivative) machinery does NOT evaluate its unity — that stays the OPEN boundary-determinant computation.
Count HOLDS 4; I do NOT bank the muon at unity.

THE OBJECT (from the corpus, exact):
  * formal-degree polynomial d(ν) = (5/2−ν)(1−ν)(2−ν)(3−ν)(4−ν)  [5 noncompact roots of SO(5,2)].
  * ELECTRON: sits ON the BF zero ν=5/2 → d(5/2)=0. Its residue is the DERIVATIVE |d'(5/2)| = 9/16 =
    N_c²/rank^{n_C−1} (F343). A rational O(1) ≠ 1 — the electron residue is NOT unity (the reference that proves
    residues need not be 1).
  * MUON: at the UNITARITY BOUND ν=3/2. d(3/2) = −15/16 ≠ 0 → the muon is NOT on a formal-degree zero. Its
    degeneracy is in the BOUNDARY normalization (a Γ-pole at the unitarity bound where the mode shortens to a
    boundary/null field, F115), and its residue is a boundary partition-function DETERMINANT over dim SO(4)=6
    directions with the π¹² boundary-Szegő normalization (F343) — a DIFFERENT object from c_FK (bulk, π^{9/2}).

WHAT I VALIDATE (exact):
  (1) electron residue = |d'(5/2)| = 9/16 = N_c²/rank^{n_C−1} (reproduces F343 — the object + machinery confirmed).
  (2) muon is NOT a formal-degree zero: d(3/2) = −15/16 ≠ 0 → the electron's "derivative-at-the-zero" recipe does
      NOT transfer. This is the concrete reason unity is "verify, not assume" (different degeneracy TYPE).
  (3) forward structural ratio that DOES hold: d_τ/d_μ = d(0)/|d(3/2)| = 60/(15/16) = 64 = 2^{C_2} (exact,
      target-innocent).

WHAT STAYS OPEN (honest, not banked): the muon UNITY (Szegő residue = 1?) is the boundary partition-function
determinant at the unitarity bound — a different object from the validated formal-degree derivative, requiring the
π¹² boundary-Szegő normalization convention (NOT the bulk c_FK, per Keeper). I cannot evaluate it with the
validated machinery, so I do NOT report a unity value. The count-mover remains OPEN; strict forced-count HOLDS 4.

⟹ VERDICT: electron reference validated exactly (9/16 = |d'(5/2)| = N_c²/rank^{n_C−1}); the muon is a DIFFERENT
degeneracy type (unitarity bound, not a formal-degree zero), so unity is genuinely not automatic and the electron
recipe doesn't transfer; the muon unity is the OPEN boundary-determinant computation (π¹², dim SO(4)=6). I do NOT
bank the muon — count HOLDS 4. The forward piece that holds: d_τ/d_μ = 2^{C_2} = 64. Count ~7-8 (α RULED, identified).
"""
from sympy import Rational, symbols, diff, Abs
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

nu = symbols('nu')
d = (Rational(5,2) - nu)*(1 - nu)*(2 - nu)*(3 - nu)*(4 - nu)   # formal-degree polynomial
dp = diff(d, nu)                                                # d'(ν)

def dval(x):  return d.subs(nu, Rational(x).limit_denominator())
def dpval(x): return dp.subs(nu, Rational(x).limit_denominator())

print("=" * 96)
print("Toy 4662 — muon Szegő residue: electron 9/16 = |d'(5/2)| validated; muon is a DIFFERENT degeneracy type → unity OPEN")
print("=" * 96)

# ---- (1) VALIDATE the electron reference ------------------------------------
d_e = d.subs(nu, Rational(5,2))                 # should be 0 (electron ON the BF zero)
dprime_e = dp.subs(nu, Rational(5,2))           # the residue = derivative at the zero
res_e = abs(dprime_e)
target = Rational(N_c**2, rank**(n_C-1))        # N_c²/rank^{n_C−1} = 9/16
print(f"\n[electron]: d(5/2) = {d_e} (BF zero); residue |d'(5/2)| = {res_e} ;  N_c²/rank^(n_C−1) = {target}")
check("VALIDATE electron reference: the electron sits ON the BF zero d(5/2)=0, so its residue is the DERIVATIVE "
      "|d'(5/2)| = 9/16 = N_c²/rank^(n_C−1) (reproduces F343 exactly). Object + machinery confirmed. Note 9/16 ≠ 1 "
      "— the reference proving a degeneracy residue need NOT be unity.",
      d_e == 0 and res_e == target and target == Rational(9,16), "9/16 = |d'(5/2)| = N_c²/rank^(n_C−1); electron residue is a rational, not unity")

# ---- (2) the muon is NOT a formal-degree zero -------------------------------
d_mu = d.subs(nu, Rational(3,2))
print(f"\n[muon]: d(3/2) = {d_mu} ≠ 0  → the muon is NOT on a formal-degree zero → the electron 'derivative-at-the-zero' recipe does NOT transfer")
check("MUON IS A DIFFERENT DEGENERACY TYPE: d(3/2) = −15/16 ≠ 0 → the muon is NOT on a formal-degree zero (it's the "
      "UNITARITY BOUND, a Γ-pole in the BOUNDARY normalization, F115). So the electron's 'residue = derivative at "
      "the zero' recipe does NOT apply — the muon residue is a boundary partition-function DETERMINANT (π¹², dim "
      "SO(4)=6), a different object. THIS is why unity is 'verify, not assume' (Keeper).",
      d_mu != 0 and d_mu == Rational(-15,16), "muon at a boundary Γ-pole, not a formal-degree zero — a genuinely different residue object")

# ---- (3) the forward structural ratio that DOES hold ------------------------
d_tau = d.subs(nu, Rational(0))                 # tau at ν=0
ratio_tau_mu = d_tau/abs(d_mu)
print(f"\n[forward ratio]: d_τ = d(0) = {d_tau} ; |d_μ| = |d(3/2)| = {abs(d_mu)} ; d_τ/d_μ = {ratio_tau_mu} = 2^C_2 = {2**C_2}")
check("FORWARD RATIO holds exactly: d_τ/d_μ = d(0)/|d(3/2)| = 60/(15/16) = 64 = 2^{C_2} (target-innocent). The τ/μ "
      "formal-degree ratio IS a clean substrate power — a forward structural fact independent of the open unity check.",
      ratio_tau_mu == 2**C_2, "d_τ/d_μ = 64 = 2^C_2 exactly — forward, target-innocent")

# ---- (4) the muon UNITY stays OPEN (not banked) -----------------------------
check("MUON UNITY STAYS OPEN (not banked): the Szegő residue = 1? question is the boundary partition-function "
      "determinant at the unitarity bound (π¹² boundary-Szegő normalization, dim SO(4)=6) — a DIFFERENT object from "
      "the validated formal-degree derivative, and from the bulk c_FK (π^{9/2}, Keeper). The validated machinery "
      "does NOT evaluate it. I do NOT report a unity value; the count-mover remains OPEN; strict forced-count HOLDS 4.",
      True, "electron recipe doesn't transfer; muon unity = open boundary determinant; count HOLDS 4, not banked")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: electron reference VALIDATED exactly (9/16 = |d'(5/2)| = N_c²/rank^(n_C−1)); the muon is a "
      "DIFFERENT degeneracy type (unitarity bound, NOT a formal-degree zero) so unity is genuinely not automatic and "
      "the electron recipe doesn't transfer; the muon unity is the OPEN boundary-determinant computation (π¹², dim "
      "SO(4)=6). NOT banked — count HOLDS 4. Forward piece that holds: d_τ/d_μ = 2^{C_2} = 64. The search-first "
      "discipline prevented banking a muon unity I can't yet evaluate.",
      True, "moved the problem (validated reference + pinned the object) without fabricating unity. Count ~7-8 (α RULED)")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print("""
MUON count-mover — electron 9/16 validated; muon is a DIFFERENT degeneracy type → unity stays OPEN (count HOLDS 4):
  * ELECTRON (validated exact): on the BF zero d(5/2)=0 → residue = |d'(5/2)| = 9/16 = N_c²/rank^(n_C−1). A rational
    ≠ 1 — the reference proving a residue need NOT be unity.
  * MUON: d(3/2) = −15/16 ≠ 0 → NOT a formal-degree zero → the electron 'derivative-at-the-zero' recipe does NOT
    transfer. The muon residue is the boundary partition-function DETERMINANT (unitarity bound, π¹², dim SO(4)=6) —
    a different, harder object. THIS is why unity is 'verify, not assume'.
  * FORWARD ratio that holds: d_τ/d_μ = d(0)/|d(3/2)| = 60/(15/16) = 64 = 2^{C_2} (target-innocent).
  * MUON UNITY stays OPEN — the boundary determinant (≠ validated formal-degree machinery; ≠ bulk c_FK). NOT banked.
  => count HOLDS 4; the muon derives forward ONLY when the boundary determinant is evaluated. Search-first prevented
     banking an unverifiable unity. Count ~7-8.
""")
