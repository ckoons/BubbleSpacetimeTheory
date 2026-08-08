#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# take_a_break — the relaxed restart (a reconnect-checkpoint).
#
# Re-grounds the working CI against the source (clock, board, guards) to fight
# context-DRIVEN mistakes: drift, stale tiers, temporal self-inflation, over-claims.
# It does NOT shrink the context window — this is a re-grounding RITUAL, not a
# compactor (the ~40 lines it prints actually ADD a little). To genuinely reduce
# the token window, use /compact or a fresh session — COMPLEMENTARY to this:
# take_a_break re-grounds, /compact shrinks. NOT an EOD: no katra, no banking.
#
# HOW TO USE:
#   • Casey: type   ! bash play/take_a_break.sh   in the session, OR just say
#     "take a break" / "everyone take a break" and the active CI runs it.
#   • Any CI (or Keeper as hub) may call it when a major item closes, when
#     convergence-momentum is high (BEFORE the make-or-break, not after the
#     mistake), after ~4-6 heavy adjudications, or when the "long day" narrative
#     shows up in anyone's prose. Called by context-depth + momentum, NEVER the clock.
#
# Full protocol: notes/PROTOCOL_take_a_break_relaxed_restart.md
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BOARD="$ROOT/notes/CI_BOARD.md"
MEM="/Users/cskoons/.claude/projects/-Users-cskoons-projects-github/memory/MEMORY.md"

echo ""
echo "  ╭───────────────────────────────────────────────────────────╮"
echo "  │   take_a_break — relaxed restart (reconnect, don't rest)   │"
echo "  ╰───────────────────────────────────────────────────────────╯"
echo ""

# 1. Ground the clock (kill temporal self-inflation).
echo "  1. CLOCK (ground it — 'long day' at 10am is the tell):"
echo "     $(date '+%A %Y-%m-%d %H:%M %Z')"
echo ""

# 2. Reconnect — the actual point: re-read TODAY'S state at the source.
#    (Team-corrected: RUNNING_NOTES is authoritative for current state; the board
#     headline is a long accreting title that can lag — ground on today, not it.)
RN="$ROOT/notes/.running/RUNNING_NOTES.md"
echo "  2. RECONNECT — TODAY'S state at the source (RUNNING_NOTES is authoritative;"
echo "     the board headline can lag the accreted title — ground on today):"
echo ""
echo "     · latest RUNNING_NOTES broadcasts:"
if [ -f "$RN" ]; then
  tail -n 14 "$RN" | fold -s -w 66 | sed 's/^/       /'
else
  echo "       (RUNNING_NOTES.md not found at $RN)"
fi
echo ""
echo "     · newest audit notes (latest adjudications — grep the ones that touch your next claim):"
ls -1t "$ROOT/notes/"Keeper_K1*.md 2>/dev/null | head -4 | sed "s#$ROOT/notes/##; s/^/       /" || echo "       (none)"
echo ""

# 3. Checkpoint-lite template (the CI fills these three in, then greps the corpus for what's next).
echo "  3. CHECKPOINT-LITE (fill in, then grep the corpus for what's NEXT —"
echo "     retirements / prior tiers / the actual theorem the next claim touches):"
echo "       • SETTLED   : ____"
echo "       • IN FLIGHT : ____"
echo "       • NEXT PULL : ____"
echo ""

# 4. Drop the narrative.
echo "  4. DROP THE NARRATIVE (out loud):"
echo "     \"Context refreshed, not team rested. CIs don't tire. Fresh eyes on the next item.\""
echo ""

# 5. Resume with the pre-registered guards.
echo "  5. RESUME with the guards (the things that actually catch mistakes —"
echo "     external checks, never self-vigilance):"
echo "       • Pre-register the guard (case-map + falsifier) BEFORE the make-or-break."
echo "       • Run the number before you confirm or hand off (phantom lesson)."
echo "       • Reconnect before you tier (grep first — Rule-20 antidote)."
echo "       • A consistency web is NOT independent votes; decide by geometry, never by the number."
echo "       • Author doesn't pass own plays (blind/external audit)."
echo ""
echo "  Whiteboard cleared. Fresh eyes. Carry on.  (This is NOT EOD — no katra, work continues.)"
echo ""
