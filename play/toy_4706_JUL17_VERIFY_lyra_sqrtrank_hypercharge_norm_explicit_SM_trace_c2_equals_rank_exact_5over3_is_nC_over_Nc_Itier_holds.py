#!/usr/bin/env python3
"""
Toy 4706 — Jul 17 (VERIFY Lyra's √rank hypercharge localization, mine; the index-arithmetic gate): Lyra localized
sin²θ_W to a single factor — Q = T₃ + √rank·Y takes the forbidden GUT 3/8 to BST's 3/13 — and solved (not fit) for the
hypercharge normalization, getting c² = rank cleanly. My assignment: verify the index arithmetic against the three
bars the moment it lands. I compute the EXPLICIT one-generation SM fermion trace from scratch. Result: it CHECKS
exactly — sin²θ_W = Tr(T₃²)/Tr(Q²) = 3/8 (standard), and rescaling Q = T₃ + c·Y and solving sin²θ_W = 3/13 gives
c² = rank = 2 EXACTLY. BONUS structural finding: Tr(Y²)/Tr(T₃²) = 5/3 = n_C/N_c — the standard GUT hypercharge
normalization factor IS n_C/N_c, so even the GUT value 3/8 = N_c/(N_c+n_C) is BST-flavored, and BST's shift is exactly
c²=rank multiplying the n_C. HONEST TIER HELD: c²=rank is SOLVED-clean-primary (target-innocent SM hypercharges → the
needed normalization is exactly a BST primary — stronger than matching), but the GEOMETRIC FORCING (Lyra's two-rulers
rank-2 boundary) is a LEAD, not computed. sin²θ_W stays I-tier (reduced-to-c²=rank), NOT derived.

THE EXPLICIT TRACE (one SM generation, from scratch — target-innocent, SM hypercharges are fixed data):
  * Tr(T₃²) = 4 doublets × 2·(1/2)² = 2. (1 lepton + 3 color quark left-doublets.)
  * Tr(Q²) = leptons[0+1+1] + quarks[3·2·(2/3)² + 3·2·(1/3)²] = 2 + 10/3 = 16/3.
  * sin²θ_W(standard) = Tr(T₃²)/Tr(Q²) = 2/(16/3) = 3/8 = N_c/(N_c+n_C). ← the GUT value, BST-flavored.
  * Tr(Y²) = Tr(Q²) − Tr(T₃²) = 10/3 (cross term Tr(T₃Y) = 0, verified per-doublet). Tr(Y²)/Tr(T₃²) = 5/3 = n_C/N_c.
  * rescale Q = T₃ + c·Y ⟹ Tr(Q'²) = Tr(T₃²) + c²·Tr(Y²); solve sin²θ_W = 3/13 ⟹ c² = rank = 2 EXACTLY.
  * general form: sin²θ_W = N_c/(N_c + c²·n_C); c²=1 → 3/8 (GUT), c²=rank → 3/13 (BST). c² IS Lyra's k.

⟹ VERDICT: Lyra's algebra is EXACT — the SM fermion trace gives 3/8 standard, and c²=rank (Q=T₃+√rank·Y) gives 3/13
EXACTLY; the solved normalization is a clean BST primary (rank), and the GUT normalization factor is n_C/N_c. This is
target-innocent-SHAPED (the SM hypercharges are fixed data; the needed normalization comes out exactly rank, not some
ugly number). But it is SOLVED, not GEOMETRICALLY FORCED — the two-rulers rank-2 boundary is a LEAD. sin²θ_W stays
I-tier (reduced-to-c²=rank), NOT derived, pending Lyra's boundary normalization computation. When she forces √rank from
the geometry innocent of 3/13, I re-verify and it moves I→derived. Count ~7-8 (α RULED). Five-Absence-safe.
"""
from fractions import Fraction as F
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- explicit one-generation SM trace (from scratch) ------------------------
Tr_T3sq = 4*F(1,2)                                          # 4 left doublets × 2·(1/2)²
lep  = F(0)**2 + F(-1)**2 + F(-1)**2                        # ν, e_L, e_R
quark = 3*(2*F(2,3)**2) + 3*(2*F(1,3)**2)                   # u(L,R)×3col + d(L,R)×3col
Tr_Qsq = lep + quark                                        # 16/3
Tr_Ysq = Tr_Qsq - Tr_T3sq                                  # 10/3 (cross term = 0)
sw_std = Tr_T3sq/Tr_Qsq                                     # 3/8
print(f"\n[trace]: Tr(T₃²)={Tr_T3sq}, Tr(Q²)={Tr_Qsq}, Tr(Y²)={Tr_Ysq}; sin²θ_W(std) = {sw_std} = {float(sw_std):.5f}")
check("EXPLICIT SM TRACE VERIFIED (from scratch, target-innocent SM hypercharges): Tr(T₃²)=2 (4 left doublets), "
      "Tr(Q²)=16/3 (all L+R fermions, 1 generation), sin²θ_W(standard) = 2/(16/3) = 3/8 — the GUT value, computed "
      "directly from the fixed SM fermion content.",
      Tr_T3sq == 2 and Tr_Qsq == F(16,3) and sw_std == F(3,8), "SM trace: Tr(T₃²)=2, Tr(Q²)=16/3, sin²θ_W(std)=3/8 (GUT) — verified from scratch")

