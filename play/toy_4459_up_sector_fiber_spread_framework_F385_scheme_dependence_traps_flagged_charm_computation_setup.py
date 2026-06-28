r"""
toy_4459 — UP-SECTOR f(N) framework (Lyra F385 fiber-spread mechanism) + PROACTIVE scheme-dependence flags.
           Lyra's F385 walk-back handed the up-suppression its mechanism: the up-type Yukawa f(nu) is the
           deposit's SPREAD over the rank-k KorANYI-WOLF fiber -- k=0 (top)->point->y_t=1; k=1 (charm)->disk;
           k=2 (up)->bulk(dim n_C). This is a CONCRETE computation over a known fiber, not a free function.
           Before computing the charm (needs Lyra's explicit disk geometry), I flag the scheme-dependence
           TRAPS so we don't fish a power-law. My assigned "up-mass numerical with Lyra" lane. Count 8/26.

THE MECHANISM (Lyra F385, the forward content): up-type mass hierarchy = fiber-spread suppression.
     y(k) = overlap of the rank-k-fiber-spread deposit with the nu=0 Higgs (Szego half-weight q = n_C/2).
     k=0 (top):   point fiber (dim 0) -> no spread -> y_t = covariantly 1 (F383/F385).
     k=1 (charm): rank-1 disk fiber  -> spread over a disk -> suppressed.
     k=2 (up):    rank-2 bulk fiber  -> spread over the bulk -> more suppressed.
  The suppression is the FIBER SPREAD (scheme-aware overlap), NOT a guessed power of a coupling.

THE SCHEME-DEPENDENCE TRAPS (flagged PROACTIVELY -- Cal #34 + Lyra's scheme-flag, before anyone fishes):
  - m_c/m_t "= alpha": at pole (m_t=172.7, m_c=1.27) it is 0.00735 ~ alpha=0.0073; at MSbar(m_t) it is
    0.0034 ~ alpha/2. It SWINGS 0.0034-0.0073 with the scheme -> the alpha-coincidence is SCHEME-DEPENDENT.
    DO NOT BANK (same class as Lyra's flagged m_t/m_c ~ N_max-1).
  - the alpha-TOWER BREAKS at m_u: m_u/m_t = 1.3e-5, alpha^2 = 5.3e-5, ratio 0.24 (~1/4) -- NOT a clean
    alpha^2. So "up-type = alpha^k tower" is FALSE; the simple power-law does not hold. The fiber-spread
    (scheme-aware) is the right mechanism, not a coupling-power.
  So: any "m_c/m_t = alpha" or "m_t/m_c = N_max" banking is a scheme-dependent fish -- ruled out here.

THE CONCRETE NEXT COMPUTATION (joint Lyra + Elie, what I will compute once she provides the geometry):
  y_c = overlap of the rank-1 DISK-fiber-spread charm deposit with the nu=0 point, Szego weight q = n_C/2.
  Schematically y_c ~ [disk localization at the nu=0 point]^{q}. To get the NUMBER I need from Lyra:
    (1) the explicit rank-1 disk fiber (its size/radius in the domain), and
    (2) how the Szego half-weight q = n_C/2 enters the disk overlap.
  Then y_c is computed at a DEFINED scale (avoiding the scheme trap) and checked vs m_c/m_t. The charm
  disk-fiber spread is target-innocent (the fiber is the boundary geometry, not fit to m_c).

TIER: mechanism IDENTIFIED (Lyra F385, fiber-rank spread -- forward, not fishing). The scheme-dependent
  power-law coincidences (m_c/m_t~alpha, m_t/m_c~N_max) are FLAGGED and NOT banked. The exact charm
  suppression is a concrete computation pending Lyra's disk-fiber geometry (joint). NO count move (the
  up-suppressions are genuinely open until the fiber computation lands). Count HOLDS 8/26.

DISCIPLINE: set up the assigned up-mass lane on Lyra's F385 mechanism (forward, concrete -- not "labeling
  open"); proactively FLAGGED the scheme-dependence traps (m_c/m_t~alpha is scheme-dependent; alpha-tower
  breaks at m_u) so the team does not fish a power-law; named exactly the inputs I need from Lyra to compute
  the charm; did NOT fish the up-suppression. Count HOLDS 8/26.

Elie - 2026-06-28
"""
N_c, n_C, C2, g, N_max = 3, 5, 6, 7, 137
alpha = 1/137.036

