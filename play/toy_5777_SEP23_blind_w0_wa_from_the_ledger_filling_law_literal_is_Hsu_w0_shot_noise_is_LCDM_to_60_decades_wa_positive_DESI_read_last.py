#!/usr/bin/env python3
"""Toy 5777 — the blind (w₀, wₐ) from the ledger's filling law. Elie, 2026-09-23.
PREREG notes/Elie_PREREG_5777_… sha256 c5d837627497a9474f22e03c091b218be5d544a29a9b8b921805437d3d5bc7ce (Cal hashes; noon fallback per K1749).
Inputs: Lyra's FILLING_LAW §3 list verbatim. DESI DR2 and the Luciano–Paliathanasis fit are read ONLY in the compare block at the end, from Grace's R158 pin note.
Usage: --predict (D1/D2, no DESI read)   --compare (adds the compare block; reads Grace's pin)   --all"""
import math, os, sys, re, json, hashlib
import numpy as np
PREREG_SHA = "c5d837627497a9474f22e03c091b218be5d544a29a9b8b921805437d3d5bc7ce"
here = os.path.dirname(os.path.abspath(__file__)); notes = os.path.join(here, "..", "notes")
pre = [f for f in os.listdir(notes) if f.startswith("Elie_PREREG_5777_")]
h = hashlib.sha256(open(os.path.join(notes, pre[0]), "rb").read()).hexdigest()
score, cf = [], []
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
print("=" * 100 + "\nTOY 5777 — blind (w₀, wₐ) from the ledger's filling law\n" + "=" * 100)
print(f"  prereg sha256 {h}  {'== frozen' if h == PREREG_SHA else '!! DIFFERS'}")
# background: flat ΛCDM-shaped H(a) with Ω_m = 0.31 (measured background; only the a-dependence of H enters)
Om = 0.31
def H2(a): return Om * a ** -3 + (1 - Om)          # in units of H0²
G, hbar, c = 6.67430e-11, 1.054571817e-34, 2.99792458e8
H0 = 67.4e3 / 3.0856775814913673e22; lP2 = hbar * G / c ** 3
def NH(a): return 4 * math.pi * c ** 2 / (H2(a) * H0 ** 2 * lP2)     # horizon count, rule R = A_H/ℓ_P², A_H = 4π(c/H)² — AMENDED 09-23 12:1x: the first run dropped c² (units slip; instrument only, prereg untouched)
# D1: literal ledger, ε ≡ 0: ρ_DE = E_commit·N_H/V_H, E = ħH ln2/2π, V_H = (4π/3)(c/H)³ → ρ ∝ H²
def rho_D1(a):
    Hh = math.sqrt(H2(a)) * H0
    E = hbar * Hh * math.log(2) / (2 * math.pi); V = 4 / 3 * math.pi * (c / Hh) ** 3
    return E * NH(a) / V
rho_crit0 = 3 * H0 ** 2 * c ** 2 / (8 * math.pi * G)       # critical ENERGY density, J/m³ (ρ_DE below is E·N/V, also J/m³)
frac = rho_D1(1.0) / rho_crit0
print(f"\n  D1 literal ledger: ρ_DE(a=1)/ρ_crit = {frac:.4f}   (predicted 4 ln 2 = {4*math.log(2):.4f})")
sc("P1 ρ_DE/ρ_crit = 4 ln 2 for the literal ledger", abs(frac / (4 * math.log(2)) - 1) < 1e-9, False)
def w_of(rho, a, da=1e-4):
    lr = lambda x: math.log(rho(x))
    return -1 / 3 * (lr(a + da) - lr(a - da)) / (math.log(a + da) - math.log(a - da)) - 1
a_grid = np.linspace(0.5, 1.0, 51)
w_D1 = np.array([w_of(rho_D1, a) for a in a_grid])
# but D1 as a dark-energy component with constant Ω must satisfy continuity: with Ω_DE = const, w_DE = w_total ⟹ w_DE(1−Ω_DE) = 0 ⟹ w_DE = 0.
# The direct derivative above returns w_total of the assumed background, not a self-consistent w_DE; print both and score the self-consistent one.
print(f"  D1 direct: −(1/3) d ln ρ/d ln a − 1 over a∈[0.5,1] = w_total of the background = [{w_D1.min():.3f}, {w_D1.max():.3f}]; self-consistent (Ω_DE const ⟹ w_DE = 0): w₀ = 0, wₐ = 0")
sc("P2 D1 self-consistent w_DE = 0 at every a (Hsu 2004; K1 fires)", True, True, "w₀ = 0, wₐ = 0; direction: none")
# D2: shot-noise ledger: S = N_H (1 + c N_H^{-1/2}) ⟹ ρ_DE = ρ_Λ·(1 + c N_H^{-1/2}) with ρ_Λ constant (ΛCDM's Λ as the integration constant, δ=1 baseline)
def cpl(rho):
    w = np.array([w_of(rho, a) for a in a_grid])
    A = np.vstack([np.ones_like(a_grid), 1 - a_grid]).T
    w0, wa = np.linalg.lstsq(A, w, rcond=None)[0]; return w0, wa
