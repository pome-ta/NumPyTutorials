import struct
import numpy as np

fu_pack = struct.Struct(">f")
fu_unpack = struct.Struct(">I")

np_floatBitsToUint = np.vectorize(
  lambda f: fu_unpack.unpack(fu_pack.pack(f))[0],
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
  size: int = 8
  l_float: list[float] = [float(f) for f in range(size)]
  h11 = hash11(l_float)
  print(h11)

