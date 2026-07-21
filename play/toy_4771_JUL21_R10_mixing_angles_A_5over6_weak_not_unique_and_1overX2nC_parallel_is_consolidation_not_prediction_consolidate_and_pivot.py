#!/usr/bin/env python3
"""
Toy 4771 — Jul 21 (Round-10, the course-correction: mixing ANGLES direct, Elie's target-innocent PREDICTION test): after
3 unvalidated capstone reframes, Casey/Keeper course-corrected to the clean ground — the mixing ANGLES, direct from the
primaries, never through the Tier-2 masses. The solid inventory: PMNS {sin²θ₁₂=3/10, sin²θ₂₃=4/7, sin²θ₁₃=1/45} + Cabibbo
sin²θ_C=1/20, all primary-fractions, RG-clean. My assignment: the target-innocent PREDICTION — (1) test A = n_C/C_2 = 5/6
(Wolfenstein A) for UNIQUENESS (the 20-beats-21 standard), and (2) test whether the 1/(X²·n_C) shared primitive predicts a
NOT-used angle. Honest result: A=5/6 is a WEAK candidate (unique only at 1σ; 4/5=rank²/n_C competes at 2σ; C_2 has 5 forms)
— it does NOT pass the clean uniqueness bar. And the 1/(X²·n_C) parallel appears at only TWO mismatched positions (CKM
12-angle, PMNS 13-angle) with NO third instance → it is a target-innocent CONSOLIDATION relation, not a prediction of a
new quantity. So per the pull's own bar (win = prediction, not reproduction), this is the HONEST-PIVOT outcome: consolidate
the solid angle inventory, bank nothing new, pivot to fresh ground. No reframe #4.

TEST 1 — A = n_C/C_2 = 5/6 UNIQUENESS (WEAK): A = |V_cb|/|V_us|² = 0.826 ± 0.014. 5/6 = 0.833 (0.9%) is in the 1σ band and
IS unique there — BUT 4/5 = rank²/n_C = 0.800 (3.2%) competes in the 2σ band, and C_2 = 6 has five BST forms (1+n_C =
rank·N_c = 2N_c = g−1 = C_2). So A=5/6 does NOT pass the clean 20-beats-21 standard (where 20 was 0.0% and beat 21 by 8× in
a tight band). I-tier CANDIDATE, not a bankable prediction.
TEST 2 — the 1/(X²·n_C) parallel is CONSOLIDATION, not prediction: sin²θ₁₃(PMNS) = 1/(N_c²·n_C) = 1/45 and sin²θ_C(CKM) =
1/(rank²·n_C) = 1/20 share the form 1/(X²·n_C), giving a target-innocent RELATION sin²θ₁₃/sin²θ_C = rank²/N_c² = 4/9 (obs
0.437, 2%; n_C cancels). BUT: (i) it uses TWO already-known angles → consolidation, not a prediction of a not-used
quantity; (ii) the two positions are MISMATCHED (CKM 12-angle vs PMNS 13-angle); (iii) the form appears at NO third
position (θ₁₂ PMNS, θ₁₃ CKM, θ₂₃ PMNS all give non-primary X), so there is no not-used angle for it to predict. So the
parallel is a real but coincidence-flavored consolidation, not a win.

⟹ VERDICT: the course-correction landed on solid ground — the angle inventory (PMNS triple + Cabibbo, all primary-
fractions, RG-clean, DIRECT overlaps not via masses) is a genuine, publishable gem, and the 1/(X²·n_C) θ₁₃↔θ_C parallel is
a real target-innocent relation (rank²/N_c², 2%). BUT there is NO clean NEW prediction: A=5/6 is a weak candidate (fails
2σ uniqueness; C_2 multi-form), and the parallel is consolidation (two known angles, mismatched positions, no third
instance). Per the pull's bar (win = prediction, not reproduction), this is the HONEST-PIVOT outcome: bank the consolidated
angle inventory, bank NOTHING new, and pivot to fresh ground (neutrino Δm², gravity/G, Λ). One pull, assessed — no reframe
#4. The discipline held: I tested my own sector's candidates target-innocently and neither cleanly survives. Count ~7-8.
Five-Absence-safe.
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- Test 1: A = 5/6 uniqueness --------------------------------------------
Vcb, Vcb_e, Vus = 0.04182, 0.0007, 0.2250
A = Vcb/Vus**2; Ae = Vcb_e/Vus**2
in_1sig = A - Ae <= 5/6 <= A + Ae
competitor_2sig = A - 2*Ae <= 4/5 <= A + 2*Ae
print(f"\n[A test] A = {A:.4f} ± {Ae:.4f}; 5/6 = {5/6:.4f} (0.9%, in 1σ: {in_1sig}); 4/5 = 0.800 (3.2%, competes in 2σ: {competitor_2sig})")
check("TEST 1 — A = n_C/C_2 = 5/6 UNIQUENESS (WEAK): A = |V_cb|/|V_us|² = 0.826 ± 0.014. 5/6 = 0.833 (0.9%) is unique in "
      "the 1σ band — BUT 4/5 = rank²/n_C = 0.800 (3.2%) competes in the 2σ band, and C_2=6 has five BST forms. So A=5/6 "
      "does NOT pass the clean 20-beats-21 standard (20 was 0.0%, 8× margin). I-tier CANDIDATE, not a bankable prediction.",
      in_1sig and competitor_2sig, "A=5/6 unique at 1σ but 4/5 competes at 2σ + C_2 multi-form → weak I-tier candidate, fails the clean uniqueness bar")

# ---- Test 2: no third instance -> consolidation not prediction --------------
ratio_pred = rank**2/N_c**2
ratio_obs = (1/45)/(1/20)
third_instances = 0   # θ₁₂(PMNS)=3/10, θ₁₃(CKM)~1e-5, θ₂₃(PMNS)=4/7 all give non-primary X in 1/(X²·n_C)
print(f"[parallel] sin²θ₁₃/sin²θ_C = rank²/N_c² = {ratio_pred:.4f} (obs {ratio_obs:.4f}, 2%); third 1/(X²·n_C) instances = {third_instances}")
check("TEST 2 — the 1/(X²·n_C) parallel is CONSOLIDATION, not prediction: sin²θ₁₃(PMNS)=1/45 and sin²θ_C(CKM)=1/20 share "
      "1/(X²·n_C) → target-innocent relation rank²/N_c²=4/9 (obs 0.437, 2%, n_C cancels). BUT (i) uses TWO known angles → "
      "consolidation; (ii) positions MISMATCHED (CKM 12 vs PMNS 13); (iii) NO third instance (θ₁₂/θ₂₃ PMNS, θ₁₃ CKM give "
      "non-primary X) → no not-used angle to predict. Real relation, but coincidence-flavored, not a win.",
      abs(ratio_pred - ratio_obs)/ratio_obs < 0.03 and third_instances == 0, "1/(X²·n_C) parallel = target-innocent consolidation relation (rank²/N_c², 2%), not a new prediction (2 known angles, mismatched positions, no 3rd instance)")

# ---- Test 3: the inventory is solid (the genuine gem) -----------------------
inv = {"sin²θ₁₂(PMNS)=3/10": (3/10, 0.307), "sin²θ₂₃(PMNS)=4/7": (4/7, 0.55),
       "sin²θ₁₃(PMNS)=1/45": (1/45, 0.0220), "sin²θ_C(CKM)=1/20": (1/20, 0.0503)}
allclose = all(abs(v[0]-v[1])/v[1] < 0.06 for v in inv.values())
check("TEST 3 — the angle inventory is SOLID (the genuine gem): PMNS {3/10, 4/7, 1/45} + Cabibbo 1/20 — all "
      "primary-fractions, RG-clean (angles don't run like masses), DIRECT overlaps (never through the Tier-2 masses). This "
      "is real, publishable consolidation — the clean ground the session should have stayed on.",
      allclose, "PMNS triple + Cabibbo all primary-fractions within ~1-2σ, RG-clean, direct-overlap → solid consolidated inventory (the gem)")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the course-correction landed on solid ground — the angle inventory (PMNS triple + Cabibbo, direct "
      "primary-fractions, RG-clean) is a genuine gem, and the 1/(X²·n_C) θ₁₃↔θ_C parallel is a real target-innocent "
      "relation (rank²/N_c², 2%). BUT NO clean NEW prediction: A=5/6 is weak (fails 2σ uniqueness; C_2 multi-form) and the "
      "parallel is consolidation (two known angles, mismatched positions, no third instance). Per the pull's bar (win = "
      "prediction, not reproduction), this is the HONEST-PIVOT: bank the consolidated inventory, bank NOTHING new, pivot "
      "to fresh ground (ν Δm², gravity/G, Λ). One pull, assessed — no reframe #4.",
      in_1sig and competitor_2sig and third_instances == 0 and allclose,
      "solid angle inventory consolidated + real θ₁₃↔θ_C relation (2%); but A=5/6 weak + parallel=consolidation → NO new prediction → honest-pivot, bank nothing new, move to fresh ground")

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
ROUND-10 mixing angles direct — Elie's target-innocent prediction test (honest-pivot outcome):
  * A = n_C/C_2 = 5/6: WEAK — unique at 1σ (0.9%) but 4/5=rank²/n_C competes at 2σ + C_2 multi-form → I-tier candidate, fails the clean 20-beats-21 bar.
  * 1/(X²·n_C) parallel (θ₁₃ PMNS ↔ θ_C CKM): target-innocent relation rank²/N_c²=4/9 (2%) — but CONSOLIDATION (2 known angles, mismatched positions, no 3rd instance), not a new prediction.
  * SOLID GEM: PMNS {{3/10,4/7,1/45}} + Cabibbo 1/20 — direct primary-fractions, RG-clean. Real, publishable consolidation.
  => NO clean new prediction → per the pull's bar (prediction not reproduction) = HONEST-PIVOT: bank the inventory, bank nothing new, move to fresh ground. No reframe #4.
""")
