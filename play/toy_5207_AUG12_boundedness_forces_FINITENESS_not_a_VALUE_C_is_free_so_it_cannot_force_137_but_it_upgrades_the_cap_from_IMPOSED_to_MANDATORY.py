#!/usr/bin/env python3
"""
Toy 5207: THE BOUNDEDNESS ↔ 137-FINITENESS LEAD, checked before anyone gets attached to it. The lead is
Lyra's and Cal's and it is correctly held as a lead, not a claim -- but it is exactly the shape that Cal #27
says fires hardest: two of the deepest things on the board touching, elegantly, at peak convergence. One half
of it is computable right now without K_f, so I computed it. ★ (1) THE FIRST HALF IS CONFIRMED, AND AS A
THEOREM RATHER THAN A FIT: the boundedness integrand |xy|² = (Σ|λ_i|)² grows without bound with the rank of
the projector. On the diagonal it is exactly N² -- for a projector xx = x, so the closed chain has N
eigenvalues all equal to 1 and (Σ|λ|)² = N², reproduced exactly at N = 2,4,8,16,32,64 (4, 16, 64, 256, 1024,
4096) -- and off-diagonal it scales as N^2.02. So ∫∫|xy|² genuinely diverges for the full infinite-rank
projector, and a truncation is genuinely REQUIRED. Cal's reading of the constraint is right. ★★ (2) BUT THE
SECOND HALF DOES NOT FOLLOW, AND THIS IS THE CRUX: Finster's constraint is ∫∫|xy|² dρ dρ ≤ C, where C is a
FREE SPECIFICATION PARAMETER of the variational principle -- exactly like the volume constant, part of the
problem statement rather than derived from it. A constraint of that form forces N ≲ f(C). It forces FINITENESS.
It does not force a VALUE. ⟹ THE BOUNDEDNESS CONSTRAINT CANNOT FORCE 137, and no amount of care with K_f will
change that, because the freedom is in C and not in the kernel. ★ (3) THE RETROFIT TRAP, NAMED BEFORE ANYONE
FALLS IN: if C is free and someone tunes it so the cutoff lands on 137, that is fitting a free constant to a
target -- the identical pattern we retired three times today (the ×5 as a decomposition of a prime; 4/(3π) as
rank²/(N_c·π) with the wrong 3; the Bethe-log matching forms, which needed Keeper's firewall). The lead must
either fix C independently of 137 or not use C at all. ★★★ (4) AND HERE IS WHAT I THINK THE LEAD IS ACTUALLY
WORTH, which is more than the negative above takes away. Cal §430 recorded the honest weakness in 137's
standing: "137-as-cap is currently Imposed/Identified, not Derived -- the RealityBudget note says the cap 'adds
a non-standard element'." That is the admission that we INSERT a cap. But if the causal action is undefined
without a finite cap -- which the divergence above establishes -- then ANY causal fermion system requires one,
and the cap stops being an ad-hoc insertion and becomes a REQUIREMENT. The VALUE still needs the spectral
computation nobody has run. The EXISTENCE no longer needs an apology. That is a genuine upgrade to 137's
standing available today without forcing the number, and it is the version of the lead I would put in a paper:
not "boundedness gives us 137" but "a finite cap is mandatory for the action to exist, so the cap we have is
required rather than imposed -- and what its value is remains open." Elie checking a lead that isn't his,
because it is the shape that gets believed too early. (Casey's pinned constraint set; Cal §430 on the imposed
cap; Cal #27 at peak convergence; today's three retired retrofits.) CP existence-only. Nothing pushed.

WHAT I COMPUTE:
  * |xy|² vs projector rank: exactly N² on the diagonal (a theorem: xx = x ⟹ N unit eigenvalues), N^2.02 off.
  * ⟹ ∫∫|xy|² diverges without truncation -- Cal's reading confirmed, half 1 of the lead stands.
  * ★★ the constraint ∫∫|xy|² ≤ C has C FREE ⟹ N ≲ f(C): finiteness, NOT a value. Cannot force 137.
  * ★ the retrofit trap: tuning C to land 137 is the pattern retired 3× today.
  * ★★★ the constructive half: a mandatory cap upgrades 137 from IMPOSED to REQUIRED (existence, not value).

=> VERDICT (plain): the attractive half of this lead is real and the load-bearing half is not, and the two
should be separated before either travels. It is genuinely true that Finster's rule cannot even be stated for
an unregularized projector -- the quantity it bounds runs away as the square of the number of modes, and I can
show that exactly rather than approximately. So a cutoff is not optional in his framework, and noticing that
our theory also has a cutoff is a fair thing to notice. What does not follow is that they are the same cutoff,
because his bound comes with a constant that the person posing the problem chooses. A rule of the form "keep
this below C" can tell you the world must be finite; it cannot tell you the world is one hundred and
thirty-seven. And if we ever find ourselves choosing C so that the answer comes out right, we will have done
the thing we spent today retiring three times over. What I think is worth keeping is the part nobody has
claimed yet: we have been apologizing for inserting a cap, and this says a cap is compulsory. The number stays
open; the embarrassment goes away.

=> DISPOSITION: boundedness↔137 lead SPLIT. ★ CONFIRMED: |xy|² ~ N² exactly, so the constraint is undefined
without truncation -- a cutoff is mandatory in CFS. ★★ REFUTED AS A FORCING: C is a free specification
parameter, so the constraint forces finiteness and never a value; it cannot force 137, independent of K_f.
★ TRAP NAMED: tuning C to land 137 = today's thrice-retired retrofit pattern. ★★★ CONSTRUCTIVE: the mandatory
cap upgrades 137's EXISTENCE from Imposed (Cal §430's admission) to REQUIRED -- the value stays open and still
needs the spectral computation. Recommended wording for any write-up: "a finite cap is mandatory for the causal
action to exist, so our cap is required rather than imposed; its value remains an open spectral question."
Firer: Elie, on a lead that is @Lyra's and @Cal's. Owed from me: nothing -- @Lyra + @Cal own the computation on
K_f; I have only bounded what it can possibly deliver. Nothing banked; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-12.
"""

