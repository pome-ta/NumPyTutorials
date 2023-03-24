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


def np_fract(p: np.array) -> np.array:
  return np.mod(p, 1.0)


def np_length(v: np.array) -> np.array:
  _, _, _shape = v.shape
  return np.sqrt(sum([np.square(v[..., _i]) for _i in range(_shape)]))


def np_normalize(v: np.array) -> np.array:
  _, _, _shape = v.shape
  _l = np_length(v)
  return np.dstack([v[..., _i] / _l for _i in range(_shape)])


def np_dot(v0: np.array, v1: np.array) -> np.array:
  _, _, _shape = v0.shape
  return sum([v0[..., _i] * v1[..., _i] for _i in range(_shape)])


def np_min(v: np.array, a) -> np.array:
  v[np.less(a, v)] = a
  return v


def np_max(v: np.array, a) -> np.array:
  v[np.less(v, a)] = a
  return v


def np_clamp(v: np.array, a, b) -> np.array:
  return np_min(np_max(v, a), b)


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


def switch_yx(p: np.array) -> np.array:
  _p = p.copy()
  _p[..., 0] = p[..., 1]
  _p[..., 1] = p[..., 0]
  return _p


def switch_yzx(p: np.array) -> np.array:
  _p = p.copy()
  _p[..., 0] = p[..., 1]
  _p[..., 1] = p[..., 2]
  _p[..., 2] = p[..., 0]
  return _p


def hsv2rgb(cx: np.array, cy: float, cz: float):
  cx_vec3 = _vec(width_size, height_size, 3)
  cx_vec3[..., 0], cx_vec3[..., 1], cx_vec3[..., 2] = [cx, cx, cx]
  rgb_vec3 = _vec(width_size, height_size, 3)
  rgb_vec3[..., 0], rgb_vec3[..., 1], rgb_vec3[..., 2] = [0.0, 4.0, 2.0]

  _abs_mod = np.abs(np.mod(cx_vec3 * 6.0 + rgb_vec3, 6.0) - 3.0)
  rgb = np_clamp(_abs_mod - 1.0, 0.0, 1.0)

  x_vec3 = _vec(width_size, height_size, 3)
  x_vec3[..., 0], x_vec3[..., 1], x_vec3[..., 2] = [1.0, 1.0, 1.0]
  cy_vec3 = _vec(width_size, height_size, 3)
  cy_vec3[..., 0], cy_vec3[..., 1], cy_vec3[..., 2] = [cy, cy, cy]

  return cz * np_mix(x_vec3, rgb, cy_vec3)


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
  n ^= (switch_yx(n) << _u)
  n ^= (switch_yx(n) >> _u)
  n *= _k
  n ^= (switch_yx(n) << _u)
  return n * _k


def uhash33(n: np.array) -> np.array:
  n ^= (switch_yzx(n) << u)
  n ^= (switch_yzx(n) >> u)
  n *= k
  n ^= (switch_yzx(n) << u)
  return n * k


