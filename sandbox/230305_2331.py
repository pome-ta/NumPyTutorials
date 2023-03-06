from itertools import product

import numpy as np
from PIL import Image as ImageP

RGB_SIZE = 255
COLOR_CH = 3

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
  _x, _y = np.meshgrid(_row, _col)
  _pos = _vec(width, height, 2)
  _pos[..., 0] = _x
  _pos[..., 1] = _y
  return _pos


# start hash
UINT_MAX = 0xffff_ffff
k = np.array([0x456789ab, 0x6789ab45, 0x89ab4567]).astype(np.uint32)
u = np.array([1, 2, 3]).astype(np.uint32)


def uhash11(n: np.array) -> np.array:
  n ^= (n << u[0])
  n ^= (n >> [0])
  n *= k[0]
  n ^= (n << [0])
  return n * k[0]


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


def hash11(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash11(n).astype(np.float32) / float(UINT_MAX)


def hash21(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  _h22 = uhash22(n).astype(np.float32)
  return _h22[..., 0] / float(UINT_MAX)


def hash31(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  _h33 = uhash33(n).astype(np.float32)
  return _h33[..., 0] / float(UINT_MAX)


def hash22(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash22(n).astype(np.float32) / float(UINT_MAX)


def hash33(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash33(n).astype(np.float32) / float(UINT_MAX)


# end hash


def g_noise21(p: np.array) -> np.array:
  n: np.array = np.floor(p)
  f: np.array = np.mod(p, 1.0)
  _, _, _index = f.shape
  v: list = []
  for j in range(2):
    for i in range(2):
      g = np_normalize(hash22(n + [i, j]) - 0.5)
      _ = 1
      v[i + 2 * j] = sum([g[..., _i] * (f - [i, j]) for _i in range(_index)])
  f = f * f * f * (10.0 - 15.0 * f + 6.0 * f * f)
  return 0.5 * np_mix(
    np_mix(
      v[0],
      v[1],
      f[..., 0], ),
    np_mix(
      v[2],
      v[3],
      f[..., 1], ),
    f[..., 1], ) + 0.5


def vnoise21_n(p: np.array) -> np.array:
  n: np.array = np.floor(p)
  v: list = [hash21(n + [_i, _j]) for _j, _i in product_list2]
  f: np.array = p - n
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


def gl_main():
  pos = (fragCoord * 2.0 - sq_size) / sq_size
  
  fragColor[..., 0] = pos[..., 0]
  fragColor[..., 1] = pos[..., 1]
  fragColor[..., 2] = 0.0
  return fragColor


def convert_uint8_rgb(_rgb):
  _l = _rgb * RGB_SIZE
  _l[np.less(_l, 0)] = 0
  _l[np.less(RGB_SIZE, _l)] = RGB_SIZE
  return np.flipud(_l).astype(np.uint8)


def main():
  canvas_px = convert_uint8_rgb(gl_main())
  _ = 1
  imgp = ImageP.fromarray(canvas_px)

  is_show = True
  if is_show:
    imgp.show()


if __name__ == '__main__':
  sq_size: int = 512
  width_size = sq_size
  height_size = sq_size

  u_time = 0.4321
  fragColor = _vec(width_size, height_size, COLOR_CH)
  fragCoord = FragCoord(width_size, height_size)
  main()
  _ = 1

