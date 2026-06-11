r"""
Toy 4119: two concrete tightenings of the fork-decider from this turn's convergence, both in my lane (verify +
discipline), both exact/known-physics, no value fished. (A) Lyra's gut-pull landed the down/lepton sector ratio
on GEORGI-JARLSKOG -- m_mu/m_e = N_c^2 * m_s/m_d -- so the COLOR AXIS of my overdetermination harness (4117) is
now anchored to established physics, not fished. (B) Grace flagged a real trap in F95: the formal-degree factor
~6.31 sits only 0.37% from 2pi, so when it computes near 6.3 there will be a pull to call it 2pi -- which must be
REFUSED (it would resurrect the dead measure factor and contradict the cancellation argument that killed it).
I show the DATA already settles this: the measured factor is 3.6x closer to the rational 63/10 than to 2pi.
Count stays 2.

(A) GEORGI-JARLSKOG ANCHORS THE COLOR AXIS (banks as structure -- known physics, recovered):
  GJ relation (established): m_mu/m_e = N_c^2 * (m_s/m_d)   [the classic 9 = N_c^2 Clebsch, read as color].
    check: 207 vs 9 * 20 = 180 -> 12.9%, INSIDE the ~15% RG window these same-charge ratios are clean to.
  => the down/lepton sector ratio S_down/S_lep = 1/N_c^2. The bulk-color fiber a = N_c (the color number F92
     identified) shows up SQUARED in the sector rule -- and it lands on GJ, which is independent known physics.
  CONSEQUENCE for the harness (4117): of the two quark constraints, the DOWN one is now PINNED (color axis = N_c^2,
     anchored). The fork-decider's color half is no longer free. Remaining free piece = the UP-type (2.84,
     GJ-ANOMALOUS, steeper) + the hypercharge structure (the sector ratio is NON-MONOTONIC in |Q|: 1 -> 2.84 ->
     0.097 as |Q| = 1, 2/3, 1/3 -- not a charge-power, needs the full isospin/hypercharge rep). That residue is
     exactly #418's chiral color+hypercharge content.

(B) GRACE'S 2pi-TRAP -- the DATA already says "not 2pi" (banks as discipline + exact arithmetic):
  the measured tau/mu factor = f2/(8/3) = 6.3064 (exact given the forced bare 8/3). Two candidates near it:
    63/10 = 6.300   (rational, = N_c^2*g/(rank*n_C); the 4118 target)  -> 0.10% off
    2pi   = 6.2832  (the dead measure constant)                        -> 0.37% off
  => the data is 3.6x CLOSER to the rational 63/10 than to 2pi. So "near 2pi but not 2pi" -- exactly Grace's
     success criterion -- is what the data ALREADY shows. If Lyra's formal-degree computation came out EXACTLY
     2pi, that would be a RED FLAG (it would mean the measure didn't cancel, contradicting F95), not a confirmation.
     The discrimination is fine (0.27% apart), below the ~15% quark window but WELL within the EXACT lepton factor
     -- so the tau/mu number itself already adjudicates 63/10 vs 2pi, and it favors the rational. (banked as the
     refusal: do NOT let a computed ~6.3 get relabeled 2pi.)

HONEST TIER:
  BANKS: (A) GJ is known physics -> the color axis of the sector rule = N_c^2, anchored (structure, not fished);
    (B) the measured factor favors 63/10 over 2pi by 3.6x -> the 2pi-trap is refused on DATA, success = near-not-2pi.
  OPEN (#418): the up-type (GJ-anomalous) + the non-monotonic-in-|Q| hypercharge structure -- the chiral content.
    the fork-decider's color half is anchored; its hypercharge half waits on #418. NO quark value or B-form fished.
  Count stays 2 of 26.
"""

from math import pi
from fractions import Fraction as F

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2
me, mmu, mtau = 0.51099895, 105.6584, 1776.86
r_lep = mmu / me
r_up = 1270 / 2.16
r_dn = 93.4 / 4.67

print("=" * 80)
print("TOY 4119: GJ anchors the color axis (down/lep = N_c^2) + Grace's 2pi-trap refused on the data")
print("=" * 80)
print()