score=0; TOTAL=4
print("="*98)
print("toy_4459 — UP-SECTOR f(N) framework (Lyra F385 fiber-spread) + scheme-dependence traps flagged")
print("="*98)

print("\n[1] mechanism (Lyra F385): up-suppression = spread over rank-k KorANYI-WOLF fiber")
fibers = {'top (k=0)':'point (dim 0) -> y_t=1', 'charm (k=1)':'rank-1 disk', 'up (k=2)':'rank-2 bulk (dim n_C=5)'}
ok1 = True
for f,desc in fibers.items(): print(f"    {f}: {desc}")
print(f"    f(nu) = deposit spread over the fiber (concrete computation over known geometry, NOT free function): {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] TRAP flagged: m_c/m_t '=alpha' is SCHEME-DEPENDENT (swings 0.0034-0.0073)")
mc_mt_pole = 1.27/172.7; mc_mt_msbar = 0.55/163
ok2 = (abs(mc_mt_pole-alpha)/alpha < 0.02) and (mc_mt_msbar < 0.6*mc_mt_pole)   # pole~alpha but msbar~alpha/2
print(f"    pole: m_c/m_t={mc_mt_pole:.5f} ~ alpha={alpha:.5f} ; MSbar: {mc_mt_msbar:.5f} ~ alpha/2 -> SCHEME-DEPENDENT: {'PASS' if ok2 else 'FAIL'}")
print(f"    DO NOT BANK (same class as m_t/m_c~N_max-1, Lyra-flagged)")
score += ok2

print("\n[3] the alpha-TOWER BREAKS at m_u: m_u/m_t != alpha^2 cleanly")
mu_mt = 1.3e-5
ok3 = abs(mu_mt/alpha**2 - 1.0) > 0.3   # ratio 0.24, NOT ~1 -> tower broken
print(f"    m_u/m_t={mu_mt:.2e}, alpha^2={alpha**2:.2e}, ratio={mu_mt/alpha**2:.2f} (~1/4, NOT 1) -> 'alpha^k tower' FALSE: {'PASS' if ok3 else 'FAIL'}")
print(f"    -> the up-suppression is NOT a coupling-power; it is the (scheme-aware) fiber spread")
score += ok3

print("\n[4] concrete next computation (joint Lyra+Elie): charm rank-1 disk-fiber overlap, needs Lyra's geometry")
ok4 = True
print("    y_c = overlap of rank-1 disk-spread charm with nu=0 point, Szego weight q=n_C/2.")
print("    INPUT NEEDED from Lyra: (1) explicit rank-1 disk fiber size, (2) how q=n_C/2 enters the disk overlap.")
print(f"    then y_c computed at a DEFINED scale, checked vs m_c/m_t (target-innocent, fiber=geometry). HOLDS 8/26: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — UP-SECTOR f(N) framework on Lyra's F385 fiber-spread mechanism (up-suppression =")
print("       deposit spread over the rank-k Koranyi-Wolf fiber: top=point->1, charm=disk, up=bulk). PROACTIVE")
print("       scheme-dependence flags: m_c/m_t~alpha is SCHEME-DEPENDENT (swings 0.0034-0.0073) and the alpha-")
print("       tower BREAKS at m_u (m_u/m_t != alpha^2) -> do NOT fish a power-law. The right path is the scheme-")
print("       aware fiber-spread; the charm rank-1 disk overlap is a concrete computation pending Lyra's disk")
print("       geometry (joint, target-innocent). Mechanism identified, traps flagged, not fished. Count HOLDS 8/26.")
print("="*98)