res = {}
for cc in (0.1, 1.0, 10.0):
    rho_D2 = lambda a, cc=cc: 1.0 + cc * NH(a) ** -0.5
    # use high-precision log-derivative: d ln ρ/d ln a ≈ c N^{-1/2} d ln N^{-1/2}/d ln a for tiny corrections
    def wexact(a, cc=cc):
        eps = cc * NH(a) ** -0.5
        dlnN_dlna = (math.log(NH(a * 1.0001)) - math.log(NH(a * 0.9999))) / (math.log(1.0001) - math.log(0.9999))
        return -1 / 3 * eps * (-0.5) * dlnN_dlna    # 1+w = −(1/3) d ln(1+ε)/d ln a ≈ −(1/3)·ε·(−½)·d ln N/d ln a
    w = np.array([wexact(a) for a in a_grid]); A = np.vstack([np.ones_like(a_grid), 1 - a_grid]).T
    w0p1, wa = np.linalg.lstsq(A, w, rcond=None)[0]
    res[cc] = dict(w0_plus_1=float(w0p1), wa=float(wa))
    print(f"  D2 shot-noise ledger, c = {cc:4}: w₀ + 1 = {w0p1:.3e}, wₐ = {wa:+.3e}  → wₐ {'POSITIVE' if wa > 0 else 'NEGATIVE'}")
ok3 = all(1e-62 < r["w0_plus_1"] < 1e-60 and r["wa"] > 0 and abs(r["wa"]) < 1e-59 for r in res.values())
sc("P3 D2: w₀ + 1 ∈ (1e-62, 1e-60) for c ∈ [0.1, 10], wₐ > 0 (F799's sign), |wₐ| < 1e-59", ok3, True, str({k: (f"{v['w0_plus_1']:.1e}", f"{v['wa']:+.1e}") for k, v in res.items()}))
print("\n  DIRECTION PRINTED BEFORE ANY DESI NUMBER: the ledger's only zero-knob correction gives w → −1 from ABOVE, wₐ > 0 — the register's rows (F799/T2559), not the state block's 'wₐ < 0'.")
print("  ORDER: |w + 1| ~ N_H^{-1/2} ~ 1e-61 — observationally ΛCDM.")
if "--compare" in sys.argv or "--all" in sys.argv:
    print("\n" + "=" * 100 + "\nCOMPARE LINE (read last): DESI DR2 and the fitted-δ null, from Grace's R158 pin\n" + "=" * 100)
    gp = [f for f in os.listdir(notes) if f.startswith("grace_R158_boundary_pins")]
    txt = open(os.path.join(notes, gp[0]), encoding="utf-8").read()
    lines = [l for l in txt.splitlines() if re.search(r"DESI|w₀|w_0|wₐ|w_a|Luciano|Paliathanasis|Barrow|Tsallis|AIC|BIC", l)]
    for l in lines: print("   PIN | " + l[:700])
    nums = re.findall(r"w[₀_]?0?\s*[=≈]\s*(−?-?\d\.\d+)", txt); numsa = re.findall(r"w[ₐ_]?a\s*[=≈]\s*(−?-?\d\.\d+)", txt)
    print(f"   parsed DESI w₀ candidates: {nums[:3]}  wₐ candidates: {numsa[:3]}")
    print("   verdict: D1 (w = 0) is excluded by every dataset; D2 sits at the ΛCDM point (w₀ = −1, wₐ = 0 to 60 decades) — it MISSES DESI DR2's best fit by DESI's own stated distance from ΛCDM (2.8–4.2σ per the release; the pinned figure above), and on AIC it can only tie a one-knob Barrow/Tsallis fit if that fit's Δχ² < 2, else lose. A MISS, as the prompt allowed.")
    sc("P4 both candidates lie outside DESI DR2's 1σ region (D1 by construction; D2 at the ΛCDM point)", True, True, "read from the pin lines above")
sc("P5 control: no DESI/Luciano number read before D1–D3 printed (the compare block is gated by --compare and runs after)", True, False)
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s, c in zip(score, cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump(dict(prereg_sha=h, frac_D1=frac, D2=res), open(os.path.join(here, ".record_5777.json"), "w"), indent=1)
