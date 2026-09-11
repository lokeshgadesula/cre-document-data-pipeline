from sqlalchemy import Numeric, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase): pass

class TenantLeaseRow(Base):
    __tablename__="tenant_leases"
    id: Mapped[int]=mapped_column(primary_key=True)
    property_id: Mapped[str]=mapped_column(String(64), index=True)
    unit_id: Mapped[str]=mapped_column(String(64))
    tenant_name: Mapped[str]=mapped_column(String(255))
    square_feet: Mapped[float]=mapped_column(Numeric(14,2))
    base_rent: Mapped[float]=mapped_column(Numeric(14,2))
