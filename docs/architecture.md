# Architecture

The system separates source-specific extraction from validation and persistence. Excel inputs are normalized before DataFrame construction. OCR/PDF adapters retain page/geometry metadata so page-boundary continuations can be reconstructed. Provider-specific LLM extraction sits behind a structured extractor boundary. Pydantic validates records, then aggregate reconciliation blocks persistence on mismatches. Public-record enrichment uses bounded exponential backoff.

```mermaid
flowchart LR
  A[PDF / Excel] --> B[Source adapters]
  B --> C[Normalize / reconstruct]
  C --> D[Structured extraction boundary]
  D --> E[Pydantic validation]
  E --> F[Reconciliation]
  F -->|pass| G[(PostgreSQL)]
  F -->|fail| H[Exception JSONL]
  I[Public records] --> J[Rate-limit aware scraper]
  J --> G
```
