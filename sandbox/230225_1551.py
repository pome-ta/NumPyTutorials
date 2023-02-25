from pathlib import Path

path_nouint = Path('./imgs/noUint.PNG')
path_uint = Path('./imgs/uint.PNG')

nouint_buff = path_nouint.read_bytes()
uint_buff = path_uint.read_bytes()

print(f'no: {len(nouint_buff)}')
print(f'ut: {len(uint_buff)}')

for x, y in zip(nouint_buff, uint_buff):
  if x == y:
    continue
  print(x, y)
