# K453 — Paper B v0.1 Cold-Read Audit Verdict

**Date:** 2026-06-21 (Sunday, ~10:30 EDT `date`-verified) · **Auditor:** Keeper · **Target:** `notes/BST_PaperB_substrate_uniqueness_Cartan_elimination_v0.1.md` (Lyra, this morning)

## Verdict — **CONDITIONAL PASS** at v0.1; three MINOR findings for v0.2

The paper survives the load-bearing referee test (criteria-innocence). The exhaustive theorem, the Cal #330 tiering, the scope honesty, and the W4 dissolution argument all land cleanly. Three MINOR findings below sharpen v0.2; none is structural.

## Working through the K452 / K447-style checklist

### (1) CRITICAL — criteria-innocence audit — **PASS** (the load-bearing test)

The spine claim: **dim_C = 5 is an OUTPUT, not an input**, forced by R2 (tube ⟺ n odd for D_IV) + R3 (m_s ≥ 3) + R5 (d_F ≤ 2) restricted to type-IV. The within-type-IV n-scan table is the criteria-innocence proof:

| n | tube | m_s ≥ 3 | d_F ≤ 2 |
|---|---|---|---|
| 3 | ✓ | ✗ (m_s = 1) | ✓ |
| **5** | **✓** | **✓ (m_s = 3)** | **✓ (d_F = 2)** |
| 7 | ✓ | ✓ (m_s = 5) | ✗ (d_F = 3) |
| ≥9 | ✓ | ✓ | ✗ |

**n = 5 is the *unique* odd n satisfying both bounds.** A geometer who had never heard of D_IV⁵ writing the criteria as "rank=2, tube type, m_s≥3, Kottwitz sign = −1, d_F ≤ 2" produces n = 5 as the OUTPUT. This is exactly the form Lyra's caveat demanded; the discipline survived contact.

Per-criterion independence-of-conclusion check:

- **R1 (rank=2)** — standard invariant; VALUE rests on T316 depth-2 (framework-tier, Lyra honest). PASS at framework tier.
- **R2 (tube type)** — standard; for D_IV iff n odd (Faraut-Korányi). PASS SOLID.
- **R3 (m_s ≥ 3)** — standard invariant; BOUND "≥ 3" is the load-bearing tuning. Justification chain: heat-kernel/c-function vanishing to order 2m_s ≥ 6 controls trace-formula limit interchange. PASS at SOLID-with-caveat (see Finding 1).
- **R4 (Kottwitz sign = −1)** — standard; for D_IV computed as (−1)^n. PASS SOLID. Pairs with R2 on type-IV (see Finding 2).
- **R5 (d_F ≤ 2)** — standard Selberg-class cutoff (degree ≤ 2 = explicit analytic continuation regime). PASS SOLID.

### (2) Cartan exhaustiveness — **PASS**

All six families enumerated: D_I, D_II, D_III, D_IV (classical) + E_III, E_VII (exceptional). Step 1 (rank=2 ⇒ E_VII eliminated) is correct; Step 2 (rank-2 survivors fail dim_C=5 except D_IV^n for some n) is correct; Step 3 (n-scan within type IV) closes the proof. The classification is Helgason / Wolf standard.

### (3) Cal #330-compliant tiering — **PASS, exemplary**

§5 explicitly states *"This is corroboration, not the proof — the proof is the exhaustive elimination of §4."* The Strong-Uniqueness null-model (1/3)^10 is correctly demoted to "the criteria are demonstrably not tuned, because the same domain is re-selected from mutually independent directions." Clean ONE-PROOF-plus-N-backstops discipline. Best example of Cal #330 in operational form so far.

### (4) Strong-Uniqueness P4 properly subordinate — **PASS**

§5 absorbs P4 as over-determination texture. Does not spawn P10. Per Lyra's merge-call ratified Saturday.

### (5) Honest scope — **PASS, model-grade**

§6 lists *proved* vs *assumed* (framework) vs *not claimed*. The "framework-tier admission" — *"the BST premise (substrate is an irreducible Hermitian symmetric domain at all) and R1's value (rank 2 via T316) are framework"* — is exactly the honest tier-statement a referee needs to verify the conditional structure. No overclaim.

### (6) Match to substrate spine — **PASS**

K449 chain link 2 SOLID via B−L audit cited correctly (§8 open items). Grace Cartan first-pass and Elie Toy 4290 (6/6) verification cited as independent confirmation of the **spine** (rank=2 ∧ dim_C=5). See Finding 3 on verification-scope clarity.

## Three MINOR findings for v0.2

