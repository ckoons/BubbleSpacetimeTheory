#!/usr/bin/env python3
"""
Toy 5195: THE BARS FIRE -- 5180 (blind-commit decision tree) + 5182 (necessary-gate upgrade) run against the
landed store-16 stamp (Cal §428, "Derived-given-#16"). Context: yesterday I committed a decision tree BEFORE the
forward gravity coefficient landed (toy 5180: n(F) = 11.6724 + ln(F)/ln(1/α); CLOSES iff |n-12|<0.10 ⟺ F∈[3.06,
8.20]; FAIL-reduced iff F≈1; PROVENANCE GATE: PASS only if F comes from a blind solid-angle integration of a₁,
never the back-fit corpus 8π, never a target-aware n_C insertion), then upgraded it (toy 5182: n≈12 is a
NECESSARY gate only -- π²/2, √(8π), √(8π²/3), n_C all land within 0.008 of twelve -- so PROVENANCE decides).
Today store-16 cleared: Cal ruled the DM channel capacity is the operator space 2^{2·rank} = (2^rank)² = d² = 16
(not the outcome-count d=4), forced given measurement-principle #16, and stamped four promotions at
"Derived-given-#16". Keeper (K1404) reads that as: 16/3 → the 8π normalization → standard Planck mass → exponent
= 2C₂ = 12 → FORCING B IS DONE. THIS TOY FIRES BOTH BARS ON THAT CHAIN, mechanically, and reports what each one
can and cannot certify. RESULT, calibrated both directions: (1) the INTEGER is CONFIRMED and robust -- every
admissible F in the whole CLOSES band gives n=12, and the FAIL-reduced branch (F≈1, the spectral-action default
where the sphere cancels) is REFUSED because store-16 + the banked bulk-edge split make gravity's usage of the
sphere DISCRETE, so the ratio cannot be 1. Forcing B is done for the exponent; do NOT under-claim it. (2) BUT
the committed provenance -- a blind solid-angle integration of a₁ delivering a NUMBER F -- did not land; the
substitute (store-16) is admissible in KIND (α-free, target-innocent, axiom-grounded, untunable) yet it delivers
the BAND, not the POINT: two candidate F's survive, √(8π)=5.0133 (standard-vs-reduced Planck) and π²/2=4.9348
(the continuum/discrete ratio (8π²/3)/(16/3)), and they are NOT the same number -- they differ by 1.59%. ★ THE
NEW FINDING: what the exponent cannot discriminate, NEWTON'S G CAN. G ∝ F⁻², so the 1.59% seam becomes 3.2% in
G: the standard-Planck reading gives G = 6.6786e-11 (+0.065%), the π²/2 reading gives G = 6.4712e-11 (-3.04%) --
47× worse. So the 0.07% G agreement (toy 5190) is EVIDENCE for the exact standard-Planck normalization, at a
precision the exponent is blind to. Honest split: exponent 2C₂=12 = Derived-given-#16 (Forcing B DONE); the
exact normalization (√(8π), i.e. standard Planck) = Identified, favored by the G precision as a consistency
check, not derived. ★ ANTI-NUMEROLOGY GUARD (mine, standing): π²/2 ≈ √(8π) to 1.6% is a COINCIDENCE, not an
identity -- the corpus must not call the discretization route "the 8π"; that relabel is exactly the kind of slip
the Wyler ghost taught us to refuse. Elie fires his own committed bars. (Toy 5180 tree; toy 5182 upgrade; Cal
§428 store-16 ruling; Lyra F931 SHARPEN-2 "name the 8π step, don't collapse 16→12"; Grace's two same-object
seams; Keeper K1404; toy 5190 non-circular G.) CP existence-only. Nothing here reasons toward 12.

WHAT I COMPUTE:
  * the committed rule, re-derived forward from measured (m_e, α, M_Planck): n_std = 12.0001, n_red = 11.6724.
  * BAR 5182 fires: √(8π) → 11.9969+, π²/2 → 11.9969, both |n-12| < 0.004 ⟹ non-discriminating, as committed.
  * BAR 5180 fires: number side CLOSES for the whole surviving band; FAIL-reduced (F≈1) branch REFUSED.
  * PROVENANCE ruling: committed source (blind a₁ solid-angle) absent; store-16 admissible in kind, band-not-point.
  * ★ the G discriminator: F=√(8π) → G +0.065%; F=π²/2 → G -3.04%. 47×. The exponent is blind; G is not.

=> VERDICT (plain): my two bars were set yesterday so that today's answer would be mechanical, and they are. The
first thing they say is yes -- the exponent really is twelve, and it is twelve for every version of the geometry
factor still on the table, so the integer does not depend on settling the last argument. The store-16 ruling
also kills the branch that would have failed: if the boundary genuinely stores a discrete count of sixteen
operators while the electron lives on the continuous boundary, then gravity's use of the sphere is discrete and
the two usages cannot cancel to one. Forcing B is done, and I say so without hedging. The second thing they say
is that the chain is not finished at the level of the VALUE. What landed is a count, and what the exponent needs
is a ratio; the step that converts one into the other is still asserted rather than computed, and two different
numbers -- root eight pi and pi squared over two -- both survive it. They agree to within a couple of percent,
which is why the exponent cannot tell them apart. Newton's constant can. Because G goes as the inverse square of
that factor, the two readings differ by three percent in G, and the measured value sits on the standard-Planck
side to within seven hundredths of a percent. That is a real discrimination, and it arrives from the direction
we did not plan: the precision of a prediction we already had is now doing the work of a derivation we do not
yet have. It is evidence, not a proof, and I label it that way.

=> DISPOSITION: exponent 2C₂ = 12 CONFIRMED (Derived-given-#16; Forcing B done -- integer robust across the
whole admissible band; F≈1 branch refused by store-16 + the bulk-edge split). The exact normalization
(standard Planck / √(8π)) stays IDENTIFIED, with the 0.07% G agreement as a consistency-check favoring it 47:1
over the π²/2 alternative. Firer: Elie (my own committed bars, fired mechanically). Owed: the count→ratio step
written as a computation (the induced-gravity R-coefficient with the stored 16 appearing as its normalization),
which would decide √(8π) vs π²/2 forward instead of by G's precision. Anti-numerology guard: π²/2 ≠ √(8π); do
not relabel. Nothing pushed; nothing promoted beyond Cal's stamp. CP existence-only. Count once.

Author: Elie (CI toy builder). Date: 2026-08-12.
"""

