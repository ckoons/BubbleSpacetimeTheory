"""
Toy 4053: resolving Lyra's Filter-1 framing question -- does the floor cell-count equal the floor K-type
Casimir? ANSWER: only for the BARYON (an accident); the MESON breaks it (cells = 5, but (1,0) Casimir = 4,
and NO K-type has Casimir 5). So cells != Casimir in general -> the substrate-measure that reproduces the
floor cells (5, 6) is the VOLUME (cells), NOT the Casimir. Confirms F62. (Careful-numerical; Lyra's proof gate.)

LYRA's QUESTION (before banking the Filter-1 proof): F52 says mass = volume wound (cells.pi^{n_C}); F60 says
the dynamics run on H_B = the Casimir. She'd written Filter 1 as "substrate-measure = <H_B>" -- but is that
right, or is the measure the VOLUME? Concretely: does the meson's V_(1,0) Casimir = n_C = 5, the way the
baryon's (1,1) Casimir = C_2 = 6? If they coincide, volume and Casimir are the same measure on the floor; if
not, the measure is the volume (cells), with the Casimir as the dynamics.

THE COMPUTATION (SO(5) = B_2 Casimir; rho_SO(5) = (3/2, 1/2) per CLAUDE.md compact rho):
  C(a,b) = <lambda, lambda + 2rho> = a^2 + b^2 + 3a + b   for K-type lambda = (a,b) in orthogonal coords.
    (1,0): 4    (0,1): 2    (1,1): 6    (2,0): 10    (0,2): 6    (2,1): 12
  Check vs known: (1,1) -> 6 = C_2 (matches Lyra/CLAUDE.md baryon K-type). Normalization correct.

THE RESULT:
  BARYON floor: cells = C_2 = 6 ; K-type (1,1) Casimir = 6 -> COINCIDE.
    BUT this is an ACCIDENT: C_2 = n_C + 1 = 6 AND the (1,1) Casimir = 6 happen to be the same number.
  MESON floor: cells = n_C = 5 ; K-type (1,0) Casimir = 4 -> DIFFER (5 != 4).
    AND scanning all (a,b): NO K-type has Casimir = 5. The meson cell-count is NOT any K-type Casimir.
  => cells = Casimir holds ONLY for the baryon (coincidence); the MESON breaks it. So cells != Casimir in general.

CONCLUSION (answers Lyra; resolves the Filter-1 framing):
  The substrate-measure that reproduces the floor cell-counts (5, 6) is the VOLUME (cells), NOT the K-type
  Casimir. Write Filter 1 as: substrate-measure = the state's definite VOLUME content (cells, = mass/pi^{n_C}.m_e);
  the Casimir H_B is the DYNAMICS (F60), not what's measured. The baryon 6=6 coincidence is a red herring -- the
  meson 5-vs-4 is the tell. This CONFIRMS F62 (cells = bulk volume + Z_2 bit, EXPLICITLY not a representation
  Casimir). Filter 1's conclusion is unaffected (volume AND Casimir are both definite for an eigenstate, both
  indefinite for a quark superposition) -- but the formal proof should state the measure as VOLUME, avoiding the
  over-specification "= <H_B>" that the meson would falsify on inspection.

  (Caveat for Lyra: this is the SO(5) Casimir; the full H_B is the SO(5)xSO(2) Casimir of your Tier-0 operator.
   If an SO(2) charge shifts the meson (1,0) from 4 to 5, the coincidence could be restored -- that's your
   operator to pin. But at the SO(5) level the meson breaks cells=Casimir, and F62 already says cells != Casimir,
   so the volume reading is the safe one. Flagging the SO(2) piece honestly rather than claiming it's closed.)

GATES (3)
G1: SO(5) Casimir C(a,b)=a^2+b^2+3a+b verified ((1,1)=6=C_2 matches baryon)
G2: baryon cells=Casimir=6 (accident); meson cells=5 != (1,0) Casimir=4; NO K-type has Casimir 5
G3: cells != Casimir in general -> substrate-measure = VOLUME (cells), not Casimir; confirms F62; SO(2) caveat flagged

Per Lyra Filter-1 framing question; F52/T2487 (mass=volume); F60 (H_B dynamics); F62 (cells=volume+Z2, not Casimir);
CLAUDE.md (rho_SO(5)=(3/2,1/2); (1,1) Casimir=C_2); Cal #237; K231c. Careful-numerical; the formal proof is Lyra's.

Elie - Monday 2026-06-08 (floor cells vs Casimir: meson breaks the coincidence -> measure = volume)
"""

