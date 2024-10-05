from json import JSONDecodeError
import logging
import time

from curl_cffi import requests

logger = logging.getLogger("rosreestr")


async def search_address(text: str, tolerancy: int = 32768) -> list[dict] | None:
    async with requests.AsyncSession() as s:
        r = await s.get(
            "https://pkk.rosreestr.ru/arcgis/rest/services/Address/pkk_locator_street/GeocodeServer/findAddressCandidates",
            params={"SingleLine": text, "f": "json", "tolerancy": tolerancy},
            impersonate="chrome110",
            verify="russian_trusted_root_ca.cer",  # type: ignore[arg-type]
        )
        data: dict = r.json()
        return data

# async def extract_cadastre_objects():
#     async with requests.AsyncSession() as s:
#         r = await s.get("https://pkk.rosreestr.ru/arcgis/rest/services/PKK6/CadastreObjects/MapServer/export",
#                         params={"layers", "show:27,24,23,22",
#                                 "dpi": "96"
#                                 "format": "PNG32",
#                                 "bbox": "5474114.218345504,7472483.884825574%2C5476560.203250695%2C7474929.869730763&bboxSR=102100&imageSR=102100&size=1024%2C1024&transparent=true&f=image&_ts=false
#     https://pkk.rosreestr.ru/arcgis/rest/services/PKK6/CadastreObjects/MapServer/export?layers=show%3A27%2C24%2C23%2C22&dpi=96&format=PNG32&bbox=5474114.218345504%2C7472483.884825574%2C5476560.203250695%2C7474929.869730763&bboxSR=102100&imageSR=102100&size=1024%2C1024&transparent=true&f=image&_ts=false