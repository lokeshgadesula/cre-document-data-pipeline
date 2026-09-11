"""Provider-neutral structured extraction boundary.

Production adapters can call Anthropic/OpenAI here. The portfolio demo remains
offline and deterministic so tests do not require credentials or incur cost.
"""
from typing import Protocol
from .models import TenantLease

class StructuredExtractor(Protocol):
    def extract(self, text: str) -> list[TenantLease]: ...

class FixtureExtractor:
    def __init__(self, records: list[dict]): self.records=records
    def extract(self, text: str) -> list[TenantLease]:
        return [TenantLease.model_validate(x) for x in self.records]
