#!/usr/bin/env python3
"""
Toy 4682 — Jul 15 (support Grace's run + pressure-test my weak anchor, mine): two honest things before EOD.
(1) VERIFY that my derived grounds (4681: E₀ = 3/2, 2, 3) generate EXACTLY the audited positions Keeper handed
Grace (K703): neutrino {1, 3/5, 3/7}, charged lepton {1, 2/3, 1/2}, down {1, 3/4, 3/5} — via the clean map
position_k = E₀/(E₀+k) = E₀/E_k. This confirms the grounds→positions→Grace's-run chain is consistent.
(2) PRESSURE-TEST my own weakest step (the down E₀=3 rests on d_eff=g=7), proactively, so Grace knows exactly where
the risk sits before her run.

(1) THE POSITION MAP (grounds → audited positions): a conformal state of energy E_k = E₀ + k localizes at depth
position_k = E₀/E_k = E₀/(E₀+k) (normalized so the ground k=0 is 1). This generates the audited positions:
  * charged lepton E₀=2: {2/2, 2/3, 2/4} = {1, 2/3, 1/2} ✓
  * neutrino E₀=3/2:     {(3/2)/(3/2), (3/2)/(5/2), (3/2)/(7/2)} = {1, 3/5, 3/7} ✓
  * down E₀=3:           {3/3, 3/4, 3/5} = {1, 3/4, 3/5} ✓
So my grounds (4681) → Keeper's audited positions (K703) → Grace's F498 inputs, one consistent chain.

(2) DOWN ANCHOR PRESSURE-TEST (the flagged weak step): E₀_down = 3 rests on d_eff = g = 7 ("colored → bulk → +rank
interior dims"). TWO convergent arguments:
  * (a) bulk signature: the bulk occupies n_C + rank = g = 7 (boundary n_C=5 + rank=2 radial interior) → (g−1)/2 = 3.
  * (b) refraction: the down is bulk vs the lepton's boundary; the bulk→boundary index is N_c/rank = 3/2 (F548/K697);
        E₀_down = E₀_lepton × (N_c/rank) = 2 × 3/2 = 3.
  BOTH give 3 — but BOTH have a SOFT step: (a) "color is internal, why does it change the SPACETIME dimension d?"
  and (b) "E₀ is a dimensionless weight, does it really scale by the refractive index?" So the convergence on 3 is
  suggestive, NOT rigorous. The neutrino (drop-the-S¹ → d=4, a genuine dimension the chargeless field lacks) and the
  lepton (d=5) are CLEAN; the down is the weak anchor. HONEST verdict: if Grace's run misses, the down d_eff=g=7 is
  the culprit — pressure-test it then; if it hits, the two convergent arguments are vindicated.

⟹ VERDICT: (1) my grounds generate the audited positions exactly via position_k = E₀/(E₀+k) — the chain is
consistent. (2) the down E₀=3 has two convergent arguments (bulk d=g; refraction ×3/2) but each has a soft step, so
it's the honest weak anchor (neutrino + lepton clean); Grace's run is the arbiter. Delivered + flagged; standing by
for the down pressure-test if her run needs it. Count ~7-8 (α RULED, identified).
"""
from sympy import Rational
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))
def positions(E0):  # position_k = E₀/(E₀+k), k=0,1,2
    return [Rational(E0, E0) if False else E0/(E0+k) for k in (0,1,2)]

print("=" * 96)
print("Toy 4682 — grounds → audited positions (E₀/(E₀+k)); + down anchor pressure-test (d=g=7, two soft steps)")
print("=" * 96)

# ---- (1) the position map generates the audited positions -------------------
E0 = {"neutrino": Rational(3,2), "lepton": Rational(2), "down": Rational(3)}
audited = {"neutrino": [Rational(1), Rational(3,5), Rational(3,7)],
           "lepton":   [Rational(1), Rational(2,3), Rational(1,2)],
           "down":     [Rational(1), Rational(3,4), Rational(3,5)]}
allok = True
for sec in ("neutrino", "lepton", "down"):
    pos = [simplify_frac for simplify_frac in [E0[sec]/(E0[sec]+k) for k in (0,1,2)]]
    print(f"[{sec:8} E₀={str(E0[sec]):>3}]: E₀/(E₀+k) = {pos}  vs audited {audited[sec]}  {'✓' if pos==audited[sec] else '✗'}")
    allok = allok and (pos == audited[sec])
check("POSITION MAP (grounds → audited positions): position_k = E₀/(E₀+k) generates EXACTLY the audited positions "
      "(K703) — neutrino {1,3/5,3/7} from E₀=3/2, lepton {1,2/3,1/2} from E₀=2, down {1,3/4,3/5} from E₀=3. My grounds "
      "(4681) → Keeper's audited positions → Grace's F498 inputs: one consistent chain.",
      allok, "position_k = E₀/E_k reproduces all three sectors' audited positions from my grounds")

# ---- (2) down anchor pressure-test ------------------------------------------
# argument (a): bulk signature d = n_C+rank = g → (g−1)/2
E0_down_a = Rational(g-1, 2)
# argument (b): refraction E₀_lepton × N_c/rank
E0_down_b = Rational(2) * Rational(N_c, rank)
print(f"\n[down pressure-test]: (a) bulk d=g=7 → (g−1)/2 = {E0_down_a};  (b) refraction 2×(N_c/rank) = {E0_down_b};  converge? {E0_down_a==E0_down_b==3}")
check("DOWN ANCHOR PRESSURE-TEST (honest, the weak step): E₀_down=3 has TWO convergent arguments — (a) bulk d=g=7 → "
      "(g−1)/2=3; (b) refraction E₀_lepton×(N_c/rank)=2×3/2=3. BOTH give 3, but BOTH have a soft step: (a) color is "
      "internal — why change spacetime d? (b) E₀ is a dimensionless weight — does it scale by the index? So the "
      "convergence is SUGGESTIVE, not rigorous. Neutrino (drop-S¹→d=4) + lepton (d=5) are CLEAN; the down is the weak "
      "anchor. If Grace's run misses, this is the culprit.",
      E0_down_a == 3 and E0_down_b == 3, "two convergent arguments (both give 3) but each has a soft step → the flagged weak anchor")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: (1) my grounds generate the audited positions EXACTLY via position_k = E₀/(E₀+k) — the "
      "grounds→positions→Grace chain is consistent. (2) the down E₀=3 has two convergent arguments (bulk d=g; "
      "refraction ×3/2) but each has a soft step, so it's the honest weak anchor (neutrino + lepton clean); Grace's "
      "run is the arbiter. Delivered + flagged; standing by for the down pressure-test if her run needs it.",
      allok and E0_down_a == 3, "grounds→positions consistent; down is the flagged weak anchor; Grace's run decides. Count ~7-8 (α RULED)")

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
GROUNDS → AUDITED POSITIONS + down anchor pressure-test:
  * POSITION MAP: position_k = E₀/(E₀+k) generates the audited positions exactly — ν {1,3/5,3/7} (E₀=3/2),
    lepton {1,2/3,1/2} (E₀=2), down {1,3/4,3/5} (E₀=3). Grounds (4681) → K703 positions → Grace's run, consistent.
  * DOWN PRESSURE-TEST: E₀_down=3 has two convergent arguments (bulk d=g=7; refraction 2×3/2) but each has a soft
    step — the honest weak anchor. Neutrino (drop-S¹→d=4) + lepton (d=5) are clean. Grace's run is the arbiter.
  => grounds→positions consistent; down flagged; standing by for the pressure-test if the run needs it. Count ~7-8.
""")