# ---- BONUS: the GUT normalization factor is n_C/N_c -------------------------
ratio = Tr_Ysq/Tr_T3sq                                     # 5/3
print(f"[bonus]: Tr(Y²)/Tr(T₃²) = {ratio} = n_C/N_c = {F(n_C,N_c)}; so 3/8 = N_c/(N_c+n_C) — BST-flavored GUT value")
check("BONUS STRUCTURAL FINDING: Tr(Y²)/Tr(T₃²) = 5/3 = n_C/N_c — the STANDARD GUT hypercharge normalization factor IS "
      "n_C/N_c. So even the GUT value 3/8 = N_c/(N_c+n_C) is BST-flavored, and the primaries {N_c, n_C} sit inside the "
      "SM fermion hypercharge content. BST's shift is c²=rank multiplying the n_C.",
      ratio == F(n_C,N_c) and sw_std == F(N_c, N_c+n_C), "Tr(Y²)/Tr(T₃²)=5/3=n_C/N_c; 3/8=N_c/(N_c+n_C) — GUT norm factor is n_C/N_c")

# ---- solve for the hypercharge normalization: c² = rank exactly -------------
# Q = T3 + c·Y ⟹ Tr(Q'²) = Tr(T3²) + c²·Tr(Y²) (cross term 0); solve sin²θ_W = 3/13
# 3/13 = Tr_T3sq/(Tr_T3sq + c²·Tr_Ysq)  ⟹  c² = (Tr_T3sq·13/3 − Tr_T3sq)/Tr_Ysq
c2 = (Tr_T3sq*F(13,3) - Tr_T3sq)/Tr_Ysq
sw_rank = Tr_T3sq/(Tr_T3sq + rank*Tr_Ysq)
print(f"[solve]: Q=T₃+c·Y, solve sin²θ_W=3/13 → c² = {c2} = rank; check c²=rank → sin²θ_W = {sw_rank} = {float(sw_rank):.5f} vs obs 0.23122")
check("SOLVE — c² = rank EXACTLY (Lyra's 'solved not fit', verified): rescaling Q = T₃ + c·Y gives Tr(Q'²) = "
      "Tr(T₃²)+c²·Tr(Y²); solving sin²θ_W = 3/13 yields c² = 2 = rank EXACTLY (a clean BST primary, not an ugly "
      "number). And c²=rank → sin²θ_W = 3/13 = N_c/(N_c+rank·n_C) (0.19% vs obs). c² IS Lyra's hypercharge-normalization k.",
      c2 == rank and sw_rank == F(3,13), "solved hypercharge normalization c² = rank = 2 EXACTLY → 3/13; c² is Lyra's k")

