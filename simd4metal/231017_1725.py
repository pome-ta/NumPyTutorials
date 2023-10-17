import numpy as np
'''
ext_vector_type = 

Vertex = np.dtype({'names': ['position', 'color'], 'formats':[]})
'''

ext_vector_type = np.dtype((np.float32, 4))
#Vertex = np.dtype({'names': ['position', 'color'], 'formats':[ext_vector_type(4), ext_vector_type(4)]})

dt = np.dtype((np.int32, (np.int8, 4)))

print(np.float32)
print(type(np.float32))
print(ext_vector_type)
print(type(ext_vector_type))

