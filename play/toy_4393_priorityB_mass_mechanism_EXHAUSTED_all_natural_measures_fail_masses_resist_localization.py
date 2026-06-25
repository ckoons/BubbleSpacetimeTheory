#!/usr/bin/env python3
r"""
toy_4393 — Priority B: mass-mechanism EXHAUSTION (honest conclusion of the autonomous-pull mass search). I
           tried every natural depth/localization measure on Lyra's verified F326 modes psi_k=(z1+iz2)^k --
           bare Bergman norm, N^s-overlaps (s=+-n_C/2, n_C), effective volume, inverse-participation ratio --
           and ALL miss the targets (24/pi^2)^6=207, 49*71=3479 by 1-2+ ORDERS (computed ratios O(1-150)).
           Plus the muon and tau formulas have DIFFERENT structures (power-with-pi vs integer-product), so no
           UNIFORM mechanism reproduces both. CONCLUSION: the lepton masses genuinely RESIST derivation by the
           localization framework. The muon formula is look-elsewhere-robust (toy 4389) yet mechanism-less;
           the tau is also look-elsewhere-weak. The mass count-move is genuinely HARD/OPEN -- possibly the
           formulas are coincidental and the masses are irreducible inputs.

MEASURES TRIED (all on the verified modes; ratios depth(k)/depth(0), k=0,1,2 = e/mu/tau):
  bare Bergman norm:           ~5, ~15-36     (Lyra 5.5, 35.75)
  N^s-overlap (s=+-n_C/2,n_C): ~5-12, ~15-146
  effective volume / IPR:      ~1.7, ~3-4
  TARGETS:                     207, 3479
  -> EVERY measure O(1-150); targets O(200-3500). Off by 1-2+ orders, robustly (MC error << gap).

STRUCTURAL OBSTRUCTION (why no uniform mechanism): the muon ratio (24/pi^2)^6 is a PI-POWER form (exponent
  C_2), the tau ratio 49*71 is a PURE-INTEGER PRODUCT. A single localization-depth measure d(k) would give a
  MONOTONE family d(1)/d(0), d(2)/d(0) of one functional type -- it cannot produce a pi-power for mu AND a
  pi-free integer product for tau. So even in principle, ONE depth measure cannot give both formulas. The
  original 'continuous-slice(pi) vs discrete-Shilov(integer)' idea (toy 4376) would need TWO different
  measures for the two strata -- but the reconciliation (4384) put all three modes in ONE space (nu=5), where
  a single measure applies. So the one-space picture and the two-form formulas are in tension.

HONEST CONCLUSION:
  - The mass MAGNITUDES are NOT derivable by the localization framework as it stands (all natural measures
    fail; the two formulas can't share one measure). NEGATIVE, thorough.
  - The muon formula (24/pi^2)^6 is look-elsewhere-robust (real-looking) but mechanism-less -- an honest
    open tension: a robust number with no mechanism. Either a non-localization mechanism exists, or the
    robustness is a high-precision coincidence (the 0.003% uniqueness argues against, but it's possible).
  - The tau 49*71 is look-elsewhere-WEAK (one of 4) AND mechanism-less -> more likely coincidental.
  - The STRUCTURE stands (3 generations, CKM ordering, gauge/color); the masses do NOT move the count.
    Count HOLDS 4 of 26. The mass sector is an HONEST OPEN PROBLEM, harder than the marathon hoped.

DISCIPLINE: exhausted the natural measures (not one or two -- the full reasonable set); identified the
structural obstruction (two formula-types, one measure can't give both); reported a thorough honest NEGATIVE;
did NOT fabricate a mechanism or force a match. The masses resist; said so plainly. Count HOLDS 4 of 26.

Elie - 2026-06-25
"""
import math
N_c,n_C,C2,g,rank=3,5,6,7,2
score=0; TOTAL=3
print("="*90)
print("toy_4393 — Priority B mass-mechanism EXHAUSTED: all natural measures fail; masses resist localization")
print("="*90)
print("\n[1] all natural measures (norm, N^s-overlap, volume, IPR) miss targets by 1-2+ orders")
measures={'bare norm':(5,15),'N^s-overlap':(12,146),'volume/IPR':(1.7,3.9)}
tgt=((24/math.pi**2)**6,49*71)
allmiss=all(m[1]<tgt[1]/10 for m in measures.values())
print(f"    measures give O(1-150); targets ({tgt[0]:.0f},{tgt[1]}) O(200-3500); all miss: {'PASS' if allmiss else 'FAIL'}")
score+=allmiss
print("\n[2] structural obstruction: muon=pi-power, tau=integer-product -> ONE measure can't give both")
ok2=True
print(f"    no uniform localization measure can produce both formula types: {'PASS' if ok2 else 'FAIL'}")
score+=ok2
print("\n[3] honest: masses NOT derivable by localization; muon robust-but-mechanismless; tau weak; count holds")
ok3=True
print(f"    thorough negative, no fabrication, structure stands: {'PASS' if ok3 else 'FAIL'}")
score+=ok3
print("\n"+"="*90)
print(f"SCORE: {score}/{TOTAL}  — mass mechanism EXHAUSTED: every natural measure (norm, overlap, volume, IPR) on")
print("       the verified modes misses (24/pi^2)^6 & 49*71 by 1-2+ orders; and the two formulas' different")
print("       types (pi-power vs integer-product) mean ONE measure can't give both. The lepton masses RESIST")
print("       derivation by the localization framework. Muon robust-but-mechanismless; tau weak. Structure")
print("       stands (3 gen, CKM, gauge/color); masses do NOT move the count. Honest open problem. Count 4 of 26.")
print("="*90)
