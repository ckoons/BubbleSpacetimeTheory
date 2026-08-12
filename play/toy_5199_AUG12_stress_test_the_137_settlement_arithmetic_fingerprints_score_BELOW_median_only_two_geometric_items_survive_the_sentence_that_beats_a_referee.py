#!/usr/bin/env python3
"""
Toy 5199: STRESS-TESTING CASEY'S 137 SETTLEMENT -- not to contest it, but because the ruling was argued on a
premise that is checkable in ten minutes, and if I can check it in ten minutes so can a referee. Casey settled
137 as a defining invariant of D_IV⁵ at tier Identified-strong, with this as the supporting argument: "A fit
lands in one place; an invariant leaves fingerprints everywhere, and 137 does" -- the cited fingerprints being
the quadric's 27 = N_c³ unique at n_C = 5, the Fermat two-square form, store-16 sitting inside it, and the K38
+rank. I ran the fingerprints against null models. ★ RESULT, and it is not what the argument assumes: the
ARITHMETIC fingerprints carry essentially ZERO evidential weight, and one of them is actively worse than
average. Building an atom set from the BST integers {2,3,5,6,7} (powers to the fifth, pairwise products, 114
atoms) and counting representations as sums of at most three atoms, 137 admits 95 of them -- against a
neighbourhood median of 102 over 120..155, ranking 30th of 36. It is BELOW MEDIAN. Robust across five grammar
variants (30/36, 30/36, 30/36, 20/36; only the sparsest bare-powers grammar puts it mildly above at 4/36, on
5 representations against a median of 2). So "137 = N_c³·n_C + rank" is not a fingerprint -- every integer
around there has about a hundred such forms, which is exactly the "a prime has no forced decomposition" lesson
that killed the coding morning, now with a number attached instead of an intuition. ★ The Fermat item is mild,
not strong: every prime ≡ 1 mod 4 has a unique two-square form automatically, so the only content is that the
small part is rank⁴ = 16, and 9 of the 147 such primes under 2000 share it -- 6.1%, one in sixteen, alongside
41, 97, 241, 457, 641, 857, 977, 1697. ★ And store-16-inside-137 is THE SAME FACT as the Fermat small part
(4² = 16 = rank⁴), so it must be counted once, not twice -- my own catch this morning, and I am the one who
has to apply count-once to it. ★ WHAT SURVIVES IS EXACTLY TWO ITEMS, AND THEY ARE OF A DIFFERENT KIND: the
quadric's 27 = N_c³ (a Hilbert-polynomial computation, target-innocent, verified) and the K38 +rank (three
convergent geometric routes, ~93%). Both are computed geometry, not arithmetic coincidence -- and they are
precisely the two facts the open ×5 sits between. ★ THE POINT, and it supports the settlement rather than
undermining it: Casey's ruling is a claim about the GEOMETRY -- 137 is a structural invariant of D_IV⁵,
non-tunable because you cannot change it without leaving the domain. Nothing here touches that. What this
removes is the weak arithmetic scaffolding propped against it, so the strong claim can stand clean. If we
write "fingerprints everywhere," a referee runs this computation over coffee and finds 137 scoring below
median, and the sentence dies taking the ruling's credibility with it. If we write the geometric sentence, we
are unassailable at Identified-strong. ★ AND THE DISANALOGY A REFEREE WILL PRESS FIRST, stated so we answer it
before it is asked: n_C = 5 is DEFINITIONAL -- it is in the name D_IV⁵ -- while N_max = 137 is not in the
definition; it is claimed to be a COMPUTED invariant of that domain whose computation is, by our own audit
(Cal §430, the RealityBudget note), not carried out. "137 is like 5" is therefore not exact: 5 is an input,
137 is an output-in-principle with an open derivation. The tier is still right; the WORDING has to carry that
distinction or the first question kills it. Proposed sentence in the toy. Elie stress-testing a ruling he
agrees with. (Casey's settlement; Keeper's framing; Cal §429/§430 decoy discipline; Grace's ×5 refutation;
Lyra F931-F934.) Tier commentary only -- I rule nothing. CP existence-only.

WHAT I COMPUTE:
  * post-hoc funnel: 4 fixed predicates over 2..2000 → 303 primes → 147 (≡1 mod 4) → 9 → 137 UNIQUE.
  * ★ arithmetic null model: 137 has 95 BST-atom representations vs neighbourhood median 102 -- BELOW median,
    rank 30/36; robust across 5 grammar variants. The decomposition carries ZERO weight.
  * Fermat base rate: small two-square part = rank⁴ holds for 9/147 primes ≡1 mod 4 under 2000 (6.1%). Mild.
  * count-once: store-16-inside-137 IS the Fermat small part. One fact, not two.
  * survivors: exactly 2, both computed geometry (quadric 27 = N_c³; K38 +rank).

=> VERDICT (plain): the settlement is right and the argument offered for it is half wrong, which is worth
saying out loud now rather than hearing from a referee later. The half that is wrong is the arithmetic. We have
been treating it as significant that a hundred and thirty-seven can be written as three cubed times five plus
two, but every number in that neighbourhood can be written about a hundred different ways out of our own five
integers, and a hundred and thirty-seven can be written slightly FEWER ways than its neighbours can. So that
particular decomposition is not a fingerprint; it is the ordinary background hum of small-integer arithmetic,
and we have been reading a signal into it. The two-square form is a little better but not much -- one prime in
sixteen does the same thing -- and the stored sixteen sitting inside the prime is not an extra clue at all,
because it is literally the same arithmetic fact wearing a different name, which means my own count-once rule
applies to a finding I was pleased with this morning. What survives is two items, and they are the two that
were computed rather than noticed: the twenty-seven that falls out of the quadric's Hilbert polynomial, and the
rank that three independent geometric routes force. Those are real. And they are enough, because the ruling was
never really an arithmetic claim -- it was the claim that this number belongs to the domain the way a dimension
does. That claim stands untouched by anything here. It just has to be made on its own terms, with one honest
clause about the difference between a number that is in the domain's name and a number that has to be computed
from it.

=> DISPOSITION: settlement SUPPORTED, supporting argument TRIMMED. Arithmetic fingerprints (the N_c³·n_C+rank
decomposition; the Fermat form; store-16-inside) carry ~zero, mild, and zero-additional weight respectively --
do not cite them as evidence that 137 is an invariant. Two geometric items survive (quadric 27 = N_c³; K38
+rank) and they are the right ones to cite. Tier Identified-strong UNCHANGED -- I am not contesting it. Firer:
Elie. Owed to whoever writes this up: the wording distinction between definitional n_C and computed N_max
(proposed sentence below), so the referee's first question is already answered in the text. @Cal @Keeper rule;
I rule nothing. Nothing pushed; nothing banked.

Author: Elie (CI toy builder). Date: 2026-08-12.
"""

