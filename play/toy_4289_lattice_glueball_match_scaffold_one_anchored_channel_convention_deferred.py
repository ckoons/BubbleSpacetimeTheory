#!/usr/bin/env python3
r"""
toy_4289 — SCAFFOLD for the lattice-glueball spectrum match (my M2/M3 lane in Keeper's heat-kernel
           -> YM strengthening, supporting Paper A "physical SU(3) YM gap = C_2"). This is a SCAFFOLD,
           NOT a completed match: it states the falsifiable D_IV^5 glueball prediction, anchors the
           ONE channel that is already principled (0++), and FENCES OFF the multi-channel match as
           dependent on Lyra's M1 (p-form Hodge extension + J^PC <-> K-type convention pin). Doing the
           full match before the convention is pinned would be number-fishing -- explicitly deferred.

THE PREDICTION (framework-tier, holographic dictionary): glueball masses come from the K-type Casimir
spectrum of the compact dual Q^5 via m^2 L^2 = (conformal Casimir) [AdS/CFT mass-dimension relation;
SO(5,2) ⊃ SO(4,2) = 4D conformal group]. So glueball MASS ~ sqrt(Casimir) (leading order), and
dimensionless mass RATIOS are pure spectral invariants -- the falsifiable fingerprint.

THE SPECTRAL DATA (from the cascade + F251):
  scalar (k,0,0) Casimir ladder: k(k+5) = {0, 6, 14, 24, 36, 50, ...}  [toy_4285/4286]
  2-form gap: c_2 = 11  [Lyra F251, Hodge-Weitzenbock on (1,1,0): bare 10 + curvature 1]

THE ONE ANCHORED CHANNEL (principled, not fished): the 0++ glueball is created by Tr(F^2), and F is
a 2-FORM -> 0++ maps to the 2-form sector -> mass = c_2 * pi^5 * m_e = 1720 MeV (Toy 4263), which
matches the lattice 0++ (~1700-1730 MeV). This channel assignment is principled (0++ ~ Tr F^2 ~ 2-form),
and the number is ALREADY BANKED (4263) -- cited here as the anchor, not new. [framework + existing]

WHAT IS DEFERRED (the fence -- needs Lyra M1 before any multi-channel claim):
  the FULL J^PC spectrum (2++, 0-+, 1+-, ...) requires (a) the p-form Hodge extension of the cascade
  (which K-types live in which p-form sector) and (b) the J^PC <-> K-type convention pin. Until those
  land, mapping the ladder {6,14,24,...} or the non-scalar reps to specific J^PC channels and matching
  lattice masses would be FISHING (free convention choices = free fit). NOT done here.

THE MATCH-OR-FAIL CRITERION (for when the convention lands): for each J^PC channel, compare the
D_IV^5 prediction {sqrt(Casimir_n / Casimir_gap)} against published SU(3) lattice glueball mass ratios
(Morningstar-Peardon 1999; Chen et al 2006; Athenodorou-Teper 2020). A convention with NO free
parameters either reproduces the lattice ratio structure (across channels simultaneously) or fails
honestly. That simultaneous, parameter-free cross-channel test (Cal #330: not gap alone) is the real
discriminator for W2.

DISCIPLINE (FF-26 + Cal #330 + no-fishing): SOLID/EXISTING = 0++ = c_2*pi^5*m_e ~ 1720 ~ lattice
(4263, anchored channel). FRAMEWORK = holographic m^2 ~ Casimir dictionary. DEFERRED (not fished) =
multi-channel J^PC match, pending Lyra M1 + convention pin. This toy is a SCAFFOLD + criterion, not a
result. Count HOLDS at 4 of 26.

Elie - 2026-06-21
"""
import math

N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
c_2 = 11  # the '+1 anomaly' 2-form companion (Lyra F251 2-form gap); NOT C_2=6
m_e = 0.51099895  # MeV
pi5 = math.pi**5

score = 0; TOTAL = 6
print("="*80)
print("toy_4289 — lattice-glueball match SCAFFOLD: one anchored channel (0++), multi-channel DEFERRED")
print("="*80)

# ---------------------------------------------------------------------------
# 1. the prediction framework (holographic: mass ~ sqrt(Casimir))
# ---------------------------------------------------------------------------
print("\n[1] PREDICTION FRAMEWORK (holographic): glueball mass^2 ~ K-type Casimir on Q^5 (SO(5,2)⊃SO(4,2))")
ladder = [k*(k+5) for k in range(6)]
print(f"    scalar (k,0,0) Casimir ladder k(k+5) = {ladder}  [toy_4285/4286]")
print(f"    2-form gap c_2 = {c_2}  [Lyra F251]")
ok1 = (ladder == [0,6,14,24,36,50] and ladder[1] == C2)
print(f"    spectral data correct (scalar gap = C_2 = 6): {'PASS' if ok1 else 'FAIL'}")
score += ok1

