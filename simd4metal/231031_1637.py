import ctypes
import numpy as np

Float = np.dtype(np.float32, align=True)

UInt16 = np.dtype(np.uint16, align=True)

Vertex = np.dtype({
  'names': ['x', 'y', 'z',],
  'formats': [Float, Float, Float,],
  'offsets': [o * Float.itemsize for o in range(3)],
  'itemsize': 3 * Float.itemsize,
}, align=True)  # yapf: disable

PackedFloat3 = Vertex

simd_float3 = np.dtype({
  'names': ['x', 'y', 'z',],
  'formats': [Float, Float, Float,],
  'offsets': [o * Float.itemsize for o in range(3)],
  'itemsize': 16,
}, align=True)  # yapf: disable


scale = 0.8

vertices_np = np.array(
  [
    np.array((-1,  1,  0,), dtype=PackedFloat3),
    np.array(( 1,  1,  0,), dtype=PackedFloat3),
    np.array((-1, -1,  0,), dtype=PackedFloat3),
    np.array(( 1, -1,  0,), dtype=PackedFloat3),
  ]
)  # yapf: disable

#pl3 = np.array((-1,  1,  0,), dtype=PackedFloat3)
#pl3['x'] *= scale

#print(pl3['x'])
#print(dir(pl3['x']))
'''
for pl3 in vertices_np:
  #print(pl3)
  print(dir(pl3))
'''

#[[pl3[n]] for pl3 in vertices_np]
#print(PackedFloat3.names)

for pl3 in vertices_np:
  for name in PackedFloat3.names:
    pl3[name] *= scale


print(vertices_np.size)
