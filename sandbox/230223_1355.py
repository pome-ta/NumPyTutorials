import numpy as np
from PIL import Image as ImageP

UINT_MAX = 0xffff_ffff

sq_size = 8
RGB_SIZE = 256
color_ch = 3

length_size = sq_size * sq_size * color_ch

xx = np.array([[int(x / sq_size * RGB_SIZE) for x in range(sq_size)] for _ in range(sq_size)], dtype=np.uint8)
yy = np.array([[y for _ in range(sq_size)] for y in range(sq_size)])
x = np.linspace(0, RGB_SIZE, num=sq_size)




#imgp = ImageP.fromarray(uary)

_ = 1


