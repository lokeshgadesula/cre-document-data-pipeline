import asyncio
from decimal import Decimal
import httpx
from bs4 import BeautifulSoup
from .models import ParcelRecord

async def fetch_with_backoff(url: str, attempts: int = 3, base_delay: float = 0.25) -> str:
    async with httpx.AsyncClient(timeout=10) as client:
        for attempt in range(attempts):
            response=await client.get(url)
            if response.status_code == 429 or response.status_code >= 500:
                if attempt == attempts-1: response.raise_for_status()
                await asyncio.sleep(base_delay * (2**attempt)); continue
            response.raise_for_status(); return response.text
    raise RuntimeError("unreachable")

def parse_assessment_html(html: str) -> ParcelRecord:
    soup=BeautifulSoup(html, "html.parser")
    def text(field):
        node=soup.select_one(f'[data-field="{field}"]')
        if node is None: raise ValueError(f"missing {field}")
        return node.get_text(strip=True)
    money=lambda s: Decimal(s.replace("$","").replace(",",""))
    return ParcelRecord(parcel_id=text("parcel_id"), assessed_value=money(text("assessed_value")), zoning=text("zoning"), tax_amount=money(text("tax_amount")))
