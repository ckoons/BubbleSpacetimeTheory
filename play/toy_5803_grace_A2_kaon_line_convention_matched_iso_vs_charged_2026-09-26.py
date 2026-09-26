#!/usr/bin/env python3
"""
Toy 5803 — Grace, 2026-09-26 (round 5, item 2 + Cal item 2 input).

WHAT I OWN: R163 (09-25) wrote "A2 predicts f_K±/f_π± = 0.27679·√19 = 1.2065(15)"
and put it 5.4σ above FLAG 2+1+1 1.1934(19). 0.27679 is the ISOSPIN-LIMIT
K_μ2/π_μ2 product (PDG 2026 Vud/Vus Eq. 67.15, paired there with the isospin-limit
F_K/F_π = 1.1978; Cirigliano et al. 2022, a2208.11707.txt:135-136). FLAG's
1.1934 is the isospin-BROKEN charged ratio in QCD (flag.txt:3425, :4119). The
5.4σ compared two conventions.

KILL LINE (candidate, re-keyed; Cal rules the word): A2 dies on the K_μ2 route if a
CONVENTION-MATCHED lattice ratio sits > 5σ from its A2 value with the experimental
product unchanged.

DIRECTION BEFORE NUMBERS: matching conventions REDUCES the tension (the charged
product 0.27599 is smaller than 0.27679 by about the same fraction as 1.1934 is
smaller than 1.1978). Predictions:
  P1 convention-matched charged tension (FLAG 2+1+1) is below 5σ and above 3σ.
  P2 convention-matched isospin-limit tension (Cirigliano 1.1978) is below 5σ and above 3σ.
  P3 the newest single lattice results (Hudspith 2026, Conigli 2025) are within 3σ
     in their own convention.
  C1 control: 1.1978·√(1 − 0.0073) reproduces 1.1934 to 0.0002 (ETM δSU(2), flag.txt:4110).
  C2 control: 0.27679/1.1978 reproduces PDG's |Vus/Vud| 0.23108 (Eq. 67.17) to 1e-5.
"""
from math import sqrt

r19 = sqrt(19.0)
# products |Vus/Vud| f_K/f_pi
P_iso, eP_iso = 0.27679, sqrt(0.00028**2 + 0.00020**2)      # PDG rev-vud-vus Eq. 67.15 (:209)
P_ch,  eP_ch  = 0.27599, sqrt(0.00033**2 + 0.00024**2)      # PDG rev-pseudoscalar Eq. 71.9 (:268, :283)

A_iso, eA_iso = P_iso * r19, eP_iso * r19
A_ch,  eA_ch  = P_ch * r19,  eP_ch * r19
print(f"A2 isospin-limit F_K/F_pi = {A_iso:.4f}({eA_iso*1e4:.0f})")
print(f"A2 charged    f_K+/f_pi+ = {A_ch:.4f}({eA_ch*1e4:.0f})\n")

charged = [("FLAG 2+1+1 avg", 1.1934, 0.0019, "flag.txt:4119"),
           ("ETM 21", 1.1957, sqrt(44**2 + 7**2) * 1e-4, "flag.txt:3886"),
           ("CalLat 20", 1.1942, sqrt(32**2 + 31**2) * 1e-4, "flag.txt:3887"),
           ("FNAL/MILC 17", 1.1950, sqrt(15**2 + 18**2) * 1e-4, "flag.txt:3888"),
           ("HPQCD 13A", 1.1916, sqrt(15**2 + 16**2) * 1e-4, "flag.txt:3895"),
           ("Hudspith 2026", 1.1962, 0.0034, "a2605.06560.txt:161"),
           ("Conigli 2025 (2+1)", 1.1848, sqrt(59**2 + 84**2 + 24**2) * 1e-4, "a2512.19294.txt:800")]
iso = [("Cirigliano 2022 avg (=PDG 1.1978)", 1.1978, 0.0022, "a2208.11707.txt:135"),
       ("Hudspith 2026 iso", 1.1984, sqrt(23**2 + 7**2 + 17**2 + 17**2) * 1e-4, "a2605.06560.txt:147"),
       ("Conigli 2025 iso", 1.1872, 0.0103, "a2512.19294.txt:915")]

def sig(a, ea, x, ex): return (a - x) / sqrt(ea**2 + ex**2)
out = {}
print("CHARGED (isospin-broken QCD) vs A2 charged:")
for n, x, e, s in charged:
    out[n] = sig(A_ch, eA_ch, x, e)
    print(f"  {n:34s} {x:.4f}({e*1e4:.0f})  {out[n]:+.2f} sigma   old mixed: {sig(A_iso,eA_iso,x,e):+.2f}   {s}")
print("ISOSPIN LIMIT vs A2 iso:")
for n, x, e, s in iso:
    out[n] = sig(A_iso, eA_iso, x, e)
    print(f"  {n:34s} {x:.4f}({e*1e4:.0f})  {out[n]:+.2f} sigma   {s}")

score = total = 0
def check(label, ok):
    global score, total
    total += 1; score += ok
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
print()
f = out["FLAG 2+1+1 avg"]; c = out["Cirigliano 2022 avg (=PDG 1.1978)"]
check(f"P1 charged FLAG tension in (3,5): {f:.2f}", 3 < f < 5)
check(f"P2 iso Cirigliano tension in (3,5): {c:.2f}", 3 < c < 5)
nw = [out["Hudspith 2026"], out["Conigli 2025 (2+1)"], out["Hudspith 2026 iso"], out["Conigli 2025 iso"]]
check(f"P3 newest single results within 3 sigma: {[round(v,2) for v in nw]}", all(v < 3 for v in nw))
check(f"C1 1.1978*sqrt(1-0.0073) = {1.1978*sqrt(1-0.0073):.4f} vs 1.1934", abs(1.1978*sqrt(1-0.0073) - 1.1934) < 2e-4)
check(f"C2 0.27679/1.1978 = {P_iso/1.1978:.5f} vs 0.23108", abs(P_iso/1.1978 - 0.23108) < 1e-5)
print(f"\nSCORE {score}/{total}")