def hash11(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  #return uhash11(n).astype(np.float32) / float(UINT_MAX)
  return uhash11(n) / float(UINT_MAX)


def hash21(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  _h22 = uhash22(n).astype(np.float32)
  return _h22[..., 0] / float(UINT_MAX)


def hash31(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  print(n)
  _h33 = uhash33(n).astype(np.float32)
  return _h33[..., 0] / float(UINT_MAX)


def hash22(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash22(n).astype(np.float32) / float(UINT_MAX)


def hash33(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash33(n).astype(np.float32) / float(UINT_MAX)


# end hash


def vnoise21(p: np.array) -> np.array:
  n = np.floor(p)
  v = [hash21(n + [_i, _j]) for _j, _i in product_list2]
  f = np_fract(p)
  f = f * f * f * (10.0 - 15.0 * f + 6.0 * f * f)
  return np_mix(
    np_mix(v[0], v[1], f[..., 0]),
    np_mix(v[2], v[3], f[..., 0]),
    f[..., 1], )


def vnoise31(p: np.array) -> np.array:
  n = np.floor(p)
  v = [hash31(n + [_i, _j, _k]) for _k, _j, _i in product_list3]
  f = np_fract(p)
  f = f * f * f * (10.0 - 15.0 * f + 6.0 * f * f)
  w = [
    np_mix(
      np_mix(v[4 * _i], v[4 * _i + 1], f[..., 0]),
      np_mix(v[4 * _i + 2], v[4 * _i + 3], f[..., 0]), f[..., 1]) for _i in _xy
  ]
  return np_mix(w[0], w[1], f[..., 2])


def gnoise21(p: np.array) -> np.array:
  n: np.array = np.floor(p)
  f: np.array = np_fract(p)
  v: list = [
    np_dot(np_normalize(hash22(n + [_i, _j]) - 0.5), f - [_i, _j])
    for _j, _i in product_list2
  ]
  f = f * f * f * (10.0 - 15.0 * f + 6.0 * f * f)
  return 0.5 * np_mix(
    np_mix(
      v[0],
      v[1],
      f[..., 0], ),
    np_mix(
      v[2],
      v[3],
      f[..., 0], ),
    f[..., 1], ) + 0.5


def gnoise31(p: np.array) -> np.array:
  n: np.array = np.floor(p)
  f: np.array = np_fract(p)
  v: list = [
    np_dot(np_normalize(hash33(n + [_i, _j, _k]) - 0.5), f - [_i, _j, _k])
    for _k, _j, _i in product_list3
  ]
  f = f * f * f * (10.0 - 15.0 * f + 6.0 * f * f)
  w: list = [
    np_mix(
      np_mix(
        v[4 * _i],
        v[4 * _i + 1],
        f[..., 0], ),
      np_mix(
        v[4 * _i + 2],
        v[4 * _i + 3],
        f[..., 0], ),
      f[..., 1], ) for _i in _xy
  ]
  return 0.5 * np_mix(
    w[0],
    w[1],
    f[..., 2], ) + 0.5


def gtable2(lattice: np.array, p: np.array) -> np.array:
  px, py = [p[..., 0], p[..., 1]]
  n = np_floatBitsToUint(lattice)
  ind = uhash22(n)[..., 0] >> 29
  _u = 0.92387953 * np.where(ind < 4, px, py)  # 0.92387953 = cos(pi/8)
  _v = 0.38268343 * np.where(ind < 4, py, px)  # 0.38268343 = sin(pi/8)
  return np.where((ind & 1) == 0, _u, -_u) + np.where((ind & 2) == 0, _v, -_v)


def pnoise21(p: np.array) -> np.array:
  n: np.array = np.floor(p)
  f: np.array = np_fract(p)
  v: list = [gtable2(n + [_i, _j], f - [_i, _j]) for _j, _i in product_list2]
  f = f * f * f * (10.0 - 15.0 * f + 6.0 * f * f)
  return 0.5 * np_mix(
    np_mix(
      v[0],
      v[1],
      f[..., 0], ),
    np_mix(
      v[2],
      v[3],
      f[..., 0], ),
    f[..., 1], ) + 0.5


def gtable3(lattice: np.array, p: np.array) -> np.array:
  px, py, pz = [p[..., 0], p[..., 1], p[..., 2]]
  n = np_floatBitsToUint(lattice)
  ind = uhash33(n)[..., 0] >> 28
  _u = np.where(ind < 8, px, py)
  _v = np.where(ind < 4, py, np.where((ind == 12) | (ind == 14), px, pz))
  return np.where((ind & 1) == 1, _u, -_u) + np.where((ind & 2) == 1, _v, -_v)


def pnoise31(p: np.array) -> np.array:
  n: np.array = np.floor(p)
  f: np.array = np_fract(p)
  v: list = [
    gtable3(n + [_i, _j, _k], f - [_i, _j, _k]) * 0.70710678  # ≒ 1/sqrt(2)
    for _k, _j, _i in product_list3
  ]
  f = f * f * f * (10.0 - 15.0 * f + 6.0 * f * f)
  w: list = [
    np_mix(
      np_mix(
        v[4 * _i],
        v[4 * _i + 1],
        f[..., 0], ),
      np_mix(
        v[4 * _i + 2],
        v[4 * _i + 3],
        f[..., 0], ),
      f[..., 1], ) for _i in _xy
  ]
  return 0.5 * np_mix(
    w[0],
    w[1],
    f[..., 2], ) + 0.5


def gl_main():
  # pos = (fragCoord * 2.0 - sq_size) / sq_size
  pos = fragCoord / sq_size
  pos = 18.0 * pos + u_time

  vec3 = _vec(width_size, height_size, 3)
  vec3[..., 0], vec3[..., 1], vec3[..., 2] = [pos[..., 0], pos[..., 1], u_time]

  # p31 = pnoise31(vec3)
  #g31 = hash11(pos[..., 0])
  g31 = hash31(vec3)
  
  print(g31)
  # p21 = pnoise21(pos)
  for c in range(COLOR_CH):
    fragColor[..., c] = g31

  return fragColor


def convert_uint8_rgb(_rgb):
  _l = _rgb * RGB_SIZE
  _l[np.less(_l, 0)] = 0
  _l[np.less(RGB_SIZE, _l)] = RGB_SIZE
  return np.flipud(_l).astype(np.uint8)


def main():
  gl_canvas = gl_main()
  canvas_px = convert_uint8_rgb(gl_canvas)
  imgp = ImageP.fromarray(canvas_px)

  if is_show:
    imgp.show()


if __name__ == '__main__':
  is_profile = 0
  is_show = 1

  sq_size: int = 512
  width_size = sq_size
  height_size = sq_size

  u_time = 0.4321
  fragColor = _vec(width_size, height_size, COLOR_CH)
  fragCoord = FragCoord(width_size, height_size)

  if is_profile:
    import cProfile

    cProfile.run('main()', sort=1)
  else:
    main()
  _ = 1

