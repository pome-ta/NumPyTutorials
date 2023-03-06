import numpy as np
from PIL import Image as ImageP

sq_size = 320
RGB_SIZE = 256
color_ch = 3

length_size = sq_size * sq_size * color_ch

canvasnp = np.zeros((sq_size, sq_size, 3), dtype=np.uint8)

xx = np.array(
    [[int(x / sq_size * RGB_SIZE) for x in range(sq_size)]
     for _ in range(sq_size)],
    dtype=np.uint8)
yy = np.array(
    [[int(y / sq_size * RGB_SIZE) for _ in range(sq_size)]
     for y in range(sq_size)],
    dtype=np.uint8)

canvasnp[:, :, 0] = xx
canvasnp[:, :, 1] = xx
canvasnp[:, :, 2] = xx

# zero = np.array(np.np.linspace)

zero = np.array(
    np.linspace(0, 1, num=length_size),
    dtype=np.float32).reshape(sq_size, sq_size, color_ch)

imgp = ImageP.fromarray(canvasnp)
imgp.show()

_ = 1