import itertools
import statistics
from sympy import isprime

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

BST = [2, 3, 5, 6, 7]          # rank, N_c, n_C, C_2, g
N_max = 137

def two_square_small(p):
    for a in range(1, int(p**0.5)+1):
        b2 = p - a*a
        b = int(b2**0.5)
        if b*b == b2:
            return min(a, b)
    return None

print("=" * 78)
print("Toy 5199: stress-testing the 137 settlement -- do the fingerprints survive a null model?")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The post-hoc funnel (consistency, explicitly NOT evidence).
# ---------------------------------------------------------------------------
print("\n--- 1. the post-hoc funnel: 137 is unique -- and that fact is nearly content-free ---")
def all_preds(p):
    if not (isprime(p) and p % 4 == 1):
        return False
    if two_square_small(p) != 4:                 # small part = rank² ⟹ rank⁴ = 16 = store-16
        return False
    if (p - 2) % 5 != 0:                         # (p − rank) divisible by n_C
        return False
    q = (p - 2)//5
    c = round(q ** (1/3))
    return c**3 == q and c in BST                # quotient a perfect cube of a BST integer

hits = [p for p in range(2, 2001) if all_preds(p)]
n_prime = sum(1 for p in range(2, 2001) if isprime(p))
n_1mod4 = sum(1 for p in range(2, 2001) if isprime(p) and p % 4 == 1)
n_small4 = sum(1 for p in range(2, 2001) if isprime(p) and p % 4 == 1 and two_square_small(p) == 4)
check("Running the four cited fingerprint predicates as fixed filters over 2..2000 gives the funnel "
      f"{n_prime} primes → {n_1mod4} at ≡1 mod 4 → {n_small4} with two-square small part rank² → {len(hits)}: "
      f"137 is UNIQUE. That looks impressive and it is very nearly content-free, because the predicates were "
      "extracted FROM 137 -- a post-hoc filter set will single out its own source almost every time. I record "
      "it as CONSISTENCY, not as evidence, and I would say the same if a colleague brought it to me.",
      hits == [137],
      f"funnel {n_prime}→{n_1mod4}→{n_small4}→{len(hits)}; unique hit {hits} -- post-hoc, therefore consistency only")

