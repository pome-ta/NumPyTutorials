import struct
import numpy as np

#fu_pack = struct.Struct(">f")
#fu_unpack = struct.Struct(">I")
'''
np_floatBitsToUint = np.vectorize(
  lambda f: fu_unpack.unpack(fu_pack.pack(f))[0],
  otypes=[np.uint32],
  cache=True)
'''


def floatBitsToUint(f: float) -> int:
  #return fu_unpack.unpack(fu_pack.pack(f))[0]
  #f_p = fu_pack.pack(f)
  f_p = struct.pack('>f', f)
  #print(f'{f_p=}')
  #f_u = fu_unpack.unpack(f_p)
  f_u = struct.unpack('>I', f_p)
  #print(f'{f_u=}')
  return f_u[0]


np_floatBitsToUint = np.vectorize(floatBitsToUint,
                                  otypes=[np.uint32],
                                  cache=True)

UINT_MAX = 0xFFFF_FFFF
k = 0x4567_89AB


def out_bin(u32, memo=''):
  print(format(u32, '032b'), memo)


def uhash11(n: np.ndarray) -> np.ndarray:
  out_bin(UINT_MAX)
  out_bin(k)
  print('---')
  #print(f'0:{n=}')

  out_bin(n[0], 'null')
  _n = n << 1
  out_bin(_n[0], '<<')
  n ^= _n
  #print(f'1:{n=}')
  #print(bin(n[0]))
  out_bin(n[0], '^')
  _n = n >> 1
  out_bin(_n[0], '>>')

  n ^= _n
  #print(f'2:{n=}')
  #print(bin(n[0]))
  out_bin(n[0], '^')
  n *= k
  #print(f'3:{n=}')
  #print(bin(n[0]))
  out_bin(n[0], '*')
  n ^= n << 1
  #print(f'4:{n=}')
  #print(bin(n[0]))
  out_bin(n[0])
  nk = n * k
  #print(f'{nk=}')
  #print(bin(nk[0]))
  out_bin(n[0])
  return nk


def hash11(p: list[float]) -> np.ndarray:
  n = np_floatBitsToUint(p)
  return uhash11(n).astype(np.float32) / float(UINT_MAX)


if __name__ == "__main__":
  '''
  size: int = 8
  l_float: list[float] = [float(f) for f in range(size)]
  h11 = hash11(l_float)
  '''
  h11 = hash11([1.0])
  print(f'{h11=}')

