import struct
from functools import lru_cache

import numpy as np
from PIL import Image as ImageP

# ハッシュ値関係
UINT_MAX = 0xffff_ffff
k = 0x4567_89ab

# キャンバスサイズ関係
sq_size: int = 128
width_size = sq_size
height_size = sq_size

# キャンバスカラー関係
RGB_SIZE = 255
color_ch = 3


fu_pack = struct.Struct('>f')
fu_unpack = struct.Struct('>I')


@lru_cache()
def floatBitsToUint(f: float) -> int:
  return fu_unpack.unpack(fu_pack.pack(f))[0]


np_floatBitsToUint = np.vectorize(floatBitsToUint,
                                  otypes=[np.uint32],
                                  cache=True)


def uhash11(n: np.array) -> np.array:
  n ^= (n << 1)
  n ^= (n >> 1)
  n *= k
  n ^= (n << 1)
  return n * k


def hash11(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash11(n).astype(np.float32) / float(UINT_MAX)


h11 = hash11([list(range(sq_size))])

canvas_px = np.zeros((width_size, height_size, 3)).astype(np.uint8)

for c in range(color_ch):
  canvas_px[:, :, c] = h11 * RGB_SIZE

imgp = ImageP.fromarray(canvas_px)
imgp.show()

_ = 1

