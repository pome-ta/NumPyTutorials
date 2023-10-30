import ctypes
from dataclasses import dataclass

import numpy as np

Float = np.dtype(np.float32, align=True)
UInt16 = np.dtype(np.uint16)

indices = np.array((0, 3, 2, 0, 1, 3), dtype=UInt16)

#print(dir(indices))
#print(indices.itemsize)
#print(indices.size)
#print(dir(UInt16))
#print(UInt16.itemsize)

print(type(indices.size))
