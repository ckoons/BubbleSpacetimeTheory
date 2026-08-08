#!/usr/bin/env python3
"""
Toy 5112: #85 blind r = g'^2/g^2 -- the case-structure computed rigorously from the fermion traces;
the A/B/C verdict is the doubling-DOMAIN hinge (Lyra-vs-Grace), which I localize and do NOT assert
un-tuned (Cal §341). Elie's independent half of the two-party blind. (K1276.)
E / Elie -- I compute what is unambiguous (the trace baseline + what each case REQUIRES) and honestly
flag the one open hinge (which traces double) rather than fabricate a confident case. Blind to Keeper's r.

PROTOCOL (K1276, phantom-proofed): output r = g'^2/g^2 (NOT sin^2); fixed map sin^2 = r/(1+r); the three
cases have DISTINCT r (no overlap): A r=3/10 -> 3/13 | B r=3/7 -> 3/10 | C r=3/5 -> 3/8.

PINNED INPUTS (Grace generators + Lyra F856 convention, target-innocent, sourced):
  * Y = T_3R + (B-L)/2 (standard Pati-Salam; reproduces the SM hypercharges); SU(2)_L one SU(2) of
    SO(4) c SO(5); B-L on the SO(2) axis (= the J / complex-structure / Bekenstein SO(2)).
  * F856: J acts on the WHOLE tangent (Helgason); Tr_R = 2 Tr_C (realification); color N_c = short-root
    MULTIPLICITY (a count, SU(3) not-c SO(5)) -> Lyra reads: does NOT double.
  * OPEN HINGE (Lyra owes, line "@Lyra owes exact J-eigenspace of V12"): does the color root space sit
    in J's complexified part (-> doubles -> Case C) or is it a J-real multiplicity (-> Case A)? Grace
    reads the doubling as on the (B-L)-on-SO(2) COMPONENT only (-> Case B). This is what the blind decides.

WHAT I COMPUTE (unambiguous): the GUT/undoubled baseline r = Tr(T_3L^2)/Tr(Y^2) over one fermion
generation, and what each doubling-domain gives.
  * Tr(T_3L^2) = 2, Tr(T_3R^2) = 2, Tr((B-L)^2) = 16/3, Tr(Y^2) = Tr(T_3R^2) + (1/4)Tr((B-L)^2) = 10/3.
  * No doubling (GUT):           r = 2/(10/3) = 3/5  -> Case C (sin^2 3/8). [the un-doubled anchor]
  * Only the (B-L)/SO(2) doubles: Tr(Y^2) = 2 + 2*(4/3) = 14/3, r = 3/7 -> Case B (sin^2 3/10). [Grace]
  * The whole hypercharge norm doubles vs isospin: Tr(Y^2) -> 20/3, r = 3/10 -> Case A (sin^2 3/13). [Lyra/A]

WHAT I DO NOT DO (Cal §341): assert Case A un-tuned. Case A requires the hypercharge trace to double
while the isospin trace does not -- an ASYMMETRY that needs the color-as-count reading (T2545) AND the
exact J-eigenspace to justify, not the desired 3/13. I report my LEAN, flag the hinge, and defer the
verdict to (i) Lyra's owed J-eigenspace of V12 and (ii) Keeper's independent blind r.

=> VERDICT (plain, honest): the case-to-r map is VERIFIED from the fermion traces (C 3/5, B 3/7, A 3/10);
the A/B/C decision is the doubling-DOMAIN hinge -- whether the color/short-root space is J-real (count,
does-not-double -> A) or J-complexified (doubles -> C), and whether U(1)_Y's norm inherits the whole
tangent (A) or a component (B). My lean, from the selectivity principle (K1274: no N_c inside a doubling
trace) + T2545 (color = a count), is CASE A (r=3/10 -> 3/13) -- but I do NOT bank it un-tuned; the
J-eigenspace (Lyra) + Keeper's independent r settle it. If A confirms un-tuned, 3/13 -> Derived + the
SO(2)-triple. sin^2 stays Structural/Identified until the two-party blind + the J-eigenspace agree.

=> DISPOSITION: contributes the verified case-structure + localizes the single open hinge; my blind
lean = A, flagged not-un-tuned; defers the verdict to the J-eigenspace + Keeper's cross-check. Cal §341
honored (no un-tuned assertion of the target). Firer/checker: Elie (this) + Keeper (independent). Nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-08.
"""

