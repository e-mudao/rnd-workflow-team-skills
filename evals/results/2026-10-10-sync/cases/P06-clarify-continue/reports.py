import csv

REPORTS = [{"id":1,"status":"open"},{"id":2,"status":"closed"},{"id":3,"status":"open"}]

def list_reports(status=None, page=1, size=2):
    rows = [r for r in REPORTS if status is None or r["status"] == status]
    return rows[(page-1)*size:page*size]


def export_reports(path, status=None):
    """Write every matching report to a UTF-8 CSV file at path."""
    rows = (r for r in REPORTS if status is None or r["status"] == status)
    with open(path, "w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["id", "status"])
        writer.writeheader()
        writer.writerows(rows)
