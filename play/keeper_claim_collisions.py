#!/usr/bin/env python3
"""keeper_claim_collisions — find places where the corpus asserts two different
things about the SAME named object.

Why this exists. On 2026-08-28 the corpus was found to contain, simultaneously:
  * T1043: "The B_2 root system has three root lengths"
  * RUNNING_NOTES:1395: "B_2 exponents {1,3} verified from eigenvalue phases"
and separately |rho|^2 = 37/2 in four files, four months after that value was
ruled wrong and every BARE instance of it was swept. The wrong ones survived by
wearing a convention note; a correction rule written against "~9X%" likewise
missed "~5%", the same forbidden claim from the other end.

Every one of those escapes has the same cause: OUR SWEEPS MATCH SURFACE FORMS.
They are written against how an error has appeared so far, not against what the
error IS. This tool does not match a form. It groups every sentence mentioning an
object by the VALUES it asserts, and reports when the groups disagree. The
disagreement is the signal; a human adjudicates which side is right.

    keeper_claim_collisions.py 'B_2|B₂'
    keeper_claim_collisions.py 'rho|ρ' --near 'norm|\\|.*\\|\\^2'
    keeper_claim_collisions.py 'n_C' --root notes --ext md

It is deliberately dumb about semantics and deliberately loud about conflict.
False positives are expected and cheap; a missed collision is what costs four
months.

Author: Keeper, 2026-08-28.
"""

import argparse
import os
import re
import sys
from collections import defaultdict

# What counts as an asserted value: integers, fractions, ratios, set literals,
# and simple tuples. These are the things two sentences can disagree about.
VALUE = re.compile(
    r"\{[^}]{1,40}\}"           # {1,3}
    r"|\([^)]{1,40}\)"          # (5/2, 3/2)
    r"|\d+\s*/\s*\d+"           # 37/2
    r"|\d+(?::\d+)+"            # 1:3:5
    r"|\b\d+(?:\.\d+)?\b"       # 3, 0.0019
    r"|\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten)\b",
    re.I,
)

# Counts get written as words at least as often as digits, and the first version
# of this tool matched only digits — so "three root lengths" and "two root
# lengths" landed in different groups instead of colliding. That is precisely the
# surface-form dependence this tool exists to remove, committed inside the tool
# that removes it. Words are normalised to digits before grouping.
WORD_NUM = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
            "five": "5", "six": "6", "seven": "7", "eight": "8",
            "nine": "9", "ten": "10"}

# Words that turn a mention into a claim. A line with an object and none of
# these is usually a pointer, not an assertion.
CLAIM_WORDS = re.compile(
    r"\b(is|are|has|have|equals?|gives?|yields?|=|becomes?|"
    r"exponents?|multiplicit|length|rank|order|dimension|ratio|norm|value)\b",
    re.I,
)

SKIP_DIRS = {".git", "__pycache__", ".claude", "node_modules"}


def iter_files(root, exts):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if any(fn.endswith("." + e) for e in exts):
                yield os.path.join(dirpath, fn)


def signature(text, obj_re):
    """The multiset of values asserted in this sentence, minus the object itself."""
    stripped = obj_re.sub(" ", text)
    vals = []
    for v in VALUE.findall(stripped):
        v = v.strip()
        v = WORD_NUM.get(v.lower(), v)      # "three" and "3" are one claim
        if re.fullmatch(r"20\d\d", v):      # bare years are never the claim
            continue
        vals.append(v)
    return tuple(sorted(set(vals)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("object", help="regex naming the object, e.g. 'B_2|B₂'")
    ap.add_argument("--root", default=".", help="directory to scan")
    ap.add_argument("--ext", default="md", help="comma-separated extensions")
    ap.add_argument("--near", help="only lines also matching this regex")
    ap.add_argument("--min-values", type=int, default=1,
                    help="ignore sentences asserting fewer than N values")
    ap.add_argument("--all", action="store_true",
                    help="show every group, not just disagreeing ones")
    args = ap.parse_args()

    try:
        obj_re = re.compile(args.object)
        near_re = re.compile(args.near, re.I) if args.near else None
    except re.error as e:
        sys.exit(f"bad regex: {e}")

    exts = [e.strip().lstrip(".") for e in args.ext.split(",")]
    groups = defaultdict(list)
    scanned = hits = 0

    for path in iter_files(args.root, exts):
        scanned += 1
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                lines = fh.readlines()
        except OSError:
            continue
        for i, line in enumerate(lines, 1):
            if not obj_re.search(line):
                continue
            if near_re and not near_re.search(line):
                continue
            if not CLAIM_WORDS.search(line):
                continue
            sig = signature(line, obj_re)
            if len(sig) < args.min_values:
                continue
            hits += 1
            rel = os.path.relpath(path, args.root)
            groups[sig].append((rel, i, line.strip()[:150]))

    if not groups:
        print(f"no assertions about /{args.object}/ found "
              f"({scanned} files scanned) — if that surprises you, the "
              f"instrument is wrong, not the corpus")
        return

    interesting = groups if args.all else {k: v for k, v in groups.items()}
    print(f"{hits} assertion(s) about /{args.object}/ across {scanned} files, "
          f"in {len(groups)} distinct value-group(s)\n")
    if len(groups) > 1 and not args.all:
        print("MORE THAN ONE VALUE-GROUP: the corpus says different things "
              "about this object. Adjudicate; do not sweep by string.\n")

    for sig in sorted(interesting, key=lambda s: -len(groups[s])):
        label = ", ".join(sig) if sig else "(no values)"
        print(f"── values: {label}   [{len(groups[sig])} site(s)]")
        for rel, ln, text in sorted(groups[sig])[:8]:
            print(f"   {rel}:{ln}")
            print(f"      {text}")
        if len(groups[sig]) > 8:
            print(f"   ... {len(groups[sig]) - 8} more")
        print()


if __name__ == "__main__":
    main()
