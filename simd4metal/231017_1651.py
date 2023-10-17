# [NumPy - Structured arrays](https://runebook.dev/ja/docs/numpy/user/basics.rec)

import numpy as np

x = np.array([('Rex', 9, 81.0), ('Fido', 3, 27.0), ('washi', 32, 56.5)],
             dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])

print(f'{x=}')
print(f'{x[1]=}')
print(f'{x["age"]=}')

print(x.itemsize)