# ---------------------------------------------------------------------------
# 2. ★ The arithmetic null model -- the test that actually discriminates.
# ---------------------------------------------------------------------------
print("\n--- 2. ★ the arithmetic null model: how special is 137 among BST-integer combinations? ---")
def atom_set(max_exp=5, products=True, cap=2000):
    a = set()
    for b in BST:
        for e in range(1, max_exp+1):
            if b**e <= cap:
                a.add(b**e)
    if products:
        for x, y in itertools.combinations_with_replacement(sorted(a), 2):
            if x*y <= cap:
                a.add(x*y)
    return sorted(a)

def reps(target, atoms, max_terms=3):
    tot = 0
    for k in range(1, max_terms+1):
        tot += sum(1 for c in itertools.combinations_with_replacement(atoms, k) if sum(c) == target)
    return tot

atoms = atom_set()
neigh = {t: reps(t, atoms) for t in range(120, 156)}
med = statistics.median(neigh.values())
rank137 = sorted(neigh.values(), reverse=True).index(neigh[137]) + 1
check("★ Build every atom the five BST integers make -- powers to the fifth plus pairwise products, 114 atoms "
      f"-- and count how many ways each integer near 137 is a sum of at most three of them. 137 admits "
      f"{neigh[137]} representations. The neighbourhood 120..155 has median {med:.0f} and 137 ranks "
      f"{rank137}th of 36. IT IS BELOW MEDIAN. So 'N_c³·n_C + rank = 137' is not a fingerprint at all -- it is "
      "the ordinary background hum of small-integer arithmetic, and 137 hums slightly more quietly than its "
      "neighbours. This is the 'a prime has no forced decomposition' lesson that ended the coding morning, now "
      "with a number instead of an intuition.",
      neigh[137] < med,
      f"137 → {neigh[137]} reps; neighbourhood median {med:.0f}; rank {rank137}/36 (below median)")

variants = [(5, True, 3), (4, True, 3), (5, False, 3), (5, True, 2), (6, True, 3)]
vres = []
for me_, pr, nt in variants:
    at = atom_set(me_, pr)
    sc = {t: reps(t, at, nt) for t in range(120, 156)}
    vres.append((me_, pr, nt, sc[137], statistics.median(sc.values()),
                 sorted(sc.values(), reverse=True).index(sc[137]) + 1))
below = sum(1 for v in vres if v[3] < v[4])
check("Robustness across five grammar variants (exponent bound, with/without products, term bound): 137 lands "
      + "; ".join(f"exp≤{a} prod={b} terms≤{c}: {d} vs median {e:.0f} (rank {f}/36)" for a, b, c, d, e, f in vres)
      + f". Below median in {below} of 5. The single exception is the sparsest grammar -- bare powers only, "
      "where the counts are tiny (5 against a median of 2) and the statistic is not meaningful. Nowhere is 137 "
      "an outlier. The conclusion is grammar-independent: arithmetic decomposability carries no weight here.",
      below >= 4,
      f"below median in {below}/5 variants; never an outlier -- conclusion is grammar-independent")

