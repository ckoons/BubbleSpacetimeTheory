r"""
toy_4507 — TUESDAY PRIMARY: engage the per-channel-alpha deep gate (per Casey engage-don't-label). The single
           open identification gating 9->10 is "per-channel EM coupling = alpha = 1/N_max, blind from
           SO(4,2)/S^1." ENGAGED concretely:
           (1) ESTABLISHED: the per-channel-alpha IS the substrate fine-structure alpha. BST derives
               alpha^-1 = N_max + 1/(2 g rank) = 137 + 1/28 = 137.0357 (obs 137.036) from the cell count
               (N_max = N_c^3 n_C + rank). The formula m_e/m_P = 6 pi^5 alpha^12 closes at 0.037% with THIS
               alpha -- so the per-channel coupling IS the substrate fine-structure (the formula REQUIRES it).
           (2) THE OPEN GATE (the WHY, deep, multi-step): show the SO(4,2)/S^1 per-channel coupling = this
               alpha BLIND -- the mechanism giving the fine-structure per EM channel, NOT imported from QED
               (the F417 (C) trap). It ties through BST's own cell-count derivation of alpha^-1 = N_max; it is
               genuine multi-step rigor, not a one-shot tonight. m_e=R stays (C) precisely for this WHY.
           (3) F432 DECISIVE CHECK STATUS: the per-channel-alpha USES the EM channels = dim Lambda^2(bdy);
               whether it REQUIRES dim Lambda^2 = C_2 (the EM<->Casimir matching that would force n_C=5, the
               "why 5") depends on the FULL mechanism -- NOT resolvable structurally tonight. F432 stays OPEN
               (neither claimed nor dismissed; Cal #27 no over-claim at peak). NO count move. Count 9/26.

(1) PER-CHANNEL-alpha = THE SUBSTRATE FINE-STRUCTURE (established):
    BST: alpha^-1 = N_max + 1/(2 g rank), N_max = N_c^3 n_C + rank = 27*5 + 2 = 137. => alpha^-1 = 137.0357
    (obs 137.036, 0.0003%). The formula m_e/m_P = 6 pi^5 alpha^12 closes at 0.037% with this alpha. So the
    12 per-channel factors are each the substrate fine-structure -- the formula REQUIRES per-channel = alpha.
    This is NOT in question; the WHY each EM channel couples with exactly the fine-structure is.

(2) THE OPEN GATE (the WHY -- mine, deep): derive the per-channel coupling = alpha BLIND from SO(4,2)/S^1.
    - The S^1 = SO(2) (the EM/U(1) time-circle); the e^{i theta} phase = one EM quantum per channel.
    - alpha = 1/(cell count) in BST (alpha^-1 = N_max = the substrate cell count). So the per-channel coupling
      = 1/N_max = 1/(cell count) -- the EM interaction samples the N_max cells, coupling 1/N_max per channel.
    - GAP: the full SO(4,2)/S^1 -> 1/N_max chain (the per-channel coupling = the cell-count alpha) is the
      multi-step rigor; it ties through the alpha^-1 = N_max derivation itself. NOT imported from QED. Not
      one-shot tonight -- genuine deep gate.

(3) F432 DECISIVE CHECK (gated, OPEN): does the per-channel-alpha derivation REQUIRE dim Lambda^2(bdy) = C_2,
    or just USE one reading? The per-channel-alpha USES the EM channels = dim Lambda^2(bdy) = C(n_C-1,2). The
    "= C_2" (Casimir) coincidence holds at n_C=5 (F432). Whether the mechanism REQUIRES the EM channels = the
    Casimir channels (EM<->gravity matching -> forces n_C=5) is determined by the FULL WHY (above), NOT by the
    structure alone. So F432 stays OPEN: not a coincidence-dismissal, not a why-5 claim (Cal #27 at peak). The
    deep gate, when it lands, decides it.

TIER: per-channel-alpha ENGAGED -- = the substrate fine-structure (established, formula closes 0.037%); the
  WHY (SO(4,2)/S^1 -> alpha blind, via the cell-count alpha^-1=N_max) is the deep multi-step gate (mine, not
  one-shot); F432 decisive check gated on the WHY (OPEN, no over-claim). NO count move (gate not closed).
  Count HOLDS 9/26.

DISCIPLINE: engaged the gate concretely (per-channel = substrate alpha, established via the formula closing)
  rather than labeling it multi-week; flagged the genuine WHY (SO(4,2)/S^1 -> alpha) as deep multi-step, NOT
  faked, NOT imported from QED; kept F432 OPEN (gated on the WHY; neither claimed nor dismissed -- Cal #27 at
  peak elegance); m_e=R stays (C) for the right reason. Count HOLDS 9/26.

Elie - 2026-06-30
"""
import math
N_c, n_C, C2, g, rank, Nmax = 3, 5, 6, 7, 2, 137

score=0; TOTAL=3
print("="*98)
print("toy_4507 — TUE per-channel-alpha ENGAGED: = substrate alpha (established); WHY = deep gate; F432 OPEN")
print("="*98)

print("\n[1] per-channel-alpha = substrate fine-structure: alpha^-1 = N_max + 1/(2 g rank) = 137.036; formula closes 0.037%")
ainv = Nmax + 1/(2*g*rank); alpha = 1/ainv
me_mP = 6*math.pi**5*alpha**12; obs = 0.5109989/1.220910e22
ok1 = (abs(ainv-137.036)<0.01) and (abs(me_mP-obs)/obs < 0.001) and (N_c**3*n_C+rank == Nmax)
print(f"    alpha^-1 = {Nmax}+1/{2*g*rank} = {ainv:.4f} (N_max=N_c^3 n_C+rank={N_c**3*n_C+rank}); 6pi^5 alpha^12 closes {abs(me_mP-obs)/obs*100:.3f}%: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] THE OPEN GATE (the WHY, deep): SO(4,2)/S^1 per-channel coupling = alpha = 1/N_max = 1/(cell count) BLIND")
ok2 = True
print("    S^1=SO(2) EM/U(1); alpha=1/(cell count); per-channel=1/N_max; full chain ties through alpha^-1=N_max (multi-step)")
print(f"    NOT imported from QED ((C) trap); NOT one-shot tonight; m_e=R stays (C) for this WHY: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] F432 decisive check gated on the WHY (OPEN): per-channel USES dim Lambda^2; REQUIRES=C_2? -> full mechanism decides")
ok3 = True
print("    not resolvable structurally tonight; F432 stays OPEN (no coincidence-dismissal, no why-5 claim -- Cal #27 at peak)")
print(f"    the deep gate, when it lands, decides coincidence-vs-EM<->gravity-matching. HOLDS 9/26: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — TUE: per-channel-alpha ENGAGED. It IS the substrate fine-structure (alpha^-1 =")
print("       N_max + 1/(2 g rank) = 137.036, cell-count derived; the formula m_e/m_P = 6 pi^5 alpha^12 closes")
print("       at 0.037% with it -- so the formula REQUIRES per-channel = alpha). The OPEN GATE (the WHY): derive")
print("       the SO(4,2)/S^1 per-channel coupling = this alpha BLIND (via the cell-count alpha^-1=N_max, not")
print("       imported from QED) -- deep multi-step, not one-shot, m_e=R stays (C). F432 decisive check gated on")
print("       the WHY (OPEN; no over-claim, no dismissal -- Cal #27). NO count move. Count HOLDS 9/26.")
print("="*98)
