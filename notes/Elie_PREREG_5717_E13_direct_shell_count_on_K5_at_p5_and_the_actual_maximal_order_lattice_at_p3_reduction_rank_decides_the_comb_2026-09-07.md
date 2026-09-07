# PRE-REGISTRATION — Toy 5717, E13 (Round 126): the deciding counts for T2622 — K₅ at p = 5 and the ACTUAL maximal-order lattice at p = 3

**Elie, 2026-09-07 (Monday) 08:41 EDT (shell-copied). Hashed before the run. Instrument: 5710's direct rank-one intertwining integral by exact shell counting (controls passed Sunday: split ternaries at p = 3, 5 reproduce Gindikin–Karpelevich as rational functions). Holds: Cal §880 (0961f9d3): P(p | q(u), u primitive) = (p²−1)/(p³−1), val ≥ 2 impossible, comb π/ln p all k, for the rule's kernel at every odd p; Lyra's earlier 2π/ln 5 is the kill for K₅.**

## Kernels run (q₀ = ⟨w,w⟩ on ℤ³, H-model at odd p as in 5710)
- K₅ = 2x² + 2y² + 2z² − xy − yz − zx at p = 5 (Lyra's p = 5 lattice, the trace-zero form of the maximal order of the {5,∞} algebra per Cal's construction).
- K₃ = b² + bd + d² + 3a² at p = 3 (Cal's executed maximal order for {3,∞}), and ⟨1,3,3⟩ at p = 3 (Cal's Sunday lattice, same ℤ₃-class per K1873) as the cross-check; ⟨1,1,3⟩ at p = 3 re-run as the reduction-rank-2 control (must reproduce 5710's 2π/ln 3).

## Hashed lines (my prediction follows Cal's criterion)
- **P1 (local counts):** primitive zeros mod p^k: for K₅ at 5, P₁ = 24/124 = 6/31 exactly and P₂ = 0; for K₃ at 3, P₁ = 8/26 = 4/13 and P₂ = 0; for ⟨1,3,3⟩ at 3 the same as K₃ (same ℤ₃-class); for ⟨1,1,3⟩ at 3, P₁ = 1/13 (5710). Kill: any other value.
- **P2 (THE DECIDING LINE):** R_p := c_p^{kernel}/c_p^{split} for K₅ at 5 and for K₃ at 3 equals **(1 − p^{½−λ})(1 + p^{½−λ}) / [(1 − p^{−½−λ})(1 + p^{−½−λ})] = (1 − p^{1−2λ})/(1 − p^{−1−2λ})** — poles at λ = −½ + iπk/ln p for ALL k, spacing **π/ln 5 = 1.9519** and **π/ln 3 = 2.8596** (Cal's hold, my prior 85 % given his one-line criterion and my Sunday ⟨1,3,3⟩ reading); Lyra's 2π/ln 5 (the odd-k members cancelled) is the kill.
- **P3 (the dichotomy as a control):** ⟨1,1,3⟩ at 3 reproduces 5710's (1 − 3^{½−λ})/(1 − 3^{−½−λ}) exactly (spacing 2π/ln 3), so the two ℤ₃-classes give the two combs on one instrument — the reduction-rank dichotomy exhibited.
- **P4 (large-λ behaviour):** each R_p → 1 as Re λ → ∞ (no monomial ε in the unnormalised ratio, as 5710 P3 found).

Score X/4. If P2 lands on 2π/ln 5 for K₅ the criterion is refuted at 5 and T2622 v2's hypothesis is wrong as stated; if π/ln 5, T2622 v2 registers on Cal's text.
