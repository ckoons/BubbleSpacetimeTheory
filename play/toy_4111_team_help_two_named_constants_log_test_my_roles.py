"""
Toy 4111: my contribution to Casey's "ask the team for help" -- on Lyra's open core (the two ground-state
boundary-norms she ground the lepton-mass problem down to). Three things: (1) the target SHARPENED to two
named rep-theory objects; (2) the log-prediction TEST framework; (3) an honest assessment of where my numerical
eyes help vs where I'd only add fishing risk. Count still 2; I do NOT fish the constants.

(1) THE TWO NAMED CONSTANTS (the team-help target -- specific, literature-able objects):
  A_tau = 1            -- the trivial rep at the vertex (DERIVED, the reference).
  A_mu  ~ 0.0595       -- the bulk-volume norm of the MINIMAL / harmonic ("scalar singleton") rep of SO(5,2)
                          at nu = 3/2 = (d-2)/2. [target for cross-check, NOT an input]
  A_e   ~ 2.88e-4      -- the BF-bound rep boundary norm = the LOG coefficient at nu = 5/2 = d/2. [cross-check target]
  ordering A_e < A_mu < A_tau (boundary norm increases toward the boundary; tau vertex = full = 1). f2 = A_tau/A_mu
  = 16.82, f1 = A_mu/A_e = 206.77 -- these are the TARGETS (the masses), not values to fit.

  WHERE THE BARE FUNCTION FAILS (Lyra's grind, confirmed): the bare Gamma_Omega residue ratio is 8/3 = 2.67 for
  tau/mu; the needed value is 16.82 (correction ~6.3). And bare x 2pi = 16.76 was the DEAD value (0.4% off) -- the
  2pi was a scheme-dependent regularization, refused. So A_mu, A_e are the QUOTIENT (null-removed) norms -- the
  minimal-rep and BF-rep normalizations of SO(5,2) -- NOT the bare reproducing kernel times anything.

(2) THE LOG-PREDICTION TEST (Lyra's structural claim; my framework to gate it when the constants land):
  tau/mu (both ordinary simple poles) -> ALGEBRAIC: a rational times a sqrt, no logarithm.
  mu/e and tau/e (touch the electron's BF point Delta = d/2, where equal indicial roots force a log) -> carry a LOG.
  => the lepton ratios live in (primaries)[pi, log]; the log enters ONLY through the electron. So 16.82 should be
     algebraic (clean), 206.77 doomed to carry a log (irrational/ugly). TEST when the constants land: is A_tau/A_mu
     algebraic? does A_mu/A_e carry a log? If yes, the "ugliness" of 206.77 IS the BF-electron's structural fingerprint
     -- its anomalous lightness and its irrationality are the same fact (the log).

(3) HONEST on where I help vs add risk (the ask-for-help answer):
  - the two constants are SPECIALIZED rep theory (minimal-rep + BF-rep normalizations of SO(5,2)). Lyra hit the edge
    and refused vol(S^3)=2pi^2 as a stand-in for 16.82. I would hit the same edge -- attempting to DERIVE them rapidly
    = fishing, not help. A wrong number that coincidentally hits or misses is worse than no number. So I do NOT race the constants.
  - WHAT I genuinely add: (a) the ONE-STEP HARNESS (hand me A_mu, A_e -> f1, f2 -> verdict vs {206.77, 16.82}, scale
    cancels, no knob); (b) INDEPENDENT CROSS-CHECK of any sub-result Lyra surfaces (the harmonic boundary trace, the
    BF log coefficient) -- a second computation catches errors; (c) the LOG-PREDICTION test framework above; (d) the
    BASE-RATE discipline (the dense space hands out 225-18=207 for free -> only a DERIVED pair counts).
  - team-help conclusion: the two constants need the rep-theory LITERATURE (the SO(5,2) minimal-rep / scalar-singleton
    normalization + the BF-bound-rep normalization) or a careful derivation -- a research-grade, references-open task.
    The most useful team contributions are (i) whoever has the literature pins those two normalizations, (ii) Lyra
    derives the quotient norms carefully, (iii) I cross-check + run the harness + gate the log prediction.
  - I OFFER: if Lyra wants a second independent computation, I will systematically grind the surviving-state Shapovalov
    products for the two quotients -- flagged explicitly as a cross-check candidate, NOT a banked result, NOT fished.

HONEST TIER:
  BANKED (this toy): the target sharpened to two named constants (A_mu = minimal-rep norm, A_e = BF-rep log coefficient);
    the log-prediction test framework; the honest role split (verify/harness/discipline, not race).
  NOT done / DECLINED: the two constants themselves -- specialized rep theory / literature. I do NOT fish them (vol(S^3),
    2pi, 225-18 all refused). COUNT still 2; banks 2->4 only when the derived pair lands within Grace's gate.

GATES (2)
G1: target sharpened -- two named SO(5,2) rep-theory constants: A_mu = minimal/singleton-rep norm (nu=3/2), A_e = BF-bound-rep norm / log coefficient (nu=5/2=d/2); ordering A_e<A_mu<A_tau=1; bare Gamma_Omega fails (dead 2pi); quotient norms needed
G2: log-prediction test framework (tau/mu algebraic, mu/e carries a log) + honest role split (I verify + harness + cross-check + discipline; I do NOT race the specialized constants = fishing risk); team-help = pin the two named normalizations from the literature; count still 2

Per Casey (ask the team for help) + Lyra (ground the problem to two constants: minimal-rep + BF-rep norms;
refused vol(S^3); log prediction) + Grace (gate; base-rate) + Keeper K308/K309; Elie 4106-4110 (quotient structure,
BF mechanism, walkback, harness); SO(5,2) minimal rep / singletons + BF bound (standard rep theory); Cal #237 + F79.
Team-help: sharpen the target + the log test + my verify/harness/discipline roles; the constants need the literature.

Elie - Thursday 2026-06-11 (team help: 2 named constants A_mu=minimal-rep norm + A_e=BF-rep log coeff of SO(5,2); log-prediction test; I verify+harness+cross-check+discipline, do NOT race the specialized constants (fishing risk); count 2)
"""

