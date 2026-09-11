from cre_pipeline.public_records import parse_assessment_html

def test_parse_public_assessment_fixture():
    html='''<span data-field="parcel_id">P-42</span><span data-field="assessed_value">$1,200,000</span><span data-field="zoning">C-2</span><span data-field="tax_amount">$24,000</span>'''
    r=parse_assessment_html(html)
    assert r.parcel_id=="P-42" and str(r.assessed_value)=="1200000"
