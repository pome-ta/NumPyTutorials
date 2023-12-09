import struct
import numpy as np

# --- Python 上のでの型キャスト調整
fu_pack = struct.Struct(">f")
fu_unpack = struct.Struct(">I")

np_floatBitsToUint = np.vectorize(
  lambda f: fu_unpack.unpack(fu_pack.pack(f))[0],
  otypes=[np.uint32],
  cache=True)
# --- --- --- /

UINT_MAX = 0xFFFF_FFFF  # 符号なし整数の最大値(uint32)
k = 0x4567_89AB  # 算術積に使う大きな桁数の定数(uint32)


def uhash11(n: np.ndarray) -> np.ndarray:
  # --- コラムの部分 Xorshift
  n ^= n << 1
  n ^= n >> 1
  n *= k
  n ^= n << 1
  u_list = n * k
  #print(u_list)
  return u_list


def hash11(p: list[float]) -> np.ndarray:
  n = np_floatBitsToUint(p)  # 浮動小数点数(float32) のビット列を符号なし整数(uint32)に変換
  return uhash11(n).astype(np.float32) / float(UINT_MAX)  # 値の正規化


if __name__ == "__main__":
  size: int = 8
  l_float: list[float] = [
    float(f) for f in range(size)
  ]  # 長さ`'size` の[0.0, 1.0, 2.0, ..., (`size` - 1.0)] の配列
  h11 = hash11(l_float)
  print(h11)

