import FeatureCollection_pb2

a = FeatureCollection_pb2.FeatureCollectionPBuffer()

with open("1303.pbf", "rb") as file:
    a.ParseFromString(file.read())

print(a)