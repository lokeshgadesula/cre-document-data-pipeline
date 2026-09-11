from openpyxl.worksheet.worksheet import Worksheet

def expand_merged_cells(ws: Worksheet) -> None:
    """Copy each merged-range anchor into every cell, then unmerge."""
    for merged in list(ws.merged_cells.ranges):
        value = ws.cell(merged.min_row, merged.min_col).value
        ws.unmerge_cells(str(merged))
        for row in ws.iter_rows(min_row=merged.min_row, max_row=merged.max_row, min_col=merged.min_col, max_col=merged.max_col):
            for cell in row:
                cell.value = value

def hierarchical_headers(ws: Worksheet, header_rows: int = 2) -> list[str]:
    """Flatten multi-row headers after horizontal/downward parent propagation."""
    matrix=[]
    for r in range(1, header_rows+1):
        vals=[]; last=None
        for c in range(1, ws.max_column+1):
            v=ws.cell(r,c).value
            if v not in (None, ""): last=str(v).strip()
            vals.append(last)
        matrix.append(vals)
    out=[]
    for c in range(ws.max_column):
        parts=[]
        for r in range(header_rows):
            v=matrix[r][c]
            if v and (not parts or parts[-1] != v): parts.append(v)
        out.append("__".join(parts).lower().replace(" ", "_"))
    return out
