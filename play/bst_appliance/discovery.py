"""BST Discovery Engine — the write path.

When a query has no match in the knowledge base, the discovery engine:
  1. Classifies the observable type
  2. Generates BST candidate expressions
  3. Finds matches within tolerance
  4. Proposes theorems for Keeper audit

SAFETY: Never auto-registers. All proposals go to audit queue.
"""
from .candidate_generator import find_matches

# Observable type detection heuristics
TYPE_KEYWORDS = {
    "angle_deg": ["angle", "degrees", "°", "arccos", "bend", "tilt"],
    "count": ["number", "count", "how many", "total", "integer"],
    "length_bohr": ["length", "radius", "distance", "bond length", "angstrom", "bohr"],
    "energy_ry": ["energy", "binding", "dissociation", "rydberg", "ev", "mev"],
    "ratio": ["ratio", "fraction", "percentage", "coupling", "constant"],
}


def classify_observable(query, value=None):
    """Guess the observable type from the query text."""
    q = query.lower()

    for obs_type, keywords in TYPE_KEYWORDS.items():
        for kw in keywords:
            if kw in q:
                return obs_type

    # If value is an integer, try count
    if value is not None and isinstance(value, (int, float)):
        if value == int(value) and 1 <= value <= 1000:
            return "count"

    return "ratio"  # default


def discover(query, observed_value, obs_type=None, tolerance=0.02):
    """Run the discovery pipeline.

    Returns list of proposal dicts, sorted by accuracy.
    """
    if obs_type is None:
        obs_type = classify_observable(query, observed_value)

    matches = find_matches(observed_value, obs_type, tolerance)

    proposals = []
    for name, predicted, error in matches:
        accuracy_pct = error * 100

        # Determine depth: count/ratio with no pi = 0, with pi = 1
        if "pi" in name.lower() or "arccos" in name.lower():
            depth = 1
        elif obs_type in ("count",):
            depth = 0
        else:
            depth = 0

        # Count unique BST integers used
        integers_used = []
        for int_name in ["N_c", "n_C", "C_2", "N_max", "rank"]:
            if int_name in name:
                integers_used.append(int_name)
        # g needs special handling (avoid matching "deg", etc.)
        if "g" in name.split("*") or "g" in name.split("/") or name == "g" or name.startswith("g*") or name.startswith("g/") or "/g" in name or "*g" in name:
            integers_used.append("g")

        # Non-uniqueness warning
        is_unique = True
        if len(matches) > 1 and len(matches) >= 2:
            # Check if top 2 matches are comparably good
            if matches[1][2] < error * 2 + 0.001:
                is_unique = False

        proposal = {
            "query": query,
            "expression": name,
            "predicted": predicted,
            "observed": observed_value,
            "accuracy_pct": accuracy_pct,
            "obs_type": obs_type,
            "depth": depth,
            "integers": integers_used,
            "is_unique": is_unique,
            "status": "PROPOSED",
            "falsification": (
                f"Disproved if measured value deviates from "
                f"{predicted:.6g} by more than 2%."
            ),
        }
        proposals.append(proposal)

    return proposals


def format_proposal(proposal):
    """Format a proposal for display."""
    p = proposal
    lines = []
    lines.append(f"  PROPOSED: {p['query']} = {p['expression']}")
    lines.append(f"  Predicted: {p['predicted']:.6g}")
    lines.append(f"  Observed:  {p['observed']:.6g}")
    lines.append(f"  Accuracy:  {p['accuracy_pct']:.4f}%")
    lines.append(f"  Depth:     {p['depth']}")
    lines.append(f"  Integers:  {', '.join(p['integers']) if p['integers'] else 'pure geometry'}")

    if not p['is_unique']:
        lines.append(f"  WARNING:   Non-unique decomposition (multiple matches)")

    lines.append(f"  Status:    {p['status']} — needs Keeper audit")
    return "\n".join(lines)


def format_discovery_output(query, proposals, show_all=False):
    """Format the full discovery mode output."""
    from .output import hline, boxline, BOX_W

    lines = []
    lines.append(hline("═"))
    lines.append(boxline("BST APPLIANCE v1.1 — DISCOVERY MODE", "center"))
    lines.append(hline("─"))
    lines.append(boxline(f"Query: {query}"))

    if not proposals:
        lines.append(boxline(f""))
        lines.append(boxline(f"  No BST expression matches within tolerance."))
        lines.append(boxline(f"  This observable may be outside BST scope."))
        lines.append(hline("═"))
        return "\n".join(lines)

    best = proposals[0]
    lines.append(boxline(f"Mode:  DISCOVERY"))
    lines.append(hline("─"))
    lines.append(boxline(f""))
    lines.append(boxline(f"  BEST MATCH:"))
    lines.append(boxline(f"  {best['expression']} = {best['predicted']:.6g}"))
    lines.append(boxline(f"  Observed:  {best['observed']:.6g}"))
    lines.append(boxline(f"  Accuracy:  {best['accuracy_pct']:.4f}%"))
    lines.append(boxline(f"  Depth:     {best['depth']}"))

    ints = ", ".join(best["integers"]) if best["integers"] else "—"
    lines.append(boxline(f"  Integers:  {ints}"))

    if not best["is_unique"]:
        lines.append(boxline(f""))
        lines.append(boxline(f"  ** NON-UNIQUE: multiple BST expressions match **"))

    lines.append(boxline(f""))
    lines.append(boxline(f"  Status: PROPOSED — needs Keeper audit"))
    lines.append(boxline(f"  {best['falsification']}"))

    if show_all and len(proposals) > 1:
        lines.append(hline("─"))
        lines.append(boxline(f"  Other candidates:"))
        for p in proposals[1:5]:
            lines.append(boxline(f"    {p['expression']} = {p['predicted']:.6g} ({p['accuracy_pct']:.4f}%)"))

    lines.append(hline("═"))
    return "\n".join(lines)
