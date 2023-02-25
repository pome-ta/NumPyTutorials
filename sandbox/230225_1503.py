import ctypes
import struct
from functools import lru_cache

import numpy as np
from PIL import Image as ImageP

from pprint import pprint

UINT_MAX = 0xffff_ffff

k = np.array([0x456789ab, 0x6789ab45, 0x89ab4567]).astype(np.uint32)
u = np.array([1, 2, 3]).astype(np.uint32)

sq_size: int = 256

width_size = sq_size
height_size = sq_size

RGB_SIZE = 255
color_ch = 3

u_time = 0.123


@lru_cache()
def _vec(w, h, c):
  return np.empty((w, h, c)).astype(np.float32)


def FragCoord(width, height) -> np.array:
  _row = np.arange(0, width)
  _col = np.arange(0, height).reshape(height, 1)
  _x, _y = np.meshgrid(_row, _col)
  _pos = _vec(width, height, 2)
  _pos[:, :, 0] = _x
  _pos[:, :, 1] = _y
  return _pos


@lru_cache()
def uint32(s) -> int:
  _s = s if s > 0 else 0
  return int(_s) if _s <= UINT_MAX else ctypes.c_uint32(int(_s)).value


fu_pack = struct.Struct('>f')
fu_unpack = struct.Struct('>I')


@lru_cache()
def floatBitsToUint(f: float) -> int:
  fp = fu_pack.pack(f)
  fu = fu_unpack.unpack(fp)[0]
  return uint32(fu)


np_floatBitsToUint = np.vectorize(
  floatBitsToUint, otypes=[np.uint32], cache=True)
'''
def uhash11(n: np.array) -> np.array:
  n ^= (n << 1)
  n ^= (n >> 1)
  n *= k
  n ^= (n << 1)
  return n * k


def hash11(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash11(n).astype(np.float32) / float(UINT_MAX)
'''


def uhash22(n: np.array) -> np.array:
  _n = n.copy()
  _n[..., 0] = n[..., 1]
  _n[..., 1] = n[..., 0]
  n ^= (_n << u[:2])

  _n = n.copy()
  _n[..., 0] = n[..., 1]
  _n[..., 1] = n[..., 0]
  n ^= (_n >> u[:2])

  n *= k[:2]

  _n = n.copy()
  _n[..., 0] = n[..., 1]
  _n[..., 1] = n[..., 0]
  n ^= (_n << u[:2])
  return n * k[:2]


def uhash33(n: np.array) -> np.array:
  _n = n.copy()
  _n[..., 0] = n[..., 1]
  _n[..., 1] = n[..., 2]
  _n[..., 2] = n[..., 0]
  n ^= (_n << u)

  _n = n.copy()
  _n[..., 0] = n[..., 1]
  _n[..., 1] = n[..., 2]
  _n[..., 2] = n[..., 0]
  n ^= (_n >> u)

  n *= k

  __n = n.copy()
  _n[..., 0] = n[..., 1]
  _n[..., 1] = n[..., 2]
  _n[..., 2] = n[..., 0]
  n ^= (_n << u)
  return n * k


def hash22(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash22(n).astype(np.float32) / float(UINT_MAX)


def hash33(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash33(n).astype(np.float32) / float(UINT_MAX)


def hash21(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  _h22 = uhash22(n).astype(np.float32)
  return _h22[..., 0] / float(UINT_MAX)


def hash31(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  _h33 = uhash33(n).astype(np.float32)
  return _h33[..., 0] / float(UINT_MAX)


pos = FragCoord(width_size, height_size)
vec3 = _vec(width_size, height_size, 3)
vec3[..., 0] = pos[..., 0]
vec3[..., 1] = pos[..., 1]
vec3[..., 2] = u_time

hash_xy = hash22(pos)
h21 = hash21(pos)
h33 = hash33(vec3)

# canvas_px = np.zeros((width_size, height_size, 3), dtype=np.uint8)
canvas_px = np.zeros((width_size, height_size, 3)).astype(np.uint8)
'''
canvas_px[:, :, 0] = hash_xy[:, :, 0] * RGB_SIZE
canvas_px[:, :, 1] = hash_xy[..., 1] * RGB_SIZE
canvas_px[:, :, 2] = RGB_SIZE
'''
'''
canvas_px[:, :, 0] = h21 * RGB_SIZE
canvas_px[:, :, 1] = h21 * RGB_SIZE
canvas_px[:, :, 2] = h21 * RGB_SIZE
'''

canvas_px[:, :, 0] = h33[...,0] * RGB_SIZE
canvas_px[:, :, 1] = h33[...,1] * RGB_SIZE
canvas_px[:, :, 2] = h33[...,2] * RGB_SIZE

imgp = ImageP.fromarray(canvas_px)

# a = np.arange(18).reshape((3, 3, 2))
# aa = a[:, 1:]

_ = 1

