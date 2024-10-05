import asyncio

from pyproj import Transformer

from rosreestr import search_address

async def main():
    transformer = Transformer.from_crs("EPSG:3857", "EPSG:4326") 

    a = await search_address("Пиголи")
    print(a)
    xmin = a["candidates"][0]["extent"]["xmin"]
    ymin = a["candidates"][0]["extent"]["ymin"]
    xmax = a["candidates"][0]["extent"]["xmax"]
    ymax = a["candidates"][0]["extent"]["ymax"]
    transformed = transformer.transform_bounds(xmin, ymin, xmax, ymax)
    print(transformed)
    print(transformer.transform(5474114.218345504, 7472483.884825574))

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())