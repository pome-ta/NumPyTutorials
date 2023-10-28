import ctypes
from dataclasses import dataclass

import numpy as np

Float = np.dtype(np.float32, align=True)
UInt16 = np.dtype(np.uint16)

oldVertices = np.array(
  (-1,  1,  0,  # triangle 1
    1, -1,  0,
   -1, -1,  0,
   -1,  1,  0,  # triangle 2
    1,  1,  0,
    1, -1,  0,),
  dtype=Float)  # yapf: disable

scale = 0.8
vertices = oldVertices * scale
#print(dir(oldVertices))
print(oldVertices.strides)
print(oldVertices.size)
print(UInt16.itemsize)
print(oldVertices.ctypes)
print(dir(Float))
print(Float.alignment)
print(UInt16.alignment)
print(Float.byteorder)
print(Float.itemsize)

