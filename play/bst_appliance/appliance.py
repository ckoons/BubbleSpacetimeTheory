#!/usr/bin/env python3
"""BST Appliance v1.1 — The Ball and Counting Tool.

Science Engineering appliance: translates physics/chemistry/biology questions
into BST integer expressions in Q(integers)[pi].

v1.0: Read path (lookup).  v1.1: Write path (discovery).

Usage:
    python -m bst_appliance "proton mass"
    python -m bst_appliance --discover 42 angle_deg
    python -m bst_appliance --interactive
    python -m bst_appliance --list
    python -m bst_appliance --integers

Five integers.  Zero free parameters.  "Give a child a ball and teach them to count."
"""
import sys
import os

# Add parent directory to path so we can run from play/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bst_appliance.parser import search, find_best, list_categories
from bst_appliance.output import format_answer, format_gap, format_browse, format_integers
from bst_appliance.knowledge_base import PREDICTIONS


HELP_TEXT = """
BST Appliance v1.1 — The Ball and Counting Tool

READ PATH (lookup):
  <query>             Search for a BST prediction
  list                Show all categories
  list <category>     Show predictions in category
  integers            Show the five BST integers
  all                 Show all predictions

WRITE PATH (discovery):
  discover <value> <type>   Find BST expressions matching a value
                            Types: count, ratio, angle_deg, length_bohr, energy_ry
  discover --save <value> <type>  Find match AND queue for Keeper audit
  discover 42 angle_deg     → finds C_2*g = 42 (rainbow angle)
  discover 20 count         → finds C_2*N_c+rank = 20 (amino acids)
  discover 0.685 ratio      → finds 13/19 (dark energy)

OTHER:
  help                Show this help
  quit / exit         Exit

Examples:
  proton mass         -> m_p/m_e = 6*pi^5 (0.002%)
  dark energy         -> Omega_Lambda = 13/19 (0.07 sigma)
  discover 42 angle_deg -> C_2*g = 42° (rainbow, 0.07%)
"""


def handle_query(query):
    """Process a query and return formatted output."""
    q = query.strip().lower()

    if q in ("help", "?", "h"):
        return HELP_TEXT

    if q in ("quit", "exit", "q"):
        return None  # signal to exit

    if q == "integers":
        return format_integers()

    if q == "list":
        return format_browse()

    if q.startswith("list "):
        category = q[5:].strip()
        return format_browse(category)

    # Discovery mode: "discover <value> <type>"
    if q.startswith("discover "):
        return handle_discover(q[9:].strip())

    if q == "all":
        lines = []
        for p in PREDICTIONS:
            try:
                from bst_appliance.evaluator import evaluate
                val = evaluate(p["code"])
                if val == float('inf'):
                    val_str = "inf"
                elif val == int(val) and abs(val) < 1e6:
                    val_str = str(int(val))
                else:
                    val_str = f"{val:.6g}"
            except Exception:
                val_str = "—"
            lines.append(f"  [{p['id']:>6}] {p['name']:<40} = {val_str:<12} ({p['precision']})")
        return "\n".join(lines)

    # Search
    results = search(query, top_n=5)

    if not results:
        return format_gap(query)

    best_score, best_pred = results[0]

    if best_score < 3:
        # Low confidence — show gap with suggestions
        output = format_gap(query)
        if results:
            output += "\n\n  Did you mean:\n"
            for sc, pred in results[:3]:
                output += f"    - {pred['name']} ({pred['id']})\n"
        return output

    # Show the best match
    output = format_answer(best_pred, query)

    # If there are other close matches, mention them
    if len(results) > 1 and results[1][0] > best_score * 0.5:
        output += "\n  See also:"
        for sc, pred in results[1:3]:
            output += f"\n    - {pred['name']} ({pred['id']})"
        output += "\n"

    return output


def handle_discover(args_str):
    """Handle discovery mode: 'discover [--save] <value> [type]'."""
    from bst_appliance.discovery import discover, format_discovery_output, queue_proposal

    parts = args_str.split()

    # Check for --save flag
    save = False
    if "--save" in parts:
        save = True
        parts.remove("--save")

    if len(parts) < 1:
        return "  Usage: discover [--save] <value> [type]\n  Types: count, ratio, angle_deg, length_bohr, energy_ry"

    try:
        observed = float(parts[0])
    except ValueError:
        return f"  Error: '{parts[0]}' is not a number."

    obs_type = parts[1] if len(parts) > 1 else None

    VALID_TYPES = {"count", "ratio", "angle_deg", "length_bohr", "energy_ry"}
    if obs_type and obs_type not in VALID_TYPES:
        return f"  Unknown type: '{obs_type}'. Valid types: {', '.join(sorted(VALID_TYPES))}"

    # If no type specified, try to guess
    if obs_type is None:
        if observed == int(observed) and 1 <= observed <= 1000:
            obs_type = "count"
        else:
            obs_type = "ratio"

    clean_args = " ".join(parts)
    proposals = discover(clean_args, observed, obs_type, tolerance=0.05)
    output = format_discovery_output(f"discover {observed} {obs_type}", proposals, show_all=True)

    if save and proposals:
        n = queue_proposal(proposals[0])
        output += f"\n  Proposal #{n} queued for Keeper audit."

    return output


def interactive_mode():
    """Run the appliance in interactive mode."""
    print(format_integers())
    print()
    print("  Type a question, 'list', 'integers', or 'help'.")
    print("  Type 'quit' to exit.\n")

    while True:
        try:
            query = input("BST> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n")
            break

        if not query:
            continue

        result = handle_query(query)
        if result is None:
            break
        print(result)
        print()


def main():
    """Entry point."""
    args = sys.argv[1:]

    if not args or args == ["--interactive"] or args == ["-i"]:
        interactive_mode()
        return

    if args == ["--list"] or args == ["-l"]:
        print(format_browse())
        return

    if len(args) == 2 and args[0] in ("--list", "-l"):
        print(format_browse(args[1]))
        return

    if args == ["--integers"]:
        print(format_integers())
        return

    if args == ["--help"] or args == ["-h"]:
        print(HELP_TEXT)
        return

    if args == ["--all"]:
        print(handle_query("all"))
        return

    if args[0] == "--discover":
        print(handle_discover(" ".join(args[1:])))
        return

    # Treat all args as a query
    query = " ".join(args)
    result = handle_query(query)
    if result:
        print(result)


if __name__ == "__main__":
    main()
