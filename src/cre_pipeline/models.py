from decimal import Decimal
from pydantic import BaseModel, Field, model_validator

class TenantLease(BaseModel):
    property_id: str
    unit_id: str
    tenant_name: str
    square_feet: Decimal = Field(gt=0)
    base_rent: Decimal = Field(ge=0)
    reimbursements: Decimal = Field(default=Decimal("0"), ge=0)
    lease_start: str
    lease_end: str

    @model_validator(mode="after")
    def dates_are_ordered(self):
        if self.lease_end < self.lease_start:
            raise ValueError("lease_end must not precede lease_start")
        return self

class DocumentTotals(BaseModel):
    square_feet: Decimal
    gross_rent: Decimal

class ParcelRecord(BaseModel):
    parcel_id: str
    assessed_value: Decimal
    zoning: str
    tax_amount: Decimal
