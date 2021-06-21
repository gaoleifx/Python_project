#元组
import os

t = (10, [20, 30], 40)
print(t)
print(type(t))
print(t[0], type(t[0]), id(t[0]))
print(t[1], type(t[1]), id(t[1]))
print(t[2], type(t[2]), id(t[2]))

t[1].append(100)
print(t)
print(t[1][2])

a, b, *rest = range(5)
print(type(rest))

t = divmod(20, 8)
print(t)

_, filename = os.path.split('D:\WYGame\Assets\HoudiniEngineAssetCache\Geo\Terrain_geo_new\Terrain_geo_4_6.bgeo.sc')
path, _ = os.path.split('D:\WYGame\Assets\HoudiniEngineAssetCache\Geo\Terrain_geo_new\Terrain_geo_4_6.bgeo.sc')
print(path)