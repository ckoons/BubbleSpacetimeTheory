#!/usr/bin/env python3
"""
Toy 5500 — LANE P FIRE HARNESS (Elie's fire-time halves). *** HOLSTERED: runs only
after Cal's §770 audit PASS + Keeper's gate on Grace's P prereg. ***
Zero mechanism content in this file: the candidate form arrives from the GATED
prereg at fire time. This file is the instrument: frozen bands, control order,
count printing. Built pre-gate so the shot spends its hour on the shot.
"""
import math
from fractions import Fraction

# FROZEN (T3 ladder + PDG 2024 — derived arithmetic, no choices; R99-published)
M_E, M_MU, M_TAU = 0.51099895069, 105.6583755, 1776.93
R_MEAS = math.log(M_MU/M_E)/math.log(M_TAU/M_MU)          # 1.88901
WIN_LO, WIN_HI  = 1.8796, 1.8985
SUGG_LO, SUGG_HI = 1.7946, 1.9835
SPREAD_MU_E, SPREAD_TAU_MU = 206.768, 16.817               # W2a capability targets (order-of)

def w2a_capability(family_R_range, family_spread_range):
    """W2a FIRST: can the gated family produce spreads ~207 and ~16.9 AND R > 1.7946?
    A search that cannot succeed proves nothing (5454). Returns PROCEED/FLOOR."""
    lo, hi = family_R_range
    ok = hi > SUGG_LO and family_spread_range[1] >= SPREAD_MU_E
    return "PROCEED" if ok else "FLOOR: family under-hierarchical or wrong-direction — lane floors, no scoring"

def w4_verdict(R_produced, free_params, targets_hit):
    """Verdict LAST. Count prints BESIDE it (§770 line 3 / Grace's rule)."""
    if free_params >= targets_hit:
        return f"CAPPED: reparameterization (free={free_params} >= targets={targets_hit})"
    dev = abs(R_produced/R_MEAS - 1)
    v = "WIN" if WIN_LO <= R_produced <= WIN_HI else ("SUGGESTIVE" if SUGG_LO < R_produced < SUGG_HI else "FAIL")
    return f"{v} (R={R_produced:.4f}, dev={100*dev:.2f}%, free={free_params}, targets={targets_hit})"

def w5_mustfail_downsector(mechanism_fn):
    """5487 must-fail RUN in the shot, not cited: the mechanism applied to the
    down tower (m_d=4.7, m_s=93.4, m_b=4180) must NOT land in the lepton WIN band."""
    R_dq = mechanism_fn(4.7, 93.4, 4180.0)
    return ("MUST-FAIL OK" if not (WIN_LO <= R_dq <= WIN_HI) else
            "MUST-FAIL VIOLATED — mechanism is sector-blind, shot invalid")

if __name__ == "__main__":
    print(__doc__)
    print(f"Frozen: R_meas={R_MEAS:.5f}  WIN=[{WIN_LO},{WIN_HI}]  SUGG=({SUGG_LO},{SUGG_HI})")
    print("SCORE: 0/0 (harness only — the gated shot scores)")
