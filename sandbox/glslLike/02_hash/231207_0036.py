import struct
from functools import lru_cache

import numpy as np
from PIL import Image as ImageP

UINT_MAX = 0xffff_ffff

k = np.array([0x456789ab, 0x6789ab45, 0x89ab4567]).astype(np.uint32)
u = np.array([1, 2, 3]).astype(np.uint32)

sq_size: int = 32

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


np_floatBitsToUint = np.vectorize(floatBitsToUint,
                                  otypes=[np.uint32],
                                  cache=True)


def uhash11(n: np.array) -> np.array:
  n ^= (n << u[0])
  n ^= (n >> u[0])
  n *= k[0]
  n ^= (n << u[0])
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


def hash22(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash22(n).astype(np.float32) / float(UINT_MAX)


def hash21(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  _h22 = uhash22(n).astype(np.float32)
  return _h22[..., 0] / float(UINT_MAX)


pos = FragCoord(width_size, height_size)
h11 = hash11([list(range(32))])
h21 = hash21(pos)
#h11 = hash11(pos[0])

canvas_px = np.zeros((width_size, height_size, 3)).astype(np.uint8)

for c in range(color_ch):
  canvas_px[:, :, c] = h11 * RGB_SIZE

imgp = ImageP.fromarray(canvas_px)
imgp.show()

_ = 1

