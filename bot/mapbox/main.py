import asyncio
import glob
import json
import math
import os

import numpy as np
import mapbox_vector_tile
import matplotlib.pyplot as plt

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
fig, ax = plt.subplots()
# fig1, ax1 = plt.subplots()
for filename in glob.glob("tiles/11_638_1301.pbf"):
    with open(filename, "rb") as file:
        data = file.read()
        a = mapbox_vector_tile.decode(data)

        # print(a.keys())
        # print(len(a['Кадастровые кварталы/label']['features']), len(a['Кадастровые кварталы']['features']))
        # for index, label in enumerate(a['Кадастровые кварталы/label']['features']):
        #     print(index, label)
        # print(a['Кадастровые кварталы/label']['features'][0])
        coordinates = a['Кадастровые кварталы']['features'][0]['geometry']['coordinates']
        for coordinates in a['Кадастровые кварталы']['features']:
            coordinates = coordinates['geometry']['coordinates']
            if len(coordinates) != 1:
                # print(1)
                # continue
                # Это те кадастровые кварталы, которые не полностью вошли в загруженный tile
                for coordinate in coordinates:
                    # Проходимся по кускам этого не вошедшего квартала
                    if len(coordinate) != 1:
                        raise NotImplementedError()
                    arr = np.array(coordinate[0])
                    ax.plot(*arr.T, 'r')
            else:
                arr = np.array(coordinates[0])
                # ax.plot(*arr.T, 'g')

plt.show()
