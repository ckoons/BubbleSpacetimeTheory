#!/usr/bin/env python3
"""Cal Section 984 -- two adversarial checks on K1923 Sections 2-3 (2026-09-25).
Inputs: Grace R159 pins (PDG 2026) and K1923's K; beam value 887.7(2.2) is K1923's UNPINNED compare value.
PREDICTIONS written before the run:
 P1  g_A = 4/pi lies BETWEEN the lambda the bottle route implies and the lambda the beam route implies,
     i.e. 4/pi is 'fired' only conditional on the bottle-beam discrepancy being resolved toward the bottle.
 P2  A2 (V_ud^2 = 19/20) and generic unitarity with the K_l3 |V_us| give products tau(1+3l^2) that differ by
     about one sigma of K: the neutron product cannot separate A2 from 'unitarity with measured V_us' today.
 P3  the tau precision needed to separate them at 3 sigma is below 0.1 s (with K's error held at 1.7 s it is impossible).
"""
from math import sqrt, pi
K, dK = 4905.7, 1.7
VUB2 = 1.5e-5
routes = {
 "A2 exact (19/20)":            19/20,
 "unitarity, Vus K_l3 0.22330": 1 - 0.22330**2 - VUB2,
 "unitarity, Vus avg 0.22431":  1 - 0.22431**2 - VUB2,
 "superallowed HT 0.97367":     0.97367**2,
}
taus = {"bottle UCNtau 877.82(22) [PDG2026 input]": (877.82, 0.22),
        "bottle UCNtau 877.75(34) [K1923 input]":    (877.75, 0.34),
        "beam 887.7(2.2) [unpinned]":                (887.7, 2.2)}
lam_4pi = 4/pi
print(f"4/pi = {lam_4pi:.5f};  PERKEO III 1.27641(56): {(1.27641-lam_4pi)/0.00056:.2f} sigma")
print("\nlambda implied by each (V_ud route, tau) pair; sigma of 4/pi from it:")
for rn, v2 in routes.items():
    P = K / v2
    for tn, (t, dt) in taus.items():
        l2 = (P / t - 1) / 3; l = sqrt(l2)
        # error: dP/P = dK/K ; d(P/t) = P/t*sqrt((dK/K)^2+(dt/t)^2); dl = d(l2)/(2l)
        dl = (P/t) * sqrt((dK/K)**2 + (dt/t)**2) / 3 / (2*l)
        print(f"  {rn:30s} | {tn:40s} | lambda = {l:.5f} +- {dl:.5f} | 4/pi at {(l-lam_4pi)/dl:+.1f} sigma")
print("\nP1: is 4/pi between bottle- and beam-route lambda (A2 route)?")
lb = sqrt((K/(19/20)/877.82 - 1)/3); lm = sqrt((K/(19/20)/887.7 - 1)/3)
print(f"  bottle {lb:.5f}  beam {lm:.5f}  -> between: {min(lb,lm) < lam_4pi < max(lb,lm)}")
print("\nP2: product tau(1+3l^2) = K/V_ud^2 for each route:")
PA = K/(19/20)
for rn, v2 in routes.items():
    P = K/v2; print(f"  {rn:30s} {P:8.1f} +- {P*dK/K:.1f}   diff from A2 {P-PA:+.1f} s = {(P-PA)/(P*dK/K):+.2f} sigma_K")
meas = 877.82*(1+3*1.27641**2); dmeas = sqrt((0.22*(1+3*1.27641**2))**2 + (877.82*6*1.27641*0.00056)**2)
print(f"  measured (UCNtau 877.82, PERKEO III): {meas:.1f} +- {dmeas:.1f}")
print("\nP3: separation A2 vs unitarity-K_l3 is", f"{K/(1-0.22330**2-VUB2)-PA:.2f} s;",
      "tau error contributes 5.89*dtau; K error alone 1.8 s -> 3-sigma separation needs total < %.2f s" % ((K/(1-0.22330**2-VUB2)-PA)/3))
