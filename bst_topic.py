#!/usr/bin/env python3
"""
bst_topic.py — ask the BST corpus a topic and get the CURRENT view (computed, never hand-maintained).

    python3 bst_topic.py "up quark"              # all matching notes, reverse-chronological (newest first)
    python3 bst_topic.py "up quark" --current    # only the current/supported head(s) — the "modern reference"
    python3 bst_topic.py --lint                  # drift report (broken chains, missed stamps, mixed-status)
    python3 bst_topic.py --lint "glueball"       # lint restricted to a topic

Built to the supersession spec (Keeper, 2026-07-27 [RECONCILE]):
  notes/BST_supersession_convention_SPEC_for_bst_topic_and_stamping_2026-07-27.md

Current-state is COMPUTED from each note's frontmatter (status / superseded_by / claims), never stored —
so it can't drift like the hand-maintained ledger that misled the auditor on m_u. Notes not yet stamped
(the retrofit is in progress) fall back to filename-date + title and are treated as `current`.

Zero external dependencies (stdlib only) — reviewer-runnable like verify_bst.py.
Casey Koons & Elie | 2026-07-27 [PROGRAM: RECONCILE]
"""
import os, re, sys, glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
NOTES_DIR = os.path.join(SCRIPT_DIR, "notes")
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")


# ───────────────────────── minimal YAML-subset frontmatter parser (zero-dep) ─────────────────────────
# Handles exactly the spec schema: scalar `k: v`, inline list `k: [a, b]`, `null`, and the nested
# `claims:` block-list of dicts. Not a general YAML parser — deliberately small and auditable.

def _strip_comment(s):
    i = s.find(" #")
    return (s[:i] if i != -1 else s).strip()

def _scalar_or_list(s):
    s = s.strip()
    # quoted string: take the quoted content literally (a '#' inside is NOT a comment — e.g. "Paper #103")
    if len(s) >= 2 and s[0] in "\"'":
        end = s.find(s[0], 1)
        if end != -1:
            return s[1:end]
    s = _strip_comment(s)
    if s in ("null", "~", ""):
        return None
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        return [x.strip().strip('"').strip("'") for x in inner.split(",")] if inner else []
    return s.strip('"').strip("'")

def _parse_block_list(sub):
    items, cur = [], None
    for line in sub:
        st = line.strip()
        if not st or st.startswith("#"):
            continue
        if st.startswith("- "):
            if cur is not None:
                items.append(cur)
            cur = {}
            st = st[2:]
            if ":" in st:
                k, _, v = st.partition(":")
                cur[k.strip()] = _scalar_or_list(v)
        elif cur is not None and ":" in st:
            k, _, v = st.partition(":")
            cur[k.strip()] = _scalar_or_list(v)
    if cur is not None:
        items.append(cur)
    return items

def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    lines = text[3:end].split("\n")
    d, i, n = {}, 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#") or line.startswith((" ", "\t")):
            i += 1
            continue
        key, _, rest = line.partition(":")
        key, rest = key.strip(), rest.strip()
        if rest == "":                       # possible block (claims:) — gather indented lines
            sub, j = [], i + 1
            while j < n and (lines[j].startswith((" ", "\t")) or not lines[j].strip()):
                sub.append(lines[j])
                j += 1
            d[key] = _parse_block_list(sub) if any(s.strip().startswith("- ") for s in sub) else None
            i = j
        else:
            d[key] = _scalar_or_list(rest)
            i += 1
    return d


# ───────────────────────── the note model ─────────────────────────

