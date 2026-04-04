"""BST Output Formatter — three display modes.

Mode 1: ANSWER  (theorem exists, value computed)
Mode 2: GAP     (no theorem, but fertile gap identified)
Mode 3: BROWSE  (list predictions by category)
"""
from .evaluator import evaluate, show_integers


# ── Tier labels ───────────────────────────────────────────────────────
TIER_LABELS = {
    1: "[DERIVED]",
    2: "[STRUCTURAL]",
    3: "[OBSERVED -- mechanism TBD]",
}

def tier_label(prediction):
    """Return the display label for a prediction's tier."""
    t = prediction.get("tier", 0)
    return TIER_LABELS.get(t, "[UNKNOWN TIER]")


# ── Box drawing ────────────────────────────────────────────────────────
BOX_W = 62

def hline(char="─"):
    return "+" + char * BOX_W + "+"

def boxline(text, align="left"):
    if align == "center":
        padded = text.center(BOX_W)
    else:
        padded = f" {text}".ljust(BOX_W)
    return f"|{padded}|"


def format_answer(prediction, query=""):
    """Format Mode 1: ANSWER — full prediction display."""
    p = prediction

    # Evaluate the BST expression
    try:
        predicted_val = evaluate(p["code"])
    except Exception:
        predicted_val = None

    # Compute deviation
    measured = p["measured"]
    if predicted_val is not None and measured not in (None, 0, float('inf')):
        if measured == float('inf') or predicted_val == float('inf'):
            dev_str = "exact (both infinite)"
        else:
            dev = abs(predicted_val - measured) / abs(measured) * 100
            dev_str = f"{dev:.4f}%"
    else:
        dev_str = p.get("precision", "—")

    # Integer decomposition
    int_list = p.get("integers", [])
    int_str = ", ".join(int_list) if int_list else "pure geometry"

    # Tier display
    tlabel = tier_label(p)
    mechanism = p.get("mechanism", "")

    lines = []
    lines.append(hline("═"))
    lines.append(boxline("BST APPLIANCE v2.0", "center"))
    lines.append(hline("─"))

    if query:
        lines.append(boxline(f"Query: {query}"))
    lines.append(boxline(f"Mode:  ANSWER"))
    lines.append(hline("─"))

    lines.append(boxline(f"  {p['name']}"))
    lines.append(boxline(f"  Tier: {tlabel}"))
    lines.append(boxline(f""))
    lines.append(boxline(f"  BST Formula: {p['formula']}"))
    lines.append(boxline(f""))

    if predicted_val is not None:
        if predicted_val == float('inf'):
            lines.append(boxline(f"  Predicted:  infinity"))
        elif predicted_val == int(predicted_val) and abs(predicted_val) < 1e6:
            lines.append(boxline(f"  Predicted:  {int(predicted_val)}"))
        else:
            lines.append(boxline(f"  Predicted:  {predicted_val:.6g}"))

    if measured == float('inf'):
        lines.append(boxline(f"  Measured:   > 1.6e34 yr (Super-K)"))
    elif measured is not None:
        if measured == int(measured) and abs(measured) < 1e6:
            lines.append(boxline(f"  Measured:   {int(measured)}"))
        else:
            lines.append(boxline(f"  Measured:   {measured:.6g}"))

    unit = p.get("unit", "")
    if unit:
        lines.append(boxline(f"  Unit:       {unit}"))

    lines.append(boxline(f"  Accuracy:   {dev_str}"))
    lines.append(boxline(f""))
    lines.append(boxline(f"  Theorem:    {p['id']}"))
    lines.append(boxline(f"  Depth:      {p['depth']}"))
    lines.append(boxline(f"  Integers:   {int_str}"))
    lines.append(boxline(f"  Source:     {p.get('measured_src', '')}"))
    if mechanism:
        lines.append(hline("─"))
        # Word-wrap mechanism to fit in box
        mech_words = mechanism.split()
        mech_line = ""
        for w in mech_words:
            if len(mech_line) + len(w) + 1 > BOX_W - 4:
                lines.append(boxline(f"  {mech_line}"))
                mech_line = w
            else:
                mech_line = f"{mech_line} {w}" if mech_line else w
        if mech_line:
            lines.append(boxline(f"  {mech_line}"))
    lines.append(hline("═"))

    return "\n".join(lines)


