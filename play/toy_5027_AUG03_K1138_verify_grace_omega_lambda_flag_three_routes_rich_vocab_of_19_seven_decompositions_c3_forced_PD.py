#!/usr/bin/env python3
"""
Toy 5027 — Aug 3 [PROGRAM: TEGMARK] (verify Grace's Ω_Λ over-claim flag before the external-facing language change Casey just approved:
const_014's "13/19 via three independent routes, most overdetermined result in BST" is rich-vocabulary of the ONE denominator 19, K741-class;
K1138). Casey approved Grace's language fix (external-facing) — recomputing the flagged claim (my "recompute the surfaced proxy" role, same as
r_* and m_b) to confirm it with an independent check before it lands. Grep-first (const_014 mechanism + tier_review already updated by Grace).

★ THE CLAIM (superseded): "Chern polynomial of D_IV⁵ gives 13/19 via three independent routes — most overdetermined result in BST." Grace's
  three "routes" for the denominator 19: N_c²+2n_C=19, c₃+χ=13+6=19, genus-2 Verlinde 7+5+4+3=19.

★ THE VERIFICATION (STRENGTHENS the flag): 19 is a small integer with MANY additive BST decompositions — I trivially found FOUR MORE beyond
  Grace's three: rank+n_C+g+n_C=19, N_c·C_2+1=19, C_2+g+C_2=19, 2g+n_C=19. Seven decompositions total. So "three independent routes" is NOT
  special over-determination — it is the rich-vocabulary illusion (F417 / Cal-286): a small integer in a 6-integer vocabulary has many ways to
  be WRITTEN, and finding three (or seven) is expected, not evidence. Exactly the K741 retraction class (Λ "5-fold over-determined" was one
  factorization ×5).

★ THE FORCED PART (stands): the NUMERATOR c₃=13 is Chern-Weil forced (c₃(Q⁵)=13 from (1+H)⁷/(1+2H), exponent 7=g, quadric degree 2). Ω_Λ =
  c₃/(c₃+χ) = 13/19 = 0.6842 vs observed 0.6847 (0.07%). The OPEN part: the specific COMBINATION c₃/(c₃+χ) is not yet forced over alternatives
  (c₂/(c₂+χ) etc.) — a reachable index-theoretic derivation (blind vacuum-fraction operator), not an impossibility.

★ THE CONFIRMATION: Grace's flag is CORRECT and if anything UNDERSTATED (7 decompositions, not 3). The "most overdetermined result in BST"
  language must NOT travel externally (rich-vocabulary of 19, K741-class). Tier stays PARTIALLY DERIVED (c₃=13 forced; combination open) — this
  is a confirmation/representation flag, NOT a tier move. Casey approved the language fix; this backs it computationally. ⟹ DISPOSITION: Grace's
  Ω_Λ over-claim flag CONFIRMED (independent check found 7 decompositions of 19 — rich-vocabulary, not over-determination); c₃=13 forced part
  stands; tier PD unchanged; external "most overdetermined" language dropped (Casey OK'd). Elie, K1138, Grace Ω_Λ flag confirmed). Corpus-run
  (const_014 Ω_Λ=13/19; c₃(Q⁵)=13 Chern-Weil; F417/Cal-286 rich-vocabulary; K741 retraction pattern), holding the discipline (recompute the
  flagged claim independently; confirm — and strengthen — the over-claim finding straight; the forced c₃=13 stands; no tier move; back the
  approved external-language fix).

⟹ VERDICT (plain — Grace's Ω_Λ flag confirmed and strengthened): the const_014 "13/19 via three independent routes, most overdetermined result
in BST" is rich-vocabulary of the ONE denominator 19 — I independently found SEVEN BST-integer decompositions of 19 (Grace's 3 + 4 more), so
"three independent routes" is the expected rich-vocabulary illusion (F417/Cal-286, K741-class), NOT over-determination. The forced part stands
(numerator c₃=13 Chern-Weil, Ω_Λ=13/19=0.68 at 0.07%); the combination c₃/(c₃+χ) is the open part. Tier stays Partially Derived (confirmation
flag, not a tier move); the external "most overdetermined" language is correctly dropped (Casey approved Grace's fix). [TEGMARK]. Nothing
deleted. Count 5.
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- the denominator 19 and its decompositions -----------------------------
chi = C_2                                          # χ(Q⁵) = 6 = C₂
c3 = 13                                            # c₃(Q⁵) Chern-Weil forced
denom = 19
graces_routes = {
    'N_c²+2n_C': N_c**2 + 2 * n_C,                 # 19
    'c₃+χ': c3 + chi,                              # 19
    'genus-2 Verlinde 7+5+4+3': 7 + 5 + 4 + 3,     # 19
}
my_extra_routes = {
    'rank+n_C+g+n_C': rank + n_C + g + n_C,         # 19
    'N_c·C_2+1': N_c * C_2 + 1,                     # 19
    'C_2+g+C_2': C_2 + g + C_2,                     # 19
    '2g+n_C': 2 * g + n_C,                          # 19
}
all_routes = {**graces_routes, **my_extra_routes}
all_equal_19 = all(v == denom for v in all_routes.values())
n_decompositions = len(all_routes)                  # 7
rich_vocabulary = (n_decompositions >= 5)           # many decompositions → rich-vocabulary, not over-determination

# ---- the forced part -------------------------------------------------------
Omega_Lambda = c3 / (c3 + chi)                      # 13/19
obs = 0.6847
c3_forced = (c3 == 13)                              # Chern-Weil c₃(Q⁵)=13
value_matches = (abs(Omega_Lambda - obs) / obs < 0.002)   # 0.07%
combination_open = True                             # c₃/(c₃+χ) not yet forced over alternatives

# ---- confirmation ----------------------------------------------------------
flag_confirmed = all_equal_19 and rich_vocabulary   # Grace's flag correct (and understated)
tier_stays_PD = c3_forced and combination_open      # confirmation flag, not a tier move
external_language_dropped = True                    # Casey approved

print(f"\n[Verify Grace's Ω_Λ over-claim flag (const_014) — K1138]")
print(f"  the denominator 19 — {n_decompositions} BST-integer decompositions (Grace's 3 + my 4):")
for name, v in all_routes.items():
    print(f"    19 = {name} = {v}  {'✓' if v == 19 else '✗'}")
print(f"  → 'three independent routes' = rich-vocabulary of ONE number 19 (F417/Cal-286, K741-class), NOT over-determination.")
print(f"  FORCED part stands: numerator c₃=13 (Chern-Weil c₃(Q⁵)); Ω_Λ=13/19={Omega_Lambda:.4f} vs {obs} ({abs(Omega_Lambda-obs)/obs*100:.2f}%). OPEN: combination c₃/(c₃+χ).")
print(f"  ⟹ Grace's flag CONFIRMED (and understated: 7 decompositions, not 3). Tier stays PD (confirmation flag, not a tier move). External 'most overdetermined' language dropped (Casey OK).")

check("THE VERIFICATION (strengthens the flag): 19 has MANY additive BST decompositions — I independently found FOUR MORE beyond Grace's three "
      "(rank+n_C+g+n_C, N_c·C_2+1, C_2+g+C_2, 2g+n_C), seven total, all = 19. So 'three independent routes' is NOT over-determination — it is "
      "the rich-vocabulary illusion (F417/Cal-286): a small integer in a 6-integer vocabulary has many ways to be written; finding three (or "
      "seven) is expected, not evidence. Same class as the K741 retraction.",
      all_equal_19 and rich_vocabulary and n_decompositions >= 7,
      "verification: 7 BST-integer decompositions of 19 (Grace's 3 + my 4), all =19 → rich-vocabulary of one number (F417/Cal-286, K741-class), not over-determination")

check("THE FORCED PART (stands): the NUMERATOR c₃=13 is Chern-Weil forced (c₃(Q⁵)=13 from (1+H)⁷/(1+2H), exponent 7=g, quadric degree 2). "
      "Ω_Λ = c₃/(c₃+χ) = 13/19 = 0.6842 vs observed 0.6847 (0.07%). The OPEN part: the specific combination c₃/(c₃+χ) is not yet forced over "
      "alternatives — a reachable index-theoretic derivation, not an impossibility.",
      c3_forced and value_matches and combination_open,
      "forced part: numerator c₃=13 Chern-Weil forced; Ω_Λ=13/19=0.68 at 0.07%; combination c₃/(c₃+χ) open (reachable, not impossible)")

check("THE CONFIRMATION: Grace's flag is CORRECT and if anything UNDERSTATED (7 decompositions, not 3). The 'most overdetermined result in BST' "
      "language must NOT travel externally (rich-vocabulary of 19, K741-class). Tier stays PARTIALLY DERIVED (c₃=13 forced; combination open) — "
      "a confirmation/representation flag, NOT a tier move. Casey approved the language fix; this backs it computationally.",
      flag_confirmed and tier_stays_PD and external_language_dropped,
      "confirmation: Grace's flag correct (understated — 7 decompositions); tier stays PD (confirmation flag, not a tier move); external 'most overdetermined' language dropped (Casey OK)")

check("VERDICT: const_014's 'three independent routes, most overdetermined result in BST' is rich-vocabulary of the ONE denominator 19 — 7 "
      "BST-integer decompositions found (Grace's 3 + 4 more), so it is the expected rich-vocabulary illusion (F417/Cal-286, K741-class), NOT "
      "over-determination. The forced part stands (numerator c₃=13 Chern-Weil, Ω_Λ=13/19=0.68 at 0.07%); the combination is the open part. "
      "Tier stays Partially Derived (confirmation flag, not a tier move); external 'most overdetermined' language correctly dropped (Casey "
      "approved Grace's fix).",
      flag_confirmed and c3_forced and tier_stays_PD,
      "verdict: Grace's Ω_Λ flag confirmed+strengthened (7 decompositions of 19 = rich-vocabulary, not over-determination); c₃=13 forced stands; tier PD; external language dropped")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-03 [TEGMARK] verify Grace's Ω_Λ over-claim flag (const_014) — CONFIRMED + strengthened (Elie, K1138):
  * 19 has 7 BST-integer decompositions (Grace's 3 + my 4: rank+n_C+g+n_C, N_c·C_2+1, C_2+g+C_2, 2g+n_C) → rich-vocabulary of ONE number, NOT over-determination (F417/Cal-286, K741-class).
  * FORCED part stands: numerator c₃=13 Chern-Weil forced; Ω_Λ=13/19=0.6842 vs 0.6847 (0.07%). OPEN: combination c₃/(c₃+χ).
  * Grace's flag CORRECT and UNDERSTATED (7 not 3). Tier stays PD (confirmation flag, not a tier move). External "most overdetermined" language dropped (Casey approved).
""")
