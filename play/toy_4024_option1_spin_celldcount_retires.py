"""
Toy 4024: Option 1 (spin-dependent cell-count) -- empirical sweep -> RETIRES.

Keeper assigned Option 1: does cells = n_C + 2J (spin-dependent) explain a broader hadron
spectrum, or does the substrate reach only the 4 light u/d ground states (T2488)? Falsifier:
if the spin-3/2 light decuplet doesn't propagate cleanly at few-%, retire. Base-rate
discipline per Toy 4017. Do NOT revive the retracted lambda2-ladder (Z_2 is a bit).

RESULT: Option 1 RETIRES. Three honest reasons:
 1. cells = n_C + 2J fits NON-strange baryons p,n (J=1/2 -> 6) and Delta (J=3/2 -> 8,
    marginal), but FAILS the strange decuplet: all spin-3/2, so n_C+2J predicts 8 for ALL,
    yet Sigma*,Xi*,Omega are at 8.85, 9.80, 10.70 -- they spread by strangeness, not spin.
 2. The apparent "cells = 8 + n_strange" decuplet pattern DEGRADES into base-rate noise:
    residuals 0.12 -> 0.15 -> 0.20 -> 0.30; base-rate p 0.24 -> 0.29 -> 0.41 -> 0.61
    (%dev 1.5 -> 1.6 -> 2.1 -> 2.9). Not a clean propagation; the heavier members are noise.
 3. Excited baryons fail: N(1440) Roper (J=1/2) -> n_C+2J predicts 6, observed 9.21; N(1520)
    (J=3/2) -> predicts 8, observed 9.69. Excitations are outside the rule entirely.

So per the falsifier, Option 1 does NOT propagate cleanly -> RETIRE. This SUPPORTS Option 4
(narrow substrate reach): the substrate cleanly reaches the light-u/d GROUND states only
(rho,omega n_C=5; p,n n_C+1=6; Delta a marginal spin-3/2 addition at 8). Strangeness and
excitation degrade into base-rate noise. The Z_2 boson/fermion BIT is the robust structure;
the spin/strangeness "ladders" are NOT (confirms the lambda2-ladder retraction, T2488).

Sub-lead (weight 0, NOT established): each strange quark MIGHT add ~1 cell (8+n_s), but the
base-rate degradation says this is marginal-to-noise -- flag for Grace's base-rate filter,
do not build on it.

GATES (4)
G1: spin rule fits non-strange p,n,Delta; FAILS strange decuplet
G2: 8+n_strange pattern degrades into base-rate noise
G3: excited baryons fail
G4: verdict -> RETIRE Option 1, support Option 4 (narrow reach); ladder stays retracted

Per Toy 4017 base-rate; Keeper falsifier; Cal #237; K231c.

Elie - Sunday 2026-06-07
"""

import mpmath as mp
mp.mp.dps = 15
unit = float(mp.pi**5) * 0.51099895
n_C = 5

B = [('p', 938.272, 0.5, 0, 'octet gs'), ('n', 939.565, 0.5, 0, 'octet gs'),
     ('Delta', 1232.0, 1.5, 0, 'decuplet gs'), ('Sigma*', 1384.6, 1.5, 1, 'decuplet s'),
     ('Xi*', 1531.8, 1.5, 2, 'decuplet ss'), ('Omega', 1672.45, 1.5, 3, 'decuplet sss'),
     ('N(1440)', 1440.0, 0.5, 0, 'excited'), ('N(1520)', 1515.0, 1.5, 0, 'excited')]

print("=" * 80)
print(f"TOY 4024: Option 1 spin cell-count sweep (unit pi^5 m_e = {unit:.2f} MeV) -> RETIRES")
print("=" * 80)
print()

print("G1+G2: spin rule cells=n_C+2J vs strangeness pattern 8+n_s (base-rate)")
print("-" * 80)
print(f"  {'state':<10}{'obs':>8}{'n_C+2J':>8}{'8+n_s':>7}{'%dev(8+ns)':>11}{'p_base':>8}  {'kind'}")
for nm, m, J, ns, k in B:
    obs = m / unit
    r1 = n_C + 2 * J
    r2 = 8 + ns
    dev = abs(r2 * unit - m) / m * 100
    pb = min(1.0, 2 * abs(obs - round(obs)))
    print(f"  {nm:<10}{obs:>8.3f}{r1:>8.0f}{r2:>7}{dev:>10.1f}%{pb:>8.2f}  {k}")
print()
print("  spin rule n_C+2J: fits p,n (6), Delta (8 marginal); but predicts 8 for ALL spin-3/2")
print("    -> FAILS Sigma*,Xi*,Omega (they spread by strangeness, not spin).")
print("  8+n_s decuplet pattern: residual/p_base DEGRADE (0.24->0.61) -> base-rate NOISE, not clean.")
print()

print("G3: excited baryons fail both rules")
print("-" * 80)
print("  N(1440) Roper J=1/2: n_C+2J predicts 6, observed 9.21 -> FAIL.")
print("  N(1520) J=3/2:       n_C+2J predicts 8, observed 9.69 -> FAIL.")
print("  Excitations are outside the cell-count rule entirely.")
print()

print("G4: verdict -> RETIRE Option 1; support Option 4 (narrow reach)")
print("-" * 80)
print("  Per Keeper's falsifier (spin-3/2 light decuplet must propagate cleanly at few-%):")
print("  - the only LIGHT (non-strange) spin-3/2 baryon is Delta (8, marginal 1.5%, p=0.24).")
print("  - the strange decuplet degrades into base-rate noise; excited states fail.")
print("  => Option 1 does NOT propagate cleanly -> RETIRE.")
print()
print("  SUPPORTS OPTION 4 (narrow substrate reach): the substrate cleanly reaches the light-u/d")
print("  GROUND states only -- rho,omega (n_C=5), p,n (n_C+1=6), + Delta as a marginal spin-3/2")
print("  point (8). Strangeness and excitation degrade out. This is substrate-architectural")
print("  INFORMATION (where the substrate reaches), not failure (Cal #237 / Keeper Option 4).")
print()
print("  CONFIRMS the lambda2-ladder retraction (T2488): the spin/strangeness 'ladders' are")
print("  base-rate noise; the Z_2 boson/fermion BIT is the robust structure. Do NOT rebuild ladders.")
print()
print("  Sub-lead (weight 0): strangeness MIGHT add ~1 cell/s-quark (8+n_s), but base-rate")
print("  degradation (0.24->0.61) makes it marginal-to-noise -- @Grace base-rate filter, not built on.")
print()
print("  Score: 4/4 (spin rule fails strange decuplet; 8+n_s degrades to noise; excited fail;")
print("  Option 1 RETIRES -> Option 4 narrow reach; ladder stays retracted)")
print()
print("=" * 80)
print("TOY 4024 SUMMARY -- Option 1 (spin cell-count) RETIRES: fits non-strange p,n,Delta but the")
print("  strange decuplet degrades into base-rate noise + excited baryons fail. Supports Option 4")
print("  (narrow reach: light-u/d ground states only). Z_2 BIT robust; ladders stay retracted.")
print("=" * 80)
print()
print("SCORE: 4/4")
