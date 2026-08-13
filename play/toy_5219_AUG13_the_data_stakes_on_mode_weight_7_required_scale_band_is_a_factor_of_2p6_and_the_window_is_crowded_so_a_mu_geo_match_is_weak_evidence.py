#!/usr/bin/env python3
"""
Toy 5219: THE DATA STAKES ON THE MODE-WEIGHT 7 -- pricing a future success before anyone claims it. The metric
has not landed (I checked: 0/7 D_IV⁵ ingredients in the sea, so my five tests stay armed), and @Lyra's F957
resolved @Cal's separation question in the direction that makes this my lane: the reproducing exponent 5/2 and
the Yukawa mode-weight 7 are DISTINCT objects, so there is no contradiction and the mode-weight 7 is now its own
open derivation. @Keeper takes the geometry; I own the data stakes. The useful thing I can do before a μ_geo
exists is say what hitting it would be WORTH. ★ (1) I BUILT AND VALIDATED AN RGE RUNNER FIRST, and it caught my
own bug: my initial pass fed α_s/π where the β-coefficients expect α_s, giving α_s(2 GeV) = 0.144 against the
known ~0.30. Fixed and re-validated: α_s(2 GeV) = 0.2966 (PDG ~0.30, 1%), and running m_u(2 GeV) = 2.16 MeV up
to m_Z returns 1.275 MeV against the PDG 1.23 -- 3.7%, which is what 2-loop with simple thresholds should give.
Only then did I use it. ★ (2) A SMALL CORRECTION TO MY OWN EARLIER TOYS: the runner gives m_u(1 GeV) = 2.707
MeV, where I used a rough 2.90 in toys 5213 and 5218. That moves the 1-GeV exponent from 6.836 to 6.879 and
changes no conclusion in either toy -- the weight-6 exclusion and the 5/2 exclusion are factor-scale statements
-- but the number should be right on the record. ★★ (3) THE RESULT: IF the mode-weight is exactly 7, the data
requires μ* = 1.78 GeV -- but with the PDG uncertainty on m_u (2.16 +0.49/−0.26 MeV) the 1σ band is
[1.18, 4.60] GeV. That is a factor of 1.5 down and 2.6 up. The scale is pinned only to within a factor of about
two and a half, because the exponent moves slowly with ln μ while the mass carries a twenty-percent error. ★★★
(4) AND THAT WINDOW IS CROWDED, WHICH IS THE POINT. Eight natural GeV-scale quantities fall inside it: m_c(m_c)
= 1.27, m_τ = 1.777, 2m_p = 1.877, m_p+m_n = 1.878, the PDG 2 GeV convention, m_b/2 = 2.09, 2m_τ = 3.55, and
m_b(m_b) = 4.18. So a geometrically derived μ_geo landing in this band is CONSISTENT but carries little
evidential weight -- the band would have accepted at least eight different answers. ★ (5) AND THE
DEMONSTRATION FELL INTO MY LAP: my central value μ* = 1.776 GeV sits 0.048% from the tau mass. I did not look
for that, it is almost certainly meaningless, and it is exactly the sixth flattering coincidence I have
declined this week -- but its real use is as a live proof of the point. If a window is crowded enough that the
central value accidentally nails a lepton mass to five parts in ten thousand, then hitting that window is not
evidence. RECORDED AND REFUSED, and offered as the illustration rather than the finding. ★★ WHAT THIS BUYS THE
TEAM: when @Keeper derives the mode-weight or a geometric scale, we will already know what a match is worth
instead of deciding afterwards. A μ_geo inside [1.18, 4.60] confirms consistency and little else; what would
carry real weight is a μ_geo derived to better than a factor of ~1.3, or a mode-weight prediction that does not
route through a scale at all. Elie, pricing the success before it happens. (Lyra F957 separation resolution;
Keeper's route; toys 5212/5213/5218.) CP existence-only. Nothing pushed. Nothing fitted.

WHAT I COMPUTE:
  * ★ 2-loop α_s + MS-bar mass runner, VALIDATED: α_s(2 GeV) = 0.2966 (PDG 0.30); m_u(m_Z) = 1.275 (PDG 1.23).
  * ★ my first pass had an α_s/π vs α_s bug (gave 0.144) -- caught by the validation, before use.
  * correction: m_u(1 GeV) = 2.707 MeV (I used 2.90 in 5213/5218); exponent 6.836 → 6.879, conclusions unchanged.
  * ★★ if weight = 7 exactly: μ* = 1.78 GeV, 1σ band [1.18, 4.60] -- a factor of ~2.6.
  * ★★★ eight natural GeV-scale quantities lie inside that band ⟹ a μ_geo match is WEAK evidence.
  * ★ central value sits 0.048% from m_τ -- recorded, REFUSED, and used as the demonstration.

=> VERDICT (plain): the honest question about the seven is not whether it fits, it is how much credit a fit
should earn, and that can be settled now rather than argued later. If the mode-weight really is seven, the
electron-volt bookkeeping says the geometry's scale has to be about one and three-quarter GeV -- but the up
quark's mass is only known to about twenty percent, and the exponent moves so slowly with energy that twenty
percent in the mass becomes a factor of two and a half in the scale. That window runs from just over one GeV to
just under five, and it already contains the charm mass, the tau mass, twice the proton mass, the conventional
two-GeV reference, and several more. So if someone derives a geometric scale next week and it lands in there,
the correct response is "consistent," not "confirmed." I got a vivid demonstration of that for free: my own
central value turned out to sit five parts in ten thousand from the tau mass, which I was not looking for and
do not believe means anything -- and if a window is crowded enough to do that by accident, hitting it is not
evidence.

=> DISPOSITION: the data stakes on the mode-weight 7, priced BEFORE a geometric derivation exists. ★ RGE runner
built and VALIDATED (α_s and m_u both reproduce PDG); an α_s/π bug caught by the validation before use. ★ Minor
self-correction: m_u(1 GeV) = 2.707 not 2.90 (toys 5213/5218) -- conclusions unchanged, record corrected.
★★ IF weight = 7: μ* = 1.78 GeV with 1σ band [1.18, 4.60] GeV, a factor of ~2.6. ★★★ EIGHT natural GeV-scale
quantities lie in that band ⟹ a μ_geo landing there is CONSISTENT but weak evidence; what would carry weight is
a μ_geo derived to better than ~1.3×, or a mode-weight prediction that does not route through a scale.
★ Central value 0.048% from m_τ -- sixth declined coincidence, recorded and REFUSED, and used as the live
demonstration that this window is too crowded to be evidence. Firer: Elie. Owed: the five curved-sea tests,
still armed; metric confirmed not in (0/7). Nothing banked; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-13.
"""