import math

A_tau = 1.0
A_mu = 1 / 16.817
A_e = A_mu / 206.77

print("=" * 78)
print("TOY 4111: team help -- two named constants + log-prediction test + my roles")
print("=" * 78)
print()

print("G1: the target sharpened to two named SO(5,2) rep-theory constants")
print("-" * 78)
print(f"  A_tau = 1.0       trivial rep at the vertex (DERIVED, reference)")
print(f"  A_mu  ~ {A_mu:.4f}    bulk-volume norm of the MINIMAL/harmonic (singleton) rep of SO(5,2), nu=3/2  [cross-check target]")
print(f"  A_e   ~ {A_e:.2e}  BF-bound rep boundary norm = the LOG coefficient, nu=5/2=d/2  [cross-check target]")
print(f"  ordering A_e < A_mu < A_tau=1 (norm increases toward the boundary). bare Gamma_Omega ratio 8/3=2.67 fails; bare x 2pi = 16.76 = DEAD. quotient norms needed.")
print()

print("G2: log-prediction test + honest role split")
print("-" * 78)
print(f"  LOG PREDICTION (Lyra): tau/mu (both ordinary poles) -> ALGEBRAIC (rational x sqrt); mu/e, tau/e (touch electron BF point) -> carry a LOG.")
print(f"    => 16.82 should be algebraic, 206.77 doomed to a log (irrational). TEST when constants land. (the ugliness of 206.77 = the BF-electron's signature.)")
print(f"  HONEST role split: I do NOT race the constants -- minimal-rep + BF-rep norms of SO(5,2) are specialized rep theory; rapid attempts = fishing (vol(S^3), 2pi refused).")
print(f"    I add: one-step harness (A_mu,A_e -> verdict); INDEPENDENT cross-check of Lyra's sub-results; the log-test framework; base-rate discipline.")
print(f"  @Casey/team: the help needed = pin the two named normalizations (SO(5,2) minimal/singleton + BF-bound rep) from the literature or careful derivation. My role = verify, not race.")
print(f"  @Lyra: offer -- if you want a second independent computation, I'll grind the surviving-state Shapovalov products as a CROSS-CHECK (flagged, not banked).")
print(f"  Score: 2/2 (target = two named constants; log-prediction test; honest role split (verify/harness/discipline, not race); count still 2)")
print()
print("=" * 78)
print("TOY 4111 SUMMARY -- my contribution to 'ask the team for help.' The open core is two named SO(5,2)")
print("  rep-theory constants: A_mu = the minimal/harmonic (singleton) rep's bulk-volume norm (nu=3/2), and A_e =")
print("  the BF-bound rep's boundary norm / log coefficient (nu=5/2=d/2). The bare Gamma_Omega fails (8/3, and the")
print("  bare x 2pi = 16.76 was the dead value); the quotient norms are needed. Lyra's log prediction (tau/mu")
print("  algebraic, mu/e carries a log) is a testable structural claim I can gate when the constants land. Honest")
print("  role split: I do NOT race the specialized constants (rapid attempts = fishing, vol(S^3)/2pi refused); I add")
print("  the one-step harness, independent cross-check of Lyra's sub-results, the log test, and the base-rate")
print("  discipline. Team-help = pin the two named normalizations from the literature/careful derivation. Count still 2.")
print("=" * 78)
print()
print("SCORE: 2/2")
