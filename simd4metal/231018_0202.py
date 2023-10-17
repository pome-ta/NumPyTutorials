import numpy as np

v = np.dtype({
  'names': [
    'color',
    'ambientIntensity',
    'diffuseIntensity',
    'direction',
  ],
  'formats': ['i4', 'f4'],
  'offsets': [0, 4],
  'itemsize':
  12
})

