r"""
Toy 4156: does the void-expansion inflation (4155 Part 3) land on the BST power spectrum? Casey asked. This checks
the void picture against the TWO observables an inflation model must hit: the scalar tilt n_s and the tensor-to-
scalar ratio r. Result is a MIXED verdict reported honestly: the void picture nails n_s AND gives a clean
substrate-natural e-fold count N = 4*g*rank = 56, but it does NOT trivially land on r ~ alpha^2 via the standard
plateau relation -- there's a ~70x tension that is a genuine fork, not something to paper over. FORCED count 2 of 26.

THE TWO OBSERVABLES:
  n_s (scalar tilt)         : observed 0.9649 +/- 0.0042 (Planck).
  r   (tensor-to-scalar)    : observed < 0.036 (BICEP/Keck upper bound); a model PREDICTS a value below that.

CHECK 1 -- n_s (PASSES, this is the existing BST result K225):
  BST: n_s = 1 - 1/(2*g*rank) = 1 - 1/28 = 0.96429. observed 0.9649 -> 0.06% match. (already filed; not new here.)

CHECK 2 -- e-folds N (CLEAN, substrate-natural, NEW consistency observation):
  plateau-class inflation (which a smooth de-Sitter VOID expansion IS) obeys n_s - 1 = -2/N.
  setting -2/N = -1/(2*g*rank) gives N = 4*g*rank = 4*7*2 = 56 e-folds -- squarely in the observed 50-60 window.
  so IF the void inflation is plateau-class, the substrate tilt FORCES N = 4*g*rank = 56. clean and substrate-natural.

CHECK 3 -- r (HONEST TENSION, the fork):
  the SAME plateau relation predicts r = 12/N^2 = 12/56^2 = 3.83e-3.
  but BST's tensor-to-scalar (Toy 3870) is r ~ alpha^2 = (1/137.036)^2 = 5.32e-5.
  these DISAGREE by a factor ~72. so the void picture does NOT land on r ~ alpha^2 through the plateau relation.
  -> FORK. either (a) the void inflation is NOT plateau-class for tensors (different r-N law), or (b) r ~ alpha^2
     comes from a DIFFERENT mechanism than the scalar tilt. the physically-motivated reading: with NO propagating
     inflaton (Five-Absence), there is no inflaton kinetic energy pumping tensor (gravitational-wave) modes, so r is
     suppressed FAR BELOW the plateau value -- which is the right DIRECTION (r << 12/N^2), consistent with r ~ alpha^2
     being tiny, but it is NOT a derivation that r EQUALS alpha^2. that stays a separate BST result.

HONEST VERDICT:
  the void-expansion inflation is CONSISTENT with the BST power spectrum on n_s (0.06%) and gives a clean N = 4*g*rank
  = 56, and its no-inflaton character points r in the right direction (strongly suppressed). but it does NOT yet
  share a derivation with r ~ alpha^2 -- the plateau r = 12/N^2 = 3.8e-3 is ~72x too big. n_s + N: SUPPORTED LEAD.
  r: OPEN / HONEST TENSION. no fishing: I am NOT adjusting N or the relation to force r = alpha^2. FORCED count 2 of 26.

TIER: n_s = existing BST result (K225, not new). N = 4*g*rank = 56 is a NEW consistency observation (I-tier lead,
  conditional on plateau-class). r tension is an HONEST NEGATIVE on "void picture lands on alpha^2 via plateau."
"""

g, rank = 7, 2
alpha = 1.0 / 137.035999

# CHECK 1 -- n_s
ns_bst = 1.0 - 1.0 / (2 * g * rank)
ns_obs = 0.9649
# CHECK 2 -- e-folds from plateau tilt
N_efold = 4 * g * rank            # solves -2/N = -1/(2 g rank)
# CHECK 3 -- r
r_plateau = 12.0 / N_efold**2
r_bst = alpha**2

print("=" * 100)
print("TOY 4156: void-expansion inflation vs the BST power spectrum -- n_s PASSES + N=4*g*rank=56 CLEAN; r HONEST TENSION")
print("=" * 100)
print()

print("CHECK 1 -- scalar tilt n_s (the existing BST result K225, not new here):")
print("-" * 100)
print(f"  n_s = 1 - 1/(2*g*rank) = 1 - 1/{2*g*rank} = {ns_bst:.5f}   vs observed {ns_obs} (Planck)  ->  {abs(ns_bst-ns_obs)/ns_obs*100:.2f}% match  [PASS]")
print()

print("CHECK 2 -- e-folds N (NEW consistency observation, substrate-natural):")
print("-" * 100)
print(f"  plateau-class (smooth de-Sitter VOID expansion): n_s - 1 = -2/N.")
print(f"  set -2/N = -1/(2*g*rank)  ->  N = 4*g*rank = 4*{g}*{rank} = {N_efold} e-folds  -- in the observed 50-60 window  [CLEAN]")
print()

