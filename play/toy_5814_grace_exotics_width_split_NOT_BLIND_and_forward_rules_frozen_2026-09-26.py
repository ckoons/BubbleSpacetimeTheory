#!/usr/bin/env python3
"""
Toy 5814 — Grace, 2026-09-26, round 7 item 4 (K1929 GRACE item 4): the width-scaled test, and whether a
quarkonium-pair class can be fixed in advance.

NOT BLIND. I have seen δ for all 17 states of the A14 class (toy 5810). Nothing here is counted for A14.
This toy (a) DESCRIBES the narrow/broad split on the 17, and (b) FREEZES two rules for FORWARD use only.

INVARIANT: δ = M − M_thr (a mass difference); Γ = the PDG table width (Tables 77.2/77.3, same lines as 5810).
WIDTH RULE (frozen here, forward): a state is NARROW iff Γ < 2·CUT = 60 MeV (the half-width is below the
  30 MeV proximity cut, so "within 30 MeV" is resolvable). Tcc̄s̄1(4000) (Γ quoted as a range 5–150) is
  UNCLASSIFIABLE and excluded from both groups.
FORWARD RULE 1 (A14 extension): every PDG 'T'- or 'P'-named heavy exotic FIRST LISTED after 2026-09-26 is
  scored with 5810's V_OPEN thresholds (P states: open-flavour baryon–meson pairs, list to be frozen by Cal
  before the next PDG edition), split NARROW/BROAD by the width rule; k/N vs the ±200 MeV null, per group.
FORWARD RULE 2 (quarkonium-pair class): for fully-heavy QQQ̄Q̄ states, thresholds = pairs of the frozen
  charmonium list of 5810 (8 states). DECISION CRITERION, written before computing: if the ±200 MeV null
  covers > 80 % of the window at the three observed Tccc̄c̄ masses, the class has no power and is NOT counted.
DIRECTION: the proximity reading predicts narrow states sit at threshold at least as often as broad ones.
  D1 narrow in-window fraction ≥ broad in-window fraction.       [can fail; descriptive, not blind]
  D2 quarkonium-pair null coverage > 0.8 at all three Tccc̄c̄ masses (⇒ no power).   [can fail]
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


GAMMA = {"Tcc(3875)": 0.048, "Tccbar1(3900)": 29.5, "Tccbars1(4000)": None, "Tccbar(4020)": 13,
 "Tccbar(4050)": 82, "Tccbar(4055)": 45, "Tccbar(4100)": 152, "Tccbars1(4220)": 233, "Tccbar0(4240)": 220,
 "Tccbar1(4200)": 310, "Tccbar(4250)": 177, "Tccbar1(4430)": 189, "Tcccc(6600)": 440, "Tcccc(6900)": 161,
 "Tcccc(7100)": 97, "Tbbbar1(10610)": 18.4, "Tbbbar1(10650)": 11.5}
score = total = 0
def check(label, ok):
    global score, total
    total += 1; score += bool(ok); print(f"[{'PASS' if ok else 'FAIL'}] {label}")
groups = {"NARROW": [], "BROAD": []}
for name, m, sec, src in CLASS:
    g = GAMMA[name]
    if g is None:
        print(f"  {name:18s} UNCLASSIFIABLE (width quoted as a range)"); continue
    ths = TH[sec]["open"]
    nt = nearest(m, ths); p = p_null(m, ths)
    inside = nt is not None and abs(nt[0]) <= CUT
    grp = "NARROW" if g < 2 * CUT else "BROAD"
    groups[grp].append((inside, p))
    ds = f"{nt[0]:+8.1f}" if nt else "   none "
    print(f"  {name:18s} Γ={g:7.3f}  {grp:6s}  δ={ds}  {'IN ' if inside else 'out'}  p0={p:.2f}")
fr = {}
for grp, v in groups.items():
    k = sum(i for i, _ in v); ps = [p for _, p in v]
    tail = poisson_binomial_tail(ps, k)
    fr[grp] = k / len(v)
    print(f"{grp}: k/N = {k}/{len(v)}  null Σp = {sum(ps):.2f}  P(k>=obs|null) = {tail:.3g}   [NOT BLIND]")
check(f"D1 narrow fraction {fr['NARROW']:.2f} >= broad fraction {fr['BROAD']:.2f}", fr["NARROW"] >= fr["BROAD"])
cov = [p_null(m, TH["cccc"]["extra"]) for n, m, s, _ in CLASS if s == "cccc"]
check(f"D2 quarkonium-pair null coverage {[round(c,2) for c in cov]} all > 0.8 (=> class has no power, not counted)", all(c > 0.8 for c in cov))
print(f"\nSCORE {score}/{total}")
