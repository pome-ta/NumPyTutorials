import numpy as np

vector_float4 = np.dtype(
  {
    'names': [
      'x',
      'y',
      'z',
      'w',
    ],
    'formats': [
      np.float32,
      np.float32,
      np.float32,
      np.float32,
    ],
    #'offsets': [o * 4 for o in range(4)],
    #'itemsize': 16,
  },
  align=False)

#Vertex = np.dtype([('position', vector_float4), ('color', vector_float4)])

Vertex = np.dtype({
  'names': [
    'position',
    'color',
  ],
  'formats': [
    vector_float4,
    vector_float4,
  ],
  'offsets': [0, 16],
})

#vertexData = np.array([[-0.5, -0.5, 0.0, 1.0], [1, 0, 0, 1]], dtype=Vertex)

bf_array = [[
  [-0.5, -0.5, 0.0, 1.0],
  [1.0, 0.0, 0.0, 1.0],
], [
  [0.5, -0.5, 0.0, 1.0],
  [0.0, 1.0, 0.0, 1.0],
], [
  [0.0, 0.5, 0.0, 1.0],
  [0.0, 0.0, 1.0, 1.0],
]]

#vertexData = np.array(bf_array, dtype=Vertex)


position = np.array([-0.5, -0.5, 0.0, 1.0], dtype=vector_float4)



