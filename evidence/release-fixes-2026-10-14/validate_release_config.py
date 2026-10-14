#!/usr/bin/env python3
"""Validate the package's release config against upstream schemas.

Read-only. Checks CITATION.cff against the Citation File Format 1.2.0 JSON
Schema, and the GitHub workflow / issue forms against SchemaStore's published
schemas. Schema paths are passed in so nothing is fetched at run time; each
schema's digest is recorded in the output for audit.

Usage:
    python3 validate_release_config.py <cff-schema.json> <workflow-schema.json> \
        <issue-forms-schema.json>
"""
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft7Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_SOURCES = {
    "cff": "https://raw.githubusercontent.com/citation-file-format/citation-file-format/1.2.0/schema.json",
    "workflow": "https://www.schemastore.org/github-workflow.json",
    "issue_forms": "https://www.schemastore.org/github-issue-forms.json",
}
TARGETS = {
    "cff": ["CITATION.cff"],
    "workflow": [".github/workflows/check.yml"],
    "issue_forms": [".github/ISSUE_TEMPLATE/bug.yml", ".github/ISSUE_TEMPLATE/feature.yml"],
}


class GitHubYaml(yaml.SafeLoader):
    """GitHub reads YAML 1.2 core: only true/false are booleans.

    PyYAML implements YAML 1.1, where `on`, `off`, `yes` and `no` are also
    booleans; under that loader a workflow's `on:` key becomes True.
    """


_BOOL_TAG = "tag:yaml.org,2002:bool"
_BOOL_RE = re.compile(r"^(?:true|True|TRUE|false|False|FALSE)$")
for _ch, _resolvers in list(GitHubYaml.yaml_implicit_resolvers.items()):
    _kept = [(t, rx) for t, rx in _resolvers if t != _BOOL_TAG]
    if _ch in ("t", "T", "f", "F"):
        _kept.append((_BOOL_TAG, _BOOL_RE))
    GitHubYaml.yaml_implicit_resolvers[_ch] = _kept


def load(path):
    return yaml.load(Path(path).read_text(), Loader=GitHubYaml)


def validate(schema, target):
    """Validate one repo-relative target. All schema $refs are internal (#/...)."""
    errors = sorted(
        Draft7Validator(schema).iter_errors(load(ROOT / target)),
        key=lambda error: list(error.path),
    )
    return {
        "target": target,
        "valid": not errors,
        "errors": [
            {"path": "/".join(map(str, error.path)) or "<root>", "message": error.message}
            for error in errors
        ],
    }


def main(argv):
    if len(argv) != 4:
        print(__doc__)
        return 2
    results = []
    for name, schema_path in zip(("cff", "workflow", "issue_forms"), argv[1:]):
        raw = Path(schema_path).read_bytes()
        schema = json.loads(raw)
        for target in TARGETS[name]:
            entry = validate(schema, target)
            entry.update({
                "schema": name,
                "schema_source": SCHEMA_SOURCES[name],
                "schema_sha256": hashlib.sha256(raw).hexdigest(),
            })
            results.append(entry)
    report = {
        "scope": (
            "Release config only: CITATION.cff vs Citation File Format 1.2.0, "
            "the GitHub workflow and issue forms vs SchemaStore schemas. "
            "Schema files are caller-supplied, not fetched; digests recorded. "
            "Not a GitHub-side rendering or Actions execution."
        ),
        "yaml_loader": "GitHub Actions semantics (YAML 1.2 core: only true/false are booleans)",
        "results": results,
        "passed": all(entry["valid"] for entry in results),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
