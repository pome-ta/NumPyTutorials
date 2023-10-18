import numpy as np

vector_float4 = np.dtype(
  {
    'names': [
      'x',
      'y',
      'z',
      'w',
    ],
    'formats': [
      np.float32,
      np.float32,
      np.float32,
      np.float32,
    ],
    'offsets': [o * 4 for o in range(4)],
    'itemsize': 16,
  },
  align=True)

Vertex = np.dtype([('position', vector_float4), ('color', vector_float4)])