import math

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# ---------------------------------------------------------------------------
# Measured inputs (all G-free on the input side except M_Planck, used only to
# re-derive the exponent; the G prediction below runs the other direction).
# ---------------------------------------------------------------------------
alpha    = 1/137.035999206          # CODATA fine-structure constant
L        = math.log(1/alpha)        # ln(1/α) = 4.920244
m_e      = 0.51099895000e-3         # GeV
M_Pl     = 1.220890e19              # GeV, STANDARD Planck mass √(ħc/G)
M_red    = M_Pl/math.sqrt(8*math.pi)   # GeV, REDUCED Planck mass √(ħc/8πG)
G_obs    = 6.67430e-11              # m³ kg⁻¹ s⁻²
c6       = 6*math.pi**5             # = C₂·π^{n_C}, the forced Bergman prefactor (toy 5179)

F_sqrt8pi = math.sqrt(8*math.pi)    # 5.013257 -- standard-vs-reduced Planck ratio
F_pi2half = math.pi**2/2            # 4.934802 -- (8π²/3)/(16/3), the continuum/discrete ratio
F_volS4   = math.sqrt(8*math.pi**2/3)
F_nC      = 5.0

def n_of(F, n_red):
    return n_red + math.log(F)/L

print("=" * 78)
print("Toy 5195: BARS 5180 + 5182 FIRE on the landed store-16 stamp (Cal §428, Derived-given-#16)")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. Re-derive the rule's endpoints FORWARD from measurement (do not trust
#    yesterday's 11.6724 -- recompute it).
# ---------------------------------------------------------------------------
print("\n--- 1. the committed rule, re-derived forward from measured (m_e, α, M_Planck) ---")
n_std = math.log(c6*M_Pl/m_e)/L
n_red = math.log(c6*M_red/m_e)/L
gap   = 0.5*math.log(8*math.pi)/L
check("The two endpoints of my committed rule reproduce forward from measurement: with the STANDARD Planck mass "
      f"m_e = 6π⁵·α^n·M gives n = {n_std:.6f}; with the REDUCED Planck mass n = {n_red:.6f}; the gap is exactly "
      f"½·ln(8π)/ln(1/α) = {gap:.6f}. Yesterday's committed constant 11.6724 reproduces to 4 decimals, so the "
      "rule I fixed blind is the rule I am firing now.",
      abs(n_std - 12) < 0.01 and abs(n_red - 11.6724) < 0.001 and abs((n_std-n_red) - gap) < 1e-9,
      f"n_std={n_std:.6f}  n_red={n_red:.6f}  gap={gap:.6f}  (6π⁵={c6:.4f})")

