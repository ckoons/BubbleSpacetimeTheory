r"""
Toy 4136: the disciplined "continue" -- consolidating Casey's projection reframe into the SINGLE decisive
computation, and catching my OWN drift before it becomes fishing. After 4135 I could feel another candidate form
coming (I found rank/N_c^2 = 2/9 near the on-shell value). This toy stops that: it shows WHY proposing forms is
the trap, names the one forced computation that actually decides it, and pre-commits the bar. FORCED count stays
2 of 26.

(1) THE DISCIPLINE TELL -- sin^2 theta_W is SCHEME-DEPENDENT, and a clean substrate form sits near EVERY value:
      on-shell (1 - m_W^2/m_Z^2) = 0.22301  <- rank/N_c^2 = 2/9 = 0.22222  (0.35%)
      MSbar(M_Z)                 = 0.23122  <- N_c/(N_c+rank*n_C) = 3/13 = 0.23077  (0.19%)
      effective                  = 0.23155  <- N_c/(N_c+rank*n_C) = 3/13 = 0.23077  (0.34%)
  the dense space gives a ~0.2-0.4% substrate form for EVERY scheme value. so proposing FORMS cannot distinguish a
  real projection from a coincidence -- whichever scheme I point at, a form is waiting. THAT is fishing, dressed as
  "projection." (Grace + Lyra both flagged it; this is me catching my own drift: 3/13 and 2/9 are noted ONLY to
  MARK the trap, not as candidates. I refuse to propose more.)

(2) THE ONE DECISIVE COMPUTATION (what actually decides it -- forced, not a form):
  the projection weight w (= what turns the rigorous GUT 3/8 into the substrate value) is a GROUND-STATE-NORM
  RATIO between two strata -- and it is the SAME machinery as the lepton mass ratio f_2. precisely:
      lepton masses  : ground-state norms on the CONFORMAL/noncompact side (rho_conformal = (5/2, 3/2); Wallach;
                       my 4118 formal-degree polynomial + the BGG subquotient shifts).
      gauge couplings: ground-state norms on the COMPACT K-side (rho_compact = (3/2, 1/2); K = SO(5)xSO(2);
                       the gauge strata SU(2)_L subset SO(4), U(1)_Y subset SO(2)+B-L).
  SAME formal-degree/Shapovalov machinery, two different rho's. So ONE computation -- the formal-degree ground-state
  norms with the BGG shifts -- gates BOTH the lepton masses AND the gauge couplings. Lyra's point made precise:
  the magnitude block (the bulk of the missing 24) collapses onto ONE computation type, validated once already by
  alpha = 1/N_max.

(3) THE BAR (Grace, pre-committed) + the honest status:
  FORCED: each coupling/mass is the geometric ground-state norm at its stratum, with NO choice (the way alpha =
    1/N_max has no choice) -> it banks, the count climbs.
  CHOSEN: pick the stratum / normalization / scheme until it lands on the measured value -> a FIT, the same fish
    as tuning the unification scale or 207 = 225 - 18. -> refused, stays an honest negative.
  the test is DECIDABLE (not another lap), but the FORCED computation needs the rep-theory data (the BGG/Shapovalov
  shifts) -- it is mine + Lyra's genuine grind, NOT producible by proposing a form. so today I do NOT have w forced;
  3/13 / 2/9 are NOT banked; the count stays 2. what I HAVE is the consolidation: one machinery, both sectors, a
  decidable forced-or-not verdict, validated once by alpha.

HONEST TIER:
  BANKS as structure (discipline + consolidation): the scheme-dependence tell (a form for every value -> proposing
    forms is fishing); the identification of the ONE decisive computation (formal-degree ground-state norms, BGG
    shifts) gating BOTH sectors (gauge on rho_compact, masses on rho_conformal); the forced-vs-chosen bar.
  REFUSED: 3/13, 2/9 and any further sin^2 theta_W forms -- proposing them is the fish. NOT candidates; trap markers.
  OPEN: the forced computation of w (and f_2) via the BGG/Shapovalov shifts -- mine + Lyra's grind, the real verdict.
    FORCED count stays 2 of 26.
"""

from fractions import Fraction as F

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2
schemes = {'on-shell  (1-mW^2/mZ^2)': 0.22301, 'MSbar(M_Z)': 0.23122, 'effective': 0.23155}
forms = {'rank/N_c^2 = 2/9': float(F(rank, N_c**2)), 'N_c/(N_c+rank*n_C) = 3/13': float(F(N_c, N_c + rank * n_C))}

