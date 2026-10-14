#!/usr/bin/env python3
"""Read-only checks for this standalone skill collection; Python standard library only."""
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"rnd-team-" + name for name in (
    "lead", "discover", "spec", "plan", "build", "review", "verify",
    "release", "architecture", "design", "security")}


# Fixed release inventory, independent of the source records being checked.
# Update deliberately when bundled upstream sources are added or removed.
EXPECTED_SOURCES = {
    'rnd-team-architecture': [('upstream/agent-skills-documentation-and-adrs.md', 'upstream/agent-skills-LICENSE.txt')],
    'rnd-team-build': [('upstream/superpowers-executing-plans.md', 'upstream/superpowers-LICENSE.txt'), ('upstream/superpowers-test-driven-development.md', 'upstream/superpowers-LICENSE.txt'), ('upstream/superpowers-systematic-debugging.md', 'upstream/superpowers-LICENSE.txt')],
    'rnd-team-design': [('upstream/HumanLayer-design-control-loop.md', 'upstream/HumanLayer-LICENSE.txt')],
    'rnd-team-discover': [('upstream/pm-skills-identify-assumptions-new.md', 'upstream/pm-skills-LICENSE.txt'), ('upstream/pm-skills-summarize-interview.md', 'upstream/pm-skills-LICENSE.txt')],
    'rnd-team-lead': [('upstream/gsd-resume-method.md', 'upstream/gsd-LICENSE.txt')],
    'rnd-team-plan': [('upstream/superpowers-writing-plans.md', 'upstream/superpowers-LICENSE.txt')],
    'rnd-team-release': [('upstream/agent-skills-ci-cd-and-automation.md', 'upstream/agent-skills-LICENSE.txt'), ('upstream/agent-skills-shipping-and-launch.md', 'upstream/agent-skills-LICENSE.txt')],
    'rnd-team-review': [('upstream/superpowers-code-reviewer.md', 'upstream/superpowers-LICENSE.txt'), ('upstream/agent-skills-code-review-and-quality.md', 'upstream/agent-skills-LICENSE.txt')],
    'rnd-team-security': [('upstream/security-audit-skill-security-audit.md', 'upstream/security-audit-skill-LICENSE.txt')],
    'rnd-team-spec': [('upstream/github-spec-kit-specify.md', 'upstream/github-spec-kit-LICENSE.txt')],
    'rnd-team-verify': [('upstream/superpowers-verification-before-completion.md', 'upstream/superpowers-LICENSE.txt')]
}


def check(root):
    errors = []
    counts = {"skills": 0, "local_links": 0, "source_digests": 0}
    skills = sorted((root / "skills").glob("*/SKILL.md"))
    if {p.parent.name for p in skills} != EXPECTED:
        errors.append("Skill directory set differs from the expected 11 skills")
    workflows = []
    for skill in skills:
        counts["skills"] += 1
        body = skill.read_text()
        front = re.match(r"\A---\n(.*?)\n---\n", body, re.S)
        if not front or not re.search(r"^name: " + re.escape(skill.parent.name) + r"$", front[1], re.M) or not re.search(r"^description: .+", front[1], re.M):
            errors.append(f"Invalid name/description: {skill.relative_to(root)}")
        for relative in ("LICENSE", "THIRD_PARTY_NOTICES.md", "references/workflow.md", "references/methods.md", "references/sources.json"):
            if not (skill.parent / relative).is_file():
                errors.append(f"Missing {skill.parent.name}/{relative}")
        workflow = skill.parent / "references/workflow.md"
        if workflow.exists():
            workflows.append(workflow.read_bytes())
        source_file = skill.parent / "references/sources.json"
        try:
            sources = json.loads(source_file.read_text())["sources"]
            if not isinstance(sources, list):
                raise ValueError("sources must be a list")
            identities = [(source["excerpt_ref"]["path"], source["license_ref"]["path"])
                          for source in sources]
            expected = EXPECTED_SOURCES.get(skill.parent.name, [])
            if sorted(identities) != sorted(expected):
                errors.append(f"Source inventory mismatch: {source_file.relative_to(root)}")
            for source in sources:
                for key in ("excerpt_ref", "license_ref"):
                    ref = source[key]
                    path = source_file.parent / ref["path"]
                    counts["source_digests"] += 1
                    actual = "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()
                    if actual != ref["digest"]:
                        errors.append(f"Digest mismatch: {path.relative_to(root)}")
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f"Invalid source record {source_file.relative_to(root)}: {exc}")
    if len(set(workflows)) != 1:
        errors.append("Shared workflow copies differ or are absent")
    for path in sorted(root.rglob("*.md")):
        if "upstream" in path.relative_to(root).parts:
            continue  # Retained upstream documents may refer to their original project.
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            url = urlsplit(target.strip("<>"))
            if url.scheme or not url.path:
                continue
            counts["local_links"] += 1
            resolved = (path.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(f"Missing or external local link: {path.relative_to(root)} -> {target}")
    return {"scope": "Current package structure, local link targets (not anchors), shared workflow equality and bundled source digests; not runtime or historical validation", "counts": counts, "passed": not errors, "errors": errors}


if __name__ == "__main__":
    result = check(ROOT)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["passed"] else 1)
