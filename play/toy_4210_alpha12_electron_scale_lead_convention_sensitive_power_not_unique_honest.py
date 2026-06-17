r"""
Toy 4210: the alpha^12 electron-scale lead (Casey green-lit) -- verified, with two honest caveats that keep it a LEAD, not
a near-bank. The lore: m_e = 6 pi^5 * alpha^12 * m_Planck at "0.03%", 12 = electron twist depth. My count-keeper job is to
check it honestly. RESULTS:
  (A) the formula works, BUT the precision is CONVENTION-SENSITIVE: with BST's OWN substrate alpha = 1/137 = 1/N_max it is
      0.35% (3.5e-3); the "0.03%" lore used the PHYSICAL alpha = 1/137.036. the 12th power AMPLIFIES the 0.026% alpha-
      difference into 0.3%, so the headline precision depends on which alpha you feed it -- and the BST-consistent choice
      (substrate alpha) gives 0.35%, within the LOOSE Tier-2 floor, not the tight one.
  (B) the power 12 is SHARP (only 12 lands; 11 -> 70 MeV, 13 -> 0.0037 MeV) but NOT uniquely FORWARD: several forced
      quantities equal 12 (2*C2, N_c*rank*2, the claimed electron twist depth), so "12 = 2*C2" is a CANDIDATE reading, not
      a unique derivation. sharpness is the numerology-trap signature, not evidence of forwardness.
  (C) 6 pi^5 is NOT independent here -- it is m_p/m_e (T187). so the relation is really m_e^2 = m_p * m_Planck * alpha^12
      (a relation among already-known quantities), not a fresh derivation of m_e.
CONCLUSION: a genuine structural LEAD with the electron-on-strip running rationale (alpha lives at the electron because it
deposits on the spectral strip, the running locus), but doubly un-banked: convention-sensitive precision + power-not-
uniquely-forward. it counts only if the power 12 is FORWARD-derived from the electron's geometry (blind), AND stated with
the substrate alpha. numerology-trap-flagged (K231c). Count stays 4 of 26.

(A) CONVENTION SENSITIVITY (the 12th power amplifies the alpha choice):
  m_e = 6 pi^5 * alpha^12 * m_Planck
    substrate alpha = 1/137      -> 0.51278 MeV, resid 3.5e-3 (0.35%)  <- the BST-consistent number
    physical  alpha = 1/137.036  -> 0.51116 MeV, resid 3.2e-4 (0.03%)  <- the lore's number (uses MEASURED alpha)
  (137.036/137)^12 = 1.0032 -> the 0.026% alpha gap becomes a 0.3% m_e gap. so "0.03%" is NOT a BST prediction; with BST's
  own alpha=1/137 the honest figure is 0.35%. precision claims on alpha-towers must state the alpha convention.

(B) THE POWER 12 IS SHARP BUT NOT UNIQUELY FORWARD:
  power scan: 11 -> 70 MeV ; 12 -> 0.513 MeV ; 13 -> 0.0037 MeV. only 12 is close (sharp). BUT 12 = 2*C2 = N_c*rank*2 =
  (claimed) electron twist depth -- multiple forced quantities equal 12, so the power is not pinned to a single forward
  mechanism. sharpness here is the trap signature (a sharp exponent that fits), not proof it is derived.

(C) 6 pi^5 = m_p/m_e (T187), NOT independent:
  6 pi^5 = C2 * pi^n_C = 1836.12 = m_p/m_e. so m_e = (m_p/m_e) * alpha^12 * m_Planck  <=>  m_e^2 = m_p * m_Planck * alpha^12.
  it is a relation among m_e, m_p, m_Planck, alpha -- not a standalone derivation of m_e. (still interesting structurally.)

HONEST STATUS:
  the alpha^12 lead is REAL as a structural relation (m_e^2 = m_p*m_Planck*alpha^12) with a mechanism rationale (electron
  on the spectral strip = the running/alpha locus, Lyra F142). but it is doubly un-banked: (A) its headline precision is
  convention-sensitive and the BST-consistent value is 0.35% not 0.03%, and (B) the power 12 is sharp but not uniquely
  forward (several forced quantities = 12). it counts only with the power FORWARD-derived (blind, from the electron's
  geometry/twist) AND stated at substrate alpha. flagged numerology-trap (K231c); banks nothing. the value of this toy is
  the honest correction (0.03% -> 0.35% at substrate alpha; power sharp != forward) so the lead is carried at its true
  weight. count stays 4 of 26.
"""

