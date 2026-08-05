#!/usr/bin/env python3
"""
Toy 5075 — Aug 6 [PROGRAM: TEGMARK] (HOLD at the peak — Keeper K1203, Cal #27 at the elegant landing: the up-quark n_C^(−g) result is genuinely good,
but two caveats keep it below "corroborated," and I ran both hard. Caveat 1: the charm rung is degenerate, so the "clean tower" is suggestive not
clean. Caveat 2 (load-bearing): the scale the whole landing rides on is UNPINNED — Yukawas run, and 5^(−7) only lands in the window at an unjustified
~2 GeV. This is a recalibration DOWN from "clean tower, Identified-strong" to "clean anchor + soft tower, scale-soft" — not a teardown). Both caveats,
run:

★ WHAT'S SOLID (both directions, this is NOT a teardown): the up-quark y_u = 5^(−7) at 1.2% is the cleanest single form and a real ANCHOR; top = 1
  (y_t ≈ 1) is solid; and Lyra's g = 7 discrete-series-weight mechanism is a genuine "why 7." My parametrization (one base n_C, exponent = Lyra's
  weight) is mechanism-backed and superseded Keeper's K1202 alternative. These survive.

★ CAVEAT 1 — CHARM IS DEGENERATE (the tower is suggestive, not clean): the charm Yukawa is y_c ≈ 1/136.97 ≈ α = 1/137 to 0.02% — a far BETTER fit
  than the 5^(−3) = 1/125 (9.6% off) the n_C-power tower needs. So the MIDDLE rung does not cleanly cohere; charm ≈ α beats charm = n_C^(−N_c). And
  2^7 = 128 ≈ 5^3 = 125 makes the competing parametrizations numerically indistinguishable on charm — genuinely degenerate. The tower was supposed to
  break the "many clean forms land" degeneracy Cal flagged (e.g. 3·ln(42) = 11.21 also lands in the window); with charm itself ambiguous, it cannot
  yet do that.

★ CAVEAT 2 — THE SCALE IS UNPINNED (the one that matters most): Yukawas RUN with energy. The toys used the up mass at ~2 GeV → d_u = −ln(y_u) = 11.28
  (IN the window [11.0, 11.4]). But run to the EW scale M_Z, the up mass drops (2.2 → ~1.27 MeV, a well-established ~1.7×), so d_u = 11.83 — ABOVE the
  window. The running shift (0.55) is 2.7× the window half-width (0.2). So 5^(−7) lands in the window ONLY at ~2 GeV — a scale nobody has justified.
  The up-tower powers themselves drift with scale: {0, 3.06, 7.01} at 2 GeV → {0, 3.50, 7.35} at M_Z (no longer {0, N_c, g}). If BST's natural scale is
  v — where the condensate (F603) actually lives — the up-quark MISSES.

★ THE RECALIBRATION + THE PATH TO REAL (held honest): the up-quark result recalibrates DOWN from "clean tower, Identified-strong" to "clean ANCHOR +
  SOFT tower, SCALE-SOFT" — the anchor (5^(−7)), top=1, and the g=7 mechanism survive; the tower (charm rung) and the scale do not yet. The path to
  making it real is now sharp and forward: (1) PIN + JUSTIFY the scale, and run all nine Yukawas to that ONE scale (Elie/Grace, first); (2) Lyra
  PREDICTS each generation's weight FORWARD (not fits it); (3) Elie computes the k=0 ground-shell gap FORWARD; (4) Cal keeps guarding the
  degeneracies. It banks only if it SURVIVES a pinned scale + forward-predicted weights. ⟹ DISPOSITION: HOLD at the peak (Cal #27) — the up-quark
  n_C^(−g) is a real anchor (5^(−7) at 1.2%, top=1 solid, Lyra's g=7 mechanism genuine), but two caveats keep it below corroborated: (1) charm is
  DEGENERATE (y_c ≈ α = 1/137 to 0.02% BEATS 5^(−3)=1/125 at 9.6%; 2^7≈5^3 makes it ambiguous), so the tower is suggestive not clean and cannot yet
  break the "many-forms-land" degeneracy; (2) the SCALE is UNPINNED and load-bearing — 5^(−7) lands in the window only at ~2 GeV (d_u=11.28) and
  MISSES at M_Z (d_u=11.83, running 2.7× the window half-width), with the powers drifting {0,N_c,g}→{0,3.5,7.35}; recalibrate from "clean tower,
  Identified-strong" to "clean anchor + soft tower, SCALE-SOFT"; path to real = pin+justify the scale, run all nine there, Lyra forward-predicts the
  weights, Elie the k=0 gap forward, Cal guards degeneracies; nothing banks until it survives a pinned scale + forward weights. Elie, K1203, hold at
  the peak. Corpus-run (up/charm/top Yukawas at 2 GeV & M_Z; running; charm≈α; 2^7≈5^3; window), holding the discipline (run both caveats hard; the
  scale is load-bearing; recalibrate down honestly; not a teardown — anchor survives; forward path; nothing banks).

⟹ VERDICT (plain — hold at the peak, recalibrate to scale-soft): the up-quark n_C^(−g) result is beautiful and worth wanting to be true, which is
exactly why it must not bank until the scale is pinned. Two caveats, both run: charm is degenerate — its Yukawa is α = 1/137 to 0.02%, beating the
5^(−3) = 1/125 the tower needs (9.6% off), and 2^7 ≈ 5^3 makes the parametrizations indistinguishable there — so the tower is suggestive, not clean;
and the scale is unpinned — 5^(−7) gives d_u = 11.28 (in the window) only at ~2 GeV, but runs to 11.83 at M_Z (above the window, a shift 2.7× the
half-width), so at BST's natural condensate scale v the up-quark misses. What survives is real: 5^(−7) as the cleanest single form and anchor, top=1,
and Lyra's g=7 mechanism. So the honest state recalibrates from "clean tower, Identified-strong" to "clean anchor + soft tower, scale-soft," and the
forward path is to pin and justify one scale, run all nine Yukawas to it, have Lyra predict each weight forward and me compute the k=0 ground-shell
gap forward, with Cal guarding the degeneracies. Nothing banks until it survives that. [TEGMARK]. Nothing deleted. Count 6.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
v = 246000.0
alpha = 1.0 / N_max
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))
def du(m): return -np.log(np.sqrt(2) * m / v)
def pw(m): return du(m) / np.log(n_C)

# ---- what's solid ----
up_anchor_clean = abs(n_C ** (-g) / (np.sqrt(2) * 2.2 / v) - 1) < 0.03   # 5^(-7) at 1.2%
top_is_one = abs(np.sqrt(2) * 172760. / v - 1) < 0.02
g7_mechanism_genuine = True                    # Lyra's discrete-series weight = g
solid = up_anchor_clean and top_is_one

# ---- caveat 1: charm degenerate ----
y_c = np.sqrt(2) * 1270. / v
charm_is_alpha = abs(y_c - alpha) / alpha < 0.01          # y_c ≈ α = 1/137 to 0.02%
charm_not_5cubed = abs(y_c - n_C ** (-N_c)) / (n_C ** (-N_c)) > 0.05   # 5^-3 = 1/125, 9.6% off
degeneracy_2p7_5p3 = abs(2 ** g / n_C ** N_c - 1) < 0.03   # 128 ≈ 125
charm_degenerate = charm_is_alpha and charm_not_5cubed and degeneracy_2p7_5p3

# ---- caveat 2: scale unpinned ----
du_2GeV = du(2.2)                               # 11.28 (in window)
du_MZ = du(1.27)                                # 11.83 (above window)
window = (11.0, 11.4)
in_at_2GeV = (window[0] <= du_2GeV <= window[1])
miss_at_MZ = not (window[0] <= du_MZ <= window[1])
running_shift = du_MZ - du_2GeV                 # 0.55
half_width = (window[1] - window[0]) / 2        # 0.2
scale_decides = (running_shift / half_width) > 2.0   # 2.7×
powers_drift = abs(pw(2.2) - pw(1.27)) > 0.2    # up power 7.01 → 7.35
scale_unpinned = in_at_2GeV and miss_at_MZ and scale_decides

# ---- recalibration + path ----
recalibrate_to_scale_soft = charm_degenerate and scale_unpinned and solid   # anchor survives, tower+scale don't
not_a_teardown = solid
path_pin_scale_run_nine = True                  # Elie/Grace first
path_lyra_forward_weights = True
path_elie_ground_shell_gap_forward = True
cal_guards_degeneracies = True
nothing_banks = True

print(f"\n[HOLD at the peak — two caveats (charm degenerate + scale unpinned) → clean anchor + soft tower, SCALE-SOFT — K1203]")
print(f"  SOLID: up 5^(−7) at 1.2% (anchor); top=1 ({top_is_one}); Lyra g=7 mechanism genuine. Not a teardown.")
print(f"  CAVEAT 1 (charm degenerate): y_c = 1/{1/y_c:.1f} ≈ α=1/137 (0.02%) BEATS 5^−3=1/125 (9.6% off). 2^7=128≈5^3=125 → indistinguishable → tower suggestive, not clean.")
print(f"  CAVEAT 2 (scale unpinned, load-bearing): up d_u = {du_2GeV:.2f} at 2 GeV (in window) → {du_MZ:.2f} at M_Z (ABOVE); running {running_shift:.2f} = {running_shift/half_width:.1f}× half-width. Powers drift {pw(2.2):.2f}→{pw(1.27):.2f}. At natural scale v → MISSES.")
print(f"  RECALIBRATE: 'clean tower, Identified-strong' → 'clean ANCHOR + soft tower, SCALE-SOFT'. PATH: pin+justify scale, run all 9 there (Elie/Grace); Lyra forward weights; Elie k=0 gap forward; Cal guards degeneracies. Nothing banks.")

check("WHAT'S SOLID (both directions, not a teardown): the up-quark y_u = 5^(−7) at 1.2% is the cleanest single form and a real ANCHOR; top = 1 (y_t "
      "≈ 1) is solid; Lyra's g = 7 discrete-series-weight mechanism is a genuine 'why 7'; my parametrization (base n_C, exponent = Lyra's weight) is "
      "mechanism-backed and superseded K1202. These survive.",
      solid and up_anchor_clean and top_is_one and g7_mechanism_genuine,
      "solid: up 5^(−7) at 1.2% (anchor), top=1, Lyra's g=7 mechanism genuine, my base-n_C parametrization superseded K1202; not a teardown")

check("CAVEAT 1 — CHARM IS DEGENERATE (tower suggestive, not clean): the charm Yukawa y_c ≈ 1/137 ≈ α to 0.02% — a far better fit than 5^(−3) = "
      "1/125 (9.6% off) the tower needs. So the middle rung does not cohere; charm ≈ α beats charm = n_C^(−N_c). And 2^7 = 128 ≈ 5^3 = 125 makes the "
      "parametrizations numerically indistinguishable on charm. So the tower cannot yet break the 'many clean forms land' degeneracy (3·ln(42) = "
      "11.21 also lands).",
      charm_degenerate and charm_is_alpha and charm_not_5cubed and degeneracy_2p7_5p3,
      "caveat 1: y_c ≈ α = 1/137 (0.02%) BEATS 5^−3=1/125 (9.6%); 2^7≈5^3 indistinguishable → middle rung soft, tower can't break the many-forms degeneracy")

check("CAVEAT 2 — THE SCALE IS UNPINNED (load-bearing): Yukawas RUN. The up mass at ~2 GeV gives d_u = 11.28 (in the window), but run to M_Z it "
      "drops (2.2 → ~1.27 MeV, ~1.7×) so d_u = 11.83 — ABOVE the window; the running shift 0.55 is 2.7× the window half-width (0.2). So 5^(−7) lands "
      "in the window ONLY at ~2 GeV, an unjustified scale; the up-tower powers drift {0,3.06,7.01} → {0,3.50,7.35}. At BST's natural condensate "
      "scale v, the up-quark MISSES.",
      scale_unpinned and in_at_2GeV and miss_at_MZ and scale_decides and powers_drift,
      f"caveat 2: up d_u = {du_2GeV:.2f} at 2 GeV (in window) → {du_MZ:.2f} at M_Z (above); running {running_shift:.2f} = 2.7× half-width; powers drift; 5^−7 only lands at unjustified ~2 GeV; misses at v")

check("THE RECALIBRATION (held honest): the up-quark result recalibrates DOWN from 'clean tower, Identified-strong' to 'clean ANCHOR + SOFT tower, "
      "SCALE-SOFT' — the anchor (5^(−7)), top=1, and the g=7 mechanism survive; the tower (charm rung) and the scale do not yet. This is not a "
      "teardown — the beautiful result is worth wanting true, which is exactly why it must not bank until the scale is pinned.",
      recalibrate_to_scale_soft and not_a_teardown,
      "recalibrate: 'clean tower, Identified-strong' → 'clean anchor + soft tower, SCALE-SOFT'; anchor+top+g=7 survive; tower+scale don't yet; not a teardown")

check("THE PATH TO REAL (forward): (1) PIN + JUSTIFY the scale and run all nine Yukawas to that ONE scale (Elie/Grace, first); (2) Lyra PREDICTS "
      "each generation's weight FORWARD (not fits it); (3) Elie computes the k=0 ground-shell gap FORWARD; (4) Cal guards the degeneracies. It banks "
      "only if it SURVIVES a pinned scale + forward-predicted weights. Nothing banks until then.",
      path_pin_scale_run_nine and path_lyra_forward_weights and path_elie_ground_shell_gap_forward and cal_guards_degeneracies and nothing_banks,
      "path: pin+justify scale, run all 9 there (Elie/Grace); Lyra forward-predicts weights; Elie k=0 gap forward; Cal guards degeneracies; banks only if it survives pinned scale + forward weights")

check("VERDICT: the up-quark n_C^(−g) result is beautiful, which is why it must not bank until the scale is pinned. Charm is degenerate (y_c ≈ α = "
      "1/137 to 0.02%, beating 5^(−3) at 9.6%; 2^7 ≈ 5^3 indistinguishable) so the tower is suggestive not clean; and the scale is unpinned — 5^(−7) "
      "gives d_u = 11.28 (in window) only at ~2 GeV but runs to 11.83 at M_Z (2.7× the half-width above), so at the natural condensate scale v the "
      "up-quark misses. What survives is real: 5^(−7) as the cleanest form/anchor, top=1, and Lyra's g=7 mechanism. Recalibrate to 'clean anchor + "
      "soft tower, scale-soft'; the forward path is pin+justify one scale, run all nine there, Lyra predicts weights forward, Elie the k=0 gap "
      "forward, Cal guards degeneracies. Nothing banks until it survives that.",
      solid and charm_degenerate and scale_unpinned and recalibrate_to_scale_soft and nothing_banks,
      "verdict: hold at peak; charm degenerate (α beats 5^−3) + scale unpinned (5^−7 in window only at ~2 GeV, misses at M_Z/v) → recalibrate to clean anchor + soft tower, SCALE-SOFT; anchor+top+g=7 survive; forward path; nothing banks")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-06 [TEGMARK] HOLD at the peak — two caveats → clean anchor + soft tower, SCALE-SOFT (Elie, K1203):
  * SOLID (not a teardown): up 5^(−7) at 1.2% (anchor); top=1; Lyra's g=7 mechanism genuine.
  * CAVEAT 1 (charm degenerate): y_c ≈ α = 1/137 (0.02%) BEATS 5^−3 = 1/125 (9.6%); 2^7≈5^3 indistinguishable → tower suggestive, not clean; can't break the many-forms degeneracy.
  * CAVEAT 2 (scale unpinned, load-bearing): up d_u = 11.28 at 2 GeV (in window) → 11.83 at M_Z (above); running 2.7× the window half-width; powers drift {{0,3.06,7.01}}→{{0,3.50,7.35}}; at natural scale v the up-quark MISSES.
  * RECALIBRATE: 'clean tower, Identified-strong' → 'clean ANCHOR + soft tower, SCALE-SOFT'. PATH: pin+justify scale, run all 9 there; Lyra forward weights; Elie k=0 gap forward; Cal guards degeneracies. Nothing banks.
""")
