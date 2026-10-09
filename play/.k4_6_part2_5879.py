# Part 2 of toy 5879 — written 15:40 EDT AFTER Cal S1042 (hash; credit NONE under every outcome; the run is a REPORT) and
# Lyra K4-6 (M-recoil closed negative; B2 for dust; M-mode has a sentence; M-writer's row is ƛ_e). Census: FROZEN 5877 record.
cen = json.load(open(os.path.join(here, '.record_5877_census.json')))
N_req = cen["N_req"]; cls = cen["classes"]; forks = cen["forks"]
N_atoms = 2.054e78   # hydrogen atoms in V_H,0 (5877 part 1 print; recomputed below from the census file's own numbers would need n_H; kept as the printed instrument value)
A = {lab: v for lab, v in areas.items()}
def key(sub): return next(k for k in A if sub in k)
census = {"21cm (troughs)": cls["21cm_troughs_only"], "Lyα (once)": cls["Lya_absorptions_once_fork_x1_of_LyC"],
          "LyC": cls["LyC_photoionizations_pre_z6_MD14"], "dust (primary)": cls["dust_absorptions_primary_zbar2_Eabs2eV"]}
print(f"\nPART 2 — REPORT (Cal S1042: no credit possible today). N_req = {N_req:.3e} (log {math.log10(N_req):.2f}); census classes: " +
      ", ".join(f"{k} {v:.2e}" for k, v in census.items()))
RES = []
def line(mech, c, rowlab, Acells):
    Nc = census[c] * Acells; r = math.log10(Nc / N_req); RES.append((mech, c, rowlab, Nc, r))
    print(f"   {mech:<9} {c:<16} × {rowlab:<44} → N_cells = {Nc:9.2e}  log10(N_cells/N_req) = {r:+6.2f}")
print("  needed area if one class alone carried N_req (log10 cells):", {c: round(math.log10(N_req / v), 2) for c, v in census.items()})
print("\n  M-recoil (Lyra: CLOSED NEGATIVE as a mechanism; Cal: B2 is the physics for dust; rows printed as the report asks)")
for cc in ("21cm (troughs)", "Lyα (once)", "LyC"):
    for sub in ("proton charge radius", "proton Compton", "Bohr radius"):
        line("M-recoil", cc, key(sub), A[key(sub)])
for sub in ("A = 12", "A = 28", "A = 56"):
    line("M-recoil", "dust (primary)", key(sub) + " [B1]", A[key(sub)])
for sub in ("0.01 μm", "0.1 μm", "radius 1 μm"):
    line("M-recoil", "dust (primary)", key(sub) + " [B2]", A[key(sub)])
print("\n  M-mode (the mode's étendue cell λ²; class-dependent)")
line("M-mode", "21cm (troughs)", key("21 cm"), A[key("21 cm")])
line("M-mode", "Lyα (once)", key("Lyα"), A[key("Lyα")])
line("M-mode", "LyC", key("LyC"), A[key("LyC")])
for sub in ("0.4 μm", "0.6 μm", "1.2 μm"):
    line("M-mode", "dust (primary)", key(sub), A[key(sub)])
print("\n  M-writer (Lyra: the Compton circle ƛ_e is the row; a₀ and r_e are named alternatives without a sentence) — class-independent area")
for sub in ("electron Compton", "Bohr radius", "classical electron"):
    tot = sum(census.values()) * A[key(sub)]
    for cc in census: line("M-writer", cc, key(sub), A[key(sub)])
    print(f"      sum over classes × {key(sub)[:40]}: log10(N_cells/N_req) = {math.log10(tot / N_req):+.2f}")
