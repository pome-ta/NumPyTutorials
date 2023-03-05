from itertools import product

import numpy as np
from PIL import Image as ImageP

UINT_MAX = 0xffff_ffff

k = np.array([0x456789ab, 0x6789ab45, 0x89ab4567]).astype(np.uint32)
u = np.array([1, 2, 3]).astype(np.uint32)

sq_size: int = 512

width_size = sq_size
height_size = sq_size

RGB_SIZE = 255
COLOR_CH = 3

u_time = 0.4321
_xy = range(2)
product_list2 = list(product(_xy, repeat=2))
product_list3 = list(product(_xy, repeat=3))


def np_floatBitsToUint(f: np.array) -> np.array:
  shape = f.shape
  return np.reshape(
    np.frombuffer(np.array(f, dtype='f'), dtype=np.uint32), shape)


def np_mix(x: np.array, y: np.array, a: np.array) -> np.array:
  return (x * (1.0 - a)) + (y * a)


def _vec(w: int, h: int, c: int) -> np.array:
  return np.empty((w, h, c)).astype(np.float32)


def FragCoord(width, height) -> np.array:
  _row = np.arange(0, width)
  _col = _row[:np.newaxis]
  # return np.dstack(np.meshgrid(_row, _col))
  _x, _y = np.meshgrid(_row, _col)
  _pos = _vec(width, height, 2)
  _pos[..., 0] = _x
  _pos[..., 1] = _y
  return _pos


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
  _u = u[:2]
  _k = k[:2]

  x, y = np.dsplit(n, 2)
  n ^= (np.dstack([y, x]) << _u)

  x, y = np.dsplit(n, 2)
  n ^= (np.dstack([y, x]) >> _u)

  n *= _k

  x, y = np.dsplit(n, 2)
  n ^= (np.dstack([y, x]) << _u)
  return n * _k


def uhash33(n: np.array) -> np.array:
  x, y, z = np.dsplit(n, 3)
  n ^= (np.dstack([y, z, x]) << u)

  x, y, z = np.dsplit(n, 3)
  n ^= (np.dstack([y, z, x]) >> u)

  n *= k

  x, y, z = np.dsplit(n, 3)
  n ^= (np.dstack([y, z, x]) << u)
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


def vnoise21_n(p: np.array) -> np.array:
  n = np.floor(p)
  v = [hash21(n + [_i, _j]) for _j, _i in product_list2]
  f = p - n
  return np_mix(
    np_mix(v[0], v[1], f[..., 0]),
    np_mix(v[2], v[3], f[..., 0]),
    f[..., 1], )


def vnoise21_f(p: np.array) -> np.array:
  n = np.floor(p)
  v = [hash21(n + [_i, _j]) for _j, _i in product_list2]
  f = p - n
  f = f * f * (3.0 - 2.0 * f)
  return np_mix(
    np_mix(v[0], v[1], f[..., 0]),
    np_mix(v[2], v[3], f[..., 0]),
    f[..., 1], )


def vnoise31(p: np.array) -> np.array:
  n = np.floor(p)
  v = [hash31(n + [_i, _j, _k]) for _k, _j, _i in product_list3]
  f = p - n
  f = f * f * (3.0 - 2.0 * f)

  w = [
    np_mix(
      np_mix(v[4 * _i], v[4 * _i + 1], f[..., 0]),
      np_mix(v[4 * _i + 2], v[4 * _i + 3], f[..., 0]), f[..., 1]) for _i in _xy
  ]

  return np_mix(w[0], w[1], f[..., 2])


def convert_uint8_rgb(_rgb):
  _l = _rgb * RGB_SIZE
  _l[np.less(_l, 0)] = 0
  _l[np.less(RGB_SIZE, _l)] = RGB_SIZE
  return _l


canvas_px = np.zeros((width_size, height_size, COLOR_CH)).astype(np.uint8)
fragCoord = FragCoord(width_size, height_size)
pos = fragCoord / sq_size
pos = 10.0 * pos + u_time

vec3 = _vec(width_size, height_size, 3)
vec3[..., 0] = pos[..., 0]
vec3[..., 1] = pos[..., 1]
vec3[..., 2] = u_time

v21_n = vnoise21_n(pos)
v21_f = vnoise21_f(pos)
v31 = vnoise31(vec3)

out_n = convert_uint8_rgb(v21_n)
out_f = convert_uint8_rgb(v21_f)
out_3 = convert_uint8_rgb(v31)

split_num = int(sq_size / 3)

for div in range(3):
  if div == 0:
    for i in range(3):
      s = split_num * div
      e = split_num * (div + 1)
      canvas_px[..., s:e, i] = out_n[..., s:e]
  if div == 1:
    for i in range(3):
      s = split_num * div + 1
      e = split_num * (div + 1)
      canvas_px[..., s:e, i] = out_f[..., s:e]
  if div == 2:
    for i in range(3):
      s = split_num * div + 1
      e = sq_size
      canvas_px[..., s:e, i] = out_3[..., s:e]

imgp = ImageP.fromarray(canvas_px)

_ = 1

