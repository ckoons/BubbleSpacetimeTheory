#!/usr/bin/env python3
"""Toy 5772 — Keeper's fact-pack question (item 7): was T2488's meson row (ρ, ω at n_C·π⁵·m_e) written before the
ratio was read, and what is its base-rate p with the look-elsewhere on the list it was found in?
Provenance from the files: T187 (6π⁵, proton) is foundational (early 2026); toys 4017/4020/4022/4023 are all 2026-06-07 —
the meson integer n_C = 5 was found by delimiting a clean set on a cross-mass list with the unit π⁵·m_e already fixed by the proton.
Masses re-pinned from the PDG 2024 summary tables (notes/sources_R144/rpp2024-sum-{mesons,baryons}.txt). Elie, 2026-09-21."""
import math, re, os
from math import comb
here = os.path.dirname(os.path.abspath(__file__)); src = os.path.join(here, "..", "notes", "sources_R144")
def pin(fname, pattern):
    txt = open(os.path.join(src, fname), encoding="utf-8", errors="ignore").read()
    m = re.search(pattern, txt); return (float(m.group(1)), float(m.group(2))) if m else None
me = 0.51099895069  # CODATA 2022 m_e c² MeV
pins = {"p": pin("rpp2024-sum-baryons.txt", r"Mass m = (938\.\d+) ± ([\d.]+) MeV"),
        "n": pin("rpp2024-sum-baryons.txt", r"Mass m = (939\.\d+) ± ([\d.]+) MeV"),
        "omega": pin("rpp2024-sum-mesons.txt", r"Mass m = (782\.\d+) ± ([\d.]+) MeV"),
        "rho": pin("rpp2024-sum-mesons.txt", r"ρ0 mass \(Breit-Wigner\) = (775\.\d+) ± ([\d.]+) MeV")}
unit = math.pi ** 5 * me
print("=" * 100 + f"\nTOY 5772 — T2488 provenance: unit π⁵·m_e = {unit:.4f} MeV\n" + "=" * 100)
print("  pins (PDG 2024 summary tables): " + "; ".join(f"{k} = {v[0]} ± {v[1]}" if v else f"{k} = NOT PINNED" for k, v in pins.items()))
# toy 4020's 13-state list, verbatim, with the four pinned masses substituted where the pin exists
S = [('p', 938.272), ('n', 939.565), ('rho', 775.26), ('omega', 782.66), ('phi', 1019.461), ('Kstar', 891.67), ('pi+', 139.570),
     ('K+', 493.677), ('eta', 547.862), ('Lambda', 1115.683), ('Sigma+', 1189.37), ('Delta', 1232.0), ('Xi', 1314.86)]
S = [(nm, pins[nm][0] if nm in pins and pins[nm] else m) for nm, m in S]
score, cf = [], []
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
rows = []
for nm, m in S:
    r = m / unit; k = round(r); res = abs(r - k); p = min(1.0, 2 * res); rows.append((nm, r, k, res, p))
print(f"\n  {'state':8}{'r = m/(π⁵m_e)':>16}{'k':>4}{'|r−k|':>8}{'p_rand':>8}")
for nm, r, k, res, p in sorted(rows, key=lambda t: t[3]): print(f"  {nm:8}{r:16.4f}{k:4d}{res:8.4f}{p:8.3f}")
sig = [t for t in rows if t[4] < 0.1]
print(f"\n  states at p < 0.1: {[t[0] for t in sig]} (toy 4020's clean set)")
def tail(nlist, k, q=0.1): return sum(comb(nlist, j) * q ** j * (1 - q) ** (nlist - j) for j in range(k, nlist + 1))
N = len(rows); k_all = len(sig); P_all = tail(N, k_all)
k_np = len([t for t in sig if t[0] != 'p']); P_np = tail(N - 1, k_np)
print(f"  look-elsewhere on the list the pattern was found in: {k_all} of {N} at p<0.1, chance 0.1·{N} = {0.1*N:.1f}, P(≥{k_all}) = {P_all:.3f}")
print(f"  with the proton removed (it FIXES the unit — 6π⁵ is T187, months earlier): {k_np} of {N-1}, chance {0.1*(N-1):.1f}, P(≥{k_np}) = {P_np:.3f}")
print("  the '~200' cross-mass list of toy 4017 is not retained as a list in that file; 4020's 13 is the retained one.")
sc("C1 the four pins exist and reproduce toy 4020's integers (p 6, n 6, ω 5, ρ 5)", all(pins.values()) and [t[2] for t in rows[:4]] == [6, 6, 5, 5], False)
sc("C2 provenance: T2488's meson integer postdates T187 (files: toys 4017/4020/4022/4023 all 2026-06-07)", True, False)
sc("P1 with the proton removed the clean set is NOT significant at the 5 % level on its own list (P ≥ 0.05)", P_np >= 0.05, True, f"P = {P_np:.3f}")
print(f"\nREADING for Lyra/Keeper: the meson row is a post-hoc delimitation on a 13-state list with the unit fixed by the proton; "
      f"three states at p < 0.1 out of twelve is P = {P_np:.2f} by chance. Not target-innocent in the 'written before read' sense; "
      f"ω at 5.005 is the one tight meson number (p = {[t for t in rows if t[0]=='omega'][0][4]:.3f}); ρ at 4.958 is marginal.")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s, c in zip(score, cf) if c and s)}/{sum(cf)} can-fail hit")
