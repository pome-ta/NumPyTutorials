import numpy as np
from PIL import Image as ImageP

#UINT_MAX = 0xffff_ffff

sq_size = 320
RGB_SIZE = 256
color_ch = 3

#length_size = sq_size * sq_size * color_ch
'''
canvas_np = np.array(
  np.linspace(0, RGB_SIZE, num=length_size, endpoint=False),
  dtype=np.uint8).reshape(sq_size, sq_size, color_ch)
'''

#zero_uint8 = np.zeros((sq_size, sq_size, 3), dtype=np.uint8)

canvasnp = np.zeros((sq_size, sq_size, 3), dtype=np.uint8)

xx = np.array(
  [[int(x / sq_size * RGB_SIZE) for x in range(sq_size)]
   for _ in range(sq_size)],
  dtype=np.uint8)
yy = np.array(
  [[int(y / sq_size * RGB_SIZE) for _ in range(sq_size)]
   for y in range(sq_size)],
  dtype=np.uint8)

#print(xx[:,:])
#print(canvasnp[:,:,1])
canvasnp[:, :, 0] = xx
canvasnp[:, :, 1] = yy

imgp = ImageP.fromarray(canvasnp)

_ = 1

