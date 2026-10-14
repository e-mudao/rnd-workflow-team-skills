REPORTS = [{"id":1,"status":"open"},{"id":2,"status":"closed"},{"id":3,"status":"open"}]

def list_reports(status=None, page=1, size=2):
    rows = [r for r in REPORTS if status is None or r["status"] == status]
    return rows[(page-1)*size:page*size]
