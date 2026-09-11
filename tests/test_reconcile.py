import pytest
from cre_pipeline.pipeline import validate_batch

RECORD={"property_id":"P1","unit_id":"101","tenant_name":"Acme","square_feet":"1000","base_rent":"2500","reimbursements":"250","lease_start":"2025-01-01","lease_end":"2027-12-31"}

def test_valid_batch_passes(tmp_path):
    out=validate_batch("fixture",[RECORD],{"square_feet":"1000","gross_rent":"2750"},tmp_path/"q.jsonl")
    assert out[0].unit_id=="101"

def test_bad_total_quarantines(tmp_path):
    q=tmp_path/"q.jsonl"
    with pytest.raises(ValueError): validate_batch("fixture",[RECORD],{"square_feet":"900","gross_rent":"2750"},q)
    assert '"difference": "100"' in q.read_text()
