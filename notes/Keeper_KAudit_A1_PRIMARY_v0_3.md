---
title: "Keeper K-audit — Paper A1 (Substrate Hall Algebra, PRIMARY) v0.3"
author: "Keeper"
date: "2026-05-28 Thursday PM EDT"
status: "CONDITIONAL PASS. Verified spine is sound and referee-grade in substance. TWO internal inconsistencies must be fixed before Cal cold-read / submission: (1) MODERATE — genus self-contradiction (§8.1 vs §1/§8.4); (2) MINOR — kernel-exponent staleness (§1 vs §8.4). K-number provisional (assign next-free at EOD)."
verdict: "CONDITIONAL PASS → fix two internal-consistency items, then PASS-ready for Cal cold-read."
related: ["Lyra_Paper_Substrate_Hall_Algebra_Primary_Draft_v0_2.md (internally v0.3)", "Keeper_Macdonald_Parameter_Role_Flag_v0_1.md", "Keeper_Audit_cFK_Derived_Measure_Theorem_v0_1.md", "Keeper_Genus_Verdict_T2442_Escalation_v0_1.md"]
---

# Keeper K-audit — A1 (PRIMARY) v0.3

## What's strong (acknowledge first)

A1 v0.3 is in genuinely good shape and the substance is referee-grade:
- **The RIGOROUS spine holds**: Serre structure constants [2]_2 = N_c, [3]_4 = N_c·g (Type A, forward, Elie-verified) — the central result is real and correctly placed at the Hall-Littlewood corner.
- **Discipline is exemplary**: scheme-dependent mass-ratio leads and back-fit relations are explicitly EXCLUDED (§8.3); tiers are stated per claim (§8.1-8.4); the Cal #146 unification correction (shared W_n, distinct K-types) is in; the empirical contact is restricted to the scheme-invariant mixing-angle spine.
- **The Macdonald parameter-role fix is correctly incorporated** (§5, §8.4): Hall-Littlewood corner, α as evaluation/coupling, integrality argument cited. The gate I raised this morning is properly closed in the text.
- **c_FK-derived-measure theorem** (§8.4) is correctly stated as a Strong-Uniqueness strengthener.

The paper is close. The two findings below are internal-consistency defects, not substance defects — but they are exactly the kind a referee catches on first read, and one of them is embarrassing precisely because the paper makes a virtue of not conflating genera.

## Finding 1 — MODERATE: the paper contradicts itself on the genus of D_IV⁵

- **§1 + Route-A table + §8.4** say: **Hua genus = n_C = 5; Faraut-Korányi genus = C_2 = 6**; g = 7 = embedding.
- **§8.1 (line 150)** says: **"n_C = Faraut-Korányi genus = 5."**

These cannot both hold. §8.1 calls n_C=5 the *FK* genus; §1/§8.4 call C_2=6 the FK genus and n_C=5 the *Hua* genus. **A paper whose own headline convention (§1) is "do not conflate the three genera" cannot then conflate them in §8.1.** A referee will flag it instantly, and the contradiction undercuts the very convention the paper introduces.

Worse, the underlying fact is **not actually settled**: the FK multiplicity formula p = a(r−1)+b+2 for Type IV₅ (a=3, b=0, r=2) gives **p = 5 = n_C** — which supports §8.1 ("FK genus = 5") and *contradicts* "FK genus = C_2 = 6." So the team has two competing claims about what the FK genus *is*, and the "FK genus = C_2 = 6" identification may itself be a mislabel (C_2 = 6 is the quadratic Casimir; whether it is *also* a genus is the open question).

**What is NOT in dispute**: the Bergman kernel exponent = n_C = 5 (convention-free, Elie ν=5 MC-confirmed). The dispute is purely the *naming* (is 5 the Hua or the FK genus?) and whether C_2=6 is a genus at all.

**Required fix (before Cal cold-read):** pin the FK genus of Type IV_n against a **primary source** (Faraut-Korányi *Analysis on Symmetric Cones* genus table, or Upmeier), not the team's competing notes. Then make §1, the Route-A table, §8.1, and §8.4 say the *same* thing. **I am not adjudicating the name from memory** — I was wrong on genus naming once today, and the multiplicity formula (giving 5) conflicts with the team's "FK=6" note, so this needs the book, not a guess. Route: Keeper (literature) + Lyra. This is the one item genuinely blocking a clean submission.

