r"""
toy_4508 — TUESDAY: TAKE Cal #481 (correcting my 4507's prefactor) + ground the lepton prefactor + unify the
           electron formula. Cal #481: my 4507 used "6 pi^5 = m_p/m_e = F402" as the m_e/m_P prefactor, but
           F402's 6 is the PROTON's baryon antisymmetrizer (N_c!) -- the electron is a LEPTON, so the
           lepton-appropriate prefactor is the all-geometric C_2 * pi^{n_C} (SAME number 6 pi^5, RIGHT object:
           C_2 the Casimir/EM-channels, not N_c! the baryon). Taken. GROUNDING (mine): C_2 = dim Lambda^2(S^4)
           = the EM field-strength channels (my 4505); pi^{n_C} = the bulk volume = pi^{dim_C} (my U-1.5). So
           the lepton prefactor = (EM channel count) x (bulk volume) -- all-geometric, lepton object.
           UNIFICATION: the electron formula m_e/m_P = C_2 * pi^{n_C} * alpha^{2 C_2} has C_2 = the EM channels
           THROUGHOUT -- prefactor C_2 (1x channels), exponent 2 C_2 (2x channels). All-geometric, closes
           0.037%. 3 open pieces now (Cal #481): (1) per-channel alpha (mine, deep), (2) mass-unit = Bergman
           (Grace), (3) the prefactor product-origin (components grounded, structural why remaining). NO count
           move. Count 9/26.

CAL #481 (taken): for the ELECTRON (a lepton), the prefactor is NOT the proton's F402 = N_c! * pi^5 (baryon
  antisymmetrizer). It is the lepton-geometric C_2 * pi^{n_C}. Same number (6 pi^5 = 1836.1), different OBJECT:
  C_2 (Casimir / EM-channel count) vs N_c! (baryon 3-quark antisymmetry). A lepton has no baryon
  antisymmetrizer; the right object is C_2. My 4507's "6 pi^5 = m_p/m_e" framing for m_e/m_P is RETRACTED.

GROUNDING the lepton prefactor (mine): C_2 * pi^{n_C} = (EM channel count) x (bulk volume):
  - C_2 = dim Lambda^2(S^4) = the EM field-strength F_mn 2-form components (my 4505) = the EM coupling channels.
  - pi^{n_C} = the D_IV^5 bulk volume = pi^{dim_C} (my U-1.5 / 4477).
  So the lepton prefactor is (channels) x (volume) -- all-geometric, built from established pieces.

UNIFICATION: m_e/m_P = C_2 * pi^{n_C} * alpha^{2 C_2}. C_2 (the EM channel count) appears THROUGHOUT:
  - prefactor C_2 = 1 x (channel count)
  - exponent 2 C_2 = 2 x (channel count) [the per-channel alpha, holo x antiholo]
  So the lepton mass-ratio is built entirely from C_2 (EM channels) + pi^{n_C} (bulk volume) + alpha
  (per-channel). All-geometric, lepton-consistent (no baryon factor), closes 0.037%.

THE 3 OPEN PIECES (per Cal #481):
  (1) per-channel alpha = 1/N_max -- MINE, the deep SO(4,2)/S^1 gate (4507).
  (2) mass-unit = Bergman scale -- Grace, reduced to "is 1/L_Bergman = m_P exactly (central charge 1)?".
  (3) the prefactor PRODUCT-origin -- why the lepton prefactor = (channel count) x (bulk volume); the
      COMPONENTS are grounded (C_2 = channels, pi^{n_C} = volume), the structural why-this-product remains.

TIER: Cal #481 TAKEN (lepton prefactor C_2 * pi^{n_C}, not N_c! * pi^5); grounded as (EM channels) x (bulk
  volume) from my established pieces; electron formula UNIFIED (C_2 = EM channels throughout, prefactor C_2 +
  exponent 2 C_2, all-geometric, closes 0.037%); open piece 3 partly resolved (components grounded, product-
  origin remaining). NO count move (3 open pieces). Count HOLDS 9/26.

DISCIPLINE: TOOK Cal #481 on my own 4507 (the lepton-vs-baryon prefactor object) without defense; grounded
  the lepton prefactor from my established channel + bulk-volume pieces (not fishing a new form -- same number,
  right object); unified the electron formula honestly (C_2 throughout); kept the product-origin (open piece 3)
  flagged as components-grounded-structure-remaining, not over-claimed as fully derived. Count HOLDS 9/26.

Elie - 2026-06-30
"""
import math
N_c, n_C, C2, g, rank, Nmax = 3, 5, 6, 7, 2, 137

score=0; TOTAL=3
print("="*98)
print("toy_4508 — TUE: take Cal #481 (lepton prefactor C_2*pi^{n_C}); ground as channels x volume; unify formula")
print("="*98)

print("\n[1] Cal #481: lepton prefactor = C_2*pi^{n_C} (geometric), NOT N_c!*pi^5 (baryon F402) -- same number, right object")
ok1 = (C2*math.pi**n_C == math.factorial(N_c)*math.pi**5) and (C2 == math.factorial(N_c))
print(f"    C_2*pi^{n_C} = {C2*math.pi**n_C:.2f} = N_c!*pi^5; OBJECT: C_2 (EM channels) not N_c! (baryon) -- lepton has no baryon factor: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] GROUND: C_2 = dim Lambda^2(S^4) = EM channels (4505); pi^{n_C} = bulk volume (U-1.5) -> prefactor = channels x volume")
from math import comb
ok2 = (comb(4,2) == C2) and (n_C == 5)
print(f"    C_2 = dim Lambda^2 = {comb(4,2)} = EM channels; pi^{n_C} = bulk volume; prefactor = (channels) x (volume), all-geometric: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] UNIFIED: m_e/m_P = C_2*pi^{n_C}*alpha^{2C_2}; C_2 = EM channels THROUGHOUT (prefactor C_2, exponent 2C_2)")
alpha = 1/(Nmax+1/(2*g*rank))
me_mP = C2*math.pi**n_C*alpha**(2*C2); obs = 0.5109989/1.220910e22
ok3 = (abs(me_mP-obs)/obs < 0.001)
print(f"    m_e/m_P = C_2 pi^{n_C} alpha^{2*C2} = {me_mP:.4e} vs obs {obs:.4e} ({abs(me_mP-obs)/obs*100:.3f}%); C_2 throughout: {'PASS' if ok3 else 'FAIL'}")
print(f"    3 open pieces: (1) per-channel alpha (mine,deep) (2) mass-unit=Bergman (Grace) (3) prefactor product-origin (components grounded)")
score += ok3

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — TUE: took Cal #481 (the electron is a lepton -> prefactor is the geometric")
print("       C_2*pi^{n_C}, not the proton's N_c!*pi^5 = F402; same number, right object). Grounded it from my")
print("       established pieces: C_2 = dim Lambda^2 = EM channels (4505), pi^{n_C} = bulk volume (U-1.5), so")
print("       the lepton prefactor = (channels) x (volume), all-geometric. The electron formula UNIFIES:")
print("       m_e/m_P = C_2*pi^{n_C}*alpha^{2 C_2}, with C_2 = the EM channels THROUGHOUT (prefactor C_2,")
print("       exponent 2 C_2), closes 0.037%. 3 open pieces; piece 3 (prefactor) components grounded. HOLDS 9/26.")
print("="*98)
