import struct
from functools import lru_cache

import numpy as np
from PIL import Image as ImageP

UINT_MAX = 0xffff_ffff

k = np.array([0x456789ab, 0x6789ab45, 0x89ab4567]).astype(np.uint32)
u = np.array([1, 2, 3]).astype(np.uint32)

sq_size: int = 320

width_size = sq_size
height_size = sq_size

RGB_SIZE = 255
color_ch = 3

u_time = 0.4321


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


fu_pack = struct.Struct('>f')
fu_unpack = struct.Struct('>I')


@lru_cache()
def floatBitsToUint(f: float) -> int:
  return fu_unpack.unpack(fu_pack.pack(f))[0]


def _mix(x, y, a):
  return (x * (1 - a)) + (y * a)


np_floatBitsToUint = np.vectorize(
  floatBitsToUint, otypes=[np.uint32], cache=True)

np_mix = np.vectorize(_mix, otypes=[np.float32], cache=True)


def uhash11(n: np.array) -> np.array:
  n ^= (n << u[0])
  n ^= (n >> [0])
  n *= k[0]
  n ^= (n << [0])
  return n * k[0]


def hash11(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash11(n).astype(np.float32) / float(UINT_MAX)


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


def vnoise21(p: np.array) -> np.array:
  n = np.floor(p)
  v = list(range(4))
  for j in range(2):
    for i in range(2):
      v[i + 2 * j] = hash21(n + [i, j])
  f = p - n
  return np_mix(
    np_mix(v[0], v[1], f[..., 0]),
    np_mix(v[2], v[3], f[..., 0]),
    f[..., 1], )


canvas_px = np.zeros((width_size, height_size, 3)).astype(np.uint8)
fragCoord = FragCoord(width_size, height_size)
# pos = (fragCoord * 2.0 - sq_size) / sq_size
pos = fragCoord / sq_size
pos = 16.0 * pos

v21 = vnoise21(pos)

# canvas_px[..., 0] = l[...,0] * RGB_SIZE
# canvas_px[..., 1] = l[...,0] * RGB_SIZE
# canvas_px[..., 2] = l[...,0] * RGB_SIZE


def _cnv(f):
  #   print(f * RGB_SIZE)
  #   _rgb2 = RGB_SIZE * 2
  #   _n = f * _rgb2 - RGB_SIZE
  #   return f * RGB_SIZE if _n < 0 else 0
  _n = f * RGB_SIZE
  return _n if _n > 0 else 0


np_cnv = np.vectorize(_cnv, otypes=[np.uint8], cache=True)


def uintCnv(l):
  _l = l * RGB_SIZE
  _l[np.less(_l, 0)] = 0
  _l[np.less(RGB_SIZE, _l)] = RGB_SIZE
  return _l


_pos = uintCnv(v21)

canvas_px[..., 0] = _pos
canvas_px[..., 1] = _pos
canvas_px[..., 2] = _pos

imgp = ImageP.fromarray(canvas_px)
imgp.show()

_ = 1

