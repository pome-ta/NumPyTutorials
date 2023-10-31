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


_vertices = [
  [-1,  1,  0,],
  [ 1,  1,  0,],
  [ 1, -1,  0,],
  [ 1, -1,  0,],
]  # # yapf: disable


vertices_py = [[vc * cs]]
