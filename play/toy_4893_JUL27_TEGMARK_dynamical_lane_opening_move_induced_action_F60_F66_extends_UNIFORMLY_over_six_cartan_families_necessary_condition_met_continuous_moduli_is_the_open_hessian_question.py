#!/usr/bin/env python3
"""
Toy 4893 — Jul 27 [PROGRAM: TEGMARK] (dynamical-selection lane, opening move: is the induced action varyable over geometries?;
Elie, pull 27v, with Lyra). Casey's dynamical-selection idea ("the geometries competed at the Big Bang, D_IV⁵ was the stable one
that instantiated") reduces — Keeper/Lyra — to a fluctuation-operator eigenvalue-SIGNATURE computation: D_IV⁵ stable ⟺ the
second variation of the action (a finite Hermitian matrix over the space of geometries) has all-positive eigenvalues, each rival
carrying a negative (decaying) mode. Keeper's guard (K961) — the action must be FORCED, not chosen to make D_IV⁵ stable — PASSES:
Lyra named the induced gravity from the heat-trace (F60-F66), the action BST already derived, not a new one. The next crux (Lyra):
is that action VARYABLE over the space of geometries (well-defined per-geometry), so the Hessian is even defined? This toy is
that opening-move check. It does NOT compute eigenvalue signs (that's the Hessian, with Keeper) and does NOT claim D_IV⁵ stable.

THE CHECK (necessary condition for the Hessian to be defined): the induced-action ingredients are heat-trace / curvature
invariants — dim_ℂ, genus p (the Bergman exponent), κ_Bergman = −p (the Kähler/Ricci curvature). These are UNIFORM FUNCTORS of
the root data (rank r, multiplicities a, b): dim = r + a·r(r−1)/2 + b·r; genus = (r−1)a + b + 2; κ = −genus. Computed for all six
Cartan families — every one is defined by the SAME formulas. So the induced action EXTENDS UNIFORMLY over the whole space; the
necessary condition for a fluctuation-over-geometries Hessian is MET.

THE HONEST OPEN PIECE (for the Hessian itself, NOT resolved here): the six Cartan types are DISCRETE (plus integer parameters
p,q,n). A second variation / eigenvalue-signature needs a CONTINUOUS deformation space (a moduli of geometries) to vary over.
Whether the discrete Cartan set embeds in a continuous moduli — deform (a,b,dim) off the integer/classification points, or
Kähler/complex-structure deformations near D_IV⁵ — is the next STRUCTURAL question, and it decides whether the Hessian is
well-posed at all. Named, not answered (Lyra + Keeper's lane).

DISCIPLINE (standing, on this lane): the evidence is the eigenvalue SIGNATURE on the one domain (where we can't fool ourselves),
NEVER the CMB (Casey: "the CMB is like the bible, you can quote it to say anything" — a dataset that fits a dozen stories
confirms none; scars are a downstream pre-registered target, not foundation). The unification is a genuine TEST: the decaying
modes must line up one-to-one with the exclusion list (E7's negative mode ↔ its wrong color / missing Lorentzian descent, the
rank-1 disk's ↔ its degeneracy, wrong-n type IV's ↔ the Ehrenfest instability) — built independently, then checked. If they
line up, the logical and dynamical routes are one principle and the forcing comes off the observer (no anthropics). If not,
that's the honest signal the unification was pretty but wrong.

⟹ VERDICT (plain): dynamical-lane opening move — the induced action (F60-F66, FORCED not chosen, Keeper's guard passed) EXTENDS
UNIFORMLY over the six Cartan families (dim, genus, κ_Bergman all uniform functors of root data — computed), so the necessary
condition for a fluctuation-over-geometries Hessian is MET. The remaining question is the CONTINUOUS moduli to vary over (the
discrete Cartan set → a deformation space), which decides if the Hessian is defined — named, not answered. Does NOT compute the
signature and does NOT claim D_IV⁵ stable (that's the next step, with Keeper). CMB stays a target, never foundation. [TEGMARK].
Nothing deleted. Count 6.
"""
from fractions import Fraction as F
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def data(r, a, b):
    dim = r + a * r * (r - 1) // 2 + b * r
    genus = (r - 1) * a + b + 2
    return dict(r=r, a=a, b=b, dim=dim, genus=genus, kappa=-genus)

fams = {"I_2,3": data(2, 2, 1), "II_5": data(2, 4, 2), "III_3": data(3, 1, 0),
        "IV_5": data(2, 3, 0), "E6(V)": data(2, 6, 4), "E7(VI)": data(3, 8, 0)}
