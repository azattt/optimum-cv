import asyncio
import glob
import json
import math
import os

import numpy as np
import mapbox_vector_tile
from PIL import Image, ImageDraw, ImageFont

from curl_cffi import requests

# XMin: -2.00375070672E7
# YMin: -2.0037508342787E7
# XMax: 2.00375070672E7
# YMax: 2.0037508342787E7
# Spatial Reference: 102100  (3857)

# 'extent': {'xmin': 49.17124, 'ymin': 55.56135, 'xmax': 49.18403, 'ymax': 55.56947}
# (5473717.398473845, 7471583.8593900185, 5475141.174761091, 7473182.391965037)

# Взято из: https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Lon..2Flat._to_tile_numbers_2
def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 1 << zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return xtile, ytile

async def load_locality(xmin, ymin, xmax, ymax, zoom=11):
    tile_coords = (deg2num(ymin, xmin, zoom), deg2num(ymax, xmax, zoom))
    for tile_x in range(tile_coords[0][0], tile_coords[1][0]+1):
        for tile_y in range(tile_coords[1][1], tile_coords[0][1]+1):
            async with requests.AsyncSession() as session:
                r = await session.get(f"https://pkk.rosreestr.ru/arcgis/rest/services/Hosted/caddivsion/VectorTileServer/tile/{zoom}/{tile_y}/{tile_x}.pbf", impersonate="chrome110",
            verify="../russian_trusted_root_ca.cer")  # type: ignore[arg-type])
                with open(f"tiles/{zoom}_{tile_y}_{tile_x}.pbf", "wb") as file:
                    file.write(r.content)

# asyncio.run(load_locality(*{
#   "xmin": 48.83084,
#   "ymin": 55.66961,
#   "xmax": 49.28241,
#   "ymax": 55.91818
# }.values()))

# with open("tilemap", encoding="utf-8") as file:
#     data = json.loads(file.read())
#     print(data['index'][0])


# 50201

# fig1, ax1 = plt.subplots()
x = 0
images = []
for filename in glob.glob("tiles/11_638_*.pbf"):
    with open(filename, "rb") as file:
        data = file.read()
        a = mapbox_vector_tile.decode(data)
        # print(a.keys())
        # print(len(a['Кадастровые кварталы/label']['features']), len(a['Кадастровые кварталы']['features']))
        # for index, label in enumerate(a['Кадастровые кварталы/label']['features']):
        #     print(index, label)
        # print(a['Кадастровые кварталы/label']['features'][0])
        print(a.keys())
        extent: int = a['Кадастровые кварталы']['extent']
        img = Image.new('RGB', (1024, 1024), 'white')
        font = ImageFont.truetype("arial.ttf", 20)
        draw = ImageDraw.Draw(img, 'RGB')
        ratio = 1024 / extent
        for feature in a['Кадастровые кварталы']['features']:
            geometry = feature['geometry']
            if geometry['type'] == 'Polygon':
                for coordinates in geometry['coordinates']:
                    # print(list(map(lambda x: (x[0], x[1]), coordinates)))
                    arr = np.array(np.array(coordinates, dtype=int) * ratio, dtype=int)
                    print(arr.flatten().tolist())
                    draw.polygon(xy=arr.flatten().tolist(), fill=(0, 0, 0), outline="green", width=2)
            # break

        if 'Кадастровые кварталы/label' in a:
            for feature in a['Кадастровые кварталы/label']['features']:
                geometry = feature['geometry']
                if geometry['type'] == 'Point':
                    coordinates = geometry['coordinates']
                    if feature['properties']['_label_class'] == 3:
                        draw.text(np.array(coordinates) * ratio, feature['properties']['_name'], fill=(255, 0, 0), font=font)
     
        img.save(f"{filename}.png", "PNG")
        images.append(img)
        x += 1

new_image = Image.new("RGB", (4096, 1024))
for i, image in enumerate(images):
    new_image.paste(image, (i*1024, 0))
new_image.save("test1.png")
