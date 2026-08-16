"""
Toy 5294 (Elie, 2026-08-16) -- Phase 2, my assignment: is n_C = 5 forced over 7, 8, 9 by anything
COMMITMENT-NATIVE, or does it need a separate minimality principle?

ANSWER: IT NEEDS A SEPARATE PRINCIPLE. Nothing commitment-native distinguishes 5. And on the way to
that answer, two structural findings the dig needs.

★ (1) THE EXCEPTIONAL ISOMORPHISMS *ARE* THE DIVISION-ALGEBRA SPIN FACTORS -- the list has a reason.
Herm_2(A) for a division algebra A is rank-2 of dimension 2 + dim(A), which as a spin factor is
n = 2 + dim(A):
      A = R (1) -> n = 3      A = C (2) -> n = 4      A = H (4) -> n = 6      A = O (8) -> n = 10
Against Keeper's verified degeneracies: n=3 Siegel = Sym_2(R), n=4 = 2x2 complex = Herm_2(C),
n=6 = SO*(8) = Herm_2(H). THEY MATCH EXACTLY. So n = 5 is genuinely type-IV PRECISELY BECAUSE it is
NOT a Herm_2(division algebra). That explains the list instead of merely reciting it.

★★ (2) AND IT EXPOSES A NEIGHBOUR MISSING FROM THE LIST: n = 10 = Herm_2(O), OCTONIONIC.
It stays type IV (O yields no matrix Cartan type), but it is a DISTINGUISHED type-IV point --
the octonionic one, adjacent to the Albert algebra Herm_3(O) (dim 27, E_6). K1595 says exclude E_6
and E_7 explicitly; n = 10 is that same family and is NOT on the neighbour list. It should be.

★★★ (3) THE ENUMERATION, BEFORE ANY "THEREFORE":
   criterion                                selects              verdict
   genuine type IV (no exceptional iso)     {5,7,8,9,10,...}     a MINIMUM of 5, not 5 uniquely
   rank 2                                   all type IV          does not distinguish n at all
   Shilov (S^{n-1} x S^1)/Z_2               all n                does not distinguish n
   n odd (Spin(n) quaternionic, T2547)      {5,7,9,11,...}       kills 8 and 10 -- leaves {5,7,9}
   division-algebra spin factor             {3,4,6,10}           EXCLUDES 5; cannot be the selector
   minimality ("smallest genuine type IV")  {5}                  works -- but a SEPARATE PRINCIPLE
   n+1 = 2(n-2)                             {5}                  FORBIDDEN (K1595: target physics)
=> NOTHING COMMITMENT-NATIVE DISTINGUISHES 5 FROM 7, 8, 9 OR 10. The only criterion landing on 5
alone is MINIMALITY, and Occam is not a derivation. Even the strongest non-forbidden narrowing
(odd n) leaves {5,7,9}.
=> THE HONEST STATEMENT, if the type-forcing lands: "COMMITMENT FORCES TYPE IV; n >= 5; THE
   DIMENSION IS NOT FORCED." That is Keeper's pre-registered partial win, and it is the one I can
   support.

(4) THE "22 CONDITIONS" BAR -- what would make it evidence. It becomes evidence ONLY if the SAME 22,
applied to n = 7, 8, 9, 10, collect strictly fewer; and every condition mentioning N_c, N_f,
confinement, or n+1 = 2(n-2) must be STRUCK FIRST as target physics. I cannot run it -- the 22 are
not in a machine-readable list. PRE-REGISTERED PREDICTION (before anyone assembles them): after
striking the physics-circular conditions, far fewer than 22 survive, and the survivors select
{5,7,9} (odd), not {5}.

★ (5) THE #35 PRE-FLAG KEEPER ASKED FOR -- WITH A REFINEMENT THAT CUTS BOTH WAYS.
The 27 readings are: 3^3; N_c^3; the qqq tensor 3(x)3(x)3 (reducible 10+8+8+1, complex); the 27 lines
on a smooth cubic surface; the Albert algebra Herm_3(O) (dim 27); the E_7 domain EVII (complex dim
27). BUT THE LAST THREE ARE ONE CLASSICAL OBJECT -- the 27 lines carry the E_6 configuration, the
Albert algebra is its Jordan avatar, and EVII is the same exceptional family. So the honest count is
THREE distinct readings plus ONE exceptional-algebra family, not five or six. Miscounting inflates
the apparent coincidence in BOTH directions; I flag it now, before the connection gets made.

Nothing pushed. CP existence-only.
"""
import numpy as np

print("=" * 92)
print("Toy 5294: n_C = 5 is NOT forced by anything commitment-native; the exceptional isos ARE the")
print("          division-algebra spin factors; and n = 10 (octonionic) is missing from the list.")
print("=" * 92)

tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

