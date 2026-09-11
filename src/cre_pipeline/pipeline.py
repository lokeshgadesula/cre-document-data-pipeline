from pathlib import Path
from .exception_queue import quarantine
from .models import DocumentTotals, TenantLease
from .reconcile import reconcile

def validate_batch(source: str, raw_records: list[dict], totals: dict, exception_path="exceptions/failed.jsonl") -> list[TenantLease]:
    records=[TenantLease.model_validate(x) for x in raw_records]
    failures=reconcile(records, DocumentTotals.model_validate(totals))
    if failures:
        quarantine(source, failures, Path(exception_path))
        raise ValueError(f"reconciliation failed: {failures}")
    return records
