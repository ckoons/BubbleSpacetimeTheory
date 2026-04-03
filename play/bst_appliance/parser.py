"""BST Parser — question to prediction matcher.

v1: keyword matching with substring search and scoring.
v2 will add fuzzy matching / embedding similarity.
"""
from .knowledge_base import PREDICTIONS, get_categories, get_by_category


def normalize(text):
    """Lowercase, strip punctuation, collapse whitespace."""
    import re
    text = text.lower().strip()
    text = re.sub(r"[^\w\s/']", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def score_match(query_tokens, prediction):
    """Score how well a query matches a prediction.

    Returns (score, prediction) where higher score = better match.
    Scoring:
      +10 for exact keyword phrase match
      +3  for each query token found in any keyword
      +1  for token found in name
    """
    query_text = " ".join(query_tokens)
    score = 0

    # Check keyword phrases
    for kw in prediction["keywords"]:
        kw_norm = normalize(kw)
        if kw_norm == query_text:
            score += 20  # exact keyword match
        elif kw_norm in query_text or query_text in kw_norm:
            score += 10  # substring match on keyword
        else:
            # Token-level matching within keywords
            for qt in query_tokens:
                if qt in kw_norm:
                    score += 3

    # Check name
    name_norm = normalize(prediction["name"])
    for qt in query_tokens:
        if qt in name_norm:
            score += 1

    # Check category
    cat_norm = normalize(prediction["category"])
    for qt in query_tokens:
        if qt in cat_norm:
            score += 1

    return score


def search(query, top_n=5):
    """Search predictions by natural language query.

    Returns list of (score, prediction) sorted by score descending.
    Only includes results with score > 0.
    """
    query_norm = normalize(query)
    query_tokens = query_norm.split()

    if not query_tokens:
        return []

    results = []
    for pred in PREDICTIONS:
        sc = score_match(query_tokens, pred)
        if sc > 0:
            results.append((sc, pred))

    results.sort(key=lambda x: -x[0])
    return results[:top_n]


def find_best(query):
    """Return the single best-matching prediction, or None."""
    results = search(query, top_n=1)
    if results and results[0][0] > 0:
        return results[0][1]
    return None


def list_categories():
    """Return formatted category listing."""
    cats = get_categories()
    lines = []
    for cat in cats:
        preds = get_by_category(cat)
        lines.append(f"  {cat:<16} ({len(preds)} predictions)")
    return "\n".join(lines)
