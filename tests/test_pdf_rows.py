from cre_pipeline.pdf_rows import OCRRow, stitch_page_split_rows

def test_page_split_row_stitches_only_on_new_page():
    rows=[OCRRow(1,700,{"unit_id":"101","tenant_name":"Acme","base_rent":None}), OCRRow(2,40,{"unit_id":None,"base_rent":"2500"})]
    out=stitch_page_split_rows(rows)
    assert len(out)==1 and out[0]["base_rent"]=="2500"