# sums per mechanism under the named primary combinations
print("\n  sums (all classes) under named combinations:")
combos = {
  "M-recoil B2 (physics): proton for 21-cm/Lyman, 0.1 μm grain for dust": census["21cm (troughs)"] * A[key("proton charge")] + (census["Lyα (once)"] + census["LyC"]) * A[key("proton charge")] + census["dust (primary)"] * A[key("0.1 μm")],
  "M-recoil B1 (no sentence): proton for 21-cm/Lyman, A = 28 nucleus for dust": census["21cm (troughs)"] * A[key("proton charge")] + (census["Lyα (once)"] + census["LyC"]) * A[key("proton charge")] + census["dust (primary)"] * A[key("A = 28")],
  "M-mode: 21 cm, Lyα, LyC, 0.6 μm": census["21cm (troughs)"] * A[key("21 cm")] + census["Lyα (once)"] * A[key("Lyα")] + census["LyC"] * A[key("LyC")] + census["dust (primary)"] * A[key("0.6 μm")],
  "M-writer: ƛ_e for all": sum(census.values()) * A[key("electron Compton")],
}
for k, v in combos.items():
    print(f"   {k:<72} log10(N_cells/N_req) = {math.log10(v / N_req):+6.2f}")
# K4 composition check under the one combination that lands: 21-cm-only vs dust-only subtotals
r21 = math.log10(census["21cm (troughs)"] * A[key("proton charge")] / N_req); rdust = math.log10(census["dust (primary)"] * A[key("A = 28")] / N_req)
print(f"\n  K4 composition check (proton row / B1 nucleus): 21-cm-only subtotal {r21:+.2f}, dust-only subtotal {rdust:+.2f} — " +
      ("straddle by > 1.5 decades" if abs(r21 - rdust) > 1.5 else "within 1.5 decades of each other"))
# the Eddington–Dirac identification (Cal S1042 Sec. 3), reproduced from the record's numbers
RH2 = (c / (67.36e3 / 3.0856775814913673e22)) ** 2 / lP ** 2
per_atom = census["dust (primary)"] / N_atoms + census["21cm (troughs)"] / N_atoms
dirac = RH2 / N_atoms / A[key("proton charge")]
print(f"\n  Eddington–Dirac (Cal S1042 Sec. 3): (R_H/r_p)²/N_atoms = 10^{math.log10(dirac):.2f}; absorptions per atom (dust + 21-cm) = 10^{math.log10(per_atom):.2f}; "
      f"their ratio {math.log10(per_atom / dirac):+.2f} decades = the proton-row 'landing'")
score("P2a", abs(math.log10(dirac) - 4.11) < 0.05 and abs(math.log10(per_atom) - 4.86) < 0.05, "Cal's two numbers reproduced from the frozen census: Dirac residual 10^4.11, absorptions per atom 10^4.86 — two instruments agree")
needed = {cc: math.log10(N_req / v) for cc, v in census.items()}
score("P2b", abs(needed["dust (primary)"] - 39.30) < 0.02 and abs(needed["21cm (troughs)"] - 39.78) < 0.02, "needed areas dust 39.30, 21-cm 39.78 (log cells) reproduce Cal's instrument")
land = [x for x in RES if abs(x[4]) <= 1]
others_miss = all(abs(x[4]) > 1 for x in RES if x[0] == "M-mode" or "Bohr" in x[2] or "MRN" in x[2])
score("P2c", all(("proton charge" in x[2] or "classical electron" in x[2]) for x in land) and len(land) == 2 and others_miss,
      f"the only ±1-decade landings under the per-class assignment are nuclear-scale rows: {[(x[1], x[2][:22], round(x[4], 2)) for x in land]}; "
      "dust × A = 12 nucleus is +1.15 (just outside); every M-mode row, a₀ and the grain miss by > 1 decade (M-mode by 12–28) — Cal S1042 Sec. 2 reproduced (his +0.13/+0.68 are cross-class products); CREDIT NONE (Sec. 0, 3)")
rec["N_cells_report"] = [(m, c_, r_, N_, l_) for (m, c_, r_, N_, l_) in RES]; rec["N_req"] = N_req
json.dump(rec, open(os.path.join(here, '.record_5879_menu.json'), 'w'), indent=1)