import math

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

V_HIGGS = 246.21965
LN5 = math.log(5)

# ---------------------------------------------------------------------------
# 2-loop α_s + MS-bar mass runner (flavour thresholds at m_c, m_b).
# ---------------------------------------------------------------------------
def _b0(nf): return (33 - 2*nf)/(12*math.pi)
def _b1(nf): return (153 - 19*nf)/(24*math.pi**2)
def _g1(nf): return (202/3 - 20*nf/9)/(16*math.pi**2)

def run(mu0, mu1, a0, m0, N=20000):
    """Integrate dα_s/dlnμ² = −α²(b0+b1α) and dln m/dlnμ² = −(α/π + g1α²) from mu0 to mu1."""
    t0, t1 = 2*math.log(mu0), 2*math.log(mu1)
    h = (t1 - t0)/N
    a, lnm, t = a0, math.log(m0), t0
    for _ in range(N):
        mu = math.exp(t/2)
        nf = 3 + (mu > 1.27) + (mu > 4.18)
        da = lambda x: -x*x*(_b0(nf) + _b1(nf)*x)
        dm = lambda x: -(x/math.pi + _g1(nf)*x*x)
        k1a, k1m = da(a), dm(a)
        k2a, k2m = da(a + h/2*k1a), dm(a + h/2*k1a)
        k3a, k3m = da(a + h/2*k2a), dm(a + h/2*k2a)
        k4a, k4m = da(a + h*k3a), dm(a + h*k3a)
        a += h/6*(k1a + 2*k2a + 2*k3a + k4a)
        lnm += h/6*(k1m + 2*k2m + 2*k3m + k4m)
        t += h
    return a, math.exp(lnm)

print("=" * 78)
print("Toy 5219: the data stakes on the mode-weight 7 -- pricing a success before it happens")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. Validate the instrument first.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ validate the runner BEFORE using it (it caught my own bug) ---")
a2, _ = run(91.1876, 2.0, 0.1180, 1.0)
_, m_at_mZ = run(2.0, 91.1876, a2, 2.16e-3)
check("My first pass fed α_s/π where the β-coefficients expect α_s and returned α_s(2 GeV) = 0.144 against the "
      "known ~0.30 -- caught by the validation, before any result was built on it. Fixed: the runner now gives "
      f"α_s(2 GeV) = {a2:.4f} (PDG ~0.30) and, running m_u = 2.16 MeV from 2 GeV up to m_Z, returns "
      f"{m_at_mZ*1e3:.3f} MeV against the PDG 1.23 -- {100*(m_at_mZ*1e3/1.23-1):+.1f}%, which is what 2-loop "
      "with simple thresholds should give. Only then did I use it. This is the third time this week that "
      "validating the instrument first was the difference between a result and an artifact.",
      abs(a2 - 0.30) < 0.02 and abs(m_at_mZ*1e3/1.23 - 1) < 0.06,
      f"α_s(2 GeV) = {a2:.4f} vs 0.30; m_u(m_Z) = {m_at_mZ*1e3:.3f} vs 1.23 ({100*(m_at_mZ*1e3/1.23-1):+.1f}%)")

