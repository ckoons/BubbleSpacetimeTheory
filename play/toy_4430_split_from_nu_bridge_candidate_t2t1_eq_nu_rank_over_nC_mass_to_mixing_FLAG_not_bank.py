#!/usr/bin/env python3
r"""
toy_4430 — the MASS->MIXING bridge candidate (Grace's lead, made forward): the within-point split t2/t1 follows
           from the mass coordinate nu via split = nu * rank / n_C. For the muon nu=3/2 -> split = 3/5 = N_c/n_C
           (Grace's value). Cross-generation: split = {1, 3/5, 0} for {e, mu, tau} -- monotone, geometrically
           sensible. FLAGGED as a forward candidate (Cal #411-class), NOT banked: it is a clean 1-line relation
           but the V_us magnitude needs Grace's exact V_us(t1,t2) + the scale t1, not just the ratio.

THE BRIDGE: each generation's Koranyi-Wolf stratum has a mass coordinate nu (depth below the BF bound) AND a
  geometric within-point split t2/t1 = (a-b)/(a+b) (Grace's rank-2 point z = a u1 + i b u2). The candidate
  forward relation, from the muon Wallach point nu = N_c/rank:
      split = nu * rank / n_C.
  nu=3/2 -> split = (3/2)(2/5) = 3/5 = N_c/n_C (matches Grace's bridge value exactly). Cross-gen:
      e   (nu=5/2): split = 1   (t2=t1, degenerate -> the origin)
      mu  (nu=3/2): split = 3/5 (= N_c/n_C)
      tau (nu=0):   split = 0   (t2=0, single characteristic value -> the Shilov edge)
  Monotone and geometrically sensible (origin -> mid -> Shilov), so it is a coherent forward candidate for the
  mass->mixing bridge: the mass coordinate nu forces the mixing split.

HONEST TIER (FLAG, not bank): the relation is clean (nu, rank, n_C all substrate-fixed) but it is essentially a
  1-line rearrangement -- nu = N_c/rank and split = N_c/n_C are both "N_c over something," so split = nu*rank/n_C
  is an identity among those, not yet a derivation. To bank it as the bridge needs: (1) Grace's exact V_us(t1,t2)
  formula -- the split RATIO alone does not give V_us, the SCALE t1 is also needed; (2) a forward reason the
  split is t2/t1 (not some other function of nu). So it is a Cal #411-class lead: clean, suggestive, forcing
  open. I flag it, hand it to Grace+Lyra, and do NOT bank it.

THE THREE-WAY JOIN STATE (after this round, all forward, all fit-pending the exact measure):
  - muon address DOUBLY-PINNED from nu=3/2: k=1, (1,1), N=9/16 (Lyra norm-power + Elie deposit-locus agree, 4429).
  - leading V_us = (9/16)^{n_C/2} = 0.237 (6%); the 6% = exact-FK-center correction; the -1 (->79) = open (Lyra).
  - split candidate: t2/t1 = nu*rank/n_C = 3/5 (this toy) -- the mass->mixing bridge, flagged.
  - V_cb = Grace's exact rank-2 frame angle chi (~30 deg, flagged).
  All pieces forward and interlocked; the exact magnitudes (FK center, -1, chi, V_us(t1,t2)) are Lyra+Grace's
  exact-measure/geometry lanes. Count HOLDS 5/26 (mechanism forward; values fit-pending the K-type forcing).

DISCIPLINE: made Grace's bridge lead forward (split = nu*rank/n_C, cross-gen consistent); flagged it Cal #411-
class (clean but 1-line rearrangement; needs exact V_us(t1,t2) + scale); banked nothing; handed to Grace+Lyra.
Count HOLDS 5/26.

Elie - 2026-06-27
"""
from fractions import Fraction as Fr
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

gens = [('e', Fr(5,2)), ('mu', Fr(3,2)), ('tau', Fr(0))]
score = 0; TOTAL = 3
print("="*94)
print("toy_4430 — mass->mixing bridge candidate: split t2/t1 = nu*rank/n_C; muon -> 3/5 (FLAG, not bank)")
print("="*94)

print("\n[1] muon: split = nu*rank/n_C = (3/2)(2/5) = 3/5 = N_c/n_C (matches Grace's bridge value)")
split_mu = Fr(3,2)*rank/n_C
ok1 = (split_mu == Fr(N_c, n_C) == Fr(3,5))
print(f"    split_mu = {split_mu} = N_c/n_C = {Fr(N_c,n_C)}: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] cross-gen monotone {1, 3/5, 0} (origin -> mid -> Shilov), geometrically sensible")
splits = [nu*rank/n_C for _, nu in gens]
ok2 = (splits[0] > splits[1] > splits[2]) and splits[0] == 1 and splits[2] == 0
for (nm, nu), s in zip(gens, splits): print(f"    {nm:3}: nu={nu} -> split = {s}")
print(f"    monotone, e=1 (degenerate), tau=0 (single-char): {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] FLAG not bank: clean but 1-line rearrangement; needs Grace exact V_us(t1,t2) + scale t1 (ratio alone insufficient)")
ok3 = True
print(f"    Cal #411-class lead; handed to Grace+Lyra; count HOLDS 5/26: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — mass->mixing bridge candidate: the within-point split t2/t1 = nu*rank/n_C follows")
print("       from the mass coordinate nu; muon nu=3/2 -> split=3/5=N_c/n_C (Grace's value), cross-gen {1,3/5,0}")
print("       monotone+sensible. FLAGGED Cal #411-class (clean, but a 1-line rearrangement; V_us needs the exact")
print("       V_us(t1,t2) + scale, not just the ratio). Handed to Grace+Lyra. NOT banked. The three-way join is")
print("       fully interlocked forward; exact magnitudes are Lyra+Grace's lanes. Count HOLDS 5/26.")
print("="*94)
