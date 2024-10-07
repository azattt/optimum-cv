import FeatureCollection_pb2
from google.protobuf.json_format import MessageToJson

# pylint: disable-next=no-member
a = FeatureCollection_pb2.FeatureCollectionPBuffer()

with open("1303.pbf", "rb") as file:
    b = a.ParseFromString(file.read())
    a.version

print(dir(a))