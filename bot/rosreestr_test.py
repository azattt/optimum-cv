import math
import asyncio

from pyproj import Transformer

from rosreestr import search_address, extract_cadastre_objects

# взято из https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames

def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 1 << zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return xtile, ytile

async def main():
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:3857") 

    a = await search_address("Пиголи")
    print(a["candidates"][0])
    xmin = a["candidates"][0]["extent"]["xmin"]
    ymin = a["candidates"][0]["extent"]["ymin"]
    xmax = a["candidates"][0]["extent"]["xmax"]
    ymax = a["candidates"][0]["extent"]["ymax"]
    transformed = transformer.transform_bounds(ymin, xmin, ymax, xmax)
    print(transformed)
    content = await extract_cadastre_objects(transformed)
    with open("test.png", "wb+") as file:
        file.write(content)

    


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())