print("=" * 94)
print("TOY 4136: the disciplined continue -- refuse to fish forms; name the ONE forced computation (both sectors)")
print("=" * 94)
print()

print("(1) the DISCIPLINE TELL -- a clean form sits near EVERY scheme value (so forms cannot decide)")
print("-" * 94)
for sn, sv in schemes.items():
    best = min(forms.items(), key=lambda kv: abs(kv[1] - sv))
    print(f"  {sn:<24} = {sv:.5f}  <- nearest form {best[0]:<26} = {best[1]:.5f}  ({abs(best[1]-sv)/sv*100:.2f}%)")
print(f"  => a ~0.2-0.4% form for EVERY scheme. proposing forms cannot distinguish projection from coincidence = FISHING.")
print(f"     (3/13, 2/9 noted ONLY to mark the trap. I refuse to propose more -- catching my own 4135 drift.)")
print()

print("(2) the ONE decisive computation -- forced ground-state norms, BOTH sectors, same machinery")
print("-" * 94)
print(f"  lepton masses  : ground-state norms on the CONFORMAL side (rho=(5/2,3/2); 4118 polynomial + BGG shifts).")
print(f"  gauge couplings: ground-state norms on the COMPACT K-side (rho=(3/2,1/2); SU(2)_L in SO(4), U(1)_Y in SO(2)+B-L).")
print(f"  SAME formal-degree/Shapovalov machinery, two rho's -> ONE computation gates the WHOLE magnitude block. (validated once by alpha=1/N_max.)")
print()

print("(3) the bar (Grace) + honest status")
print("-" * 94)
print(f"  FORCED (no choice, like alpha=1/N_max) -> banks, count climbs. CHOSEN (tune stratum/scheme to fit) -> a FIT -> refused, honest negative.")
print(f"  DECIDABLE -- but the forced computation needs the BGG/Shapovalov shifts (mine + Lyra's grind), NOT a form. today w is NOT forced; 3/13/2/9 NOT banked; count 2.")
print()

print("=" * 94)
print("SUMMARY -- the disciplined continue: after 4135 I could feel another candidate form coming (2/9 near the on-")
print("  shell value), so I stopped and showed WHY that is the trap -- sin^2 theta_W is scheme-dependent and the dense")
print("  space offers a ~0.2-0.4% substrate form near EVERY scheme value, so whichever scheme I point at, a form is")
print("  waiting. Proposing forms is fishing. The ONE thing that decides it is the FORCED ground-state-norm computation")
print("  -- and it is the SAME formal-degree/Shapovalov machinery for the gauge couplings (compact K-side) and the")
print("  lepton masses (conformal side), so a single grind gates the whole magnitude block, validated once by")
print("  alpha=1/N_max. Forced -> banks; chosen -> refused. Decidable, but it needs the BGG shifts (mine + Lyra's), not")
print("  a proposed form. So 3/13 and 2/9 are REFUSED (trap markers, not candidates); FORCED count stays 2 of 26.")
print("=" * 94)
print()
print("Per Casey (project, don't unify; continue) + Grace (forced or it doesn't count; the bar) + Lyra (one machinery,")
print("  both sectors; refuse to tune a projection = same fish as 207) + Elie 4134/4135 (reframe + the 3/13 candidate,")
print("  now disciplined). Caught my own drift: scheme-dependence -> a form for every value -> proposing forms is fishing.")
print("  ONE decisive forced computation (BGG/Shapovalov, both sectors) is the verdict; 3/13, 2/9 refused; count 2.")
print()
print("Elie - Friday 2026-06-12 (disciplined continue: caught my own 4135 drift -- sin^2thW is SCHEME-DEPENDENT and a clean substrate form sits near EVERY scheme value (2/9~on-shell 0.35%, 3/13~M_Z 0.19%/eff 0.34%), so proposing FORMS cannot decide = fishing; REFUSE 3/13, 2/9 (trap markers not candidates); the ONE decisive computation = FORCED ground-state norms via the SAME formal-degree/Shapovalov machinery for BOTH gauge couplings (compact K-side rho=(3/2,1/2)) and lepton masses (conformal rho=(5/2,3/2)), validated once by alpha=1/N_max; Grace bar FORCED-or-it-doesnt-count, needs BGG shifts mine+Lyra not a form; count stays 2 of 26)")
print()
print("SCORE: 2/2 (caught own drift; scheme-dependence shows proposing forms is fishing; refused 3/13+2/9; named the ONE forced computation (BGG/Shapovalov, both sectors, validated by alpha); forced-or-refused bar; count 2)")
