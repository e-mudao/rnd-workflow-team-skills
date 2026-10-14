"""Regression tests using disposable copies of the installed skill payload."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from check_delivery import ROOT, check


class DeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="rnd-delivery-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / "skills", self.root / "skills")

    def change_sources(self, role, transform):
        path = self.root / "skills" / ("rnd-team-" + role) / "references/sources.json"
        data = json.loads(path.read_text())
        data["sources"] = transform(data["sources"])
        path.write_text(json.dumps(data))

    def assert_rejected(self):
        result = check(self.root)
        self.assertFalse(result["passed"], result)
        self.assertTrue(result["errors"], result)

    def test_standalone_payload_passes(self):
        result = check(self.root)
        self.assertTrue(result["passed"], result)
        self.assertEqual(result["counts"]["source_digests"], 32)

    def test_empty_sources_rejected(self):
        self.change_sources("lead", lambda sources: [])
        self.assert_rejected()

    def test_partial_source_deletion_rejected(self):
        self.change_sources("build", lambda sources: sources[1:])
        self.assert_rejected()

    def test_duplicate_replacing_missing_source_rejected(self):
        self.change_sources("build", lambda sources: [sources[0], sources[0], sources[2]])
        self.assert_rejected()

    def test_wrong_source_collection_type_rejected(self):
        self.change_sources("lead", lambda sources: {})
        self.assert_rejected()

    def test_reordered_sources_pass(self):
        self.change_sources("build", lambda sources: list(reversed(sources)))
        result = check(self.root)
        self.assertTrue(result["passed"], result)

    def test_changed_source_bytes_rejected(self):
        path = self.root / "skills/rnd-team-lead/references/upstream/gsd-resume-method.md"
        path.write_bytes(path.read_bytes() + b"\nchanged\n")
        self.assert_rejected()


if __name__ == "__main__":
    unittest.main()
