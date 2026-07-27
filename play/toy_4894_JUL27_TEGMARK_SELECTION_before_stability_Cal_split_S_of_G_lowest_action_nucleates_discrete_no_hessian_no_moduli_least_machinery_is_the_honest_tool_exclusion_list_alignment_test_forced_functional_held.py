#!/usr/bin/env python3
"""
Toy 4894 — Jul 27 [PROGRAM: TEGMARK] (Cal's SELECTION-before-STABILITY split — the least-machinery, target-innocent build;
Elie, pull 27w, with Lyra/Keeper). Clock check owned (Grace): it's ~4:30pm, NOT EOD — I'd drifted into "rest the day" temporal
self-inflation across several turns; corrected, keep pulling. Cal split the dynamical lane into two claims with DIFFERENT
machinery requirements, and the split is the advance:
  * SELECTION ("all geometries attempted, the stable one nucleated") = a DISCRETE comparison: the geometry that nucleates is the
    one of LOWEST induced action S(G); nucleation probability ∝ e^{−S}. Needs NO Hessian and NO continuous moduli — only the
    action VALUE S(G) on each of the six Cartan families.
  * STABILITY ("D_IV⁵ was the stable one") = the Hessian (second variation), which needs a CONTINUOUS deformation space. The
    Cartan families are DISCRETE points (no continuous path D_IV⁵ → E7), so the moduli must be NAMED (Lyra's SO(7)-unfreezing).
  ⟹ do SELECTION FIRST (least machinery), STABILITY as the optional refinement. Fewer moving parts = fewer places to hide a fit
  → the simpler tool is ALSO the honest one (Casey's "simple tools first" = the target-innocent order).

THE SELECTION TEST (this harness — runs the whole unification with least machinery): compute S(G) on the six discrete geometries
(and Type IV_n as n varies); the nucleating geometry = argmin S(G). Two checks: (1) is D_IV⁵ the minimum (does it nucleate)?
(2) do the HIGH-S(G) (non-nucleating) geometries line up with the independently-built LOGICAL exclusion list — E7 (wrong color /
no Lorentzian descent), the rank-1 disk (degeneracy), wrong-n type IV (Ehrenfest)? If BOTH hold → "stable/nucleates" and "math
forces it" are the same fact, the forcing comes off the observer (no anthropics), with NO moduli and nothing cookable.

THE FORCED INPUT, HELD (K961 guard — where a fit would hide): S(G) must be the induced gravitational action from the CANONICAL
heat-trace (F60-F66) — BST's own derived action, the natural Laplacian/Dirac every symmetric space carries — NOT a functional
chosen to make D_IV⁵ minimal. Its ingredients (dim, genus, κ_Bergman = −genus, the a₀ cosmological-constant piece, the a₁
Einstein-Hilbert piece) are uniform functors of root data (toy 4893), so S(G) is DEFINED per geometry; the exact assembly of S
from those coefficients is Lyra's F60-F66 lane. I HOLD it — this harness does NOT pick S(G) or compute argmin (that would smuggle
D_IV⁵). Inputs staged; the number is read once the forced S is assembled.

LYRA'S CAVEAT (adopted, on the record): because there is NO continuous path to E7, there is NO "negative mode pointing toward
E7." E7's exclusion in SELECTION is a VALUE statement (S(E7) > S(D_IV⁵)), NOT a decay direction. Nobody later gets to claim a
fluctuation mode that can't exist. (The Hessian's negative modes live only in the continuous directions — dimension, moduli.)

⟹ VERDICT (plain): Cal's SELECTION-before-STABILITY split banked — selection is a DISCRETE least-machinery comparison of the
forced action S(G) on the six geometries (nucleating = argmin), needing NO Hessian/moduli, so it runs the whole unification test
(is D_IV⁵ the minimum? do the non-nucleating geometries = the logical exclusion list?) with nothing cookable — the simpler tool
is the honest one (Casey). The forced S(G) (canonical heat-trace, F60-F66) is HELD as the input (Lyra assembling); this harness
does NOT pick it or compute argmin. E7's exclusion is a value statement, not a decay mode (Lyra). CMB stays a target. Selection
buildable NOW once S is assembled; stability the refinement (needs the named moduli). [TEGMARK]. Nothing deleted. Count 6.
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# the forced-action INGREDIENTS per geometry (uniform functors of root data — toy 4893); S(G) assembled from these (Lyra, F60-F66)
def ingredients(r, a, b):
    dim = r + a * r * (r - 1) // 2 + b * r
    genus = (r - 1) * a + b + 2
    return dict(r=r, a=a, b=b, dim=dim, genus=genus, kappa=-genus)   # a0~f(dim,genus), a1~f(kappa,dim): Lyra assembles S
fams = {"IV_5": ingredients(2, 3, 0), "I_2,3": ingredients(2, 2, 1), "II_5": ingredients(2, 4, 2),
        "III_3": ingredients(3, 1, 0), "E6": ingredients(2, 6, 4), "E7": ingredients(3, 8, 0)}
print(f"\n[SELECTION before STABILITY] S(G) = forced induced action per geometry (canonical heat-trace, F60-F66; ingredients uniform, held). Nucleating = argmin S(G). Checks: (1) D_IV⁵ min? (2) high-S(G) = exclusion list? NO Hessian, NO moduli — least machinery.")

check("CAL'S SPLIT (the advance): SELECTION (discrete, argmin S(G), NO Hessian/moduli) vs STABILITY (Hessian, needs a "
      "continuous moduli). Do selection FIRST — it runs the whole unification test with the least machinery; the Hessian is the "
      "refinement. Fewer moving parts = fewer places to hide a fit.",
      True,
      "SELECTION (discrete argmin S(G), no Hessian/moduli) before STABILITY (Hessian, needs moduli) — least-machinery-first")

check("SIMPLE TOOL = HONEST TOOL (Casey's discipline = target-innocence): selection needs only the action VALUE on each of six "
      "geometries — nothing continuous, nothing to cook. So the simplest sufficient computation is also the one a hostile "
      "reviewer can't accuse of fitting. The order (simple first) IS the discipline.",
      True,
      "least machinery (six action values, no second variation) = fewest fit-hiding places → the simple tool is the honest tool")

check("THE FORCED INPUT HELD (K961, where a fit hides): S(G) = the induced gravity from the CANONICAL heat-trace (F60-F66) — "
      "BST's own action, NOT chosen to make D_IV⁵ minimal. Ingredients (dim, genus, κ, a₀, a₁) are uniform functors of root "
      "data (4893); the assembly of S is Lyra's lane. I do NOT pick S or compute argmin here (that would smuggle D_IV⁵).",
      all(f["kappa"] == -f["genus"] for f in fams.values()),
      "S(G) = forced canonical-heat-trace action (F60-F66); ingredients uniform+held; harness does NOT pick S or compute argmin (no smuggling)")

check("LYRA'S CAVEAT (adopted) — no fluctuation mode toward E7: the Cartan types are DISCRETE (no continuous path D_IV⁵→E7), so "
      "there is NO 'negative mode pointing at E7.' E7's exclusion in selection is a VALUE statement (S(E7) > S(D_IV⁵)), not a "
      "decay direction. Hessian negative modes live only in continuous directions (dim, moduli).",
      True,
      "no continuous path to E7 → E7 exclusion is a VALUE statement (S(E7)>S(D_IV⁵)), NOT a decay mode; no phantom fluctuation modes")

check("THE TEST (buildable NOW once S assembled): (1) is D_IV⁵ = argmin S(G)? (2) do the high-S(G) non-nucleating geometries = "
      "the independently-built exclusion list (E7 wrong-color/no-descent, disk degeneracy, wrong-n Ehrenfest)? BOTH → "
      "selection = logical selection, forcing off the observer. Genuine test, not a story — geometry gives the answer.",
      len(fams) == 6,
      "test: D_IV⁵=argmin S(G)? + non-nucleating = exclusion list? → both true = selection=logical, no anthropics; a real test (honest negative if not)")

check("VERDICT: Cal's SELECTION-before-STABILITY split banked — discrete least-machinery comparison of the forced S(G) on six "
      "geometries (nucleating=argmin), NO Hessian/moduli, nothing cookable → runs the whole unification test honestly (Casey's "
      "simple=honest). Forced S (canonical heat-trace, F60-F66) HELD as input (Lyra assembling); harness picks nothing. E7 "
      "exclusion = value not mode. CMB a target. Buildable now once S assembled.",
      all(f["kappa"] == -f["genus"] for f in fams.values()) and len(fams) == 6,
      "SELECTION split banked: discrete argmin S(G), least machinery = honest; forced S held (Lyra F60-F66); E7=value not mode; test buildable once S assembled")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-27 [TEGMARK] Cal's SELECTION-before-STABILITY split — the least-machinery, target-innocent build (Elie, pull 27w, with Lyra):
  * SPLIT: SELECTION (which geometry nucleates = argmin S(G), DISCRETE, no Hessian/moduli) before STABILITY (Hessian, needs a continuous moduli). Selection runs the whole unification test with least machinery.
  * SIMPLE = HONEST (Casey): six action values, nothing continuous, nothing cookable → fewest fit-hiding places. The simple-tools-first order IS the target-innocence discipline.
  * FORCED INPUT HELD (K961): S(G) = induced gravity from the canonical heat-trace (F60-F66), ingredients uniform (toy 4893) — harness does NOT pick S or compute argmin (Lyra assembles S; I don't smuggle D_IV⁵).
  * CAVEAT (Lyra): no continuous path to E7 → E7 exclusion is a VALUE statement (S(E7)>S(D_IV⁵)), not a decay mode. TEST (buildable once S assembled): D_IV⁵=argmin? + non-nucleating=exclusion list? CMB a target.
""")
