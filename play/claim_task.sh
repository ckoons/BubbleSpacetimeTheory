#!/bin/bash
# claim_task.sh — Atomic task claiming for CI coordination
# Usage: ./play/claim_task.sh <ci_name> <task_description> [toy_number]
#
# Appends a CLAIMED row to notes/.running/CLAIMS.md with mkdir lock.
# Prevents two CIs from claiming the same toy number simultaneously.
#
# Examples:
#   ./play/claim_task.sh Keeper "Chern Class Rosetta Stone" 907
#   ./play/claim_task.sh Grace "Paper #13 re-audit"
#   ./play/claim_task.sh Elie "Edge sprint — cosmology bridges"

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CLAIMS_FILE="$REPO_ROOT/notes/.running/CLAIMS.md"
LOCK_DIR="$REPO_ROOT/notes/.running/.claims.lock"

CI_NAME="${1:-}"
TASK_DESC="${2:-}"
TOY_NUM="${3:-—}"

if [ -z "$CI_NAME" ] || [ -z "$TASK_DESC" ]; then
    echo "Usage: $0 <ci_name> <task_description> [toy_number]"
    echo "  ci_name:    Keeper | Grace | Elie | Lyra | Casey"
    echo "  task_desc:  Short description of the work"
    echo "  toy_number: Optional toy number (use claim_number.sh first!)"
    exit 1
fi

# Atomic lock via mkdir (same pattern as claim_number.sh)
MAX_RETRIES=10
RETRY=0
while ! mkdir "$LOCK_DIR" 2>/dev/null; do
    RETRY=$((RETRY + 1))
    if [ "$RETRY" -ge "$MAX_RETRIES" ]; then
        echo "ERROR: Lock held for too long. Check $LOCK_DIR"
        echo "  If stale: rmdir $LOCK_DIR"
        exit 1
    fi
    sleep 0.2
done

# Ensure lock cleanup on exit
trap 'rmdir "$LOCK_DIR" 2>/dev/null' EXIT

TIMESTAMP=$(date "+%b %d %H:%M")

# Check for duplicate toy number claim
if [ "$TOY_NUM" != "—" ]; then
    if grep -q "| $TOY_NUM " "$CLAIMS_FILE" 2>/dev/null; then
        EXISTING=$(grep "| $TOY_NUM " "$CLAIMS_FILE" | head -1)
        # Check if it's ABANDONED — if so, allow reclaim
        if echo "$EXISTING" | grep -q "ABANDONED"; then
            echo "Reclaiming abandoned toy $TOY_NUM"
            # Update the existing row
            sed -i '' "s/| $TOY_NUM | ABANDONED .*/| $TOY_NUM | CLAIMED | $TIMESTAMP | — |/" "$CLAIMS_FILE" 2>/dev/null || true
        else
            echo "ERROR: Toy $TOY_NUM already claimed:"
            echo "  $EXISTING"
            echo "Pick a different task or mark existing as ABANDONED first."
            exit 1
        fi
    fi
fi

# Insert claim into Active Claims table (before ## Collision Log)
NEW_ROW="| $CI_NAME | $TASK_DESC | $TOY_NUM | CLAIMED | $TIMESTAMP | — |"

# Find the line number of "## Collision Log" and insert before it
COLLISION_LINE=$(grep -n "## Collision Log" "$CLAIMS_FILE" 2>/dev/null | head -1 | cut -d: -f1)

if [ -n "$COLLISION_LINE" ]; then
    # Insert before the Collision Log section (with blank line)
    sed -i '' "${COLLISION_LINE}i\\
${NEW_ROW}
" "$CLAIMS_FILE"
else
    # Fallback: append to end
    echo "$NEW_ROW" >> "$CLAIMS_FILE"
fi

echo "CLAIMED: $CI_NAME → $TASK_DESC (Toy: $TOY_NUM)"
echo "  File: $CLAIMS_FILE"
echo "  Remember: UPDATE to DONE when file exists + tests pass."
