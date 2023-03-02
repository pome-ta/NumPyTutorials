from itertools import product
from functools import lru_cache

from pathlib import Path

import numpy as np
from PIL import Image as ImageP

UINT_MAX = 0xffff_ffff

k = np.array([0x456789ab, 0x6789ab45, 0x89ab4567]).astype(np.uint32)
u = np.array([1, 2, 3]).astype(np.uint32)

sq_size: int = 512

width_size = sq_size
height_size = sq_size

RGB_SIZE = 255
color_ch = 3

u_time = 0.4321
_xy = range(2)
product_list2 = list(product(_xy, repeat=2))
product_list3 = list(product(_xy, repeat=3))

testImg_path = Path(f'./testImg/test_img{sq_size:03}.npy')


def np_floatBitsToUint(f: np.array) -> np.array:
    shape = f.shape
    return np.reshape(
        np.frombuffer(np.array(f, dtype='f'), dtype=np.uint32), shape)


def np_mix(x: np.array, y: np.array, a: np.array) -> np.array:
    return (x * (1.0 - a)) + (y * a)


@lru_cache()
def _vec(w: int, h: int, c: int) -> np.array:
    return np.empty((w, h, c)).astype(np.float32)


@lru_cache()
def FragCoord(width, height) -> np.array:
    _row = np.arange(0, width)
    _col = np.arange(0, height).reshape(height, 1)
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
    
    _n = n.copy()
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


def grad(p: np.array) -> np.array:
    eps = 0.001
    x = vnoise21_f(p + [eps, 0.0]) - vnoise21_f(p - [eps, 0.0])
    y = vnoise21_f(p + [0.0, eps]) - vnoise21_f(p - [0.0, eps])
    _w, _h, _c = p.shape
    vec2 = _vec(_w, _h, _c)
    vec2[..., 0] = x
    vec2[..., 1] = y
    return 0.5 * vec2 / eps


def imageP2uint8_convert(_rgb):
    _l = _rgb * RGB_SIZE
    _l[np.less(_l, 0)] = 0
    _l[np.less(RGB_SIZE, _l)] = RGB_SIZE
    return _l


canvas_px = np.zeros((width_size, height_size, 3)).astype(np.uint8)
fragCoord = FragCoord(width_size, height_size)
# pos = (fragCoord * 2.0 - sq_size) / sq_size
pos = fragCoord / sq_size
pos = 26.0 * pos + u_time

np_grad = grad(pos)
_w, _h, _c = np_grad.shape
np_grad2b2 = np.reshape(np_grad, (_c, _w * _h))
np_ones = np.ones_like(np_grad2b2)

np_dot = np.dot(np_ones, np_grad2b2)

vec3 = _vec(width_size, height_size, 3)
vec3[..., 0] = pos[..., 0]
vec3[..., 1] = pos[..., 1]
vec3[..., 2] = u_time

u_grad = imageP2uint8_convert(np_grad)
canvas_px[..., 0] = u_grad[..., 0]
canvas_px[..., 1] = u_grad[..., 1]
# canvas_px[..., 2] = imageP2uint8_convert(np_dot)
imgp = ImageP.fromarray(canvas_px)

is_show = False
if is_show:
    imgp.show()

_ = 1