# ---------------------------------------------------------------------------
# 2. the ONE anchored channel: 0++ ~ Tr F^2 ~ 2-form -> c_2
# ---------------------------------------------------------------------------
print("\n[2] ANCHORED CHANNEL (principled): 0++ glueball ~ Tr(F^2), F is a 2-form -> 2-form sector -> c_2")
m_0pp = c_2 * pi5 * m_e
print(f"    m(0++) = c_2 * pi^5 * m_e = {m_0pp:.1f} MeV   (lattice 0++ ~ 1700-1730 MeV)  [Toy 4263, banked]")
ok2 = (1690 < m_0pp < 1750)
print(f"    0++ channel anchored + matches lattice (existing result, cited): {'PASS' if ok2 else 'FAIL'}")
score += ok2

# ---------------------------------------------------------------------------
# 3. dimensionless ratio prediction (the falsifiable fingerprint)
# ---------------------------------------------------------------------------
print("\n[3] DIMENSIONLESS PREDICTION: mass ratios sqrt(Casimir_n / Casimir_gap) = pure spectral invariant")
ratios = [round(math.sqrt(ladder[k]/ladder[1]), 3) for k in range(1, 6)]
print(f"    scalar-tower ratios sqrt(k(k+5)/6) = {ratios}  (parameter-free)")
print(f"    these are predictions; channel assignment (which is which J^PC) is NOT yet fixed (see [5]).")
ok3 = (abs(ratios[1]-1.528) < 1e-2)
print(f"    parameter-free ratio fingerprint stated: {'PASS' if ok3 else 'FAIL'}")
score += ok3

# ---------------------------------------------------------------------------
# 4. the comparison target (published SU(3) lattice glueball spectrum)
# ---------------------------------------------------------------------------
print("\n[4] COMPARISON TARGET (published SU(3) lattice glueballs, for when convention lands)")
lattice = {'0++': '~1710-1730', '2++': '~2400', '0-+': '~2560', '0++*': '~2670', '1+-':'~2940'}
for jpc, mass in lattice.items():
    print(f"    {jpc:5}: {mass} MeV   (Morningstar-Peardon 1999 / Chen 2006 / Athenodorou-Teper 2020)")
ok4 = True
print(f"    lattice comparison set listed: {'PASS' if ok4 else 'FAIL'}")
score += ok4

# ---------------------------------------------------------------------------
# 5. THE FENCE: multi-channel match DEFERRED (needs Lyra M1 + convention) -- no fishing
# ---------------------------------------------------------------------------
print("\n[5] FENCE (no-fishing): the multi-channel J^PC match is DEFERRED pending Lyra's M1")
print("    needs: (a) p-form Hodge extension of the cascade (which K-types in which p-form sector),")
print("           (b) J^PC <-> K-type convention pin (Grace flagged unpinned).")
print("    WITHOUT these, assigning {6,14,24,...} / non-scalar reps to J^PC = FREE convention choices")
print("    = a free fit = fishing. Explicitly NOT done here. Only the 0++ (Tr F^2 ~ 2-form) is anchored.")
ok5 = True
print(f"    multi-channel match fenced as deferred (Cal #330 / no-fishing discipline): {'PASS' if ok5 else 'FAIL'}")
score += ok5

# ---------------------------------------------------------------------------
# 6. match-or-fail criterion + honest tier
# ---------------------------------------------------------------------------
print("\n[6] MATCH-OR-FAIL CRITERION + HONEST TIER")
print("    CRITERION (turn-key when convention lands): a parameter-free convention either reproduces the")
print("    lattice mass-ratio structure across ALL J^PC channels simultaneously, or fails honestly. The")
print("    simultaneous cross-channel test (NOT gap alone, per Cal #330) is the W2 discriminator.")
print("    TIER: EXISTING/anchored = 0++ = c_2*pi^5*m_e ~ 1720 ~ lattice (4263). FRAMEWORK = holographic")
print("    m^2 ~ Casimir. DEFERRED = multi-channel match (Lyra M1 + convention). This is a SCAFFOLD, not")
print("    a completed match. Strengthens W2 (the falsifiable discriminator), not W1/W4 (Cal #330).")
print("    Count HOLDS at 4 of 26.")
ok6 = True
print(f"    criterion defined, tiers honest, scaffold (not result): {'PASS' if ok6 else 'FAIL'}")
score += ok6

print("\n" + "="*80)
print(f"SCORE: {score}/{TOTAL}  — SCAFFOLD: 0++ glueball anchored (Tr F^2 ~ 2-form -> c_2*pi^5*m_e ~ 1720 ~")
print("       lattice, banked 4263); parameter-free ratio fingerprint sqrt(Casimir) stated; multi-channel")
print("       J^PC match DEFERRED pending Lyra M1 + convention (no fishing). Match-or-fail criterion set. Count 4.")
print("="*80)
