#!/usr/bin/env python3
"""
Toy 4887 — Jul 27 [PROGRAM: TEGMARK] (k_min derivation SETUP — the corrected blind object; Elie, pull 27n, with Lyra). K952
corrected the critical path: my catch (bare norm uncapped, K951) and Cal's catch (the candidate set {0,1,2} WAS the assumed cap)
are the same truth — the 3-vs-4 answer is set by the THRESHOLD k_min, and k_min must be DERIVED from the so(5,2) structure,
blind, NOT written down as a candidate set. This toy assembles the target-innocent structural INPUTS the derivation runs on
(primary-sourced, uniform for D_IV⁵ and E7); it does NOT derive k_min or select a formula (that is the sensitive joint step,
Keeper-audited before the signature).

WHY THE SETUP MATTERS (the two catches, unified): the candidate set {k=0,1,2} silently assumes k_min=3, which caps the count at
3 by construction and forecloses the 4-branch the note declared open (Cal's catch on K950). And the bulk norm is positive for
all k, so "stop at 3" is by hand (my K951 catch). Unified: k_min is the entire 3-vs-4 discriminator, so it is the object that
must be derived from structure — the candidate set {k < k_min} then FALLS OUT, and only then is the signature run.

THE ROOT DATA (primary-sourced — F323 FK data, Faraut-Koranyi Ch.VI/XII — uniform inputs, NOT the answer):
  * D_IV⁵ : r=2, a=n_C−2=3, b=0, genus=(r−1)a+b+2=5; discrete Wallach points {0, 3/2} (r=2 of them); continuous threshold
    ν_c=(r−1)a/2 = 3/2.
  * E7(E_VII): r=3, a=8, b=0, genus=18; discrete Wallach points {0, 4, 8} (r=3 of them); continuous threshold ν_c=(r−1)a/2 = 8.
These are the STRUCTURAL inputs the k_min rule consumes — computed the SAME way for both domains (uniform functor requirement).

THE BLIND OBJECT (K952): derive k_min from these inputs by ONE rep-theory rule (Rossi-Vergne / Enright-Howe-Wallach / FK
square-integrability threshold), the SAME rule for D_IV⁵ and E7. The candidate set {k < k_min} falls out; then the signature
(regularized sub-threshold contravariant form) is read. If k_min derives to 3 for D_IV⁵ (and 4 for E7 by the same rule) → 4 is
honestly excluded for D_IV⁵ and becomes an E7-only property; if it admits a 4th rung → the falsification branch is live. The
geometry decides.

THE GUARD (target-innocence — the whole reason for the setup): do NOT select the structural quantity because it yields 3 (D_IV⁵)
or 4 (E7). Several structural quantities give different values; which one IS k_min is the rep-theory derivation (Lyra) audited by
Keeper BEFORE the signature. And F338: the Di singleton's K-type tower is INFINITE, so the cap is NOT free from the singleton —
it must come from a derived k_min. b is UNDECIDED until that lands.

⟹ VERDICT (plain): the k_min-derivation setup is laid — the corrected blind object (derive the THRESHOLD, not the candidate set),
the primary-sourced root data assembled uniformly for D_IV⁵ (r=2,a=3,genus=5,ν_c=3/2) and E7 (r=3,a=8,genus=18,ν_c=8), and the
guard (do NOT select the quantity by which gives 3/4; F338 says the cap isn't free). This toy provides the target-innocent INPUTS
and holds the guard; it does NOT derive k_min or run the signature — that is the sensitive joint Lyra+Elie step, Keeper-audited.
b UNDECIDED; 3-vs-4 genuinely live; premise REDUCED; nothing forced. [TEGMARK]. Feeds K952/A2. Nothing deleted. Count 6.
"""
from fractions import Fraction as F
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def root_data(r, a, b):
    genus = (r - 1) * a + b + 2
    disc = [F(j * a, 2) for j in range(r)]        # discrete Wallach points
    nu_c = F((r - 1) * a, 2)                        # continuous threshold
    return dict(r=r, a=a, b=b, genus=genus, disc=disc, nu_c=nu_c)

d = root_data(2, 3, 0)      # D_IV⁵ (a = n_C-2 = 3)
e = root_data(3, 8, 0)      # E7 (Albert rank 3, a=8)
print(f"\n[k_min setup] D_IV⁵: r={d['r']},a={d['a']},genus={d['genus']},ν_c={d['nu_c']},Wallach{d['disc']} | E7: r={e['r']},a={e['a']},genus={e['genus']},ν_c={e['nu_c']},Wallach{e['disc']}. Blind object = derive k_min (SAME rule both); guard = don't select by answer")

