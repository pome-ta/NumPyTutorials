import struct
import numpy as np

fu_pack = struct.Struct(">f")
fu_unpack = struct.Struct(">I")
'''
np_floatBitsToUint = np.vectorize(
  lambda f: fu_unpack.unpack(fu_pack.pack(f))[0],
  otypes=[np.uint32],
  cache=True)
'''


def floatBitsToUint(f: float) -> int:
  #return fu_unpack.unpack(fu_pack.pack(f))[0]
  f_p = fu_pack.pack(f)
  print(f'{f_p=}')
  f_u = fu_unpack.unpack(f_p)
  print(f'{f_u=}')
  return f_u[0]


np_floatBitsToUint = np.vectorize(floatBitsToUint,
                                  otypes=[np.uint32],
                                  cache=True)

UINT_MAX = 0xFFFF_FFFF
k = 0x4567_89AB


def uhash11(n: np.ndarray) -> np.ndarray:
  n ^= n << 1
  n ^= n >> 1
  n *= k
  n ^= n << 1
  return n * k


def hash11(p: list[float]) -> np.ndarray:
  n = np_floatBitsToUint(p)
  return uhash11(n).astype(np.float32) / float(UINT_MAX)


if __name__ == "__main__":
  #size: int = 8
  #l_float: list[float] = [float(f) for f in range(size)]
  #h11 = hash11(l_float)
  h11 = hash11([1.0])
  print(f'{h11=}')