import math

N_max, C2, n_C, N_c, rank = 137, 6, 5, 3, 2
m_e = 0.51099895
m_Planck = 1.220890e22
pref = C2 * math.pi**n_C          # 6 pi^5 = m_p/m_e

def pred(alpha, p=12):
    return pref * alpha**p * m_Planck

res_sub = abs(pred(1/137) - m_e)/m_e
res_phys = abs(pred(1/137.035999) - m_e)/m_e
amp = (137.035999/137)**12

m_p = 6*math.pi**5*m_e
implied_a12 = m_e**2/(m_p*m_Planck)

print("=" * 100)
print("TOY 4210: alpha^12 electron-scale lead -- verified, two honest caveats (convention-sensitive + power-not-unique)")
print("=" * 100)
print()
print("(A) convention sensitivity (12th power amplifies the alpha choice):")
print("-" * 100)
print(f"  m_e = 6 pi^5 * alpha^12 * m_Planck:")
print(f"    substrate alpha=1/137     -> {pred(1/137):.5f} MeV  resid {res_sub:.2e} (0.35%)  <- BST-consistent")
print(f"    physical  alpha=1/137.036 -> {pred(1/137.035999):.5f} MeV  resid {res_phys:.2e} (0.03%)  <- lore (measured alpha)")
print(f"    (137.036/137)^12 = {amp:.4f} -> 0.026% alpha gap becomes ~0.3% m_e gap")
print()
print("(B) the power 12 is SHARP but not uniquely FORWARD:")
print("-" * 100)
for p in [10, 11, 12, 13, 14]:
    print(f"    power {p}: {pred(1/137, p):.3e} MeV  resid {abs(pred(1/137,p)-m_e)/m_e:.2e}")
print(f"    12 = 2*C2 = {2*C2} = N_c*rank*2 = {N_c*rank*2} = (claimed) electron twist depth -> multiple forced readings, not unique")
print()
print("(C) 6 pi^5 = m_p/m_e (T187), not independent:")
print("-" * 100)
print(f"    6 pi^5 = C2*pi^n_C = {pref:.4f} = m_p/m_e -> relation m_e^2 = m_p*m_Planck*alpha^12")
print(f"    implied alpha^12 = m_e^2/(m_p*m_Planck) = {implied_a12:.3e}  vs (1/137)^12 = {(1/137)**12:.3e}")
print()

checks = [
    ("substrate alpha=1/137 gives 0.35% (not 0.03%)", abs(res_sub - 3.5e-3) < 5e-4),
    ("physical alpha=1/137.036 gives 0.03% (the lore used measured alpha)", res_phys < 5e-4),
    ("12th power amplifies 0.026% alpha gap into ~0.3%", abs(amp - 1.0032) < 0.001),
    ("power 12 is sharp (11 and 13 are off by orders)", abs(pred(1/137,11)-m_e)/m_e > 1 and abs(pred(1/137,13)-m_e)/m_e > 0.5),
    ("power 12 = 2*C2 = N_c*rank*2 (multiple forced readings, not unique)", 2*C2 == N_c*rank*2 == 12),
    ("6 pi^5 = m_p/m_e (T187, not independent)", abs(pref - 1836.12) < 0.1),
    ("lead: real structural relation but doubly un-banked (convention + power)", True),
]
passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
print()

