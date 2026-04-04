#!/bin/bash
# Atomic number claim for .next_toy and .next_theorem
# Usage: ./claim_number.sh toy [count]    — claims count toy numbers (default 1)
#        ./claim_number.sh theorem [count] — claims count theorem numbers (default 1)
#
# Uses mkdir as atomic lock (POSIX-portable, works on macOS).
# Returns the first claimed number. If claiming multiple, prints "start-end".

set -euo pipefail

TYPE="${1:-toy}"
COUNT="${2:-1}"
DIR="$(cd "$(dirname "$0")" && pwd)"

case "$TYPE" in
  toy)     FILE="$DIR/.next_toy" ;;
  theorem) FILE="$DIR/.next_theorem" ;;
  *)       echo "Usage: $0 {toy|theorem} [count]" >&2; exit 1 ;;
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

# Ensure lock is released on exit
trap 'rmdir "$LOCKDIR" 2>/dev/null' EXIT

CURRENT=$(cat "$FILE" 2>/dev/null || echo 1)
FIRST=$CURRENT
LAST=$((CURRENT + COUNT - 1))
NEXT=$((LAST + 1))

echo "$NEXT" > "$FILE"

if [ "$COUNT" -eq 1 ]; then
  echo "$FIRST"
else
  echo "${FIRST}-${LAST}"
fi
