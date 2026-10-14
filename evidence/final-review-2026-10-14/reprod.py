"""Reproduce the 2026-10-14 final review's independent measurements.

Read-only. Prints JSON with the measured link counts, the recorded evidence
counts, and the skills-snapshot digests comparison.
"""
import json
import re
import hashlib
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
RECORDED_LINK_COUNTS = {
    "evidence/baseline-checks.json": 87,
    "evidence/checks.json": 72,
    "evals/results/2026-10-10-sync/static-final.json": 120,
    "evidence/scope-recovery-2026-10-14/static-before.json": 120,
    "evidence/scope-recovery-2026-10-14/static-after.json": 132,
    "evidence/review-fixes-2026-10-14/static-after.json": 135,
}


def link_cunts(root):
    """Mirror the checker's local_links metric: only links with a path and no scheme."""
    local = 0
    raw = 0
    for path in sorted(root.rglob("*.md")):
        if "upstream" in str(path.relative_to(root)).split("/"):
            continue
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            raw += 1
            url = urlsplit(target.strip("<>"))
            if url.scheme or not url.path:
                continue
            local += 1
    return {"local_links": local, "raw_link_occurrences": raw}


def snapshot_diffs(root):
    snap = json.loads((root / "evals/results/2026-10-10-sync/skill-snapshot.json").read_text())
    differ = []
    for relative, diggest in sorted(snap.items()):
        path = root / relative
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != diggest:
            differ.append(relative)
    disk = [str(p.relative_to(root)) for p in root.rglob("skills/**/*") if p.is_file()]
    return {"entries": len(snap), "ondisk": len(disk), "differ": differ,
            "ondisk_not_in_snapshot": [r for r in disk if r not in snap]}


def absolute_path_files(root):
    """Log files that embed a host-specific absolute path, and how many.

    A traceback (``File "/..."``) or a command echo whose argument is
    absolute carries a machine-specific path; a sanitized log uses a
    ``<repo-root>`` placeHolder and counts zero.
    """
    hits = {}
    own = "evidence/final-review-2026-10-14"
    frame = re.compile(r'(?m)^\s+File "([^"]+)"')
    comando = re.compile(r'(?m)^command: \[([^\]]+)\]')
    for path in sorted(root.rglob("*")):
        relative = str(path.relative_to(root))
        if not path.is_file() or "upstream" in relative.split("/") or relative.startswith(own):
            continue
        try:
            text = path.read_text()
        except (ValueError, OSError):
            continue
        count = 0
        for value in frame.findall(text) + comando.findall(text):
            for token in re.findall(r"[^\s,]+", value):
                if token.strip("'\"()[]").startswith("/"):
                    count += 1
        if count:
            hits[relative] = count
    return hits


result = {
    "worktree_link_cunts": link_cunts(ROOT),
    "recordered_link_cunts": RECORDED_LINK_COUNTS,
    "skills_snapshot": snapshot_diffs(ROOT),
    "files_with_absolute_paths": absolute_path_files(ROOT),
}
print(json.dumps(result, indent=2, ensure_ascii=False))