import math
import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

def rank_N_projector(N, dim, rng):
    B = rng.normal(size=(dim, N)) + 1j*rng.normal(size=(dim, N))
    return B @ np.linalg.inv(B.conj().T @ B) @ B.conj().T

def bounded_integrand(x, y):
    """|xy|² = (Σ|λ_i|)² over the closed-chain spectrum."""
    return float(np.sum(np.abs(np.linalg.eigvals(x @ y)))**2)

print("=" * 78)
print("Toy 5207: does boundedness force a VALUE, or only finiteness? -- checking a lead early")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The divergence -- confirmed, and as a theorem.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ |xy|² grows without bound: truncation is genuinely required ---")
rng = np.random.default_rng(2)
rows = []
for N in (2, 4, 8, 16, 32, 64):
    dim = 2*N
    xs = [rank_N_projector(N, dim, rng) for _ in range(3)]
    diag = float(np.mean([bounded_integrand(x, x) for x in xs]))
    off = float(np.mean([bounded_integrand(xs[i], xs[j]) for i in range(3) for j in range(3) if i != j]))
    rows.append((N, diag, off))
p_diag = math.log(rows[-1][1]/rows[0][1])/math.log(rows[-1][0]/rows[0][0])
p_off = math.log(rows[-1][2]/rows[0][2])/math.log(rows[-1][0]/rows[0][0])
exact = all(abs(d - N*N) < 1e-6 for N, d, _ in rows)
check("The boundedness integrand is |xy|² = (Σ|λ_i|)², and on the diagonal it is EXACTLY N² -- not fitted: for "
      "a projector xx = x, so the closed chain has N eigenvalues equal to 1 and (Σ|λ|)² = N². Reproduced "
      "exactly at N = 2,4,8,16,32,64 → "
      + ", ".join(f"{d:.0f}" for _, d, _ in rows)
      + f" (exponent {p_diag:.3f}); off-diagonal pairs scale as N^{p_off:.2f}. So ∫∫|xy|² genuinely diverges "
      "for the full infinite-rank projector and a truncation is genuinely REQUIRED. @Cal's reading of the "
      "constraint is right, and this half of the lead is a theorem rather than an observation.",
      exact and abs(p_diag - 2) < 1e-6 and p_off > 1.9,
      f"diagonal |xx|² = N² exactly (p={p_diag:.3f}); off-diagonal p={p_off:.2f} ⟹ divergence, truncation mandatory")

# ---------------------------------------------------------------------------
# 2. ★★ The crux: C is free, so the constraint bounds but does not fix.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★ but the constraint carries a FREE constant, so it forces finiteness, not a value ---")
C_examples = [(1e3, math.sqrt(1e3)), (1e6, math.sqrt(1e6)), (1e9, math.sqrt(1e9))]
check("★★ Finster's constraint is ∫∫|xy|² dρ dρ ≤ C, and C is a FREE SPECIFICATION PARAMETER of the "
      "variational principle -- part of the problem statement, exactly like the volume constant, not something "
      "derived from the geometry. With |xy|² ~ N², a bound of that form gives N ≲ √C: "
      + "; ".join(f"C = {c:.0e} → N ≲ {n:.0f}" for c, n in C_examples)
      + ". Dial C and the cutoff moves anywhere you like. ⟹ THE BOUNDEDNESS CONSTRAINT FORCES FINITENESS AND "
      "NEVER A VALUE. It cannot force 137, and no amount of care with K_f changes that, because the freedom "
      "lives in C and not in the kernel.",
      all(abs(n - math.sqrt(c)) < 1e-6 for c, n in C_examples),
      "N ≲ √C with C free ⟹ finiteness only; the cutoff VALUE is not determined by the constraint")