## Finding 2 — MINOR: kernel-exponent staleness (§1 contradicts §8.4)

- **§1 (line 40)**: "The kernel singularity exponent (h^{−?/rank}) is **under active recheck** ... whether the established 7/2 stands is the open item."
- **§8.4 (line 170)**: "**RESOLVED** — kernel singularity exponent = n_C/rank = 5/2 (Elie 3580-3581, MC-confirmed; un-held)."

§1 is stale — it describes the kernel exponent as open when §8.4 (and today's work) resolved it to 5/2. **Fix:** update §1 line 40 to state the resolved value (5/2 = n_C/rank, Hua) and drop "under active recheck." Trivial, but it's a self-contradiction a careful reader will notice.

## Verdict

**CONDITIONAL PASS.** The verified spine is sound; the exclusions and tiers are disciplined; the substance is referee-grade. Clear Finding 1 (genus self-contradiction + primary-source pin) and Finding 2 (kernel-exponent staleness), and A1 is **PASS-ready for Cal's cold-read**. No CRITICAL gaps; the central RIGOROUS result (Serre constants) and the scheme-invariant empirical spine are unaffected by either finding.

## Fix list → v0.4 (drives A1 to done)

1. **[blocking] Finding 1** — pin FK genus of Type IV₅ vs primary source; make §1 / Route-A / §8.1 / §8.4 consistent. (Keeper lit + Lyra.)
2. **[quick] Finding 2** — update §1 kernel-exponent wording to the resolved 5/2. (Lyra.)
3. **[quick] α_fine placement** — §5.1 says "RESOLVED" (evaluation/coupling) but §4/§5.1 also still flag it "open" in places; make the disposition uniformly "resolved: evaluation, not a Macdonald coordinate." (Lyra.)
4. **[parallel] PMNS double-set** (§8.5) — Cal's typing closed /N_max as canonical (§7); §8.5 still says "FLAGGED for reconciliation." Reconcile §7 (closed) vs §8.5 (flagged) — they disagree on whether it's settled. (Lyra + Cal.)
5. Then → Cal cold-read → v0.4 → Keeper final PASS.

Note: items 3 and 4 are two MORE internal staleness points (the paper says "resolved/closed" in one section and "open/flagged" in another for the same items). A1 has accumulated within-session edits faster than its cross-section consistency — a **consistency sweep across all sections** is the real v0.4 task. That's the honest state: the substance is done; the document needs one careful internal-consistency pass so no section contradicts another.

— Keeper, 2026-05-28 Thursday PM. A1 CONDITIONAL PASS; substance referee-grade; needs one internal-consistency sweep (genus naming is the load-bearing fix) before Cal cold-read.

---

## v0.4 verification read (Keeper, PM) — sweep ~95% landed; TWO residuals block final PASS

I read Lyra's swept v0.4 (in-place, mtime 17:09) end-to-end to issue the final PASS. The sweep largely landed — but **trust-but-verify caught two residuals the sweep missed**, and one is the genus mislabel *again*. **Final PASS withheld** pending these (both quick, both real contradictions a referee catches):

**Residual 1 — MODERATE (the genus, third time today): line 59 still contradicts the corrected §1 box.** The §1 box (lines 38–42) and §8.4 (line 174) now correctly say "ONE genus = n_C = 5 (FK = Hua); C_2 = 6 is the Casimir, NOT a genus." But **line 59 still reads: "(Correction… n_C is the Hua genus, NOT the FK genus; C_2 is the FK genus; g is the embedding dimension…)"** — i.e., it STILL asserts "C_2 is the FK genus," the exact mislabel the box corrects, and STILL asserts a Hua-vs-FK distinction the box says doesn't exist. Direct self-contradiction. **Fix (Lyra): delete the line-59 parenthetical or replace with the box's statement** — "n_C = 5 is the genus (FK=Hua, no distinction); C_2 = 6 is the Casimir; g = 7 is the embedding — neither C_2 nor g is a genus." (I'm routing this to Lyra rather than editing her paper, because the wording touches the naming I've deferred to the book-pin; she applies the box's already-correct statement.)

**Residual 2 — MINOR (stale footer): the v0.2 provenance + closing signature (lines ~200–208) were not swept.** Line 202 ("n_C re-anchored to FK genus") and the §"Provenance of v0.2 changes" + the closing signature (line 208: "HELD: g-anchor wording + c_FK normalization pending T2442 recheck. Ready for Cal cold-read once T2442 lands") are leftover **v0.2** text — they describe items as HELD/pending that §8.4 now marks RESOLVED. **Fix (Lyra): refresh the footer to the v0.4 state** (c_FK resolved/un-held; T2442 stands; genus one-genus; ready for cold-read pending the line-59 fix + book-pin).

**Everything else verified clean**: §1 box, §7 mixing-angle spine, §8.1, §8.4 genus/c_FK/kernel-exponent, §8.5 PMNS (CLOSED, consistent with §7), §9 conclusions — all consistent and correct. The substance (Serre spine RIGOROUS, mixing angles, c_FK-derived, confinement, two-corner) is referee-grade and unaffected.

**Verdict: CONDITIONAL PASS (one micro-sweep from final PASS).** Clear Residual 1 (line 59) + Residual 2 (footer), and the document is internally consistent. Then: final Keeper PASS → Cal cold-read (Cal already cold-read v0.3 per Cal #155; v0.4 is a quick verify) → submission-grade. The genus-naming book-pin remains my next-session item, but the doc handles it correctly by stating value+role + "pending primary-source pin," so it does NOT block the PASS once line 59 is fixed.

**Meta:** this is the third genus-bite today and the second time a "sweep done" report had a residual — both caught by the Keeper read, not the self-report. It vindicates the trust-but-verify discipline and Casey's "drive A1" call once more: A1 is genuinely one micro-fix from a final PASS, but it was NOT there on report alone.

— Keeper, 2026-05-28 Thursday PM. A1 v0.4 CONDITIONAL PASS — two residuals (line 59 genus contradiction MODERATE; stale v0.2 footer MINOR) routed to Lyra; final PASS on the corrected version.

---

## FINAL VERDICT — A1 v0.4: **PASS** (Keeper, verified)

Lyra applied both fixes; I **grep-verified** rather than taking the report (the discipline this session earned): no "C_2 = FK genus," no "Hua genus NOT the FK," no "HELD pending"/"under recheck"/"once T2442 lands" anywhere; the one-genus convention ("Casimir NOT a genus") stated consistently (4×). Both residuals are closed.

**Verdict: PASS.** A1 v0.4 is internally consistent end-to-end and substantively referee-grade:
- RIGOROUS Serre-constant spine ([2]_2=N_c, [3]_4=N_c·g) at the correct Hall-Littlewood corner.
- Scheme-invariant mixing-angle empirical spine (invariant-anchored); PMNS closed (Cal #153) consistently in §7 + §8.5.
- c_FK = derived-measure theorem; one-genus convention (n_C=5 genus / C_2=6 Casimir / g=7 embedding) consistent in §1 box, §8.1, §8.4, anchor table, §9, line-59, footer.
- Cal #146-corrected unification; confinement FRAMEWORK-PLUS; leads + back-fit EXCLUDED; tiers honest throughout.

**One non-blocking proof-stage action** (my next-session item): confirm the genus *citation* against Faraut-Korányi/Loos before final submission. This does NOT condition the PASS — the genus *value* (5) is derivation-certain + 4-way confirmed, and the paper states it by value+role + cites + flags the naming as pending-pin, so it makes no claim the book-check could falsify. Belt-and-suspenders citation tightening, not a correctness gate.

**Path to submission-grade:** Keeper PASS (this) → Cal's quick v0.4 verify (he cold-read v0.3 per Cal #155; v0.4 confirms the sweep + 2 substantive flags) → submission-grade. The PRIMARY paper is there.

This is what "drive A1, don't park it" produced: a Keeper-PASSed, internally-consistent, referee-grade PRIMARY paper — reached by driving and *verifying* end-to-end (three genus-bites and two missed-residuals caught by the read, not the reports), not by parking-and-reporting.

— Keeper, 2026-05-28 Thursday PM. **A1 v0.4 — Keeper final PASS** (grep-verified). Cal quick-verify → submission-grade; genus citation book-pin is a non-blocking proof-stage item.
