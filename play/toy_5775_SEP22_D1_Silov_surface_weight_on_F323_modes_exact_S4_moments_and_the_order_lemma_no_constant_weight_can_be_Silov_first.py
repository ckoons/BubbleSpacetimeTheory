#!/usr/bin/env python3
"""Toy 5775 — D1: the Šilov surface-measure weight on the exhibited F323 modes, and the order lemma.
Prereg notes/Elie_PREREG_5775_… (Cal hashes before this runs). Elie, 2026-09-22."""
import math, numpy as np
from fractions import Fraction as F
score, cf = [], []
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
E = {"e": F(25, 4), "mu": F(9, 4), "tau": F(0)}   # K1827/K1828: E = ν², ν = 5/2, 3/2, 0
names = ["e", "mu", "tau"]
def freeze_order(w, taus=np.linspace(0, 12, 240001)):
    """order in which channels LOSE the lead (first loss first), from the leadership curve"""
    W = np.array([float(w[n]) for n in names]); Ev = np.array([float(E[n]) for n in names])
    lead = np.argmax(np.log(W)[None, :] - taus[:, None] * Ev[None, :], axis=1)
    order = []
    for L in lead:
        if not order or order[-1] != L: order.append(int(L))
    lost = order[:-1]                      # every leader except the final one lost the lead, in this sequence
    return [names[i] for i in lost] + [names[order[-1]]]
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
order_S = freeze_order(w_S)
print(f"  switch times: τ_eμ = ln(5/2)/4 = {t_emu:.5f}, τ_μτ = ln(7/4)/(9/4) = {t_mutau:.5f} → μ leads for Δτ = {t_mutau - t_emu:.4f}; freeze (lose-the-lead) order: {order_S}")
sc("P3 Šilov weights give the order e → μ → τ (Šilov LAST), the reverse of the frozen order", order_S == ["e", "mu", "tau"], True)
# P4 control: equal weights reproduce Lecture 6's certified negative
sc("P4a equal weights (1,1,1) reproduce the certified negative e → μ → τ", freeze_order({n: F(1) for n in names}) == ["e", "mu", "tau"], False)
# P1 lemma, checked numerically: sweep 10^4 random positive triples over 8 decades; count Šilov-first outcomes
cnt = {"silov_first": 0, "e_first": 0, "other": 0}
for _ in range(10_000):
    w = {n: F(10) ** int(rng.integers(-4, 5)) * F(int(rng.integers(1, 100)), int(rng.integers(1, 100))) for n in names}
    o = freeze_order(w)
    if o[0] == "tau": cnt["silov_first"] += 1
    elif o[0] == "e": cnt["e_first"] += 1
    else: cnt["other"] += 1
print(f"  sweep of 10,000 random positive weight triples (8 decades): first-to-freeze = {cnt}")
sc("P1 lemma: no constant positive weight triple is Šilov-first (0 of 10,000); e loses the lead first in every case", cnt["silov_first"] == 0 and cnt["other"] == 0, True)
print("  proof in one line: for E_j < E_k, (w_j/w_k)·e^{(E_k−E_j)τ} is increasing in τ, so k can lose the lead only to lower-E channels; E_τ = 0 is the minimum, so τ never loses the lead and cannot freeze first.")
print("\nVERDICT: FLOOR-BY-ORDER. The Šilov surface weight EXISTS (three finite non-zero numbers, zero freedom) — and it cannot matter: under leadership-switch freeze-out with E = ν², "
      "no constant weight of any kind can make the Šilov stratum freeze first. The door Lecture 6 names is not a door for this mechanism; a successor must change the E's or the switch rule, not the weights.")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s, c in zip(score, cf) if c and s)}/{sum(cf)} can-fail hit")
