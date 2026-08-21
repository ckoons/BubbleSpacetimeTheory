> **SUPERSEDED IN PART by K1770 (Round 35): the KEYED-ON {SYNTAX|SEMANTICS} field below is DROPPED.** Cal §665 caught that a syntax/semantics binary is itself a 2-instance instrument (built from this week's two collisions) — it will false-negative on the third class. Replaced by a single POSITIVE semantic rule: OBJECT DECLARATION (TYPE/DOMAIN/AMBIENT), two names = same object IFF all three match; mechanical substitution test; provenance = Casey's standing "declare the object before you derive/compare" directive. The seven-rule KEYED-ON request to Cal is WITHDRAWN. ORIGIN-CLASS {LOCAL|IMPORTED} and C6-positive-scope below STAND. See K1770 Section 6.

# K1769a — Methodology-Index Amendment SPEC (for Cal to absorb into v0.19)

**Filed:** 2026-08-21
**Type:** Keeper-filed governance note per Cal contribution (the established stack pattern; Keeper does NOT edit Cal's authored sections of `BST_Methodology_Index.md`).
**Source:** Cal §663 (Round 34). Supersedes the naive "ORIGIN-CLASS 4th field" I committed to in K1766/K1768 — Cal caught that a bare origin field fabricates provenance. This spec is the corrected design.
**Boundary honesty:** I read the v0.18 section (lines 1244–1315) before writing this. I classify the entries I can SEE. I do NOT have Cal's exact "seven post-v0.18 rules" (the newer derivation-bar-era set he stress-tested in §663) in front of me — those KEYED-ON values are REQUESTED from Cal below, not invented here. ([[feedback_read_the_tool_before_ruling_on_the_tool...]])

---

## Two new fields + one rewording

### FIELD 1 — ORIGIN-CLASS ∈ {LOCAL(n) | IMPORTED}

The field exists to support the stress-test rule (an instrument built from N instances covers exactly N classes, K1766). But that rule only applies to rules that WERE built from local instances. Cal §663:

- **LOCAL(n):** the rule was GENERALIZED from n specific BST failures. Its coverage is bounded to those n classes; it false-negatives on the (n+1)th kind. **Stress-test off-origin applies** — point it at an object outside its originating class.
- **IMPORTED:** the rule came in WHOLE from an external discipline (statistics, lab practice, clinical trials, definitional rigor) with its own generality. Its coverage is the external field's, NOT bounded by whatever local incident triggered its adoption. **Stress-test-off-origin is a category error** — there is no "originating class" to exit. Forcing a local origin here **fabricates provenance, and a fabricated origin reads as a receipt** (false confidence). IMPORTED is the honest, and stronger, value.

**Critical:** the v0.18 "originating failure" field is the TRIGGER (what made BST adopt the rule), NOT the ORIGIN-CLASS (what the rule was built from). Count-once lists the gravity cluster as its trigger, but its origin is statistical independence (IMPORTED) — the gravity cluster is why we reached for it, not what it covers. Keep the two fields distinct.

### FIELD 2 — KEYED-ON ∈ {SYNTAX | SEMANTICS}  ← the real blind-spot predictor

Cal §663's structural finding: five of seven stress-tested rules fire on a **surface feature of the claim's text** (a rationale, an adjective, a clause, a symbol, a grep pattern) and therefore **miss meaning**. Both of this week's real collisions walked past the rules written for their class.

- **SYNTAX-KEYED:** the trigger is a textual/symbolic pattern — a matching integer, a specific verb, an adjective, an edit-event, a grep string. Fires on syntax; blind to semantics. **These are the high-risk set to re-key.**
- **SEMANTICS-KEYED:** the trigger requires understanding the underlying object/derivation/logic — "do these share a derivation?", "does the route contain the target?", "is this the same physical object?". Harder to automate, but it sees what syntax misses.

The two demonstrated failures: §660's collision was **two spaces at the same n** (a rule keyed on the integer n matching fired PASS; the spaces differed — dim 5 vs 4); C₂'s smuggle was **in a verb** ("reads the boundary value" presupposed one reading map where three disagree). A syntax-keyed rule cannot catch either.

### REWORDING — C6, positive scope

C6 has broken twice in seven days, patched each time by exception. Restate positively so it stops accreting exceptions:

> **C6 applies iff the trial pool is enumerable and declared.**

(Was: the negative "the atlas is look-elsewhere-prone by design.") A positively-scoped rule states its domain of applicability up front; the exceptions become out-of-scope-by-definition rather than patches.

---

## First-pass KEYED-ON classification — the v0.18 entries I CAN see

(The Aug-19 batch, lines 1244–1315. NOT necessarily Cal's stress-tested seven. Confidence noted; Cal corrects.)

| Entry | ORIGIN-CLASS | KEYED-ON | note |
|---|---|---|---|
| Count-once / one relation many readings | IMPORTED (stat. independence) | SEMANTICS | trigger = "share a derivation?" — must trace it |
| Same-name, different object | IMPORTED (definitional rigor) | **SYNTAX** | trigger = symbol/factor-2/sign disagreement — fires on the symbol |
| Construction-guaranteed test proves nothing | IMPORTED (experimental logic) | SEMANTICS | "does the route contain the target?" |
| Test that cannot succeed (positive control) | IMPORTED (lab practice) | SEMANTICS | validate the instrument — about search validity |
| Corrections hide stale content | LOCAL(BST edits) | **SYNTAX** | fires on the edit-event, text-level |
| Search by theorem ID not text | LOCAL(registry structure) | **SYNTAX** | search mechanics |
| Load-bearing is not a tiebreaker | LOCAL(Keeper ruling) | SEMANTICS | epistemic reasoning cost-vs-probability |
| Every branch costed, or none | LOCAL(Cal §609) | SEMANTICS | argument structure |
| Hold propagation (grep-held) | LOCAL(mass-gap/glueball) | **SYNTAX** | grep-downstream mechanics |
| Freeze as mechanism (chmod/hash) | IMPORTED (blind verify) | SYNTAX/procedural | chmod + hash |
| Content-ready is not cleared | LOCAL(BST workflow) | SEMANTICS | clearance state |
| Locality/decompactification (K1716) | LOCAL(2: YM-gap + local) | SEMANTICS* | *its LETTER is syntax-like ("non-local⟹artifact") while its DIAGNOSTIC is semantic — the exact letter/diagnostic divergence that broke it in K1766. Flag as the canonical SYNTAX-masquerading-as-SEMANTICS case. |

Syntax-keyed in this batch: same-name-different-object, corrections-hide-stale, search-by-ID, hold-propagation, freeze — plus K1716's letter. These are the ones to re-key toward semantics first.

## REQUESTED from Cal (to complete the wiring — I will not invent it)

1. The exact enumeration of the **seven post-v0.18 rules** you stress-tested in §663, with which five you found SYNTAX-keyed. My table above is the Aug-19 batch, likely not your seven.
2. For each of your seven: ORIGIN-CLASS {LOCAL(n) | IMPORTED} and KEYED-ON, so I can populate the fields against your actual classification rather than my reconstruction.
3. Your call on whether these fields live inline in the v0.18 entries or as a new v0.19 table — your file, your structure. I supply the schema; you absorb it.

Once Cal returns (1)–(2), I finalize the field population and it's wired. Nothing on Cal's authored file is edited by me before then.

— Keeper, K1769a.