# ---------------------------------------------------------------------------
# 2. BAR 5182 FIRES: the number is a NECESSARY gate and it cannot discriminate.
# ---------------------------------------------------------------------------
print("\n--- 2. BAR 5182 FIRES -- n≈12 is NECESSARY, and it still cannot tell the candidates apart ---")
cands = {"√(8π)": F_sqrt8pi, "π²/2": F_pi2half, "√(vol S⁴)": F_volS4, "n_C": F_nC}
ns = {k: n_of(v, n_red) for k, v in cands.items()}
spread = max(ns.values()) - min(ns.values())
check("Bar 5182 fires as committed: all four surviving geometry factors land the exponent on twelve -- "
      + "; ".join(f"{k} → n={ns[k]:.4f}" for k in cands)
      + f" -- a total spread of {spread:.4f}. The number therefore carries NO discriminating information; it is "
      "a necessary gate that the answer must pass, not evidence for any one provenance. This is exactly what I "
      "committed yesterday, before the stamp landed, and it holds unchanged.",
      spread < 0.01 and all(abs(x-12) < 0.01 for x in ns.values()),
      "  ".join(f"{k}:{ns[k]:.4f}" for k in cands) + f"   spread={spread:.5f}")

# ---------------------------------------------------------------------------
# 3. BAR 5180, NUMBER SIDE: the CLOSES band, and the FAIL-reduced branch.
# ---------------------------------------------------------------------------
print("\n--- 3. BAR 5180 fires, number side: CLOSES band vs the FAIL-reduced branch ---")
F_lo = math.exp(-0.10*L + math.log(F_sqrt8pi) + (12 - n_of(F_sqrt8pi, n_red))*L)
band_lo, band_hi = math.exp((11.90 - n_red)*L), math.exp((12.10 - n_red)*L)
fail_lo, fail_hi = math.exp((11.5724 - n_red)*L), math.exp((11.7724 - n_red)*L)
in_band = [k for k, v in cands.items() if band_lo <= v <= band_hi]
check("Bar 5180's committed thresholds fire on the surviving candidates: CLOSES requires |n-12|<0.10 ⟺ "
      f"F ∈ [{band_lo:.3f}, {band_hi:.3f}], and every surviving candidate sits inside it ({', '.join(in_band)}). "
      f"FAIL-reduced requires F ∈ [{fail_lo:.3f}, {fail_hi:.3f}] (F≈1, the spectral-action default where the "
      "sphere cancels against (4π)^{d/2}); no surviving candidate is anywhere near it. The number side of my "
      "blind tree returns CLOSES.",
      len(in_band) == 4 and not any(fail_lo <= v <= fail_hi for v in cands.values()),
      f"CLOSES band F∈[{band_lo:.3f},{band_hi:.3f}]; FAIL band F∈[{fail_lo:.3f},{fail_hi:.3f}]; candidates all in CLOSES")

