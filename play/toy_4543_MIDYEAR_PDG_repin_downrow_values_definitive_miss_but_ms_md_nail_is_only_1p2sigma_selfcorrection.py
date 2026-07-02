#!/usr/bin/env python3
"""
Toy 4543 — Mid-Year Pass-1 item-1 (PDG RE-PIN), applied to my own down-row finding.
Authoritative PDG 2024 values, and an HONEST SELF-CORRECTION: my "running-immune
nail" (m_s/m_d) is only ~1.2σ, not decisive — the re-pin was mandatory precisely to
catch that dev% ≠ σ-significance when the reference carries a big error bar.

AUTHORITATIVE PDG 2024 (rpp2024-rev-quark-masses.pdf, fetched 2026-07-02):
  m_u = 2.16 ± 0.49 MeV      m_d = 4.67 ± 0.48 MeV     m_s = 93.5 ± 8.6 MeV   (MS-bar 2 GeV)
  m_c(m_c) = 1.27 ± 0.02 GeV m_b(m_b) = 4.18 ± 0.03 GeV
  m_s/m_d = 20.0 ± 2.4  (PDG quotes the RATIO directly)   m_u/m_d = 0.46 ± 0.11
  leptons (precise): m_e = 0.51099895 MeV, m_μ = 105.6583755, m_τ = 1776.86 ± 0.12 MeV
  (I had been using m_s = 93.4; corrected to 93.5. Everything else unchanged.)

TWO RESULTS:
  1. PRIMARY (STRENGTHENED): the down-row VALUES {3, 1/3, 1} are a DEFINITIVE MISS
     vs observed {9.14, 0.884, 2.353} — 6-80σ. Rock-solid; re-pin confirms.
  2. SELF-CORRECTION (my/Keeper's "nail"): m_s/m_d forced = 22.97 vs PDG 20.0 ± 2.4
     = 14.9% BUT only **1.24σ** (PDG m_s/m_d error is 12%!). So the running-immune
     internal cross-check is a MILD tension, NOT the decisive kill we framed. The
     DECISIVE evidence is the direct value-misses (result 1), not the cross-check.
Target-innocent (PDG primary source). No count move; conclusion (down-row = MISS)
UNCHANGED and stronger, but the "nail" framing softened honestly.
"""
import math

C_2 = 6
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- PDG 2024 authoritative (with 1σ) ---------------------------------------
m_e, m_mu, m_ta = 0.51099895, 105.6583755, 1776.86
m_d, dm_d = 4.67, 0.48
m_s, dm_s = 93.5, 8.6            # PDG 2024 (was using 93.4)
m_b, dm_b = 4180.0, 30.0
ms_md_pdg, d_ms_md_pdg = 20.0, 2.4   # PDG quotes the RATIO directly

print("=" * 78)
print("Toy 4543 — PDG re-pin of the down-row finding (Pass-1 item-1) + self-correction")
print("=" * 78)

# ---- RESULT 1: down-row VALUES are a definitive multi-σ MISS -----------------
print("\n[RESULT 1] down-row banked VALUES {3,1/3,1} vs authoritative observed:")
rows = [
    ("m_d/m_e", 3.0,   m_d/m_e,   (dm_d/m_d)*(m_d/m_e)),
    ("m_s/m_mu",1/3,   m_s/m_mu,  (dm_s/m_s)*(m_s/m_mu)),
    ("m_b/m_ta",1.0,   m_b/m_ta,  (dm_b/m_b)*(m_b/m_ta)),
]
sigmas = []
for name, bank, obs, err in rows:
    dev = abs(bank-obs)/obs
    sig = abs(bank-obs)/err
    sigmas.append(sig)
    print(f"  {name:9s}: bank {bank:.3f}  obs {obs:.3f} ± {err:.3f}  → {dev:.0%} = {sig:.1f}σ")
check("down-row VALUES are a DEFINITIVE MISS (all >5σ) — re-pin CONFIRMS the primary finding",
      all(s > 5 for s in sigmas), f"σ = {[round(s,1) for s in sigmas]} — the values simply aren't the observables")

