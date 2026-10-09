# Part 2 of toy 5877 — written at 15:02 EDT AFTER the census record (sha 9c3f39f1…) was committed (ddf3c2ad).
# N_req per Cal S1041 Sec. 2: the count that makes rho_DE = Omega_Lambda rho_crit today under the law's own
# E_commit = hbar H0 ln2/(2 pi) and V_H = (4 pi/3)(c/H0)^3. Identity (K1919 Sec. 7): it is the horizon-area count,
# N_req = (pi Omega_Lambda / ln 2) (c/H0)^2 / l_P^2.
Om_L = 1 - Om_m                                                     # Planck 2018 baseline, flat (Omega_m = 0.3153)
rho_crit_E = 3 * H0 ** 2 * c ** 2 / (8 * math.pi * G)               # critical ENERGY density, J m^-3
E_commit = hbar * H0 * math.log(2) / (2 * math.pi)                  # Landauer's bit at T_dS
N_req = Om_L * rho_crit_E * V_H0 / E_commit
lP2 = hbar * G / c ** 3
N_req_identity = (math.pi * Om_L / math.log(2)) * (c / H0) ** 2 / lP2
print(f"  N_req = Omega_L rho_crit V_H / E_commit = {N_req:.3e}   (log10 {math.log10(N_req):.2f});  identity (pi Omega_L/ln2) (c/H0)^2/l_P^2 = {N_req_identity:.3e}")
score("I1", abs(N_req / N_req_identity - 1) < 1e-12, "N_req = (pi Omega_Lambda/ln 2)(c/H0)^2/l_P^2 — the horizon-area count in Planck units: K1919 Sec. 7's identity, exactly")
Nc = rec["N_census_primary"]; lo, hi = rec["N_census_low"], rec["N_census_high"]
r = math.log10(Nc / N_req)
print(f"\n  N_census (primary) = {Nc:.3e};  N_req = {N_req:.3e};  log10(N_census/N_req) = {r:+.2f}")
print(f"  fork span to N_req: smallest fork {lo:.2e} is {math.log10(N_req / lo):.1f} decades below N_req; largest fork {hi:.2e} is {math.log10(N_req / hi):.1f} below")
span = math.log10(N_req / lo)
print(f"  chance of a ±1-decade landing on a log-uniform null over the span (Cal's null): 2/{span:.1f} = {2 / span:.3f}")
verdict = "MATCH" if abs(r) <= 1 else ("REPORT (same kind of number)" if abs(r) <= 3 else "MISS (the pincer fires)")
print(f"  Cal S1041 rule: |log10| = {abs(r):.2f} → {verdict}")
score("T3", abs(r) <= 1, f"CREDIT iff |log10| <= 1: {verdict} — the two counts differ by {abs(r):.1f} decades; no fork comes within 38 decades (a FAIL here is the hashed test's own verdict, reported as such)")
rec["N_req"] = N_req; rec["log10_ratio_primary"] = r; rec["verdict"] = verdict
json.dump(rec, open(REC, "w"), indent=1)
print(f"\nSCORE (part 2): {sum(RESULTS)}/{len(RESULTS)}  (I1 the identity; T3 the hashed test — FAIL = MISS under Cal S1041)")
