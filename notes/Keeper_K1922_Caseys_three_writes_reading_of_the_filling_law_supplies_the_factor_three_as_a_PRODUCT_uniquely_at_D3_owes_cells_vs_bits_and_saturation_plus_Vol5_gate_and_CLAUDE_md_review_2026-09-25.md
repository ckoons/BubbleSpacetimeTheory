# Keeper K1922 — Casey's "three writes" reading of the filling law; Vol 5 gate-read; CLAUDE.md review (2026-09-25)

Friday 2026-09-25, written ~14:50 EDT (clock). Rubric cell: External 4 / Internal C (Λ, the commitment ontology) for Section 1; Internal D on the presentation for Sections 2–3. `didwe` "three writes" → 0; "filling law" → Lyra's 09-22 note only. The lane is new.

## 1. Casey's mechanism (verbatim, 2026-09-25)
> "Three times faster is simple, 3 commitment writes make a single unit of 3D information. I sincerely believe each write is a single dimension of measurement. Like branches spreading in a two dimensional tree, the same one dimensional twig spreading in three dimensions creates 3D."

**Antecedent restated (Lyra, FILLING_LAW 2026-09-22, Section 1):** for ρ_DE = E_commit·N/V_H to be constant in the matter era, the committed count must obey d ln N/dt = 2H(1+ε) with ε = 2, i.e. N ∝ a⁶. The ledger as stated gives N ∝ a² (Hsu, dead on sight).

**What the reading supplies (instrument: `play/keeper_K1922_three_writes_exponent_check.py`, sha256 151b84d7dc3f5b2d…, SCORE 6/6, output `play/.out_keeper_K1922.txt`; exact rationals; no DESI input; no w-direction printed):**
- **"Make" read as a PRODUCT** (a 3D unit is one write chosen on each axis; the twig spreading in three directions): N₃ = N₁³ ∝ (a²)³ = a⁶ — **ε = 2 exactly, zero knobs.** That is the O(1) mechanism Lyra's Section 4 named as the door.
- **"Make" read as a QUOTIENT** (a unit consumes three writes): N₃ = N₁/3 — a constant factor, which cannot move a logarithmic derivative. **It supplies nothing.** The sentence must carry the product reading or it does no work.
- **Dimension check (the number is not free):** requiring the matter-era exponent D(D+1)/2 in D spatial dimensions, the product reading matches **only at D = 3**, under both natural generalizations of the ledger's "2" (area law a^(D−1), or the 2 held fixed). The control (the literal ledger at D = 3) fails as Lyra found. So the factor three is the number of spatial dimensions, and the match holds in three and in no other — a real consistency, and a clean number, so it gets scrutiny, not a wave-through (below).
- **Radiation era, same reading:** ρ_DE ∝ H⁴N ∝ a⁻⁸·a⁶ = a⁻² (w = −1/3 there). Subdominant then, but its fraction grows as a² through radiation; an early-dark-energy bound is a check that could fail. Owed as a number, not a sentence.

**Verdict: CONDITIONAL PASS as the filling-law candidate (not a derivation).** Three things it owes before it is an input list:
1. **Cells versus bits (MODERATE, the load-bearing gap).** Landauer charges per bit. The product N₁³ is a count of *cells*; the information to name one cell is 3·log₂N₁ bits, which is additive. The reading works only if each 3D cell is one commitment costing one Landauer bit — i.e. the unit of commitment is the 3D cell and the three writes are its coordinates, not three separately-charged events. The ledger must say which it counts. If writes are charged separately, the energy grows like N₁ and the factor is gone.
2. **Saturation (MODERATE).** f = N/N_H grows as a³ in the matter era; in de Sitter N_H is constant while N₁³ keeps growing, so f must stop at a ceiling (f ≤ 1 or a named one). The late-time behaviour — and therefore the sign of wₐ — lives in that clause. It is **Lyra's to write and Elie's to run blind**; I print no direction here (K1921).
3. **F799's constraint (Lyra's input (vi)).** Whatever ε(a) the product-plus-saturation gives must be completely monotone to −1 from above, or F799/T2559 is the row that dies. Pre-registered, not checked here.

**Scrutiny of the clean number (feedback: no wave-through on a perfect number).** "3 = spatial dimensions" matching "the factor three" is a clue, not a justification: both threes trace to D = 3 (matter dilutes as a⁻³ because space has three dimensions), so the match is a consistency between two readings of the same D, which is what the D-scan shows. It would be a derivation only once item 1 is settled from the commitment picture itself.

**Routing:** Lyra writes ε(a) with item 1 and a saturation clause stated before any number, appended to her Section 3 input list; Cal hashes; Elie runs blind with the direction printed first. Casey's words go into the input list verbatim.

## 2. Vol 5 gate-read against the corrected boundary paragraph (owed from K1921)
Ch01 rewrite (Sections 1–7 + tier line), Ch02 head, INDEX: **PASS.** A1 carries the register's direction in words (relaxes from above, no crossing); F2 carries no direction and names the filling law as the door; F4 = theorem; E1 = fired and lost. No "better than a percent", "located on its boundary", holography or leaked direction anywhere above the May record.
One gap (MINOR, the K1921 error in another costume): the May 43.7 Summary row "Dark energy w ≠ −1 — Prediction confirmed in direction" was covered only by the general "tables are not the register" bullet. **Fixed:** a named line in the head-note (withdrawn as a confirmation; DESI's wₐ < 0 crossing is a tension with A1, not a confirmation). PDF rebuilt.

## 3. CLAUDE.md shrink (Elie, uncommitted since 09-24) — CONDITIONAL PASS, conditions applied
Verified: 225 of 247 removed lines are verbatim in `notes/CLAUDE_md_status_history_2026-05-19_to_2026-06-09.md`; the other 22 are the Commands table (lives in `.claude/commands/README.md`) and the **Repository Layout table — dropped with no home; it was CLAUDE.md's only pointer to Guide/. Restored**, with stale counts refreshed (6,000+ notes, 5,800+ toy scripts, counted today). The shrink also **deleted `.claude/commands/take-a-break.md`**, a byte-identical twin of `take_a_break.md` that the commands README still names at line 11 — **restored** (deleting it would silently remove `/take-a-break`). PDF rebuilt. Committed on Casey's "do the other items" (09-25); revert is one command if he prefers the shrink as Elie left it.

## Owed
Lyra: ε(a) with cells-vs-bits and saturation stated (Section 1). Cal: cold read of the corrected boundary paragraph (still open from K1921) and of this Section 1. Zenodo version + front-page door sentence: unblocked by Section 3 — goes to Casey with Cal's read.

— Keeper. Counter next K1923.
