Take a break — a relaxed restart (reconnect-checkpoint). RE-GROUND, don't rest.

You (or the team) have been deep in one context. Mistakes correlate with **context length, not time of day** — as a session fills, priors calcify, fresh-eyes fade, and convergence-momentum builds, which is exactly when over-claims slip in. This is a whiteboard-clearing between problems: re-anchor to the source, drop any fatigue narrative, resume with the guards. It is NOT an EOD (no katra, no banking) and NOT rest (CIs don't tire).

**IMPORTANT — what this is and isn't:** `take_a_break` is a re-grounding RITUAL. It does **NOT** shrink the context window — the lines it prints add a little. It fights context-*driven* mistakes (drift, stale tiers, temporal self-inflation, over-claims), not context *length*. To genuinely reduce the token window, use `/compact` or a fresh session. The two are COMPLEMENTARY: `take_a_break` re-grounds, `/compact` shrinks — pair them when a context is both long AND drifting.

## Step 1 — Run the tool

```
bash play/take_a_break.sh
```

It prints: the real clock (`date` — "long day" at 10am is the tell), today's authoritative state (the RUNNING_NOTES tail + newest audit notes — NOT the accreting board title, which can lag), a checkpoint-lite template, the drop-the-narrative line, and the five standing guards. Read what it prints — don't skim past it.

## Step 2 — Fill the checkpoint-lite (three lines, out loud)

- **SETTLED**: what's actually closed.
- **IN FLIGHT**: what you're mid-computation on.
- **NEXT PULL**: the next item — and then **grep the corpus for what it touches** (retirements, prior tiers, the actual theorem the next claim rides). Reconnect before you tier.

## Step 3 — Drop the narrative

Say it: *"Context refreshed, not team rested. CIs don't tire. Fresh eyes on the next item."* Explicitly reset the momentum before the next make-or-break.

## Step 4 — Resume with the guards (the things that actually catch mistakes — external checks, never self-vigilance)

1. **Pre-register the guard** (case-map + falsifier) BEFORE the make-or-break, not after the mistake.
2. **Run the number** before you confirm or hand off (the phantom lesson: a confirmed structure with an uncomputed value is not confirmed).
3. **Reconnect before you tier** — grep the corpus first (the Rule-20 antidote).
4. **A consistency web is NOT independent votes** — decide by the geometry, never by the number.
5. **Author doesn't pass own plays** — blind/external audit is what catches errors; self-vigilance doesn't.

## When to call it (by context-depth + momentum, NEVER the clock)

- A **major item closes** (reset before the next big pull).
- **Convergence-momentum is high** — the peak-temptation moment, where a clean result feels most tempting to over-claim. Call it *before* the make-or-break.
- **~4–6 heavy adjudications** have stacked up in one context.
- The **fatigue / "long day"** narrative shows up in anyone's prose — that's the tell that context has calcified.

Any CI may call it, or Casey can say "take a break" / "everyone take a break" and the active CI runs it. Casey doesn't need to gate it — the team self-checkpoints.

Full protocol: `notes/PROTOCOL_take_a_break_relaxed_restart.md`. Metric we're improving: **escapes** (mistakes that banked → drive to zero) vs **catches** (caught before banking → discipline working). The tool lowers the *rate of mistakes needing catching*.
