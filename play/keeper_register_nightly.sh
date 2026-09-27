#!/bin/bash
# Keeper — Approaches Register nightly/backfill run.  Model-agnostic: set APPROACHES_MODEL (and optionally
# APPROACHES_API=openai + APPROACHES_ENDPOINT + APPROACHES_API_KEY) before running.  First run = full backfill
# (~3000 files); later runs cost only new/changed files (cache by sha).
#   usage:  play/keeper_register_nightly.sh   (default model qwen3.8:27b since 2026-09-27: 10/11 controls, 0/11 evidence verify-fails; qwen3:30b-a3b left Ollama ~09-23)
set -u
cd "$(dirname "$0")/.."
LOG=notes/.running/approaches_register_nightly_$(date +%Y-%m-%d_%H%M).log
echo "== $(date)  model=${APPROACHES_MODEL:-qwen3.8:27b} api=${APPROACHES_API:-ollama}" | tee "$LOG"
python3 play/keeper_approaches_register.py --selftest >> "$LOG" 2>&1 || { echo "SELFTEST FAIL — see $LOG"; exit 1; }
python3 play/keeper_approaches_register.py -v --controls play/keeper_approaches_controls_RH.tsv >> "$LOG" 2>&1
RC=$?   # 2 = controls mismatch (reported, not fatal: 9/11 is the known state); 1 = build failure
echo "== $(date) exit=$RC" | tee -a "$LOG"
grep -E "^rows=|^CONTROLS|Unstable" "$LOG" notes/BST_Approaches_Register.md | tail -4
[ "$RC" -eq 2 ] && exit 0
exit $RC
