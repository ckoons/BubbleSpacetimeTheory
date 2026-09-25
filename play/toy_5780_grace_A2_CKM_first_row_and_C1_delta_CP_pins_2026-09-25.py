#!/usr/bin/env python3
"""
Toy 5780 — Grace, 2026-09-25. The retained instrument for the A2 (CKM first row)
and C1 (delta_CP) pin tables in
notes/grace_R159_A2_CKM_C1_deltaCP_Lane1_EDE_pins_2026-09-25.md.

No BST number is adjusted here. Inputs are the primaries' printed values, each
checked by grep against the text extracts retained in data/sources_grace_2026-09-25/
(pdftotext of the fetched PDFs) — the check FAILS the toy if a string is absent.
NuFIT 6.1 Delta-chi^2 values are read from NuFIT's own 1D DCP projections
(extracted from v61.release-{TBoff,TByes}-{NO,IO}.txt, retained in the same folder)
and linearly interpolated on NuFIT's 5-degree grid. sigma = sqrt(Delta-chi^2), 1 dof.
"""
import math, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "sources_grace_2026-09-25")
LAM_BST = 1 / math.sqrt(20)
score = [0, 0]

def check(name, ok):
    score[1] += 1; score[0] += bool(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

def in_text(fname, s):
    with open(os.path.join(SRC, fname), encoding="utf-8", errors="replace") as f:
        return s in f.read()

print("=== A2: printed values present in the retained primaries ===")
pins = [("pdg2025.txt", "λ = 0.22501 ± 0.00068"),          # PDG 2024 text, repeated in the 2025 update
        ("pdg2026.txt", "λ = 0.22517 ± 0.00068"),          # PDG 2026 CKM review, Revised March 2026
        ("pdg2026.txt", "a 2.3 σ tension with unitarity in the 1st row"),
        ("vv26.txt", "= 0.9983(6)(4)"),                    # PDG 2026 Vud/Vus review Eq. 67.21
        ("flag.txt", "0.99802(66)"),                       # FLAG 2024 Section 5.4, K_l3 route
        ("flag.txt", "0.99888(67)")]                       # FLAG 2024, K_mu2 route
for f, s in pins:
    check(f"{f}: '{s}'", in_text(f, s))

print("\n=== A2: Wolfenstein lambda against 1/sqrt(20) = %.7f ===" % LAM_BST)
lams = [("PDG 2024 CKMfitter (the register row's input)", 0.22501, 0.00068),
        ("PDG 2026 CKMfitter", 0.22517, 0.00068),
        ("PDG 2024 UTfit", 0.22497, 0.00070),
        ("PDG 2026 UTfit", 0.22519, 0.00068),
        ("PDG 2024 tree-level fit", 0.22509, 0.00068),
        ("PDG 2026 tree-level fit", 0.22528, 0.00069),
        ("|V_us| PDG average (S = 2.5)", 0.22431, 0.00085),
        ("|V_us| K_l3 (PDG 2026)", 0.22330, 0.00053),
        ("|V_us| K_mu2 (PDG CKM review)", 0.2250, 0.0004)]
z = {}
for name, v, s in lams:
    z[name] = (v - LAM_BST) / s
    print(f"  {name:48s} {v:.5f} ± {s:.5f}  ->  {z[name]:+.2f} sigma")
check("register row's 2.06 sigma reproduced", abs(z[lams[0][0]] - 2.06) < 0.005)
check("PDG 2026 global-fit lambda is further from 1/sqrt20 than PDG 2024's (the tension GREW)",
      z["PDG 2026 CKMfitter"] > z[lams[0][0]])

print("\n=== A2: first-row sum, direct (|V_us| 0.22431(85), |V_ub| 0.00382) ===")
Vus, sVus, Vub = 0.22431, 0.00085, 0.00382
for name, vud, s in [("Hardy-Towner 2020 (PDG 2024 = 2026)", 0.97367, 0.00032),
                     ("Ma et al. 2024 lattice gamma-W box", 0.97386, 0.00031),
                     ("Xayavong et al. 2025 delta_C shell model", 0.97359, 0.00033)]:
    S = vud**2 + Vus**2 + Vub**2
    sS = math.hypot(2 * vud * s, 2 * Vus * sVus)
    print(f"  {name:44s} sum = {S:.5f} ± {sS:.5f}   deficit {(1 - S) / sS:.2f} sigma")

print("\n=== A2: the row's other printed value, |V_ud| = sqrt(19/20), against the |V_ud| pins ===")
VUD_BST = math.sqrt(19 / 20)
check("pdg2026 Vud/Vus review prints neutron best value 0.97413(42)", in_text("vv26.txt", "0.97413(20)τn (35)λ (13)∆R (42)TOT"))
for name, vud, s in [("superallowed, Hardy-Towner 2020 (PDG 2026 Eq. 67.4)", 0.97367, 0.00032),
                     ("superallowed, Ma et al. 2024 lattice box", 0.97386, 0.00031),
                     ("superallowed, Xayavong et al. 2025", 0.97359, 0.00033),
                     ("neutron, PDG 2026 best values (Eq. 67.8)", 0.97413, 0.00042),
                     ("neutron, PDG 2026 averages (Eq. 67.7)", 0.97441, 0.00088)]:
    print(f"  sqrt(19/20) = {VUD_BST:.6f} vs {name:52s} {vud:.5f}({s*1e5:.0f}) -> {(VUD_BST - vud) / s:+.2f} sigma")

print("\n=== C1: NuFIT 6.1 Delta-chi^2 at the corpus claims (1D DCP projection) ===")
def load(tag):
    pts = []
    with open(os.path.join(SRC, f"nufit61_{tag}.dcp_projection.txt")) as f:
        for line in f:
            if line.startswith("#") or not line.strip(): continue
            a, c = line.split()[:2]; pts.append((float(a), float(c)))
    return sorted(pts)
def interp(pts, deg):
    d = ((deg + 180) % 360) - 180
    for (a0, c0), (a1, c1) in zip(pts, pts[1:]):
        if a0 <= d <= a1:
            return c0 + (c1 - c0) * (d - a0) / (a1 - a0)
    raise ValueError(deg)
claims = [309, 77, 197, 163]
rows = {}
for tag in ["TBoff-NO", "TBoff-IO", "TByes-NO", "TByes-IO"]:
    pts = load(tag); mn = min(c for _, c in pts)
    vals = {d: interp(pts, d) for d in claims}
    rows[tag] = vals
    print(f"  {tag:9s} (file min {mn:.2f}) " +
          "  ".join(f"{d}°: {v:6.2f} ({math.sqrt(max(v, 0)):.2f}σ)" for d, v in vals.items()))
check("NO minima are zero (Delta-chi^2 relative to the global = NO minimum)",
      all(min(c for _, c in load(t)) < 1e-9 for t in ["TBoff-NO", "TByes-NO"]))
check("197° inside 1σ in NO on both NuFIT 6.1 data sets", all(rows[t][197] < 1 for t in ["TBoff-NO", "TByes-NO"]))
check("77° beyond 3σ in NO on both NuFIT 6.1 data sets", all(rows[t][77] > 9 for t in ["TBoff-NO", "TByes-NO"]))

print(f"\nSCORE {score[0]}/{score[1]}")
sys.exit(0 if score[0] == score[1] else 1)