class Note:
    def __init__(self, path):
        self.path = path
        self.fname = os.path.basename(path)
        with open(path, "r", errors="ignore") as f:
            head = f.read(8000)
        self.fm = parse_frontmatter(head)
        # title = first '# ' heading in the body
        self.title = ""
        for ln in head.split("\n"):
            if ln.startswith("# "):
                self.title = ln[2:].strip()
                break
        # date: frontmatter (normalized to YYYY-MM-DD), else filename, else title, else epoch-min
        self.date = (self._date_from(self.fm.get("date")) or self._date_from(self.fname)
                     or self._date_from(self.title) or "0000-00-00")
        # id: frontmatter, else leading token of filename (K755 / F704 / toy_4875), else stem
        self.id = self.fm.get("id") or self._id_from_fname()
        # normalize status: catches both the new form ("superseded") and old prose ("SUPERSEDED by Paper #103")
        s = (self.fm.get("status") or "current").strip().lower()
        if "supersed" in s:
            self.status = "partially-superseded" if "part" in s else "superseded"
        else:
            self.status = "current"
        self.superseded_by = self.fm.get("superseded_by")
        self.supersedes = self.fm.get("supersedes") or []
        self.topic_tags = self.fm.get("topic_tags") or []
        self.claims = self.fm.get("claims") or []
        # "stamped" = supersession-aware (has status / superseded_by / claims), not merely "has frontmatter"
        self.stamped = bool(self.fm.get("status") or self.fm.get("superseded_by") or self.fm.get("claims"))

    @staticmethod
    def _date_from(s):
        m = DATE_RE.search(s or "")
        return m.group(1) if m else None

    def _id_from_fname(self):
        m = re.match(r"(K\d+|F\d+|T\d+|toy_\d+|INV-\d+)", self.fname)
        return m.group(1) if m else self.fname[:-3][:40]

    def haystack(self):
        parts = [self.title, self.fname[:-3]] + list(self.topic_tags)
        parts += [c.get("topic", "") for c in self.claims]
        # normalize: lowercase, hyphen->space (so "up-quark" matches "up quark"); keep '_' (m_u, sin2_theta)
        return " ".join(parts).lower().replace("-", " ")

    def matches(self, topic):
        hay = self.haystack()
        # all whitespace-separated query tokens must appear (AND); hyphens normalized like the haystack
        toks = topic.lower().replace("-", " ").split()
        return all(t in hay for t in toks)

    def current_claims(self):
        """The supported/current claims (for --current). Empty list means 'note-level status governs'."""
        if not self.claims:
            return None
        return [c for c in self.claims if (c.get("status") or "current").lower() in ("current", "supported")]

    def is_current(self):
        if self.status == "superseded":
            return False
        if self.status == "partially-superseded":
            cc = self.current_claims()
            return bool(cc)
        return True   # 'current' or unstamped-default

    def line(self):
        stamp = self.status if self.stamped else "current*"   # * = unstamped default
        one = (self.title or self.fname)[:78]
        return f"  {self.date}  {self.id:14.14s}  [{stamp:20.20s}]  {one}"


# ───────────────────────── index ─────────────────────────

def load_notes():
    notes = []
    for path in glob.glob(os.path.join(NOTES_DIR, "**", "*.md"), recursive=True):
        if os.sep + ".running" + os.sep in path:      # transient broadcast files, not corpus notes
            continue
        try:
            notes.append(Note(path))
        except Exception:
            pass
    return notes


# ───────────────────────── commands ─────────────────────────

def cmd_topic(topic, current_only):
    notes = [n for n in load_notes() if n.matches(topic)]
    notes.sort(key=lambda n: n.date, reverse=True)
    if current_only:
        notes = [n for n in notes if n.is_current()]
    label = "CURRENT view (modern reference)" if current_only else "ALL notes, reverse-chronological"
    print()
    print(f'bst_topic "{topic}" — {label}')
    print("=" * 100)
    if not notes:
        print("  (no matching notes)")
    for n in notes:
        print(n.line())
        if current_only and n.status == "partially-superseded":
            for c in (n.current_claims() or []):
                print(f"        └─ supported claim: {c.get('topic','?')}")
    print("=" * 100)
    stamped = sum(1 for n in notes if n.stamped)
    print(f"  {len(notes)} notes  ·  {stamped} stamped, {len(notes)-stamped} unstamped (shown as current* — retrofit in progress)")
    print()


NOTE_ID_TOK = re.compile(r"\b(K\d+|F\d+|toy_\d+|INV-\d+)\b")   # ids that name a NOTE (T\d+ = theorem, lives in the graph)

