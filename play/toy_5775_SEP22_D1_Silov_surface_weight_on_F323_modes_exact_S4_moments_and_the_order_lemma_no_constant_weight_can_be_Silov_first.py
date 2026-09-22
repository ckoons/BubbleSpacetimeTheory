#!/usr/bin/env python3
"""Toy 5775 — D1: the Šilov surface-measure weight on the exhibited F323 modes, and the order lemma.
Prereg notes/Elie_PREREG_5775_… (Cal hashes before this runs). Elie, 2026-09-22."""
import math, numpy as np
from fractions import Fraction as F
score, cf = [], []
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
E = {"e": F(25, 4), "mu": F(9, 4), "tau": F(0)}   # K1827/K1828: E = ν², ν = 5/2, 3/2, 0
names = ["e", "mu", "tau"]
def freeze_order(w, taus=np.linspace(1e-9, 12, 240001)):
    """AMENDED 09-22 11:1x (post-freeze; diff posted, instrument only): returns (losers, final_leader).
    freeze = LOSING the lead (K1828 reading, Cal §981 pin). losers = channels in the order they lose leadership;
    the final leader never freezes. τ starts at 1e-9 so the τ = 0 tie does not fabricate a leader."""
    W = np.array([float(w[n]) for n in names]); Ev = np.array([float(E[n]) for n in names])
    lead = np.argmax(np.log(W)[None, :] - taus[:, None] * Ev[None, :], axis=1)
    seq = []
    for L in lead:
        if not seq or seq[-1] != L: seq.append(int(L))
    return [names[i] for i in seq[:-1]], names[seq[-1]]
print("=" * 100 + "\nTOY 5775 — D1: Šilov surface weight on F323 modes; the order lemma\n" + "=" * 100)
# P2: exact Šilov weights = moments of r² = x1²+x2² on S⁴ (Beta(1, 3/2))
a, b = F(1), F(3, 2)
def beta_moment(k):
    v = F(1)
    for j in range(k): v *= (a + j) / (a + b + j)
    return v
w_S = {n: beta_moment(k) for n, k in zip(names, (0, 1, 2))}
rng = np.random.default_rng(5775); X = rng.normal(size=(2_000_000, 5)); X /= np.linalg.norm(X, axis=1, keepdims=True)
r2 = X[:, 0] ** 2 + X[:, 1] ** 2; mc = [1.0, r2.mean(), (r2 ** 2).mean()]
print(f"  Šilov weights w_k = ⟨(x₁²+x₂²)^k⟩_{{S⁴}}: exact {[str(w_S[n]) for n in names]} = {[float(w_S[n]) for n in names]}; MC {[round(m, 4) for m in mc]}")
sc("P2 existence gate: three finite non-zero weights, exact (1, 2/5, 8/35), MC agrees to 3 digits", all(0 < w_S[n] < math.inf for n in names) and all(abs(mc[i] - float(w_S[n])) < 2e-3 for i, n in enumerate(names)), True)
# P3: switch times and order with the Šilov weights
t_emu = math.log(float(w_S["e"] / w_S["mu"])) / float(E["e"] - E["mu"]); t_mutau = math.log(float(w_S["mu"] / w_S["tau"])) / float(E["mu"] - E["tau"])
losers_S, final_S = freeze_order(w_S)
print(f"  switch times: τ_eμ = ln(5/2)/4 = {t_emu:.5f}, τ_μτ = ln(7/4)/(9/4) = {t_mutau:.5f} → μ leads for Δτ = {t_mutau - t_emu:.4f}; lose-the-lead order: {losers_S}, final leader {final_S} (never freezes)")
sc("P3 Šilov weights: e freezes first, then μ; τ (Šilov) is the final leader and never freezes — the reverse of the frozen order", losers_S == ["e", "mu"] and final_S == "tau", True)
# P4 control: equal weights reproduce Lecture 6's certified negative
eq_losers, eq_final = freeze_order({n: F(1) for n in names})
rank_eq = sorted(names, key=lambda n: -float(E[n]))   # population e^{-τE} ranks lowest-first by E for any τ>0: e < μ < τ
sc("P4a equal weights: τ leads from τ>0 and never loses (no channel freezes below it); population order for τ>0 is e < μ < τ = K1828's strict reverse of Šilov-first", eq_final == "tau" and eq_losers == [] and rank_eq == ["e", "mu", "tau"], False, f"losers {eq_losers}, final {eq_final}")
# P1 lemma, checked numerically: sweep 10^4 random positive triples over 8 decades; count Šilov-first outcomes
cnt = {"silov_first_loser": 0, "e_first_loser": 0, "mu_first_loser": 0, "no_switch": 0, "final_not_tau": 0}
for _ in range(10_000):
    w = {n: F(10) ** int(rng.integers(-4, 5)) * F(int(rng.integers(1, 100)), int(rng.integers(1, 100))) for n in names}
    losers, final = freeze_order(w)
    if final != "tau": cnt["final_not_tau"] += 1
    if not losers: cnt["no_switch"] += 1
    else: cnt[{"tau": "silov_first_loser", "e": "e_first_loser", "mu": "mu_first_loser"}[losers[0]]] += 1
print(f"  sweep of 10,000 random positive weight triples (8 decades): {cnt}")
sc("P1 lemma: the Šilov stratum is NEVER the first to lose the lead, and is the final leader in every case (0 exceptions in 10,000)", cnt["silov_first_loser"] == 0 and cnt["final_not_tau"] == 0, True)
print("  proof in one line: for E_j < E_k, (w_j/w_k)·e^{(E_k−E_j)τ} is increasing in τ, so k can lose the lead only to lower-E channels; E_τ = 0 is the minimum, so τ never loses the lead and cannot freeze first.")
print("\nVERDICT: FLOOR-BY-ORDER. The Šilov surface weight EXISTS (three finite non-zero numbers, zero freedom) — and it cannot matter: under leadership-switch freeze-out with E = ν², "
      "no constant weight of any kind can make the Šilov stratum freeze first. The door Lecture 6 names is not a door for this mechanism; a successor must change the E's or the switch rule, not the weights.")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s, c in zip(score, cf) if c and s)}/{sum(cf)} can-fail hit")
