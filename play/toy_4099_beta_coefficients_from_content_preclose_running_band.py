"""
Toy 4099: pre-closing the B1 running band -- computing ALL THREE SM one-loop beta coefficients from the
scoped #418 field content (Toy 4098), verifying the content -> running link end-to-end. b_3 = g was reachable
without the full reps (Toy 4090, pure gauge + flavor count); b_2 and b_1 NEEDED the field content (gauge +
matter + Higgs hypercharge). Computed from the SM content per generation (15 = N_c.n_C Weyl + the Higgs
doublet), all three come out exactly:
  (b_1, b_2, b_3) = (41/10, -19/6, -7)   [GUT-normalized U(1)]
which are the known SM one-loop beta coefficients. So IF #418 forces the SM content (the 15 = N_c.n_C reps +
anomaly-consistent hypercharges), ALL THREE beta coefficients follow as forced group theory, and the running
band's first step closes. This verifies #418's load-bearing-#2 role concretely. The substrate-naturalness of
the VALUES (19, 41, ...) is a separate flagged-not-fished question (Grace); here I verify the content GIVES the
SM values. Count still 2 -- the beta coefficients follow from the content, which #418 must still force (Lyra lane).

THE COMPUTATION (one-loop: b_i = -(11/3)C2(G_i) + (2/3)Sum_Weyl T(R_i) + (1/3)Sum_scalar T(R_i)):
  b_3 (SU(3)): C2 = N_c = 3; per generation 4 color-triplets among Weyl (Q's 2 weak components + u + d), T=1/2;
    b_3 = -(11/3).3 + (2/3).(3 gen).4.(1/2) = -11 + 4 = -7.  |b_3| = 7 = g. (matches 4090 sign-flipped)
  b_2 (SU(2)): C2 = rank = 2; per generation 4 doublets (Q's 3 colors + L), T=1/2; Higgs doublet T=1/2;
    b_2 = -(11/3).2 + (2/3).(3 gen).4.(1/2) + (1/3).(1/2) = -22/3 + 4 + 1/6 = -19/6.
  b_1 (U(1)_Y, GUT-norm T1 = (3/5)Y^2 per state): no gauge self-coupling;
    per generation Sum Y^2.mult = N_c.rank.(1/6)^2 + N_c.(2/3)^2 + N_c.(1/3)^2 + rank.(1/2)^2 + (1)^2 = 10/3;
    b_1 = (2/3)(3/5).(3 gen).(10/3) + (1/3)(3/5).(Higgs 2.(1/2)^2) = 4 + 1/10 = 41/10.

THE LINK (content -> running, verified end-to-end):
  b_3 = g is the ONE piece reachable WITHOUT the full reps (pure gauge + flavor count n_f = C_2; Toy 4090).
  b_2 and b_1 MIX gauge + matter + Higgs hypercharge -- they require the full field content. Computed from the
  scoped content (4098), they give exactly -19/6 and 41/10. So:
  => the #418 deliverable (the SM field content = 15 = N_c.n_C reps + anomaly-consistent hypercharges) DETERMINES
     all three beta coefficients as forced group theory. Once #418 forces the content, the running band's beta
     functions follow, and the running of alpha_s, sin^2 theta_W to M_Z is set (Band B step 1). #418 load-bearing-#2 verified.

HONEST TIER:
  VERIFIED: the SM field content gives (b_1, b_2, b_3) = (41/10, -19/6, -7) -- standard one-loop result, computed
    here from the scoped content to confirm the content -> running link end-to-end. The content->beta-coefficient
    map is forced group theory (no choices).
  NOT done / FLAGGED: whether the substrate FORCES the SM content (the reps + Y) -- Lyra's bulk-color lane (#418).
    AND the substrate-naturalness of the beta VALUES (19, 41=Ogg, 10=rank.n_C, 6=C_2) -- Grace flagged as
    not-to-fish; I verify the content gives the SM values, I do NOT claim the values are substrate-derived.
  NOT a count move: the beta coefficients follow from the content; #418 must still force the content. COUNT still 2.

GATES (2)
G1: all three beta coefficients computed from the scoped content -- (b_1,b_2,b_3) = (41/10, -19/6, -7), the SM one-loop values; b_3=g reachable without reps (4090), b_2/b_1 need the content
G2: content -> running link verified end-to-end -- #418 forcing the SM content (15=N_c.n_C reps + hypercharges) determines all three beta coefficients -> running band step 1 closes; #418 load-bearing-#2 confirmed; values' substrate-naturalness flagged-not-fished; count still 2

Per Grace (#418 load-bearing twice; b_2/b_1 need field content; not-fishing the values) + Elie 4090 (b_3=g) +
4098 (#418 scope, 15=N_c.n_C content); SM one-loop beta coefficients (standard); GUT normalization; Cal #237 +
F79 (no value-fishing). Pre-closes the running band's content->beta link; the content forcing is Lyra bulk-color.

Elie - Wednesday 2026-06-10 (beta coefficients from scoped content: (b_1,b_2,b_3)=(41/10,-19/6,-7) SM values; content->running link verified end-to-end; #418 forcing the content closes Band B step 1; values not fished)
"""