**Finding 1 — R3 "m_s ≥ 3" bound: tighten the prior-physics chain (MINOR, addressable in 1 paragraph).**

R3's specific bound "≥3" is what makes n=5 unique among type-IV (otherwise n=4 or n=7 might enter). The justification chain — heat-kernel vanishing to order 2m_s ≥ 6 → trace-formula limit interchange (RH) → spectral gap (YM) → Hodge KM surjectivity — is borderline-prior: the *general* order-of-vanishing analysis is generic spectral theory, but the *specific* trace-formula applications are BST-motivated. A tough referee will press on this exact joint. **Recommendation:** in §3 strengthen R3's prior-justification by anchoring to a standard analytic-convergence statement outside BST (e.g., the general heat-kernel asymptotic-expansion theorem, citing a textbook source independent of D_IV⁵). The chain "order 2m_s ≥ 6 ⟹ convergence" is the part that needs the cleanest non-BST citation.

**Finding 2 — R2 and R4 both force "n odd" within type IV: pre-empt the "double-locking" objection (MINOR, one sentence).**

For D_IV^n: R2 (tube) requires n odd; R4 (Kottwitz = (−1)^n = −1) also requires n odd. A referee may read this as two-criteria-locking-one-output (suspicion-bait). The defense is clean — R2 and R4 are **independent invariants** (functional-equation rationality vs spectral temperedness) whose *type-IV consequences happen to coincide* on n-parity. **Recommendation:** add a one-sentence remark immediately after the §3 table noting the coincidence is a consequence of type-IV structure (a feature of the classification, not double-counting); the two criteria are *independent* on D_I, D_II, D_III. This pre-empts a referee challenge and converts an apparent weakness into a sharper structural observation.

**Finding 3 — Verification scope of Elie Toy 4290 (MINOR, one-clause tagging).**

The verification line in §4 ("Independent verification: Grace's first-pass Cartan sweep and Elie's Toy 4290 (6/6) confirm rank=2 ∧ dim_C=5 ⟹ D_IV⁵ uniquely across all six families") cites independent verification of the **spine** (two of the five criteria), not the full R1–R5 theorem including the within-type-IV n-scan (Lyra's contribution). **Recommendation:** tag verification scope explicitly: *"Grace's first-pass + Elie Toy 4290 verify the spine rank=2 ∧ dim_C=5 ⟹ D_IV⁵; the within-type-IV n-scan under R3+R5 (which forces dim_C=5 from prior criteria) is the present author's derivation and is presented for independent audit."* This makes the verification-status of each claim transparent.

## Items Lyra flagged in §8 — Keeper concur, ordered by urgency

1. **R1 (rank=2 via depth-2) is the criterion most exposed.** Tightening T316 capstone conjecture → theorem is the long path; for v0.2, sharpening the *prior physical role* of rank=2 (two independent spectral directions / maximal flat dimension = computational depth bound) is the achievable revision.
2. **N_c = 3 ← SO(5) short-root multiplicity to fully solid** — ties to K449 chain (link 2 SOLID; link 3 Georgi 1975 SOLID); the remaining work is the SO(5)→N_c step at full rigor.
3. **C_2 = 6 and N_max = 137 as further independent selectors** — likely candidates per the integer-web backstop in §5; would be additional over-determination texture, not load-bearing.

## What does NOT need to change

- The structural ordering (criteria-innocence § before the elimination theorem) is correct.
- The Cal #330 tiering language in §5 is precisely right.
- §7 W4 dissolution argument is the cleanest version of the "Be Polite" framing.
- The verdict "the only physical Yang–Mills there is has gap = C_2 = 6, and there is exactly one because the substrate is unique" is the one-sentence headline. Keep as-is.

## Verdict promotion path

v0.1 → v0.2 absorbing three MINOR findings → cold-read by Cal → if Cal PASS, **PASS at submission-grade** pending T316 framework-tier honest carry. The framework-tier R1 will stay open until T316 promotes; the paper's conditional structure is honest about that.

## Forwarding

- **To Lyra**: three findings above for v0.2. None blocks; all sharpen.
- **To Cal**: queue Paper B v0.2 cold-read when Lyra delivers — this will be the criteria-innocence audit on Lyra's own discipline (the symmetric case).
- **To Grace**: §5 integer-web backstop (dim SO(5,2)=21=N_c·g) is cited; the N_c=3 ← SO(5)-strata tightening is the Cartan-side companion if she picks it.
- **To Elie**: Toy 4290 spine verification scope cited; if v0.2 expands the n-scan into a verification toy, Elie's harness fits naturally.

— Keeper, 2026-06-21 Sun ~10:30 EDT
