import ctypes
import struct
import numpy as np
from PIL import Image as ImageP
from pprint import pprint

UINT_MAX = 0xffff_ffff
k = 0x4567_89ab

sq_size: int = 4

width_size = sq_size
height_size = sq_size

RGB_SIZE = 255
color_ch = 3


def _vec(x):
  _vec_array = np.empty(x).astype(np.float32)


def vec(x):
  pass


def FragCoord(width, height) -> np.array:
  _row = np.arange(0, width)
  _col = np.arange(0, height).reshape(height, 1)
  _x, _y = np.meshgrid(_row, _col)
  _pos = np.empty((width, height, 2)).astype(np.float32)
  _pos[:, :, 0] = _x
  _pos[:, :, 1] = _y
  return _pos


def uint32(s) -> int:
  _s = s if s > 0 else 0
  return int(_s) if _s <= UINT_MAX else ctypes.c_uint32(int(_s)).value


fu_pack = struct.Struct('>f')
fu_unpack = struct.Struct('>I')


def floatBitsToUint(f: float) -> int:
  fp = fu_pack.pack(f)
  fu = fu_unpack.unpack(fp)[0]
  return uint32(fu)


np_floatBitsToUint = np.vectorize(
  floatBitsToUint, otypes=[np.uint32], cache=True)


def uhash11(n: np.array) -> np.array:
  n ^= (n << 1)
  n ^= (n >> 1)
  n *= k
  n ^= (n << 1)
  return n * k


def hash11(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash11(n).astype(np.float32) / float(UINT_MAX)


#vec1 = np.empty((width_size, height_size, 1)).astype(np.float32)
#vec2 = np.empty((width_size, height_size, 2)).astype(np.float32)
#vec3 = np.empty((width_size, height_size, 3)).astype(np.float32)

pos = FragCoord(width_size, height_size)
pprint(pos[0])

hash_x = hash11(pos[:, :, 0])

#canvas_px = np.zeros((width_size, height_size, 3), dtype=np.uint8)
canvas_px = np.zeros((width_size, height_size, 3)).astype(np.uint8)
canvas_px[:, :, 0] = hash_x * RGB_SIZE
canvas_px[:, :, 1] = hash_x * RGB_SIZE
canvas_px[:, :, 2] = hash_x * RGB_SIZE

imgp = ImageP.fromarray(canvas_px)

_ = 1

