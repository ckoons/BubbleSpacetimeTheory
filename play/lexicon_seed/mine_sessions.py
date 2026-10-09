#!/usr/bin/env python3 -I
"""Mine Claude Code session transcripts for Casey<->CI clarification / correction exchanges.

Streams each .jsonl line by line; reconstructs ordered (role, text, ts) per session;
emits candidate pairs (Pattern A: CI asks clarifying question; Pattern B: Casey corrects a reading).
"""
import glob
import json
import os
import re
import sys
from collections import Counter

SRC = "/Users/cskoons/.claude/projects/-Users-cskoons-projects-github/*.jsonl"
OUT = "/private/tmp/claude-501/-Users-cskoons-projects-github/f954bc8c-c958-4398-8763-6dc82a8e7d0e/scratchpad/mine_sessions_raw.jsonl"

# Pattern A: assistant clarifying phrases
PAT_A = re.compile(
    r"(which (do|did) you mean|do you mean|what do you mean|I read (this|that|you|it|your [a-z]+) as"
    r"|pin (one thing|what you mean|which|the (reading|sense|meaning))|two readings|three readings|is that what you mean"
    r"|did you mean|before I can judge|I need you to pin|which side is which|one thing to pin"
    r"|two (possible|plausible) readings|I take (this|that|you|your [a-z]+) to mean|I('m| am) reading (this|that|you|it) as"
    r"|I('m| am) not sure (what|which) you mean|can you say which|which one do you mean|which [a-z]+ do you mean"
    r"|if you mean|if by .{1,40} you mean|I('ll| will) take .{1,40} to mean|clarif(y|ication)|which reading"
    r"|are you (asking|saying|pointing)"
    r"|when you (say|said|wrote|write) [“\"'‘]|by [“\"'‘][^”\"'’]{1,40}[”\"'’],? (do you|you) mean|[“\"'‘][^”\"'’]{1,40}[”\"'’] (here )?(means|could mean|can mean|has two|carries two)"
    r"|[Yy]our (word|phrase|term|sentence) |[Yy]our [“\"'‘][^”\"'’]{2,40}[”\"'’]"
    r"|(two|three|both) (senses|meanings|ways to read|readings of)|ambiguous|I (hear|heard) (this|that|you) as|I('ll| will) read (this|that|it|you) as"
    r"|(reading|sense) \(?[AB1]\)?.{0,60}(reading|sense) \(?[B2]\)?|which (of these|one) (is|did|do)|is (this|that|it) (the|what) (you|right)"
    r"|one (question|thing) (before|first)|need(s)? (to be )?pinned|I need (one|two|three) (thing|pin|answer)|before (I|we|anyone) (can|run|compute|write)"
    r"|not (sure|clear) (I|what|which) (follow|you|part|mean)|did I (read|get|have) (that|this|you|it) (right|wrong)|have I (got|read) (that|this|you|it) (right|wrong)"
    r"|(does|did) (that|this) (match|capture|land|read) (what|how|as) you|is that (right|the sense|the reading|what you)|correct me if"
    r"|I can't place|I cannot place|I found no [“\"'‘]?[A-Za-z]+[”\"'’]? in the corpus|Here's how I read you|here is how I read you|As I read you|that's a different (idea|claim) from|I scored the wrong claim|You meant\b|one word needs (pinning|adjusting)|the word[: ]|Your message got cut off|finish the thought)",
    re.I,
)
# Pattern B: Casey correcting a reading
PAT_B = re.compile(
    r"(\bI meant\b|I did not mean|I didn't mean|\bno,? I mean\b|please understand|what I meant|\bI mean(t)? by\b"
    r"|to be clear|not what I|you misread|you misunderstood|that's not what|that is not what|\bI was (not )?(saying|asking|talking about)\b"
    r"|you (mis)?read (me|it|that|this)|let me (rephrase|restate|be clear(er)?)|wrong (reading|interpretation)|\bI'm saying\b|\bI am saying\b"
    r"|\bI see it as\b|\bI see (the|an?|this|that) [a-z]+ as\b|\bwhat I was\b|\bI('m| am) not saying\b|\bI was not\b|\bI wasn't\b|\bnot quite\b|\bbetter than I said\b"
    r"|\bmy claim\b|carefully chosen word|\bwhen I (say|said|use|wrote|speak)\b|\bby [“\"'‘][^”\"'’]{1,40}[”\"'’] I mean|\bI (call|use the word|use the term)\b|\bI meant\b|\bmy (meaning|intent|intention)\b"
    r"|\bI did not\b|\bI don't think you\b|\bnot my (point|meaning|claim|question)\b|\bmissed (my|the) (point|meaning)\b|\bI am asking\b|\bI('m| am) asking (about|whether|if)\b|\bI('m| am) pointing\b"
    r"|^(no|nope|not exactly|not really|close|almost)\b[,. ]|\bmy point (is|was)\b|\bthe point (is|was)\b|\bI('m| am) suggesting\b|\bI think you (mis|have|are)\b|\bthat('s| is) not (it|right|what)\b|\byou (took|read|have) (it|me|this|that) (too|as)\b"
    r"|\blet me clarify\b|\bI (simply|just|only|really|actually) meant\b|\bmy (comment|point|question) on [a-z' ]+ is this\b|\bI('d| would) (suggest|argue) my\b|\bYou caught the (correct|intended)\b|\b(\d|two|one)[\)\.]? ammended\b|\bamended\b|\bclarif(y|ication)\b)",
    re.I,
)

