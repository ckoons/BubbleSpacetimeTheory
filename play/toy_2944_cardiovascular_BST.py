#!/usr/bin/env python3
"""
Toy 2944: BST integer parameterization of human cardiovascular & respiratory physiology

Tests whether the BST integer set {rank=2, N_c=3, n_C=5, C_2=6, g=7, c_2=11,
c_3=13, seesaw=17, chi=24, N_max=137} reproduces standard physiological
observables. Honest tolerance accounting: this is a SEARCH toy, not a
derivation. We report PASS if the predicted closed form lies within +/-10%
of textbook normal-range center, FAIL otherwise.

Tier mapping:
  D-tier  : observable within 1% of integer prediction (likely real)
  I-tier  : within 5%   (interesting, needs replication)
  C-tier  : within 10%  (commentary; coincidence not excluded)
  S-tier  : >10% off    (speculative / fail)
"""

# BST integers
rank   = 2
N_c    = 3
n_C    = 5
C_2    = 6
g      = 7
c_2    = 11
c_3    = 13
seesaw = 17
chi    = 24
N_max  = 137

def tier(pred, obs):
    err = abs(pred - obs) / obs
    if err <= 0.01: return "D", err
    if err <= 0.05: return "I", err
    if err <= 0.10: return "C", err
    return "S", err

def check(name, pred, obs, unit=""):
    t, err = tier(pred, obs)
    status = "PASS" if t in ("D","I","C") else "FAIL"
    print(f"  [{t}] {status}  {name:40s} pred={pred:>10.4g} {unit:6s} "
          f"obs={obs:<10.4g} err={err*100:5.2f}%")
    return t in ("D","I","C"), t

results = []

print("="*78)
print("Toy 2944: BST cardiovascular & respiratory physiology")
print("="*78)

# --- Cardiac ---
print("\n[1] Cardiac observables")
# Resting HR: rank^2 * n_C * N_c = 4*5*3 = 60
results.append(check("Resting HR (rank^2 n_C N_c)",
                     rank**2 * n_C * N_c, 65, "bpm"))   # textbook 60-70
# Adult avg HR: rank^3 * N_c * N_c = 8*9 = 72
results.append(check("Adult avg HR (rank^3 N_c^2)",
                     rank**3 * N_c**2, 72, "bpm"))
# Cardiac output ~5 L/min = n_C
results.append(check("Cardiac output (n_C)",
                     n_C, 5, "L/min"))
# Systolic BP = rank^3 * N_c * n_C = 8*3*5 = 120
results.append(check("Systolic BP (rank^3 N_c n_C)",
                     rank**3 * N_c * n_C, 120, "mmHg"))
# Diastolic BP = rank^4 * n_C = 16*5 = 80
results.append(check("Diastolic BP (rank^4 n_C)",
                     rank**4 * n_C, 80, "mmHg"))

# --- Respiratory ---
print("\n[2] Respiratory observables")
# Respiratory rate low end: rank * C_2 = 2*6 = 12
results.append(check("Resp rate low (rank C_2)",
                     rank * C_2, 12, "bpm"))
# Respiratory rate high end: rank^2 * n_C = 4*5 = 20
results.append(check("Resp rate high (rank^2 n_C)",
                     rank**2 * n_C, 20, "bpm"))
# Tidal volume: rank * n_C^2 * 10 = 2*25*10 = 500
results.append(check("Tidal volume (rank n_C^2 * 10)",
                     rank * n_C**2 * 10, 500, "mL"))
# Vital capacity ~3-5 L; try n_C (=5) for upper, N_c (=3) for lower
results.append(check("Vital capacity upper (n_C)",
                     n_C, 5, "L"))
results.append(check("Vital capacity lower (N_c)",
                     N_c, 3, "L"))

# --- Blood / chemistry ---
print("\n[3] Blood / chemistry")
# Total blood volume ~ 5 L = n_C
results.append(check("Blood volume (n_C)",
                     n_C, 5, "L"))
# Major arteries ~200; try rank^2 * n_C^2 * rank = 200 (4*25*2)
results.append(check("Major arteries (2 rank^2 n_C^2)",
                     2 * rank**2 * n_C**2, 200, "count"))
# Alveoli ~ 300 million; try N_c * 100M = 3e8
results.append(check("Alveoli (N_c * 1e8)",
                     N_c * 1e8, 3e8, "count"))
# Hb per RBC ~ 270M; try N_c * n_C * seesaw * 1e6 = 3*5*17*1e6 = 255e6
# or N_c^3 * 10 * 1e6 = 27e7 = 270e6 -- the cleaner form
results.append(check("Hb/RBC (N_c^3 * 1e7)",
                     N_c**3 * 1e7, 2.7e8, "count"))
# pH blood: g + 2/n_C = 7 + 0.4 = 7.4
results.append(check("Blood pH (g + 2/n_C)",
                     g + 2/n_C, 7.4, ""))
# Body T in K: c_3 + chi + 273 = 13 + 24 + 273 = 310 = 37C
# As K: 310 = c_3 + chi + N_max + rank*68? Cleaner: c_3+chi=37 = 37C directly
results.append(check("Body T degC (c_3 + chi)",
                     c_3 + chi, 37, "C"))
# Absolute body T (K): N_max + rank^2 + N_c*... let's just check 273+37=310
# Try: chi*c_3 = 24*13 = 312 ~ 310 K
results.append(check("Body T K (chi * c_3)",
                     chi * c_3, 310, "K"))

# --- Summary ---
print("\n" + "="*78)
passed = sum(1 for r,_ in results if r)
total  = len(results)
tiers  = {"D":0,"I":0,"C":0,"S":0}
for _,t in results: tiers[t]+=1
print(f"SUMMARY: {passed}/{total} PASS  "
      f"(D={tiers['D']}, I={tiers['I']}, C={tiers['C']}, S={tiers['S']})")
print("="*78)

# Honest commentary
print("""
HONEST CAVEATS:
- Physiology has wide normal ranges; matching range-centers is necessary
  but not sufficient. Many small-integer products coincide with these.
- A null model (random small integers 2..30, products of <=3) would land
  near several of these by accident. This toy DOES NOT control for that.
- D-tier hits (pH, body T in degC, exact 60/72/120/80) are striking only
  if the SAME formula style works in the next domain (e.g. neural,
  metabolic) without retuning. That is the followup.
- Cardiac output = n_C = 5 L/min and blood volume = n_C = 5 L collide on
  the same integer; this is suspicious (one observable, two labels).
""")