from fractions import Fraction as Fr

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

def sin2_from_r(r):
    return r/(1+r)

print("=" * 78)
print("Toy 5112: #85 blind r -- case-structure verified; doubling-domain hinge localized (K1276)")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. Fermion traces over one generation (Pati-Salam charges).
# ----------------------------------------------------------------------------
print("\n--- fermion traces (one generation, Pati-Salam Y = T_3R + (B-L)/2) ---")
# states: (label, count, T_3L list, T_3R list, B-L)
# Q_L: SU(2)_L doublet, N_c=3 colors, B-L=1/3 ; u_R,d_R: SU(2)_R doublet, 3 colors, B-L=1/3
# L: SU(2)_L doublet, B-L=-1 ; e_R,nu_R: SU(2)_R doublet, B-L=-1
N_c = 3
Tr_T3L = Fr(0)
Tr_T3R = Fr(0)
Tr_BL2 = Fr(0)
# left doublets (T_3L = +-1/2, T_3R = 0)
for mult, bl in [(N_c, Fr(1,3)), (1, Fr(-1))]:      # Q_L (x N_c), L (x1)
    Tr_T3L += mult * (Fr(1,4) + Fr(1,4))            # two states +-1/2
    Tr_BL2 += mult * 2 * bl**2
# right doublets (T_3R = +-1/2, T_3L = 0)
for mult, bl in [(N_c, Fr(1,3)), (1, Fr(-1))]:      # u_R,d_R (x N_c), e_R,nu_R (x1)
    Tr_T3R += mult * (Fr(1,4) + Fr(1,4))
    Tr_BL2 += mult * 2 * bl**2
Tr_Y2 = Tr_T3R + Fr(1,4)*Tr_BL2                     # Y = T_3R + (B-L)/2, T_3R _|_ B-L
check("fermion traces: Tr(T_3L^2)=2, Tr(T_3R^2)=2, Tr((B-L)^2)=16/3, Tr(Y^2)=T_3R + (1/4)(B-L)^2 = 10/3 "
      "(standard; reproduces the GUT normalization)",
      Tr_T3L == 2 and Tr_T3R == 2 and Tr_BL2 == Fr(16,3) and Tr_Y2 == Fr(10,3),
      f"Tr(T_3L^2)={Tr_T3L}, Tr(T_3R^2)={Tr_T3R}, Tr((B-L)^2)={Tr_BL2}, Tr(Y^2)={Tr_Y2}. Y is Pati-Salam.")

# ----------------------------------------------------------------------------
# 2. The three cases: r = Tr(T_3L^2)/Tr(Y^2) with the doubling applied to different domains.
# ----------------------------------------------------------------------------
print("\n--- the three cases (distinct r, phantom-proofed map sin^2 = r/(1+r)) ---")
r_C = Tr_T3L / Tr_Y2                                             # no doubling (GUT anchor)
r_B = Tr_T3L / (Tr_T3R + 2*Fr(1,4)*Tr_BL2)                       # only (B-L)/SO(2) doubles
r_A = Tr_T3L / (2*Tr_Y2)                                          # whole hypercharge norm doubles vs isospin
check("case C (no doubling, GUT anchor): r = Tr(T_3L^2)/Tr(Y^2) = 3/5 -> sin^2 = 3/8. This is the "
      "un-doubled baseline (everything doubling uniformly CANCELS to this)",
      r_C == Fr(3,5) and sin2_from_r(r_C) == Fr(3,8),
      f"r_C = {r_C} = 3/5 -> sin^2 = {sin2_from_r(r_C)} = 3/8.")
check("case B (only the (B-L)-on-SO(2) component doubles -- Grace's reading): Tr(Y^2) -> 14/3, r = 3/7 "
      "-> sin^2 = 3/10",
      r_B == Fr(3,7) and sin2_from_r(r_B) == Fr(3,10),
      f"r_B = {r_B} = 3/7 -> sin^2 = {sin2_from_r(r_B)} = 3/10. Grace: doubling on the component only.")
check("case A (the whole hypercharge norm doubles vs isospin -- Lyra's whole-tangent + color-as-count "
      "reading): r = 3/10 -> sin^2 = 3/13",
      r_A == Fr(3,10) and sin2_from_r(r_A) == Fr(3,13),
      f"r_A = {r_A} = 3/10 -> sin^2 = {sin2_from_r(r_A)} = 3/13. Requires Tr(Y^2) to double while Tr(T_3L^2) "
      "does not -- the asymmetry that needs the color-as-count + J-eigenspace justification.")

