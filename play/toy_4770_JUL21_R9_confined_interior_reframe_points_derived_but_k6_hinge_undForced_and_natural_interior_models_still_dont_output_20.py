#!/usr/bin/env python3
"""
Toy 4770 — Jul 21 (Round-9, CAPSTONE confinement reframe, Elie's fish-detector on the third reframe): Casey's diagnosis —
quarks are CONFINED (bulk interior), NOT boundary orbits; leptons are at the Shilov boundary. Physically better and
corpus-grounded (bulk-vs-Shilov two-region; D_IV⁵ boundedness = the IR cutoff holographic QCD adds by hand). The redo: the
quark mass is a confined interior overlap ⟨f_n|O|f_n⟩ at the interior radii r² = k/(k+N_c) with color. My job: keep doing
the linear algebra and report honestly whether THIS frame validates gate (a). Result: (1) Grace's interior points
{0, 1/4, 2/3} are DERIVED (not the circularity), (2) BUT the k=C_2=6 hinge is NOT forced — normalizability (r²<1) admits
ALL k, so gen-3 at k=6 needs a geometric cutoff that must be derived, not chosen to hit r²=2/3, and (3) natural interior
mass models do NOT output m_s/m_d=20 tuning-free either. So the confinement reframe is physically better but gate (a) is
STILL unmet by computation, and the k=6 hinge is un-derived. Third reframe, still unvalidated — nothing banks.

DERIVED POINTS (Grace, confirmed): r² = k/(k+N_c) at k = {0, 1, C_2=6} → {0, 1/4, 2/3} = T2509. The interior radii ARE
derived from the K-addresses via a clean geometric formula — so the points are NOT the circularity risk. Good.
THE k=C_2=6 HINGE (un-derived, the load-bearing item): normalizability r²<1 admits ALL k (r²→1 as k→∞), so there is NO
upper bound on k from normalizability. Therefore gen-3 sitting at k=6 is NOT forced by "the last normalizable state"
naively — it needs a SPECIFIC geometric cutoff. The candidate is k = C_2 = 6 (the Casimir / last K-type before a Wallach
threshold), which is plausible and pretty — but it MUST be derived (a real bound), not chosen because r²(6) = 2/3 lands a
mass. If k=6 was picked to hit 2/3, the capstone is circular. This one integer decides it (Grace's hinge).
GATE (a) INTERIOR FRAME (fish-detector): natural interior mass models at the derived radii {0, 1/4, 2/3} do NOT give
m_s/m_d = 20 tuning-free. mass ~ 1/(1-r²)^p = ((k+N_c)/N_c)^p gives ratios (4/3)^p and (9/4)^p; forcing m_s/m_d=(4/3)^p=20
needs p = 10.4 (non-clean), and THEN m_b/m_s = (27/16)^10.4 ≈ 232 (vs observed ~50) — inconsistent across rungs. So, as in
the boundary frame (toy 4769: {5,6,17.5,21,27}), the natural interior computations do NOT output 20 without tuning.
HONEST CAVEAT (fair to Lyra): the RIGOROUS FK interior overlap ⟨f_n|O|f_n⟩ (the K264 machinery — the vector condensate O
between the color-charged spinor modes at the interior points, with the proper Gindikin measure) is Lyra's and is NOT
evaluated here. This does NOT disprove the reframe; it shows the SIMPLE interior models don't give 20, so the burden is on
her rigorous interior overlap to OUTPUT 20 tuning-free.

⟹ VERDICT: the confinement reframe is physically better (quarks confined in the bounded bulk = the IR cutoff; leptons at
the Shilov boundary) and corpus-grounded — a genuinely improved starting frame. BUT gate (a) is STILL unmet by
computation: the derived interior points are clean, yet (i) the k=C_2=6 hinge is un-derived (normalizability admits all k
→ k=6 must be forced by a geometric cutoff, not chosen to land r²=2/3), and (ii) natural interior mass models do NOT output
20 tuning-free (like the boundary frame). This is the THIRD capstone reframe (search → computation → confined-interior),
each promising, none validated. Nothing banks. The burden: Lyra's rigorous FK interior overlap must OUTPUT 20 with the
derived ν + a DERIVED k=6, no ad-hoc shifts (gate a); then PREDICT a second independent quantity (gate b). Pivot-exit
stands if it needs tuning or k=6 is a fit. Discipline held at peak convergence — I did the linear algebra; it doesn't
validate yet. Count ~7-8. Five-Absence-safe.
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- derived interior points ------------------------------------------------
ks = [0, 1, C_2]
r2 = [k/(k+N_c) for k in ks]
print(f"\n[derived points] r² = k/(k+N_c) at k={ks} → {[round(x,4) for x in r2]} = {{0, 1/4, 2/3}} (T2509)")
check("DERIVED POINTS (Grace, confirmed): r² = k/(k+N_c) at k = {0, 1, C_2=6} → {0, 1/4, 2/3} = T2509. The interior radii "
      "ARE derived from the K-addresses via a clean geometric formula → the POINTS are NOT the circularity risk.",
      abs(r2[1] - 0.25) < 1e-9 and abs(r2[2] - 2/3) < 1e-9, "interior radii {0,1/4,2/3} derived from r²=k/(k+N_c) at k={0,1,6} → points derived, not the circularity")

# ---- the k=6 hinge is not forced by normalizability -------------------------
big_k_still_normalizable = (100/(100+N_c)) < 1   # r²<1 for arbitrarily large k
print(f"[hinge] r²(k=100) = {100/(100+N_c):.3f} < 1 → normalizability admits ALL k → no upper bound → k=6 NOT forced naively")
check("THE k=C_2=6 HINGE (un-derived): normalizability r²<1 admits ALL k (r²→1 as k→∞) → NO upper bound from "
      "normalizability, so gen-3 at k=6 is NOT forced by 'last normalizable state' naively. It needs a SPECIFIC geometric "
      "cutoff; the candidate k=C_2=6 (Casimir / last K-type before a Wallach threshold) is plausible but MUST be derived "
      "(a real bound), not chosen because r²(6)=2/3 lands a mass. This one integer decides circular-vs-real.",
      big_k_still_normalizable, "normalizability admits all k → k=6 not forced naively; k=C_2=6 must be a DERIVED cutoff, not chosen to hit r²=2/3 (the hinge)")

# ---- gate (a) interior frame: natural models don't give 20 ------------------
p_needed = math.log(20)/math.log(4/3)
mbs_at_p = (27/16)**p_needed
print(f"[gate a interior] force m_s/m_d=(4/3)^p=20 → p={p_needed:.1f}; then m_b/m_s=(27/16)^p={mbs_at_p:.0f} (vs ~50) — inconsistent")
check("GATE (a) INTERIOR FRAME (fish-detector): natural interior mass models at {0,1/4,2/3} do NOT give m_s/m_d=20 "
      "tuning-free. mass ~ 1/(1-r²)^p = ((k+N_c)/N_c)^p → forcing m_s/m_d=(4/3)^p=20 needs p=10.4 (non-clean), and THEN "
      "m_b/m_s=(27/16)^10.4 ≈ 232 (vs observed ~50) — inconsistent across rungs. Like the boundary frame (toy 4769: "
      "{5,6,17.5,21,27}), natural computations don't output 20 without tuning.",
      p_needed > 8 and mbs_at_p > 100, "natural interior models don't output 20 (need p≈10.4 non-clean; m_b/m_s then ≈232, inconsistent) → gate (a) still unmet")

# ---- honest caveat ----------------------------------------------------------
check("HONEST CAVEAT (fair to Lyra): the RIGOROUS FK interior overlap ⟨f_n|O|f_n⟩ (K264 machinery — the vector condensate "
      "O between color-charged spinor modes at the interior points, proper Gindikin measure) is Lyra's and NOT evaluated "
      "here. This does NOT disprove the reframe; it shows the SIMPLE interior models don't give 20, so the burden is on "
      "her rigorous interior overlap to OUTPUT 20 tuning-free.",
      True, "rigorous FK interior overlap (Lyra's, K264) not evaluated here → burden on it to output 20 tuning-free; simple models don't")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the confinement reframe is physically better (quarks confined in the bounded bulk = the IR cutoff; leptons "
      "at the Shilov boundary; corpus-grounded) — a genuinely improved frame. BUT gate (a) is STILL unmet by computation: "
      "the derived interior points are clean, yet (i) the k=C_2=6 hinge is un-derived (normalizability admits all k), and "
      "(ii) natural interior models don't output 20 tuning-free (like the boundary frame). THIRD reframe, none validated. "
      "Nothing banks. Burden: Lyra's rigorous FK interior overlap must OUTPUT 20 with a DERIVED k=6, no ad-hoc shifts "
      "(gate a); then PREDICT a second independent quantity (gate b). Pivot-exit stands.",
      abs(r2[2] - 2/3) < 1e-9 and big_k_still_normalizable and p_needed > 8,
      "confinement reframe better but gate (a) still unmet (k=6 hinge un-derived + natural models don't give 20); 3rd reframe unvalidated; burden on Lyra's rigorous FK; pivot-exit stands")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-9 confinement reframe — Elie's fish-detector (third reframe, still gating honestly):
  * DERIVED POINTS: r²=k/(k+N_c) at k={{0,1,6}} = {{0,1/4,2/3}} (T2509) — points derived, NOT the circularity. Good.
  * THE k=C_2=6 HINGE (un-derived): normalizability r²<1 admits ALL k → k=6 not forced naively; must be a DERIVED cutoff (Casimir?), not chosen to hit r²=2/3. Load-bearing.
  * GATE (a) INTERIOR: natural models don't output 20 (need p≈10.4; then m_b/m_s≈232, inconsistent) — like the boundary frame. Still unmet.
  * => confinement reframe physically better but STILL unvalidated (3rd reframe). Nothing banks. Burden on Lyra's rigorous FK interior overlap (output 20 + derive k=6); then gate (b). Pivot-exit stands.
""")
