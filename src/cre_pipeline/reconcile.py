from decimal import Decimal
from .models import DocumentTotals, TenantLease

def reconcile(records: list[TenantLease], totals: DocumentTotals) -> list[dict]:
    actual_sf=sum((r.square_feet for r in records), Decimal("0"))
    actual_rent=sum((r.base_rent+r.reimbursements for r in records), Decimal("0"))
    checks=[]
    for metric, actual, expected in [("square_feet",actual_sf,totals.square_feet),("gross_rent",actual_rent,totals.gross_rent)]:
        if actual != expected:
            checks.append({"metric":metric,"expected":str(expected),"actual":str(actual),"difference":str(actual-expected)})
    return checks