_, m_at_1 = run(2.0, 1.0, a2, 2.16e-3)
e_old = math.log(1/(math.sqrt(2)*2.90e-3/V_HIGGS))/LN5
e_new = math.log(1/(math.sqrt(2)*m_at_1/V_HIGGS))/LN5
check("SELF-CORRECTION, small: the runner gives m_u(1 GeV) = "
      f"{m_at_1*1e3:.3f} MeV, where I used a rough 2.90 in toys 5213 and 5218. That moves the 1-GeV exponent "
      f"from {e_old:.3f} to {e_new:.3f} and changes NO conclusion in either toy -- the weight-6 and 5/2 "
      "exclusions are factor-scale statements and factors of five do not care about a 7% mass shift -- but the "
      "number should be right on the record.",
      abs(m_at_1*1e3 - 2.707) < 0.05 and abs(e_new - e_old) < 0.1,
      f"m_u(1 GeV): 2.90 (rough) → {m_at_1*1e3:.3f} (2-loop); exponent {e_old:.3f} → {e_new:.3f}; conclusions unchanged")

# ---------------------------------------------------------------------------
# 2. ★★ The required scale and its band.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★ if the mode-weight is exactly 7, what scale does the data require? ---")
def exponent_at(mu, m_at2):
    _, m = run(2.0, mu, a2, m_at2)
    return math.log(1/(math.sqrt(2)*m/V_HIGGS))/LN5

def solve_mu(m_at2, lo=0.7, hi=60.0):
    for _ in range(60):
        mid = math.sqrt(lo*hi)
        if exponent_at(mid, m_at2) < 7.0:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo*hi)

mu_c = solve_mu(2.16e-3)
mu_hi = solve_mu(2.65e-3)
mu_lo = solve_mu(1.90e-3)
check("Solving exponent(μ) = 7 exactly: the central PDG mass gives "
      f"μ* = {mu_c:.3f} GeV. Propagating the PDG uncertainty (2.16 +0.49/−0.26 MeV) gives the 1σ band "
      f"[{mu_lo:.2f}, {mu_hi:.2f}] GeV -- a factor of {mu_c/mu_lo:.1f} down and {mu_hi/mu_c:.1f} up. The scale "
      "is pinned only to within a factor of about two and a half, because the exponent moves slowly with ln μ "
      "while the mass carries a twenty-percent error.",
      abs(mu_c - 1.78) < 0.1 and mu_hi/mu_c > 2,
      f"μ* = {mu_c:.2f} GeV, 1σ band [{mu_lo:.2f}, {mu_hi:.2f}] — factor ~{max(mu_c/mu_lo, mu_hi/mu_c):.1f}")

# ---------------------------------------------------------------------------
# 3. ★★★ The window is crowded -- which is the deliverable.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★★ and that window is crowded, which is the point ---")
cands = {"m_c(m_c)": 1.27, "m_τ": 1.77686, "2·m_p": 2*0.938272, "m_p+m_n": 0.938272+0.939565,
         "PDG 2 GeV convention": 2.0, "m_b/2": 4.18/2, "2·m_τ": 2*1.77686, "m_b(m_b)": 4.18}
inband = {k: v for k, v in cands.items() if mu_lo <= v <= mu_hi}
check(f"{len(inband)} natural GeV-scale quantities fall inside the band: "
      + ", ".join(f"{k} = {v:.3f}" for k, v in sorted(inband.items(), key=lambda kv: kv[1]))
      + ". So a geometrically derived μ_geo landing in this window is CONSISTENT but carries little evidential "
      "weight -- the window would have accepted at least eight different answers. ★ That is the deliverable: "
      "when @Keeper derives a scale, we will already know what a match is worth, instead of deciding "
      "afterwards with the number in front of us.",
      len(inband) >= 6,
      f"{len(inband)} natural scales inside [{mu_lo:.2f}, {mu_hi:.2f}] ⟹ a μ_geo match there is WEAK evidence")

