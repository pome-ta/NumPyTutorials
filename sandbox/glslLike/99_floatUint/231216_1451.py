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
  print('=' * 32)

  out_bin(n[0], 'null')
  _n = n << 1
  out_bin(_n[0], '<<')
  n ^= _n
  out_bin(n[0], '^')
  print('-' * 32)

  out_bin(n[0], 'null')
  _n = n >> 1
  out_bin(_n[0], '>>')
  n ^= _n
  out_bin(n[0], '^')
  print('-' * 32)

  out_bin(n[0], 'null')
  out_bin(k, 'k')
  #print(f'{n[0]=}')
  #print(f'{k=}')
  
  int_mul = n[0] * k
  form_bin = format(int_mul, 'b')
  print('//')
  print(int_mul)
  print(form_bin)
  print('→')
  ln = len(form_bin)
  print(form_bin[ln - 32:ln])
  print('//')
  
  n *= k
  
  out_bin(n[0], '*')
  print('-' * 32)

  out_bin(n[0], 'null')
  _n = n << 1
  out_bin(_n[0], '<<')
  n ^= _n
  out_bin(n[0], '^')
  print('-' * 32)

  out_bin(n[0], 'null')
  out_bin(k, 'k')
  nk = n * k
  out_bin(nk[0], '^')
  print('-' * 32)
  return nk


def hash11(p: list[float]) -> np.ndarray:
  #f_p = struct.pack('>f', p[0])
  #print(format(p[0], 'f'))
  #print(f_p)
  n = np_floatBitsToUint(p)
  print(f'{n=}')
  return uhash11(n).astype(np.float32) / float(UINT_MAX)


if __name__ == "__main__":
  '''
  size: int = 8
  l_float: list[float] = [float(f) for f in range(size)]
  h11 = hash11(l_float)
  '''
  h11 = hash11([1.0])
  print(f'{h11=}')
  print('')