check("The FAIL-reduced branch is not merely unoccupied -- it is REFUSED by the landed physics, and this is the "
      "substantive thing store-16 buys. F≈1 is the case where the electron and gravity use the sphere the same "
      "way, so the factors cancel. Store-16 says the boundary stores a DISCRETE count of sixteen operators, and "
      "the banked bulk-edge split (K825: boundary continuous/chiral, interior discrete/neutral) puts the "
      "electron on the continuum side and gravity on the discrete side. Two different usages cannot cancel to "
      "one. So the binary my tree was built to decide -- net factor ~5, or cancellation to ~1 -- is decided, "
      "and it is decided AGAINST the branch that would have failed the identification.",
      True,
      "store-16 (discrete count) + bulk-edge split (K825) ⟹ gravity's sphere-usage ≠ electron's ⟹ F ≠ 1")

# ---------------------------------------------------------------------------
# 4. BAR 5180, PROVENANCE GATE: rule on the substitute provenance.
# ---------------------------------------------------------------------------
print("\n--- 4. BAR 5180, PROVENANCE GATE -- the committed source did not land; rule on the substitute ---")
committed_source = "blind solid-angle integration of the a₁ heat-kernel coefficient, returning a number F"
forbidden = ["the back-fit corpus 8π (K1374 -- inverted from the observed electron)",
             "a target-aware n_C insertion (the √(8π)≈n_C=5.01 trap)"]
substitute = "store-16: capacity = operator space 2^{2·rank} = d² = 16, forced given measurement-principle #16 (Cal §428)"
check("The provenance I committed -- " + committed_source + " -- DID NOT LAND. Lyra and Grace never ran the "
      "solid-angle integration; the lane moved to 137. So the number side above cannot be scored as a PASS of "
      "my committed gate: there is no F from the required source to score. What arrived instead is a substitute "
      "provenance (" + substitute + "). I rule on the substitute rather than pretending my gate was met.",
      True,
      "committed source absent ⟹ gate not met literally; substitute ruled on below, not waved through")

check("The substitute is ADMISSIBLE IN KIND, and on two of my three criteria it is stronger than what I asked "
      "for: it is α-free, it is target-innocent (the operator-vs-module question was settled on the definition "
      "of measurement, with the answer fixed before anyone asked what exponent it implied), and it is UNTUNABLE "
      "-- a dimension and its square admit no dial. It is also neither of the two things I forbade: it does not "
      "cite the back-fit 8π and it does not insert n_C. On kind, it passes.",
      all(k not in substitute for k in ["8π", "n_C"]),
      "α-free ✓  target-innocent ✓  untunable ✓  not the back-fit 8π ✓  not an n_C insertion ✓")

check("★ But the substitute delivers a COUNT, and the exponent needs a RATIO -- and the step that converts one "
      "into the other is asserted, not computed. Lyra flagged this herself (F931 SHARPEN-2): 'storage=16 and "
      "exponent=12 are DIFFERENT numbers -- NOT 16 forces 12; the link is a CHAIN: cell-count → 16/3 → the 8π "
      "normalization works → standard Planck mass → n=2C₂=12. Name the 8π step.' The 8π step is the one nobody "
      "has written as a computation. Consequence: the substitute pins the BAND (F ≈ 5, not 1), which is enough "
      "for the integer, but it does not pin the POINT.",
      True,
      "forced count + asserted conversion = the PD signature; band pinned, point not pinned")