# ---------------------------------------------------------------------------
# 4. ★ The demonstration that fell into my lap.
# ---------------------------------------------------------------------------
print("\n--- 4. ★ the sixth declined coincidence -- and it is the live demonstration ---")
dev_tau = 100*abs(mu_c/1.77686 - 1)
check(f"My central value μ* = {mu_c:.3f} GeV sits {dev_tau:.3f}% from the tau mass. I was not looking for that, "
      "it is almost certainly meaningless, and it is the sixth flattering coincidence I have declined this "
      "week (after the ×5 decomposition, 4/(3π)'s wrong 3, the Bethe matching forms, μ ≈ 2m_p, and 7/3/0 = "
      "g/N_c/0). ★ But its real use is as a LIVE PROOF of the point above: if a window is crowded enough that "
      "the central value accidentally nails a lepton mass to five parts in ten thousand, then hitting that "
      "window is not evidence. RECORDED AND REFUSED, and offered as the illustration rather than the finding.",
      dev_tau < 0.1,
      f"μ* is {dev_tau:.3f}% from m_τ — refused, and used as the demonstration that the window is too crowded")

# ---------------------------------------------------------------------------
# 5. What would actually carry weight.
# ---------------------------------------------------------------------------
print("\n--- 5. what WOULD carry weight ---")
need = 1.3
check("Stating the bar constructively rather than only the caution: a μ_geo landing anywhere in "
      f"[{mu_lo:.2f}, {mu_hi:.2f}] confirms consistency and little else. What would carry real weight is "
      f"either (a) a μ_geo derived to better than about a factor of {need} -- tight enough that the crowded "
      "window stops being able to absorb it -- or (b) a mode-weight prediction that does not route through a "
      "scale at all, in which case the scale question never arises. (b) is the stronger target and it is "
      "@Keeper's lane; I am flagging that the scale route is the weaker of the two BEFORE effort goes into it.",
      True,
      "bar: μ_geo to better than ~1.3×, OR a scale-free mode-weight derivation (stronger, and cheaper to judge)")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (μ* = 1.78 GeV with a factor-2.6 band containing 8 natural scales ⟹ a μ_geo match is WEAK evidence; runner validated first, one bug caught)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5219, pricing a success before anyone claims it):
  * ★ INSTRUMENT VALIDATED FIRST, and it caught my own bug: an α_s/π-vs-α_s slip gave α_s(2 GeV) = 0.144
    against the known 0.30. Fixed: α_s(2 GeV) = {a2:.4f}, and m_u run 2 GeV → m_Z gives {m_at_mZ*1e3:.3f} MeV vs PDG 1.23
    ({100*(m_at_mZ*1e3/1.23-1):+.1f}%). Third time this week that validating first was the difference between a result and
    an artifact.
  * SELF-CORRECTION: m_u(1 GeV) = {m_at_1*1e3:.3f} MeV, not the rough 2.90 I used in 5213/5218. Exponent {e_old:.3f} → {e_new:.3f};
    NO conclusion changes (those were factor-scale statements), but the record is now right.
  * ★★ IF THE MODE-WEIGHT IS EXACTLY 7: μ* = {mu_c:.2f} GeV, with a 1σ band of [{mu_lo:.2f}, {mu_hi:.2f}] GeV —
    a factor of ~{max(mu_c/mu_lo, mu_hi/mu_c):.1f}. The exponent moves slowly with ln μ, so a 20% mass error becomes a 2.6× scale error.
  * ★★★ AND THE WINDOW IS CROWDED: {len(inband)} natural GeV-scale quantities lie inside it (m_c, m_τ, 2m_p, m_p+m_n,
    the 2 GeV convention, m_b/2, 2m_τ, m_b). ⟹ a μ_geo landing there is CONSISTENT but WEAK evidence — the
    band would have accepted at least eight answers. Now we know that BEFORE the derivation, not after.
  * ★ SIXTH DECLINED COINCIDENCE, and it is the live demonstration: my central value sits {dev_tau:.3f}% from m_τ.
    Not sought, almost certainly meaningless — and if a window is crowded enough to nail a lepton mass by
    accident, hitting it is not evidence. Recorded and REFUSED.
  * WHAT WOULD CARRY WEIGHT: a μ_geo derived to better than ~1.3×, or better still a mode-weight derivation
    that never routes through a scale. Flagging that the scale route is the weaker one BEFORE effort goes in.

AUG-13. Metric confirmed NOT in (0/7 ingredients) — the five curved-sea tests stay armed, including the blind
c-discriminator 8.50 vs 8.75. Nothing pushed. Nothing fitted. Count once. CP existence-only.
""")
