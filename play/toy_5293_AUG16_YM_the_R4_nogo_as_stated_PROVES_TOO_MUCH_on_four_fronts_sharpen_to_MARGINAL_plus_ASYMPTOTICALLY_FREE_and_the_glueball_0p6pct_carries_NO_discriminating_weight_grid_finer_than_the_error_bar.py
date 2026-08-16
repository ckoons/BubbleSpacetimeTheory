"""
Toy 5293 (Elie, 2026-08-16 afternoon) -- Phase 1 make-or-break: the S2 false-neighbour check on the
R^4 no-go, plus the honest glueball tier. Both come back with corrections the draft needs BEFORE it
is written, not after.

★★★ (A) THE NO-GO AS STATED PROVES TOO MUCH -- ON FOUR FRONTS, NOT ONE.
The mechanism as written is "the gap is a BULK property of D_IV^5; R^4-alone cannot carry it." That
sentence names NO gauge group and NO dimension, so it applies verbatim to:
  1. FREE/ABELIAN U(1) on R^4 -- which is RIGOROUSLY CONSTRUCTED (Gaussian measure, textbook). The
     loose no-go would block a construction that demonstrably exists.
  2. phi^4 in d=2 (Glimm-Jaffe) -- RIGOROUSLY CONSTRUCTED and MASSIVE. A gap built natively on FLAT
     space, no bulk anywhere.
  3. phi^4 in d=3 -- same. So "flat space cannot carry a constructed gap" is simply FALSE; it was
     done in the 1970s.
  4. And the subtlest: SU(3) YM on a 4D lattice has its gap MEASURED. So the no-go cannot be about
     the gap's EXISTENCE on R^4 at all -- only about a rigorous CONSTRUCTION. Those are different
     claims and the draft must not slide between them.
Keeper asked about the abelian neighbour; there were three more, and (2)/(3) are the dangerous ones
because they refute the bulk-vs-flat framing directly.

★★ (B) THE SHARPENING -- what IS non-abelian-specific and d=4-specific, as numbers.
  * one-loop b_0 = 11N/3 - 2 n_f/3. The 11N/3 term is the GLUON SELF-INTERACTION and is EXACTLY ZERO
    for an abelian group: U(1) 0.000, SU(2) 7.333, SU(3) 11.000, SU(5) 18.333. That term IS the
    abelian/non-abelian discriminator, and it is a number, not a story.
  * [g^2] has mass dimension 4-d: d=2 -> +2 and d=3 -> +1 are SUPER-renormalisable (which is exactly
    WHY phi^4_2 and phi^4_3 are constructible), d=4 -> 0 is MARGINAL. The hardness of Clay-YM is a
    DIMENSION statement, not a bulk-vs-flat statement.
  ★ SHARPENED NO-GO (the form that survives all four neighbours):
      "No R^4-native construction is available for a theory that is MARGINAL (d=4) AND
       ASYMPTOTICALLY FREE (b_0 > 0, i.e. non-abelian) -- the two conditions that jointly force
       dimensional transmutation, so the gap cannot be read off the Lagrangian."
    Excludes abelian (b_0 < 0), excludes phi^4_{2,3} (not marginal), and is SILENT about the gap's
    existence on the lattice. Exactly the four neighbours, excluded by construction.

★★★ (C) THE GLUEBALL: THE 0.6% CARRIES ESSENTIALLY NO DISCRIMINATING WEIGHT, AND I HAVE TO SAY SO.
Delta = c_2 pi^5 m_e with c_2 = 11 gives 1720.14 MeV against the quenched-lattice 0++ at
1730 +- 50 +- 80 (combined +-94): 0.57%, 0.10 sigma. Looks superb. But the formula's allowed values
form an INTEGER GRID of spacing pi^5 m_e = 156.4 MeV, and the comparison window is 189 MeV wide --
WINDOW/GRID = 1.21. THE WINDOW IS WIDER THAN THE SPACING, SO SOME INTEGER c_2 IS GUARANTEED TO LAND
IN IT. The agreement is not evidence.
=> THE ENTIRE CONTENT IS WHETHER c_2 = 11 IS DERIVED TARGET-INNOCENTLY (Lyra: the 2-form K-type
   Casimir). If it is, the RESULT IS THE DERIVATION OF 11 and the 0.6% is decoration. If it is not,
   there is nothing here. The claim line should lead with the derivation of c_2, never with the 0.6%.
AND A SECOND TIER CAUTION: 1730 is itself a LATTICE COMPUTATION, not a measurement -- the 0++
glueball has never been unambiguously observed (f_0(1710) mixes with q-qbar). This is a
computation-to-computation comparison. I-tier is right; I would put the word "lattice" in the claim
line so no referee mistakes it for data.

Nothing pushed. CP existence-only.
"""
import numpy as np

print("=" * 92)
print("Toy 5293: the R^4 no-go as stated PROVES TOO MUCH on four fronts -> sharpen to MARGINAL +")
print("          ASYMPTOTICALLY FREE; and the glueball 0.6% carries no discriminating weight.")
print("=" * 92)

tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

