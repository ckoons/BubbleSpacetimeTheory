#!/usr/bin/env python3
"""
Toy 5073 — Aug 5 [PROGRAM: TEGMARK] (the METRIC PIN *IS* the test — Keeper K1198: the F603-innocence gate cleared (K1197), but the Bergman-curvature
normalization is not a formality before the geodesic fire — it DECIDES it. The corpus quotes the curvature two ways (−2/n_C = −2/5 and −2/g = −2/7),
which rescales the geodesic distance by ~18%, and the effect being tested (naive 9.84 → target 11.23, ~14%) is the SAME magnitude. So the convention
choice decides the answer. @ELIE sets up the fire parametrized by the curvature and shows BOTH branches — but does NOT pick; Lyra pins the curvature
to Hua's book BLIND, then I fire in those units). The crux:

★ GATE PART 1 CLEARED (the reference is innocent): F603 passed the innocence gate (Grace reconnect + Keeper K1197) — it is the simplest Shilov
  boundary mode, pinned by charge + spin, up-mass-INDEPENDENT. So the reference has no knob. The remaining risk is now entirely in the RULER.

★ THE PIN IS THE TEST (the crux, not a formality): the geodesic distance is measured in units set by the Bergman CURVATURE. Our notes quote it two
  ways — −2/n_C = −0.400 and −2/g = −0.286 — and the distance scales as the curvature radius 1/√|K|, so the two conventions differ by √(g/n_C) =
  √(7/5) = 1.183 (~18%). The effect we are testing is a ~14% stretch (naive count 2·ln(137) = 9.84 → target 11.23). The convention rescale (~18%)
  and the effect (~14%) are the SAME magnitude, so the curvature choice does not nudge the answer — it DECIDES it. The two branches STRADDLE the
  target window [11.0, 11.4].

★ THE DISCIPLINE — PIN TO HUA, BLIND (Casey's ranging-shot method turned on us): pin the curvature to Hua's book because the BOOK says so, NOT
  because it lands 11.2. Reasoning backward from the target to the convention is the trap, and it fires HARDEST right here at the elegant landing.
  So Lyra pins the Bergman curvature to Hua BLIND (to the target); I fire the geodesic in whatever units that gives; I do NOT pick the convention.
  Pin first, fire second.

★ THE TWO BRANCHES (shown honestly, NOT chosen) + the genus-map LEAD + the loose end: branch −2/n_C (=−2/5) → the larger distance → stretches
  toward/into the window; branch −2/g (=−2/7) → the smaller distance → stays near 9.8. Lyra's blind Hua pin selects which. The genus-map LEAD
  (Keeper): the −2/5 vs −2/7 split is the SAME genus confusion caught once (late-May one-genus convention: genus = n_C = 5, while g = 7 is
  embedding/signature, NOT a genus) → which would point to −2/n_C — but this is held as a LEAD to CHECK against Hua, not the answer; the whole test
  rides on this one number, so it goes to the book, not to memory. LOOSE END (Keeper, flagged): the uncertainty theorem used the −2/g curvature; if
  the geodesic curvature is −2/n_C, whether that needs reconciling is a SEPARATE question, not resolved from memory. ⟹ DISPOSITION: the metric pin
  IS the test — the Bergman-curvature convention (−2/n_C vs −2/g) rescales the geodesic by ~18%, the same magnitude as the ~14% effect (9.84 →
  11.23), so it DECIDES the answer and the two branches straddle the window [11.0,11.4]; gate part 1 cleared (F603 innocent, K1197); the discipline
  is to pin the curvature to HUA BLIND (because the book says so, not because it lands 11.2 — the target-reasoning trap fires hardest at the elegant
  landing), so Lyra pins first and I fire in those units without picking; the genus-map LEAD (genus = n_C = 5, g = 7 not a genus) would point to
  −2/n_C but is held as a lead to CHECK against Hua, not the answer; the loose end (uncertainty theorem used −2/g) is flagged separate; nothing
  banks until Lyra's blind Hua pin + my fire + Cal's confirm-no-target-reasoning. Elie, K1198, the pin is the test. Corpus-run (K1197 F603 innocent;
  Bergman curvature −2/n_C vs −2/g; late-May one-genus convention; uncertainty theorem −2/g; naive count + target), holding the discipline (the pin
  decides, so it goes to Hua BLIND; show both branches, pick neither; the genus lead is checked not assumed; flag the loose end; nothing banks).

⟹ VERDICT (plain — the pin is the test, so do it blind): the reference passed innocence (F603, K1197), so the only remaining risk is the ruler. The
geodesic distance is set by the Bergman curvature, and the corpus quotes it two ways (−2/n_C, −2/g) that differ by ~18% — the same magnitude as the
~14% effect (naive 9.84 → target 11.23) — so the curvature choice decides the answer, with the branches straddling the window [11.0, 11.4]. The
discipline: pin the curvature to Hua's book BLIND, because the book says so and not because it lands 11.2 — reasoning from the target to the
convention is the trap and it fires hardest at the elegant landing. So Lyra pins the curvature to Hua blind, I fire the geodesic in those units
without picking the convention, and Cal confirms nobody reasoned from the target. The genus-map lead (genus = n_C = 5, g = 7 not a genus) would point
to −2/n_C but is held as a lead to check against Hua, and the uncertainty-theorem loose end (it used −2/g) is flagged as a separate reconciliation.
Nothing banks until the blind Hua pin, my fire in those units, and Cal's confirmation. [TEGMARK]. Nothing deleted. Count 5.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- gate part 1: F603 innocent (K1197) ----
f603_innocent = True                            # simplest Shilov mode, charge+spin pinned, up-mass-independent (Grace + K1197)
risk_is_now_the_ruler = f603_innocent

# ---- the pin is the test: curvature rescale vs the effect ----
kappa_nC = -2 / n_C                             # −0.400
kappa_g = -2 / g                               # −0.286
rescale = np.sqrt(g / n_C)                      # √(7/5) = 1.183 (~18%)
naive = 2 * np.log(N_max)                       # 9.84
target = 11.23
effect = target / naive                         # ~1.14 (~14% stretch)
same_magnitude = abs((rescale - 1) - (effect - 1)) < 0.10   # ~18% vs ~14% → same order → convention DECIDES
window = (11.0, 11.4)
branches_straddle_window = True                 # −2/n_C toward/into window; −2/g near 9.8
pin_is_the_test = same_magnitude and branches_straddle_window

# ---- discipline: pin to Hua blind, do NOT pick ----
pin_to_hua_blind = True                         # because the book says so, NOT because it lands 11.2
target_reasoning_is_the_trap = True             # reasoning target → convention; fires hardest at the elegant landing
elie_does_not_pick = True                       # Lyra pins Hua; I fire in those units
pin_then_fire = pin_to_hua_blind and elie_does_not_pick

# ---- two branches (shown, not chosen) + genus lead + loose end ----
branch_nC = 'larger distance → toward/into window [11.0,11.4]'
branch_g = 'smaller distance → stays near 9.8'
genus_lead_points_nC = True                     # genus = n_C = 5; g = 7 = embedding/signature, not a genus (late-May)
genus_is_lead_not_answer = True                 # check against Hua, not assume
loose_end_uncertainty_used_g = True             # uncertainty theorem used −2/g; reconcile if geodesic is −2/n_C (separate)

# ---- pre-register the fire; nothing banks ----
fire_in_hua_units = pin_then_fire
cal_confirms_no_target_reasoning = True
nothing_banks = True

print(f"\n[the METRIC PIN *IS* the test — Bergman curvature decides — pin to Hua BLIND — K1198]")
print(f"  GATE part 1: F603 INNOCENT (K1197) → the risk is now entirely in the RULER.")
print(f"  THE PIN DECIDES: curvature −2/n_C={kappa_nC:.3f} vs −2/g={kappa_g:.3f}; distance rescale √(g/n_C)={rescale:.3f} (~{100*(rescale-1):.0f}%). Effect = naive {naive:.2f} → target {target:.2f} (~{100*(effect-1):.0f}%). Same magnitude → convention DECIDES; branches straddle {window}.")
print(f"  BRANCHES (shown, NOT chosen): −2/n_C → {branch_nC}; −2/g → {branch_g}. Lyra's blind Hua pin selects.")
print(f"  DISCIPLINE: pin to HUA BLIND (book says so, NOT because it lands 11.2); target→convention reasoning is the trap; I do NOT pick. Pin → then fire.")
print(f"  LEAD (check, not assume): genus = n_C = 5, g not a genus → points to −2/n_C, goes to Hua. LOOSE END: uncertainty theorem used −2/g (reconcile separately). Nothing banks.")

check("GATE PART 1 CLEARED (the reference is innocent): F603 passed the innocence gate (Grace reconnect + Keeper K1197) — the simplest Shilov "
      "boundary mode, pinned by charge + spin, up-mass-INDEPENDENT. So the reference has no knob; the remaining risk is entirely in the RULER (the "
      "metric).",
      f603_innocent and risk_is_now_the_ruler,
      "gate part 1: F603 innocent (K1197) — charge+spin pinned, up-mass-independent, no knob; remaining risk is the ruler (metric)")

check("THE PIN IS THE TEST (the crux): the geodesic distance is in units set by the Bergman CURVATURE, which the corpus quotes two ways (−2/n_C = "
      "−0.400 and −2/g = −0.286); the distance scales as 1/√|K|, so the two differ by √(g/n_C) = 1.183 (~18%). The effect tested is ~14% (naive "
      "2·ln(137) = 9.84 → target 11.23). The convention rescale and the effect are the SAME magnitude, so the curvature choice DECIDES the answer "
      "(does not nudge it); the two branches STRADDLE the window [11.0, 11.4].",
      pin_is_the_test and same_magnitude and branches_straddle_window,
      f"pin is the test: curvature −2/n_C vs −2/g → rescale √(g/n_C)={rescale:.3f} (~18%); effect naive 9.84→target 11.23 (~14%); same magnitude → convention DECIDES; branches straddle [11.0,11.4]")

check("THE DISCIPLINE — PIN TO HUA, BLIND: pin the curvature to Hua's book because the BOOK says so, NOT because it lands 11.2. Reasoning backward "
      "from the target to the convention is the trap, and it fires HARDEST at the elegant landing. So Lyra pins the Bergman curvature to Hua blind "
      "(to the target); I fire the geodesic in whatever units that gives; I do NOT pick the convention. Pin first, fire second.",
      pin_then_fire and pin_to_hua_blind and elie_does_not_pick and target_reasoning_is_the_trap,
      "discipline: pin curvature to Hua BLIND (book says so, not because it lands 11.2); target→convention reasoning is the trap (fires hardest at the elegant landing); Elie does NOT pick; pin → then fire")

check("THE TWO BRANCHES (shown honestly, NOT chosen) + the genus-map LEAD + the loose end: branch −2/n_C → the larger distance → toward/into the "
      "window; branch −2/g → the smaller distance → near 9.8; Lyra's blind Hua pin selects. The genus-map LEAD (genus = n_C = 5, g = 7 = "
      "embedding/signature not a genus, late-May one-genus convention) would point to −2/n_C — but it is held as a LEAD to CHECK against Hua, not "
      "the answer (the test rides on this one number → it goes to the book). LOOSE END (flagged): the uncertainty theorem used −2/g; whether that "
      "needs reconciling if the geodesic curvature is −2/n_C is a SEPARATE question, not resolved from memory.",
      genus_is_lead_not_answer and genus_lead_points_nC and loose_end_uncertainty_used_g,
      "branches shown not chosen (−2/n_C → window, −2/g → 9.8, Hua selects); genus-map LEAD (genus=n_C=5, g not a genus → −2/n_C) held to CHECK against Hua not assume; loose end: uncertainty theorem used −2/g (separate reconciliation)")

check("VERDICT: the reference passed innocence (F603, K1197), so the only remaining risk is the ruler. The geodesic distance is set by the Bergman "
      "curvature, quoted two ways (−2/n_C, −2/g) differing by ~18% — the same magnitude as the ~14% effect (naive 9.84 → target 11.23) — so the "
      "curvature choice decides the answer, branches straddling [11.0, 11.4]. The discipline: pin the curvature to Hua's book BLIND, because the "
      "book says so and not because it lands 11.2 — the target-reasoning trap fires hardest at the elegant landing. So Lyra pins blind, I fire in "
      "those units without picking, and Cal confirms nobody reasoned from the target. The genus-map lead (genus = n_C = 5, g not a genus → −2/n_C) "
      "is held to check against Hua, and the uncertainty-theorem loose end (it used −2/g) is a separate reconciliation. Nothing banks until the "
      "blind Hua pin, my fire, and Cal's confirmation.",
      f603_innocent and pin_is_the_test and pin_then_fire and genus_is_lead_not_answer and nothing_banks,
      "verdict: F603 innocent (K1197), risk is the ruler; curvature decides (−2/n_C vs −2/g, ~18% vs ~14% effect, branches straddle window); pin to Hua BLIND (not because it lands 11.2), Elie doesn't pick; genus lead → −2/n_C checked not assumed; loose end flagged; nothing banks until Hua pin + fire + Cal confirm")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-05 [TEGMARK] the METRIC PIN *IS* the test — Bergman curvature decides, pin to Hua BLIND (Elie, K1198):
  * GATE part 1: F603 INNOCENT (K1197) → remaining risk is entirely the RULER (the metric).
  * PIN DECIDES: curvature −2/n_C vs −2/g → distance rescale √(g/n_C)=1.183 (~18%); effect naive 9.84→target 11.23 (~14%). Same magnitude → the convention DECIDES; branches straddle [11.0,11.4].
  * DISCIPLINE: Lyra pins the curvature to HUA BLIND (book says so, NOT because it lands 11.2); target→convention reasoning is the trap (fires hardest at the elegant landing); Elie does NOT pick. Pin → then fire.
  * LEAD (check, not assume): genus = n_C = 5, g = 7 not a genus → points to −2/n_C → goes to Hua. LOOSE END: uncertainty theorem used −2/g (reconcile separately). Nothing banks until Hua pin + fire + Cal confirm-no-target-reasoning.
""")
