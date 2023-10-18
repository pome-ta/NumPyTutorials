import numpy as np

vector_float4 = np.dtype(
  {
    'names': [
      'a','b','c','d',
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
  align=False)

position = np.array((-0.5, -0.5, 0.0, 1.0), dtype=vector_float4)
