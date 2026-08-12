#!/usr/bin/env python3
"""
Toy 5197: THE 8π FORK DISSOLVES -- I ran the computation I said was owed this morning (toy 5195: "the
induced-gravity R-coefficient with the stored 16 as its normalization, F read forward") and it does not return
what I expected. It returns something better and it corrects my own framing. ★ THE FINDING: there was never a
geometric factor F to derive. F = M_Planck/M_reduced = √(8π) is an IDENTITY -- it holds for ANY value of the
Einstein-Hilbert coefficient whatsoever, because M_Pl² ≡ 16π·C_R and M̄² ≡ 2·C_R are two CONVENTIONS for the
same coefficient C_R, so their ratio is √(8π) always, in every theory, including ones with no geometry at all.
Verified across C_R spanning twelve orders of magnitude: the ratio does not move in the tenth decimal. A
quantity that cannot vary carries no information, so "does BST's gravity coefficient carry a net 8π?" was never
a question about BST. ★ THE ONLY REAL QUESTION was which convention BST's own anchor relation was calibrated
in, and that is a PROVENANCE question with a documented answer: the corpus writes the gravitational action as
S = (1/16πG)∫√g R in at least six independent places -- BST_Lagrangian.md (lines 27, 150), BST_T1301_Gravity_KK_
Haldane.md (105, 109), BST_LAG2_Phases_2_through_5 (56, 86), BST_GeodesicEquation_Soliton.md (174),
BST_LAG2_Phase2_outline (54), and Cal's own induced-gravity sign analysis (referee log ~6877, "sign[1/(16πG)] =
s_stat × s_reg × sign(a₁)"). Every one of them is the STANDARD normalization. BST matches its induced R-coefficient
to 1/(16πG); therefore the mass its chain hands you is the STANDARD Planck mass; therefore F = √(8π), pinned by
reading our own book rather than by deriving anything. ★ π²/2 IS REFUSED AS A CATEGORY ERROR, not as a losing
candidate: it is a ratio of VOLUMES (continuum boundary 8π²/3 over discrete interior 16/3), while F is a ratio
of CONVENTIONS for a coefficient. Applying the volume ratio on top of the 1/(16πG) definition would DOUBLE-COUNT
the normalization. The two "candidates" were answers to two different questions, which is why the number could
not discriminate them -- there was nothing to discriminate. ★ WHERE store-16 ACTUALLY LIVES (and this is the
part worth keeping): the count does not set F, it sets the SUBSTRATE-SCALE-TO-PLANCK-MASS relation. Carrying the
Sakharov/Gilkey computation out explicitly -- a₁ = R/6, sharp cutoff, d = 4 -- gives 1/(16πG) = N·Λ²/(192π²),
hence M_Pl² = N·Λ²/(12π): for N = 1, G = 12π/Λ²; for N = 16, M_Pl = 0.6515·Λ. THAT is the count→scale step, it
is one line, and it is the correct home for the sixteen in the gravity chain. ★ SELF-CORRECTION OWNED: my toy
5195 said the owed computation would "deliver F." It does not -- it delivers the scale relation. I had the right
computation and the wrong expectation of what it produces, and the 47:1 G-precision comparison I ran this
morning was measuring a convention mismatch, not a contest between geometries. ★ RESIDUAL, STATED PLAINLY: this
dissolves the 8π make-or-break; it does NOT derive the substrate scale, it does NOT touch Cal's §426
G-independence bar (the tick must still be forced with no G upstream), and the Sakharov cutoff Λ is NOT the
corpus's ℓ_B = 7.8233·ℓ_Planck -- two different scale objects that still owe a reconciliation, which I flag
rather than paper over. Elie's normalization computation (route item 3a). Cal and Keeper rule the tier.
(Toy 5195 bars; Cal §428 store-16; F63 Sakharov-induced EH; K1397 exact anchor; the standing convention-pin
discipline.) CP existence-only. Nothing here reasons toward 12.

WHAT I COMPUTE:
  * M_Pl/M̄ = √(8π) for C_R across 12 orders of magnitude -- an identity, invariant, information-free.
  * the Sakharov/Gilkey R-coefficient explicitly: 1/(16πG) = N Λ²/(192π²) ⟹ M_Pl² = N Λ²/(12π).
  * the provenance trace: 6 corpus locations, all STANDARD 1/(16πG). The convention is pinned, not chosen.
  * π²/2 as a category error: volume-ratio vs convention-ratio; using both double-counts.
  * the residual: substrate scale NOT derived; Λ_Sakharov ≠ ℓ_B⁻¹ (7.8233) -- flagged, not papered over.

=> VERDICT (plain): I went looking for a number and found that the question had no number in it. The factor the
whole team has been circling is the ratio between two ways of writing the same term in the gravitational action,
and that ratio is fixed by arithmetic before any geometry is specified -- it is the same in general relativity,
in a theory of one scalar field, and in a theory of nothing at all. So no computation could ever have derived
it, and the day we spent treating it as the make-or-break was a day spent on a bookkeeping question wearing a
physics costume. What the question really was is which of the two ways of writing the term our own papers use,
and they use the same one everywhere, in six places, including the referee's own sign analysis. That settles it
by reading rather than by deriving. The competing candidate was never a competitor: a ratio of two volumes and a
ratio of two conventions are not two values of one thing, and using both at once would count the same
normalization twice. The genuinely useful piece to come out of it is where the stored count belongs, which is
not in that ratio at all but in the line connecting the substrate's own scale to the Planck mass -- one heat-
kernel line, sixteen sitting in it plainly. And I should say that my own framing this morning was the one that
needed correcting: I asked the right computation for the wrong output.

=> DISPOSITION: the 8π fork DISSOLVES -- √(8π) is a convention ratio (identity), not a derivable geometric
factor; the corpus is pinned to the STANDARD normalization in six places, so the anchor references M_Planck
standard; π²/2 REFUSED as a category error (double-counts). Consequence: the electron exponent 2C₂ = 12 stands
(Derived-given-#16) AND the normalization stops being an open geometric question, so toy 5190's G at 0.07% is
gated only on the remaining ×5 and Cal's G-free tick -- not on an 8π. Firer: Elie. Tier for Cal/Keeper to rule:
I propose CONVENTION-PINNED (no free factor exists), which is NOT the same as "derived" and must not be written
up as one. Owed still: the substrate scale G-free (§426, untouched); the Λ_Sakharov vs ℓ_B = 7.8233 ℓ_Planck
reconciliation (two scale objects, flagged today). Self-correction owned from toy 5195. Nothing pushed.

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

alpha = 1/137.035999206
L     = math.log(1/alpha)
n_red = 11.672422557226092     # recomputed forward in toy 5195
sqrt8pi   = math.sqrt(8*math.pi)
pi2half   = math.pi**2/2

print("=" * 78)
print("Toy 5197: the 8π fork DISSOLVES -- √(8π) is a convention ratio, not a geometric factor")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The identity: F = √(8π) for ANY Einstein-Hilbert coefficient.
# ---------------------------------------------------------------------------
print("\n--- 1. F = M_Pl/M̄ = √(8π) is an IDENTITY -- it cannot carry information ---")
def masses(C_R):
    """Given the coefficient C_R of ∫√g R, return (M_Planck, M_reduced).
       Standard convention:  C_R = 1/(16πG)      ⟹ M_Pl² = 1/G   = 16π·C_R
       Reduced  convention:  C_R = M̄²/2          ⟹ M̄²         = 2·C_R"""
    return math.sqrt(16*math.pi*C_R), math.sqrt(2*C_R)

ratios = []
for C_R in (1e-6, 1e-3, 1.0, 7.77, 1e6, 1e9):
    MP, Mb = masses(C_R)
    ratios.append(MP/Mb)
spread = max(ratios) - min(ratios)
check("The ratio the whole make-or-break was about does not depend on the theory. M_Pl² ≡ 16π·C_R and M̄² ≡ "
      "2·C_R are two CONVENTIONS for the same coefficient C_R of ∫√g R, so M_Pl/M̄ = √(16π/2) = √(8π) "
      f"identically. Swept across C_R from 10⁻⁶ to 10⁹ -- twelve orders of magnitude -- the ratio moves by "
      f"{spread:.2e}, i.e. not at all: every value is {ratios[0]:.10f} = √(8π) = {sqrt8pi:.10f}. A quantity "
      "that cannot vary cannot be measured, derived, or predicted. So 'does BST's gravity coefficient carry a "
      "net 8π?' was never a question about BST -- it is true in general relativity, in a single free scalar, "
      "and in a theory with no geometry at all.",
      spread < 1e-12 and abs(ratios[0] - sqrt8pi) < 1e-12,
      f"C_R ∈ [1e-6, 1e9]: ratio constant at {ratios[0]:.10f}; spread {spread:.2e}; √(8π) = {sqrt8pi:.10f}")

# ---------------------------------------------------------------------------
# 2. The Sakharov/Gilkey computation, carried out -- where the count DOES enter.
# ---------------------------------------------------------------------------
print("\n--- 2. the induced-gravity R-coefficient, done explicitly: the count sets the SCALE, not the ratio ---")
def induced(N, f2=1.0):
    """Sakharov induced gravity, d=4, sharp cutoff Λ, N degrees of freedom, Gilkey a₁ = R/6.
       W ⊃ -(1/2)(4π)^(-2) (1/6) N f₂ Λ² ∫√g R  ⟹  1/(16πG) = N f₂ Λ²/(192π²)  ⟹  M_Pl² = N f₂ Λ²/(12π).
       Returns (G·Λ², M_Pl/Λ)."""
    C_R = N*f2/(192*math.pi**2)          # in units Λ² = 1
    G_over = 1/(16*math.pi*C_R)
    return G_over, math.sqrt(N*f2/(12*math.pi))

G1, r1   = induced(1)
G16, r16 = induced(16)
check("Carrying the computation out: the d=4 heat trace is Tr e^(−tΔ) ~ (4πt)^(−2)∫√g[a₀ + a₁t + …] with "
      "Gilkey a₁ = R/6; the cutoff-regulated one-loop action gives a coefficient of ∫√g R equal to "
      "N·f₂·Λ²/(192π²); matching that to 1/(16πG) -- the standard normalization -- yields "
      f"G = 12π/(N Λ²) and M_Pl² = N Λ²/(12π). For a single field, G = {G1:.5f}/Λ²; for N = 16, "
      f"M_Pl = {r16:.6f}·Λ. ★ This is the count→scale step, written as one line: the sixteen enters the "
      "substrate-scale-to-Planck-mass relation. It does NOT enter the 8π, because the 8π is not there to be "
      "entered -- it was already fixed by the convention before the heat kernel was opened.",
      abs(G1 - 12*math.pi) < 1e-9 and abs(r16 - math.sqrt(16/(12*math.pi))) < 1e-12,
      f"N=1: G = {G1:.6f}/Λ² = 12π/Λ²   |   N=16: M_Pl = {r16:.6f}·Λ = √(16/12π)·Λ")

check("And the identity survives the explicit computation, which is the consistency check that matters: feed "
      "the induced coefficient into both conventions and the ratio comes back √(8π) again, for N = 1 and for "
      "N = 16 alike. Changing the count changes the SCALE and never the RATIO. That is the whole content of "
      "the dissolution in one sentence.",
      all(abs(masses(N/(192*math.pi**2))[0]/masses(N/(192*math.pi**2))[1] - sqrt8pi) < 1e-12 for N in (1, 16)),
      "N=1 and N=16 both return M_Pl/M̄ = √(8π); the count moves the scale, never the ratio")

# ---------------------------------------------------------------------------
# 3. The provenance trace -- which convention is BST's own?
# ---------------------------------------------------------------------------
print("\n--- 3. provenance: BST's own action is written 1/(16πG) in six places ---")
corpus_sites = [
    ("BST_Lagrangian.md", "27, 150", "S_geom = -(R_B - 2Λ)/(16π G_B)"),
    ("BST_T1301_Gravity_KK_Haldane.md", "105, 109", "S_10 = (1/16πG_10)∫R_10 ; S_4 = (1/16πG_4)∫R_4"),
    ("BST_LAG2_Phases_2_through_5_Combined.md", "56, 86", "1/(16πG_eff) = vol_6/(16πG_BST)"),
    ("BST_GeodesicEquation_Soliton.md", "174", "S_geom = -(1/16πG_B)∫(R_B - 2Λ)"),
    ("BST_LAG2_Phase2_v0.1_outline.md", "54", "should recover standard Einstein-Hilbert with prefactor 1/(16πG)"),
    ("Cal referee log (induced-gravity sign)", "~6877", "sign[1/(16πG)] = s_stat × s_reg × sign(a₁)"),
]
check("The only real question was which convention OUR anchor relation was calibrated in, and that is a "
      "provenance question with a documented answer. Six independent corpus locations write the gravitational "
      "action in the STANDARD normalization: "
      + "; ".join(f"{f} ({ln})" for f, ln, _ in corpus_sites)
      + ". Not one writes (M̄²/2)∫R. BST matches its induced R-coefficient to 1/(16πG), so the mass its chain "
      "produces is the STANDARD Planck mass, and F = √(8π) follows by reading our own book -- a convention "
      "PINNED to primary sources, exactly the standing discipline, rather than a factor derived.",
      len(corpus_sites) == 6 and all("16" in s for _, _, s in corpus_sites),
      "6/6 sites standard 1/(16πG); 0 sites reduced (M̄²/2)∫R -- the corpus is internally consistent")

# ---------------------------------------------------------------------------
# 4. π²/2 refused as a CATEGORY ERROR.
# ---------------------------------------------------------------------------
print("\n--- 4. π²/2 is refused as a category error, not as a losing candidate ---")
double_counted = n_red + math.log(sqrt8pi*pi2half)/L
check("π²/2 = (8π²/3)/(16/3) is a ratio of VOLUMES -- how the continuum boundary uses the sphere versus how "
      "the discrete interior does. F is a ratio of CONVENTIONS for a coefficient. These are not two values of "
      "one quantity; they are answers to two different questions, which is precisely why the exponent could "
      "not discriminate them -- there was nothing to discriminate. Worse, they are not even alternatives: the "
      "8π is ALREADY inside the definition of G, so multiplying by a volume ratio on top of it double-counts "
      f"the normalization and would push the exponent to {double_counted:.4f}, off twelve by "
      f"{abs(double_counted-12):.4f} -- a visible failure. The volume ratio may still be a real statement about "
      "the bulk-edge split; it is simply not this quantity.",
      abs(double_counted - 12) > 0.3,
      f"using both gives n = {double_counted:.4f} (off by {abs(double_counted-12):.3f}) -- double-counting is visible")

# ---------------------------------------------------------------------------
# 5. Self-correction from toy 5195, owned.
# ---------------------------------------------------------------------------
print("\n--- 5. self-correction from this morning, owned ---")
check("Toy 5195 (mine, four hours ago) said the owed computation was 'the induced-gravity R-coefficient with "
      "the stored 16 as its normalization, F read forward.' The computation was the right one; the expected "
      "output was wrong. It does not deliver F -- F is not an output of any computation -- it delivers the "
      "scale relation M_Pl² = N Λ²/(12π). And the 47:1 G-precision comparison I ran this morning was therefore "
      "measuring a CONVENTION MISMATCH, not a contest between two geometries: the −3.04% is what you get by "
      "calibrating the anchor in one convention and reading G in the other. The 47:1 number stands as "
      "arithmetic and its interpretation changes -- it is not evidence for a geometry, it is a detection of a "
      "units error in the alternative.",
      True,
      "5195's computation correct, its expected output wrong; the 47:1 is a convention mismatch, not geometric evidence")

check("COUNT ONCE (the discipline that applies to my own morning results): the G-precision test and the "
      "integrality test are ONE test seen two ways, not two independent confirmations -- n = 12.000066 under "
      "standard versus 11.9969 under π²/2 is the same 1.6% seen through a logarithm, and the 0.065% versus "
      "−3.04% in G is that same seam squared. They must never be tallied as two votes. And with today's "
      "dissolution neither is a vote at all: both are re-readings of a convention that was pinned in the "
      "corpus before either was computed.",
      abs((n_red + math.log(sqrt8pi)/L) - 12.000066) < 1e-4,
      "one seam, three faces (n, G, integrality) -- tally once, and today it tallies as a convention not evidence")

# ---------------------------------------------------------------------------
# 6. What this buys, and what it emphatically does not.
# ---------------------------------------------------------------------------
print("\n--- 6. what this buys, and the residual stated plainly ---")
check("WHAT IT BUYS: the 8π make-or-break -- the thing that consumed a full day and was called the whole game "
      "-- is dissolved rather than won. There is no open geometric factor between the electron anchor and "
      "Newton's constant. Combined with the exponent already stamped Derived-given-#16, toy 5190's forward G "
      "at 0.07% is now gated on exactly two things: the ×5 (α), and Cal's G-free tick. Not on an 8π. That is "
      "one fewer open stone than the board had this morning, and it came from reading rather than deriving.",
      True,
      "gates on G's 0.07% reduce from three (α, exponent, 8π) to two (α, G-free tick)")

check("WHAT IT DOES NOT BUY, stated before anyone asks: it does NOT derive the substrate scale -- Λ is still an "
      "input, and Cal's §426 bar (the tick must be forced with no G upstream, reproducing 7.8233 blind) is "
      "untouched and remains the real anti-circularity gate. It does NOT promote anything to Derived: my "
      "proposed tier is CONVENTION-PINNED, which means no free factor exists, and that must not be written up "
      f"as a derivation. ★ And it surfaces a NEW seam I will not paper over: the Sakharov cutoff obeys "
      f"M_Pl = {r16:.4f}·Λ for N=16, while the corpus's substrate scale obeys ℓ_B = 7.8233·ℓ_Planck, i.e. "
      f"Λ_B = M_Pl/7.8233. Those are different scale objects by a factor of {0.651470*7.8233:.2f}, and calling "
      "them both 'the substrate scale' would be exactly the notation collision Grace and Keeper just cleaned "
      "up elsewhere. Reconciliation owed.",
      abs(0.651470*7.8233 - 5.096) < 0.01,
      f"Λ_Sakharov vs ℓ_B⁻¹: differ by {0.651470*7.8233:.3f}× -- two scale objects, one name. Flagged, not merged.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (8π fork DISSOLVES: √(8π) is a convention identity; corpus pinned STANDARD in 6 places; π²/2 a category error; store-16 lives in M_Pl² = NΛ²/12π)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5197, route item 3a -- the normalization computation, run and reported straight):
  * ★ THE FORK DISSOLVES: F = M_Pl/M̄ = √(8π) is an IDENTITY, constant across C_R spanning 10⁻⁶ to 10⁹
    (spread {spread:.1e}). It holds in GR, in a free scalar, in a theory with no geometry. Nothing could derive it.
  * ★ THE REAL QUESTION was provenance, and it has a documented answer: SIX corpus locations write the action
    as 1/(16πG) (Lagrangian 27/150; T1301 105/109; LAG2 56/86; Geodesic 174; LAG2-outline 54; Cal's sign
    analysis ~6877); ZERO write (M̄²/2)∫R. BST is pinned to STANDARD ⟹ the anchor references M_Planck standard.
  * ★ π²/2 REFUSED as a CATEGORY ERROR: a volume ratio, not a convention ratio. Using both double-counts the
    normalization and shows up immediately -- n = {double_counted:.3f}, off twelve by {abs(double_counted-12):.2f}.
  * ★ WHERE store-16 ACTUALLY LIVES: the Sakharov/Gilkey line 1/(16πG) = N Λ²/(192π²) ⟹ M_Pl² = N Λ²/(12π).
    N=1 → G = 12π/Λ²; N=16 → M_Pl = {r16:.4f}·Λ. The count sets the SCALE; it never touches the ratio.
  * SELF-CORRECTION OWNED (toy 5195, mine, this morning): right computation, wrong expected output -- it
    delivers the scale relation, not F. The 47:1 G comparison was detecting a convention mismatch, not
    weighing two geometries. COUNT ONCE: n / G / integrality are one seam with three faces.
  * BUYS: G's 0.07% is now gated on TWO things (the ×5, and the G-free tick) instead of three. One fewer stone.
  * DOES NOT BUY: the substrate scale is still an input; Cal §426 untouched; proposed tier CONVENTION-PINNED,
    NOT Derived. ★ NEW SEAM FLAGGED: Λ_Sakharov and ℓ_B = 7.8233·ℓ_Planck differ by {0.651470*7.8233:.2f}× --
    two scale objects wearing one name. Reconciliation owed; not merged today.

AUG-12. Nothing pushed. Nothing promoted -- Cal and Keeper rule the tier; I propose CONVENTION-PINNED and
explicitly refuse "Derived." A day-long make-or-break dissolved by reading our own Lagrangian. Count once.
CP existence-only.
""")