print("\n(A) S2 FALSE-NEIGHBOUR CHECK on 'the gap is a BULK property; R^4-alone cannot carry it'\n")
neigh = [
    ("free/abelian U(1) on R^4", "RIGOROUSLY CONSTRUCTED (Gaussian)", "blocks a construction that EXISTS"),
    ("phi^4 in d=2 (Glimm-Jaffe)", "CONSTRUCTED and MASSIVE", "a gap on FLAT space, no bulk"),
    ("phi^4 in d=3", "CONSTRUCTED and MASSIVE", "'flat space cannot carry a gap' is FALSE"),
    ("SU(3) YM on a 4D lattice", "gap MEASURED numerically", "so the no-go is about CONSTRUCTION, not existence"),
]
for a, b, c in neigh:
    print("   - %-30s %-34s -> %s" % (a, b, c))
check("1. ★★★ THE NO-GO AS STATED PROVES TOO MUCH -- four neighbours, not one",
      len(neigh) == 4,
      "the sentence names no gauge group and no dimension, so it applies verbatim to all four. "
      "Keeper asked about the abelian one; (2) and (3) are the dangerous ones, because phi^4_{2,3} "
      "are rigorously constructed WITH gaps on flat space -- they refute the bulk-vs-flat framing "
      "directly. And (4) is the sliding risk: the lattice gap is MEASURED, so the no-go can only be "
      "about a rigorous CONSTRUCTION.")

print("\n(B) THE SHARPENING\n")
print("      group          N     11N/3     b_0 (n_f=6)    asymptotically free?")
rows = []
for name, N in (("U(1) abelian", 0), ("SU(2)", 2), ("SU(3)", 3), ("SU(5)", 5)):
    t = 11 * N / 3
    rows.append((name, N, t, t - 4.0))
    print("    %-14s %3d  %8.3f  %11.3f      %s" % (name, N, t, t - 4.0, "YES" if t - 4.0 > 0 else "NO"))
check("2. ★★ THE 11N/3 GLUON SELF-COUPLING IS THE ABELIAN DISCRIMINATOR -- a number, not a story",
      rows[0][2] == 0.0 and all(r[2] > 0 for r in rows[1:]),
      "11N/3 is EXACTLY ZERO for abelian (photons do not couple to photons) and 7.333/11.000/18.333 "
      "for SU(2)/SU(3)/SU(5). Any BST no-go must be CONDITIONED on it, or it applies to the photon.")

dims = [(d, 4 - d) for d in (2, 3, 4, 5)]
check("3. AND d = 4 IS THE MARGINAL CASE -- the hardness is a DIMENSION statement",
      [x for x in dims if x[1] == 0][0][0] == 4,
      "[g^2] has mass dimension 4-d: " + ", ".join("d=%d:%+d" % x for x in dims) +
      ". d=2,3 are SUPER-renormalisable, which is exactly WHY phi^4_2 and phi^4_3 are constructible; "
      "d=4 is marginal. Clay-YM is hard because of the DIMENSION, not because R^4 lacks a bulk.")

check("4. ★ THE SHARPENED NO-GO THAT SURVIVES ALL FOUR NEIGHBOURS",
      True,
      "'No R^4-native construction is available for a theory that is MARGINAL (d=4) AND "
      "ASYMPTOTICALLY FREE (b_0 > 0, i.e. non-abelian) -- the two conditions that jointly force "
      "dimensional transmutation, so the gap cannot be read off the Lagrangian.' Excludes abelian "
      "(b_0 < 0), excludes phi^4_{2,3} (not marginal), silent about the lattice gap's existence.")

print("\n(C) THE GLUEBALL TIER\n")
me, pi5 = 0.511, np.pi ** 5
pred = 11 * pi5 * me
obs, tot = 1730.0, float(np.hypot(50.0, 80.0))
grid, window = pi5 * me, 2 * tot
print("      Delta = c_2 pi^5 m_e, c_2 = 11  ->  %.2f MeV" % pred)
print("      lattice 0++ (Morningstar-Peardon): 1730 +- 50 +- 80 = +-%.0f  ->  %.2f%%, %.2f sigma"
      % (tot, 100 * abs(pred - obs) / obs, abs(pred - obs) / tot))
for c in range(9, 14):
    v = c * pi5 * me
    print("        c_2=%2d -> %8.1f MeV %s" % (c, v, "  <- INSIDE the window" if abs(v - obs) < tot else ""))
check("5. ★★★ THE 0.6% CARRIES NO DISCRIMINATING WEIGHT -- the grid is finer than the error bar",
      window / grid > 1.0,
      "the formula's allowed values form an INTEGER GRID of spacing %.1f MeV; the comparison window "
      "is %.0f MeV wide. WINDOW/GRID = %.2f > 1, so SOME integer c_2 is GUARANTEED to land in it. "
      "=> the ENTIRE content is whether c_2 = 11 is DERIVED target-innocently (the 2-form K-type "
      "Casimir). If it is, the result IS the derivation of 11 and the 0.6%% is decoration; if it is "
      "not, there is nothing here. The claim line must lead with the derivation, never the 0.6%%."
      % (grid, window, window / grid))

check("6. AND 1730 IS A LATTICE COMPUTATION, NOT A MEASUREMENT",
      True,
      "the 0++ glueball has never been unambiguously observed; f_0(1710) is a candidate that MIXES "
      "with q-qbar states. This is a computation-to-computation comparison and cannot carry the tier "
      "an experimental match would. I-tier is right -- and I would put the word 'lattice' IN the "
      "claim line so no referee mistakes it for data.")

print("\n" + "=" * 92)
print("SCORE: %d/%d   four false neighbours, not one; sharpen to marginal + asymptotically free;"
      % (sum(tests), len(tests)))
print("       and the glueball agreement is guaranteed by the grid -- the content is c_2 = 11.")
print("=" * 92)
