#!/usr/bin/env python3
"""Regenerate raw/attempts.tsv: one line per harness invocation in Experiment 2,
including failed, truncated, and aborted draws. Session-1 draws are reconstructed
from the archived output files' modification times and contents; session-2 draws
come from the collector's run.log. Run from the exp2 directory."""
import datetime
import glob
import os
import re
import sys

OLD = "/private/tmp/claude-501/-Users-akclark/a8c643ef-cf7c-426f-81f3-9e7bf7a7b3ca/scratchpad/exp2"
SP = "/private/tmp/claude-501/-Users-akclark/16941fa9-ccc8-4d58-b223-e359f041e6ac/scratchpad/exp2"
S1_ARCHIVE = "raw/session1-attempts.tsv"  # frozen copy of the session-1 rows, in case the scratchpad is gone


def provider(t):
    m = re.search(r"\)\s+via (\S+)\s+[\d.]+s", t)
    return m.group(1) if m else "-"


def outcome(path):
    t = open(path, errors="replace").read()
    if not t.strip():
        return "ABORTED", "operator stop at pause (0 bytes)"
    m = re.search(r"\)\s+(?:via \S+\s+)?([\d.]+)s", t)
    secs = m.group(1) if m else ""
    if "0/1 lanes answered" in t:
        return "FAIL", f"{secs}s; no answer, token budget exhausted on reasoning (2 attempts)"
    if "TRUNCATED" in t:
        return "OK-TRUNCATED", f"{secs}s; hit max_tokens, scored on delivered text"
    if "1/1 lanes answered" in t:
        return "OK", f"{secs}s"
    return "UNKNOWN", ""


rows = []
if os.path.isdir(OLD):
    for f in sorted(glob.glob(f"{OLD}/r*.out"), key=os.path.getmtime):
        r, lane = re.match(r".*/r(\d+)-(.+)\.out", f).groups()
        o, note = outcome(f)
        pv = provider(open(f, errors="replace").read())
        ts = datetime.datetime.fromtimestamp(os.path.getmtime(f)).strftime("%H:%M:%S")
        rows.append((ts, "s1", r, lane, o, pv, note))
    with open(S1_ARCHIVE, "w") as w:
        for row in rows:
            w.write("\t".join(row) + "\n")
elif os.path.exists(S1_ARCHIVE):
    rows = [tuple(l.rstrip("\n").split("\t")) for l in open(S1_ARCHIVE)]
else:
    sys.exit("no session-1 source available")

for line in open(f"{SP}/run.log"):
    m = re.match(r"(\d\d:\d\d:\d\d) pass(\d) r(\d+) (\S+) (OK|FAIL)", line.strip())
    if not m:
        continue
    ts, p, r, lane, res = m.groups()
    f = f"{SP}/r{r}-{lane}.out"
    side = f"{SP}/r{r}-{lane}.fail{p}.txt"
    src = side if res == "FAIL" and os.path.exists(side) else f
    o, note = outcome(src)
    pv = provider(open(src, errors="replace").read())
    if res == "FAIL" and o != "FAIL":
        o, note = "FAIL", "(output later overwritten by retry)"
    rows.append((ts, f"s2p{p}", r, lane, o, pv, note))

with open("raw/attempts.tsv", "w") as w:
    w.write("# Every draw attempted in Experiment 2, in wall-clock order (2026-09-01 CDT). One line per harness invocation.\n")
    w.write("# session: s1 = first session (Claude Opus 5 convening, paused 13:48); s2pN = resumed session (Claude Fable 5.1 convening), collector pass N.\n")
    w.write("# outcome: OK = answer delivered; OK-TRUNCATED = answer delivered but cut at max_tokens (scored on delivered text);\n")
    w.write("#          FAIL = no answer after the harness's 2 attempts (re-drawn later; failed output kept as raw/rN-LANE.failK.txt); ABORTED = killed by operator at the pause, re-drawn.\n")
    w.write("# served_by: the upstream provider OpenRouter routed the call to, as reported by the harness header; '-' when no completed response was received.\n")
    w.write("time\tsession\tround\tlane\toutcome\tserved_by\tnote\n")
    for row in rows:
        w.write("\t".join(row) + "\n")
print(f"attempts.tsv: {len(rows)} draws")
