#!/usr/bin/env python3
"""
Toy 5810 — Grace, 2026-09-26, round 6, on Cal Section 992 (F): "A14 needs its class fixed
BEFORE δ is read ... take every PDG 2026 exotic and its nearest quantum-number-allowed
two-hadron threshold, and report k/N. Elie's 5802 null (±200 MeV windows) is the right base rate."

FROZEN BEFORE ANY δ IS COMPUTED (this file is hashed before its first run):
CLASS: every entry that PDG 2026 itself names "T" (its label for manifestly exotic minimal content) in
  the heavy-quarkonium review's Table 77.2 (states above the first open-flavour threshold) and Table 77.3
  (near it) — rpp2026-rev-heavy-quarkonium-spectroscopy.txt lines 445-520 and 674-712. 17 states.
  Masses are the table's central values; the Tcc̄s̄1(4000) range "3980 − 4010" is taken at its midpoint 3995.
  NOT BLIND to the masses (the table was read to build the class); blind to δ.
  Excluded by construction and said so: the P (pentaquark) states and T_cs states (not in these tables);
  the χ/ψ-named entries (PDG does not name them exotic).
THRESHOLDS: pairs of hadrons from the frozen lists below, masses from PDG 2026 summary tables (file:line).
  "Allowed" = flavour content and charge only (J^PC and isospin NOT imposed — named as the limit; it
  makes thresholds DENSER, so it can only make the null easier to beat, not harder).
  V_OPEN: open-flavour pairs only (the molecular channels: D(*)D̄(*), D_s(*)D̄_s(*), D_s(*)D̄(*), D(*)D(*), B(*)B̄(*)).
  V_ALL : V_OPEN + (quarkonium × light meson) + (charmonium × charmonium) pairs.
  B_s omitted (not pinned on disk).
CUT: |δ| ≤ 30 MeV (R164's cut, unchanged).
NULL: for each state, the fraction p_i of [M−200, M+200] within 30 MeV of some threshold of its own sector
  (exact, 0.1-MeV grid); k0 = Σ p_i; P(k ≥ k_obs) by the Poisson-binomial.

KILL LINE (for the proximity claim as a CLASS statement): if k_obs is not above the null at P < 0.01 in
  V_OPEN, "observed exotics sit at their two-hadron thresholds" is not supported beyond chance on the
  PDG-fixed class, and A14's claim cell must say so.
DIRECTION (written before running): proximity predicts k/N well above Σp_i/N in V_OPEN. I EXPECT V_ALL to be
  uninformative (dense thresholds → p_i near 1): that outcome is "no test", not "pass".
  P1 V_OPEN: k_obs/N ≥ 0.5.                                  [can fail]
  P2 V_OPEN: P(k ≥ k_obs | null) < 0.01.                     [can fail]
  P3 V_ALL : mean p_i > 0.5 (the loose set cannot discriminate).  [can fail]
  C1 control: X(3872) is NOT in the class (PDG names it χc1) — asserted, so it cannot inflate k.
  C2 control: a state placed exactly on a threshold gives δ = 0 and counts; one 200 MeV from all thresholds does not.
"""
from itertools import combinations_with_replacement, product

# PDG 2026 summary-table masses (MeV). Files under data/sources_grace_2026-09-26/exotics/ (tab-*) and
# data/sources_grace_2026-09-25/meson_photon/rpp2026-tab-mesons-light.txt (light).
M = {
 "pi+": 139.57039, "pi0": 134.9768, "eta": 547.862,            # light:15,57,89
 "rho": 775.26, "omega": 782.66, "etap": 957.78, "phi": 1019.460,  # light:190 (ρ0 BW), 224, 257, 355
 "K+": 493.677, "K0": 497.611, "K*+": 891.88, "K*0": 895.56,   # strange:13,232,503,505
 "D0": 1864.84, "D+": 1869.66, "D*0": 2006.86, "D*+": 2010.27, # charm:537,13,1519,1541
 "Ds": 1968.35, "Ds*": 2112.2,                                  # charm-strange:18,526
 "etac": 2984.09, "Jpsi": 3096.900, "chic0": 3415.50, "chic1": 3510.67,  # c-cbar:11,108,712,873
 "hc": 3525.37, "chic2": 3556.17, "etac2S": 3637.8, "psi2S": 3686.097,  # c-cbar:1035,1088,1241,1303
 "B+": 5279.41, "B0": 5279.72, "B*": 5324.75,                   # bottom:81,1586,3423
 "etab": 9398.7, "Y1S": 9460.40, "chib0": 9859.44, "chib1": 9892.78, "hb1P": 9899.3,  # b-bbar:11,28,224,258,290
 "chib2": 9912.21, "Y2S": 10023.4, "chib1_2P": 10255.46, "hb2P": 10259.8, "chib2_2P": 10268.65,  # :308,336,545,580,599
 "Y3S": 10355.1,                                                # b-bbar:634
}
Dq = ["D0", "D+", "D*0", "D*+"]
charmonia = ["etac", "Jpsi", "chic0", "chic1", "hc", "chic2", "etac2S", "psi2S"]
bottomonia = ["etab", "Y1S", "chib0", "chib1", "hb1P", "chib2", "Y2S", "chib1_2P", "hb2P", "chib2_2P", "Y3S"]
light0 = ["pi+", "pi0", "eta", "rho", "omega", "etap", "phi"]      # S = 0 light mesons (charge variants folded)
lightS = ["K+", "K0", "K*+", "K*0"]