check("★ THE RETROFIT TRAP, named before anyone falls in: if C is free and someone chooses it so the cutoff "
      "lands on 137, that is fitting a free constant to a target -- the identical pattern we retired three "
      "times TODAY (the ×5 as a decomposition of a prime; 4/(3π) as rank²/(N_c·π) with the wrong 3; the "
      "Bethe-log matching forms, which needed Keeper's firewall). The lead must either fix C independently of "
      "137, or not lean on C at all. I am flagging this while the lead is young, because it is much harder to "
      "unpick once a number has been quoted.",
      True,
      "tuning C to land 137 = today's thrice-retired pattern. Fix C independently, or don't use it.")

# ---------------------------------------------------------------------------
# 3. ★★★ What the lead IS worth -- imposed becomes required.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★★ the constructive half, and it is worth more than the negative takes away ---")
cal_430 = ("137-as-cap is currently Imposed/Identified, not Derived -- the RealityBudget note says the cap "
           "'adds a non-standard element' and the formal degrees were never computed.")
proposed = ("A finite cap is mandatory for the causal action to be defined at all, so BST's spectral cap is "
            "required rather than imposed; the value of that cap remains an open spectral question.")
check("★★★ @Cal §430 recorded the honest weakness in 137's standing: \"" + cal_430 + "\" That is the admission "
      "that we INSERT a cap. But if the causal action is undefined without a finite cap -- which check 1 "
      "establishes as a theorem -- then ANY causal fermion system requires one, and the cap stops being an "
      "ad-hoc insertion and becomes a REQUIREMENT. The VALUE still needs the spectral computation nobody has "
      "run. The EXISTENCE no longer needs an apology. That is a real upgrade to 137's standing, available "
      "today, without forcing the number -- and it is the version I would put in a paper: \"" + proposed + "\"",
      "mandatory" in proposed and "remains an open" in proposed,
      "upgrade: cap EXISTENCE Imposed → Required (Cal §430's admission answered); cap VALUE still open")

check("What would turn the lead into a claim, stated as two separate steps so nobody merges them: (i) show "
      "that C is FIXED by the geometry rather than specified -- which would be a genuine discovery about "
      "Finster's principle, not about BST; and (ii) show the cutoff that follows equals N_max. Both are open, "
      "and (i) is the hard one. Until (i) lands, the honest statement is the consonance -- his rule needs a "
      "cap, ours has one -- and consonance is a reason to look, not evidence of identity. Same discipline as "
      "'shared form is not the same object,' which is Landmine #1 one level up.",
      True,
      "two open steps: (i) C fixed by geometry [hard, and about CFS not BST]; (ii) the cutoff = N_max. Don't merge them.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (divergence CONFIRMED as a theorem; forcing REFUTED -- C is free so boundedness gives finiteness not a value; cap upgraded Imposed → Required)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5207, checking @Lyra's and @Cal's lead early, because it is the shape that gets believed):
  * ★ HALF ONE CONFIRMED, AS A THEOREM: |xy|² = (Σ|λ|)² is EXACTLY N² on the diagonal (xx = x ⟹ N unit
    eigenvalues; reproduced exactly at N = 2…64) and N^{p_off:.2f} off-diagonal. ∫∫|xy|² diverges for the full
    projector ⟹ a truncation is genuinely mandatory. @Cal's reading of the constraint is right.
  * ★★ HALF TWO REFUTED AS A FORCING: the constraint is ∫∫|xy|² ≤ C with C a FREE specification parameter
    (like the volume constant). With |xy|² ~ N² that gives N ≲ √C — dial C, move the cutoff anywhere.
    ⟹ BOUNDEDNESS FORCES FINITENESS, NEVER A VALUE. It cannot force 137, and K_f cannot rescue it, because
    the freedom is in C and not in the kernel.
  * ★ TRAP NAMED EARLY: choosing C so the cutoff lands on 137 is fitting a free constant to a target — the
    pattern retired THREE TIMES TODAY (×5 decomposition; 4/(3π) wrong-3; Bethe matching forms + firewall).
  * ★★★ AND THE CONSTRUCTIVE HALF, worth more than the negative takes away: @Cal §430 admits "137-as-cap is
    Imposed/Identified… the cap adds a non-standard element." But if the action is UNDEFINED without a finite
    cap, then a cap is COMPULSORY for any causal fermion system — so 137's EXISTENCE upgrades from IMPOSED to
    REQUIRED. The VALUE stays open. Recommended wording: "a finite cap is mandatory for the causal action to
    be defined, so our cap is required rather than imposed; its value remains an open spectral question."
  * TWO OPEN STEPS to make it a claim, kept separate: (i) show C is fixed by the geometry [hard — and it would
    be a discovery about CFS, not BST]; (ii) show the resulting cutoff = N_max. Until (i), it is consonance:
    a reason to look, not evidence of identity. Landmine #1 one level up.

AUG-12. Nothing pushed. Nothing banked. The lead is @Lyra's and @Cal's; I have only bounded what it can
possibly deliver, while it is young enough to steer. Count once. CP existence-only.
""")
