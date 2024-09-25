from json import JSONDecodeError
import logging
import time

from curl_cffi import requests

logger = logging.getLogger("rosreestr")

async def search_address(text: str, tolerance: int = 32768) -> list[dict] | None:
    
    async with requests.AsyncSession() as s:
        r = await s.get(
            "https://pkk.rosreestr.ru/arcgis/rest/services/Address/pkk_locator_street/GeocodeServer/findAddressCandidates",
            params={"SingleLine": text, "f": "json", "tolerancy": tolerance},
            impersonate="chrome110",
            verify="russian_trusted_root_ca.cer",  # type: ignore[arg-type]
        )
        print(r.text)
        data: dict = r.json()
        return data.get("candidates", None)


async def search_locality(text: str):
    r = requests.get(
        "https://pkk.rosreestr.ru/api/typeahead/1",
        params={"text": text, "_": int(time.time() * 1000), "tolerancy": 0},
        impersonate="chrome110",
        verify="russian_trusted_root_ca.cer",  # type: ignore[arg-type]
    )
    print(r.text)

