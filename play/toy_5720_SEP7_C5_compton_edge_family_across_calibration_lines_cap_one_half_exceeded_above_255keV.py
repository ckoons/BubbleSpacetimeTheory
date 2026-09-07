#!/usr/bin/env python3
"""Toy 5720 — C5 scoring (Lyra 851a1355, Cal §893). Compton kinematics on a free electron: E' = E/(1 + x(1 − cos θ)), x = E/m_ec².
Maximal fractional transfer (backscatter) T_max = 2x/(1+2x); the dictionary's (C)-loading cost x/(1+2x) caps at 1/2.
Family: every standard calibration line above m_ec²/2 = 255.5 keV exceeds the cap. Line energies pinned to sources in the post."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
mec2 = 510.998950   # keV, CODATA 2018
lines = {"Am-241": 59.5409, "Ba-133": 356.0129, "Na-22 (annihilation)": 510.999, "Cs-137": 661.657, "Mn-54": 834.848, "Co-60 a": 1173.228, "Na-22": 1274.537, "Co-60 b": 1332.492}
print(f"{'line':22s} {'E keV':>9s} {'x':>8s} {'edge keV':>9s} {'T_max=2x/(1+2x)':>16s} {'cost x/(1+2x)':>14s} {'exceeds 1/2':>11s}")
out = {}
for name, E in lines.items():
    x = E / mec2; Tmax = 2 * x / (1 + 2 * x); edge = E * Tmax; cost = x / (1 + 2 * x)
    out[name] = {'E': E, 'x': x, 'edge': edge, 'Tmax': Tmax, 'cost': cost}
    print(f"{name:22s} {E:9.3f} {x:8.5f} {edge:9.3f} {Tmax:16.5f} {cost:14.5f} {str(Tmax > 0.5):>11s}")
print(f"\nT_max > 1/2 iff x > 1/2 iff E > m_ec²/2 = {mec2/2:.3f} keV: every line above 255.5 keV is a witness; Cs-137's edge = {out['Cs-137']['edge']:.3f} keV, fraction {out['Cs-137']['Tmax']:.6f}.")
print("Cal's label note confirmed: at Cs-137, x = 1.29483, cost x/(1+2x) = 0.36071 (Lyra's text printed 0.360711 as 'x'; it is the cost).")
json.dump(out, open(os.path.join(HERE, '.compton_5720.json'), 'w'), indent=1)