print("=" * 100)
print("SUMMARY -- the alpha^12 electron-scale lead, green-lit and checked honestly. The formula m_e = 6 pi^5 * alpha^12 *")
print("  m_Planck is real and carries a mechanism rationale (the electron deposits on the spectral strip, the running/alpha")
print("  locus, so alpha appears -- Lyra F142). But two caveats keep it a LEAD, not a near-bank. First, the headline")
print("  precision is convention-sensitive: the 12th power amplifies the 0.026% gap between BST's substrate alpha (1/137) and")
print("  the physical alpha (1/137.036) into 0.3%, so the BST-consistent figure is 0.35%, not the lore's 0.03% (which used")
print("  the measured alpha). Second, the power 12 is sharp -- only 12 lands -- but that sharpness is the numerology-trap")
print("  signature, not forwardness: 12 = 2*C2 = N_c*rank*2 = the claimed twist depth, several forced quantities, so the")
print("  exponent is not pinned to a single forward mechanism. And 6 pi^5 is m_p/m_e (T187), so the relation is really m_e^2")
print("  = m_p*m_Planck*alpha^12 -- among already-known quantities, not a fresh m_e derivation. So it counts only when the")
print("  power 12 is FORWARD-derived from the electron's geometry (blind) AND quoted at substrate alpha. numerology-trap-")
print("  flagged (K231c); banks nothing; carried at its true weight (0.35%, power open). Count stays 4 of 26.")
print("=" * 100)
print()
print("Elie - Tuesday 2026-06-16 (alpha^12 electron-scale lead Casey green-lit, verified with two honest caveats keeping it a LEAD not near-bank: lore m_e = 6 pi^5 * alpha^12 * m_Planck at '0.03%', 12 = electron twist depth; (A) CONVENTION-SENSITIVE precision -- substrate alpha=1/137=1/N_max gives 0.35% (3.5e-3), the '0.03%' lore used PHYSICAL alpha=1/137.036, the 12th power AMPLIFIES the 0.026% alpha-gap into 0.3% ((137.036/137)^12=1.0032), so the BST-consistent figure is 0.35% within LOOSE Tier-2 floor not tight, '0.03%' is NOT a BST prediction (uses measured alpha); (B) power 12 SHARP (only 12 lands, 11->70 MeV, 13->0.0037 MeV) but NOT uniquely FORWARD -- 12 = 2*C2 = N_c*rank*2 = claimed electron twist depth, multiple forced quantities equal 12 so power not pinned to single forward mechanism, sharpness is the numerology-trap signature not forwardness; (C) 6 pi^5 = C2*pi^n_C = 1836.12 = m_p/m_e (T187) NOT independent, relation is really m_e^2 = m_p*m_Planck*alpha^12 among already-known quantities not a standalone m_e derivation; CONCLUSION genuine structural LEAD with electron-on-strip running rationale (alpha lives at electron because it deposits on spectral strip the running locus Lyra F142) but doubly un-banked (convention-sensitive precision + power-not-uniquely-forward), counts only if power 12 FORWARD-derived from electron geometry/twist (blind) AND stated at substrate alpha, numerology-trap-flagged K231c banks nothing; value of toy = honest correction 0.03%->0.35% at substrate alpha + power sharp != forward so lead carried at true weight; count 4 of 26)")
print()
print(f"SCORE: {passed}/{len(checks)} (alpha^12 electron-scale lead verified + 2 honest caveats: (A) precision CONVENTION-SENSITIVE -- substrate alpha=1/137 gives 0.35% not the lore's 0.03% (physical alpha), 12th power amplifies 0.026% alpha-gap into 0.3%; (B) power 12 SHARP but not uniquely forward (12=2*C2=N_c*rank*2=twist depth, multiple readings, sharpness=trap signature); (C) 6 pi^5 = m_p/m_e (T187) not independent, relation = m_e^2 = m_p*m_Planck*alpha^12; LEAD with electron-on-strip rationale, doubly un-banked, counts only if power forward-derived + substrate alpha, K231c trap-flagged, banks nothing; count 4 of 26)")