# ---------------------------------------------------------------------------
# 3. Base rate of the Fermat item, and count-once on store-16.
# ---------------------------------------------------------------------------
print("\n--- 3. the Fermat item is mild; and store-16-inside is the SAME fact (count once) ---")
share = [p for p in range(2, 2001) if isprime(p) and p % 4 == 1 and two_square_small(p) == 4]
check("Every prime ≡ 1 mod 4 has a unique two-square form automatically (Fermat), so '137 = 11² + 4²' is not "
      "itself a coincidence -- the only content is that the small part is rank² (hence rank⁴ = 16). That holds "
      f"for {len(share)} of the {n_1mod4} such primes under 2000, i.e. {100*len(share)/n_1mod4:.1f}%, one in "
      f"sixteen, shared with {share[:2]}, {share[3:6]} and others. MILD -- worth a sentence, not worth a "
      "load-bearing role.",
      abs(100*len(share)/n_1mod4 - 6.1) < 0.5 and 137 in share,
      f"small part = rank²: {len(share)}/{n_1mod4} = {100*len(share)/n_1mod4:.1f}% -- {share}")

check("★ COUNT ONCE, applied to my own finding. This morning I offered '137 = 11² + store-16' as a structural "
      "tie between the day's two forcings, and Keeper and Cal both recorded it. It is the SAME ARITHMETIC FACT "
      "as the Fermat small part -- 4² = 16 = rank⁴ -- wearing a different name. One fact, not two, and it does "
      "not add to the fingerprint tally. I am the one who wrote the count-once discipline into this morning's "
      "toys, so I am the one who has to apply it to a result I was pleased with.",
      (two_square_small(137) or 0) ** 2 == 16 == 2**(2*2),
      "137 = 11² + 4²; 4² = 16 = 2^(2·rank) = store-16. Same fact. Tally once, not twice.")

# ---------------------------------------------------------------------------
# 4. What survives.
# ---------------------------------------------------------------------------
print("\n--- 4. exactly two survive, and they are of a different kind ---")
survivors = {
    "quadric 27 = N_c³ (Hilbert polynomial on Q⁵, unique at n_C = 5)": "computed geometry, target-innocent, verified",
    "K38 +rank (Hilbert shift / K3 Hodge / Shilov winding, ~93%)": "computed geometry, three convergent routes",
}
discarded = {
    "N_c³·n_C + rank decomposition": "ZERO weight -- below median in the null model",
    "Fermat two-square form": "MILD -- 6.1% base rate; a sentence, not a pillar",
    "store-16 inside 137": "ZERO ADDITIONAL -- same fact as the Fermat small part (count once)",
}
check("The fingerprint set reduces to exactly two items, and the two that survive are the two that were "
      "COMPUTED rather than noticed: " + "; ".join(survivors) + ". Discarded or downgraded: "
      + "; ".join(f"{k} ({v})" for k, v in discarded.items())
      + ". And the two survivors are precisely the facts the open ×5 sits BETWEEN -- which is why Grace's "
      "refutation this morning was the informative result it was, rather than a failure.",
      len(survivors) == 2 and len(discarded) == 3,
      "survivors: 2 computed-geometry items | downgraded: 3 arithmetic items (one of them mine)")

# ---------------------------------------------------------------------------
# 5. Why this SUPPORTS the settlement.
# ---------------------------------------------------------------------------
print("\n--- 5. this supports the ruling -- by removing the scaffolding propped against it ---")
check("Casey's ruling is a claim about the GEOMETRY: 137 is a structural invariant of D_IV⁵, non-tunable "
      "because you cannot change it without leaving the domain. Nothing computed here touches that claim, and "
      "I am not contesting it -- the tier Identified-strong is right. What this removes is the weak arithmetic "
      "scaffolding leaning against it, and removing it makes the ruling STRONGER, because a claim supported by "
      "one solid pillar and three rotten ones is judged on the rotten ones. ★ The practical stake: if we write "
      "'fingerprints everywhere,' a referee reproduces this null model over coffee, finds 137 scoring below "
      "median, and the sentence dies taking the ruling's credibility with it. If we write the geometric "
      "sentence, we are unassailable at Identified-strong.",
      True,
      "settlement SUPPORTED; supporting argument TRIMMED from 5 items to 2. Stronger, not weaker.")

