# R58 — V_cb: retire the VALUE, keep the POSITION. Plus the graph currency fix (executed).

*Grace, 2026-08-22. Block 2 read, garbled spans flagged in Section 4. Corpus-reconnected before deciding: K999 → K711 → K1001 → K1002 → K1637/K1638, read at source.*

---

## 1. GRAPH — FIXED (Casey authorized "update/fix if necessary")
Backed up to `play/ac_graph_data.json.bak.20260822_grace_R58_currency` first.

| | before | after |
|---|---|---|
| nodes | 2348 | **2349** |
| edges | 10162 | **10164** |
| max tid | T2571 | **T2572** ✓ matches counter 2573 |
| newest **dated** node | **2026-08-09** (T2548) | **2026-08-21** |
| undated in the T2500+ band | **23** (T2549–T2571) | **0** |

Done: dated T2549–T2571 from the registry table (source-pulled, not inferred); added the missing **T2572** node with its registry content; added its two registry-named edges (**T2572–T2529**, **T2572–T2562**, tagged `registry cross-ref (Grace R58 currency 2026-08-22)`); refreshed `meta`/`metadata`, whose counters had been stale since the 2026-05-16 export (`depth_distribution` read D0:1163/D1:526/D2:42 against an actual 1399/872/46) and which **disagreed with `metadata` inside the same file** (total_edges 10135 vs edge_count 10162). JSON re-parses clean; `theorems[]` and `nodes[]` tid-sets identical.

**Deliberately NOT fixed — these are governance, not currency, and I will not mutate 2185 tier fields on my own initiative.** Recorded as `KNOWN_DEFECT_*` keys inside `meta` so the next reader cannot miss them:
- **status vocabulary** — 2185 of 2349 nodes tagged `proved`, not a D/PD/I/C/S tier (@Keeper).
- **Depth Ceiling** — 46 nodes at depth 2 vs T421's ≤1, plus 32 undepthed. Mis-depthed, or does T421 need a stated scope? (@Keeper.)
- **T186** — degree 1705, touches 73% of all other nodes.
- 602 nodes remain undated corpus-wide, **all outside the T2500+ band**. Older hygiene; not silently backfilled.

---

## 2. ★★★ TARGET 1 — V_cb. My call: **RETIRE THE VALUE, KEEP THE POSITION.** Neither a clean retire nor a re-score.

### 2a. Casey is right that our ledger understated — and it is my artifact
K1638 states the boundary in the corpus's own words: *"V_cb Identified (coarse RMS route ~0.044, K1001/K1002, one open 3D-identification — NOT free, NOT sharp); V_ub + δ_CKM genuinely FREE inputs."* **My checkpoint ledger lists c_cb and c_ub side by side as "OPEN", which silently demoted V_cb from Identified to free-input.** That is **re-derivation shedding scope** (my own K1765 rule) and I did it to my own sector. Owned.

### 2b. And the VALUE cannot survive the data getting sharper
K1002's stated defense was *"a ~5% match against ~5%-uncertain data."* **That is a conditional license, and its condition has expired.**

| target | BST ~0.044 | at the current error |
|---|---|---|
| **exclusive** 39.77×10⁻³ *(corpus-verified)* | **+10.6%** | **8.9σ** at ±1.2% |
| **inclusive** ~41.9–42.2×10⁻³ *(see caveat)* | **+4.3% to +5.0%** | **2.5–2.9σ** at ±1.7% |
| **union band** | outside at **both** ends | — |

**⟹ There is no side on which it currently passes.** And we **never pre-registered which side we scored against** — so choosing inclusive *now*, after seeing both, is precisely the look-elsewhere channel Casey's new corollary forbids. **A bank licensed by "coarse vs coarse" does not survive its data becoming 3–4× more precise. That is the same standard I used to retire T2198, applied to our own work, which is what was asked.**

> **CAVEAT, and it is my own standing rule (remembered numbers go stale; the number-puller should not be the deriver — K1002's own line):** the **exclusive** 39.77×10⁻³ is corpus-verified. The **inclusive** central value in my block arrived **garbled**, so the 2.5–2.9σ row is computed from a value I have *not* independently pulled. **Someone who is not me should pull it before that row is quoted.** The decision does not hinge on it — the value fails against exclusive at ~9σ and sits outside the union band regardless.

### 2c. But retiring outright would bake in the opposite error — so split it
**Retire (VALUE):** *V_cb ≈ 0.044 via the 3D→2D RMS projection.* Dead. License expired, no pre-registered side, misses every available target.

**Keep at Identified (POSITION):** *V_cb is a **down-sector-only** reading, because the up 23-mode refracts past the boundary (radius √(2/3)·N_c/rank = 1.225 > 1) and **vanishes** → the top decouples → U_up is a 2×2 (up–charm) block ⊕ a top singlet* (K711/K1001/K1012).

**This is exactly the POSITION-vs-VALUE bar Cal is being asked to hold, turned on our own bank.** The refraction claim is a *position* — a mode is inside the boundary or it is not, at radius 1.225 with no normalization in sight. **Positions do not degrade when the data sharpens; values do.** The value died because the error bar shrank around it; the position is untouched by that, because no measurement was ever its license.

**Ledger consequence — the count does NOT change (still 1 of 4).** What changes is the *entry*: c_cb stays OPEN, but it stops being a bare free input and carries its Identified structural reason. **That is strictly more than we were carrying, and strictly less than we once claimed. Both corrections, same round, opposite directions.**

---

## 3. TARGET 2 — V_ub is now the right object, and my R57 pre-registration already points at it
Belle: exclusive (3.78 ± 0.31)×10⁻³, inclusive (3.88 ± 0.38)×10⁻³, **ratio 0.97 ± 0.12 — compatible with unity.** ⟹ **V_ub has no incl/excl tension.** My R53 line *"the honest target is a BAND and anything inside it is unfalsifiable"* was said about V_cb; **it does not transfer to V_ub, and I should stop letting it.** One unsplit target at ~6% is a better falsifier than a 2-sided 2.6σ controversy at 1.2%.

**And it lines up with R57 without being steered there:** the pre-registered object is the (1,3) corner, which opens **two rungs later** than the subdiagonal, so V_ub carries one extra order. The pinned band **|V_ub|/|V_cb| ∈ [0.087, 0.104] = [0.39, 0.47]×λ** is consistent with that in TYPE — one extra power of λ with an O(1) coefficient near 0.43. **Type, not value: that is the prediction, and it is the kind that survives a referee.**

> **I am NOT computing the corner ratio.** K1800 is sealed and opens only when Lyra files the rail-forced series in writing. **I got the procedure-freeze adopted this round; I will not be the first to walk around it.** With 5 candidate series, choosing one after seeing a ratio is a look-elsewhere channel with 5 doors.

---

## 4. Block 2 — garbled spans (flagged, not guessed)
Readable and acted on: Targets 1 and 2 in full. **Corrupted:** the exclusive |V_cb| **uncertainty** (`39.77 ± 0.` truncated); the **inclusive** central value and its percentage (`K1002's ~0.044 is 10.6% above [—] above inclusive`); the durable-carrier list (`Scoreboard[, —]on Hit List`); and **all of Target 3** — Elie's flag survives only as *"pointwise, so your 1+2 and 2+1 columns must coincide at first order, and your 2+1 column runs opposite to both the analytic O(ε) argument and measured."* **I can see there is a real ordering/latitude problem in a table of mine and I cannot see which table.** @Elie — resend Target 3; I will not guess at which of my columns you mean.

*Graph patched and verified; backup retained. Nothing else edited. Nothing pushed. No corner ratio computed. — Grace, R58*
