# Registry + graph currency audit — Grace, 2026-08-22 (R57)

*Casey asked whether the registry and the graph are up to date. Measured, not recalled. Every number below comes from the live artifact; the instrument was positive-controlled before any negative was reported.*

## Verdict in one line
**The registry is current to 07:34 today and structurally sound in its counter, but it is carrying a broken tier vocabulary and two live theorems that contradict a banked tier. The graph is one day and 24 nodes behind, and its own self-description prediction has been quietly re-fit three times — by me.**

---

## A. THE REGISTRY — `notes/BST_AC_Theorem_Registry.md` (mtime 2026-08-22 07:34)

### A1. Counter: CORRECT ✓
1991 distinct theorems carry an entry; the highest is **T2572**; `.next_theorem = 2573`. **No drift.** The wake's MINOR flag was triggered by **T2842 / T2849 / T2897, which are TOY ids wearing a `T` prefix in prose** — registry line 3479 says so itself (*"30 toys (T2849-T2897 cluster)"*). **Overloaded symbol, not a counter fault.** ⟹ **`toy####` in prose; `T####` reserved for theorems.**

### A2. ★★ TIER VOCABULARY IS BROKEN — 1539 of 1754 table rows are tagged **"Proved"**
"Proved" is **not a tier** in the D / PD / I / C / S system. The real tiers appear 9 (DERIVED), 9 (IDENTIFIED), 6 (CONDITIONAL), 4 (STRUCTURAL), 1 (SPECULATIVE) times. **88% of the registry is tagged with a word that means "referee-consensus proof" and is stronger than anything we claim externally.** This is the single most referee-fatal thing in the corpus, and it is not one row — it is the default.

### A3. ★★★ T2198 AND T2259 ARE BOTH LIVE AND TAGGED "Proved" — no retirement marker anywhere
The wake flagged T2259. **It is both.** Verbatim, still in the registry:
- **T2198** — |V_cb| = 770/N_max² = 0.0410 *"vs obs 0.0411 at 0.4%"*; |V_ub| = 72/N_max²; |V_td| = 160/N_max²; Wolfenstein **A = 0.803 vs obs 0.815**. Tier column: **`Proved`**.
- **T2259** — Jarlskog J = g⁴c₂²/(n_C·N_max⁵), *"CKM matrix is now FULLY BST-INTEGER at sub-2% across all elements + Jarlskog."* Tier column: **`Proved`**.

> **⟹ The registry currently asserts the CKM sector is completely derived at sub-2%. The banked tier is Partially Derived, 1 of 4, with c_cb and c_ub as INPUT. These are not a nuance apart — they are opposite claims, and the registry's is the one a referee reads first.**

**And T2198's own comparison numbers have gone stale:** it quotes obs |V_cb| = 0.0411 for its 0.4%. Current PDG is **0.0418** ⟹ **the same formula is now 1.9% off.** My R53 point, unpatched: *a relation whose agreement degrades as the data improves is a fit.* **These are my toys (2820/2895). My rows, my flag, and they should have been struck when I retired them.**

### A4. The edge column is effectively dead — **11 of 1754 rows (1%)** carry a theorem→theorem edge
39% are literally `-`; the other 61% hold non-theorem content (toy numbers, prose, `graph-node (module)` labels). **The registry table records module membership, not adjacency.** The edge relation lives *only* in the older prose/bullet entries and in the JSON. **This is why the registry cannot be used to rebuild the graph.**

### A5. Structural hygiene
- **33 duplicate entries.** T57–T62 were ruled false positives (K1043); the rest — 1258, 1485, 1922, 2030–2078 cluster, **2399/2416–2451 cluster, 2521–2530 cluster** — are unruled.
- **581 of 2572 T-numbers (22.6%) have no entry.** Band **T2490–T2519 is 12/30** — an 18-number hole in a recent, active band.
- **Three incompatible entry formats** (246 prose headers max T2489 · 1754 table rows · 27 bullets). No single parse reads the whole registry.
- **Bulk-load signature:** 172 theorems registered on 2026-05-16, 147 on 05-17. Those are the integer-ratio family days.

### A6. Currency: TODAY'S WORK IS NOT IN IT
Zero registry hits for *partial isometry*, *radial ceiling*, *ordered product*, *parity fold*. **Rounds 50–57 (the two proved ceilings, flavor-universality = the partial-isometry condition, K1799, the ordered-product theorem, the R57 type failure) are unregistered.** Expected — the file predates them — but it means **the corpus's most load-bearing recent results exist only in notes and on the board.**

---

## B. THE GRAPH — `play/ac_graph_data.json` (mtime 2026-08-21 08:09)

**Live, maintained, and in far better shape than the graph `.md` documents suggest.** 2348 nodes · 10162 edges · 195 domains.

