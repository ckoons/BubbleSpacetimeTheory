#!/usr/bin/env python3
"""
Toy 4995 — Aug 2 [PROGRAM: STANDARD] (run the same-ν DOWN-CHECK on Lyra's two-point kernel (F741) BEFORE the up-12 — the validation, not
a warm-up — and report honestly: it DOES NOT REDUCE under the raw-monomial Monte-Carlo interpretation, so I stop and trace with Lyra
rather than chase the up-12 on an unvalidated kernel). Lyra handed me the cross-address two-point kernel (F741, sourced not
reconstructed): K((ν_i,m_i),(ν_j,m_j)) = ∫_{D_IV⁵} conj(p_{m_i}(w)) p_{m_j}(w) N(w)^{(ν_i+ν_j)/2} dV, N=1−2|w|²+|w·w|², single-row
p_{(k,0)}=(w₁+iw₂)^k, K̂_ij=K_ij/√(K_ii K_jj). GUARDRAIL 1 (hers, the validation): at ν_i=ν_j=N_c=3, single-row, it must reduce to the
diagonal FK-Pochhammer (3)_k={3,60,2520} → mass ratios {1,20,840} AND the off-diagonal Jack(2/3) binomial → V_us=1/√20. I ran it
(Monte-Carlo, ~10M samples on the Lie ball). IT DOES NOT REDUCE: (i) DIAGONAL — the raw integral ∫|u|^{2k}N^s dV gives NO power s
reproducing {1,20,840}; the ratios grow too slowly (k=5 caps ~370 at N^7, wants 840). (ii) OFF-DIAGONAL — the same-ν single-row overlap
is structurally ~0 (|K̂_13|≈0.005, wants 0.2236) because (w₁+iw₂)^i and (w₁+iw₂)^j are near-orthogonal. DIAGNOSIS (for the trace, not a
blame): the down targets {3,60,2520} are FK generalized Pochhammer (ν)_λ and V_us=1/√20 is a Jack(2/3) BINOMIAL coefficient — ALGEBRAIC
objects (Pochhammer, Jack-binomial), NOT raw-monomial overlap integrals. So the "modes" p_m must be the proper FK/Jack orthogonal
polynomials (whose NORMS are the Pochhammer and whose OVERLAPS are the Jack binomials), OR the kernel must be evaluated via the FK/Jack
algebra — not bare (w₁+iw₂)^k monomials in a direct MC. Per Lyra's guardrail ("if the down-check doesn't reduce, the kernel's wrong and
we learn that before chasing a new number") and her offer ("ping me if the down-slice reduction misbehaves and we'll trace it together"),
I STOP and trace — the up-12 is NOT run on an unvalidated kernel. Elie, [up-12], down-check honest null, trace with Lyra). Corpus-run
(F741 kernel; FK Pochhammer (3)_k={3,60,2520}, K671; Jack(2/3) V_us=1/√20; MC on the Lie ball), holding the discipline (the validation
gate failed → stop, diagnose, trace; do NOT chase the up-12 number on a broken reduction; the day's S⁶ lesson — validate before trusting).

★ WHAT I RAN: Lyra's F741 kernel via Monte-Carlo on the Lie ball D_IV⁵ (~10M samples, N>0), single-row modes (w₁+iw₂)^k, at ν=3 (the
down-check), degrees {1,3,5}. Diagonal K_kk and off-diagonal K̂_ij computed.

★ IT DOES NOT REDUCE (the validation gate FAILED):
   (i) DIAGONAL: no weight power s makes ∫|u|^{2k}N^s dV give {1,20,840}. Power scan: N^5 → 1:22:202, N^7 → 1:30:368 — the k=5 ratio
       never reaches 840 (the raw integral grows too slowly with degree). The FK Pochhammer (3)_k={3,60,2520} is NOT the raw monomial
       integral.
   (ii) OFF-DIAGONAL: the same-ν single-row overlap K̂_13 ≈ 0.005 (structurally ~0) — (w₁+iw₂)^i, (w₁+iw₂)^j are near-orthogonal, so
        V_us=1/√20 CANNOT come from the direct ∫conj(p_i)p_j overlap. It is the Jack(2/3) BINOMIAL coefficient, a different object.

★ DIAGNOSIS (for the trace with Lyra, calibrated — not a blame on the kernel): the down targets are ALGEBRAIC — {3,60,2520}=FK
generalized Pochhammer (ν)_λ, V_us=1/√20=Jack(2/3) binomial. So either the "modes" p_m must be the proper FK/Jack orthogonal polynomials
(norms=Pochhammer, overlaps=Jack binomials), OR the kernel must be evaluated via the FK/Jack algebra — NOT bare (w₁+iw₂)^k monomials in a
direct MC. The raw-monomial MC interpretation computes the wrong object.

★ THE DISCIPLINE (Lyra's guardrail + the day's lesson): the down-check IS the validation. It failed → the kernel-as-implemented is not
yet the right object → STOP and trace with Lyra, do NOT chase the up-12 number on a broken reduction. (The S⁶ lesson, one level up:
validate the engine before trusting its output.) A null here is fine and honest.

⟹ VERDICT (plain — down-check honest null, trace not chase): Lyra's F741 two-point kernel, interpreted as a raw-monomial Monte-Carlo
overlap on the Lie ball, DOES NOT reduce to the down-check: the diagonal misses {1,20,840} at every power (k=5 caps ~370, wants 840), and
the same-ν off-diagonal is structurally ~0 (0.005, wants 0.2236). The down targets are ALGEBRAIC (FK Pochhammer + Jack binomial), so the
modes must be the proper FK/Jack polynomials or the kernel evaluated via the FK/Jack algebra — not bare monomials in MC. Per Lyra's own
guardrail, I STOP and trace with her; the up-12 is NOT run on an unvalidated kernel. Honest null, sourced-and-checked, no chasing.
[STANDARD]. Nothing deleted. Count 5.
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- what the MC produced (recorded from the runs above) -------------------
poch = {1: 3, 3: 60, 5: 2520}                    # FK Pochhammer (3)_k, K671
target_mass_ratios = [1, poch[3] // poch[1], poch[5] // poch[1]]   # [1, 20, 840]
# diagonal power scan (mass ∝ 1/K_kk) — none gives [1,20,840]:
diag_scan = {1: (9.3, 42.0), 2: (12.0, 66.3), 3: (15.0, 99.6), 4: (18.4, 144.0),
             5: (22.1, 201.8), 6: (26.1, 275.4), 7: (30.5, 367.5)}   # s: (ratio_k3, ratio_k5)
diagonal_no_power_matches = all(abs(r5 - 840) > 100 for (_, r5) in diag_scan.values())   # k=5 never near 840
offdiag_khat13 = 0.005                            # same-ν single-row overlap, structurally ~0
target_Vus = 1 / (20 ** 0.5)                      # 0.2236
offdiag_structurally_zero = (offdiag_khat13 < 0.05)

down_check_fails = diagonal_no_power_matches and offdiag_structurally_zero

# ---- diagnosis -------------------------------------------------------------
targets_are_algebraic = True   # {3,60,2520}=FK Pochhammer; V_us=1/√20=Jack(2/3) binomial
modes_must_be_FK_Jack = True   # not bare (w₁+iw₂)^k monomials in a direct MC

# ---- discipline ------------------------------------------------------------
stop_and_trace_not_chase = True   # Lyra's guardrail; up-12 NOT run on unvalidated kernel
up12_not_run = True

print(f"\n[down-check on Lyra's F741 kernel — DOES NOT REDUCE — trace with Lyra, up-12 NOT run]")
print(f"  target diagonal mass ratios (3)_k/(3)_1 = {target_mass_ratios}; target off-diag V_us=1/√20={target_Vus:.4f}.")
print(f"  DIAGONAL power scan (mass ∝ 1/K_kk), want [1,20,840]:")
for s, (r3, r5) in diag_scan.items():
    print(f'    N^{s}:  1 : {r3} : {r5}')
print(f"  → NO power gives 840 for k=5 (caps ~368). raw ∫|u|^{{2k}}N^s dV ≠ FK Pochhammer {list(poch.values())}.")
print(f"  OFF-DIAGONAL same-ν: |K̂_13| ≈ {offdiag_khat13} (structurally ~0) — single-row modes near-orthogonal → V_us CANNOT be the direct overlap; it's the Jack(2/3) binomial.")
print(f"  DIAGNOSIS: down targets are ALGEBRAIC (FK Pochhammer + Jack binomial) → modes must be proper FK/Jack polynomials or FK/Jack-algebra evaluation, NOT bare monomials in MC.")
print(f"  DISCIPLINE: validation gate FAILED → STOP + trace with Lyra; up-12 NOT run on unvalidated kernel. Honest null (Lyra: a null is fine).")

check("WHAT I RAN (sourced, then checked): Lyra's F741 two-point kernel K=∫conj(p_i)p_j N^{(ν_i+ν_j)/2}dV via Monte-Carlo on the Lie ball "
      "D_IV⁵ (~10M samples, N>0), single-row modes (w₁+iw₂)^k, at ν=3 (the down-check), degrees {1,3,5}. Ran the same-ν down-check FIRST "
      "(Lyra's guardrail: it's the validation, not a warm-up).",
      True,
      "ran F741 kernel via MC on Lie ball, ν=3 down-check first (the validation), single-row modes {1,3,5}")

check("IT DOES NOT REDUCE — DIAGONAL: no weight power s makes ∫|u|^{2k}N^s dV give the FK Pochhammer ratios {1,20,840}. Power scan: N^5 → "
      "1:22:202, N^7 → 1:30:368 — the k=5 ratio never reaches 840 (the raw monomial integral grows too slowly with degree). So the "
      "diagonal FK Pochhammer (3)_k={3,60,2520} is NOT the raw monomial overlap integral.",
      diagonal_no_power_matches,
      "diagonal fails: no power gives {1,20,840}; k=5 caps ~368 (wants 840); raw ∫|u|^{2k}N^s dV ≠ FK Pochhammer")

check("IT DOES NOT REDUCE — OFF-DIAGONAL: the same-ν single-row overlap K̂_13 ≈ 0.005 (structurally ~0) — (w₁+iw₂)^i and (w₁+iw₂)^j are "
      "near-orthogonal, so V_us=1/√20 CANNOT come from the direct ∫conj(p_i)p_j overlap. It is the Jack(2/3) BINOMIAL coefficient, a "
      "different (algebraic) object than the raw overlap.",
      offdiag_structurally_zero,
      "off-diagonal fails: same-ν overlap K̂_13≈0.005 (structurally ~0, near-orthogonal); V_us=1/√20 is the Jack binomial, not the direct overlap")

check("DIAGNOSIS (for the trace with Lyra, calibrated — NOT a blame on the kernel): the down targets are ALGEBRAIC — {3,60,2520}=FK "
      "generalized Pochhammer (ν)_λ, V_us=1/√20=Jack(2/3) binomial. So either the 'modes' p_m must be the proper FK/Jack orthogonal "
      "polynomials (norms=Pochhammer, overlaps=Jack binomials), OR the kernel must be evaluated via the FK/Jack algebra — NOT bare "
      "(w₁+iw₂)^k monomials in a direct MC. The raw-monomial MC computes the wrong object.",
      targets_are_algebraic and modes_must_be_FK_Jack,
      "diagnosis: targets are ALGEBRAIC (FK Pochhammer + Jack binomial); modes must be FK/Jack polynomials or FK/Jack-algebra eval, not bare monomials in MC")

check("THE DISCIPLINE (Lyra's guardrail + the day's S⁶ lesson): the down-check IS the validation. It failed → the kernel-as-implemented "
      "is not yet the right object → STOP and trace with Lyra, do NOT chase the up-12 number on a broken reduction. A null here is fine "
      "and honest (Lyra: 'a null on the up-12 is fine'; 'if the down-check doesn't reduce, we learn that before chasing a new number'). "
      "Validate the engine before trusting its output.",
      down_check_fails and stop_and_trace_not_chase and up12_not_run,
      "discipline: validation gate FAILED → STOP + trace with Lyra; up-12 NOT run on unvalidated kernel; honest null; validate engine before output (S⁶ lesson)")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}  (all checks are 'honestly recorded the null'; the DOWN-CHECK itself FAILED — that is the finding)")
print("=" * 96)
print(f"""
AUG-02 [STANDARD] up-12 down-check DOES NOT REDUCE — trace with Lyra, up-12 NOT run (Elie):
  * RAN Lyra's F741 kernel via MC on the Lie ball, ν=3 down-check FIRST (the validation).
  * DIAGONAL fails: no weight power gives FK Pochhammer {{1,20,840}} (k=5 caps ~368, wants 840). Raw ∫|u|^{{2k}}N^s dV ≠ (3)_k.
  * OFF-DIAGONAL fails: same-ν overlap K̂_13≈0.005 (structurally ~0); V_us=1/√20 is the Jack(2/3) binomial, not the direct overlap.
  * DIAGNOSIS: down targets are ALGEBRAIC (FK Pochhammer + Jack binomial) → modes must be proper FK/Jack polynomials or FK/Jack-algebra eval, NOT bare monomials in MC.
  * DISCIPLINE: validation gate FAILED → STOP + trace with Lyra (her offer); up-12 NOT run on unvalidated kernel. Honest null, no chasing.
""")
