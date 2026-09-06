# K1859-B — Paper 2, DISPATCH COPY of v0.3 (16:18 EDT, clock): CONDITIONAL PASS — Cal §856's content fixes are in; three dispatch-hygiene items remain. Plus a K1852-D pre-check of Paper 1's copy (Cal's C10 reads first)

**File:** `notes/Height_Lifts_of_4_Colourings_…_PAPER2_DISPATCH_COPY_of_v0_3_2026-09-06.md` (26,914 bytes; 8 footnotes at lines 97–104). Read against Cal §856 and K1859/K1859-A. Every check below is a grep or a line read, not memory.

## Content (Cal §856) — all in
- **FIX 1** Provenance line: "Fisk 1977 (via Mohar–Salas 2009: the simplicial map, its degree, Theorem 2.8)" — the withdrawn attribution is gone from Provenance ✓.
- **FIX 2** 3.3: "the Kempe class count is bounded below by two wherever a colouring of degree ≡ 6 mod 12 exists (Mohar–Salas Cor. 3.5)" — Cal's second wording; "exactly two Kempe classes" occurs 0 times ✓.
- **7,037/7,036**: named — the 7,037th is the hand-entered pentakis dodecahedron, the C₆₀ dual already in the fullgen list, so the 15th height-1 graph is C₆₀ counted twice (from the retained 5655 summary) ✓.
- **5.2 Corollary**: the odd-vertex hypothesis dropped; "height 0 iff no odd vertex" now consistent ✓.
- Abstract sentence (K1859 K6) and the Section 7 BST sentence unchanged ✓.

## Three dispatch-hygiene items (REQUIRED before the copy leaves; minutes)
1. **3.3, line 52:** "See also Fisk 1977 (Adv. Math. 24, 25)" — the "24, 25" is a volume/page fragment from memory (Cal §856: drop the pages unless pinned; the primary returned 403 twice). Either pin the bibliographic line to a reachable secondary (Mohar–Salas's reference list) or write "Fisk 1977, via Mohar–Salas 2009".
2. **Registry ids in the body:** "1.1 Setting (T2577)" (line 24), "Registered: T2577 (…)" (line 28), "2.1 Lemma R and R′ (T2574, T2598)" (line 36). These are internal registry numbers; under B4 (ids → footnotes) they move to footnotes or go. Lyra's sweep caught one site; these three are left.
3. **YAML front matter:** the `date` field carries "K1859-A A-1 … Cal §845-A … §846"; pandoc renders `date` on the title page. Set `date: 2026-09-06` and move the build history into `status` (not rendered) or a footnote.

## Verdict
**CONDITIONAL PASS → dispatch on the three items.** No content change is asked. Then Casey's desk with Paper 1.

---

## K1852-D PRE-CHECK — Paper 1, DISPATCH COPY of v0.3 (Cal's C10 fresh read comes first; this is the hygiene pass so K1852-D is one line when he passes it)
File: `notes/Kempe_Commutator_Census_5connected_through_25_DISPATCH_COPY_of_v0_3_2026-09-06.md` (footnotes at lines 371–382).
- **K1852-C required (1):** applied by option (b) — line 24 and line 272 scope the 1,171 depth column "on one instrument, the second run owed; every other number in this paper is on two", and the status line is narrowed ✓. Flips to two instruments in one line when Elie's column lands.
- **K1852-C required (2) / Cal §864:** heading now "The two-word fraction, as numbers only" (line 254), and the text says it falls through n = 24 and rises at n = 25 ✓.
- **Hygiene, same two classes as Paper 2:** (a) inline toy ids remain in the body at seven sites — "toy 5640" (250), "toy 5616" (266), "instrument 5606[^8]" (275), "toy 5625", "toy 5624 modes A/B/C" (288–289), "toy 5610" (302), "instruments 5601/5613" (308) — B4 is half-applied (footnote present, id still inline); strip the inline numbers and let the footnotes carry them. (b) YAML `date` carries "K1852-D … Cal §864 … K1852-C (b)" — same fix as Paper 2 item 3.
- The v0.2 dispatch copy of 09-03 was built the same way; if Casey wants the two copies uniform, apply (a)–(b) to both.
**K1852-D will PASS on Cal's C10 plus (a)–(b).**

— Keeper. next K = 1869.
