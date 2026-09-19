#!/bin/bash
# Keeper — Approaches Register nightly/backfill run.  Model-agnostic: set APPROACHES_MODEL (and optionally
# APPROACHES_API=openai + APPROACHES_ENDPOINT + APPROACHES_API_KEY) before running.  First run = full backfill
# (~3000 files); later runs cost only new/changed files (cache by sha).
#   usage:  APPROACHES_MODEL=qwen3:30b-a3b play/keeper_register_nightly.sh
set -u
cd "$(dirname "$0")/.."
LOG=notes/.running/approaches_register_nightly_$(date +%Y-%m-%d_%H%M).log
echo "== $(date)  model=${APPROACHES_MODEL:-qwen3:30b-a3b} api=${APPROACHES_API:-ollama}" | tee "$LOG"
python3 play/keeper_approaches_register.py --selftest >> "$LOG" 2>&1 || { echo "SELFTEST FAIL — see $LOG"; exit 1; }
python3 play/keeper_approaches_register.py -v --controls play/keeper_approaches_controls_RH.tsv >> "$LOG" 2>&1
RC=$?
echo "== $(date) exit=$RC" | tee -a "$LOG"
grep -E "^rows=|^CONTROLS|Unstable" "$LOG" notes/BST_Approaches_Register.md | tail -4
exit $RC