def cmd_lint(topic=None):
    notes = load_notes()
    if topic:
        notes = [n for n in notes if n.matches(topic)]
    by_id = {}
    for n in notes:
        by_id.setdefault(n.id, n)

    def resolve_note(val):
        """Find the NOTE a superseded_by value points to (by id token or filename-stem substring), else None."""
        if not val:
            return None
        for tok in NOTE_ID_TOK.findall(val):
            if tok in by_id:
                return by_id[tok]
        for m in notes:
            if m.fname[:-3] in val:
                return m
        return None

    def references(val, note):
        return bool(val) and (note.id in (val or "") or note.fname[:-3] in (val or ""))

    findings = []

    # (1) broken chains: a note→NOTE supersession pointer that lands on a superseded note or a named-but-missing note.
    #     (Pointers to theorems T#, papers, or prose are NOT note-chains — not flagged here.)
    for n in notes:
        targets = ([n.superseded_by] if n.superseded_by else []) + [c["superseded_by"] for c in n.claims if c.get("superseded_by")]
        for t in targets:
            tgt = resolve_note(t)
            m = NOTE_ID_TOK.search(t)
            if tgt is not None and tgt.status == "superseded":
                findings.append(("BROKEN-CHAIN", n, f"superseded_by → '{tgt.id}' which is itself superseded (points past the current head)"))
            elif tgt is None and m:
                findings.append(("BROKEN-CHAIN", n, f"superseded_by names note '{m.group(1)}' not found in corpus"))

    # (2) multi-claim mixed status (highest-drift): partially-superseded or claims of differing status
    for n in notes:
        if n.claims:
            sts = {(c.get("status") or "current").lower() for c in n.claims}
            if len(sts) > 1 or n.status == "partially-superseded":
                findings.append(("MULTI-CLAIM-MIXED", n, f"{len(n.claims)} claims, statuses {sorted(sts)} — one id, mixed status"))

    # (3) candidate missed stamps (the m_u shape): an older 'current' note shares a topic_tag with a
    #     newer note that does NOT list it in `supersedes` — possible un-stamped supersession.
    tagged = [n for n in notes if n.topic_tags]
    for older in tagged:
        if older.status == "superseded":
            continue
        for newer in tagged:
            if newer is older or newer.date <= older.date:
                continue
            shared = set(older.topic_tags) & set(newer.topic_tags)
            if not shared:
                continue
            # already-stamped link either way (older→newer, or newer.supersedes older) → not a missed stamp
            older_targets = ([older.superseded_by] if older.superseded_by else []) + [c.get("superseded_by") for c in older.claims]
            if any(references(t, newer) for t in older_targets):
                continue
            if any(references(s, older) or s == older.id for s in newer.supersedes):
                continue
            # if the shared topic is covered by an already-superseded claim of `older`, it's handled
            covered = any((c.get("status") or "").lower() == "superseded" and set([c.get("topic", "")]) for c in older.claims
                          if any(tag in (c.get("topic", "") or "").lower() for tag in shared))
            if covered:
                continue
            findings.append(("CANDIDATE-MISSED-STAMP", older,
                             f"shared topic {sorted(shared)} with newer {newer.id} ({newer.date}) which doesn't supersede it — un-stamped supersession?"))
            break

    print()
    print(f"bst_topic --lint{(' ' + repr(topic)) if topic else ''} — corpus-currency drift report")
    print("=" * 100)
    if not findings:
        print("  no drift found (among stamped notes; unstamped notes are assumed current pending retrofit)")
    order = {"BROKEN-CHAIN": 0, "MULTI-CLAIM-MIXED": 1, "CANDIDATE-MISSED-STAMP": 2}
    for kind, n, detail in sorted(findings, key=lambda f: order.get(f[0], 9)):
        print(f"  [{kind}] {n.id} ({n.date})")
        print(f"        {detail}")
    print("=" * 100)
    nstamp = sum(1 for n in notes if n.stamped)
    print(f"  scanned {len(notes)} notes ({nstamp} stamped) · {len(findings)} findings")
    print("  note: coverage grows as the reverse-walk stamps the corpus; unstamped notes can't be chain-checked yet.")
    print()


def main(argv):
    args = argv[1:]
    current_only = "--current" in args
    lint = "--lint" in args
    positional = [a for a in args if not a.startswith("--")]
    topic = positional[0] if positional else None
    if lint:
        cmd_lint(topic)
    elif topic:
        cmd_topic(topic, current_only)
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv)