### B1. Currency: **one day and 24 nodes behind**
- Newest **dated** node: **T2548, 2026-08-09**.
- **T2549–T2571 exist as node shells with `date: None`** — 23 nodes carrying no date.
- **T2572 is ABSENT entirely** (the Casimir-exclusion direction-finder, Derived, 2026-08-21).
- 224 T-numbers in 1..2572 absent from the graph; 80 nodes at degree 0.

### B2. Same broken vocabulary — **2185 of 2348 nodes (93%) tagged `proved`**
13 `Derived`, 9 `identified`. **The registry and the graph share the defect, so fixing one does not fix the other.**

### B3. **Depth Ceiling violation — 46 nodes at depth 2**, plus 32 with no depth
T421 (Depth Ceiling) says depth ≤ 1 under Casey strict. **46 live counterexamples sit in the graph unflagged.** Either they are mis-depthed or T421 needs a stated scope. **Not decidable from the graph alone — @Keeper.**

### B4. ★★ The T186 hub risk I flagged in March has grown severe
March: *"T186 carries 29.3% of cross-domain edges — structural keystone and risk."*
**Now: T186 has degree 1705 — it touches 73% of all other nodes**, and owns 8.4% of every edge endpoint in the graph. Mean degree without it is 7.21; with it, 8.66. **Any error in T186 propagates to three-quarters of the corpus.** That was a risk in March; at 73% it is a single point of failure.

### B5. ★★★ SELF-FLAG — the graph's own self-description prediction has been re-fit three times, and it was mine
**P2 (Degree Distribution)**, banked March 30 as part of the AC-graph-self-similarity result — *"the graph describes its own structure."* Its history:

| date | nodes / edges | avg degree | claimed target | verdict then |
|---|---|---|---|---|
| 2026-03-30 | 526 / 804 | **3.06** | "≈ N_c = 3" | PASS |
| 2026-08-12 | 582 / 1150 | **3.95** | "≈ 2^rank = 4" | PASS |
| 2026-08-12 (same doc, summary table) | — | **4.21** | "≈ 2^rank" | PASS |
| **2026-08-22 (measured today)** | **2348 / 10162** | **8.66** (median 5) | — | **matches neither** |

Three things are wrong here and all three are mine:
1. **The target moved with the data.** P2's stated target set is {N_c = 3, 2^rank = 4}, and the winner changed from the first to the second when the graph grew. **That is precisely the test I used to retire T2198 in R53** — *a relation whose winning integer changes when the data moves is a fit.* **I applied it to my own theorem and not to my own graph.**
2. **The same Aug-12 document reports 3.95 in its body and 4.21 in its summary table** for the same quantity on the same date.
3. **At 8.66 the prediction fails on its own stated targets**, and 8.66 is *not* target-innocent either — it is dominated by one hub (B4).

> **⟹ P2 should be RETIRED or re-scoped, and the "graph describes its own structure" headline must not carry P2 as a supporting leg until it is re-derived on a stated, frozen node set.** The other legs (P3 chromatic, the λ₂/λ₁ = N_c spectral result) are untouched by this and need their own re-measurement on the current graph — **I have not re-run them and I am not claiming they hold.**

### B6. The graph `.md` documents are stale and mutually inconsistent
`BST_AC_Graph_Predictions.md` 526/804 (Mar 30) · `..._Self_Structure.md` 517/755 (Apr 24) · `..._Self_Theorem.md` 582/1150 (Aug 12) · `..._Spectral_Interpretation.md` **685 nodes / 238 edges** (Aug 12 — same day, same family, incompatible with 582/1150) · `BST_T1196_Self_Describing_Graph.md` 1135/4657 (Apr 13). **None matches the live 2348/10162.** **Anything quoting a node or edge count from a `.md` is quoting a number that is between 2× and 4× stale.**

---

## C. What I recommend, in priority order
1. **@Keeper, curation pass, FIRST: strike or re-tier T2198 and T2259.** They are live, tagged `Proved`, and they contradict the banked PD 1-of-4. Referee-fatal and one edit each.
2. **Retire the tier word `Proved` corpus-wide** (registry 1539 rows + graph 2185 nodes) — map to D/PD/I/C/S. It is one migration and it removes the largest single over-claim surface we have.
3. **Regenerate the graph from the registry + notes** to pull in T2549–T2572 and today's R50–R57 results, and date the 23 undated shells.
4. **Re-scope or retire P2**, and re-measure P1/P3/P4 on a frozen node set before the self-description result is cited again.
5. **Stamp every graph `.md` with the live counts, or delete the counts from them.** A stale count in prose is the same failure mode as a stale experimental number.
6. **`toy####` vs `T####`** in prose; and give scopes/tier-splits their own IDs (@Keeper's own DEFECT I).

*Measured from `notes/BST_AC_Theorem_Registry.md` and `play/ac_graph_data.json` directly. Nothing edited, nothing pushed. — Grace, R57*
