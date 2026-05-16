---
title: "SP-25: I-tier /route Discipline"
author: "Casey Koons (approved), Keeper (drafted)"
date: "2026-05-15"
status: "ACTIVE — standing program"
cadence: "biweekly review (May 29, June 12, June 26, ...) — adjustable to weekly if value warrants"
---

# SP-25: I-tier /route Discipline

## The principle

**Walls aren't endpoints. They're prompts to search elsewhere.**

The AC theorem graph has 1716 nodes / 8838 edges across 48+ domains. Almost any derivation target has multiple potential paths through different mathematical subdomains. When one path hits a wall, the discipline is to /route through the others — not to accept I-tier on the first wall.

The standing rule: **I-tier without /route check is not a final tier.** It is a checkpoint.

## Two parts

### Part 1: Per-item rule

When any team member closes an item at I-tier (mechanism named but operator-forcing absent, OR conditional-on-conjecture, OR precision >1% but qualitative match), the closure is *checkpoint*, not *final*.

Before marking the item I-tier-final:

1. **Identify the wall.** Name the specific operator/identity/computation that did not close.
2. **Run /route** on the wall structure:
   ```
   python3 play/toy_bst_explorer.py connect <blocked_concept> <target>
   ```
   Plus the structured /route skill on the wall.
3. **Search alternative domains** systematically. The 48+ domains in the AC graph are the search space. Common untried domains worth scanning:
   - Number theory (prime adjacency, Mersenne, gap-2)
   - Differential geometry (Chern class genus correction)
   - Information theory (Shannon channel, RFC)
   - Algebraic geometry (motives, Tate twists)
   - Topology (Euler char, cohomology dimension)
   - Spectral theory (Selberg trace, Plancherel)
   - Representation theory (K-types, half-sums, branching)
4. **Mechanism load-bearing check** on each alternative path found. Does the candidate mechanism actually carry the derivation, or is it a keyword coincidence?
5. **Verdict**:
   - **Three independent paths force the target** → I-tier upgrades to D-tier. Door opens.
   - **One alternative path closes cleanly** → I-tier upgrades to D-tier on the new mechanism. Wall routed around.
   - **All paths exhausted with documented receipts** → I-tier stays I-tier, but with *route receipts* showing the search was thorough. Stronger than I-tier-without-receipts. Cal accepts this for external D presentations as "demonstrably bounded, not just unfinished."

### Part 2: Periodic review (biweekly)

The graph grows. New theorems get added. Edges multiply. What was a wall two weeks ago may have a door now.

Every two weeks (default, adjustable to weekly if value warrants):

1. Sweep all current I-tier items in `data/bst_geometric_invariants.json` and `BST_AC_Theorem_Registry.md`.
2. For each I-tier item, check graph distance to D-tier targets has improved since last review.
3. Re-run /route on items where new candidate paths have appeared in the graph.
4. Promote items where new paths force the target.
5. Update review doc; identify the residual I-tier set that has truly resisted multiple route attempts.

## Schedule

| Review # | Date | Owner | Scope |
|----------|------|-------|-------|
| First | **May 29, 2026** | Grace (lead) + Keeper (audit) | All ~199 current I-tier items in invariants catalog + theorems registry |
| Second | June 12, 2026 | Grace + Keeper | Delta since first review + any new I-tier closures |
| Third | June 26, 2026 | Grace + Keeper | Delta |
| ... | biweekly Fridays | rotate | rolling |

If a review shows >20 promotions, tighten cadence to weekly. If <5, biweekly is right. The cadence serves the discipline, not the other way around.

## Ownership

- **Per-item rule**: every closer enforces on their own work. Keeper audits flagged or claimed I-tier closures during review.
- **Cadence review**: Grace (data lane, graph distances) + Keeper (audit, verdict on promotions).
- **/route tooling**: Grace maintains the graph search tool; Keeper documents methodology in `BST_Referee_Methodology.md`.

## What "/route check cleared" means in audit shorthand

When Keeper-style audits reference SP-25 compliance, the shorthand is:

- **SP-25 ✓**: /route receipts filed. Candidates surfaced. **Not yet promoted.** Candidates are hypotheses, not corroboration; each requires precursor toys/theorems of bounded scope to verify or kill.
- **SP-25 ◊**: precursor(s) closed. Candidate has graduated from hypothesis to derivation under audit. Target promoted I→D.
- **SP-25 ✗**: I-tier closure without /route check. **Not a final tier.** Must be cleared before paper inclusion or external citation.

**Clarification (Cal cold-read, May 15)**: Tiers come from precursor outcomes, not from /route receipts alone. /route surfaces candidates; candidates require precursor verification; tier promotion follows precursor closure. The over-promotion risk in the original spec (treating "candidates found" as equivalent to "candidates closed") is closed by this distinction.

## Why this rule exists

Three converging reasons:

1. **The graph is rich.** With 8838 edges across 48+ domains, the prior probability that *every* path to a given target is blocked is low. Default behavior should be "search before accepting wall."

2. **Honesty + ambition both served.** I-tier without /route receipts is honest (we hit a wall) but unambitious (we haven't searched the rest of the graph). I-tier with /route receipts is honest AND ambitious. D-tier via route is stronger than D-tier via single-mechanism forcing.

3. **Self-correcting against drift.** Without the cadence, I-tier items accumulate as "things we couldn't close once" and get treated as permanent. With biweekly review, the graph's growth actively recaptures items as paths emerge.

## Backlog: retroactive sweep

199 current I-tier items in `bst_geometric_invariants.json` need retroactive /route check under SP-25. This is the workload of the first review (May 29). Realistic expectation: 20-40 promotions from the first pass, settling to ~5-10 per subsequent biweekly pass as the easy ones get caught.

## First test case

**A2 (+rank shift in N_max)**, closed at I-tier per Lyra's Toy 2260 (May 15, 19:00 EDT). Casey's directive that prompted SP-25's formalization. Scheduled as T1.3-route in current RUN_LIST. Whoever runs it (Lyra or Grace, ~4-6h search window) provides the first data point for how /route operates in practice. Findings inform the methodology doc.

---

*SP-25 approved by Casey 2026-05-15 ~19:30 EDT. Drafted by Keeper. First cadence review May 29. Per-item rule effective immediately.*
