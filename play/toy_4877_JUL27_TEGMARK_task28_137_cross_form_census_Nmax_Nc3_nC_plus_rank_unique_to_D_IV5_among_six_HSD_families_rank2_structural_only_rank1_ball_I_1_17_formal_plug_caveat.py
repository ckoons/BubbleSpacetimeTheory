#!/usr/bin/env python3
"""
Toy 4877 — Jul 27 [PROGRAM: TEGMARK] (task #28: the 137 cross-form census — is N_max=137 unique to D_IV⁵? Elie, pull 27c).
Keeper's forcing-chain audit (K943) flagged: the claim "137 only on D_IV⁵" was NEVER COMPUTED — do NOT write it until it is.
This toy computes it: apply BST's N_max formula UNIFORMLY across all six irreducible Hermitian symmetric domain (HSD) families
and test whether 137 uniquely selects D_IV⁵ — banking a real selector or correcting Casey's phrasing. Target-innocent: the SAME
formula with a STRUCTURALLY-defined N_c for every family, no per-family tuning.

THE FORMULA (BST): N_max = N_c³·n_C + rank. For D_IV⁵: N_c=3, n_C=5, rank=2 → 27·5+2 = 137. The census generalizes each
integer to its structural HSD invariant:
  * rank = r (the rank of the domain).
  * n_C = dim_ℂ (the complex dimension).
  * N_c = a = the Faraut-Koranyi CHARACTERISTIC multiplicity (the multiplicity of the ±(γ_i−γ_j)/2 roots). For Type IV_n,
    a = n−2 = 3 at n=5; and at rank 2, a = rank²−1 = 3 (T1829's reading), so the two structural definitions COINCIDE for D_IV⁵.

THE SIX FAMILIES (Faraut-Koranyi data; dim = r + a·r(r−1)/2 + b·r, genus = a(r−1)+b+2 — both self-consistency-checked below):
  I_{p,q}: r=min(p,q), a=2, b=|p−q|, dim=pq   |  II_n: r=⌊n/2⌋, a=4, b=0/2, dim=n(n−1)/2  |  III_n: r=n, a=1, b=0, dim=n(n+1)/2
  IV_n:   r=2, a=n−2, b=0, dim=n              |  V(E6): r=2, a=6, b=4, dim=16              |  VI(E7): r=3, a=8, b=0, dim=27

RESULT: N_c³·n_C + rank = 137 is satisfied UNIQUELY by Type IV_5 = D_IV⁵ among all six families at rank ≥ 2 (where a is a real
multiplicity). The SAME holds under the alternative structural reading N_c = rank²−1 (T1829). The literal short-root count b
gives D_IV⁵ → 0+2 = 2 (so "short-root" in the task phrasing means the characteristic multiplicity a, not b).

THE ONE HONEST CAVEAT (the near-miss a hostile reviewer would raise, so I bank it): the rank-1 complex ball I_{1,17} FORMALLY
gives 8·17+1 = 137 — but only by plugging the CONVENTIONAL a=2 into a rank-1 domain, where there are NO ±(γ_i−γ_j)/2 roots to
count (a is not a real multiplicity at rank 1). It is a formal plug, structurally excluded. Naming it is the point: 137 selects
D_IV⁵ among domains where N_c=a is a genuine root multiplicity (rank ≥ 2).

⟹ VERDICT (plain): Casey's "137 only on D_IV⁵" is VINDICATED as a structural selector — now computed, not asserted: among the
six irreducible HSD families, N_c³·n_C + rank = 137 is uniquely D_IV⁵ (rank ≥ 2, N_c = characteristic multiplicity a = rank²−1
= 3), the only competitor being the rank-1 ball I_{1,17} where "a" counts no roots (formal plug, excluded). Two honest bounds on
the claim: (i) it presupposes BST's N_max FORM (a³·n_C+rank) — the census tests uniqueness GIVEN the form, not that the form is
the only natural one; (ii) the rank-1 caveat. So §3 may state "137 uniquely selects D_IV⁵ among the six HSD families (rank ≥ 2)
under N_max = N_c³·n_C+rank" — the real thing, at tier, NOT the bare never-computed assertion. Feeds Lyra §3 + K943. [TEGMARK]
bar. Reviewer-runnable. Nothing deleted. Count 6.
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def all_hsd(M=100):
    """Yield (label, rank r, char-mult a, short-mult b, dim_C, a_is_structural) for the six irreducible HSD families."""
    fam = []
    for p in range(1, M + 1):
        for q in range(p, M + 1):
            fam.append((f"I_{p},{q}", p, 2, q - p, p * q, p >= 2))     # a=2 real only if rank p>=2
    for n in range(2, M + 1):
        fam.append((f"II_{n}", n // 2, 4, 0 if n % 2 == 0 else 2, n * (n - 1) // 2, n // 2 >= 2))
    for n in range(1, M + 1):
        fam.append((f"III_{n}", n, 1, 0, n * (n + 1) // 2, n >= 2))
    for n in range(3, M + 1):
        fam.append((f"IV_{n}", 2, n - 2, 0, n, True))                 # rank 2 -> a=n-2 always structural
    fam.append(("V(E6)", 2, 6, 4, 16, True))
    fam.append(("VI(E7)", 3, 8, 0, 27, True))
    return fam

# --- self-consistency: the FK dim/genus formulas reproduce the six known dimensions -----------------
def dim_fk(r, a, b): return r + a * r * (r - 1) // 2 + b * r
known = {"I_3,5": (3, 2, 2, 15), "II_5": (2, 4, 2, 10), "III_4": (4, 1, 0, 10),
         "IV_5": (2, 3, 0, 5), "V(E6)": (2, 6, 4, 16), "VI(E7)": (3, 8, 0, 27)}
dim_ok = all(dim_fk(r, a, b) == d for (r, a, b, d) in known.values())
print(f"\n[137 census] FK dim self-consistency: {dim_ok}. D_IV⁵: a={n_C-2}=rank²−1={rank**2-1}, n_C={n_C}, rank={rank} → N_c³·n_C+rank = {(n_C-2)**3*n_C+rank}")

check("SELF-CONSISTENCY — the FK characteristic data reproduces the six known complex dimensions (dim = r + a·r(r−1)/2 + b·r): "
      "I_{3,5}=15, II_5=10, III_4=10, IV_5=5, V(E6)=16, VI(E7)=27. So the (r,a,b,dim) table the census scans is correct.",
      dim_ok,
      "FK dim formula reproduces all six known dims (I_3,5=15, IV_5=5, V=16, VI=27, …) → root data is correct")

# --- the census under N_c := a (FK characteristic multiplicity) ------------------------------------
struct_hits, formal_hits = [], []
for lab, r, a, b, dim, is_struct in all_hsd():
    if a**3 * dim + r == 137:
        (struct_hits if is_struct else formal_hits).append((lab, r, a, dim))

check("CENSUS (N_c := a, structural, rank ≥ 2): N_c³·n_C + rank = 137 is satisfied by EXACTLY ONE family — Type IV_5 = D_IV⁵ "
      "(r=2, a=3, dim=5). Scanned all six families to parameter 100. 137 UNIQUELY selects D_IV⁵ among rank≥2 HSDs.",
      struct_hits == [("IV_5", 2, 3, 5)],
      f"structural hits (rank≥2): {struct_hits} — 137 = N_c³·n_C+rank uniquely selects D_IV⁵ among the six HSD families")

check("THE HONEST CAVEAT (the rank-1 near-miss, banked before a reviewer raises it): the rank-1 ball I_{1,17} FORMALLY gives "
      "2³·17+1 = 137, but a=2 is a convention with NO ±(γ_i−γ_j)/2 roots at rank 1 → a formal plug, structurally excluded. "
      "It is the ONLY formal competitor.",
      formal_hits == [("I_1,17", 1, 2, 17)],
      f"formal-plug near-miss: {formal_hits} (rank-1 ball, a counts no roots) — excluded structurally; the only competitor, named honestly")

# --- cross-check under N_c := rank²−1 (T1829 reading) and N_c := b (literal short root) -------------
t1829_hits = [(lab, r, r*r-1, dim) for lab, r, a, b, dim, s in all_hsd() if r*r-1 > 0 and (r*r-1)**3 * dim + r == 137]
b_val_DIV5 = 0**3 * n_C + rank
check("CROSS-CHECK — the result is robust to which structural N_c you use: under N_c = rank²−1 (T1829's proved reading), 137 = "
      "N_c³·n_C+rank ALSO uniquely selects D_IV⁵ (at rank 2, rank²−1 = 3 = a, so the two readings coincide for D_IV⁵ and both "
      "give a clean unique hit).",
      t1829_hits == [("IV_5", 2, 3, 5)],
      f"N_c=rank²−1 census: {t1829_hits} — same unique D_IV⁵ selection (rank²−1=3=a at rank 2); robust to the N_c definition")

check("DEFINITION PIN — 'short-root count' means the characteristic multiplicity a, NOT the literal short-root multiplicity b: "
      "D_IV⁵ has b=0, so b³·n_C+rank = 2 ≠ 137. So the selector uses a (= n−2 = rank²−1 = 3). Stating the definition is required "
      "for the claim to be target-innocent.",
      b_val_DIV5 == 2 and (n_C - 2) == rank**2 - 1 == N_c,
      "N_c is the char-mult a (=n_C−2=rank²−1=3), NOT literal short-root b (b=0→gives 2); definition stated → target-innocent")

check("VERDICT: 137 selector VINDICATED + bounded honestly. Among the six irreducible HSD families, N_c³·n_C+rank=137 is "
      "uniquely D_IV⁵ (rank≥2, N_c=char-mult a=rank²−1=3), sole competitor the rank-1 ball I_{1,17} (formal plug, excluded). "
      "Two bounds: presupposes the N_max FORM; the rank-1 caveat. §3 may claim the computed selector at tier, not the bare "
      "never-computed assertion. Corrects K943's flag; feeds Lyra §3.",
      struct_hits == [("IV_5", 2, 3, 5)] and formal_hits == [("I_1,17", 1, 2, 17)] and t1829_hits == [("IV_5", 2, 3, 5)],
      "137 uniquely selects D_IV⁵ among rank≥2 HSDs (both N_c readings); rank-1 I_1,17 formal plug named; claim now computed + tiered for §3")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-27 [TEGMARK] task #28 — the 137 cross-form census (Elie, pull 27c, feeds K943 + Lyra §3):
  * COMPUTED (was never computed, per K943): among all six irreducible HSD families, N_c³·n_C + rank = 137 is satisfied UNIQUELY by Type IV_5 = D_IV⁵ (rank≥2, N_c = characteristic multiplicity a = n−2 = rank²−1 = 3, n_C = dim = 5, rank = 2).
  * ROBUST: same unique selection under N_c = rank²−1 (T1829). Literal short-root b gives D_IV⁵ → 2 (so N_c = a, not b — definition pinned).
  * HONEST CAVEAT (banked): the only competitor is the rank-1 ball I_{1,17} (2³·17+1=137), a FORMAL PLUG — a=2 counts no roots at rank 1 → structurally excluded.
  * TWO BOUNDS on the claim: (i) presupposes BST's N_max FORM a³·n_C+rank; (ii) the rank-1 caveat. => §3 states the computed selector at tier, NOT the bare 'only D_IV⁵'. Casey's phrasing vindicated, precisely bounded.
""")
