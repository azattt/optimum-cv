import asyncio

from pyproj import Transformer

from rosreestr import search_address, extract_cadastre_objects

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