import struct
import numpy as np

# --- Python 上のでの型キャスト調整
fu_pack = struct.Struct(">f")
fu_unpack = struct.Struct(">I")

np_floatBitsToUint = np.vectorize(
  lambda f: fu_unpack.unpack(fu_pack.pack(f))[0],
  otypes=[np.uint32],
  cache=True)
# --- /

# ハッシュ値関係
UINT_MAX = 0xFFFF_FFFF
K = 0x4567_89AB


def uhash11(n: np.ndarray) -> np.ndarray:
  n ^= n << 1
  n ^= n >> 1
  n *= K
  n ^= n << 1
  return n * K


def hash11(p: list[float]) -> np.ndarray:
  n = np_floatBitsToUint(p)
  return uhash11(n).astype(np.float32) / float(UINT_MAX)


if __name__ == "__main__":
  length_size: int = 32
  # l_float = list(map(float, range(length_size)))
  l_float = [float(f) for f in range(length_size)]
  h11 = hash11(l_float)
  print(h11)