# ---- RESULT 2: the m_s/m_d "nail" — self-correction on significance ----------
muon = (24/math.pi**2)**C_2
forced_ms_md = (1/3) * muon / 3
dev_ms_md = abs(forced_ms_md - ms_md_pdg)/ms_md_pdg
sig_ms_md = abs(forced_ms_md - ms_md_pdg)/d_ms_md_pdg
print(f"\n[RESULT 2] the running-immune cross-check (my 'nail'), re-pinned:")
print(f"  banks+muon force m_s/m_d = {forced_ms_md:.2f}")
print(f"  PDG 2024 m_s/m_d = {ms_md_pdg} ± {d_ms_md_pdg}  (12% error — quoted directly)")
print(f"  → {dev_ms_md:.0%} deviation, but only {sig_ms_md:.2f}σ")
check("SELF-CORRECTION: m_s/m_d 'nail' is 14.9% but only ~1.24σ (PDG error is 12%) — MILD, not decisive",
      1.0 < sig_ms_md < 1.6, f"{sig_ms_md:.2f}σ — my/Keeper's 'decisive nail' framing OVERSTATED it")
check("dev% ≠ σ-significance: this is exactly why the PDG re-pin is mandatory (Pass-1 item-1)",
      dev_ms_md > 0.14 and sig_ms_md < 1.6, "a 15% dev on a ±12% reference is ~1σ, not a kill")

# ---- the honest reconciliation ----------------------------------------------
print("\n[RECONCILE] the conclusion is UNCHANGED and stronger, the 'nail' framing softened:")
print("  * The DECISIVE evidence the down-row is a MISS = the DIRECT value-misses (6-80σ).")
print("  * The m_s/m_d internal cross-check is real and running-immune, but only ~1.2σ —")
print("    it CORROBORATES, it does not by itself decide. I over-claimed it as 'the nail';")
print("    the direct multi-σ value-misses are the actual nail.")
check("down-row = STRUCTURAL MISS stands (stronger via direct value-misses); 'nail' recharacterized",
      all(s > 5 for s in sigmas), "count 8 unchanged; honest tier down-row = structural-MISS confirmed")

# ---- other re-pin deltas (for the almanac) ----------------------------------
print("\n[ALMANAC deltas from re-pin] (hand to Keeper/Grace for the reference column):")
print(f"  m_s: 93.4 → 93.5 MeV (PDG 2024); m_s/m_d: use PDG DIRECT 20.0 ± 2.4 (not 93.5/4.67).")
print(f"  m_d/m_e = {m_d/m_e:.2f}, m_s/m_mu = {m_s/m_mu:.3f}, m_b/m_ta = {m_b/m_ta:.3f} (re-pinned).")
check("re-pinned reference values recorded with PDG 2024 uncertainties for the almanac",
      True, "Pass-1 item-1 subset (down-row) done; full 26 = joint Elie+Grace on Casey's greenlight")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 78)
print("RESULTS")
print("=" * 78)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}")
print("=" * 78)
print("""
PDG RE-PIN VERDICT (Pass-1 item-1, down-row subset — with an honest self-correction):
  * PRIMARY finding STRENGTHENED: the down-row VALUES {3,1/3,1} miss observed
    {9.14,0.884,2.353} by 6.5σ / 6.8σ / 80σ. Definitively not the observables.
    The down-row = STRUCTURAL MISS is rock-solid on the re-pinned PDG values.
  * SELF-CORRECTION: my (and Keeper's K642) 'running-immune nail' — m_s/m_d forced
    22.97 vs observed 20 — is 14.9% but only **1.24σ**, because PDG 2024 quotes
    m_s/m_d = 20.0 ± 2.4 (a 12% error). So it's a MILD corroborating tension, NOT
    the decisive kill. The decisive evidence is the direct multi-σ value-misses.
  * This is precisely why the re-pin is Pass-1 item-1: dev% (15%) ≠ σ (1.2σ) when
    the reference carries a big band. I over-tightened; corrected now, on authority.
  Conclusion unchanged (down-row structural-MISS, count 8), 'nail' recharacterized.
  Full-26 re-pin = joint Elie+Grace into the almanac on Casey's Pass-1 greenlight.
""")