def format_gap(query):
    """Format Mode 2: GAP — no theorem exists."""
    lines = []
    from .knowledge_base import PREDICTIONS
    lines.append(hline("═"))
    lines.append(boxline("BST APPLIANCE v2.0", "center"))
    lines.append(hline("─"))
    lines.append(boxline(f"Query: {query}"))
    lines.append(boxline(f"Mode:  GAP"))
    lines.append(hline("─"))
    lines.append(boxline(f""))
    lines.append(boxline(f"  No BST prediction found for this query."))
    lines.append(boxline(f""))
    lines.append(boxline(f"  This may be:"))
    lines.append(boxline(f"  (a) A fertile gap — try rephrasing"))
    lines.append(boxline(f"  (b) Outside BST scope"))
    lines.append(boxline(f"  (c) Not yet in the v2.0 database ({len(PREDICTIONS)} entries)"))
    lines.append(boxline(f""))
    lines.append(boxline(f"  Try: 'list' to see all categories"))
    lines.append(boxline(f"       'list <category>' for predictions"))
    lines.append(hline("═"))
    return "\n".join(lines)


def format_browse(category=None):
    """Format Mode 3: BROWSE — list predictions."""
    from .knowledge_base import PREDICTIONS, get_categories, get_by_category

    lines = []
    # Count tiers
    t1 = sum(1 for p in PREDICTIONS if p.get("tier") == 1)
    t2 = sum(1 for p in PREDICTIONS if p.get("tier") == 2)
    t3 = sum(1 for p in PREDICTIONS if p.get("tier") == 3)

    lines.append(hline("═"))
    lines.append(boxline("BST APPLIANCE v2.0 — Prediction Browser", "center"))
    lines.append(hline("─"))

    if category:
        preds = get_by_category(category)
        if not preds:
            lines.append(boxline(f"  No predictions in category '{category}'"))
        else:
            lines.append(boxline(f"  Category: {category} ({len(preds)} predictions)"))
            lines.append(boxline(f""))
            for p in preds:
                tl = {1: "D", 2: "S", 3: "O"}.get(p.get("tier", 0), "?")
                tag = f"  [{p['id']}] ({tl}) {p['name']}"
                if len(tag) > BOX_W - 1:
                    tag = tag[:BOX_W - 4] + "..."
                lines.append(boxline(tag))
    else:
        cats = get_categories()
        lines.append(boxline(f"  {len(PREDICTIONS)} predictions in {len(cats)} categories:"))
        lines.append(boxline(f""))
        lines.append(boxline(f"  Tier 1 DERIVED:    {t1:>3}  (full proof chain)"))
        lines.append(boxline(f"  Tier 2 STRUCTURAL: {t2:>3}  (mechanism, gaps)"))
        lines.append(boxline(f"  Tier 3 OBSERVED:   {t3:>3}  (numerical match)"))
        lines.append(boxline(f""))
        for cat in cats:
            n = len(get_by_category(cat))
            lines.append(boxline(f"    {cat:<16} {n:>3} predictions"))
        lines.append(boxline(f""))
        lines.append(boxline(f"  Use 'list <category>' to browse"))
        lines.append(boxline(f"  (D)=Derived (S)=Structural (O)=Observed"))

    lines.append(hline("═"))
    return "\n".join(lines)


def format_integers():
    """Format the five BST integers display."""
    lines = []
    lines.append(hline("═"))
    lines.append(boxline("THE FIVE BST INTEGERS", "center"))
    lines.append(hline("─"))
    lines.append(boxline(f""))
    lines.append(boxline(f"  D_IV^5 = SO_0(5,2) / [SO(5) x SO(2)]"))
    lines.append(boxline(f""))
    lines.append(boxline(f"  N_c   = 3     color dimension (SU(3))"))
    lines.append(boxline(f"  n_C   = 5     compact dimension (CP^2)"))
    lines.append(boxline(f"  g     = 7     Bergman genus"))
    lines.append(boxline(f"  C_2   = 6     Casimir invariant"))
    lines.append(boxline(f"  N_max = 137   maximum quantum number"))
    lines.append(boxline(f""))
    lines.append(boxline(f"  rank  = 2     (derived)"))
    lines.append(boxline(f"  pi    = 3.14159...  (the one transcendental)"))
    lines.append(boxline(f""))
    lines.append(boxline(f"  Zero free parameters.  Everything follows."))
    lines.append(hline("═"))
    return "\n".join(lines)
