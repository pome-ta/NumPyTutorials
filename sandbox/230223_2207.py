import ctypes
import struct
import numpy as np
from PIL import Image as ImageP

UINT_MAX = 0xffff_ffff
sq_size: int = 256

width_size = sq_size
height_size = sq_size


def hash11(p: np.array):
    pass


def FragCoord(width, height) -> np.array:
    _x, _y = np.meshgrid(np.arange(0, width), np.arange(0, height).reshape(height, 1))
    _pos = np.empty((width, height, 2), dtype=np.float32)
    _pos[:, :, 0] = _x
    _pos[:, :, 1] = _y
    return _pos


def uint32(s) -> int:
    # xxx: 負の値処理するかどうか？
    _s = s
    # _s = s if s > 0 else 0
    _c_uint32 = ctypes.c_uint32(int(_s))
    return _c_uint32.value


fu_pack = struct.Struct('>f')
fu_unpack = struct.Struct('>I')


def floatBitsToUint(f: float) -> int:
    # fp = struct.pack('>f', f)
    # fu = struct.unpack('>I', fp)[0]
    fp = fu_pack.pack(f)
    fu = fu_unpack.unpack(fp)[0]
    return uint32(fu)


pos = FragCoord(width_size, height_size)

canvas_px = np.zeros((width_size, height_size, 3), dtype=np.uint8)
canvas_px[:, :, 0] = pos[:, :, 1]
canvas_px[:, :, 1] = pos[:, :, 0]

# ImageP.fromarray(canvas_px).show()

fbu = floatBitsToUint(1.0)

_ = 1
