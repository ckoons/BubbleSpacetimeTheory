#!/bin/bash
# Atomic toy/theorem number management.
# Usage:
#   ./claim_number.sh toy [count]    — claim number(s): recycle list first, then counter
#   ./claim_number.sh theorem [count] — claim theorem number(s)
#   ./claim_number.sh recover        — scan for gaps, populate recycle list
#   ./claim_number.sh audit          — find duplicate toy numbers (two files, same number)
#
# Flow: recycle list -> pop first available -> if empty, bump counter.
# Before returning, checks no file already exists with that number.
# Uses mkdir as atomic lock (POSIX-portable, works on macOS).

set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
RECYCLE_FILE="$DIR/.recycle_toys"

# --- Check if a toy number already has a file ---
toy_file_exists() {
  local n="$1"
  ls "$DIR"/toy_${n}_*.py &>/dev/null || ls "$DIR"/toy_${n}.py &>/dev/null
}

# --- Audit: find duplicate toy numbers ---
if [ "${1:-}" = "audit" ]; then
  echo "Scanning for duplicate toy numbers..."
  DUPES=0
  # Extract all toy numbers from filenames
  ls "$DIR"/toy_*.py 2>/dev/null | sed -E 's/.*\/toy_([0-9]+).*/\1/' | sort -n | uniq -d | while read -r NUM; do
    echo "  DUPLICATE: toy_${NUM} has multiple files:"
    ls "$DIR"/toy_${NUM}_*.py "$DIR"/toy_${NUM}.py 2>/dev/null | sed 's/^/    /'
    DUPES=$((DUPES + 1))
  done
  # Count dupes (subshell above doesn't propagate)
  DCOUNT=$(ls "$DIR"/toy_*.py 2>/dev/null | sed -E 's/.*\/toy_([0-9]+).*/\1/' | sort -n | uniq -d | wc -l | tr -d ' ')
  if [ "$DCOUNT" -eq 0 ]; then
    echo "No duplicates found."
  else
    echo "$DCOUNT duplicate number(s) found. Resolve by renaming one file in each pair."
  fi
  exit 0
fi

# --- Recover: scan for gaps, populate recycle list ---
if [ "${1:-}" = "recover" ]; then
  CURRENT=$(cat "$DIR/.next_toy" 2>/dev/null || echo 1)
  START=$(( CURRENT > 200 ? CURRENT - 200 : 1 ))
  END=$((CURRENT - 1))
  GAPS=""
  GAP_COUNT=0
  for i in $(seq "$START" "$END"); do
    if ! toy_file_exists "$i"; then
      GAPS="$GAPS $i"
      GAP_COUNT=$((GAP_COUNT + 1))
    fi
  done
  if [ -z "$GAPS" ]; then
    echo "No gaps in range ${START}-${END}. Next available: $CURRENT"
  else
    # Write gaps to recycle file (one per line, sorted)
    echo "$GAPS" | tr ' ' '\n' | grep -v '^$' | sort -n > "$RECYCLE_FILE"
    echo "Found ${GAP_COUNT} gaps in ${START}-${END}. Written to .recycle_toys."
    echo "Numbers:$GAPS"
    echo "Next claim will pop from this list first."
  fi
  exit 0
fi

# --- Claim mode ---
TYPE="${1:-toy}"
COUNT="${2:-1}"

case "$TYPE" in
  toy)     FILE="$DIR/.next_toy" ;;
  theorem) FILE="$DIR/.next_theorem" ;;
  *)       echo "Usage: $0 {toy|theorem|recover|audit} [count]" >&2; exit 1 ;;
esac

LOCKDIR="${FILE}.lock"

# Acquire lock (mkdir is atomic on all filesystems)
TRIES=0
while ! mkdir "$LOCKDIR" 2>/dev/null; do
  TRIES=$((TRIES + 1))
  if [ "$TRIES" -gt 50 ]; then
    echo "ERROR: Could not acquire lock after 5s. Stale lock? Remove $LOCKDIR" >&2
    exit 1
  fi
  sleep 0.1
done
trap 'rmdir "$LOCKDIR" 2>/dev/null' EXIT

CLAIMED=""
CLAIMED_COUNT=0

# --- Try recycle list first (toys only) ---
if [ "$TYPE" = "toy" ] && [ -f "$RECYCLE_FILE" ] && [ -s "$RECYCLE_FILE" ]; then
  while [ "$CLAIMED_COUNT" -lt "$COUNT" ] && [ -s "$RECYCLE_FILE" ]; do
    CANDIDATE=$(head -1 "$RECYCLE_FILE")
    # Remove from list
    tail -n +2 "$RECYCLE_FILE" > "${RECYCLE_FILE}.tmp" && mv "${RECYCLE_FILE}.tmp" "$RECYCLE_FILE"
    # Verify no file exists (someone may have filled the gap)
    if toy_file_exists "$CANDIDATE"; then
      continue  # skip, already used
    fi
    CLAIMED="$CLAIMED $CANDIDATE"
    CLAIMED_COUNT=$((CLAIMED_COUNT + 1))
  done
  # Clean up empty recycle file
  if [ ! -s "$RECYCLE_FILE" ]; then
    rm -f "$RECYCLE_FILE"
  fi
fi

# --- Fill remaining from counter ---
if [ "$CLAIMED_COUNT" -lt "$COUNT" ]; then
  CURRENT=$(cat "$FILE" 2>/dev/null || echo 1)
  REMAINING=$((COUNT - CLAIMED_COUNT))
  for i in $(seq 1 "$REMAINING"); do
    # Skip if file already exists (duplicate protection — toys only)
    if [ "$TYPE" = "toy" ]; then
      while toy_file_exists "$CURRENT" 2>/dev/null; do
        CURRENT=$((CURRENT + 1))
      done
    fi
    CLAIMED="$CLAIMED $CURRENT"
    CLAIMED_COUNT=$((CLAIMED_COUNT + 1))
    CURRENT=$((CURRENT + 1))
  done
  echo "$CURRENT" > "$FILE"
fi

# Output
CLAIMED=$(echo "$CLAIMED" | xargs)  # trim whitespace
if [ "$COUNT" -eq 1 ]; then
  echo "$CLAIMED"
else
  echo "$CLAIMED"
fi
