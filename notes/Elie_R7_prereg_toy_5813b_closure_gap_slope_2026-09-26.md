# Elie — PREREG 5813b (second, separately hashed test, owed per Cal Section 993 (3)) — written 2026-09-26 13:00 EDT; no δ read
Antecedent (Cal S993 (3), verbatim): "The discriminating statistic is the slope of log|δ| against log μ: window: 0; fixed-γ QCD: −1; one-pion-exchange deep binding: positive. … on the below-threshold subset, where the QCD predictions apply."
Invariant: δ = M − M_thr (a mass difference, scheme-independent), μ = reduced mass of the nearest V_OPEN threshold pair (Grace 5810's definitions, unchanged).
Subset: the states of 5813's frozen class with δ < 0 (below threshold). If fewer than 4 states, report 'no test'.
Statistic: OLS slope b of log|δ| on log μ; 95 % interval by case bootstrap (10⁴ resamples, fixed seed 5813) and by the OLS t-interval (both reported).
Rule: a hypothesis is DISFAVOURED iff its predicted slope lies outside the 95 % bootstrap interval. Window: b = 0. Fixed-γ: b = −1. OPE-deep: b > 0 (disfavoured iff the whole interval is ≤ 0).
DIRECTION (mine, stated with its reason): NO DISCRIMINATION — the below-threshold μ's span at most D D̄ (~930 MeV) to B B̄* (~2650 MeV), a lever of ~1 in log μ, and |δ| is noisy at the MeV level; I expect the 95 % interval to contain both 0 and −1. Can fail: an interval that excludes 0 (window disfavoured) or excludes −1 (fixed-γ disfavoured).
Secondary (reported, not scored): the same slope on all 17 with |δ|, and the leverage (sd of log μ).