SKIP_SUBSTR = ("system-reminder", "task-notification", "<local-command", "<command-name", "<bash-input", "<bash-stdout", "[Request interrupted")


def iter_messages(path):
    """Yield (role, text, ts, sid) for text blocks in order of file lines."""
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                d = json.loads(line)
            except Exception:
                continue
            t = d.get("type")
            if t not in ("user", "assistant"):
                continue
            if d.get("isSidechain"):
                continue  # subagent threads: not Casey
            m = d.get("message") or {}
            ct = m.get("content")
            ts = d.get("timestamp", "")
            sid = d.get("sessionId", os.path.basename(path)[:8])
            texts = []
            if isinstance(ct, str):
                texts.append(ct)
            elif isinstance(ct, list):
                for b in ct:
                    if isinstance(b, dict) and b.get("type") == "text":
                        texts.append(b.get("text") or "")
            for tx in texts:
                tx = tx.strip()
                if not tx:
                    continue
                if t == "user":
                    ok = (d.get("origin") or {}).get("kind")
                    if ok not in (None, "human"):
                        continue
                    if "<pasted_content" in tx:
                        tx = tx.split("<pasted_content", 1)[0].strip()
                        tx = re.sub(r"^(Keeper|Grace|Elie|Lyra|Cal|Cal \(Prime\)|Casey)\s*:\s*$", "", tx).strip()
                        if not tx:
                            continue
                    if tx.startswith("<") or len(tx) > 3000:
                        continue
                    if any(s in tx for s in SKIP_SUBSTR):
                        continue
                    # drop pure slash-commands and trivial tokens
                    if tx.startswith("/") and len(tx) < 60:
                        continue
                    # drop assistant-interrupt echoes
                    if tx.startswith("[Request interrupted"):
                        continue
                yield (t, tx, ts, sid)


def clip(s, n):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def main():
    files = sorted(glob.glob(SRC))
    stats = Counter()
    records = []
    global DUMP
    DUMP = []
    for path in files:
        stats["sessions"] += 1
        seq = list(iter_messages(path))
        n = len(seq)
        casey_idx = [i for i, (r, _, _, _) in enumerate(seq) if r == "user"]
        stats["casey_msgs"] += len(casey_idx)
        stats["assistant_texts"] += n - len(casey_idx)
        for k, i in enumerate(casey_idx):
            role, ctext, cts, sid = seq[i]
            # dump for reading
            nxt_a = ""
            jj = i + 1
            while jj < n and seq[jj][0] == "assistant":
                nxt_a += seq[jj][1] + " ⏎ "
                jj += 1
            DUMP.append(f"=== {cts[:16]} {sid[:8]}\nC: {clip(ctext, 1200)}\nA: {clip(nxt_a, 900)}\n")
            # next Casey message (for followup)
            nxt_c = seq[casey_idx[k + 1]][1] if k + 1 < len(casey_idx) else ""
            # Pattern A: look at next up to 2 assistant texts before the next Casey msg
            j = i + 1
            seen = 0
            while j < n and seq[j][0] == "assistant" and seen < 2:
                m = PAT_A.search(seq[j][1])
                if m:
                    # extract passage window around match
                    a = seq[j][1]
                    s = max(0, m.start() - 250)
                    e = min(len(a), m.end() + 350)
                    records.append(
                        {
                            "session": sid,
                            "timestamp": cts,
                            "pattern": "A",
                            "casey_text": clip(ctext, 600),
                            "assistant_text": clip(a[s:e], 600),
                            "match": m.group(0),
                            "casey_followup": clip(nxt_c, 400),
                        }
                    )
                    stats["hits_A"] += 1
                    break
                seen += 1
                j += 1
            # Pattern B: Casey corrects
            mb = PAT_B.search(ctext)
            if mb:
                # previous assistant text (the misreading)
                prev_a = ""
                p = i - 1
                while p >= 0:
                    if seq[p][0] == "assistant":
                        prev_a = seq[p][1]
                        break
                    p -= 1
                records.append(
                    {
                        "session": sid,
                        "timestamp": cts,
                        "pattern": "B",
                        "casey_text": clip(ctext, 600),
                        "assistant_text": clip(prev_a[-700:], 600),
                        "match": mb.group(0),
                        "casey_followup": "",
                    }
                )
                stats["hits_B"] += 1
    with open(OUT, "w", encoding="utf-8") as out:
        for r in records:
            out.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(OUT.replace("mine_sessions_raw.jsonl", "casey_all.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(DUMP))
    print(json.dumps(stats, indent=1))
    print("wrote", len(records), "records to", OUT)


if __name__ == "__main__":
    main()