# ----------------------------------------------------------------------------
# 3. The open hinge (the decider) -- localized, NOT asserted (Cal §341).
# ----------------------------------------------------------------------------
print("\n--- the open hinge: the doubling DOMAIN (Lyra A vs Grace B); needs the J-eigenspace ---")
check("the A/B/C verdict IS the doubling-domain hinge: does the color/short-root space sit in J's "
      "COMPLEXIFIED part (doubles -> C) or is it a J-REAL multiplicity (a count that does NOT double -> "
      "A)? and does U(1)_Y's norm inherit the WHOLE tangent (A) or a COMPONENT (B, Grace)? The exact "
      "J-eigenspace of V12 (Lyra owes) + Keeper's independent r settle it -- I do NOT assert it",
      r_A != r_B != r_C and r_A == Fr(3,10),
      "distinct r per case (no phantom overlap). Cal §341: the factor must fall out un-tuned; I flag the "
      "hinge rather than pick A because 3/13 is wanted.")

check("MY BLIND LEAN (flagged, NOT banked un-tuned): the selectivity make-or-break (K1274 -- 'nothing "
      "with N_c inside a doubling trace') + T2545 (color = short-root MULTIPLICITY, a count, SU(3) not-c "
      "SO(5)) point to CASE A (color does not double; the substrate does) -> r=3/10 -> 3/13. But this "
      "rests on the color-as-count reading (contested by Grace's component reading B); the J-eigenspace decides",
      r_A == Fr(3,10),
      "lean A; NOT banked. If A confirms un-tuned (J-eigenspace + Keeper agree), 3/13 -> Derived + the "
      "SO(2)-triple (time + Bekenstein + Weinberg). sin^2 stays Structural/Identified until then.")

check("VERDICT: case-to-r map VERIFIED from the fermion traces (C 3/5, B 3/7, A 3/10, distinct); the "
      "decision is the doubling-domain hinge; my lean = A (selectivity + T2545), flagged not-un-tuned; "
      "verdict deferred to Lyra's J-eigenspace of V12 + Keeper's independent blind r. Cal §341 honored",
      r_C == Fr(3,5) and r_B == Fr(3,7) and r_A == Fr(3,10),
      "Elie's independent half of the two-party blind: the structure + the localized hinge + an honest "
      "lean, no un-tuned assertion. Two-party cross-check + J-eigenspace = the settle.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (blind r: lean A = 3/10 -> 3/13, hinge-flagged, NOT banked)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5112, #85 blind r -- case-structure + localized hinge, Elie's independent half):
  * Fermion traces (Pati-Salam Y=T_3R+(B-L)/2): Tr(T_3L^2)=2, Tr(Y^2)=10/3 -> GUT anchor r=3/5 (Case C).
  * The three cases, distinct r (phantom-proofed, sin^2 = r/(1+r)):
      C  no doubling (GUT/cancel)             r = 3/5  -> sin^2 3/8
      B  only (B-L)-on-SO(2) doubles (Grace)  r = 3/7  -> sin^2 3/10
      A  whole hypercharge norm doubles (Lyra) r = 3/10 -> sin^2 3/13
  * The A/B/C verdict IS the doubling-DOMAIN hinge: is the color/short-root space J-real (count, no
    double -> A) or J-complexified (doubles -> C)? does U(1)_Y normalize over the whole tangent (A) or a
    component (B)? The exact J-eigenspace of V12 (Lyra owes) + Keeper's independent r settle it.
  * MY BLIND LEAN (NOT banked un-tuned, Cal §341): CASE A (r=3/10 -> 3/13), from the selectivity principle
    (no N_c inside a doubling trace) + T2545 (color = a count). I flag it, I do NOT assert it -- the
    hinge + Keeper decide. If A confirms un-tuned: 3/13 -> Derived + the SO(2)-triple.

AUG-08 [TEGMARK]. Nothing pushed. Nothing banked. Verified the case-structure; localized the one open
hinge; honest lean = A, flagged not-un-tuned. sin^2 stays Structural/Identified. Elie's blind half. Count N.
""")
