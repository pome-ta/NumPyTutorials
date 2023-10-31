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

'''
vertices = np.array(
  (
    np.array((-1,  1,  0,), dtype=PackedFloat3),
    np.array(( 1,  1,  0,), dtype=PackedFloat3),
    np.array((-1, -1,  0,), dtype=PackedFloat3),
    np.array(( 1, -1,  0,), dtype=PackedFloat3),
  )
)  # yapf: disable
'''
#print(dir(vertices))
#print(vertices.size)
#a = vertices * 0.8
scale = 0.8
#a = vertices * np.array((scale), dtype=PackedFloat3)

#a = np.array([-1,  1,  0,], dtype=PackedFloat3)
'''
vertices = np.array(
  [
    (-1,  1,  0,),
    ( 1,  1,  0,),
    (-1, -1,  0,),
    ( 1, -1,  0,),
  ],
dtype=PackedFloat3)  # yapf: disable
'''

#print(vertices.size)

#a = np.frompyfunc(lambda x, )

#a = vertices * np.array((scale), dtype=PackedFloat3)
#print(dir(vertices))
'''
__vertices = [
  np.array((-1,  1,  0,), dtype=Float),
  np.array(( 1,  1,  0,), dtype=Float),
  np.array((-1, -1,  0,), dtype=Float),
  np.array(( 1, -1,  0,), dtype=Float),
]  # yapf: disable

_vertices = [v * scale for v in __vertices]
'''

'''
_vertices = [
  [-1,  1,  0,],
  [ 1,  1,  0,],
  [ 1, -1,  0,],
  [ 1, -1,  0,],
]  # # yapf: disable

_vertices = [
  (-1,  1,  0,),
  ( 1,  1,  0,),
  ( 1, -1,  0,),
  ( 1, -1,  0,),
]  # # yapf: disable
'''


#vertices = np.array(_vertices, dtype=PackedFloat3)

vertices = np.array(
  [
    np.array((-1,  1,  0,), dtype=Float),
    np.array(( 1,  1,  0,), dtype=Float),
    np.array((-1, -1,  0,), dtype=Float),
    np.array(( 1, -1,  0,), dtype=Float),
  ], dtype=PackedFloat3
)  # yapf: disable

