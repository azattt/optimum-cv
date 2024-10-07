import logging

from curl_cffi import requests

logger = logging.getLogger("rosreestr")


async def search_address(text: str, tolerancy: int = 32768) -> dict:
    async with requests.AsyncSession() as s:
        params = {"SingleLine": text, "f": "json", "tolerancy": tolerancy}
        r = await s.get(
            "https://pkk.rosreestr.ru/arcgis/rest/services/Address/pkk_locator_street/GeocodeServer/findAddressCandidates",
            params=params,
            impersonate="chrome110",
            verify="russian_trusted_root_ca.cer",  # type: ignore[arg-type]
        )
        data: dict = r.json()
        return data


async def extract_cadastre_objects(
    bbox: tuple[float, float, float, float],
    dpi: int = 96,
    format: str = "PNG32",
    size: tuple[int, int] = (1024, 1024),
):
    """Экспорт изображения границ кадастровых участков
    Считаю, что лучше не менять другие параметры запроса.
    Args:
        bbox (tuple[float, float, float, float]): Границы изображения в формате ESPG:3857 (1021000)
            Похоже что координаты перепутаны таким образом, что прямоугольник имеет вид: (ymin, xmin, ymax, xmax)
        dpi (int): DPI. По умолчанию 96
        format (str): Формат выходного изображения. По умолчанию PNG32. Ограниченный список можно получить по адресу
            https://pkk.rosreestr.ru/arcgis/rest/services/PKK6/CadastreObjects/MapServer/export
            Тем не менее, не все доступные форматы разрешены для экспорта. Например, так желаемый и удобный SVG запрещен (не просто так наверное).
        size (tuple[int, int]): Ширина и высота выходного изображения в пикселях. По умолчанию 1024x1024.
    """
    # Эталонный запрос с pkk.rosreestr.ru
    # https://pkk.rosreestr.ru/arcgis/rest/services/PKK6/CadastreObjects/MapServer/export?layers=show%3A27%2C24%2C23%2C22&dpi=96&format=PNG32&bbox=5474114.218345504%2C7472483.884825574%2C5476560.203250695%2C7474929.869730763&bboxSR=102100&imageSR=102100&size=1024%2C1024&transparent=true&f=image&_ts=false
    async with requests.AsyncSession() as s:
        r = await s.get(
            "https://pkk.rosreestr.ru/arcgis/rest/services/PKK6/CadastreObjects/MapServer/export",
            params={
                "layers": "show:27,24,23,22",
                "dpi": dpi,
                "format": "PNG32",
                "bbox": f"{bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]}",
                "bboxSR": "102100",
                "imageSR": "102100",
                "size": f"{size[0]},{size[1]}",
                "transparent": "true",
                "f": "image",
                "_ts": "false",
            },
            impersonate="chrome110",
            verify="russian_trusted_root_ca.cer",  # type: ignore[arg-type]
        )
        return r.content
