from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class OCRRow:
    page: int
    y: float
    values: dict[str, Any]

def stitch_page_split_rows(rows: list[OCRRow], key="unit_id") -> list[dict]:
    """Merge a leading continuation row on a new page into the prior record."""
    output=[]
    prior_page=None
    for row in rows:
        values=dict(row.values)
        is_new_page = prior_page is not None and row.page != prior_page
        if is_new_page and not values.get(key) and output:
            # Only fill missing/blank fields; never overwrite source values.
            for k,v in values.items():
                if v not in (None, "") and output[-1].get(k) in (None, ""):
                    output[-1][k]=v
        else:
            output.append(values)
        prior_page=row.page
    return output
