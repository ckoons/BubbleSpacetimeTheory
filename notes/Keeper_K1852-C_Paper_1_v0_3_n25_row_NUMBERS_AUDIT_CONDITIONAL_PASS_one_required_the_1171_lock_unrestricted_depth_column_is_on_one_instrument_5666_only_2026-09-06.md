# K1852-C — Paper 1 v0.3 (Kempe Commutator Census through 25), the n = 25 row: NUMBERS AUDIT — CONDITIONAL PASS, one REQUIRED (16:01 EDT, clock)

**Scope (per Casey Friday: "n = 25 GOES IN"; the round's word given in K1866):** the numbers only. K1852/K1852-A/B conditions on v0.1 → v0.2 (Cal §831's blocking list, the Errera-in-frame clause, internal ids stripped in the dispatch copy) were met by the 09-03 dispatch copy and are not re-opened. File: `notes/Kempe_Commutator_Census_5connected_through_25_v0_3_DRAFT_2026-09-06.md` (built 15:55 by exact-match edits from v0.2).

## Verified against retained instruments (every figure below was read from an out-file or TOY_LOG, not from the paper)
| paper figure | source | check |
|---|---|---|
| n = 25: 26,870,832 stuck colourings; 44,566 without a direct one-word exit; 43,395 gate in one word; 1,171 in two; 0 deeper | TOY_LOG 5600/5601 (stage 1 26.5 h, stage 2 10.3 h; 23,384 graphs); `.out_5601_n25.txt` (43395/44566; direct 0); `.out_5672.txt` (1,171 two-word locks) | ✓ |
| second instrument on the 44,566 and the 1,171 | Grace 5666: population 44,566 hashed e9ae614c before counts; lock list hashed d4fdec14 before the diff; 1,171 common, 0 either-side-only | ✓ |
| totals: 34,250,085 = 7,379,253 (v0.2 total) + 26,870,832; 57,794 = 13,228 + 44,566; 56,274 = 12,879 + 43,395; 1,520 = 349 + 1,171; depth-3 column 0 | v0.2 totals row (line 231) + n = 25 row | ✓ arithmetic exact |
| 1,520 by n: 8 + 18 + 23 + 44 + 256 + 1,171 | v0.2 rows + 5672 | ✓ = 1,520 |
| 1,171/44,566 = 2.6 percent (line 257) | — | ✓ 2.63 % |
| unrestricted plain-swap depth on the 44,566: {18,341; 22,046; 4,160; 19}, max 4, unreached 0 (line 287) | Elie 5664a (prereg 49670a3b) AND Grace 5666 [C:all] — identical | ✓ two instruments |
| abstract: "all but 1,520 reach the gate phase within one word; all 1,520 within two; none needs three" | Table 3.1 | ✓ consistent |
| "none of the 22 bits or the five conditions was re-measured on the 1,171" (line 214); the gate/direct sub-split at n = 25 not printed (line 257) | Elie 5601 says 1,113 gate + 58 direct; Grace 5666 [D] says 1,171 direct — the instruments DISAGREE on the sub-split (definition-dependent), and the paper correctly prints the count only | ✓ honest scoping |

## The one REQUIRED
**Line 24 / Table 3.3 / line 274: "of the 1,171 at n = 25, 100 exit in one swap and none needs more than four."** The unrestricted plain-swap depth on the 1,171 lock witnesses, {1: 100, 2: 426, 3: 629, 4: 16}, exists in **Grace 5666 [C:S-leaves 1171] only**. Elie 5664a ran the unrestricted depth on the 44,566, not on the 1,171 (no such line in `.out_5664a_n25.txt`, `.out_5664b_n25.txt`, or `.out_5601_n25.txt`). The paper's status line promises "every number on two independent instruments." **Fix, either:** (a) Elie runs 5664a's method on the hashed 1,171 witness list (minutes) and posts {100, 426, 629, 16} or the discrepancy; or (b) the sentence and the 1,171 column of Table 3.3 are scoped "(one instrument, Grace 5666; Elie's second run owed)" and the status line is narrowed accordingly. (a) is preferred and cheap.

## Minor (not blocking)
- Line 24's "27 exit in one swap" on the 349 is unchanged from v0.2 (K1852-B checked it); fine.
- TOY_LOG's n = 25 sub-split "1,113 gate + 58 direct" should not migrate into the paper while the two instruments disagree on it; it has not.

## Verdict
**CONDITIONAL PASS on the numbers.** With (a) or (b) applied: → Cal's fresh read of v0.3 (his C10) → the dispatch copy (internal ids stripped, as v0.2's was) → K1852-D on the copy → Casey's desk (Zenodo version → the Gethner note → arXiv on endorsement). Nothing in the n = 25 row changes any claim of v0.2; it extends the census by one vertex count with the same shape (no lock deeper than two; unrestricted depth ≤ 4).

— Keeper

## Amendment 16:04 — Cal §864 (his read of v0.3, 15:58) folded in
Cal: PASS, one wording fix — line 256's heading "**The falling fraction, as numbers only.**" is false at n = 25: the two-word fraction runs 7.8, 2.8, 2.8, 2.4, **2.6** percent and RISES from 2.44 to 2.63 by exact counts. Rename to "The two-word fraction, as numbers only" and let the sentence state the rise. Every n = 25 number re-added and consistent; scoping to n ≤ 24 where required; B4 (internal ids → footnotes) remains for the dispatch copy. **K1852-C's required items are now two:** (1) the 1,171-lock depth column on a second instrument (or scoped); (2) the heading. Both are minutes. Then the dispatch copy → K1852-D → Casey's desk.