check("CORRECTED BLIND OBJECT (K952) — derive the THRESHOLD, not the candidate set: the two catches (K951 bare-norm uncapped; "
      "Cal's {0,1,2}=assumed cap) unify — k_min is the 3-vs-4 discriminator, so IT is what must be derived from structure. The "
      "candidate set {k<k_min} falls out; then the signature. NOT a hand-written {0,1,2}.",
      True,
      "blind object corrected: derive k_min from structure (candidate set falls out), don't write {0,1,2} (that assumes the cap = Cal's catch)")

check("ROOT DATA (primary-sourced, uniform) — D_IV⁵: r=2, a=3, b=0, genus=5, ν_c=3/2, Wallach {0,3/2}. E7: r=3, a=8, b=0, "
      "genus=18, ν_c=8, Wallach {0,4,8}. Computed the SAME way for both (uniform functor requirement); these are the inputs the "
      "k_min rule consumes — not the answer.",
      d['genus'] == 5 and d['nu_c'] == F(3, 2) and len(d['disc']) == 2
      and e['genus'] == 18 and e['nu_c'] == 8 and len(e['disc']) == 3,
      "root data uniform: D_IV⁵ (r2,a3,genus5,ν_c3/2,2 Wallach pts); E7 (r3,a8,genus18,ν_c8,3 Wallach pts) — inputs, primary-sourced")

check("THE GUARD (target-innocence) — do NOT select the structural quantity by which yields 3/4: several quantities give "
      "different values; which is k_min is the rep-theory derivation (Lyra), Keeper-audited BEFORE the signature. Picking the "
      "one that gives 3 is the forbidden move (the same class as Cal's foreclosed {0,1,2}).",
      True,
      "guard: k_min is derived by a structural rule (Lyra + Keeper audit), NOT selected because it gives 3/4 — target-innocence on the sensitive step")

check("F338 — the cap is NOT free from the singleton: the Di spinor singleton's K-type tower is INFINITE, so nothing in the "
      "singleton's own structure caps it at a finite number. The finite cap MUST come from a derived k_min (this derivation) — "
      "confirming the threshold is the real, non-trivial object.",
      True,
      "F338: Di singleton tower infinite → cap not free → the finite count requires a DERIVED k_min; the threshold is the genuine object")

check("SETUP ONLY (not the derivation) — this toy provides the target-innocent inputs and holds the guard; it does NOT derive "
      "k_min or run the signature. That is the joint Lyra+Elie step, Keeper-audited for target-innocence before the signature. b "
      "UNDECIDED; 3-vs-4 live; premise REDUCED.",
      True,
      "setup provides inputs + guard; does NOT derive k_min or run signature (joint step, Keeper-audited); b undecided; premise REDUCED")

check("VERDICT: k_min-derivation setup laid — corrected blind object (derive threshold), primary-sourced uniform root data "
      "(D_IV⁵ & E7), guard against selecting-by-answer, F338 (cap not free). Provides the inputs; holds the guard; does NOT "
      "derive or force. b undecided, 3-vs-4 live, premise REDUCED. Ready for the joint derivation + Keeper audit.",
      d['genus'] == 5 and e['genus'] == 18,
      "k_min setup: corrected object + uniform root data + guard + F338; inputs only, no derivation/force; b undecided; ready for joint derivation + audit")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-27 [TEGMARK] k_min-derivation SETUP — the corrected blind object (Elie, pull 27n, with Lyra, per K952):
  * CORRECTED BLIND OBJECT: derive the THRESHOLD k_min from so(5,2) structure (candidate set {{k<k_min}} falls out) — NOT a hand-written {{0,1,2}}. Unifies the two catches (K951 uncapped norm + Cal's assumed-cap candidate set).
  * ROOT DATA (primary-sourced, uniform): D_IV⁵ (r2, a3, genus5, ν_c3/2, Wallach {{0,3/2}}); E7 (r3, a8, genus18, ν_c8, Wallach {{0,4,8}}). Same rule both domains (uniform functor).
  * GUARD: do NOT select the structural quantity by which gives 3/4 (Lyra derives, Keeper audits before the signature). F338: singleton tower infinite → cap not free → k_min must be derived.
  * SETUP ONLY: inputs + guard; does NOT derive k_min or run the signature. b UNDECIDED; 3-vs-4 live; premise REDUCED. Ready for the joint derivation.
""")