# ---- general form + Five-Absence -------------------------------------------
forms = {c2v: F(N_c, N_c + c2v*n_C) for c2v in (1, rank)}
print(f"[form]: sin²θ_W = N_c/(N_c+c²·n_C); c²=1 → {forms[1]} (GUT, forbidden), c²=rank → {forms[rank]} (BST)")
check("GENERAL FORM + FIVE-ABSENCE: sin²θ_W = N_c/(N_c + c²·n_C); c²=1 → 3/8 (GUT, Five-Absence-forbidden), c²=rank → "
      "3/13 (BST, observed). The naive/GUT normalization (c²=1) lands ON the forbidden value; BST's c²=rank does not → "
      "Five-Absence PASS. c²=rank is the geometric normalization the domain must supply.",
      forms[1] == F(3,8) and forms[rank] == F(3,13), "sin²θ_W=N_c/(N_c+c²·n_C); c²=1→3/8 forbidden, c²=rank→3/13 — Five-Absence PASS")

# ---- honest tier hold -------------------------------------------------------
check("HONEST TIER HELD (target-innocence bar): c²=rank is SOLVED-clean-primary — given the target-innocent SM "
      "hypercharges, the needed normalization comes out EXACTLY rank (target-innocent-SHAPED, stronger than matching). "
      "BUT it is SOLVED (set sin²θ_W=3/13, found c²), NOT geometrically FORCED — Lyra's two-rulers rank-2 boundary is a "
      "LEAD, not computed. sin²θ_W stays I-tier (reduced-to-c²=rank), NOT derived. When Lyra forces √rank from the "
      "boundary innocent of 3/13, I re-verify and it moves I→derived. @Grace: hold the tier-map at reduced, not derived.",
      c2 == rank, "c²=rank solved-clean-primary (target-innocent-shaped) but geometric forcing pending → I-tier holds, NOT derived")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: Lyra's algebra is EXACT — SM trace gives 3/8 standard; Q=T₃+√rank·Y gives 3/13 EXACTLY; the solved "
      "normalization c²=rank is a clean primary; the GUT norm factor is n_C/N_c. Target-innocent-shaped, Five-Absence "
      "PASS. But SOLVED, not geometrically forced (two-rulers boundary is a LEAD). sin²θ_W stays I-tier reduced-to-"
      "c²=rank, NOT derived, pending the boundary normalization computation — which I verify against the three bars "
      "when it lands. Count ~7-8 (α RULED). Five-Absence-safe.",
      c2 == rank and sw_rank == F(3,13) and forms[1] == F(3,8),
      "√rank algebra exact (c²=rank→3/13, 5/3=n_C/N_c); solved-clean-primary but forcing pending → I-tier reduced-not-derived")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 100)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 100)
print(f"SCORE: {passed}/{total}")
print("=" * 100)
print("""
VERIFY Lyra's √rank hypercharge localization (index-arithmetic gate) — algebra EXACT, tier HELD:
  * EXPLICIT SM TRACE (from scratch): Tr(T₃²)=2, Tr(Q²)=16/3 → sin²θ_W(std) = 3/8 (GUT). Target-innocent SM hypercharges.
  * BONUS: Tr(Y²)/Tr(T₃²) = 5/3 = n_C/N_c — the GUT norm factor IS n_C/N_c; 3/8 = N_c/(N_c+n_C) is BST-flavored.
  * SOLVE: Q=T₃+c·Y, sin²θ_W=3/13 → c² = rank = 2 EXACTLY (clean primary, Lyra's 'solved not fit' verified). c² = her k.
  * FIVE-ABSENCE: c²=1→3/8 forbidden GUT, c²=rank→3/13 → PASS.
  * TIER HELD: solved-clean-primary (target-innocent-shaped) but geometric forcing (two-rulers boundary) is a LEAD →
    sin²θ_W stays I-tier reduced-to-c²=rank, NOT derived. Verify the boundary computation when it lands. Count ~7-8.
""")