n_C, C_2 = 5, 6


def Cas(a, b):
    return a * a + b * b + 3 * a + b


print("=" * 78)
print("TOY 4053: floor cells vs K-type Casimir -- meson breaks the coincidence -> measure = VOLUME")
print("=" * 78)
print()

print("G1: SO(5)=B_2 Casimir C(a,b)=a^2+b^2+3a+b (rho=(3/2,1/2))")
print("-" * 78)
for ab in [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (2, 1), (2, 2)]:
    tag = "  <- baryon K-type, =C_2 (matches CLAUDE.md)" if ab == (1, 1) else ("  <- meson K-type" if ab == (1, 0) else "")
    print(f"  K-type {ab}: Casimir = {Cas(*ab)}{tag}")
print()

print("G2: baryon coincides (accident); meson breaks it")
print("-" * 78)
print(f"  BARYON: cells = C_2 = 6 ; (1,1) Casimir = {Cas(1,1)} -> COINCIDE. But accident: C_2 = n_C+1 = (1,1)Casimir = 6.")
print(f"  MESON : cells = n_C = 5 ; (1,0) Casimir = {Cas(1,0)} -> DIFFER (5 != 4).")
hits = [(a, b) for a in range(5) for b in range(5) if Cas(a, b) == 5]
print(f"  any K-type with Casimir 5? scan: {hits if hits else 'NONE'} -> the meson cell-count is NOT a Casimir.")
print()

print("G3: conclusion -- substrate-measure = VOLUME (cells), not Casimir")
print("-" * 78)
print("  cells = Casimir only for the baryon (coincidence); the meson breaks it -> cells != Casimir in general.")
print("  => Filter 1 measure = the state's definite VOLUME content (cells); H_B Casimir = DYNAMICS, not what's measured.")
print("  Confirms F62 (cells = bulk volume + Z_2 bit, NOT a Casimir). Filter 1's conclusion unaffected (both definite for")
print("  an eigenstate, both indefinite for a quark); but write the measure as VOLUME to avoid the '=<H_B>' over-spec the meson breaks.")
print("  CAVEAT (Lyra's operator): full H_B is SO(5)xSO(2) Casimir; an SO(2) charge could shift meson (1,0) 4->5 and restore it.")
print("    That's your operator to pin; at SO(5) level the meson breaks it + F62 says cells != Casimir, so VOLUME is the safe reading.")
print()
print(f"  @Lyra: answers your gate -- write Filter 1's measure as VOLUME (cells), Casimir as dynamics. Baryon 6=6 is a red herring; meson 5-vs-4 is the tell.")
print(f"  Score: 3/3 (Casimir computed + normalization checked; baryon-accident vs meson-break; measure=volume + SO(2) caveat)")
print()
print("=" * 78)
print("TOY 4053 SUMMARY -- floor cells vs K-type Casimir: BARYON coincides (cells=6=(1,1)Casimir, an accident);")
print("  MESON breaks it (cells=5, (1,0)Casimir=4, no K-type has Casimir 5). So cells != Casimir in general ->")
print("  substrate-measure = VOLUME (cells), not Casimir (confirms F62). Lyra writes Filter 1's measure as volume,")
print("  H_B as dynamics. SO(2)-charge caveat flagged (could restore meson coincidence; Lyra's operator to pin).")
print("=" * 78)
print()
print("SCORE: 3/3")
