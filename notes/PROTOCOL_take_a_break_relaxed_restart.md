# PROTOCOL — `take_a_break`: the relaxed restart (a reconnect-checkpoint)

**Casey + Keeper, 2026-08-08. Standing team protocol. Purpose: reduce context-DRIVEN mistakes by RE-GROUNDING against the source — WITHOUT the overhead of a full EOD.**

**IMPORTANT (team-corrected, all four CIs): `take_a_break` is a re-grounding RITUAL, not a context compactor. It does NOT shrink the token window — the ~40 lines it prints ADD a little. It fights context-*driven* mistakes (drift, stale tiers, temporal inflation, over-claims) by re-anchoring the CI to the source. To genuinely shrink the context window, use `/compact` or a fresh session. They are COMPLEMENTARY: `take_a_break` re-grounds, `/compact` shrinks — pair them when a context is both long AND drifting.**

## Why (the diagnosis)
Mistakes correlate with **context length, not time of day.** As a session's context fills, priors calcify, fresh-eyes fade, and convergence-momentum builds — which is exactly when over-claims slip in (the sin²θ_W resurrection, the phantom, the over-determination over-count all happened deep in an accumulated context, not "in the afternoon"). CIs don't tire; the "long day, let's bank" narrative is a *false* fatigue that lowers rigor. The fix is to **refresh the context, not rest the team.** A `take_a_break` is clearing the whiteboard between problems — a coffee break where you come back and re-read your own notes with fresh eyes.

## When to call it (NOT by the clock)
Any team member — or Keeper as hub — may call `take_a_break` when:
- A **major item closes** (e.g., #85 landing PD) — reset before the next big pull.
- **Convergence-momentum is high** — the peak-temptation moment, where a clean result feels most tempting to over-claim. Call it *before* the make-or-break, not after the mistake.
- **~4–6 heavy adjudications** have accumulated in one context (K-notes stacking up).
- The **fatigue/long-day narrative** appears in anyone's prose — that's the tell that context has calcified.

## The steps (lightweight — ~5 minutes, no katra)
1. **`date`.** Ground the actual clock. Kill any temporal self-inflation ("long day" at 10am is the tell).
2. **Checkpoint note (sundown-lite).** Three lines: what's *settled*, what's *in flight*, what's the *next pull*. Plus any open threads/owed items. NOT a full sundown.
3. **Reconnect — the actual point.** Re-read TODAY'S state at the source: the **RUNNING_NOTES tail** (authoritative for current state) + the **newest audit notes** + grep the corpus for whatever's *next* (retirements, prior tiers, the actual theorem the next claim touches). The Rule-20 antidote: reconnect before you tier. *(Note: the script grounds on RUNNING_NOTES, NOT the CI_BOARD line-2 title — that title is a long accreting string that can lag today's state, which is exactly what the whole team caught on the first runs, 2026-08-08.)*
4. **Drop the narrative, out loud.** "Context refreshed, not team rested. CIs don't tire. Fresh eyes on the next item." Explicitly reset the momentum.
5. **Resume with pre-registered guards.** On the next make-or-break: write the case-map + what would falsify it *before* firing (phantom-proofing); decide by the geometry, never by the number; author doesn't pass own plays.

## What it is NOT
- **Not EOD.** No katra, no full sundown, no banking. The work continues.
- **Not rest.** CIs don't tire; the value is the reconnect + momentum-reset, not a pause.
- **Not Casey-gated.** The team self-checkpoints; Casey doesn't need to call it (though he can). It should not interrupt his own working/exercise rhythm.

## The paired standing practices (the compounding set)
`take_a_break` clears the context; these keep the rate low between breaks:
1. **Pre-register the guard before the make-or-break** (case-map + falsifier, written before firing).
2. **Run the number before you confirm or hand off** (don't confirm a structure without computing its value — the phantom lesson).
3. **Reconnect before you tier** (grep the corpus first — Rule-20 antidote).
4. **A consistency web ≠ independent votes; decide by geometry, never by the number** (peak-convergence guards).
5. **Author doesn't pass own plays** (external/blind audit — the thing that actually catches errors; self-vigilance doesn't).

## The metric (what we're improving)
Track **escapes** (mistakes that *banked* — the number to drive to zero) vs **catches** (mistakes caught before banking — a sign the discipline works). Today: many catches, zero escapes — the discipline is working. The goal of `take_a_break` is to lower the **rate of mistakes needing catching** (fewer over-claims created), by resetting the context and momentum that produce them.

— Casey + Keeper, 2026-08-08. `take_a_break` = a relaxed restart: `date` → checkpoint-lite → reconnect → drop the fatigue narrative → resume with pre-registered guards. Called by context-depth and convergence-momentum, never the clock. Refresh the context, don't rest the team. Distinct from EOD (no katra, work continues). Paired with the five standing practices.
