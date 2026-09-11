# Failure analysis

## Merged Excel headers
`openpyxl` exposes the anchor value for a merged range while other merged cells do not carry independent values. The pipeline expands the range first, then flattens hierarchical headers. This avoids overstating the behavior as “Pandas shifts columns”; misalignment is a consequence of naive header transformation, not Pandas itself.

## Page-split OCR rows
The reconstruction function only treats a keyless row as a continuation when the page changes. It fills missing fields on the preceding record and never overwrites already extracted values. A production OCR adapter would additionally use bounding boxes/column overlap and confidence thresholds.

## Reconciliation
Pydantic catches record-level contract violations. Aggregate checks catch plausible-but-wrong extraction by comparing square footage and gross rent with stated document totals. Any mismatch is quarantined with exact expected/actual/difference values.
