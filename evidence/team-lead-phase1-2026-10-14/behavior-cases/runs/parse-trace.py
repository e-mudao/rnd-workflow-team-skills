#! /usr/bin/env python3
"""Extract and verify a subagent session trace from the DSH session store.

Trace: ~/.dsh/sessions/<workspace>/<agent-id>/session.v4.jsonl.zstd
Usage: zstd -dc <trace> > t.jsonl && python3 parse-trace.py t.jsonl "label"

Every file access is reported as a triple (full path, content digest, read mode)
so same-named copies in different directories, and body-loads versus byte reads,
can be told apart.

Read modes:
  body     read tool        -> file BODY loaded into model context
  bytes    wc/shasum/stat   -> BYTES read for metadata/digest checks, no body
  display  cat/head/sed/od  -> bytes printed to terminal, no read-tool load
"""
import json
import sys
import collections
import pathlib
import hashlib

KW_BYTES = ("wc", "shasum", "stat", "sha256", "find", "ls", "grep", "glob")
KW_DISPLAY = ("cat ", "head ", "sed ", "od ", "diff ", "tar ")

def dig(p, cache):
    if p in cache:
        return cache[p]
    try:
        q = pathlib.Path(p)
        cache[p] = hashlib.sha256(q.read_bytes()).hexdigest()[:16] if q.is_file() else "n/a"
    except Exception:
        cache[p] = "unreadable"
    return cache[p]

def load(trace):
    ev = [json.loads(l) for l in open(trace) if l.strip()]
    calls, results = {}, {}
    for e in ev:
        d = e.get("data", {})
        if e.get("type") == "tool/call":
            a = d.get("arguments")
            if isinstance(a, str):
                try: a = json.loads(a)
                except Exception: a = {}
            calls[d.get("callId")] = {"seq": e.get("seq"), "turn": d.get("turn"),
                                      "tool": d.get("name"), "args": a}
        elif e.get("type") == "tool/result":
            m = d.get("message", {})
            txt = "".join(c.get("text", "") for c in m.get("content", []) if isinstance(c, dict))
            cid = (m.get("source") or {}).get("callId") or m.get("toolCallId")
            results[cid] = {"seq": e.get("seq"), "turn": d.get("turn"), "text": txt}
    return ev, calls, results

def _interesting(p):
    return (p.endswith(".md") or p.endswith(".py") or p.endswith(".txt")
            or p.endswith(".cfg") or p.endswith(".json") or "skils" in p or "skills" in p)

def accesses(calls):
    """Return [(seq, turn, mode, path, note)] for every file access we can see."""
    out = []
    for cid, c in sorted(calls.items(), key=lambda kv: kv[1]["seq"]):
        tool, a = c["tool"], c["args"]
        if tool == "read":
            out.append((c["seq"], c["turn"], "body", a.get("file_path", "?"), "read"))
        elif tool in ("edit", "write"):
            out.append((c["seq"], c["turn"], "body", a.get("file_path", "?"), tool + ":rewrite"))
        elif tool in ("glob", "grep"):
            out.append((c["seq"], c["turn"], "bytes", a.get("path") or a.get("pattern") or "?",
                        tool + ":scope"))
        elif tool == "bash":
            cmd = str(a.get("command", ""))
            mode = "bytes"
            if any(k in cmd for k in KW_DISPLAY):
                mode = "display"
            if not any(k in cmd for k in KW_BYTES) and mode == "bytes":
                mode = "display"
            toks = [t.strip("'\"<>()|;") for t in cmd.split()]
            paths = [t for t in toks if t.startswith("/") and _interesting(t)]
            for p in paths[:12] or ["(no absolute path in command)"]:
                out.append((c["seq"], c["turn"], mode, p, "bash"))
    return out

def report(trace, label):
    ev, calls, results = load(trace)
    print("\n" + "=" * 78 + f"\n{label}\n" + "=" * 78)
    print(f"tool calls={len(calls)}  results={len(results)}  paired={len(set(calls) & set(results))}")
    print(f"calls per turn={dict(sorted(collections.Counter(c['turn'] for c in calls.values()).items()))}")

    cache = {}
    rows = accesses(calls)
    print("\n--- accesses: (mode, path, current digest, note) ---")
    for seq, turn, mode, p, note in rows:
        print(f"  turn{turn} seq={seq:4} {mode:7} {dig(p, cache)}  {p}  {note}")

    print("\n--- BODY loads grouped by path ---")
    byc = collections.Counter(p for _, _, m, p, _ in rows if m == "body")
    for p, n in sorted(byc.items()):
        print(f"  {n}x  {p}   sha256={dig(p, cache)}")
    wf = [p for p in byc if p.endswith("references/workflow.md")]
    print(f"  workflow.md BODY loads: total={sum(byc[p] for p in wf)}  distinct copies={len(wf)}")

    ab = "#".join(json.dumps(c["args"], ensure_ascii=False) for c in calls.values())
    rb = "#".join(r["text"] for r in results.values())
    print("\n--- leak scan: occurrences in call args / results ---")
    for p in ["evidence", "case-plan", "ANSWER_KEY", "setup-fixtures", "T1.spec-after"]:
        print(f"  {p:16s} args={ab.count(p):3d}  results={rb.count(p):3d}")
    return calls, results

if __name__ == "__main__":
    report(sys.argv[1], sys.argv[2])
