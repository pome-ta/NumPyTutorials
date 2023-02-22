import numpy as np
from PIL import Image as ImageP

UINT_MAX = 0xffffffff

u = np.array([UINT_MAX + 1], dtype=np.uint32)

sq_size = 64
np_canvas = np.zeros((sq_size, sq_size, 3), dtype=np.float32)

p_canvas = np.zeros((sq_size, sq_size, 3), dtype=np.uint8)

# init_img = ImageP.new('RGB', (sq_size, sq_size))
# base_array = np.asarray(init_img)
imgp = ImageP.fromarray(p_canvas)