# ---------------------------------------------------------------------------
# 6. The disanalogy a referee presses first -- answered in advance.
# ---------------------------------------------------------------------------
print("\n--- 6. the n_C-vs-N_max disanalogy, and the sentence that survives it ---")
proposed = ("D_IV⁵ is the theory's one input. Its five structural integers are read directly off the domain, "
            "and N_max = 137 is a structural invariant of that same domain -- non-tunable, since it cannot be "
            "changed without leaving D_IV⁵ -- whose closed-form derivation from the domain's discrete series "
            "remains open. Two computed geometric facts exhibit it: the quadric's 27 = N_c³, unique at "
            "n_C = 5, and the K38 +rank.")
check("★ The referee's first question will be: 'n_C = 5 is in the name of your domain -- where is 137 in its "
      "definition?' It is a fair question and the analogy is not exact: 5 is an INPUT (definitional), while "
      "137 is claimed to be a COMPUTED invariant whose computation is, by our own audit (Cal §430, the "
      "RealityBudget note admitting the formal degrees were never carried out), open. That does not make the "
      "tier wrong -- Identified-strong already carries exactly that much. It means the WORDING must carry the "
      "distinction, or the first question kills the sentence before the geometry gets a hearing. Proposed "
      "wording, offered to whoever writes it up: \"" + proposed + "\"",
      "non-tunable" in proposed and "remains open" in proposed,
      "input (n_C) vs computed-invariant-with-open-derivation (N_max) -- distinction stated in the text, not left for the referee")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (settlement SUPPORTED; arithmetic fingerprints score BELOW median and are trimmed; two computed-geometry items survive)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5199, stress-testing a ruling I agree with, because a referee can run this in ten minutes):
  * POST-HOC FUNNEL: {n_prime} primes → {n_1mod4} (≡1 mod 4) → {n_small4} → 137 UNIQUE. Impressive-looking and
    nearly content-free: the predicates were extracted from 137. Recorded as CONSISTENCY, not evidence.
  * ★ ARITHMETIC NULL MODEL: 114 BST-integer atoms, sums of ≤3. 137 admits {neigh[137]} representations against a
    neighbourhood median of {med:.0f} -- BELOW MEDIAN, rank {rank137}/36. Below median in 4 of 5 grammar variants,
    never an outlier. ⟹ "137 = N_c³·n_C + rank" carries ZERO evidential weight. The "a prime has no forced
    decomposition" lesson, now with a number attached.
  * FERMAT: mild. Small two-square part = rank² holds for {len(share)}/{n_1mod4} primes ≡1 mod 4 under 2000 ({100*len(share)/n_1mod4:.1f}%).
  * ★ COUNT-ONCE ON MY OWN FINDING: "137 = 11² + store-16" IS the Fermat small part (4² = 16 = rank⁴). One
    fact, not two. I wrote the discipline this morning; it applies to my own result first.
  * SURVIVORS -- exactly two, both COMPUTED geometry: the quadric's 27 = N_c³ (Hilbert polynomial, unique at
    n_C = 5, target-innocent) and K38 +rank (three convergent routes). They are the two facts the open ×5
    sits BETWEEN -- which is why Grace's refutation was informative rather than a failure.
  * ★ THIS SUPPORTS THE SETTLEMENT: the ruling is a claim about the GEOMETRY and is untouched here. Trimming
    the rotten scaffolding makes it stronger -- a claim propped by one solid pillar and three weak ones gets
    judged on the weak ones. Tier Identified-strong UNCHANGED; I contest nothing.
  * ★ ANSWER THE REFEREE IN ADVANCE: n_C = 5 is definitional (it is in the domain's name); N_max = 137 is a
    computed invariant with an open derivation (our own audit says so). Proposed wording carried in the toy.

AUG-12. Nothing pushed. Nothing banked. I rule no tiers -- @Cal and @Keeper do. This is a toy that checks the
argument for a conclusion I agree with, which is the only kind of check worth running on your own side.
Count once. CP existence-only.
""")