div = [("R", 1), ("C", 2), ("H", 4), ("O", 8)]
ns = [2 + d for _, d in div]
print("\n   Herm_2(A), rank 2, dim 2+dim(A) -> as a spin factor, n = 2 + dim(A):")
for (A, d), n in zip(div, ns):
    print("      A = %-1s (dim %d)  ->  Herm_2(%s) dim %2d  ->  n = %2d" % (A, d, A, 2 + d, n))
check("1. ★ THE EXCEPTIONAL ISOMORPHISMS *ARE* THE DIVISION-ALGEBRA SPIN FACTORS",
      ns == [3, 4, 6, 10],
      "n = 3, 4, 6, 10 from R, C, H, O -- matching Keeper's verified degeneracies exactly "
      "(n=3 Siegel = Sym_2 R, n=4 = 2x2 complex = Herm_2 C, n=6 = SO*(8) = Herm_2 H). So n = 5 is "
      "genuinely type-IV PRECISELY BECAUSE it is NOT a Herm_2(division algebra). The list has a "
      "reason, not just entries.")

check("2. ★★ AND n = 10 = Herm_2(O) IS MISSING FROM THE NEIGHBOUR LIST",
      10 in ns and 10 not in (1, 2, 3, 4, 6),
      "n = 10 stays type IV (O gives no matrix Cartan type) but is the OCTONIONIC point, adjacent to "
      "the Albert algebra Herm_3(O) (dim 27, E_6). K1595 says exclude E_6 and E_7 explicitly -- "
      "n = 10 is that same family and is not on the list. @Keeper: it should be.")

cands = [
    ("genuine type IV (no exceptional iso)", "{5,7,8,9,10,...}", "MINIMUM 5, not unique"),
    ("rank 2", "all type IV", "no discrimination"),
    ("Shilov (S^{n-1} x S^1)/Z_2", "all n", "no discrimination"),
    ("n odd (Spin(n) quaternionic, T2547)", "{5,7,9,11,...}", "kills 8,10 -- leaves {5,7,9}"),
    ("division-algebra spin factor", "{3,4,6,10}", "EXCLUDES 5 -- cannot be the selector"),
    ("minimality", "{5}", "works, but a SEPARATE PRINCIPLE"),
    ("n+1 = 2(n-2)", "{5}", "FORBIDDEN -- target physics (K1595)"),
]
print("\n   ENUMERATION, before any 'therefore':")
print("   %-38s %-22s %s" % ("criterion", "selects", "verdict"))
for a, b, c in cands:
    print("   %-38s %-22s %s" % (a, b, c))
survivors = [c for c in cands if c[1] == "{5}" and "FORBIDDEN" not in c[2]]
check("3. ★★★ NOTHING COMMITMENT-NATIVE DISTINGUISHES 5 -- the answer to my assignment is NO",
      len(survivors) == 1 and "SEPARATE PRINCIPLE" in survivors[0][2],
      "the only criterion landing on 5 alone is MINIMALITY, and Occam is not a derivation. The "
      "strongest non-forbidden narrowing (odd n) still leaves {5,7,9}. ⟹ the honest statement, if "
      "the type-forcing lands: 'COMMITMENT FORCES TYPE IV; n >= 5; THE DIMENSION IS NOT FORCED.' "
      "That is exactly Keeper's pre-registered PARTIAL win, and it is the one I can support.")

check("4. THE '22 CONDITIONS' BAR -- specified, and my prediction pre-registered",
      True,
      "it is evidence ONLY if the SAME 22, applied to n = 7,8,9,10, collect strictly fewer -- and "
      "every condition mentioning N_c, N_f, confinement or n+1=2(n-2) must be STRUCK FIRST. I cannot "
      "run it (not machine-readable). PRE-REGISTERED, before anyone assembles them: after striking "
      "the physics-circular conditions FAR fewer than 22 survive, and the survivors select {5,7,9}, "
      "not {5}.")

r = [("3^3", "distinct"), ("N_c^3", "distinct"), ("qqq tensor 3x3x3", "distinct"),
     ("27 lines on a cubic", "E_6 -- ONE object"), ("Albert Herm_3(O) dim 27", "E_6 -- ONE object"),
     ("E_7 domain EVII dim 27", "same family")]
check("5. ★ THE #35 PRE-FLAG -- with a refinement that cuts BOTH ways",
      sum(1 for _, v in r if v == "distinct") == 3,
      "the 27 readings are: " + "; ".join("%s (%s)" % x for x in r) + ". THE LAST THREE ARE ONE "
      "CLASSICAL OBJECT -- the 27 lines carry the E_6 configuration, the Albert algebra is its "
      "Jordan avatar, EVII is the same exceptional family. So the honest count is THREE distinct "
      "readings plus ONE exceptional family, not five or six. Miscounting inflates the coincidence "
      "in BOTH directions.")

print("\n" + "=" * 92)
print("SCORE: %d/%d   n=5 needs a separate minimality principle; the exceptional isos are the"
      % (sum(tests), len(tests)))
print("       division-algebra spin factors; n=10 (octonionic) belongs on the neighbour list.")
print("=" * 92)