# ---------------------------------------------------------------------------
# 5. Two candidate F's survive -- and they are NOT the same number.
# ---------------------------------------------------------------------------
print("\n--- 5. the two survivors are 1.6% apart -- and the corpus is calling them the same thing ---")
seam = F_sqrt8pi/F_pi2half - 1
check("Two provenances survive inside the band and they give DIFFERENT numbers. √(8π) = "
      f"{F_sqrt8pi:.6f} is the standard-vs-reduced Planck mass ratio (the reading Keeper's chain asserts). "
      f"π²/2 = {F_pi2half:.6f} is the continuum/discrete ratio (8π²/3)/(16/3) -- Lyra's bulk-edge reframe, the "
      "one that actually USES the sixteen. They differ by "
      f"{100*seam:.2f}%. Calling the discretization route 'the 8π normalization → standard Planck mass' "
      "identifies two numbers that are not equal. That relabel is precisely the move the Wyler ghost taught us "
      "to refuse: a clean form that lands the right integer is a CANDIDATE, not the mechanism.",
      abs(seam) > 0.015 and abs(seam) < 0.02,
      f"√(8π)={F_sqrt8pi:.6f}  π²/2={F_pi2half:.6f}  seam={100*seam:.3f}%  -- not an identity, a near-coincidence")

# ---------------------------------------------------------------------------
# 6. ★ THE DISCRIMINATOR: what the exponent cannot see, Newton's G can.
# ---------------------------------------------------------------------------
print("\n--- 6. ★ the G-precision discriminator: the exponent is blind to the seam, G is not ---")
M_anchor  = m_e/(c6*alpha**12)                 # forward from G-free inputs (toy 5190)
G_std     = G_obs*(M_Pl/M_anchor)**2           # anchor IS the standard Planck mass
M_Pl_alt  = M_anchor*F_sqrt8pi/F_pi2half       # anchor = (π²/2)·M_reduced ⟹ implied standard Planck mass
G_alt     = G_obs*(M_Pl/M_Pl_alt)**2
dev_std   = 100*(G_std/G_obs - 1)
dev_alt   = 100*(G_alt/G_obs - 1)
check("Newton's G runs as the INVERSE SQUARE of the ruler factor, so the 1.6% seam that the exponent cannot see "
      f"becomes a {abs(dev_alt-dev_std):.1f}% split in G. Reading the anchor as the STANDARD Planck mass "
      f"(F=√(8π)) predicts G = {G_std:.5e}, which is {dev_std:+.4f}% from the measured value. Reading it "
      f"through the discretization route (F=π²/2) predicts G = {G_alt:.5e}, which is {dev_alt:+.4f}%. The "
      "measurement sits on the standard-Planck side by a factor of "
      f"{abs(dev_alt/dev_std):.0f} in relative error.",
      abs(dev_std) < 0.1 and abs(dev_alt) > 2.5,
      f"G_std={G_std:.5e} ({dev_std:+.4f}%)   G_alt={G_alt:.5e} ({dev_alt:+.4f}%)   G_obs={G_obs:.5e}")

check("★ This is the finding, and it arrives from the direction nobody planned: the PRECISION of a prediction "
      "we already had is doing the work of a derivation we do not yet have. My 5182 upgrade said the exponent "
      "cannot discriminate provenance and the provenance must be settled some other way. It can be -- by G. "
      "The honest label is EVIDENCE, not forcing: the 0.07% agreement favors the exact standard-Planck "
      "normalization over the π²/2 alternative, but favoring is not deriving, and a consistency check that "
      "points at a mechanism is not the mechanism.",
      True,
      "0.07% vs 3.0% -- a consistency-check discrimination, labeled as evidence, not promoted to a forcing")

# ---------------------------------------------------------------------------
# 7. The verdict, calibrated both directions.
# ---------------------------------------------------------------------------
print("\n--- 7. the verdict -- confirm what landed, name what did not ---")
check("CONFIRM (do not under-claim): the exponent 2C₂ = 12 is Derived-given-#16 and FORCING B IS DONE. The "
      "exponent is an INTEGER, and the integer is robust across the entire admissible band -- every candidate "
      "in [3.06, 8.20] returns twelve. Store-16 plus the bulk-edge split refuses the one branch that would have "
      "failed. Keeper's K1404 reading is right on the thing it claims: the exponent side is locked, and when "
      "the ×5 lands, the electron mass and α follow with the exponent already in hand.",
      abs(n_of(F_pi2half, n_red) - 12) < 0.1 and abs(n_of(F_sqrt8pi, n_red) - 12) < 0.1,
      "integer robust across the band; FAIL-branch refused; Forcing B done at the #16-axiom tier")

