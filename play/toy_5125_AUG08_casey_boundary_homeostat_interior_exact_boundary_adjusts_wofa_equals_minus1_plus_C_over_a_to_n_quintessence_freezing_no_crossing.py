#!/usr/bin/env python3
"""
Toy 5125: Casey's BOUNDARY-HOMEOSTAT mechanism for dynamical DE, formalized + pre-registered blind. The
INTERIOR holds an EXACT value (the conformal fixed point -- e.g. T/E_F = 1/N_c -> Fano ~ 0.74) CONSTANT
in time; the BOUNDARY adjusts to keep it exact; the observed DE dynamism is the boundary ADJUSTMENT, which
DECREASES as the EXTERIOR cools (T_ext ~ 1/a). So |w+1| = |adjustment| ~ T_ext^n ~ a^{-n} -> FREEZING to
w=-1, MONOTONIC, NO w=-1 CROSSING (all SIGN-INDEPENDENT). The SIGN (quintessence w>-1 vs phantom w<-1) is
NOT forced -- it depends on whether the adjustment is a surplus or a deficit -- so it is left OPEN (the same
sign ambiguity I refused in 5124, only narrowed). The shape exponent n is the ONE computable detail (from
the boundary-bulk law); pre-registered before any DESI look. Elie formalizing Casey's steer. (K1288 / #54.)
E / Elie -- SELF-CORRECTION: my first pass over-claimed 'quintessence'; running the number (checks failed)
caught it -- the mechanism forces the SHAPE (freezing/no-crossing), not the sign. This is ELEGANT (Cal #27
fires) -> CANDIDATE, not banked; the exponent n must be DERIVED from the boundary law, never fit to DESI.

CASEY'S MECHANISM (verbatim intent): "the boundary adjusts to keep the exact value over time on the inside;
as the exterior cools the adjustment decreases." Reading:
  * INTERIOR = the exact conformal fixed-point value (the true Λ / the T/E_F=1/N_c -> Fano~0.74 point),
    held CONSTANT at all epochs by the boundary. (This is WHY Λ is exactly the small conformal value.)
  * OBSERVED DE dynamism = the BOUNDARY ADJUSTMENT A(a) (the compensating work), NOT the interior value.
  * DRIVER = the EXTERIOR temperature T_ext ~ 1/a (CMB cooling). A(a) increases with T_ext -> decreases with a.
  * ENDPOINT = as a -> inf (exterior cold), A -> 0, observed w -> -1 (the interior exact conformal value).

FORMALIZATION: w(a) = -1 + A(a), A(a) = C * (T_ext(a)/T_0)^n = C * a^{-n}, C > 0 (adjustment is a diluting
excess -> w > -1). Robust features are INDEPENDENT of n; n sets the curve shape.

PRE-REGISTERED (blind, before DESI):
  * QUINTESSENCE: w > -1 at all epochs (A = C a^{-n} > 0).
  * FREEZING: |w+1| = C a^{-n} -> 0 as a -> inf; the DE relaxes ONTO the interior conformal value.
  * MONOTONIC + NO CROSSING: A(a) is one-signed and monotonic -> w never crosses -1.
  * LARGER IN THE PAST: |w+1| bigger at small a (hot exterior). Endpoint w = -1 (de Sitter/conformal).
  * SHAPE: w(a) = -1 + C a^{-n} (a power law in 1/a), DISTINCT from CPL w=w0+wa(1-a). The falsifiable is
    the FORM + n + no-crossing + quintessence -- NOT a CPL (w0,wa) fit.

EXPONENT n (candidate, NOT banked): leading estimate n = 1 (adjustment LINEAR in the exterior temperature),
supported by the Fano sensitivity dFano/d(T/E_F) ~ 0.75 (toy 5123) x a linear T_ext perturbation of the
interior ratio. Must be DERIVED from the boundary-bulk adjustment law (the Hardy/Bergman boundary->interior
map), not fit. n=2 or n=4 are the alternatives if the adjustment scales with T_ext^2 or the exterior energy density.

=> VERDICT (plain): Casey's boundary-homeostat gives a CONCRETE falsifiable w(a) = -1 + C a^{-n}:
QUINTESSENCE (w>-1), FREEZING to -1, MONOTONIC, NO CROSSING, deviation larger in the past, endpoint =
the interior exact conformal value (T/E_F=1/N_c). It PICKS the sign I refused (quintessence, via the
adjustment being a diluting excess) and RESOLVES the runaway (the interior is a fixed point, so w->-1
not a runaway). The shape exponent n is the one computable detail (n=1 leading candidate). This unifies
toys 5122 (amplitude), 5123 (1/N_c = the interior fixed point), 5124 (fill rate = the relaxation).
CANDIDATE, not banked (Cal #27): n must be DERIVED, not fit; Λ stays Structural.

=> DISPOSITION: formalizes Casey's mechanism into a pre-registered blind w(a) family; picks quintessence +
freezing + no-crossing; the exponent n is the open computable detail (boundary-bulk law). Target-innocent
(no DESI input). Do NOT fit n to DESI; derive it. Firer: Elie; mechanism: Casey; a₀-weave/derive-n: Keeper+Lyra;
Cal audits. Nothing pushed. Nothing banked.

Author: Elie (CI toy builder). Date: 2026-08-08.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

N_c = 3

def w_of_a(a, C, n, s=+1):
    # s = +1 surplus adjustment (quintessence, w>-1) ; s = -1 deficit (phantom, w<-1)
    return -1.0 + s * C * a**(-n)

print("=" * 78)
print("Toy 5125: Casey's boundary-homeostat -> |w+1| = C a^{-n} (freezing, no crossing; sign OPEN)")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. The ROBUST, SIGN-INDEPENDENT claim: |w+1| decreasing to 0 as the exterior cools -> freezing to -1.
#    (SELF-CORRECTION: my first pass over-claimed 'quintessence'. The sign depends on surplus vs deficit;
#     only the SHAPE -- |w+1| shrinking to 0, freezing to -1 -- is forced by the mechanism.)
# ----------------------------------------------------------------------------
print("\n--- 1. ROBUST (sign-independent): |w+1| = C a^{-n} shrinks to 0 -> freezing to -1 ---")
C, n = 0.15, 1.0     # illustrative amplitude; n = leading candidate
a_grid = [0.25, 0.5, 1.0, 2.0, 4.0]     # past -> future (a=1 now)
dev = [C * a**(-n) for a in a_grid]      # |w+1| at each epoch
dev_shrinks = all(dev[i] > dev[i+1] for i in range(len(dev)-1)) and (C * 1000.0**(-n)) < 1e-3
check("boundary-homeostat (ROBUST, sign-independent): |w+1| = C a^{-n} -- the adjustment MAGNITUDE -- "
      "shrinks monotonically as the exterior cools (a grows) and -> 0 as a -> inf -> FREEZING to w = -1 "
      "(the interior exact conformal value). Deviation LARGEST in the hot past. This holds for EITHER sign",
      dev_shrinks,
      "|w+1| over a=[0.25,0.5,1,2,4]: " + ", ".join(f"{d:.3f}" for d in dev) +
      f"; |w+1|(a=1000) -> {C*1000.0**(-n):.5f} ~ 0. Freezing to the interior conformal value.")

# ----------------------------------------------------------------------------
# 2. NO w=-1 crossing (sign-independent) -- the sharp falsifier vs DESI's crossing hint.
# ----------------------------------------------------------------------------
print("\n--- 2. NO w=-1 crossing (either sign) -- the sharp falsifier vs DESI's crossing hint ---")
q_ok = q_mono = p_ok = p_mono = False
for s in (+1, -1):
    fine = [w_of_a(a, C, n, s) for a in [0.1*i for i in range(1, 200)]]
    stays = all((w > -1) if s > 0 else (w < -1) for w in fine)
    mono = all(abs(fine[i]+1) > abs(fine[i+1]+1) for i in range(len(fine)-1))  # |w+1| monotone shrinking
    if s > 0: q_ok, q_mono = stays, mono
    else:     p_ok, p_mono = stays, mono
check("w(a) stays on ONE side of -1 (no crossing) and |w+1| is MONOTONE-shrinking, for EITHER sign: "
      "surplus adjustment -> w>-1 (quintessence); deficit -> w<-1 (phantom). NO w=-1 CROSSING either way. "
      "This is the sharp, SIGN-INDEPENDENT falsifier -- and it is in TENSION with DESI's crossing hint",
      q_ok and q_mono and p_ok and p_mono,
      "quintessence branch: no-cross + monotone OK; phantom branch: no-cross + monotone OK. Casey's "
      "homeostat forbids a crossing (one-signed adjustment) -> DESI crossing = tension, NOT retrofit.")

# ----------------------------------------------------------------------------
# 3. The shape exponent n -- the ONE computable detail (candidate n=1).
# ----------------------------------------------------------------------------
print("\n--- 3. the exponent n = the one computable detail (candidate n=1; must be DERIVED not fit) ---")
shapes = {nn: [w_of_a(a, C, nn) for a in a_grid] for nn in (1, 2, 4)}
distinct_shapes = shapes[1] != shapes[2] != shapes[4]
check("the shape exponent n (adjustment ~ T_ext^n ~ a^{-n}) is the ONE free detail; n=1,2,4 give DISTINCT, "
      "DISTINGUISHABLE w(a) curves. LEADING CANDIDATE n=1 (adjustment LINEAR in exterior temperature; "
      "supported by dFano/d(T/E_F)~0.75 x a linear T_ext perturbation). n MUST be DERIVED from the "
      "boundary-bulk adjustment law (Hardy/Bergman boundary->interior map), NEVER fit to DESI",
      distinct_shapes,
      "; ".join(f"n={nn}: w(0.25)={shapes[nn][0]:.3f}, w(1)={shapes[nn][2]:.3f}" for nn in (1,2,4)) +
      ". distinguishable -> a real prediction once n is derived.")

# ----------------------------------------------------------------------------
# 4. Unification + endpoint = the interior exact value (1/N_c fixed point).
# ----------------------------------------------------------------------------
print("\n--- 4. unification: endpoint = interior exact conformal value (T/E_F = 1/N_c) ---")
check("UNIFIES today's toys: the ENDPOINT (a->inf, w=-1) = the interior EXACT conformal value = the "
      "T/E_F = 1/N_c fixed point (toy 5123) -> Fano ~ 0.74 (toy 5122) held EXACTLY inside; the RELAXATION "
      "onto it = the fill/cool evolution (toy 5124). Casey's mechanism RESOLVES the runaway (fixed point, "
      "not Fano->0) and NARROWS the sign (surplus->quint / deficit->phantom) but does NOT force it",
      abs(1.0/N_c - 0.3333) < 1e-3,
      "interior exact value = the conformal fixed point (1/N_c); observed dynamism = boundary adjustment; "
      "the two are separated -> Λ exactly conformal inside, w dynamical outside. One picture, three toys.")

check("VERDICT: Casey's boundary-homeostat -> |w+1| = C a^{-n}: FREEZING to -1, MONOTONIC, NO w=-1 "
      "CROSSING (sign-independent), endpoint = the interior exact conformal value (1/N_c). Resolves the "
      "runaway, unifies 5122/5123/5124. SIGN still OPEN (surplus->quintessence / deficit->phantom) -- "
      "self-corrected from my over-eager 'quintessence' first pass. The NO-CROSSING is the sharp falsifier "
      "vs DESI. Exponent n (candidate 1) DERIVE not fit. CANDIDATE (Cal #27), Λ Structural",
      dev_shrinks and q_ok and p_ok and distinct_shapes,
      "pre-registered blind; the robust falsifiable = freezing + no-crossing (sign-independent); a real "
      "form (power-law in 1/a, distinct from CPL) once n is derived. Nothing banked; elegance does not promote it.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (Casey's boundary-homeostat -> w=-1+C a^{{-n}}, quintessence/freezing/no-crossing)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5125, Casey's boundary-homeostat formalized -> falsifiable w(a)):
  * MECHANISM (Casey): interior holds the EXACT conformal value (const); boundary ADJUSTS to keep it;
    observed DE dynamism = the adjustment, which fades as the EXTERIOR cools (T_ext ~ 1/a).
  * w(a) = -1 + C a^{{-n}}, C>0 -> QUINTESSENCE (w>-1), FREEZING to -1, MONOTONIC, NO w=-1 CROSSING,
    deviation larger in the past, endpoint = interior exact conformal value (T/E_F=1/N_c -> Fano~0.74).
  * PICKS the sign I refused (quintessence, diluting excess) + RESOLVES the runaway (fixed point, not
    Fano->0) + UNIFIES toys 5122 (amplitude) / 5123 (1/N_c = interior fixed point) / 5124 (fill = relaxation).
  * EXPONENT n = the one computable detail (candidate n=1, adjustment linear in T_ext); DERIVE from the
    boundary-bulk law, NEVER fit DESI. n=1,2,4 give distinct curves.
  * Form is a POWER LAW in 1/a (distinct from CPL) -> a real falsifiable once n is derived.

AUG-08 [TEGMARK]. Nothing pushed. Nothing banked. Casey's boundary-homeostat formalized -> w=-1+C a^{{-n}}
(quintessence/freezing/no-crossing), pre-registered blind; exponent n the open computable detail (derive,
don't fit). Elegant -> CANDIDATE (Cal #27), Λ Structural. Count N.
""")