def pairs(a, b): return sorted({M[x] + M[y] for x, y in product(a, b)})
def selfpairs(a): return sorted({M[x] + M[y] for x, y in combinations_with_replacement(a, 2)})

TH = {
 "ccbar":  {"open": pairs(Dq, Dq) + selfpairs(["Ds", "Ds*"]), "extra": pairs(charmonia, light0)},
 "ccbars": {"open": pairs(["Ds", "Ds*"], Dq),               "extra": pairs(charmonia, lightS)},
 "cc":     {"open": pairs(Dq, Dq),                           "extra": []},
 "cccc":   {"open": [],                                      "extra": selfpairs(charmonia)},
 "bbbar":  {"open": pairs(["B+", "B0", "B*"], ["B+", "B0", "B*"]), "extra": pairs(bottomonia, light0)},
}
# the class: PDG 2026 Table 77.2 / 77.3 "T"-named entries (name, mass, sector, table:line)
CLASS = [
 ("Tcc(3875)",       3874.74, "cc",     "77.3 line 687"),
 ("Tccbar1(3900)",   3886.7,  "ccbar",  "77.3 line 689"),
 ("Tccbars1(4000)",  3995.0,  "ccbars", "77.3 line 694 (range 3980-4010, midpoint)"),
 ("Tccbar(4020)",    4024.1,  "ccbar",  "77.3 line 697"),
 ("Tccbar(4050)",    4051.0,  "ccbar",  "77.2 line 461"),
 ("Tccbar(4055)",    4054.0,  "ccbar",  "77.2 line 465"),
 ("Tccbar(4100)",    4096.0,  "ccbar",  "77.2 line 467"),
 ("Tccbars1(4220)",  4216.0,  "ccbars", "77.3 line 701"),
 ("Tccbar0(4240)",   4239.0,  "ccbar",  "77.2 line 481"),
 ("Tccbar1(4200)",   4242.0,  "ccbar",  "77.2 line 476"),
 ("Tccbar(4250)",    4248.0,  "ccbar",  "77.2 line 485"),
 ("Tccbar1(4430)",   4478.0,  "ccbar",  "77.2 line 496"),
 ("Tcccc(6600)",     6646.0,  "cccc",   "77.2 line 513"),
 ("Tcccc(6900)",     6898.0,  "cccc",   "77.2 line 515"),
 ("Tcccc(7100)",     7134.0,  "cccc",   "77.2 line 516"),
 ("Tbbbar1(10610)",  10607.2, "bbbar",  "77.3 line 706"),
 ("Tbbbar1(10650)",  10652.2, "bbbar",  "77.3 line 711"),
]
assert len(CLASS) == 17
CUT, W = 30.0, 200.0

def nearest(m, ths):
    if not ths: return None
    t = min(ths, key=lambda x: abs(m - x)); return m - t, t
def p_null(m, ths):
    if not ths: return 0.0
    n = int(2 * W * 10); hit = 0
    for i in range(n + 1):
        x = m - W + i * 0.1
        if any(abs(x - t) <= CUT for t in ths): hit += 1
    return hit / (n + 1)
def poisson_binomial_tail(ps, k):
    dist = [1.0]
    for p in ps:
        new = [0.0] * (len(dist) + 1)
        for j, q in enumerate(dist):
            new[j] += q * (1 - p); new[j + 1] += q * p
        dist = new
    return sum(dist[k:])

score = total = 0
def check(label, ok):
    global score, total
    total += 1; score += bool(ok); print(f"[{'PASS' if ok else 'FAIL'}] {label}")

res = {}
for variant in ("open", "all"):
    print(f"\n=== V_{variant.upper()} ===")
    ks, ps = 0, []
    for name, m, sec, src in CLASS:
        ths = TH[sec]["open"] + (TH[sec]["extra"] if variant == "all" else [])
        nt = nearest(m, ths); p = p_null(m, ths); ps.append(p)
        if nt is None:
            print(f"  {name:18s} {m:9.1f}  no threshold in this variant            p0={p:.2f}  {src}")
            continue
        d, t = nt; inside = abs(d) <= CUT; ks += inside
        print(f"  {name:18s} {m:9.1f}  thr {t:9.2f}  δ={d:+8.1f}  {'IN ' if inside else 'out'}  p0={p:.2f}  {src}")
    k0 = sum(ps); tail = poisson_binomial_tail(ps, ks)
    res[variant] = (ks, k0, tail, sum(ps) / len(ps))
    print(f"  k/N = {ks}/{len(CLASS)};  null expectation Σp = {k0:.2f};  P(k ≥ {ks} | null) = {tail:.3g};  mean p = {sum(ps)/len(ps):.2f}")

print()
ko, k0o, to, _ = res["open"]; _, _, _, mpa = res["all"]
check(f"P1 V_OPEN k/N = {ko}/17 >= 0.5", ko / 17 >= 0.5)
check(f"P2 V_OPEN P(k>={ko}|null) = {to:.3g} < 0.01", to < 0.01)
check(f"P3 V_ALL mean p = {mpa:.2f} > 0.5 (loose set cannot discriminate)", mpa > 0.5)
check("C1 X(3872) not in class", all("3872" not in n for n, *_ in CLASS))
t0 = TH["cc"]["open"][0]
check("C2 on-threshold counts, far does not", abs(nearest(t0, TH["cc"]["open"])[0]) <= CUT and abs(nearest(t0 - 200, TH["cc"]["open"])[0]) > CUT)
print(f"\nSCORE {score}/{total}")
