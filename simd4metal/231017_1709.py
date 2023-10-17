import numpy as np

'''
ext_vector_type = 

Vertex = np.dtype({'names': ['position', 'color'], 'formats':[]})
'''

ext_vector_type = np.dtype([('x', np.float32)])

print(np.float32)
print(type(np.float32))
print(ext_vector_type)
print(type(ext_vector_type))