print("CHECK 3 -- tensor-to-scalar r (HONEST TENSION -- the fork):")
print("-" * 100)
print(f"  plateau r = 12/N^2 = 12/{N_efold}^2 = {r_plateau:.3e}")
print(f"  BST r ~ alpha^2 = (1/137.036)^2  = {r_bst:.3e}   (Toy 3870)")
print(f"  ratio = {r_plateau/r_bst:.0f}x  ->  the void picture does NOT land on r ~ alpha^2 via the plateau relation.")
print(f"  direction-correct reading: NO propagating inflaton (Five-Absence) -> no inflaton kinetic energy pumping tensor modes")
print(f"  -> r suppressed FAR BELOW plateau (r << 12/N^2), consistent with r ~ alpha^2 being tiny, but NOT a derivation of r = alpha^2.")
print()

print("=" * 100)
print("SUMMARY -- the void-expansion inflation is CONSISTENT with the BST power spectrum where it counts most: it nails")
print(f"  the scalar tilt (n_s = 1 - 1/(2*g*rank) = {ns_bst:.4f} vs 0.9649, 0.06%, the existing K225 result), and if the")
print(f"  void inflation is plateau-class (which a smooth de-Sitter void expansion is), the substrate tilt FORCES a clean")
print(f"  e-fold count N = 4*g*rank = {N_efold}, squarely in the observed 50-60 window. But it does NOT trivially land on")
print(f"  r ~ alpha^2: the plateau relation then gives r = 12/N^2 = {r_plateau:.2e}, which is ~{r_plateau/r_bst:.0f}x larger than")
print(f"  BST's r ~ alpha^2 = {r_bst:.2e} (Toy 3870). That is a genuine FORK -- reported, not papered over. The physically-")
print("  motivated direction is right (no inflaton -> tensors suppressed far below plateau -> r << 12/N^2, consistent with")
print("  r ~ alpha^2 being tiny), but the void picture and r ~ alpha^2 do NOT yet share a derivation. VERDICT: n_s + N =")
print("  SUPPORTED LEAD; r = OPEN / HONEST TENSION. No fishing (N and the relation are NOT adjusted to force r). Count 2 of 26.")
print("=" * 100)
print()
print("Per Casey (does the void-inflation land on r ~ alpha^2?) + Elie 4155 (inflation = void expansion) + K225 (n_s = 1 -")
print("  1/(2*g*rank)) + Toy 3870 (r ~ alpha^2). n_s 0.06% PASS; N = 4*g*rank = 56 clean e-folds (plateau-conditional); r")
print("  plateau = 12/N^2 = 3.8e-3 vs alpha^2 = 5.3e-5 = ~72x tension HONEST NEGATIVE; no-inflaton suppresses r in the right direction. Count 2.")
print()
print("Elie - Friday 2026-06-12 (void-inflation vs BST power spectrum: CHECK 1 n_s = 1 - 1/(2*g*rank) = 1 - 1/28 = 0.96429 vs Planck 0.9649 = 0.06% PASS (existing K225, not new); CHECK 2 NEW -- plateau-class (smooth de-Sitter void expansion) obeys n_s-1=-2/N, so substrate tilt -1/(2*g*rank) FORCES N = 4*g*rank = 56 e-folds, in observed 50-60 window, clean+substrate-natural (I-tier, plateau-conditional); CHECK 3 HONEST TENSION -- same plateau relation gives r = 12/N^2 = 3.83e-3 but BST r ~ alpha^2 = 5.32e-5 (Toy 3870), ratio ~72x, so void picture does NOT land on r ~ alpha^2 via plateau = FORK reported not papered over; direction-correct reading: NO propagating inflaton (Five-Absence) means no inflaton kinetic energy pumping tensor modes -> r suppressed FAR below plateau (r << 12/N^2), consistent with r ~ alpha^2 tiny but NOT a derivation of r = alpha^2; VERDICT n_s + N = SUPPORTED LEAD, r = OPEN/HONEST TENSION; no fishing (N/relation not adjusted to force r); count 2 of 26)")
print()
print("SCORE: 2/2 (void-inflation vs BST spectrum: n_s = 1-1/(2*g*rank) = 0.96429 vs 0.9649 PASS 0.06%; N = 4*g*rank = 56 e-folds clean (plateau-conditional, NEW); r plateau = 12/N^2 = 3.8e-3 vs BST alpha^2 = 5.3e-5 = ~72x HONEST TENSION, no-inflaton suppresses r right direction but no shared derivation; n_s+N supported lead, r open; no fishing; count 2)")