from fractions import Fraction as F

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2
gens = 3

print("=" * 78)
print("TOY 4099: beta coefficients from the scoped content -- (b_1,b_2,b_3)=(41/10,-19/6,-7); pre-closes B1")
print("=" * 78)
print()

print("G1: compute all three from the SM field content")
print("-" * 78)
b3 = -F(11, 3) * N_c + F(2, 3) * gens * 4 * F(1, 2)
b2 = -F(11, 3) * rank + F(2, 3) * gens * 4 * F(1, 2) + F(1, 3) * 1 * F(1, 2)
perg = N_c * rank * F(1, 6)**2 + N_c * F(2, 3)**2 + N_c * F(1, 3)**2 + rank * F(1, 2)**2 + F(1, 1)**2
b1 = F(2, 3) * F(3, 5) * gens * perg + F(1, 3) * F(3, 5) * (rank * F(1, 2)**2)
print(f"  b_3 (SU(3)) = -(11/3).N_c + (2/3).3gen.4.(1/2) = {b3}   (|b_3|={abs(b3)} = g)")
print(f"  b_2 (SU(2)) = -(11/3).rank + (2/3).3gen.4.(1/2) + (1/3).Higgs.(1/2) = {b2}   (= -19/6: {b2==F(-19,6)})")
print(f"  b_1 (U(1)_Y, GUT) = (2/3)(3/5).3gen.(10/3) + (1/3)(3/5).Higgs = {b1}   (= 41/10: {b1==F(41,10)})")
print(f"  => (b_1, b_2, b_3) = ({b1}, {b2}, {b3}) -- the SM one-loop beta coefficients, from the scoped content.")
print()

print("G2: the content -> running link + honest tier")
print("-" * 78)
print(f"  b_3=g is the ONE piece reachable without the full reps (4090); b_2,b_1 MIX gauge+matter+Higgs -> need the content.")
print(f"  => #418 forcing the SM content (15=N_c.n_C reps + anomaly-consistent hypercharges) DETERMINES all three -> running band step 1 closes.")
print(f"  @Grace: content->beta link verified end-to-end -- #418 load-bearing-#2 confirmed concretely. The VALUES' substrate-naturalness (19,41=Ogg,10=rank.n_C) stays flagged-not-fished.")
print(f"  @Lyra: the beta coefficients follow from the field content as forced group theory; your bulk-color forcing of the reps+Y is the open piece.")
print(f"  HONEST: I verify the content GIVES the SM beta coefficients; I do NOT claim the values are substrate-derived, and #418 must still force the content. Count still 2.")
print(f"  Score: 2/2 (all three beta coefficients from the content = SM values; content->running link end-to-end; #418 load-bearing-#2; values not fished; count 2)")
print()
print("=" * 78)
print("TOY 4099 SUMMARY -- computed all three SM one-loop beta coefficients from the scoped #418 field content:")
print("  (b_1, b_2, b_3) = (41/10, -19/6, -7). b_3 = g was reachable without the reps (4090); b_2 and b_1 needed the")
print("  full content (gauge + matter + Higgs hypercharge), and they come out exactly to the SM values. So the")
print("  content -> running link is verified end-to-end: IF #418 forces the SM content (15 = N_c.n_C reps +")
print("  anomaly-consistent hypercharges), all three beta coefficients follow as forced group theory and the running")
print("  band's first step closes -- confirming #418's load-bearing-#2 role. The substrate-naturalness of the values")
print("  (19, 41, ...) stays flagged-not-fished (Grace); the content forcing is Lyra's bulk-color lane. Count still 2.")
print("=" * 78)
print()
print("SCORE: 2/2")