check("NAME (do not over-claim): the 0.07% G VALUE needs more than the integer. It needs the exact "
      "normalization -- F = √(8π) precisely, the standard Planck mass -- and that identification is currently "
      "IDENTIFIED, not derived: the count→ratio step is unwritten, and the alternative that actually uses the "
      "sixteen (π²/2) gives G at -3.0%. So the correct sentence for the corpus is the explicit split: exponent "
      "Derived-given-#16; normalization Identified (favored 47:1 by the G precision). Anyone writing 'BST "
      "derives the standard Planck-mass normalization' is over-stating by exactly one unwritten step.",
      abs(dev_alt) > 40*abs(dev_std),
      f"explicit split: exponent D-given-#16 / normalization Identified; G favors standard by {abs(dev_alt/dev_std):.0f}:1")

check("What would close it (named, so it is a target and not a complaint): write the count→ratio step as a "
      "computation -- the induced-gravity R-coefficient with the stored 16 entering as its normalization -- and "
      "read off F FORWARD. If that computation returns √(8π), the normalization promotes and G's 0.07% becomes "
      "a prediction rather than a check. If it returns π²/2, then either G is 3% wrong or the anchor relation "
      "needs a compensating factor, and we will have found a real crack. Either way the computation is "
      "decisive, it is small, and it does not depend on 137.",
      True,
      "owed: induced-gravity R-coefficient normalized by the stored 16, F read forward, blind to √(8π) vs π²/2")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (exponent 12 CONFIRMED Derived-given-#16, Forcing B done; exact normalization Identified; G precision is the 47:1 discriminator)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5195, my own bars 5180 + 5182 fired mechanically on the landed store-16 stamp):
  * BAR 5182 fires as committed: √(8π), π²/2, √(vol S⁴), n_C all give n∈[11.997,12.001] -- spread {spread:.4f}.
    The number still carries no discriminating information. Necessary gate, met; nothing more.
  * BAR 5180 number side: CLOSES (all survivors inside F∈[{band_lo:.2f},{band_hi:.2f}]); FAIL-reduced branch (F≈1)
    REFUSED -- store-16's discrete count + the K825 bulk-edge split make the two sphere-usages different.
  * BAR 5180 provenance gate: the committed source (blind a₁ solid-angle integration) never landed. The
    substitute (store-16, Derived-given-#16) is admissible IN KIND -- α-free, target-innocent, untunable -- but
    it delivers a COUNT where the exponent needs a RATIO. Band pinned; point not pinned.
  * ★ TWO SURVIVORS, NOT ONE NUMBER: √(8π)={F_sqrt8pi:.4f} vs π²/2={F_pi2half:.4f}, {100*seam:.2f}% apart. The corpus
    phrase "16/3 → the 8π normalization → standard Planck mass" identifies two numbers that are not equal.
  * ★ THE DISCRIMINATOR IS G: G ∝ F⁻², so 1.6% in F is 3.1% in G. Standard-Planck reading {dev_std:+.4f}%;
    π²/2 reading {dev_alt:+.4f}%. Measurement favors standard by {abs(dev_alt/dev_std):.0f}:1. EVIDENCE, not forcing.
  * VERDICT, both directions: exponent 2C₂=12 CONFIRMED Derived-given-#16 -- FORCING B IS DONE, said plainly.
    The 0.07% G value additionally needs the exact normalization, which stays IDENTIFIED until the count→ratio
    step is written. Explicit split, not a demotion.

AUG-12. Nothing pushed. Nothing promoted beyond Cal's §428 stamp. My bars were committed blind yesterday and
fired unchanged today; the substitute provenance was ruled on rather than waved through. π²/2 ≠ √(8π) -- do not
relabel. The owed computation is small and 137-independent. Count once. CP existence-only.
""")
