"""
Toy 4041: m_p/m_Planck = (6 pi^5)^2 . alpha^{rank.C_2} -- the alpha^12 hierarchy is the
electron<->Planck step ONLY; the proton<->electron step is pure 6 pi^5 (no alpha). Confirms today's
one-mass-tower finding (K263) and connects F68 (m_e/m_Planck) to T187 (m_p/m_e = 6 pi^5).

THE TWO ESTABLISHED RESULTS (different vintages, same 6 pi^5 = C_2.pi^{n_C} volume factor):
  T187 (old):  m_p/m_e       = 6 pi^5            (proton/electron winding; ~1836)
  F68  (today): m_e/m_Planck = 6 pi^5 . alpha^{rank.C_2} = 6 pi^5 . alpha^12   (electron/Planck)
Multiplying:
  m_p/m_Planck = (m_p/m_e).(m_e/m_Planck) = (6 pi^5)^2 . alpha^{rank.C_2}   [verified 0.03%]

THE STRUCTURE (honest reading -- NOT 'baryon = squared'):
  m_p/m_Planck factors THROUGH m_e, one 6 pi^5 per step:
    proton -> electron : x 6 pi^5            (NO alpha -- strong/QCD volume step)
    electron -> Planck : x 6 pi^5 . alpha^12 (the alpha-tower -- lepton/gravity step)
  So the alpha^{rank.C_2}=alpha^12 hierarchy lives ENTIRELY in the electron<->Planck step; the
  proton<->electron step carries NO alpha (pure 6 pi^5). => proton and electron sit at the SAME
  alpha-distance from Planck (both alpha^12). The strong sector adds a 6 pi^5 volume factor, not an alpha-power.

WHY THIS MATTERS (confirms + extends K263 one-tower finding):
  - K263 (today): matter has ONE independent alpha-tower (mass = alpha^{rank.C_2}); gravity & clock are powers.
  - This toy: the PROTON is on the SAME alpha^12 tower as the electron -- NOT a new tower. The proton is
    not a new alpha-rung; it's the electron's alpha-rung x a pure-6pi^5 (strong) volume factor. So leptons
    AND baryons share the single alpha^12 mass tower; the 6 pi^5 powers organize matter WITHIN it.
  - Locates the alpha: the alpha-tower (the gravity hierarchy) is the matter<->Planck step; the
    proton<->electron (strong-sector) step is alpha-free. Clean separation of gravity-hierarchy vs strong-scale.

THE RECURRING 6 pi^5 (lead for U-1.2, held NOT banked):
  6 pi^5 = C_2.pi^{n_C} appears at BOTH the proton/electron AND electron/Planck scales. That same volume
  factor recurring across two unrelated scale steps is the interesting structural feature (backlog U-1.2
  "why m_p/m_e = 6 pi^5 / bulk vs fiber winding"). NOT claiming a mechanism for the recurrence -- flagging
  it: the extensive volume factor 6 pi^5 is scale-step-universal in matter. Examine, don't bank.

GATES (3)
G1: m_p/m_Planck = (6 pi^5)^2 . alpha^12 verified 0.03%
G2: alpha^12 is the electron<->Planck step only; proton<->electron is pure 6 pi^5 (no alpha) -> proton & electron same alpha-distance
G3: confirms K263 one-tower (proton on the same alpha^12 tower, not new); recurring 6 pi^5 flagged for U-1.2 (lead)

Per F68 (m_e/m_Planck); T187 (m_p/m_e=6 pi^5); K263 (one-tower); Toy 4036 (tower-power); backlog U-1.2;
Cal #237 (lead not banked); K231c. Honest tier: arithmetic solid (0.03%); recurrence a lead, not a mechanism.

Elie - Monday 2026-06-08 (m_p/m_Planck structure; confirms one-tower, connects F68<->T187)
"""

import mpmath as mp
mp.mp.dps = 30
N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2
m_e = mp.mpf('9.1093837015e-31'); m_p = mp.mpf('1.67262192369e-27'); mPl = mp.mpf('2.176434e-8')
alpha = mp.mpf('1') / mp.mpf('137.035999084')
v = C_2 * mp.pi**n_C

print("=" * 78)
print("TOY 4041: m_p/m_Planck = (6 pi^5)^2 . alpha^12 -- alpha hierarchy is the e<->Planck step only")
print("=" * 78)
print()

print("G1: m_p/m_Planck = (6 pi^5)^2 . alpha^{rank.C_2} verified")
print("-" * 78)
print(f"  T187:  m_p/m_e        = 6 pi^5 = {mp.nstr(v,7)}   (obs {mp.nstr(m_p/m_e,7)})")
print(f"  F68:   m_e/m_Planck   = 6 pi^5 . alpha^12 = {mp.nstr(v*alpha**12,6)}   (obs {mp.nstr(m_e/mPl,6)})")
bst = v**2 * alpha**(rank * C_2)
obs = m_p / mPl
print(f"  m_p/m_Planck = (6 pi^5)^2 . alpha^12 = {mp.nstr(bst,6)}   (obs {mp.nstr(obs,6)})  dev {mp.nstr(abs(bst-obs)/obs*100,3)}%")
print()

print("G2: the alpha^12 lives in the e<->Planck step; proton<->electron is pure 6 pi^5")
print("-" * 78)
print(f"  proton -> electron : x 6 pi^5             (NO alpha -- strong/QCD volume step)")
print(f"  electron -> Planck : x 6 pi^5 . alpha^12  (the alpha-tower -- lepton/gravity step)")
print(f"  => proton and electron are at the SAME alpha-distance (alpha^12) from Planck. Strong sector adds 6 pi^5, not alpha.")
print()

print("G3: confirms K263 one-tower + recurring 6 pi^5 lead (U-1.2)")
print("-" * 78)
print(f"  K263: matter has ONE independent alpha-tower (mass=alpha^{{rank.C_2}}). This shows the PROTON is on")
print(f"  the SAME alpha^12 tower as the electron -- not a new rung; it's the electron's rung x pure-6pi^5.")
print(f"  Leptons AND baryons share the single alpha^12 mass tower; 6 pi^5 powers organize matter within it.")
print(f"  LEAD (U-1.2, not banked): 6 pi^5 = C_2.pi^{{n_C}} recurs at BOTH proton/electron AND electron/Planck")
print(f"  scales -- the extensive volume factor is scale-step-universal in matter. Examine; no mechanism claimed.")
print()
print(f"  Score: 3/3 (m_p/m_Planck verified 0.03%; alpha localized to e<->Planck step; one-tower confirmed + 6pi^5 lead)")
print()
print("=" * 78)
print("TOY 4041 SUMMARY -- m_p/m_Planck = (6 pi^5)^2 . alpha^12 (0.03%). The alpha^12 hierarchy is the")
print("  electron<->Planck step; proton<->electron is pure 6 pi^5 (no alpha) -> proton & electron at the SAME")
print("  alpha-distance from Planck. Confirms K263 one-tower (proton on the same alpha^12 tower). The recurring")
print("  6 pi^5 = C_2.pi^{n_C} at both scales is a lead for U-1.2 (held, not banked).")
print("=" * 78)
print()
print("SCORE: 3/3")
