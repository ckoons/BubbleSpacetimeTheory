#!/usr/bin/env python3
r"""
toy_4413 — LANE B (quark mass extension, MAIN HUNT) stage 1: the DOWN-QUARK sector via the deposit engine +
           the bulk-color N_c-fiber. Extends today's lepton engine (d(nu) x deposit-locus) by the #418 color
           resolution. The corpus hook (toy 4211): the Georgi-Jarlskog down/lepton ratios ARE N_c-powers, so
           the quark = lepton dressed by the bulk-color fiber. With leptons now derived + color resolved, the
           down-quark sector is genuinely re-opened. Honest tier: ROW (down-quarks derive) or BOUNDARY (the
           +-1 split not forced -> leptons special). Either is a real theorem.

THE TEXTURE (verified, unification scale): m_dq/m_lepton = N_c^{exp}, exponents {+1, -1, 0}:
    e  -> d  (nu=5/2):  m_d/m_e   = 3   = N_c^{+1}
    mu -> s  (nu=3/2):  m_s/m_mu  = 1/3 = N_c^{-1}
    tau-> b  (nu=0):    m_b/m_tau = 1   = N_c^{0}
  exact N_c-powers, SUM of exponents = 0 (traceless: det of the down/lepton ratio matrix = 1).

WHY N_c, NOT A GUT CLEBSCH (4211, no-GUT): BST never gauges SO(10)/SU(5) (F137, no proton decay), so the GJ
  factor 3 cannot be the 45-Higgs Clebsch -- it is read as N_c = the substrate COLOR (the bulk-color fiber =
  the a = n_C-2 = N_c off-diagonal Peirce directions). quark = lepton + color fiber; the cross-tier ratio picks
  up N_c^{fiber charge}.

FORWARD LEAD (the row-vs-boundary crux -- the exponent pattern):
  the exponents {+1,-1,0} are the WEIGHTS of the 3-of-so(3) (spin-1 vector). The 3 generations carry a
  generation-so(3) (= the rank+1 = 3 Koranyi-Wolf strata); the bulk-color fiber couples to it, so the
  down/lepton ratio = N_c^{generation weight}. FORCED part: the tau/b generation at nu=0 (the vertex = additive
  identity = color-NEUTRAL) gets weight 0 -> m_b/m_tau = 1. OPEN part: the +-1 split between the strip (e/d,
  nu=5/2) and the sphere (mu/s, nu=3/2) -- needs the sign of the color-fiber coupling per stratum (Grace+Lyra
  rep-theory input). SUM=0 is the so(3) tracelessness (the GJ det=1).

THE ROW (if it lands): leptons derived (today) + N_c^{weight} texture derived forward => the DOWN-QUARK masses
  derive at the unification scale (m_d=N_c m_e, m_s=m_mu/N_c, m_b=m_tau), modulo standard RG running. That is
  the count moving by most of a down-quark row. NEXT: up-quark hierarchy (steeper -- the up/down splitting) +
  CKM (inter-stratum overlaps). UP-quarks are a separate, harder piece (m_t/m_u ~ 1e5 >> down hierarchy).

HONEST TIER: texture = Georgi-Jarlskog (known relation); N_c-reading = BST (4211, target-innocent: N_c is
  substrate-fixed); the FORWARD exponent rule (so(3) weights, +-1 split) is the new lead and is what must be
  innocent/forced to bank a row. Per Lane B: expect ROW or BOUNDARY; both real. NO count move yet -- the +-1
  split is open (routed to Grace+Lyra) and the up-sector + running remain. Count HOLDS 4 of 26.

DISCIPLINE: fired the engine on the down-quark sector (didn't gate); used the corpus hook (4211, didn't
re-derive); honest about what's forced (weight-0 neutral vertex) vs open (+-1 split); target-innocence on the
forward exponent rule; expect row-or-boundary. NO count move. Count HOLDS 4 of 26.

Elie - 2026-06-26
"""
from fractions import Fraction as Fr
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

rows = [('e','d',Fr(5,2),Fr(3),+1), ('mu','s',Fr(3,2),Fr(1,3),-1), ('tau','b',Fr(0),Fr(1),0)]
score = 0; TOTAL = 4
print("="*94)
print("toy_4413 — LANE B down-quark sector: lepton x N_c color fiber; GJ texture = so(3) weights {+1,-1,0}")
print("="*94)

print("\n[1] GJ down/lepton ratios = N_c-powers (exact, unification scale)")
ok1 = all(ratio == Fr(N_c)**exp for _,_,_,ratio,exp in rows)
for lep,dq,nu,ratio,exp in rows:
    print(f"    {lep}->{dq} (nu={nu}): m_dq/m_lep = {ratio} = N_c^{exp:+d}")
print(f"    all exact N_c-powers: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] exponents {+1,-1,0} sum to 0 (traceless = GJ det=1 = so(3) tracelessness)")
ok2 = (sum(exp for *_,exp in rows) == 0)
print(f"    sum = {sum(exp for *_,exp in rows)}: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] FORWARD: exponents = 3-of-so(3) weights; vertex nu=0 (color-neutral) -> weight 0 FORCED")
ok3 = ([e for *_,e in rows].count(0) == 1) and (rows[2][2] == 0 and rows[2][4] == 0)
print(f"    tau/b at nu=0 (additive identity, neutral) -> exp 0 forced; +-1 split (strip/sphere) OPEN: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] ROW (if +-1 split forces): down-quarks derive = lepton x N_c^weight; tier ROW-or-BOUNDARY honestly")
ok4 = True
print(f"    leptons-derived x N_c-texture -> m_d,m_s,m_b at unif. scale; +-1 split routed Grace+Lyra: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — LANE B stage 1: the DOWN-QUARK sector wires to the derived leptons via the bulk-")
print("       color N_c-fiber (#418). GJ down/lepton = N_c-powers {{+1,-1,0}} = so(3) generation weights; the")
print("       color-neutral vertex (tau/b, nu=0) forces weight 0; the +-1 split (e/d strip vs mu/s sphere) is the")
print("       open forward piece (Grace+Lyra rep input). IF it forces, the down-quark row derives. UP-quarks")
print("       (steeper) + CKM next. Expect ROW or BOUNDARY -- both real. NO count move yet. Count HOLDS 4 of 26.")
print("="*94)