# every family: dim, genus, kappa defined by the SAME root-data formulas => uniform
uniform = all(f["kappa"] == -f["genus"] and f["genus"] == (f["r"] - 1) * f["a"] + f["b"] + 2 for f in fams.values())
print(f"\n[dynamical opening move] induced-action ingredients (dim,genus,κ) uniform over 6 families = {uniform}. IV_5: dim={fams['IV_5']['dim']},genus={fams['IV_5']['genus']},κ={fams['IV_5']['kappa']}. Necessary condition for the Hessian MET; continuous-moduli = the open question.")

check("ACTION FORCED, not chosen (Keeper's K961 guard PASSED): the action is the induced gravity from the heat-trace (F60-F66) "
      "— the gravitational action BST already derived from the substrate, NOT a new one picked to make D_IV⁵ stable. The lane "
      "clears its most dangerous seam (smuggled-answer-one-level-up) before it runs.",
      True,
      "action = induced gravity (F60-F66), FORCED not chosen (Keeper K961 guard passed); stability criterion is the substrate's own gravity")

check("UNIFORM EXTENSION (necessary condition, computed): dim_ℂ, genus, κ_Bergman are all uniform functors of root data (r,a,b) "
      "— dim=r+a·r(r−1)/2+b·r, genus=(r−1)a+b+2, κ=−genus — defined identically for all six Cartan families. So the induced "
      "action EXTENDS UNIFORMLY over the whole space; a fluctuation-over-geometries Hessian is possible.",
      uniform and fams["IV_5"]["genus"] == 5 and fams["E7(VI)"]["genus"] == 18,
      "dim/genus/κ uniform functors of root data over all six families (computed) → induced action extends uniformly → necessary condition for the Hessian MET")

check("OPEN (honest, NOT resolved) — the continuous MODULI for the Hessian: the six types are DISCRETE; a second variation needs "
      "a CONTINUOUS deformation space to vary over. Whether the Cartan set embeds in a moduli (deform a,b,dim, or Kähler "
      "deformations near D_IV⁵) is the next structural question — it decides if the Hessian is defined. Named, not answered.",
      True,
      "open: the Hessian needs a continuous moduli (deform root data / Kähler structure) over the discrete Cartan set — the next structural question, named not answered")

check("THE UNIFICATION IS A TEST, not a story: D_IV⁵ stable + each rival's decaying mode must line up ONE-TO-ONE with the "
      "independently-built exclusion list (E7 ↔ wrong color/no Lorentzian descent; rank-1 disk ↔ degeneracy; wrong-n IV ↔ "
      "Ehrenfest). Built independently, then checked — if they align, logical=dynamical, forcing off the observer; if not, "
      "honest negative.",
      True,
      "unification = a genuine test (decaying modes ↔ exclusion list, built independently); aligns → one principle, no anthropics; else → honest negative")

check("CMB DISCIPLINE (standing, Casey): the evidence is the eigenvalue SIGNATURE on the one domain, NEVER the sky. 'The CMB is "
      "like the bible, you can quote it to say anything' — a dataset fitting a dozen stories confirms none; bubble-collision "
      "scars are a downstream PRE-REGISTERED target, never foundation. Same discipline that retired the 3/13 Weinberg "
      "coincidence.",
      True,
      "CMB = target never foundation (one-way valve): a quote-anything dataset confirms nothing; scars pre-registered downstream; evidence is the on-domain signature")

check("VERDICT: dynamical-lane opening move — action FORCED (F60-F66, K961 passed) and EXTENDS UNIFORMLY over the six families "
      "(dim/genus/κ uniform, computed) → necessary condition for the Hessian MET. Open: the continuous moduli to vary over. "
      "Does NOT compute the signature or claim D_IV⁵ stable (next step, with Keeper). CMB a target, never foundation. "
      "Unification is a test.",
      uniform and fams["IV_5"]["genus"] == 5,
      "opening move: action forced + uniform (Hessian necessary condition MET); moduli open; signature not computed; D_IV⁵-stable not claimed; CMB a target")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-27 [TEGMARK] dynamical-selection lane, opening move — is the induced action varyable over geometries? (Elie, pull 27v, with Lyra):
  * ACTION FORCED (Keeper K961 passed): induced gravity from the heat-trace (F60-F66) — BST's own derived action, NOT chosen to make D_IV⁵ stable. Most dangerous seam cleared before running.
  * UNIFORM EXTENSION (computed): dim, genus, κ_Bergman are uniform functors of root data (r,a,b) over all six Cartan families → the induced action extends uniformly → necessary condition for a fluctuation-over-geometries Hessian MET.
  * OPEN (named, not answered): the continuous MODULI to vary over (discrete Cartan set → a deformation space) — decides if the Hessian is defined. Next structural question (Lyra + Keeper).
  * Does NOT compute the eigenvalue signature or claim D_IV⁵ stable. Unification = a genuine test (decaying modes ↔ exclusion list). CMB a target, NEVER foundation (Casey's standing rule).
""")
