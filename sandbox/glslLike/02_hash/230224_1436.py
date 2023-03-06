import ctypes
import struct
import numpy as np
from PIL import Image as ImageP

UINT_MAX = 0xffff_ffff
k = 0x4567_89ab

sq_size: int = 8

width_size = sq_size
height_size = sq_size

RGB_SIZE = 255
color_ch = 3



def FragCoord(width, height) -> np.array:
  _x, _y = np.meshgrid(
    np.arange(0, width), np.arange(0, height).reshape(height, 1))
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


#4294_9672_95
#4265_4433_28
#2092_9904_64
#1610_6127_36
vec1 = np.empty((width_size, height_size, 1)).astype(np.float32)
vec2 = np.empty((width_size, height_size, 2)).astype(np.float32)
vec3 = np.empty((width_size, height_size, 3)).astype(np.float32)

pos = FragCoord(width_size, height_size)
pos2 = np.array([pos[:, :, 1], pos[:, :, 0]])

hash_x = hash11(pos[:, :, 0])

#canvas_px = np.zeros((width_size, height_size, 3), dtype=np.uint8)
canvas_px = np.zeros((width_size, height_size, 3)).astype(np.uint8)
canvas_px[:, :, 0] = hash_x * RGB_SIZE
canvas_px[:, :, 1] = hash_x * RGB_SIZE
canvas_px[:, :, 2] = hash_x * RGB_SIZE


imgp = ImageP.fromarray(canvas_px)

#fbu = floatBitsToUint(1.0)

_ = 1

