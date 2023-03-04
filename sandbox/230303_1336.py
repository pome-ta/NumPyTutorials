import numpy as np
from PIL import Image as ImageP

sq_size = 512
RGB_SIZE = 255
COLOR_CH = 3


def create_img(*args):
  print(args)


canvas_px = np.zeros((sq_size, sq_size, COLOR_CH)).astype(np.uint8)

create_img(0)

imgp = ImageP.fromarray(canvas_px)

