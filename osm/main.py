import numpy as np
import mapbox_vector_tile
import matplotlib.pyplot as plt

# 50201

with open("1303.pbf", "rb") as file:
    data = file.read()
    a = mapbox_vector_tile.decode(data)
    print(a.keys())
    # print(len(a['Кадастровые кварталы/label']['features']), len(a['Кадастровые кварталы']['features']))
    # for index, label in enumerate(a['Кадастровые кварталы/label']['features']):
    #     print(index, label)
    # print(a['Кадастровые кварталы/label']['features'][0])
    coordinates = a['Кадастровые кварталы']['features'][0]['geometry']['coordinates']
    fig, ax = plt.subplots()
    for coordinates in a['Кадастровые кварталы']['features']:
        coordinates = coordinates['geometry']['coordinates']
        if len(coordinates) != 1:
            print("!=1")
            continue
            # raise NotImplementedError()
        arr = np.array(coordinates[0])
        # print(arr.max(axis=0))
        # print(arr[:, 0] / arr.max(axis=0))
        max_val = max(arr.max(axis=0))
        # normalized = arr @ (1/max_val * np.identity(2))
        normalized = arr
        ax.plot(*normalized.T)

plt.show()