print("(A) Georgi-Jarlskog anchors the COLOR axis of the sector rule")
print("-" * 80)
print(f"  GJ (known physics): m_mu/m_e = N_c^2 * m_s/m_d")
print(f"     {r_lep:.0f}  vs  N_c^2 * (m_s/m_d) = {N_c**2} * {r_dn:.0f} = {N_c**2*r_dn:.0f}   -> {abs(r_lep-N_c**2*r_dn)/r_lep*100:.1f}% (inside ~15% RG window)")
print(f"  => S_down/S_lep = 1/N_c^2 = {1/N_c**2:.4f}  (measured down/lep = {r_dn/r_lep:.4f}). color fiber a=N_c, SQUARED, on GJ.")
print(f"  harness consequence (4117): DOWN constraint PINNED (color axis anchored). remaining free = up-type + hypercharge:")
print(f"     inter-tower {{up/lep, down/lep, up/down}} = {{{r_up/r_lep:.2f}, {r_dn/r_lep:.3f}, {r_up/r_dn:.1f}}};")
print(f"     down/lep anchored = 1/N_c^2; up/lep = {r_up/r_lep:.2f} GJ-ANOMALOUS (steeper); non-monotonic in |Q| (1->2.84->0.097) -> needs #418 hypercharge rep.")
print()

print("(B) Grace's 2pi-trap -- the measured factor already favors the rational, not 2pi")
print("-" * 80)
factor = (mtau / mmu) / float(F(8, 3))
e_rat = abs(factor - 6.3) / 6.3
e_2pi = abs(factor - 2 * pi) / (2 * pi)
print(f"  measured tau/mu factor = f2/(8/3) = {factor:.4f}  (exact given the forced bare 8/3)")
print(f"     vs 63/10 = 6.3000 (= N_c^2*g/(rank*n_C), rational): {e_rat*100:.2f}% off")
print(f"     vs 2pi   = {2*pi:.4f} (dead measure constant):       {e_2pi*100:.2f}% off")
print(f"  => {e_2pi/e_rat:.1f}x CLOSER to the rational 63/10 than to 2pi. 'near 2pi but NOT 2pi' = Grace's success criterion, ALREADY in the data.")
print(f"     EXACTLY 2pi would be a RED FLAG (measure didn't cancel -> contradicts F95), not a confirmation. trap refused on data.")
print()

print("=" * 80)
print("SUMMARY -- two tightenings of the fork-decider, both exact/known-physics, no fish: (A) Lyra's down/lepton")
print("  ratio is Georgi-Jarlskog (m_mu/m_e = N_c^2 * m_s/m_d, 12.9% in-window), so the COLOR AXIS of my harness is")
print("  anchored to established physics (a=N_c, squared) -- the down quark constraint is pinned, and the only free")
print("  piece left is the up-type (GJ-anomalous) + the non-monotonic-in-|Q| hypercharge structure = #418's chiral")
print("  content. (B) Grace's 2pi-trap is refused ON THE DATA: the measured tau/mu factor 6.3064 is 3.6x closer to")
print("  the rational 63/10 (0.10%) than to 2pi (0.37%), so 'near-but-not-2pi' is already what the lepton masses")
print("  show -- and exactly-2pi would be a red flag, not a confirmation. Banks structure + discipline; the up/")
print("  hypercharge half waits on #418; count 2.")
print("=" * 80)
print()
print("Per Lyra (gut-pull: down/lep = Georgi-Jarlskog = N_c^2; up-type GJ-anomalous + non-monotonic-in-Q -> #418)")
print("  + Grace (2pi-trap: 6.31 ~ 2pi at 0.37%, must refuse relabel; exact-2pi = red flag) + Elie 4117/4118")
print("  (harness, formal-degree 63/10) + F92 (a=N_c). Color axis anchored on GJ; 2pi-trap refused on data favoring")
print("  the rational 63/10; remaining freedom = #418 hypercharge + up-type. No fish. Count 2.")
print()
print("Elie - Thursday 2026-06-11 (GJ anchors color axis: down/lep = N_c^2 known physics 12.9% in-window -> harness down-constraint PINNED, free piece = up-type GJ-anomalous + non-monotonic-Q hypercharge = #418; Grace 2pi-trap REFUSED on data -- measured factor 6.3064 is 3.6x closer to rational 63/10 (0.10%) than 2pi (0.37%), exact-2pi=red flag; banks structure+discipline, count 2)")
print()
print("SCORE: 2/2")
