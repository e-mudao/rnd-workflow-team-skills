import csv
from pathlib import Path
import tempfile
import unittest
from reports import export_reports, list_reports

class ExportTests(unittest.TestCase):
    def export(self, status=None):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "reports.csv"
            export_reports(path, status=status)
            with path.open(encoding="utf-8", newline="") as stream:
                return list(csv.reader(stream))
    def test_all_not_paginated(self):
        self.assertEqual(self.export(), [["id", "status"], ["1", "open"], ["2", "closed"], ["3", "open"]])
    def test_filtered_not_paginated(self):
        self.assertEqual(list_reports("open", size=1), [{"id": 1, "status": "open"}])
        self.assertEqual(self.export("open"), [["id", "status"], ["1", "open"], ["3", "open"]])
    def test_empty_has_header(self):
        self.assertEqual(self.export("missing"), [["id", "status"]])
    def test_existing_pagination(self):
        self.assertEqual(list_reports(page=2), [{"id": 3, "status": "open"}])
    def test_invalid_destination_error(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(FileNotFoundError):
                export_reports(Path(directory) / "missing" / "out.csv")

if __name__ == "__main__":
    unittest.main()
