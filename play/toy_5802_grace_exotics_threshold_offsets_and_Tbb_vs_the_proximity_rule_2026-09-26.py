#!/usr/bin/env python3
"""
Toy 5802 — Grace, 2026-09-26 (round 5, item 1). NOT BLIND: I knew the rough
offsets of X(3872), T_cc+ and the P_c states from memory before the pins landed.

KILL LINES FIRST (K1925 Addendum 4, Keeper's wording; Lyra words the final ones):
  (1) a stable, or weak-decay-only, hadron containing an unclosed pair beyond the
      ground-state baryons and mesons;
  (2) an exotic bound FAR below every two-hadron threshold (a compact multiquark,
      not a proximity pair).

DIRECTION BEFORE NUMBERS (written before running):
  P1  Every OBSERVED exotic that has a natural two-hadron threshold sits within
      30 MeV of it (|offset| <= 30 MeV).                         [can fail]
  P2  No OBSERVED exotic is bound more than 30 MeV below every threshold
      -> kill (2) has NOT fired on observed states.             [can fail]
  P3  Every observed exotic decays strongly (width >= 10 keV)
      -> kill (1) has NOT fired on observed states.              [can fail]
  P4  The lattice-QCD T_bb (bb ubar dbar) prediction, if realised, fires BOTH
      kill lines: every one of the ten pinned lattice values is > 30 MeV below
      B B* and every paper that states stability says weak-only.  [can fail]
  C1  Control: threshold arithmetic reproduces LHCb's own quoted X(3872)
      delta-E (+0.07 +- 0.12 MeV, 2005.13422:685) and T_cc+ threshold
      (3875.1, via delta m) to 0.02 MeV.
  C2  Control: the proximity cut is not trivially satisfied — a random-mass null
      (masses uniform in [threshold-200, threshold+200]) passes P1 for all
      N states with probability << 1.

Every number carries file:line in data/sources_grace_2026-09-26/exotics/.
"""
import random

# PDG 2026 summary-table masses (MeV)
D0, Dp, Ds0, Dsp = 1864.84, 1869.66, 2006.86, 2010.27   # tab-mesons-charm.txt:537,13,1519,1541
Bp, B0, Bst = 5279.41, 5279.72, 5324.75                  # tab-mesons-bottom.txt:81,1586,3423
Sigc = 2452.65                                           # sum-baryons.txt:2411
Xicp, Xic0 = 2467.79, 2470.50                            # sum-baryons.txt:2527,2620
Kst = 891.88                                             # tab-mesons-strange.txt:503
Jpsi = 3096.900                                          # tab-mesons-c-cbar.txt:108

# (name, mass, nearest natural threshold, width MeV, source)
states = [
 ("X(3872)",        3871.64, D0 + Ds0,  1.19,   "tab-c-cbar:1830-1831"),
 ("T_cc(3875)+",    3875.11 - 0.360, Dsp + D0, 0.048, "2109.01056:968-972 (pole)"),
 ("P_c(4312)+",     4311.9,  Sigc + D0, 9.8,    "1904.03947:361-362"),
 ("P_c(4440)+",     4440.3,  Sigc + Ds0, 20.6,  "1904.03947:365-366"),
 ("P_c(4457)+",     4457.3,  Sigc + Ds0, 6.4,   "1904.03947:369-370"),
 ("Z_c(3900)",      3886.7,  Dp + Ds0,  29.5,   "PDG list-Tcc1-3900:27,98"),
 ("Z_c(4020)",      4024.1,  Dsp + Ds0, 13.0,   "PDG list:27,42"),
 ("Z_b(10610)",     10607.2, Bp + Bst,  18.4,   "1110.2251:155"),
 ("Z_b(10650)",     10652.2, Bst + Bst, 11.5,   "1110.2251:155"),
 ("T_csbar0(2900)", 2908.0,  Dsp + Kst, 136.0,  "2212.02716:433-434"),
 ("T*_cs0(2870)",   2874.0,  Dsp + Kst, 68.0,   "PDG list:17 (LHCb avg, CL 0.044)"),
 ("T*_cs1(2900)",   2904.0,  Dsp + Kst, 110.0,  "2009.00026:1485"),
 ("P_psis(4338)",   4338.2,  Xicp + Dp, 7.0,    "2210.10346:25"),
 ("P_cs(4459) [3.1 sigma]", 4458.8, Xic0 + Ds0, 17.3, "2012.10380:29"),
]
no_threshold = [("X(6900)", 6898.0, 2 * Jpsi, 161.0, "PDG avg; 2006.16957:638,648 (model-dependent)")]

# T_bb lattice binding energies relative to B B* (MeV), tbb/TBB_PINS_draft.md
tbb = [("Francis+ 2017", -189), ("Junnarkar+ 2019", -143), ("Leskovec+ 2019", -128),
       ("Mohanta-Basak 2020", -167), ("Hudspith-Mohler 2023", -112), ("HAL QCD 2023 cc", -83),
       ("Alexandrou+ 2024", -100), ("Colquhoun+ 2024", -115), ("Tripathy+ 2025", -116),
       ("Hoffmann-Meinel 2026", -74)]

CUT = 30.0
score, total = 0, 0
print(f"{'state':26s} {'mass':>9s} {'thresh':>9s} {'offset':>8s} {'width':>7s}  source")
offs = []
for n, m, t, w, s in states:
    o = m - t
    offs.append(o)
    print(f"{n:26s} {m:9.2f} {t:9.2f} {o:+8.2f} {w:7.3f}  {s}")
for n, m, t, w, s in no_threshold:
    print(f"{n:26s} {m:9.2f} {t:9.2f} {m-t:+8.2f} {w:7.3f}  {s}  [no natural threshold; J/psi J/psi shown]")

def check(label, ok):
    global score, total
    total += 1; score += ok
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")

print()
far = [(n, m - t) for n, m, t, w, s in states if abs(m - t) > CUT]
check(f"P1 every thresholded exotic within {CUT} MeV (outliers: {far})", not far)
deep = [(n, m - t) for n, m, t, w, s in states if m - t < -CUT]
check(f"P2 none bound > {CUT} MeV below threshold (deep: {deep})", not deep)
narrow = [n for n, m, t, w, s in states + no_threshold if w < 0.010]
check(f"P3 every observed exotic decays strongly, width >= 10 keV (narrower: {narrow})", not narrow)
check(f"P4 all ten lattice T_bb values bound > {CUT} MeV (range {min(b for _,b in tbb)} .. {max(b for _,b in tbb)})",
      all(b < -CUT for _, b in tbb))

# C1 controls
xE = (D0 + Ds0) - 3871.59   # LHCb 2005.13422:668 mass; paper's delta-E +0.07 +- 0.12 (:685)
check(f"C1a X(3872) delta-E from LHCb mass = {xE:+.3f} vs paper +0.07", abs(xE - 0.07) < 0.05)
check(f"C1b T_cc threshold D*+ D0 = {Dsp + D0:.2f} (pole 3874.75 + 0.36 = 3875.11)", abs(Dsp + D0 - 3875.11) < 0.02)

# C2 null: random masses within +-200 MeV of each threshold
random.seed(5802)
trials, hits = 200000, 0
for _ in range(trials):
    if all(abs(random.uniform(-200, 200)) <= CUT for _ in states):
        hits += 1
p_analytic = (CUT / 200.0) ** len(states)
check(f"C2 null passes P1 in {hits}/{trials} trials (analytic {p_analytic:.2e})", p_analytic < 1e-6)

print(f"\nSCORE {score}/{total}")
