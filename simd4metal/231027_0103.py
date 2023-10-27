import ctypes
from dataclasses import dataclass

import numpy as np

Float = np.dtype(np.float32)

oldVertices = np.array(
  (
    # yapf: disable
    -1,
    1,
    0,
    1,
    -1,
    0,
    -1,
    -1,
    0,
    -1,
    1,
    0,
    1,
    1,
    0,
    1,
    -1,
    0),
  dtype=Float)
# yapf: enable

#print(dir(oldVertices))
print(oldVertices.strides)
print(oldVertices.size)

