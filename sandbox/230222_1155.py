import numpy as np
from PIL import Image as ImageP

UINT_MAX = 0xffff_ffff

sq_size = 8
RGB_SIZE = 256
color_ch = 3

length_size = sq_size * sq_size * color_ch

#xyz = np.arange(0, length_size, dtype=np.uint8).reshape(sq_size, sq_size, color_ch)
#xyz = np.arange(0, 10)
#zoro_uint8 = np.zeros((sq_size, sq_size, 3), dtype=np.uint8)

#xyz = np.arange(0, length_size,RGB_SIZE)  #.reshape(sq_size, sq_size, color_ch)

#imgp = ImageP.fromarray(xyz)

#print(sq_size/RGB_SIZE * length_size)

ll = np.linspace(0, RGB_SIZE, num=length_size, endpoint=False)

ll_size = ll.size

uary =np.array(ll, dtype=np.uint8).reshape(sq_size, sq_size, color_ch)
u_size = uary.size

cr_np = np.full((sq_size, sq_size), 1, dtype=np.uint8)
cg_np = np.full((sq_size, sq_size), 0, dtype=np.uint8)
cb_np = np.full((sq_size, sq_size), 0, dtype=np.uint8)

imgp = ImageP.fromarray(uary)

_ = 1

'''
1111_1111
1111_1111
1111_1111
1111_1111
'''

